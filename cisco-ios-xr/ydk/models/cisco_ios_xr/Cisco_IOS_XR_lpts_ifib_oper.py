""" Cisco_IOS_XR_lpts_ifib_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lpts\-ifib package operational data.

This module contains definitions
for the following management objects\:
  lpts\-ifib\: lpts ifib database

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class LptsIfib(object):
    """
    lpts ifib database
    
    .. attribute:: nodes
    
    	Node ifib database
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_ifib_oper.LptsIfib.Nodes>`
    
    

    """

    _prefix = 'lpts-ifib-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = LptsIfib.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Node ifib database
        
        .. attribute:: node
        
        	Per node slice 
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_ifib_oper.LptsIfib.Nodes.Node>`
        
        

        """

        _prefix = 'lpts-ifib-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Per node slice 
            
            .. attribute:: node_name  <key>
            
            	The node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: slice_ids
            
            	Slice specific
            	**type**\:   :py:class:`SliceIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_ifib_oper.LptsIfib.Nodes.Node.SliceIds>`
            
            

            """

            _prefix = 'lpts-ifib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.slice_ids = LptsIfib.Nodes.Node.SliceIds()
                self.slice_ids.parent = self


            class SliceIds(object):
                """
                Slice specific
                
                .. attribute:: slice_id
                
                	slice types
                	**type**\: list of    :py:class:`SliceId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_ifib_oper.LptsIfib.Nodes.Node.SliceIds.SliceId>`
                
                

                """

                _prefix = 'lpts-ifib-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.slice_id = YList()
                    self.slice_id.parent = self
                    self.slice_id.name = 'slice_id'


                class SliceId(object):
                    """
                    slice types
                    
                    .. attribute:: slice_name  <key>
                    
                    	Type value
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: entry
                    
                    	Data for single pre\-ifib entry
                    	**type**\: list of    :py:class:`Entry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_ifib_oper.LptsIfib.Nodes.Node.SliceIds.SliceId.Entry>`
                    
                    

                    """

                    _prefix = 'lpts-ifib-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.slice_name = None
                        self.entry = YList()
                        self.entry.parent = self
                        self.entry.name = 'entry'


                    class Entry(object):
                        """
                        Data for single pre\-ifib entry
                        
                        .. attribute:: entry  <key>
                        
                        	Single Pre\-ifib entry
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: accepts
                        
                        	Packets matched to accept
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: deliver_list_long
                        
                        	Deliver List Long Format
                        	**type**\:  str
                        
                        .. attribute:: deliver_list_short
                        
                        	Deliver List Short Format
                        	**type**\:  str
                        
                        .. attribute:: destination_addr
                        
                        	Destination IP Address
                        	**type**\:  str
                        
                        .. attribute:: destination_type
                        
                        	Destination Key Type
                        	**type**\:  str
                        
                        .. attribute:: destination_value
                        
                        	Destination Port/ICMP Type/IGMP Type
                        	**type**\:  str
                        
                        .. attribute:: drops
                        
                        	Packets matched to drop
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: flow_type
                        
                        	Flow type
                        	**type**\:  str
                        
                        .. attribute:: ifib_program_time
                        
                        	ifib program time in netio
                        	**type**\:  str
                        
                        .. attribute:: intf_handle
                        
                        	Interface Handle
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: intf_name
                        
                        	Interface Name
                        	**type**\:  str
                        
                        .. attribute:: is_fgid
                        
                        	Is FGID or not
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_syn
                        
                        	Is SYN
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: l3protocol
                        
                        	Layer 3 Protocol
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: l4protocol
                        
                        	Layer 4 Protocol
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: listener_tag
                        
                        	Listener Tag
                        	**type**\:  str
                        
                        .. attribute:: local_flag
                        
                        	Local Flag
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: min_ttl
                        
                        	Minimum TTL
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: opcode
                        
                        	Opcode
                        	**type**\:  str
                        
                        .. attribute:: pending_ifibq_delay
                        
                        	pending ifib queue delay
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sl_ifibq_delay
                        
                        	sl\_ifibq delay
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: source_addr
                        
                        	Source IP Address
                        	**type**\:  str
                        
                        .. attribute:: source_port
                        
                        	Source port
                        	**type**\:  str
                        
                        .. attribute:: vid
                        
                        	VRF ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: vrf_name
                        
                        	VRF Name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'lpts-ifib-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.entry = None
                            self.accepts = None
                            self.deliver_list_long = None
                            self.deliver_list_short = None
                            self.destination_addr = None
                            self.destination_type = None
                            self.destination_value = None
                            self.drops = None
                            self.flow_type = None
                            self.ifib_program_time = None
                            self.intf_handle = None
                            self.intf_name = None
                            self.is_fgid = None
                            self.is_syn = None
                            self.l3protocol = None
                            self.l4protocol = None
                            self.listener_tag = None
                            self.local_flag = None
                            self.min_ttl = None
                            self.opcode = None
                            self.pending_ifibq_delay = None
                            self.sl_ifibq_delay = None
                            self.source_addr = None
                            self.source_port = None
                            self.vid = None
                            self.vrf_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.entry is None:
                                raise YPYModelError('Key property entry is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-lpts-ifib-oper:entry[Cisco-IOS-XR-lpts-ifib-oper:entry = ' + str(self.entry) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.entry is not None:
                                return True

                            if self.accepts is not None:
                                return True

                            if self.deliver_list_long is not None:
                                return True

                            if self.deliver_list_short is not None:
                                return True

                            if self.destination_addr is not None:
                                return True

                            if self.destination_type is not None:
                                return True

                            if self.destination_value is not None:
                                return True

                            if self.drops is not None:
                                return True

                            if self.flow_type is not None:
                                return True

                            if self.ifib_program_time is not None:
                                return True

                            if self.intf_handle is not None:
                                return True

                            if self.intf_name is not None:
                                return True

                            if self.is_fgid is not None:
                                return True

                            if self.is_syn is not None:
                                return True

                            if self.l3protocol is not None:
                                return True

                            if self.l4protocol is not None:
                                return True

                            if self.listener_tag is not None:
                                return True

                            if self.local_flag is not None:
                                return True

                            if self.min_ttl is not None:
                                return True

                            if self.opcode is not None:
                                return True

                            if self.pending_ifibq_delay is not None:
                                return True

                            if self.sl_ifibq_delay is not None:
                                return True

                            if self.source_addr is not None:
                                return True

                            if self.source_port is not None:
                                return True

                            if self.vid is not None:
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_ifib_oper as meta
                            return meta._meta_table['LptsIfib.Nodes.Node.SliceIds.SliceId.Entry']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.slice_name is None:
                            raise YPYModelError('Key property slice_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-lpts-ifib-oper:slice-id[Cisco-IOS-XR-lpts-ifib-oper:slice-name = ' + str(self.slice_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.slice_name is not None:
                            return True

                        if self.entry is not None:
                            for child_ref in self.entry:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_ifib_oper as meta
                        return meta._meta_table['LptsIfib.Nodes.Node.SliceIds.SliceId']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-lpts-ifib-oper:slice-ids'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.slice_id is not None:
                        for child_ref in self.slice_id:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_ifib_oper as meta
                    return meta._meta_table['LptsIfib.Nodes.Node.SliceIds']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-lpts-ifib-oper:lpts-ifib/Cisco-IOS-XR-lpts-ifib-oper:nodes/Cisco-IOS-XR-lpts-ifib-oper:node[Cisco-IOS-XR-lpts-ifib-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.slice_ids is not None and self.slice_ids._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_ifib_oper as meta
                return meta._meta_table['LptsIfib.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-lpts-ifib-oper:lpts-ifib/Cisco-IOS-XR-lpts-ifib-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_ifib_oper as meta
            return meta._meta_table['LptsIfib.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-lpts-ifib-oper:lpts-ifib'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_ifib_oper as meta
        return meta._meta_table['LptsIfib']['meta_info']



""" Cisco_IOS_XR_cmproxy_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR cmproxy package operational data.

This module contains definitions
for the following management objects\:
  sdr\-inventory\-vm\: Platform VM information

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class SdrInventoryVm(object):
    """
    Platform VM information
    
    .. attribute:: nodes
    
    	Node directory
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper.SdrInventoryVm.Nodes>`
    
    

    """

    _prefix = 'cmproxy-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = SdrInventoryVm.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Node directory
        
        .. attribute:: node
        
        	Node name
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper.SdrInventoryVm.Nodes.Node>`
        
        

        """

        _prefix = 'cmproxy-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Node name
            
            .. attribute:: name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: node_entries
            
            	VM Information
            	**type**\:   :py:class:`NodeEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper.SdrInventoryVm.Nodes.Node.NodeEntries>`
            
            

            """

            _prefix = 'cmproxy-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.name = None
                self.node_entries = SdrInventoryVm.Nodes.Node.NodeEntries()
                self.node_entries.parent = self


            class NodeEntries(object):
                """
                VM Information
                
                .. attribute:: node_entry
                
                	VM information for a node
                	**type**\: list of    :py:class:`NodeEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper.SdrInventoryVm.Nodes.Node.NodeEntries.NodeEntry>`
                
                

                """

                _prefix = 'cmproxy-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.node_entry = YList()
                    self.node_entry.parent = self
                    self.node_entry.name = 'node_entry'


                class NodeEntry(object):
                    """
                    VM information for a node
                    
                    .. attribute:: name  <key>
                    
                    	Node name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: card_type
                    
                    	card type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: card_type_string
                    
                    	card type string
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: node_ip
                    
                    	node IP address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: node_ipv4_string
                    
                    	node IPv4 address string
                    	**type**\:  str
                    
                    	**length:** 0..16
                    
                    .. attribute:: node_name
                    
                    	node name string
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: node_sw_state
                    
                    	current software state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: node_sw_state_string
                    
                    	current software state string
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: nodeid
                    
                    	node ID
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: partner_id
                    
                    	partner node id
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: partner_name
                    
                    	partner name string
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: prev_sw_state
                    
                    	previous software state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prev_sw_state_string
                    
                    	previous software state string
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: red_state
                    
                    	redundancy state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: red_state_string
                    
                    	redundancy state string
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: valid
                    
                    	valid flag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'cmproxy-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.name = None
                        self.card_type = None
                        self.card_type_string = None
                        self.node_ip = None
                        self.node_ipv4_string = None
                        self.node_name = None
                        self.node_sw_state = None
                        self.node_sw_state_string = None
                        self.nodeid = None
                        self.partner_id = None
                        self.partner_name = None
                        self.prev_sw_state = None
                        self.prev_sw_state_string = None
                        self.red_state = None
                        self.red_state_string = None
                        self.valid = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.name is None:
                            raise YPYModelError('Key property name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-cmproxy-oper:node-entry[Cisco-IOS-XR-cmproxy-oper:name = ' + str(self.name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.name is not None:
                            return True

                        if self.card_type is not None:
                            return True

                        if self.card_type_string is not None:
                            return True

                        if self.node_ip is not None:
                            return True

                        if self.node_ipv4_string is not None:
                            return True

                        if self.node_name is not None:
                            return True

                        if self.node_sw_state is not None:
                            return True

                        if self.node_sw_state_string is not None:
                            return True

                        if self.nodeid is not None:
                            return True

                        if self.partner_id is not None:
                            return True

                        if self.partner_name is not None:
                            return True

                        if self.prev_sw_state is not None:
                            return True

                        if self.prev_sw_state_string is not None:
                            return True

                        if self.red_state is not None:
                            return True

                        if self.red_state_string is not None:
                            return True

                        if self.valid is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cmproxy_oper as meta
                        return meta._meta_table['SdrInventoryVm.Nodes.Node.NodeEntries.NodeEntry']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-cmproxy-oper:node-entries'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.node_entry is not None:
                        for child_ref in self.node_entry:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cmproxy_oper as meta
                    return meta._meta_table['SdrInventoryVm.Nodes.Node.NodeEntries']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-cmproxy-oper:sdr-inventory-vm/Cisco-IOS-XR-cmproxy-oper:nodes/Cisco-IOS-XR-cmproxy-oper:node[Cisco-IOS-XR-cmproxy-oper:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.node_entries is not None and self.node_entries._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cmproxy_oper as meta
                return meta._meta_table['SdrInventoryVm.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-cmproxy-oper:sdr-inventory-vm/Cisco-IOS-XR-cmproxy-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cmproxy_oper as meta
            return meta._meta_table['SdrInventoryVm.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-cmproxy-oper:sdr-inventory-vm'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cmproxy_oper as meta
        return meta._meta_table['SdrInventoryVm']['meta_info']



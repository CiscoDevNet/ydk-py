""" Cisco_IOS_XR_pppoe_ea_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR pppoe\-ea package operational data.

This module contains definitions
for the following management objects\:
  pppoe\-ea\: PPPoE Ea data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class PppoeEa(object):
    """
    PPPoE Ea data
    
    .. attribute:: nodes
    
    	PPPOE\_EA list of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes>`
    
    

    """

    _prefix = 'pppoe-ea-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = PppoeEa.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        PPPOE\_EA list of nodes
        
        .. attribute:: node
        
        	PPPOE\-EA operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node>`
        
        

        """

        _prefix = 'pppoe-ea-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            PPPOE\-EA operational data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: interface_ids
            
            	PPPoE interface info
            	**type**\:   :py:class:`InterfaceIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.InterfaceIds>`
            
            .. attribute:: parent_interface_ids
            
            	PPPoE parent interface info
            	**type**\:   :py:class:`ParentInterfaceIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.ParentInterfaceIds>`
            
            

            """

            _prefix = 'pppoe-ea-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.interface_ids = PppoeEa.Nodes.Node.InterfaceIds()
                self.interface_ids.parent = self
                self.parent_interface_ids = PppoeEa.Nodes.Node.ParentInterfaceIds()
                self.parent_interface_ids.parent = self


            class ParentInterfaceIds(object):
                """
                PPPoE parent interface info
                
                .. attribute:: parent_interface_id
                
                	PPPoE parent interface info
                	**type**\: list of    :py:class:`ParentInterfaceId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId>`
                
                

                """

                _prefix = 'pppoe-ea-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.parent_interface_id = YList()
                    self.parent_interface_id.parent = self
                    self.parent_interface_id.name = 'parent_interface_id'


                class ParentInterfaceId(object):
                    """
                    PPPoE parent interface info
                    
                    .. attribute:: parent_interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: is_in_sync
                    
                    	Is in sync
                    	**type**\:  bool
                    
                    .. attribute:: srgv_mac
                    
                    	SRG VMac\-address
                    	**type**\:   :py:class:`SrgvMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac>`
                    
                    

                    """

                    _prefix = 'pppoe-ea-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.parent_interface_name = None
                        self.interface = None
                        self.is_in_sync = None
                        self.srgv_mac = PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac()
                        self.srgv_mac.parent = self


                    class SrgvMac(object):
                        """
                        SRG VMac\-address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'pppoe-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.macaddr = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-pppoe-ea-oper:srgv-mac'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.macaddr is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pppoe_ea_oper as meta
                            return meta._meta_table['PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.parent_interface_name is None:
                            raise YPYModelError('Key property parent_interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-pppoe-ea-oper:parent-interface-id[Cisco-IOS-XR-pppoe-ea-oper:parent-interface-name = ' + str(self.parent_interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.parent_interface_name is not None:
                            return True

                        if self.interface is not None:
                            return True

                        if self.is_in_sync is not None:
                            return True

                        if self.srgv_mac is not None and self.srgv_mac._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pppoe_ea_oper as meta
                        return meta._meta_table['PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pppoe-ea-oper:parent-interface-ids'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.parent_interface_id is not None:
                        for child_ref in self.parent_interface_id:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pppoe_ea_oper as meta
                    return meta._meta_table['PppoeEa.Nodes.Node.ParentInterfaceIds']['meta_info']


            class InterfaceIds(object):
                """
                PPPoE interface info
                
                .. attribute:: interface_id
                
                	PPPoE interface info
                	**type**\: list of    :py:class:`InterfaceId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.InterfaceIds.InterfaceId>`
                
                

                """

                _prefix = 'pppoe-ea-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_id = YList()
                    self.interface_id.parent = self
                    self.interface_id.name = 'interface_id'


                class InterfaceId(object):
                    """
                    PPPoE interface info
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: is_in_sync
                    
                    	Is in sync
                    	**type**\:  bool
                    
                    .. attribute:: is_platform_created
                    
                    	Is Platform created
                    	**type**\:  bool
                    
                    .. attribute:: is_priority_set
                    
                    	Is Priority Set
                    	**type**\:  bool
                    
                    .. attribute:: local_mac
                    
                    	Local Mac\-address
                    	**type**\:   :py:class:`LocalMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac>`
                    
                    .. attribute:: parent_interface
                    
                    	Parent Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: peer_mac
                    
                    	Peer Mac\-address
                    	**type**\:   :py:class:`PeerMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac>`
                    
                    .. attribute:: priority
                    
                    	Priority
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: srgv_mac
                    
                    	SRG VMac\-address
                    	**type**\:   :py:class:`SrgvMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac>`
                    
                    .. attribute:: vlanid
                    
                    	VLAN Ids
                    	**type**\:  list of int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'pppoe-ea-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.interface = None
                        self.is_in_sync = None
                        self.is_platform_created = None
                        self.is_priority_set = None
                        self.local_mac = PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac()
                        self.local_mac.parent = self
                        self.parent_interface = None
                        self.peer_mac = PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac()
                        self.peer_mac.parent = self
                        self.priority = None
                        self.session_id = None
                        self.srgv_mac = PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac()
                        self.srgv_mac.parent = self
                        self.vlanid = YLeafList()
                        self.vlanid.parent = self
                        self.vlanid.name = 'vlanid'


                    class PeerMac(object):
                        """
                        Peer Mac\-address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'pppoe-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.macaddr = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-pppoe-ea-oper:peer-mac'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.macaddr is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pppoe_ea_oper as meta
                            return meta._meta_table['PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac']['meta_info']


                    class LocalMac(object):
                        """
                        Local Mac\-address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'pppoe-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.macaddr = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-pppoe-ea-oper:local-mac'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.macaddr is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pppoe_ea_oper as meta
                            return meta._meta_table['PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac']['meta_info']


                    class SrgvMac(object):
                        """
                        SRG VMac\-address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'pppoe-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.macaddr = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-pppoe-ea-oper:srgv-mac'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.macaddr is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pppoe_ea_oper as meta
                            return meta._meta_table['PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-pppoe-ea-oper:interface-id[Cisco-IOS-XR-pppoe-ea-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.interface is not None:
                            return True

                        if self.is_in_sync is not None:
                            return True

                        if self.is_platform_created is not None:
                            return True

                        if self.is_priority_set is not None:
                            return True

                        if self.local_mac is not None and self.local_mac._has_data():
                            return True

                        if self.parent_interface is not None:
                            return True

                        if self.peer_mac is not None and self.peer_mac._has_data():
                            return True

                        if self.priority is not None:
                            return True

                        if self.session_id is not None:
                            return True

                        if self.srgv_mac is not None and self.srgv_mac._has_data():
                            return True

                        if self.vlanid is not None:
                            for child in self.vlanid:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pppoe_ea_oper as meta
                        return meta._meta_table['PppoeEa.Nodes.Node.InterfaceIds.InterfaceId']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pppoe-ea-oper:interface-ids'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_id is not None:
                        for child_ref in self.interface_id:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pppoe_ea_oper as meta
                    return meta._meta_table['PppoeEa.Nodes.Node.InterfaceIds']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-pppoe-ea-oper:pppoe-ea/Cisco-IOS-XR-pppoe-ea-oper:nodes/Cisco-IOS-XR-pppoe-ea-oper:node[Cisco-IOS-XR-pppoe-ea-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.interface_ids is not None and self.interface_ids._has_data():
                    return True

                if self.parent_interface_ids is not None and self.parent_interface_ids._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pppoe_ea_oper as meta
                return meta._meta_table['PppoeEa.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-pppoe-ea-oper:pppoe-ea/Cisco-IOS-XR-pppoe-ea-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pppoe_ea_oper as meta
            return meta._meta_table['PppoeEa.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-pppoe-ea-oper:pppoe-ea'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pppoe_ea_oper as meta
        return meta._meta_table['PppoeEa']['meta_info']



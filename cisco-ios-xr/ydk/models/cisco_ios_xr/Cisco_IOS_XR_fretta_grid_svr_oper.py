""" Cisco_IOS_XR_fretta_grid_svr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fretta\-grid\-svr package operational data.

This module contains definitions
for the following management objects\:
  grid\: GRID operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Grid(object):
    """
    GRID operational data
    
    .. attribute:: nodes
    
    	Table of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper.Grid.Nodes>`
    
    

    """

    _prefix = 'fretta-grid-svr-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = Grid.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Table of nodes
        
        .. attribute:: node
        
        	Operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper.Grid.Nodes.Node>`
        
        

        """

        _prefix = 'fretta-grid-svr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Operational data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node ID
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: client_xr
            
            	GRID Client Table
            	**type**\:   :py:class:`ClientXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper.Grid.Nodes.Node.ClientXr>`
            
            .. attribute:: clients
            
            	GRID Client Consistency Check
            	**type**\:   :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper.Grid.Nodes.Node.Clients>`
            
            

            """

            _prefix = 'fretta-grid-svr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.client_xr = Grid.Nodes.Node.ClientXr()
                self.client_xr.parent = self
                self.clients = Grid.Nodes.Node.Clients()
                self.clients.parent = self


            class ClientXr(object):
                """
                GRID Client Table
                
                .. attribute:: client
                
                	GRID Client Database
                	**type**\: list of    :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper.Grid.Nodes.Node.ClientXr.Client>`
                
                

                """

                _prefix = 'fretta-grid-svr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.client = YList()
                    self.client.parent = self
                    self.client.name = 'client'


                class Client(object):
                    """
                    GRID Client Database
                    
                    .. attribute:: client_name  <key>
                    
                    	Client name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: client_data
                    
                    	Client information
                    	**type**\: list of    :py:class:`ClientData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper.Grid.Nodes.Node.ClientXr.Client.ClientData>`
                    
                    

                    """

                    _prefix = 'fretta-grid-svr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.client_name = None
                        self.client_data = YList()
                        self.client_data.parent = self
                        self.client_data.name = 'client_data'


                    class ClientData(object):
                        """
                        Client information
                        
                        .. attribute:: res_id
                        
                        	Resource ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'fretta-grid-svr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.res_id = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-fretta-grid-svr-oper:client-data'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.res_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_grid_svr_oper as meta
                            return meta._meta_table['Grid.Nodes.Node.ClientXr.Client.ClientData']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.client_name is None:
                            raise YPYModelError('Key property client_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-fretta-grid-svr-oper:client[Cisco-IOS-XR-fretta-grid-svr-oper:client-name = ' + str(self.client_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.client_name is not None:
                            return True

                        if self.client_data is not None:
                            for child_ref in self.client_data:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_grid_svr_oper as meta
                        return meta._meta_table['Grid.Nodes.Node.ClientXr.Client']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-fretta-grid-svr-oper:client-xr'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.client is not None:
                        for child_ref in self.client:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_grid_svr_oper as meta
                    return meta._meta_table['Grid.Nodes.Node.ClientXr']['meta_info']


            class Clients(object):
                """
                GRID Client Consistency Check
                
                .. attribute:: client
                
                	GRID Client Consistency Check
                	**type**\: list of    :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper.Grid.Nodes.Node.Clients.Client>`
                
                

                """

                _prefix = 'fretta-grid-svr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.client = YList()
                    self.client.parent = self
                    self.client.name = 'client'


                class Client(object):
                    """
                    GRID Client Consistency Check
                    
                    .. attribute:: client_name  <key>
                    
                    	Client name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: client_data
                    
                    	Client information
                    	**type**\: list of    :py:class:`ClientData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper.Grid.Nodes.Node.Clients.Client.ClientData>`
                    
                    

                    """

                    _prefix = 'fretta-grid-svr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.client_name = None
                        self.client_data = YList()
                        self.client_data.parent = self
                        self.client_data.name = 'client_data'


                    class ClientData(object):
                        """
                        Client information
                        
                        .. attribute:: res_id
                        
                        	Resource ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'fretta-grid-svr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.res_id = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-fretta-grid-svr-oper:client-data'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.res_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_grid_svr_oper as meta
                            return meta._meta_table['Grid.Nodes.Node.Clients.Client.ClientData']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.client_name is None:
                            raise YPYModelError('Key property client_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-fretta-grid-svr-oper:client[Cisco-IOS-XR-fretta-grid-svr-oper:client-name = ' + str(self.client_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.client_name is not None:
                            return True

                        if self.client_data is not None:
                            for child_ref in self.client_data:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_grid_svr_oper as meta
                        return meta._meta_table['Grid.Nodes.Node.Clients.Client']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-fretta-grid-svr-oper:clients'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.client is not None:
                        for child_ref in self.client:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_grid_svr_oper as meta
                    return meta._meta_table['Grid.Nodes.Node.Clients']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-fretta-grid-svr-oper:grid/Cisco-IOS-XR-fretta-grid-svr-oper:nodes/Cisco-IOS-XR-fretta-grid-svr-oper:node[Cisco-IOS-XR-fretta-grid-svr-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.client_xr is not None and self.client_xr._has_data():
                    return True

                if self.clients is not None and self.clients._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_grid_svr_oper as meta
                return meta._meta_table['Grid.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-fretta-grid-svr-oper:grid/Cisco-IOS-XR-fretta-grid-svr-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_grid_svr_oper as meta
            return meta._meta_table['Grid.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-fretta-grid-svr-oper:grid'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_fretta_grid_svr_oper as meta
        return meta._meta_table['Grid']['meta_info']



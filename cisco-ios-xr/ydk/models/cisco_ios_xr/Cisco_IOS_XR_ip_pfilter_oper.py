""" Cisco_IOS_XR_ip_pfilter_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-pfilter package operational data.

This module contains definitions
for the following management objects\:
  pfilter\-ma\: Root class of PfilterMa Oper schema

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class PfilterMa(object):
    """
    Root class of PfilterMa Oper schema
    
    .. attribute:: nodes
    
    	Node\-specific operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes>`
    
    

    """

    _prefix = 'ip-pfilter-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = PfilterMa.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Node\-specific operational data
        
        .. attribute:: node
        
        	PfilterMa operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node>`
        
        

        """

        _prefix = 'ip-pfilter-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            PfilterMa operational data for a particular
            node
            
            .. attribute:: node_name  <key>
            
            	The node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: process
            
            	Operational data for pfilter
            	**type**\:   :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process>`
            
            

            """

            _prefix = 'ip-pfilter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.process = PfilterMa.Nodes.Node.Process()
                self.process.parent = self


            class Process(object):
                """
                Operational data for pfilter
                
                .. attribute:: ipv4
                
                	Operational data for pfilter
                	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv4>`
                
                .. attribute:: ipv6
                
                	Operational data for pfilter
                	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv6>`
                
                

                """

                _prefix = 'ip-pfilter-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ipv4 = PfilterMa.Nodes.Node.Process.Ipv4()
                    self.ipv4.parent = self
                    self.ipv6 = PfilterMa.Nodes.Node.Process.Ipv6()
                    self.ipv6.parent = self


                class Ipv6(object):
                    """
                    Operational data for pfilter
                    
                    .. attribute:: acl_info_table
                    
                    	Operational data for pfilter
                    	**type**\:   :py:class:`AclInfoTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable>`
                    
                    

                    """

                    _prefix = 'ip-pfilter-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.acl_info_table = PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable()
                        self.acl_info_table.parent = self


                    class AclInfoTable(object):
                        """
                        Operational data for pfilter
                        
                        .. attribute:: interface_infos
                        
                        	Operational data for pfilter
                        	**type**\:   :py:class:`InterfaceInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos>`
                        
                        

                        """

                        _prefix = 'ip-pfilter-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface_infos = PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos()
                            self.interface_infos.parent = self


                        class InterfaceInfos(object):
                            """
                            Operational data for pfilter
                            
                            .. attribute:: interface_info
                            
                            	Operational data for pfilter in bag
                            	**type**\: list of    :py:class:`InterfaceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos.InterfaceInfo>`
                            
                            

                            """

                            _prefix = 'ip-pfilter-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.interface_info = YList()
                                self.interface_info.parent = self
                                self.interface_info.name = 'interface_info'


                            class InterfaceInfo(object):
                                """
                                Operational data for pfilter in bag
                                
                                .. attribute:: interface_name  <key>
                                
                                	Name of the interface
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                .. attribute:: acl_info
                                
                                	acl information
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ip-pfilter-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.interface_name = None
                                    self.acl_info = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.interface_name is None:
                                        raise YPYModelError('Key property interface_name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-oper:interface-info[Cisco-IOS-XR-ip-pfilter-oper:interface-name = ' + str(self.interface_name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.interface_name is not None:
                                        return True

                                    if self.acl_info is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_pfilter_oper as meta
                                    return meta._meta_table['PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos.InterfaceInfo']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-oper:interface-infos'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.interface_info is not None:
                                    for child_ref in self.interface_info:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_pfilter_oper as meta
                                return meta._meta_table['PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-oper:acl-info-table'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.interface_infos is not None and self.interface_infos._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_pfilter_oper as meta
                            return meta._meta_table['PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-oper:ipv6'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.acl_info_table is not None and self.acl_info_table._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_pfilter_oper as meta
                        return meta._meta_table['PfilterMa.Nodes.Node.Process.Ipv6']['meta_info']


                class Ipv4(object):
                    """
                    Operational data for pfilter
                    
                    .. attribute:: acl_info_table
                    
                    	Operational data for pfilter
                    	**type**\:   :py:class:`AclInfoTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable>`
                    
                    

                    """

                    _prefix = 'ip-pfilter-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.acl_info_table = PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable()
                        self.acl_info_table.parent = self


                    class AclInfoTable(object):
                        """
                        Operational data for pfilter
                        
                        .. attribute:: interface_infos
                        
                        	Operational data for pfilter
                        	**type**\:   :py:class:`InterfaceInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos>`
                        
                        

                        """

                        _prefix = 'ip-pfilter-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface_infos = PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos()
                            self.interface_infos.parent = self


                        class InterfaceInfos(object):
                            """
                            Operational data for pfilter
                            
                            .. attribute:: interface_info
                            
                            	Operational data for pfilter in bag
                            	**type**\: list of    :py:class:`InterfaceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos.InterfaceInfo>`
                            
                            

                            """

                            _prefix = 'ip-pfilter-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.interface_info = YList()
                                self.interface_info.parent = self
                                self.interface_info.name = 'interface_info'


                            class InterfaceInfo(object):
                                """
                                Operational data for pfilter in bag
                                
                                .. attribute:: interface_name  <key>
                                
                                	Name of the interface
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                .. attribute:: acl_info
                                
                                	acl information
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ip-pfilter-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.interface_name = None
                                    self.acl_info = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.interface_name is None:
                                        raise YPYModelError('Key property interface_name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-oper:interface-info[Cisco-IOS-XR-ip-pfilter-oper:interface-name = ' + str(self.interface_name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.interface_name is not None:
                                        return True

                                    if self.acl_info is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_pfilter_oper as meta
                                    return meta._meta_table['PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos.InterfaceInfo']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-oper:interface-infos'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.interface_info is not None:
                                    for child_ref in self.interface_info:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_pfilter_oper as meta
                                return meta._meta_table['PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-oper:acl-info-table'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.interface_infos is not None and self.interface_infos._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_pfilter_oper as meta
                            return meta._meta_table['PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-oper:ipv4'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.acl_info_table is not None and self.acl_info_table._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_pfilter_oper as meta
                        return meta._meta_table['PfilterMa.Nodes.Node.Process.Ipv4']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-oper:process'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ipv4 is not None and self.ipv4._has_data():
                        return True

                    if self.ipv6 is not None and self.ipv6._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_pfilter_oper as meta
                    return meta._meta_table['PfilterMa.Nodes.Node.Process']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-ip-pfilter-oper:pfilter-ma/Cisco-IOS-XR-ip-pfilter-oper:nodes/Cisco-IOS-XR-ip-pfilter-oper:node[Cisco-IOS-XR-ip-pfilter-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.process is not None and self.process._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_pfilter_oper as meta
                return meta._meta_table['PfilterMa.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-pfilter-oper:pfilter-ma/Cisco-IOS-XR-ip-pfilter-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_pfilter_oper as meta
            return meta._meta_table['PfilterMa.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-pfilter-oper:pfilter-ma'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_pfilter_oper as meta
        return meta._meta_table['PfilterMa']['meta_info']



""" Cisco_IOS_XR_ip_pfilter_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-pfilter package operational data.

This module contains definitions
for the following management objects\:
  pfilter\-ma\: Root class of PfilterMa Oper schema

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class PfilterMa(object):
    """
    Root class of PfilterMa Oper schema
    
    .. attribute:: nodes
    
    	Node\-specific operational data
    	**type**\: :py:class:`Nodes <ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes>`
    
    

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
        	**type**\: list of :py:class:`Node <ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node>`
        
        

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
            
            .. attribute:: node_name
            
            	The node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: process
            
            	Operational data for pfilter
            	**type**\: :py:class:`Process <ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process>`
            
            

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
                	**type**\: :py:class:`Ipv4 <ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv4>`
                
                .. attribute:: ipv6
                
                	Operational data for pfilter
                	**type**\: :py:class:`Ipv6 <ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv6>`
                
                

                """

                _prefix = 'ip-pfilter-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ipv4 = PfilterMa.Nodes.Node.Process.Ipv4()
                    self.ipv4.parent = self
                    self.ipv6 = PfilterMa.Nodes.Node.Process.Ipv6()
                    self.ipv6.parent = self


                class Ipv4(object):
                    """
                    Operational data for pfilter
                    
                    .. attribute:: interfaces
                    
                    	Operational data for pfilter
                    	**type**\: :py:class:`Interfaces <ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv4.Interfaces>`
                    
                    

                    """

                    _prefix = 'ip-pfilter-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interfaces = PfilterMa.Nodes.Node.Process.Ipv4.Interfaces()
                        self.interfaces.parent = self


                    class Interfaces(object):
                        """
                        Operational data for pfilter
                        
                        .. attribute:: interface
                        
                        	Operational data for pfilter
                        	**type**\: list of :py:class:`Interface <ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv4.Interfaces.Interface>`
                        
                        

                        """

                        _prefix = 'ip-pfilter-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface = YList()
                            self.interface.parent = self
                            self.interface.name = 'interface'


                        class Interface(object):
                            """
                            Operational data for pfilter
                            
                            .. attribute:: interface_name
                            
                            	Name of the interface
                            	**type**\: str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: acl_information
                            
                            	Interface ACL Details
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ip-pfilter-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.interface_name = None
                                self.acl_information = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.interface_name is None:
                                    raise YPYDataValidationError('Key property interface_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-oper:interface[Cisco-IOS-XR-ip-pfilter-oper:interface-name = ' + str(self.interface_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.interface_name is not None:
                                    return True

                                if self.acl_information is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_pfilter_oper as meta
                                return meta._meta_table['PfilterMa.Nodes.Node.Process.Ipv4.Interfaces.Interface']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-oper:interfaces'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.interface is not None:
                                for child_ref in self.interface:
                                    if child_ref._has_data():
                                        return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_pfilter_oper as meta
                            return meta._meta_table['PfilterMa.Nodes.Node.Process.Ipv4.Interfaces']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-oper:ipv4'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.interfaces is not None and self.interfaces._has_data():
                            return True

                        if self.interfaces is not None and self.interfaces.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_pfilter_oper as meta
                        return meta._meta_table['PfilterMa.Nodes.Node.Process.Ipv4']['meta_info']


                class Ipv6(object):
                    """
                    Operational data for pfilter
                    
                    .. attribute:: interfaces
                    
                    	Operational data for pfilter
                    	**type**\: :py:class:`Interfaces <ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv6.Interfaces>`
                    
                    

                    """

                    _prefix = 'ip-pfilter-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interfaces = PfilterMa.Nodes.Node.Process.Ipv6.Interfaces()
                        self.interfaces.parent = self


                    class Interfaces(object):
                        """
                        Operational data for pfilter
                        
                        .. attribute:: interface
                        
                        	Operational data for pfilter
                        	**type**\: list of :py:class:`Interface <ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv6.Interfaces.Interface>`
                        
                        

                        """

                        _prefix = 'ip-pfilter-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface = YList()
                            self.interface.parent = self
                            self.interface.name = 'interface'


                        class Interface(object):
                            """
                            Operational data for pfilter
                            
                            .. attribute:: interface_name
                            
                            	Name of the interface
                            	**type**\: str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: acl_information
                            
                            	Interface ACL Details
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ip-pfilter-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.interface_name = None
                                self.acl_information = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.interface_name is None:
                                    raise YPYDataValidationError('Key property interface_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-oper:interface[Cisco-IOS-XR-ip-pfilter-oper:interface-name = ' + str(self.interface_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.interface_name is not None:
                                    return True

                                if self.acl_information is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_pfilter_oper as meta
                                return meta._meta_table['PfilterMa.Nodes.Node.Process.Ipv6.Interfaces.Interface']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-oper:interfaces'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.interface is not None:
                                for child_ref in self.interface:
                                    if child_ref._has_data():
                                        return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_pfilter_oper as meta
                            return meta._meta_table['PfilterMa.Nodes.Node.Process.Ipv6.Interfaces']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-oper:ipv6'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.interfaces is not None and self.interfaces._has_data():
                            return True

                        if self.interfaces is not None and self.interfaces.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_pfilter_oper as meta
                        return meta._meta_table['PfilterMa.Nodes.Node.Process.Ipv6']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-pfilter-oper:process'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.ipv4 is not None and self.ipv4._has_data():
                        return True

                    if self.ipv4 is not None and self.ipv4.is_presence():
                        return True

                    if self.ipv6 is not None and self.ipv6._has_data():
                        return True

                    if self.ipv6 is not None and self.ipv6.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_pfilter_oper as meta
                    return meta._meta_table['PfilterMa.Nodes.Node.Process']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYDataValidationError('Key property node_name is None')

                return '/Cisco-IOS-XR-ip-pfilter-oper:pfilter-ma/Cisco-IOS-XR-ip-pfilter-oper:nodes/Cisco-IOS-XR-ip-pfilter-oper:node[Cisco-IOS-XR-ip-pfilter-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.node_name is not None:
                    return True

                if self.process is not None and self.process._has_data():
                    return True

                if self.process is not None and self.process.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_pfilter_oper as meta
                return meta._meta_table['PfilterMa.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-pfilter-oper:pfilter-ma/Cisco-IOS-XR-ip-pfilter-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_pfilter_oper as meta
            return meta._meta_table['PfilterMa.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-pfilter-oper:pfilter-ma'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.nodes is not None and self.nodes._has_data():
            return True

        if self.nodes is not None and self.nodes.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_pfilter_oper as meta
        return meta._meta_table['PfilterMa']['meta_info']



""" Cisco_IOS_XR_lpts_lib_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lpts\-lib package configuration.

This module contains definitions
for the following management objects\:
  lpts\: lpts configuration commands

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.lpts.Cisco_IOS_XR_lpts_pre_ifib_cfg import LptsFlowEnum


class Lpts(object):
    """
    lpts configuration commands
    
    .. attribute:: ipolicer
    
    	Pre IFiB Configuration 
    	**type**\: :py:class:`Ipolicer <ydk.models.lpts.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer>`
    
    

    """

    _prefix = 'lpts-lib-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.ipolicer = None


    class Ipolicer(object):
        """
        Pre IFiB Configuration 
        
        .. attribute:: ipv4acls
        
        	Table for ACLs
        	**type**\: :py:class:`Ipv4Acls <ydk.models.lpts.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Ipv4Acls>`
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        .. attribute:: enable
        
        	Enabled
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        .. attribute:: flows
        
        	Table for Flows
        	**type**\: :py:class:`Flows <ydk.models.lpts.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Flows>`
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'lpts-pre-ifib-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.ipv4acls = Lpts.Ipolicer.Ipv4Acls()
            self.ipv4acls.parent = self
            self.enable = None
            self.flows = Lpts.Ipolicer.Flows()
            self.flows.parent = self


        class Ipv4Acls(object):
            """
            Table for ACLs
            
            .. attribute:: ipv4acl
            
            	ACL name
            	**type**\: list of :py:class:`Ipv4Acl <ydk.models.lpts.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Ipv4Acls.Ipv4Acl>`
            
            

            """

            _prefix = 'lpts-pre-ifib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.ipv4acl = YList()
                self.ipv4acl.parent = self
                self.ipv4acl.name = 'ipv4acl'


            class Ipv4Acl(object):
                """
                ACL name
                
                .. attribute:: acl_name  <key>
                
                	ACL name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: acl_rate
                
                	pre\-ifib policer rate config commands
                	**type**\: int
                
                	**range:** 0..100000
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.acl_name = None
                    self.acl_rate = None

                @property
                def _common_path(self):
                    if self.acl_name is None:
                        raise YPYDataValidationError('Key property acl_name is None')

                    return '/Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipv4acls/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipv4acl[Cisco-IOS-XR-lpts-pre-ifib-cfg:acl-name = ' + str(self.acl_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.acl_name is not None:
                        return True

                    if self.acl_rate is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.lpts._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                    return meta._meta_table['Lpts.Ipolicer.Ipv4Acls.Ipv4Acl']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipv4acls'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.ipv4acl is not None:
                    for child_ref in self.ipv4acl:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.lpts._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                return meta._meta_table['Lpts.Ipolicer.Ipv4Acls']['meta_info']


        class Flows(object):
            """
            Table for Flows
            
            .. attribute:: flow
            
            	selected flow type
            	**type**\: list of :py:class:`Flow <ydk.models.lpts.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Flows.Flow>`
            
            

            """

            _prefix = 'lpts-pre-ifib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.flow = YList()
                self.flow.parent = self
                self.flow.name = 'flow'


            class Flow(object):
                """
                selected flow type
                
                .. attribute:: flow_type  <key>
                
                	LPTS Flow Type
                	**type**\: :py:class:`LptsFlowEnum <ydk.models.lpts.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlowEnum>`
                
                .. attribute:: precedences
                
                	TOS Precedence value(s)
                	**type**\: :py:class:`Precedences <ydk.models.lpts.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Flows.Flow.Precedences>`
                
                .. attribute:: rate
                
                	Configured rate value
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.flow_type = None
                    self.precedences = Lpts.Ipolicer.Flows.Flow.Precedences()
                    self.precedences.parent = self
                    self.rate = None


                class Precedences(object):
                    """
                    TOS Precedence value(s)
                    
                    .. attribute:: precedence
                    
                    	Precedence values
                    	**type**\: one of the below types:
                    
                    	**type**\: list of :py:class:`LptsPreIFibPrecedenceNumberEnum <ydk.models.lpts.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPreIFibPrecedenceNumberEnum>`
                    
                    
                    ----
                    	**type**\: list of int
                    
                    	**range:** 0..7
                    
                    
                    ----
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.precedence = YLeafList()
                        self.precedence.parent = self
                        self.precedence.name = 'precedence'

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:precedences'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.precedence is not None:
                            for child in self.precedence:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.lpts._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                        return meta._meta_table['Lpts.Ipolicer.Flows.Flow.Precedences']['meta_info']

                @property
                def _common_path(self):
                    if self.flow_type is None:
                        raise YPYDataValidationError('Key property flow_type is None')

                    return '/Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer/Cisco-IOS-XR-lpts-pre-ifib-cfg:flows/Cisco-IOS-XR-lpts-pre-ifib-cfg:flow[Cisco-IOS-XR-lpts-pre-ifib-cfg:flow-type = ' + str(self.flow_type) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.flow_type is not None:
                        return True

                    if self.precedences is not None and self.precedences._has_data():
                        return True

                    if self.rate is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.lpts._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                    return meta._meta_table['Lpts.Ipolicer.Flows.Flow']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer/Cisco-IOS-XR-lpts-pre-ifib-cfg:flows'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.flow is not None:
                    for child_ref in self.flow:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.lpts._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                return meta._meta_table['Lpts.Ipolicer.Flows']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.ipv4acls is not None and self.ipv4acls._has_data():
                return True

            if self.enable is not None:
                return True

            if self.flows is not None and self.flows._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.lpts._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
            return meta._meta_table['Lpts.Ipolicer']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-lpts-lib-cfg:lpts'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.ipolicer is not None and self.ipolicer._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.lpts._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
        return meta._meta_table['Lpts']['meta_info']



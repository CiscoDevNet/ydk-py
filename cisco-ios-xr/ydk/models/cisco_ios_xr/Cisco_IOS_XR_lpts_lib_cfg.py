""" Cisco_IOS_XR_lpts_lib_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lpts\-lib package configuration.

This module contains definitions
for the following management objects\:
  lpts\: lpts configuration commands

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Lpts(object):
    """
    lpts configuration commands
    
    .. attribute:: ipolicer
    
    	Pre IFiB Configuration 
    	**type**\:   :py:class:`Ipolicer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer>`
    
    	**presence node**\: True
    
    .. attribute:: punt
    
    	Configure penalty timeout value
    	**type**\:   :py:class:`Punt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt>`
    
    

    """

    _prefix = 'lpts-lib-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.ipolicer = None
        self.punt = Lpts.Punt()
        self.punt.parent = self


    class Ipolicer(object):
        """
        Pre IFiB Configuration 
        
        .. attribute:: enable
        
        	Enabled
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        .. attribute:: flows
        
        	Table for Flows
        	**type**\:   :py:class:`Flows <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Flows>`
        
        .. attribute:: ipv4acls
        
        	Table for ACLs
        	**type**\:   :py:class:`Ipv4Acls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Ipv4Acls>`
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'lpts-pre-ifib-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.enable = None
            self.flows = Lpts.Ipolicer.Flows()
            self.flows.parent = self
            self.ipv4acls = Lpts.Ipolicer.Ipv4Acls()
            self.ipv4acls.parent = self


        class Ipv4Acls(object):
            """
            Table for ACLs
            
            .. attribute:: ipv4acl
            
            	ACL name
            	**type**\: list of    :py:class:`Ipv4Acl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Ipv4Acls.Ipv4Acl>`
            
            

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
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: ipv4vrf_names
                
                	VRF list
                	**type**\:   :py:class:`Ipv4VrfNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Ipv4Acls.Ipv4Acl.Ipv4VrfNames>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.acl_name = None
                    self.ipv4vrf_names = Lpts.Ipolicer.Ipv4Acls.Ipv4Acl.Ipv4VrfNames()
                    self.ipv4vrf_names.parent = self


                class Ipv4VrfNames(object):
                    """
                    VRF list
                    
                    .. attribute:: ipv4vrf_name
                    
                    	VRF name
                    	**type**\: list of    :py:class:`Ipv4VrfName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Ipv4Acls.Ipv4Acl.Ipv4VrfNames.Ipv4VrfName>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ipv4vrf_name = YList()
                        self.ipv4vrf_name.parent = self
                        self.ipv4vrf_name.name = 'ipv4vrf_name'


                    class Ipv4VrfName(object):
                        """
                        VRF name
                        
                        .. attribute:: vrf_name  <key>
                        
                        	VRF name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: acl_rate
                        
                        	pre\-ifib policer rate config commands
                        	**type**\:  int
                        
                        	**range:** 0..100000
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.vrf_name = None
                            self.acl_rate = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.vrf_name is None:
                                raise YPYModelError('Key property vrf_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipv4vrf-name[Cisco-IOS-XR-lpts-pre-ifib-cfg:vrf-name = ' + str(self.vrf_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.vrf_name is not None:
                                return True

                            if self.acl_rate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                            return meta._meta_table['Lpts.Ipolicer.Ipv4Acls.Ipv4Acl.Ipv4VrfNames.Ipv4VrfName']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipv4vrf-names'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.ipv4vrf_name is not None:
                            for child_ref in self.ipv4vrf_name:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                        return meta._meta_table['Lpts.Ipolicer.Ipv4Acls.Ipv4Acl.Ipv4VrfNames']['meta_info']

                @property
                def _common_path(self):
                    if self.acl_name is None:
                        raise YPYModelError('Key property acl_name is None')

                    return '/Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipv4acls/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipv4acl[Cisco-IOS-XR-lpts-pre-ifib-cfg:acl-name = ' + str(self.acl_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.acl_name is not None:
                        return True

                    if self.ipv4vrf_names is not None and self.ipv4vrf_names._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                    return meta._meta_table['Lpts.Ipolicer.Ipv4Acls.Ipv4Acl']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipv4acls'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.ipv4acl is not None:
                    for child_ref in self.ipv4acl:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                return meta._meta_table['Lpts.Ipolicer.Ipv4Acls']['meta_info']


        class Flows(object):
            """
            Table for Flows
            
            .. attribute:: flow
            
            	selected flow type
            	**type**\: list of    :py:class:`Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Flows.Flow>`
            
            

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
                	**type**\:   :py:class:`LptsFlowEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlowEnum>`
                
                .. attribute:: precedences
                
                	TOS Precedence value(s)
                	**type**\:   :py:class:`Precedences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Flows.Flow.Precedences>`
                
                .. attribute:: rate
                
                	Configured rate value
                	**type**\:  int
                
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
                    
                    	**type**\:  list of   :py:class:`LptsPreIFibPrecedenceNumberEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPreIFibPrecedenceNumberEnum>`
                    
                    
                    ----
                    	**type**\:  list of int
                    
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
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:precedences'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.precedence is not None:
                            for child in self.precedence:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                        return meta._meta_table['Lpts.Ipolicer.Flows.Flow.Precedences']['meta_info']

                @property
                def _common_path(self):
                    if self.flow_type is None:
                        raise YPYModelError('Key property flow_type is None')

                    return '/Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer/Cisco-IOS-XR-lpts-pre-ifib-cfg:flows/Cisco-IOS-XR-lpts-pre-ifib-cfg:flow[Cisco-IOS-XR-lpts-pre-ifib-cfg:flow-type = ' + str(self.flow_type) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.flow_type is not None:
                        return True

                    if self.precedences is not None and self.precedences._has_data():
                        return True

                    if self.rate is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                    return meta._meta_table['Lpts.Ipolicer.Flows.Flow']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer/Cisco-IOS-XR-lpts-pre-ifib-cfg:flows'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.flow is not None:
                    for child_ref in self.flow:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                return meta._meta_table['Lpts.Ipolicer.Flows']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self._is_presence:
                return True
            if self.enable is not None:
                return True

            if self.flows is not None and self.flows._has_data():
                return True

            if self.ipv4acls is not None and self.ipv4acls._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
            return meta._meta_table['Lpts.Ipolicer']['meta_info']


    class Punt(object):
        """
        Configure penalty timeout value
        
        .. attribute:: flowtrap
        
        	excessive punt flow trap configuration commands
        	**type**\:   :py:class:`Flowtrap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap>`
        
        

        """

        _prefix = 'lpts-punt-flowtrap-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.flowtrap = Lpts.Punt.Flowtrap()
            self.flowtrap.parent = self


        class Flowtrap(object):
            """
            excessive punt flow trap configuration commands
            
            .. attribute:: dampening
            
            	Dampening period for a bad actor flow in milliseconds
            	**type**\:  int
            
            	**range:** 5000..60000
            
            .. attribute:: et_size
            
            	Should be power of 2. Any one of 1,2,4,8,16,32 ,64,128
            	**type**\:  int
            
            	**range:** 1..128
            
            .. attribute:: eviction_search_limit
            
            	Eviction search limit, should be less than trap\-size
            	**type**\:  int
            
            	**range:** 1..128
            
            .. attribute:: eviction_threshold
            
            	Eviction threshold, should be less than report\-threshold
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: exclude
            
            	Exclude an item from all traps
            	**type**\:   :py:class:`Exclude <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.Exclude>`
            
            .. attribute:: interface_based_flow
            
            	Identify flow based on interface and flowtype
            	**type**\:  bool
            
            .. attribute:: max_flow_gap
            
            	Maximum flow gap in milliseconds
            	**type**\:  int
            
            	**range:** 1..60000
            
            .. attribute:: non_subscriber_interfaces
            
            	Enable trap based on source mac on non\-subscriber interface
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: penalty_rates
            
            	Configure penalty policing rate
            	**type**\:   :py:class:`PenaltyRates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.PenaltyRates>`
            
            .. attribute:: penalty_timeouts
            
            	Configure penalty timeout value
            	**type**\:   :py:class:`PenaltyTimeouts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.PenaltyTimeouts>`
            
            .. attribute:: report_threshold
            
            	Threshold to cross for a flow to be considered as bad actor flow
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: routing_protocols_enable
            
            	Allow routing protocols to pass through copp sampler
            	**type**\:  bool
            
            .. attribute:: sample_prob
            
            	Probability of packets to be sampled
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: subscriber_interfaces
            
            	Enable the trap on subscriber interfaces
            	**type**\:  bool
            
            

            """

            _prefix = 'lpts-punt-flowtrap-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.dampening = None
                self.et_size = None
                self.eviction_search_limit = None
                self.eviction_threshold = None
                self.exclude = Lpts.Punt.Flowtrap.Exclude()
                self.exclude.parent = self
                self.interface_based_flow = None
                self.max_flow_gap = None
                self.non_subscriber_interfaces = None
                self.penalty_rates = Lpts.Punt.Flowtrap.PenaltyRates()
                self.penalty_rates.parent = self
                self.penalty_timeouts = Lpts.Punt.Flowtrap.PenaltyTimeouts()
                self.penalty_timeouts.parent = self
                self.report_threshold = None
                self.routing_protocols_enable = None
                self.sample_prob = None
                self.subscriber_interfaces = None


            class PenaltyRates(object):
                """
                Configure penalty policing rate
                
                .. attribute:: penalty_rate
                
                	none
                	**type**\: list of    :py:class:`PenaltyRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.PenaltyRates.PenaltyRate>`
                
                

                """

                _prefix = 'lpts-punt-flowtrap-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.penalty_rate = YList()
                    self.penalty_rate.parent = self
                    self.penalty_rate.name = 'penalty_rate'


                class PenaltyRate(object):
                    """
                    none
                    
                    .. attribute:: protocol_name  <key>
                    
                    	none
                    	**type**\:   :py:class:`LptsPuntFlowtrapProtoIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_punt_flowtrap_cfg.LptsPuntFlowtrapProtoIdEnum>`
                    
                    .. attribute:: rate
                    
                    	Penalty policer rate in packets\-per\-second
                    	**type**\:  int
                    
                    	**range:** 2..100
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'lpts-punt-flowtrap-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.protocol_name = None
                        self.rate = None

                    @property
                    def _common_path(self):
                        if self.protocol_name is None:
                            raise YPYModelError('Key property protocol_name is None')

                        return '/Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:flowtrap/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:penalty-rates/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:penalty-rate[Cisco-IOS-XR-lpts-punt-flowtrap-cfg:protocol-name = ' + str(self.protocol_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.protocol_name is not None:
                            return True

                        if self.rate is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                        return meta._meta_table['Lpts.Punt.Flowtrap.PenaltyRates.PenaltyRate']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:flowtrap/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:penalty-rates'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.penalty_rate is not None:
                        for child_ref in self.penalty_rate:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                    return meta._meta_table['Lpts.Punt.Flowtrap.PenaltyRates']['meta_info']


            class PenaltyTimeouts(object):
                """
                Configure penalty timeout value
                
                .. attribute:: penalty_timeout
                
                	none
                	**type**\: list of    :py:class:`PenaltyTimeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.PenaltyTimeouts.PenaltyTimeout>`
                
                

                """

                _prefix = 'lpts-punt-flowtrap-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.penalty_timeout = YList()
                    self.penalty_timeout.parent = self
                    self.penalty_timeout.name = 'penalty_timeout'


                class PenaltyTimeout(object):
                    """
                    none
                    
                    .. attribute:: protocol_name  <key>
                    
                    	none
                    	**type**\:   :py:class:`LptsPuntFlowtrapProtoIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_punt_flowtrap_cfg.LptsPuntFlowtrapProtoIdEnum>`
                    
                    .. attribute:: timeout
                    
                    	Timeout value in minutes
                    	**type**\:  int
                    
                    	**range:** 1..1000
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'lpts-punt-flowtrap-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.protocol_name = None
                        self.timeout = None

                    @property
                    def _common_path(self):
                        if self.protocol_name is None:
                            raise YPYModelError('Key property protocol_name is None')

                        return '/Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:flowtrap/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:penalty-timeouts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:penalty-timeout[Cisco-IOS-XR-lpts-punt-flowtrap-cfg:protocol-name = ' + str(self.protocol_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.protocol_name is not None:
                            return True

                        if self.timeout is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                        return meta._meta_table['Lpts.Punt.Flowtrap.PenaltyTimeouts.PenaltyTimeout']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:flowtrap/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:penalty-timeouts'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.penalty_timeout is not None:
                        for child_ref in self.penalty_timeout:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                    return meta._meta_table['Lpts.Punt.Flowtrap.PenaltyTimeouts']['meta_info']


            class Exclude(object):
                """
                Exclude an item from all traps
                
                .. attribute:: interface_names
                
                	none
                	**type**\:   :py:class:`InterfaceNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.Exclude.InterfaceNames>`
                
                

                """

                _prefix = 'lpts-punt-flowtrap-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_names = Lpts.Punt.Flowtrap.Exclude.InterfaceNames()
                    self.interface_names.parent = self


                class InterfaceNames(object):
                    """
                    none
                    
                    .. attribute:: interface_name
                    
                    	Name of interface to exclude from all traps
                    	**type**\: list of    :py:class:`InterfaceName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.Exclude.InterfaceNames.InterfaceName>`
                    
                    

                    """

                    _prefix = 'lpts-punt-flowtrap-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = YList()
                        self.interface_name.parent = self
                        self.interface_name.name = 'interface_name'


                    class InterfaceName(object):
                        """
                        Name of interface to exclude from all traps
                        
                        .. attribute:: ifname  <key>
                        
                        	Name of interface to exclude from all traps
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: id1
                        
                        	Enabled or disabled
                        	**type**\:  bool
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'lpts-punt-flowtrap-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ifname = None
                            self.id1 = None

                        @property
                        def _common_path(self):
                            if self.ifname is None:
                                raise YPYModelError('Key property ifname is None')

                            return '/Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:flowtrap/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:exclude/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:interface-names/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:interface-name[Cisco-IOS-XR-lpts-punt-flowtrap-cfg:ifname = ' + str(self.ifname) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.ifname is not None:
                                return True

                            if self.id1 is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                            return meta._meta_table['Lpts.Punt.Flowtrap.Exclude.InterfaceNames.InterfaceName']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:flowtrap/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:exclude/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:interface-names'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.interface_name is not None:
                            for child_ref in self.interface_name:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                        return meta._meta_table['Lpts.Punt.Flowtrap.Exclude.InterfaceNames']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:flowtrap/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:exclude'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.interface_names is not None and self.interface_names._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                    return meta._meta_table['Lpts.Punt.Flowtrap.Exclude']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:flowtrap'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.dampening is not None:
                    return True

                if self.et_size is not None:
                    return True

                if self.eviction_search_limit is not None:
                    return True

                if self.eviction_threshold is not None:
                    return True

                if self.exclude is not None and self.exclude._has_data():
                    return True

                if self.interface_based_flow is not None:
                    return True

                if self.max_flow_gap is not None:
                    return True

                if self.non_subscriber_interfaces is not None:
                    return True

                if self.penalty_rates is not None and self.penalty_rates._has_data():
                    return True

                if self.penalty_timeouts is not None and self.penalty_timeouts._has_data():
                    return True

                if self.report_threshold is not None:
                    return True

                if self.routing_protocols_enable is not None:
                    return True

                if self.sample_prob is not None:
                    return True

                if self.subscriber_interfaces is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                return meta._meta_table['Lpts.Punt.Flowtrap']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.flowtrap is not None and self.flowtrap._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
            return meta._meta_table['Lpts.Punt']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-lpts-lib-cfg:lpts'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.ipolicer is not None and self.ipolicer._has_data():
            return True

        if self.punt is not None and self.punt._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
        return meta._meta_table['Lpts']['meta_info']



""" Cisco_IOS_XR_infra_xtc_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-xtc package configuration.

This module contains definitions
for the following management objects\:
  pce\: PCE configuration data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class PceDisjointPathEnum(Enum):
    """
    PceDisjointPathEnum

    Pce disjoint path

    .. data:: link = 1

    	Link

    .. data:: node = 2

    	Node

    .. data:: srlg = 3

    	SRLG

    """

    link = 1

    node = 2

    srlg = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_cfg as meta
        return meta._meta_table['PceDisjointPathEnum']


class PceExplicitPathHopEnum(Enum):
    """
    PceExplicitPathHopEnum

    Pce explicit path hop

    .. data:: address = 1

    	Address

    .. data:: sid_node = 2

    	SID Node

    .. data:: sid_adjancency = 3

    	SID Adjacency

    .. data:: binding_sid = 4

    	Binding SID

    """

    address = 1

    sid_node = 2

    sid_adjancency = 3

    binding_sid = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_cfg as meta
        return meta._meta_table['PceExplicitPathHopEnum']



class Pce(object):
    """
    PCE configuration data
    
    .. attribute:: backoff
    
    	PCE backoff configuration
    	**type**\:   :py:class:`Backoff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.Backoff>`
    
    .. attribute:: disjoint_path
    
    	Disjoint path configuration
    	**type**\:   :py:class:`DisjointPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.DisjointPath>`
    
    .. attribute:: enable
    
    	True only
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: explicit_paths
    
    	Explicit paths
    	**type**\:   :py:class:`ExplicitPaths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.ExplicitPaths>`
    
    .. attribute:: logging
    
    	PCE logging configuration
    	**type**\:   :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.Logging>`
    
    .. attribute:: netconf
    
    	NETCONF configuration
    	**type**\:   :py:class:`Netconf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.Netconf>`
    
    .. attribute:: password
    
    	MD5 password
    	**type**\:  str
    
    	**pattern:** (!.+)\|([^!].+)
    
    .. attribute:: pcc_addresses
    
    	Path computation client configuration
    	**type**\:   :py:class:`PccAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.PccAddresses>`
    
    .. attribute:: segment_routing
    
    	PCE segment\-routing configuration
    	**type**\:   :py:class:`SegmentRouting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.SegmentRouting>`
    
    .. attribute:: server_address
    
    	IPv4 address of PCE server
    	**type**\:  str
    
    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
    
    .. attribute:: state_syncs
    
    	Standby PCE configuration
    	**type**\:   :py:class:`StateSyncs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.StateSyncs>`
    
    .. attribute:: timers
    
    	PCE Timers configuration
    	**type**\:   :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.Timers>`
    
    

    """

    _prefix = 'infra-xtc-cfg'
    _revision = '2016-05-31'

    def __init__(self):
        self.backoff = Pce.Backoff()
        self.backoff.parent = self
        self.disjoint_path = Pce.DisjointPath()
        self.disjoint_path.parent = self
        self.enable = None
        self.explicit_paths = Pce.ExplicitPaths()
        self.explicit_paths.parent = self
        self.logging = Pce.Logging()
        self.logging.parent = self
        self.netconf = Pce.Netconf()
        self.netconf.parent = self
        self.password = None
        self.pcc_addresses = Pce.PccAddresses()
        self.pcc_addresses.parent = self
        self.segment_routing = Pce.SegmentRouting()
        self.segment_routing.parent = self
        self.server_address = None
        self.state_syncs = Pce.StateSyncs()
        self.state_syncs.parent = self
        self.timers = Pce.Timers()
        self.timers.parent = self


    class PccAddresses(object):
        """
        Path computation client configuration
        
        .. attribute:: pcc_address
        
        	Path computation client address
        	**type**\: list of    :py:class:`PccAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.PccAddresses.PccAddress>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.pcc_address = YList()
            self.pcc_address.parent = self
            self.pcc_address.name = 'pcc_address'


        class PccAddress(object):
            """
            Path computation client address
            
            .. attribute:: address  <key>
            
            	IPv4 address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: enable
            
            	True only
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: lsp_names
            
            	MPLS label switched path
            	**type**\:   :py:class:`LspNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.PccAddresses.PccAddress.LspNames>`
            
            

            """

            _prefix = 'infra-xtc-cfg'
            _revision = '2016-05-31'

            def __init__(self):
                self.parent = None
                self.address = None
                self.enable = None
                self.lsp_names = Pce.PccAddresses.PccAddress.LspNames()
                self.lsp_names.parent = self


            class LspNames(object):
                """
                MPLS label switched path
                
                .. attribute:: lsp_name
                
                	MPLS label switched path
                	**type**\: list of    :py:class:`LspName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.PccAddresses.PccAddress.LspNames.LspName>`
                
                

                """

                _prefix = 'infra-xtc-cfg'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.lsp_name = YList()
                    self.lsp_name.parent = self
                    self.lsp_name.name = 'lsp_name'


                class LspName(object):
                    """
                    MPLS label switched path
                    
                    .. attribute:: name  <key>
                    
                    	LSP name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: enable
                    
                    	True only
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: explicit_path_name
                    
                    	Explicit\-path name
                    	**type**\:  str
                    
                    .. attribute:: rsvp_te
                    
                    	RSVP\-TE configuration
                    	**type**\:   :py:class:`RsvpTe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe>`
                    
                    .. attribute:: undelegate
                    
                    	Undelegate LSP
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'infra-xtc-cfg'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.name = None
                        self.enable = None
                        self.explicit_path_name = None
                        self.rsvp_te = Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe()
                        self.rsvp_te.parent = self
                        self.undelegate = None


                    class RsvpTe(object):
                        """
                        RSVP\-TE configuration
                        
                        .. attribute:: affinity
                        
                        	LSP Affinity
                        	**type**\:   :py:class:`Affinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Affinity>`
                        
                        .. attribute:: bandwidth
                        
                        	Bandwidth configuration
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**units**\: kbit/s
                        
                        .. attribute:: enable
                        
                        	True only
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: fast_protect
                        
                        	Enable fast protection
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: priority
                        
                        	Tunnel Setup and Hold Priorities
                        	**type**\:   :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Priority>`
                        
                        	**presence node**\: True
                        
                        

                        """

                        _prefix = 'infra-xtc-cfg'
                        _revision = '2016-05-31'

                        def __init__(self):
                            self.parent = None
                            self.affinity = Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Affinity()
                            self.affinity.parent = self
                            self.bandwidth = None
                            self.enable = None
                            self.fast_protect = None
                            self.priority = None


                        class Affinity(object):
                            """
                            LSP Affinity
                            
                            .. attribute:: exclude_any
                            
                            	Exclude\-any affinity value
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            .. attribute:: include_all
                            
                            	Include\-all affinity value
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            .. attribute:: include_any
                            
                            	Include\-any affinity value
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            

                            """

                            _prefix = 'infra-xtc-cfg'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self.exclude_any = None
                                self.include_all = None
                                self.include_any = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-cfg:affinity'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.exclude_any is not None:
                                    return True

                                if self.include_all is not None:
                                    return True

                                if self.include_any is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_cfg as meta
                                return meta._meta_table['Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Affinity']['meta_info']


                        class Priority(object):
                            """
                            Tunnel Setup and Hold Priorities
                            
                            .. attribute:: hold_priority
                            
                            	Hold Priority
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            	**mandatory**\: True
                            
                            .. attribute:: setup_priority
                            
                            	Setup Priority
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            	**mandatory**\: True
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'infra-xtc-cfg'
                            _revision = '2016-05-31'

                            def __init__(self):
                                self.parent = None
                                self._is_presence = True
                                self.hold_priority = None
                                self.setup_priority = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-cfg:priority'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self._is_presence:
                                    return True
                                if self.hold_priority is not None:
                                    return True

                                if self.setup_priority is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_cfg as meta
                                return meta._meta_table['Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Priority']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-cfg:rsvp-te'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.affinity is not None and self.affinity._has_data():
                                return True

                            if self.bandwidth is not None:
                                return True

                            if self.enable is not None:
                                return True

                            if self.fast_protect is not None:
                                return True

                            if self.priority is not None and self.priority._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_cfg as meta
                            return meta._meta_table['Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.name is None:
                            raise YPYModelError('Key property name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-cfg:lsp-name[Cisco-IOS-XR-infra-xtc-cfg:name = ' + str(self.name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.name is not None:
                            return True

                        if self.enable is not None:
                            return True

                        if self.explicit_path_name is not None:
                            return True

                        if self.rsvp_te is not None and self.rsvp_te._has_data():
                            return True

                        if self.undelegate is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_cfg as meta
                        return meta._meta_table['Pce.PccAddresses.PccAddress.LspNames.LspName']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-cfg:lsp-names'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.lsp_name is not None:
                        for child_ref in self.lsp_name:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_cfg as meta
                    return meta._meta_table['Pce.PccAddresses.PccAddress.LspNames']['meta_info']

            @property
            def _common_path(self):
                if self.address is None:
                    raise YPYModelError('Key property address is None')

                return '/Cisco-IOS-XR-infra-xtc-cfg:pce/Cisco-IOS-XR-infra-xtc-cfg:pcc-addresses/Cisco-IOS-XR-infra-xtc-cfg:pcc-address[Cisco-IOS-XR-infra-xtc-cfg:address = ' + str(self.address) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.address is not None:
                    return True

                if self.enable is not None:
                    return True

                if self.lsp_names is not None and self.lsp_names._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_cfg as meta
                return meta._meta_table['Pce.PccAddresses.PccAddress']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-cfg:pce/Cisco-IOS-XR-infra-xtc-cfg:pcc-addresses'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.pcc_address is not None:
                for child_ref in self.pcc_address:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_cfg as meta
            return meta._meta_table['Pce.PccAddresses']['meta_info']


    class Logging(object):
        """
        PCE logging configuration
        
        .. attribute:: fallback
        
        	Logging fallback configuration
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: no_path
        
        	Logging NO\-PATH configuration
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.fallback = None
            self.no_path = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-cfg:pce/Cisco-IOS-XR-infra-xtc-cfg:logging'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.fallback is not None:
                return True

            if self.no_path is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_cfg as meta
            return meta._meta_table['Pce.Logging']['meta_info']


    class Backoff(object):
        """
        PCE backoff configuration
        
        .. attribute:: difference
        
        	Backoff common difference configuration
        	**type**\:  int
        
        	**range:** 0..255
        
        	**default value**\: 2
        
        .. attribute:: ratio
        
        	Backoff common ratio configuration
        	**type**\:  int
        
        	**range:** 0..255
        
        	**default value**\: 2
        
        .. attribute:: threshold
        
        	Backoff threshold configuration
        	**type**\:  int
        
        	**range:** 0..3600
        
        	**default value**\: 0
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.difference = None
            self.ratio = None
            self.threshold = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-cfg:pce/Cisco-IOS-XR-infra-xtc-cfg:backoff'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.difference is not None:
                return True

            if self.ratio is not None:
                return True

            if self.threshold is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_cfg as meta
            return meta._meta_table['Pce.Backoff']['meta_info']


    class StateSyncs(object):
        """
        Standby PCE configuration
        
        .. attribute:: state_sync
        
        	Standby PCE ipv4 address
        	**type**\: list of    :py:class:`StateSync <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.StateSyncs.StateSync>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.state_sync = YList()
            self.state_sync.parent = self
            self.state_sync.name = 'state_sync'


        class StateSync(object):
            """
            Standby PCE ipv4 address
            
            .. attribute:: address  <key>
            
            	IPv4 address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'infra-xtc-cfg'
            _revision = '2016-05-31'

            def __init__(self):
                self.parent = None
                self.address = None

            @property
            def _common_path(self):
                if self.address is None:
                    raise YPYModelError('Key property address is None')

                return '/Cisco-IOS-XR-infra-xtc-cfg:pce/Cisco-IOS-XR-infra-xtc-cfg:state-syncs/Cisco-IOS-XR-infra-xtc-cfg:state-sync[Cisco-IOS-XR-infra-xtc-cfg:address = ' + str(self.address) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.address is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_cfg as meta
                return meta._meta_table['Pce.StateSyncs.StateSync']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-cfg:pce/Cisco-IOS-XR-infra-xtc-cfg:state-syncs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.state_sync is not None:
                for child_ref in self.state_sync:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_cfg as meta
            return meta._meta_table['Pce.StateSyncs']['meta_info']


    class SegmentRouting(object):
        """
        PCE segment\-routing configuration
        
        .. attribute:: strict_sid_only
        
        	Use strict\-sid\-only configuration
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: te_latency
        
        	Use te\-latency algorithm configuration
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.strict_sid_only = None
            self.te_latency = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-cfg:pce/Cisco-IOS-XR-infra-xtc-cfg:segment-routing'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.strict_sid_only is not None:
                return True

            if self.te_latency is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_cfg as meta
            return meta._meta_table['Pce.SegmentRouting']['meta_info']


    class Timers(object):
        """
        PCE Timers configuration
        
        .. attribute:: keepalive
        
        	Keepalive interval in seconds, zero to disable
        	**type**\:  int
        
        	**range:** 0..255
        
        	**units**\: second
        
        	**default value**\: 30
        
        .. attribute:: minimum_peer_keepalive
        
        	Minimum acceptable peer proposed keepalive interval
        	**type**\:  int
        
        	**range:** 0..255
        
        	**units**\: second
        
        	**default value**\: 20
        
        .. attribute:: reoptimization_timer
        
        	Topology reoptimization timer configuration
        	**type**\:  int
        
        	**range:** 10..3600
        
        	**units**\: second
        
        	**default value**\: 60
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.keepalive = None
            self.minimum_peer_keepalive = None
            self.reoptimization_timer = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-cfg:pce/Cisco-IOS-XR-infra-xtc-cfg:timers'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.keepalive is not None:
                return True

            if self.minimum_peer_keepalive is not None:
                return True

            if self.reoptimization_timer is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_cfg as meta
            return meta._meta_table['Pce.Timers']['meta_info']


    class Netconf(object):
        """
        NETCONF configuration
        
        .. attribute:: netconf_ssh
        
        	NETCONF SSH configuration
        	**type**\:   :py:class:`NetconfSsh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.Netconf.NetconfSsh>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.netconf_ssh = Pce.Netconf.NetconfSsh()
            self.netconf_ssh.parent = self


        class NetconfSsh(object):
            """
            NETCONF SSH configuration
            
            .. attribute:: netconf_ssh_password
            
            	Password to use for NETCONF SSH connections
            	**type**\:  str
            
            	**pattern:** (!.+)\|([^!].+)
            
            .. attribute:: netconf_ssh_user
            
            	User name to use for NETCONF SSH connections
            	**type**\:  str
            
            

            """

            _prefix = 'infra-xtc-cfg'
            _revision = '2016-05-31'

            def __init__(self):
                self.parent = None
                self.netconf_ssh_password = None
                self.netconf_ssh_user = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-xtc-cfg:pce/Cisco-IOS-XR-infra-xtc-cfg:netconf/Cisco-IOS-XR-infra-xtc-cfg:netconf-ssh'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.netconf_ssh_password is not None:
                    return True

                if self.netconf_ssh_user is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_cfg as meta
                return meta._meta_table['Pce.Netconf.NetconfSsh']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-cfg:pce/Cisco-IOS-XR-infra-xtc-cfg:netconf'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.netconf_ssh is not None and self.netconf_ssh._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_cfg as meta
            return meta._meta_table['Pce.Netconf']['meta_info']


    class DisjointPath(object):
        """
        Disjoint path configuration
        
        .. attribute:: groups
        
        	Association configuration
        	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.DisjointPath.Groups>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.groups = Pce.DisjointPath.Groups()
            self.groups.parent = self


        class Groups(object):
            """
            Association configuration
            
            .. attribute:: group
            
            	Association Group Configuration
            	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.DisjointPath.Groups.Group>`
            
            

            """

            _prefix = 'infra-xtc-cfg'
            _revision = '2016-05-31'

            def __init__(self):
                self.parent = None
                self.group = YList()
                self.group.parent = self
                self.group.name = 'group'


            class Group(object):
                """
                Association Group Configuration
                
                .. attribute:: group_id  <key>
                
                	Group ID
                	**type**\:  int
                
                	**range:** 1..65535
                
                .. attribute:: dp_type  <key>
                
                	Disjoiness type
                	**type**\:   :py:class:`PceDisjointPathEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.PceDisjointPathEnum>`
                
                .. attribute:: sub_id  <key>
                
                	Sub group ID, 0 to unset
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: strict
                
                	Disable Fallback
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'infra-xtc-cfg'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.group_id = None
                    self.dp_type = None
                    self.sub_id = None
                    self.strict = None

                @property
                def _common_path(self):
                    if self.group_id is None:
                        raise YPYModelError('Key property group_id is None')
                    if self.dp_type is None:
                        raise YPYModelError('Key property dp_type is None')
                    if self.sub_id is None:
                        raise YPYModelError('Key property sub_id is None')

                    return '/Cisco-IOS-XR-infra-xtc-cfg:pce/Cisco-IOS-XR-infra-xtc-cfg:disjoint-path/Cisco-IOS-XR-infra-xtc-cfg:groups/Cisco-IOS-XR-infra-xtc-cfg:group[Cisco-IOS-XR-infra-xtc-cfg:group-id = ' + str(self.group_id) + '][Cisco-IOS-XR-infra-xtc-cfg:dp-type = ' + str(self.dp_type) + '][Cisco-IOS-XR-infra-xtc-cfg:sub-id = ' + str(self.sub_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.group_id is not None:
                        return True

                    if self.dp_type is not None:
                        return True

                    if self.sub_id is not None:
                        return True

                    if self.strict is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_cfg as meta
                    return meta._meta_table['Pce.DisjointPath.Groups.Group']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-xtc-cfg:pce/Cisco-IOS-XR-infra-xtc-cfg:disjoint-path/Cisco-IOS-XR-infra-xtc-cfg:groups'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.group is not None:
                    for child_ref in self.group:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_cfg as meta
                return meta._meta_table['Pce.DisjointPath.Groups']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-cfg:pce/Cisco-IOS-XR-infra-xtc-cfg:disjoint-path'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.groups is not None and self.groups._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_cfg as meta
            return meta._meta_table['Pce.DisjointPath']['meta_info']


    class ExplicitPaths(object):
        """
        Explicit paths
        
        .. attribute:: explicit_path
        
        	Explicit\-path configuration
        	**type**\: list of    :py:class:`ExplicitPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.ExplicitPaths.ExplicitPath>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            self.parent = None
            self.explicit_path = YList()
            self.explicit_path.parent = self
            self.explicit_path.name = 'explicit_path'


        class ExplicitPath(object):
            """
            Explicit\-path configuration
            
            .. attribute:: name  <key>
            
            	Explicit\-path name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: enable
            
            	True only
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: path_hops
            
            	Path Hops
            	**type**\:   :py:class:`PathHops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.ExplicitPaths.ExplicitPath.PathHops>`
            
            

            """

            _prefix = 'infra-xtc-cfg'
            _revision = '2016-05-31'

            def __init__(self):
                self.parent = None
                self.name = None
                self.enable = None
                self.path_hops = Pce.ExplicitPaths.ExplicitPath.PathHops()
                self.path_hops.parent = self


            class PathHops(object):
                """
                Path Hops
                
                .. attribute:: path_hop
                
                	Explicit path hop configuration
                	**type**\: list of    :py:class:`PathHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.ExplicitPaths.ExplicitPath.PathHops.PathHop>`
                
                

                """

                _prefix = 'infra-xtc-cfg'
                _revision = '2016-05-31'

                def __init__(self):
                    self.parent = None
                    self.path_hop = YList()
                    self.path_hop.parent = self
                    self.path_hop.name = 'path_hop'


                class PathHop(object):
                    """
                    Explicit path hop configuration
                    
                    .. attribute:: index  <key>
                    
                    	Hop Index
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: address
                    
                    	IPv4 Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**default value**\: 0.0.0.0
                    
                    .. attribute:: hop_type
                    
                    	Path hop type
                    	**type**\:   :py:class:`PceExplicitPathHopEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.PceExplicitPathHopEnum>`
                    
                    .. attribute:: mpls_label
                    
                    	MPLS Label
                    	**type**\:  int
                    
                    	**range:** 0..1048575
                    
                    	**default value**\: 0
                    
                    .. attribute:: remote_address
                    
                    	Remote IPv4 address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**default value**\: 0.0.0.0
                    
                    

                    """

                    _prefix = 'infra-xtc-cfg'
                    _revision = '2016-05-31'

                    def __init__(self):
                        self.parent = None
                        self.index = None
                        self.address = None
                        self.hop_type = None
                        self.mpls_label = None
                        self.remote_address = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.index is None:
                            raise YPYModelError('Key property index is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-cfg:path-hop[Cisco-IOS-XR-infra-xtc-cfg:index = ' + str(self.index) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.index is not None:
                            return True

                        if self.address is not None:
                            return True

                        if self.hop_type is not None:
                            return True

                        if self.mpls_label is not None:
                            return True

                        if self.remote_address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_cfg as meta
                        return meta._meta_table['Pce.ExplicitPaths.ExplicitPath.PathHops.PathHop']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-xtc-cfg:path-hops'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.path_hop is not None:
                        for child_ref in self.path_hop:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_cfg as meta
                    return meta._meta_table['Pce.ExplicitPaths.ExplicitPath.PathHops']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-infra-xtc-cfg:pce/Cisco-IOS-XR-infra-xtc-cfg:explicit-paths/Cisco-IOS-XR-infra-xtc-cfg:explicit-path[Cisco-IOS-XR-infra-xtc-cfg:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.enable is not None:
                    return True

                if self.path_hops is not None and self.path_hops._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_cfg as meta
                return meta._meta_table['Pce.ExplicitPaths.ExplicitPath']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-xtc-cfg:pce/Cisco-IOS-XR-infra-xtc-cfg:explicit-paths'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.explicit_path is not None:
                for child_ref in self.explicit_path:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_cfg as meta
            return meta._meta_table['Pce.ExplicitPaths']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-xtc-cfg:pce'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.backoff is not None and self.backoff._has_data():
            return True

        if self.disjoint_path is not None and self.disjoint_path._has_data():
            return True

        if self.enable is not None:
            return True

        if self.explicit_paths is not None and self.explicit_paths._has_data():
            return True

        if self.logging is not None and self.logging._has_data():
            return True

        if self.netconf is not None and self.netconf._has_data():
            return True

        if self.password is not None:
            return True

        if self.pcc_addresses is not None and self.pcc_addresses._has_data():
            return True

        if self.segment_routing is not None and self.segment_routing._has_data():
            return True

        if self.server_address is not None:
            return True

        if self.state_syncs is not None and self.state_syncs._has_data():
            return True

        if self.timers is not None and self.timers._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_cfg as meta
        return meta._meta_table['Pce']['meta_info']



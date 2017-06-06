""" Cisco_IOS_XE_bfd_oper 

This module contains a collection of YANG definitions for
monitoring BFD neighbours.Copyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class BfdLspTypeEnum(Enum):
    """
    BfdLspTypeEnum

    BFD lsp type

    .. data:: working = 0

    .. data:: protect = 1

    .. data:: unknown = 2

    """

    working = 0

    protect = 1

    unknown = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bfd_oper as meta
        return meta._meta_table['BfdLspTypeEnum']


class BfdOperSessionTypeEnum(Enum):
    """
    BfdOperSessionTypeEnum

    BFD session type

    .. data:: ipv4 = 0

    .. data:: ipv6 = 1

    .. data:: vccv = 2

    .. data:: mpls_tp = 3

    .. data:: ipv4_multihop = 4

    .. data:: ipv6_multihop = 5

    """

    ipv4 = 0

    ipv6 = 1

    vccv = 2

    mpls_tp = 3

    ipv4_multihop = 4

    ipv6_multihop = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bfd_oper as meta
        return meta._meta_table['BfdOperSessionTypeEnum']


class BfdRemoteStateTypeEnum(Enum):
    """
    BfdRemoteStateTypeEnum

    BFD remote state type

    .. data:: up = 0

    .. data:: down = 1

    .. data:: init = 2

    .. data:: admindown = 3

    .. data:: invalid = 4

    """

    up = 0

    down = 1

    init = 2

    admindown = 3

    invalid = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bfd_oper as meta
        return meta._meta_table['BfdRemoteStateTypeEnum']


class BfdStateTypeEnum(Enum):
    """
    BfdStateTypeEnum

    BFD state type

    .. data:: admindown = 0

    .. data:: down = 1

    .. data:: fail = 2

    .. data:: init = 3

    .. data:: up = 4

    .. data:: invalid = 5

    """

    admindown = 0

    down = 1

    fail = 2

    init = 3

    up = 4

    invalid = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bfd_oper as meta
        return meta._meta_table['BfdStateTypeEnum']



class BfdState(object):
    """
    Data nodes for BFD neighbors.
    
    .. attribute:: sessions
    
    	
    	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions>`
    
    

    """

    _prefix = 'bfd-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        self.sessions = BfdState.Sessions()
        self.sessions.parent = self


    class Sessions(object):
        """
        
        
        .. attribute:: session
        
        	
        	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session>`
        
        

        """

        _prefix = 'bfd-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.session = YList()
            self.session.parent = self
            self.session.name = 'session'


        class Session(object):
            """
            
            
            .. attribute:: type  <key>
            
            	Session type
            	**type**\:   :py:class:`BfdOperSessionTypeEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdOperSessionTypeEnum>`
            
            .. attribute:: bfd_circuits
            
            	
            	**type**\:   :py:class:`BfdCircuits <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdCircuits>`
            
            .. attribute:: bfd_mhop_nbrs
            
            	
            	**type**\:   :py:class:`BfdMhopNbrs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdMhopNbrs>`
            
            .. attribute:: bfd_mhop_vrf_nbrs
            
            	
            	**type**\:   :py:class:`BfdMhopVrfNbrs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdMhopVrfNbrs>`
            
            .. attribute:: bfd_nbrs
            
            	
            	**type**\:   :py:class:`BfdNbrs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdNbrs>`
            
            .. attribute:: bfd_tunnel_paths
            
            	
            	**type**\:   :py:class:`BfdTunnelPaths <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdTunnelPaths>`
            
            

            """

            _prefix = 'bfd-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.type = None
                self.bfd_circuits = BfdState.Sessions.Session.BfdCircuits()
                self.bfd_circuits.parent = self
                self.bfd_mhop_nbrs = BfdState.Sessions.Session.BfdMhopNbrs()
                self.bfd_mhop_nbrs.parent = self
                self.bfd_mhop_vrf_nbrs = BfdState.Sessions.Session.BfdMhopVrfNbrs()
                self.bfd_mhop_vrf_nbrs.parent = self
                self.bfd_nbrs = BfdState.Sessions.Session.BfdNbrs()
                self.bfd_nbrs.parent = self
                self.bfd_tunnel_paths = BfdState.Sessions.Session.BfdTunnelPaths()
                self.bfd_tunnel_paths.parent = self


            class BfdTunnelPaths(object):
                """
                
                
                .. attribute:: bfd_tunnel_path
                
                	Tunnel Path
                	**type**\: list of    :py:class:`BfdTunnelPath <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdTunnelPaths.BfdTunnelPath>`
                
                

                """

                _prefix = 'bfd-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.bfd_tunnel_path = YList()
                    self.bfd_tunnel_path.parent = self
                    self.bfd_tunnel_path.name = 'bfd_tunnel_path'


                class BfdTunnelPath(object):
                    """
                    Tunnel Path
                    
                    .. attribute:: interface  <key>
                    
                    	
                    	**type**\:  str
                    
                    .. attribute:: lsp_type  <key>
                    
                    	
                    	**type**\:   :py:class:`BfdLspTypeEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdLspTypeEnum>`
                    
                    .. attribute:: ld
                    
                    	local\-discriminator
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rd
                    
                    	remote\-discriminator
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: remote_state
                    
                    	 Remote Heard. RH state of BFD version '0'   is also mapped to up/down. 
                    	**type**\:   :py:class:`BfdRemoteStateTypeEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdRemoteStateTypeEnum>`
                    
                    .. attribute:: state
                    
                    	BFD state
                    	**type**\:   :py:class:`BfdStateTypeEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdStateTypeEnum>`
                    
                    

                    """

                    _prefix = 'bfd-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.interface = None
                        self.lsp_type = None
                        self.ld = None
                        self.rd = None
                        self.remote_state = None
                        self.state = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface is None:
                            raise YPYModelError('Key property interface is None')
                        if self.lsp_type is None:
                            raise YPYModelError('Key property lsp_type is None')

                        return self.parent._common_path +'/Cisco-IOS-XE-bfd-oper:bfd-tunnel-path[Cisco-IOS-XE-bfd-oper:interface = ' + str(self.interface) + '][Cisco-IOS-XE-bfd-oper:lsp-type = ' + str(self.lsp_type) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface is not None:
                            return True

                        if self.lsp_type is not None:
                            return True

                        if self.ld is not None:
                            return True

                        if self.rd is not None:
                            return True

                        if self.remote_state is not None:
                            return True

                        if self.state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bfd_oper as meta
                        return meta._meta_table['BfdState.Sessions.Session.BfdTunnelPaths.BfdTunnelPath']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-bfd-oper:bfd-tunnel-paths'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bfd_tunnel_path is not None:
                        for child_ref in self.bfd_tunnel_path:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bfd_oper as meta
                    return meta._meta_table['BfdState.Sessions.Session.BfdTunnelPaths']['meta_info']


            class BfdCircuits(object):
                """
                
                
                .. attribute:: bfd_circuit
                
                	BFD circuit
                	**type**\: list of    :py:class:`BfdCircuit <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdCircuits.BfdCircuit>`
                
                

                """

                _prefix = 'bfd-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.bfd_circuit = YList()
                    self.bfd_circuit.parent = self
                    self.bfd_circuit.name = 'bfd_circuit'


                class BfdCircuit(object):
                    """
                    BFD circuit
                    
                    .. attribute:: interface  <key>
                    
                    	
                    	**type**\:  str
                    
                    .. attribute:: vcid  <key>
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ld
                    
                    	local\-discriminator
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rd
                    
                    	remote\-discriminator
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: remote_state
                    
                    	 Remote Heard. RH state of BFD version '0'   is also mapped to up/down. 
                    	**type**\:   :py:class:`BfdRemoteStateTypeEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdRemoteStateTypeEnum>`
                    
                    .. attribute:: state
                    
                    	BFD state
                    	**type**\:   :py:class:`BfdStateTypeEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdStateTypeEnum>`
                    
                    

                    """

                    _prefix = 'bfd-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.interface = None
                        self.vcid = None
                        self.ld = None
                        self.rd = None
                        self.remote_state = None
                        self.state = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface is None:
                            raise YPYModelError('Key property interface is None')
                        if self.vcid is None:
                            raise YPYModelError('Key property vcid is None')

                        return self.parent._common_path +'/Cisco-IOS-XE-bfd-oper:bfd-circuit[Cisco-IOS-XE-bfd-oper:interface = ' + str(self.interface) + '][Cisco-IOS-XE-bfd-oper:vcid = ' + str(self.vcid) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface is not None:
                            return True

                        if self.vcid is not None:
                            return True

                        if self.ld is not None:
                            return True

                        if self.rd is not None:
                            return True

                        if self.remote_state is not None:
                            return True

                        if self.state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bfd_oper as meta
                        return meta._meta_table['BfdState.Sessions.Session.BfdCircuits.BfdCircuit']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-bfd-oper:bfd-circuits'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bfd_circuit is not None:
                        for child_ref in self.bfd_circuit:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bfd_oper as meta
                    return meta._meta_table['BfdState.Sessions.Session.BfdCircuits']['meta_info']


            class BfdNbrs(object):
                """
                
                
                .. attribute:: bfd_nbr
                
                	This is for directly connected neighbor case
                	**type**\: list of    :py:class:`BfdNbr <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdNbrs.BfdNbr>`
                
                

                """

                _prefix = 'bfd-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.bfd_nbr = YList()
                    self.bfd_nbr.parent = self
                    self.bfd_nbr.name = 'bfd_nbr'


                class BfdNbr(object):
                    """
                    This is for directly connected neighbor case
                    
                    .. attribute:: ip  <key>
                    
                    	
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: interface  <key>
                    
                    	
                    	**type**\:  str
                    
                    .. attribute:: ld
                    
                    	local\-discriminator
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rd
                    
                    	remote\-discriminator
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: remote_state
                    
                    	 Remote Heard. RH state of BFD version '0'   is also mapped to up/down. 
                    	**type**\:   :py:class:`BfdRemoteStateTypeEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdRemoteStateTypeEnum>`
                    
                    .. attribute:: state
                    
                    	BFD state
                    	**type**\:   :py:class:`BfdStateTypeEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdStateTypeEnum>`
                    
                    

                    """

                    _prefix = 'bfd-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.ip = None
                        self.interface = None
                        self.ld = None
                        self.rd = None
                        self.remote_state = None
                        self.state = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.ip is None:
                            raise YPYModelError('Key property ip is None')
                        if self.interface is None:
                            raise YPYModelError('Key property interface is None')

                        return self.parent._common_path +'/Cisco-IOS-XE-bfd-oper:bfd-nbr[Cisco-IOS-XE-bfd-oper:ip = ' + str(self.ip) + '][Cisco-IOS-XE-bfd-oper:interface = ' + str(self.interface) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ip is not None:
                            return True

                        if self.interface is not None:
                            return True

                        if self.ld is not None:
                            return True

                        if self.rd is not None:
                            return True

                        if self.remote_state is not None:
                            return True

                        if self.state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bfd_oper as meta
                        return meta._meta_table['BfdState.Sessions.Session.BfdNbrs.BfdNbr']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-bfd-oper:bfd-nbrs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bfd_nbr is not None:
                        for child_ref in self.bfd_nbr:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bfd_oper as meta
                    return meta._meta_table['BfdState.Sessions.Session.BfdNbrs']['meta_info']


            class BfdMhopNbrs(object):
                """
                
                
                .. attribute:: bfd_mhop_nbr
                
                	This is for multi hop neighbor scenario  for global VRF (no VRF)
                	**type**\: list of    :py:class:`BfdMhopNbr <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdMhopNbrs.BfdMhopNbr>`
                
                

                """

                _prefix = 'bfd-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.bfd_mhop_nbr = YList()
                    self.bfd_mhop_nbr.parent = self
                    self.bfd_mhop_nbr.name = 'bfd_mhop_nbr'


                class BfdMhopNbr(object):
                    """
                    This is for multi hop neighbor scenario 
                    for global VRF (no VRF).
                    
                    .. attribute:: ip  <key>
                    
                    	
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: ld
                    
                    	local\-discriminator
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rd
                    
                    	remote\-discriminator
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: remote_state
                    
                    	 Remote Heard. RH state of BFD version '0'   is also mapped to up/down. 
                    	**type**\:   :py:class:`BfdRemoteStateTypeEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdRemoteStateTypeEnum>`
                    
                    .. attribute:: state
                    
                    	BFD state
                    	**type**\:   :py:class:`BfdStateTypeEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdStateTypeEnum>`
                    
                    

                    """

                    _prefix = 'bfd-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.ip = None
                        self.ld = None
                        self.rd = None
                        self.remote_state = None
                        self.state = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.ip is None:
                            raise YPYModelError('Key property ip is None')

                        return self.parent._common_path +'/Cisco-IOS-XE-bfd-oper:bfd-mhop-nbr[Cisco-IOS-XE-bfd-oper:ip = ' + str(self.ip) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ip is not None:
                            return True

                        if self.ld is not None:
                            return True

                        if self.rd is not None:
                            return True

                        if self.remote_state is not None:
                            return True

                        if self.state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bfd_oper as meta
                        return meta._meta_table['BfdState.Sessions.Session.BfdMhopNbrs.BfdMhopNbr']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-bfd-oper:bfd-mhop-nbrs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bfd_mhop_nbr is not None:
                        for child_ref in self.bfd_mhop_nbr:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bfd_oper as meta
                    return meta._meta_table['BfdState.Sessions.Session.BfdMhopNbrs']['meta_info']


            class BfdMhopVrfNbrs(object):
                """
                
                
                .. attribute:: bfd_mhop_vrf_nbr
                
                	This is for multi hop neighbor scenario  for non\-global VRF
                	**type**\: list of    :py:class:`BfdMhopVrfNbr <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdMhopVrfNbrs.BfdMhopVrfNbr>`
                
                

                """

                _prefix = 'bfd-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.bfd_mhop_vrf_nbr = YList()
                    self.bfd_mhop_vrf_nbr.parent = self
                    self.bfd_mhop_vrf_nbr.name = 'bfd_mhop_vrf_nbr'


                class BfdMhopVrfNbr(object):
                    """
                    This is for multi hop neighbor scenario 
                    for non\-global VRF.
                    
                    .. attribute:: ip  <key>
                    
                    	
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: vrf  <key>
                    
                    	
                    	**type**\:  str
                    
                    .. attribute:: ld
                    
                    	local\-discriminator
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rd
                    
                    	remote\-discriminator
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: remote_state
                    
                    	 Remote Heard. RH state of BFD version '0'   is also mapped to up/down. 
                    	**type**\:   :py:class:`BfdRemoteStateTypeEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdRemoteStateTypeEnum>`
                    
                    .. attribute:: state
                    
                    	BFD state
                    	**type**\:   :py:class:`BfdStateTypeEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdStateTypeEnum>`
                    
                    

                    """

                    _prefix = 'bfd-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.ip = None
                        self.vrf = None
                        self.ld = None
                        self.rd = None
                        self.remote_state = None
                        self.state = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.ip is None:
                            raise YPYModelError('Key property ip is None')
                        if self.vrf is None:
                            raise YPYModelError('Key property vrf is None')

                        return self.parent._common_path +'/Cisco-IOS-XE-bfd-oper:bfd-mhop-vrf-nbr[Cisco-IOS-XE-bfd-oper:ip = ' + str(self.ip) + '][Cisco-IOS-XE-bfd-oper:vrf = ' + str(self.vrf) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ip is not None:
                            return True

                        if self.vrf is not None:
                            return True

                        if self.ld is not None:
                            return True

                        if self.rd is not None:
                            return True

                        if self.remote_state is not None:
                            return True

                        if self.state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bfd_oper as meta
                        return meta._meta_table['BfdState.Sessions.Session.BfdMhopVrfNbrs.BfdMhopVrfNbr']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-bfd-oper:bfd-mhop-vrf-nbrs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bfd_mhop_vrf_nbr is not None:
                        for child_ref in self.bfd_mhop_vrf_nbr:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bfd_oper as meta
                    return meta._meta_table['BfdState.Sessions.Session.BfdMhopVrfNbrs']['meta_info']

            @property
            def _common_path(self):
                if self.type is None:
                    raise YPYModelError('Key property type is None')

                return '/Cisco-IOS-XE-bfd-oper:bfd-state/Cisco-IOS-XE-bfd-oper:sessions/Cisco-IOS-XE-bfd-oper:session[Cisco-IOS-XE-bfd-oper:type = ' + str(self.type) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.type is not None:
                    return True

                if self.bfd_circuits is not None and self.bfd_circuits._has_data():
                    return True

                if self.bfd_mhop_nbrs is not None and self.bfd_mhop_nbrs._has_data():
                    return True

                if self.bfd_mhop_vrf_nbrs is not None and self.bfd_mhop_vrf_nbrs._has_data():
                    return True

                if self.bfd_nbrs is not None and self.bfd_nbrs._has_data():
                    return True

                if self.bfd_tunnel_paths is not None and self.bfd_tunnel_paths._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bfd_oper as meta
                return meta._meta_table['BfdState.Sessions.Session']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-bfd-oper:bfd-state/Cisco-IOS-XE-bfd-oper:sessions'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.session is not None:
                for child_ref in self.session:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bfd_oper as meta
            return meta._meta_table['BfdState.Sessions']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-bfd-oper:bfd-state'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.sessions is not None and self.sessions._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bfd_oper as meta
        return meta._meta_table['BfdState']['meta_info']



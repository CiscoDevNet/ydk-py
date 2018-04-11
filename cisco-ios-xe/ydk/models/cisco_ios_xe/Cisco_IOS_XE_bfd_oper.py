""" Cisco_IOS_XE_bfd_oper 

This module contains a collection of YANG definitions
for BFD neighbor monitoring.
Copyright (c) 2016\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class BfdLspType(Enum):
    """
    BfdLspType (Enum Class)

    BFD LSP type

    .. data:: working = 0

    .. data:: protect = 1

    .. data:: unknown = 2

    """

    working = Enum.YLeaf(0, "working")

    protect = Enum.YLeaf(1, "protect")

    unknown = Enum.YLeaf(2, "unknown")


class BfdOperSessionType(Enum):
    """
    BfdOperSessionType (Enum Class)

    BFD session type

    .. data:: ipv4 = 0

    .. data:: ipv6 = 1

    .. data:: vccv = 2

    .. data:: mpls_tp = 3

    .. data:: ipv4_multihop = 4

    .. data:: ipv6_multihop = 5

    """

    ipv4 = Enum.YLeaf(0, "ipv4")

    ipv6 = Enum.YLeaf(1, "ipv6")

    vccv = Enum.YLeaf(2, "vccv")

    mpls_tp = Enum.YLeaf(3, "mpls-tp")

    ipv4_multihop = Enum.YLeaf(4, "ipv4-multihop")

    ipv6_multihop = Enum.YLeaf(5, "ipv6-multihop")


class BfdRemoteStateType(Enum):
    """
    BfdRemoteStateType (Enum Class)

    BFD remote state type

    .. data:: remote_up = 0

    .. data:: remote_down = 1

    .. data:: remote_init = 2

    .. data:: remote_admindown = 3

    .. data:: remote_invalid = 4

    """

    remote_up = Enum.YLeaf(0, "remote-up")

    remote_down = Enum.YLeaf(1, "remote-down")

    remote_init = Enum.YLeaf(2, "remote-init")

    remote_admindown = Enum.YLeaf(3, "remote-admindown")

    remote_invalid = Enum.YLeaf(4, "remote-invalid")


class BfdStateType(Enum):
    """
    BfdStateType (Enum Class)

    BFD state type

    .. data:: admindown = 0

    .. data:: down = 1

    .. data:: fail = 2

    .. data:: init = 3

    .. data:: up = 4

    .. data:: invalid = 5

    """

    admindown = Enum.YLeaf(0, "admindown")

    down = Enum.YLeaf(1, "down")

    fail = Enum.YLeaf(2, "fail")

    init = Enum.YLeaf(3, "init")

    up = Enum.YLeaf(4, "up")

    invalid = Enum.YLeaf(5, "invalid")



class BfdState(Entity):
    """
    BFD neighbor information
    
    .. attribute:: sessions
    
    	BFD neighbor session information
    	**type**\:  :py:class:`Sessions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions>`
    
    

    """

    _prefix = 'bfd-ios-xe-oper'
    _revision = '2017-09-10'

    def __init__(self):
        super(BfdState, self).__init__()
        self._top_entity = None

        self.yang_name = "bfd-state"
        self.yang_parent_name = "Cisco-IOS-XE-bfd-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("sessions", ("sessions", BfdState.Sessions))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.sessions = BfdState.Sessions()
        self.sessions.parent = self
        self._children_name_map["sessions"] = "sessions"
        self._children_yang_names.add("sessions")
        self._segment_path = lambda: "Cisco-IOS-XE-bfd-oper:bfd-state"


    class Sessions(Entity):
        """
        BFD neighbor session information
        
        .. attribute:: session
        
        	List of BFD sessions
        	**type**\: list of  		 :py:class:`Session <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session>`
        
        

        """

        _prefix = 'bfd-ios-xe-oper'
        _revision = '2017-09-10'

        def __init__(self):
            super(BfdState.Sessions, self).__init__()

            self.yang_name = "sessions"
            self.yang_parent_name = "bfd-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("session", ("session", BfdState.Sessions.Session))])
            self._leafs = OrderedDict()

            self.session = YList(self)
            self._segment_path = lambda: "sessions"
            self._absolute_path = lambda: "Cisco-IOS-XE-bfd-oper:bfd-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BfdState.Sessions, [], name, value)


        class Session(Entity):
            """
            List of BFD sessions
            
            .. attribute:: type  (key)
            
            	Session type
            	**type**\:  :py:class:`BfdOperSessionType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdOperSessionType>`
            
            .. attribute:: bfd_tunnel_paths
            
            	BFD tunnel path information
            	**type**\:  :py:class:`BfdTunnelPaths <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdTunnelPaths>`
            
            .. attribute:: bfd_circuits
            
            	BFD circuit information
            	**type**\:  :py:class:`BfdCircuits <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdCircuits>`
            
            .. attribute:: bfd_nbrs
            
            	BFD neighbor information
            	**type**\:  :py:class:`BfdNbrs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdNbrs>`
            
            .. attribute:: bfd_mhop_nbrs
            
            	Multi hop neighbors for multi hop neighbor scenario  for global VRF (no VRF)
            	**type**\:  :py:class:`BfdMhopNbrs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdMhopNbrs>`
            
            .. attribute:: bfd_mhop_vrf_nbrs
            
            	Multi hop neighbors for multi hop neighbor scenario with non\-global VRF
            	**type**\:  :py:class:`BfdMhopVrfNbrs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdMhopVrfNbrs>`
            
            

            """

            _prefix = 'bfd-ios-xe-oper'
            _revision = '2017-09-10'

            def __init__(self):
                super(BfdState.Sessions.Session, self).__init__()

                self.yang_name = "session"
                self.yang_parent_name = "sessions"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['type']
                self._child_container_classes = OrderedDict([("bfd-tunnel-paths", ("bfd_tunnel_paths", BfdState.Sessions.Session.BfdTunnelPaths)), ("bfd-circuits", ("bfd_circuits", BfdState.Sessions.Session.BfdCircuits)), ("bfd-nbrs", ("bfd_nbrs", BfdState.Sessions.Session.BfdNbrs)), ("bfd-mhop-nbrs", ("bfd_mhop_nbrs", BfdState.Sessions.Session.BfdMhopNbrs)), ("bfd-mhop-vrf-nbrs", ("bfd_mhop_vrf_nbrs", BfdState.Sessions.Session.BfdMhopVrfNbrs))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('type', YLeaf(YType.enumeration, 'type')),
                ])
                self.type = None

                self.bfd_tunnel_paths = BfdState.Sessions.Session.BfdTunnelPaths()
                self.bfd_tunnel_paths.parent = self
                self._children_name_map["bfd_tunnel_paths"] = "bfd-tunnel-paths"
                self._children_yang_names.add("bfd-tunnel-paths")

                self.bfd_circuits = BfdState.Sessions.Session.BfdCircuits()
                self.bfd_circuits.parent = self
                self._children_name_map["bfd_circuits"] = "bfd-circuits"
                self._children_yang_names.add("bfd-circuits")

                self.bfd_nbrs = BfdState.Sessions.Session.BfdNbrs()
                self.bfd_nbrs.parent = self
                self._children_name_map["bfd_nbrs"] = "bfd-nbrs"
                self._children_yang_names.add("bfd-nbrs")

                self.bfd_mhop_nbrs = BfdState.Sessions.Session.BfdMhopNbrs()
                self.bfd_mhop_nbrs.parent = self
                self._children_name_map["bfd_mhop_nbrs"] = "bfd-mhop-nbrs"
                self._children_yang_names.add("bfd-mhop-nbrs")

                self.bfd_mhop_vrf_nbrs = BfdState.Sessions.Session.BfdMhopVrfNbrs()
                self.bfd_mhop_vrf_nbrs.parent = self
                self._children_name_map["bfd_mhop_vrf_nbrs"] = "bfd-mhop-vrf-nbrs"
                self._children_yang_names.add("bfd-mhop-vrf-nbrs")
                self._segment_path = lambda: "session" + "[type='" + str(self.type) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-bfd-oper:bfd-state/sessions/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(BfdState.Sessions.Session, ['type'], name, value)


            class BfdTunnelPaths(Entity):
                """
                BFD tunnel path information
                
                .. attribute:: bfd_tunnel_path
                
                	List of BFD tunnel paths
                	**type**\: list of  		 :py:class:`BfdTunnelPath <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdTunnelPaths.BfdTunnelPath>`
                
                

                """

                _prefix = 'bfd-ios-xe-oper'
                _revision = '2017-09-10'

                def __init__(self):
                    super(BfdState.Sessions.Session.BfdTunnelPaths, self).__init__()

                    self.yang_name = "bfd-tunnel-paths"
                    self.yang_parent_name = "session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("bfd-tunnel-path", ("bfd_tunnel_path", BfdState.Sessions.Session.BfdTunnelPaths.BfdTunnelPath))])
                    self._leafs = OrderedDict()

                    self.bfd_tunnel_path = YList(self)
                    self._segment_path = lambda: "bfd-tunnel-paths"

                def __setattr__(self, name, value):
                    self._perform_setattr(BfdState.Sessions.Session.BfdTunnelPaths, [], name, value)


                class BfdTunnelPath(Entity):
                    """
                    List of BFD tunnel paths
                    
                    .. attribute:: interface  (key)
                    
                    	Associated interface
                    	**type**\: str
                    
                    .. attribute:: lsp_type  (key)
                    
                    	LSP type
                    	**type**\:  :py:class:`BfdLspType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdLspType>`
                    
                    .. attribute:: ld
                    
                    	Local discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rd
                    
                    	Remote discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: remote_state
                    
                    	Remote Heard. RH state of BFD version '0'  is also mapped to up/down
                    	**type**\:  :py:class:`BfdRemoteStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdRemoteStateType>`
                    
                    .. attribute:: state
                    
                    	BFD state
                    	**type**\:  :py:class:`BfdStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdStateType>`
                    
                    

                    """

                    _prefix = 'bfd-ios-xe-oper'
                    _revision = '2017-09-10'

                    def __init__(self):
                        super(BfdState.Sessions.Session.BfdTunnelPaths.BfdTunnelPath, self).__init__()

                        self.yang_name = "bfd-tunnel-path"
                        self.yang_parent_name = "bfd-tunnel-paths"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface','lsp_type']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface', YLeaf(YType.str, 'interface')),
                            ('lsp_type', YLeaf(YType.enumeration, 'lsp-type')),
                            ('ld', YLeaf(YType.uint32, 'ld')),
                            ('rd', YLeaf(YType.uint32, 'rd')),
                            ('remote_state', YLeaf(YType.enumeration, 'remote-state')),
                            ('state', YLeaf(YType.enumeration, 'state')),
                        ])
                        self.interface = None
                        self.lsp_type = None
                        self.ld = None
                        self.rd = None
                        self.remote_state = None
                        self.state = None
                        self._segment_path = lambda: "bfd-tunnel-path" + "[interface='" + str(self.interface) + "']" + "[lsp-type='" + str(self.lsp_type) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BfdState.Sessions.Session.BfdTunnelPaths.BfdTunnelPath, ['interface', 'lsp_type', 'ld', 'rd', 'remote_state', 'state'], name, value)


            class BfdCircuits(Entity):
                """
                BFD circuit information
                
                .. attribute:: bfd_circuit
                
                	List of BFD circuits
                	**type**\: list of  		 :py:class:`BfdCircuit <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdCircuits.BfdCircuit>`
                
                

                """

                _prefix = 'bfd-ios-xe-oper'
                _revision = '2017-09-10'

                def __init__(self):
                    super(BfdState.Sessions.Session.BfdCircuits, self).__init__()

                    self.yang_name = "bfd-circuits"
                    self.yang_parent_name = "session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("bfd-circuit", ("bfd_circuit", BfdState.Sessions.Session.BfdCircuits.BfdCircuit))])
                    self._leafs = OrderedDict()

                    self.bfd_circuit = YList(self)
                    self._segment_path = lambda: "bfd-circuits"

                def __setattr__(self, name, value):
                    self._perform_setattr(BfdState.Sessions.Session.BfdCircuits, [], name, value)


                class BfdCircuit(Entity):
                    """
                    List of BFD circuits
                    
                    .. attribute:: interface  (key)
                    
                    	Associated interface
                    	**type**\: str
                    
                    .. attribute:: vcid  (key)
                    
                    	Virtual circuit identifier
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ld
                    
                    	Local discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rd
                    
                    	Remote discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: remote_state
                    
                    	Remote Heard. RH state of BFD version '0'  is also mapped to up/down
                    	**type**\:  :py:class:`BfdRemoteStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdRemoteStateType>`
                    
                    .. attribute:: state
                    
                    	BFD state
                    	**type**\:  :py:class:`BfdStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdStateType>`
                    
                    

                    """

                    _prefix = 'bfd-ios-xe-oper'
                    _revision = '2017-09-10'

                    def __init__(self):
                        super(BfdState.Sessions.Session.BfdCircuits.BfdCircuit, self).__init__()

                        self.yang_name = "bfd-circuit"
                        self.yang_parent_name = "bfd-circuits"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface','vcid']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface', YLeaf(YType.str, 'interface')),
                            ('vcid', YLeaf(YType.uint32, 'vcid')),
                            ('ld', YLeaf(YType.uint32, 'ld')),
                            ('rd', YLeaf(YType.uint32, 'rd')),
                            ('remote_state', YLeaf(YType.enumeration, 'remote-state')),
                            ('state', YLeaf(YType.enumeration, 'state')),
                        ])
                        self.interface = None
                        self.vcid = None
                        self.ld = None
                        self.rd = None
                        self.remote_state = None
                        self.state = None
                        self._segment_path = lambda: "bfd-circuit" + "[interface='" + str(self.interface) + "']" + "[vcid='" + str(self.vcid) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BfdState.Sessions.Session.BfdCircuits.BfdCircuit, ['interface', 'vcid', 'ld', 'rd', 'remote_state', 'state'], name, value)


            class BfdNbrs(Entity):
                """
                BFD neighbor information
                
                .. attribute:: bfd_nbr
                
                	List of BFD neighbors
                	**type**\: list of  		 :py:class:`BfdNbr <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdNbrs.BfdNbr>`
                
                

                """

                _prefix = 'bfd-ios-xe-oper'
                _revision = '2017-09-10'

                def __init__(self):
                    super(BfdState.Sessions.Session.BfdNbrs, self).__init__()

                    self.yang_name = "bfd-nbrs"
                    self.yang_parent_name = "session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("bfd-nbr", ("bfd_nbr", BfdState.Sessions.Session.BfdNbrs.BfdNbr))])
                    self._leafs = OrderedDict()

                    self.bfd_nbr = YList(self)
                    self._segment_path = lambda: "bfd-nbrs"

                def __setattr__(self, name, value):
                    self._perform_setattr(BfdState.Sessions.Session.BfdNbrs, [], name, value)


                class BfdNbr(Entity):
                    """
                    List of BFD neighbors
                    
                    .. attribute:: ip  (key)
                    
                    	Neighbor IP address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: interface  (key)
                    
                    	Interface
                    	**type**\: str
                    
                    .. attribute:: ld
                    
                    	Local discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rd
                    
                    	Remote discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: remote_state
                    
                    	Remote Heard. RH state of BFD version '0'  is also mapped to up/down
                    	**type**\:  :py:class:`BfdRemoteStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdRemoteStateType>`
                    
                    .. attribute:: state
                    
                    	BFD state
                    	**type**\:  :py:class:`BfdStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdStateType>`
                    
                    

                    """

                    _prefix = 'bfd-ios-xe-oper'
                    _revision = '2017-09-10'

                    def __init__(self):
                        super(BfdState.Sessions.Session.BfdNbrs.BfdNbr, self).__init__()

                        self.yang_name = "bfd-nbr"
                        self.yang_parent_name = "bfd-nbrs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['ip','interface']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ip', YLeaf(YType.str, 'ip')),
                            ('interface', YLeaf(YType.str, 'interface')),
                            ('ld', YLeaf(YType.uint32, 'ld')),
                            ('rd', YLeaf(YType.uint32, 'rd')),
                            ('remote_state', YLeaf(YType.enumeration, 'remote-state')),
                            ('state', YLeaf(YType.enumeration, 'state')),
                        ])
                        self.ip = None
                        self.interface = None
                        self.ld = None
                        self.rd = None
                        self.remote_state = None
                        self.state = None
                        self._segment_path = lambda: "bfd-nbr" + "[ip='" + str(self.ip) + "']" + "[interface='" + str(self.interface) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BfdState.Sessions.Session.BfdNbrs.BfdNbr, ['ip', 'interface', 'ld', 'rd', 'remote_state', 'state'], name, value)


            class BfdMhopNbrs(Entity):
                """
                Multi hop neighbors for multi hop neighbor scenario 
                for global VRF (no VRF)
                
                .. attribute:: bfd_mhop_nbr
                
                	List of MHOP neighbors
                	**type**\: list of  		 :py:class:`BfdMhopNbr <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdMhopNbrs.BfdMhopNbr>`
                
                

                """

                _prefix = 'bfd-ios-xe-oper'
                _revision = '2017-09-10'

                def __init__(self):
                    super(BfdState.Sessions.Session.BfdMhopNbrs, self).__init__()

                    self.yang_name = "bfd-mhop-nbrs"
                    self.yang_parent_name = "session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("bfd-mhop-nbr", ("bfd_mhop_nbr", BfdState.Sessions.Session.BfdMhopNbrs.BfdMhopNbr))])
                    self._leafs = OrderedDict()

                    self.bfd_mhop_nbr = YList(self)
                    self._segment_path = lambda: "bfd-mhop-nbrs"

                def __setattr__(self, name, value):
                    self._perform_setattr(BfdState.Sessions.Session.BfdMhopNbrs, [], name, value)


                class BfdMhopNbr(Entity):
                    """
                    List of MHOP neighbors
                    
                    .. attribute:: ip  (key)
                    
                    	Neighbor IP address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: src_ip  (key)
                    
                    	Source IP address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ld
                    
                    	Local discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rd
                    
                    	Remote discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: remote_state
                    
                    	Remote Heard. RH state of BFD version '0'  is also mapped to up/down
                    	**type**\:  :py:class:`BfdRemoteStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdRemoteStateType>`
                    
                    .. attribute:: state
                    
                    	BFD state
                    	**type**\:  :py:class:`BfdStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdStateType>`
                    
                    

                    """

                    _prefix = 'bfd-ios-xe-oper'
                    _revision = '2017-09-10'

                    def __init__(self):
                        super(BfdState.Sessions.Session.BfdMhopNbrs.BfdMhopNbr, self).__init__()

                        self.yang_name = "bfd-mhop-nbr"
                        self.yang_parent_name = "bfd-mhop-nbrs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['ip','src_ip']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ip', YLeaf(YType.str, 'ip')),
                            ('src_ip', YLeaf(YType.str, 'src-ip')),
                            ('ld', YLeaf(YType.uint32, 'ld')),
                            ('rd', YLeaf(YType.uint32, 'rd')),
                            ('remote_state', YLeaf(YType.enumeration, 'remote-state')),
                            ('state', YLeaf(YType.enumeration, 'state')),
                        ])
                        self.ip = None
                        self.src_ip = None
                        self.ld = None
                        self.rd = None
                        self.remote_state = None
                        self.state = None
                        self._segment_path = lambda: "bfd-mhop-nbr" + "[ip='" + str(self.ip) + "']" + "[src-ip='" + str(self.src_ip) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BfdState.Sessions.Session.BfdMhopNbrs.BfdMhopNbr, ['ip', 'src_ip', 'ld', 'rd', 'remote_state', 'state'], name, value)


            class BfdMhopVrfNbrs(Entity):
                """
                Multi hop neighbors for multi hop neighbor scenario
                with non\-global VRF
                
                .. attribute:: bfd_mhop_vrf_nbr
                
                	List of multi hop neighbors
                	**type**\: list of  		 :py:class:`BfdMhopVrfNbr <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdMhopVrfNbrs.BfdMhopVrfNbr>`
                
                

                """

                _prefix = 'bfd-ios-xe-oper'
                _revision = '2017-09-10'

                def __init__(self):
                    super(BfdState.Sessions.Session.BfdMhopVrfNbrs, self).__init__()

                    self.yang_name = "bfd-mhop-vrf-nbrs"
                    self.yang_parent_name = "session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("bfd-mhop-vrf-nbr", ("bfd_mhop_vrf_nbr", BfdState.Sessions.Session.BfdMhopVrfNbrs.BfdMhopVrfNbr))])
                    self._leafs = OrderedDict()

                    self.bfd_mhop_vrf_nbr = YList(self)
                    self._segment_path = lambda: "bfd-mhop-vrf-nbrs"

                def __setattr__(self, name, value):
                    self._perform_setattr(BfdState.Sessions.Session.BfdMhopVrfNbrs, [], name, value)


                class BfdMhopVrfNbr(Entity):
                    """
                    List of multi hop neighbors
                    
                    .. attribute:: ip  (key)
                    
                    	Neighbor IP address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: vrf  (key)
                    
                    	Neighbor VFR
                    	**type**\: str
                    
                    .. attribute:: src_ip  (key)
                    
                    	Source IP address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ld
                    
                    	Local discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rd
                    
                    	Remote discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: remote_state
                    
                    	Remote Heard. RH state of BFD version '0'  is also mapped to up/down
                    	**type**\:  :py:class:`BfdRemoteStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdRemoteStateType>`
                    
                    .. attribute:: state
                    
                    	BFD state
                    	**type**\:  :py:class:`BfdStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdStateType>`
                    
                    

                    """

                    _prefix = 'bfd-ios-xe-oper'
                    _revision = '2017-09-10'

                    def __init__(self):
                        super(BfdState.Sessions.Session.BfdMhopVrfNbrs.BfdMhopVrfNbr, self).__init__()

                        self.yang_name = "bfd-mhop-vrf-nbr"
                        self.yang_parent_name = "bfd-mhop-vrf-nbrs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['ip','vrf','src_ip']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ip', YLeaf(YType.str, 'ip')),
                            ('vrf', YLeaf(YType.str, 'vrf')),
                            ('src_ip', YLeaf(YType.str, 'src-ip')),
                            ('ld', YLeaf(YType.uint32, 'ld')),
                            ('rd', YLeaf(YType.uint32, 'rd')),
                            ('remote_state', YLeaf(YType.enumeration, 'remote-state')),
                            ('state', YLeaf(YType.enumeration, 'state')),
                        ])
                        self.ip = None
                        self.vrf = None
                        self.src_ip = None
                        self.ld = None
                        self.rd = None
                        self.remote_state = None
                        self.state = None
                        self._segment_path = lambda: "bfd-mhop-vrf-nbr" + "[ip='" + str(self.ip) + "']" + "[vrf='" + str(self.vrf) + "']" + "[src-ip='" + str(self.src_ip) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BfdState.Sessions.Session.BfdMhopVrfNbrs.BfdMhopVrfNbr, ['ip', 'vrf', 'src_ip', 'ld', 'rd', 'remote_state', 'state'], name, value)

    def clone_ptr(self):
        self._top_entity = BfdState()
        return self._top_entity


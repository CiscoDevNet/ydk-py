""" Cisco_IOS_XE_bfd_oper 

This module contains a collection of YANG definitions for
monitoring BFD neighbours.Copyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class BfdLspType(Enum):
    """
    BfdLspType

    BFD lsp type

    .. data:: working = 0

    .. data:: protect = 1

    .. data:: unknown = 2

    """

    working = Enum.YLeaf(0, "working")

    protect = Enum.YLeaf(1, "protect")

    unknown = Enum.YLeaf(2, "unknown")


class BfdOperSessionType(Enum):
    """
    BfdOperSessionType

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
    BfdRemoteStateType

    BFD remote state type

    .. data:: up = 0

    .. data:: down = 1

    .. data:: init = 2

    .. data:: admindown = 3

    .. data:: invalid = 4

    """

    up = Enum.YLeaf(0, "up")

    down = Enum.YLeaf(1, "down")

    init = Enum.YLeaf(2, "init")

    admindown = Enum.YLeaf(3, "admindown")

    invalid = Enum.YLeaf(4, "invalid")


class BfdStateType(Enum):
    """
    BfdStateType

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
    Data nodes for BFD neighbors.
    
    .. attribute:: sessions
    
    	
    	**type**\:  :py:class:`Sessions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions>`
    
    

    """

    _prefix = 'bfd-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(BfdState, self).__init__()
        self._top_entity = None

        self.yang_name = "bfd-state"
        self.yang_parent_name = "Cisco-IOS-XE-bfd-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"sessions" : ("sessions", BfdState.Sessions)}
        self._child_list_classes = {}

        self.sessions = BfdState.Sessions()
        self.sessions.parent = self
        self._children_name_map["sessions"] = "sessions"
        self._children_yang_names.add("sessions")
        self._segment_path = lambda: "Cisco-IOS-XE-bfd-oper:bfd-state"


    class Sessions(Entity):
        """
        
        
        .. attribute:: session
        
        	
        	**type**\: list of  		 :py:class:`Session <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session>`
        
        

        """

        _prefix = 'bfd-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(BfdState.Sessions, self).__init__()

            self.yang_name = "sessions"
            self.yang_parent_name = "bfd-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"session" : ("session", BfdState.Sessions.Session)}

            self.session = YList(self)
            self._segment_path = lambda: "sessions"
            self._absolute_path = lambda: "Cisco-IOS-XE-bfd-oper:bfd-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BfdState.Sessions, [], name, value)


        class Session(Entity):
            """
            
            
            .. attribute:: type  <key>
            
            	Session type
            	**type**\:  :py:class:`BfdOperSessionType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdOperSessionType>`
            
            .. attribute:: bfd_tunnel_paths
            
            	
            	**type**\:  :py:class:`BfdTunnelPaths <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdTunnelPaths>`
            
            .. attribute:: bfd_circuits
            
            	
            	**type**\:  :py:class:`BfdCircuits <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdCircuits>`
            
            .. attribute:: bfd_nbrs
            
            	
            	**type**\:  :py:class:`BfdNbrs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdNbrs>`
            
            .. attribute:: bfd_mhop_nbrs
            
            	
            	**type**\:  :py:class:`BfdMhopNbrs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdMhopNbrs>`
            
            .. attribute:: bfd_mhop_vrf_nbrs
            
            	
            	**type**\:  :py:class:`BfdMhopVrfNbrs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdMhopVrfNbrs>`
            
            

            """

            _prefix = 'bfd-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(BfdState.Sessions.Session, self).__init__()

                self.yang_name = "session"
                self.yang_parent_name = "sessions"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"bfd-tunnel-paths" : ("bfd_tunnel_paths", BfdState.Sessions.Session.BfdTunnelPaths), "bfd-circuits" : ("bfd_circuits", BfdState.Sessions.Session.BfdCircuits), "bfd-nbrs" : ("bfd_nbrs", BfdState.Sessions.Session.BfdNbrs), "bfd-mhop-nbrs" : ("bfd_mhop_nbrs", BfdState.Sessions.Session.BfdMhopNbrs), "bfd-mhop-vrf-nbrs" : ("bfd_mhop_vrf_nbrs", BfdState.Sessions.Session.BfdMhopVrfNbrs)}
                self._child_list_classes = {}

                self.type = YLeaf(YType.enumeration, "type")

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
                self._segment_path = lambda: "session" + "[type='" + self.type.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-bfd-oper:bfd-state/sessions/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(BfdState.Sessions.Session, ['type'], name, value)


            class BfdTunnelPaths(Entity):
                """
                
                
                .. attribute:: bfd_tunnel_path
                
                	Tunnel Path
                	**type**\: list of  		 :py:class:`BfdTunnelPath <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdTunnelPaths.BfdTunnelPath>`
                
                

                """

                _prefix = 'bfd-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(BfdState.Sessions.Session.BfdTunnelPaths, self).__init__()

                    self.yang_name = "bfd-tunnel-paths"
                    self.yang_parent_name = "session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"bfd-tunnel-path" : ("bfd_tunnel_path", BfdState.Sessions.Session.BfdTunnelPaths.BfdTunnelPath)}

                    self.bfd_tunnel_path = YList(self)
                    self._segment_path = lambda: "bfd-tunnel-paths"

                def __setattr__(self, name, value):
                    self._perform_setattr(BfdState.Sessions.Session.BfdTunnelPaths, [], name, value)


                class BfdTunnelPath(Entity):
                    """
                    Tunnel Path
                    
                    .. attribute:: interface  <key>
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: lsp_type  <key>
                    
                    	
                    	**type**\:  :py:class:`BfdLspType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdLspType>`
                    
                    .. attribute:: ld
                    
                    	local\-discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rd
                    
                    	remote\-discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: remote_state
                    
                    	 Remote Heard. RH state of BFD version '0'   is also mapped to up/down. 
                    	**type**\:  :py:class:`BfdRemoteStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdRemoteStateType>`
                    
                    .. attribute:: state
                    
                    	BFD state
                    	**type**\:  :py:class:`BfdStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdStateType>`
                    
                    

                    """

                    _prefix = 'bfd-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(BfdState.Sessions.Session.BfdTunnelPaths.BfdTunnelPath, self).__init__()

                        self.yang_name = "bfd-tunnel-path"
                        self.yang_parent_name = "bfd-tunnel-paths"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.interface = YLeaf(YType.str, "interface")

                        self.lsp_type = YLeaf(YType.enumeration, "lsp-type")

                        self.ld = YLeaf(YType.uint32, "ld")

                        self.rd = YLeaf(YType.uint32, "rd")

                        self.remote_state = YLeaf(YType.enumeration, "remote-state")

                        self.state = YLeaf(YType.enumeration, "state")
                        self._segment_path = lambda: "bfd-tunnel-path" + "[interface='" + self.interface.get() + "']" + "[lsp-type='" + self.lsp_type.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BfdState.Sessions.Session.BfdTunnelPaths.BfdTunnelPath, ['interface', 'lsp_type', 'ld', 'rd', 'remote_state', 'state'], name, value)


            class BfdCircuits(Entity):
                """
                
                
                .. attribute:: bfd_circuit
                
                	BFD circuit
                	**type**\: list of  		 :py:class:`BfdCircuit <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdCircuits.BfdCircuit>`
                
                

                """

                _prefix = 'bfd-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(BfdState.Sessions.Session.BfdCircuits, self).__init__()

                    self.yang_name = "bfd-circuits"
                    self.yang_parent_name = "session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"bfd-circuit" : ("bfd_circuit", BfdState.Sessions.Session.BfdCircuits.BfdCircuit)}

                    self.bfd_circuit = YList(self)
                    self._segment_path = lambda: "bfd-circuits"

                def __setattr__(self, name, value):
                    self._perform_setattr(BfdState.Sessions.Session.BfdCircuits, [], name, value)


                class BfdCircuit(Entity):
                    """
                    BFD circuit
                    
                    .. attribute:: interface  <key>
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: vcid  <key>
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ld
                    
                    	local\-discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rd
                    
                    	remote\-discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: remote_state
                    
                    	 Remote Heard. RH state of BFD version '0'   is also mapped to up/down. 
                    	**type**\:  :py:class:`BfdRemoteStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdRemoteStateType>`
                    
                    .. attribute:: state
                    
                    	BFD state
                    	**type**\:  :py:class:`BfdStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdStateType>`
                    
                    

                    """

                    _prefix = 'bfd-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(BfdState.Sessions.Session.BfdCircuits.BfdCircuit, self).__init__()

                        self.yang_name = "bfd-circuit"
                        self.yang_parent_name = "bfd-circuits"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.interface = YLeaf(YType.str, "interface")

                        self.vcid = YLeaf(YType.uint32, "vcid")

                        self.ld = YLeaf(YType.uint32, "ld")

                        self.rd = YLeaf(YType.uint32, "rd")

                        self.remote_state = YLeaf(YType.enumeration, "remote-state")

                        self.state = YLeaf(YType.enumeration, "state")
                        self._segment_path = lambda: "bfd-circuit" + "[interface='" + self.interface.get() + "']" + "[vcid='" + self.vcid.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BfdState.Sessions.Session.BfdCircuits.BfdCircuit, ['interface', 'vcid', 'ld', 'rd', 'remote_state', 'state'], name, value)


            class BfdNbrs(Entity):
                """
                
                
                .. attribute:: bfd_nbr
                
                	This is for directly connected neighbor case
                	**type**\: list of  		 :py:class:`BfdNbr <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdNbrs.BfdNbr>`
                
                

                """

                _prefix = 'bfd-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(BfdState.Sessions.Session.BfdNbrs, self).__init__()

                    self.yang_name = "bfd-nbrs"
                    self.yang_parent_name = "session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"bfd-nbr" : ("bfd_nbr", BfdState.Sessions.Session.BfdNbrs.BfdNbr)}

                    self.bfd_nbr = YList(self)
                    self._segment_path = lambda: "bfd-nbrs"

                def __setattr__(self, name, value):
                    self._perform_setattr(BfdState.Sessions.Session.BfdNbrs, [], name, value)


                class BfdNbr(Entity):
                    """
                    This is for directly connected neighbor case
                    
                    .. attribute:: ip  <key>
                    
                    	
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: interface  <key>
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: ld
                    
                    	local\-discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rd
                    
                    	remote\-discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: remote_state
                    
                    	 Remote Heard. RH state of BFD version '0'   is also mapped to up/down. 
                    	**type**\:  :py:class:`BfdRemoteStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdRemoteStateType>`
                    
                    .. attribute:: state
                    
                    	BFD state
                    	**type**\:  :py:class:`BfdStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdStateType>`
                    
                    

                    """

                    _prefix = 'bfd-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(BfdState.Sessions.Session.BfdNbrs.BfdNbr, self).__init__()

                        self.yang_name = "bfd-nbr"
                        self.yang_parent_name = "bfd-nbrs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.ip = YLeaf(YType.str, "ip")

                        self.interface = YLeaf(YType.str, "interface")

                        self.ld = YLeaf(YType.uint32, "ld")

                        self.rd = YLeaf(YType.uint32, "rd")

                        self.remote_state = YLeaf(YType.enumeration, "remote-state")

                        self.state = YLeaf(YType.enumeration, "state")
                        self._segment_path = lambda: "bfd-nbr" + "[ip='" + self.ip.get() + "']" + "[interface='" + self.interface.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BfdState.Sessions.Session.BfdNbrs.BfdNbr, ['ip', 'interface', 'ld', 'rd', 'remote_state', 'state'], name, value)


            class BfdMhopNbrs(Entity):
                """
                
                
                .. attribute:: bfd_mhop_nbr
                
                	This is for multi hop neighbor scenario  for global VRF (no VRF)
                	**type**\: list of  		 :py:class:`BfdMhopNbr <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdMhopNbrs.BfdMhopNbr>`
                
                

                """

                _prefix = 'bfd-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(BfdState.Sessions.Session.BfdMhopNbrs, self).__init__()

                    self.yang_name = "bfd-mhop-nbrs"
                    self.yang_parent_name = "session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"bfd-mhop-nbr" : ("bfd_mhop_nbr", BfdState.Sessions.Session.BfdMhopNbrs.BfdMhopNbr)}

                    self.bfd_mhop_nbr = YList(self)
                    self._segment_path = lambda: "bfd-mhop-nbrs"

                def __setattr__(self, name, value):
                    self._perform_setattr(BfdState.Sessions.Session.BfdMhopNbrs, [], name, value)


                class BfdMhopNbr(Entity):
                    """
                    This is for multi hop neighbor scenario 
                    for global VRF (no VRF).
                    
                    .. attribute:: ip  <key>
                    
                    	
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ld
                    
                    	local\-discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rd
                    
                    	remote\-discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: remote_state
                    
                    	 Remote Heard. RH state of BFD version '0'   is also mapped to up/down. 
                    	**type**\:  :py:class:`BfdRemoteStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdRemoteStateType>`
                    
                    .. attribute:: state
                    
                    	BFD state
                    	**type**\:  :py:class:`BfdStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdStateType>`
                    
                    

                    """

                    _prefix = 'bfd-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(BfdState.Sessions.Session.BfdMhopNbrs.BfdMhopNbr, self).__init__()

                        self.yang_name = "bfd-mhop-nbr"
                        self.yang_parent_name = "bfd-mhop-nbrs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.ip = YLeaf(YType.str, "ip")

                        self.ld = YLeaf(YType.uint32, "ld")

                        self.rd = YLeaf(YType.uint32, "rd")

                        self.remote_state = YLeaf(YType.enumeration, "remote-state")

                        self.state = YLeaf(YType.enumeration, "state")
                        self._segment_path = lambda: "bfd-mhop-nbr" + "[ip='" + self.ip.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BfdState.Sessions.Session.BfdMhopNbrs.BfdMhopNbr, ['ip', 'ld', 'rd', 'remote_state', 'state'], name, value)


            class BfdMhopVrfNbrs(Entity):
                """
                
                
                .. attribute:: bfd_mhop_vrf_nbr
                
                	This is for multi hop neighbor scenario  for non\-global VRF
                	**type**\: list of  		 :py:class:`BfdMhopVrfNbr <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdMhopVrfNbrs.BfdMhopVrfNbr>`
                
                

                """

                _prefix = 'bfd-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(BfdState.Sessions.Session.BfdMhopVrfNbrs, self).__init__()

                    self.yang_name = "bfd-mhop-vrf-nbrs"
                    self.yang_parent_name = "session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"bfd-mhop-vrf-nbr" : ("bfd_mhop_vrf_nbr", BfdState.Sessions.Session.BfdMhopVrfNbrs.BfdMhopVrfNbr)}

                    self.bfd_mhop_vrf_nbr = YList(self)
                    self._segment_path = lambda: "bfd-mhop-vrf-nbrs"

                def __setattr__(self, name, value):
                    self._perform_setattr(BfdState.Sessions.Session.BfdMhopVrfNbrs, [], name, value)


                class BfdMhopVrfNbr(Entity):
                    """
                    This is for multi hop neighbor scenario 
                    for non\-global VRF.
                    
                    .. attribute:: ip  <key>
                    
                    	
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: vrf  <key>
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: ld
                    
                    	local\-discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rd
                    
                    	remote\-discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: remote_state
                    
                    	 Remote Heard. RH state of BFD version '0'   is also mapped to up/down. 
                    	**type**\:  :py:class:`BfdRemoteStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdRemoteStateType>`
                    
                    .. attribute:: state
                    
                    	BFD state
                    	**type**\:  :py:class:`BfdStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdStateType>`
                    
                    

                    """

                    _prefix = 'bfd-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(BfdState.Sessions.Session.BfdMhopVrfNbrs.BfdMhopVrfNbr, self).__init__()

                        self.yang_name = "bfd-mhop-vrf-nbr"
                        self.yang_parent_name = "bfd-mhop-vrf-nbrs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.ip = YLeaf(YType.str, "ip")

                        self.vrf = YLeaf(YType.str, "vrf")

                        self.ld = YLeaf(YType.uint32, "ld")

                        self.rd = YLeaf(YType.uint32, "rd")

                        self.remote_state = YLeaf(YType.enumeration, "remote-state")

                        self.state = YLeaf(YType.enumeration, "state")
                        self._segment_path = lambda: "bfd-mhop-vrf-nbr" + "[ip='" + self.ip.get() + "']" + "[vrf='" + self.vrf.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BfdState.Sessions.Session.BfdMhopVrfNbrs.BfdMhopVrfNbr, ['ip', 'vrf', 'ld', 'rd', 'remote_state', 'state'], name, value)

    def clone_ptr(self):
        self._top_entity = BfdState()
        return self._top_entity


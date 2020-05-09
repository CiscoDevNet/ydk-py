""" openconfig_bfd 

An OpenConfig model of Bi\-Directional Forwarding Detection (BFD)
configuration and operational state.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class BfdDiagnosticCode(Enum):
    """
    BfdDiagnosticCode (Enum Class)

    Diagnostic codes defined by BFD. These typically indicate the

    reason for a change of session state.

    .. data:: NO_DIAGNOSTIC = 0

    	No diagnostic code was specified, or the session has not

    	changed state.

    .. data:: DETECTION_TIMEOUT = 1

    	The control detection time expired: no BFD packet was

    	received within the required period.

    .. data:: ECHO_FAILED = 2

    	The BFD echo function failed - echo packets have not been

    	received for the required period of time.

    .. data:: FORWARDING_RESET = 3

    	The forwarding plane in the local system was reset - such

    	that the remote system cannot rely on the forwarding state of

    	the device specifying this error code.

    .. data:: PATH_DOWN = 4

    	Signalling outside of BFD specified that the path underlying

    	this session has failed.

    .. data:: CONCATENATED_PATH_DOWN = 5

    	When a BFD session runs over a series of path segments, this

    	error code indicates that a subsequent path segment (i.e.,

    	one in the transmit path between the source and destination

    	of the session) has failed.

    .. data:: ADMIN_DOWN = 6

    	The BFD session has been administratively disabled by the

    	peer.

    .. data:: REVERSE_CONCATENATED_PATH_DOWN = 7

    	In the case that a BFD session is running over a series of

    	path segments, this error code indicates that a path segment

    	on the reverse path (i.e., in the transmit direction from the

    	destination to the source of the session) has failed.

    """

    NO_DIAGNOSTIC = Enum.YLeaf(0, "NO_DIAGNOSTIC")

    DETECTION_TIMEOUT = Enum.YLeaf(1, "DETECTION_TIMEOUT")

    ECHO_FAILED = Enum.YLeaf(2, "ECHO_FAILED")

    FORWARDING_RESET = Enum.YLeaf(3, "FORWARDING_RESET")

    PATH_DOWN = Enum.YLeaf(4, "PATH_DOWN")

    CONCATENATED_PATH_DOWN = Enum.YLeaf(5, "CONCATENATED_PATH_DOWN")

    ADMIN_DOWN = Enum.YLeaf(6, "ADMIN_DOWN")

    REVERSE_CONCATENATED_PATH_DOWN = Enum.YLeaf(7, "REVERSE_CONCATENATED_PATH_DOWN")


class BfdSessionState(Enum):
    """
    BfdSessionState (Enum Class)

    The state of the BFD session according to the system referred

    to by the context of the leaf.

    .. data:: UP = 0

    	The BFD session is perceived to be up by the system.

    .. data:: DOWN = 1

    	The BFD session is perceived to be down by the system.

    .. data:: ADMIN_DOWN = 2

    	The BFD session is administratively disabled.

    .. data:: INIT = 3

    	The BFD session is perceived to be initialising by the

    	system.

    """

    UP = Enum.YLeaf(0, "UP")

    DOWN = Enum.YLeaf(1, "DOWN")

    ADMIN_DOWN = Enum.YLeaf(2, "ADMIN_DOWN")

    INIT = Enum.YLeaf(3, "INIT")



class Bfd(_Entity_):
    """
    Configuration and operational state parameters for BFD.
    
    .. attribute:: interfaces
    
    	Interfaces on which BFD sessions are to be enabled
    	**type**\:  :py:class:`Interfaces <ydk.models.openconfig.openconfig_bfd.Bfd.Interfaces>`
    
    

    """

    _prefix = 'oc-bfd'
    _revision = '2018-11-21'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Bfd, self).__init__()
        self._top_entity = None

        self.yang_name = "bfd"
        self.yang_parent_name = "openconfig-bfd"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("interfaces", ("interfaces", Bfd.Interfaces))])
        self._leafs = OrderedDict()

        self.interfaces = Bfd.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._segment_path = lambda: "openconfig-bfd:bfd"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Bfd, [], name, value)


    class Interfaces(_Entity_):
        """
        Interfaces on which BFD sessions are to be enabled.
        
        .. attribute:: interface
        
        	Per\-interface configuration and state parameters for BFD
        	**type**\: list of  		 :py:class:`Interface <ydk.models.openconfig.openconfig_bfd.Bfd.Interfaces.Interface>`
        
        

        """

        _prefix = 'oc-bfd'
        _revision = '2018-11-21'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Bfd.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "bfd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface", ("interface", Bfd.Interfaces.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "openconfig-bfd:bfd/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Bfd.Interfaces, [], name, value)


        class Interface(_Entity_):
            """
            Per\-interface configuration and state parameters for BFD.
            
            .. attribute:: id  (key)
            
            	A reference to an identifier for the interface on which BFD is enabled
            	**type**\: str
            
            	**refers to**\:  :py:class:`id <ydk.models.openconfig.openconfig_bfd.Bfd.Interfaces.Interface.Config>`
            
            .. attribute:: config
            
            	Configuration parameters for BFD on the specified interface
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bfd.Bfd.Interfaces.Interface.Config>`
            
            .. attribute:: state
            
            	Operational state parameters for BFD on the specified interface
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bfd.Bfd.Interfaces.Interface.State>`
            
            	**config**\: False
            
            .. attribute:: interface_ref
            
            	Reference to an interface or subinterface
            	**type**\:  :py:class:`InterfaceRef <ydk.models.openconfig.openconfig_bfd.Bfd.Interfaces.Interface.InterfaceRef>`
            
            .. attribute:: micro_bfd_sessions
            
            	Parameters relating to micro\-BFD sessions associated with the interface
            	**type**\:  :py:class:`MicroBfdSessions <ydk.models.openconfig.openconfig_bfd.Bfd.Interfaces.Interface.MicroBfdSessions>`
            
            .. attribute:: peers
            
            	Parameters relating to the BFD peers which are seen over this interface
            	**type**\:  :py:class:`Peers <ydk.models.openconfig.openconfig_bfd.Bfd.Interfaces.Interface.Peers>`
            
            

            """

            _prefix = 'oc-bfd'
            _revision = '2018-11-21'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Bfd.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['id']
                self._child_classes = OrderedDict([("config", ("config", Bfd.Interfaces.Interface.Config)), ("state", ("state", Bfd.Interfaces.Interface.State)), ("interface-ref", ("interface_ref", Bfd.Interfaces.Interface.InterfaceRef)), ("micro-bfd-sessions", ("micro_bfd_sessions", Bfd.Interfaces.Interface.MicroBfdSessions)), ("peers", ("peers", Bfd.Interfaces.Interface.Peers))])
                self._leafs = OrderedDict([
                    ('id', (YLeaf(YType.str, 'id'), ['str'])),
                ])
                self.id = None

                self.config = Bfd.Interfaces.Interface.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = Bfd.Interfaces.Interface.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"

                self.interface_ref = Bfd.Interfaces.Interface.InterfaceRef()
                self.interface_ref.parent = self
                self._children_name_map["interface_ref"] = "interface-ref"

                self.micro_bfd_sessions = Bfd.Interfaces.Interface.MicroBfdSessions()
                self.micro_bfd_sessions.parent = self
                self._children_name_map["micro_bfd_sessions"] = "micro-bfd-sessions"

                self.peers = Bfd.Interfaces.Interface.Peers()
                self.peers.parent = self
                self._children_name_map["peers"] = "peers"
                self._segment_path = lambda: "interface" + "[id='" + str(self.id) + "']"
                self._absolute_path = lambda: "openconfig-bfd:bfd/interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Bfd.Interfaces.Interface, ['id'], name, value)


            class Config(_Entity_):
                """
                Configuration parameters for BFD on the specified
                interface.
                
                .. attribute:: id
                
                	A unique identifier for the interface
                	**type**\: str
                
                .. attribute:: enabled
                
                	When this leaf is set to true then the BFD session is enabled on the specified interface \- if it is set to false, it is administratively disabled
                	**type**\: bool
                
                .. attribute:: local_address
                
                	The source IP address to be used for BFD sessions over this interface
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                
                		**type**\: str
                
                			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                
                .. attribute:: desired_minimum_tx_interval
                
                	The minimum interval between transmission of BFD control packets that the operator desires. This value is advertised to the peer, however the actual interval used is specified by taking the maximum of desired\-minimum\-tx\-interval and the value of the remote required\-minimum\-receive interval value.  This value is specified as an integer number of microseconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: microseconds
                
                .. attribute:: required_minimum_receive
                
                	The minimum interval between received BFD control packets that this system should support. This value is advertised to the remote peer to indicate the maximum frequency (i.e., minimum inter\-packet interval) between BFD control packets that is acceptable to the local system
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: microseconds
                
                .. attribute:: detection_multiplier
                
                	The number of packets that must be missed to declare this session as down. The detection interval for the BFD session is calculated by multiplying the value of the negotiated transmission interval by this value
                	**type**\: int
                
                	**range:** 1..65535
                
                .. attribute:: enable_per_member_link
                
                	When this leaf is set to true \- BFD will be enabled on each member interface of the aggregated Ethernet bundle
                	**type**\: bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'oc-bfd'
                _revision = '2018-11-21'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Bfd.Interfaces.Interface.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('id', (YLeaf(YType.str, 'id'), ['str'])),
                        ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                        ('local_address', (YLeaf(YType.str, 'local-address'), ['str','str'])),
                        ('desired_minimum_tx_interval', (YLeaf(YType.uint32, 'desired-minimum-tx-interval'), ['int'])),
                        ('required_minimum_receive', (YLeaf(YType.uint32, 'required-minimum-receive'), ['int'])),
                        ('detection_multiplier', (YLeaf(YType.uint16, 'detection-multiplier'), ['int'])),
                        ('enable_per_member_link', (YLeaf(YType.boolean, 'enable-per-member-link'), ['bool'])),
                    ])
                    self.id = None
                    self.enabled = None
                    self.local_address = None
                    self.desired_minimum_tx_interval = None
                    self.required_minimum_receive = None
                    self.detection_multiplier = None
                    self.enable_per_member_link = None
                    self._segment_path = lambda: "config"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Bfd.Interfaces.Interface.Config, ['id', 'enabled', 'local_address', 'desired_minimum_tx_interval', 'required_minimum_receive', 'detection_multiplier', 'enable_per_member_link'], name, value)



            class State(_Entity_):
                """
                Operational state parameters for BFD on the specified
                interface.
                
                .. attribute:: id
                
                	A unique identifier for the interface
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: enabled
                
                	When this leaf is set to true then the BFD session is enabled on the specified interface \- if it is set to false, it is administratively disabled
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: local_address
                
                	The source IP address to be used for BFD sessions over this interface
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                
                		**type**\: str
                
                			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                
                	**config**\: False
                
                .. attribute:: desired_minimum_tx_interval
                
                	The minimum interval between transmission of BFD control packets that the operator desires. This value is advertised to the peer, however the actual interval used is specified by taking the maximum of desired\-minimum\-tx\-interval and the value of the remote required\-minimum\-receive interval value.  This value is specified as an integer number of microseconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                	**units**\: microseconds
                
                .. attribute:: required_minimum_receive
                
                	The minimum interval between received BFD control packets that this system should support. This value is advertised to the remote peer to indicate the maximum frequency (i.e., minimum inter\-packet interval) between BFD control packets that is acceptable to the local system
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                	**units**\: microseconds
                
                .. attribute:: detection_multiplier
                
                	The number of packets that must be missed to declare this session as down. The detection interval for the BFD session is calculated by multiplying the value of the negotiated transmission interval by this value
                	**type**\: int
                
                	**range:** 1..65535
                
                	**config**\: False
                
                .. attribute:: enable_per_member_link
                
                	When this leaf is set to true \- BFD will be enabled on each member interface of the aggregated Ethernet bundle
                	**type**\: bool
                
                	**config**\: False
                
                	**default value**\: false
                
                

                """

                _prefix = 'oc-bfd'
                _revision = '2018-11-21'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Bfd.Interfaces.Interface.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('id', (YLeaf(YType.str, 'id'), ['str'])),
                        ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                        ('local_address', (YLeaf(YType.str, 'local-address'), ['str','str'])),
                        ('desired_minimum_tx_interval', (YLeaf(YType.uint32, 'desired-minimum-tx-interval'), ['int'])),
                        ('required_minimum_receive', (YLeaf(YType.uint32, 'required-minimum-receive'), ['int'])),
                        ('detection_multiplier', (YLeaf(YType.uint16, 'detection-multiplier'), ['int'])),
                        ('enable_per_member_link', (YLeaf(YType.boolean, 'enable-per-member-link'), ['bool'])),
                    ])
                    self.id = None
                    self.enabled = None
                    self.local_address = None
                    self.desired_minimum_tx_interval = None
                    self.required_minimum_receive = None
                    self.detection_multiplier = None
                    self.enable_per_member_link = None
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Bfd.Interfaces.Interface.State, ['id', 'enabled', 'local_address', 'desired_minimum_tx_interval', 'required_minimum_receive', 'detection_multiplier', 'enable_per_member_link'], name, value)



            class InterfaceRef(_Entity_):
                """
                Reference to an interface or subinterface
                
                .. attribute:: config
                
                	Configured reference to interface / subinterface
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bfd.Bfd.Interfaces.Interface.InterfaceRef.Config>`
                
                .. attribute:: state
                
                	Operational state for interface\-ref
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bfd.Bfd.Interfaces.Interface.InterfaceRef.State>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-bfd'
                _revision = '2018-11-21'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Bfd.Interfaces.Interface.InterfaceRef, self).__init__()

                    self.yang_name = "interface-ref"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("config", ("config", Bfd.Interfaces.Interface.InterfaceRef.Config)), ("state", ("state", Bfd.Interfaces.Interface.InterfaceRef.State))])
                    self._leafs = OrderedDict()

                    self.config = Bfd.Interfaces.Interface.InterfaceRef.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.state = Bfd.Interfaces.Interface.InterfaceRef.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._segment_path = lambda: "interface-ref"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Bfd.Interfaces.Interface.InterfaceRef, [], name, value)


                class Config(_Entity_):
                    """
                    Configured reference to interface / subinterface
                    
                    .. attribute:: interface
                    
                    	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                    
                    .. attribute:: subinterface
                    
                    	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                    
                    

                    """

                    _prefix = 'oc-bfd'
                    _revision = '2018-11-21'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Bfd.Interfaces.Interface.InterfaceRef.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "interface-ref"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('subinterface', (YLeaf(YType.str, 'subinterface'), ['int'])),
                        ])
                        self.interface = None
                        self.subinterface = None
                        self._segment_path = lambda: "config"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bfd.Interfaces.Interface.InterfaceRef.Config, ['interface', 'subinterface'], name, value)



                class State(_Entity_):
                    """
                    Operational state for interface\-ref
                    
                    .. attribute:: interface
                    
                    	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                    
                    	**config**\: False
                    
                    .. attribute:: subinterface
                    
                    	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-bfd'
                    _revision = '2018-11-21'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Bfd.Interfaces.Interface.InterfaceRef.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "interface-ref"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('subinterface', (YLeaf(YType.str, 'subinterface'), ['int'])),
                        ])
                        self.interface = None
                        self.subinterface = None
                        self._segment_path = lambda: "state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bfd.Interfaces.Interface.InterfaceRef.State, ['interface', 'subinterface'], name, value)




            class MicroBfdSessions(_Entity_):
                """
                Parameters relating to micro\-BFD sessions associated
                with the interface.
                
                .. attribute:: micro_bfd_session
                
                	This list contains configuration and state parameters relating to micro\-BFD session
                	**type**\: list of  		 :py:class:`MicroBfdSession <ydk.models.openconfig.openconfig_bfd.Bfd.Interfaces.Interface.MicroBfdSessions.MicroBfdSession>`
                
                

                """

                _prefix = 'oc-bfd'
                _revision = '2018-11-21'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Bfd.Interfaces.Interface.MicroBfdSessions, self).__init__()

                    self.yang_name = "micro-bfd-sessions"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("micro-bfd-session", ("micro_bfd_session", Bfd.Interfaces.Interface.MicroBfdSessions.MicroBfdSession))])
                    self._leafs = OrderedDict()

                    self.micro_bfd_session = YList(self)
                    self._segment_path = lambda: "micro-bfd-sessions"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Bfd.Interfaces.Interface.MicroBfdSessions, [], name, value)


                class MicroBfdSession(_Entity_):
                    """
                    This list contains configuration and state parameters
                    relating to micro\-BFD session.
                    
                    .. attribute:: member_interface  (key)
                    
                    	A reference to the member interface of the link aggregate
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`member_interface <ydk.models.openconfig.openconfig_bfd.Bfd.Interfaces.Interface.MicroBfdSessions.MicroBfdSession.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration parameters for the micro\-BFD session
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bfd.Bfd.Interfaces.Interface.MicroBfdSessions.MicroBfdSession.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state parameters for the micro\-BFD session
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bfd.Bfd.Interfaces.Interface.MicroBfdSessions.MicroBfdSession.State>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-bfd'
                    _revision = '2018-11-21'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Bfd.Interfaces.Interface.MicroBfdSessions.MicroBfdSession, self).__init__()

                        self.yang_name = "micro-bfd-session"
                        self.yang_parent_name = "micro-bfd-sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['member_interface']
                        self._child_classes = OrderedDict([("config", ("config", Bfd.Interfaces.Interface.MicroBfdSessions.MicroBfdSession.Config)), ("state", ("state", Bfd.Interfaces.Interface.MicroBfdSessions.MicroBfdSession.State))])
                        self._leafs = OrderedDict([
                            ('member_interface', (YLeaf(YType.str, 'member-interface'), ['str'])),
                        ])
                        self.member_interface = None

                        self.config = Bfd.Interfaces.Interface.MicroBfdSessions.MicroBfdSession.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = Bfd.Interfaces.Interface.MicroBfdSessions.MicroBfdSession.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "micro-bfd-session" + "[member-interface='" + str(self.member_interface) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bfd.Interfaces.Interface.MicroBfdSessions.MicroBfdSession, ['member_interface'], name, value)


                    class Config(_Entity_):
                        """
                        Configuration parameters for the micro\-BFD session.
                        
                        .. attribute:: local_address
                        
                        	The local IP address used by the system for the micro\-BFD session specified
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                        
                        .. attribute:: remote_address
                        
                        	The remote IP destination that should be used by the system for the micro\-BFD session specified
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                        
                        .. attribute:: member_interface
                        
                        	Reference to a member link of the aggregate interface being described
                        	**type**\: str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Config>`
                        
                        

                        """

                        _prefix = 'oc-bfd'
                        _revision = '2018-11-21'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Bfd.Interfaces.Interface.MicroBfdSessions.MicroBfdSession.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "micro-bfd-session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('local_address', (YLeaf(YType.str, 'local-address'), ['str','str'])),
                                ('remote_address', (YLeaf(YType.str, 'remote-address'), ['str','str'])),
                                ('member_interface', (YLeaf(YType.str, 'member-interface'), ['str'])),
                            ])
                            self.local_address = None
                            self.remote_address = None
                            self.member_interface = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bfd.Interfaces.Interface.MicroBfdSessions.MicroBfdSession.Config, ['local_address', 'remote_address', 'member_interface'], name, value)



                    class State(_Entity_):
                        """
                        Operational state parameters for the micro\-BFD session.
                        
                        .. attribute:: local_address
                        
                        	The local IP address used by the system for the micro\-BFD session specified
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                        
                        	**config**\: False
                        
                        .. attribute:: remote_address
                        
                        	The remote IP destination that should be used by the system for the micro\-BFD session specified
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                        
                        	**config**\: False
                        
                        .. attribute:: member_interface
                        
                        	Reference to a member link of the aggregate interface being described
                        	**type**\: str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Config>`
                        
                        	**config**\: False
                        
                        .. attribute:: session_state
                        
                        	The state of the BFD session perceived by the local system
                        	**type**\:  :py:class:`BfdSessionState <ydk.models.openconfig.openconfig_bfd.BfdSessionState>`
                        
                        	**config**\: False
                        
                        .. attribute:: remote_session_state
                        
                        	The reported state of the BFD session according to the remote system. This state reflects the last state reported in a BFD control packet
                        	**type**\:  :py:class:`BfdSessionState <ydk.models.openconfig.openconfig_bfd.BfdSessionState>`
                        
                        	**config**\: False
                        
                        .. attribute:: last_failure_time
                        
                        	The time of the last transition of the BFD session out of the UP state, expressed as the number of nanoseconds since the Unix epoch
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: failure_transitions
                        
                        	The number of times that the BFD session has transitioned out of the UP state
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: local_discriminator
                        
                        	A unique identifier used by the local system to identify this BFD session
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: remote_discriminator
                        
                        	A unique identified used by the remote system to identify this BFD session
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: local_diagnostic_code
                        
                        	The local BFD diagnostic code indicating the most recent reason for failure of this BFD session
                        	**type**\:  :py:class:`BfdDiagnosticCode <ydk.models.openconfig.openconfig_bfd.BfdDiagnosticCode>`
                        
                        	**config**\: False
                        
                        .. attribute:: remote_diagnostic_code
                        
                        	The remote BFD diagnostic code indicating the remote system's reason for failure of the BFD session
                        	**type**\:  :py:class:`BfdDiagnosticCode <ydk.models.openconfig.openconfig_bfd.BfdDiagnosticCode>`
                        
                        	**config**\: False
                        
                        .. attribute:: remote_minimum_receive_interval
                        
                        	The value of the minimum receive interval that was specified in the most recent BFD control packet received from the peer
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: demand_mode_requested
                        
                        	This leaf is set to true when the remote system has requested demand mode be run for this session
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: remote_authentication_enabled
                        
                        	This leaf is set to true when the remote system has specified that authentication is present for the BFD session
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: remote_control_plane_independent
                        
                        	This leaf is set to true when the remote system has specified that the hardware implementing this BFD session is independent of the control plane's liveliness
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: async_
                        
                        	Operational state parameters specifically relating to asynchronous mode of BFD
                        	**type**\:  :py:class:`Async <ydk.models.openconfig.openconfig_bfd.Bfd.Interfaces.Interface.MicroBfdSessions.MicroBfdSession.State.Async>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-bfd'
                        _revision = '2018-11-21'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Bfd.Interfaces.Interface.MicroBfdSessions.MicroBfdSession.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "micro-bfd-session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("async", ("async_", Bfd.Interfaces.Interface.MicroBfdSessions.MicroBfdSession.State.Async))])
                            self._leafs = OrderedDict([
                                ('local_address', (YLeaf(YType.str, 'local-address'), ['str','str'])),
                                ('remote_address', (YLeaf(YType.str, 'remote-address'), ['str','str'])),
                                ('member_interface', (YLeaf(YType.str, 'member-interface'), ['str'])),
                                ('session_state', (YLeaf(YType.enumeration, 'session-state'), [('ydk.models.openconfig.openconfig_bfd', 'BfdSessionState', '')])),
                                ('remote_session_state', (YLeaf(YType.enumeration, 'remote-session-state'), [('ydk.models.openconfig.openconfig_bfd', 'BfdSessionState', '')])),
                                ('last_failure_time', (YLeaf(YType.uint64, 'last-failure-time'), ['int'])),
                                ('failure_transitions', (YLeaf(YType.uint64, 'failure-transitions'), ['int'])),
                                ('local_discriminator', (YLeaf(YType.str, 'local-discriminator'), ['str'])),
                                ('remote_discriminator', (YLeaf(YType.str, 'remote-discriminator'), ['str'])),
                                ('local_diagnostic_code', (YLeaf(YType.enumeration, 'local-diagnostic-code'), [('ydk.models.openconfig.openconfig_bfd', 'BfdDiagnosticCode', '')])),
                                ('remote_diagnostic_code', (YLeaf(YType.enumeration, 'remote-diagnostic-code'), [('ydk.models.openconfig.openconfig_bfd', 'BfdDiagnosticCode', '')])),
                                ('remote_minimum_receive_interval', (YLeaf(YType.uint32, 'remote-minimum-receive-interval'), ['int'])),
                                ('demand_mode_requested', (YLeaf(YType.boolean, 'demand-mode-requested'), ['bool'])),
                                ('remote_authentication_enabled', (YLeaf(YType.boolean, 'remote-authentication-enabled'), ['bool'])),
                                ('remote_control_plane_independent', (YLeaf(YType.boolean, 'remote-control-plane-independent'), ['bool'])),
                            ])
                            self.local_address = None
                            self.remote_address = None
                            self.member_interface = None
                            self.session_state = None
                            self.remote_session_state = None
                            self.last_failure_time = None
                            self.failure_transitions = None
                            self.local_discriminator = None
                            self.remote_discriminator = None
                            self.local_diagnostic_code = None
                            self.remote_diagnostic_code = None
                            self.remote_minimum_receive_interval = None
                            self.demand_mode_requested = None
                            self.remote_authentication_enabled = None
                            self.remote_control_plane_independent = None

                            self.async_ = Bfd.Interfaces.Interface.MicroBfdSessions.MicroBfdSession.State.Async()
                            self.async_.parent = self
                            self._children_name_map["async_"] = "async"
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bfd.Interfaces.Interface.MicroBfdSessions.MicroBfdSession.State, ['local_address', 'remote_address', 'member_interface', 'session_state', 'remote_session_state', 'last_failure_time', 'failure_transitions', 'local_discriminator', 'remote_discriminator', 'local_diagnostic_code', 'remote_diagnostic_code', 'remote_minimum_receive_interval', 'demand_mode_requested', 'remote_authentication_enabled', 'remote_control_plane_independent'], name, value)


                        class Async(_Entity_):
                            """
                            Operational state parameters specifically relating to
                            asynchronous mode of BFD.
                            
                            .. attribute:: last_packet_transmitted
                            
                            	The date and time at which the last BFD packet was transmitted for this session, expressed as the number of nanoseconds since the Unix Epoch (January 1, 1970, 00\:00 UTC)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: last_packet_received
                            
                            	The date and time at which the last BFD packet was received for this session, expressed as the number of nanoseconds since the Unix Epoch (January 1, 1970, 00\:00 UTC)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: transmitted_packets
                            
                            	The number of packets that have been transmitted by the local system
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: received_packets
                            
                            	The number of packets that have been received by the local system from the remote neighbour
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: up_transitions
                            
                            	The number of times that the adjacency with the neighbor has transitioned into the up state
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-bfd'
                            _revision = '2018-11-21'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Bfd.Interfaces.Interface.MicroBfdSessions.MicroBfdSession.State.Async, self).__init__()

                                self.yang_name = "async"
                                self.yang_parent_name = "state"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('last_packet_transmitted', (YLeaf(YType.uint64, 'last-packet-transmitted'), ['int'])),
                                    ('last_packet_received', (YLeaf(YType.uint64, 'last-packet-received'), ['int'])),
                                    ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                    ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                    ('up_transitions', (YLeaf(YType.uint64, 'up-transitions'), ['int'])),
                                ])
                                self.last_packet_transmitted = None
                                self.last_packet_received = None
                                self.transmitted_packets = None
                                self.received_packets = None
                                self.up_transitions = None
                                self._segment_path = lambda: "async"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bfd.Interfaces.Interface.MicroBfdSessions.MicroBfdSession.State.Async, ['last_packet_transmitted', 'last_packet_received', 'transmitted_packets', 'received_packets', 'up_transitions'], name, value)






            class Peers(_Entity_):
                """
                Parameters relating to the BFD peers which are seen
                over this interface.
                
                .. attribute:: peer
                
                	Parameters relating to the BFD peer specified by the remote address
                	**type**\: list of  		 :py:class:`Peer <ydk.models.openconfig.openconfig_bfd.Bfd.Interfaces.Interface.Peers.Peer>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-bfd'
                _revision = '2018-11-21'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Bfd.Interfaces.Interface.Peers, self).__init__()

                    self.yang_name = "peers"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("peer", ("peer", Bfd.Interfaces.Interface.Peers.Peer))])
                    self._leafs = OrderedDict()

                    self.peer = YList(self)
                    self._segment_path = lambda: "peers"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Bfd.Interfaces.Interface.Peers, [], name, value)


                class Peer(_Entity_):
                    """
                    Parameters relating to the BFD peer specified by the
                    remote address.
                    
                    .. attribute:: local_discriminator  (key)
                    
                    	The local discriminator, which is unique for the session on the system
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`local_discriminator <ydk.models.openconfig.openconfig_bfd.Bfd.Interfaces.Interface.Peers.Peer.State>`
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	Operational state parameters for the BFD session
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bfd.Bfd.Interfaces.Interface.Peers.Peer.State>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-bfd'
                    _revision = '2018-11-21'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Bfd.Interfaces.Interface.Peers.Peer, self).__init__()

                        self.yang_name = "peer"
                        self.yang_parent_name = "peers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['local_discriminator']
                        self._child_classes = OrderedDict([("state", ("state", Bfd.Interfaces.Interface.Peers.Peer.State))])
                        self._leafs = OrderedDict([
                            ('local_discriminator', (YLeaf(YType.str, 'local-discriminator'), ['str'])),
                        ])
                        self.local_discriminator = None

                        self.state = Bfd.Interfaces.Interface.Peers.Peer.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "peer" + "[local-discriminator='" + str(self.local_discriminator) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bfd.Interfaces.Interface.Peers.Peer, ['local_discriminator'], name, value)


                    class State(_Entity_):
                        """
                        Operational state parameters for the BFD session.
                        
                        .. attribute:: local_address
                        
                        	The IP address used by the local system for this BFD session
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                        
                        	**config**\: False
                        
                        .. attribute:: remote_address
                        
                        	The IP address used by the remote system for this BFD session
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                        
                        	**config**\: False
                        
                        .. attribute:: subscribed_protocols
                        
                        	Indicates the set of protocols that currently use this BFD session for liveliness detection
                        	**type**\: list of   :py:class:`INSTALLPROTOCOLTYPE <ydk.models.openconfig.openconfig_policy_types.INSTALLPROTOCOLTYPE>`
                        
                        	**config**\: False
                        
                        .. attribute:: session_state
                        
                        	The state of the BFD session perceived by the local system
                        	**type**\:  :py:class:`BfdSessionState <ydk.models.openconfig.openconfig_bfd.BfdSessionState>`
                        
                        	**config**\: False
                        
                        .. attribute:: remote_session_state
                        
                        	The reported state of the BFD session according to the remote system. This state reflects the last state reported in a BFD control packet
                        	**type**\:  :py:class:`BfdSessionState <ydk.models.openconfig.openconfig_bfd.BfdSessionState>`
                        
                        	**config**\: False
                        
                        .. attribute:: last_failure_time
                        
                        	The time of the last transition of the BFD session out of the UP state, expressed as the number of nanoseconds since the Unix epoch
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: failure_transitions
                        
                        	The number of times that the BFD session has transitioned out of the UP state
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: local_discriminator
                        
                        	A unique identifier used by the local system to identify this BFD session
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: remote_discriminator
                        
                        	A unique identified used by the remote system to identify this BFD session
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: local_diagnostic_code
                        
                        	The local BFD diagnostic code indicating the most recent reason for failure of this BFD session
                        	**type**\:  :py:class:`BfdDiagnosticCode <ydk.models.openconfig.openconfig_bfd.BfdDiagnosticCode>`
                        
                        	**config**\: False
                        
                        .. attribute:: remote_diagnostic_code
                        
                        	The remote BFD diagnostic code indicating the remote system's reason for failure of the BFD session
                        	**type**\:  :py:class:`BfdDiagnosticCode <ydk.models.openconfig.openconfig_bfd.BfdDiagnosticCode>`
                        
                        	**config**\: False
                        
                        .. attribute:: remote_minimum_receive_interval
                        
                        	The value of the minimum receive interval that was specified in the most recent BFD control packet received from the peer
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: demand_mode_requested
                        
                        	This leaf is set to true when the remote system has requested demand mode be run for this session
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: remote_authentication_enabled
                        
                        	This leaf is set to true when the remote system has specified that authentication is present for the BFD session
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: remote_control_plane_independent
                        
                        	This leaf is set to true when the remote system has specified that the hardware implementing this BFD session is independent of the control plane's liveliness
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: echo
                        
                        	Operational state parameters specifically relating to the echo mode of BFD
                        	**type**\:  :py:class:`Echo <ydk.models.openconfig.openconfig_bfd.Bfd.Interfaces.Interface.Peers.Peer.State.Echo>`
                        
                        	**config**\: False
                        
                        .. attribute:: async_
                        
                        	Operational state parameters specifically relating to asynchronous mode of BFD
                        	**type**\:  :py:class:`Async <ydk.models.openconfig.openconfig_bfd.Bfd.Interfaces.Interface.Peers.Peer.State.Async>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-bfd'
                        _revision = '2018-11-21'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Bfd.Interfaces.Interface.Peers.Peer.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "peer"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("echo", ("echo", Bfd.Interfaces.Interface.Peers.Peer.State.Echo)), ("async", ("async_", Bfd.Interfaces.Interface.Peers.Peer.State.Async))])
                            self._leafs = OrderedDict([
                                ('local_address', (YLeaf(YType.str, 'local-address'), ['str','str'])),
                                ('remote_address', (YLeaf(YType.str, 'remote-address'), ['str','str'])),
                                ('subscribed_protocols', (YLeafList(YType.identityref, 'subscribed-protocols'), [('ydk.models.openconfig.openconfig_policy_types', 'INSTALLPROTOCOLTYPE')])),
                                ('session_state', (YLeaf(YType.enumeration, 'session-state'), [('ydk.models.openconfig.openconfig_bfd', 'BfdSessionState', '')])),
                                ('remote_session_state', (YLeaf(YType.enumeration, 'remote-session-state'), [('ydk.models.openconfig.openconfig_bfd', 'BfdSessionState', '')])),
                                ('last_failure_time', (YLeaf(YType.uint64, 'last-failure-time'), ['int'])),
                                ('failure_transitions', (YLeaf(YType.uint64, 'failure-transitions'), ['int'])),
                                ('local_discriminator', (YLeaf(YType.str, 'local-discriminator'), ['str'])),
                                ('remote_discriminator', (YLeaf(YType.str, 'remote-discriminator'), ['str'])),
                                ('local_diagnostic_code', (YLeaf(YType.enumeration, 'local-diagnostic-code'), [('ydk.models.openconfig.openconfig_bfd', 'BfdDiagnosticCode', '')])),
                                ('remote_diagnostic_code', (YLeaf(YType.enumeration, 'remote-diagnostic-code'), [('ydk.models.openconfig.openconfig_bfd', 'BfdDiagnosticCode', '')])),
                                ('remote_minimum_receive_interval', (YLeaf(YType.uint32, 'remote-minimum-receive-interval'), ['int'])),
                                ('demand_mode_requested', (YLeaf(YType.boolean, 'demand-mode-requested'), ['bool'])),
                                ('remote_authentication_enabled', (YLeaf(YType.boolean, 'remote-authentication-enabled'), ['bool'])),
                                ('remote_control_plane_independent', (YLeaf(YType.boolean, 'remote-control-plane-independent'), ['bool'])),
                            ])
                            self.local_address = None
                            self.remote_address = None
                            self.subscribed_protocols = []
                            self.session_state = None
                            self.remote_session_state = None
                            self.last_failure_time = None
                            self.failure_transitions = None
                            self.local_discriminator = None
                            self.remote_discriminator = None
                            self.local_diagnostic_code = None
                            self.remote_diagnostic_code = None
                            self.remote_minimum_receive_interval = None
                            self.demand_mode_requested = None
                            self.remote_authentication_enabled = None
                            self.remote_control_plane_independent = None

                            self.echo = Bfd.Interfaces.Interface.Peers.Peer.State.Echo()
                            self.echo.parent = self
                            self._children_name_map["echo"] = "echo"

                            self.async_ = Bfd.Interfaces.Interface.Peers.Peer.State.Async()
                            self.async_.parent = self
                            self._children_name_map["async_"] = "async"
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bfd.Interfaces.Interface.Peers.Peer.State, ['local_address', 'remote_address', 'subscribed_protocols', 'session_state', 'remote_session_state', 'last_failure_time', 'failure_transitions', 'local_discriminator', 'remote_discriminator', 'local_diagnostic_code', 'remote_diagnostic_code', 'remote_minimum_receive_interval', 'demand_mode_requested', 'remote_authentication_enabled', 'remote_control_plane_independent'], name, value)


                        class Echo(_Entity_):
                            """
                            Operational state parameters specifically relating to the
                            echo mode of BFD.
                            
                            .. attribute:: active
                            
                            	This leaf is set to true when echo mode is running between the local and remote system. When it is set to false, solely asynchronous mode is active
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: last_packet_transmitted
                            
                            	The date and time at which the last BFD packet was transmitted for this session, expressed as the number of nanoseconds since the Unix Epoch (January 1, 1970, 00\:00 UTC)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: last_packet_received
                            
                            	The date and time at which the last BFD packet was received for this session, expressed as the number of nanoseconds since the Unix Epoch (January 1, 1970, 00\:00 UTC)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: transmitted_packets
                            
                            	The number of packets that have been transmitted by the local system
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: received_packets
                            
                            	The number of packets that have been received by the local system from the remote neighbour
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: up_transitions
                            
                            	The number of times that the adjacency with the neighbor has transitioned into the up state
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-bfd'
                            _revision = '2018-11-21'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Bfd.Interfaces.Interface.Peers.Peer.State.Echo, self).__init__()

                                self.yang_name = "echo"
                                self.yang_parent_name = "state"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('active', (YLeaf(YType.boolean, 'active'), ['bool'])),
                                    ('last_packet_transmitted', (YLeaf(YType.uint64, 'last-packet-transmitted'), ['int'])),
                                    ('last_packet_received', (YLeaf(YType.uint64, 'last-packet-received'), ['int'])),
                                    ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                    ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                    ('up_transitions', (YLeaf(YType.uint64, 'up-transitions'), ['int'])),
                                ])
                                self.active = None
                                self.last_packet_transmitted = None
                                self.last_packet_received = None
                                self.transmitted_packets = None
                                self.received_packets = None
                                self.up_transitions = None
                                self._segment_path = lambda: "echo"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bfd.Interfaces.Interface.Peers.Peer.State.Echo, ['active', 'last_packet_transmitted', 'last_packet_received', 'transmitted_packets', 'received_packets', 'up_transitions'], name, value)



                        class Async(_Entity_):
                            """
                            Operational state parameters specifically relating to
                            asynchronous mode of BFD.
                            
                            .. attribute:: last_packet_transmitted
                            
                            	The date and time at which the last BFD packet was transmitted for this session, expressed as the number of nanoseconds since the Unix Epoch (January 1, 1970, 00\:00 UTC)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: last_packet_received
                            
                            	The date and time at which the last BFD packet was received for this session, expressed as the number of nanoseconds since the Unix Epoch (January 1, 1970, 00\:00 UTC)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: transmitted_packets
                            
                            	The number of packets that have been transmitted by the local system
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: received_packets
                            
                            	The number of packets that have been received by the local system from the remote neighbour
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: up_transitions
                            
                            	The number of times that the adjacency with the neighbor has transitioned into the up state
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-bfd'
                            _revision = '2018-11-21'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Bfd.Interfaces.Interface.Peers.Peer.State.Async, self).__init__()

                                self.yang_name = "async"
                                self.yang_parent_name = "state"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('last_packet_transmitted', (YLeaf(YType.uint64, 'last-packet-transmitted'), ['int'])),
                                    ('last_packet_received', (YLeaf(YType.uint64, 'last-packet-received'), ['int'])),
                                    ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                    ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                    ('up_transitions', (YLeaf(YType.uint64, 'up-transitions'), ['int'])),
                                ])
                                self.last_packet_transmitted = None
                                self.last_packet_received = None
                                self.transmitted_packets = None
                                self.received_packets = None
                                self.up_transitions = None
                                self._segment_path = lambda: "async"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bfd.Interfaces.Interface.Peers.Peer.State.Async, ['last_packet_transmitted', 'last_packet_received', 'transmitted_packets', 'received_packets', 'up_transitions'], name, value)







    def clone_ptr(self):
        self._top_entity = Bfd()
        return self._top_entity




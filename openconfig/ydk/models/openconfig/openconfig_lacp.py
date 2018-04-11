""" openconfig_lacp 

This module describes configuration and operational state
data for Link Aggregation Control Protocol (LACP) for
managing aggregate interfaces.   It works in conjunction with
the OpenConfig interfaces and aggregate interfaces models.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class LacpActivityType(Enum):
    """
    LacpActivityType (Enum Class)

    Describes the LACP membership type, active or passive, of the

    interface in the aggregate

    .. data:: ACTIVE = 0

    	Interface is an active member, i.e., will detect and

    	maintain aggregates

    .. data:: PASSIVE = 1

    	Interface is a passive member, i.e., it participates

    	with an active partner

    """

    ACTIVE = Enum.YLeaf(0, "ACTIVE")

    PASSIVE = Enum.YLeaf(1, "PASSIVE")


class LacpPeriodType(Enum):
    """
    LacpPeriodType (Enum Class)

    Defines the period options for the time between sending

    LACP messages

    .. data:: FAST = 0

    	Send LACP packets every second

    .. data:: SLOW = 1

    	Send LACP packets every 30 seconds

    """

    FAST = Enum.YLeaf(0, "FAST")

    SLOW = Enum.YLeaf(1, "SLOW")


class LacpSynchronizationType(Enum):
    """
    LacpSynchronizationType (Enum Class)

    Indicates LACP synchronization state of participant

    .. data:: IN_SYNC = 0

    	Participant is in sync with the system id and key

    	transmitted

    .. data:: OUT_SYNC = 1

    	Participant is not in sync with the system id and key

    	transmitted

    """

    IN_SYNC = Enum.YLeaf(0, "IN_SYNC")

    OUT_SYNC = Enum.YLeaf(1, "OUT_SYNC")


class LacpTimeoutType(Enum):
    """
    LacpTimeoutType (Enum Class)

    Type of timeout used, short or long, by LACP participants

    .. data:: LONG = 0

    	Participant wishes to use long timeouts to detect

    	status of the aggregate, i.e., will expect less frequent

    	transmissions. Long timeout is 90 seconds.

    .. data:: SHORT = 1

    	Participant wishes to use short timeouts, i.e., expects

    	frequent transmissions to aggressively detect status

    	changes. Short timeout is 3 seconds.

    """

    LONG = Enum.YLeaf(0, "LONG")

    SHORT = Enum.YLeaf(1, "SHORT")



class Lacp(Entity):
    """
    Configuration and operational state data for LACP protocol
    operation on the aggregate interface
    
    .. attribute:: config
    
    	Configuration data for LACP
    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_lacp.Lacp.Config>`
    
    .. attribute:: state
    
    	Operational state data for LACP
    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_lacp.Lacp.State>`
    
    .. attribute:: interfaces
    
    	Enclosing container for the list of LACP\-enabled interfaces
    	**type**\:  :py:class:`Interfaces <ydk.models.openconfig.openconfig_lacp.Lacp.Interfaces>`
    
    

    """

    _prefix = 'oc-lacp'
    _revision = '2016-05-26'

    def __init__(self):
        super(Lacp, self).__init__()
        self._top_entity = None

        self.yang_name = "lacp"
        self.yang_parent_name = "openconfig-lacp"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("config", ("config", Lacp.Config)), ("state", ("state", Lacp.State)), ("interfaces", ("interfaces", Lacp.Interfaces))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.config = Lacp.Config()
        self.config.parent = self
        self._children_name_map["config"] = "config"
        self._children_yang_names.add("config")

        self.state = Lacp.State()
        self.state.parent = self
        self._children_name_map["state"] = "state"
        self._children_yang_names.add("state")

        self.interfaces = Lacp.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")
        self._segment_path = lambda: "openconfig-lacp:lacp"


    class Config(Entity):
        """
        Configuration data for LACP
        
        .. attribute:: system_priority
        
        	Sytem priority used by the node on this LAG interface. Lower value is higher priority for determining which node is the controlling system
        	**type**\: int
        
        	**range:** 0..65535
        
        

        """

        _prefix = 'oc-lacp'
        _revision = '2016-05-26'

        def __init__(self):
            super(Lacp.Config, self).__init__()

            self.yang_name = "config"
            self.yang_parent_name = "lacp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('system_priority', YLeaf(YType.uint16, 'system-priority')),
            ])
            self.system_priority = None
            self._segment_path = lambda: "config"
            self._absolute_path = lambda: "openconfig-lacp:lacp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Lacp.Config, ['system_priority'], name, value)


    class State(Entity):
        """
        Operational state data for LACP
        
        .. attribute:: system_priority
        
        	Sytem priority used by the node on this LAG interface. Lower value is higher priority for determining which node is the controlling system
        	**type**\: int
        
        	**range:** 0..65535
        
        

        """

        _prefix = 'oc-lacp'
        _revision = '2016-05-26'

        def __init__(self):
            super(Lacp.State, self).__init__()

            self.yang_name = "state"
            self.yang_parent_name = "lacp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('system_priority', YLeaf(YType.uint16, 'system-priority')),
            ])
            self.system_priority = None
            self._segment_path = lambda: "state"
            self._absolute_path = lambda: "openconfig-lacp:lacp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Lacp.State, ['system_priority'], name, value)


    class Interfaces(Entity):
        """
        Enclosing container for the list of LACP\-enabled
        interfaces
        
        .. attribute:: interface
        
        	List of aggregate interfaces managed by LACP
        	**type**\: list of  		 :py:class:`Interface <ydk.models.openconfig.openconfig_lacp.Lacp.Interfaces.Interface>`
        
        

        """

        _prefix = 'oc-lacp'
        _revision = '2016-05-26'

        def __init__(self):
            super(Lacp.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "lacp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("interface", ("interface", Lacp.Interfaces.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "openconfig-lacp:lacp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Lacp.Interfaces, [], name, value)


        class Interface(Entity):
            """
            List of aggregate interfaces managed by LACP
            
            .. attribute:: name  (key)
            
            	Reference to the list key
            	**type**\: str
            
            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_lacp.Lacp.Interfaces.Interface.Config>`
            
            .. attribute:: config
            
            	Configuration data for each LACP aggregate interface
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_lacp.Lacp.Interfaces.Interface.Config>`
            
            .. attribute:: state
            
            	Operational state data for each LACP aggregate interface
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_lacp.Lacp.Interfaces.Interface.State>`
            
            .. attribute:: members
            
            	Enclosing container for the list of members interfaces of the aggregate. This list is considered operational state only so is labeled config false and has no config container
            	**type**\:  :py:class:`Members <ydk.models.openconfig.openconfig_lacp.Lacp.Interfaces.Interface.Members>`
            
            

            """

            _prefix = 'oc-lacp'
            _revision = '2016-05-26'

            def __init__(self):
                super(Lacp.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_container_classes = OrderedDict([("config", ("config", Lacp.Interfaces.Interface.Config)), ("state", ("state", Lacp.Interfaces.Interface.State)), ("members", ("members", Lacp.Interfaces.Interface.Members))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', YLeaf(YType.str, 'name')),
                ])
                self.name = None

                self.config = Lacp.Interfaces.Interface.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.state = Lacp.Interfaces.Interface.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")

                self.members = Lacp.Interfaces.Interface.Members()
                self.members.parent = self
                self._children_name_map["members"] = "members"
                self._children_yang_names.add("members")
                self._segment_path = lambda: "interface" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "openconfig-lacp:lacp/interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Lacp.Interfaces.Interface, ['name'], name, value)


            class Config(Entity):
                """
                Configuration data for each LACP aggregate interface
                
                .. attribute:: name
                
                	Reference to the interface on which LACP should be configured.   The type of the target interface must be ieee8023adLag
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                
                .. attribute:: interval
                
                	Set the period between LACP messages \-\- uses the lacp\-period\-type enumeration
                	**type**\:  :py:class:`LacpPeriodType <ydk.models.openconfig.openconfig_lacp.LacpPeriodType>`
                
                	**default value**\: SLOW
                
                .. attribute:: lacp_mode
                
                	ACTIVE is to initiate the transmission of LACP packets. PASSIVE is to wait for peer to initiate the transmission of LACP packets
                	**type**\:  :py:class:`LacpActivityType <ydk.models.openconfig.openconfig_lacp.LacpActivityType>`
                
                	**default value**\: ACTIVE
                
                .. attribute:: system_id_mac
                
                	The MAC address portion of the node's System ID. This is combined with the system priority to construct the 8\-octet system\-id
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: system_priority
                
                	Sytem priority used by the node on this LAG interface. Lower value is higher priority for determining which node is the controlling system
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'oc-lacp'
                _revision = '2016-05-26'

                def __init__(self):
                    super(Lacp.Interfaces.Interface.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                        ('interval', YLeaf(YType.enumeration, 'interval')),
                        ('lacp_mode', YLeaf(YType.enumeration, 'lacp-mode')),
                        ('system_id_mac', YLeaf(YType.str, 'system-id-mac')),
                        ('system_priority', YLeaf(YType.uint16, 'system-priority')),
                    ])
                    self.name = None
                    self.interval = None
                    self.lacp_mode = None
                    self.system_id_mac = None
                    self.system_priority = None
                    self._segment_path = lambda: "config"

                def __setattr__(self, name, value):
                    self._perform_setattr(Lacp.Interfaces.Interface.Config, ['name', 'interval', 'lacp_mode', 'system_id_mac', 'system_priority'], name, value)


            class State(Entity):
                """
                Operational state data for each LACP aggregate
                interface
                
                .. attribute:: name
                
                	Reference to the interface on which LACP should be configured.   The type of the target interface must be ieee8023adLag
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                
                .. attribute:: interval
                
                	Set the period between LACP messages \-\- uses the lacp\-period\-type enumeration
                	**type**\:  :py:class:`LacpPeriodType <ydk.models.openconfig.openconfig_lacp.LacpPeriodType>`
                
                	**default value**\: SLOW
                
                .. attribute:: lacp_mode
                
                	ACTIVE is to initiate the transmission of LACP packets. PASSIVE is to wait for peer to initiate the transmission of LACP packets
                	**type**\:  :py:class:`LacpActivityType <ydk.models.openconfig.openconfig_lacp.LacpActivityType>`
                
                	**default value**\: ACTIVE
                
                .. attribute:: system_id_mac
                
                	The MAC address portion of the node's System ID. This is combined with the system priority to construct the 8\-octet system\-id
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: system_priority
                
                	Sytem priority used by the node on this LAG interface. Lower value is higher priority for determining which node is the controlling system
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'oc-lacp'
                _revision = '2016-05-26'

                def __init__(self):
                    super(Lacp.Interfaces.Interface.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                        ('interval', YLeaf(YType.enumeration, 'interval')),
                        ('lacp_mode', YLeaf(YType.enumeration, 'lacp-mode')),
                        ('system_id_mac', YLeaf(YType.str, 'system-id-mac')),
                        ('system_priority', YLeaf(YType.uint16, 'system-priority')),
                    ])
                    self.name = None
                    self.interval = None
                    self.lacp_mode = None
                    self.system_id_mac = None
                    self.system_priority = None
                    self._segment_path = lambda: "state"

                def __setattr__(self, name, value):
                    self._perform_setattr(Lacp.Interfaces.Interface.State, ['name', 'interval', 'lacp_mode', 'system_id_mac', 'system_priority'], name, value)


            class Members(Entity):
                """
                Enclosing container for the list of members interfaces of
                the aggregate. This list is considered operational state
                only so is labeled config false and has no config container
                
                .. attribute:: member
                
                	List of member interfaces and their associated status for a LACP\-controlled aggregate interface.  Member list is not configurable here \-\- each interface indicates items its participation in the LAG
                	**type**\: list of  		 :py:class:`Member <ydk.models.openconfig.openconfig_lacp.Lacp.Interfaces.Interface.Members.Member>`
                
                

                """

                _prefix = 'oc-lacp'
                _revision = '2016-05-26'

                def __init__(self):
                    super(Lacp.Interfaces.Interface.Members, self).__init__()

                    self.yang_name = "members"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("member", ("member", Lacp.Interfaces.Interface.Members.Member))])
                    self._leafs = OrderedDict()

                    self.member = YList(self)
                    self._segment_path = lambda: "members"

                def __setattr__(self, name, value):
                    self._perform_setattr(Lacp.Interfaces.Interface.Members, [], name, value)


                class Member(Entity):
                    """
                    List of member interfaces and their associated status for
                    a LACP\-controlled aggregate interface.  Member list is not
                    configurable here \-\- each interface indicates items
                    its participation in the LAG.
                    
                    .. attribute:: interface  (key)
                    
                    	Reference to aggregate member interface
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`interface <ydk.models.openconfig.openconfig_lacp.Lacp.Interfaces.Interface.Members.Member.State>`
                    
                    .. attribute:: state
                    
                    	Operational state data for aggregate members
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_lacp.Lacp.Interfaces.Interface.Members.Member.State>`
                    
                    

                    """

                    _prefix = 'oc-lacp'
                    _revision = '2016-05-26'

                    def __init__(self):
                        super(Lacp.Interfaces.Interface.Members.Member, self).__init__()

                        self.yang_name = "member"
                        self.yang_parent_name = "members"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface']
                        self._child_container_classes = OrderedDict([("state", ("state", Lacp.Interfaces.Interface.Members.Member.State))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface', YLeaf(YType.str, 'interface')),
                        ])
                        self.interface = None

                        self.state = Lacp.Interfaces.Interface.Members.Member.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "member" + "[interface='" + str(self.interface) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lacp.Interfaces.Interface.Members.Member, ['interface'], name, value)


                    class State(Entity):
                        """
                        Operational state data for aggregate members
                        
                        .. attribute:: interface
                        
                        	Reference to interface member of the LACP aggregate
                        	**type**\: str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                        
                        .. attribute:: activity
                        
                        	Indicates participant is active or passive
                        	**type**\:  :py:class:`LacpActivityType <ydk.models.openconfig.openconfig_lacp.LacpActivityType>`
                        
                        .. attribute:: timeout
                        
                        	The timeout type (short or long) used by the participant
                        	**type**\:  :py:class:`LacpTimeoutType <ydk.models.openconfig.openconfig_lacp.LacpTimeoutType>`
                        
                        .. attribute:: synchronization
                        
                        	Indicates whether the participant is in\-sync or out\-of\-sync
                        	**type**\:  :py:class:`LacpSynchronizationType <ydk.models.openconfig.openconfig_lacp.LacpSynchronizationType>`
                        
                        .. attribute:: aggregatable
                        
                        	A true value indicates that the participant will allow the link to be used as part of the aggregate. A false value indicates the link should be used as an individual link
                        	**type**\: bool
                        
                        .. attribute:: collecting
                        
                        	If true, the participant is collecting incoming frames on the link, otherwise false
                        	**type**\: bool
                        
                        .. attribute:: distributing
                        
                        	When true, the participant is distributing outgoing frames; when false, distribution is disabled
                        	**type**\: bool
                        
                        .. attribute:: system_id
                        
                        	MAC address that defines the local system ID for the aggregate interface
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: oper_key
                        
                        	Current operational value of the key for the aggregate interface
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: partner_id
                        
                        	MAC address representing the protocol partner's interface system ID
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: partner_key
                        
                        	Operational value of the protocol partner's key
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: counters
                        
                        	LACP protocol counters
                        	**type**\:  :py:class:`Counters <ydk.models.openconfig.openconfig_lacp.Lacp.Interfaces.Interface.Members.Member.State.Counters>`
                        
                        

                        """

                        _prefix = 'oc-lacp'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Lacp.Interfaces.Interface.Members.Member.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "member"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("counters", ("counters", Lacp.Interfaces.Interface.Members.Member.State.Counters))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface', YLeaf(YType.str, 'interface')),
                                ('activity', YLeaf(YType.enumeration, 'activity')),
                                ('timeout', YLeaf(YType.enumeration, 'timeout')),
                                ('synchronization', YLeaf(YType.enumeration, 'synchronization')),
                                ('aggregatable', YLeaf(YType.boolean, 'aggregatable')),
                                ('collecting', YLeaf(YType.boolean, 'collecting')),
                                ('distributing', YLeaf(YType.boolean, 'distributing')),
                                ('system_id', YLeaf(YType.str, 'system-id')),
                                ('oper_key', YLeaf(YType.uint16, 'oper-key')),
                                ('partner_id', YLeaf(YType.str, 'partner-id')),
                                ('partner_key', YLeaf(YType.uint16, 'partner-key')),
                            ])
                            self.interface = None
                            self.activity = None
                            self.timeout = None
                            self.synchronization = None
                            self.aggregatable = None
                            self.collecting = None
                            self.distributing = None
                            self.system_id = None
                            self.oper_key = None
                            self.partner_id = None
                            self.partner_key = None

                            self.counters = Lacp.Interfaces.Interface.Members.Member.State.Counters()
                            self.counters.parent = self
                            self._children_name_map["counters"] = "counters"
                            self._children_yang_names.add("counters")
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lacp.Interfaces.Interface.Members.Member.State, ['interface', 'activity', 'timeout', 'synchronization', 'aggregatable', 'collecting', 'distributing', 'system_id', 'oper_key', 'partner_id', 'partner_key'], name, value)


                        class Counters(Entity):
                            """
                            LACP protocol counters
                            
                            .. attribute:: lacp_in_pkts
                            
                            	Number of LACPDUs received
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: lacp_out_pkts
                            
                            	Number of LACPDUs transmitted
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: lacp_rx_errors
                            
                            	Number of LACPDU receive packet errors
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: lacp_tx_errors
                            
                            	Number of LACPDU transmit packet errors
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: lacp_unknown_errors
                            
                            	Number of LACPDU unknown packet errors
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: lacp_errors
                            
                            	Number of LACPDU illegal packet errors
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'oc-lacp'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Lacp.Interfaces.Interface.Members.Member.State.Counters, self).__init__()

                                self.yang_name = "counters"
                                self.yang_parent_name = "state"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('lacp_in_pkts', YLeaf(YType.uint64, 'lacp-in-pkts')),
                                    ('lacp_out_pkts', YLeaf(YType.uint64, 'lacp-out-pkts')),
                                    ('lacp_rx_errors', YLeaf(YType.uint64, 'lacp-rx-errors')),
                                    ('lacp_tx_errors', YLeaf(YType.uint64, 'lacp-tx-errors')),
                                    ('lacp_unknown_errors', YLeaf(YType.uint64, 'lacp-unknown-errors')),
                                    ('lacp_errors', YLeaf(YType.uint64, 'lacp-errors')),
                                ])
                                self.lacp_in_pkts = None
                                self.lacp_out_pkts = None
                                self.lacp_rx_errors = None
                                self.lacp_tx_errors = None
                                self.lacp_unknown_errors = None
                                self.lacp_errors = None
                                self._segment_path = lambda: "counters"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lacp.Interfaces.Interface.Members.Member.State.Counters, ['lacp_in_pkts', 'lacp_out_pkts', 'lacp_rx_errors', 'lacp_tx_errors', 'lacp_unknown_errors', 'lacp_errors'], name, value)

    def clone_ptr(self):
        self._top_entity = Lacp()
        return self._top_entity


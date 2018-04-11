""" openconfig_lldp 

This module defines configuration and operational state data
for the LLDP protocol.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Lldp(Entity):
    """
    Top\-level container for LLDP configuration and state data
    
    .. attribute:: config
    
    	Configuration data 
    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_lldp.Lldp.Config>`
    
    .. attribute:: state
    
    	Operational state data 
    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_lldp.Lldp.State>`
    
    .. attribute:: interfaces
    
    	Enclosing container 
    	**type**\:  :py:class:`Interfaces <ydk.models.openconfig.openconfig_lldp.Lldp.Interfaces>`
    
    

    """

    _prefix = 'oc-lldp'
    _revision = '2016-05-16'

    def __init__(self):
        super(Lldp, self).__init__()
        self._top_entity = None

        self.yang_name = "lldp"
        self.yang_parent_name = "openconfig-lldp"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("config", ("config", Lldp.Config)), ("state", ("state", Lldp.State)), ("interfaces", ("interfaces", Lldp.Interfaces))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.config = Lldp.Config()
        self.config.parent = self
        self._children_name_map["config"] = "config"
        self._children_yang_names.add("config")

        self.state = Lldp.State()
        self.state.parent = self
        self._children_name_map["state"] = "state"
        self._children_yang_names.add("state")

        self.interfaces = Lldp.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")
        self._segment_path = lambda: "openconfig-lldp:lldp"


    class Config(Entity):
        """
        Configuration data 
        
        .. attribute:: enabled
        
        	System level state of the LLDP protocol
        	**type**\: bool
        
        	**default value**\: true
        
        .. attribute:: hello_timer
        
        	System level hello timer for the LLDP protocol
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: seconds
        
        .. attribute:: suppress_tlv_advertisement
        
        	Indicates whether the local system should suppress the advertisement of particular TLVs with the LLDP PDUs that it transmits. Where a TLV type is specified within this list, it should not be included in any LLDP PDU transmitted by the local agent
        	**type**\: list of   :py:class:`LLDPTLV <ydk.models.openconfig.openconfig_lldp_types.LLDPTLV>`
        
        .. attribute:: system_name
        
        	The system name field shall contain an alpha\-numeric string that indicates the system's administratively assigned name. The system name should be the system's fully qualified domain name. If implementations support IETF RFC 3418, the sysName object should be used for this field
        	**type**\: str
        
        	**length:** 0..255
        
        .. attribute:: system_description
        
        	The system description field shall contain an alpha\-numeric string that is the textual description of the network entity. The system description should include the full name and version identification of the system's hardware type, software operating system, and networking software. If implementations support IETF RFC 3418, the sysDescr object should be used for this field
        	**type**\: str
        
        	**length:** 0..255
        
        .. attribute:: chassis_id
        
        	The Chassis ID is a mandatory TLV which identifies the chassis component of the endpoint identifier associated with the transmitting LLDP agent
        	**type**\: str
        
        .. attribute:: chassis_id_type
        
        	This field identifies the format and source of the chassis identifier string. It is an enumerator defined by the LldpChassisIdSubtype object from IEEE 802.1AB MIB
        	**type**\:  :py:class:`ChassisIdType <ydk.models.openconfig.openconfig_lldp_types.ChassisIdType>`
        
        

        """

        _prefix = 'oc-lldp'
        _revision = '2016-05-16'

        def __init__(self):
            super(Lldp.Config, self).__init__()

            self.yang_name = "config"
            self.yang_parent_name = "lldp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('enabled', YLeaf(YType.boolean, 'enabled')),
                ('hello_timer', YLeaf(YType.uint64, 'hello-timer')),
                ('suppress_tlv_advertisement', YLeafList(YType.identityref, 'suppress-tlv-advertisement')),
                ('system_name', YLeaf(YType.str, 'system-name')),
                ('system_description', YLeaf(YType.str, 'system-description')),
                ('chassis_id', YLeaf(YType.str, 'chassis-id')),
                ('chassis_id_type', YLeaf(YType.enumeration, 'chassis-id-type')),
            ])
            self.enabled = None
            self.hello_timer = None
            self.suppress_tlv_advertisement = []
            self.system_name = None
            self.system_description = None
            self.chassis_id = None
            self.chassis_id_type = None
            self._segment_path = lambda: "config"
            self._absolute_path = lambda: "openconfig-lldp:lldp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Lldp.Config, ['enabled', 'hello_timer', 'suppress_tlv_advertisement', 'system_name', 'system_description', 'chassis_id', 'chassis_id_type'], name, value)


    class State(Entity):
        """
        Operational state data 
        
        .. attribute:: enabled
        
        	System level state of the LLDP protocol
        	**type**\: bool
        
        	**default value**\: true
        
        .. attribute:: hello_timer
        
        	System level hello timer for the LLDP protocol
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: seconds
        
        .. attribute:: suppress_tlv_advertisement
        
        	Indicates whether the local system should suppress the advertisement of particular TLVs with the LLDP PDUs that it transmits. Where a TLV type is specified within this list, it should not be included in any LLDP PDU transmitted by the local agent
        	**type**\: list of   :py:class:`LLDPTLV <ydk.models.openconfig.openconfig_lldp_types.LLDPTLV>`
        
        .. attribute:: system_name
        
        	The system name field shall contain an alpha\-numeric string that indicates the system's administratively assigned name. The system name should be the system's fully qualified domain name. If implementations support IETF RFC 3418, the sysName object should be used for this field
        	**type**\: str
        
        	**length:** 0..255
        
        .. attribute:: system_description
        
        	The system description field shall contain an alpha\-numeric string that is the textual description of the network entity. The system description should include the full name and version identification of the system's hardware type, software operating system, and networking software. If implementations support IETF RFC 3418, the sysDescr object should be used for this field
        	**type**\: str
        
        	**length:** 0..255
        
        .. attribute:: chassis_id
        
        	The Chassis ID is a mandatory TLV which identifies the chassis component of the endpoint identifier associated with the transmitting LLDP agent
        	**type**\: str
        
        .. attribute:: chassis_id_type
        
        	This field identifies the format and source of the chassis identifier string. It is an enumerator defined by the LldpChassisIdSubtype object from IEEE 802.1AB MIB
        	**type**\:  :py:class:`ChassisIdType <ydk.models.openconfig.openconfig_lldp_types.ChassisIdType>`
        
        .. attribute:: counters
        
        	Global LLDP counters
        	**type**\:  :py:class:`Counters <ydk.models.openconfig.openconfig_lldp.Lldp.State.Counters>`
        
        

        """

        _prefix = 'oc-lldp'
        _revision = '2016-05-16'

        def __init__(self):
            super(Lldp.State, self).__init__()

            self.yang_name = "state"
            self.yang_parent_name = "lldp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("counters", ("counters", Lldp.State.Counters))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('enabled', YLeaf(YType.boolean, 'enabled')),
                ('hello_timer', YLeaf(YType.uint64, 'hello-timer')),
                ('suppress_tlv_advertisement', YLeafList(YType.identityref, 'suppress-tlv-advertisement')),
                ('system_name', YLeaf(YType.str, 'system-name')),
                ('system_description', YLeaf(YType.str, 'system-description')),
                ('chassis_id', YLeaf(YType.str, 'chassis-id')),
                ('chassis_id_type', YLeaf(YType.enumeration, 'chassis-id-type')),
            ])
            self.enabled = None
            self.hello_timer = None
            self.suppress_tlv_advertisement = []
            self.system_name = None
            self.system_description = None
            self.chassis_id = None
            self.chassis_id_type = None

            self.counters = Lldp.State.Counters()
            self.counters.parent = self
            self._children_name_map["counters"] = "counters"
            self._children_yang_names.add("counters")
            self._segment_path = lambda: "state"
            self._absolute_path = lambda: "openconfig-lldp:lldp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Lldp.State, ['enabled', 'hello_timer', 'suppress_tlv_advertisement', 'system_name', 'system_description', 'chassis_id', 'chassis_id_type'], name, value)


        class Counters(Entity):
            """
            Global LLDP counters
            
            .. attribute:: frame_in
            
            	The number of lldp frames received
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: frame_out
            
            	The number of frames transmitted out
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: frame_error_in
            
            	The number of LLDP frames received with errors
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: frame_discard
            
            	The number of LLDP frames received and discarded
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: tlv_discard
            
            	The number of TLV frames received and discarded
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: tlv_unknown
            
            	The number of frames received with unknown TLV
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: last_clear
            
            	Indicates the last time the counters were cleared
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: tlv_accepted
            
            	The number of valid TLVs received
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: entries_aged_out
            
            	The number of entries aged out due to timeout
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'oc-lldp'
            _revision = '2016-05-16'

            def __init__(self):
                super(Lldp.State.Counters, self).__init__()

                self.yang_name = "counters"
                self.yang_parent_name = "state"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('frame_in', YLeaf(YType.uint64, 'frame-in')),
                    ('frame_out', YLeaf(YType.uint64, 'frame-out')),
                    ('frame_error_in', YLeaf(YType.uint64, 'frame-error-in')),
                    ('frame_discard', YLeaf(YType.uint64, 'frame-discard')),
                    ('tlv_discard', YLeaf(YType.uint64, 'tlv-discard')),
                    ('tlv_unknown', YLeaf(YType.uint64, 'tlv-unknown')),
                    ('last_clear', YLeaf(YType.str, 'last-clear')),
                    ('tlv_accepted', YLeaf(YType.uint64, 'tlv-accepted')),
                    ('entries_aged_out', YLeaf(YType.uint64, 'entries-aged-out')),
                ])
                self.frame_in = None
                self.frame_out = None
                self.frame_error_in = None
                self.frame_discard = None
                self.tlv_discard = None
                self.tlv_unknown = None
                self.last_clear = None
                self.tlv_accepted = None
                self.entries_aged_out = None
                self._segment_path = lambda: "counters"
                self._absolute_path = lambda: "openconfig-lldp:lldp/state/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Lldp.State.Counters, ['frame_in', 'frame_out', 'frame_error_in', 'frame_discard', 'tlv_discard', 'tlv_unknown', 'last_clear', 'tlv_accepted', 'entries_aged_out'], name, value)


    class Interfaces(Entity):
        """
        Enclosing container 
        
        .. attribute:: interface
        
        	List of interfaces on which LLDP is enabled / available
        	**type**\: list of  		 :py:class:`Interface <ydk.models.openconfig.openconfig_lldp.Lldp.Interfaces.Interface>`
        
        

        """

        _prefix = 'oc-lldp'
        _revision = '2016-05-16'

        def __init__(self):
            super(Lldp.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "lldp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("interface", ("interface", Lldp.Interfaces.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "openconfig-lldp:lldp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Lldp.Interfaces, [], name, value)


        class Interface(Entity):
            """
            List of interfaces on which LLDP is enabled / available
            
            .. attribute:: name  (key)
            
            	Reference to the list key
            	**type**\: str
            
            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_lldp.Lldp.Interfaces.Interface.Config>`
            
            .. attribute:: config
            
            	Configuration data for LLDP on each interface
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_lldp.Lldp.Interfaces.Interface.Config>`
            
            .. attribute:: state
            
            	Operational state data 
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_lldp.Lldp.Interfaces.Interface.State>`
            
            .. attribute:: neighbors
            
            	Enclosing container for list of LLDP neighbors on an interface
            	**type**\:  :py:class:`Neighbors <ydk.models.openconfig.openconfig_lldp.Lldp.Interfaces.Interface.Neighbors>`
            
            

            """

            _prefix = 'oc-lldp'
            _revision = '2016-05-16'

            def __init__(self):
                super(Lldp.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_container_classes = OrderedDict([("config", ("config", Lldp.Interfaces.Interface.Config)), ("state", ("state", Lldp.Interfaces.Interface.State)), ("neighbors", ("neighbors", Lldp.Interfaces.Interface.Neighbors))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', YLeaf(YType.str, 'name')),
                ])
                self.name = None

                self.config = Lldp.Interfaces.Interface.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.state = Lldp.Interfaces.Interface.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")

                self.neighbors = Lldp.Interfaces.Interface.Neighbors()
                self.neighbors.parent = self
                self._children_name_map["neighbors"] = "neighbors"
                self._children_yang_names.add("neighbors")
                self._segment_path = lambda: "interface" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "openconfig-lldp:lldp/interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Lldp.Interfaces.Interface, ['name'], name, value)


            class Config(Entity):
                """
                Configuration data for LLDP on each interface
                
                .. attribute:: name
                
                	Reference to the LLDP Ethernet interface
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                
                .. attribute:: enabled
                
                	Enable or disable the LLDP protocol on the interface
                	**type**\: bool
                
                	**default value**\: true
                
                

                """

                _prefix = 'oc-lldp'
                _revision = '2016-05-16'

                def __init__(self):
                    super(Lldp.Interfaces.Interface.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                        ('enabled', YLeaf(YType.boolean, 'enabled')),
                    ])
                    self.name = None
                    self.enabled = None
                    self._segment_path = lambda: "config"

                def __setattr__(self, name, value):
                    self._perform_setattr(Lldp.Interfaces.Interface.Config, ['name', 'enabled'], name, value)


            class State(Entity):
                """
                Operational state data 
                
                .. attribute:: name
                
                	Reference to the LLDP Ethernet interface
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                
                .. attribute:: enabled
                
                	Enable or disable the LLDP protocol on the interface
                	**type**\: bool
                
                	**default value**\: true
                
                .. attribute:: counters
                
                	LLDP counters on each interface
                	**type**\:  :py:class:`Counters <ydk.models.openconfig.openconfig_lldp.Lldp.Interfaces.Interface.State.Counters>`
                
                

                """

                _prefix = 'oc-lldp'
                _revision = '2016-05-16'

                def __init__(self):
                    super(Lldp.Interfaces.Interface.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("counters", ("counters", Lldp.Interfaces.Interface.State.Counters))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                        ('enabled', YLeaf(YType.boolean, 'enabled')),
                    ])
                    self.name = None
                    self.enabled = None

                    self.counters = Lldp.Interfaces.Interface.State.Counters()
                    self.counters.parent = self
                    self._children_name_map["counters"] = "counters"
                    self._children_yang_names.add("counters")
                    self._segment_path = lambda: "state"

                def __setattr__(self, name, value):
                    self._perform_setattr(Lldp.Interfaces.Interface.State, ['name', 'enabled'], name, value)


                class Counters(Entity):
                    """
                    LLDP counters on each interface
                    
                    .. attribute:: frame_in
                    
                    	The number of lldp frames received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: frame_out
                    
                    	The number of frames transmitted out
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: frame_error_in
                    
                    	The number of LLDP frames received with errors
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: frame_discard
                    
                    	The number of LLDP frames received and discarded
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: tlv_discard
                    
                    	The number of TLV frames received and discarded
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: tlv_unknown
                    
                    	The number of frames received with unknown TLV
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: last_clear
                    
                    	Indicates the last time the counters were cleared
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: frame_error_out
                    
                    	The number of frame transmit errors on the interface
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'oc-lldp'
                    _revision = '2016-05-16'

                    def __init__(self):
                        super(Lldp.Interfaces.Interface.State.Counters, self).__init__()

                        self.yang_name = "counters"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('frame_in', YLeaf(YType.uint64, 'frame-in')),
                            ('frame_out', YLeaf(YType.uint64, 'frame-out')),
                            ('frame_error_in', YLeaf(YType.uint64, 'frame-error-in')),
                            ('frame_discard', YLeaf(YType.uint64, 'frame-discard')),
                            ('tlv_discard', YLeaf(YType.uint64, 'tlv-discard')),
                            ('tlv_unknown', YLeaf(YType.uint64, 'tlv-unknown')),
                            ('last_clear', YLeaf(YType.str, 'last-clear')),
                            ('frame_error_out', YLeaf(YType.uint64, 'frame-error-out')),
                        ])
                        self.frame_in = None
                        self.frame_out = None
                        self.frame_error_in = None
                        self.frame_discard = None
                        self.tlv_discard = None
                        self.tlv_unknown = None
                        self.last_clear = None
                        self.frame_error_out = None
                        self._segment_path = lambda: "counters"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lldp.Interfaces.Interface.State.Counters, ['frame_in', 'frame_out', 'frame_error_in', 'frame_discard', 'tlv_discard', 'tlv_unknown', 'last_clear', 'frame_error_out'], name, value)


            class Neighbors(Entity):
                """
                Enclosing container for list of LLDP neighbors on an
                interface
                
                .. attribute:: neighbor
                
                	List of LLDP neighbors
                	**type**\: list of  		 :py:class:`Neighbor <ydk.models.openconfig.openconfig_lldp.Lldp.Interfaces.Interface.Neighbors.Neighbor>`
                
                

                """

                _prefix = 'oc-lldp'
                _revision = '2016-05-16'

                def __init__(self):
                    super(Lldp.Interfaces.Interface.Neighbors, self).__init__()

                    self.yang_name = "neighbors"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("neighbor", ("neighbor", Lldp.Interfaces.Interface.Neighbors.Neighbor))])
                    self._leafs = OrderedDict()

                    self.neighbor = YList(self)
                    self._segment_path = lambda: "neighbors"

                def __setattr__(self, name, value):
                    self._perform_setattr(Lldp.Interfaces.Interface.Neighbors, [], name, value)


                class Neighbor(Entity):
                    """
                    List of LLDP neighbors
                    
                    .. attribute:: id  (key)
                    
                    	 
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`id <ydk.models.openconfig.openconfig_lldp.Lldp.Interfaces.Interface.Neighbors.Neighbor.State>`
                    
                    .. attribute:: config
                    
                    	Configuration data 
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_lldp.Lldp.Interfaces.Interface.Neighbors.Neighbor.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data 
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_lldp.Lldp.Interfaces.Interface.Neighbors.Neighbor.State>`
                    
                    .. attribute:: custom_tlvs
                    
                    	Enclosing container for list of custom TLVs from a neighbor
                    	**type**\:  :py:class:`CustomTlvs <ydk.models.openconfig.openconfig_lldp.Lldp.Interfaces.Interface.Neighbors.Neighbor.CustomTlvs>`
                    
                    .. attribute:: capabilities
                    
                    	Enclosing container for list of LLDP capabilities
                    	**type**\:  :py:class:`Capabilities <ydk.models.openconfig.openconfig_lldp.Lldp.Interfaces.Interface.Neighbors.Neighbor.Capabilities>`
                    
                    

                    """

                    _prefix = 'oc-lldp'
                    _revision = '2016-05-16'

                    def __init__(self):
                        super(Lldp.Interfaces.Interface.Neighbors.Neighbor, self).__init__()

                        self.yang_name = "neighbor"
                        self.yang_parent_name = "neighbors"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['id']
                        self._child_container_classes = OrderedDict([("config", ("config", Lldp.Interfaces.Interface.Neighbors.Neighbor.Config)), ("state", ("state", Lldp.Interfaces.Interface.Neighbors.Neighbor.State)), ("custom-tlvs", ("custom_tlvs", Lldp.Interfaces.Interface.Neighbors.Neighbor.CustomTlvs)), ("capabilities", ("capabilities", Lldp.Interfaces.Interface.Neighbors.Neighbor.Capabilities))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('id', YLeaf(YType.str, 'id')),
                        ])
                        self.id = None

                        self.config = Lldp.Interfaces.Interface.Neighbors.Neighbor.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Lldp.Interfaces.Interface.Neighbors.Neighbor.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")

                        self.custom_tlvs = Lldp.Interfaces.Interface.Neighbors.Neighbor.CustomTlvs()
                        self.custom_tlvs.parent = self
                        self._children_name_map["custom_tlvs"] = "custom-tlvs"
                        self._children_yang_names.add("custom-tlvs")

                        self.capabilities = Lldp.Interfaces.Interface.Neighbors.Neighbor.Capabilities()
                        self.capabilities.parent = self
                        self._children_name_map["capabilities"] = "capabilities"
                        self._children_yang_names.add("capabilities")
                        self._segment_path = lambda: "neighbor" + "[id='" + str(self.id) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lldp.Interfaces.Interface.Neighbors.Neighbor, ['id'], name, value)


                    class Config(Entity):
                        """
                        Configuration data 
                        
                        

                        """

                        _prefix = 'oc-lldp'
                        _revision = '2016-05-16'

                        def __init__(self):
                            super(Lldp.Interfaces.Interface.Neighbors.Neighbor.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "neighbor"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()
                            self._segment_path = lambda: "config"


                    class State(Entity):
                        """
                        Operational state data 
                        
                        .. attribute:: system_name
                        
                        	The system name field shall contain an alpha\-numeric string that indicates the system's administratively assigned name. The system name should be the system's fully qualified domain name. If implementations support IETF RFC 3418, the sysName object should be used for this field
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        .. attribute:: system_description
                        
                        	The system description field shall contain an alpha\-numeric string that is the textual description of the network entity. The system description should include the full name and version identification of the system's hardware type, software operating system, and networking software. If implementations support IETF RFC 3418, the sysDescr object should be used for this field
                        	**type**\: str
                        
                        	**length:** 0..255
                        
                        .. attribute:: chassis_id
                        
                        	The Chassis ID is a mandatory TLV which identifies the chassis component of the endpoint identifier associated with the transmitting LLDP agent
                        	**type**\: str
                        
                        .. attribute:: chassis_id_type
                        
                        	This field identifies the format and source of the chassis identifier string. It is an enumerator defined by the LldpChassisIdSubtype object from IEEE 802.1AB MIB
                        	**type**\:  :py:class:`ChassisIdType <ydk.models.openconfig.openconfig_lldp_types.ChassisIdType>`
                        
                        .. attribute:: id
                        
                        	System generated identifier for the neighbor on the interface
                        	**type**\: str
                        
                        .. attribute:: age
                        
                        	Age since discovery
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: seconds
                        
                        .. attribute:: last_update
                        
                        	Seconds since last update received
                        	**type**\: int
                        
                        	**range:** \-9223372036854775808..9223372036854775807
                        
                        .. attribute:: port_id
                        
                        	The Port ID is a mandatory TLV which identifies the port component of the endpoint identifier associated with the transmitting LLDP agent. If the specified port is an IEEE 802.3 Repeater port, then this TLV is optional
                        	**type**\: str
                        
                        .. attribute:: port_id_type
                        
                        	This field identifies the format and source of the port identifier string. It is an enumerator defined by the PtopoPortIdType object from RFC2922
                        	**type**\:  :py:class:`PortIdType <ydk.models.openconfig.openconfig_lldp_types.PortIdType>`
                        
                        .. attribute:: port_description
                        
                        	The binary string containing the actual port identifier for the port which this LLDP PDU was transmitted. The source and format of this field is defined by PtopoPortId from RFC2922
                        	**type**\: str
                        
                        .. attribute:: management_address
                        
                        	The Management Address is a mandatory TLV which identifies a network address associated with the local LLDP agent, which can be used to reach the agent on the port identified in the Port ID TLV
                        	**type**\: str
                        
                        .. attribute:: management_address_type
                        
                        	The enumerated value for the network address type identified in this TLV. This enumeration is defined in the 'Assigned Numbers' RFC [RFC3232] and the ianaAddressFamilyNumbers object
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'oc-lldp'
                        _revision = '2016-05-16'

                        def __init__(self):
                            super(Lldp.Interfaces.Interface.Neighbors.Neighbor.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "neighbor"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('system_name', YLeaf(YType.str, 'system-name')),
                                ('system_description', YLeaf(YType.str, 'system-description')),
                                ('chassis_id', YLeaf(YType.str, 'chassis-id')),
                                ('chassis_id_type', YLeaf(YType.enumeration, 'chassis-id-type')),
                                ('id', YLeaf(YType.str, 'id')),
                                ('age', YLeaf(YType.uint64, 'age')),
                                ('last_update', YLeaf(YType.int64, 'last-update')),
                                ('port_id', YLeaf(YType.str, 'port-id')),
                                ('port_id_type', YLeaf(YType.enumeration, 'port-id-type')),
                                ('port_description', YLeaf(YType.str, 'port-description')),
                                ('management_address', YLeaf(YType.str, 'management-address')),
                                ('management_address_type', YLeaf(YType.str, 'management-address-type')),
                            ])
                            self.system_name = None
                            self.system_description = None
                            self.chassis_id = None
                            self.chassis_id_type = None
                            self.id = None
                            self.age = None
                            self.last_update = None
                            self.port_id = None
                            self.port_id_type = None
                            self.port_description = None
                            self.management_address = None
                            self.management_address_type = None
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lldp.Interfaces.Interface.Neighbors.Neighbor.State, ['system_name', 'system_description', 'chassis_id', 'chassis_id_type', 'id', 'age', 'last_update', 'port_id', 'port_id_type', 'port_description', 'management_address', 'management_address_type'], name, value)


                    class CustomTlvs(Entity):
                        """
                        Enclosing container for list of custom TLVs from a
                        neighbor
                        
                        .. attribute:: tlv
                        
                        	List of custom LLDP TLVs from a neighbor
                        	**type**\: list of  		 :py:class:`Tlv <ydk.models.openconfig.openconfig_lldp.Lldp.Interfaces.Interface.Neighbors.Neighbor.CustomTlvs.Tlv>`
                        
                        

                        """

                        _prefix = 'oc-lldp'
                        _revision = '2016-05-16'

                        def __init__(self):
                            super(Lldp.Interfaces.Interface.Neighbors.Neighbor.CustomTlvs, self).__init__()

                            self.yang_name = "custom-tlvs"
                            self.yang_parent_name = "neighbor"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("tlv", ("tlv", Lldp.Interfaces.Interface.Neighbors.Neighbor.CustomTlvs.Tlv))])
                            self._leafs = OrderedDict()

                            self.tlv = YList(self)
                            self._segment_path = lambda: "custom-tlvs"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lldp.Interfaces.Interface.Neighbors.Neighbor.CustomTlvs, [], name, value)


                        class Tlv(Entity):
                            """
                            List of custom LLDP TLVs from a neighbor
                            
                            .. attribute:: type  (key)
                            
                            	Reference to type list key
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**refers to**\:  :py:class:`type <ydk.models.openconfig.openconfig_lldp.Lldp.Interfaces.Interface.Neighbors.Neighbor.CustomTlvs.Tlv.State>`
                            
                            .. attribute:: oui  (key)
                            
                            	Reference to oui list key
                            	**type**\: str
                            
                            	**refers to**\:  :py:class:`oui <ydk.models.openconfig.openconfig_lldp.Lldp.Interfaces.Interface.Neighbors.Neighbor.CustomTlvs.Tlv.State>`
                            
                            .. attribute:: oui_subtype  (key)
                            
                            	Reference to oui\-subtype list key
                            	**type**\: str
                            
                            	**refers to**\:  :py:class:`oui_subtype <ydk.models.openconfig.openconfig_lldp.Lldp.Interfaces.Interface.Neighbors.Neighbor.CustomTlvs.Tlv.State>`
                            
                            .. attribute:: config
                            
                            	Configuration data 
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_lldp.Lldp.Interfaces.Interface.Neighbors.Neighbor.CustomTlvs.Tlv.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state data 
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_lldp.Lldp.Interfaces.Interface.Neighbors.Neighbor.CustomTlvs.Tlv.State>`
                            
                            

                            """

                            _prefix = 'oc-lldp'
                            _revision = '2016-05-16'

                            def __init__(self):
                                super(Lldp.Interfaces.Interface.Neighbors.Neighbor.CustomTlvs.Tlv, self).__init__()

                                self.yang_name = "tlv"
                                self.yang_parent_name = "custom-tlvs"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['type','oui','oui_subtype']
                                self._child_container_classes = OrderedDict([("config", ("config", Lldp.Interfaces.Interface.Neighbors.Neighbor.CustomTlvs.Tlv.Config)), ("state", ("state", Lldp.Interfaces.Interface.Neighbors.Neighbor.CustomTlvs.Tlv.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('type', YLeaf(YType.str, 'type')),
                                    ('oui', YLeaf(YType.str, 'oui')),
                                    ('oui_subtype', YLeaf(YType.str, 'oui-subtype')),
                                ])
                                self.type = None
                                self.oui = None
                                self.oui_subtype = None

                                self.config = Lldp.Interfaces.Interface.Neighbors.Neighbor.CustomTlvs.Tlv.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Lldp.Interfaces.Interface.Neighbors.Neighbor.CustomTlvs.Tlv.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "tlv" + "[type='" + str(self.type) + "']" + "[oui='" + str(self.oui) + "']" + "[oui-subtype='" + str(self.oui_subtype) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lldp.Interfaces.Interface.Neighbors.Neighbor.CustomTlvs.Tlv, ['type', 'oui', 'oui_subtype'], name, value)


                            class Config(Entity):
                                """
                                Configuration data 
                                
                                

                                """

                                _prefix = 'oc-lldp'
                                _revision = '2016-05-16'

                                def __init__(self):
                                    super(Lldp.Interfaces.Interface.Neighbors.Neighbor.CustomTlvs.Tlv.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "tlv"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict()
                                    self._segment_path = lambda: "config"


                            class State(Entity):
                                """
                                Operational state data 
                                
                                .. attribute:: type
                                
                                	The integer value identifying the type of information contained in the value field
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: oui
                                
                                	The organizationally unique identifier field shall contain the organization's OUI as defined in Clause 9 of IEEE Std 802. The high\-order octet is 0 and the low\-order 3 octets are the SMI Network Management Private Enterprise Code of the Vendor in network byte order, as defined in the 'Assigned Numbers' RFC [RFC3232]
                                	**type**\: str
                                
                                .. attribute:: oui_subtype
                                
                                	The organizationally defined subtype field shall contain a unique subtype value assigned by the defining organization
                                	**type**\: str
                                
                                .. attribute:: value
                                
                                	A variable\-length octet\-string containing the instance\-specific information for this TLV
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'oc-lldp'
                                _revision = '2016-05-16'

                                def __init__(self):
                                    super(Lldp.Interfaces.Interface.Neighbors.Neighbor.CustomTlvs.Tlv.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "tlv"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('type', YLeaf(YType.int32, 'type')),
                                        ('oui', YLeaf(YType.str, 'oui')),
                                        ('oui_subtype', YLeaf(YType.str, 'oui-subtype')),
                                        ('value', YLeaf(YType.str, 'value')),
                                    ])
                                    self.type = None
                                    self.oui = None
                                    self.oui_subtype = None
                                    self.value = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Lldp.Interfaces.Interface.Neighbors.Neighbor.CustomTlvs.Tlv.State, ['type', 'oui', 'oui_subtype', 'value'], name, value)


                    class Capabilities(Entity):
                        """
                        Enclosing container for list of LLDP capabilities
                        
                        .. attribute:: capability
                        
                        	List of LLDP system capabilities advertised by the neighbor
                        	**type**\: list of  		 :py:class:`Capability <ydk.models.openconfig.openconfig_lldp.Lldp.Interfaces.Interface.Neighbors.Neighbor.Capabilities.Capability>`
                        
                        

                        """

                        _prefix = 'oc-lldp'
                        _revision = '2016-05-16'

                        def __init__(self):
                            super(Lldp.Interfaces.Interface.Neighbors.Neighbor.Capabilities, self).__init__()

                            self.yang_name = "capabilities"
                            self.yang_parent_name = "neighbor"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("capability", ("capability", Lldp.Interfaces.Interface.Neighbors.Neighbor.Capabilities.Capability))])
                            self._leafs = OrderedDict()

                            self.capability = YList(self)
                            self._segment_path = lambda: "capabilities"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lldp.Interfaces.Interface.Neighbors.Neighbor.Capabilities, [], name, value)


                        class Capability(Entity):
                            """
                            List of LLDP system capabilities advertised by the
                            neighbor
                            
                            .. attribute:: name  (key)
                            
                            	Reference to capabilities list key
                            	**type**\:  :py:class:`LLDPSYSTEMCAPABILITY <ydk.models.openconfig.openconfig_lldp_types.LLDPSYSTEMCAPABILITY>`
                            
                            .. attribute:: config
                            
                            	Configuration data for LLDP capabilities
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_lldp.Lldp.Interfaces.Interface.Neighbors.Neighbor.Capabilities.Capability.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state data for LLDP capabilities
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_lldp.Lldp.Interfaces.Interface.Neighbors.Neighbor.Capabilities.Capability.State>`
                            
                            

                            """

                            _prefix = 'oc-lldp'
                            _revision = '2016-05-16'

                            def __init__(self):
                                super(Lldp.Interfaces.Interface.Neighbors.Neighbor.Capabilities.Capability, self).__init__()

                                self.yang_name = "capability"
                                self.yang_parent_name = "capabilities"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['name']
                                self._child_container_classes = OrderedDict([("config", ("config", Lldp.Interfaces.Interface.Neighbors.Neighbor.Capabilities.Capability.Config)), ("state", ("state", Lldp.Interfaces.Interface.Neighbors.Neighbor.Capabilities.Capability.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('name', YLeaf(YType.identityref, 'name')),
                                ])
                                self.name = None

                                self.config = Lldp.Interfaces.Interface.Neighbors.Neighbor.Capabilities.Capability.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Lldp.Interfaces.Interface.Neighbors.Neighbor.Capabilities.Capability.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "capability" + "[name='" + str(self.name) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lldp.Interfaces.Interface.Neighbors.Neighbor.Capabilities.Capability, ['name'], name, value)


                            class Config(Entity):
                                """
                                Configuration data for LLDP capabilities
                                
                                

                                """

                                _prefix = 'oc-lldp'
                                _revision = '2016-05-16'

                                def __init__(self):
                                    super(Lldp.Interfaces.Interface.Neighbors.Neighbor.Capabilities.Capability.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "capability"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict()
                                    self._segment_path = lambda: "config"


                            class State(Entity):
                                """
                                Operational state data for LLDP capabilities
                                
                                .. attribute:: name
                                
                                	Name of the system capability advertised by the neighbor. Capabilities are represented in a bitmap that defines the primary functions of the system. The capabilities are defined in IEEE 802.1AB
                                	**type**\:  :py:class:`LLDPSYSTEMCAPABILITY <ydk.models.openconfig.openconfig_lldp_types.LLDPSYSTEMCAPABILITY>`
                                
                                .. attribute:: enabled
                                
                                	Indicates whether the corresponding system capability is enabled on the neighbor
                                	**type**\: bool
                                
                                

                                """

                                _prefix = 'oc-lldp'
                                _revision = '2016-05-16'

                                def __init__(self):
                                    super(Lldp.Interfaces.Interface.Neighbors.Neighbor.Capabilities.Capability.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "capability"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('name', YLeaf(YType.identityref, 'name')),
                                        ('enabled', YLeaf(YType.boolean, 'enabled')),
                                    ])
                                    self.name = None
                                    self.enabled = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Lldp.Interfaces.Interface.Neighbors.Neighbor.Capabilities.Capability.State, ['name', 'enabled'], name, value)

    def clone_ptr(self):
        self._top_entity = Lldp()
        return self._top_entity


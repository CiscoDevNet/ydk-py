""" openconfig_vlan 

This module defines configuration and state variables for VLANs,
in addition to VLAN parameters associated with interfaces

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Vlans(Entity):
    """
    Container for VLAN configuration and state
    variables
    
    .. attribute:: vlan
    
    	Configured VLANs keyed by id
    	**type**\: list of    :py:class:`Vlan <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan>`
    
    

    """

    _prefix = 'oc-vlan'
    _revision = '2016-05-26'

    def __init__(self):
        super(Vlans, self).__init__()
        self._top_entity = None

        self.yang_name = "vlans"
        self.yang_parent_name = "openconfig-vlan"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"vlan" : ("vlan", Vlans.Vlan)}

        self.vlan = YList(self)
        self._segment_path = lambda: "openconfig-vlan:vlans"

    def __setattr__(self, name, value):
        self._perform_setattr(Vlans, [], name, value)


    class Vlan(Entity):
        """
        Configured VLANs keyed by id
        
        .. attribute:: vlan_id  <key>
        
        	references the configured vlan\-id
        	**type**\:  int
        
        	**range:** 1..4094
        
        	**refers to**\:  :py:class:`vlan_id <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan.Config>`
        
        .. attribute:: config
        
        	Configuration parameters for VLANs
        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan.Config>`
        
        .. attribute:: members
        
        	Enclosing container for list of member interfaces
        	**type**\:   :py:class:`Members <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan.Members>`
        
        .. attribute:: state
        
        	State variables for VLANs
        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan.State>`
        
        

        """

        _prefix = 'oc-vlan'
        _revision = '2016-05-26'

        def __init__(self):
            super(Vlans.Vlan, self).__init__()

            self.yang_name = "vlan"
            self.yang_parent_name = "vlans"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"config" : ("config", Vlans.Vlan.Config), "members" : ("members", Vlans.Vlan.Members), "state" : ("state", Vlans.Vlan.State)}
            self._child_list_classes = {}

            self.vlan_id = YLeaf(YType.str, "vlan-id")

            self.config = Vlans.Vlan.Config()
            self.config.parent = self
            self._children_name_map["config"] = "config"
            self._children_yang_names.add("config")

            self.members = Vlans.Vlan.Members()
            self.members.parent = self
            self._children_name_map["members"] = "members"
            self._children_yang_names.add("members")

            self.state = Vlans.Vlan.State()
            self.state.parent = self
            self._children_name_map["state"] = "state"
            self._children_yang_names.add("state")
            self._segment_path = lambda: "vlan" + "[vlan-id='" + self.vlan_id.get() + "']"
            self._absolute_path = lambda: "openconfig-vlan:vlans/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Vlans.Vlan, ['vlan_id'], name, value)


        class Config(Entity):
            """
            Configuration parameters for VLANs
            
            .. attribute:: name
            
            	Interface VLAN name
            	**type**\:  str
            
            .. attribute:: status
            
            	Admin state of the VLAN
            	**type**\:   :py:class:`Status <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan.Config.Status>`
            
            	**default value**\: ACTIVE
            
            .. attribute:: tpid
            
            	Optionally set the tag protocol identifier field (TPID) that is accepted on the VLAN
            	**type**\:   :py:class:`TPIDTYPES <ydk.models.openconfig.openconfig_vlan_types.TPIDTYPES>`
            
            	**default value**\: oc-vlan-types:TPID_0x8100
            
            .. attribute:: vlan_id
            
            	Interface VLAN id
            	**type**\:  int
            
            	**range:** 1..4094
            
            

            """

            _prefix = 'oc-vlan'
            _revision = '2016-05-26'

            def __init__(self):
                super(Vlans.Vlan.Config, self).__init__()

                self.yang_name = "config"
                self.yang_parent_name = "vlan"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.name = YLeaf(YType.str, "name")

                self.status = YLeaf(YType.enumeration, "status")

                self.tpid = YLeaf(YType.identityref, "tpid")

                self.vlan_id = YLeaf(YType.uint16, "vlan-id")
                self._segment_path = lambda: "config"

            def __setattr__(self, name, value):
                self._perform_setattr(Vlans.Vlan.Config, ['name', 'status', 'tpid', 'vlan_id'], name, value)

            class Status(Enum):
                """
                Status

                Admin state of the VLAN

                .. data:: ACTIVE = 0

                	VLAN is active

                .. data:: SUSPENDED = 1

                	VLAN is inactive / suspended

                """

                ACTIVE = Enum.YLeaf(0, "ACTIVE")

                SUSPENDED = Enum.YLeaf(1, "SUSPENDED")



        class Members(Entity):
            """
            Enclosing container for list of member interfaces
            
            .. attribute:: member
            
            	List of references to interfaces / subinterfaces associated with the VLAN
            	**type**\: list of    :py:class:`Member <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan.Members.Member>`
            
            

            """

            _prefix = 'oc-vlan'
            _revision = '2016-05-26'

            def __init__(self):
                super(Vlans.Vlan.Members, self).__init__()

                self.yang_name = "members"
                self.yang_parent_name = "vlan"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"member" : ("member", Vlans.Vlan.Members.Member)}

                self.member = YList(self)
                self._segment_path = lambda: "members"

            def __setattr__(self, name, value):
                self._perform_setattr(Vlans.Vlan.Members, [], name, value)


            class Member(Entity):
                """
                List of references to interfaces / subinterfaces
                associated with the VLAN.
                
                .. attribute:: interface_ref
                
                	Reference to an interface or subinterface
                	**type**\:   :py:class:`InterfaceRef <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan.Members.Member.InterfaceRef>`
                
                

                """

                _prefix = 'oc-vlan'
                _revision = '2016-05-26'

                def __init__(self):
                    super(Vlans.Vlan.Members.Member, self).__init__()

                    self.yang_name = "member"
                    self.yang_parent_name = "members"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"interface-ref" : ("interface_ref", Vlans.Vlan.Members.Member.InterfaceRef)}
                    self._child_list_classes = {}

                    self.interface_ref = Vlans.Vlan.Members.Member.InterfaceRef()
                    self.interface_ref.parent = self
                    self._children_name_map["interface_ref"] = "interface-ref"
                    self._children_yang_names.add("interface-ref")
                    self._segment_path = lambda: "member"


                class InterfaceRef(Entity):
                    """
                    Reference to an interface or subinterface
                    
                    .. attribute:: state
                    
                    	Operational state for interface\-ref
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan.Members.Member.InterfaceRef.State>`
                    
                    

                    """

                    _prefix = 'oc-vlan'
                    _revision = '2016-05-26'

                    def __init__(self):
                        super(Vlans.Vlan.Members.Member.InterfaceRef, self).__init__()

                        self.yang_name = "interface-ref"
                        self.yang_parent_name = "member"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"state" : ("state", Vlans.Vlan.Members.Member.InterfaceRef.State)}
                        self._child_list_classes = {}

                        self.state = Vlans.Vlan.Members.Member.InterfaceRef.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "interface-ref"


                    class State(Entity):
                        """
                        Operational state for interface\-ref
                        
                        .. attribute:: interface
                        
                        	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                        
                        .. attribute:: subinterface
                        
                        	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                        
                        

                        """

                        _prefix = 'oc-vlan'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Vlans.Vlan.Members.Member.InterfaceRef.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "interface-ref"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.interface = YLeaf(YType.str, "interface")

                            self.subinterface = YLeaf(YType.str, "subinterface")
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vlans.Vlan.Members.Member.InterfaceRef.State, ['interface', 'subinterface'], name, value)


        class State(Entity):
            """
            State variables for VLANs
            
            .. attribute:: name
            
            	Interface VLAN name
            	**type**\:  str
            
            .. attribute:: status
            
            	Admin state of the VLAN
            	**type**\:   :py:class:`Status <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan.State.Status>`
            
            	**default value**\: ACTIVE
            
            .. attribute:: tpid
            
            	Optionally set the tag protocol identifier field (TPID) that is accepted on the VLAN
            	**type**\:   :py:class:`TPIDTYPES <ydk.models.openconfig.openconfig_vlan_types.TPIDTYPES>`
            
            	**default value**\: oc-vlan-types:TPID_0x8100
            
            .. attribute:: vlan_id
            
            	Interface VLAN id
            	**type**\:  int
            
            	**range:** 1..4094
            
            

            """

            _prefix = 'oc-vlan'
            _revision = '2016-05-26'

            def __init__(self):
                super(Vlans.Vlan.State, self).__init__()

                self.yang_name = "state"
                self.yang_parent_name = "vlan"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.name = YLeaf(YType.str, "name")

                self.status = YLeaf(YType.enumeration, "status")

                self.tpid = YLeaf(YType.identityref, "tpid")

                self.vlan_id = YLeaf(YType.uint16, "vlan-id")
                self._segment_path = lambda: "state"

            def __setattr__(self, name, value):
                self._perform_setattr(Vlans.Vlan.State, ['name', 'status', 'tpid', 'vlan_id'], name, value)

            class Status(Enum):
                """
                Status

                Admin state of the VLAN

                .. data:: ACTIVE = 0

                	VLAN is active

                .. data:: SUSPENDED = 1

                	VLAN is inactive / suspended

                """

                ACTIVE = Enum.YLeaf(0, "ACTIVE")

                SUSPENDED = Enum.YLeaf(1, "SUSPENDED")


    def clone_ptr(self):
        self._top_entity = Vlans()
        return self._top_entity


""" openconfig_acl 

This module defines configuration and operational state
data for network access control lists (i.e., filters, rules,
etc.).  ACLs are organized into ACL sets, with each set
containing one or more ACL entries.  ACL sets are identified
by a unique name, while each entry within a set is assigned
a sequence\-id that determines the order in which the ACL
rules are applied to a packet.

Individual ACL rules specify match criteria based on fields in
the packet, along with an action that defines how matching
packets should be handled. Entries have a type that indicates
the type of match criteria, e.g., MAC layer, IPv4, IPv6, etc.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class ACLTYPE(Identity):
    """
    Base identity for types of ACL sets
    
    

    """

    _prefix = 'oc-acl'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/acl", pref="openconfig-acl", tag="openconfig-acl:ACL_TYPE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ACLTYPE, self).__init__(ns, pref, tag)



class FORWARDINGACTION(Identity):
    """
    Base identity for actions in the forwarding category
    
    

    """

    _prefix = 'oc-acl'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/acl", pref="openconfig-acl", tag="openconfig-acl:FORWARDING_ACTION"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FORWARDINGACTION, self).__init__(ns, pref, tag)



class LOGACTION(Identity):
    """
    Base identity for defining the destination for logging
    actions
    
    

    """

    _prefix = 'oc-acl'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/acl", pref="openconfig-acl", tag="openconfig-acl:LOG_ACTION"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(LOGACTION, self).__init__(ns, pref, tag)



class ACLCOUNTERCAPABILITY(Identity):
    """
    Base identity for system to indicate how it is able to report
    counters
    
    

    """

    _prefix = 'oc-acl'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/acl", pref="openconfig-acl", tag="openconfig-acl:ACL_COUNTER_CAPABILITY"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ACLCOUNTERCAPABILITY, self).__init__(ns, pref, tag)



class Acl(_Entity_):
    """
    Top level enclosing container for ACL model config
    and operational state data
    
    .. attribute:: config
    
    	Global config data for ACLs
    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_acl.Acl.Config>`
    
    .. attribute:: state
    
    	Global operational state data for ACLs
    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_acl.Acl.State>`
    
    	**config**\: False
    
    .. attribute:: acl_sets
    
    	Access list entries variables enclosing container
    	**type**\:  :py:class:`AclSets <ydk.models.openconfig.openconfig_acl.Acl.AclSets>`
    
    .. attribute:: interfaces
    
    	Enclosing container for the list of interfaces on which ACLs are set
    	**type**\:  :py:class:`Interfaces <ydk.models.openconfig.openconfig_acl.Acl.Interfaces>`
    
    

    """

    _prefix = 'oc-acl'
    _revision = '2017-05-26'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Acl, self).__init__()
        self._top_entity = None

        self.yang_name = "acl"
        self.yang_parent_name = "openconfig-acl"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("config", ("config", Acl.Config)), ("state", ("state", Acl.State)), ("acl-sets", ("acl_sets", Acl.AclSets)), ("interfaces", ("interfaces", Acl.Interfaces))])
        self._leafs = OrderedDict()

        self.config = Acl.Config()
        self.config.parent = self
        self._children_name_map["config"] = "config"

        self.state = Acl.State()
        self.state.parent = self
        self._children_name_map["state"] = "state"

        self.acl_sets = Acl.AclSets()
        self.acl_sets.parent = self
        self._children_name_map["acl_sets"] = "acl-sets"

        self.interfaces = Acl.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._segment_path = lambda: "openconfig-acl:acl"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Acl, [], name, value)


    class Config(_Entity_):
        """
        Global config data for ACLs
        
        

        """

        _prefix = 'oc-acl'
        _revision = '2017-05-26'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Acl.Config, self).__init__()

            self.yang_name = "config"
            self.yang_parent_name = "acl"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict()
            self._segment_path = lambda: "config"
            self._absolute_path = lambda: "openconfig-acl:acl/%s" % self._segment_path()
            self._is_frozen = True



    class State(_Entity_):
        """
        Global operational state data for ACLs
        
        .. attribute:: counter_capability
        
        	System reported indication of how ACL counters are reported by the target
        	**type**\:  :py:class:`ACLCOUNTERCAPABILITY <ydk.models.openconfig.openconfig_acl.ACLCOUNTERCAPABILITY>`
        
        	**config**\: False
        
        

        """

        _prefix = 'oc-acl'
        _revision = '2017-05-26'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Acl.State, self).__init__()

            self.yang_name = "state"
            self.yang_parent_name = "acl"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('counter_capability', (YLeaf(YType.identityref, 'counter-capability'), [('ydk.models.openconfig.openconfig_acl', 'ACLCOUNTERCAPABILITY')])),
            ])
            self.counter_capability = None
            self._segment_path = lambda: "state"
            self._absolute_path = lambda: "openconfig-acl:acl/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Acl.State, ['counter_capability'], name, value)



    class AclSets(_Entity_):
        """
        Access list entries variables enclosing container
        
        .. attribute:: acl_set
        
        	List of ACL sets, each comprising of a list of ACL entries
        	**type**\: list of  		 :py:class:`AclSet <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet>`
        
        

        """

        _prefix = 'oc-acl'
        _revision = '2017-05-26'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Acl.AclSets, self).__init__()

            self.yang_name = "acl-sets"
            self.yang_parent_name = "acl"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("acl-set", ("acl_set", Acl.AclSets.AclSet))])
            self._leafs = OrderedDict()

            self.acl_set = YList(self)
            self._segment_path = lambda: "acl-sets"
            self._absolute_path = lambda: "openconfig-acl:acl/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Acl.AclSets, [], name, value)


        class AclSet(_Entity_):
            """
            List of ACL sets, each comprising of a list of ACL
            entries
            
            .. attribute:: name  (key)
            
            	Reference to the name list key
            	**type**\: str
            
            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.Config>`
            
            .. attribute:: type  (key)
            
            	Reference to the type list key
            	**type**\:  :py:class:`ACLTYPE <ydk.models.openconfig.openconfig_acl.ACLTYPE>`
            
            .. attribute:: config
            
            	Access list config
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.Config>`
            
            .. attribute:: state
            
            	Access list state information
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.State>`
            
            	**config**\: False
            
            .. attribute:: acl_entries
            
            	Access list entries container
            	**type**\:  :py:class:`AclEntries <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries>`
            
            

            """

            _prefix = 'oc-acl'
            _revision = '2017-05-26'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Acl.AclSets.AclSet, self).__init__()

                self.yang_name = "acl-set"
                self.yang_parent_name = "acl-sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name','type']
                self._child_classes = OrderedDict([("config", ("config", Acl.AclSets.AclSet.Config)), ("state", ("state", Acl.AclSets.AclSet.State)), ("acl-entries", ("acl_entries", Acl.AclSets.AclSet.AclEntries))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('type', (YLeaf(YType.identityref, 'type'), [('ydk.models.openconfig.openconfig_acl', 'ACLTYPE')])),
                ])
                self.name = None
                self.type = None

                self.config = Acl.AclSets.AclSet.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = Acl.AclSets.AclSet.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"

                self.acl_entries = Acl.AclSets.AclSet.AclEntries()
                self.acl_entries.parent = self
                self._children_name_map["acl_entries"] = "acl-entries"
                self._segment_path = lambda: "acl-set" + "[name='" + str(self.name) + "']" + "[type='" + str(self.type) + "']"
                self._absolute_path = lambda: "openconfig-acl:acl/acl-sets/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Acl.AclSets.AclSet, ['name', 'type'], name, value)


            class Config(_Entity_):
                """
                Access list config
                
                .. attribute:: name
                
                	The name of the access\-list set
                	**type**\: str
                
                .. attribute:: type
                
                	The type determines the fields allowed in the ACL entries belonging to the ACL set (e.g., IPv4, IPv6, etc.)
                	**type**\:  :py:class:`ACLTYPE <ydk.models.openconfig.openconfig_acl.ACLTYPE>`
                
                .. attribute:: description
                
                	Description, or comment, for the ACL set
                	**type**\: str
                
                

                """

                _prefix = 'oc-acl'
                _revision = '2017-05-26'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Acl.AclSets.AclSet.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "acl-set"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('type', (YLeaf(YType.identityref, 'type'), [('ydk.models.openconfig.openconfig_acl', 'ACLTYPE')])),
                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                    ])
                    self.name = None
                    self.type = None
                    self.description = None
                    self._segment_path = lambda: "config"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Acl.AclSets.AclSet.Config, ['name', 'type', 'description'], name, value)



            class State(_Entity_):
                """
                Access list state information
                
                .. attribute:: name
                
                	The name of the access\-list set
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: type
                
                	The type determines the fields allowed in the ACL entries belonging to the ACL set (e.g., IPv4, IPv6, etc.)
                	**type**\:  :py:class:`ACLTYPE <ydk.models.openconfig.openconfig_acl.ACLTYPE>`
                
                	**config**\: False
                
                .. attribute:: description
                
                	Description, or comment, for the ACL set
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-acl'
                _revision = '2017-05-26'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Acl.AclSets.AclSet.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "acl-set"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('type', (YLeaf(YType.identityref, 'type'), [('ydk.models.openconfig.openconfig_acl', 'ACLTYPE')])),
                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                    ])
                    self.name = None
                    self.type = None
                    self.description = None
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Acl.AclSets.AclSet.State, ['name', 'type', 'description'], name, value)



            class AclEntries(_Entity_):
                """
                Access list entries container
                
                .. attribute:: acl_entry
                
                	List of ACL entries comprising an ACL set
                	**type**\: list of  		 :py:class:`AclEntry <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry>`
                
                

                """

                _prefix = 'oc-acl'
                _revision = '2017-05-26'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Acl.AclSets.AclSet.AclEntries, self).__init__()

                    self.yang_name = "acl-entries"
                    self.yang_parent_name = "acl-set"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("acl-entry", ("acl_entry", Acl.AclSets.AclSet.AclEntries.AclEntry))])
                    self._leafs = OrderedDict()

                    self.acl_entry = YList(self)
                    self._segment_path = lambda: "acl-entries"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Acl.AclSets.AclSet.AclEntries, [], name, value)


                class AclEntry(_Entity_):
                    """
                    List of ACL entries comprising an ACL set
                    
                    .. attribute:: sequence_id  (key)
                    
                    	references the list key
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**refers to**\:  :py:class:`sequence_id <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry.Config>`
                    
                    .. attribute:: config
                    
                    	Access list entries config
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry.Config>`
                    
                    .. attribute:: state
                    
                    	State information for ACL entries
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry.State>`
                    
                    	**config**\: False
                    
                    .. attribute:: l2
                    
                    	Ethernet header fields
                    	**type**\:  :py:class:`L2 <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry.L2>`
                    
                    .. attribute:: ipv4
                    
                    	Top level container for IPv4 match field data
                    	**type**\:  :py:class:`Ipv4 <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv4>`
                    
                    .. attribute:: ipv6
                    
                    	Top\-level container for IPv6 match field data
                    	**type**\:  :py:class:`Ipv6 <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv6>`
                    
                    .. attribute:: transport
                    
                    	Transport fields container
                    	**type**\:  :py:class:`Transport <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry.Transport>`
                    
                    .. attribute:: input_interface
                    
                    	Input interface container
                    	**type**\:  :py:class:`InputInterface <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface>`
                    
                    .. attribute:: actions
                    
                    	Enclosing container for list of ACL actions associated with an entry
                    	**type**\:  :py:class:`Actions <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry.Actions>`
                    
                    

                    """

                    _prefix = 'oc-acl'
                    _revision = '2017-05-26'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Acl.AclSets.AclSet.AclEntries.AclEntry, self).__init__()

                        self.yang_name = "acl-entry"
                        self.yang_parent_name = "acl-entries"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['sequence_id']
                        self._child_classes = OrderedDict([("config", ("config", Acl.AclSets.AclSet.AclEntries.AclEntry.Config)), ("state", ("state", Acl.AclSets.AclSet.AclEntries.AclEntry.State)), ("l2", ("l2", Acl.AclSets.AclSet.AclEntries.AclEntry.L2)), ("ipv4", ("ipv4", Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv4)), ("ipv6", ("ipv6", Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv6)), ("transport", ("transport", Acl.AclSets.AclSet.AclEntries.AclEntry.Transport)), ("input-interface", ("input_interface", Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface)), ("actions", ("actions", Acl.AclSets.AclSet.AclEntries.AclEntry.Actions))])
                        self._leafs = OrderedDict([
                            ('sequence_id', (YLeaf(YType.str, 'sequence-id'), ['int'])),
                        ])
                        self.sequence_id = None

                        self.config = Acl.AclSets.AclSet.AclEntries.AclEntry.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = Acl.AclSets.AclSet.AclEntries.AclEntry.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"

                        self.l2 = Acl.AclSets.AclSet.AclEntries.AclEntry.L2()
                        self.l2.parent = self
                        self._children_name_map["l2"] = "l2"

                        self.ipv4 = Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv4()
                        self.ipv4.parent = self
                        self._children_name_map["ipv4"] = "ipv4"

                        self.ipv6 = Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv6()
                        self.ipv6.parent = self
                        self._children_name_map["ipv6"] = "ipv6"

                        self.transport = Acl.AclSets.AclSet.AclEntries.AclEntry.Transport()
                        self.transport.parent = self
                        self._children_name_map["transport"] = "transport"

                        self.input_interface = Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface()
                        self.input_interface.parent = self
                        self._children_name_map["input_interface"] = "input-interface"

                        self.actions = Acl.AclSets.AclSet.AclEntries.AclEntry.Actions()
                        self.actions.parent = self
                        self._children_name_map["actions"] = "actions"
                        self._segment_path = lambda: "acl-entry" + "[sequence-id='" + str(self.sequence_id) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Acl.AclSets.AclSet.AclEntries.AclEntry, ['sequence_id'], name, value)


                    class Config(_Entity_):
                        """
                        Access list entries config
                        
                        .. attribute:: sequence_id
                        
                        	The sequence id determines the order in which ACL entries are applied.  The sequence id must be unique for each entry in an ACL set.  Target devices should apply the ACL entry rules in the order determined by sequence id, rather than the relying only on order in the list
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: description
                        
                        	A user\-defined description, or comment, for this Access List Entry
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'oc-acl'
                        _revision = '2017-05-26'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Acl.AclSets.AclSet.AclEntries.AclEntry.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "acl-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sequence_id', (YLeaf(YType.uint32, 'sequence-id'), ['int'])),
                                ('description', (YLeaf(YType.str, 'description'), ['str'])),
                            ])
                            self.sequence_id = None
                            self.description = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Acl.AclSets.AclSet.AclEntries.AclEntry.Config, ['sequence_id', 'description'], name, value)



                    class State(_Entity_):
                        """
                        State information for ACL entries
                        
                        .. attribute:: sequence_id
                        
                        	The sequence id determines the order in which ACL entries are applied.  The sequence id must be unique for each entry in an ACL set.  Target devices should apply the ACL entry rules in the order determined by sequence id, rather than the relying only on order in the list
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: description
                        
                        	A user\-defined description, or comment, for this Access List Entry
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: matched_packets
                        
                        	Count of the number of packets matching the current ACL entry.  An implementation should provide this counter on a per\-interface per\-ACL\-entry if possible.  If an implementation only supports ACL counters per entry (i.e., not broken out per interface), then the value should be equal to the aggregate count across all interfaces.  An implementation that provides counters per entry per interface is not required to also provide an aggregate count, e.g., per entry \-\- the user is expected to be able implement the required aggregation if such a count is needed
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: matched_octets
                        
                        	Count of the number of octets (bytes) matching the current ACL entry.  An implementation should provide this counter on a per\-interface per\-ACL\-entry if possible.  If an implementation only supports ACL counters per entry (i.e., not broken out per interface), then the value should be equal to the aggregate count across all interfaces.  An implementation that provides counters per entry per interface is not required to also provide an aggregate count, e.g., per entry \-\- the user is expected to be able implement the required aggregation if such a count is needed
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-acl'
                        _revision = '2017-05-26'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Acl.AclSets.AclSet.AclEntries.AclEntry.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "acl-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sequence_id', (YLeaf(YType.uint32, 'sequence-id'), ['int'])),
                                ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                ('matched_packets', (YLeaf(YType.uint64, 'matched-packets'), ['int'])),
                                ('matched_octets', (YLeaf(YType.uint64, 'matched-octets'), ['int'])),
                            ])
                            self.sequence_id = None
                            self.description = None
                            self.matched_packets = None
                            self.matched_octets = None
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Acl.AclSets.AclSet.AclEntries.AclEntry.State, ['sequence_id', 'description', 'matched_packets', 'matched_octets'], name, value)



                    class L2(_Entity_):
                        """
                        Ethernet header fields
                        
                        .. attribute:: config
                        
                        	Configuration data
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry.L2.Config>`
                        
                        .. attribute:: state
                        
                        	State Information
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry.L2.State>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-acl'
                        _revision = '2017-05-26'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Acl.AclSets.AclSet.AclEntries.AclEntry.L2, self).__init__()

                            self.yang_name = "l2"
                            self.yang_parent_name = "acl-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("config", ("config", Acl.AclSets.AclSet.AclEntries.AclEntry.L2.Config)), ("state", ("state", Acl.AclSets.AclSet.AclEntries.AclEntry.L2.State))])
                            self._leafs = OrderedDict()

                            self.config = Acl.AclSets.AclSet.AclEntries.AclEntry.L2.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"

                            self.state = Acl.AclSets.AclSet.AclEntries.AclEntry.L2.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._segment_path = lambda: "l2"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Acl.AclSets.AclSet.AclEntries.AclEntry.L2, [], name, value)


                        class Config(_Entity_):
                            """
                            Configuration data
                            
                            .. attribute:: source_mac
                            
                            	Source IEEE 802 MAC address
                            	**type**\: str
                            
                            	**pattern:** ^[0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}$
                            
                            .. attribute:: source_mac_mask
                            
                            	Source IEEE 802 MAC address mask
                            	**type**\: str
                            
                            	**pattern:** ^[0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}$
                            
                            .. attribute:: destination_mac
                            
                            	Destination IEEE 802 MAC address
                            	**type**\: str
                            
                            	**pattern:** ^[0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}$
                            
                            .. attribute:: destination_mac_mask
                            
                            	Destination IEEE 802 MAC address mask
                            	**type**\: str
                            
                            	**pattern:** ^[0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}$
                            
                            .. attribute:: ethertype
                            
                            	Ethertype field to match in Ethernet packets
                            	**type**\: union of the below types:
                            
                            		**type**\: int
                            
                            			**range:** 1..65535
                            
                            		**type**\:  :py:class:`ETHERTYPE <ydk.models.openconfig.openconfig_packet_match_types.ETHERTYPE>`
                            
                            

                            """

                            _prefix = 'oc-acl'
                            _revision = '2017-05-26'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Acl.AclSets.AclSet.AclEntries.AclEntry.L2.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "l2"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('source_mac', (YLeaf(YType.str, 'source-mac'), ['str'])),
                                    ('source_mac_mask', (YLeaf(YType.str, 'source-mac-mask'), ['str'])),
                                    ('destination_mac', (YLeaf(YType.str, 'destination-mac'), ['str'])),
                                    ('destination_mac_mask', (YLeaf(YType.str, 'destination-mac-mask'), ['str'])),
                                    ('ethertype', (YLeaf(YType.str, 'ethertype'), ['int',('ydk.models.openconfig.openconfig_packet_match_types', 'ETHERTYPE')])),
                                ])
                                self.source_mac = None
                                self.source_mac_mask = None
                                self.destination_mac = None
                                self.destination_mac_mask = None
                                self.ethertype = None
                                self._segment_path = lambda: "config"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Acl.AclSets.AclSet.AclEntries.AclEntry.L2.Config, ['source_mac', 'source_mac_mask', 'destination_mac', 'destination_mac_mask', 'ethertype'], name, value)



                        class State(_Entity_):
                            """
                            State Information.
                            
                            .. attribute:: source_mac
                            
                            	Source IEEE 802 MAC address
                            	**type**\: str
                            
                            	**pattern:** ^[0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}$
                            
                            	**config**\: False
                            
                            .. attribute:: source_mac_mask
                            
                            	Source IEEE 802 MAC address mask
                            	**type**\: str
                            
                            	**pattern:** ^[0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}$
                            
                            	**config**\: False
                            
                            .. attribute:: destination_mac
                            
                            	Destination IEEE 802 MAC address
                            	**type**\: str
                            
                            	**pattern:** ^[0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}$
                            
                            	**config**\: False
                            
                            .. attribute:: destination_mac_mask
                            
                            	Destination IEEE 802 MAC address mask
                            	**type**\: str
                            
                            	**pattern:** ^[0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}$
                            
                            	**config**\: False
                            
                            .. attribute:: ethertype
                            
                            	Ethertype field to match in Ethernet packets
                            	**type**\: union of the below types:
                            
                            		**type**\: int
                            
                            			**range:** 1..65535
                            
                            		**type**\:  :py:class:`ETHERTYPE <ydk.models.openconfig.openconfig_packet_match_types.ETHERTYPE>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-acl'
                            _revision = '2017-05-26'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Acl.AclSets.AclSet.AclEntries.AclEntry.L2.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "l2"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('source_mac', (YLeaf(YType.str, 'source-mac'), ['str'])),
                                    ('source_mac_mask', (YLeaf(YType.str, 'source-mac-mask'), ['str'])),
                                    ('destination_mac', (YLeaf(YType.str, 'destination-mac'), ['str'])),
                                    ('destination_mac_mask', (YLeaf(YType.str, 'destination-mac-mask'), ['str'])),
                                    ('ethertype', (YLeaf(YType.str, 'ethertype'), ['int',('ydk.models.openconfig.openconfig_packet_match_types', 'ETHERTYPE')])),
                                ])
                                self.source_mac = None
                                self.source_mac_mask = None
                                self.destination_mac = None
                                self.destination_mac_mask = None
                                self.ethertype = None
                                self._segment_path = lambda: "state"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Acl.AclSets.AclSet.AclEntries.AclEntry.L2.State, ['source_mac', 'source_mac_mask', 'destination_mac', 'destination_mac_mask', 'ethertype'], name, value)




                    class Ipv4(_Entity_):
                        """
                        Top level container for IPv4 match field data
                        
                        .. attribute:: config
                        
                        	Configuration data for IPv4 match fields
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv4.Config>`
                        
                        .. attribute:: state
                        
                        	State information for IPv4 match fields
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv4.State>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-acl'
                        _revision = '2017-05-26'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv4, self).__init__()

                            self.yang_name = "ipv4"
                            self.yang_parent_name = "acl-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("config", ("config", Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv4.Config)), ("state", ("state", Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv4.State))])
                            self._leafs = OrderedDict()

                            self.config = Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv4.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"

                            self.state = Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv4.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._segment_path = lambda: "ipv4"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv4, [], name, value)


                        class Config(_Entity_):
                            """
                            Configuration data for IPv4 match fields
                            
                            .. attribute:: source_address
                            
                            	Source IPv4 address prefix
                            	**type**\: str
                            
                            	**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))$
                            
                            .. attribute:: destination_address
                            
                            	Destination IPv4 address prefix
                            	**type**\: str
                            
                            	**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))$
                            
                            .. attribute:: dscp
                            
                            	Value of diffserv codepoint
                            	**type**\: int
                            
                            	**range:** 0..63
                            
                            .. attribute:: protocol
                            
                            	The protocol carried in the IP packet, expressed either as its IP protocol number, or by a defined identity
                            	**type**\: union of the below types:
                            
                            		**type**\: int
                            
                            			**range:** 0..254
                            
                            		**type**\:  :py:class:`IPPROTOCOL <ydk.models.openconfig.openconfig_packet_match_types.IPPROTOCOL>`
                            
                            .. attribute:: hop_limit
                            
                            	The IP packet's hop limit \-\- known as TTL (in hops) in IPv4 packets, and hop limit in IPv6
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'oc-acl'
                            _revision = '2017-05-26'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv4.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "ipv4"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                    ('destination_address', (YLeaf(YType.str, 'destination-address'), ['str'])),
                                    ('dscp', (YLeaf(YType.uint8, 'dscp'), ['int'])),
                                    ('protocol', (YLeaf(YType.str, 'protocol'), ['int',('ydk.models.openconfig.openconfig_packet_match_types', 'IPPROTOCOL')])),
                                    ('hop_limit', (YLeaf(YType.uint8, 'hop-limit'), ['int'])),
                                ])
                                self.source_address = None
                                self.destination_address = None
                                self.dscp = None
                                self.protocol = None
                                self.hop_limit = None
                                self._segment_path = lambda: "config"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv4.Config, ['source_address', 'destination_address', 'dscp', 'protocol', 'hop_limit'], name, value)



                        class State(_Entity_):
                            """
                            State information for IPv4 match fields
                            
                            .. attribute:: source_address
                            
                            	Source IPv4 address prefix
                            	**type**\: str
                            
                            	**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))$
                            
                            	**config**\: False
                            
                            .. attribute:: destination_address
                            
                            	Destination IPv4 address prefix
                            	**type**\: str
                            
                            	**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))$
                            
                            	**config**\: False
                            
                            .. attribute:: dscp
                            
                            	Value of diffserv codepoint
                            	**type**\: int
                            
                            	**range:** 0..63
                            
                            	**config**\: False
                            
                            .. attribute:: protocol
                            
                            	The protocol carried in the IP packet, expressed either as its IP protocol number, or by a defined identity
                            	**type**\: union of the below types:
                            
                            		**type**\: int
                            
                            			**range:** 0..254
                            
                            		**type**\:  :py:class:`IPPROTOCOL <ydk.models.openconfig.openconfig_packet_match_types.IPPROTOCOL>`
                            
                            	**config**\: False
                            
                            .. attribute:: hop_limit
                            
                            	The IP packet's hop limit \-\- known as TTL (in hops) in IPv4 packets, and hop limit in IPv6
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-acl'
                            _revision = '2017-05-26'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv4.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "ipv4"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                    ('destination_address', (YLeaf(YType.str, 'destination-address'), ['str'])),
                                    ('dscp', (YLeaf(YType.uint8, 'dscp'), ['int'])),
                                    ('protocol', (YLeaf(YType.str, 'protocol'), ['int',('ydk.models.openconfig.openconfig_packet_match_types', 'IPPROTOCOL')])),
                                    ('hop_limit', (YLeaf(YType.uint8, 'hop-limit'), ['int'])),
                                ])
                                self.source_address = None
                                self.destination_address = None
                                self.dscp = None
                                self.protocol = None
                                self.hop_limit = None
                                self._segment_path = lambda: "state"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv4.State, ['source_address', 'destination_address', 'dscp', 'protocol', 'hop_limit'], name, value)




                    class Ipv6(_Entity_):
                        """
                        Top\-level container for IPv6 match field data
                        
                        .. attribute:: config
                        
                        	Configuration data for IPv6 match fields
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv6.Config>`
                        
                        .. attribute:: state
                        
                        	Operational state data for IPv6 match fields
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv6.State>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-acl'
                        _revision = '2017-05-26'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv6, self).__init__()

                            self.yang_name = "ipv6"
                            self.yang_parent_name = "acl-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("config", ("config", Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv6.Config)), ("state", ("state", Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv6.State))])
                            self._leafs = OrderedDict()

                            self.config = Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv6.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"

                            self.state = Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv6.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._segment_path = lambda: "ipv6"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv6, [], name, value)


                        class Config(_Entity_):
                            """
                            Configuration data for IPv6 match fields
                            
                            .. attribute:: source_address
                            
                            	Source IPv6 address prefix
                            	**type**\: str
                            
                            	**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))/(12[0\-8]\|1[0\-1][0\-9]\|[1\-9][0\-9]\|[0\-9])$
                            
                            .. attribute:: source_flow_label
                            
                            	Source IPv6 Flow label
                            	**type**\: int
                            
                            	**range:** 0..1048575
                            
                            .. attribute:: destination_address
                            
                            	Destination IPv6 address prefix
                            	**type**\: str
                            
                            	**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))/(12[0\-8]\|1[0\-1][0\-9]\|[1\-9][0\-9]\|[0\-9])$
                            
                            .. attribute:: destination_flow_label
                            
                            	Destination IPv6 Flow label
                            	**type**\: int
                            
                            	**range:** 0..1048575
                            
                            .. attribute:: dscp
                            
                            	Value of diffserv codepoint
                            	**type**\: int
                            
                            	**range:** 0..63
                            
                            .. attribute:: protocol
                            
                            	The protocol carried in the IP packet, expressed either as its IP protocol number, or by a defined identity
                            	**type**\: union of the below types:
                            
                            		**type**\: int
                            
                            			**range:** 0..254
                            
                            		**type**\:  :py:class:`IPPROTOCOL <ydk.models.openconfig.openconfig_packet_match_types.IPPROTOCOL>`
                            
                            .. attribute:: hop_limit
                            
                            	The IP packet's hop limit \-\- known as TTL (in hops) in IPv4 packets, and hop limit in IPv6
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'oc-acl'
                            _revision = '2017-05-26'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv6.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "ipv6"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                    ('source_flow_label', (YLeaf(YType.uint32, 'source-flow-label'), ['int'])),
                                    ('destination_address', (YLeaf(YType.str, 'destination-address'), ['str'])),
                                    ('destination_flow_label', (YLeaf(YType.uint32, 'destination-flow-label'), ['int'])),
                                    ('dscp', (YLeaf(YType.uint8, 'dscp'), ['int'])),
                                    ('protocol', (YLeaf(YType.str, 'protocol'), ['int',('ydk.models.openconfig.openconfig_packet_match_types', 'IPPROTOCOL')])),
                                    ('hop_limit', (YLeaf(YType.uint8, 'hop-limit'), ['int'])),
                                ])
                                self.source_address = None
                                self.source_flow_label = None
                                self.destination_address = None
                                self.destination_flow_label = None
                                self.dscp = None
                                self.protocol = None
                                self.hop_limit = None
                                self._segment_path = lambda: "config"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv6.Config, ['source_address', 'source_flow_label', 'destination_address', 'destination_flow_label', 'dscp', 'protocol', 'hop_limit'], name, value)



                        class State(_Entity_):
                            """
                            Operational state data for IPv6 match fields
                            
                            .. attribute:: source_address
                            
                            	Source IPv6 address prefix
                            	**type**\: str
                            
                            	**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))/(12[0\-8]\|1[0\-1][0\-9]\|[1\-9][0\-9]\|[0\-9])$
                            
                            	**config**\: False
                            
                            .. attribute:: source_flow_label
                            
                            	Source IPv6 Flow label
                            	**type**\: int
                            
                            	**range:** 0..1048575
                            
                            	**config**\: False
                            
                            .. attribute:: destination_address
                            
                            	Destination IPv6 address prefix
                            	**type**\: str
                            
                            	**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))/(12[0\-8]\|1[0\-1][0\-9]\|[1\-9][0\-9]\|[0\-9])$
                            
                            	**config**\: False
                            
                            .. attribute:: destination_flow_label
                            
                            	Destination IPv6 Flow label
                            	**type**\: int
                            
                            	**range:** 0..1048575
                            
                            	**config**\: False
                            
                            .. attribute:: dscp
                            
                            	Value of diffserv codepoint
                            	**type**\: int
                            
                            	**range:** 0..63
                            
                            	**config**\: False
                            
                            .. attribute:: protocol
                            
                            	The protocol carried in the IP packet, expressed either as its IP protocol number, or by a defined identity
                            	**type**\: union of the below types:
                            
                            		**type**\: int
                            
                            			**range:** 0..254
                            
                            		**type**\:  :py:class:`IPPROTOCOL <ydk.models.openconfig.openconfig_packet_match_types.IPPROTOCOL>`
                            
                            	**config**\: False
                            
                            .. attribute:: hop_limit
                            
                            	The IP packet's hop limit \-\- known as TTL (in hops) in IPv4 packets, and hop limit in IPv6
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-acl'
                            _revision = '2017-05-26'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv6.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "ipv6"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                    ('source_flow_label', (YLeaf(YType.uint32, 'source-flow-label'), ['int'])),
                                    ('destination_address', (YLeaf(YType.str, 'destination-address'), ['str'])),
                                    ('destination_flow_label', (YLeaf(YType.uint32, 'destination-flow-label'), ['int'])),
                                    ('dscp', (YLeaf(YType.uint8, 'dscp'), ['int'])),
                                    ('protocol', (YLeaf(YType.str, 'protocol'), ['int',('ydk.models.openconfig.openconfig_packet_match_types', 'IPPROTOCOL')])),
                                    ('hop_limit', (YLeaf(YType.uint8, 'hop-limit'), ['int'])),
                                ])
                                self.source_address = None
                                self.source_flow_label = None
                                self.destination_address = None
                                self.destination_flow_label = None
                                self.dscp = None
                                self.protocol = None
                                self.hop_limit = None
                                self._segment_path = lambda: "state"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Acl.AclSets.AclSet.AclEntries.AclEntry.Ipv6.State, ['source_address', 'source_flow_label', 'destination_address', 'destination_flow_label', 'dscp', 'protocol', 'hop_limit'], name, value)




                    class Transport(_Entity_):
                        """
                        Transport fields container
                        
                        .. attribute:: config
                        
                        	Configuration data
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry.Transport.Config>`
                        
                        .. attribute:: state
                        
                        	State data
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry.Transport.State>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-acl'
                        _revision = '2017-05-26'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Acl.AclSets.AclSet.AclEntries.AclEntry.Transport, self).__init__()

                            self.yang_name = "transport"
                            self.yang_parent_name = "acl-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("config", ("config", Acl.AclSets.AclSet.AclEntries.AclEntry.Transport.Config)), ("state", ("state", Acl.AclSets.AclSet.AclEntries.AclEntry.Transport.State))])
                            self._leafs = OrderedDict()

                            self.config = Acl.AclSets.AclSet.AclEntries.AclEntry.Transport.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"

                            self.state = Acl.AclSets.AclSet.AclEntries.AclEntry.Transport.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._segment_path = lambda: "transport"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Acl.AclSets.AclSet.AclEntries.AclEntry.Transport, [], name, value)


                        class Config(_Entity_):
                            """
                            Configuration data
                            
                            .. attribute:: source_port
                            
                            	Source port or range
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** ^(6[0\-5][0\-5][0\-3][0\-5]\|[0\-5]?[0\-9]?[0\-9]?[0\-9]?[0\-9]?)\\.\\.(6[0\-5][0\-5][0\-3][0\-5]\|[0\-5]?[0\-9]?[0\-9]?[0\-9]?[0\-9]?)$
                            
                            		**type**\: int
                            
                            			**range:** 0..65535
                            
                            		**type**\:  :py:class:`PortNumRange <ydk.models.openconfig.openconfig_packet_match_types.PortNumRange>`
                            
                            .. attribute:: destination_port
                            
                            	Destination port or range
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** ^(6[0\-5][0\-5][0\-3][0\-5]\|[0\-5]?[0\-9]?[0\-9]?[0\-9]?[0\-9]?)\\.\\.(6[0\-5][0\-5][0\-3][0\-5]\|[0\-5]?[0\-9]?[0\-9]?[0\-9]?[0\-9]?)$
                            
                            		**type**\: int
                            
                            			**range:** 0..65535
                            
                            		**type**\:  :py:class:`PortNumRange <ydk.models.openconfig.openconfig_packet_match_types.PortNumRange>`
                            
                            .. attribute:: tcp_flags
                            
                            	List of TCP flags to match
                            	**type**\: list of   :py:class:`TCPFLAGS <ydk.models.openconfig.openconfig_packet_match_types.TCPFLAGS>`
                            
                            

                            """

                            _prefix = 'oc-acl'
                            _revision = '2017-05-26'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Acl.AclSets.AclSet.AclEntries.AclEntry.Transport.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "transport"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('source_port', (YLeaf(YType.str, 'source-port'), ['str','int',('ydk.models.openconfig.openconfig_packet_match_types', 'PortNumRange', '')])),
                                    ('destination_port', (YLeaf(YType.str, 'destination-port'), ['str','int',('ydk.models.openconfig.openconfig_packet_match_types', 'PortNumRange', '')])),
                                    ('tcp_flags', (YLeafList(YType.identityref, 'tcp-flags'), [('ydk.models.openconfig.openconfig_packet_match_types', 'TCPFLAGS')])),
                                ])
                                self.source_port = None
                                self.destination_port = None
                                self.tcp_flags = []
                                self._segment_path = lambda: "config"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Acl.AclSets.AclSet.AclEntries.AclEntry.Transport.Config, ['source_port', 'destination_port', 'tcp_flags'], name, value)



                        class State(_Entity_):
                            """
                            State data
                            
                            .. attribute:: source_port
                            
                            	Source port or range
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** ^(6[0\-5][0\-5][0\-3][0\-5]\|[0\-5]?[0\-9]?[0\-9]?[0\-9]?[0\-9]?)\\.\\.(6[0\-5][0\-5][0\-3][0\-5]\|[0\-5]?[0\-9]?[0\-9]?[0\-9]?[0\-9]?)$
                            
                            		**type**\: int
                            
                            			**range:** 0..65535
                            
                            		**type**\:  :py:class:`PortNumRange <ydk.models.openconfig.openconfig_packet_match_types.PortNumRange>`
                            
                            	**config**\: False
                            
                            .. attribute:: destination_port
                            
                            	Destination port or range
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** ^(6[0\-5][0\-5][0\-3][0\-5]\|[0\-5]?[0\-9]?[0\-9]?[0\-9]?[0\-9]?)\\.\\.(6[0\-5][0\-5][0\-3][0\-5]\|[0\-5]?[0\-9]?[0\-9]?[0\-9]?[0\-9]?)$
                            
                            		**type**\: int
                            
                            			**range:** 0..65535
                            
                            		**type**\:  :py:class:`PortNumRange <ydk.models.openconfig.openconfig_packet_match_types.PortNumRange>`
                            
                            	**config**\: False
                            
                            .. attribute:: tcp_flags
                            
                            	List of TCP flags to match
                            	**type**\: list of   :py:class:`TCPFLAGS <ydk.models.openconfig.openconfig_packet_match_types.TCPFLAGS>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-acl'
                            _revision = '2017-05-26'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Acl.AclSets.AclSet.AclEntries.AclEntry.Transport.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "transport"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('source_port', (YLeaf(YType.str, 'source-port'), ['str','int',('ydk.models.openconfig.openconfig_packet_match_types', 'PortNumRange', '')])),
                                    ('destination_port', (YLeaf(YType.str, 'destination-port'), ['str','int',('ydk.models.openconfig.openconfig_packet_match_types', 'PortNumRange', '')])),
                                    ('tcp_flags', (YLeafList(YType.identityref, 'tcp-flags'), [('ydk.models.openconfig.openconfig_packet_match_types', 'TCPFLAGS')])),
                                ])
                                self.source_port = None
                                self.destination_port = None
                                self.tcp_flags = []
                                self._segment_path = lambda: "state"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Acl.AclSets.AclSet.AclEntries.AclEntry.Transport.State, ['source_port', 'destination_port', 'tcp_flags'], name, value)




                    class InputInterface(_Entity_):
                        """
                        Input interface container
                        
                        .. attribute:: config
                        
                        	Config data
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface.Config>`
                        
                        .. attribute:: state
                        
                        	State information
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface.State>`
                        
                        	**config**\: False
                        
                        .. attribute:: interface_ref
                        
                        	Reference to an interface or subinterface
                        	**type**\:  :py:class:`InterfaceRef <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface.InterfaceRef>`
                        
                        

                        """

                        _prefix = 'oc-acl'
                        _revision = '2017-05-26'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface, self).__init__()

                            self.yang_name = "input-interface"
                            self.yang_parent_name = "acl-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("config", ("config", Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface.Config)), ("state", ("state", Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface.State)), ("interface-ref", ("interface_ref", Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface.InterfaceRef))])
                            self._leafs = OrderedDict()

                            self.config = Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"

                            self.state = Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"

                            self.interface_ref = Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface.InterfaceRef()
                            self.interface_ref.parent = self
                            self._children_name_map["interface_ref"] = "interface-ref"
                            self._segment_path = lambda: "input-interface"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface, [], name, value)


                        class Config(_Entity_):
                            """
                            Config data
                            
                            

                            """

                            _prefix = 'oc-acl'
                            _revision = '2017-05-26'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "input-interface"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict()
                                self._segment_path = lambda: "config"
                                self._is_frozen = True



                        class State(_Entity_):
                            """
                            State information
                            
                            

                            """

                            _prefix = 'oc-acl'
                            _revision = '2017-05-26'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "input-interface"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict()
                                self._segment_path = lambda: "state"
                                self._is_frozen = True



                        class InterfaceRef(_Entity_):
                            """
                            Reference to an interface or subinterface
                            
                            .. attribute:: config
                            
                            	Configured reference to interface / subinterface
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface.InterfaceRef.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state for interface\-ref
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface.InterfaceRef.State>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-acl'
                            _revision = '2017-05-26'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface.InterfaceRef, self).__init__()

                                self.yang_name = "interface-ref"
                                self.yang_parent_name = "input-interface"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("config", ("config", Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface.InterfaceRef.Config)), ("state", ("state", Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface.InterfaceRef.State))])
                                self._leafs = OrderedDict()

                                self.config = Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface.InterfaceRef.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"

                                self.state = Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface.InterfaceRef.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._segment_path = lambda: "interface-ref"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface.InterfaceRef, [], name, value)


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

                                _prefix = 'oc-acl'
                                _revision = '2017-05-26'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface.InterfaceRef.Config, self).__init__()

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
                                    self._perform_setattr(Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface.InterfaceRef.Config, ['interface', 'subinterface'], name, value)



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

                                _prefix = 'oc-acl'
                                _revision = '2017-05-26'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface.InterfaceRef.State, self).__init__()

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
                                    self._perform_setattr(Acl.AclSets.AclSet.AclEntries.AclEntry.InputInterface.InterfaceRef.State, ['interface', 'subinterface'], name, value)





                    class Actions(_Entity_):
                        """
                        Enclosing container for list of ACL actions associated
                        with an entry
                        
                        .. attribute:: config
                        
                        	Config data for ACL actions
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry.Actions.Config>`
                        
                        .. attribute:: state
                        
                        	State information for ACL actions
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry.Actions.State>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-acl'
                        _revision = '2017-05-26'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Acl.AclSets.AclSet.AclEntries.AclEntry.Actions, self).__init__()

                            self.yang_name = "actions"
                            self.yang_parent_name = "acl-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("config", ("config", Acl.AclSets.AclSet.AclEntries.AclEntry.Actions.Config)), ("state", ("state", Acl.AclSets.AclSet.AclEntries.AclEntry.Actions.State))])
                            self._leafs = OrderedDict()

                            self.config = Acl.AclSets.AclSet.AclEntries.AclEntry.Actions.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"

                            self.state = Acl.AclSets.AclSet.AclEntries.AclEntry.Actions.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._segment_path = lambda: "actions"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Acl.AclSets.AclSet.AclEntries.AclEntry.Actions, [], name, value)


                        class Config(_Entity_):
                            """
                            Config data for ACL actions
                            
                            .. attribute:: forwarding_action
                            
                            	Specifies the forwarding action.  One forwarding action must be specified for each ACL entry
                            	**type**\:  :py:class:`FORWARDINGACTION <ydk.models.openconfig.openconfig_acl.FORWARDINGACTION>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: log_action
                            
                            	Specifies the log action and destination for matched packets.  The default is not to log the packet
                            	**type**\:  :py:class:`LOGACTION <ydk.models.openconfig.openconfig_acl.LOGACTION>`
                            
                            	**default value**\: LOG_NONE
                            
                            

                            """

                            _prefix = 'oc-acl'
                            _revision = '2017-05-26'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Acl.AclSets.AclSet.AclEntries.AclEntry.Actions.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "actions"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('forwarding_action', (YLeaf(YType.identityref, 'forwarding-action'), [('ydk.models.openconfig.openconfig_acl', 'FORWARDINGACTION')])),
                                    ('log_action', (YLeaf(YType.identityref, 'log-action'), [('ydk.models.openconfig.openconfig_acl', 'LOGACTION')])),
                                ])
                                self.forwarding_action = None
                                self.log_action = None
                                self._segment_path = lambda: "config"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Acl.AclSets.AclSet.AclEntries.AclEntry.Actions.Config, ['forwarding_action', 'log_action'], name, value)



                        class State(_Entity_):
                            """
                            State information for ACL actions
                            
                            .. attribute:: forwarding_action
                            
                            	Specifies the forwarding action.  One forwarding action must be specified for each ACL entry
                            	**type**\:  :py:class:`FORWARDINGACTION <ydk.models.openconfig.openconfig_acl.FORWARDINGACTION>`
                            
                            	**mandatory**\: True
                            
                            	**config**\: False
                            
                            .. attribute:: log_action
                            
                            	Specifies the log action and destination for matched packets.  The default is not to log the packet
                            	**type**\:  :py:class:`LOGACTION <ydk.models.openconfig.openconfig_acl.LOGACTION>`
                            
                            	**config**\: False
                            
                            	**default value**\: LOG_NONE
                            
                            

                            """

                            _prefix = 'oc-acl'
                            _revision = '2017-05-26'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Acl.AclSets.AclSet.AclEntries.AclEntry.Actions.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "actions"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('forwarding_action', (YLeaf(YType.identityref, 'forwarding-action'), [('ydk.models.openconfig.openconfig_acl', 'FORWARDINGACTION')])),
                                    ('log_action', (YLeaf(YType.identityref, 'log-action'), [('ydk.models.openconfig.openconfig_acl', 'LOGACTION')])),
                                ])
                                self.forwarding_action = None
                                self.log_action = None
                                self._segment_path = lambda: "state"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Acl.AclSets.AclSet.AclEntries.AclEntry.Actions.State, ['forwarding_action', 'log_action'], name, value)








    class Interfaces(_Entity_):
        """
        Enclosing container for the list of interfaces on which
        ACLs are set
        
        .. attribute:: interface
        
        	List of interfaces on which ACLs are set
        	**type**\: list of  		 :py:class:`Interface <ydk.models.openconfig.openconfig_acl.Acl.Interfaces.Interface>`
        
        

        """

        _prefix = 'oc-acl'
        _revision = '2017-05-26'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Acl.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "acl"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface", ("interface", Acl.Interfaces.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "openconfig-acl:acl/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Acl.Interfaces, [], name, value)


        class Interface(_Entity_):
            """
            List of interfaces on which ACLs are set
            
            .. attribute:: id  (key)
            
            	Reference to the interface id list key
            	**type**\: str
            
            	**refers to**\:  :py:class:`id <ydk.models.openconfig.openconfig_acl.Acl.Interfaces.Interface.Config>`
            
            .. attribute:: config
            
            	Configuration for ACL per\-interface data
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_acl.Acl.Interfaces.Interface.Config>`
            
            .. attribute:: state
            
            	Operational state for ACL per\-interface data
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_acl.Acl.Interfaces.Interface.State>`
            
            	**config**\: False
            
            .. attribute:: interface_ref
            
            	Reference to an interface or subinterface
            	**type**\:  :py:class:`InterfaceRef <ydk.models.openconfig.openconfig_acl.Acl.Interfaces.Interface.InterfaceRef>`
            
            .. attribute:: ingress_acl_sets
            
            	Enclosing container the list of ingress ACLs on the interface
            	**type**\:  :py:class:`IngressAclSets <ydk.models.openconfig.openconfig_acl.Acl.Interfaces.Interface.IngressAclSets>`
            
            .. attribute:: egress_acl_sets
            
            	Enclosing container the list of egress ACLs on the interface
            	**type**\:  :py:class:`EgressAclSets <ydk.models.openconfig.openconfig_acl.Acl.Interfaces.Interface.EgressAclSets>`
            
            

            """

            _prefix = 'oc-acl'
            _revision = '2017-05-26'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Acl.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['id']
                self._child_classes = OrderedDict([("config", ("config", Acl.Interfaces.Interface.Config)), ("state", ("state", Acl.Interfaces.Interface.State)), ("interface-ref", ("interface_ref", Acl.Interfaces.Interface.InterfaceRef)), ("ingress-acl-sets", ("ingress_acl_sets", Acl.Interfaces.Interface.IngressAclSets)), ("egress-acl-sets", ("egress_acl_sets", Acl.Interfaces.Interface.EgressAclSets))])
                self._leafs = OrderedDict([
                    ('id', (YLeaf(YType.str, 'id'), ['str'])),
                ])
                self.id = None

                self.config = Acl.Interfaces.Interface.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = Acl.Interfaces.Interface.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"

                self.interface_ref = Acl.Interfaces.Interface.InterfaceRef()
                self.interface_ref.parent = self
                self._children_name_map["interface_ref"] = "interface-ref"

                self.ingress_acl_sets = Acl.Interfaces.Interface.IngressAclSets()
                self.ingress_acl_sets.parent = self
                self._children_name_map["ingress_acl_sets"] = "ingress-acl-sets"

                self.egress_acl_sets = Acl.Interfaces.Interface.EgressAclSets()
                self.egress_acl_sets.parent = self
                self._children_name_map["egress_acl_sets"] = "egress-acl-sets"
                self._segment_path = lambda: "interface" + "[id='" + str(self.id) + "']"
                self._absolute_path = lambda: "openconfig-acl:acl/interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Acl.Interfaces.Interface, ['id'], name, value)


            class Config(_Entity_):
                """
                Configuration for ACL per\-interface data
                
                .. attribute:: id
                
                	User\-defined identifier for the interface \-\- a common convention could be '<if name>.<subif index>'
                	**type**\: str
                
                

                """

                _prefix = 'oc-acl'
                _revision = '2017-05-26'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Acl.Interfaces.Interface.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('id', (YLeaf(YType.str, 'id'), ['str'])),
                    ])
                    self.id = None
                    self._segment_path = lambda: "config"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Acl.Interfaces.Interface.Config, ['id'], name, value)



            class State(_Entity_):
                """
                Operational state for ACL per\-interface data
                
                .. attribute:: id
                
                	User\-defined identifier for the interface \-\- a common convention could be '<if name>.<subif index>'
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-acl'
                _revision = '2017-05-26'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Acl.Interfaces.Interface.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('id', (YLeaf(YType.str, 'id'), ['str'])),
                    ])
                    self.id = None
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Acl.Interfaces.Interface.State, ['id'], name, value)



            class InterfaceRef(_Entity_):
                """
                Reference to an interface or subinterface
                
                .. attribute:: config
                
                	Configured reference to interface / subinterface
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_acl.Acl.Interfaces.Interface.InterfaceRef.Config>`
                
                .. attribute:: state
                
                	Operational state for interface\-ref
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_acl.Acl.Interfaces.Interface.InterfaceRef.State>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-acl'
                _revision = '2017-05-26'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Acl.Interfaces.Interface.InterfaceRef, self).__init__()

                    self.yang_name = "interface-ref"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("config", ("config", Acl.Interfaces.Interface.InterfaceRef.Config)), ("state", ("state", Acl.Interfaces.Interface.InterfaceRef.State))])
                    self._leafs = OrderedDict()

                    self.config = Acl.Interfaces.Interface.InterfaceRef.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.state = Acl.Interfaces.Interface.InterfaceRef.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._segment_path = lambda: "interface-ref"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Acl.Interfaces.Interface.InterfaceRef, [], name, value)


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

                    _prefix = 'oc-acl'
                    _revision = '2017-05-26'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Acl.Interfaces.Interface.InterfaceRef.Config, self).__init__()

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
                        self._perform_setattr(Acl.Interfaces.Interface.InterfaceRef.Config, ['interface', 'subinterface'], name, value)



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

                    _prefix = 'oc-acl'
                    _revision = '2017-05-26'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Acl.Interfaces.Interface.InterfaceRef.State, self).__init__()

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
                        self._perform_setattr(Acl.Interfaces.Interface.InterfaceRef.State, ['interface', 'subinterface'], name, value)




            class IngressAclSets(_Entity_):
                """
                Enclosing container the list of ingress ACLs on the
                interface
                
                .. attribute:: ingress_acl_set
                
                	List of ingress ACLs on the interface
                	**type**\: list of  		 :py:class:`IngressAclSet <ydk.models.openconfig.openconfig_acl.Acl.Interfaces.Interface.IngressAclSets.IngressAclSet>`
                
                

                """

                _prefix = 'oc-acl'
                _revision = '2017-05-26'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Acl.Interfaces.Interface.IngressAclSets, self).__init__()

                    self.yang_name = "ingress-acl-sets"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ingress-acl-set", ("ingress_acl_set", Acl.Interfaces.Interface.IngressAclSets.IngressAclSet))])
                    self._leafs = OrderedDict()

                    self.ingress_acl_set = YList(self)
                    self._segment_path = lambda: "ingress-acl-sets"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Acl.Interfaces.Interface.IngressAclSets, [], name, value)


                class IngressAclSet(_Entity_):
                    """
                    List of ingress ACLs on the interface
                    
                    .. attribute:: set_name  (key)
                    
                    	Reference to set name list key
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`set_name <ydk.models.openconfig.openconfig_acl.Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.Config>`
                    
                    .. attribute:: type  (key)
                    
                    	Reference to type list key
                    	**type**\:  :py:class:`ACLTYPE <ydk.models.openconfig.openconfig_acl.ACLTYPE>`
                    
                    .. attribute:: config
                    
                    	Configuration data 
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_acl.Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for interface ingress ACLs
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_acl.Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.State>`
                    
                    	**config**\: False
                    
                    .. attribute:: acl_entries
                    
                    	Enclosing container for list of references to ACLs
                    	**type**\:  :py:class:`AclEntries <ydk.models.openconfig.openconfig_acl.Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-acl'
                    _revision = '2017-05-26'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Acl.Interfaces.Interface.IngressAclSets.IngressAclSet, self).__init__()

                        self.yang_name = "ingress-acl-set"
                        self.yang_parent_name = "ingress-acl-sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['set_name','type']
                        self._child_classes = OrderedDict([("config", ("config", Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.Config)), ("state", ("state", Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.State)), ("acl-entries", ("acl_entries", Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries))])
                        self._leafs = OrderedDict([
                            ('set_name', (YLeaf(YType.str, 'set-name'), ['str'])),
                            ('type', (YLeaf(YType.identityref, 'type'), [('ydk.models.openconfig.openconfig_acl', 'ACLTYPE')])),
                        ])
                        self.set_name = None
                        self.type = None

                        self.config = Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"

                        self.acl_entries = Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries()
                        self.acl_entries.parent = self
                        self._children_name_map["acl_entries"] = "acl-entries"
                        self._segment_path = lambda: "ingress-acl-set" + "[set-name='" + str(self.set_name) + "']" + "[type='" + str(self.type) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Acl.Interfaces.Interface.IngressAclSets.IngressAclSet, ['set_name', 'type'], name, value)


                    class Config(_Entity_):
                        """
                        Configuration data 
                        
                        .. attribute:: set_name
                        
                        	Reference to the ACL set name applied on ingress
                        	**type**\: str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.Config>`
                        
                        .. attribute:: type
                        
                        	Reference to the ACL set type applied on ingress
                        	**type**\:  :py:class:`ACLTYPE <ydk.models.openconfig.openconfig_acl.ACLTYPE>`
                        
                        

                        """

                        _prefix = 'oc-acl'
                        _revision = '2017-05-26'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "ingress-acl-set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('set_name', (YLeaf(YType.str, 'set-name'), ['str'])),
                                ('type', (YLeaf(YType.identityref, 'type'), [('ydk.models.openconfig.openconfig_acl', 'ACLTYPE')])),
                            ])
                            self.set_name = None
                            self.type = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.Config, ['set_name', 'type'], name, value)



                    class State(_Entity_):
                        """
                        Operational state data for interface ingress ACLs
                        
                        .. attribute:: set_name
                        
                        	Reference to the ACL set name applied on ingress
                        	**type**\: str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.Config>`
                        
                        	**config**\: False
                        
                        .. attribute:: type
                        
                        	Reference to the ACL set type applied on ingress
                        	**type**\:  :py:class:`ACLTYPE <ydk.models.openconfig.openconfig_acl.ACLTYPE>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-acl'
                        _revision = '2017-05-26'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "ingress-acl-set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('set_name', (YLeaf(YType.str, 'set-name'), ['str'])),
                                ('type', (YLeaf(YType.identityref, 'type'), [('ydk.models.openconfig.openconfig_acl', 'ACLTYPE')])),
                            ])
                            self.set_name = None
                            self.type = None
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.State, ['set_name', 'type'], name, value)



                    class AclEntries(_Entity_):
                        """
                        Enclosing container for list of references to ACLs
                        
                        .. attribute:: acl_entry
                        
                        	List of ACL entries assigned to an interface
                        	**type**\: list of  		 :py:class:`AclEntry <ydk.models.openconfig.openconfig_acl.Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries.AclEntry>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-acl'
                        _revision = '2017-05-26'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries, self).__init__()

                            self.yang_name = "acl-entries"
                            self.yang_parent_name = "ingress-acl-set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("acl-entry", ("acl_entry", Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries.AclEntry))])
                            self._leafs = OrderedDict()

                            self.acl_entry = YList(self)
                            self._segment_path = lambda: "acl-entries"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries, [], name, value)


                        class AclEntry(_Entity_):
                            """
                            List of ACL entries assigned to an interface
                            
                            .. attribute:: sequence_id  (key)
                            
                            	Reference to per\-interface acl entry key
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**refers to**\:  :py:class:`sequence_id <ydk.models.openconfig.openconfig_acl.Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries.AclEntry.State>`
                            
                            	**config**\: False
                            
                            .. attribute:: state
                            
                            	Operational state data for per\-interface ACL entries
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_acl.Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries.AclEntry.State>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-acl'
                            _revision = '2017-05-26'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries.AclEntry, self).__init__()

                                self.yang_name = "acl-entry"
                                self.yang_parent_name = "acl-entries"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['sequence_id']
                                self._child_classes = OrderedDict([("state", ("state", Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries.AclEntry.State))])
                                self._leafs = OrderedDict([
                                    ('sequence_id', (YLeaf(YType.str, 'sequence-id'), ['int'])),
                                ])
                                self.sequence_id = None

                                self.state = Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries.AclEntry.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._segment_path = lambda: "acl-entry" + "[sequence-id='" + str(self.sequence_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries.AclEntry, ['sequence_id'], name, value)


                            class State(_Entity_):
                                """
                                Operational state data for per\-interface ACL entries
                                
                                .. attribute:: sequence_id
                                
                                	Reference to an entry in the ACL set applied to an interface
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**refers to**\:  :py:class:`sequence_id <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry>`
                                
                                	**config**\: False
                                
                                .. attribute:: matched_packets
                                
                                	Count of the number of packets matching the current ACL entry.  An implementation should provide this counter on a per\-interface per\-ACL\-entry if possible.  If an implementation only supports ACL counters per entry (i.e., not broken out per interface), then the value should be equal to the aggregate count across all interfaces.  An implementation that provides counters per entry per interface is not required to also provide an aggregate count, e.g., per entry \-\- the user is expected to be able implement the required aggregation if such a count is needed
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: matched_octets
                                
                                	Count of the number of octets (bytes) matching the current ACL entry.  An implementation should provide this counter on a per\-interface per\-ACL\-entry if possible.  If an implementation only supports ACL counters per entry (i.e., not broken out per interface), then the value should be equal to the aggregate count across all interfaces.  An implementation that provides counters per entry per interface is not required to also provide an aggregate count, e.g., per entry \-\- the user is expected to be able implement the required aggregation if such a count is needed
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'oc-acl'
                                _revision = '2017-05-26'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries.AclEntry.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "acl-entry"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('sequence_id', (YLeaf(YType.str, 'sequence-id'), ['int'])),
                                        ('matched_packets', (YLeaf(YType.uint64, 'matched-packets'), ['int'])),
                                        ('matched_octets', (YLeaf(YType.uint64, 'matched-octets'), ['int'])),
                                    ])
                                    self.sequence_id = None
                                    self.matched_packets = None
                                    self.matched_octets = None
                                    self._segment_path = lambda: "state"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Acl.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries.AclEntry.State, ['sequence_id', 'matched_packets', 'matched_octets'], name, value)







            class EgressAclSets(_Entity_):
                """
                Enclosing container the list of egress ACLs on the
                interface
                
                .. attribute:: egress_acl_set
                
                	List of egress ACLs on the interface
                	**type**\: list of  		 :py:class:`EgressAclSet <ydk.models.openconfig.openconfig_acl.Acl.Interfaces.Interface.EgressAclSets.EgressAclSet>`
                
                

                """

                _prefix = 'oc-acl'
                _revision = '2017-05-26'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Acl.Interfaces.Interface.EgressAclSets, self).__init__()

                    self.yang_name = "egress-acl-sets"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("egress-acl-set", ("egress_acl_set", Acl.Interfaces.Interface.EgressAclSets.EgressAclSet))])
                    self._leafs = OrderedDict()

                    self.egress_acl_set = YList(self)
                    self._segment_path = lambda: "egress-acl-sets"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Acl.Interfaces.Interface.EgressAclSets, [], name, value)


                class EgressAclSet(_Entity_):
                    """
                    List of egress ACLs on the interface
                    
                    .. attribute:: set_name  (key)
                    
                    	Reference to set name list key
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`set_name <ydk.models.openconfig.openconfig_acl.Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.Config>`
                    
                    .. attribute:: type  (key)
                    
                    	Reference to type list key
                    	**type**\:  :py:class:`ACLTYPE <ydk.models.openconfig.openconfig_acl.ACLTYPE>`
                    
                    .. attribute:: config
                    
                    	Configuration data 
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_acl.Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for interface egress ACLs
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_acl.Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.State>`
                    
                    	**config**\: False
                    
                    .. attribute:: acl_entries
                    
                    	Enclosing container for list of references to ACLs
                    	**type**\:  :py:class:`AclEntries <ydk.models.openconfig.openconfig_acl.Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-acl'
                    _revision = '2017-05-26'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Acl.Interfaces.Interface.EgressAclSets.EgressAclSet, self).__init__()

                        self.yang_name = "egress-acl-set"
                        self.yang_parent_name = "egress-acl-sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['set_name','type']
                        self._child_classes = OrderedDict([("config", ("config", Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.Config)), ("state", ("state", Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.State)), ("acl-entries", ("acl_entries", Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries))])
                        self._leafs = OrderedDict([
                            ('set_name', (YLeaf(YType.str, 'set-name'), ['str'])),
                            ('type', (YLeaf(YType.identityref, 'type'), [('ydk.models.openconfig.openconfig_acl', 'ACLTYPE')])),
                        ])
                        self.set_name = None
                        self.type = None

                        self.config = Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"

                        self.acl_entries = Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries()
                        self.acl_entries.parent = self
                        self._children_name_map["acl_entries"] = "acl-entries"
                        self._segment_path = lambda: "egress-acl-set" + "[set-name='" + str(self.set_name) + "']" + "[type='" + str(self.type) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Acl.Interfaces.Interface.EgressAclSets.EgressAclSet, ['set_name', 'type'], name, value)


                    class Config(_Entity_):
                        """
                        Configuration data 
                        
                        .. attribute:: set_name
                        
                        	Reference to the ACL set name applied on egress
                        	**type**\: str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.Config>`
                        
                        .. attribute:: type
                        
                        	Reference to the ACL set type applied on egress
                        	**type**\:  :py:class:`ACLTYPE <ydk.models.openconfig.openconfig_acl.ACLTYPE>`
                        
                        

                        """

                        _prefix = 'oc-acl'
                        _revision = '2017-05-26'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "egress-acl-set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('set_name', (YLeaf(YType.str, 'set-name'), ['str'])),
                                ('type', (YLeaf(YType.identityref, 'type'), [('ydk.models.openconfig.openconfig_acl', 'ACLTYPE')])),
                            ])
                            self.set_name = None
                            self.type = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.Config, ['set_name', 'type'], name, value)



                    class State(_Entity_):
                        """
                        Operational state data for interface egress ACLs
                        
                        .. attribute:: set_name
                        
                        	Reference to the ACL set name applied on egress
                        	**type**\: str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.Config>`
                        
                        	**config**\: False
                        
                        .. attribute:: type
                        
                        	Reference to the ACL set type applied on egress
                        	**type**\:  :py:class:`ACLTYPE <ydk.models.openconfig.openconfig_acl.ACLTYPE>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-acl'
                        _revision = '2017-05-26'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "egress-acl-set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('set_name', (YLeaf(YType.str, 'set-name'), ['str'])),
                                ('type', (YLeaf(YType.identityref, 'type'), [('ydk.models.openconfig.openconfig_acl', 'ACLTYPE')])),
                            ])
                            self.set_name = None
                            self.type = None
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.State, ['set_name', 'type'], name, value)



                    class AclEntries(_Entity_):
                        """
                        Enclosing container for list of references to ACLs
                        
                        .. attribute:: acl_entry
                        
                        	List of ACL entries assigned to an interface
                        	**type**\: list of  		 :py:class:`AclEntry <ydk.models.openconfig.openconfig_acl.Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries.AclEntry>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-acl'
                        _revision = '2017-05-26'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries, self).__init__()

                            self.yang_name = "acl-entries"
                            self.yang_parent_name = "egress-acl-set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("acl-entry", ("acl_entry", Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries.AclEntry))])
                            self._leafs = OrderedDict()

                            self.acl_entry = YList(self)
                            self._segment_path = lambda: "acl-entries"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries, [], name, value)


                        class AclEntry(_Entity_):
                            """
                            List of ACL entries assigned to an interface
                            
                            .. attribute:: sequence_id  (key)
                            
                            	Reference to per\-interface acl entry key
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**refers to**\:  :py:class:`sequence_id <ydk.models.openconfig.openconfig_acl.Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries.AclEntry.State>`
                            
                            	**config**\: False
                            
                            .. attribute:: state
                            
                            	Operational state data for per\-interface ACL entries
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_acl.Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries.AclEntry.State>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-acl'
                            _revision = '2017-05-26'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries.AclEntry, self).__init__()

                                self.yang_name = "acl-entry"
                                self.yang_parent_name = "acl-entries"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['sequence_id']
                                self._child_classes = OrderedDict([("state", ("state", Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries.AclEntry.State))])
                                self._leafs = OrderedDict([
                                    ('sequence_id', (YLeaf(YType.str, 'sequence-id'), ['int'])),
                                ])
                                self.sequence_id = None

                                self.state = Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries.AclEntry.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._segment_path = lambda: "acl-entry" + "[sequence-id='" + str(self.sequence_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries.AclEntry, ['sequence_id'], name, value)


                            class State(_Entity_):
                                """
                                Operational state data for per\-interface ACL entries
                                
                                .. attribute:: sequence_id
                                
                                	Reference to an entry in the ACL set applied to an interface
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**refers to**\:  :py:class:`sequence_id <ydk.models.openconfig.openconfig_acl.Acl.AclSets.AclSet.AclEntries.AclEntry>`
                                
                                	**config**\: False
                                
                                .. attribute:: matched_packets
                                
                                	Count of the number of packets matching the current ACL entry.  An implementation should provide this counter on a per\-interface per\-ACL\-entry if possible.  If an implementation only supports ACL counters per entry (i.e., not broken out per interface), then the value should be equal to the aggregate count across all interfaces.  An implementation that provides counters per entry per interface is not required to also provide an aggregate count, e.g., per entry \-\- the user is expected to be able implement the required aggregation if such a count is needed
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: matched_octets
                                
                                	Count of the number of octets (bytes) matching the current ACL entry.  An implementation should provide this counter on a per\-interface per\-ACL\-entry if possible.  If an implementation only supports ACL counters per entry (i.e., not broken out per interface), then the value should be equal to the aggregate count across all interfaces.  An implementation that provides counters per entry per interface is not required to also provide an aggregate count, e.g., per entry \-\- the user is expected to be able implement the required aggregation if such a count is needed
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'oc-acl'
                                _revision = '2017-05-26'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries.AclEntry.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "acl-entry"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('sequence_id', (YLeaf(YType.str, 'sequence-id'), ['int'])),
                                        ('matched_packets', (YLeaf(YType.uint64, 'matched-packets'), ['int'])),
                                        ('matched_octets', (YLeaf(YType.uint64, 'matched-octets'), ['int'])),
                                    ])
                                    self.sequence_id = None
                                    self.matched_packets = None
                                    self.matched_octets = None
                                    self._segment_path = lambda: "state"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Acl.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries.AclEntry.State, ['sequence_id', 'matched_packets', 'matched_octets'], name, value)








    def clone_ptr(self):
        self._top_entity = Acl()
        return self._top_entity



class ACLIPV4(ACLTYPE):
    """
    IP\-layer ACLs with IPv4 addresses
    
    

    """

    _prefix = 'oc-acl'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/acl", pref="openconfig-acl", tag="openconfig-acl:ACL_IPV4"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ACLIPV4, self).__init__(ns, pref, tag)



class ACLIPV6(ACLTYPE):
    """
    IP\-layer ACLs with IPv6 addresses
    
    

    """

    _prefix = 'oc-acl'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/acl", pref="openconfig-acl", tag="openconfig-acl:ACL_IPV6"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ACLIPV6, self).__init__(ns, pref, tag)



class ACLL2(ACLTYPE):
    """
    MAC\-layer ACLs
    
    

    """

    _prefix = 'oc-acl'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/acl", pref="openconfig-acl", tag="openconfig-acl:ACL_L2"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ACLL2, self).__init__(ns, pref, tag)



class ACLMIXED(ACLTYPE):
    """
    Mixed\-mode ACL that specifies L2 and L3 protocol
    fields.  This ACL type is not implemented by many
    routing/switching devices.
    
    

    """

    _prefix = 'oc-acl'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/acl", pref="openconfig-acl", tag="openconfig-acl:ACL_MIXED"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ACLMIXED, self).__init__(ns, pref, tag)



class ACCEPT(FORWARDINGACTION):
    """
    Accept the packet
    
    

    """

    _prefix = 'oc-acl'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/acl", pref="openconfig-acl", tag="openconfig-acl:ACCEPT"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ACCEPT, self).__init__(ns, pref, tag)



class DROP(FORWARDINGACTION):
    """
    Drop packet without sending any ICMP error message
    
    

    """

    _prefix = 'oc-acl'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/acl", pref="openconfig-acl", tag="openconfig-acl:DROP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DROP, self).__init__(ns, pref, tag)



class REJECT(FORWARDINGACTION):
    """
    Drop the packet and send an ICMP error message to the source
    
    

    """

    _prefix = 'oc-acl'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/acl", pref="openconfig-acl", tag="openconfig-acl:REJECT"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(REJECT, self).__init__(ns, pref, tag)



class LOGSYSLOG(LOGACTION):
    """
    Log the packet in Syslog
    
    

    """

    _prefix = 'oc-acl'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/acl", pref="openconfig-acl", tag="openconfig-acl:LOG_SYSLOG"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(LOGSYSLOG, self).__init__(ns, pref, tag)



class LOGNONE(LOGACTION):
    """
    No logging
    
    

    """

    _prefix = 'oc-acl'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/acl", pref="openconfig-acl", tag="openconfig-acl:LOG_NONE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(LOGNONE, self).__init__(ns, pref, tag)



class INTERFACEONLY(ACLCOUNTERCAPABILITY):
    """
    ACL counters are available and reported only per interface
    
    

    """

    _prefix = 'oc-acl'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/acl", pref="openconfig-acl", tag="openconfig-acl:INTERFACE_ONLY"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(INTERFACEONLY, self).__init__(ns, pref, tag)



class AGGREGATEONLY(ACLCOUNTERCAPABILITY):
    """
    ACL counters are aggregated over all interfaces, and reported
    only per ACL entry
    
    

    """

    _prefix = 'oc-acl'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/acl", pref="openconfig-acl", tag="openconfig-acl:AGGREGATE_ONLY"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AGGREGATEONLY, self).__init__(ns, pref, tag)



class INTERFACEAGGREGATE(ACLCOUNTERCAPABILITY):
    """
    ACL counters are reported per interface, and also aggregated
    and reported per ACL entry.
    
    

    """

    _prefix = 'oc-acl'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/acl", pref="openconfig-acl", tag="openconfig-acl:INTERFACE_AGGREGATE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(INTERFACEAGGREGATE, self).__init__(ns, pref, tag)




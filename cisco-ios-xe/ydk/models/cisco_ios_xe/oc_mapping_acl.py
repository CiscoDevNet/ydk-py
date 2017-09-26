""" oc_mapping_acl 

This module defines mapping state data
that must be saved to implement the openconfig\-acl
model because the capabilities are not implemented
on XE devices

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AclMapping(Entity):
    """
    Top level enclosing container for ACL model config
    and operational state data
    
    .. attribute:: acl_sets
    
    	Access list entries variables enclosing container
    	**type**\:   :py:class:`AclSets <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.AclSets>`
    
    .. attribute:: interfaces
    
    	Enclosing container for the list of interfaces on which ACLs are set
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces>`
    
    

    """

    _prefix = 'oc-map-acl'
    _revision = '2017-01-17'

    def __init__(self):
        super(AclMapping, self).__init__()
        self._top_entity = None

        self.yang_name = "acl-mapping"
        self.yang_parent_name = "oc-mapping-acl"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"acl-sets" : ("acl_sets", AclMapping.AclSets), "interfaces" : ("interfaces", AclMapping.Interfaces)}
        self._child_list_classes = {}

        self.acl_sets = AclMapping.AclSets()
        self.acl_sets.parent = self
        self._children_name_map["acl_sets"] = "acl-sets"
        self._children_yang_names.add("acl-sets")

        self.interfaces = AclMapping.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")
        self._segment_path = lambda: "oc-mapping-acl:acl-mapping"


    class AclSets(Entity):
        """
        Access list entries variables enclosing container
        
        .. attribute:: acl_set
        
        	List of ACL sets, each comprising of a list of ACL entries
        	**type**\: list of    :py:class:`AclSet <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.AclSets.AclSet>`
        
        

        """

        _prefix = 'oc-map-acl'
        _revision = '2017-01-17'

        def __init__(self):
            super(AclMapping.AclSets, self).__init__()

            self.yang_name = "acl-sets"
            self.yang_parent_name = "acl-mapping"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"acl-set" : ("acl_set", AclMapping.AclSets.AclSet)}

            self.acl_set = YList(self)
            self._segment_path = lambda: "acl-sets"
            self._absolute_path = lambda: "oc-mapping-acl:acl-mapping/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(AclMapping.AclSets, [], name, value)


        class AclSet(Entity):
            """
            List of ACL sets, each comprising of a list of ACL
            entries
            
            .. attribute:: name  <key>
            
            	Reference to the name list key
            	**type**\:  str
            
            .. attribute:: config
            
            	Access list config
            	**type**\:   :py:class:`Config <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.AclSets.AclSet.Config>`
            
            

            """

            _prefix = 'oc-map-acl'
            _revision = '2017-01-17'

            def __init__(self):
                super(AclMapping.AclSets.AclSet, self).__init__()

                self.yang_name = "acl-set"
                self.yang_parent_name = "acl-sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"config" : ("config", AclMapping.AclSets.AclSet.Config)}
                self._child_list_classes = {}

                self.name = YLeaf(YType.str, "name")

                self.config = AclMapping.AclSets.AclSet.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")
                self._segment_path = lambda: "acl-set" + "[name='" + self.name.get() + "']"
                self._absolute_path = lambda: "oc-mapping-acl:acl-mapping/acl-sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(AclMapping.AclSets.AclSet, ['name'], name, value)


            class Config(Entity):
                """
                Access list config
                
                .. attribute:: acl_entries
                
                	Access list entries container
                	**type**\:   :py:class:`AclEntries <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.AclSets.AclSet.Config.AclEntries>`
                
                .. attribute:: acl_type
                
                	The type of the access\-list set
                	**type**\:   :py:class:`IpVersion <ydk.models.ietf.ietf_inet_types.IpVersion>`
                
                .. attribute:: description
                
                	Description, or comment, for the ACL set
                	**type**\:  str
                
                .. attribute:: name
                
                	The name of the access\-list set
                	**type**\:  str
                
                

                """

                _prefix = 'oc-map-acl'
                _revision = '2017-01-17'

                def __init__(self):
                    super(AclMapping.AclSets.AclSet.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "acl-set"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"acl-entries" : ("acl_entries", AclMapping.AclSets.AclSet.Config.AclEntries)}
                    self._child_list_classes = {}

                    self.acl_type = YLeaf(YType.enumeration, "acl-type")

                    self.description = YLeaf(YType.str, "description")

                    self.name = YLeaf(YType.str, "name")

                    self.acl_entries = AclMapping.AclSets.AclSet.Config.AclEntries()
                    self.acl_entries.parent = self
                    self._children_name_map["acl_entries"] = "acl-entries"
                    self._children_yang_names.add("acl-entries")
                    self._segment_path = lambda: "config"

                def __setattr__(self, name, value):
                    self._perform_setattr(AclMapping.AclSets.AclSet.Config, ['acl_type', 'description', 'name'], name, value)


                class AclEntries(Entity):
                    """
                    Access list entries container
                    
                    .. attribute:: acl_entry
                    
                    	List of ACL entries comprising an ACL set
                    	**type**\: list of    :py:class:`AclEntry <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.AclSets.AclSet.Config.AclEntries.AclEntry>`
                    
                    

                    """

                    _prefix = 'oc-map-acl'
                    _revision = '2017-01-17'

                    def __init__(self):
                        super(AclMapping.AclSets.AclSet.Config.AclEntries, self).__init__()

                        self.yang_name = "acl-entries"
                        self.yang_parent_name = "config"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"acl-entry" : ("acl_entry", AclMapping.AclSets.AclSet.Config.AclEntries.AclEntry)}

                        self.acl_entry = YList(self)
                        self._segment_path = lambda: "acl-entries"

                    def __setattr__(self, name, value):
                        self._perform_setattr(AclMapping.AclSets.AclSet.Config.AclEntries, [], name, value)


                    class AclEntry(Entity):
                        """
                        List of ACL entries comprising an ACL set
                        
                        .. attribute:: sequence_id  <key>
                        
                        	The sequence id determines the order in which ACL entries are applied.  The sequence id must be unique for each entry in an ACL set.  Target devices should apply the ACL entry rules in the order determined by sequence id, rather than the relying only on order in the list
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_version
                        
                        	IP version of the header
                        	**type**\:   :py:class:`IpVersion <ydk.models.ietf.ietf_inet_types.IpVersion>`
                        
                        

                        """

                        _prefix = 'oc-map-acl'
                        _revision = '2017-01-17'

                        def __init__(self):
                            super(AclMapping.AclSets.AclSet.Config.AclEntries.AclEntry, self).__init__()

                            self.yang_name = "acl-entry"
                            self.yang_parent_name = "acl-entries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.sequence_id = YLeaf(YType.uint32, "sequence-id")

                            self.ip_version = YLeaf(YType.enumeration, "ip-version")
                            self._segment_path = lambda: "acl-entry" + "[sequence-id='" + self.sequence_id.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(AclMapping.AclSets.AclSet.Config.AclEntries.AclEntry, ['sequence_id', 'ip_version'], name, value)


    class Interfaces(Entity):
        """
        Enclosing container for the list of interfaces on which
        ACLs are set
        
        .. attribute:: interface
        
        	List of interfaces on which ACLs are set
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface>`
        
        

        """

        _prefix = 'oc-map-acl'
        _revision = '2017-01-17'

        def __init__(self):
            super(AclMapping.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "acl-mapping"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface" : ("interface", AclMapping.Interfaces.Interface)}

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "oc-mapping-acl:acl-mapping/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(AclMapping.Interfaces, [], name, value)


        class Interface(Entity):
            """
            List of interfaces on which ACLs are set
            
            .. attribute:: id  <key>
            
            	Reference to the interface id list key
            	**type**\:  str
            
            .. attribute:: config
            
            	Configuration for ACL per\-interface data
            	**type**\:   :py:class:`Config <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.Config>`
            
            .. attribute:: egress_acl_sets
            
            	Enclosing container the list of egress ACLs on the interface
            	**type**\:   :py:class:`EgressAclSets <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.EgressAclSets>`
            
            .. attribute:: ingress_acl_sets
            
            	Enclosing container the list of ingress ACLs on the interface
            	**type**\:   :py:class:`IngressAclSets <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.IngressAclSets>`
            
            .. attribute:: interface_ref
            
            	Reference to an interface or subinterface
            	**type**\:   :py:class:`InterfaceRef <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.InterfaceRef>`
            
            

            """

            _prefix = 'oc-map-acl'
            _revision = '2017-01-17'

            def __init__(self):
                super(AclMapping.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"config" : ("config", AclMapping.Interfaces.Interface.Config), "egress-acl-sets" : ("egress_acl_sets", AclMapping.Interfaces.Interface.EgressAclSets), "ingress-acl-sets" : ("ingress_acl_sets", AclMapping.Interfaces.Interface.IngressAclSets), "interface-ref" : ("interface_ref", AclMapping.Interfaces.Interface.InterfaceRef)}
                self._child_list_classes = {}

                self.id = YLeaf(YType.str, "id")

                self.config = AclMapping.Interfaces.Interface.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.egress_acl_sets = AclMapping.Interfaces.Interface.EgressAclSets()
                self.egress_acl_sets.parent = self
                self._children_name_map["egress_acl_sets"] = "egress-acl-sets"
                self._children_yang_names.add("egress-acl-sets")

                self.ingress_acl_sets = AclMapping.Interfaces.Interface.IngressAclSets()
                self.ingress_acl_sets.parent = self
                self._children_name_map["ingress_acl_sets"] = "ingress-acl-sets"
                self._children_yang_names.add("ingress-acl-sets")

                self.interface_ref = AclMapping.Interfaces.Interface.InterfaceRef()
                self.interface_ref.parent = self
                self._children_name_map["interface_ref"] = "interface-ref"
                self._children_yang_names.add("interface-ref")
                self._segment_path = lambda: "interface" + "[id='" + self.id.get() + "']"
                self._absolute_path = lambda: "oc-mapping-acl:acl-mapping/interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(AclMapping.Interfaces.Interface, ['id'], name, value)


            class Config(Entity):
                """
                Configuration for ACL per\-interface data
                
                .. attribute:: id
                
                	User\-defined identifier for the interface \-\- a common convention could be '<if name>.<subif index>'
                	**type**\:  str
                
                

                """

                _prefix = 'oc-map-acl'
                _revision = '2017-01-17'

                def __init__(self):
                    super(AclMapping.Interfaces.Interface.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.id = YLeaf(YType.str, "id")
                    self._segment_path = lambda: "config"

                def __setattr__(self, name, value):
                    self._perform_setattr(AclMapping.Interfaces.Interface.Config, ['id'], name, value)


            class EgressAclSets(Entity):
                """
                Enclosing container the list of egress ACLs on the
                interface
                
                .. attribute:: egress_acl_set
                
                	List of egress ACLs on the interface
                	**type**\: list of    :py:class:`EgressAclSet <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet>`
                
                

                """

                _prefix = 'oc-map-acl'
                _revision = '2017-01-17'

                def __init__(self):
                    super(AclMapping.Interfaces.Interface.EgressAclSets, self).__init__()

                    self.yang_name = "egress-acl-sets"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"egress-acl-set" : ("egress_acl_set", AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet)}

                    self.egress_acl_set = YList(self)
                    self._segment_path = lambda: "egress-acl-sets"

                def __setattr__(self, name, value):
                    self._perform_setattr(AclMapping.Interfaces.Interface.EgressAclSets, [], name, value)


                class EgressAclSet(Entity):
                    """
                    List of egress ACLs on the interface
                    
                    .. attribute:: set_name  <key>
                    
                    	Reference to set name list key
                    	**type**\:  str
                    
                    .. attribute:: acl_entries
                    
                    	Enclosing container for list of references to ACLs
                    	**type**\:   :py:class:`AclEntries <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries>`
                    
                    .. attribute:: config
                    
                    	Configuration data 
                    	**type**\:   :py:class:`Config <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.Config>`
                    
                    

                    """

                    _prefix = 'oc-map-acl'
                    _revision = '2017-01-17'

                    def __init__(self):
                        super(AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet, self).__init__()

                        self.yang_name = "egress-acl-set"
                        self.yang_parent_name = "egress-acl-sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"acl-entries" : ("acl_entries", AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries), "config" : ("config", AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.Config)}
                        self._child_list_classes = {}

                        self.set_name = YLeaf(YType.str, "set-name")

                        self.acl_entries = AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries()
                        self.acl_entries.parent = self
                        self._children_name_map["acl_entries"] = "acl-entries"
                        self._children_yang_names.add("acl-entries")

                        self.config = AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")
                        self._segment_path = lambda: "egress-acl-set" + "[set-name='" + self.set_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet, ['set_name'], name, value)


                    class AclEntries(Entity):
                        """
                        Enclosing container for list of references to ACLs
                        
                        .. attribute:: acl_entry
                        
                        	List of ACL entries assigned to an interface
                        	**type**\: list of    :py:class:`AclEntry <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries.AclEntry>`
                        
                        

                        """

                        _prefix = 'oc-map-acl'
                        _revision = '2017-01-17'

                        def __init__(self):
                            super(AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries, self).__init__()

                            self.yang_name = "acl-entries"
                            self.yang_parent_name = "egress-acl-set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"acl-entry" : ("acl_entry", AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries.AclEntry)}

                            self.acl_entry = YList(self)
                            self._segment_path = lambda: "acl-entries"

                        def __setattr__(self, name, value):
                            self._perform_setattr(AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries, [], name, value)


                        class AclEntry(Entity):
                            """
                            List of ACL entries assigned to an interface
                            
                            .. attribute:: sequence_id  <key>
                            
                            	Reference to per\-interface acl entry key
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'oc-map-acl'
                            _revision = '2017-01-17'

                            def __init__(self):
                                super(AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries.AclEntry, self).__init__()

                                self.yang_name = "acl-entry"
                                self.yang_parent_name = "acl-entries"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.sequence_id = YLeaf(YType.str, "sequence-id")
                                self._segment_path = lambda: "acl-entry" + "[sequence-id='" + self.sequence_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.AclEntries.AclEntry, ['sequence_id'], name, value)


                    class Config(Entity):
                        """
                        Configuration data 
                        
                        .. attribute:: set_name
                        
                        	Reference to the ACL set applied on egress
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'oc-map-acl'
                        _revision = '2017-01-17'

                        def __init__(self):
                            super(AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "egress-acl-set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.set_name = YLeaf(YType.str, "set-name")
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(AclMapping.Interfaces.Interface.EgressAclSets.EgressAclSet.Config, ['set_name'], name, value)


            class IngressAclSets(Entity):
                """
                Enclosing container the list of ingress ACLs on the
                interface
                
                .. attribute:: ingress_acl_set
                
                	List of ingress ACLs on the interface
                	**type**\: list of    :py:class:`IngressAclSet <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet>`
                
                

                """

                _prefix = 'oc-map-acl'
                _revision = '2017-01-17'

                def __init__(self):
                    super(AclMapping.Interfaces.Interface.IngressAclSets, self).__init__()

                    self.yang_name = "ingress-acl-sets"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"ingress-acl-set" : ("ingress_acl_set", AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet)}

                    self.ingress_acl_set = YList(self)
                    self._segment_path = lambda: "ingress-acl-sets"

                def __setattr__(self, name, value):
                    self._perform_setattr(AclMapping.Interfaces.Interface.IngressAclSets, [], name, value)


                class IngressAclSet(Entity):
                    """
                    List of ingress ACLs on the interface
                    
                    .. attribute:: set_name  <key>
                    
                    	Reference to set name list key
                    	**type**\:  str
                    
                    .. attribute:: acl_entries
                    
                    	Enclosing container for list of references to ACLs
                    	**type**\:   :py:class:`AclEntries <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries>`
                    
                    .. attribute:: config
                    
                    	Configuration data 
                    	**type**\:   :py:class:`Config <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for interface ingress ACLs
                    	**type**\:   :py:class:`State <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.State>`
                    
                    

                    """

                    _prefix = 'oc-map-acl'
                    _revision = '2017-01-17'

                    def __init__(self):
                        super(AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet, self).__init__()

                        self.yang_name = "ingress-acl-set"
                        self.yang_parent_name = "ingress-acl-sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"acl-entries" : ("acl_entries", AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries), "config" : ("config", AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.Config), "state" : ("state", AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.State)}
                        self._child_list_classes = {}

                        self.set_name = YLeaf(YType.str, "set-name")

                        self.acl_entries = AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries()
                        self.acl_entries.parent = self
                        self._children_name_map["acl_entries"] = "acl-entries"
                        self._children_yang_names.add("acl-entries")

                        self.config = AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "ingress-acl-set" + "[set-name='" + self.set_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet, ['set_name'], name, value)


                    class AclEntries(Entity):
                        """
                        Enclosing container for list of references to ACLs
                        
                        .. attribute:: acl_entry
                        
                        	List of ACL entries assigned to an interface
                        	**type**\: list of    :py:class:`AclEntry <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries.AclEntry>`
                        
                        

                        """

                        _prefix = 'oc-map-acl'
                        _revision = '2017-01-17'

                        def __init__(self):
                            super(AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries, self).__init__()

                            self.yang_name = "acl-entries"
                            self.yang_parent_name = "ingress-acl-set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"acl-entry" : ("acl_entry", AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries.AclEntry)}

                            self.acl_entry = YList(self)
                            self._segment_path = lambda: "acl-entries"

                        def __setattr__(self, name, value):
                            self._perform_setattr(AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries, [], name, value)


                        class AclEntry(Entity):
                            """
                            List of ACL entries assigned to an interface
                            
                            .. attribute:: sequence_id  <key>
                            
                            	Reference to per\-interface acl entry key
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'oc-map-acl'
                            _revision = '2017-01-17'

                            def __init__(self):
                                super(AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries.AclEntry, self).__init__()

                                self.yang_name = "acl-entry"
                                self.yang_parent_name = "acl-entries"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.sequence_id = YLeaf(YType.str, "sequence-id")
                                self._segment_path = lambda: "acl-entry" + "[sequence-id='" + self.sequence_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.AclEntries.AclEntry, ['sequence_id'], name, value)


                    class Config(Entity):
                        """
                        Configuration data 
                        
                        .. attribute:: set_name
                        
                        	Reference to the ACL set applied on ingress
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'oc-map-acl'
                        _revision = '2017-01-17'

                        def __init__(self):
                            super(AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "ingress-acl-set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.set_name = YLeaf(YType.str, "set-name")
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.Config, ['set_name'], name, value)


                    class State(Entity):
                        """
                        Operational state data for interface ingress ACLs
                        
                        .. attribute:: set_name
                        
                        	Reference to the ACL set applied on ingress
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'oc-map-acl'
                        _revision = '2017-01-17'

                        def __init__(self):
                            super(AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "ingress-acl-set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.set_name = YLeaf(YType.str, "set-name")
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(AclMapping.Interfaces.Interface.IngressAclSets.IngressAclSet.State, ['set_name'], name, value)


            class InterfaceRef(Entity):
                """
                Reference to an interface or subinterface
                
                .. attribute:: config
                
                	Configured reference to interface / subinterface
                	**type**\:   :py:class:`Config <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.InterfaceRef.Config>`
                
                .. attribute:: state
                
                	Operational state for interface\-ref
                	**type**\:   :py:class:`State <ydk.models.cisco_ios_xe.oc_mapping_acl.AclMapping.Interfaces.Interface.InterfaceRef.State>`
                
                

                """

                _prefix = 'oc-map-acl'
                _revision = '2017-01-17'

                def __init__(self):
                    super(AclMapping.Interfaces.Interface.InterfaceRef, self).__init__()

                    self.yang_name = "interface-ref"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"config" : ("config", AclMapping.Interfaces.Interface.InterfaceRef.Config), "state" : ("state", AclMapping.Interfaces.Interface.InterfaceRef.State)}
                    self._child_list_classes = {}

                    self.config = AclMapping.Interfaces.Interface.InterfaceRef.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = AclMapping.Interfaces.Interface.InterfaceRef.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "interface-ref"


                class Config(Entity):
                    """
                    Configured reference to interface / subinterface
                    
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

                    _prefix = 'oc-map-acl'
                    _revision = '2017-01-17'

                    def __init__(self):
                        super(AclMapping.Interfaces.Interface.InterfaceRef.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "interface-ref"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.interface = YLeaf(YType.str, "interface")

                        self.subinterface = YLeaf(YType.str, "subinterface")
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(AclMapping.Interfaces.Interface.InterfaceRef.Config, ['interface', 'subinterface'], name, value)


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

                    _prefix = 'oc-map-acl'
                    _revision = '2017-01-17'

                    def __init__(self):
                        super(AclMapping.Interfaces.Interface.InterfaceRef.State, self).__init__()

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
                        self._perform_setattr(AclMapping.Interfaces.Interface.InterfaceRef.State, ['interface', 'subinterface'], name, value)

    def clone_ptr(self):
        self._top_entity = AclMapping()
        return self._top_entity


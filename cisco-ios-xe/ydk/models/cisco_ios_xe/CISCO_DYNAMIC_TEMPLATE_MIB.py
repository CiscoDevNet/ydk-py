""" CISCO_DYNAMIC_TEMPLATE_MIB 

This MIB defines objects that describe dynamic templates.  A
dynamic template is a set of configuration attributes that a
system can dynamically apply to a target.

The target of a dynamic template is the entity configured by the
system using the configuration attributes contained by a 
template. At the time of this writing, an interface represents
the only valid target of a dynamic template.  However, the
architecture does not prevent other target types, and hence, the
MIB definition generalizes the notion of a target to allow for
this.

Generally, the system does not directly apply the attributes
contained by a dynamic template to an associated
target.  The system might generate a derived configuration from
the set of dynamic templates associated with the target.  A
derived configuration represents the union of the configuration
attributes contained by each associated dynamic template.  In
the case of a conflict (i.e., more than one dynamic template
specifies the same configuration attribute), the system accepts
the configuration attribute from the dynamic template with the
highest precedence.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoDynamicTemplateMib(Entity):
    """
    
    
    .. attribute:: cdtethernettemplatetable
    
    	This table contains attributes relating to dynamic interfaces initiated on Ethernet virtual interfaces (e.g., EoMPLS) or automatically created VLANs.  This table has a sparse\-dependent relationship on the cdtTemplateTable, containing a row for each dynamic template having a cdtTemplateType of one of the following values\:      'derived'     'ethernet'
    	**type**\:   :py:class:`Cdtethernettemplatetable <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtethernettemplatetable>`
    
    .. attribute:: cdtiftemplatetable
    
    	This table contains attributes relating to interface configuration.  This table has a sparse\-dependent relationship on the cdtTemplateTable, containing a row for each dynamic template having a cdtTemplateType of one of the following values\:      'derived'     'ppp'     'ethernet'     'ipSubscriber'
    	**type**\:   :py:class:`Cdtiftemplatetable <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtiftemplatetable>`
    
    .. attribute:: cdtppppeeripaddrpooltable
    
    	This table contains a prioritized list of named pools for each PPP template.  A list corresponding to a PPP template specifies the pools the system searches in an attempt to assign an IP address to the peer of a target PPP connection. The system searches the pools in the order of their priority.  This table has an expansion dependent relationship on the cdtPppTemplateTable, containing zero or more rows for each PPP template
    	**type**\:   :py:class:`Cdtppppeeripaddrpooltable <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtppppeeripaddrpooltable>`
    
    .. attribute:: cdtppptemplatetable
    
    	This table contains attributes relating to PPP connection configuration.  This table has a sparse\-dependent relationship on the cdtTemplateTable, containing a row for each dynamic template having a cdtTemplateType of one of the following values\:      'derived'     'ppp'
    	**type**\:   :py:class:`Cdtppptemplatetable <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtppptemplatetable>`
    
    .. attribute:: cdtsrvtemplatetable
    
    	This table contains attributes relating to a service.  This table has a sparse\-dependent relationship on the cdtTemplateTable, containing a row for each dynamic template having a cdtTemplateType of one of the following values\:      'derived'     'service'
    	**type**\:   :py:class:`Cdtsrvtemplatetable <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtsrvtemplatetable>`
    
    .. attribute:: cdttemplateassociationtable
    
    	This table contains a list of templates associated with each target.  This table has an expansion dependent relationship on the cdtTemplateTargetTable, containing zero or more rows for each target
    	**type**\:   :py:class:`Cdttemplateassociationtable <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdttemplateassociationtable>`
    
    .. attribute:: cdttemplatecommontable
    
    	This table contains attributes relating to all dynamic templates.  Observe that the type of dynamic templates containing these attributes may change with the addition of new dynamic template types.  This table has a sparse\-dependent relationship on the cdtTemplateTable, containing a row for each dynamic template having a cdtTemplateType of one of the following values\:      'derived'     'ppp'     'ethernet'     'ipSubscriber'     'service'
    	**type**\:   :py:class:`Cdttemplatecommontable <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdttemplatecommontable>`
    
    .. attribute:: cdttemplatetable
    
    	This table lists the dynamic templates maintained by the system, including those that have been locally\-configured on the system and those pushed to the system by external policy servers
    	**type**\:   :py:class:`Cdttemplatetable <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdttemplatetable>`
    
    .. attribute:: cdttemplatetargettable
    
    	This table contains a list of targets associated with one or more dynamic templates
    	**type**\:   :py:class:`Cdttemplatetargettable <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdttemplatetargettable>`
    
    .. attribute:: cdttemplateusagetable
    
    	This table contains a list of targets using each dynamic template.  This table has an expansion dependent relationship on the cdtTemplateTable, containing zero or more rows for each dynamic template
    	**type**\:   :py:class:`Cdttemplateusagetable <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdttemplateusagetable>`
    
    

    """

    _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
    _revision = '2007-09-06'

    def __init__(self):
        super(CiscoDynamicTemplateMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-DYNAMIC-TEMPLATE-MIB"
        self.yang_parent_name = "CISCO-DYNAMIC-TEMPLATE-MIB"

        self.cdtethernettemplatetable = CiscoDynamicTemplateMib.Cdtethernettemplatetable()
        self.cdtethernettemplatetable.parent = self
        self._children_name_map["cdtethernettemplatetable"] = "cdtEthernetTemplateTable"
        self._children_yang_names.add("cdtEthernetTemplateTable")

        self.cdtiftemplatetable = CiscoDynamicTemplateMib.Cdtiftemplatetable()
        self.cdtiftemplatetable.parent = self
        self._children_name_map["cdtiftemplatetable"] = "cdtIfTemplateTable"
        self._children_yang_names.add("cdtIfTemplateTable")

        self.cdtppppeeripaddrpooltable = CiscoDynamicTemplateMib.Cdtppppeeripaddrpooltable()
        self.cdtppppeeripaddrpooltable.parent = self
        self._children_name_map["cdtppppeeripaddrpooltable"] = "cdtPppPeerIpAddrPoolTable"
        self._children_yang_names.add("cdtPppPeerIpAddrPoolTable")

        self.cdtppptemplatetable = CiscoDynamicTemplateMib.Cdtppptemplatetable()
        self.cdtppptemplatetable.parent = self
        self._children_name_map["cdtppptemplatetable"] = "cdtPppTemplateTable"
        self._children_yang_names.add("cdtPppTemplateTable")

        self.cdtsrvtemplatetable = CiscoDynamicTemplateMib.Cdtsrvtemplatetable()
        self.cdtsrvtemplatetable.parent = self
        self._children_name_map["cdtsrvtemplatetable"] = "cdtSrvTemplateTable"
        self._children_yang_names.add("cdtSrvTemplateTable")

        self.cdttemplateassociationtable = CiscoDynamicTemplateMib.Cdttemplateassociationtable()
        self.cdttemplateassociationtable.parent = self
        self._children_name_map["cdttemplateassociationtable"] = "cdtTemplateAssociationTable"
        self._children_yang_names.add("cdtTemplateAssociationTable")

        self.cdttemplatecommontable = CiscoDynamicTemplateMib.Cdttemplatecommontable()
        self.cdttemplatecommontable.parent = self
        self._children_name_map["cdttemplatecommontable"] = "cdtTemplateCommonTable"
        self._children_yang_names.add("cdtTemplateCommonTable")

        self.cdttemplatetable = CiscoDynamicTemplateMib.Cdttemplatetable()
        self.cdttemplatetable.parent = self
        self._children_name_map["cdttemplatetable"] = "cdtTemplateTable"
        self._children_yang_names.add("cdtTemplateTable")

        self.cdttemplatetargettable = CiscoDynamicTemplateMib.Cdttemplatetargettable()
        self.cdttemplatetargettable.parent = self
        self._children_name_map["cdttemplatetargettable"] = "cdtTemplateTargetTable"
        self._children_yang_names.add("cdtTemplateTargetTable")

        self.cdttemplateusagetable = CiscoDynamicTemplateMib.Cdttemplateusagetable()
        self.cdttemplateusagetable.parent = self
        self._children_name_map["cdttemplateusagetable"] = "cdtTemplateUsageTable"
        self._children_yang_names.add("cdtTemplateUsageTable")


    class Cdttemplatetable(Entity):
        """
        This table lists the dynamic templates maintained by the
        system, including those that have been locally\-configured on the
        system and those pushed to the system by external policy
        servers.
        
        .. attribute:: cdttemplateentry
        
        	An entry describes a dynamic template, which serves as a container for configuration attributes.  The configuration attributes contained by a dynamic template depends on its type.  The system automatically creates a corresponding entry when a dynamic template has been created through another management entity (e.g., the system's local console).  Likewise, the system automatically destroys a corresponding entry when a dynamic template has been destroyed through another management entity.  The system automatically creates a corresponding entry when an external policy server pushes a user profile or a service profile to the system.  The system automatically creates a corresponding entry when it generates a derived configuration
        	**type**\: list of    :py:class:`Cdttemplateentry <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdttemplatetable.Cdttemplateentry>`
        
        

        """

        _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
        _revision = '2007-09-06'

        def __init__(self):
            super(CiscoDynamicTemplateMib.Cdttemplatetable, self).__init__()

            self.yang_name = "cdtTemplateTable"
            self.yang_parent_name = "CISCO-DYNAMIC-TEMPLATE-MIB"

            self.cdttemplateentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoDynamicTemplateMib.Cdttemplatetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoDynamicTemplateMib.Cdttemplatetable, self).__setattr__(name, value)


        class Cdttemplateentry(Entity):
            """
            An entry describes a dynamic template, which serves as a
            container for configuration attributes.  The configuration
            attributes contained by a dynamic template depends on its type.
            
            The system automatically creates a corresponding entry when a
            dynamic template has been created through another management
            entity (e.g., the system's local console).  Likewise, the system
            automatically destroys a corresponding entry when a dynamic
            template has been destroyed through another management entity.
            
            The system automatically creates a corresponding entry when an
            external policy server pushes a user profile or a service
            profile to the system.
            
            The system automatically creates a corresponding entry when it
            generates a derived configuration.
            
            .. attribute:: cdttemplatename  <key>
            
            	This object indicates a string\-value that uniquely identifies the dynamic template.  If the corresponding instance of cdtTemplateSrc is not 'local', then the system automatically generates the name identifying the dynamic template
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cdttemplatesrc
            
            	This object specifies the source of the dynamic template\:  'other'     The implementation of the MIB module does not recognize the     source of the dynamic template.  'derived'     The system created the set of attributes from one or     more dynamic templates.  'local'     The dynamic template was locally configured through a     management entity, such as the local console or a SNMP     entity.  'aaaUserProfile'     The dynamic template originated from a user profile     pushed from an external policy server.  'aaaServiceProfile'     The dynamic template originated from a service profile     pushed from an external policy server
            	**type**\:   :py:class:`Cdttemplatesrc <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdttemplatetable.Cdttemplateentry.Cdttemplatesrc>`
            
            .. attribute:: cdttemplatestatus
            
            	This object specifies the status of the dynamic template.  The following columns must be valid before activating a dynamic template\:      \- cdtTemplateStorage     \- cdtTemplateType  However, these objects specify a default value.  Thus, it is possible to use create\-and\-go semantics without setting any additional columns.  An implementation must allow the EMS/NMS to modify any column when this column is 'active', including columns defined in tables that have a one\-to\-one or sparse dependent relationship on this table
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cdttemplatestorage
            
            	This object specifies what happens to the dynamic template upon restart.  If the corresponding instance of cdtTemplateSrc is not 'local', then this column must be 'volatile'
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: cdttemplatetype
            
            	This object indicates the types of dynamic template
            	**type**\:   :py:class:`Dynamictemplatetype <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_TC_MIB.Dynamictemplatetype>`
            
            .. attribute:: cdttemplateusagecount
            
            	This object specifies the number of targets using a dynamic template
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
            _revision = '2007-09-06'

            def __init__(self):
                super(CiscoDynamicTemplateMib.Cdttemplatetable.Cdttemplateentry, self).__init__()

                self.yang_name = "cdtTemplateEntry"
                self.yang_parent_name = "cdtTemplateTable"

                self.cdttemplatename = YLeaf(YType.str, "cdtTemplateName")

                self.cdttemplatesrc = YLeaf(YType.enumeration, "cdtTemplateSrc")

                self.cdttemplatestatus = YLeaf(YType.enumeration, "cdtTemplateStatus")

                self.cdttemplatestorage = YLeaf(YType.enumeration, "cdtTemplateStorage")

                self.cdttemplatetype = YLeaf(YType.enumeration, "cdtTemplateType")

                self.cdttemplateusagecount = YLeaf(YType.uint32, "cdtTemplateUsageCount")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cdttemplatename",
                                "cdttemplatesrc",
                                "cdttemplatestatus",
                                "cdttemplatestorage",
                                "cdttemplatetype",
                                "cdttemplateusagecount") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoDynamicTemplateMib.Cdttemplatetable.Cdttemplateentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoDynamicTemplateMib.Cdttemplatetable.Cdttemplateentry, self).__setattr__(name, value)

            class Cdttemplatesrc(Enum):
                """
                Cdttemplatesrc

                This object specifies the source of the dynamic template\:

                'other'

                    The implementation of the MIB module does not recognize the

                    source of the dynamic template.

                'derived'

                    The system created the set of attributes from one or

                    more dynamic templates.

                'local'

                    The dynamic template was locally configured through a

                    management entity, such as the local console or a SNMP

                    entity.

                'aaaUserProfile'

                    The dynamic template originated from a user profile

                    pushed from an external policy server.

                'aaaServiceProfile'

                    The dynamic template originated from a service profile

                    pushed from an external policy server.

                .. data:: other = 1

                .. data:: derived = 2

                .. data:: local = 3

                .. data:: aaaUserProfile = 4

                .. data:: aaaServiceProfile = 5

                """

                other = Enum.YLeaf(1, "other")

                derived = Enum.YLeaf(2, "derived")

                local = Enum.YLeaf(3, "local")

                aaaUserProfile = Enum.YLeaf(4, "aaaUserProfile")

                aaaServiceProfile = Enum.YLeaf(5, "aaaServiceProfile")


            def has_data(self):
                return (
                    self.cdttemplatename.is_set or
                    self.cdttemplatesrc.is_set or
                    self.cdttemplatestatus.is_set or
                    self.cdttemplatestorage.is_set or
                    self.cdttemplatetype.is_set or
                    self.cdttemplateusagecount.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cdttemplatename.yfilter != YFilter.not_set or
                    self.cdttemplatesrc.yfilter != YFilter.not_set or
                    self.cdttemplatestatus.yfilter != YFilter.not_set or
                    self.cdttemplatestorage.yfilter != YFilter.not_set or
                    self.cdttemplatetype.yfilter != YFilter.not_set or
                    self.cdttemplateusagecount.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cdtTemplateEntry" + "[cdtTemplateName='" + self.cdttemplatename.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/cdtTemplateTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cdttemplatename.is_set or self.cdttemplatename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdttemplatename.get_name_leafdata())
                if (self.cdttemplatesrc.is_set or self.cdttemplatesrc.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdttemplatesrc.get_name_leafdata())
                if (self.cdttemplatestatus.is_set or self.cdttemplatestatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdttemplatestatus.get_name_leafdata())
                if (self.cdttemplatestorage.is_set or self.cdttemplatestorage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdttemplatestorage.get_name_leafdata())
                if (self.cdttemplatetype.is_set or self.cdttemplatetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdttemplatetype.get_name_leafdata())
                if (self.cdttemplateusagecount.is_set or self.cdttemplateusagecount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdttemplateusagecount.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cdtTemplateName" or name == "cdtTemplateSrc" or name == "cdtTemplateStatus" or name == "cdtTemplateStorage" or name == "cdtTemplateType" or name == "cdtTemplateUsageCount"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cdtTemplateName"):
                    self.cdttemplatename = value
                    self.cdttemplatename.value_namespace = name_space
                    self.cdttemplatename.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtTemplateSrc"):
                    self.cdttemplatesrc = value
                    self.cdttemplatesrc.value_namespace = name_space
                    self.cdttemplatesrc.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtTemplateStatus"):
                    self.cdttemplatestatus = value
                    self.cdttemplatestatus.value_namespace = name_space
                    self.cdttemplatestatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtTemplateStorage"):
                    self.cdttemplatestorage = value
                    self.cdttemplatestorage.value_namespace = name_space
                    self.cdttemplatestorage.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtTemplateType"):
                    self.cdttemplatetype = value
                    self.cdttemplatetype.value_namespace = name_space
                    self.cdttemplatetype.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtTemplateUsageCount"):
                    self.cdttemplateusagecount = value
                    self.cdttemplateusagecount.value_namespace = name_space
                    self.cdttemplateusagecount.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cdttemplateentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cdttemplateentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cdtTemplateTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cdtTemplateEntry"):
                for c in self.cdttemplateentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoDynamicTemplateMib.Cdttemplatetable.Cdttemplateentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cdttemplateentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cdtTemplateEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cdttemplatetargettable(Entity):
        """
        This table contains a list of targets associated with
        one or more dynamic templates.
        
        .. attribute:: cdttemplatetargetentry
        
        	An entry describes a target associated with one or more dynamic templates.  The system automatically creates an entry when it associates a dynamic template to a target.  Likewise, the system automatically destroys an entry when a target no longer has any associated dynamic templates
        	**type**\: list of    :py:class:`Cdttemplatetargetentry <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdttemplatetargettable.Cdttemplatetargetentry>`
        
        

        """

        _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
        _revision = '2007-09-06'

        def __init__(self):
            super(CiscoDynamicTemplateMib.Cdttemplatetargettable, self).__init__()

            self.yang_name = "cdtTemplateTargetTable"
            self.yang_parent_name = "CISCO-DYNAMIC-TEMPLATE-MIB"

            self.cdttemplatetargetentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoDynamicTemplateMib.Cdttemplatetargettable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoDynamicTemplateMib.Cdttemplatetargettable, self).__setattr__(name, value)


        class Cdttemplatetargetentry(Entity):
            """
            An entry describes a target associated with one or more
            dynamic templates.
            
            The system automatically creates an entry when it associates a
            dynamic template to a target.  Likewise, the system
            automatically destroys an entry when a target no longer has any
            associated dynamic templates.
            
            .. attribute:: cdttemplatetargettype  <key>
            
            	This object indicates the type of target
            	**type**\:   :py:class:`Dynamictemplatetargettype <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_TC_MIB.Dynamictemplatetargettype>`
            
            .. attribute:: cdttemplatetargetid  <key>
            
            	This object uniquely identifies the target within the scope of its type
            	**type**\:  str
            
            	**length:** 1..20
            
            .. attribute:: cdttemplatetargetstatus
            
            	This object specifies the status of the dynamic template target.  The following columns must be valid before activating a subscriber access profile\:      \- cdtTemplateTargetStorage  However, these objects specify a default value.  Thus, it is possible to use create\-and\-go semantics without setting any additional columns.  An implementation must allow the EMS/NMS to modify any column when this column is 'active', including columns defined in tables that have a one\-to\-one or sparse dependent relationship on this table
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cdttemplatetargetstorage
            
            	This object specifies what happens to the dynamic template target upon restart
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
            _revision = '2007-09-06'

            def __init__(self):
                super(CiscoDynamicTemplateMib.Cdttemplatetargettable.Cdttemplatetargetentry, self).__init__()

                self.yang_name = "cdtTemplateTargetEntry"
                self.yang_parent_name = "cdtTemplateTargetTable"

                self.cdttemplatetargettype = YLeaf(YType.enumeration, "cdtTemplateTargetType")

                self.cdttemplatetargetid = YLeaf(YType.str, "cdtTemplateTargetId")

                self.cdttemplatetargetstatus = YLeaf(YType.enumeration, "cdtTemplateTargetStatus")

                self.cdttemplatetargetstorage = YLeaf(YType.enumeration, "cdtTemplateTargetStorage")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cdttemplatetargettype",
                                "cdttemplatetargetid",
                                "cdttemplatetargetstatus",
                                "cdttemplatetargetstorage") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoDynamicTemplateMib.Cdttemplatetargettable.Cdttemplatetargetentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoDynamicTemplateMib.Cdttemplatetargettable.Cdttemplatetargetentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cdttemplatetargettype.is_set or
                    self.cdttemplatetargetid.is_set or
                    self.cdttemplatetargetstatus.is_set or
                    self.cdttemplatetargetstorage.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cdttemplatetargettype.yfilter != YFilter.not_set or
                    self.cdttemplatetargetid.yfilter != YFilter.not_set or
                    self.cdttemplatetargetstatus.yfilter != YFilter.not_set or
                    self.cdttemplatetargetstorage.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cdtTemplateTargetEntry" + "[cdtTemplateTargetType='" + self.cdttemplatetargettype.get() + "']" + "[cdtTemplateTargetId='" + self.cdttemplatetargetid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/cdtTemplateTargetTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cdttemplatetargettype.is_set or self.cdttemplatetargettype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdttemplatetargettype.get_name_leafdata())
                if (self.cdttemplatetargetid.is_set or self.cdttemplatetargetid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdttemplatetargetid.get_name_leafdata())
                if (self.cdttemplatetargetstatus.is_set or self.cdttemplatetargetstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdttemplatetargetstatus.get_name_leafdata())
                if (self.cdttemplatetargetstorage.is_set or self.cdttemplatetargetstorage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdttemplatetargetstorage.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cdtTemplateTargetType" or name == "cdtTemplateTargetId" or name == "cdtTemplateTargetStatus" or name == "cdtTemplateTargetStorage"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cdtTemplateTargetType"):
                    self.cdttemplatetargettype = value
                    self.cdttemplatetargettype.value_namespace = name_space
                    self.cdttemplatetargettype.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtTemplateTargetId"):
                    self.cdttemplatetargetid = value
                    self.cdttemplatetargetid.value_namespace = name_space
                    self.cdttemplatetargetid.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtTemplateTargetStatus"):
                    self.cdttemplatetargetstatus = value
                    self.cdttemplatetargetstatus.value_namespace = name_space
                    self.cdttemplatetargetstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtTemplateTargetStorage"):
                    self.cdttemplatetargetstorage = value
                    self.cdttemplatetargetstorage.value_namespace = name_space
                    self.cdttemplatetargetstorage.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cdttemplatetargetentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cdttemplatetargetentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cdtTemplateTargetTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cdtTemplateTargetEntry"):
                for c in self.cdttemplatetargetentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoDynamicTemplateMib.Cdttemplatetargettable.Cdttemplatetargetentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cdttemplatetargetentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cdtTemplateTargetEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cdttemplateassociationtable(Entity):
        """
        This table contains a list of templates associated with each
        target.
        
        This table has an expansion dependent relationship on the
        cdtTemplateTargetTable, containing zero or more rows for each
        target.
        
        .. attribute:: cdttemplateassociationentry
        
        	An entry indicates an association of a dynamic template with a target.  The system automatically creates an entry when it associates a dynamic template to a target.  The system also creates an entry when it derives the configuration that it applies to a target.  The system automatically destroys an entry under the following circumstances\:  1)  The target indicated by the entry no longer exists.  2)  The association between the target and the dynamic template     no longer exists
        	**type**\: list of    :py:class:`Cdttemplateassociationentry <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdttemplateassociationtable.Cdttemplateassociationentry>`
        
        

        """

        _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
        _revision = '2007-09-06'

        def __init__(self):
            super(CiscoDynamicTemplateMib.Cdttemplateassociationtable, self).__init__()

            self.yang_name = "cdtTemplateAssociationTable"
            self.yang_parent_name = "CISCO-DYNAMIC-TEMPLATE-MIB"

            self.cdttemplateassociationentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoDynamicTemplateMib.Cdttemplateassociationtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoDynamicTemplateMib.Cdttemplateassociationtable, self).__setattr__(name, value)


        class Cdttemplateassociationentry(Entity):
            """
            An entry indicates an association of a dynamic template with a
            target.
            
            The system automatically creates an entry when it associates a
            dynamic template to a target.
            
            The system also creates an entry when it derives the
            configuration that it applies to a target.
            
            The system automatically destroys an entry under the following
            circumstances\:
            
            1)  The target indicated by the entry no longer exists.
            
            2)  The association between the target and the dynamic template
                no longer exists.
            
            .. attribute:: cdttemplatetargettype  <key>
            
            	
            	**type**\:   :py:class:`Dynamictemplatetargettype <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_TC_MIB.Dynamictemplatetargettype>`
            
            .. attribute:: cdttemplatetargetid  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..20
            
            	**refers to**\:  :py:class:`cdttemplatetargetid <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdttemplatetargettable.Cdttemplatetargetentry>`
            
            .. attribute:: cdttemplateassociationname  <key>
            
            	This object indicates the name of the template associated with the target
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cdttemplateassociationprecedence
            
            	This object indicates the relative precedence of the associated dynamic template.  Lower values have higher precedence than higher values
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
            _revision = '2007-09-06'

            def __init__(self):
                super(CiscoDynamicTemplateMib.Cdttemplateassociationtable.Cdttemplateassociationentry, self).__init__()

                self.yang_name = "cdtTemplateAssociationEntry"
                self.yang_parent_name = "cdtTemplateAssociationTable"

                self.cdttemplatetargettype = YLeaf(YType.enumeration, "cdtTemplateTargetType")

                self.cdttemplatetargetid = YLeaf(YType.str, "cdtTemplateTargetId")

                self.cdttemplateassociationname = YLeaf(YType.str, "cdtTemplateAssociationName")

                self.cdttemplateassociationprecedence = YLeaf(YType.uint32, "cdtTemplateAssociationPrecedence")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cdttemplatetargettype",
                                "cdttemplatetargetid",
                                "cdttemplateassociationname",
                                "cdttemplateassociationprecedence") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoDynamicTemplateMib.Cdttemplateassociationtable.Cdttemplateassociationentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoDynamicTemplateMib.Cdttemplateassociationtable.Cdttemplateassociationentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cdttemplatetargettype.is_set or
                    self.cdttemplatetargetid.is_set or
                    self.cdttemplateassociationname.is_set or
                    self.cdttemplateassociationprecedence.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cdttemplatetargettype.yfilter != YFilter.not_set or
                    self.cdttemplatetargetid.yfilter != YFilter.not_set or
                    self.cdttemplateassociationname.yfilter != YFilter.not_set or
                    self.cdttemplateassociationprecedence.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cdtTemplateAssociationEntry" + "[cdtTemplateTargetType='" + self.cdttemplatetargettype.get() + "']" + "[cdtTemplateTargetId='" + self.cdttemplatetargetid.get() + "']" + "[cdtTemplateAssociationName='" + self.cdttemplateassociationname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/cdtTemplateAssociationTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cdttemplatetargettype.is_set or self.cdttemplatetargettype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdttemplatetargettype.get_name_leafdata())
                if (self.cdttemplatetargetid.is_set or self.cdttemplatetargetid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdttemplatetargetid.get_name_leafdata())
                if (self.cdttemplateassociationname.is_set or self.cdttemplateassociationname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdttemplateassociationname.get_name_leafdata())
                if (self.cdttemplateassociationprecedence.is_set or self.cdttemplateassociationprecedence.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdttemplateassociationprecedence.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cdtTemplateTargetType" or name == "cdtTemplateTargetId" or name == "cdtTemplateAssociationName" or name == "cdtTemplateAssociationPrecedence"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cdtTemplateTargetType"):
                    self.cdttemplatetargettype = value
                    self.cdttemplatetargettype.value_namespace = name_space
                    self.cdttemplatetargettype.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtTemplateTargetId"):
                    self.cdttemplatetargetid = value
                    self.cdttemplatetargetid.value_namespace = name_space
                    self.cdttemplatetargetid.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtTemplateAssociationName"):
                    self.cdttemplateassociationname = value
                    self.cdttemplateassociationname.value_namespace = name_space
                    self.cdttemplateassociationname.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtTemplateAssociationPrecedence"):
                    self.cdttemplateassociationprecedence = value
                    self.cdttemplateassociationprecedence.value_namespace = name_space
                    self.cdttemplateassociationprecedence.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cdttemplateassociationentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cdttemplateassociationentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cdtTemplateAssociationTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cdtTemplateAssociationEntry"):
                for c in self.cdttemplateassociationentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoDynamicTemplateMib.Cdttemplateassociationtable.Cdttemplateassociationentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cdttemplateassociationentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cdtTemplateAssociationEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cdttemplateusagetable(Entity):
        """
        This table contains a list of targets using each dynamic
        template.
        
        This table has an expansion dependent relationship on the
        cdtTemplateTable, containing zero or more rows for each
        dynamic template.
        
        .. attribute:: cdttemplateusageentry
        
        	An entry indicates a target using the dynamic template.  The system automatically creates an entry when it associates a dynamic template to a target.  The system also creates an entry when it derives the configuration that it applies to a target.  The system automatically destroys an entry under the following circumstances\:  1)  The target indicated by the entry no longer exists.  2)  The association between the target and the dynamic template     no longer exists
        	**type**\: list of    :py:class:`Cdttemplateusageentry <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdttemplateusagetable.Cdttemplateusageentry>`
        
        

        """

        _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
        _revision = '2007-09-06'

        def __init__(self):
            super(CiscoDynamicTemplateMib.Cdttemplateusagetable, self).__init__()

            self.yang_name = "cdtTemplateUsageTable"
            self.yang_parent_name = "CISCO-DYNAMIC-TEMPLATE-MIB"

            self.cdttemplateusageentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoDynamicTemplateMib.Cdttemplateusagetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoDynamicTemplateMib.Cdttemplateusagetable, self).__setattr__(name, value)


        class Cdttemplateusageentry(Entity):
            """
            An entry indicates a target using the dynamic template.
            
            The system automatically creates an entry when it associates a
            dynamic template to a target.
            
            The system also creates an entry when it derives the
            configuration that it applies to a target.
            
            The system automatically destroys an entry under the following
            circumstances\:
            
            1)  The target indicated by the entry no longer exists.
            
            2)  The association between the target and the dynamic template
                no longer exists.
            
            .. attribute:: cdttemplatename  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..64
            
            	**refers to**\:  :py:class:`cdttemplatename <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdttemplatetable.Cdttemplateentry>`
            
            .. attribute:: cdttemplateusagetargettype  <key>
            
            	This object indicates the type of target using the dynamic template
            	**type**\:   :py:class:`Dynamictemplatetargettype <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_TC_MIB.Dynamictemplatetargettype>`
            
            .. attribute:: cdttemplateusagetargetid  <key>
            
            	This object indicates the name of the target using the dynamic template
            	**type**\:  str
            
            	**length:** 1..20
            
            

            """

            _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
            _revision = '2007-09-06'

            def __init__(self):
                super(CiscoDynamicTemplateMib.Cdttemplateusagetable.Cdttemplateusageentry, self).__init__()

                self.yang_name = "cdtTemplateUsageEntry"
                self.yang_parent_name = "cdtTemplateUsageTable"

                self.cdttemplatename = YLeaf(YType.str, "cdtTemplateName")

                self.cdttemplateusagetargettype = YLeaf(YType.enumeration, "cdtTemplateUsageTargetType")

                self.cdttemplateusagetargetid = YLeaf(YType.str, "cdtTemplateUsageTargetId")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cdttemplatename",
                                "cdttemplateusagetargettype",
                                "cdttemplateusagetargetid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoDynamicTemplateMib.Cdttemplateusagetable.Cdttemplateusageentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoDynamicTemplateMib.Cdttemplateusagetable.Cdttemplateusageentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cdttemplatename.is_set or
                    self.cdttemplateusagetargettype.is_set or
                    self.cdttemplateusagetargetid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cdttemplatename.yfilter != YFilter.not_set or
                    self.cdttemplateusagetargettype.yfilter != YFilter.not_set or
                    self.cdttemplateusagetargetid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cdtTemplateUsageEntry" + "[cdtTemplateName='" + self.cdttemplatename.get() + "']" + "[cdtTemplateUsageTargetType='" + self.cdttemplateusagetargettype.get() + "']" + "[cdtTemplateUsageTargetId='" + self.cdttemplateusagetargetid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/cdtTemplateUsageTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cdttemplatename.is_set or self.cdttemplatename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdttemplatename.get_name_leafdata())
                if (self.cdttemplateusagetargettype.is_set or self.cdttemplateusagetargettype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdttemplateusagetargettype.get_name_leafdata())
                if (self.cdttemplateusagetargetid.is_set or self.cdttemplateusagetargetid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdttemplateusagetargetid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cdtTemplateName" or name == "cdtTemplateUsageTargetType" or name == "cdtTemplateUsageTargetId"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cdtTemplateName"):
                    self.cdttemplatename = value
                    self.cdttemplatename.value_namespace = name_space
                    self.cdttemplatename.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtTemplateUsageTargetType"):
                    self.cdttemplateusagetargettype = value
                    self.cdttemplateusagetargettype.value_namespace = name_space
                    self.cdttemplateusagetargettype.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtTemplateUsageTargetId"):
                    self.cdttemplateusagetargetid = value
                    self.cdttemplateusagetargetid.value_namespace = name_space
                    self.cdttemplateusagetargetid.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cdttemplateusageentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cdttemplateusageentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cdtTemplateUsageTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cdtTemplateUsageEntry"):
                for c in self.cdttemplateusageentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoDynamicTemplateMib.Cdttemplateusagetable.Cdttemplateusageentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cdttemplateusageentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cdtTemplateUsageEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cdttemplatecommontable(Entity):
        """
        This table contains attributes relating to all dynamic
        templates.  Observe that the type of dynamic templates
        containing these attributes may change with the addition of new
        dynamic template types.
        
        This table has a sparse\-dependent relationship on the
        cdtTemplateTable, containing a row for each dynamic template
        having a cdtTemplateType of one of the following values\:
        
            'derived'
            'ppp'
            'ethernet'
            'ipSubscriber'
            'service'
        
        .. attribute:: cdttemplatecommonentry
        
        	An entry containing attributes relating to any target.  The system automatically creates an entry when the system or the EMS/NMS creates a row in the cdtTemplateTable with a cdtTemplateType of on the following values\:      'derived'     'ppp'     'ethernet'     'ipSubscriber'     'service'  Likewise, the system automatically destroys an entry when the system or the EMS/NMS destroys the corresponding row in the cdtTemplateTable
        	**type**\: list of    :py:class:`Cdttemplatecommonentry <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdttemplatecommontable.Cdttemplatecommonentry>`
        
        

        """

        _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
        _revision = '2007-09-06'

        def __init__(self):
            super(CiscoDynamicTemplateMib.Cdttemplatecommontable, self).__init__()

            self.yang_name = "cdtTemplateCommonTable"
            self.yang_parent_name = "CISCO-DYNAMIC-TEMPLATE-MIB"

            self.cdttemplatecommonentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoDynamicTemplateMib.Cdttemplatecommontable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoDynamicTemplateMib.Cdttemplatecommontable, self).__setattr__(name, value)


        class Cdttemplatecommonentry(Entity):
            """
            An entry containing attributes relating to any target.
            
            The system automatically creates an entry when the system or the
            EMS/NMS creates a row in the cdtTemplateTable with a
            cdtTemplateType of on the following values\:
            
                'derived'
                'ppp'
                'ethernet'
                'ipSubscriber'
                'service'
            
            Likewise, the system automatically destroys an entry when the
            system or the EMS/NMS destroys the corresponding row in the
            cdtTemplateTable.
            
            .. attribute:: cdttemplatename  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..64
            
            	**refers to**\:  :py:class:`cdttemplatename <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdttemplatetable.Cdttemplateentry>`
            
            .. attribute:: cdtcommonaddrpool
            
            	This object specifies the name of the IP address pool the system will use to assign an IP address to a peer of a target.  This column is valid only if the 'addrPool' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cdtcommondescr
            
            	This object specifies a human\-readable description for the dynamic template.  This column is valid only if the 'descr' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cdtcommonipv4accessgroup
            
            	This object specifies the name (or number) of the IPv4 ACL applied to a target.  This column is valid only if the 'ipv4AccessGroup' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cdtcommonipv4unreachables
            
            	This object specifies whether a target generates ICMPv4 unreachable messages.  This column is valid only if the 'ipv4Unreachables' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\:  bool
            
            .. attribute:: cdtcommonipv6accessgroup
            
            	This object specifies the name (or number) of the IPv4 ACL applied to a target.  This column is valid only if the 'ipv6AccessGroup' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cdtcommonipv6unreachables
            
            	This object specifies whether a target generates ICMPv6 unreachable messages.  This column is valid only if the 'ipv6Unreachables' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\:  bool
            
            .. attribute:: cdtcommonkeepaliveint
            
            	This object specifies the interval that the system sends keepalive messages to a target.  This column is valid only if the 'keepaliveInterval' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cdtcommonkeepaliveretries
            
            	This object specifies the number of times the system will resend a keepalive message without a response before it transitions a target to an operationally down state.  This column is valid only if the 'keepaliveRetries' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\:  int
            
            	**range:** 1..255
            
            	**units**\: retries
            
            .. attribute:: cdtcommonsrvacct
            
            	This object specifies the name of the traffic accounting policy applied to a target.  The system should assume that the cbpPolicyMapType (defined by the CISCO\-CBP\-BASE\-CFG\-MIB) of the policy is cbpPmtTrafficAccounting (defined by the CISCO\-CBP\-TYPE\-OID\-MIB).  This column is valid only if the 'srvAcct' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\:  str
            
            .. attribute:: cdtcommonsrvnetflow
            
            	This object specifies the name of the NetFlow policy applied to a target.  The system should assume that the cbpPolicyMapType (defined by the CISCO\-CBP\-BASE\-CFG\-MIB) of the policy is cbpPmtNetflow (defined by the CISCO\-CBP\-TYPE\-OID\-MIB).  This column is valid only if the 'srvNetflow' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\:  str
            
            .. attribute:: cdtcommonsrvqos
            
            	This object specifies the name of the traffic QoS policy applied to a target.  The system should assume that the cbpPolicyMapType (defined by the CISCO\-CBP\-BASE\-CFG\-MIB) of the policy is cbpPmtQos (defined by the CISCO\-CBP\-TYPE\-OID\-MIB).  This column is valid only if the 'srvQos' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\:  str
            
            .. attribute:: cdtcommonsrvredirect
            
            	This object specifies the name of the traffic redirect policy applied to a target.  The system should assume that the cbpPolicyMapType (defined by the CISCO\-CBP\-BASE\-CFG\-MIB) of the policy is cbpPmtTrafficRedirect (defined by the CISCO\-CBP\-TYPE\-OID\-MIB).  This column is valid only if the 'srvRedirect' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\:  str
            
            .. attribute:: cdtcommonsrvsubcontrol
            
            	This object specifies the name of the subscriber control policy applied to a target.  The system should assume that the cbpPolicyMapType (defined by the CISCO\-CBP\-BASE\-CFG\-MIB) of the policy is cbpPmtControlSubscriber (defined by the CISCO\-CBP\-TYPE\-OID\-MIB).  This column is valid only if the 'srvSubControl' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\:  str
            
            .. attribute:: cdtcommonvalid
            
            	This object specifies which attributes in the dynamic template have been configured to valid values.  Each bit in this bit string corresponds to a column in this table.  If the bit is '0', then the value of the corresponding column is not valid.  If the bit is '1', then the value of the corresponding column has been configured to a valid value.  The following list specifies the mappings between bits and the columns\:      'descr'             => cdtCommonDescr     'keepaliveInt'      => cdtCommonKeepaliveInt     'keepaliveRetries'  => cdtCommonKeepaliveRetries     'vrf'               => cdtCommonVrf     'addrPool'          => cdtCommonAddrPool     'ipv4AccessGroup'   => cdtCommonIpv4AccessGroup     'ipv4Unreachables'  => cdtCommonIpv4Unreachables     'ipv6AccessGroup'   => cdtCommonIpv6AccessGroup     'ipv6Unreachables'  => cdtCommonIpv6Unreachables     'srvSubControl'     => cdtCommonSrvSubControl     'srvRedirect'       => cdtCommonSrvRedirect     'srvAcct'           => cdtCommonSrvAcct     'srvQos'            => cdtCommonSrvQos     'srvNetflow'        => cdtCommonSrvNetflow
            	**type**\:   :py:class:`Cdtcommonvalid <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdttemplatecommontable.Cdttemplatecommonentry.Cdtcommonvalid>`
            
            .. attribute:: cdtcommonvrf
            
            	This object specifies the name of the VRF with which a target has an association.  This column is valid only if the 'vrf' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\:  str
            
            	**length:** 0..32
            
            

            """

            _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
            _revision = '2007-09-06'

            def __init__(self):
                super(CiscoDynamicTemplateMib.Cdttemplatecommontable.Cdttemplatecommonentry, self).__init__()

                self.yang_name = "cdtTemplateCommonEntry"
                self.yang_parent_name = "cdtTemplateCommonTable"

                self.cdttemplatename = YLeaf(YType.str, "cdtTemplateName")

                self.cdtcommonaddrpool = YLeaf(YType.str, "cdtCommonAddrPool")

                self.cdtcommondescr = YLeaf(YType.str, "cdtCommonDescr")

                self.cdtcommonipv4accessgroup = YLeaf(YType.str, "cdtCommonIpv4AccessGroup")

                self.cdtcommonipv4unreachables = YLeaf(YType.boolean, "cdtCommonIpv4Unreachables")

                self.cdtcommonipv6accessgroup = YLeaf(YType.str, "cdtCommonIpv6AccessGroup")

                self.cdtcommonipv6unreachables = YLeaf(YType.boolean, "cdtCommonIpv6Unreachables")

                self.cdtcommonkeepaliveint = YLeaf(YType.uint32, "cdtCommonKeepaliveInt")

                self.cdtcommonkeepaliveretries = YLeaf(YType.uint32, "cdtCommonKeepaliveRetries")

                self.cdtcommonsrvacct = YLeaf(YType.str, "cdtCommonSrvAcct")

                self.cdtcommonsrvnetflow = YLeaf(YType.str, "cdtCommonSrvNetflow")

                self.cdtcommonsrvqos = YLeaf(YType.str, "cdtCommonSrvQos")

                self.cdtcommonsrvredirect = YLeaf(YType.str, "cdtCommonSrvRedirect")

                self.cdtcommonsrvsubcontrol = YLeaf(YType.str, "cdtCommonSrvSubControl")

                self.cdtcommonvalid = YLeaf(YType.bits, "cdtCommonValid")

                self.cdtcommonvrf = YLeaf(YType.str, "cdtCommonVrf")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cdttemplatename",
                                "cdtcommonaddrpool",
                                "cdtcommondescr",
                                "cdtcommonipv4accessgroup",
                                "cdtcommonipv4unreachables",
                                "cdtcommonipv6accessgroup",
                                "cdtcommonipv6unreachables",
                                "cdtcommonkeepaliveint",
                                "cdtcommonkeepaliveretries",
                                "cdtcommonsrvacct",
                                "cdtcommonsrvnetflow",
                                "cdtcommonsrvqos",
                                "cdtcommonsrvredirect",
                                "cdtcommonsrvsubcontrol",
                                "cdtcommonvalid",
                                "cdtcommonvrf") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoDynamicTemplateMib.Cdttemplatecommontable.Cdttemplatecommonentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoDynamicTemplateMib.Cdttemplatecommontable.Cdttemplatecommonentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cdttemplatename.is_set or
                    self.cdtcommonaddrpool.is_set or
                    self.cdtcommondescr.is_set or
                    self.cdtcommonipv4accessgroup.is_set or
                    self.cdtcommonipv4unreachables.is_set or
                    self.cdtcommonipv6accessgroup.is_set or
                    self.cdtcommonipv6unreachables.is_set or
                    self.cdtcommonkeepaliveint.is_set or
                    self.cdtcommonkeepaliveretries.is_set or
                    self.cdtcommonsrvacct.is_set or
                    self.cdtcommonsrvnetflow.is_set or
                    self.cdtcommonsrvqos.is_set or
                    self.cdtcommonsrvredirect.is_set or
                    self.cdtcommonsrvsubcontrol.is_set or
                    self.cdtcommonvalid.is_set or
                    self.cdtcommonvrf.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cdttemplatename.yfilter != YFilter.not_set or
                    self.cdtcommonaddrpool.yfilter != YFilter.not_set or
                    self.cdtcommondescr.yfilter != YFilter.not_set or
                    self.cdtcommonipv4accessgroup.yfilter != YFilter.not_set or
                    self.cdtcommonipv4unreachables.yfilter != YFilter.not_set or
                    self.cdtcommonipv6accessgroup.yfilter != YFilter.not_set or
                    self.cdtcommonipv6unreachables.yfilter != YFilter.not_set or
                    self.cdtcommonkeepaliveint.yfilter != YFilter.not_set or
                    self.cdtcommonkeepaliveretries.yfilter != YFilter.not_set or
                    self.cdtcommonsrvacct.yfilter != YFilter.not_set or
                    self.cdtcommonsrvnetflow.yfilter != YFilter.not_set or
                    self.cdtcommonsrvqos.yfilter != YFilter.not_set or
                    self.cdtcommonsrvredirect.yfilter != YFilter.not_set or
                    self.cdtcommonsrvsubcontrol.yfilter != YFilter.not_set or
                    self.cdtcommonvalid.yfilter != YFilter.not_set or
                    self.cdtcommonvrf.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cdtTemplateCommonEntry" + "[cdtTemplateName='" + self.cdttemplatename.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/cdtTemplateCommonTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cdttemplatename.is_set or self.cdttemplatename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdttemplatename.get_name_leafdata())
                if (self.cdtcommonaddrpool.is_set or self.cdtcommonaddrpool.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtcommonaddrpool.get_name_leafdata())
                if (self.cdtcommondescr.is_set or self.cdtcommondescr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtcommondescr.get_name_leafdata())
                if (self.cdtcommonipv4accessgroup.is_set or self.cdtcommonipv4accessgroup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtcommonipv4accessgroup.get_name_leafdata())
                if (self.cdtcommonipv4unreachables.is_set or self.cdtcommonipv4unreachables.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtcommonipv4unreachables.get_name_leafdata())
                if (self.cdtcommonipv6accessgroup.is_set or self.cdtcommonipv6accessgroup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtcommonipv6accessgroup.get_name_leafdata())
                if (self.cdtcommonipv6unreachables.is_set or self.cdtcommonipv6unreachables.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtcommonipv6unreachables.get_name_leafdata())
                if (self.cdtcommonkeepaliveint.is_set or self.cdtcommonkeepaliveint.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtcommonkeepaliveint.get_name_leafdata())
                if (self.cdtcommonkeepaliveretries.is_set or self.cdtcommonkeepaliveretries.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtcommonkeepaliveretries.get_name_leafdata())
                if (self.cdtcommonsrvacct.is_set or self.cdtcommonsrvacct.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtcommonsrvacct.get_name_leafdata())
                if (self.cdtcommonsrvnetflow.is_set or self.cdtcommonsrvnetflow.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtcommonsrvnetflow.get_name_leafdata())
                if (self.cdtcommonsrvqos.is_set or self.cdtcommonsrvqos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtcommonsrvqos.get_name_leafdata())
                if (self.cdtcommonsrvredirect.is_set or self.cdtcommonsrvredirect.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtcommonsrvredirect.get_name_leafdata())
                if (self.cdtcommonsrvsubcontrol.is_set or self.cdtcommonsrvsubcontrol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtcommonsrvsubcontrol.get_name_leafdata())
                if (self.cdtcommonvalid.is_set or self.cdtcommonvalid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtcommonvalid.get_name_leafdata())
                if (self.cdtcommonvrf.is_set or self.cdtcommonvrf.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtcommonvrf.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cdtTemplateName" or name == "cdtCommonAddrPool" or name == "cdtCommonDescr" or name == "cdtCommonIpv4AccessGroup" or name == "cdtCommonIpv4Unreachables" or name == "cdtCommonIpv6AccessGroup" or name == "cdtCommonIpv6Unreachables" or name == "cdtCommonKeepaliveInt" or name == "cdtCommonKeepaliveRetries" or name == "cdtCommonSrvAcct" or name == "cdtCommonSrvNetflow" or name == "cdtCommonSrvQos" or name == "cdtCommonSrvRedirect" or name == "cdtCommonSrvSubControl" or name == "cdtCommonValid" or name == "cdtCommonVrf"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cdtTemplateName"):
                    self.cdttemplatename = value
                    self.cdttemplatename.value_namespace = name_space
                    self.cdttemplatename.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtCommonAddrPool"):
                    self.cdtcommonaddrpool = value
                    self.cdtcommonaddrpool.value_namespace = name_space
                    self.cdtcommonaddrpool.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtCommonDescr"):
                    self.cdtcommondescr = value
                    self.cdtcommondescr.value_namespace = name_space
                    self.cdtcommondescr.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtCommonIpv4AccessGroup"):
                    self.cdtcommonipv4accessgroup = value
                    self.cdtcommonipv4accessgroup.value_namespace = name_space
                    self.cdtcommonipv4accessgroup.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtCommonIpv4Unreachables"):
                    self.cdtcommonipv4unreachables = value
                    self.cdtcommonipv4unreachables.value_namespace = name_space
                    self.cdtcommonipv4unreachables.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtCommonIpv6AccessGroup"):
                    self.cdtcommonipv6accessgroup = value
                    self.cdtcommonipv6accessgroup.value_namespace = name_space
                    self.cdtcommonipv6accessgroup.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtCommonIpv6Unreachables"):
                    self.cdtcommonipv6unreachables = value
                    self.cdtcommonipv6unreachables.value_namespace = name_space
                    self.cdtcommonipv6unreachables.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtCommonKeepaliveInt"):
                    self.cdtcommonkeepaliveint = value
                    self.cdtcommonkeepaliveint.value_namespace = name_space
                    self.cdtcommonkeepaliveint.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtCommonKeepaliveRetries"):
                    self.cdtcommonkeepaliveretries = value
                    self.cdtcommonkeepaliveretries.value_namespace = name_space
                    self.cdtcommonkeepaliveretries.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtCommonSrvAcct"):
                    self.cdtcommonsrvacct = value
                    self.cdtcommonsrvacct.value_namespace = name_space
                    self.cdtcommonsrvacct.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtCommonSrvNetflow"):
                    self.cdtcommonsrvnetflow = value
                    self.cdtcommonsrvnetflow.value_namespace = name_space
                    self.cdtcommonsrvnetflow.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtCommonSrvQos"):
                    self.cdtcommonsrvqos = value
                    self.cdtcommonsrvqos.value_namespace = name_space
                    self.cdtcommonsrvqos.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtCommonSrvRedirect"):
                    self.cdtcommonsrvredirect = value
                    self.cdtcommonsrvredirect.value_namespace = name_space
                    self.cdtcommonsrvredirect.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtCommonSrvSubControl"):
                    self.cdtcommonsrvsubcontrol = value
                    self.cdtcommonsrvsubcontrol.value_namespace = name_space
                    self.cdtcommonsrvsubcontrol.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtCommonValid"):
                    self.cdtcommonvalid[value] = True
                if(value_path == "cdtCommonVrf"):
                    self.cdtcommonvrf = value
                    self.cdtcommonvrf.value_namespace = name_space
                    self.cdtcommonvrf.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cdttemplatecommonentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cdttemplatecommonentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cdtTemplateCommonTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cdtTemplateCommonEntry"):
                for c in self.cdttemplatecommonentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoDynamicTemplateMib.Cdttemplatecommontable.Cdttemplatecommonentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cdttemplatecommonentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cdtTemplateCommonEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cdtiftemplatetable(Entity):
        """
        This table contains attributes relating to interface
        configuration.
        
        This table has a sparse\-dependent relationship on the
        cdtTemplateTable, containing a row for each dynamic template
        having a cdtTemplateType of one of the following values\:
        
            'derived'
            'ppp'
            'ethernet'
            'ipSubscriber'
        
        .. attribute:: cdtiftemplateentry
        
        	An entry containing attributes relating to interface configuration.  The system automatically creates an entry when the system or the EMS/NMS creates a row in the cdtTemplateTable with a cdtTemplateType of one of the following values\:      'derived'     'ppp'     'ethernet'     'ipSubscriber'  Likewise, the system automatically destroys an entry when the system or the EMS/NMS destroys the corresponding row in the cdtTemplateTable
        	**type**\: list of    :py:class:`Cdtiftemplateentry <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry>`
        
        

        """

        _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
        _revision = '2007-09-06'

        def __init__(self):
            super(CiscoDynamicTemplateMib.Cdtiftemplatetable, self).__init__()

            self.yang_name = "cdtIfTemplateTable"
            self.yang_parent_name = "CISCO-DYNAMIC-TEMPLATE-MIB"

            self.cdtiftemplateentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoDynamicTemplateMib.Cdtiftemplatetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoDynamicTemplateMib.Cdtiftemplatetable, self).__setattr__(name, value)


        class Cdtiftemplateentry(Entity):
            """
            An entry containing attributes relating to interface
            configuration.
            
            The system automatically creates an entry when the system or the
            EMS/NMS creates a row in the cdtTemplateTable with a
            cdtTemplateType of one of the following values\:
            
                'derived'
                'ppp'
                'ethernet'
                'ipSubscriber'
            
            Likewise, the system automatically destroys an entry when the
            system or the EMS/NMS destroys the corresponding row in the
            cdtTemplateTable.
            
            .. attribute:: cdttemplatename  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..64
            
            	**refers to**\:  :py:class:`cdttemplatename <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdttemplatetable.Cdttemplateentry>`
            
            .. attribute:: cdtifcdpenable
            
            	This object specifies whether the target interface participates in the Cisco Discovery Protocol (CDP).  This column is valid only if the 'cdpEnable' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  bool
            
            .. attribute:: cdtifflowmonitor
            
            	This object specifies the name of the flow monitor associated with the target interface.  This column is valid only if the 'flowMonitor' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cdtifipv4mtu
            
            	This object specifies the Maximum Transfer Unit (MTU) size for IPv4 packets sent on the target interface.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid.  This column is valid only if the 'ipv4Mtu' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  int
            
            	**range:** 0..None \| 128..65535
            
            	**units**\: octets
            
            .. attribute:: cdtifipv4subenable
            
            	This object specifies whether the target interface allows IPv4 subscriber sessions.  This column is valid only if the 'ipv4SubEnable' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  bool
            
            .. attribute:: cdtifipv4tcpmssadjust
            
            	This object specifies the adjustment to the Maximum Segment Size (MSS) of TCP SYN packets received by the target interface contained in IPv4 datagrams.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid.  This column is valid only if the 'ipv4TcpMssAdjust' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  int
            
            	**range:** 0..None \| 500..1460
            
            	**units**\: octets
            
            .. attribute:: cdtifipv4unnumbered
            
            	This object specifies the interface of the source address that the target interface uses when originating IPv4 packets.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid (e.g., immediately following the creation of an instance of the object).  This column is valid only if the 'ipv4Unnumbered' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cdtifipv4verifyunirpf
            
            	This object specifies whether the type of unicast RPF the system performs on IPv4 packets received by the target interface.  This column is valid only if the 'ipv4VerifyUniRpf' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:   :py:class:`Unicastrpftype <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.Unicastrpftype>`
            
            .. attribute:: cdtifipv4verifyunirpfacl
            
            	This object specifies the name (or number) of the IPv4 ACL used to determine whether the system should permit/deny packets received by the target interface that fail unicast RPF verification.  This column is valid only if the 'ipv4VerifyUniRpfAcl' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cdtifipv4verifyunirpfopts
            
            	This object specifies the options that affect how the system performs unicast RPF on IPv4 packets received by the target interface.  This column is valid only if the 'ipv4VerifyUniRpfOpts' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:   :py:class:`Unicastrpfoptions <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.Unicastrpfoptions>`
            
            .. attribute:: cdtifipv6enable
            
            	This object specifies whether the system processes IPv6 packets received by the target interface.  This column is valid only if the 'ipv6Enable' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  bool
            
            .. attribute:: cdtifipv6nddadattempts
            
            	This object specifies the number of consecutive neighbor solitication messages the system sends on the target interface while performing duplicate address detection on unicast IPv6 addresses on the target interface.  The value '0' disables duplicate address detection on the target interface.  This column is valid only if the 'ipv6NdDadAttempts' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  int
            
            	**range:** 0..600
            
            .. attribute:: cdtifipv6ndnsinterval
            
            	This object specifies the interval between neighbor solicitation retransmissions on the target interface.  This column is valid only if the 'ipv6NdNsIntervals' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  int
            
            	**range:** 1000..3600000
            
            	**units**\: milliseconds
            
            .. attribute:: cdtifipv6ndopts
            
            	This object specifies options that affect advertisements sent on the target interface\:      'advertise'         This option specifies that the system should advertise         the IPv6 prefix (i.e., the corresponding instance of         cdtIfIpv6NdPrefix).      'onlink'         This option specifies that the IPv6 prefix has been         assigned to a link.  If set to '0', the system         advertises the IPv6 prefix as 'offlink'.      'router'         This option indicates that the router will send the full         router address and not set the 'R' bit in prefix         advertisements.      'autoConfig'         This option indicates to hosts on the local link that         the specified prefix supports IPv6 auto\-configuration.      'advertisementInterval'         This option specifies the advertisement interval option         in router advertisements sent on the target interface.      'managedConfigFlag'         This option causes the system to set the 'managed         address configuration flag' in router advertisements         sent on the target interface.      'otherConfigFlag'         This option causes the system to set the 'other stateful         configuration' flag in router advertisements sent on the         target interface.      'frameIpv6Prefix'         This option causes the system to add the prefix in a         received RADIUS framed IPv6 prefix attribute to the         target interface's neighbor discovery prefix queue and         includes it in router advertisements sent on the target         interface.      'raSupress'         This option suppresses the transmission of router         advertisements on the target interface.  This column is valid only if the 'ipv6NdOpts' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:   :py:class:`Cdtifipv6Ndopts <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry.Cdtifipv6Ndopts>`
            
            .. attribute:: cdtifipv6ndpreferredlife
            
            	This object specifies the interval that the system advertises the IPv6 prefix (i.e., the corresponding instance of cdtIfIpv6NdPrefix) as 'preferred' for IPv6 router advertisements sent on the target interface.  This column is valid only if the 'ipv6NdPreferredLife' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cdtifipv6ndprefix
            
            	This object specifies the IPv6 network number included in IPv6 router advertisements sent on the target interface.  This column is valid only if the 'ipv6NdPrefix' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  str
            
            .. attribute:: cdtifipv6ndprefixlength
            
            	This object specifies the length of the IPv6 prefix specified by the corresponding instance of cdtIpv6NdPrefix.  This column is valid only if the 'ipv6NdPrefix' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  int
            
            	**range:** 0..2040
            
            .. attribute:: cdtifipv6ndraintervalmax
            
            	This object specifies the maximum interval between IPv6 router advertisements sent on the target interface.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid.  This column is valid only if the 'ipv6NdRaInterval' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cdtifipv6ndraintervalmin
            
            	This object specifies the minimum interval between IPv6 router advertisements sent on the target interface.  The value of this column has the following restrictions\:  1)  This value cannot be less than 75% of the value specified     for cdtIfIpv6NdRaIntervalMax.  2)  If the corresponding instance of cdtIfIpv6NdRaIntervalUnits     is 'seconds', then this value cannot be less than '3'.  3)  If the corresponding instance of cdtIfIpv6NdRaIntervalUnits     is 'milliseconds', then this value cannot be less than '30'.  If the target interface template does not specify this value, then the system automatically assumes a minimum interval that is 75% of the corresponding instance of cdtIfIpv6NdRaIntervalMax.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid.  This column is valid only if the 'ipv6NdRaInterval' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cdtifipv6ndraintervalunits
            
            	This object specifies the units of time for the corresponding instances of cdtIfIpv6NdRaIntervalMin and cdtIfIpv6NdRaIntervalMax.  This column is valid only if the 'ipv6NdRaInterval' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:   :py:class:`Cdtifipv6Ndraintervalunits <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry.Cdtifipv6Ndraintervalunits>`
            
            .. attribute:: cdtifipv6ndralife
            
            	This object specifies the router lifetime value in IPv6 router advertisements sent on the target interface.  The value '0' specifies that neighbors should not consider the router as a default router
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cdtifipv6ndreachabletime
            
            	This object specifies the amount of time the system considers a neighbor of the target interface reachable after a reachability confirmation event has occurred.  The value '0' disables neighbor reachability detection on the target interface.  This column is valid only if the 'ipv6NdReachable' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cdtifipv6ndrouterpreference
            
            	This object specifies the Default Router Preference (DRP) for the router on the target interface.  This column is valid only if the 'ipv6NdRouterPreference' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:   :py:class:`Cdtifipv6Ndrouterpreference <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry.Cdtifipv6Ndrouterpreference>`
            
            .. attribute:: cdtifipv6ndvalidlife
            
            	This object specifies the interval that the system advertises the IPv6 prefix (i.e., the corresponding instance of cdtIfIpv6NdPrefix) as 'valid' for IPv6 router advertisements sent on the target interface.  This column is valid only if the 'ipv6NdValidLife' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cdtifipv6subenable
            
            	This object specifies whether the target interface allows IPv6 subscriber sessions.  This column is valid only if the 'ipv6SubEnable' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  bool
            
            .. attribute:: cdtifipv6tcpmssadjust
            
            	This object specifies the adjustment to the Maximum Segment Size (MSS) of TCP SYN packets received by the target interface contained in IPv6 datagrams.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid.  This column is valid only if the 'ipv6TcpMssAdjust' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  int
            
            	**range:** 0..None \| 500..1460
            
            	**units**\: octets
            
            .. attribute:: cdtifipv6verifyunirpf
            
            	This object specifies whether the type of unicast RPF the system performs on IPv6 packets received by the target interface.  This column is valid only if the 'ipv6VerifyUniRpf' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:   :py:class:`Unicastrpftype <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.Unicastrpftype>`
            
            .. attribute:: cdtifipv6verifyunirpfacl
            
            	This object specifies the name (or number) of the IPv6 ACL used to determine whether the system should permit/deny packets received by the target interface that fail unicast RPF verification.  This column is valid only if the 'ipv6VerifyUniRpfAcl' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cdtifipv6verifyunirpfopts
            
            	This object specifies the options that affect how the system performs unicast RPF on IPv6 packets received by the target interface.  This column is valid only if the 'ipv6VerifyUniRpfOpts' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:   :py:class:`Unicastrpfoptions <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.Unicastrpfoptions>`
            
            .. attribute:: cdtifmtu
            
            	This object specifies the Maximum Transfer Unit (MTU) size for all packets sent on the target interface.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid.  This column is valid only if the 'mtu' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  int
            
            	**range:** 0..None \| 64..65535
            
            	**units**\: octets
            
            .. attribute:: cdtifvalid
            
            	This object specifies which attributes in the dynamic template have been configured to valid values.  Each bit in this bit string corresponds to a column in this table.  If the bit is '0', then the value of the corresponding column is not valid.  If the bit is '1', then the value of the corresponding column has been configured to a valid value.  The following list specifies the mappings between bits and the columns\:      'mtu'                     => cdtIfMtu     'cdpEnable'               => cdtIfCdpEnable     'flowMonitor'             => cdtIfFlowMonitor     'ipv4Unnumbered'          => cdtIfIpv4Unnumbered     'ipv4SubEnable'           => cdtIfIpv4SubEnable     'ipv4Mtu'                 => cdtIfIpv4Mtu     'ipv4TcpMssAdjust'        => cdtIfIpv4TcpMssAdjust     'ipv4VerifyUniRpf'        => cdtIfIpv4VerifyUniRpf     'ipv4VerifyUniRpfAcl'     => cdtIfIpv4VerifyUniRpfAcl     'ipv4VerifyUniRpfOpts'    => cdtIfIpv4VerifyUniRpfOpts     'ipv6Enable'              => cdtIfIpv6Enable     'ipv6SubEnable'           => cdtIfIpv6SubEnable     'ipv6TcpMssAdjust'        => cdtIfIpv6TcpMssAdjust     'ipv6VerifyUniRpf'        => cdtIfIpv6VerifyUniRpf     'ipv6VerifyUniRpfAcl'     => cdtIfIpv6VerifyUniRpfAcl     'ipv6VerifyUniRpfOpts'    => cdtIfIpv6VerifyUniRpfOpts     'ipv6NdPrefix'            => cdtIfIpv6NdPrefix,                                  cdtIfIpv6NdPrefixLength     'ipv6NdValidLife'         => cdtIfIpv6NdValidLife     'ipv6NdPreferredLife'     => cdtIfIpv6NdPreferredLife     'ipv6NdOpts'              => cdtIfIpv6NdOpts     'ipv6NdDadAttempts'       => cdtIfIpv6NdDadAttempts     'ipv6NdNsInterval'        => cdtIfIpv6NdNsInterval     'ipv6NdReacableTime'      => cdtIfIpv6NdReacableTime     'ipv6NdRaIntervalMax'     => cdtIfIpv6NdRaIntervalUnits,                                  cdtIfIpv6NdRaIntervalMax     'ipv6NdRaIntervalMin'     => cdtIfIpv6NdRaIntervalMin     'ipv6NdRaLife'            => cdtIfIpv6NdRaLife     'ipv6NdRouterPreference'' => cdtIfIpv6NdRouterPreference
            	**type**\:   :py:class:`Cdtifvalid <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry.Cdtifvalid>`
            
            

            """

            _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
            _revision = '2007-09-06'

            def __init__(self):
                super(CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry, self).__init__()

                self.yang_name = "cdtIfTemplateEntry"
                self.yang_parent_name = "cdtIfTemplateTable"

                self.cdttemplatename = YLeaf(YType.str, "cdtTemplateName")

                self.cdtifcdpenable = YLeaf(YType.boolean, "cdtIfCdpEnable")

                self.cdtifflowmonitor = YLeaf(YType.str, "cdtIfFlowMonitor")

                self.cdtifipv4mtu = YLeaf(YType.uint32, "cdtIfIpv4Mtu")

                self.cdtifipv4subenable = YLeaf(YType.boolean, "cdtIfIpv4SubEnable")

                self.cdtifipv4tcpmssadjust = YLeaf(YType.uint32, "cdtIfIpv4TcpMssAdjust")

                self.cdtifipv4unnumbered = YLeaf(YType.int32, "cdtIfIpv4Unnumbered")

                self.cdtifipv4verifyunirpf = YLeaf(YType.enumeration, "cdtIfIpv4VerifyUniRpf")

                self.cdtifipv4verifyunirpfacl = YLeaf(YType.str, "cdtIfIpv4VerifyUniRpfAcl")

                self.cdtifipv4verifyunirpfopts = YLeaf(YType.bits, "cdtIfIpv4VerifyUniRpfOpts")

                self.cdtifipv6enable = YLeaf(YType.boolean, "cdtIfIpv6Enable")

                self.cdtifipv6nddadattempts = YLeaf(YType.uint32, "cdtIfIpv6NdDadAttempts")

                self.cdtifipv6ndnsinterval = YLeaf(YType.uint32, "cdtIfIpv6NdNsInterval")

                self.cdtifipv6ndopts = YLeaf(YType.bits, "cdtIfIpv6NdOpts")

                self.cdtifipv6ndpreferredlife = YLeaf(YType.uint32, "cdtIfIpv6NdPreferredLife")

                self.cdtifipv6ndprefix = YLeaf(YType.str, "cdtIfIpv6NdPrefix")

                self.cdtifipv6ndprefixlength = YLeaf(YType.uint32, "cdtIfIpv6NdPrefixLength")

                self.cdtifipv6ndraintervalmax = YLeaf(YType.uint32, "cdtIfIpv6NdRaIntervalMax")

                self.cdtifipv6ndraintervalmin = YLeaf(YType.uint32, "cdtIfIpv6NdRaIntervalMin")

                self.cdtifipv6ndraintervalunits = YLeaf(YType.enumeration, "cdtIfIpv6NdRaIntervalUnits")

                self.cdtifipv6ndralife = YLeaf(YType.uint32, "cdtIfIpv6NdRaLife")

                self.cdtifipv6ndreachabletime = YLeaf(YType.uint32, "cdtIfIpv6NdReachableTime")

                self.cdtifipv6ndrouterpreference = YLeaf(YType.enumeration, "cdtIfIpv6NdRouterPreference")

                self.cdtifipv6ndvalidlife = YLeaf(YType.uint32, "cdtIfIpv6NdValidLife")

                self.cdtifipv6subenable = YLeaf(YType.boolean, "cdtIfIpv6SubEnable")

                self.cdtifipv6tcpmssadjust = YLeaf(YType.uint32, "cdtIfIpv6TcpMssAdjust")

                self.cdtifipv6verifyunirpf = YLeaf(YType.enumeration, "cdtIfIpv6VerifyUniRpf")

                self.cdtifipv6verifyunirpfacl = YLeaf(YType.str, "cdtIfIpv6VerifyUniRpfAcl")

                self.cdtifipv6verifyunirpfopts = YLeaf(YType.bits, "cdtIfIpv6VerifyUniRpfOpts")

                self.cdtifmtu = YLeaf(YType.uint32, "cdtIfMtu")

                self.cdtifvalid = YLeaf(YType.bits, "cdtIfValid")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cdttemplatename",
                                "cdtifcdpenable",
                                "cdtifflowmonitor",
                                "cdtifipv4mtu",
                                "cdtifipv4subenable",
                                "cdtifipv4tcpmssadjust",
                                "cdtifipv4unnumbered",
                                "cdtifipv4verifyunirpf",
                                "cdtifipv4verifyunirpfacl",
                                "cdtifipv4verifyunirpfopts",
                                "cdtifipv6enable",
                                "cdtifipv6nddadattempts",
                                "cdtifipv6ndnsinterval",
                                "cdtifipv6ndopts",
                                "cdtifipv6ndpreferredlife",
                                "cdtifipv6ndprefix",
                                "cdtifipv6ndprefixlength",
                                "cdtifipv6ndraintervalmax",
                                "cdtifipv6ndraintervalmin",
                                "cdtifipv6ndraintervalunits",
                                "cdtifipv6ndralife",
                                "cdtifipv6ndreachabletime",
                                "cdtifipv6ndrouterpreference",
                                "cdtifipv6ndvalidlife",
                                "cdtifipv6subenable",
                                "cdtifipv6tcpmssadjust",
                                "cdtifipv6verifyunirpf",
                                "cdtifipv6verifyunirpfacl",
                                "cdtifipv6verifyunirpfopts",
                                "cdtifmtu",
                                "cdtifvalid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry, self).__setattr__(name, value)

            class Cdtifipv6Ndraintervalunits(Enum):
                """
                Cdtifipv6Ndraintervalunits

                This object specifies the units of time for the corresponding

                instances of cdtIfIpv6NdRaIntervalMin and

                cdtIfIpv6NdRaIntervalMax.

                This column is valid only if the 'ipv6NdRaInterval' bit of the

                corresponding instance of cdtIfValid is '1'.

                .. data:: seconds = 1

                .. data:: milliseconds = 2

                """

                seconds = Enum.YLeaf(1, "seconds")

                milliseconds = Enum.YLeaf(2, "milliseconds")


            class Cdtifipv6Ndrouterpreference(Enum):
                """
                Cdtifipv6Ndrouterpreference

                This object specifies the Default Router Preference (DRP) for

                the router on the target interface.

                This column is valid only if the 'ipv6NdRouterPreference' bit of

                the corresponding instance of cdtIfValid is '1'.

                .. data:: high = 1

                .. data:: medium = 2

                .. data:: low = 3

                """

                high = Enum.YLeaf(1, "high")

                medium = Enum.YLeaf(2, "medium")

                low = Enum.YLeaf(3, "low")


            def has_data(self):
                return (
                    self.cdttemplatename.is_set or
                    self.cdtifcdpenable.is_set or
                    self.cdtifflowmonitor.is_set or
                    self.cdtifipv4mtu.is_set or
                    self.cdtifipv4subenable.is_set or
                    self.cdtifipv4tcpmssadjust.is_set or
                    self.cdtifipv4unnumbered.is_set or
                    self.cdtifipv4verifyunirpf.is_set or
                    self.cdtifipv4verifyunirpfacl.is_set or
                    self.cdtifipv4verifyunirpfopts.is_set or
                    self.cdtifipv6enable.is_set or
                    self.cdtifipv6nddadattempts.is_set or
                    self.cdtifipv6ndnsinterval.is_set or
                    self.cdtifipv6ndopts.is_set or
                    self.cdtifipv6ndpreferredlife.is_set or
                    self.cdtifipv6ndprefix.is_set or
                    self.cdtifipv6ndprefixlength.is_set or
                    self.cdtifipv6ndraintervalmax.is_set or
                    self.cdtifipv6ndraintervalmin.is_set or
                    self.cdtifipv6ndraintervalunits.is_set or
                    self.cdtifipv6ndralife.is_set or
                    self.cdtifipv6ndreachabletime.is_set or
                    self.cdtifipv6ndrouterpreference.is_set or
                    self.cdtifipv6ndvalidlife.is_set or
                    self.cdtifipv6subenable.is_set or
                    self.cdtifipv6tcpmssadjust.is_set or
                    self.cdtifipv6verifyunirpf.is_set or
                    self.cdtifipv6verifyunirpfacl.is_set or
                    self.cdtifipv6verifyunirpfopts.is_set or
                    self.cdtifmtu.is_set or
                    self.cdtifvalid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cdttemplatename.yfilter != YFilter.not_set or
                    self.cdtifcdpenable.yfilter != YFilter.not_set or
                    self.cdtifflowmonitor.yfilter != YFilter.not_set or
                    self.cdtifipv4mtu.yfilter != YFilter.not_set or
                    self.cdtifipv4subenable.yfilter != YFilter.not_set or
                    self.cdtifipv4tcpmssadjust.yfilter != YFilter.not_set or
                    self.cdtifipv4unnumbered.yfilter != YFilter.not_set or
                    self.cdtifipv4verifyunirpf.yfilter != YFilter.not_set or
                    self.cdtifipv4verifyunirpfacl.yfilter != YFilter.not_set or
                    self.cdtifipv4verifyunirpfopts.yfilter != YFilter.not_set or
                    self.cdtifipv6enable.yfilter != YFilter.not_set or
                    self.cdtifipv6nddadattempts.yfilter != YFilter.not_set or
                    self.cdtifipv6ndnsinterval.yfilter != YFilter.not_set or
                    self.cdtifipv6ndopts.yfilter != YFilter.not_set or
                    self.cdtifipv6ndpreferredlife.yfilter != YFilter.not_set or
                    self.cdtifipv6ndprefix.yfilter != YFilter.not_set or
                    self.cdtifipv6ndprefixlength.yfilter != YFilter.not_set or
                    self.cdtifipv6ndraintervalmax.yfilter != YFilter.not_set or
                    self.cdtifipv6ndraintervalmin.yfilter != YFilter.not_set or
                    self.cdtifipv6ndraintervalunits.yfilter != YFilter.not_set or
                    self.cdtifipv6ndralife.yfilter != YFilter.not_set or
                    self.cdtifipv6ndreachabletime.yfilter != YFilter.not_set or
                    self.cdtifipv6ndrouterpreference.yfilter != YFilter.not_set or
                    self.cdtifipv6ndvalidlife.yfilter != YFilter.not_set or
                    self.cdtifipv6subenable.yfilter != YFilter.not_set or
                    self.cdtifipv6tcpmssadjust.yfilter != YFilter.not_set or
                    self.cdtifipv6verifyunirpf.yfilter != YFilter.not_set or
                    self.cdtifipv6verifyunirpfacl.yfilter != YFilter.not_set or
                    self.cdtifipv6verifyunirpfopts.yfilter != YFilter.not_set or
                    self.cdtifmtu.yfilter != YFilter.not_set or
                    self.cdtifvalid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cdtIfTemplateEntry" + "[cdtTemplateName='" + self.cdttemplatename.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/cdtIfTemplateTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cdttemplatename.is_set or self.cdttemplatename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdttemplatename.get_name_leafdata())
                if (self.cdtifcdpenable.is_set or self.cdtifcdpenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifcdpenable.get_name_leafdata())
                if (self.cdtifflowmonitor.is_set or self.cdtifflowmonitor.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifflowmonitor.get_name_leafdata())
                if (self.cdtifipv4mtu.is_set or self.cdtifipv4mtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv4mtu.get_name_leafdata())
                if (self.cdtifipv4subenable.is_set or self.cdtifipv4subenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv4subenable.get_name_leafdata())
                if (self.cdtifipv4tcpmssadjust.is_set or self.cdtifipv4tcpmssadjust.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv4tcpmssadjust.get_name_leafdata())
                if (self.cdtifipv4unnumbered.is_set or self.cdtifipv4unnumbered.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv4unnumbered.get_name_leafdata())
                if (self.cdtifipv4verifyunirpf.is_set or self.cdtifipv4verifyunirpf.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv4verifyunirpf.get_name_leafdata())
                if (self.cdtifipv4verifyunirpfacl.is_set or self.cdtifipv4verifyunirpfacl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv4verifyunirpfacl.get_name_leafdata())
                if (self.cdtifipv4verifyunirpfopts.is_set or self.cdtifipv4verifyunirpfopts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv4verifyunirpfopts.get_name_leafdata())
                if (self.cdtifipv6enable.is_set or self.cdtifipv6enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv6enable.get_name_leafdata())
                if (self.cdtifipv6nddadattempts.is_set or self.cdtifipv6nddadattempts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv6nddadattempts.get_name_leafdata())
                if (self.cdtifipv6ndnsinterval.is_set or self.cdtifipv6ndnsinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv6ndnsinterval.get_name_leafdata())
                if (self.cdtifipv6ndopts.is_set or self.cdtifipv6ndopts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv6ndopts.get_name_leafdata())
                if (self.cdtifipv6ndpreferredlife.is_set or self.cdtifipv6ndpreferredlife.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv6ndpreferredlife.get_name_leafdata())
                if (self.cdtifipv6ndprefix.is_set or self.cdtifipv6ndprefix.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv6ndprefix.get_name_leafdata())
                if (self.cdtifipv6ndprefixlength.is_set or self.cdtifipv6ndprefixlength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv6ndprefixlength.get_name_leafdata())
                if (self.cdtifipv6ndraintervalmax.is_set or self.cdtifipv6ndraintervalmax.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv6ndraintervalmax.get_name_leafdata())
                if (self.cdtifipv6ndraintervalmin.is_set or self.cdtifipv6ndraintervalmin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv6ndraintervalmin.get_name_leafdata())
                if (self.cdtifipv6ndraintervalunits.is_set or self.cdtifipv6ndraintervalunits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv6ndraintervalunits.get_name_leafdata())
                if (self.cdtifipv6ndralife.is_set or self.cdtifipv6ndralife.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv6ndralife.get_name_leafdata())
                if (self.cdtifipv6ndreachabletime.is_set or self.cdtifipv6ndreachabletime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv6ndreachabletime.get_name_leafdata())
                if (self.cdtifipv6ndrouterpreference.is_set or self.cdtifipv6ndrouterpreference.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv6ndrouterpreference.get_name_leafdata())
                if (self.cdtifipv6ndvalidlife.is_set or self.cdtifipv6ndvalidlife.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv6ndvalidlife.get_name_leafdata())
                if (self.cdtifipv6subenable.is_set or self.cdtifipv6subenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv6subenable.get_name_leafdata())
                if (self.cdtifipv6tcpmssadjust.is_set or self.cdtifipv6tcpmssadjust.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv6tcpmssadjust.get_name_leafdata())
                if (self.cdtifipv6verifyunirpf.is_set or self.cdtifipv6verifyunirpf.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv6verifyunirpf.get_name_leafdata())
                if (self.cdtifipv6verifyunirpfacl.is_set or self.cdtifipv6verifyunirpfacl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv6verifyunirpfacl.get_name_leafdata())
                if (self.cdtifipv6verifyunirpfopts.is_set or self.cdtifipv6verifyunirpfopts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifipv6verifyunirpfopts.get_name_leafdata())
                if (self.cdtifmtu.is_set or self.cdtifmtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifmtu.get_name_leafdata())
                if (self.cdtifvalid.is_set or self.cdtifvalid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtifvalid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cdtTemplateName" or name == "cdtIfCdpEnable" or name == "cdtIfFlowMonitor" or name == "cdtIfIpv4Mtu" or name == "cdtIfIpv4SubEnable" or name == "cdtIfIpv4TcpMssAdjust" or name == "cdtIfIpv4Unnumbered" or name == "cdtIfIpv4VerifyUniRpf" or name == "cdtIfIpv4VerifyUniRpfAcl" or name == "cdtIfIpv4VerifyUniRpfOpts" or name == "cdtIfIpv6Enable" or name == "cdtIfIpv6NdDadAttempts" or name == "cdtIfIpv6NdNsInterval" or name == "cdtIfIpv6NdOpts" or name == "cdtIfIpv6NdPreferredLife" or name == "cdtIfIpv6NdPrefix" or name == "cdtIfIpv6NdPrefixLength" or name == "cdtIfIpv6NdRaIntervalMax" or name == "cdtIfIpv6NdRaIntervalMin" or name == "cdtIfIpv6NdRaIntervalUnits" or name == "cdtIfIpv6NdRaLife" or name == "cdtIfIpv6NdReachableTime" or name == "cdtIfIpv6NdRouterPreference" or name == "cdtIfIpv6NdValidLife" or name == "cdtIfIpv6SubEnable" or name == "cdtIfIpv6TcpMssAdjust" or name == "cdtIfIpv6VerifyUniRpf" or name == "cdtIfIpv6VerifyUniRpfAcl" or name == "cdtIfIpv6VerifyUniRpfOpts" or name == "cdtIfMtu" or name == "cdtIfValid"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cdtTemplateName"):
                    self.cdttemplatename = value
                    self.cdttemplatename.value_namespace = name_space
                    self.cdttemplatename.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfCdpEnable"):
                    self.cdtifcdpenable = value
                    self.cdtifcdpenable.value_namespace = name_space
                    self.cdtifcdpenable.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfFlowMonitor"):
                    self.cdtifflowmonitor = value
                    self.cdtifflowmonitor.value_namespace = name_space
                    self.cdtifflowmonitor.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfIpv4Mtu"):
                    self.cdtifipv4mtu = value
                    self.cdtifipv4mtu.value_namespace = name_space
                    self.cdtifipv4mtu.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfIpv4SubEnable"):
                    self.cdtifipv4subenable = value
                    self.cdtifipv4subenable.value_namespace = name_space
                    self.cdtifipv4subenable.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfIpv4TcpMssAdjust"):
                    self.cdtifipv4tcpmssadjust = value
                    self.cdtifipv4tcpmssadjust.value_namespace = name_space
                    self.cdtifipv4tcpmssadjust.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfIpv4Unnumbered"):
                    self.cdtifipv4unnumbered = value
                    self.cdtifipv4unnumbered.value_namespace = name_space
                    self.cdtifipv4unnumbered.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfIpv4VerifyUniRpf"):
                    self.cdtifipv4verifyunirpf = value
                    self.cdtifipv4verifyunirpf.value_namespace = name_space
                    self.cdtifipv4verifyunirpf.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfIpv4VerifyUniRpfAcl"):
                    self.cdtifipv4verifyunirpfacl = value
                    self.cdtifipv4verifyunirpfacl.value_namespace = name_space
                    self.cdtifipv4verifyunirpfacl.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfIpv4VerifyUniRpfOpts"):
                    self.cdtifipv4verifyunirpfopts[value] = True
                if(value_path == "cdtIfIpv6Enable"):
                    self.cdtifipv6enable = value
                    self.cdtifipv6enable.value_namespace = name_space
                    self.cdtifipv6enable.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfIpv6NdDadAttempts"):
                    self.cdtifipv6nddadattempts = value
                    self.cdtifipv6nddadattempts.value_namespace = name_space
                    self.cdtifipv6nddadattempts.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfIpv6NdNsInterval"):
                    self.cdtifipv6ndnsinterval = value
                    self.cdtifipv6ndnsinterval.value_namespace = name_space
                    self.cdtifipv6ndnsinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfIpv6NdOpts"):
                    self.cdtifipv6ndopts[value] = True
                if(value_path == "cdtIfIpv6NdPreferredLife"):
                    self.cdtifipv6ndpreferredlife = value
                    self.cdtifipv6ndpreferredlife.value_namespace = name_space
                    self.cdtifipv6ndpreferredlife.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfIpv6NdPrefix"):
                    self.cdtifipv6ndprefix = value
                    self.cdtifipv6ndprefix.value_namespace = name_space
                    self.cdtifipv6ndprefix.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfIpv6NdPrefixLength"):
                    self.cdtifipv6ndprefixlength = value
                    self.cdtifipv6ndprefixlength.value_namespace = name_space
                    self.cdtifipv6ndprefixlength.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfIpv6NdRaIntervalMax"):
                    self.cdtifipv6ndraintervalmax = value
                    self.cdtifipv6ndraintervalmax.value_namespace = name_space
                    self.cdtifipv6ndraintervalmax.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfIpv6NdRaIntervalMin"):
                    self.cdtifipv6ndraintervalmin = value
                    self.cdtifipv6ndraintervalmin.value_namespace = name_space
                    self.cdtifipv6ndraintervalmin.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfIpv6NdRaIntervalUnits"):
                    self.cdtifipv6ndraintervalunits = value
                    self.cdtifipv6ndraintervalunits.value_namespace = name_space
                    self.cdtifipv6ndraintervalunits.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfIpv6NdRaLife"):
                    self.cdtifipv6ndralife = value
                    self.cdtifipv6ndralife.value_namespace = name_space
                    self.cdtifipv6ndralife.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfIpv6NdReachableTime"):
                    self.cdtifipv6ndreachabletime = value
                    self.cdtifipv6ndreachabletime.value_namespace = name_space
                    self.cdtifipv6ndreachabletime.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfIpv6NdRouterPreference"):
                    self.cdtifipv6ndrouterpreference = value
                    self.cdtifipv6ndrouterpreference.value_namespace = name_space
                    self.cdtifipv6ndrouterpreference.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfIpv6NdValidLife"):
                    self.cdtifipv6ndvalidlife = value
                    self.cdtifipv6ndvalidlife.value_namespace = name_space
                    self.cdtifipv6ndvalidlife.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfIpv6SubEnable"):
                    self.cdtifipv6subenable = value
                    self.cdtifipv6subenable.value_namespace = name_space
                    self.cdtifipv6subenable.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfIpv6TcpMssAdjust"):
                    self.cdtifipv6tcpmssadjust = value
                    self.cdtifipv6tcpmssadjust.value_namespace = name_space
                    self.cdtifipv6tcpmssadjust.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfIpv6VerifyUniRpf"):
                    self.cdtifipv6verifyunirpf = value
                    self.cdtifipv6verifyunirpf.value_namespace = name_space
                    self.cdtifipv6verifyunirpf.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfIpv6VerifyUniRpfAcl"):
                    self.cdtifipv6verifyunirpfacl = value
                    self.cdtifipv6verifyunirpfacl.value_namespace = name_space
                    self.cdtifipv6verifyunirpfacl.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfIpv6VerifyUniRpfOpts"):
                    self.cdtifipv6verifyunirpfopts[value] = True
                if(value_path == "cdtIfMtu"):
                    self.cdtifmtu = value
                    self.cdtifmtu.value_namespace = name_space
                    self.cdtifmtu.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtIfValid"):
                    self.cdtifvalid[value] = True

        def has_data(self):
            for c in self.cdtiftemplateentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cdtiftemplateentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cdtIfTemplateTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cdtIfTemplateEntry"):
                for c in self.cdtiftemplateentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cdtiftemplateentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cdtIfTemplateEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cdtppptemplatetable(Entity):
        """
        This table contains attributes relating to PPP connection
        configuration.
        
        This table has a sparse\-dependent relationship on the
        cdtTemplateTable, containing a row for each dynamic template
        having a cdtTemplateType of one of the following values\:
        
            'derived'
            'ppp'
        
        .. attribute:: cdtppptemplateentry
        
        	An entry containing attributes relating to PPP connection configuration.  The system automatically creates an entry when the system or the EMS/NMS creates a row in the cdtTemplateTable with a cdtTemplateType of one of the following values\:      'derived'     'ppp'  Likewise, the system automatically destroys an entry when the system or the EMS/NMS destroys the corresponding row in the cdtTemplateTable
        	**type**\: list of    :py:class:`Cdtppptemplateentry <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry>`
        
        

        """

        _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
        _revision = '2007-09-06'

        def __init__(self):
            super(CiscoDynamicTemplateMib.Cdtppptemplatetable, self).__init__()

            self.yang_name = "cdtPppTemplateTable"
            self.yang_parent_name = "CISCO-DYNAMIC-TEMPLATE-MIB"

            self.cdtppptemplateentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoDynamicTemplateMib.Cdtppptemplatetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoDynamicTemplateMib.Cdtppptemplatetable, self).__setattr__(name, value)


        class Cdtppptemplateentry(Entity):
            """
            An entry containing attributes relating to PPP connection
            configuration.
            
            The system automatically creates an entry when the system or the
            EMS/NMS creates a row in the cdtTemplateTable with a
            cdtTemplateType of one of the following values\:
            
                'derived'
                'ppp'
            
            Likewise, the system automatically destroys an entry when the
            system or the EMS/NMS destroys the corresponding row in the
            cdtTemplateTable.
            
            .. attribute:: cdttemplatename  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..64
            
            	**refers to**\:  :py:class:`cdttemplatename <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdttemplatetable.Cdttemplateentry>`
            
            .. attribute:: cdtpppaccounting
            
            	This object specifies whether the system applies accounting services to the target PPP connection.  This column is valid only if the 'accounting' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  bool
            
            .. attribute:: cdtpppauthentication
            
            	This object specifies authentication services applied to a target PPP connection and other options affecting authentication services\:      'chap'         This option enables the Challenge Handshake Protocol (CHAP)         on a target PPP connection.      'msChap'         This option enables Microsoft's CHAP on a target PPP         connection.      'msChapV2'         This option enables version 2 of Microsoft's CHAP on a         target PPP connection.      'pap'         This option enables Password Authentication Protocol (PAP)         on a target PPP connection.      'eap'         This option enables Extensible Authentication Protocol (EAP)         on a target PPP connection.      'optional'         This option specifies that the system accepts the connection         even if the peer of a target PPP connection refuses to         accept the authentication methods the system has         requested.      'callin'         This option specifies that authentication should only happen         for incoming calls.      'oneTime'         This option specifies that the system accepts the username         and password in the username field of authentication         responses received on a target PPP connection.  This column is valid only if the 'authentication' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:   :py:class:`Cdtpppauthentication <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtpppauthentication>`
            
            .. attribute:: cdtpppauthenticationmethods
            
            	This object specifies the name of a list of authentication methods used on a target PPP connection.  If the template does not include this attribute, then the system uses the default method list.  This column is valid only if the 'authentication' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cdtpppauthorization
            
            	This object specifies whether the system applies authorization services to a target PPP connection.  This column is valid only if the 'authorization' bit of the corresponding instance of cditPppValid is '1'
            	**type**\:  bool
            
            .. attribute:: cdtpppchaphostname
            
            	This object specifies the hostname sent in a CHAP response on a target PPP connection.  If the template does not include this attribute, then the system uses its assigned hostname.  This column is valid only if the 'chapHostname' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cdtpppchapopts
            
            	This object specifies how the system processes the CHAP on a target PPP connection\:      'refuse'         This option specifies that the system should refuse CHAP         requests from peers of a target PPP connection.      'callin'         This option specifies that the system should only refuse         CHAP requests for incoming calls on a target PPP         connection.  This option is only relevant if the         'refuse' option is set to '1'.      'wait'         This option delays CHAP authentication until after the         peer of a target PPP connection has authenticated itself         to the system.      'encrypted'         This option specifies that the value specified by the         corresponding instance of cdtPppChapPassword is already         encrypted.  This column is valid only if the 'chapOpts' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:   :py:class:`Cdtpppchapopts <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtpppchapopts>`
            
            .. attribute:: cdtpppchappassword
            
            	This object specifies the password used to construct a CHAP response on the target PPP connection.  This column is valid only if the 'chapPassword' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cdtpppeapidentity
            
            	This object specifies the identity sent in an EAP response on a target PPP connection.  This column is valid only if the 'eapIdentity' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cdtpppeapopts
            
            	This object specifies how the system processes the EAP on a target PPP connection\:      'refuse'         This option specifies that the system should refuse EAP         requests from peers of a target PPP connection.      'callin'         This option specifies that the system should only refuse EAP         requests for incoming calls on a target PPP connection.         This option is only relevant if the 'refuse' option is         set to '1'.      'wait'         This option delays EAP authentication until after the         peer of a target PPP connection has authenticated itself         to the system.      'local'         This option specifies that the system should locally         authenticate the peer of a target PPP connection,         rather than acting as a proxy to an external AAA server.  This column is valid only if the 'eapOpts' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:   :py:class:`Cdtpppeapopts <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtpppeapopts>`
            
            .. attribute:: cdtpppeappassword
            
            	This object specifies the password used to construct an EAP response on a target PPP connection.  This column is valid only if the 'eapPassword' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cdtpppipcpaddroption
            
            	This object specifies the IPCP address option for a target PPP connection\:      'other'         The implementation of this MIB module does not recognize         the configured IPCP address option.      'accept'         The system accepts any non\-zero IP address from the peer         of a target PPP connection.      'required'         The system disconnects the peer of a target PPP         connection if it could not negotiate an IP address.      'unique'         The system disconnects the peer of a target PPP         connection if the IP address is already in use.  This column is valid only if the 'ipcpAddrOption' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:   :py:class:`Cdtpppipcpaddroption <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtpppipcpaddroption>`
            
            .. attribute:: cdtpppipcpdnsoption
            
            	This object specifies the IPCP DNS option for the dynamic interface\:      'other'         The implementation of this MIB module does not recognize         the configured DNS option.      'accept'         The system accepts any non\-zero DNS address form the         peer of a target PPP connection.      'request'         The system requests the DNS address from the peer of a         target PPP connection.      'reject'         The system rejects the DNS option from the peer of a         target PPP connection.  This column is valid only if the 'ipcpDnsOption' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:   :py:class:`Cdtpppipcpdnsoption <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtpppipcpdnsoption>`
            
            .. attribute:: cdtpppipcpdnsprimary
            
            	This object specifies the IP address of the primary DNS server offered to the peer of a target PPP connection.  This column is valid only if the 'ipcpDnsPrimary' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  str
            
            .. attribute:: cdtpppipcpdnssecondary
            
            	This object specifies the IP address of the secondary DNS server offered to the peer of a target PPP connection.  This column is valid only if the 'ipcpDnsSecondary' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  str
            
            .. attribute:: cdtpppipcpmask
            
            	This object specifies the IP address mask offered to the peer of a target PPP connection.  This column is valid only if the 'ipcpMask' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  str
            
            .. attribute:: cdtpppipcpmaskoption
            
            	This object specifies the IPCP IP subnet mask option for a target PPP connection\:      'other'         The implementation of this MIB module does not recognize         the configured IP subnet mask option.      'request'         The system requests the IP subnet mask from the peer of         a target PPP connection.      'reject'         The system rejects the IP subnet mask option from the         peer of a target PPP connection.  This column is valid only if the 'ipcpMaskOption' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:   :py:class:`Cdtpppipcpmaskoption <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtpppipcpmaskoption>`
            
            .. attribute:: cdtpppipcpwinsoption
            
            	This object specifies the IPCP WINS option for a target PPP connection\:      'other'         The implementation of this MIB module does not recognize         the configured WINS option.      'accept'         The system accepts any non\-zero WINS address from the         peer of a target PPP connection.      'request'         The system requests the WINS address from the peer of         a target PPP connection.      'reject'         The system rejects the WINS option from the peer of a         target PPP connection.  This column is valid only if the 'ipcpWinsOption' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:   :py:class:`Cdtpppipcpwinsoption <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtpppipcpwinsoption>`
            
            .. attribute:: cdtpppipcpwinsprimary
            
            	This object specifies the IP address of the primary WINS server offered to the peer of a target PPP connection.  This column is valid only if the 'ipcpWinsPrimary' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  str
            
            .. attribute:: cdtpppipcpwinssecondary
            
            	This object specifies the IP address of the secondary WINS server offered to the peer of a target PPP connection.  This column is valid only if the 'ipcpWinsSecondary' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  str
            
            .. attribute:: cdtppploopbackignore
            
            	This object specifies whether the system ignores loopback on a target PPP connection.  When the system ignores loopback, loopback detection is disabled.  This column is valid only if the 'loopbackIgnore' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  bool
            
            .. attribute:: cdtpppmaxbadauth
            
            	This object specifies the number of authentication failures allowed by the system before a target PPP connection is reset.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid.  This column is valid only if the 'maxBadAuth' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cdtpppmaxconfigure
            
            	This object specifies the number of unacknowledged Configure\-Request messages a target PPP connection can send before the system abandons LCP or NCP negotiations.  This column is valid only if the 'maxConfigure' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: cdtpppmaxfailure
            
            	This object specifies the number of Configure\-Nak messages a target PPP connection can receive before the system abandons LCP or NCP negotiations.  This column is valid only if the 'maxFailure' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: cdtpppmaxterminate
            
            	This object specifies the number of unacknowledged Terminate\-Request messages a target PPP connection can send before the system abandons LCP or NCP negotiations.  This column is valid only if the 'maxTerminate' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: cdtpppmschapv1hostname
            
            	This object specifies the hostname sent in a Microsoft CHAP (v1) response on a target PPP connection.  If the template does not include this attribute, then the system uses its assigned hostname.  This column is valid only if the 'msChapV1Hostname' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cdtpppmschapv1opts
            
            	This object specifies how the system processes version 1 of Microsoft CHAP on a target PPP connection\:      'refuse'         This option specifies that the system should refuse         Microsoft CHAP (v1) requests from peers of a target PPP         connection.      'callin'         This option specifies that the system should only refuse         Microsoft CHAP (v1) requests for incoming calls on a         target PPP connection.  This option is only relevant if         the 'refuse' option is set to '1'.      'wait'         This option delays Microsoft CHAP (v1) authentication         until after the peer of a target PPP connection has         authenticated itself to the system.      'encrypted'         This option specifies that the value specified by the         corresponding instance of cdtPppMsChapV1Password is         already encrypted.  This column is valid only if the 'msChapV1Opts' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:   :py:class:`Cdtpppmschapv1Opts <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtpppmschapv1Opts>`
            
            .. attribute:: cdtpppmschapv1password
            
            	This object specifies the password used to construct a Microsoft CHAP (v1) response on a target PPP connection.  This column is valid only if the 'msChapV1Password' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cdtpppmschapv2hostname
            
            	This object specifies the hostname sent in a Microsoft CHAP (v2) response on a target PPP connection.  If the template does not include this attribute, then the system uses its assigned hostname.  This column is valid only if the 'msChapV2Hostname' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cdtpppmschapv2opts
            
            	This object specifies how the system processes version 2 of Microsoft CHAP on a target PPP connection\:      'refuse'         This option specifies that the system should refuse         Microsoft CHAP (v2) requests from peers of a target PPP         connection.      'callin'         This option specifies that the system should only refuse         Microsoft CHAP (v2) requests for incoming calls on a         target PPP connection.  This option is only relevant if         the 'refuse' option is set to '1'.      'wait'         This option delays Microsoft CHAP (v2) authentication         until after the peer of a target PPP connection has         authenticated itself to the system.      'encrypted'         This option specifies that the value specified by the         corresponding instance of cdtPppMsChapV2Password is         already encrypted.  This column is valid only if the 'msChapV2Opts' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:   :py:class:`Cdtpppmschapv2Opts <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtpppmschapv2Opts>`
            
            .. attribute:: cdtpppmschapv2password
            
            	This object specifies the password used to construct a Microsoft CHAP (v2) response on a target PPP connection.  This column is valid only if the 'msChapV2Password' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cdtppppapopts
            
            	This object specifies how the system processes the PAP on a target PPP connection\:      'refuse'         This option specifies that the system should refuse PAP         requests from peers of a target PPP connection.      'encrypted'         This option specifies that the value specified by the         corresponding instance of cdtPppPapSentPassword is         already encrypted.  This column is valid only if the 'papOpts' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:   :py:class:`Cdtppppapopts <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtppppapopts>`
            
            .. attribute:: cdtppppappassword
            
            	This object specifies the username used to construct a PAP response on a target PPP connection.  This column is valid only if the 'papPassword' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cdtppppapusername
            
            	This object specifies the username sent in a PAP response on a target PPP connection.  This column is valid only if the 'papUsername' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cdtppppeerdefipaddr
            
            	This object specifies the IP address the system assigns to the peer of a target PPP connection.  This column is valid only if the 'peerDefIpAddr' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  str
            
            .. attribute:: cdtppppeerdefipaddropts
            
            	This object specifies options that affect how the system assigns an IP address to the peer of a target PPP connection\:      'ipAddrForced'         This option forces the system to assign the next         available IP address in the pool to the peer of a         target PPP connection.  When disabled, the peer may         negotiate a specific IP address or the system can assign         the peer its previously assigned IP address.      'matchAaaPools'         This option specifies that the names of the IP address         pools provided by an external AAA server must appear in         the corresponding list of IP address pool specified by         the cdtPppPeerIpAddrPoolTable.      'backupPools'         This option specifies that the corresponding names of         the IP address pools specified by the         cditPppPeerIpAddrPoolTable serve as backup pools to         those provided by an external AAA server.      'staticPools'         This option suppresses an attempt to load pools from an         external AAA server when the system encounters a missing         pool name.  This column is valid only if the 'peerIpAddrOpts' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:   :py:class:`Cdtppppeerdefipaddropts <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtppppeerdefipaddropts>`
            
            .. attribute:: cdtppppeerdefipaddrsrc
            
            	This object specifies how the system assigns an IP address to the peer of a target PPP connection\:      'static'         The system assigns the IP address specified by the         corresponding instance of cdtPppPeerDefIpAddr.      'pool'         The system allocates the first available IP address from         the corresponding list of named pools contained by the         cdtPppPeerIpAddrPoolTable.      'dhcp'         The system acts as a DHCP proxy\-client to obtain an IP         address.  This column is valid only if the 'peerDefIpAddrSrc' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:   :py:class:`Cdtppppeerdefipaddrsrc <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtppppeerdefipaddrsrc>`
            
            .. attribute:: cdtppptimeoutauthentication
            
            	This objects specifies the maximum time the system will wait for a response to an authentication request on a target PPP connection.  This column is valid only if the 'timeoutAuthentication' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  int
            
            	**range:** 1..255
            
            	**units**\: seconds
            
            .. attribute:: cdtppptimeoutretry
            
            	This objects specifies the maximum time the system will wait for a response to a PPP control packets on a target PPP connection.  This column is valid only if the 'timeoutRetry' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  int
            
            	**range:** 1..255
            
            	**units**\: seconds
            
            .. attribute:: cdtpppvalid
            
            	This object specifies which attributes in the dynamic template have been configured to valid values.  Each bit in this bit string corresponds to a column in this table.  If the bit is '0', then the value of the corresponding column is not valid.  If the bit is '1', then the value of the corresponding column has been configured to a valid value.  The following list specifies the mappings between bits and the columns\:      accounting              => cdtPppAccounting     authentication          => cdtPppAuthentication     authenticationMethods   => cdtPppAuthenticationMethods     authorization           => cdtPppAuthorization     loopbackIgnore          => cdtPppLoopbackIgnore     maxBadAuth              => cdtPppMaxBadAuth     maxConfigure            => cdtPppMaxConfigure     maxFailure              => cdtPppMaxFailure     maxTerminate            => cdtPppMaxTerminate     timeoutAuthentication   => cdtPppTimeoutAuthentication     timeoutRetry            => cdtPppTimeoutRetry     chapOpts                => cdtPppChapOpts     chapHostname            => cdtPppChapHostname     chapPassword            => cdtPppChapPassword     msChapV1Opts            => cdtPppMsChapV1Opts     msChapV1Hostname        => cdtPppMsChapV1Hostname     msChapV1Password        => cdtPppMsChapV1Password     msChapV2Opts            => cdtPppMsChapV2Opts     msChapV2Hostname        => cdtPppMsChapV2Hostname     msChapV2Password        => cdtPppMsChapV2Password     papOpts                 => cdtPppPapOpts     papSentUsername         => cdtPppPapUsername     papSentPassword         => cdtPppPapPassword     eapOpts                 => cdtPppEapOpts     eapIdentity             => cdtPppEapIdentity     eapPassword             => cdtPppEapPassword     ipcpAddrOption          => cdtPppIpcpAddrOption     ipcpDnsOption           => cdtPppIpcpDnsOption     ipcpDnsPrimary          => cdtPppIpcpDnsPrimary     ipcpDnsSecondary        => cdtPppIpcpDnsSecondary     ipcpWinsOption          => cdtPppIpcpWinsOption     ipcpWinsPrimary         => cdtPppIpcpWinsPrimary     ipcpWinsSecondary       => cdtPppIpcpWinsSecondary     ipcpMaskOption          => cdtPppIpcpMaskOption     ipcpMask                => cdtPppIpcpMask     peerDefIpAddrOpts       => cdtPppPeerOpts     peerDefIpAddrSrc        => cdtPppPeerDefIpAddrSrc     peerDefIpAddr           => cdtPppPeerDefIpAddr
            	**type**\:   :py:class:`Cdtpppvalid <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtpppvalid>`
            
            

            """

            _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
            _revision = '2007-09-06'

            def __init__(self):
                super(CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry, self).__init__()

                self.yang_name = "cdtPppTemplateEntry"
                self.yang_parent_name = "cdtPppTemplateTable"

                self.cdttemplatename = YLeaf(YType.str, "cdtTemplateName")

                self.cdtpppaccounting = YLeaf(YType.boolean, "cdtPppAccounting")

                self.cdtpppauthentication = YLeaf(YType.bits, "cdtPppAuthentication")

                self.cdtpppauthenticationmethods = YLeaf(YType.str, "cdtPppAuthenticationMethods")

                self.cdtpppauthorization = YLeaf(YType.boolean, "cdtPppAuthorization")

                self.cdtpppchaphostname = YLeaf(YType.str, "cdtPppChapHostname")

                self.cdtpppchapopts = YLeaf(YType.bits, "cdtPppChapOpts")

                self.cdtpppchappassword = YLeaf(YType.str, "cdtPppChapPassword")

                self.cdtpppeapidentity = YLeaf(YType.str, "cdtPppEapIdentity")

                self.cdtpppeapopts = YLeaf(YType.bits, "cdtPppEapOpts")

                self.cdtpppeappassword = YLeaf(YType.str, "cdtPppEapPassword")

                self.cdtpppipcpaddroption = YLeaf(YType.enumeration, "cdtPppIpcpAddrOption")

                self.cdtpppipcpdnsoption = YLeaf(YType.enumeration, "cdtPppIpcpDnsOption")

                self.cdtpppipcpdnsprimary = YLeaf(YType.str, "cdtPppIpcpDnsPrimary")

                self.cdtpppipcpdnssecondary = YLeaf(YType.str, "cdtPppIpcpDnsSecondary")

                self.cdtpppipcpmask = YLeaf(YType.str, "cdtPppIpcpMask")

                self.cdtpppipcpmaskoption = YLeaf(YType.enumeration, "cdtPppIpcpMaskOption")

                self.cdtpppipcpwinsoption = YLeaf(YType.enumeration, "cdtPppIpcpWinsOption")

                self.cdtpppipcpwinsprimary = YLeaf(YType.str, "cdtPppIpcpWinsPrimary")

                self.cdtpppipcpwinssecondary = YLeaf(YType.str, "cdtPppIpcpWinsSecondary")

                self.cdtppploopbackignore = YLeaf(YType.boolean, "cdtPppLoopbackIgnore")

                self.cdtpppmaxbadauth = YLeaf(YType.uint32, "cdtPppMaxBadAuth")

                self.cdtpppmaxconfigure = YLeaf(YType.uint32, "cdtPppMaxConfigure")

                self.cdtpppmaxfailure = YLeaf(YType.uint32, "cdtPppMaxFailure")

                self.cdtpppmaxterminate = YLeaf(YType.uint32, "cdtPppMaxTerminate")

                self.cdtpppmschapv1hostname = YLeaf(YType.str, "cdtPppMsChapV1Hostname")

                self.cdtpppmschapv1opts = YLeaf(YType.bits, "cdtPppMsChapV1Opts")

                self.cdtpppmschapv1password = YLeaf(YType.str, "cdtPppMsChapV1Password")

                self.cdtpppmschapv2hostname = YLeaf(YType.str, "cdtPppMsChapV2Hostname")

                self.cdtpppmschapv2opts = YLeaf(YType.bits, "cdtPppMsChapV2Opts")

                self.cdtpppmschapv2password = YLeaf(YType.str, "cdtPppMsChapV2Password")

                self.cdtppppapopts = YLeaf(YType.bits, "cdtPppPapOpts")

                self.cdtppppappassword = YLeaf(YType.str, "cdtPppPapPassword")

                self.cdtppppapusername = YLeaf(YType.str, "cdtPppPapUsername")

                self.cdtppppeerdefipaddr = YLeaf(YType.str, "cdtPppPeerDefIpAddr")

                self.cdtppppeerdefipaddropts = YLeaf(YType.bits, "cdtPppPeerDefIpAddrOpts")

                self.cdtppppeerdefipaddrsrc = YLeaf(YType.enumeration, "cdtPppPeerDefIpAddrSrc")

                self.cdtppptimeoutauthentication = YLeaf(YType.uint32, "cdtPppTimeoutAuthentication")

                self.cdtppptimeoutretry = YLeaf(YType.uint32, "cdtPppTimeoutRetry")

                self.cdtpppvalid = YLeaf(YType.bits, "cdtPppValid")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cdttemplatename",
                                "cdtpppaccounting",
                                "cdtpppauthentication",
                                "cdtpppauthenticationmethods",
                                "cdtpppauthorization",
                                "cdtpppchaphostname",
                                "cdtpppchapopts",
                                "cdtpppchappassword",
                                "cdtpppeapidentity",
                                "cdtpppeapopts",
                                "cdtpppeappassword",
                                "cdtpppipcpaddroption",
                                "cdtpppipcpdnsoption",
                                "cdtpppipcpdnsprimary",
                                "cdtpppipcpdnssecondary",
                                "cdtpppipcpmask",
                                "cdtpppipcpmaskoption",
                                "cdtpppipcpwinsoption",
                                "cdtpppipcpwinsprimary",
                                "cdtpppipcpwinssecondary",
                                "cdtppploopbackignore",
                                "cdtpppmaxbadauth",
                                "cdtpppmaxconfigure",
                                "cdtpppmaxfailure",
                                "cdtpppmaxterminate",
                                "cdtpppmschapv1hostname",
                                "cdtpppmschapv1opts",
                                "cdtpppmschapv1password",
                                "cdtpppmschapv2hostname",
                                "cdtpppmschapv2opts",
                                "cdtpppmschapv2password",
                                "cdtppppapopts",
                                "cdtppppappassword",
                                "cdtppppapusername",
                                "cdtppppeerdefipaddr",
                                "cdtppppeerdefipaddropts",
                                "cdtppppeerdefipaddrsrc",
                                "cdtppptimeoutauthentication",
                                "cdtppptimeoutretry",
                                "cdtpppvalid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry, self).__setattr__(name, value)

            class Cdtpppipcpaddroption(Enum):
                """
                Cdtpppipcpaddroption

                This object specifies the IPCP address option for a target PPP

                connection\:

                    'other'

                        The implementation of this MIB module does not recognize

                        the configured IPCP address option.

                    'accept'

                        The system accepts any non\-zero IP address from the peer

                        of a target PPP connection.

                    'required'

                        The system disconnects the peer of a target PPP

                        connection if it could not negotiate an IP address.

                    'unique'

                        The system disconnects the peer of a target PPP

                        connection if the IP address is already in use.

                This column is valid only if the 'ipcpAddrOption' bit of the

                corresponding instance of cdtPppValid is '1'.

                .. data:: other = 1

                .. data:: accept = 2

                .. data:: required = 3

                .. data:: unique = 4

                """

                other = Enum.YLeaf(1, "other")

                accept = Enum.YLeaf(2, "accept")

                required = Enum.YLeaf(3, "required")

                unique = Enum.YLeaf(4, "unique")


            class Cdtpppipcpdnsoption(Enum):
                """
                Cdtpppipcpdnsoption

                This object specifies the IPCP DNS option for the dynamic

                interface\:

                    'other'

                        The implementation of this MIB module does not recognize

                        the configured DNS option.

                    'accept'

                        The system accepts any non\-zero DNS address form the

                        peer of a target PPP connection.

                    'request'

                        The system requests the DNS address from the peer of a

                        target PPP connection.

                    'reject'

                        The system rejects the DNS option from the peer of a

                        target PPP connection.

                This column is valid only if the 'ipcpDnsOption' bit of the

                corresponding instance of cdtPppValid is '1'.

                .. data:: other = 1

                .. data:: accept = 2

                .. data:: request = 3

                .. data:: reject = 4

                """

                other = Enum.YLeaf(1, "other")

                accept = Enum.YLeaf(2, "accept")

                request = Enum.YLeaf(3, "request")

                reject = Enum.YLeaf(4, "reject")


            class Cdtpppipcpmaskoption(Enum):
                """
                Cdtpppipcpmaskoption

                This object specifies the IPCP IP subnet mask option for a

                target PPP connection\:

                    'other'

                        The implementation of this MIB module does not recognize

                        the configured IP subnet mask option.

                    'request'

                        The system requests the IP subnet mask from the peer of

                        a target PPP connection.

                    'reject'

                        The system rejects the IP subnet mask option from the

                        peer of a target PPP connection.

                This column is valid only if the 'ipcpMaskOption' bit of the

                corresponding instance of cdtPppValid is '1'.

                .. data:: other = 1

                .. data:: request = 2

                .. data:: reject = 3

                """

                other = Enum.YLeaf(1, "other")

                request = Enum.YLeaf(2, "request")

                reject = Enum.YLeaf(3, "reject")


            class Cdtpppipcpwinsoption(Enum):
                """
                Cdtpppipcpwinsoption

                This object specifies the IPCP WINS option for a target PPP

                connection\:

                    'other'

                        The implementation of this MIB module does not recognize

                        the configured WINS option.

                    'accept'

                        The system accepts any non\-zero WINS address from the

                        peer of a target PPP connection.

                    'request'

                        The system requests the WINS address from the peer of

                        a target PPP connection.

                    'reject'

                        The system rejects the WINS option from the peer of a

                        target PPP connection.

                This column is valid only if the 'ipcpWinsOption' bit of the

                corresponding instance of cdtPppValid is '1'.

                .. data:: other = 1

                .. data:: accept = 2

                .. data:: request = 3

                .. data:: reject = 4

                """

                other = Enum.YLeaf(1, "other")

                accept = Enum.YLeaf(2, "accept")

                request = Enum.YLeaf(3, "request")

                reject = Enum.YLeaf(4, "reject")


            class Cdtppppeerdefipaddrsrc(Enum):
                """
                Cdtppppeerdefipaddrsrc

                This object specifies how the system assigns an IP address to

                the peer of a target PPP connection\:

                    'static'

                        The system assigns the IP address specified by the

                        corresponding instance of cdtPppPeerDefIpAddr.

                    'pool'

                        The system allocates the first available IP address from

                        the corresponding list of named pools contained by the

                        cdtPppPeerIpAddrPoolTable.

                    'dhcp'

                        The system acts as a DHCP proxy\-client to obtain an IP

                        address.

                This column is valid only if the 'peerDefIpAddrSrc' bit of the

                corresponding instance of cdtPppValid is '1'.

                .. data:: static = 1

                .. data:: pool = 2

                .. data:: dhcp = 3

                """

                static = Enum.YLeaf(1, "static")

                pool = Enum.YLeaf(2, "pool")

                dhcp = Enum.YLeaf(3, "dhcp")


            def has_data(self):
                return (
                    self.cdttemplatename.is_set or
                    self.cdtpppaccounting.is_set or
                    self.cdtpppauthentication.is_set or
                    self.cdtpppauthenticationmethods.is_set or
                    self.cdtpppauthorization.is_set or
                    self.cdtpppchaphostname.is_set or
                    self.cdtpppchapopts.is_set or
                    self.cdtpppchappassword.is_set or
                    self.cdtpppeapidentity.is_set or
                    self.cdtpppeapopts.is_set or
                    self.cdtpppeappassword.is_set or
                    self.cdtpppipcpaddroption.is_set or
                    self.cdtpppipcpdnsoption.is_set or
                    self.cdtpppipcpdnsprimary.is_set or
                    self.cdtpppipcpdnssecondary.is_set or
                    self.cdtpppipcpmask.is_set or
                    self.cdtpppipcpmaskoption.is_set or
                    self.cdtpppipcpwinsoption.is_set or
                    self.cdtpppipcpwinsprimary.is_set or
                    self.cdtpppipcpwinssecondary.is_set or
                    self.cdtppploopbackignore.is_set or
                    self.cdtpppmaxbadauth.is_set or
                    self.cdtpppmaxconfigure.is_set or
                    self.cdtpppmaxfailure.is_set or
                    self.cdtpppmaxterminate.is_set or
                    self.cdtpppmschapv1hostname.is_set or
                    self.cdtpppmschapv1opts.is_set or
                    self.cdtpppmschapv1password.is_set or
                    self.cdtpppmschapv2hostname.is_set or
                    self.cdtpppmschapv2opts.is_set or
                    self.cdtpppmschapv2password.is_set or
                    self.cdtppppapopts.is_set or
                    self.cdtppppappassword.is_set or
                    self.cdtppppapusername.is_set or
                    self.cdtppppeerdefipaddr.is_set or
                    self.cdtppppeerdefipaddropts.is_set or
                    self.cdtppppeerdefipaddrsrc.is_set or
                    self.cdtppptimeoutauthentication.is_set or
                    self.cdtppptimeoutretry.is_set or
                    self.cdtpppvalid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cdttemplatename.yfilter != YFilter.not_set or
                    self.cdtpppaccounting.yfilter != YFilter.not_set or
                    self.cdtpppauthentication.yfilter != YFilter.not_set or
                    self.cdtpppauthenticationmethods.yfilter != YFilter.not_set or
                    self.cdtpppauthorization.yfilter != YFilter.not_set or
                    self.cdtpppchaphostname.yfilter != YFilter.not_set or
                    self.cdtpppchapopts.yfilter != YFilter.not_set or
                    self.cdtpppchappassword.yfilter != YFilter.not_set or
                    self.cdtpppeapidentity.yfilter != YFilter.not_set or
                    self.cdtpppeapopts.yfilter != YFilter.not_set or
                    self.cdtpppeappassword.yfilter != YFilter.not_set or
                    self.cdtpppipcpaddroption.yfilter != YFilter.not_set or
                    self.cdtpppipcpdnsoption.yfilter != YFilter.not_set or
                    self.cdtpppipcpdnsprimary.yfilter != YFilter.not_set or
                    self.cdtpppipcpdnssecondary.yfilter != YFilter.not_set or
                    self.cdtpppipcpmask.yfilter != YFilter.not_set or
                    self.cdtpppipcpmaskoption.yfilter != YFilter.not_set or
                    self.cdtpppipcpwinsoption.yfilter != YFilter.not_set or
                    self.cdtpppipcpwinsprimary.yfilter != YFilter.not_set or
                    self.cdtpppipcpwinssecondary.yfilter != YFilter.not_set or
                    self.cdtppploopbackignore.yfilter != YFilter.not_set or
                    self.cdtpppmaxbadauth.yfilter != YFilter.not_set or
                    self.cdtpppmaxconfigure.yfilter != YFilter.not_set or
                    self.cdtpppmaxfailure.yfilter != YFilter.not_set or
                    self.cdtpppmaxterminate.yfilter != YFilter.not_set or
                    self.cdtpppmschapv1hostname.yfilter != YFilter.not_set or
                    self.cdtpppmschapv1opts.yfilter != YFilter.not_set or
                    self.cdtpppmschapv1password.yfilter != YFilter.not_set or
                    self.cdtpppmschapv2hostname.yfilter != YFilter.not_set or
                    self.cdtpppmschapv2opts.yfilter != YFilter.not_set or
                    self.cdtpppmschapv2password.yfilter != YFilter.not_set or
                    self.cdtppppapopts.yfilter != YFilter.not_set or
                    self.cdtppppappassword.yfilter != YFilter.not_set or
                    self.cdtppppapusername.yfilter != YFilter.not_set or
                    self.cdtppppeerdefipaddr.yfilter != YFilter.not_set or
                    self.cdtppppeerdefipaddropts.yfilter != YFilter.not_set or
                    self.cdtppppeerdefipaddrsrc.yfilter != YFilter.not_set or
                    self.cdtppptimeoutauthentication.yfilter != YFilter.not_set or
                    self.cdtppptimeoutretry.yfilter != YFilter.not_set or
                    self.cdtpppvalid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cdtPppTemplateEntry" + "[cdtTemplateName='" + self.cdttemplatename.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/cdtPppTemplateTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cdttemplatename.is_set or self.cdttemplatename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdttemplatename.get_name_leafdata())
                if (self.cdtpppaccounting.is_set or self.cdtpppaccounting.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppaccounting.get_name_leafdata())
                if (self.cdtpppauthentication.is_set or self.cdtpppauthentication.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppauthentication.get_name_leafdata())
                if (self.cdtpppauthenticationmethods.is_set or self.cdtpppauthenticationmethods.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppauthenticationmethods.get_name_leafdata())
                if (self.cdtpppauthorization.is_set or self.cdtpppauthorization.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppauthorization.get_name_leafdata())
                if (self.cdtpppchaphostname.is_set or self.cdtpppchaphostname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppchaphostname.get_name_leafdata())
                if (self.cdtpppchapopts.is_set or self.cdtpppchapopts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppchapopts.get_name_leafdata())
                if (self.cdtpppchappassword.is_set or self.cdtpppchappassword.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppchappassword.get_name_leafdata())
                if (self.cdtpppeapidentity.is_set or self.cdtpppeapidentity.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppeapidentity.get_name_leafdata())
                if (self.cdtpppeapopts.is_set or self.cdtpppeapopts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppeapopts.get_name_leafdata())
                if (self.cdtpppeappassword.is_set or self.cdtpppeappassword.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppeappassword.get_name_leafdata())
                if (self.cdtpppipcpaddroption.is_set or self.cdtpppipcpaddroption.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppipcpaddroption.get_name_leafdata())
                if (self.cdtpppipcpdnsoption.is_set or self.cdtpppipcpdnsoption.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppipcpdnsoption.get_name_leafdata())
                if (self.cdtpppipcpdnsprimary.is_set or self.cdtpppipcpdnsprimary.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppipcpdnsprimary.get_name_leafdata())
                if (self.cdtpppipcpdnssecondary.is_set or self.cdtpppipcpdnssecondary.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppipcpdnssecondary.get_name_leafdata())
                if (self.cdtpppipcpmask.is_set or self.cdtpppipcpmask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppipcpmask.get_name_leafdata())
                if (self.cdtpppipcpmaskoption.is_set or self.cdtpppipcpmaskoption.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppipcpmaskoption.get_name_leafdata())
                if (self.cdtpppipcpwinsoption.is_set or self.cdtpppipcpwinsoption.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppipcpwinsoption.get_name_leafdata())
                if (self.cdtpppipcpwinsprimary.is_set or self.cdtpppipcpwinsprimary.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppipcpwinsprimary.get_name_leafdata())
                if (self.cdtpppipcpwinssecondary.is_set or self.cdtpppipcpwinssecondary.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppipcpwinssecondary.get_name_leafdata())
                if (self.cdtppploopbackignore.is_set or self.cdtppploopbackignore.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtppploopbackignore.get_name_leafdata())
                if (self.cdtpppmaxbadauth.is_set or self.cdtpppmaxbadauth.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppmaxbadauth.get_name_leafdata())
                if (self.cdtpppmaxconfigure.is_set or self.cdtpppmaxconfigure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppmaxconfigure.get_name_leafdata())
                if (self.cdtpppmaxfailure.is_set or self.cdtpppmaxfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppmaxfailure.get_name_leafdata())
                if (self.cdtpppmaxterminate.is_set or self.cdtpppmaxterminate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppmaxterminate.get_name_leafdata())
                if (self.cdtpppmschapv1hostname.is_set or self.cdtpppmschapv1hostname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppmschapv1hostname.get_name_leafdata())
                if (self.cdtpppmschapv1opts.is_set or self.cdtpppmschapv1opts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppmschapv1opts.get_name_leafdata())
                if (self.cdtpppmschapv1password.is_set or self.cdtpppmschapv1password.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppmschapv1password.get_name_leafdata())
                if (self.cdtpppmschapv2hostname.is_set or self.cdtpppmschapv2hostname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppmschapv2hostname.get_name_leafdata())
                if (self.cdtpppmschapv2opts.is_set or self.cdtpppmschapv2opts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppmschapv2opts.get_name_leafdata())
                if (self.cdtpppmschapv2password.is_set or self.cdtpppmschapv2password.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppmschapv2password.get_name_leafdata())
                if (self.cdtppppapopts.is_set or self.cdtppppapopts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtppppapopts.get_name_leafdata())
                if (self.cdtppppappassword.is_set or self.cdtppppappassword.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtppppappassword.get_name_leafdata())
                if (self.cdtppppapusername.is_set or self.cdtppppapusername.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtppppapusername.get_name_leafdata())
                if (self.cdtppppeerdefipaddr.is_set or self.cdtppppeerdefipaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtppppeerdefipaddr.get_name_leafdata())
                if (self.cdtppppeerdefipaddropts.is_set or self.cdtppppeerdefipaddropts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtppppeerdefipaddropts.get_name_leafdata())
                if (self.cdtppppeerdefipaddrsrc.is_set or self.cdtppppeerdefipaddrsrc.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtppppeerdefipaddrsrc.get_name_leafdata())
                if (self.cdtppptimeoutauthentication.is_set or self.cdtppptimeoutauthentication.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtppptimeoutauthentication.get_name_leafdata())
                if (self.cdtppptimeoutretry.is_set or self.cdtppptimeoutretry.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtppptimeoutretry.get_name_leafdata())
                if (self.cdtpppvalid.is_set or self.cdtpppvalid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtpppvalid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cdtTemplateName" or name == "cdtPppAccounting" or name == "cdtPppAuthentication" or name == "cdtPppAuthenticationMethods" or name == "cdtPppAuthorization" or name == "cdtPppChapHostname" or name == "cdtPppChapOpts" or name == "cdtPppChapPassword" or name == "cdtPppEapIdentity" or name == "cdtPppEapOpts" or name == "cdtPppEapPassword" or name == "cdtPppIpcpAddrOption" or name == "cdtPppIpcpDnsOption" or name == "cdtPppIpcpDnsPrimary" or name == "cdtPppIpcpDnsSecondary" or name == "cdtPppIpcpMask" or name == "cdtPppIpcpMaskOption" or name == "cdtPppIpcpWinsOption" or name == "cdtPppIpcpWinsPrimary" or name == "cdtPppIpcpWinsSecondary" or name == "cdtPppLoopbackIgnore" or name == "cdtPppMaxBadAuth" or name == "cdtPppMaxConfigure" or name == "cdtPppMaxFailure" or name == "cdtPppMaxTerminate" or name == "cdtPppMsChapV1Hostname" or name == "cdtPppMsChapV1Opts" or name == "cdtPppMsChapV1Password" or name == "cdtPppMsChapV2Hostname" or name == "cdtPppMsChapV2Opts" or name == "cdtPppMsChapV2Password" or name == "cdtPppPapOpts" or name == "cdtPppPapPassword" or name == "cdtPppPapUsername" or name == "cdtPppPeerDefIpAddr" or name == "cdtPppPeerDefIpAddrOpts" or name == "cdtPppPeerDefIpAddrSrc" or name == "cdtPppTimeoutAuthentication" or name == "cdtPppTimeoutRetry" or name == "cdtPppValid"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cdtTemplateName"):
                    self.cdttemplatename = value
                    self.cdttemplatename.value_namespace = name_space
                    self.cdttemplatename.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppAccounting"):
                    self.cdtpppaccounting = value
                    self.cdtpppaccounting.value_namespace = name_space
                    self.cdtpppaccounting.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppAuthentication"):
                    self.cdtpppauthentication[value] = True
                if(value_path == "cdtPppAuthenticationMethods"):
                    self.cdtpppauthenticationmethods = value
                    self.cdtpppauthenticationmethods.value_namespace = name_space
                    self.cdtpppauthenticationmethods.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppAuthorization"):
                    self.cdtpppauthorization = value
                    self.cdtpppauthorization.value_namespace = name_space
                    self.cdtpppauthorization.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppChapHostname"):
                    self.cdtpppchaphostname = value
                    self.cdtpppchaphostname.value_namespace = name_space
                    self.cdtpppchaphostname.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppChapOpts"):
                    self.cdtpppchapopts[value] = True
                if(value_path == "cdtPppChapPassword"):
                    self.cdtpppchappassword = value
                    self.cdtpppchappassword.value_namespace = name_space
                    self.cdtpppchappassword.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppEapIdentity"):
                    self.cdtpppeapidentity = value
                    self.cdtpppeapidentity.value_namespace = name_space
                    self.cdtpppeapidentity.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppEapOpts"):
                    self.cdtpppeapopts[value] = True
                if(value_path == "cdtPppEapPassword"):
                    self.cdtpppeappassword = value
                    self.cdtpppeappassword.value_namespace = name_space
                    self.cdtpppeappassword.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppIpcpAddrOption"):
                    self.cdtpppipcpaddroption = value
                    self.cdtpppipcpaddroption.value_namespace = name_space
                    self.cdtpppipcpaddroption.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppIpcpDnsOption"):
                    self.cdtpppipcpdnsoption = value
                    self.cdtpppipcpdnsoption.value_namespace = name_space
                    self.cdtpppipcpdnsoption.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppIpcpDnsPrimary"):
                    self.cdtpppipcpdnsprimary = value
                    self.cdtpppipcpdnsprimary.value_namespace = name_space
                    self.cdtpppipcpdnsprimary.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppIpcpDnsSecondary"):
                    self.cdtpppipcpdnssecondary = value
                    self.cdtpppipcpdnssecondary.value_namespace = name_space
                    self.cdtpppipcpdnssecondary.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppIpcpMask"):
                    self.cdtpppipcpmask = value
                    self.cdtpppipcpmask.value_namespace = name_space
                    self.cdtpppipcpmask.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppIpcpMaskOption"):
                    self.cdtpppipcpmaskoption = value
                    self.cdtpppipcpmaskoption.value_namespace = name_space
                    self.cdtpppipcpmaskoption.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppIpcpWinsOption"):
                    self.cdtpppipcpwinsoption = value
                    self.cdtpppipcpwinsoption.value_namespace = name_space
                    self.cdtpppipcpwinsoption.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppIpcpWinsPrimary"):
                    self.cdtpppipcpwinsprimary = value
                    self.cdtpppipcpwinsprimary.value_namespace = name_space
                    self.cdtpppipcpwinsprimary.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppIpcpWinsSecondary"):
                    self.cdtpppipcpwinssecondary = value
                    self.cdtpppipcpwinssecondary.value_namespace = name_space
                    self.cdtpppipcpwinssecondary.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppLoopbackIgnore"):
                    self.cdtppploopbackignore = value
                    self.cdtppploopbackignore.value_namespace = name_space
                    self.cdtppploopbackignore.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppMaxBadAuth"):
                    self.cdtpppmaxbadauth = value
                    self.cdtpppmaxbadauth.value_namespace = name_space
                    self.cdtpppmaxbadauth.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppMaxConfigure"):
                    self.cdtpppmaxconfigure = value
                    self.cdtpppmaxconfigure.value_namespace = name_space
                    self.cdtpppmaxconfigure.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppMaxFailure"):
                    self.cdtpppmaxfailure = value
                    self.cdtpppmaxfailure.value_namespace = name_space
                    self.cdtpppmaxfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppMaxTerminate"):
                    self.cdtpppmaxterminate = value
                    self.cdtpppmaxterminate.value_namespace = name_space
                    self.cdtpppmaxterminate.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppMsChapV1Hostname"):
                    self.cdtpppmschapv1hostname = value
                    self.cdtpppmschapv1hostname.value_namespace = name_space
                    self.cdtpppmschapv1hostname.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppMsChapV1Opts"):
                    self.cdtpppmschapv1opts[value] = True
                if(value_path == "cdtPppMsChapV1Password"):
                    self.cdtpppmschapv1password = value
                    self.cdtpppmschapv1password.value_namespace = name_space
                    self.cdtpppmschapv1password.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppMsChapV2Hostname"):
                    self.cdtpppmschapv2hostname = value
                    self.cdtpppmschapv2hostname.value_namespace = name_space
                    self.cdtpppmschapv2hostname.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppMsChapV2Opts"):
                    self.cdtpppmschapv2opts[value] = True
                if(value_path == "cdtPppMsChapV2Password"):
                    self.cdtpppmschapv2password = value
                    self.cdtpppmschapv2password.value_namespace = name_space
                    self.cdtpppmschapv2password.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppPapOpts"):
                    self.cdtppppapopts[value] = True
                if(value_path == "cdtPppPapPassword"):
                    self.cdtppppappassword = value
                    self.cdtppppappassword.value_namespace = name_space
                    self.cdtppppappassword.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppPapUsername"):
                    self.cdtppppapusername = value
                    self.cdtppppapusername.value_namespace = name_space
                    self.cdtppppapusername.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppPeerDefIpAddr"):
                    self.cdtppppeerdefipaddr = value
                    self.cdtppppeerdefipaddr.value_namespace = name_space
                    self.cdtppppeerdefipaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppPeerDefIpAddrOpts"):
                    self.cdtppppeerdefipaddropts[value] = True
                if(value_path == "cdtPppPeerDefIpAddrSrc"):
                    self.cdtppppeerdefipaddrsrc = value
                    self.cdtppppeerdefipaddrsrc.value_namespace = name_space
                    self.cdtppppeerdefipaddrsrc.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppTimeoutAuthentication"):
                    self.cdtppptimeoutauthentication = value
                    self.cdtppptimeoutauthentication.value_namespace = name_space
                    self.cdtppptimeoutauthentication.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppTimeoutRetry"):
                    self.cdtppptimeoutretry = value
                    self.cdtppptimeoutretry.value_namespace = name_space
                    self.cdtppptimeoutretry.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppValid"):
                    self.cdtpppvalid[value] = True

        def has_data(self):
            for c in self.cdtppptemplateentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cdtppptemplateentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cdtPppTemplateTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cdtPppTemplateEntry"):
                for c in self.cdtppptemplateentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cdtppptemplateentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cdtPppTemplateEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cdtppppeeripaddrpooltable(Entity):
        """
        This table contains a prioritized list of named pools for each
        PPP template.  A list corresponding to a PPP template
        specifies the pools the system searches in an attempt to
        assign an IP address to the peer of a target PPP connection.
        The system searches the pools in the order of their priority.
        
        This table has an expansion dependent relationship on the
        cdtPppTemplateTable, containing zero or more rows for each PPP
        template.
        
        .. attribute:: cdtppppeeripaddrpoolentry
        
        	An entry specifies a named pool in a list of pools associated with a PPP template.  A PPP template can only have named pools associated with it if it has a cdtPppPeerIpAddrSrc of 'pool'.  Any attempt to create an entry for a PPP template that does not have a cdtPppPeerIpAddrSrc of 'pool' must result in a response having an error\-status of 'inconsistentValue'.  The system automatically creates a corresponding entry when the system associates a named pool with a PPP template through another management entity (e.g., the system's local console).  The system automatically destroys an entry under the following circumstances\:  1)  The system or EMS/NMS destroys the corresponding row in the     cdtTemplateTable.  2)  The system or EMS/NMS sets the corresponding instance of     cdtPppPeerIpAddrSrc with a value other than 'pool'
        	**type**\: list of    :py:class:`Cdtppppeeripaddrpoolentry <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtppppeeripaddrpooltable.Cdtppppeeripaddrpoolentry>`
        
        

        """

        _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
        _revision = '2007-09-06'

        def __init__(self):
            super(CiscoDynamicTemplateMib.Cdtppppeeripaddrpooltable, self).__init__()

            self.yang_name = "cdtPppPeerIpAddrPoolTable"
            self.yang_parent_name = "CISCO-DYNAMIC-TEMPLATE-MIB"

            self.cdtppppeeripaddrpoolentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoDynamicTemplateMib.Cdtppppeeripaddrpooltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoDynamicTemplateMib.Cdtppppeeripaddrpooltable, self).__setattr__(name, value)


        class Cdtppppeeripaddrpoolentry(Entity):
            """
            An entry specifies a named pool in a list of pools associated
            with a PPP template.  A PPP template can only have named
            pools associated with it if it has a cdtPppPeerIpAddrSrc of
            'pool'.
            
            Any attempt to create an entry for a PPP template that does not
            have a cdtPppPeerIpAddrSrc of 'pool' must result in a response
            having an error\-status of 'inconsistentValue'.
            
            The system automatically creates a corresponding entry when the
            system associates a named pool with a PPP template through
            another management entity (e.g., the system's local console).
            
            The system automatically destroys an entry under the following
            circumstances\:
            
            1)  The system or EMS/NMS destroys the corresponding row in the
                cdtTemplateTable.
            
            2)  The system or EMS/NMS sets the corresponding instance of
                cdtPppPeerIpAddrSrc with a value other than 'pool'.
            
            .. attribute:: cdttemplatename  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..64
            
            	**refers to**\:  :py:class:`cdttemplatename <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdttemplatetable.Cdttemplateentry>`
            
            .. attribute:: cdtppppeeripaddrpoolpriority  <key>
            
            	This object indicates the relative priority of the named pool in the list corresponding to a PPP template.  The system searches pools in the order of priority, where lower values represent higher priority
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: cdtppppeeripaddrpoolname
            
            	This object specifies the name of the IP address pool associated with the PPP template
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cdtppppeeripaddrpoolstatus
            
            	This object specifies the status of the entry.  The following columns must be valid before activating a subscriber access profile\:      \- cdtPppPeerIpAddrPoolStorage     \- cdtPppPeerIpAddrPoolName  However, these objects specify a default value.  Thus, it is possible to use create\-and\-go semantics without setting any additional columns.  An implementation must not allow the EMS/NMS to create an entry if the corresponding instance of cdtPppPeerIpAddrSrc is not 'pool'.  An implementation must allow the EMS/NMS to modify any column when this column is 'active'
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cdtppppeeripaddrpoolstorage
            
            	This object specifies what happens to the name pool entry upon restart.  If the corresponding instance of cdtTemplateSrc is not 'local', then this column must be 'volatile'
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
            _revision = '2007-09-06'

            def __init__(self):
                super(CiscoDynamicTemplateMib.Cdtppppeeripaddrpooltable.Cdtppppeeripaddrpoolentry, self).__init__()

                self.yang_name = "cdtPppPeerIpAddrPoolEntry"
                self.yang_parent_name = "cdtPppPeerIpAddrPoolTable"

                self.cdttemplatename = YLeaf(YType.str, "cdtTemplateName")

                self.cdtppppeeripaddrpoolpriority = YLeaf(YType.uint32, "cdtPppPeerIpAddrPoolPriority")

                self.cdtppppeeripaddrpoolname = YLeaf(YType.str, "cdtPppPeerIpAddrPoolName")

                self.cdtppppeeripaddrpoolstatus = YLeaf(YType.enumeration, "cdtPppPeerIpAddrPoolStatus")

                self.cdtppppeeripaddrpoolstorage = YLeaf(YType.enumeration, "cdtPppPeerIpAddrPoolStorage")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cdttemplatename",
                                "cdtppppeeripaddrpoolpriority",
                                "cdtppppeeripaddrpoolname",
                                "cdtppppeeripaddrpoolstatus",
                                "cdtppppeeripaddrpoolstorage") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoDynamicTemplateMib.Cdtppppeeripaddrpooltable.Cdtppppeeripaddrpoolentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoDynamicTemplateMib.Cdtppppeeripaddrpooltable.Cdtppppeeripaddrpoolentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cdttemplatename.is_set or
                    self.cdtppppeeripaddrpoolpriority.is_set or
                    self.cdtppppeeripaddrpoolname.is_set or
                    self.cdtppppeeripaddrpoolstatus.is_set or
                    self.cdtppppeeripaddrpoolstorage.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cdttemplatename.yfilter != YFilter.not_set or
                    self.cdtppppeeripaddrpoolpriority.yfilter != YFilter.not_set or
                    self.cdtppppeeripaddrpoolname.yfilter != YFilter.not_set or
                    self.cdtppppeeripaddrpoolstatus.yfilter != YFilter.not_set or
                    self.cdtppppeeripaddrpoolstorage.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cdtPppPeerIpAddrPoolEntry" + "[cdtTemplateName='" + self.cdttemplatename.get() + "']" + "[cdtPppPeerIpAddrPoolPriority='" + self.cdtppppeeripaddrpoolpriority.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/cdtPppPeerIpAddrPoolTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cdttemplatename.is_set or self.cdttemplatename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdttemplatename.get_name_leafdata())
                if (self.cdtppppeeripaddrpoolpriority.is_set or self.cdtppppeeripaddrpoolpriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtppppeeripaddrpoolpriority.get_name_leafdata())
                if (self.cdtppppeeripaddrpoolname.is_set or self.cdtppppeeripaddrpoolname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtppppeeripaddrpoolname.get_name_leafdata())
                if (self.cdtppppeeripaddrpoolstatus.is_set or self.cdtppppeeripaddrpoolstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtppppeeripaddrpoolstatus.get_name_leafdata())
                if (self.cdtppppeeripaddrpoolstorage.is_set or self.cdtppppeeripaddrpoolstorage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtppppeeripaddrpoolstorage.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cdtTemplateName" or name == "cdtPppPeerIpAddrPoolPriority" or name == "cdtPppPeerIpAddrPoolName" or name == "cdtPppPeerIpAddrPoolStatus" or name == "cdtPppPeerIpAddrPoolStorage"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cdtTemplateName"):
                    self.cdttemplatename = value
                    self.cdttemplatename.value_namespace = name_space
                    self.cdttemplatename.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppPeerIpAddrPoolPriority"):
                    self.cdtppppeeripaddrpoolpriority = value
                    self.cdtppppeeripaddrpoolpriority.value_namespace = name_space
                    self.cdtppppeeripaddrpoolpriority.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppPeerIpAddrPoolName"):
                    self.cdtppppeeripaddrpoolname = value
                    self.cdtppppeeripaddrpoolname.value_namespace = name_space
                    self.cdtppppeeripaddrpoolname.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppPeerIpAddrPoolStatus"):
                    self.cdtppppeeripaddrpoolstatus = value
                    self.cdtppppeeripaddrpoolstatus.value_namespace = name_space
                    self.cdtppppeeripaddrpoolstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtPppPeerIpAddrPoolStorage"):
                    self.cdtppppeeripaddrpoolstorage = value
                    self.cdtppppeeripaddrpoolstorage.value_namespace = name_space
                    self.cdtppppeeripaddrpoolstorage.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cdtppppeeripaddrpoolentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cdtppppeeripaddrpoolentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cdtPppPeerIpAddrPoolTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cdtPppPeerIpAddrPoolEntry"):
                for c in self.cdtppppeeripaddrpoolentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoDynamicTemplateMib.Cdtppppeeripaddrpooltable.Cdtppppeeripaddrpoolentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cdtppppeeripaddrpoolentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cdtPppPeerIpAddrPoolEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cdtethernettemplatetable(Entity):
        """
        This table contains attributes relating to dynamic interfaces
        initiated on Ethernet virtual interfaces (e.g., EoMPLS) or
        automatically created VLANs.
        
        This table has a sparse\-dependent relationship on the
        cdtTemplateTable, containing a row for each dynamic template
        having a cdtTemplateType of one of the following values\:
        
            'derived'
            'ethernet'
        
        .. attribute:: cdtethernettemplateentry
        
        	An entry containing attributes relating to dynamic interfaces initiated on Ethernet virtual interfaces (e.g., EoMPLS) or automatically created VLANs.  The system automatically creates an entry when the system or the EMS/NMS creates a row in the cdtTemplateTable with a cdtTemplateType of one of the following values\:      'derived'     'ethernet'  Likewise, the system automatically destroys an entry when the system or the EMS/NMS destroys the corresponding row in the cdtTemplateTable
        	**type**\: list of    :py:class:`Cdtethernettemplateentry <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtethernettemplatetable.Cdtethernettemplateentry>`
        
        

        """

        _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
        _revision = '2007-09-06'

        def __init__(self):
            super(CiscoDynamicTemplateMib.Cdtethernettemplatetable, self).__init__()

            self.yang_name = "cdtEthernetTemplateTable"
            self.yang_parent_name = "CISCO-DYNAMIC-TEMPLATE-MIB"

            self.cdtethernettemplateentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoDynamicTemplateMib.Cdtethernettemplatetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoDynamicTemplateMib.Cdtethernettemplatetable, self).__setattr__(name, value)


        class Cdtethernettemplateentry(Entity):
            """
            An entry containing attributes relating to dynamic interfaces
            initiated on Ethernet virtual interfaces (e.g., EoMPLS) or
            automatically created VLANs.
            
            The system automatically creates an entry when the system or the
            EMS/NMS creates a row in the cdtTemplateTable with a
            cdtTemplateType of one of the following values\:
            
                'derived'
                'ethernet'
            
            Likewise, the system automatically destroys an entry when the
            system or the EMS/NMS destroys the corresponding row in the
            cdtTemplateTable.
            
            .. attribute:: cdttemplatename  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..64
            
            	**refers to**\:  :py:class:`cdttemplatename <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdttemplatetable.Cdttemplateentry>`
            
            .. attribute:: cdtethernetbridgedomain
            
            	This object specifies the name of the bridge domain..
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cdtethernetipv4pointtopoint
            
            	This object specifies whether..
            	**type**\:  bool
            
            .. attribute:: cdtethernetmacaddr
            
            	This object specifies the..
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: cdtethernetpppoeenable
            
            	This object specifies whether..
            	**type**\:  bool
            
            .. attribute:: cdtethernetvalid
            
            	This object specifies which attributes in the dynamic template have been configured to valid values.  Each bit in this bit string corresponds to a column in this table.  If the bit is '0', then the value of the corresponding column is not valid.  If the bit is '1', then the value of the corresponding column has been configured to a valid value.  The following list specifies the mappings between bits and the columns\:      bridgeDomain     => cdtEthernetBridgeDomain     pppoeEnable      => cdtEthernetPppoeEnable     ipv4PointToPoint => cdtEthernetIpv4PointToPoint     macAddr          => cdtEthernetMacAddr
            	**type**\:   :py:class:`Cdtethernetvalid <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtethernettemplatetable.Cdtethernettemplateentry.Cdtethernetvalid>`
            
            

            """

            _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
            _revision = '2007-09-06'

            def __init__(self):
                super(CiscoDynamicTemplateMib.Cdtethernettemplatetable.Cdtethernettemplateentry, self).__init__()

                self.yang_name = "cdtEthernetTemplateEntry"
                self.yang_parent_name = "cdtEthernetTemplateTable"

                self.cdttemplatename = YLeaf(YType.str, "cdtTemplateName")

                self.cdtethernetbridgedomain = YLeaf(YType.str, "cdtEthernetBridgeDomain")

                self.cdtethernetipv4pointtopoint = YLeaf(YType.boolean, "cdtEthernetIpv4PointToPoint")

                self.cdtethernetmacaddr = YLeaf(YType.str, "cdtEthernetMacAddr")

                self.cdtethernetpppoeenable = YLeaf(YType.boolean, "cdtEthernetPppoeEnable")

                self.cdtethernetvalid = YLeaf(YType.bits, "cdtEthernetValid")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cdttemplatename",
                                "cdtethernetbridgedomain",
                                "cdtethernetipv4pointtopoint",
                                "cdtethernetmacaddr",
                                "cdtethernetpppoeenable",
                                "cdtethernetvalid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoDynamicTemplateMib.Cdtethernettemplatetable.Cdtethernettemplateentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoDynamicTemplateMib.Cdtethernettemplatetable.Cdtethernettemplateentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cdttemplatename.is_set or
                    self.cdtethernetbridgedomain.is_set or
                    self.cdtethernetipv4pointtopoint.is_set or
                    self.cdtethernetmacaddr.is_set or
                    self.cdtethernetpppoeenable.is_set or
                    self.cdtethernetvalid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cdttemplatename.yfilter != YFilter.not_set or
                    self.cdtethernetbridgedomain.yfilter != YFilter.not_set or
                    self.cdtethernetipv4pointtopoint.yfilter != YFilter.not_set or
                    self.cdtethernetmacaddr.yfilter != YFilter.not_set or
                    self.cdtethernetpppoeenable.yfilter != YFilter.not_set or
                    self.cdtethernetvalid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cdtEthernetTemplateEntry" + "[cdtTemplateName='" + self.cdttemplatename.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/cdtEthernetTemplateTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cdttemplatename.is_set or self.cdttemplatename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdttemplatename.get_name_leafdata())
                if (self.cdtethernetbridgedomain.is_set or self.cdtethernetbridgedomain.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtethernetbridgedomain.get_name_leafdata())
                if (self.cdtethernetipv4pointtopoint.is_set or self.cdtethernetipv4pointtopoint.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtethernetipv4pointtopoint.get_name_leafdata())
                if (self.cdtethernetmacaddr.is_set or self.cdtethernetmacaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtethernetmacaddr.get_name_leafdata())
                if (self.cdtethernetpppoeenable.is_set or self.cdtethernetpppoeenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtethernetpppoeenable.get_name_leafdata())
                if (self.cdtethernetvalid.is_set or self.cdtethernetvalid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtethernetvalid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cdtTemplateName" or name == "cdtEthernetBridgeDomain" or name == "cdtEthernetIpv4PointToPoint" or name == "cdtEthernetMacAddr" or name == "cdtEthernetPppoeEnable" or name == "cdtEthernetValid"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cdtTemplateName"):
                    self.cdttemplatename = value
                    self.cdttemplatename.value_namespace = name_space
                    self.cdttemplatename.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtEthernetBridgeDomain"):
                    self.cdtethernetbridgedomain = value
                    self.cdtethernetbridgedomain.value_namespace = name_space
                    self.cdtethernetbridgedomain.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtEthernetIpv4PointToPoint"):
                    self.cdtethernetipv4pointtopoint = value
                    self.cdtethernetipv4pointtopoint.value_namespace = name_space
                    self.cdtethernetipv4pointtopoint.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtEthernetMacAddr"):
                    self.cdtethernetmacaddr = value
                    self.cdtethernetmacaddr.value_namespace = name_space
                    self.cdtethernetmacaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtEthernetPppoeEnable"):
                    self.cdtethernetpppoeenable = value
                    self.cdtethernetpppoeenable.value_namespace = name_space
                    self.cdtethernetpppoeenable.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtEthernetValid"):
                    self.cdtethernetvalid[value] = True

        def has_data(self):
            for c in self.cdtethernettemplateentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cdtethernettemplateentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cdtEthernetTemplateTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cdtEthernetTemplateEntry"):
                for c in self.cdtethernettemplateentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoDynamicTemplateMib.Cdtethernettemplatetable.Cdtethernettemplateentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cdtethernettemplateentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cdtEthernetTemplateEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cdtsrvtemplatetable(Entity):
        """
        This table contains attributes relating to a service.
        
        This table has a sparse\-dependent relationship on the
        cdtTemplateTable, containing a row for each dynamic template
        having a cdtTemplateType of one of the following values\:
        
            'derived'
            'service'
        
        .. attribute:: cdtsrvtemplateentry
        
        	An entry containing attributes relating to a service.  The system automatically creates entry when the system or the EMS/NMS creates a row in the cdtTemplateTable with a cdtTemplateType of one of the following values\:      'derived'     'service'  Likewise, the system automatically destroys an entry when the system or the EMS/NMS destroys the corresponding row in the cdtTemplateTable
        	**type**\: list of    :py:class:`Cdtsrvtemplateentry <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtsrvtemplatetable.Cdtsrvtemplateentry>`
        
        

        """

        _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
        _revision = '2007-09-06'

        def __init__(self):
            super(CiscoDynamicTemplateMib.Cdtsrvtemplatetable, self).__init__()

            self.yang_name = "cdtSrvTemplateTable"
            self.yang_parent_name = "CISCO-DYNAMIC-TEMPLATE-MIB"

            self.cdtsrvtemplateentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoDynamicTemplateMib.Cdtsrvtemplatetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoDynamicTemplateMib.Cdtsrvtemplatetable, self).__setattr__(name, value)


        class Cdtsrvtemplateentry(Entity):
            """
            An entry containing attributes relating to a service.
            
            The system automatically creates entry when the system or the
            EMS/NMS creates a row in the cdtTemplateTable with a
            cdtTemplateType of one of the following values\:
            
                'derived'
                'service'
            
            Likewise, the system automatically destroys an entry when the
            system or the EMS/NMS destroys the corresponding row in the
            cdtTemplateTable.
            
            .. attribute:: cdttemplatename  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..64
            
            	**refers to**\:  :py:class:`cdttemplatename <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdttemplatetable.Cdttemplateentry>`
            
            .. attribute:: cdtsrvmulticast
            
            	This objects specifies whether the system enables multicast service for subscriber sessions of the target service.  This column is valid only if the 'sgSrvMcastRoutingIf' bit of the corresponding instance of cdtSrvValid is '1'
            	**type**\:  bool
            
            .. attribute:: cdtsrvnetworksrv
            
            	This object specifies the type of network service provided by the target service\:      'other'         The implementation of this MIB module does not recognize         the configured network service.      'none'         The target subscriber service does not provide a network         service to subscribers sessions.      'local'         The target subscriber service provides local termination         for subscriber sessions.      'vpdn'         The target subscriber service provides a Virtual Private         Dialup Network service for subscriber sessions.  This column is valid only if the 'networkSrv' bit of the corresponding instance of cdtSrvValid is '1'
            	**type**\:   :py:class:`Cdtsrvnetworksrv <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtsrvtemplatetable.Cdtsrvtemplateentry.Cdtsrvnetworksrv>`
            
            .. attribute:: cdtsrvsgsrvgroup
            
            	This object specifies the name of the service group with which the system associates subscriber sessions.  A service group specifies a set of services that may be active simultaneously for a given subscriber session.  Typically, a service group contains a primary service and one or more secondary services.  This column is valid only if the 'sgSrvGroup' bit of the corresponding instance of cdtSrvValid is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cdtsrvsgsrvtype
            
            	This object specifies whether the target service specifies a network\-forwarding policy\:      'primary'         The target service specifies a network\-forwarding         policy.  Primary services are mutually exclusive; that         is, only one primary service can be activated for any         given subscriber session.      'secondary'         The target service has a dependence on the primary         service in the group specified by the corresponding         instance of cdtSuBSrvSgSrvGroup.  After the system         activates the primary service, it activates secondary         services.  When the system deactivates the primary         service, then it deactivates all the secondary services         in the service group.  This column is valid only if the 'sgSrvType' bit of the corresponding instance of cdtSrvValid is '1'
            	**type**\:   :py:class:`Cdtsrvsgsrvtype <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtsrvtemplatetable.Cdtsrvtemplateentry.Cdtsrvsgsrvtype>`
            
            .. attribute:: cdtsrvvalid
            
            	This object specifies which attributes in the dynamic template have been configured to valid values.  Each bit in this bit string corresponds to a column in this table.  If the bit is '0', then the value of the corresponding column is not valid.  If the bit is '1', then the value of the corresponding column has been configured to a valid value.  The following list specifies the mappings between bits and the columns\:      networkSrv     => cdtSrvNetworkSrv     vpdnGroup      => cdtSrvVpdnGroup     sgSrvGroup     => cdtSrvGroup     sgSrvType      => cdtSrvSgSrvType     multicast      => cdtSrvMulticast
            	**type**\:   :py:class:`Cdtsrvvalid <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtsrvtemplatetable.Cdtsrvtemplateentry.Cdtsrvvalid>`
            
            .. attribute:: cdtsrvvpdngroup
            
            	This object specifies the name of the VPDN group used to configure the network service.  This column is valid only if the 'vpdnGroup' bit of the corresponding instance of cdtSrvValid is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
            _revision = '2007-09-06'

            def __init__(self):
                super(CiscoDynamicTemplateMib.Cdtsrvtemplatetable.Cdtsrvtemplateentry, self).__init__()

                self.yang_name = "cdtSrvTemplateEntry"
                self.yang_parent_name = "cdtSrvTemplateTable"

                self.cdttemplatename = YLeaf(YType.str, "cdtTemplateName")

                self.cdtsrvmulticast = YLeaf(YType.boolean, "cdtSrvMulticast")

                self.cdtsrvnetworksrv = YLeaf(YType.enumeration, "cdtSrvNetworkSrv")

                self.cdtsrvsgsrvgroup = YLeaf(YType.str, "cdtSrvSgSrvGroup")

                self.cdtsrvsgsrvtype = YLeaf(YType.enumeration, "cdtSrvSgSrvType")

                self.cdtsrvvalid = YLeaf(YType.bits, "cdtSrvValid")

                self.cdtsrvvpdngroup = YLeaf(YType.str, "cdtSrvVpdnGroup")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cdttemplatename",
                                "cdtsrvmulticast",
                                "cdtsrvnetworksrv",
                                "cdtsrvsgsrvgroup",
                                "cdtsrvsgsrvtype",
                                "cdtsrvvalid",
                                "cdtsrvvpdngroup") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoDynamicTemplateMib.Cdtsrvtemplatetable.Cdtsrvtemplateentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoDynamicTemplateMib.Cdtsrvtemplatetable.Cdtsrvtemplateentry, self).__setattr__(name, value)

            class Cdtsrvnetworksrv(Enum):
                """
                Cdtsrvnetworksrv

                This object specifies the type of network service provided by

                the target service\:

                    'other'

                        The implementation of this MIB module does not recognize

                        the configured network service.

                    'none'

                        The target subscriber service does not provide a network

                        service to subscribers sessions.

                    'local'

                        The target subscriber service provides local termination

                        for subscriber sessions.

                    'vpdn'

                        The target subscriber service provides a Virtual Private

                        Dialup Network service for subscriber sessions.

                This column is valid only if the 'networkSrv' bit of the

                corresponding instance of cdtSrvValid is '1'.

                .. data:: other = 1

                .. data:: none = 2

                .. data:: local = 3

                .. data:: vpdn = 4

                """

                other = Enum.YLeaf(1, "other")

                none = Enum.YLeaf(2, "none")

                local = Enum.YLeaf(3, "local")

                vpdn = Enum.YLeaf(4, "vpdn")


            class Cdtsrvsgsrvtype(Enum):
                """
                Cdtsrvsgsrvtype

                This object specifies whether the target service specifies a

                network\-forwarding policy\:

                    'primary'

                        The target service specifies a network\-forwarding

                        policy.  Primary services are mutually exclusive; that

                        is, only one primary service can be activated for any

                        given subscriber session.

                    'secondary'

                        The target service has a dependence on the primary

                        service in the group specified by the corresponding

                        instance of cdtSuBSrvSgSrvGroup.  After the system

                        activates the primary service, it activates secondary

                        services.  When the system deactivates the primary

                        service, then it deactivates all the secondary services

                        in the service group.

                This column is valid only if the 'sgSrvType' bit of the

                corresponding instance of cdtSrvValid is '1'.

                .. data:: primary = 1

                .. data:: secondary = 2

                """

                primary = Enum.YLeaf(1, "primary")

                secondary = Enum.YLeaf(2, "secondary")


            def has_data(self):
                return (
                    self.cdttemplatename.is_set or
                    self.cdtsrvmulticast.is_set or
                    self.cdtsrvnetworksrv.is_set or
                    self.cdtsrvsgsrvgroup.is_set or
                    self.cdtsrvsgsrvtype.is_set or
                    self.cdtsrvvalid.is_set or
                    self.cdtsrvvpdngroup.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cdttemplatename.yfilter != YFilter.not_set or
                    self.cdtsrvmulticast.yfilter != YFilter.not_set or
                    self.cdtsrvnetworksrv.yfilter != YFilter.not_set or
                    self.cdtsrvsgsrvgroup.yfilter != YFilter.not_set or
                    self.cdtsrvsgsrvtype.yfilter != YFilter.not_set or
                    self.cdtsrvvalid.yfilter != YFilter.not_set or
                    self.cdtsrvvpdngroup.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cdtSrvTemplateEntry" + "[cdtTemplateName='" + self.cdttemplatename.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/cdtSrvTemplateTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cdttemplatename.is_set or self.cdttemplatename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdttemplatename.get_name_leafdata())
                if (self.cdtsrvmulticast.is_set or self.cdtsrvmulticast.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtsrvmulticast.get_name_leafdata())
                if (self.cdtsrvnetworksrv.is_set or self.cdtsrvnetworksrv.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtsrvnetworksrv.get_name_leafdata())
                if (self.cdtsrvsgsrvgroup.is_set or self.cdtsrvsgsrvgroup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtsrvsgsrvgroup.get_name_leafdata())
                if (self.cdtsrvsgsrvtype.is_set or self.cdtsrvsgsrvtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtsrvsgsrvtype.get_name_leafdata())
                if (self.cdtsrvvalid.is_set or self.cdtsrvvalid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtsrvvalid.get_name_leafdata())
                if (self.cdtsrvvpdngroup.is_set or self.cdtsrvvpdngroup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdtsrvvpdngroup.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cdtTemplateName" or name == "cdtSrvMulticast" or name == "cdtSrvNetworkSrv" or name == "cdtSrvSgSrvGroup" or name == "cdtSrvSgSrvType" or name == "cdtSrvValid" or name == "cdtSrvVpdnGroup"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cdtTemplateName"):
                    self.cdttemplatename = value
                    self.cdttemplatename.value_namespace = name_space
                    self.cdttemplatename.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtSrvMulticast"):
                    self.cdtsrvmulticast = value
                    self.cdtsrvmulticast.value_namespace = name_space
                    self.cdtsrvmulticast.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtSrvNetworkSrv"):
                    self.cdtsrvnetworksrv = value
                    self.cdtsrvnetworksrv.value_namespace = name_space
                    self.cdtsrvnetworksrv.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtSrvSgSrvGroup"):
                    self.cdtsrvsgsrvgroup = value
                    self.cdtsrvsgsrvgroup.value_namespace = name_space
                    self.cdtsrvsgsrvgroup.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtSrvSgSrvType"):
                    self.cdtsrvsgsrvtype = value
                    self.cdtsrvsgsrvtype.value_namespace = name_space
                    self.cdtsrvsgsrvtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cdtSrvValid"):
                    self.cdtsrvvalid[value] = True
                if(value_path == "cdtSrvVpdnGroup"):
                    self.cdtsrvvpdngroup = value
                    self.cdtsrvvpdngroup.value_namespace = name_space
                    self.cdtsrvvpdngroup.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cdtsrvtemplateentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cdtsrvtemplateentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cdtSrvTemplateTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cdtSrvTemplateEntry"):
                for c in self.cdtsrvtemplateentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoDynamicTemplateMib.Cdtsrvtemplatetable.Cdtsrvtemplateentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cdtsrvtemplateentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cdtSrvTemplateEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cdtethernettemplatetable is not None and self.cdtethernettemplatetable.has_data()) or
            (self.cdtiftemplatetable is not None and self.cdtiftemplatetable.has_data()) or
            (self.cdtppppeeripaddrpooltable is not None and self.cdtppppeeripaddrpooltable.has_data()) or
            (self.cdtppptemplatetable is not None and self.cdtppptemplatetable.has_data()) or
            (self.cdtsrvtemplatetable is not None and self.cdtsrvtemplatetable.has_data()) or
            (self.cdttemplateassociationtable is not None and self.cdttemplateassociationtable.has_data()) or
            (self.cdttemplatecommontable is not None and self.cdttemplatecommontable.has_data()) or
            (self.cdttemplatetable is not None and self.cdttemplatetable.has_data()) or
            (self.cdttemplatetargettable is not None and self.cdttemplatetargettable.has_data()) or
            (self.cdttemplateusagetable is not None and self.cdttemplateusagetable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cdtethernettemplatetable is not None and self.cdtethernettemplatetable.has_operation()) or
            (self.cdtiftemplatetable is not None and self.cdtiftemplatetable.has_operation()) or
            (self.cdtppppeeripaddrpooltable is not None and self.cdtppppeeripaddrpooltable.has_operation()) or
            (self.cdtppptemplatetable is not None and self.cdtppptemplatetable.has_operation()) or
            (self.cdtsrvtemplatetable is not None and self.cdtsrvtemplatetable.has_operation()) or
            (self.cdttemplateassociationtable is not None and self.cdttemplateassociationtable.has_operation()) or
            (self.cdttemplatecommontable is not None and self.cdttemplatecommontable.has_operation()) or
            (self.cdttemplatetable is not None and self.cdttemplatetable.has_operation()) or
            (self.cdttemplatetargettable is not None and self.cdttemplatetargettable.has_operation()) or
            (self.cdttemplateusagetable is not None and self.cdttemplateusagetable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "cdtEthernetTemplateTable"):
            if (self.cdtethernettemplatetable is None):
                self.cdtethernettemplatetable = CiscoDynamicTemplateMib.Cdtethernettemplatetable()
                self.cdtethernettemplatetable.parent = self
                self._children_name_map["cdtethernettemplatetable"] = "cdtEthernetTemplateTable"
            return self.cdtethernettemplatetable

        if (child_yang_name == "cdtIfTemplateTable"):
            if (self.cdtiftemplatetable is None):
                self.cdtiftemplatetable = CiscoDynamicTemplateMib.Cdtiftemplatetable()
                self.cdtiftemplatetable.parent = self
                self._children_name_map["cdtiftemplatetable"] = "cdtIfTemplateTable"
            return self.cdtiftemplatetable

        if (child_yang_name == "cdtPppPeerIpAddrPoolTable"):
            if (self.cdtppppeeripaddrpooltable is None):
                self.cdtppppeeripaddrpooltable = CiscoDynamicTemplateMib.Cdtppppeeripaddrpooltable()
                self.cdtppppeeripaddrpooltable.parent = self
                self._children_name_map["cdtppppeeripaddrpooltable"] = "cdtPppPeerIpAddrPoolTable"
            return self.cdtppppeeripaddrpooltable

        if (child_yang_name == "cdtPppTemplateTable"):
            if (self.cdtppptemplatetable is None):
                self.cdtppptemplatetable = CiscoDynamicTemplateMib.Cdtppptemplatetable()
                self.cdtppptemplatetable.parent = self
                self._children_name_map["cdtppptemplatetable"] = "cdtPppTemplateTable"
            return self.cdtppptemplatetable

        if (child_yang_name == "cdtSrvTemplateTable"):
            if (self.cdtsrvtemplatetable is None):
                self.cdtsrvtemplatetable = CiscoDynamicTemplateMib.Cdtsrvtemplatetable()
                self.cdtsrvtemplatetable.parent = self
                self._children_name_map["cdtsrvtemplatetable"] = "cdtSrvTemplateTable"
            return self.cdtsrvtemplatetable

        if (child_yang_name == "cdtTemplateAssociationTable"):
            if (self.cdttemplateassociationtable is None):
                self.cdttemplateassociationtable = CiscoDynamicTemplateMib.Cdttemplateassociationtable()
                self.cdttemplateassociationtable.parent = self
                self._children_name_map["cdttemplateassociationtable"] = "cdtTemplateAssociationTable"
            return self.cdttemplateassociationtable

        if (child_yang_name == "cdtTemplateCommonTable"):
            if (self.cdttemplatecommontable is None):
                self.cdttemplatecommontable = CiscoDynamicTemplateMib.Cdttemplatecommontable()
                self.cdttemplatecommontable.parent = self
                self._children_name_map["cdttemplatecommontable"] = "cdtTemplateCommonTable"
            return self.cdttemplatecommontable

        if (child_yang_name == "cdtTemplateTable"):
            if (self.cdttemplatetable is None):
                self.cdttemplatetable = CiscoDynamicTemplateMib.Cdttemplatetable()
                self.cdttemplatetable.parent = self
                self._children_name_map["cdttemplatetable"] = "cdtTemplateTable"
            return self.cdttemplatetable

        if (child_yang_name == "cdtTemplateTargetTable"):
            if (self.cdttemplatetargettable is None):
                self.cdttemplatetargettable = CiscoDynamicTemplateMib.Cdttemplatetargettable()
                self.cdttemplatetargettable.parent = self
                self._children_name_map["cdttemplatetargettable"] = "cdtTemplateTargetTable"
            return self.cdttemplatetargettable

        if (child_yang_name == "cdtTemplateUsageTable"):
            if (self.cdttemplateusagetable is None):
                self.cdttemplateusagetable = CiscoDynamicTemplateMib.Cdttemplateusagetable()
                self.cdttemplateusagetable.parent = self
                self._children_name_map["cdttemplateusagetable"] = "cdtTemplateUsageTable"
            return self.cdttemplateusagetable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cdtEthernetTemplateTable" or name == "cdtIfTemplateTable" or name == "cdtPppPeerIpAddrPoolTable" or name == "cdtPppTemplateTable" or name == "cdtSrvTemplateTable" or name == "cdtTemplateAssociationTable" or name == "cdtTemplateCommonTable" or name == "cdtTemplateTable" or name == "cdtTemplateTargetTable" or name == "cdtTemplateUsageTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoDynamicTemplateMib()
        return self._top_entity


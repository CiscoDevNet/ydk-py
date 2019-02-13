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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCODYNAMICTEMPLATEMIB(Entity):
    """
    
    
    .. attribute:: cdttemplatetable
    
    	This table lists the dynamic templates maintained by the system, including those that have been locally\-configured on the system and those pushed to the system by external policy servers
    	**type**\:  :py:class:`CdtTemplateTable <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateTable>`
    
    	**config**\: False
    
    .. attribute:: cdttemplatetargettable
    
    	This table contains a list of targets associated with one or more dynamic templates
    	**type**\:  :py:class:`CdtTemplateTargetTable <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateTargetTable>`
    
    	**config**\: False
    
    .. attribute:: cdttemplateassociationtable
    
    	This table contains a list of templates associated with each target.  This table has an expansion dependent relationship on the cdtTemplateTargetTable, containing zero or more rows for each target
    	**type**\:  :py:class:`CdtTemplateAssociationTable <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateAssociationTable>`
    
    	**config**\: False
    
    .. attribute:: cdttemplateusagetable
    
    	This table contains a list of targets using each dynamic template.  This table has an expansion dependent relationship on the cdtTemplateTable, containing zero or more rows for each dynamic template
    	**type**\:  :py:class:`CdtTemplateUsageTable <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateUsageTable>`
    
    	**config**\: False
    
    .. attribute:: cdttemplatecommontable
    
    	This table contains attributes relating to all dynamic templates.  Observe that the type of dynamic templates containing these attributes may change with the addition of new dynamic template types.  This table has a sparse\-dependent relationship on the cdtTemplateTable, containing a row for each dynamic template having a cdtTemplateType of one of the following values\:      'derived'     'ppp'     'ethernet'     'ipSubscriber'     'service'
    	**type**\:  :py:class:`CdtTemplateCommonTable <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateCommonTable>`
    
    	**config**\: False
    
    .. attribute:: cdtiftemplatetable
    
    	This table contains attributes relating to interface configuration.  This table has a sparse\-dependent relationship on the cdtTemplateTable, containing a row for each dynamic template having a cdtTemplateType of one of the following values\:      'derived'     'ppp'     'ethernet'     'ipSubscriber'
    	**type**\:  :py:class:`CdtIfTemplateTable <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable>`
    
    	**config**\: False
    
    .. attribute:: cdtppptemplatetable
    
    	This table contains attributes relating to PPP connection configuration.  This table has a sparse\-dependent relationship on the cdtTemplateTable, containing a row for each dynamic template having a cdtTemplateType of one of the following values\:      'derived'     'ppp'
    	**type**\:  :py:class:`CdtPppTemplateTable <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable>`
    
    	**config**\: False
    
    .. attribute:: cdtppppeeripaddrpooltable
    
    	This table contains a prioritized list of named pools for each PPP template.  A list corresponding to a PPP template specifies the pools the system searches in an attempt to assign an IP address to the peer of a target PPP connection. The system searches the pools in the order of their priority.  This table has an expansion dependent relationship on the cdtPppTemplateTable, containing zero or more rows for each PPP template
    	**type**\:  :py:class:`CdtPppPeerIpAddrPoolTable <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppPeerIpAddrPoolTable>`
    
    	**config**\: False
    
    .. attribute:: cdtethernettemplatetable
    
    	This table contains attributes relating to dynamic interfaces initiated on Ethernet virtual interfaces (e.g., EoMPLS) or automatically created VLANs.  This table has a sparse\-dependent relationship on the cdtTemplateTable, containing a row for each dynamic template having a cdtTemplateType of one of the following values\:      'derived'     'ethernet'
    	**type**\:  :py:class:`CdtEthernetTemplateTable <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtEthernetTemplateTable>`
    
    	**config**\: False
    
    .. attribute:: cdtsrvtemplatetable
    
    	This table contains attributes relating to a service.  This table has a sparse\-dependent relationship on the cdtTemplateTable, containing a row for each dynamic template having a cdtTemplateType of one of the following values\:      'derived'     'service'
    	**type**\:  :py:class:`CdtSrvTemplateTable <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtSrvTemplateTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
    _revision = '2007-09-06'

    def __init__(self):
        super(CISCODYNAMICTEMPLATEMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-DYNAMIC-TEMPLATE-MIB"
        self.yang_parent_name = "CISCO-DYNAMIC-TEMPLATE-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cdtTemplateTable", ("cdttemplatetable", CISCODYNAMICTEMPLATEMIB.CdtTemplateTable)), ("cdtTemplateTargetTable", ("cdttemplatetargettable", CISCODYNAMICTEMPLATEMIB.CdtTemplateTargetTable)), ("cdtTemplateAssociationTable", ("cdttemplateassociationtable", CISCODYNAMICTEMPLATEMIB.CdtTemplateAssociationTable)), ("cdtTemplateUsageTable", ("cdttemplateusagetable", CISCODYNAMICTEMPLATEMIB.CdtTemplateUsageTable)), ("cdtTemplateCommonTable", ("cdttemplatecommontable", CISCODYNAMICTEMPLATEMIB.CdtTemplateCommonTable)), ("cdtIfTemplateTable", ("cdtiftemplatetable", CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable)), ("cdtPppTemplateTable", ("cdtppptemplatetable", CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable)), ("cdtPppPeerIpAddrPoolTable", ("cdtppppeeripaddrpooltable", CISCODYNAMICTEMPLATEMIB.CdtPppPeerIpAddrPoolTable)), ("cdtEthernetTemplateTable", ("cdtethernettemplatetable", CISCODYNAMICTEMPLATEMIB.CdtEthernetTemplateTable)), ("cdtSrvTemplateTable", ("cdtsrvtemplatetable", CISCODYNAMICTEMPLATEMIB.CdtSrvTemplateTable))])
        self._leafs = OrderedDict()

        self.cdttemplatetable = CISCODYNAMICTEMPLATEMIB.CdtTemplateTable()
        self.cdttemplatetable.parent = self
        self._children_name_map["cdttemplatetable"] = "cdtTemplateTable"

        self.cdttemplatetargettable = CISCODYNAMICTEMPLATEMIB.CdtTemplateTargetTable()
        self.cdttemplatetargettable.parent = self
        self._children_name_map["cdttemplatetargettable"] = "cdtTemplateTargetTable"

        self.cdttemplateassociationtable = CISCODYNAMICTEMPLATEMIB.CdtTemplateAssociationTable()
        self.cdttemplateassociationtable.parent = self
        self._children_name_map["cdttemplateassociationtable"] = "cdtTemplateAssociationTable"

        self.cdttemplateusagetable = CISCODYNAMICTEMPLATEMIB.CdtTemplateUsageTable()
        self.cdttemplateusagetable.parent = self
        self._children_name_map["cdttemplateusagetable"] = "cdtTemplateUsageTable"

        self.cdttemplatecommontable = CISCODYNAMICTEMPLATEMIB.CdtTemplateCommonTable()
        self.cdttemplatecommontable.parent = self
        self._children_name_map["cdttemplatecommontable"] = "cdtTemplateCommonTable"

        self.cdtiftemplatetable = CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable()
        self.cdtiftemplatetable.parent = self
        self._children_name_map["cdtiftemplatetable"] = "cdtIfTemplateTable"

        self.cdtppptemplatetable = CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable()
        self.cdtppptemplatetable.parent = self
        self._children_name_map["cdtppptemplatetable"] = "cdtPppTemplateTable"

        self.cdtppppeeripaddrpooltable = CISCODYNAMICTEMPLATEMIB.CdtPppPeerIpAddrPoolTable()
        self.cdtppppeeripaddrpooltable.parent = self
        self._children_name_map["cdtppppeeripaddrpooltable"] = "cdtPppPeerIpAddrPoolTable"

        self.cdtethernettemplatetable = CISCODYNAMICTEMPLATEMIB.CdtEthernetTemplateTable()
        self.cdtethernettemplatetable.parent = self
        self._children_name_map["cdtethernettemplatetable"] = "cdtEthernetTemplateTable"

        self.cdtsrvtemplatetable = CISCODYNAMICTEMPLATEMIB.CdtSrvTemplateTable()
        self.cdtsrvtemplatetable.parent = self
        self._children_name_map["cdtsrvtemplatetable"] = "cdtSrvTemplateTable"
        self._segment_path = lambda: "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCODYNAMICTEMPLATEMIB, [], name, value)


    class CdtTemplateTable(Entity):
        """
        This table lists the dynamic templates maintained by the
        system, including those that have been locally\-configured on the
        system and those pushed to the system by external policy
        servers.
        
        .. attribute:: cdttemplateentry
        
        	An entry describes a dynamic template, which serves as a container for configuration attributes.  The configuration attributes contained by a dynamic template depends on its type.  The system automatically creates a corresponding entry when a dynamic template has been created through another management entity (e.g., the system's local console).  Likewise, the system automatically destroys a corresponding entry when a dynamic template has been destroyed through another management entity.  The system automatically creates a corresponding entry when an external policy server pushes a user profile or a service profile to the system.  The system automatically creates a corresponding entry when it generates a derived configuration
        	**type**\: list of  		 :py:class:`CdtTemplateEntry <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateTable.CdtTemplateEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
        _revision = '2007-09-06'

        def __init__(self):
            super(CISCODYNAMICTEMPLATEMIB.CdtTemplateTable, self).__init__()

            self.yang_name = "cdtTemplateTable"
            self.yang_parent_name = "CISCO-DYNAMIC-TEMPLATE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdtTemplateEntry", ("cdttemplateentry", CISCODYNAMICTEMPLATEMIB.CdtTemplateTable.CdtTemplateEntry))])
            self._leafs = OrderedDict()

            self.cdttemplateentry = YList(self)
            self._segment_path = lambda: "cdtTemplateTable"
            self._absolute_path = lambda: "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODYNAMICTEMPLATEMIB.CdtTemplateTable, [], name, value)


        class CdtTemplateEntry(Entity):
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
            
            .. attribute:: cdttemplatename  (key)
            
            	This object indicates a string\-value that uniquely identifies the dynamic template.  If the corresponding instance of cdtTemplateSrc is not 'local', then the system automatically generates the name identifying the dynamic template
            	**type**\: str
            
            	**length:** 1..64
            
            	**config**\: False
            
            .. attribute:: cdttemplatestatus
            
            	This object specifies the status of the dynamic template.  The following columns must be valid before activating a dynamic template\:      \- cdtTemplateStorage     \- cdtTemplateType  However, these objects specify a default value.  Thus, it is possible to use create\-and\-go semantics without setting any additional columns.  An implementation must allow the EMS/NMS to modify any column when this column is 'active', including columns defined in tables that have a one\-to\-one or sparse dependent relationship on this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: cdttemplatestorage
            
            	This object specifies what happens to the dynamic template upon restart.  If the corresponding instance of cdtTemplateSrc is not 'local', then this column must be 'volatile'
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            	**config**\: False
            
            .. attribute:: cdttemplatetype
            
            	This object indicates the types of dynamic template
            	**type**\:  :py:class:`DynamicTemplateType <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_TC_MIB.DynamicTemplateType>`
            
            	**config**\: False
            
            .. attribute:: cdttemplatesrc
            
            	This object specifies the source of the dynamic template\:  'other'     The implementation of the MIB module does not recognize the     source of the dynamic template.  'derived'     The system created the set of attributes from one or     more dynamic templates.  'local'     The dynamic template was locally configured through a     management entity, such as the local console or a SNMP     entity.  'aaaUserProfile'     The dynamic template originated from a user profile     pushed from an external policy server.  'aaaServiceProfile'     The dynamic template originated from a service profile     pushed from an external policy server
            	**type**\:  :py:class:`CdtTemplateSrc <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateTable.CdtTemplateEntry.CdtTemplateSrc>`
            
            	**config**\: False
            
            .. attribute:: cdttemplateusagecount
            
            	This object specifies the number of targets using a dynamic template
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
            _revision = '2007-09-06'

            def __init__(self):
                super(CISCODYNAMICTEMPLATEMIB.CdtTemplateTable.CdtTemplateEntry, self).__init__()

                self.yang_name = "cdtTemplateEntry"
                self.yang_parent_name = "cdtTemplateTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdttemplatename']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdttemplatename', (YLeaf(YType.str, 'cdtTemplateName'), ['str'])),
                    ('cdttemplatestatus', (YLeaf(YType.enumeration, 'cdtTemplateStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('cdttemplatestorage', (YLeaf(YType.enumeration, 'cdtTemplateStorage'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('cdttemplatetype', (YLeaf(YType.enumeration, 'cdtTemplateType'), [('ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_TC_MIB', 'DynamicTemplateType', '')])),
                    ('cdttemplatesrc', (YLeaf(YType.enumeration, 'cdtTemplateSrc'), [('ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CISCODYNAMICTEMPLATEMIB', 'CdtTemplateTable.CdtTemplateEntry.CdtTemplateSrc')])),
                    ('cdttemplateusagecount', (YLeaf(YType.uint32, 'cdtTemplateUsageCount'), ['int'])),
                ])
                self.cdttemplatename = None
                self.cdttemplatestatus = None
                self.cdttemplatestorage = None
                self.cdttemplatetype = None
                self.cdttemplatesrc = None
                self.cdttemplateusagecount = None
                self._segment_path = lambda: "cdtTemplateEntry" + "[cdtTemplateName='" + str(self.cdttemplatename) + "']"
                self._absolute_path = lambda: "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/cdtTemplateTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODYNAMICTEMPLATEMIB.CdtTemplateTable.CdtTemplateEntry, ['cdttemplatename', 'cdttemplatestatus', 'cdttemplatestorage', 'cdttemplatetype', 'cdttemplatesrc', 'cdttemplateusagecount'], name, value)

            class CdtTemplateSrc(Enum):
                """
                CdtTemplateSrc (Enum Class)

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





    class CdtTemplateTargetTable(Entity):
        """
        This table contains a list of targets associated with
        one or more dynamic templates.
        
        .. attribute:: cdttemplatetargetentry
        
        	An entry describes a target associated with one or more dynamic templates.  The system automatically creates an entry when it associates a dynamic template to a target.  Likewise, the system automatically destroys an entry when a target no longer has any associated dynamic templates
        	**type**\: list of  		 :py:class:`CdtTemplateTargetEntry <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateTargetTable.CdtTemplateTargetEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
        _revision = '2007-09-06'

        def __init__(self):
            super(CISCODYNAMICTEMPLATEMIB.CdtTemplateTargetTable, self).__init__()

            self.yang_name = "cdtTemplateTargetTable"
            self.yang_parent_name = "CISCO-DYNAMIC-TEMPLATE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdtTemplateTargetEntry", ("cdttemplatetargetentry", CISCODYNAMICTEMPLATEMIB.CdtTemplateTargetTable.CdtTemplateTargetEntry))])
            self._leafs = OrderedDict()

            self.cdttemplatetargetentry = YList(self)
            self._segment_path = lambda: "cdtTemplateTargetTable"
            self._absolute_path = lambda: "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODYNAMICTEMPLATEMIB.CdtTemplateTargetTable, [], name, value)


        class CdtTemplateTargetEntry(Entity):
            """
            An entry describes a target associated with one or more
            dynamic templates.
            
            The system automatically creates an entry when it associates a
            dynamic template to a target.  Likewise, the system
            automatically destroys an entry when a target no longer has any
            associated dynamic templates.
            
            .. attribute:: cdttemplatetargettype  (key)
            
            	This object indicates the type of target
            	**type**\:  :py:class:`DynamicTemplateTargetType <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_TC_MIB.DynamicTemplateTargetType>`
            
            	**config**\: False
            
            .. attribute:: cdttemplatetargetid  (key)
            
            	This object uniquely identifies the target within the scope of its type
            	**type**\: str
            
            	**length:** 1..20
            
            	**config**\: False
            
            .. attribute:: cdttemplatetargetstatus
            
            	This object specifies the status of the dynamic template target.  The following columns must be valid before activating a subscriber access profile\:      \- cdtTemplateTargetStorage  However, these objects specify a default value.  Thus, it is possible to use create\-and\-go semantics without setting any additional columns.  An implementation must allow the EMS/NMS to modify any column when this column is 'active', including columns defined in tables that have a one\-to\-one or sparse dependent relationship on this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: cdttemplatetargetstorage
            
            	This object specifies what happens to the dynamic template target upon restart
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
            _revision = '2007-09-06'

            def __init__(self):
                super(CISCODYNAMICTEMPLATEMIB.CdtTemplateTargetTable.CdtTemplateTargetEntry, self).__init__()

                self.yang_name = "cdtTemplateTargetEntry"
                self.yang_parent_name = "cdtTemplateTargetTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdttemplatetargettype','cdttemplatetargetid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdttemplatetargettype', (YLeaf(YType.enumeration, 'cdtTemplateTargetType'), [('ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_TC_MIB', 'DynamicTemplateTargetType', '')])),
                    ('cdttemplatetargetid', (YLeaf(YType.str, 'cdtTemplateTargetId'), ['str'])),
                    ('cdttemplatetargetstatus', (YLeaf(YType.enumeration, 'cdtTemplateTargetStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('cdttemplatetargetstorage', (YLeaf(YType.enumeration, 'cdtTemplateTargetStorage'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                ])
                self.cdttemplatetargettype = None
                self.cdttemplatetargetid = None
                self.cdttemplatetargetstatus = None
                self.cdttemplatetargetstorage = None
                self._segment_path = lambda: "cdtTemplateTargetEntry" + "[cdtTemplateTargetType='" + str(self.cdttemplatetargettype) + "']" + "[cdtTemplateTargetId='" + str(self.cdttemplatetargetid) + "']"
                self._absolute_path = lambda: "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/cdtTemplateTargetTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODYNAMICTEMPLATEMIB.CdtTemplateTargetTable.CdtTemplateTargetEntry, ['cdttemplatetargettype', 'cdttemplatetargetid', 'cdttemplatetargetstatus', 'cdttemplatetargetstorage'], name, value)




    class CdtTemplateAssociationTable(Entity):
        """
        This table contains a list of templates associated with each
        target.
        
        This table has an expansion dependent relationship on the
        cdtTemplateTargetTable, containing zero or more rows for each
        target.
        
        .. attribute:: cdttemplateassociationentry
        
        	An entry indicates an association of a dynamic template with a target.  The system automatically creates an entry when it associates a dynamic template to a target.  The system also creates an entry when it derives the configuration that it applies to a target.  The system automatically destroys an entry under the following circumstances\:  1)  The target indicated by the entry no longer exists.  2)  The association between the target and the dynamic template     no longer exists
        	**type**\: list of  		 :py:class:`CdtTemplateAssociationEntry <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateAssociationTable.CdtTemplateAssociationEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
        _revision = '2007-09-06'

        def __init__(self):
            super(CISCODYNAMICTEMPLATEMIB.CdtTemplateAssociationTable, self).__init__()

            self.yang_name = "cdtTemplateAssociationTable"
            self.yang_parent_name = "CISCO-DYNAMIC-TEMPLATE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdtTemplateAssociationEntry", ("cdttemplateassociationentry", CISCODYNAMICTEMPLATEMIB.CdtTemplateAssociationTable.CdtTemplateAssociationEntry))])
            self._leafs = OrderedDict()

            self.cdttemplateassociationentry = YList(self)
            self._segment_path = lambda: "cdtTemplateAssociationTable"
            self._absolute_path = lambda: "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODYNAMICTEMPLATEMIB.CdtTemplateAssociationTable, [], name, value)


        class CdtTemplateAssociationEntry(Entity):
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
            
            .. attribute:: cdttemplatetargettype  (key)
            
            	
            	**type**\:  :py:class:`DynamicTemplateTargetType <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_TC_MIB.DynamicTemplateTargetType>`
            
            	**config**\: False
            
            .. attribute:: cdttemplatetargetid  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..20
            
            	**refers to**\:  :py:class:`cdttemplatetargetid <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateTargetTable.CdtTemplateTargetEntry>`
            
            	**config**\: False
            
            .. attribute:: cdttemplateassociationname  (key)
            
            	This object indicates the name of the template associated with the target
            	**type**\: str
            
            	**length:** 1..64
            
            	**config**\: False
            
            .. attribute:: cdttemplateassociationprecedence
            
            	This object indicates the relative precedence of the associated dynamic template.  Lower values have higher precedence than higher values
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
            _revision = '2007-09-06'

            def __init__(self):
                super(CISCODYNAMICTEMPLATEMIB.CdtTemplateAssociationTable.CdtTemplateAssociationEntry, self).__init__()

                self.yang_name = "cdtTemplateAssociationEntry"
                self.yang_parent_name = "cdtTemplateAssociationTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdttemplatetargettype','cdttemplatetargetid','cdttemplateassociationname']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdttemplatetargettype', (YLeaf(YType.enumeration, 'cdtTemplateTargetType'), [('ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_TC_MIB', 'DynamicTemplateTargetType', '')])),
                    ('cdttemplatetargetid', (YLeaf(YType.str, 'cdtTemplateTargetId'), ['str'])),
                    ('cdttemplateassociationname', (YLeaf(YType.str, 'cdtTemplateAssociationName'), ['str'])),
                    ('cdttemplateassociationprecedence', (YLeaf(YType.uint32, 'cdtTemplateAssociationPrecedence'), ['int'])),
                ])
                self.cdttemplatetargettype = None
                self.cdttemplatetargetid = None
                self.cdttemplateassociationname = None
                self.cdttemplateassociationprecedence = None
                self._segment_path = lambda: "cdtTemplateAssociationEntry" + "[cdtTemplateTargetType='" + str(self.cdttemplatetargettype) + "']" + "[cdtTemplateTargetId='" + str(self.cdttemplatetargetid) + "']" + "[cdtTemplateAssociationName='" + str(self.cdttemplateassociationname) + "']"
                self._absolute_path = lambda: "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/cdtTemplateAssociationTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODYNAMICTEMPLATEMIB.CdtTemplateAssociationTable.CdtTemplateAssociationEntry, ['cdttemplatetargettype', 'cdttemplatetargetid', 'cdttemplateassociationname', 'cdttemplateassociationprecedence'], name, value)




    class CdtTemplateUsageTable(Entity):
        """
        This table contains a list of targets using each dynamic
        template.
        
        This table has an expansion dependent relationship on the
        cdtTemplateTable, containing zero or more rows for each
        dynamic template.
        
        .. attribute:: cdttemplateusageentry
        
        	An entry indicates a target using the dynamic template.  The system automatically creates an entry when it associates a dynamic template to a target.  The system also creates an entry when it derives the configuration that it applies to a target.  The system automatically destroys an entry under the following circumstances\:  1)  The target indicated by the entry no longer exists.  2)  The association between the target and the dynamic template     no longer exists
        	**type**\: list of  		 :py:class:`CdtTemplateUsageEntry <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateUsageTable.CdtTemplateUsageEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
        _revision = '2007-09-06'

        def __init__(self):
            super(CISCODYNAMICTEMPLATEMIB.CdtTemplateUsageTable, self).__init__()

            self.yang_name = "cdtTemplateUsageTable"
            self.yang_parent_name = "CISCO-DYNAMIC-TEMPLATE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdtTemplateUsageEntry", ("cdttemplateusageentry", CISCODYNAMICTEMPLATEMIB.CdtTemplateUsageTable.CdtTemplateUsageEntry))])
            self._leafs = OrderedDict()

            self.cdttemplateusageentry = YList(self)
            self._segment_path = lambda: "cdtTemplateUsageTable"
            self._absolute_path = lambda: "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODYNAMICTEMPLATEMIB.CdtTemplateUsageTable, [], name, value)


        class CdtTemplateUsageEntry(Entity):
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
            
            .. attribute:: cdttemplatename  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..64
            
            	**refers to**\:  :py:class:`cdttemplatename <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateTable.CdtTemplateEntry>`
            
            	**config**\: False
            
            .. attribute:: cdttemplateusagetargettype  (key)
            
            	This object indicates the type of target using the dynamic template
            	**type**\:  :py:class:`DynamicTemplateTargetType <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_TC_MIB.DynamicTemplateTargetType>`
            
            	**config**\: False
            
            .. attribute:: cdttemplateusagetargetid  (key)
            
            	This object indicates the name of the target using the dynamic template
            	**type**\: str
            
            	**length:** 1..20
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
            _revision = '2007-09-06'

            def __init__(self):
                super(CISCODYNAMICTEMPLATEMIB.CdtTemplateUsageTable.CdtTemplateUsageEntry, self).__init__()

                self.yang_name = "cdtTemplateUsageEntry"
                self.yang_parent_name = "cdtTemplateUsageTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdttemplatename','cdttemplateusagetargettype','cdttemplateusagetargetid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdttemplatename', (YLeaf(YType.str, 'cdtTemplateName'), ['str'])),
                    ('cdttemplateusagetargettype', (YLeaf(YType.enumeration, 'cdtTemplateUsageTargetType'), [('ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_TC_MIB', 'DynamicTemplateTargetType', '')])),
                    ('cdttemplateusagetargetid', (YLeaf(YType.str, 'cdtTemplateUsageTargetId'), ['str'])),
                ])
                self.cdttemplatename = None
                self.cdttemplateusagetargettype = None
                self.cdttemplateusagetargetid = None
                self._segment_path = lambda: "cdtTemplateUsageEntry" + "[cdtTemplateName='" + str(self.cdttemplatename) + "']" + "[cdtTemplateUsageTargetType='" + str(self.cdttemplateusagetargettype) + "']" + "[cdtTemplateUsageTargetId='" + str(self.cdttemplateusagetargetid) + "']"
                self._absolute_path = lambda: "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/cdtTemplateUsageTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODYNAMICTEMPLATEMIB.CdtTemplateUsageTable.CdtTemplateUsageEntry, ['cdttemplatename', 'cdttemplateusagetargettype', 'cdttemplateusagetargetid'], name, value)




    class CdtTemplateCommonTable(Entity):
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
        	**type**\: list of  		 :py:class:`CdtTemplateCommonEntry <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateCommonTable.CdtTemplateCommonEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
        _revision = '2007-09-06'

        def __init__(self):
            super(CISCODYNAMICTEMPLATEMIB.CdtTemplateCommonTable, self).__init__()

            self.yang_name = "cdtTemplateCommonTable"
            self.yang_parent_name = "CISCO-DYNAMIC-TEMPLATE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdtTemplateCommonEntry", ("cdttemplatecommonentry", CISCODYNAMICTEMPLATEMIB.CdtTemplateCommonTable.CdtTemplateCommonEntry))])
            self._leafs = OrderedDict()

            self.cdttemplatecommonentry = YList(self)
            self._segment_path = lambda: "cdtTemplateCommonTable"
            self._absolute_path = lambda: "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODYNAMICTEMPLATEMIB.CdtTemplateCommonTable, [], name, value)


        class CdtTemplateCommonEntry(Entity):
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
            
            .. attribute:: cdttemplatename  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..64
            
            	**refers to**\:  :py:class:`cdttemplatename <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateTable.CdtTemplateEntry>`
            
            	**config**\: False
            
            .. attribute:: cdtcommonvalid
            
            	This object specifies which attributes in the dynamic template have been configured to valid values.  Each bit in this bit string corresponds to a column in this table.  If the bit is '0', then the value of the corresponding column is not valid.  If the bit is '1', then the value of the corresponding column has been configured to a valid value.  The following list specifies the mappings between bits and the columns\:      'descr'             => cdtCommonDescr     'keepaliveInt'      => cdtCommonKeepaliveInt     'keepaliveRetries'  => cdtCommonKeepaliveRetries     'vrf'               => cdtCommonVrf     'addrPool'          => cdtCommonAddrPool     'ipv4AccessGroup'   => cdtCommonIpv4AccessGroup     'ipv4Unreachables'  => cdtCommonIpv4Unreachables     'ipv6AccessGroup'   => cdtCommonIpv6AccessGroup     'ipv6Unreachables'  => cdtCommonIpv6Unreachables     'srvSubControl'     => cdtCommonSrvSubControl     'srvRedirect'       => cdtCommonSrvRedirect     'srvAcct'           => cdtCommonSrvAcct     'srvQos'            => cdtCommonSrvQos     'srvNetflow'        => cdtCommonSrvNetflow
            	**type**\:  :py:class:`CdtCommonValid <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateCommonTable.CdtTemplateCommonEntry.CdtCommonValid>`
            
            	**config**\: False
            
            .. attribute:: cdtcommondescr
            
            	This object specifies a human\-readable description for the dynamic template.  This column is valid only if the 'descr' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdtcommonkeepaliveint
            
            	This object specifies the interval that the system sends keepalive messages to a target.  This column is valid only if the 'keepaliveInterval' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cdtcommonkeepaliveretries
            
            	This object specifies the number of times the system will resend a keepalive message without a response before it transitions a target to an operationally down state.  This column is valid only if the 'keepaliveRetries' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: int
            
            	**range:** 1..255
            
            	**config**\: False
            
            	**units**\: retries
            
            .. attribute:: cdtcommonvrf
            
            	This object specifies the name of the VRF with which a target has an association.  This column is valid only if the 'vrf' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: cdtcommonaddrpool
            
            	This object specifies the name of the IP address pool the system will use to assign an IP address to a peer of a target.  This column is valid only if the 'addrPool' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdtcommonipv4accessgroup
            
            	This object specifies the name (or number) of the IPv4 ACL applied to a target.  This column is valid only if the 'ipv4AccessGroup' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdtcommonipv4unreachables
            
            	This object specifies whether a target generates ICMPv4 unreachable messages.  This column is valid only if the 'ipv4Unreachables' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cdtcommonipv6accessgroup
            
            	This object specifies the name (or number) of the IPv4 ACL applied to a target.  This column is valid only if the 'ipv6AccessGroup' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdtcommonipv6unreachables
            
            	This object specifies whether a target generates ICMPv6 unreachable messages.  This column is valid only if the 'ipv6Unreachables' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cdtcommonsrvsubcontrol
            
            	This object specifies the name of the subscriber control policy applied to a target.  The system should assume that the cbpPolicyMapType (defined by the CISCO\-CBP\-BASE\-CFG\-MIB) of the policy is cbpPmtControlSubscriber (defined by the CISCO\-CBP\-TYPE\-OID\-MIB).  This column is valid only if the 'srvSubControl' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cdtcommonsrvredirect
            
            	This object specifies the name of the traffic redirect policy applied to a target.  The system should assume that the cbpPolicyMapType (defined by the CISCO\-CBP\-BASE\-CFG\-MIB) of the policy is cbpPmtTrafficRedirect (defined by the CISCO\-CBP\-TYPE\-OID\-MIB).  This column is valid only if the 'srvRedirect' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cdtcommonsrvacct
            
            	This object specifies the name of the traffic accounting policy applied to a target.  The system should assume that the cbpPolicyMapType (defined by the CISCO\-CBP\-BASE\-CFG\-MIB) of the policy is cbpPmtTrafficAccounting (defined by the CISCO\-CBP\-TYPE\-OID\-MIB).  This column is valid only if the 'srvAcct' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cdtcommonsrvqos
            
            	This object specifies the name of the traffic QoS policy applied to a target.  The system should assume that the cbpPolicyMapType (defined by the CISCO\-CBP\-BASE\-CFG\-MIB) of the policy is cbpPmtQos (defined by the CISCO\-CBP\-TYPE\-OID\-MIB).  This column is valid only if the 'srvQos' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cdtcommonsrvnetflow
            
            	This object specifies the name of the NetFlow policy applied to a target.  The system should assume that the cbpPolicyMapType (defined by the CISCO\-CBP\-BASE\-CFG\-MIB) of the policy is cbpPmtNetflow (defined by the CISCO\-CBP\-TYPE\-OID\-MIB).  This column is valid only if the 'srvNetflow' bit of the corresponding instance of cdtCommonValid is '1'
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
            _revision = '2007-09-06'

            def __init__(self):
                super(CISCODYNAMICTEMPLATEMIB.CdtTemplateCommonTable.CdtTemplateCommonEntry, self).__init__()

                self.yang_name = "cdtTemplateCommonEntry"
                self.yang_parent_name = "cdtTemplateCommonTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdttemplatename']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdttemplatename', (YLeaf(YType.str, 'cdtTemplateName'), ['str'])),
                    ('cdtcommonvalid', (YLeaf(YType.bits, 'cdtCommonValid'), ['Bits'])),
                    ('cdtcommondescr', (YLeaf(YType.str, 'cdtCommonDescr'), ['str'])),
                    ('cdtcommonkeepaliveint', (YLeaf(YType.uint32, 'cdtCommonKeepaliveInt'), ['int'])),
                    ('cdtcommonkeepaliveretries', (YLeaf(YType.uint32, 'cdtCommonKeepaliveRetries'), ['int'])),
                    ('cdtcommonvrf', (YLeaf(YType.str, 'cdtCommonVrf'), ['str'])),
                    ('cdtcommonaddrpool', (YLeaf(YType.str, 'cdtCommonAddrPool'), ['str'])),
                    ('cdtcommonipv4accessgroup', (YLeaf(YType.str, 'cdtCommonIpv4AccessGroup'), ['str'])),
                    ('cdtcommonipv4unreachables', (YLeaf(YType.boolean, 'cdtCommonIpv4Unreachables'), ['bool'])),
                    ('cdtcommonipv6accessgroup', (YLeaf(YType.str, 'cdtCommonIpv6AccessGroup'), ['str'])),
                    ('cdtcommonipv6unreachables', (YLeaf(YType.boolean, 'cdtCommonIpv6Unreachables'), ['bool'])),
                    ('cdtcommonsrvsubcontrol', (YLeaf(YType.str, 'cdtCommonSrvSubControl'), ['str'])),
                    ('cdtcommonsrvredirect', (YLeaf(YType.str, 'cdtCommonSrvRedirect'), ['str'])),
                    ('cdtcommonsrvacct', (YLeaf(YType.str, 'cdtCommonSrvAcct'), ['str'])),
                    ('cdtcommonsrvqos', (YLeaf(YType.str, 'cdtCommonSrvQos'), ['str'])),
                    ('cdtcommonsrvnetflow', (YLeaf(YType.str, 'cdtCommonSrvNetflow'), ['str'])),
                ])
                self.cdttemplatename = None
                self.cdtcommonvalid = Bits()
                self.cdtcommondescr = None
                self.cdtcommonkeepaliveint = None
                self.cdtcommonkeepaliveretries = None
                self.cdtcommonvrf = None
                self.cdtcommonaddrpool = None
                self.cdtcommonipv4accessgroup = None
                self.cdtcommonipv4unreachables = None
                self.cdtcommonipv6accessgroup = None
                self.cdtcommonipv6unreachables = None
                self.cdtcommonsrvsubcontrol = None
                self.cdtcommonsrvredirect = None
                self.cdtcommonsrvacct = None
                self.cdtcommonsrvqos = None
                self.cdtcommonsrvnetflow = None
                self._segment_path = lambda: "cdtTemplateCommonEntry" + "[cdtTemplateName='" + str(self.cdttemplatename) + "']"
                self._absolute_path = lambda: "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/cdtTemplateCommonTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODYNAMICTEMPLATEMIB.CdtTemplateCommonTable.CdtTemplateCommonEntry, ['cdttemplatename', 'cdtcommonvalid', 'cdtcommondescr', 'cdtcommonkeepaliveint', 'cdtcommonkeepaliveretries', 'cdtcommonvrf', 'cdtcommonaddrpool', 'cdtcommonipv4accessgroup', 'cdtcommonipv4unreachables', 'cdtcommonipv6accessgroup', 'cdtcommonipv6unreachables', 'cdtcommonsrvsubcontrol', 'cdtcommonsrvredirect', 'cdtcommonsrvacct', 'cdtcommonsrvqos', 'cdtcommonsrvnetflow'], name, value)




    class CdtIfTemplateTable(Entity):
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
        	**type**\: list of  		 :py:class:`CdtIfTemplateEntry <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable.CdtIfTemplateEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
        _revision = '2007-09-06'

        def __init__(self):
            super(CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable, self).__init__()

            self.yang_name = "cdtIfTemplateTable"
            self.yang_parent_name = "CISCO-DYNAMIC-TEMPLATE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdtIfTemplateEntry", ("cdtiftemplateentry", CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable.CdtIfTemplateEntry))])
            self._leafs = OrderedDict()

            self.cdtiftemplateentry = YList(self)
            self._segment_path = lambda: "cdtIfTemplateTable"
            self._absolute_path = lambda: "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable, [], name, value)


        class CdtIfTemplateEntry(Entity):
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
            
            .. attribute:: cdttemplatename  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..64
            
            	**refers to**\:  :py:class:`cdttemplatename <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateTable.CdtTemplateEntry>`
            
            	**config**\: False
            
            .. attribute:: cdtifvalid
            
            	This object specifies which attributes in the dynamic template have been configured to valid values.  Each bit in this bit string corresponds to a column in this table.  If the bit is '0', then the value of the corresponding column is not valid.  If the bit is '1', then the value of the corresponding column has been configured to a valid value.  The following list specifies the mappings between bits and the columns\:      'mtu'                     => cdtIfMtu     'cdpEnable'               => cdtIfCdpEnable     'flowMonitor'             => cdtIfFlowMonitor     'ipv4Unnumbered'          => cdtIfIpv4Unnumbered     'ipv4SubEnable'           => cdtIfIpv4SubEnable     'ipv4Mtu'                 => cdtIfIpv4Mtu     'ipv4TcpMssAdjust'        => cdtIfIpv4TcpMssAdjust     'ipv4VerifyUniRpf'        => cdtIfIpv4VerifyUniRpf     'ipv4VerifyUniRpfAcl'     => cdtIfIpv4VerifyUniRpfAcl     'ipv4VerifyUniRpfOpts'    => cdtIfIpv4VerifyUniRpfOpts     'ipv6Enable'              => cdtIfIpv6Enable     'ipv6SubEnable'           => cdtIfIpv6SubEnable     'ipv6TcpMssAdjust'        => cdtIfIpv6TcpMssAdjust     'ipv6VerifyUniRpf'        => cdtIfIpv6VerifyUniRpf     'ipv6VerifyUniRpfAcl'     => cdtIfIpv6VerifyUniRpfAcl     'ipv6VerifyUniRpfOpts'    => cdtIfIpv6VerifyUniRpfOpts     'ipv6NdPrefix'            => cdtIfIpv6NdPrefix,                                  cdtIfIpv6NdPrefixLength     'ipv6NdValidLife'         => cdtIfIpv6NdValidLife     'ipv6NdPreferredLife'     => cdtIfIpv6NdPreferredLife     'ipv6NdOpts'              => cdtIfIpv6NdOpts     'ipv6NdDadAttempts'       => cdtIfIpv6NdDadAttempts     'ipv6NdNsInterval'        => cdtIfIpv6NdNsInterval     'ipv6NdReacableTime'      => cdtIfIpv6NdReacableTime     'ipv6NdRaIntervalMax'     => cdtIfIpv6NdRaIntervalUnits,                                  cdtIfIpv6NdRaIntervalMax     'ipv6NdRaIntervalMin'     => cdtIfIpv6NdRaIntervalMin     'ipv6NdRaLife'            => cdtIfIpv6NdRaLife     'ipv6NdRouterPreference'' => cdtIfIpv6NdRouterPreference
            	**type**\:  :py:class:`CdtIfValid <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable.CdtIfTemplateEntry.CdtIfValid>`
            
            	**config**\: False
            
            .. attribute:: cdtifmtu
            
            	This object specifies the Maximum Transfer Unit (MTU) size for all packets sent on the target interface.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid.  This column is valid only if the 'mtu' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 0..None \| 64..65535
            
            	**config**\: False
            
            	**units**\: octets
            
            .. attribute:: cdtifcdpenable
            
            	This object specifies whether the target interface participates in the Cisco Discovery Protocol (CDP).  This column is valid only if the 'cdpEnable' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cdtifflowmonitor
            
            	This object specifies the name of the flow monitor associated with the target interface.  This column is valid only if the 'flowMonitor' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdtifipv4unnumbered
            
            	This object specifies the interface of the source address that the target interface uses when originating IPv4 packets.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid (e.g., immediately following the creation of an instance of the object).  This column is valid only if the 'ipv4Unnumbered' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: cdtifipv4subenable
            
            	This object specifies whether the target interface allows IPv4 subscriber sessions.  This column is valid only if the 'ipv4SubEnable' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cdtifipv4mtu
            
            	This object specifies the Maximum Transfer Unit (MTU) size for IPv4 packets sent on the target interface.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid.  This column is valid only if the 'ipv4Mtu' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 0..None \| 128..65535
            
            	**config**\: False
            
            	**units**\: octets
            
            .. attribute:: cdtifipv4tcpmssadjust
            
            	This object specifies the adjustment to the Maximum Segment Size (MSS) of TCP SYN packets received by the target interface contained in IPv4 datagrams.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid.  This column is valid only if the 'ipv4TcpMssAdjust' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 0..None \| 500..1460
            
            	**config**\: False
            
            	**units**\: octets
            
            .. attribute:: cdtifipv4verifyunirpf
            
            	This object specifies whether the type of unicast RPF the system performs on IPv4 packets received by the target interface.  This column is valid only if the 'ipv4VerifyUniRpf' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  :py:class:`UnicastRpfType <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.UnicastRpfType>`
            
            	**config**\: False
            
            .. attribute:: cdtifipv4verifyunirpfacl
            
            	This object specifies the name (or number) of the IPv4 ACL used to determine whether the system should permit/deny packets received by the target interface that fail unicast RPF verification.  This column is valid only if the 'ipv4VerifyUniRpfAcl' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdtifipv4verifyunirpfopts
            
            	This object specifies the options that affect how the system performs unicast RPF on IPv4 packets received by the target interface.  This column is valid only if the 'ipv4VerifyUniRpfOpts' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  :py:class:`UnicastRpfOptions <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.UnicastRpfOptions>`
            
            	**config**\: False
            
            .. attribute:: cdtifipv6enable
            
            	This object specifies whether the system processes IPv6 packets received by the target interface.  This column is valid only if the 'ipv6Enable' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cdtifipv6subenable
            
            	This object specifies whether the target interface allows IPv6 subscriber sessions.  This column is valid only if the 'ipv6SubEnable' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cdtifipv6tcpmssadjust
            
            	This object specifies the adjustment to the Maximum Segment Size (MSS) of TCP SYN packets received by the target interface contained in IPv6 datagrams.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid.  This column is valid only if the 'ipv6TcpMssAdjust' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 0..None \| 500..1460
            
            	**config**\: False
            
            	**units**\: octets
            
            .. attribute:: cdtifipv6verifyunirpf
            
            	This object specifies whether the type of unicast RPF the system performs on IPv6 packets received by the target interface.  This column is valid only if the 'ipv6VerifyUniRpf' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  :py:class:`UnicastRpfType <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.UnicastRpfType>`
            
            	**config**\: False
            
            .. attribute:: cdtifipv6verifyunirpfacl
            
            	This object specifies the name (or number) of the IPv6 ACL used to determine whether the system should permit/deny packets received by the target interface that fail unicast RPF verification.  This column is valid only if the 'ipv6VerifyUniRpfAcl' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdtifipv6verifyunirpfopts
            
            	This object specifies the options that affect how the system performs unicast RPF on IPv6 packets received by the target interface.  This column is valid only if the 'ipv6VerifyUniRpfOpts' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  :py:class:`UnicastRpfOptions <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.UnicastRpfOptions>`
            
            	**config**\: False
            
            .. attribute:: cdtifipv6ndprefix
            
            	This object specifies the IPv6 network number included in IPv6 router advertisements sent on the target interface.  This column is valid only if the 'ipv6NdPrefix' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cdtifipv6ndprefixlength
            
            	This object specifies the length of the IPv6 prefix specified by the corresponding instance of cdtIpv6NdPrefix.  This column is valid only if the 'ipv6NdPrefix' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 0..2040
            
            	**config**\: False
            
            .. attribute:: cdtifipv6ndvalidlife
            
            	This object specifies the interval that the system advertises the IPv6 prefix (i.e., the corresponding instance of cdtIfIpv6NdPrefix) as 'valid' for IPv6 router advertisements sent on the target interface.  This column is valid only if the 'ipv6NdValidLife' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cdtifipv6ndpreferredlife
            
            	This object specifies the interval that the system advertises the IPv6 prefix (i.e., the corresponding instance of cdtIfIpv6NdPrefix) as 'preferred' for IPv6 router advertisements sent on the target interface.  This column is valid only if the 'ipv6NdPreferredLife' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cdtifipv6ndopts
            
            	This object specifies options that affect advertisements sent on the target interface\:      'advertise'         This option specifies that the system should advertise         the IPv6 prefix (i.e., the corresponding instance of         cdtIfIpv6NdPrefix).      'onlink'         This option specifies that the IPv6 prefix has been         assigned to a link.  If set to '0', the system         advertises the IPv6 prefix as 'offlink'.      'router'         This option indicates that the router will send the full         router address and not set the 'R' bit in prefix         advertisements.      'autoConfig'         This option indicates to hosts on the local link that         the specified prefix supports IPv6 auto\-configuration.      'advertisementInterval'         This option specifies the advertisement interval option         in router advertisements sent on the target interface.      'managedConfigFlag'         This option causes the system to set the 'managed         address configuration flag' in router advertisements         sent on the target interface.      'otherConfigFlag'         This option causes the system to set the 'other stateful         configuration' flag in router advertisements sent on the         target interface.      'frameIpv6Prefix'         This option causes the system to add the prefix in a         received RADIUS framed IPv6 prefix attribute to the         target interface's neighbor discovery prefix queue and         includes it in router advertisements sent on the target         interface.      'raSupress'         This option suppresses the transmission of router         advertisements on the target interface.  This column is valid only if the 'ipv6NdOpts' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  :py:class:`CdtIfIpv6NdOpts <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable.CdtIfTemplateEntry.CdtIfIpv6NdOpts>`
            
            	**config**\: False
            
            .. attribute:: cdtifipv6nddadattempts
            
            	This object specifies the number of consecutive neighbor solitication messages the system sends on the target interface while performing duplicate address detection on unicast IPv6 addresses on the target interface.  The value '0' disables duplicate address detection on the target interface.  This column is valid only if the 'ipv6NdDadAttempts' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 0..600
            
            	**config**\: False
            
            .. attribute:: cdtifipv6ndnsinterval
            
            	This object specifies the interval between neighbor solicitation retransmissions on the target interface.  This column is valid only if the 'ipv6NdNsIntervals' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 1000..3600000
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: cdtifipv6ndreachabletime
            
            	This object specifies the amount of time the system considers a neighbor of the target interface reachable after a reachability confirmation event has occurred.  The value '0' disables neighbor reachability detection on the target interface.  This column is valid only if the 'ipv6NdReachable' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: cdtifipv6ndraintervalunits
            
            	This object specifies the units of time for the corresponding instances of cdtIfIpv6NdRaIntervalMin and cdtIfIpv6NdRaIntervalMax.  This column is valid only if the 'ipv6NdRaInterval' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  :py:class:`CdtIfIpv6NdRaIntervalUnits <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable.CdtIfTemplateEntry.CdtIfIpv6NdRaIntervalUnits>`
            
            	**config**\: False
            
            .. attribute:: cdtifipv6ndraintervalmax
            
            	This object specifies the maximum interval between IPv6 router advertisements sent on the target interface.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid.  This column is valid only if the 'ipv6NdRaInterval' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdtifipv6ndraintervalmin
            
            	This object specifies the minimum interval between IPv6 router advertisements sent on the target interface.  The value of this column has the following restrictions\:  1)  This value cannot be less than 75% of the value specified     for cdtIfIpv6NdRaIntervalMax.  2)  If the corresponding instance of cdtIfIpv6NdRaIntervalUnits     is 'seconds', then this value cannot be less than '3'.  3)  If the corresponding instance of cdtIfIpv6NdRaIntervalUnits     is 'milliseconds', then this value cannot be less than '30'.  If the target interface template does not specify this value, then the system automatically assumes a minimum interval that is 75% of the corresponding instance of cdtIfIpv6NdRaIntervalMax.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid.  This column is valid only if the 'ipv6NdRaInterval' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdtifipv6ndralife
            
            	This object specifies the router lifetime value in IPv6 router advertisements sent on the target interface.  The value '0' specifies that neighbors should not consider the router as a default router
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cdtifipv6ndrouterpreference
            
            	This object specifies the Default Router Preference (DRP) for the router on the target interface.  This column is valid only if the 'ipv6NdRouterPreference' bit of the corresponding instance of cdtIfValid is '1'
            	**type**\:  :py:class:`CdtIfIpv6NdRouterPreference <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable.CdtIfTemplateEntry.CdtIfIpv6NdRouterPreference>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
            _revision = '2007-09-06'

            def __init__(self):
                super(CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable.CdtIfTemplateEntry, self).__init__()

                self.yang_name = "cdtIfTemplateEntry"
                self.yang_parent_name = "cdtIfTemplateTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdttemplatename']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdttemplatename', (YLeaf(YType.str, 'cdtTemplateName'), ['str'])),
                    ('cdtifvalid', (YLeaf(YType.bits, 'cdtIfValid'), ['Bits'])),
                    ('cdtifmtu', (YLeaf(YType.uint32, 'cdtIfMtu'), ['int'])),
                    ('cdtifcdpenable', (YLeaf(YType.boolean, 'cdtIfCdpEnable'), ['bool'])),
                    ('cdtifflowmonitor', (YLeaf(YType.str, 'cdtIfFlowMonitor'), ['str'])),
                    ('cdtifipv4unnumbered', (YLeaf(YType.int32, 'cdtIfIpv4Unnumbered'), ['int'])),
                    ('cdtifipv4subenable', (YLeaf(YType.boolean, 'cdtIfIpv4SubEnable'), ['bool'])),
                    ('cdtifipv4mtu', (YLeaf(YType.uint32, 'cdtIfIpv4Mtu'), ['int'])),
                    ('cdtifipv4tcpmssadjust', (YLeaf(YType.uint32, 'cdtIfIpv4TcpMssAdjust'), ['int'])),
                    ('cdtifipv4verifyunirpf', (YLeaf(YType.enumeration, 'cdtIfIpv4VerifyUniRpf'), [('ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB', 'UnicastRpfType', '')])),
                    ('cdtifipv4verifyunirpfacl', (YLeaf(YType.str, 'cdtIfIpv4VerifyUniRpfAcl'), ['str'])),
                    ('cdtifipv4verifyunirpfopts', (YLeaf(YType.bits, 'cdtIfIpv4VerifyUniRpfOpts'), ['Bits'])),
                    ('cdtifipv6enable', (YLeaf(YType.boolean, 'cdtIfIpv6Enable'), ['bool'])),
                    ('cdtifipv6subenable', (YLeaf(YType.boolean, 'cdtIfIpv6SubEnable'), ['bool'])),
                    ('cdtifipv6tcpmssadjust', (YLeaf(YType.uint32, 'cdtIfIpv6TcpMssAdjust'), ['int'])),
                    ('cdtifipv6verifyunirpf', (YLeaf(YType.enumeration, 'cdtIfIpv6VerifyUniRpf'), [('ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB', 'UnicastRpfType', '')])),
                    ('cdtifipv6verifyunirpfacl', (YLeaf(YType.str, 'cdtIfIpv6VerifyUniRpfAcl'), ['str'])),
                    ('cdtifipv6verifyunirpfopts', (YLeaf(YType.bits, 'cdtIfIpv6VerifyUniRpfOpts'), ['Bits'])),
                    ('cdtifipv6ndprefix', (YLeaf(YType.str, 'cdtIfIpv6NdPrefix'), ['str'])),
                    ('cdtifipv6ndprefixlength', (YLeaf(YType.uint32, 'cdtIfIpv6NdPrefixLength'), ['int'])),
                    ('cdtifipv6ndvalidlife', (YLeaf(YType.uint32, 'cdtIfIpv6NdValidLife'), ['int'])),
                    ('cdtifipv6ndpreferredlife', (YLeaf(YType.uint32, 'cdtIfIpv6NdPreferredLife'), ['int'])),
                    ('cdtifipv6ndopts', (YLeaf(YType.bits, 'cdtIfIpv6NdOpts'), ['Bits'])),
                    ('cdtifipv6nddadattempts', (YLeaf(YType.uint32, 'cdtIfIpv6NdDadAttempts'), ['int'])),
                    ('cdtifipv6ndnsinterval', (YLeaf(YType.uint32, 'cdtIfIpv6NdNsInterval'), ['int'])),
                    ('cdtifipv6ndreachabletime', (YLeaf(YType.uint32, 'cdtIfIpv6NdReachableTime'), ['int'])),
                    ('cdtifipv6ndraintervalunits', (YLeaf(YType.enumeration, 'cdtIfIpv6NdRaIntervalUnits'), [('ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CISCODYNAMICTEMPLATEMIB', 'CdtIfTemplateTable.CdtIfTemplateEntry.CdtIfIpv6NdRaIntervalUnits')])),
                    ('cdtifipv6ndraintervalmax', (YLeaf(YType.uint32, 'cdtIfIpv6NdRaIntervalMax'), ['int'])),
                    ('cdtifipv6ndraintervalmin', (YLeaf(YType.uint32, 'cdtIfIpv6NdRaIntervalMin'), ['int'])),
                    ('cdtifipv6ndralife', (YLeaf(YType.uint32, 'cdtIfIpv6NdRaLife'), ['int'])),
                    ('cdtifipv6ndrouterpreference', (YLeaf(YType.enumeration, 'cdtIfIpv6NdRouterPreference'), [('ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CISCODYNAMICTEMPLATEMIB', 'CdtIfTemplateTable.CdtIfTemplateEntry.CdtIfIpv6NdRouterPreference')])),
                ])
                self.cdttemplatename = None
                self.cdtifvalid = Bits()
                self.cdtifmtu = None
                self.cdtifcdpenable = None
                self.cdtifflowmonitor = None
                self.cdtifipv4unnumbered = None
                self.cdtifipv4subenable = None
                self.cdtifipv4mtu = None
                self.cdtifipv4tcpmssadjust = None
                self.cdtifipv4verifyunirpf = None
                self.cdtifipv4verifyunirpfacl = None
                self.cdtifipv4verifyunirpfopts = Bits()
                self.cdtifipv6enable = None
                self.cdtifipv6subenable = None
                self.cdtifipv6tcpmssadjust = None
                self.cdtifipv6verifyunirpf = None
                self.cdtifipv6verifyunirpfacl = None
                self.cdtifipv6verifyunirpfopts = Bits()
                self.cdtifipv6ndprefix = None
                self.cdtifipv6ndprefixlength = None
                self.cdtifipv6ndvalidlife = None
                self.cdtifipv6ndpreferredlife = None
                self.cdtifipv6ndopts = Bits()
                self.cdtifipv6nddadattempts = None
                self.cdtifipv6ndnsinterval = None
                self.cdtifipv6ndreachabletime = None
                self.cdtifipv6ndraintervalunits = None
                self.cdtifipv6ndraintervalmax = None
                self.cdtifipv6ndraintervalmin = None
                self.cdtifipv6ndralife = None
                self.cdtifipv6ndrouterpreference = None
                self._segment_path = lambda: "cdtIfTemplateEntry" + "[cdtTemplateName='" + str(self.cdttemplatename) + "']"
                self._absolute_path = lambda: "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/cdtIfTemplateTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODYNAMICTEMPLATEMIB.CdtIfTemplateTable.CdtIfTemplateEntry, ['cdttemplatename', 'cdtifvalid', 'cdtifmtu', 'cdtifcdpenable', 'cdtifflowmonitor', 'cdtifipv4unnumbered', 'cdtifipv4subenable', 'cdtifipv4mtu', 'cdtifipv4tcpmssadjust', 'cdtifipv4verifyunirpf', 'cdtifipv4verifyunirpfacl', 'cdtifipv4verifyunirpfopts', 'cdtifipv6enable', 'cdtifipv6subenable', 'cdtifipv6tcpmssadjust', 'cdtifipv6verifyunirpf', 'cdtifipv6verifyunirpfacl', 'cdtifipv6verifyunirpfopts', 'cdtifipv6ndprefix', 'cdtifipv6ndprefixlength', 'cdtifipv6ndvalidlife', 'cdtifipv6ndpreferredlife', 'cdtifipv6ndopts', 'cdtifipv6nddadattempts', 'cdtifipv6ndnsinterval', 'cdtifipv6ndreachabletime', 'cdtifipv6ndraintervalunits', 'cdtifipv6ndraintervalmax', 'cdtifipv6ndraintervalmin', 'cdtifipv6ndralife', 'cdtifipv6ndrouterpreference'], name, value)

            class CdtIfIpv6NdRaIntervalUnits(Enum):
                """
                CdtIfIpv6NdRaIntervalUnits (Enum Class)

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


            class CdtIfIpv6NdRouterPreference(Enum):
                """
                CdtIfIpv6NdRouterPreference (Enum Class)

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





    class CdtPppTemplateTable(Entity):
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
        	**type**\: list of  		 :py:class:`CdtPppTemplateEntry <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
        _revision = '2007-09-06'

        def __init__(self):
            super(CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable, self).__init__()

            self.yang_name = "cdtPppTemplateTable"
            self.yang_parent_name = "CISCO-DYNAMIC-TEMPLATE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdtPppTemplateEntry", ("cdtppptemplateentry", CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry))])
            self._leafs = OrderedDict()

            self.cdtppptemplateentry = YList(self)
            self._segment_path = lambda: "cdtPppTemplateTable"
            self._absolute_path = lambda: "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable, [], name, value)


        class CdtPppTemplateEntry(Entity):
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
            
            .. attribute:: cdttemplatename  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..64
            
            	**refers to**\:  :py:class:`cdttemplatename <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateTable.CdtTemplateEntry>`
            
            	**config**\: False
            
            .. attribute:: cdtpppvalid
            
            	This object specifies which attributes in the dynamic template have been configured to valid values.  Each bit in this bit string corresponds to a column in this table.  If the bit is '0', then the value of the corresponding column is not valid.  If the bit is '1', then the value of the corresponding column has been configured to a valid value.  The following list specifies the mappings between bits and the columns\:      accounting              => cdtPppAccounting     authentication          => cdtPppAuthentication     authenticationMethods   => cdtPppAuthenticationMethods     authorization           => cdtPppAuthorization     loopbackIgnore          => cdtPppLoopbackIgnore     maxBadAuth              => cdtPppMaxBadAuth     maxConfigure            => cdtPppMaxConfigure     maxFailure              => cdtPppMaxFailure     maxTerminate            => cdtPppMaxTerminate     timeoutAuthentication   => cdtPppTimeoutAuthentication     timeoutRetry            => cdtPppTimeoutRetry     chapOpts                => cdtPppChapOpts     chapHostname            => cdtPppChapHostname     chapPassword            => cdtPppChapPassword     msChapV1Opts            => cdtPppMsChapV1Opts     msChapV1Hostname        => cdtPppMsChapV1Hostname     msChapV1Password        => cdtPppMsChapV1Password     msChapV2Opts            => cdtPppMsChapV2Opts     msChapV2Hostname        => cdtPppMsChapV2Hostname     msChapV2Password        => cdtPppMsChapV2Password     papOpts                 => cdtPppPapOpts     papSentUsername         => cdtPppPapUsername     papSentPassword         => cdtPppPapPassword     eapOpts                 => cdtPppEapOpts     eapIdentity             => cdtPppEapIdentity     eapPassword             => cdtPppEapPassword     ipcpAddrOption          => cdtPppIpcpAddrOption     ipcpDnsOption           => cdtPppIpcpDnsOption     ipcpDnsPrimary          => cdtPppIpcpDnsPrimary     ipcpDnsSecondary        => cdtPppIpcpDnsSecondary     ipcpWinsOption          => cdtPppIpcpWinsOption     ipcpWinsPrimary         => cdtPppIpcpWinsPrimary     ipcpWinsSecondary       => cdtPppIpcpWinsSecondary     ipcpMaskOption          => cdtPppIpcpMaskOption     ipcpMask                => cdtPppIpcpMask     peerDefIpAddrOpts       => cdtPppPeerOpts     peerDefIpAddrSrc        => cdtPppPeerDefIpAddrSrc     peerDefIpAddr           => cdtPppPeerDefIpAddr
            	**type**\:  :py:class:`CdtPppValid <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppValid>`
            
            	**config**\: False
            
            .. attribute:: cdtpppaccounting
            
            	This object specifies whether the system applies accounting services to the target PPP connection.  This column is valid only if the 'accounting' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cdtpppauthentication
            
            	This object specifies authentication services applied to a target PPP connection and other options affecting authentication services\:      'chap'         This option enables the Challenge Handshake Protocol (CHAP)         on a target PPP connection.      'msChap'         This option enables Microsoft's CHAP on a target PPP         connection.      'msChapV2'         This option enables version 2 of Microsoft's CHAP on a         target PPP connection.      'pap'         This option enables Password Authentication Protocol (PAP)         on a target PPP connection.      'eap'         This option enables Extensible Authentication Protocol (EAP)         on a target PPP connection.      'optional'         This option specifies that the system accepts the connection         even if the peer of a target PPP connection refuses to         accept the authentication methods the system has         requested.      'callin'         This option specifies that authentication should only happen         for incoming calls.      'oneTime'         This option specifies that the system accepts the username         and password in the username field of authentication         responses received on a target PPP connection.  This column is valid only if the 'authentication' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  :py:class:`CdtPppAuthentication <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppAuthentication>`
            
            	**config**\: False
            
            .. attribute:: cdtpppauthenticationmethods
            
            	This object specifies the name of a list of authentication methods used on a target PPP connection.  If the template does not include this attribute, then the system uses the default method list.  This column is valid only if the 'authentication' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdtpppauthorization
            
            	This object specifies whether the system applies authorization services to a target PPP connection.  This column is valid only if the 'authorization' bit of the corresponding instance of cditPppValid is '1'
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cdtppploopbackignore
            
            	This object specifies whether the system ignores loopback on a target PPP connection.  When the system ignores loopback, loopback detection is disabled.  This column is valid only if the 'loopbackIgnore' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cdtpppmaxbadauth
            
            	This object specifies the number of authentication failures allowed by the system before a target PPP connection is reset.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid.  This column is valid only if the 'maxBadAuth' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdtpppmaxconfigure
            
            	This object specifies the number of unacknowledged Configure\-Request messages a target PPP connection can send before the system abandons LCP or NCP negotiations.  This column is valid only if the 'maxConfigure' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cdtpppmaxfailure
            
            	This object specifies the number of Configure\-Nak messages a target PPP connection can receive before the system abandons LCP or NCP negotiations.  This column is valid only if the 'maxFailure' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cdtpppmaxterminate
            
            	This object specifies the number of unacknowledged Terminate\-Request messages a target PPP connection can send before the system abandons LCP or NCP negotiations.  This column is valid only if the 'maxTerminate' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cdtppptimeoutauthentication
            
            	This objects specifies the maximum time the system will wait for a response to an authentication request on a target PPP connection.  This column is valid only if the 'timeoutAuthentication' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: int
            
            	**range:** 1..255
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cdtppptimeoutretry
            
            	This objects specifies the maximum time the system will wait for a response to a PPP control packets on a target PPP connection.  This column is valid only if the 'timeoutRetry' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: int
            
            	**range:** 1..255
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cdtpppchapopts
            
            	This object specifies how the system processes the CHAP on a target PPP connection\:      'refuse'         This option specifies that the system should refuse CHAP         requests from peers of a target PPP connection.      'callin'         This option specifies that the system should only refuse         CHAP requests for incoming calls on a target PPP         connection.  This option is only relevant if the         'refuse' option is set to '1'.      'wait'         This option delays CHAP authentication until after the         peer of a target PPP connection has authenticated itself         to the system.      'encrypted'         This option specifies that the value specified by the         corresponding instance of cdtPppChapPassword is already         encrypted.  This column is valid only if the 'chapOpts' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  :py:class:`CdtPppChapOpts <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppChapOpts>`
            
            	**config**\: False
            
            .. attribute:: cdtpppchaphostname
            
            	This object specifies the hostname sent in a CHAP response on a target PPP connection.  If the template does not include this attribute, then the system uses its assigned hostname.  This column is valid only if the 'chapHostname' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdtpppchappassword
            
            	This object specifies the password used to construct a CHAP response on the target PPP connection.  This column is valid only if the 'chapPassword' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdtpppmschapv1opts
            
            	This object specifies how the system processes version 1 of Microsoft CHAP on a target PPP connection\:      'refuse'         This option specifies that the system should refuse         Microsoft CHAP (v1) requests from peers of a target PPP         connection.      'callin'         This option specifies that the system should only refuse         Microsoft CHAP (v1) requests for incoming calls on a         target PPP connection.  This option is only relevant if         the 'refuse' option is set to '1'.      'wait'         This option delays Microsoft CHAP (v1) authentication         until after the peer of a target PPP connection has         authenticated itself to the system.      'encrypted'         This option specifies that the value specified by the         corresponding instance of cdtPppMsChapV1Password is         already encrypted.  This column is valid only if the 'msChapV1Opts' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  :py:class:`CdtPppMsChapV1Opts <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppMsChapV1Opts>`
            
            	**config**\: False
            
            .. attribute:: cdtpppmschapv1hostname
            
            	This object specifies the hostname sent in a Microsoft CHAP (v1) response on a target PPP connection.  If the template does not include this attribute, then the system uses its assigned hostname.  This column is valid only if the 'msChapV1Hostname' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdtpppmschapv1password
            
            	This object specifies the password used to construct a Microsoft CHAP (v1) response on a target PPP connection.  This column is valid only if the 'msChapV1Password' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdtpppmschapv2opts
            
            	This object specifies how the system processes version 2 of Microsoft CHAP on a target PPP connection\:      'refuse'         This option specifies that the system should refuse         Microsoft CHAP (v2) requests from peers of a target PPP         connection.      'callin'         This option specifies that the system should only refuse         Microsoft CHAP (v2) requests for incoming calls on a         target PPP connection.  This option is only relevant if         the 'refuse' option is set to '1'.      'wait'         This option delays Microsoft CHAP (v2) authentication         until after the peer of a target PPP connection has         authenticated itself to the system.      'encrypted'         This option specifies that the value specified by the         corresponding instance of cdtPppMsChapV2Password is         already encrypted.  This column is valid only if the 'msChapV2Opts' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  :py:class:`CdtPppMsChapV2Opts <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppMsChapV2Opts>`
            
            	**config**\: False
            
            .. attribute:: cdtpppmschapv2hostname
            
            	This object specifies the hostname sent in a Microsoft CHAP (v2) response on a target PPP connection.  If the template does not include this attribute, then the system uses its assigned hostname.  This column is valid only if the 'msChapV2Hostname' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdtpppmschapv2password
            
            	This object specifies the password used to construct a Microsoft CHAP (v2) response on a target PPP connection.  This column is valid only if the 'msChapV2Password' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdtppppapopts
            
            	This object specifies how the system processes the PAP on a target PPP connection\:      'refuse'         This option specifies that the system should refuse PAP         requests from peers of a target PPP connection.      'encrypted'         This option specifies that the value specified by the         corresponding instance of cdtPppPapSentPassword is         already encrypted.  This column is valid only if the 'papOpts' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  :py:class:`CdtPppPapOpts <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppPapOpts>`
            
            	**config**\: False
            
            .. attribute:: cdtppppapusername
            
            	This object specifies the username sent in a PAP response on a target PPP connection.  This column is valid only if the 'papUsername' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdtppppappassword
            
            	This object specifies the username used to construct a PAP response on a target PPP connection.  This column is valid only if the 'papPassword' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdtpppeapopts
            
            	This object specifies how the system processes the EAP on a target PPP connection\:      'refuse'         This option specifies that the system should refuse EAP         requests from peers of a target PPP connection.      'callin'         This option specifies that the system should only refuse EAP         requests for incoming calls on a target PPP connection.         This option is only relevant if the 'refuse' option is         set to '1'.      'wait'         This option delays EAP authentication until after the         peer of a target PPP connection has authenticated itself         to the system.      'local'         This option specifies that the system should locally         authenticate the peer of a target PPP connection,         rather than acting as a proxy to an external AAA server.  This column is valid only if the 'eapOpts' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  :py:class:`CdtPppEapOpts <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppEapOpts>`
            
            	**config**\: False
            
            .. attribute:: cdtpppeapidentity
            
            	This object specifies the identity sent in an EAP response on a target PPP connection.  This column is valid only if the 'eapIdentity' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdtpppeappassword
            
            	This object specifies the password used to construct an EAP response on a target PPP connection.  This column is valid only if the 'eapPassword' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdtpppipcpaddroption
            
            	This object specifies the IPCP address option for a target PPP connection\:      'other'         The implementation of this MIB module does not recognize         the configured IPCP address option.      'accept'         The system accepts any non\-zero IP address from the peer         of a target PPP connection.      'required'         The system disconnects the peer of a target PPP         connection if it could not negotiate an IP address.      'unique'         The system disconnects the peer of a target PPP         connection if the IP address is already in use.  This column is valid only if the 'ipcpAddrOption' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  :py:class:`CdtPppIpcpAddrOption <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppIpcpAddrOption>`
            
            	**config**\: False
            
            .. attribute:: cdtpppipcpdnsoption
            
            	This object specifies the IPCP DNS option for the dynamic interface\:      'other'         The implementation of this MIB module does not recognize         the configured DNS option.      'accept'         The system accepts any non\-zero DNS address form the         peer of a target PPP connection.      'request'         The system requests the DNS address from the peer of a         target PPP connection.      'reject'         The system rejects the DNS option from the peer of a         target PPP connection.  This column is valid only if the 'ipcpDnsOption' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  :py:class:`CdtPppIpcpDnsOption <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppIpcpDnsOption>`
            
            	**config**\: False
            
            .. attribute:: cdtpppipcpdnsprimary
            
            	This object specifies the IP address of the primary DNS server offered to the peer of a target PPP connection.  This column is valid only if the 'ipcpDnsPrimary' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cdtpppipcpdnssecondary
            
            	This object specifies the IP address of the secondary DNS server offered to the peer of a target PPP connection.  This column is valid only if the 'ipcpDnsSecondary' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cdtpppipcpwinsoption
            
            	This object specifies the IPCP WINS option for a target PPP connection\:      'other'         The implementation of this MIB module does not recognize         the configured WINS option.      'accept'         The system accepts any non\-zero WINS address from the         peer of a target PPP connection.      'request'         The system requests the WINS address from the peer of         a target PPP connection.      'reject'         The system rejects the WINS option from the peer of a         target PPP connection.  This column is valid only if the 'ipcpWinsOption' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  :py:class:`CdtPppIpcpWinsOption <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppIpcpWinsOption>`
            
            	**config**\: False
            
            .. attribute:: cdtpppipcpwinsprimary
            
            	This object specifies the IP address of the primary WINS server offered to the peer of a target PPP connection.  This column is valid only if the 'ipcpWinsPrimary' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cdtpppipcpwinssecondary
            
            	This object specifies the IP address of the secondary WINS server offered to the peer of a target PPP connection.  This column is valid only if the 'ipcpWinsSecondary' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cdtpppipcpmaskoption
            
            	This object specifies the IPCP IP subnet mask option for a target PPP connection\:      'other'         The implementation of this MIB module does not recognize         the configured IP subnet mask option.      'request'         The system requests the IP subnet mask from the peer of         a target PPP connection.      'reject'         The system rejects the IP subnet mask option from the         peer of a target PPP connection.  This column is valid only if the 'ipcpMaskOption' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  :py:class:`CdtPppIpcpMaskOption <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppIpcpMaskOption>`
            
            	**config**\: False
            
            .. attribute:: cdtpppipcpmask
            
            	This object specifies the IP address mask offered to the peer of a target PPP connection.  This column is valid only if the 'ipcpMask' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cdtppppeerdefipaddropts
            
            	This object specifies options that affect how the system assigns an IP address to the peer of a target PPP connection\:      'ipAddrForced'         This option forces the system to assign the next         available IP address in the pool to the peer of a         target PPP connection.  When disabled, the peer may         negotiate a specific IP address or the system can assign         the peer its previously assigned IP address.      'matchAaaPools'         This option specifies that the names of the IP address         pools provided by an external AAA server must appear in         the corresponding list of IP address pool specified by         the cdtPppPeerIpAddrPoolTable.      'backupPools'         This option specifies that the corresponding names of         the IP address pools specified by the         cditPppPeerIpAddrPoolTable serve as backup pools to         those provided by an external AAA server.      'staticPools'         This option suppresses an attempt to load pools from an         external AAA server when the system encounters a missing         pool name.  This column is valid only if the 'peerIpAddrOpts' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  :py:class:`CdtPppPeerDefIpAddrOpts <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppPeerDefIpAddrOpts>`
            
            	**config**\: False
            
            .. attribute:: cdtppppeerdefipaddrsrc
            
            	This object specifies how the system assigns an IP address to the peer of a target PPP connection\:      'static'         The system assigns the IP address specified by the         corresponding instance of cdtPppPeerDefIpAddr.      'pool'         The system allocates the first available IP address from         the corresponding list of named pools contained by the         cdtPppPeerIpAddrPoolTable.      'dhcp'         The system acts as a DHCP proxy\-client to obtain an IP         address.  This column is valid only if the 'peerDefIpAddrSrc' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:  :py:class:`CdtPppPeerDefIpAddrSrc <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppPeerDefIpAddrSrc>`
            
            	**config**\: False
            
            .. attribute:: cdtppppeerdefipaddr
            
            	This object specifies the IP address the system assigns to the peer of a target PPP connection.  This column is valid only if the 'peerDefIpAddr' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
            _revision = '2007-09-06'

            def __init__(self):
                super(CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry, self).__init__()

                self.yang_name = "cdtPppTemplateEntry"
                self.yang_parent_name = "cdtPppTemplateTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdttemplatename']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdttemplatename', (YLeaf(YType.str, 'cdtTemplateName'), ['str'])),
                    ('cdtpppvalid', (YLeaf(YType.bits, 'cdtPppValid'), ['Bits'])),
                    ('cdtpppaccounting', (YLeaf(YType.boolean, 'cdtPppAccounting'), ['bool'])),
                    ('cdtpppauthentication', (YLeaf(YType.bits, 'cdtPppAuthentication'), ['Bits'])),
                    ('cdtpppauthenticationmethods', (YLeaf(YType.str, 'cdtPppAuthenticationMethods'), ['str'])),
                    ('cdtpppauthorization', (YLeaf(YType.boolean, 'cdtPppAuthorization'), ['bool'])),
                    ('cdtppploopbackignore', (YLeaf(YType.boolean, 'cdtPppLoopbackIgnore'), ['bool'])),
                    ('cdtpppmaxbadauth', (YLeaf(YType.uint32, 'cdtPppMaxBadAuth'), ['int'])),
                    ('cdtpppmaxconfigure', (YLeaf(YType.uint32, 'cdtPppMaxConfigure'), ['int'])),
                    ('cdtpppmaxfailure', (YLeaf(YType.uint32, 'cdtPppMaxFailure'), ['int'])),
                    ('cdtpppmaxterminate', (YLeaf(YType.uint32, 'cdtPppMaxTerminate'), ['int'])),
                    ('cdtppptimeoutauthentication', (YLeaf(YType.uint32, 'cdtPppTimeoutAuthentication'), ['int'])),
                    ('cdtppptimeoutretry', (YLeaf(YType.uint32, 'cdtPppTimeoutRetry'), ['int'])),
                    ('cdtpppchapopts', (YLeaf(YType.bits, 'cdtPppChapOpts'), ['Bits'])),
                    ('cdtpppchaphostname', (YLeaf(YType.str, 'cdtPppChapHostname'), ['str'])),
                    ('cdtpppchappassword', (YLeaf(YType.str, 'cdtPppChapPassword'), ['str'])),
                    ('cdtpppmschapv1opts', (YLeaf(YType.bits, 'cdtPppMsChapV1Opts'), ['Bits'])),
                    ('cdtpppmschapv1hostname', (YLeaf(YType.str, 'cdtPppMsChapV1Hostname'), ['str'])),
                    ('cdtpppmschapv1password', (YLeaf(YType.str, 'cdtPppMsChapV1Password'), ['str'])),
                    ('cdtpppmschapv2opts', (YLeaf(YType.bits, 'cdtPppMsChapV2Opts'), ['Bits'])),
                    ('cdtpppmschapv2hostname', (YLeaf(YType.str, 'cdtPppMsChapV2Hostname'), ['str'])),
                    ('cdtpppmschapv2password', (YLeaf(YType.str, 'cdtPppMsChapV2Password'), ['str'])),
                    ('cdtppppapopts', (YLeaf(YType.bits, 'cdtPppPapOpts'), ['Bits'])),
                    ('cdtppppapusername', (YLeaf(YType.str, 'cdtPppPapUsername'), ['str'])),
                    ('cdtppppappassword', (YLeaf(YType.str, 'cdtPppPapPassword'), ['str'])),
                    ('cdtpppeapopts', (YLeaf(YType.bits, 'cdtPppEapOpts'), ['Bits'])),
                    ('cdtpppeapidentity', (YLeaf(YType.str, 'cdtPppEapIdentity'), ['str'])),
                    ('cdtpppeappassword', (YLeaf(YType.str, 'cdtPppEapPassword'), ['str'])),
                    ('cdtpppipcpaddroption', (YLeaf(YType.enumeration, 'cdtPppIpcpAddrOption'), [('ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CISCODYNAMICTEMPLATEMIB', 'CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppIpcpAddrOption')])),
                    ('cdtpppipcpdnsoption', (YLeaf(YType.enumeration, 'cdtPppIpcpDnsOption'), [('ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CISCODYNAMICTEMPLATEMIB', 'CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppIpcpDnsOption')])),
                    ('cdtpppipcpdnsprimary', (YLeaf(YType.str, 'cdtPppIpcpDnsPrimary'), ['str'])),
                    ('cdtpppipcpdnssecondary', (YLeaf(YType.str, 'cdtPppIpcpDnsSecondary'), ['str'])),
                    ('cdtpppipcpwinsoption', (YLeaf(YType.enumeration, 'cdtPppIpcpWinsOption'), [('ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CISCODYNAMICTEMPLATEMIB', 'CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppIpcpWinsOption')])),
                    ('cdtpppipcpwinsprimary', (YLeaf(YType.str, 'cdtPppIpcpWinsPrimary'), ['str'])),
                    ('cdtpppipcpwinssecondary', (YLeaf(YType.str, 'cdtPppIpcpWinsSecondary'), ['str'])),
                    ('cdtpppipcpmaskoption', (YLeaf(YType.enumeration, 'cdtPppIpcpMaskOption'), [('ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CISCODYNAMICTEMPLATEMIB', 'CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppIpcpMaskOption')])),
                    ('cdtpppipcpmask', (YLeaf(YType.str, 'cdtPppIpcpMask'), ['str'])),
                    ('cdtppppeerdefipaddropts', (YLeaf(YType.bits, 'cdtPppPeerDefIpAddrOpts'), ['Bits'])),
                    ('cdtppppeerdefipaddrsrc', (YLeaf(YType.enumeration, 'cdtPppPeerDefIpAddrSrc'), [('ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CISCODYNAMICTEMPLATEMIB', 'CdtPppTemplateTable.CdtPppTemplateEntry.CdtPppPeerDefIpAddrSrc')])),
                    ('cdtppppeerdefipaddr', (YLeaf(YType.str, 'cdtPppPeerDefIpAddr'), ['str'])),
                ])
                self.cdttemplatename = None
                self.cdtpppvalid = Bits()
                self.cdtpppaccounting = None
                self.cdtpppauthentication = Bits()
                self.cdtpppauthenticationmethods = None
                self.cdtpppauthorization = None
                self.cdtppploopbackignore = None
                self.cdtpppmaxbadauth = None
                self.cdtpppmaxconfigure = None
                self.cdtpppmaxfailure = None
                self.cdtpppmaxterminate = None
                self.cdtppptimeoutauthentication = None
                self.cdtppptimeoutretry = None
                self.cdtpppchapopts = Bits()
                self.cdtpppchaphostname = None
                self.cdtpppchappassword = None
                self.cdtpppmschapv1opts = Bits()
                self.cdtpppmschapv1hostname = None
                self.cdtpppmschapv1password = None
                self.cdtpppmschapv2opts = Bits()
                self.cdtpppmschapv2hostname = None
                self.cdtpppmschapv2password = None
                self.cdtppppapopts = Bits()
                self.cdtppppapusername = None
                self.cdtppppappassword = None
                self.cdtpppeapopts = Bits()
                self.cdtpppeapidentity = None
                self.cdtpppeappassword = None
                self.cdtpppipcpaddroption = None
                self.cdtpppipcpdnsoption = None
                self.cdtpppipcpdnsprimary = None
                self.cdtpppipcpdnssecondary = None
                self.cdtpppipcpwinsoption = None
                self.cdtpppipcpwinsprimary = None
                self.cdtpppipcpwinssecondary = None
                self.cdtpppipcpmaskoption = None
                self.cdtpppipcpmask = None
                self.cdtppppeerdefipaddropts = Bits()
                self.cdtppppeerdefipaddrsrc = None
                self.cdtppppeerdefipaddr = None
                self._segment_path = lambda: "cdtPppTemplateEntry" + "[cdtTemplateName='" + str(self.cdttemplatename) + "']"
                self._absolute_path = lambda: "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/cdtPppTemplateTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODYNAMICTEMPLATEMIB.CdtPppTemplateTable.CdtPppTemplateEntry, ['cdttemplatename', 'cdtpppvalid', 'cdtpppaccounting', 'cdtpppauthentication', 'cdtpppauthenticationmethods', 'cdtpppauthorization', 'cdtppploopbackignore', 'cdtpppmaxbadauth', 'cdtpppmaxconfigure', 'cdtpppmaxfailure', 'cdtpppmaxterminate', 'cdtppptimeoutauthentication', 'cdtppptimeoutretry', 'cdtpppchapopts', 'cdtpppchaphostname', 'cdtpppchappassword', 'cdtpppmschapv1opts', 'cdtpppmschapv1hostname', 'cdtpppmschapv1password', 'cdtpppmschapv2opts', 'cdtpppmschapv2hostname', 'cdtpppmschapv2password', 'cdtppppapopts', 'cdtppppapusername', 'cdtppppappassword', 'cdtpppeapopts', 'cdtpppeapidentity', 'cdtpppeappassword', 'cdtpppipcpaddroption', 'cdtpppipcpdnsoption', 'cdtpppipcpdnsprimary', 'cdtpppipcpdnssecondary', 'cdtpppipcpwinsoption', 'cdtpppipcpwinsprimary', 'cdtpppipcpwinssecondary', 'cdtpppipcpmaskoption', 'cdtpppipcpmask', 'cdtppppeerdefipaddropts', 'cdtppppeerdefipaddrsrc', 'cdtppppeerdefipaddr'], name, value)

            class CdtPppIpcpAddrOption(Enum):
                """
                CdtPppIpcpAddrOption (Enum Class)

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


            class CdtPppIpcpDnsOption(Enum):
                """
                CdtPppIpcpDnsOption (Enum Class)

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


            class CdtPppIpcpMaskOption(Enum):
                """
                CdtPppIpcpMaskOption (Enum Class)

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


            class CdtPppIpcpWinsOption(Enum):
                """
                CdtPppIpcpWinsOption (Enum Class)

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


            class CdtPppPeerDefIpAddrSrc(Enum):
                """
                CdtPppPeerDefIpAddrSrc (Enum Class)

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





    class CdtPppPeerIpAddrPoolTable(Entity):
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
        	**type**\: list of  		 :py:class:`CdtPppPeerIpAddrPoolEntry <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtPppPeerIpAddrPoolTable.CdtPppPeerIpAddrPoolEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
        _revision = '2007-09-06'

        def __init__(self):
            super(CISCODYNAMICTEMPLATEMIB.CdtPppPeerIpAddrPoolTable, self).__init__()

            self.yang_name = "cdtPppPeerIpAddrPoolTable"
            self.yang_parent_name = "CISCO-DYNAMIC-TEMPLATE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdtPppPeerIpAddrPoolEntry", ("cdtppppeeripaddrpoolentry", CISCODYNAMICTEMPLATEMIB.CdtPppPeerIpAddrPoolTable.CdtPppPeerIpAddrPoolEntry))])
            self._leafs = OrderedDict()

            self.cdtppppeeripaddrpoolentry = YList(self)
            self._segment_path = lambda: "cdtPppPeerIpAddrPoolTable"
            self._absolute_path = lambda: "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODYNAMICTEMPLATEMIB.CdtPppPeerIpAddrPoolTable, [], name, value)


        class CdtPppPeerIpAddrPoolEntry(Entity):
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
            
            .. attribute:: cdttemplatename  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..64
            
            	**refers to**\:  :py:class:`cdttemplatename <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateTable.CdtTemplateEntry>`
            
            	**config**\: False
            
            .. attribute:: cdtppppeeripaddrpoolpriority  (key)
            
            	This object indicates the relative priority of the named pool in the list corresponding to a PPP template.  The system searches pools in the order of priority, where lower values represent higher priority
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cdtppppeeripaddrpoolstatus
            
            	This object specifies the status of the entry.  The following columns must be valid before activating a subscriber access profile\:      \- cdtPppPeerIpAddrPoolStorage     \- cdtPppPeerIpAddrPoolName  However, these objects specify a default value.  Thus, it is possible to use create\-and\-go semantics without setting any additional columns.  An implementation must not allow the EMS/NMS to create an entry if the corresponding instance of cdtPppPeerIpAddrSrc is not 'pool'.  An implementation must allow the EMS/NMS to modify any column when this column is 'active'
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: cdtppppeeripaddrpoolstorage
            
            	This object specifies what happens to the name pool entry upon restart.  If the corresponding instance of cdtTemplateSrc is not 'local', then this column must be 'volatile'
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            	**config**\: False
            
            .. attribute:: cdtppppeeripaddrpoolname
            
            	This object specifies the name of the IP address pool associated with the PPP template
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
            _revision = '2007-09-06'

            def __init__(self):
                super(CISCODYNAMICTEMPLATEMIB.CdtPppPeerIpAddrPoolTable.CdtPppPeerIpAddrPoolEntry, self).__init__()

                self.yang_name = "cdtPppPeerIpAddrPoolEntry"
                self.yang_parent_name = "cdtPppPeerIpAddrPoolTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdttemplatename','cdtppppeeripaddrpoolpriority']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdttemplatename', (YLeaf(YType.str, 'cdtTemplateName'), ['str'])),
                    ('cdtppppeeripaddrpoolpriority', (YLeaf(YType.uint32, 'cdtPppPeerIpAddrPoolPriority'), ['int'])),
                    ('cdtppppeeripaddrpoolstatus', (YLeaf(YType.enumeration, 'cdtPppPeerIpAddrPoolStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('cdtppppeeripaddrpoolstorage', (YLeaf(YType.enumeration, 'cdtPppPeerIpAddrPoolStorage'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('cdtppppeeripaddrpoolname', (YLeaf(YType.str, 'cdtPppPeerIpAddrPoolName'), ['str'])),
                ])
                self.cdttemplatename = None
                self.cdtppppeeripaddrpoolpriority = None
                self.cdtppppeeripaddrpoolstatus = None
                self.cdtppppeeripaddrpoolstorage = None
                self.cdtppppeeripaddrpoolname = None
                self._segment_path = lambda: "cdtPppPeerIpAddrPoolEntry" + "[cdtTemplateName='" + str(self.cdttemplatename) + "']" + "[cdtPppPeerIpAddrPoolPriority='" + str(self.cdtppppeeripaddrpoolpriority) + "']"
                self._absolute_path = lambda: "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/cdtPppPeerIpAddrPoolTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODYNAMICTEMPLATEMIB.CdtPppPeerIpAddrPoolTable.CdtPppPeerIpAddrPoolEntry, ['cdttemplatename', 'cdtppppeeripaddrpoolpriority', 'cdtppppeeripaddrpoolstatus', 'cdtppppeeripaddrpoolstorage', 'cdtppppeeripaddrpoolname'], name, value)




    class CdtEthernetTemplateTable(Entity):
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
        	**type**\: list of  		 :py:class:`CdtEthernetTemplateEntry <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtEthernetTemplateTable.CdtEthernetTemplateEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
        _revision = '2007-09-06'

        def __init__(self):
            super(CISCODYNAMICTEMPLATEMIB.CdtEthernetTemplateTable, self).__init__()

            self.yang_name = "cdtEthernetTemplateTable"
            self.yang_parent_name = "CISCO-DYNAMIC-TEMPLATE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdtEthernetTemplateEntry", ("cdtethernettemplateentry", CISCODYNAMICTEMPLATEMIB.CdtEthernetTemplateTable.CdtEthernetTemplateEntry))])
            self._leafs = OrderedDict()

            self.cdtethernettemplateentry = YList(self)
            self._segment_path = lambda: "cdtEthernetTemplateTable"
            self._absolute_path = lambda: "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODYNAMICTEMPLATEMIB.CdtEthernetTemplateTable, [], name, value)


        class CdtEthernetTemplateEntry(Entity):
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
            
            .. attribute:: cdttemplatename  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..64
            
            	**refers to**\:  :py:class:`cdttemplatename <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateTable.CdtTemplateEntry>`
            
            	**config**\: False
            
            .. attribute:: cdtethernetvalid
            
            	This object specifies which attributes in the dynamic template have been configured to valid values.  Each bit in this bit string corresponds to a column in this table.  If the bit is '0', then the value of the corresponding column is not valid.  If the bit is '1', then the value of the corresponding column has been configured to a valid value.  The following list specifies the mappings between bits and the columns\:      bridgeDomain     => cdtEthernetBridgeDomain     pppoeEnable      => cdtEthernetPppoeEnable     ipv4PointToPoint => cdtEthernetIpv4PointToPoint     macAddr          => cdtEthernetMacAddr
            	**type**\:  :py:class:`CdtEthernetValid <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtEthernetTemplateTable.CdtEthernetTemplateEntry.CdtEthernetValid>`
            
            	**config**\: False
            
            .. attribute:: cdtethernetbridgedomain
            
            	This object specifies the name of the bridge domain..
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdtethernetpppoeenable
            
            	This object specifies whether..
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cdtethernetipv4pointtopoint
            
            	This object specifies whether..
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cdtethernetmacaddr
            
            	This object specifies the..
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
            _revision = '2007-09-06'

            def __init__(self):
                super(CISCODYNAMICTEMPLATEMIB.CdtEthernetTemplateTable.CdtEthernetTemplateEntry, self).__init__()

                self.yang_name = "cdtEthernetTemplateEntry"
                self.yang_parent_name = "cdtEthernetTemplateTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdttemplatename']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdttemplatename', (YLeaf(YType.str, 'cdtTemplateName'), ['str'])),
                    ('cdtethernetvalid', (YLeaf(YType.bits, 'cdtEthernetValid'), ['Bits'])),
                    ('cdtethernetbridgedomain', (YLeaf(YType.str, 'cdtEthernetBridgeDomain'), ['str'])),
                    ('cdtethernetpppoeenable', (YLeaf(YType.boolean, 'cdtEthernetPppoeEnable'), ['bool'])),
                    ('cdtethernetipv4pointtopoint', (YLeaf(YType.boolean, 'cdtEthernetIpv4PointToPoint'), ['bool'])),
                    ('cdtethernetmacaddr', (YLeaf(YType.str, 'cdtEthernetMacAddr'), ['str'])),
                ])
                self.cdttemplatename = None
                self.cdtethernetvalid = Bits()
                self.cdtethernetbridgedomain = None
                self.cdtethernetpppoeenable = None
                self.cdtethernetipv4pointtopoint = None
                self.cdtethernetmacaddr = None
                self._segment_path = lambda: "cdtEthernetTemplateEntry" + "[cdtTemplateName='" + str(self.cdttemplatename) + "']"
                self._absolute_path = lambda: "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/cdtEthernetTemplateTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODYNAMICTEMPLATEMIB.CdtEthernetTemplateTable.CdtEthernetTemplateEntry, ['cdttemplatename', 'cdtethernetvalid', 'cdtethernetbridgedomain', 'cdtethernetpppoeenable', 'cdtethernetipv4pointtopoint', 'cdtethernetmacaddr'], name, value)




    class CdtSrvTemplateTable(Entity):
        """
        This table contains attributes relating to a service.
        
        This table has a sparse\-dependent relationship on the
        cdtTemplateTable, containing a row for each dynamic template
        having a cdtTemplateType of one of the following values\:
        
            'derived'
            'service'
        
        .. attribute:: cdtsrvtemplateentry
        
        	An entry containing attributes relating to a service.  The system automatically creates entry when the system or the EMS/NMS creates a row in the cdtTemplateTable with a cdtTemplateType of one of the following values\:      'derived'     'service'  Likewise, the system automatically destroys an entry when the system or the EMS/NMS destroys the corresponding row in the cdtTemplateTable
        	**type**\: list of  		 :py:class:`CdtSrvTemplateEntry <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtSrvTemplateTable.CdtSrvTemplateEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
        _revision = '2007-09-06'

        def __init__(self):
            super(CISCODYNAMICTEMPLATEMIB.CdtSrvTemplateTable, self).__init__()

            self.yang_name = "cdtSrvTemplateTable"
            self.yang_parent_name = "CISCO-DYNAMIC-TEMPLATE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdtSrvTemplateEntry", ("cdtsrvtemplateentry", CISCODYNAMICTEMPLATEMIB.CdtSrvTemplateTable.CdtSrvTemplateEntry))])
            self._leafs = OrderedDict()

            self.cdtsrvtemplateentry = YList(self)
            self._segment_path = lambda: "cdtSrvTemplateTable"
            self._absolute_path = lambda: "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODYNAMICTEMPLATEMIB.CdtSrvTemplateTable, [], name, value)


        class CdtSrvTemplateEntry(Entity):
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
            
            .. attribute:: cdttemplatename  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..64
            
            	**refers to**\:  :py:class:`cdttemplatename <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtTemplateTable.CdtTemplateEntry>`
            
            	**config**\: False
            
            .. attribute:: cdtsrvvalid
            
            	This object specifies which attributes in the dynamic template have been configured to valid values.  Each bit in this bit string corresponds to a column in this table.  If the bit is '0', then the value of the corresponding column is not valid.  If the bit is '1', then the value of the corresponding column has been configured to a valid value.  The following list specifies the mappings between bits and the columns\:      networkSrv     => cdtSrvNetworkSrv     vpdnGroup      => cdtSrvVpdnGroup     sgSrvGroup     => cdtSrvGroup     sgSrvType      => cdtSrvSgSrvType     multicast      => cdtSrvMulticast
            	**type**\:  :py:class:`CdtSrvValid <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtSrvTemplateTable.CdtSrvTemplateEntry.CdtSrvValid>`
            
            	**config**\: False
            
            .. attribute:: cdtsrvnetworksrv
            
            	This object specifies the type of network service provided by the target service\:      'other'         The implementation of this MIB module does not recognize         the configured network service.      'none'         The target subscriber service does not provide a network         service to subscribers sessions.      'local'         The target subscriber service provides local termination         for subscriber sessions.      'vpdn'         The target subscriber service provides a Virtual Private         Dialup Network service for subscriber sessions.  This column is valid only if the 'networkSrv' bit of the corresponding instance of cdtSrvValid is '1'
            	**type**\:  :py:class:`CdtSrvNetworkSrv <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtSrvTemplateTable.CdtSrvTemplateEntry.CdtSrvNetworkSrv>`
            
            	**config**\: False
            
            .. attribute:: cdtsrvvpdngroup
            
            	This object specifies the name of the VPDN group used to configure the network service.  This column is valid only if the 'vpdnGroup' bit of the corresponding instance of cdtSrvValid is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdtsrvsgsrvgroup
            
            	This object specifies the name of the service group with which the system associates subscriber sessions.  A service group specifies a set of services that may be active simultaneously for a given subscriber session.  Typically, a service group contains a primary service and one or more secondary services.  This column is valid only if the 'sgSrvGroup' bit of the corresponding instance of cdtSrvValid is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdtsrvsgsrvtype
            
            	This object specifies whether the target service specifies a network\-forwarding policy\:      'primary'         The target service specifies a network\-forwarding         policy.  Primary services are mutually exclusive; that         is, only one primary service can be activated for any         given subscriber session.      'secondary'         The target service has a dependence on the primary         service in the group specified by the corresponding         instance of cdtSuBSrvSgSrvGroup.  After the system         activates the primary service, it activates secondary         services.  When the system deactivates the primary         service, then it deactivates all the secondary services         in the service group.  This column is valid only if the 'sgSrvType' bit of the corresponding instance of cdtSrvValid is '1'
            	**type**\:  :py:class:`CdtSrvSgSrvType <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CISCODYNAMICTEMPLATEMIB.CdtSrvTemplateTable.CdtSrvTemplateEntry.CdtSrvSgSrvType>`
            
            	**config**\: False
            
            .. attribute:: cdtsrvmulticast
            
            	This objects specifies whether the system enables multicast service for subscriber sessions of the target service.  This column is valid only if the 'sgSrvMcastRoutingIf' bit of the corresponding instance of cdtSrvValid is '1'
            	**type**\: bool
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
            _revision = '2007-09-06'

            def __init__(self):
                super(CISCODYNAMICTEMPLATEMIB.CdtSrvTemplateTable.CdtSrvTemplateEntry, self).__init__()

                self.yang_name = "cdtSrvTemplateEntry"
                self.yang_parent_name = "cdtSrvTemplateTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdttemplatename']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdttemplatename', (YLeaf(YType.str, 'cdtTemplateName'), ['str'])),
                    ('cdtsrvvalid', (YLeaf(YType.bits, 'cdtSrvValid'), ['Bits'])),
                    ('cdtsrvnetworksrv', (YLeaf(YType.enumeration, 'cdtSrvNetworkSrv'), [('ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CISCODYNAMICTEMPLATEMIB', 'CdtSrvTemplateTable.CdtSrvTemplateEntry.CdtSrvNetworkSrv')])),
                    ('cdtsrvvpdngroup', (YLeaf(YType.str, 'cdtSrvVpdnGroup'), ['str'])),
                    ('cdtsrvsgsrvgroup', (YLeaf(YType.str, 'cdtSrvSgSrvGroup'), ['str'])),
                    ('cdtsrvsgsrvtype', (YLeaf(YType.enumeration, 'cdtSrvSgSrvType'), [('ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB', 'CISCODYNAMICTEMPLATEMIB', 'CdtSrvTemplateTable.CdtSrvTemplateEntry.CdtSrvSgSrvType')])),
                    ('cdtsrvmulticast', (YLeaf(YType.boolean, 'cdtSrvMulticast'), ['bool'])),
                ])
                self.cdttemplatename = None
                self.cdtsrvvalid = Bits()
                self.cdtsrvnetworksrv = None
                self.cdtsrvvpdngroup = None
                self.cdtsrvsgsrvgroup = None
                self.cdtsrvsgsrvtype = None
                self.cdtsrvmulticast = None
                self._segment_path = lambda: "cdtSrvTemplateEntry" + "[cdtTemplateName='" + str(self.cdttemplatename) + "']"
                self._absolute_path = lambda: "CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/cdtSrvTemplateTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODYNAMICTEMPLATEMIB.CdtSrvTemplateTable.CdtSrvTemplateEntry, ['cdttemplatename', 'cdtsrvvalid', 'cdtsrvnetworksrv', 'cdtsrvvpdngroup', 'cdtsrvsgsrvgroup', 'cdtsrvsgsrvtype', 'cdtsrvmulticast'], name, value)

            class CdtSrvNetworkSrv(Enum):
                """
                CdtSrvNetworkSrv (Enum Class)

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


            class CdtSrvSgSrvType(Enum):
                """
                CdtSrvSgSrvType (Enum Class)

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




    def clone_ptr(self):
        self._top_entity = CISCODYNAMICTEMPLATEMIB()
        return self._top_entity




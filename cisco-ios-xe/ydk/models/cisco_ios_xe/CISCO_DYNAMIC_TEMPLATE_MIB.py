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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoDynamicTemplateMib(object):
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
        self.cdtethernettemplatetable = CiscoDynamicTemplateMib.Cdtethernettemplatetable()
        self.cdtethernettemplatetable.parent = self
        self.cdtiftemplatetable = CiscoDynamicTemplateMib.Cdtiftemplatetable()
        self.cdtiftemplatetable.parent = self
        self.cdtppppeeripaddrpooltable = CiscoDynamicTemplateMib.Cdtppppeeripaddrpooltable()
        self.cdtppppeeripaddrpooltable.parent = self
        self.cdtppptemplatetable = CiscoDynamicTemplateMib.Cdtppptemplatetable()
        self.cdtppptemplatetable.parent = self
        self.cdtsrvtemplatetable = CiscoDynamicTemplateMib.Cdtsrvtemplatetable()
        self.cdtsrvtemplatetable.parent = self
        self.cdttemplateassociationtable = CiscoDynamicTemplateMib.Cdttemplateassociationtable()
        self.cdttemplateassociationtable.parent = self
        self.cdttemplatecommontable = CiscoDynamicTemplateMib.Cdttemplatecommontable()
        self.cdttemplatecommontable.parent = self
        self.cdttemplatetable = CiscoDynamicTemplateMib.Cdttemplatetable()
        self.cdttemplatetable.parent = self
        self.cdttemplatetargettable = CiscoDynamicTemplateMib.Cdttemplatetargettable()
        self.cdttemplatetargettable.parent = self
        self.cdttemplateusagetable = CiscoDynamicTemplateMib.Cdttemplateusagetable()
        self.cdttemplateusagetable.parent = self


    class Cdttemplatetable(object):
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
            self.parent = None
            self.cdttemplateentry = YList()
            self.cdttemplateentry.parent = self
            self.cdttemplateentry.name = 'cdttemplateentry'


        class Cdttemplateentry(object):
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
            	**type**\:   :py:class:`CdttemplatesrcEnum <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdttemplatetable.Cdttemplateentry.CdttemplatesrcEnum>`
            
            .. attribute:: cdttemplatestatus
            
            	This object specifies the status of the dynamic template.  The following columns must be valid before activating a dynamic template\:      \- cdtTemplateStorage     \- cdtTemplateType  However, these objects specify a default value.  Thus, it is possible to use create\-and\-go semantics without setting any additional columns.  An implementation must allow the EMS/NMS to modify any column when this column is 'active', including columns defined in tables that have a one\-to\-one or sparse dependent relationship on this table
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: cdttemplatestorage
            
            	This object specifies what happens to the dynamic template upon restart.  If the corresponding instance of cdtTemplateSrc is not 'local', then this column must be 'volatile'
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            .. attribute:: cdttemplatetype
            
            	This object indicates the types of dynamic template
            	**type**\:   :py:class:`DynamictemplatetypeEnum <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_TC_MIB.DynamictemplatetypeEnum>`
            
            .. attribute:: cdttemplateusagecount
            
            	This object specifies the number of targets using a dynamic template
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
            _revision = '2007-09-06'

            def __init__(self):
                self.parent = None
                self.cdttemplatename = None
                self.cdttemplatesrc = None
                self.cdttemplatestatus = None
                self.cdttemplatestorage = None
                self.cdttemplatetype = None
                self.cdttemplateusagecount = None

            class CdttemplatesrcEnum(Enum):
                """
                CdttemplatesrcEnum

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

                other = 1

                derived = 2

                local = 3

                aaaUserProfile = 4

                aaaServiceProfile = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                    return meta._meta_table['CiscoDynamicTemplateMib.Cdttemplatetable.Cdttemplateentry.CdttemplatesrcEnum']


            @property
            def _common_path(self):
                if self.cdttemplatename is None:
                    raise YPYModelError('Key property cdttemplatename is None')

                return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateTable/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateEntry[CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateName = ' + str(self.cdttemplatename) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cdttemplatename is not None:
                    return True

                if self.cdttemplatesrc is not None:
                    return True

                if self.cdttemplatestatus is not None:
                    return True

                if self.cdttemplatestorage is not None:
                    return True

                if self.cdttemplatetype is not None:
                    return True

                if self.cdttemplateusagecount is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                return meta._meta_table['CiscoDynamicTemplateMib.Cdttemplatetable.Cdttemplateentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cdttemplateentry is not None:
                for child_ref in self.cdttemplateentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
            return meta._meta_table['CiscoDynamicTemplateMib.Cdttemplatetable']['meta_info']


    class Cdttemplatetargettable(object):
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
            self.parent = None
            self.cdttemplatetargetentry = YList()
            self.cdttemplatetargetentry.parent = self
            self.cdttemplatetargetentry.name = 'cdttemplatetargetentry'


        class Cdttemplatetargetentry(object):
            """
            An entry describes a target associated with one or more
            dynamic templates.
            
            The system automatically creates an entry when it associates a
            dynamic template to a target.  Likewise, the system
            automatically destroys an entry when a target no longer has any
            associated dynamic templates.
            
            .. attribute:: cdttemplatetargettype  <key>
            
            	This object indicates the type of target
            	**type**\:   :py:class:`DynamictemplatetargettypeEnum <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_TC_MIB.DynamictemplatetargettypeEnum>`
            
            .. attribute:: cdttemplatetargetid  <key>
            
            	This object uniquely identifies the target within the scope of its type
            	**type**\:  str
            
            	**length:** 1..20
            
            .. attribute:: cdttemplatetargetstatus
            
            	This object specifies the status of the dynamic template target.  The following columns must be valid before activating a subscriber access profile\:      \- cdtTemplateTargetStorage  However, these objects specify a default value.  Thus, it is possible to use create\-and\-go semantics without setting any additional columns.  An implementation must allow the EMS/NMS to modify any column when this column is 'active', including columns defined in tables that have a one\-to\-one or sparse dependent relationship on this table
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: cdttemplatetargetstorage
            
            	This object specifies what happens to the dynamic template target upon restart
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            

            """

            _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
            _revision = '2007-09-06'

            def __init__(self):
                self.parent = None
                self.cdttemplatetargettype = None
                self.cdttemplatetargetid = None
                self.cdttemplatetargetstatus = None
                self.cdttemplatetargetstorage = None

            @property
            def _common_path(self):
                if self.cdttemplatetargettype is None:
                    raise YPYModelError('Key property cdttemplatetargettype is None')
                if self.cdttemplatetargetid is None:
                    raise YPYModelError('Key property cdttemplatetargetid is None')

                return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateTargetTable/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateTargetEntry[CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateTargetType = ' + str(self.cdttemplatetargettype) + '][CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateTargetId = ' + str(self.cdttemplatetargetid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cdttemplatetargettype is not None:
                    return True

                if self.cdttemplatetargetid is not None:
                    return True

                if self.cdttemplatetargetstatus is not None:
                    return True

                if self.cdttemplatetargetstorage is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                return meta._meta_table['CiscoDynamicTemplateMib.Cdttemplatetargettable.Cdttemplatetargetentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateTargetTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cdttemplatetargetentry is not None:
                for child_ref in self.cdttemplatetargetentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
            return meta._meta_table['CiscoDynamicTemplateMib.Cdttemplatetargettable']['meta_info']


    class Cdttemplateassociationtable(object):
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
            self.parent = None
            self.cdttemplateassociationentry = YList()
            self.cdttemplateassociationentry.parent = self
            self.cdttemplateassociationentry.name = 'cdttemplateassociationentry'


        class Cdttemplateassociationentry(object):
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
            
            	
            	**type**\:   :py:class:`DynamictemplatetargettypeEnum <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_TC_MIB.DynamictemplatetargettypeEnum>`
            
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
                self.parent = None
                self.cdttemplatetargettype = None
                self.cdttemplatetargetid = None
                self.cdttemplateassociationname = None
                self.cdttemplateassociationprecedence = None

            @property
            def _common_path(self):
                if self.cdttemplatetargettype is None:
                    raise YPYModelError('Key property cdttemplatetargettype is None')
                if self.cdttemplatetargetid is None:
                    raise YPYModelError('Key property cdttemplatetargetid is None')
                if self.cdttemplateassociationname is None:
                    raise YPYModelError('Key property cdttemplateassociationname is None')

                return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateAssociationTable/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateAssociationEntry[CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateTargetType = ' + str(self.cdttemplatetargettype) + '][CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateTargetId = ' + str(self.cdttemplatetargetid) + '][CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateAssociationName = ' + str(self.cdttemplateassociationname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cdttemplatetargettype is not None:
                    return True

                if self.cdttemplatetargetid is not None:
                    return True

                if self.cdttemplateassociationname is not None:
                    return True

                if self.cdttemplateassociationprecedence is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                return meta._meta_table['CiscoDynamicTemplateMib.Cdttemplateassociationtable.Cdttemplateassociationentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateAssociationTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cdttemplateassociationentry is not None:
                for child_ref in self.cdttemplateassociationentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
            return meta._meta_table['CiscoDynamicTemplateMib.Cdttemplateassociationtable']['meta_info']


    class Cdttemplateusagetable(object):
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
            self.parent = None
            self.cdttemplateusageentry = YList()
            self.cdttemplateusageentry.parent = self
            self.cdttemplateusageentry.name = 'cdttemplateusageentry'


        class Cdttemplateusageentry(object):
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
            	**type**\:   :py:class:`DynamictemplatetargettypeEnum <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_TC_MIB.DynamictemplatetargettypeEnum>`
            
            .. attribute:: cdttemplateusagetargetid  <key>
            
            	This object indicates the name of the target using the dynamic template
            	**type**\:  str
            
            	**length:** 1..20
            
            

            """

            _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
            _revision = '2007-09-06'

            def __init__(self):
                self.parent = None
                self.cdttemplatename = None
                self.cdttemplateusagetargettype = None
                self.cdttemplateusagetargetid = None

            @property
            def _common_path(self):
                if self.cdttemplatename is None:
                    raise YPYModelError('Key property cdttemplatename is None')
                if self.cdttemplateusagetargettype is None:
                    raise YPYModelError('Key property cdttemplateusagetargettype is None')
                if self.cdttemplateusagetargetid is None:
                    raise YPYModelError('Key property cdttemplateusagetargetid is None')

                return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateUsageTable/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateUsageEntry[CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateName = ' + str(self.cdttemplatename) + '][CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateUsageTargetType = ' + str(self.cdttemplateusagetargettype) + '][CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateUsageTargetId = ' + str(self.cdttemplateusagetargetid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cdttemplatename is not None:
                    return True

                if self.cdttemplateusagetargettype is not None:
                    return True

                if self.cdttemplateusagetargetid is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                return meta._meta_table['CiscoDynamicTemplateMib.Cdttemplateusagetable.Cdttemplateusageentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateUsageTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cdttemplateusageentry is not None:
                for child_ref in self.cdttemplateusageentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
            return meta._meta_table['CiscoDynamicTemplateMib.Cdttemplateusagetable']['meta_info']


    class Cdttemplatecommontable(object):
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
            self.parent = None
            self.cdttemplatecommonentry = YList()
            self.cdttemplatecommonentry.parent = self
            self.cdttemplatecommonentry.name = 'cdttemplatecommonentry'


        class Cdttemplatecommonentry(object):
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
                self.parent = None
                self.cdttemplatename = None
                self.cdtcommonaddrpool = None
                self.cdtcommondescr = None
                self.cdtcommonipv4accessgroup = None
                self.cdtcommonipv4unreachables = None
                self.cdtcommonipv6accessgroup = None
                self.cdtcommonipv6unreachables = None
                self.cdtcommonkeepaliveint = None
                self.cdtcommonkeepaliveretries = None
                self.cdtcommonsrvacct = None
                self.cdtcommonsrvnetflow = None
                self.cdtcommonsrvqos = None
                self.cdtcommonsrvredirect = None
                self.cdtcommonsrvsubcontrol = None
                self.cdtcommonvalid = CiscoDynamicTemplateMib.Cdttemplatecommontable.Cdttemplatecommonentry.Cdtcommonvalid()
                self.cdtcommonvrf = None

            class Cdtcommonvalid(FixedBitsDict):
                """
                Cdtcommonvalid

                This object specifies which attributes in the dynamic template
                have been configured to valid values.
                
                Each bit in this bit string corresponds to a column in this
                table.  If the bit is '0', then the value of the corresponding
                column is not valid.  If the bit is '1', then the value of the
                corresponding column has been configured to a valid value.
                
                The following list specifies the mappings between bits and the
                columns\:
                
                    'descr'             => cdtCommonDescr
                    'keepaliveInt'      => cdtCommonKeepaliveInt
                    'keepaliveRetries'  => cdtCommonKeepaliveRetries
                    'vrf'               => cdtCommonVrf
                    'addrPool'          => cdtCommonAddrPool
                    'ipv4AccessGroup'   => cdtCommonIpv4AccessGroup
                    'ipv4Unreachables'  => cdtCommonIpv4Unreachables
                    'ipv6AccessGroup'   => cdtCommonIpv6AccessGroup
                    'ipv6Unreachables'  => cdtCommonIpv6Unreachables
                    'srvSubControl'     => cdtCommonSrvSubControl
                    'srvRedirect'       => cdtCommonSrvRedirect
                    'srvAcct'           => cdtCommonSrvAcct
                    'srvQos'            => cdtCommonSrvQos
                    'srvNetflow'        => cdtCommonSrvNetflow
                Keys are:- srvQos , srvAcct , ipv4AccessGroup , srvNetflow , ipv4Unreachables , addrPool , ipv6Unreachables , vrf , srvRedirect , descr , srvSubControl , keepalive , ipv6AccessGroup

                """

                def __init__(self):
                    self._dictionary = { 
                        'srvQos':False,
                        'srvAcct':False,
                        'ipv4AccessGroup':False,
                        'srvNetflow':False,
                        'ipv4Unreachables':False,
                        'addrPool':False,
                        'ipv6Unreachables':False,
                        'vrf':False,
                        'srvRedirect':False,
                        'descr':False,
                        'srvSubControl':False,
                        'keepalive':False,
                        'ipv6AccessGroup':False,
                    }
                    self._pos_map = { 
                        'srvQos':11,
                        'srvAcct':10,
                        'ipv4AccessGroup':4,
                        'srvNetflow':12,
                        'ipv4Unreachables':5,
                        'addrPool':3,
                        'ipv6Unreachables':7,
                        'vrf':2,
                        'srvRedirect':9,
                        'descr':0,
                        'srvSubControl':8,
                        'keepalive':1,
                        'ipv6AccessGroup':6,
                    }

            @property
            def _common_path(self):
                if self.cdttemplatename is None:
                    raise YPYModelError('Key property cdttemplatename is None')

                return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateCommonTable/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateCommonEntry[CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateName = ' + str(self.cdttemplatename) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cdttemplatename is not None:
                    return True

                if self.cdtcommonaddrpool is not None:
                    return True

                if self.cdtcommondescr is not None:
                    return True

                if self.cdtcommonipv4accessgroup is not None:
                    return True

                if self.cdtcommonipv4unreachables is not None:
                    return True

                if self.cdtcommonipv6accessgroup is not None:
                    return True

                if self.cdtcommonipv6unreachables is not None:
                    return True

                if self.cdtcommonkeepaliveint is not None:
                    return True

                if self.cdtcommonkeepaliveretries is not None:
                    return True

                if self.cdtcommonsrvacct is not None:
                    return True

                if self.cdtcommonsrvnetflow is not None:
                    return True

                if self.cdtcommonsrvqos is not None:
                    return True

                if self.cdtcommonsrvredirect is not None:
                    return True

                if self.cdtcommonsrvsubcontrol is not None:
                    return True

                if self.cdtcommonvalid is not None:
                    if self.cdtcommonvalid._has_data():
                        return True

                if self.cdtcommonvrf is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                return meta._meta_table['CiscoDynamicTemplateMib.Cdttemplatecommontable.Cdttemplatecommonentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateCommonTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cdttemplatecommonentry is not None:
                for child_ref in self.cdttemplatecommonentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
            return meta._meta_table['CiscoDynamicTemplateMib.Cdttemplatecommontable']['meta_info']


    class Cdtiftemplatetable(object):
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
            self.parent = None
            self.cdtiftemplateentry = YList()
            self.cdtiftemplateentry.parent = self
            self.cdtiftemplateentry.name = 'cdtiftemplateentry'


        class Cdtiftemplateentry(object):
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
            	**type**\:   :py:class:`UnicastrpftypeEnum <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.UnicastrpftypeEnum>`
            
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
            	**type**\:   :py:class:`Cdtifipv6NdraintervalunitsEnum <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry.Cdtifipv6NdraintervalunitsEnum>`
            
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
            	**type**\:   :py:class:`Cdtifipv6NdrouterpreferenceEnum <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry.Cdtifipv6NdrouterpreferenceEnum>`
            
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
            	**type**\:   :py:class:`UnicastrpftypeEnum <ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB.UnicastrpftypeEnum>`
            
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
                self.parent = None
                self.cdttemplatename = None
                self.cdtifcdpenable = None
                self.cdtifflowmonitor = None
                self.cdtifipv4mtu = None
                self.cdtifipv4subenable = None
                self.cdtifipv4tcpmssadjust = None
                self.cdtifipv4unnumbered = None
                self.cdtifipv4verifyunirpf = None
                self.cdtifipv4verifyunirpfacl = None
                self.cdtifipv4verifyunirpfopts = Unicastrpfoptions()
                self.cdtifipv6enable = None
                self.cdtifipv6nddadattempts = None
                self.cdtifipv6ndnsinterval = None
                self.cdtifipv6ndopts = CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry.Cdtifipv6Ndopts()
                self.cdtifipv6ndpreferredlife = None
                self.cdtifipv6ndprefix = None
                self.cdtifipv6ndprefixlength = None
                self.cdtifipv6ndraintervalmax = None
                self.cdtifipv6ndraintervalmin = None
                self.cdtifipv6ndraintervalunits = None
                self.cdtifipv6ndralife = None
                self.cdtifipv6ndreachabletime = None
                self.cdtifipv6ndrouterpreference = None
                self.cdtifipv6ndvalidlife = None
                self.cdtifipv6subenable = None
                self.cdtifipv6tcpmssadjust = None
                self.cdtifipv6verifyunirpf = None
                self.cdtifipv6verifyunirpfacl = None
                self.cdtifipv6verifyunirpfopts = Unicastrpfoptions()
                self.cdtifmtu = None
                self.cdtifvalid = CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry.Cdtifvalid()

            class Cdtifipv6NdraintervalunitsEnum(Enum):
                """
                Cdtifipv6NdraintervalunitsEnum

                This object specifies the units of time for the corresponding

                instances of cdtIfIpv6NdRaIntervalMin and

                cdtIfIpv6NdRaIntervalMax.

                This column is valid only if the 'ipv6NdRaInterval' bit of the

                corresponding instance of cdtIfValid is '1'.

                .. data:: seconds = 1

                .. data:: milliseconds = 2

                """

                seconds = 1

                milliseconds = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                    return meta._meta_table['CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry.Cdtifipv6NdraintervalunitsEnum']


            class Cdtifipv6NdrouterpreferenceEnum(Enum):
                """
                Cdtifipv6NdrouterpreferenceEnum

                This object specifies the Default Router Preference (DRP) for

                the router on the target interface.

                This column is valid only if the 'ipv6NdRouterPreference' bit of

                the corresponding instance of cdtIfValid is '1'.

                .. data:: high = 1

                .. data:: medium = 2

                .. data:: low = 3

                """

                high = 1

                medium = 2

                low = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                    return meta._meta_table['CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry.Cdtifipv6NdrouterpreferenceEnum']


            class Cdtifipv6Ndopts(FixedBitsDict):
                """
                Cdtifipv6Ndopts

                This object specifies options that affect advertisements sent
                on the target interface\:
                
                    'advertise'
                        This option specifies that the system should advertise
                        the IPv6 prefix (i.e., the corresponding instance of
                        cdtIfIpv6NdPrefix).
                
                    'onlink'
                        This option specifies that the IPv6 prefix has been
                        assigned to a link.  If set to '0', the system
                        advertises the IPv6 prefix as 'offlink'.
                
                    'router'
                        This option indicates that the router will send the full
                        router address and not set the 'R' bit in prefix
                        advertisements.
                
                    'autoConfig'
                        This option indicates to hosts on the local link that
                        the specified prefix supports IPv6 auto\-configuration.
                
                    'advertisementInterval'
                        This option specifies the advertisement interval option
                        in router advertisements sent on the target interface.
                
                    'managedConfigFlag'
                        This option causes the system to set the 'managed
                        address configuration flag' in router advertisements
                        sent on the target interface.
                
                    'otherConfigFlag'
                        This option causes the system to set the 'other stateful
                        configuration' flag in router advertisements sent on the
                        target interface.
                
                    'frameIpv6Prefix'
                        This option causes the system to add the prefix in a
                        received RADIUS framed IPv6 prefix attribute to the
                        target interface's neighbor discovery prefix queue and
                        includes it in router advertisements sent on the target
                        interface.
                
                    'raSupress'
                        This option suppresses the transmission of router
                        advertisements on the target interface.
                
                This column is valid only if the 'ipv6NdOpts' bit of the
                corresponding instance of cdtIfValid is '1'.
                Keys are:- router , framedIpv6Prefix , otherConfigFlag , advertisementInterval , advertise , onlink , raSuppress , autoConfig , managedConfigFlag

                """

                def __init__(self):
                    self._dictionary = { 
                        'router':False,
                        'framedIpv6Prefix':False,
                        'otherConfigFlag':False,
                        'advertisementInterval':False,
                        'advertise':False,
                        'onlink':False,
                        'raSuppress':False,
                        'autoConfig':False,
                        'managedConfigFlag':False,
                    }
                    self._pos_map = { 
                        'router':2,
                        'framedIpv6Prefix':7,
                        'otherConfigFlag':6,
                        'advertisementInterval':4,
                        'advertise':0,
                        'onlink':1,
                        'raSuppress':8,
                        'autoConfig':3,
                        'managedConfigFlag':5,
                    }

            class Cdtifvalid(FixedBitsDict):
                """
                Cdtifvalid

                This object specifies which attributes in the dynamic template
                have been configured to valid values.
                
                Each bit in this bit string corresponds to a column in this
                table.  If the bit is '0', then the value of the corresponding
                column is not valid.  If the bit is '1', then the value of the
                corresponding column has been configured to a valid value.
                
                The following list specifies the mappings between bits and the
                columns\:
                
                    'mtu'                     => cdtIfMtu
                    'cdpEnable'               => cdtIfCdpEnable
                    'flowMonitor'             => cdtIfFlowMonitor
                    'ipv4Unnumbered'          => cdtIfIpv4Unnumbered
                    'ipv4SubEnable'           => cdtIfIpv4SubEnable
                    'ipv4Mtu'                 => cdtIfIpv4Mtu
                    'ipv4TcpMssAdjust'        => cdtIfIpv4TcpMssAdjust
                    'ipv4VerifyUniRpf'        => cdtIfIpv4VerifyUniRpf
                    'ipv4VerifyUniRpfAcl'     => cdtIfIpv4VerifyUniRpfAcl
                    'ipv4VerifyUniRpfOpts'    => cdtIfIpv4VerifyUniRpfOpts
                    'ipv6Enable'              => cdtIfIpv6Enable
                    'ipv6SubEnable'           => cdtIfIpv6SubEnable
                    'ipv6TcpMssAdjust'        => cdtIfIpv6TcpMssAdjust
                    'ipv6VerifyUniRpf'        => cdtIfIpv6VerifyUniRpf
                    'ipv6VerifyUniRpfAcl'     => cdtIfIpv6VerifyUniRpfAcl
                    'ipv6VerifyUniRpfOpts'    => cdtIfIpv6VerifyUniRpfOpts
                    'ipv6NdPrefix'            => cdtIfIpv6NdPrefix,
                                                 cdtIfIpv6NdPrefixLength
                    'ipv6NdValidLife'         => cdtIfIpv6NdValidLife
                    'ipv6NdPreferredLife'     => cdtIfIpv6NdPreferredLife
                    'ipv6NdOpts'              => cdtIfIpv6NdOpts
                    'ipv6NdDadAttempts'       => cdtIfIpv6NdDadAttempts
                    'ipv6NdNsInterval'        => cdtIfIpv6NdNsInterval
                    'ipv6NdReacableTime'      => cdtIfIpv6NdReacableTime
                    'ipv6NdRaIntervalMax'     => cdtIfIpv6NdRaIntervalUnits,
                                                 cdtIfIpv6NdRaIntervalMax
                    'ipv6NdRaIntervalMin'     => cdtIfIpv6NdRaIntervalMin
                    'ipv6NdRaLife'            => cdtIfIpv6NdRaLife
                    'ipv6NdRouterPreference'' => cdtIfIpv6NdRouterPreference
                Keys are:- ipv4VerifyUniRpf , ipv6NdReachableTime , ipv6NdPreferredLife , mtu , ipv6NdRaIntervalMax , flowMonitor , ipv6VerifyUniRpf , ipv6NdValidLife , ipv6TcpMssAdjust , ipv6NdNsInterval , ipv6NdDadAttempts , ipv6NdRaIntervalMin , ipv4SubEnable , ipv4Unnumbered , ipv6NdRaLife , ipv6SubEnable , ipv4VerifyUniRpfAcl , ipv4Mtu , ipv6Enable , ipv4VerifyUniRpfOpts , ipv6NdOpts , ipv6VerifyUniRpfAcl , cdpEnable , ipv6VerifyUniRpfOpts , ipv6NdRaRouterPreference , ipv4TcpMssAdjust , ipv6NdPrefix

                """

                def __init__(self):
                    self._dictionary = { 
                        'ipv4VerifyUniRpf':False,
                        'ipv6NdReachableTime':False,
                        'ipv6NdPreferredLife':False,
                        'mtu':False,
                        'ipv6NdRaIntervalMax':False,
                        'flowMonitor':False,
                        'ipv6VerifyUniRpf':False,
                        'ipv6NdValidLife':False,
                        'ipv6TcpMssAdjust':False,
                        'ipv6NdNsInterval':False,
                        'ipv6NdDadAttempts':False,
                        'ipv6NdRaIntervalMin':False,
                        'ipv4SubEnable':False,
                        'ipv4Unnumbered':False,
                        'ipv6NdRaLife':False,
                        'ipv6SubEnable':False,
                        'ipv4VerifyUniRpfAcl':False,
                        'ipv4Mtu':False,
                        'ipv6Enable':False,
                        'ipv4VerifyUniRpfOpts':False,
                        'ipv6NdOpts':False,
                        'ipv6VerifyUniRpfAcl':False,
                        'cdpEnable':False,
                        'ipv6VerifyUniRpfOpts':False,
                        'ipv6NdRaRouterPreference':False,
                        'ipv4TcpMssAdjust':False,
                        'ipv6NdPrefix':False,
                    }
                    self._pos_map = { 
                        'ipv4VerifyUniRpf':7,
                        'ipv6NdReachableTime':22,
                        'ipv6NdPreferredLife':18,
                        'mtu':0,
                        'ipv6NdRaIntervalMax':23,
                        'flowMonitor':2,
                        'ipv6VerifyUniRpf':13,
                        'ipv6NdValidLife':17,
                        'ipv6TcpMssAdjust':12,
                        'ipv6NdNsInterval':21,
                        'ipv6NdDadAttempts':20,
                        'ipv6NdRaIntervalMin':24,
                        'ipv4SubEnable':4,
                        'ipv4Unnumbered':3,
                        'ipv6NdRaLife':25,
                        'ipv6SubEnable':11,
                        'ipv4VerifyUniRpfAcl':8,
                        'ipv4Mtu':5,
                        'ipv6Enable':10,
                        'ipv4VerifyUniRpfOpts':9,
                        'ipv6NdOpts':19,
                        'ipv6VerifyUniRpfAcl':14,
                        'cdpEnable':1,
                        'ipv6VerifyUniRpfOpts':15,
                        'ipv6NdRaRouterPreference':26,
                        'ipv4TcpMssAdjust':6,
                        'ipv6NdPrefix':16,
                    }

            @property
            def _common_path(self):
                if self.cdttemplatename is None:
                    raise YPYModelError('Key property cdttemplatename is None')

                return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtIfTemplateTable/CISCO-DYNAMIC-TEMPLATE-MIB:cdtIfTemplateEntry[CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateName = ' + str(self.cdttemplatename) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cdttemplatename is not None:
                    return True

                if self.cdtifcdpenable is not None:
                    return True

                if self.cdtifflowmonitor is not None:
                    return True

                if self.cdtifipv4mtu is not None:
                    return True

                if self.cdtifipv4subenable is not None:
                    return True

                if self.cdtifipv4tcpmssadjust is not None:
                    return True

                if self.cdtifipv4unnumbered is not None:
                    return True

                if self.cdtifipv4verifyunirpf is not None:
                    return True

                if self.cdtifipv4verifyunirpfacl is not None:
                    return True

                if self.cdtifipv4verifyunirpfopts is not None:
                    if self.cdtifipv4verifyunirpfopts._has_data():
                        return True

                if self.cdtifipv6enable is not None:
                    return True

                if self.cdtifipv6nddadattempts is not None:
                    return True

                if self.cdtifipv6ndnsinterval is not None:
                    return True

                if self.cdtifipv6ndopts is not None:
                    if self.cdtifipv6ndopts._has_data():
                        return True

                if self.cdtifipv6ndpreferredlife is not None:
                    return True

                if self.cdtifipv6ndprefix is not None:
                    return True

                if self.cdtifipv6ndprefixlength is not None:
                    return True

                if self.cdtifipv6ndraintervalmax is not None:
                    return True

                if self.cdtifipv6ndraintervalmin is not None:
                    return True

                if self.cdtifipv6ndraintervalunits is not None:
                    return True

                if self.cdtifipv6ndralife is not None:
                    return True

                if self.cdtifipv6ndreachabletime is not None:
                    return True

                if self.cdtifipv6ndrouterpreference is not None:
                    return True

                if self.cdtifipv6ndvalidlife is not None:
                    return True

                if self.cdtifipv6subenable is not None:
                    return True

                if self.cdtifipv6tcpmssadjust is not None:
                    return True

                if self.cdtifipv6verifyunirpf is not None:
                    return True

                if self.cdtifipv6verifyunirpfacl is not None:
                    return True

                if self.cdtifipv6verifyunirpfopts is not None:
                    if self.cdtifipv6verifyunirpfopts._has_data():
                        return True

                if self.cdtifmtu is not None:
                    return True

                if self.cdtifvalid is not None:
                    if self.cdtifvalid._has_data():
                        return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                return meta._meta_table['CiscoDynamicTemplateMib.Cdtiftemplatetable.Cdtiftemplateentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtIfTemplateTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cdtiftemplateentry is not None:
                for child_ref in self.cdtiftemplateentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
            return meta._meta_table['CiscoDynamicTemplateMib.Cdtiftemplatetable']['meta_info']


    class Cdtppptemplatetable(object):
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
            self.parent = None
            self.cdtppptemplateentry = YList()
            self.cdtppptemplateentry.parent = self
            self.cdtppptemplateentry.name = 'cdtppptemplateentry'


        class Cdtppptemplateentry(object):
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
            	**type**\:   :py:class:`CdtpppipcpaddroptionEnum <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.CdtpppipcpaddroptionEnum>`
            
            .. attribute:: cdtpppipcpdnsoption
            
            	This object specifies the IPCP DNS option for the dynamic interface\:      'other'         The implementation of this MIB module does not recognize         the configured DNS option.      'accept'         The system accepts any non\-zero DNS address form the         peer of a target PPP connection.      'request'         The system requests the DNS address from the peer of a         target PPP connection.      'reject'         The system rejects the DNS option from the peer of a         target PPP connection.  This column is valid only if the 'ipcpDnsOption' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:   :py:class:`CdtpppipcpdnsoptionEnum <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.CdtpppipcpdnsoptionEnum>`
            
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
            	**type**\:   :py:class:`CdtpppipcpmaskoptionEnum <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.CdtpppipcpmaskoptionEnum>`
            
            .. attribute:: cdtpppipcpwinsoption
            
            	This object specifies the IPCP WINS option for a target PPP connection\:      'other'         The implementation of this MIB module does not recognize         the configured WINS option.      'accept'         The system accepts any non\-zero WINS address from the         peer of a target PPP connection.      'request'         The system requests the WINS address from the peer of         a target PPP connection.      'reject'         The system rejects the WINS option from the peer of a         target PPP connection.  This column is valid only if the 'ipcpWinsOption' bit of the corresponding instance of cdtPppValid is '1'
            	**type**\:   :py:class:`CdtpppipcpwinsoptionEnum <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.CdtpppipcpwinsoptionEnum>`
            
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
            	**type**\:   :py:class:`CdtppppeerdefipaddrsrcEnum <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.CdtppppeerdefipaddrsrcEnum>`
            
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
                self.parent = None
                self.cdttemplatename = None
                self.cdtpppaccounting = None
                self.cdtpppauthentication = CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtpppauthentication()
                self.cdtpppauthenticationmethods = None
                self.cdtpppauthorization = None
                self.cdtpppchaphostname = None
                self.cdtpppchapopts = CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtpppchapopts()
                self.cdtpppchappassword = None
                self.cdtpppeapidentity = None
                self.cdtpppeapopts = CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtpppeapopts()
                self.cdtpppeappassword = None
                self.cdtpppipcpaddroption = None
                self.cdtpppipcpdnsoption = None
                self.cdtpppipcpdnsprimary = None
                self.cdtpppipcpdnssecondary = None
                self.cdtpppipcpmask = None
                self.cdtpppipcpmaskoption = None
                self.cdtpppipcpwinsoption = None
                self.cdtpppipcpwinsprimary = None
                self.cdtpppipcpwinssecondary = None
                self.cdtppploopbackignore = None
                self.cdtpppmaxbadauth = None
                self.cdtpppmaxconfigure = None
                self.cdtpppmaxfailure = None
                self.cdtpppmaxterminate = None
                self.cdtpppmschapv1hostname = None
                self.cdtpppmschapv1opts = CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtpppmschapv1Opts()
                self.cdtpppmschapv1password = None
                self.cdtpppmschapv2hostname = None
                self.cdtpppmschapv2opts = CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtpppmschapv2Opts()
                self.cdtpppmschapv2password = None
                self.cdtppppapopts = CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtppppapopts()
                self.cdtppppappassword = None
                self.cdtppppapusername = None
                self.cdtppppeerdefipaddr = None
                self.cdtppppeerdefipaddropts = CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtppppeerdefipaddropts()
                self.cdtppppeerdefipaddrsrc = None
                self.cdtppptimeoutauthentication = None
                self.cdtppptimeoutretry = None
                self.cdtpppvalid = CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.Cdtpppvalid()

            class CdtpppipcpaddroptionEnum(Enum):
                """
                CdtpppipcpaddroptionEnum

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

                other = 1

                accept = 2

                required = 3

                unique = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                    return meta._meta_table['CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.CdtpppipcpaddroptionEnum']


            class CdtpppipcpdnsoptionEnum(Enum):
                """
                CdtpppipcpdnsoptionEnum

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

                other = 1

                accept = 2

                request = 3

                reject = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                    return meta._meta_table['CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.CdtpppipcpdnsoptionEnum']


            class CdtpppipcpmaskoptionEnum(Enum):
                """
                CdtpppipcpmaskoptionEnum

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

                other = 1

                request = 2

                reject = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                    return meta._meta_table['CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.CdtpppipcpmaskoptionEnum']


            class CdtpppipcpwinsoptionEnum(Enum):
                """
                CdtpppipcpwinsoptionEnum

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

                other = 1

                accept = 2

                request = 3

                reject = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                    return meta._meta_table['CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.CdtpppipcpwinsoptionEnum']


            class CdtppppeerdefipaddrsrcEnum(Enum):
                """
                CdtppppeerdefipaddrsrcEnum

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

                static = 1

                pool = 2

                dhcp = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                    return meta._meta_table['CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry.CdtppppeerdefipaddrsrcEnum']


            class Cdtpppauthentication(FixedBitsDict):
                """
                Cdtpppauthentication

                This object specifies authentication services applied to a
                target PPP connection and other options affecting authentication
                services\:
                
                    'chap'
                        This option enables the Challenge Handshake Protocol (CHAP)
                        on a target PPP connection.
                
                    'msChap'
                        This option enables Microsoft's CHAP on a target PPP
                        connection.
                
                    'msChapV2'
                        This option enables version 2 of Microsoft's CHAP on a
                        target PPP connection.
                
                    'pap'
                        This option enables Password Authentication Protocol (PAP)
                        on a target PPP connection.
                
                    'eap'
                        This option enables Extensible Authentication Protocol (EAP)
                        on a target PPP connection.
                
                    'optional'
                        This option specifies that the system accepts the connection
                        even if the peer of a target PPP connection refuses to
                        accept the authentication methods the system has
                        requested.
                
                    'callin'
                        This option specifies that authentication should only happen
                        for incoming calls.
                
                    'oneTime'
                        This option specifies that the system accepts the username
                        and password in the username field of authentication
                        responses received on a target PPP connection.
                
                This column is valid only if the 'authentication' bit of the
                corresponding instance of cdtPppValid is '1'.
                Keys are:- msChapV2 , pap , oneTime , chap , eap , msChap , optional , callin

                """

                def __init__(self):
                    self._dictionary = { 
                        'msChapV2':False,
                        'pap':False,
                        'oneTime':False,
                        'chap':False,
                        'eap':False,
                        'msChap':False,
                        'optional':False,
                        'callin':False,
                    }
                    self._pos_map = { 
                        'msChapV2':2,
                        'pap':3,
                        'oneTime':7,
                        'chap':0,
                        'eap':4,
                        'msChap':1,
                        'optional':5,
                        'callin':6,
                    }

            class Cdtpppchapopts(FixedBitsDict):
                """
                Cdtpppchapopts

                This object specifies how the system processes the CHAP on a
                target PPP connection\:
                
                    'refuse'
                        This option specifies that the system should refuse CHAP
                        requests from peers of a target PPP connection.
                
                    'callin'
                        This option specifies that the system should only refuse
                        CHAP requests for incoming calls on a target PPP
                        connection.  This option is only relevant if the
                        'refuse' option is set to '1'.
                
                    'wait'
                        This option delays CHAP authentication until after the
                        peer of a target PPP connection has authenticated itself
                        to the system.
                
                    'encrypted'
                        This option specifies that the value specified by the
                        corresponding instance of cdtPppChapPassword is already
                        encrypted.
                
                This column is valid only if the 'chapOpts' bit of the
                corresponding instance of cdtPppValid is '1'.
                Keys are:- encrypted , refuse , callin , wait

                """

                def __init__(self):
                    self._dictionary = { 
                        'encrypted':False,
                        'refuse':False,
                        'callin':False,
                        'wait':False,
                    }
                    self._pos_map = { 
                        'encrypted':3,
                        'refuse':0,
                        'callin':1,
                        'wait':2,
                    }

            class Cdtpppeapopts(FixedBitsDict):
                """
                Cdtpppeapopts

                This object specifies how the system processes the EAP on a
                target PPP connection\:
                
                    'refuse'
                        This option specifies that the system should refuse EAP
                        requests from peers of a target PPP connection.
                
                    'callin'
                        This option specifies that the system should only refuse EAP
                        requests for incoming calls on a target PPP connection.
                        This option is only relevant if the 'refuse' option is
                        set to '1'.
                
                    'wait'
                        This option delays EAP authentication until after the
                        peer of a target PPP connection has authenticated itself
                        to the system.
                
                    'local'
                        This option specifies that the system should locally
                        authenticate the peer of a target PPP connection,
                        rather than acting as a proxy to an external AAA server.
                
                This column is valid only if the 'eapOpts' bit of the
                corresponding instance of cdtPppValid is '1'.
                Keys are:- refuse , callin , local , wait

                """

                def __init__(self):
                    self._dictionary = { 
                        'refuse':False,
                        'callin':False,
                        'local':False,
                        'wait':False,
                    }
                    self._pos_map = { 
                        'refuse':0,
                        'callin':1,
                        'local':3,
                        'wait':2,
                    }

            class Cdtpppmschapv1Opts(FixedBitsDict):
                """
                Cdtpppmschapv1Opts

                This object specifies how the system processes version 1 of
                Microsoft CHAP on a target PPP connection\:
                
                    'refuse'
                        This option specifies that the system should refuse
                        Microsoft CHAP (v1) requests from peers of a target PPP
                        connection.
                
                    'callin'
                        This option specifies that the system should only refuse
                        Microsoft CHAP (v1) requests for incoming calls on a
                        target PPP connection.  This option is only relevant if
                        the 'refuse' option is set to '1'.
                
                    'wait'
                        This option delays Microsoft CHAP (v1) authentication
                        until after the peer of a target PPP connection has
                        authenticated itself to the system.
                
                    'encrypted'
                        This option specifies that the value specified by the
                        corresponding instance of cdtPppMsChapV1Password is
                        already encrypted.
                
                This column is valid only if the 'msChapV1Opts' bit of the
                corresponding instance of cdtPppValid is '1'.
                Keys are:- encrypted , refuse , callin , wait

                """

                def __init__(self):
                    self._dictionary = { 
                        'encrypted':False,
                        'refuse':False,
                        'callin':False,
                        'wait':False,
                    }
                    self._pos_map = { 
                        'encrypted':3,
                        'refuse':0,
                        'callin':1,
                        'wait':2,
                    }

            class Cdtpppmschapv2Opts(FixedBitsDict):
                """
                Cdtpppmschapv2Opts

                This object specifies how the system processes version 2 of
                Microsoft CHAP on a target PPP connection\:
                
                    'refuse'
                        This option specifies that the system should refuse
                        Microsoft CHAP (v2) requests from peers of a target PPP
                        connection.
                
                    'callin'
                        This option specifies that the system should only refuse
                        Microsoft CHAP (v2) requests for incoming calls on a
                        target PPP connection.  This option is only relevant if
                        the 'refuse' option is set to '1'.
                
                    'wait'
                        This option delays Microsoft CHAP (v2) authentication
                        until after the peer of a target PPP connection has
                        authenticated itself to the system.
                
                    'encrypted'
                        This option specifies that the value specified by the
                        corresponding instance of cdtPppMsChapV2Password is
                        already encrypted.
                
                This column is valid only if the 'msChapV2Opts' bit of the
                corresponding instance of cdtPppValid is '1'.
                Keys are:- encrypted , refuse , callin , wait

                """

                def __init__(self):
                    self._dictionary = { 
                        'encrypted':False,
                        'refuse':False,
                        'callin':False,
                        'wait':False,
                    }
                    self._pos_map = { 
                        'encrypted':3,
                        'refuse':0,
                        'callin':1,
                        'wait':2,
                    }

            class Cdtppppapopts(FixedBitsDict):
                """
                Cdtppppapopts

                This object specifies how the system processes the PAP on a
                target PPP connection\:
                
                    'refuse'
                        This option specifies that the system should refuse PAP
                        requests from peers of a target PPP connection.
                
                    'encrypted'
                        This option specifies that the value specified by the
                        corresponding instance of cdtPppPapSentPassword is
                        already encrypted.
                
                This column is valid only if the 'papOpts' bit of the
                corresponding instance of cdtPppValid is '1'.
                Keys are:- encrypted , refuse

                """

                def __init__(self):
                    self._dictionary = { 
                        'encrypted':False,
                        'refuse':False,
                    }
                    self._pos_map = { 
                        'encrypted':1,
                        'refuse':0,
                    }

            class Cdtppppeerdefipaddropts(FixedBitsDict):
                """
                Cdtppppeerdefipaddropts

                This object specifies options that affect how the system
                assigns an IP address to the peer of a target PPP connection\:
                
                    'ipAddrForced'
                        This option forces the system to assign the next
                        available IP address in the pool to the peer of a
                        target PPP connection.  When disabled, the peer may
                        negotiate a specific IP address or the system can assign
                        the peer its previously assigned IP address.
                
                    'matchAaaPools'
                        This option specifies that the names of the IP address
                        pools provided by an external AAA server must appear in
                        the corresponding list of IP address pool specified by
                        the cdtPppPeerIpAddrPoolTable.
                
                    'backupPools'
                        This option specifies that the corresponding names of
                        the IP address pools specified by the
                        cditPppPeerIpAddrPoolTable serve as backup pools to
                        those provided by an external AAA server.
                
                    'staticPools'
                        This option suppresses an attempt to load pools from an
                        external AAA server when the system encounters a missing
                        pool name.
                
                This column is valid only if the 'peerIpAddrOpts' bit of the
                corresponding instance of cdtPppValid is '1'.
                Keys are:- staticPool , ipAddrForced , matchAaaPools

                """

                def __init__(self):
                    self._dictionary = { 
                        'staticPool':False,
                        'ipAddrForced':False,
                        'matchAaaPools':False,
                    }
                    self._pos_map = { 
                        'staticPool':2,
                        'ipAddrForced':0,
                        'matchAaaPools':1,
                    }

            class Cdtpppvalid(FixedBitsDict):
                """
                Cdtpppvalid

                This object specifies which attributes in the dynamic template
                have been configured to valid values.
                
                Each bit in this bit string corresponds to a column in this
                table.  If the bit is '0', then the value of the corresponding
                column is not valid.  If the bit is '1', then the value of the
                corresponding column has been configured to a valid value.
                
                The following list specifies the mappings between bits and the
                columns\:
                
                    accounting              => cdtPppAccounting
                    authentication          => cdtPppAuthentication
                    authenticationMethods   => cdtPppAuthenticationMethods
                    authorization           => cdtPppAuthorization
                    loopbackIgnore          => cdtPppLoopbackIgnore
                    maxBadAuth              => cdtPppMaxBadAuth
                    maxConfigure            => cdtPppMaxConfigure
                    maxFailure              => cdtPppMaxFailure
                    maxTerminate            => cdtPppMaxTerminate
                    timeoutAuthentication   => cdtPppTimeoutAuthentication
                    timeoutRetry            => cdtPppTimeoutRetry
                    chapOpts                => cdtPppChapOpts
                    chapHostname            => cdtPppChapHostname
                    chapPassword            => cdtPppChapPassword
                    msChapV1Opts            => cdtPppMsChapV1Opts
                    msChapV1Hostname        => cdtPppMsChapV1Hostname
                    msChapV1Password        => cdtPppMsChapV1Password
                    msChapV2Opts            => cdtPppMsChapV2Opts
                    msChapV2Hostname        => cdtPppMsChapV2Hostname
                    msChapV2Password        => cdtPppMsChapV2Password
                    papOpts                 => cdtPppPapOpts
                    papSentUsername         => cdtPppPapUsername
                    papSentPassword         => cdtPppPapPassword
                    eapOpts                 => cdtPppEapOpts
                    eapIdentity             => cdtPppEapIdentity
                    eapPassword             => cdtPppEapPassword
                    ipcpAddrOption          => cdtPppIpcpAddrOption
                    ipcpDnsOption           => cdtPppIpcpDnsOption
                    ipcpDnsPrimary          => cdtPppIpcpDnsPrimary
                    ipcpDnsSecondary        => cdtPppIpcpDnsSecondary
                    ipcpWinsOption          => cdtPppIpcpWinsOption
                    ipcpWinsPrimary         => cdtPppIpcpWinsPrimary
                    ipcpWinsSecondary       => cdtPppIpcpWinsSecondary
                    ipcpMaskOption          => cdtPppIpcpMaskOption
                    ipcpMask                => cdtPppIpcpMask
                    peerDefIpAddrOpts       => cdtPppPeerOpts
                    peerDefIpAddrSrc        => cdtPppPeerDefIpAddrSrc
                    peerDefIpAddr           => cdtPppPeerDefIpAddr
                Keys are:- ipcpWinsOption , ipcpAddrOption , maxConfigure , loopbackIgnore , papOpts , authorization , accounting , authentication , valid , maxTerminate , timeoutRetry , chapPassword , chapOpts , maxFailure , maxBadAuth , ipcpMask , msChapV2Opts , eapIdentity , autthenticationMethods , msChapV1Opts , chapHostname , eapPassword , peerDefIpAddr , peerDefIpAddrSrc , ipcpMaskOption , ipcpWinsSecondary , ipcpDnsPrimary , msChapV1Hostname , peerDefIpAddrOpts , msChapV1Password , eapOpts , papPassword , ipcpDnsOption , timeoutAuthentication , ipcpDnsSecondary , ipcpWinsPrimary , papUsername , msChapV2Hostname , msChapV2Password

                """

                def __init__(self):
                    self._dictionary = { 
                        'ipcpWinsOption':False,
                        'ipcpAddrOption':False,
                        'maxConfigure':False,
                        'loopbackIgnore':False,
                        'papOpts':False,
                        'authorization':False,
                        'accounting':False,
                        'authentication':False,
                        'valid':False,
                        'maxTerminate':False,
                        'timeoutRetry':False,
                        'chapPassword':False,
                        'chapOpts':False,
                        'maxFailure':False,
                        'maxBadAuth':False,
                        'ipcpMask':False,
                        'msChapV2Opts':False,
                        'eapIdentity':False,
                        'autthenticationMethods':False,
                        'msChapV1Opts':False,
                        'chapHostname':False,
                        'eapPassword':False,
                        'peerDefIpAddr':False,
                        'peerDefIpAddrSrc':False,
                        'ipcpMaskOption':False,
                        'ipcpWinsSecondary':False,
                        'ipcpDnsPrimary':False,
                        'msChapV1Hostname':False,
                        'peerDefIpAddrOpts':False,
                        'msChapV1Password':False,
                        'eapOpts':False,
                        'papPassword':False,
                        'ipcpDnsOption':False,
                        'timeoutAuthentication':False,
                        'ipcpDnsSecondary':False,
                        'ipcpWinsPrimary':False,
                        'papUsername':False,
                        'msChapV2Hostname':False,
                        'msChapV2Password':False,
                    }
                    self._pos_map = { 
                        'ipcpWinsOption':31,
                        'ipcpAddrOption':27,
                        'maxConfigure':7,
                        'loopbackIgnore':5,
                        'papOpts':21,
                        'authorization':4,
                        'accounting':1,
                        'authentication':2,
                        'valid':0,
                        'maxTerminate':9,
                        'timeoutRetry':11,
                        'chapPassword':14,
                        'chapOpts':12,
                        'maxFailure':8,
                        'maxBadAuth':6,
                        'ipcpMask':35,
                        'msChapV2Opts':18,
                        'eapIdentity':25,
                        'autthenticationMethods':3,
                        'msChapV1Opts':15,
                        'chapHostname':13,
                        'eapPassword':26,
                        'peerDefIpAddr':38,
                        'peerDefIpAddrSrc':37,
                        'ipcpMaskOption':34,
                        'ipcpWinsSecondary':33,
                        'ipcpDnsPrimary':29,
                        'msChapV1Hostname':16,
                        'peerDefIpAddrOpts':36,
                        'msChapV1Password':17,
                        'eapOpts':24,
                        'papPassword':23,
                        'ipcpDnsOption':28,
                        'timeoutAuthentication':10,
                        'ipcpDnsSecondary':30,
                        'ipcpWinsPrimary':32,
                        'papUsername':22,
                        'msChapV2Hostname':19,
                        'msChapV2Password':20,
                    }

            @property
            def _common_path(self):
                if self.cdttemplatename is None:
                    raise YPYModelError('Key property cdttemplatename is None')

                return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtPppTemplateTable/CISCO-DYNAMIC-TEMPLATE-MIB:cdtPppTemplateEntry[CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateName = ' + str(self.cdttemplatename) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cdttemplatename is not None:
                    return True

                if self.cdtpppaccounting is not None:
                    return True

                if self.cdtpppauthentication is not None:
                    if self.cdtpppauthentication._has_data():
                        return True

                if self.cdtpppauthenticationmethods is not None:
                    return True

                if self.cdtpppauthorization is not None:
                    return True

                if self.cdtpppchaphostname is not None:
                    return True

                if self.cdtpppchapopts is not None:
                    if self.cdtpppchapopts._has_data():
                        return True

                if self.cdtpppchappassword is not None:
                    return True

                if self.cdtpppeapidentity is not None:
                    return True

                if self.cdtpppeapopts is not None:
                    if self.cdtpppeapopts._has_data():
                        return True

                if self.cdtpppeappassword is not None:
                    return True

                if self.cdtpppipcpaddroption is not None:
                    return True

                if self.cdtpppipcpdnsoption is not None:
                    return True

                if self.cdtpppipcpdnsprimary is not None:
                    return True

                if self.cdtpppipcpdnssecondary is not None:
                    return True

                if self.cdtpppipcpmask is not None:
                    return True

                if self.cdtpppipcpmaskoption is not None:
                    return True

                if self.cdtpppipcpwinsoption is not None:
                    return True

                if self.cdtpppipcpwinsprimary is not None:
                    return True

                if self.cdtpppipcpwinssecondary is not None:
                    return True

                if self.cdtppploopbackignore is not None:
                    return True

                if self.cdtpppmaxbadauth is not None:
                    return True

                if self.cdtpppmaxconfigure is not None:
                    return True

                if self.cdtpppmaxfailure is not None:
                    return True

                if self.cdtpppmaxterminate is not None:
                    return True

                if self.cdtpppmschapv1hostname is not None:
                    return True

                if self.cdtpppmschapv1opts is not None:
                    if self.cdtpppmschapv1opts._has_data():
                        return True

                if self.cdtpppmschapv1password is not None:
                    return True

                if self.cdtpppmschapv2hostname is not None:
                    return True

                if self.cdtpppmschapv2opts is not None:
                    if self.cdtpppmschapv2opts._has_data():
                        return True

                if self.cdtpppmschapv2password is not None:
                    return True

                if self.cdtppppapopts is not None:
                    if self.cdtppppapopts._has_data():
                        return True

                if self.cdtppppappassword is not None:
                    return True

                if self.cdtppppapusername is not None:
                    return True

                if self.cdtppppeerdefipaddr is not None:
                    return True

                if self.cdtppppeerdefipaddropts is not None:
                    if self.cdtppppeerdefipaddropts._has_data():
                        return True

                if self.cdtppppeerdefipaddrsrc is not None:
                    return True

                if self.cdtppptimeoutauthentication is not None:
                    return True

                if self.cdtppptimeoutretry is not None:
                    return True

                if self.cdtpppvalid is not None:
                    if self.cdtpppvalid._has_data():
                        return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                return meta._meta_table['CiscoDynamicTemplateMib.Cdtppptemplatetable.Cdtppptemplateentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtPppTemplateTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cdtppptemplateentry is not None:
                for child_ref in self.cdtppptemplateentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
            return meta._meta_table['CiscoDynamicTemplateMib.Cdtppptemplatetable']['meta_info']


    class Cdtppppeeripaddrpooltable(object):
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
            self.parent = None
            self.cdtppppeeripaddrpoolentry = YList()
            self.cdtppppeeripaddrpoolentry.parent = self
            self.cdtppppeeripaddrpoolentry.name = 'cdtppppeeripaddrpoolentry'


        class Cdtppppeeripaddrpoolentry(object):
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
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: cdtppppeeripaddrpoolstorage
            
            	This object specifies what happens to the name pool entry upon restart.  If the corresponding instance of cdtTemplateSrc is not 'local', then this column must be 'volatile'
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            

            """

            _prefix = 'CISCO-DYNAMIC-TEMPLATE-MIB'
            _revision = '2007-09-06'

            def __init__(self):
                self.parent = None
                self.cdttemplatename = None
                self.cdtppppeeripaddrpoolpriority = None
                self.cdtppppeeripaddrpoolname = None
                self.cdtppppeeripaddrpoolstatus = None
                self.cdtppppeeripaddrpoolstorage = None

            @property
            def _common_path(self):
                if self.cdttemplatename is None:
                    raise YPYModelError('Key property cdttemplatename is None')
                if self.cdtppppeeripaddrpoolpriority is None:
                    raise YPYModelError('Key property cdtppppeeripaddrpoolpriority is None')

                return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtPppPeerIpAddrPoolTable/CISCO-DYNAMIC-TEMPLATE-MIB:cdtPppPeerIpAddrPoolEntry[CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateName = ' + str(self.cdttemplatename) + '][CISCO-DYNAMIC-TEMPLATE-MIB:cdtPppPeerIpAddrPoolPriority = ' + str(self.cdtppppeeripaddrpoolpriority) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cdttemplatename is not None:
                    return True

                if self.cdtppppeeripaddrpoolpriority is not None:
                    return True

                if self.cdtppppeeripaddrpoolname is not None:
                    return True

                if self.cdtppppeeripaddrpoolstatus is not None:
                    return True

                if self.cdtppppeeripaddrpoolstorage is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                return meta._meta_table['CiscoDynamicTemplateMib.Cdtppppeeripaddrpooltable.Cdtppppeeripaddrpoolentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtPppPeerIpAddrPoolTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cdtppppeeripaddrpoolentry is not None:
                for child_ref in self.cdtppppeeripaddrpoolentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
            return meta._meta_table['CiscoDynamicTemplateMib.Cdtppppeeripaddrpooltable']['meta_info']


    class Cdtethernettemplatetable(object):
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
            self.parent = None
            self.cdtethernettemplateentry = YList()
            self.cdtethernettemplateentry.parent = self
            self.cdtethernettemplateentry.name = 'cdtethernettemplateentry'


        class Cdtethernettemplateentry(object):
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
                self.parent = None
                self.cdttemplatename = None
                self.cdtethernetbridgedomain = None
                self.cdtethernetipv4pointtopoint = None
                self.cdtethernetmacaddr = None
                self.cdtethernetpppoeenable = None
                self.cdtethernetvalid = CiscoDynamicTemplateMib.Cdtethernettemplatetable.Cdtethernettemplateentry.Cdtethernetvalid()

            class Cdtethernetvalid(FixedBitsDict):
                """
                Cdtethernetvalid

                This object specifies which attributes in the dynamic template
                have been configured to valid values.
                
                Each bit in this bit string corresponds to a column in this
                table.  If the bit is '0', then the value of the corresponding
                column is not valid.  If the bit is '1', then the value of the
                corresponding column has been configured to a valid value.
                
                The following list specifies the mappings between bits and the
                columns\:
                
                    bridgeDomain     => cdtEthernetBridgeDomain
                    pppoeEnable      => cdtEthernetPppoeEnable
                    ipv4PointToPoint => cdtEthernetIpv4PointToPoint
                    macAddr          => cdtEthernetMacAddr
                Keys are:- macAddr , bridgeDomain , pppoeEnable , ipv4PointToPoint

                """

                def __init__(self):
                    self._dictionary = { 
                        'macAddr':False,
                        'bridgeDomain':False,
                        'pppoeEnable':False,
                        'ipv4PointToPoint':False,
                    }
                    self._pos_map = { 
                        'macAddr':3,
                        'bridgeDomain':0,
                        'pppoeEnable':1,
                        'ipv4PointToPoint':2,
                    }

            @property
            def _common_path(self):
                if self.cdttemplatename is None:
                    raise YPYModelError('Key property cdttemplatename is None')

                return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtEthernetTemplateTable/CISCO-DYNAMIC-TEMPLATE-MIB:cdtEthernetTemplateEntry[CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateName = ' + str(self.cdttemplatename) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cdttemplatename is not None:
                    return True

                if self.cdtethernetbridgedomain is not None:
                    return True

                if self.cdtethernetipv4pointtopoint is not None:
                    return True

                if self.cdtethernetmacaddr is not None:
                    return True

                if self.cdtethernetpppoeenable is not None:
                    return True

                if self.cdtethernetvalid is not None:
                    if self.cdtethernetvalid._has_data():
                        return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                return meta._meta_table['CiscoDynamicTemplateMib.Cdtethernettemplatetable.Cdtethernettemplateentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtEthernetTemplateTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cdtethernettemplateentry is not None:
                for child_ref in self.cdtethernettemplateentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
            return meta._meta_table['CiscoDynamicTemplateMib.Cdtethernettemplatetable']['meta_info']


    class Cdtsrvtemplatetable(object):
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
            self.parent = None
            self.cdtsrvtemplateentry = YList()
            self.cdtsrvtemplateentry.parent = self
            self.cdtsrvtemplateentry.name = 'cdtsrvtemplateentry'


        class Cdtsrvtemplateentry(object):
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
            	**type**\:   :py:class:`CdtsrvnetworksrvEnum <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtsrvtemplatetable.Cdtsrvtemplateentry.CdtsrvnetworksrvEnum>`
            
            .. attribute:: cdtsrvsgsrvgroup
            
            	This object specifies the name of the service group with which the system associates subscriber sessions.  A service group specifies a set of services that may be active simultaneously for a given subscriber session.  Typically, a service group contains a primary service and one or more secondary services.  This column is valid only if the 'sgSrvGroup' bit of the corresponding instance of cdtSrvValid is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cdtsrvsgsrvtype
            
            	This object specifies whether the target service specifies a network\-forwarding policy\:      'primary'         The target service specifies a network\-forwarding         policy.  Primary services are mutually exclusive; that         is, only one primary service can be activated for any         given subscriber session.      'secondary'         The target service has a dependence on the primary         service in the group specified by the corresponding         instance of cdtSuBSrvSgSrvGroup.  After the system         activates the primary service, it activates secondary         services.  When the system deactivates the primary         service, then it deactivates all the secondary services         in the service group.  This column is valid only if the 'sgSrvType' bit of the corresponding instance of cdtSrvValid is '1'
            	**type**\:   :py:class:`CdtsrvsgsrvtypeEnum <ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_MIB.CiscoDynamicTemplateMib.Cdtsrvtemplatetable.Cdtsrvtemplateentry.CdtsrvsgsrvtypeEnum>`
            
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
                self.parent = None
                self.cdttemplatename = None
                self.cdtsrvmulticast = None
                self.cdtsrvnetworksrv = None
                self.cdtsrvsgsrvgroup = None
                self.cdtsrvsgsrvtype = None
                self.cdtsrvvalid = CiscoDynamicTemplateMib.Cdtsrvtemplatetable.Cdtsrvtemplateentry.Cdtsrvvalid()
                self.cdtsrvvpdngroup = None

            class CdtsrvnetworksrvEnum(Enum):
                """
                CdtsrvnetworksrvEnum

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

                other = 1

                none = 2

                local = 3

                vpdn = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                    return meta._meta_table['CiscoDynamicTemplateMib.Cdtsrvtemplatetable.Cdtsrvtemplateentry.CdtsrvnetworksrvEnum']


            class CdtsrvsgsrvtypeEnum(Enum):
                """
                CdtsrvsgsrvtypeEnum

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

                primary = 1

                secondary = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                    return meta._meta_table['CiscoDynamicTemplateMib.Cdtsrvtemplatetable.Cdtsrvtemplateentry.CdtsrvsgsrvtypeEnum']


            class Cdtsrvvalid(FixedBitsDict):
                """
                Cdtsrvvalid

                This object specifies which attributes in the dynamic template
                have been configured to valid values.
                
                Each bit in this bit string corresponds to a column in this
                table.  If the bit is '0', then the value of the corresponding
                column is not valid.  If the bit is '1', then the value of the
                corresponding column has been configured to a valid value.
                
                The following list specifies the mappings between bits and the
                columns\:
                
                    networkSrv     => cdtSrvNetworkSrv
                    vpdnGroup      => cdtSrvVpdnGroup
                    sgSrvGroup     => cdtSrvGroup
                    sgSrvType      => cdtSrvSgSrvType
                    multicast      => cdtSrvMulticast
                Keys are:- sgSrvType , multicast , vpdnGroup , sgSrvGroup , networkSrv

                """

                def __init__(self):
                    self._dictionary = { 
                        'sgSrvType':False,
                        'multicast':False,
                        'vpdnGroup':False,
                        'sgSrvGroup':False,
                        'networkSrv':False,
                    }
                    self._pos_map = { 
                        'sgSrvType':3,
                        'multicast':4,
                        'vpdnGroup':1,
                        'sgSrvGroup':2,
                        'networkSrv':0,
                    }

            @property
            def _common_path(self):
                if self.cdttemplatename is None:
                    raise YPYModelError('Key property cdttemplatename is None')

                return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtSrvTemplateTable/CISCO-DYNAMIC-TEMPLATE-MIB:cdtSrvTemplateEntry[CISCO-DYNAMIC-TEMPLATE-MIB:cdtTemplateName = ' + str(self.cdttemplatename) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cdttemplatename is not None:
                    return True

                if self.cdtsrvmulticast is not None:
                    return True

                if self.cdtsrvnetworksrv is not None:
                    return True

                if self.cdtsrvsgsrvgroup is not None:
                    return True

                if self.cdtsrvsgsrvtype is not None:
                    return True

                if self.cdtsrvvalid is not None:
                    if self.cdtsrvvalid._has_data():
                        return True

                if self.cdtsrvvpdngroup is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
                return meta._meta_table['CiscoDynamicTemplateMib.Cdtsrvtemplatetable.Cdtsrvtemplateentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB/CISCO-DYNAMIC-TEMPLATE-MIB:cdtSrvTemplateTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cdtsrvtemplateentry is not None:
                for child_ref in self.cdtsrvtemplateentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
            return meta._meta_table['CiscoDynamicTemplateMib.Cdtsrvtemplatetable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-DYNAMIC-TEMPLATE-MIB:CISCO-DYNAMIC-TEMPLATE-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cdtethernettemplatetable is not None and self.cdtethernettemplatetable._has_data():
            return True

        if self.cdtiftemplatetable is not None and self.cdtiftemplatetable._has_data():
            return True

        if self.cdtppppeeripaddrpooltable is not None and self.cdtppppeeripaddrpooltable._has_data():
            return True

        if self.cdtppptemplatetable is not None and self.cdtppptemplatetable._has_data():
            return True

        if self.cdtsrvtemplatetable is not None and self.cdtsrvtemplatetable._has_data():
            return True

        if self.cdttemplateassociationtable is not None and self.cdttemplateassociationtable._has_data():
            return True

        if self.cdttemplatecommontable is not None and self.cdttemplatecommontable._has_data():
            return True

        if self.cdttemplatetable is not None and self.cdttemplatetable._has_data():
            return True

        if self.cdttemplatetargettable is not None and self.cdttemplatetargettable._has_data():
            return True

        if self.cdttemplateusagetable is not None and self.cdttemplateusagetable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_MIB as meta
        return meta._meta_table['CiscoDynamicTemplateMib']['meta_info']



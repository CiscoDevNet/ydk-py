""" ENTITY_STATE_MIB 

This MIB defines a state extension to the Entity MIB.

Copyright (C) The Internet Society 2005.  This version
of this MIB module is part of RFC 4268; see the RFC
itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class EntityStateMib(object):
    """
    
    
    .. attribute:: entstatetable
    
    	A table of information about state/status of entities. This is a sparse augment of the entPhysicalTable.  Entries appear in this table for values of entPhysicalClass [RFC4133] that in this implementation are able to report any of the state or status stored in this table
    	**type**\:   :py:class:`Entstatetable <ydk.models.cisco_ios_xe.ENTITY_STATE_MIB.EntityStateMib.Entstatetable>`
    
    

    """

    _prefix = 'ENTITY-STATE-MIB'
    _revision = '2005-11-22'

    def __init__(self):
        self.entstatetable = EntityStateMib.Entstatetable()
        self.entstatetable.parent = self


    class Entstatetable(object):
        """
        A table of information about state/status of entities.
        This is a sparse augment of the entPhysicalTable.  Entries
        appear in this table for values of
        entPhysicalClass [RFC4133] that in this implementation
        are able to report any of the state or status stored in
        this table.
        
        .. attribute:: entstateentry
        
        	State information about this physical entity
        	**type**\: list of    :py:class:`Entstateentry <ydk.models.cisco_ios_xe.ENTITY_STATE_MIB.EntityStateMib.Entstatetable.Entstateentry>`
        
        

        """

        _prefix = 'ENTITY-STATE-MIB'
        _revision = '2005-11-22'

        def __init__(self):
            self.parent = None
            self.entstateentry = YList()
            self.entstateentry.parent = self
            self.entstateentry.name = 'entstateentry'


        class Entstateentry(object):
            """
            State information about this physical entity.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: entstateadmin
            
            	The administrative state for this entity.  This object refers to an entities administrative permission to service both other entities within its containment hierarchy as well other users of its services defined by means outside the scope of this MIB.  Setting this object to 'notSupported' will result in an 'inconsistentValue' error.  For entities that do not support administrative state, all set operations will result in an 'inconsistentValue' error.  Some physical entities exhibit only a subset of the remaining administrative state values.  Some entities cannot be locked, and hence this object exhibits only the 'unlocked' state.  Other entities cannot be shutdown gracefully, and hence this object does not exhibit the 'shuttingDown' state.  A value of 'inconsistentValue' will be returned if attempts are made to set this object to values not supported by its administrative model
            	**type**\:   :py:class:`EntityadminstateEnum <ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB.EntityadminstateEnum>`
            
            .. attribute:: entstatealarm
            
            	The alarm status for this entity.  It does not include the alarms raised on child components within its containment hierarchy.  A value of 'unknown' means that this entity is  unable to report alarm state.  Note that this differs from 'indeterminate', which means that alarm state is supported and there are alarms against this entity, but the severity of some of the alarms is not known.  If no bits are set, then this entity supports reporting of alarms, but there are currently no active alarms against this entity
            	**type**\:   :py:class:`Entityalarmstatus <ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB.Entityalarmstatus>`
            
            .. attribute:: entstatelastchanged
            
            	The value of this object is the date and time when the value of any of entStateAdmin, entStateOper, entStateUsage, entStateAlarm, or entStateStandby changed for this entity.  If there has been no change since the last re\-initialization of the local system, this object contains the date and time of local system initialization.  If there has been no change since the entity was added to the local system, this object contains the date and time of the insertion
            	**type**\:  str
            
            .. attribute:: entstateoper
            
            	The operational state for this entity.  Note that unlike the state model used within the Interfaces MIB [RFC2863], this object does not follow the administrative state.  An administrative state of down does not predict an operational state of disabled.  A value of 'testing' means that entity currently being tested and cannot therefore report whether it is operational or not.  A value of 'disabled' means that an entity is totally inoperable and unable to provide service both to entities within its containment hierarchy, or to other receivers of its service as defined in ways outside the scope of this MIB.  A value of 'enabled' means that an entity is fully or partially operable and able to provide service both to  entities within its containment hierarchy, or to other receivers of its service as defined in ways outside the scope of this MIB.  Note that some implementations may not be able to accurately report entStateOper while the entStateAdmin object has a value other than 'unlocked'. In these cases, this object MUST have a value of 'unknown'
            	**type**\:   :py:class:`EntityoperstateEnum <ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB.EntityoperstateEnum>`
            
            .. attribute:: entstatestandby
            
            	The standby status for this entity.  Some entities will exhibit only a subset of the remaining standby state values.  If this entity cannot operate in a standby role, the value of this object will always be 'providingService'
            	**type**\:   :py:class:`EntitystandbystatusEnum <ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB.EntitystandbystatusEnum>`
            
            .. attribute:: entstateusage
            
            	The usage state for this entity.  This object refers to an entity's ability to service more physical entities in a containment hierarchy.  A value of 'idle' means this entity is able to contain other entities but that no other entity is currently contained within this entity.  A value of 'active' means that at least one entity is contained within this entity, but that it could handle more.  A value of 'busy' means that the entity is unable to handle any additional entities being contained in it.  Some entities will exhibit only a subset of the usage state values.  Entities that are unable to ever service any entities within a containment hierarchy will always have a usage state of 'busy'.  Some entities will only ever be able to support one entity within its containment hierarchy and will therefore only exhibit values of 'idle' and 'busy'
            	**type**\:   :py:class:`EntityusagestateEnum <ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB.EntityusagestateEnum>`
            
            

            """

            _prefix = 'ENTITY-STATE-MIB'
            _revision = '2005-11-22'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.entstateadmin = None
                self.entstatealarm = Entityalarmstatus()
                self.entstatelastchanged = None
                self.entstateoper = None
                self.entstatestandby = None
                self.entstateusage = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')

                return '/ENTITY-STATE-MIB:ENTITY-STATE-MIB/ENTITY-STATE-MIB:entStateTable/ENTITY-STATE-MIB:entStateEntry[ENTITY-STATE-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.entstateadmin is not None:
                    return True

                if self.entstatealarm is not None:
                    if self.entstatealarm._has_data():
                        return True

                if self.entstatelastchanged is not None:
                    return True

                if self.entstateoper is not None:
                    return True

                if self.entstatestandby is not None:
                    return True

                if self.entstateusage is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _ENTITY_STATE_MIB as meta
                return meta._meta_table['EntityStateMib.Entstatetable.Entstateentry']['meta_info']

        @property
        def _common_path(self):

            return '/ENTITY-STATE-MIB:ENTITY-STATE-MIB/ENTITY-STATE-MIB:entStateTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.entstateentry is not None:
                for child_ref in self.entstateentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _ENTITY_STATE_MIB as meta
            return meta._meta_table['EntityStateMib.Entstatetable']['meta_info']

    @property
    def _common_path(self):

        return '/ENTITY-STATE-MIB:ENTITY-STATE-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.entstatetable is not None and self.entstatetable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ENTITY_STATE_MIB as meta
        return meta._meta_table['EntityStateMib']['meta_info']



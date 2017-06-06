


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'EntityStateMib.Entstatetable.Entstateentry' : {
        'meta_info' : _MetaInfoClass('EntityStateMib.Entstatetable.Entstateentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'ENTITY-STATE-MIB', True),
            _MetaInfoClassMember('entStateAdmin', REFERENCE_ENUM_CLASS, 'EntityadminstateEnum' , 'ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB', 'EntityadminstateEnum', 
                [], [], 
                '''                The administrative state for this entity.
                
                This object refers to an entities administrative
                permission to service both other entities within
                its containment hierarchy as well other users of
                its services defined by means outside the scope
                of this MIB.
                
                Setting this object to 'notSupported' will result
                in an 'inconsistentValue' error.  For entities that
                do not support administrative state, all set
                operations will result in an 'inconsistentValue'
                error.
                
                Some physical entities exhibit only a subset of the
                remaining administrative state values.  Some entities
                cannot be locked, and hence this object exhibits only
                the 'unlocked' state.  Other entities cannot be shutdown
                gracefully, and hence this object does not exhibit the
                'shuttingDown' state.  A value of 'inconsistentValue'
                will be returned if attempts are made to set this
                object to values not supported by its administrative
                model.
                ''',
                'entstateadmin',
                'ENTITY-STATE-MIB', False),
            _MetaInfoClassMember('entStateAlarm', REFERENCE_BITS, 'Entityalarmstatus' , 'ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB', 'Entityalarmstatus', 
                [], [], 
                '''                The alarm status for this entity.  It does not include
                the alarms raised on child components within its
                containment hierarchy.
                
                A value of 'unknown' means that this entity is
                
                unable to report alarm state.  Note that this differs
                from 'indeterminate', which means that alarm state
                is supported and there are alarms against this entity,
                but the severity of some of the alarms is not known.
                
                If no bits are set, then this entity supports reporting
                of alarms, but there are currently no active alarms
                against this entity.
                ''',
                'entstatealarm',
                'ENTITY-STATE-MIB', False),
            _MetaInfoClassMember('entStateLastChanged', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The value of this object is the date and
                time when the value of any of entStateAdmin,
                entStateOper, entStateUsage, entStateAlarm,
                or entStateStandby changed for this entity.
                
                If there has been no change since
                the last re-initialization of the local system,
                this object contains the date and time of
                local system initialization.  If there has been
                no change since the entity was added to the
                local system, this object contains the date and
                time of the insertion.
                ''',
                'entstatelastchanged',
                'ENTITY-STATE-MIB', False),
            _MetaInfoClassMember('entStateOper', REFERENCE_ENUM_CLASS, 'EntityoperstateEnum' , 'ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB', 'EntityoperstateEnum', 
                [], [], 
                '''                The operational state for this entity.
                
                Note that unlike the state model used within the
                Interfaces MIB [RFC2863], this object does not follow
                the administrative state.  An administrative state of
                down does not predict an operational state
                of disabled.
                
                A value of 'testing' means that entity currently being
                tested and cannot therefore report whether it is
                operational or not.
                
                A value of 'disabled' means that an entity is totally
                inoperable and unable to provide service both to entities
                within its containment hierarchy, or to other receivers
                of its service as defined in ways outside the scope of
                this MIB.
                
                A value of 'enabled' means that an entity is fully or
                partially operable and able to provide service both to
                
                entities within its containment hierarchy, or to other
                receivers of its service as defined in ways outside the
                scope of this MIB.
                
                Note that some implementations may not be able to
                accurately report entStateOper while the
                entStateAdmin object has a value other than 'unlocked'.
                In these cases, this object MUST have a value
                of 'unknown'.
                ''',
                'entstateoper',
                'ENTITY-STATE-MIB', False),
            _MetaInfoClassMember('entStateStandby', REFERENCE_ENUM_CLASS, 'EntitystandbystatusEnum' , 'ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB', 'EntitystandbystatusEnum', 
                [], [], 
                '''                The standby status for this entity.
                
                Some entities will exhibit only a subset of the
                remaining standby state values.  If this entity
                cannot operate in a standby role, the value of this
                object will always be 'providingService'.
                ''',
                'entstatestandby',
                'ENTITY-STATE-MIB', False),
            _MetaInfoClassMember('entStateUsage', REFERENCE_ENUM_CLASS, 'EntityusagestateEnum' , 'ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB', 'EntityusagestateEnum', 
                [], [], 
                '''                The usage state for this entity.
                
                This object refers to an entity's ability to service more
                physical entities in a containment hierarchy.  A value
                of 'idle' means this entity is able to contain other
                entities but that no other entity is currently
                contained within this entity.
                
                A value of 'active' means that at least one entity is
                contained within this entity, but that it could handle
                more.  A value of 'busy' means that the entity is unable
                to handle any additional entities being contained in it.
                
                Some entities will exhibit only a subset of the
                usage state values.  Entities that are unable to ever
                service any entities within a containment hierarchy will
                always have a usage state of 'busy'.  Some entities will
                only ever be able to support one entity within its
                containment hierarchy and will therefore only exhibit
                values of 'idle' and 'busy'.
                ''',
                'entstateusage',
                'ENTITY-STATE-MIB', False),
            ],
            'ENTITY-STATE-MIB',
            'entStateEntry',
            _yang_ns._namespaces['ENTITY-STATE-MIB'],
        'ydk.models.cisco_ios_xe.ENTITY_STATE_MIB'
        ),
    },
    'EntityStateMib.Entstatetable' : {
        'meta_info' : _MetaInfoClass('EntityStateMib.Entstatetable',
            False, 
            [
            _MetaInfoClassMember('entStateEntry', REFERENCE_LIST, 'Entstateentry' , 'ydk.models.cisco_ios_xe.ENTITY_STATE_MIB', 'EntityStateMib.Entstatetable.Entstateentry', 
                [], [], 
                '''                State information about this physical entity.
                ''',
                'entstateentry',
                'ENTITY-STATE-MIB', False),
            ],
            'ENTITY-STATE-MIB',
            'entStateTable',
            _yang_ns._namespaces['ENTITY-STATE-MIB'],
        'ydk.models.cisco_ios_xe.ENTITY_STATE_MIB'
        ),
    },
    'EntityStateMib' : {
        'meta_info' : _MetaInfoClass('EntityStateMib',
            False, 
            [
            _MetaInfoClassMember('entStateTable', REFERENCE_CLASS, 'Entstatetable' , 'ydk.models.cisco_ios_xe.ENTITY_STATE_MIB', 'EntityStateMib.Entstatetable', 
                [], [], 
                '''                A table of information about state/status of entities.
                This is a sparse augment of the entPhysicalTable.  Entries
                appear in this table for values of
                entPhysicalClass [RFC4133] that in this implementation
                are able to report any of the state or status stored in
                this table.
                ''',
                'entstatetable',
                'ENTITY-STATE-MIB', False),
            ],
            'ENTITY-STATE-MIB',
            'ENTITY-STATE-MIB',
            _yang_ns._namespaces['ENTITY-STATE-MIB'],
        'ydk.models.cisco_ios_xe.ENTITY_STATE_MIB'
        ),
    },
}
_meta_table['EntityStateMib.Entstatetable.Entstateentry']['meta_info'].parent =_meta_table['EntityStateMib.Entstatetable']['meta_info']
_meta_table['EntityStateMib.Entstatetable']['meta_info'].parent =_meta_table['EntityStateMib']['meta_info']

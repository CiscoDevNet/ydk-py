


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AlarmseverityEnum' : _MetaInfoEnum('AlarmseverityEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB',
        {
            'critical':'critical',
            'major':'major',
            'minor':'minor',
            'info':'info',
        }, 'CISCO-ENTITY-ALARM-MIB', _yang_ns._namespaces['CISCO-ENTITY-ALARM-MIB']),
    'CiscoEntityAlarmMib.Cealarmmonitoring' : {
        'meta_info' : _MetaInfoClass('CiscoEntityAlarmMib.Cealarmmonitoring',
            False, 
            [
            _MetaInfoClassMember('ceAlarmCriticalCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of this object specifies the number of alarms
                currently asserted with a severity of 'critical'.
                ''',
                'cealarmcriticalcount',
                'CISCO-ENTITY-ALARM-MIB', False),
            _MetaInfoClassMember('ceAlarmCutOff', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If the management client writes a value of 'true' to this
                object, the agent stops signalling all external audible alarms
                under the control of the agent.  Reading this object should
                always result in a value of 'false'.
                
                Observe that alarm cutoff does not have an effect on monitoring,
                history logging, generation of notifications, or syslog message
                generation.  It also does not prevent the agent from signalling
                external audible alarms for alarms asserted after alarm-cutoff.
                
                This object emulates the 'alarm cut-off' mechanism typically
                installed in a central office (e.g., a big red button).  Observe
                this object should neither affect external visual alarms under
                the control of the agent, nor should it affect the current state
                of alarms being asserted by the system.
                ''',
                'cealarmcutoff',
                'CISCO-ENTITY-ALARM-MIB', False),
            _MetaInfoClassMember('ceAlarmMajorCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of this object specifies the number of alarms
                currently asserted with a severity of 'major'.
                ''',
                'cealarmmajorcount',
                'CISCO-ENTITY-ALARM-MIB', False),
            _MetaInfoClassMember('ceAlarmMinorCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of this object specifies the number of alarms
                currently asserted with a severity of 'minor'.
                ''',
                'cealarmminorcount',
                'CISCO-ENTITY-ALARM-MIB', False),
            ],
            'CISCO-ENTITY-ALARM-MIB',
            'ceAlarmMonitoring',
            _yang_ns._namespaces['CISCO-ENTITY-ALARM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB'
        ),
    },
    'CiscoEntityAlarmMib.Cealarmhistory' : {
        'meta_info' : _MetaInfoClass('CiscoEntityAlarmMib.Cealarmhistory',
            False, 
            [
            _MetaInfoClassMember('ceAlarmHistLastIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the value of the ceAlarmHistIndex
                object corresponding to the last entry added to the table by the
                agent.
                
                If the management client uses the notifications defined by this
                module, then it can poll this object to determine whether it has
                missed a notification sent by the agent.
                ''',
                'cealarmhistlastindex',
                'CISCO-ENTITY-ALARM-MIB', False),
            _MetaInfoClassMember('ceAlarmHistTableSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '500')], [], 
                '''                This object specifies the number of entries that the 
                ceAlarmHistTable can contain.  When a physical entity
                generates an unfiltered alarm, and the capacity of the
                ceAlarmHistTable has reached the value specified by
                this object, then the agent deletes the oldest entity in
                order to accommodate the new entry. A value of '0' prevents
                any history from being retained.  
                ''',
                'cealarmhisttablesize',
                'CISCO-ENTITY-ALARM-MIB', False),
            ],
            'CISCO-ENTITY-ALARM-MIB',
            'ceAlarmHistory',
            _yang_ns._namespaces['CISCO-ENTITY-ALARM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB'
        ),
    },
    'CiscoEntityAlarmMib.Cealarmfiltering' : {
        'meta_info' : _MetaInfoClass('CiscoEntityAlarmMib.Cealarmfiltering',
            False, 
            [
            _MetaInfoClassMember('ceAlarmFilterProfileIndexNext', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object contains an appropriate value to be used
                for ceAlarmFilterIndex when creating entries in the
                ceAlarmFilterProfileTable.  The value '0' indicates
                that no unassigned entries are available.  To obtain
                a ceAlarmFilterIndex, the management client issues
                a get request.  The agent has the responsibility of 
                modifying the value of this object following each 
                successful get request.
                ''',
                'cealarmfilterprofileindexnext',
                'CISCO-ENTITY-ALARM-MIB', False),
            _MetaInfoClassMember('ceAlarmNotifiesEnable', ATTRIBUTE, 'int' , None, None, 
                [('0', '4')], [], 
                '''                This object specifies a severity threshold governing the
                generation of ceAlarmAsserted and ceAlarmCleared
                notifications.  For example, if the value of this object is
                set to 'major', then the agent generates these notifications
                if and only if the severity of the alarm being indicated is
                'major' or 'critical'.  The value of '0' disables the 
                generation of notifications.
                
                Observe that this setting overrides the value of the 
                ceAlarmFilterNotifiesEnabled object.
                
                This object affects notification generation only; that is, it
                does not affect monitoring, history logging, and syslog message
                generation.
                ''',
                'cealarmnotifiesenable',
                'CISCO-ENTITY-ALARM-MIB', False),
            _MetaInfoClassMember('ceAlarmSyslogEnable', ATTRIBUTE, 'int' , None, None, 
                [('0', '4')], [], 
                '''                This object specifies a severity threshold governing the
                generation of syslog messages corresponding to alarms.  For
                example, if the value of this object is set to 'major', then
                the agent generates these a syslog message if and only if the
                severity of the alarm being indicated is 'major' or 'critical'.
                The value of '0' disables the generation of syslog messages
                corresponding to alarms.
                
                Observe that this setting overrides the value of the 
                ceAlarmFilterSyslogEnabled object.
                
                This object affects syslog message generation only; that is, it
                does not have an effect on monitoring, history logging, and
                generation of notifications.
                ''',
                'cealarmsyslogenable',
                'CISCO-ENTITY-ALARM-MIB', False),
            ],
            'CISCO-ENTITY-ALARM-MIB',
            'ceAlarmFiltering',
            _yang_ns._namespaces['CISCO-ENTITY-ALARM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB'
        ),
    },
    'CiscoEntityAlarmMib.Cealarmdescrmaptable.Cealarmdescrmapentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityAlarmMib.Cealarmdescrmaptable.Cealarmdescrmapentry',
            False, 
            [
            _MetaInfoClassMember('ceAlarmDescrIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object uniquely identifies an alarm description.
                ''',
                'cealarmdescrindex',
                'CISCO-ENTITY-ALARM-MIB', True),
            _MetaInfoClassMember('ceAlarmDescrVendorType', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This object specifies an object identifier (typically an
                enterprise-specific OID) that uniquely identifies the vendor
                type of those physical entities that this alarm description
                applies to.
                ''',
                'cealarmdescrvendortype',
                'CISCO-ENTITY-ALARM-MIB', False),
            ],
            'CISCO-ENTITY-ALARM-MIB',
            'ceAlarmDescrMapEntry',
            _yang_ns._namespaces['CISCO-ENTITY-ALARM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB'
        ),
    },
    'CiscoEntityAlarmMib.Cealarmdescrmaptable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityAlarmMib.Cealarmdescrmaptable',
            False, 
            [
            _MetaInfoClassMember('ceAlarmDescrMapEntry', REFERENCE_LIST, 'Cealarmdescrmapentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB', 'CiscoEntityAlarmMib.Cealarmdescrmaptable.Cealarmdescrmapentry', 
                [], [], 
                '''                A mapping between an alarm description and a vendor type.
                ''',
                'cealarmdescrmapentry',
                'CISCO-ENTITY-ALARM-MIB', False),
            ],
            'CISCO-ENTITY-ALARM-MIB',
            'ceAlarmDescrMapTable',
            _yang_ns._namespaces['CISCO-ENTITY-ALARM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB'
        ),
    },
    'CiscoEntityAlarmMib.Cealarmdescrtable.Cealarmdescrentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityAlarmMib.Cealarmdescrtable.Cealarmdescrentry',
            False, 
            [
            _MetaInfoClassMember('ceAlarmDescrIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'cealarmdescrindex',
                'CISCO-ENTITY-ALARM-MIB', True),
            _MetaInfoClassMember('ceAlarmDescrAlarmType', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the alarm type being described.
                ''',
                'cealarmdescralarmtype',
                'CISCO-ENTITY-ALARM-MIB', True),
            _MetaInfoClassMember('ceAlarmDescrSeverity', ATTRIBUTE, 'int' , None, None, 
                [('0', '4')], [], 
                '''                This object specifies the severity associated with the
                alarm type.
                
                An implementation may chose to not allow dynamic severity
                assignment, in which case it would restrict access to this
                object to be read-only.
                
                If an implementation allows dynamic severity assignment, then
                a management client can revert to the default severity by
                writing the value '0' to this object.
                
                There exists a class of systems that should implement dynamic
                severity assignment.  For example, consider a DSLAM (Digital
                Subscriber Loop Access Multiplexor) designed for both the
                central office and pedestal environments.  A 'pedestal' is
                typically a dark-green metal box mounted on a concrete or stone
                foundation in which carrier-class companies house equipment.
                The central office typically controls the temperature and
                humidity of the environment, reducing reliance on a system's
                fans.  Thus, the customer probably has a desire to reduce the 
                severity of alarms indicating the failure of a fan.  However, a
                pedestal environment has a much greater reliance on a system's
                fans.  Thus, the customer probably has a desire to increase the
                severity of alarms indicating the failure of a fan.
                ''',
                'cealarmdescrseverity',
                'CISCO-ENTITY-ALARM-MIB', False),
            _MetaInfoClassMember('ceAlarmDescrText', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies a human-readable message describing
                the alarm.
                ''',
                'cealarmdescrtext',
                'CISCO-ENTITY-ALARM-MIB', False),
            ],
            'CISCO-ENTITY-ALARM-MIB',
            'ceAlarmDescrEntry',
            _yang_ns._namespaces['CISCO-ENTITY-ALARM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB'
        ),
    },
    'CiscoEntityAlarmMib.Cealarmdescrtable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityAlarmMib.Cealarmdescrtable',
            False, 
            [
            _MetaInfoClassMember('ceAlarmDescrEntry', REFERENCE_LIST, 'Cealarmdescrentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB', 'CiscoEntityAlarmMib.Cealarmdescrtable.Cealarmdescrentry', 
                [], [], 
                '''                A collection of attributes that describe an alarm type.
                ''',
                'cealarmdescrentry',
                'CISCO-ENTITY-ALARM-MIB', False),
            ],
            'CISCO-ENTITY-ALARM-MIB',
            'ceAlarmDescrTable',
            _yang_ns._namespaces['CISCO-ENTITY-ALARM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB'
        ),
    },
    'CiscoEntityAlarmMib.Cealarmtable.Cealarmentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityAlarmMib.Cealarmtable.Cealarmentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-ALARM-MIB', True),
            _MetaInfoClassMember('ceAlarmFilterProfile', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the alarm filter profile associated
                with the corresponding physical entity.  An alarm filter
                profile controls which alarm types the agent will monitor
                and signal for the corresponding physical entity.
                
                If the value of this object is '0', then the agent monitors
                and signals all alarms associated with the corresponding
                physical entity.
                ''',
                'cealarmfilterprofile',
                'CISCO-ENTITY-ALARM-MIB', False),
            _MetaInfoClassMember('ceAlarmList', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                This object specifies those alarms currently being asserted
                by the corresponding physical entity.  Note, an alarm indicates
                a condition, not an event.  An alarm has two states:
                
                    'asserted'  Indicates that the condition described by the
                                alarm exists.
                
                    'cleared'   Indicates that the condition described by the
                                alarm does not exist.
                
                For example, a slot in a chassis may define an alarm that
                specifies whether the slot contains a module.  At the time of
                module insertion, the physical entity corresponding to the slot
                asserts this alarm, and the alarm remains asserted until the 
                slot becomes empty.
                
                If an alarm is being asserted by the physical entity, then the
                corresponding bit in the alarm list is set to a one. Observe
                that if the physical entity is not currently asserting any
                alarms, then the list will have a length of zero.
                ''',
                'cealarmlist',
                'CISCO-ENTITY-ALARM-MIB', False),
            _MetaInfoClassMember('ceAlarmSeverity', ATTRIBUTE, 'int' , None, None, 
                [('0', '4')], [], 
                '''                This object specifies the highest severity alarm currently
                being asserted by the corresponding physical entity.  A value
                of '0' indicates that there the corresponding physical entity
                currently is not asserting any alarms.
                ''',
                'cealarmseverity',
                'CISCO-ENTITY-ALARM-MIB', False),
            ],
            'CISCO-ENTITY-ALARM-MIB',
            'ceAlarmEntry',
            _yang_ns._namespaces['CISCO-ENTITY-ALARM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB'
        ),
    },
    'CiscoEntityAlarmMib.Cealarmtable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityAlarmMib.Cealarmtable',
            False, 
            [
            _MetaInfoClassMember('ceAlarmEntry', REFERENCE_LIST, 'Cealarmentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB', 'CiscoEntityAlarmMib.Cealarmtable.Cealarmentry', 
                [], [], 
                '''                Alarm control and status information related to the 
                corresponding physical entity, including a list of those
                alarms currently being asserted by that physical entity.
                ''',
                'cealarmentry',
                'CISCO-ENTITY-ALARM-MIB', False),
            ],
            'CISCO-ENTITY-ALARM-MIB',
            'ceAlarmTable',
            _yang_ns._namespaces['CISCO-ENTITY-ALARM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB'
        ),
    },
    'CiscoEntityAlarmMib.Cealarmhisttable.Cealarmhistentry.CealarmhisttypeEnum' : _MetaInfoEnum('CealarmhisttypeEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB',
        {
            'asserted':'asserted',
            'cleared':'cleared',
        }, 'CISCO-ENTITY-ALARM-MIB', _yang_ns._namespaces['CISCO-ENTITY-ALARM-MIB']),
    'CiscoEntityAlarmMib.Cealarmhisttable.Cealarmhistentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityAlarmMib.Cealarmhisttable.Cealarmhistentry',
            False, 
            [
            _MetaInfoClassMember('ceAlarmHistIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An integer value uniquely identifying the entry in the table.
                The value of this object starts at '1' and monotonically
                increases for each alarm condition transition monitored by the
                agent.  If the value of this object is '4294967295', the agent
                will reset it to '1' upon monitoring the next alarm condition
                transition.
                ''',
                'cealarmhistindex',
                'CISCO-ENTITY-ALARM-MIB', True),
            _MetaInfoClassMember('ceAlarmHistAlarmType', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the type of alarm generated.
                ''',
                'cealarmhistalarmtype',
                'CISCO-ENTITY-ALARM-MIB', False),
            _MetaInfoClassMember('ceAlarmHistEntPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                This object specifies the physical entity that generated
                the alarm.
                ''',
                'cealarmhistentphysicalindex',
                'CISCO-ENTITY-ALARM-MIB', False),
            _MetaInfoClassMember('ceAlarmHistSeverity', REFERENCE_ENUM_CLASS, 'AlarmseverityEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB', 'AlarmseverityEnum', 
                [], [], 
                '''                This object specifies the severity of the alarm generated.
                ''',
                'cealarmhistseverity',
                'CISCO-ENTITY-ALARM-MIB', False),
            _MetaInfoClassMember('ceAlarmHistTimeStamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the value of the sysUpTime object at
                the time the alarm was generated.
                ''',
                'cealarmhisttimestamp',
                'CISCO-ENTITY-ALARM-MIB', False),
            _MetaInfoClassMember('ceAlarmHistType', REFERENCE_ENUM_CLASS, 'CealarmhisttypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB', 'CiscoEntityAlarmMib.Cealarmhisttable.Cealarmhistentry.CealarmhisttypeEnum', 
                [], [], 
                '''                This object specifies whether the agent created the entry as
                the result of an alarm being asserted or cleared.
                ''',
                'cealarmhisttype',
                'CISCO-ENTITY-ALARM-MIB', False),
            ],
            'CISCO-ENTITY-ALARM-MIB',
            'ceAlarmHistEntry',
            _yang_ns._namespaces['CISCO-ENTITY-ALARM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB'
        ),
    },
    'CiscoEntityAlarmMib.Cealarmhisttable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityAlarmMib.Cealarmhisttable',
            False, 
            [
            _MetaInfoClassMember('ceAlarmHistEntry', REFERENCE_LIST, 'Cealarmhistentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB', 'CiscoEntityAlarmMib.Cealarmhisttable.Cealarmhistentry', 
                [], [], 
                '''                The information conveyed by a ceAlarmIndicate or
                ceAlarmClear trap.
                ''',
                'cealarmhistentry',
                'CISCO-ENTITY-ALARM-MIB', False),
            ],
            'CISCO-ENTITY-ALARM-MIB',
            'ceAlarmHistTable',
            _yang_ns._namespaces['CISCO-ENTITY-ALARM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB'
        ),
    },
    'CiscoEntityAlarmMib.Cealarmfilterprofiletable.Cealarmfilterprofileentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityAlarmMib.Cealarmfilterprofiletable.Cealarmfilterprofileentry',
            False, 
            [
            _MetaInfoClassMember('ceAlarmFilterIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object uniquely identifies the alarm filter profile.
                ''',
                'cealarmfilterindex',
                'CISCO-ENTITY-ALARM-MIB', True),
            _MetaInfoClassMember('ceAlarmFilterAlarmsEnabled', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                This object specifies a list of alarms that are enabled.
                ''',
                'cealarmfilteralarmsenabled',
                'CISCO-ENTITY-ALARM-MIB', False),
            _MetaInfoClassMember('ceAlarmFilterAlias', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies an arbitrary name associated with the
                alarm filter profile by the management client, and provides
                a non-volatile 'handle' for the alarm filter profile.
                
                On the first instantiation of an alarm filter profile, the
                value of this object is a zero-length string.  However, an
                agent may choose to set the value to a locally unique default
                value.
                
                If an implementation supports write access to this object,
                then the agent is responsible for ensuring the retention
                of any value written to this object until a management client
                deletes it.  The level of retention must span reboots and 
                reinitializations of the network management system, including
                those that result in different assignments to the value of
                the entPhysicalIndex associated with the physical entity.
                ''',
                'cealarmfilteralias',
                'CISCO-ENTITY-ALARM-MIB', False),
            _MetaInfoClassMember('ceAlarmFilterNotifiesEnabled', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                This object specifies a list of alarms for which notification
                generation is enabled.
                ''',
                'cealarmfilternotifiesenabled',
                'CISCO-ENTITY-ALARM-MIB', False),
            _MetaInfoClassMember('ceAlarmFilterStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object facilitates the creation, modification, or 
                deletion of a conceptual row in this table.
                
                A management client can create a conceptual row in this
                table by setting this object to 'createAndWait' or 
                'createAndGo'.  If a request to create a conceptual row
                in this table fails, then the system is not capable of
                supporting any more alarm filters.
                
                Before modifying a conceptual row in this table, the 
                management client must set this object to 'notInService'.
                After modifying a conceptual row in this table, the 
                management client must set this object to 'active'.
                This operation causes the modifications made to an
                alarm filter profile to take effect.
                
                An implementation should not allow a conceptual row in
                this table to be deleted if one or more physical entities
                reference it.
                ''',
                'cealarmfilterstatus',
                'CISCO-ENTITY-ALARM-MIB', False),
            _MetaInfoClassMember('ceAlarmFilterSyslogEnabled', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                This object specifies a list of alarms for which syslog
                message generation is enabled.
                ''',
                'cealarmfiltersyslogenabled',
                'CISCO-ENTITY-ALARM-MIB', False),
            ],
            'CISCO-ENTITY-ALARM-MIB',
            'ceAlarmFilterProfileEntry',
            _yang_ns._namespaces['CISCO-ENTITY-ALARM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB'
        ),
    },
    'CiscoEntityAlarmMib.Cealarmfilterprofiletable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityAlarmMib.Cealarmfilterprofiletable',
            False, 
            [
            _MetaInfoClassMember('ceAlarmFilterProfileEntry', REFERENCE_LIST, 'Cealarmfilterprofileentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB', 'CiscoEntityAlarmMib.Cealarmfilterprofiletable.Cealarmfilterprofileentry', 
                [], [], 
                '''                When a physical entity asserts/clears an alarm AND the
                ceAlarmFilterProfile object is not '0', the agent applies
                the specified alarm filter profile in processing the alarm.
                The agent uses the following procedure in processing the
                transition of an alarm condition of a given type:
                
                1)  If the alarm list specified by the alarm filter profile's
                    ceAlarmFilterAlarmsEnabled object specifies that the alarm
                    type is disabled, then the agent performs no further
                    processing.
                
                2)  The agent creates an entry in the ceAlarmHistTable.
                
                3)  If the alarm list specified by the alarm filter profile's 
                    ceAlarmFilterNotifiesEnabled object specifies that the alarm
                    type is enabled, then the agent generates the appropriate
                    notification.
                
                4)  If the alarm list specified by the alarm filter profile's
                    ceAlarmFilterSyslogEnabled object specifies that the alarm
                    type is enabled, then the agent generates the appropriate
                    syslog message.
                ''',
                'cealarmfilterprofileentry',
                'CISCO-ENTITY-ALARM-MIB', False),
            ],
            'CISCO-ENTITY-ALARM-MIB',
            'ceAlarmFilterProfileTable',
            _yang_ns._namespaces['CISCO-ENTITY-ALARM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB'
        ),
    },
    'CiscoEntityAlarmMib' : {
        'meta_info' : _MetaInfoClass('CiscoEntityAlarmMib',
            False, 
            [
            _MetaInfoClassMember('ceAlarmDescrMapTable', REFERENCE_CLASS, 'Cealarmdescrmaptable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB', 'CiscoEntityAlarmMib.Cealarmdescrmaptable', 
                [], [], 
                '''                For each type of entity (represented entPhysicalVendorType
                OID), this table contains a mapping between a unique 
                ceAlarmDescrIndex and entPhysicalvendorType OID.
                ''',
                'cealarmdescrmaptable',
                'CISCO-ENTITY-ALARM-MIB', False),
            _MetaInfoClassMember('ceAlarmDescrTable', REFERENCE_CLASS, 'Cealarmdescrtable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB', 'CiscoEntityAlarmMib.Cealarmdescrtable', 
                [], [], 
                '''                This table contains a description for each alarm type
                defined by each vendor type employed by the system.
                Observe that this table is sparse in nature, as it is
                rarely the case that a physical entity type needs to 
                define every alarm in its alarm space.
                ''',
                'cealarmdescrtable',
                'CISCO-ENTITY-ALARM-MIB', False),
            _MetaInfoClassMember('ceAlarmFiltering', REFERENCE_CLASS, 'Cealarmfiltering' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB', 'CiscoEntityAlarmMib.Cealarmfiltering', 
                [], [], 
                '''                ''',
                'cealarmfiltering',
                'CISCO-ENTITY-ALARM-MIB', False),
            _MetaInfoClassMember('ceAlarmFilterProfileTable', REFERENCE_CLASS, 'Cealarmfilterprofiletable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB', 'CiscoEntityAlarmMib.Cealarmfilterprofiletable', 
                [], [], 
                '''                This table contains a list of alarm filter profiles.
                ''',
                'cealarmfilterprofiletable',
                'CISCO-ENTITY-ALARM-MIB', False),
            _MetaInfoClassMember('ceAlarmHistory', REFERENCE_CLASS, 'Cealarmhistory' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB', 'CiscoEntityAlarmMib.Cealarmhistory', 
                [], [], 
                '''                ''',
                'cealarmhistory',
                'CISCO-ENTITY-ALARM-MIB', False),
            _MetaInfoClassMember('ceAlarmHistTable', REFERENCE_CLASS, 'Cealarmhisttable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB', 'CiscoEntityAlarmMib.Cealarmhisttable', 
                [], [], 
                '''                This table contains a history of ceAlarmIndicate and
                ceAlarmClear traps generated by the agent.
                ''',
                'cealarmhisttable',
                'CISCO-ENTITY-ALARM-MIB', False),
            _MetaInfoClassMember('ceAlarmMonitoring', REFERENCE_CLASS, 'Cealarmmonitoring' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB', 'CiscoEntityAlarmMib.Cealarmmonitoring', 
                [], [], 
                '''                ''',
                'cealarmmonitoring',
                'CISCO-ENTITY-ALARM-MIB', False),
            _MetaInfoClassMember('ceAlarmTable', REFERENCE_CLASS, 'Cealarmtable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB', 'CiscoEntityAlarmMib.Cealarmtable', 
                [], [], 
                '''                This table specifies alarm control and status information
                related to each physical entity contained by the system,
                including the alarms currently being asserted by each physical
                entity capable of generating alarms.
                ''',
                'cealarmtable',
                'CISCO-ENTITY-ALARM-MIB', False),
            ],
            'CISCO-ENTITY-ALARM-MIB',
            'CISCO-ENTITY-ALARM-MIB',
            _yang_ns._namespaces['CISCO-ENTITY-ALARM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_ALARM_MIB'
        ),
    },
}
_meta_table['CiscoEntityAlarmMib.Cealarmdescrmaptable.Cealarmdescrmapentry']['meta_info'].parent =_meta_table['CiscoEntityAlarmMib.Cealarmdescrmaptable']['meta_info']
_meta_table['CiscoEntityAlarmMib.Cealarmdescrtable.Cealarmdescrentry']['meta_info'].parent =_meta_table['CiscoEntityAlarmMib.Cealarmdescrtable']['meta_info']
_meta_table['CiscoEntityAlarmMib.Cealarmtable.Cealarmentry']['meta_info'].parent =_meta_table['CiscoEntityAlarmMib.Cealarmtable']['meta_info']
_meta_table['CiscoEntityAlarmMib.Cealarmhisttable.Cealarmhistentry']['meta_info'].parent =_meta_table['CiscoEntityAlarmMib.Cealarmhisttable']['meta_info']
_meta_table['CiscoEntityAlarmMib.Cealarmfilterprofiletable.Cealarmfilterprofileentry']['meta_info'].parent =_meta_table['CiscoEntityAlarmMib.Cealarmfilterprofiletable']['meta_info']
_meta_table['CiscoEntityAlarmMib.Cealarmmonitoring']['meta_info'].parent =_meta_table['CiscoEntityAlarmMib']['meta_info']
_meta_table['CiscoEntityAlarmMib.Cealarmhistory']['meta_info'].parent =_meta_table['CiscoEntityAlarmMib']['meta_info']
_meta_table['CiscoEntityAlarmMib.Cealarmfiltering']['meta_info'].parent =_meta_table['CiscoEntityAlarmMib']['meta_info']
_meta_table['CiscoEntityAlarmMib.Cealarmdescrmaptable']['meta_info'].parent =_meta_table['CiscoEntityAlarmMib']['meta_info']
_meta_table['CiscoEntityAlarmMib.Cealarmdescrtable']['meta_info'].parent =_meta_table['CiscoEntityAlarmMib']['meta_info']
_meta_table['CiscoEntityAlarmMib.Cealarmtable']['meta_info'].parent =_meta_table['CiscoEntityAlarmMib']['meta_info']
_meta_table['CiscoEntityAlarmMib.Cealarmhisttable']['meta_info'].parent =_meta_table['CiscoEntityAlarmMib']['meta_info']
_meta_table['CiscoEntityAlarmMib.Cealarmfilterprofiletable']['meta_info'].parent =_meta_table['CiscoEntityAlarmMib']['meta_info']




import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOPIMMIB.CiscoPimMIBNotificationObjects.CpimRPMappingChangeType_Enum' : _MetaInfoEnum('CpimRPMappingChangeType_Enum', 'ydk.models.pim.CISCO_PIM_MIB',
        {
            'newMapping':'NEWMAPPING',
            'deletedMapping':'DELETEDMAPPING',
            'modifiedOldMapping':'MODIFIEDOLDMAPPING',
            'modifiedNewMapping':'MODIFIEDNEWMAPPING',
        }, 'CISCO-PIM-MIB', _yang_ns._namespaces['CISCO-PIM-MIB']),
    'CISCOPIMMIB.CiscoPimMIBNotificationObjects' : {
        'meta_info' : _MetaInfoClass('CISCOPIMMIB.CiscoPimMIBNotificationObjects',
            False, 
            [
            _MetaInfoClassMember('cpimRPMappingChangeType', REFERENCE_ENUM_CLASS, 'CpimRPMappingChangeType_Enum' , 'ydk.models.pim.CISCO_PIM_MIB', 'CISCOPIMMIB.CiscoPimMIBNotificationObjects.CpimRPMappingChangeType_Enum', 
                [], [], 
                '''                Describes the operation that resulted in generation
                of cpimRPMappingChange notification.
                
                o newMapping, as the name suggests indicates that a new
                  mapping has been added into the pimRPSetTable, 
                o deletedMapping indicates that a mapping has been 
                  deleted from the pimRPSetTable, and,
                o modifiedXXXMapping indicates that an RP mapping (which
                  already existed in the table) has been modified.
                  The two modifications types i.e. modifiedOldMapping
                  and modifiedNewMapping, are defined to differentiate
                  the notification generated before modification from
                  that generated after modification.
                ''',
                'cpimrpmappingchangetype',
                'CISCO-PIM-MIB', False),
            ],
            'CISCO-PIM-MIB',
            'ciscoPimMIBNotificationObjects',
            _yang_ns._namespaces['CISCO-PIM-MIB'],
        'ydk.models.pim.CISCO_PIM_MIB'
        ),
    },
    'CISCOPIMMIB.Cpim.CpimLastErrorType_Enum' : _MetaInfoEnum('CpimLastErrorType_Enum', 'ydk.models.pim.CISCO_PIM_MIB',
        {
            'none':'NONE',
            'invalidRegister':'INVALIDREGISTER',
            'invalidJoinPrune':'INVALIDJOINPRUNE',
        }, 'CISCO-PIM-MIB', _yang_ns._namespaces['CISCO-PIM-MIB']),
    'CISCOPIMMIB.Cpim' : {
        'meta_info' : _MetaInfoClass('CISCOPIMMIB.Cpim',
            False, 
            [
            _MetaInfoClassMember('cpimInvalidJoinPruneMsgsRcvd', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                A count of the number of invalid PIM Join/Prune
                messages received by this device. A PIM Join/Prune
                message is termed invalid if
                
                o the RP specified in the packet is not the RP for
                  the group in question.
                ''',
                'cpiminvalidjoinprunemsgsrcvd',
                'CISCO-PIM-MIB', False),
            _MetaInfoClassMember('cpimInvalidRegisterMsgsRcvd', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                A count of the number of invalid PIM Register messages
                received by this device. A PIM Register message is
                termed invalid if 
                o the encapsulated IP header is malformed,
                o the destination of the PIM Register message is not the
                  RP (Rendezvous Point) for the group in question,
                o the source/DR (Designated Router) address is not a valid
                  unicast address.
                ''',
                'cpiminvalidregistermsgsrcvd',
                'CISCO-PIM-MIB', False),
            _MetaInfoClassMember('cpimLastErrorGroup', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The IP multicast group address to which the last invalid
                packet was addressed. The type of address stored
                depends on the value in cpimLastErrorGroupType. 
                
                The value of this object is a zero-length InetAddress if
                there is a problem in the packet received from the DR,
                for eg. a malformed encapsulated IP header. 
                
                The value of this object is irrelevant if the value of
                cpimLastErrorType is none(1).
                ''',
                'cpimlasterrorgroup',
                'CISCO-PIM-MIB', False),
            _MetaInfoClassMember('cpimLastErrorGroupType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                Represents the type of address stored in
                cpimLastErrorGroup. The value of this object is unknown(0)
                if there is a problem in the packet received from the
                DR.
                
                The value of this object is irrelevant if the value of
                cpimLastErrorType is none(1).
                ''',
                'cpimlasterrorgrouptype',
                'CISCO-PIM-MIB', False),
            _MetaInfoClassMember('cpimLastErrorOrigin', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object represents the Network Layer Address of the
                source that originated the last invalid packet. The type
                of address stored depends on the value in
                cpimLastErrorOriginType. 
                
                The value of this object represents the Network Layer
                Address of the Designated Router (DR) whenever the value
                of cpimLastErrorGroup is a zero-length address, 
                for eg. when encapsulated IP header is malformed.
                
                The value of this object is irrelevant if the value of
                cpimLastErrorType is none(1).
                ''',
                'cpimlasterrororigin',
                'CISCO-PIM-MIB', False),
            _MetaInfoClassMember('cpimLastErrorOriginType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                Represents the type of address stored in
                cpimLastErrorOrigin. The value of this object is
                irrelevant if the value of cpimLastErrorType is none(1).
                ''',
                'cpimlasterrororigintype',
                'CISCO-PIM-MIB', False),
            _MetaInfoClassMember('cpimLastErrorRP', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The address of the RP, as per the last invalid
                packet. The type of address stored depends on the value in
                cpimLastErrorRPType. 
                
                The value of this object is irrelevant if the value of
                cpimLastErrorType is none(1).
                ''',
                'cpimlasterrorrp',
                'CISCO-PIM-MIB', False),
            _MetaInfoClassMember('cpimLastErrorRPType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                Represents the type of address stored in
                cpimLastErrorRP. The value of this object is irrelevant
                if the value of cpimLastErrorType is none(1).
                ''',
                'cpimlasterrorrptype',
                'CISCO-PIM-MIB', False),
            _MetaInfoClassMember('cpimLastErrorType', REFERENCE_ENUM_CLASS, 'CpimLastErrorType_Enum' , 'ydk.models.pim.CISCO_PIM_MIB', 'CISCOPIMMIB.Cpim.CpimLastErrorType_Enum', 
                [], [], 
                '''                The type of the last invalid message that was received by
                this device.
                ''',
                'cpimlasterrortype',
                'CISCO-PIM-MIB', False),
            ],
            'CISCO-PIM-MIB',
            'cpim',
            _yang_ns._namespaces['CISCO-PIM-MIB'],
        'ydk.models.pim.CISCO_PIM_MIB'
        ),
    },
    'CISCOPIMMIB' : {
        'meta_info' : _MetaInfoClass('CISCOPIMMIB',
            False, 
            [
            _MetaInfoClassMember('ciscoPimMIBNotificationObjects', REFERENCE_CLASS, 'CiscoPimMIBNotificationObjects' , 'ydk.models.pim.CISCO_PIM_MIB', 'CISCOPIMMIB.CiscoPimMIBNotificationObjects', 
                [], [], 
                '''                ''',
                'ciscopimmibnotificationobjects',
                'CISCO-PIM-MIB', False),
            _MetaInfoClassMember('cpim', REFERENCE_CLASS, 'Cpim' , 'ydk.models.pim.CISCO_PIM_MIB', 'CISCOPIMMIB.Cpim', 
                [], [], 
                '''                ''',
                'cpim',
                'CISCO-PIM-MIB', False),
            ],
            'CISCO-PIM-MIB',
            'CISCO-PIM-MIB',
            _yang_ns._namespaces['CISCO-PIM-MIB'],
        'ydk.models.pim.CISCO_PIM_MIB'
        ),
    },
}
_meta_table['CISCOPIMMIB.CiscoPimMIBNotificationObjects']['meta_info'].parent =_meta_table['CISCOPIMMIB']['meta_info']
_meta_table['CISCOPIMMIB.Cpim']['meta_info'].parent =_meta_table['CISCOPIMMIB']['meta_info']

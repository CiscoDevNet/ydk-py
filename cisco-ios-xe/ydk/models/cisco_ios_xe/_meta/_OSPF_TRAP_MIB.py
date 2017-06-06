


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'OspfTrapMib.Ospftrapcontrol.OspfconfigerrortypeEnum' : _MetaInfoEnum('OspfconfigerrortypeEnum', 'ydk.models.cisco_ios_xe.OSPF_TRAP_MIB',
        {
            'badVersion':'badVersion',
            'areaMismatch':'areaMismatch',
            'unknownNbmaNbr':'unknownNbmaNbr',
            'unknownVirtualNbr':'unknownVirtualNbr',
            'authTypeMismatch':'authTypeMismatch',
            'authFailure':'authFailure',
            'netMaskMismatch':'netMaskMismatch',
            'helloIntervalMismatch':'helloIntervalMismatch',
            'deadIntervalMismatch':'deadIntervalMismatch',
            'optionMismatch':'optionMismatch',
            'mtuMismatch':'mtuMismatch',
            'duplicateRouterId':'duplicateRouterId',
            'noError':'noError',
        }, 'OSPF-TRAP-MIB', _yang_ns._namespaces['OSPF-TRAP-MIB']),
    'OspfTrapMib.Ospftrapcontrol.OspfpackettypeEnum' : _MetaInfoEnum('OspfpackettypeEnum', 'ydk.models.cisco_ios_xe.OSPF_TRAP_MIB',
        {
            'hello':'hello',
            'dbDescript':'dbDescript',
            'lsReq':'lsReq',
            'lsUpdate':'lsUpdate',
            'lsAck':'lsAck',
            'nullPacket':'nullPacket',
        }, 'OSPF-TRAP-MIB', _yang_ns._namespaces['OSPF-TRAP-MIB']),
    'OspfTrapMib.Ospftrapcontrol' : {
        'meta_info' : _MetaInfoClass('OspfTrapMib.Ospftrapcontrol',
            False, 
            [
            _MetaInfoClassMember('ospfConfigErrorType', REFERENCE_ENUM_CLASS, 'OspfconfigerrortypeEnum' , 'ydk.models.cisco_ios_xe.OSPF_TRAP_MIB', 'OspfTrapMib.Ospftrapcontrol.OspfconfigerrortypeEnum', 
                [], [], 
                '''                Potential types of configuration conflicts.
                Used by the ospfConfigError and
                ospfConfigVirtError traps.  When the last value
                of a trap using this object is needed, but no
                traps of that type have been sent, this value
                pertaining to this object should be returned as
                noError.
                ''',
                'ospfconfigerrortype',
                'OSPF-TRAP-MIB', False),
            _MetaInfoClassMember('ospfPacketSrc', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of an inbound packet that cannot
                be identified by a neighbor instance.  When
                the last value of a trap using this object is
                needed, but no traps of that type have been sent,
                this value pertaining to this object should
                be returned as 0.0.0.0.
                ''',
                'ospfpacketsrc',
                'OSPF-TRAP-MIB', False),
            _MetaInfoClassMember('ospfPacketType', REFERENCE_ENUM_CLASS, 'OspfpackettypeEnum' , 'ydk.models.cisco_ios_xe.OSPF_TRAP_MIB', 'OspfTrapMib.Ospftrapcontrol.OspfpackettypeEnum', 
                [], [], 
                '''                OSPF packet types.  When the last value of a trap
                using this object is needed, but no traps of
                that type have been sent, this value pertaining
                to this object should be returned as nullPacket.
                ''',
                'ospfpackettype',
                'OSPF-TRAP-MIB', False),
            _MetaInfoClassMember('ospfSetTrap', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                A 4-octet string serving as a bit map for
                the trap events defined by the OSPF traps.  This
                object is used to enable and disable specific
                OSPF traps where a 1 in the bit field
                represents enabled.  The right-most bit (least
                significant) represents trap 0.
                
                This object is persistent and when written
                
                the entity SHOULD save the change to non-volatile
                storage.
                ''',
                'ospfsettrap',
                'OSPF-TRAP-MIB', False),
            ],
            'OSPF-TRAP-MIB',
            'ospfTrapControl',
            _yang_ns._namespaces['OSPF-TRAP-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_TRAP_MIB'
        ),
    },
    'OspfTrapMib' : {
        'meta_info' : _MetaInfoClass('OspfTrapMib',
            False, 
            [
            _MetaInfoClassMember('ospfTrapControl', REFERENCE_CLASS, 'Ospftrapcontrol' , 'ydk.models.cisco_ios_xe.OSPF_TRAP_MIB', 'OspfTrapMib.Ospftrapcontrol', 
                [], [], 
                '''                ''',
                'ospftrapcontrol',
                'OSPF-TRAP-MIB', False),
            ],
            'OSPF-TRAP-MIB',
            'OSPF-TRAP-MIB',
            _yang_ns._namespaces['OSPF-TRAP-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_TRAP_MIB'
        ),
    },
}
_meta_table['OspfTrapMib.Ospftrapcontrol']['meta_info'].parent =_meta_table['OspfTrapMib']['meta_info']

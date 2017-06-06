


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoOspfTrapMib.Cospftrapcontrol.CospfconfigerrortypeEnum' : _MetaInfoEnum('CospfconfigerrortypeEnum', 'ydk.models.cisco_ios_xe.CISCO_OSPF_TRAP_MIB',
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
            'noError':'noError',
            'unknownShamLinkNbr':'unknownShamLinkNbr',
        }, 'CISCO-OSPF-TRAP-MIB', _yang_ns._namespaces['CISCO-OSPF-TRAP-MIB']),
    'CiscoOspfTrapMib.Cospftrapcontrol.CospfpackettypeEnum' : _MetaInfoEnum('CospfpackettypeEnum', 'ydk.models.cisco_ios_xe.CISCO_OSPF_TRAP_MIB',
        {
            'hello':'hello',
            'dbDescript':'dbDescript',
            'lsReq':'lsReq',
            'lsUpdate':'lsUpdate',
            'lsAck':'lsAck',
            'nullPacket':'nullPacket',
        }, 'CISCO-OSPF-TRAP-MIB', _yang_ns._namespaces['CISCO-OSPF-TRAP-MIB']),
    'CiscoOspfTrapMib.Cospftrapcontrol' : {
        'meta_info' : _MetaInfoClass('CiscoOspfTrapMib.Cospftrapcontrol',
            False, 
            [
            _MetaInfoClassMember('cospfConfigErrorType', REFERENCE_ENUM_CLASS, 'CospfconfigerrortypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_OSPF_TRAP_MIB', 'CiscoOspfTrapMib.Cospftrapcontrol.CospfconfigerrortypeEnum', 
                [], [], 
                '''                Potential types of configuration conflicts.
                Used  by the cospfConfigError and cospfConfigVirtError
                traps. When the last value of a trap
                using this object is needed, but no traps of
                that type have been sent, this value pertaining
                to this object should be returned as noError.
                ''',
                'cospfconfigerrortype',
                'CISCO-OSPF-TRAP-MIB', False),
            _MetaInfoClassMember('cospfPacketSrc', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of an inbound packet that can-
                not be identified by a neighbor instance. When
                the last value of a trap using this object is
                needed, but no traps of that type have been sent,
                this value pertaining to this object should
                be returned as 0.0.0.0.
                ''',
                'cospfpacketsrc',
                'CISCO-OSPF-TRAP-MIB', False),
            _MetaInfoClassMember('cospfPacketType', REFERENCE_ENUM_CLASS, 'CospfpackettypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_OSPF_TRAP_MIB', 'CiscoOspfTrapMib.Cospftrapcontrol.CospfpackettypeEnum', 
                [], [], 
                '''                OSPF packet types. When the last value of a trap
                using this object is needed, but no traps of
                that type have been sent, this value pertaining
                to this object should be returned as nullPacket.
                ''',
                'cospfpackettype',
                'CISCO-OSPF-TRAP-MIB', False),
            _MetaInfoClassMember('cospfSetTrap', REFERENCE_BITS, 'Cospfsettrap' , 'ydk.models.cisco_ios_xe.CISCO_OSPF_TRAP_MIB', 'CiscoOspfTrapMib.Cospftrapcontrol.Cospfsettrap', 
                [], [], 
                '''                An octet string serving as a bit  map  for
                the trap events defined by the OSPF traps in 
                this MIB. This object is used to enable and  
                disable  specific OSPF   traps   where  a  1  
                in  the  corresponding bit  field represents 
                enabled.
                ''',
                'cospfsettrap',
                'CISCO-OSPF-TRAP-MIB', False),
            ],
            'CISCO-OSPF-TRAP-MIB',
            'cospfTrapControl',
            _yang_ns._namespaces['CISCO-OSPF-TRAP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_OSPF_TRAP_MIB'
        ),
    },
    'CiscoOspfTrapMib' : {
        'meta_info' : _MetaInfoClass('CiscoOspfTrapMib',
            False, 
            [
            _MetaInfoClassMember('cospfTrapControl', REFERENCE_CLASS, 'Cospftrapcontrol' , 'ydk.models.cisco_ios_xe.CISCO_OSPF_TRAP_MIB', 'CiscoOspfTrapMib.Cospftrapcontrol', 
                [], [], 
                '''                ''',
                'cospftrapcontrol',
                'CISCO-OSPF-TRAP-MIB', False),
            ],
            'CISCO-OSPF-TRAP-MIB',
            'CISCO-OSPF-TRAP-MIB',
            _yang_ns._namespaces['CISCO-OSPF-TRAP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_OSPF_TRAP_MIB'
        ),
    },
}
_meta_table['CiscoOspfTrapMib.Cospftrapcontrol']['meta_info'].parent =_meta_table['CiscoOspfTrapMib']['meta_info']

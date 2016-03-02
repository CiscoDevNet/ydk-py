


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'OSPFTRAPMIB.OspfTrapControl.OspfConfigErrorType_Enum' : _MetaInfoEnum('OspfConfigErrorType_Enum', 'ydk.models.ospf.OSPF_TRAP_MIB',
        {
            'badVersion':'BADVERSION',
            'areaMismatch':'AREAMISMATCH',
            'unknownNbmaNbr':'UNKNOWNNBMANBR',
            'unknownVirtualNbr':'UNKNOWNVIRTUALNBR',
            'authTypeMismatch':'AUTHTYPEMISMATCH',
            'authFailure':'AUTHFAILURE',
            'netMaskMismatch':'NETMASKMISMATCH',
            'helloIntervalMismatch':'HELLOINTERVALMISMATCH',
            'deadIntervalMismatch':'DEADINTERVALMISMATCH',
            'optionMismatch':'OPTIONMISMATCH',
            'mtuMismatch':'MTUMISMATCH',
            'duplicateRouterId':'DUPLICATEROUTERID',
            'noError':'NOERROR',
        }, 'OSPF-TRAP-MIB', _yang_ns._namespaces['OSPF-TRAP-MIB']),
    'OSPFTRAPMIB.OspfTrapControl.OspfPacketType_Enum' : _MetaInfoEnum('OspfPacketType_Enum', 'ydk.models.ospf.OSPF_TRAP_MIB',
        {
            'hello':'HELLO',
            'dbDescript':'DBDESCRIPT',
            'lsReq':'LSREQ',
            'lsUpdate':'LSUPDATE',
            'lsAck':'LSACK',
            'nullPacket':'NULLPACKET',
        }, 'OSPF-TRAP-MIB', _yang_ns._namespaces['OSPF-TRAP-MIB']),
    'OSPFTRAPMIB.OspfTrapControl' : {
        'meta_info' : _MetaInfoClass('OSPFTRAPMIB.OspfTrapControl',
            False, 
            [
            _MetaInfoClassMember('ospfConfigErrorType', REFERENCE_ENUM_CLASS, 'OspfConfigErrorType_Enum' , 'ydk.models.ospf.OSPF_TRAP_MIB', 'OSPFTRAPMIB.OspfTrapControl.OspfConfigErrorType_Enum', 
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
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of an inbound packet that cannot
                be identified by a neighbor instance.  When
                the last value of a trap using this object is
                needed, but no traps of that type have been sent,
                this value pertaining to this object should
                be returned as 0.0.0.0.
                ''',
                'ospfpacketsrc',
                'OSPF-TRAP-MIB', False),
            _MetaInfoClassMember('ospfPacketType', REFERENCE_ENUM_CLASS, 'OspfPacketType_Enum' , 'ydk.models.ospf.OSPF_TRAP_MIB', 'OSPFTRAPMIB.OspfTrapControl.OspfPacketType_Enum', 
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
        'ydk.models.ospf.OSPF_TRAP_MIB'
        ),
    },
    'OSPFTRAPMIB' : {
        'meta_info' : _MetaInfoClass('OSPFTRAPMIB',
            False, 
            [
            _MetaInfoClassMember('ospfTrapControl', REFERENCE_CLASS, 'OspfTrapControl' , 'ydk.models.ospf.OSPF_TRAP_MIB', 'OSPFTRAPMIB.OspfTrapControl', 
                [], [], 
                '''                ''',
                'ospftrapcontrol',
                'OSPF-TRAP-MIB', False),
            ],
            'OSPF-TRAP-MIB',
            'OSPF-TRAP-MIB',
            _yang_ns._namespaces['OSPF-TRAP-MIB'],
        'ydk.models.ospf.OSPF_TRAP_MIB'
        ),
    },
}
_meta_table['OSPFTRAPMIB.OspfTrapControl']['meta_info'].parent =_meta_table['OSPFTRAPMIB']['meta_info']

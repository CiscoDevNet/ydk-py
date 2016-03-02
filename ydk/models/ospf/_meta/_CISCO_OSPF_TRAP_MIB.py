


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOOSPFTRAPMIB.CospfTrapControl.CospfConfigErrorType_Enum' : _MetaInfoEnum('CospfConfigErrorType_Enum', 'ydk.models.ospf.CISCO_OSPF_TRAP_MIB',
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
            'noError':'NOERROR',
            'unknownShamLinkNbr':'UNKNOWNSHAMLINKNBR',
        }, 'CISCO-OSPF-TRAP-MIB', _yang_ns._namespaces['CISCO-OSPF-TRAP-MIB']),
    'CISCOOSPFTRAPMIB.CospfTrapControl.CospfPacketType_Enum' : _MetaInfoEnum('CospfPacketType_Enum', 'ydk.models.ospf.CISCO_OSPF_TRAP_MIB',
        {
            'hello':'HELLO',
            'dbDescript':'DBDESCRIPT',
            'lsReq':'LSREQ',
            'lsUpdate':'LSUPDATE',
            'lsAck':'LSACK',
            'nullPacket':'NULLPACKET',
        }, 'CISCO-OSPF-TRAP-MIB', _yang_ns._namespaces['CISCO-OSPF-TRAP-MIB']),
    'CISCOOSPFTRAPMIB.CospfTrapControl' : {
        'meta_info' : _MetaInfoClass('CISCOOSPFTRAPMIB.CospfTrapControl',
            False, 
            [
            _MetaInfoClassMember('cospfConfigErrorType', REFERENCE_ENUM_CLASS, 'CospfConfigErrorType_Enum' , 'ydk.models.ospf.CISCO_OSPF_TRAP_MIB', 'CISCOOSPFTRAPMIB.CospfTrapControl.CospfConfigErrorType_Enum', 
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
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of an inbound packet that can-
                not be identified by a neighbor instance. When
                the last value of a trap using this object is
                needed, but no traps of that type have been sent,
                this value pertaining to this object should
                be returned as 0.0.0.0.
                ''',
                'cospfpacketsrc',
                'CISCO-OSPF-TRAP-MIB', False),
            _MetaInfoClassMember('cospfPacketType', REFERENCE_ENUM_CLASS, 'CospfPacketType_Enum' , 'ydk.models.ospf.CISCO_OSPF_TRAP_MIB', 'CISCOOSPFTRAPMIB.CospfTrapControl.CospfPacketType_Enum', 
                [], [], 
                '''                OSPF packet types. When the last value of a trap
                using this object is needed, but no traps of
                that type have been sent, this value pertaining
                to this object should be returned as nullPacket.
                ''',
                'cospfpackettype',
                'CISCO-OSPF-TRAP-MIB', False),
            _MetaInfoClassMember('cospfSetTrap', REFERENCE_BITS, 'CospfSetTrap_Bits' , 'ydk.models.ospf.CISCO_OSPF_TRAP_MIB', 'CISCOOSPFTRAPMIB.CospfTrapControl.CospfSetTrap_Bits', 
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
        'ydk.models.ospf.CISCO_OSPF_TRAP_MIB'
        ),
    },
    'CISCOOSPFTRAPMIB' : {
        'meta_info' : _MetaInfoClass('CISCOOSPFTRAPMIB',
            False, 
            [
            _MetaInfoClassMember('cospfTrapControl', REFERENCE_CLASS, 'CospfTrapControl' , 'ydk.models.ospf.CISCO_OSPF_TRAP_MIB', 'CISCOOSPFTRAPMIB.CospfTrapControl', 
                [], [], 
                '''                ''',
                'cospftrapcontrol',
                'CISCO-OSPF-TRAP-MIB', False),
            ],
            'CISCO-OSPF-TRAP-MIB',
            'CISCO-OSPF-TRAP-MIB',
            _yang_ns._namespaces['CISCO-OSPF-TRAP-MIB'],
        'ydk.models.ospf.CISCO_OSPF_TRAP_MIB'
        ),
    },
}
_meta_table['CISCOOSPFTRAPMIB.CospfTrapControl']['meta_info'].parent =_meta_table['CISCOOSPFTRAPMIB']['meta_info']

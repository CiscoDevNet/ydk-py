


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MplsLdpGenericStdMib.Mplsldpentitygenericlrtable.Mplsldpentitygenericlrentry.MplsldpentitygenericlabelspaceEnum' : _MetaInfoEnum('MplsldpentitygenericlabelspaceEnum', 'ydk.models.cisco_ios_xe.MPLS_LDP_GENERIC_STD_MIB',
        {
            'perPlatform':'perPlatform',
            'perInterface':'perInterface',
        }, 'MPLS-LDP-GENERIC-STD-MIB', _yang_ns._namespaces['MPLS-LDP-GENERIC-STD-MIB']),
    'MplsLdpGenericStdMib.Mplsldpentitygenericlrtable.Mplsldpentitygenericlrentry' : {
        'meta_info' : _MetaInfoClass('MplsLdpGenericStdMib.Mplsldpentitygenericlrtable.Mplsldpentitygenericlrentry',
            False, 
            [
            _MetaInfoClassMember('mplsLdpEntityLdpId', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'mplsldpentityldpid',
                'MPLS-LDP-GENERIC-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpEntityIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'mplsldpentityindex',
                'MPLS-LDP-GENERIC-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpEntityGenericLRMin', ATTRIBUTE, 'int' , None, None, 
                [('0', '1048575')], [], 
                '''                The minimum label configured for this range.
                ''',
                'mplsldpentitygenericlrmin',
                'MPLS-LDP-GENERIC-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpEntityGenericLRMax', ATTRIBUTE, 'int' , None, None, 
                [('0', '1048575')], [], 
                '''                The maximum label configured for this range.
                ''',
                'mplsldpentitygenericlrmax',
                'MPLS-LDP-GENERIC-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpEntityGenericIfIndexOrZero', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This value represents either the InterfaceIndex of
                the 'ifLayer' where these Generic Label would be created,
                
                
                or 0 (zero).  The value of zero means that the
                InterfaceIndex is not known.
                
                However, if the InterfaceIndex is known,
                then it must be represented by this value.
                
                If an InterfaceIndex becomes known, then the
                network management entity (e.g., SNMP agent) responsible
                for this object MUST change the value from 0 (zero) to the
                value of the InterfaceIndex.
                ''',
                'mplsldpentitygenericifindexorzero',
                'MPLS-LDP-GENERIC-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityGenericLabelSpace', REFERENCE_ENUM_CLASS, 'MplsldpentitygenericlabelspaceEnum' , 'ydk.models.cisco_ios_xe.MPLS_LDP_GENERIC_STD_MIB', 'MplsLdpGenericStdMib.Mplsldpentitygenericlrtable.Mplsldpentitygenericlrentry.MplsldpentitygenericlabelspaceEnum', 
                [], [], 
                '''                This value of this object is perPlatform(1), then
                this means that the label space type is
                per platform.
                
                If this object is perInterface(2), then this
                means that the label space type is per Interface.
                ''',
                'mplsldpentitygenericlabelspace',
                'MPLS-LDP-GENERIC-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityGenericLRRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row.  All writable
                objects in this row may be modified at any time,
                however, as described in  detail in the section
                entitled, 'Changing Values After Session
                Establishment', and again described in the
                DESCRIPTION clause of the mplsLdpEntityAdminStatus object,
                if a session has been initiated with a Peer,
                changing objects in this table will
                wreak havoc with the session and interrupt traffic.
                To repeat again:  the recommended procedure is
                to set the mplsLdpEntityAdminStatus to
                down, thereby explicitly causing a
                session to be torn down. Then, change objects
                in this entry, then set the mplsLdpEntityAdminStatus
                to enable which enables a new session to be initiated.
                
                There must exist at least one entry in this
                table for every LDP Entity that has a
                generic label configured.
                ''',
                'mplsldpentitygenericlrrowstatus',
                'MPLS-LDP-GENERIC-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityGenericLRStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this conceptual row.
                Conceptual rows having the value 'permanent(4)'
                need not allow write-access to any columnar
                objects in the row.
                ''',
                'mplsldpentitygenericlrstoragetype',
                'MPLS-LDP-GENERIC-STD-MIB', False),
            ],
            'MPLS-LDP-GENERIC-STD-MIB',
            'mplsLdpEntityGenericLREntry',
            _yang_ns._namespaces['MPLS-LDP-GENERIC-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_LDP_GENERIC_STD_MIB'
        ),
    },
    'MplsLdpGenericStdMib.Mplsldpentitygenericlrtable' : {
        'meta_info' : _MetaInfoClass('MplsLdpGenericStdMib.Mplsldpentitygenericlrtable',
            False, 
            [
            _MetaInfoClassMember('mplsLdpEntityGenericLREntry', REFERENCE_LIST, 'Mplsldpentitygenericlrentry' , 'ydk.models.cisco_ios_xe.MPLS_LDP_GENERIC_STD_MIB', 'MplsLdpGenericStdMib.Mplsldpentitygenericlrtable.Mplsldpentitygenericlrentry', 
                [], [], 
                '''                A row in the LDP Entity Generic Label
                Range (LR) Table.  One entry in this table contains
                information on a single range of labels
                represented by the configured Upper and Lower
                Bounds pairs.  NOTE: there is NO corresponding
                LDP message which relates to the information
                in this table, however, this table does provide
                a way for a user to 'reserve' a generic label
                range.
                
                NOTE:  The ranges for a specific LDP Entity
                are UNIQUE and non-overlapping.
                
                A row will not be created unless a unique and
                non-overlapping range is specified.
                ''',
                'mplsldpentitygenericlrentry',
                'MPLS-LDP-GENERIC-STD-MIB', False),
            ],
            'MPLS-LDP-GENERIC-STD-MIB',
            'mplsLdpEntityGenericLRTable',
            _yang_ns._namespaces['MPLS-LDP-GENERIC-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_LDP_GENERIC_STD_MIB'
        ),
    },
    'MplsLdpGenericStdMib' : {
        'meta_info' : _MetaInfoClass('MplsLdpGenericStdMib',
            False, 
            [
            _MetaInfoClassMember('mplsLdpEntityGenericLRTable', REFERENCE_CLASS, 'Mplsldpentitygenericlrtable' , 'ydk.models.cisco_ios_xe.MPLS_LDP_GENERIC_STD_MIB', 'MplsLdpGenericStdMib.Mplsldpentitygenericlrtable', 
                [], [], 
                '''                The MPLS LDP Entity Generic Label Range (LR)
                Table.
                
                The purpose of this table is to provide a mechanism
                for configurating a contiguous range of generic labels,
                or a 'label range' for LDP Entities.
                
                LDP Entities which use Generic Labels must have at least
                one entry in this table.  In other words, this table
                'extends' the mpldLdpEntityTable for Generic Labels.
                ''',
                'mplsldpentitygenericlrtable',
                'MPLS-LDP-GENERIC-STD-MIB', False),
            ],
            'MPLS-LDP-GENERIC-STD-MIB',
            'MPLS-LDP-GENERIC-STD-MIB',
            _yang_ns._namespaces['MPLS-LDP-GENERIC-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_LDP_GENERIC_STD_MIB'
        ),
    },
}
_meta_table['MplsLdpGenericStdMib.Mplsldpentitygenericlrtable.Mplsldpentitygenericlrentry']['meta_info'].parent =_meta_table['MplsLdpGenericStdMib.Mplsldpentitygenericlrtable']['meta_info']
_meta_table['MplsLdpGenericStdMib.Mplsldpentitygenericlrtable']['meta_info'].parent =_meta_table['MplsLdpGenericStdMib']['meta_info']

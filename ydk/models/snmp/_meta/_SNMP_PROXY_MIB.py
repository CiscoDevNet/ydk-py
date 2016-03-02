


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'SNMPPROXYMIB.SnmpProxyTable.SnmpProxyEntry.SnmpProxyType_Enum' : _MetaInfoEnum('SnmpProxyType_Enum', 'ydk.models.snmp.SNMP_PROXY_MIB',
        {
            'read':'READ',
            'write':'WRITE',
            'trap':'TRAP',
            'inform':'INFORM',
        }, 'SNMP-PROXY-MIB', _yang_ns._namespaces['SNMP-PROXY-MIB']),
    'SNMPPROXYMIB.SnmpProxyTable.SnmpProxyEntry' : {
        'meta_info' : _MetaInfoClass('SNMPPROXYMIB.SnmpProxyTable.SnmpProxyEntry',
            False, 
            [
            _MetaInfoClassMember('snmpProxyName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                The locally arbitrary, but unique identifier associated
                with this snmpProxyEntry.
                ''',
                'snmpproxyname',
                'SNMP-PROXY-MIB', True),
            _MetaInfoClassMember('snmpProxyContextEngineID', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9a-fA-F]){2}(:([0-9a-fA-F]){2})*)?'], 
                '''                The contextEngineID contained in messages that
                may be forwarded using the translation parameters
                defined by this entry.
                ''',
                'snmpproxycontextengineid',
                'SNMP-PROXY-MIB', False),
            _MetaInfoClassMember('snmpProxyContextName', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                The contextName contained in messages that may be
                forwarded using the translation parameters defined
                by this entry.
                
                This object is optional, and if not supported, the
                contextName contained in a message is ignored when
                selecting an entry in the snmpProxyTable.
                ''',
                'snmpproxycontextname',
                'SNMP-PROXY-MIB', False),
            _MetaInfoClassMember('snmpProxyMultipleTargetOut', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                This object selects a set of management targets defined
                in the snmpTargetAddrTable (in the SNMP-TARGET-MIB).
                
                This object is only used when selection of multiple
                targets is required (i.e. when forwarding an incoming
                notification).
                ''',
                'snmpproxymultipletargetout',
                'SNMP-PROXY-MIB', False),
            _MetaInfoClassMember('snmpProxyRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of this conceptual row.
                
                To create a row in this table, a manager must
                set this object to either createAndGo(4) or
                createAndWait(5).
                
                The following objects may not be modified while the
                value of this object is active(1):
                    - snmpProxyType
                    - snmpProxyContextEngineID
                    - snmpProxyContextName
                    - snmpProxyTargetParamsIn
                    - snmpProxySingleTargetOut
                    - snmpProxyMultipleTargetOut
                ''',
                'snmpproxyrowstatus',
                'SNMP-PROXY-MIB', False),
            _MetaInfoClassMember('snmpProxySingleTargetOut', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                This object selects a management target defined in the
                snmpTargetAddrTable (in the SNMP-TARGET-MIB).  The
                selected target is defined by an entry in the
                snmpTargetAddrTable whose index value (snmpTargetAddrName)
                is equal to this object.
                
                This object is only used when selection of a single
                target is required (i.e. when forwarding an incoming
                read or write request).
                ''',
                'snmpproxysingletargetout',
                'SNMP-PROXY-MIB', False),
            _MetaInfoClassMember('snmpProxyStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                The storage type of this conceptual row.
                Conceptual rows having the value 'permanent' need not
                allow write-access to any columnar objects in the row.
                ''',
                'snmpproxystoragetype',
                'SNMP-PROXY-MIB', False),
            _MetaInfoClassMember('snmpProxyTargetParamsIn', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                This object selects an entry in the snmpTargetParamsTable.
                The selected entry is used to determine which row of the
                snmpProxyTable to use for forwarding received messages.
                ''',
                'snmpproxytargetparamsin',
                'SNMP-PROXY-MIB', False),
            _MetaInfoClassMember('snmpProxyType', REFERENCE_ENUM_CLASS, 'SnmpProxyType_Enum' , 'ydk.models.snmp.SNMP_PROXY_MIB', 'SNMPPROXYMIB.SnmpProxyTable.SnmpProxyEntry.SnmpProxyType_Enum', 
                [], [], 
                '''                The type of message that may be forwarded using
                the translation parameters defined by this entry.
                ''',
                'snmpproxytype',
                'SNMP-PROXY-MIB', False),
            ],
            'SNMP-PROXY-MIB',
            'snmpProxyEntry',
            _yang_ns._namespaces['SNMP-PROXY-MIB'],
        'ydk.models.snmp.SNMP_PROXY_MIB'
        ),
    },
    'SNMPPROXYMIB.SnmpProxyTable' : {
        'meta_info' : _MetaInfoClass('SNMPPROXYMIB.SnmpProxyTable',
            False, 
            [
            _MetaInfoClassMember('snmpProxyEntry', REFERENCE_LIST, 'SnmpProxyEntry' , 'ydk.models.snmp.SNMP_PROXY_MIB', 'SNMPPROXYMIB.SnmpProxyTable.SnmpProxyEntry', 
                [], [], 
                '''                A set of translation parameters used by a proxy forwarder
                application for forwarding SNMP messages.
                
                Entries in the snmpProxyTable are created and deleted
                using the snmpProxyRowStatus object.
                ''',
                'snmpproxyentry',
                'SNMP-PROXY-MIB', False),
            ],
            'SNMP-PROXY-MIB',
            'snmpProxyTable',
            _yang_ns._namespaces['SNMP-PROXY-MIB'],
        'ydk.models.snmp.SNMP_PROXY_MIB'
        ),
    },
    'SNMPPROXYMIB' : {
        'meta_info' : _MetaInfoClass('SNMPPROXYMIB',
            False, 
            [
            _MetaInfoClassMember('snmpProxyTable', REFERENCE_CLASS, 'SnmpProxyTable' , 'ydk.models.snmp.SNMP_PROXY_MIB', 'SNMPPROXYMIB.SnmpProxyTable', 
                [], [], 
                '''                The table of translation parameters used by proxy forwarder
                applications for forwarding SNMP messages.
                ''',
                'snmpproxytable',
                'SNMP-PROXY-MIB', False),
            ],
            'SNMP-PROXY-MIB',
            'SNMP-PROXY-MIB',
            _yang_ns._namespaces['SNMP-PROXY-MIB'],
        'ydk.models.snmp.SNMP_PROXY_MIB'
        ),
    },
}
_meta_table['SNMPPROXYMIB.SnmpProxyTable.SnmpProxyEntry']['meta_info'].parent =_meta_table['SNMPPROXYMIB.SnmpProxyTable']['meta_info']
_meta_table['SNMPPROXYMIB.SnmpProxyTable']['meta_info'].parent =_meta_table['SNMPPROXYMIB']['meta_info']

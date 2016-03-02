


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOHSRPEXTMIB.CHsrpExtIfStandbyTable.CHsrpExtIfStandbyEntry' : {
        'meta_info' : _MetaInfoClass('CISCOHSRPEXTMIB.CHsrpExtIfStandbyTable.CHsrpExtIfStandbyEntry',
            False, 
            [
            _MetaInfoClassMember('cHsrpExtIfStandbyIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4)], [], 
                '''                This object defines the index of the standby table.
                ''',
                'chsrpextifstandbyindex',
                'CISCO-HSRP-EXT-MIB', True),
            _MetaInfoClassMember('cHsrpGrpNumber', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                ''',
                'chsrpgrpnumber',
                'CISCO-HSRP-EXT-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-HSRP-EXT-MIB', True),
            _MetaInfoClassMember('cHsrpExtIfStandbyDestAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the destination IP address of
                the standby router.
                ''',
                'chsrpextifstandbydestaddr',
                'CISCO-HSRP-EXT-MIB', False),
            _MetaInfoClassMember('cHsrpExtIfStandbyDestAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                This object specifies the type of Internet address
                denoted by cHsrpExtIfStandbyDestAddr.
                ''',
                'chsrpextifstandbydestaddrtype',
                'CISCO-HSRP-EXT-MIB', False),
            _MetaInfoClassMember('cHsrpExtIfStandbyRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The control that allows modification, creation,
                and deletion of entries. Entries may not be created
                via SNMP without explicitly setting
                cHsrpExtIfStandbyRowStatus to either
                'createAndGo' or 'createAndWait'.
                ''',
                'chsrpextifstandbyrowstatus',
                'CISCO-HSRP-EXT-MIB', False),
            _MetaInfoClassMember('cHsrpExtIfStandbySourceAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the source IP address of
                the standby router.
                ''',
                'chsrpextifstandbysourceaddr',
                'CISCO-HSRP-EXT-MIB', False),
            _MetaInfoClassMember('cHsrpExtIfStandbySourceAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                This object specifies the type of Internet address
                denoted by cHsrpExtIfStandbySourceAddr.
                ''',
                'chsrpextifstandbysourceaddrtype',
                'CISCO-HSRP-EXT-MIB', False),
            ],
            'CISCO-HSRP-EXT-MIB',
            'cHsrpExtIfStandbyEntry',
            _yang_ns._namespaces['CISCO-HSRP-EXT-MIB'],
        'ydk.models.hsrp.CISCO_HSRP_EXT_MIB'
        ),
    },
    'CISCOHSRPEXTMIB.CHsrpExtIfStandbyTable' : {
        'meta_info' : _MetaInfoClass('CISCOHSRPEXTMIB.CHsrpExtIfStandbyTable',
            False, 
            [
            _MetaInfoClassMember('cHsrpExtIfStandbyEntry', REFERENCE_LIST, 'CHsrpExtIfStandbyEntry' , 'ydk.models.hsrp.CISCO_HSRP_EXT_MIB', 'CISCOHSRPEXTMIB.CHsrpExtIfStandbyTable.CHsrpExtIfStandbyEntry', 
                [], [], 
                '''                The cHsrpExtIfStandbyEntry allows an HSRP group
                interface to track one or more standby interfaces.
                
                To create a new cHsrpExtIfStandbyEntry row, a
                management station should choose the ifIndex of
                the interface which is to be added as part of an
                HSRP group. Also, an HSRP group number and a
                cHsrpExtIfStandbyIndex should be chosen.
                ''',
                'chsrpextifstandbyentry',
                'CISCO-HSRP-EXT-MIB', False),
            ],
            'CISCO-HSRP-EXT-MIB',
            'cHsrpExtIfStandbyTable',
            _yang_ns._namespaces['CISCO-HSRP-EXT-MIB'],
        'ydk.models.hsrp.CISCO_HSRP_EXT_MIB'
        ),
    },
    'CISCOHSRPEXTMIB.CHsrpExtIfTable.CHsrpExtIfEntry' : {
        'meta_info' : _MetaInfoClass('CISCOHSRPEXTMIB.CHsrpExtIfTable.CHsrpExtIfEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-HSRP-EXT-MIB', True),
            _MetaInfoClassMember('cHsrpExtIfRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The control that allows modification, creation, and deletion
                of entries. For detailed rules see the DESCRIPTION for
                cHsrpExtIfEntry.
                ''',
                'chsrpextifrowstatus',
                'CISCO-HSRP-EXT-MIB', False),
            _MetaInfoClassMember('cHsrpExtIfUseBIA', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If set to TRUE, the HSRP Group MAC Address for all groups
                on this  interface will be the burned-in-address. Otherwise,
                this will be determined by ciscoHsrpGroupNumber. In case of
                sub-interfaces, UseBIA applies to all sub-interfaces on an 
                interface and to all groups on those sub-interfaces.
                ''',
                'chsrpextifusebia',
                'CISCO-HSRP-EXT-MIB', False),
            ],
            'CISCO-HSRP-EXT-MIB',
            'cHsrpExtIfEntry',
            _yang_ns._namespaces['CISCO-HSRP-EXT-MIB'],
        'ydk.models.hsrp.CISCO_HSRP_EXT_MIB'
        ),
    },
    'CISCOHSRPEXTMIB.CHsrpExtIfTable' : {
        'meta_info' : _MetaInfoClass('CISCOHSRPEXTMIB.CHsrpExtIfTable',
            False, 
            [
            _MetaInfoClassMember('cHsrpExtIfEntry', REFERENCE_LIST, 'CHsrpExtIfEntry' , 'ydk.models.hsrp.CISCO_HSRP_EXT_MIB', 'CISCOHSRPEXTMIB.CHsrpExtIfTable.CHsrpExtIfEntry', 
                [], [], 
                '''                If HSRP entries on this interface must use the BIA (Burned
                In Address), there must be an entry for the interface in this 
                table. Entries of this table are only accessible if HSRP has 
                been enabled i.e entries can not be created if HSRP is not
                enabled. Also, the interfaces should be of IEEE 802 ones
                (Ethernet, Token Ring, FDDI,VLAN, LANE, TR-LANE).
                
                Setting cHsrpExtIfRowStatus to active initiates the
                entry with default value for cHsrpExtIfUseBIA as FALSE.
                The value of cHsrpExtIfRowStatus may be set to destroy
                at any time. If the row is not initiated, it is similar to
                having cHsrpExtIfUseBIA as FALSE.
                
                Entries may not be created via SNMP without explicitly setting
                cHsrpExtIfRowStatus to either 'createAndGo' or 'createAndWait'.
                
                Entries can be created and modified via the management
                protocol or by the device's local management interface.
                
                If the row is not active, and a local management interface
                command modifies that row, the row may transition to active
                state.
                
                A row which is not in active state will timeout after a
                configurable period (five minutes by default). This timeout
                period can be changed by setting cHsrpConfigTimeout.
                ''',
                'chsrpextifentry',
                'CISCO-HSRP-EXT-MIB', False),
            ],
            'CISCO-HSRP-EXT-MIB',
            'cHsrpExtIfTable',
            _yang_ns._namespaces['CISCO-HSRP-EXT-MIB'],
        'ydk.models.hsrp.CISCO_HSRP_EXT_MIB'
        ),
    },
    'CISCOHSRPEXTMIB.CHsrpExtIfTrackedTable.CHsrpExtIfTrackedEntry' : {
        'meta_info' : _MetaInfoClass('CISCOHSRPEXTMIB.CHsrpExtIfTrackedTable.CHsrpExtIfTrackedEntry',
            False, 
            [
            _MetaInfoClassMember('cHsrpExtIfTracked', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The ifIndex value of the tracked interface.
                ''',
                'chsrpextiftracked',
                'CISCO-HSRP-EXT-MIB', True),
            _MetaInfoClassMember('cHsrpGrpNumber', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                ''',
                'chsrpgrpnumber',
                'CISCO-HSRP-EXT-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-HSRP-EXT-MIB', True),
            _MetaInfoClassMember('cHsrpExtIfTrackedIpNone', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies the disable HSRP IPv4 virtual
                IP address.
                ''',
                'chsrpextiftrackedipnone',
                'CISCO-HSRP-EXT-MIB', False),
            _MetaInfoClassMember('cHsrpExtIfTrackedPriority', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Priority of the tracked interface for the corresponding
                { ifIndex, cHsrpGrpNumber } pair. In the range of 0 to 255, 0
                is the lowest priority and 255 is the highest. When a tracked 
                interface is unavailable, the cHsrpGrpPriority of the router 
                is decreased by the value of this object instance (If the 
                cHsrpGrpPriority is less than the 
                cHsrpExtIfTrackedPriority, then the HSRP priority 
                becomes 0). This allows a standby router to be configured 
                with a priority such that if the currently active router's 
                priority is lowered because the tracked interface goes down, 
                the standby router can takeover.
                ''',
                'chsrpextiftrackedpriority',
                'CISCO-HSRP-EXT-MIB', False),
            _MetaInfoClassMember('cHsrpExtIfTrackedRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The control that allows modification, creation, and deletion
                of entries. For detailed rules see the DESCRIPTION for
                cHsrpExtIfTrackedEntry.
                ''',
                'chsrpextiftrackedrowstatus',
                'CISCO-HSRP-EXT-MIB', False),
            ],
            'CISCO-HSRP-EXT-MIB',
            'cHsrpExtIfTrackedEntry',
            _yang_ns._namespaces['CISCO-HSRP-EXT-MIB'],
        'ydk.models.hsrp.CISCO_HSRP_EXT_MIB'
        ),
    },
    'CISCOHSRPEXTMIB.CHsrpExtIfTrackedTable' : {
        'meta_info' : _MetaInfoClass('CISCOHSRPEXTMIB.CHsrpExtIfTrackedTable',
            False, 
            [
            _MetaInfoClassMember('cHsrpExtIfTrackedEntry', REFERENCE_LIST, 'CHsrpExtIfTrackedEntry' , 'ydk.models.hsrp.CISCO_HSRP_EXT_MIB', 'CISCOHSRPEXTMIB.CHsrpExtIfTrackedTable.CHsrpExtIfTrackedEntry', 
                [], [], 
                '''                Each row of this table allows the tracking of one
                interface of the HSRP group which is identified by the
                (ifIndex, cHsrpGrpNumber) values in this table's INDEX clause.
                Weight(priority) is given to each and every interface tracked. 
                When a tracked interface is unavailable, the HSRP priority of
                the router is decreased. i.e cHsrpGrpPriority value assigned 
                to an HSRP group will reduce by the value assigned to
                cHsrpExtIfTrackedPriority. This reduces the likelihood 
                of a router with a failed key interface becoming the 
                active router.
                
                Setting cHsrpExtIfTrackedRowStatus to active starts
                the tracking of cHsrpExtIfTracked by the HSRP group. 
                The value of cHsrpExtIfTrackedRowStatus may be set 
                to destroy at any time.
                
                Entries may not be created via SNMP without explicitly setting
                cHsrpExtIfTrackedRowStatus to either 'createAndGo' 
                or 'createAndWait'.
                
                Entries can be created and modified via the management
                protocol or by the device's local management interface.
                
                If the row is not active, and a local management interface
                command modifies that row, the row may transition to active
                state.
                
                A row entry in the cHsrpExtIfTrackedTable can not be created
                unless the corresponding row in the cHsrpGrpTable has been 
                created. If that corresponding row in cHsrpGrpTable is 
                deleted, the interfaces it tracks also get deleted.
                
                A row which is not in active state will timeout after a
                configurable period (five minutes by default). This timeout
                period can be changed by setting cHsrpConfigTimeout.
                ''',
                'chsrpextiftrackedentry',
                'CISCO-HSRP-EXT-MIB', False),
            ],
            'CISCO-HSRP-EXT-MIB',
            'cHsrpExtIfTrackedTable',
            _yang_ns._namespaces['CISCO-HSRP-EXT-MIB'],
        'ydk.models.hsrp.CISCO_HSRP_EXT_MIB'
        ),
    },
    'CISCOHSRPEXTMIB.CHsrpExtSecAddrTable.CHsrpExtSecAddrEntry' : {
        'meta_info' : _MetaInfoClass('CISCOHSRPEXTMIB.CHsrpExtSecAddrTable.CHsrpExtSecAddrEntry',
            False, 
            [
            _MetaInfoClassMember('cHsrpExtSecAddrAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                A secondary IpAddress for the {ifIndex, cHsrpGrpNumber} pair.
                As explained in the DESCRIPTION for cHsrpExtSecAddrEntry, a
                primary address must exist before a secondary address for 
                the same {ifIndex, cHsrpGrpNumber} pair can be created.
                ''',
                'chsrpextsecaddraddress',
                'CISCO-HSRP-EXT-MIB', True),
            _MetaInfoClassMember('cHsrpGrpNumber', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                ''',
                'chsrpgrpnumber',
                'CISCO-HSRP-EXT-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-HSRP-EXT-MIB', True),
            _MetaInfoClassMember('cHsrpExtSecAddrRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The control that allows modification, creation, and deletion
                of entries. For detailed rules see the DESCRIPTION for
                cHsrpExtSecAddrEntry.
                ''',
                'chsrpextsecaddrrowstatus',
                'CISCO-HSRP-EXT-MIB', False),
            ],
            'CISCO-HSRP-EXT-MIB',
            'cHsrpExtSecAddrEntry',
            _yang_ns._namespaces['CISCO-HSRP-EXT-MIB'],
        'ydk.models.hsrp.CISCO_HSRP_EXT_MIB'
        ),
    },
    'CISCOHSRPEXTMIB.CHsrpExtSecAddrTable' : {
        'meta_info' : _MetaInfoClass('CISCOHSRPEXTMIB.CHsrpExtSecAddrTable',
            False, 
            [
            _MetaInfoClassMember('cHsrpExtSecAddrEntry', REFERENCE_LIST, 'CHsrpExtSecAddrEntry' , 'ydk.models.hsrp.CISCO_HSRP_EXT_MIB', 'CISCOHSRPEXTMIB.CHsrpExtSecAddrTable.CHsrpExtSecAddrEntry', 
                [], [], 
                '''                The CHsrpExtSecAddrEntry allows creation of secondary
                IP Addresses for each cHsrpGrpEntry row.
                
                Secondary addresses can be added by setting 
                cHsrpExtSecAddrRowStatus to be active. The value of
                cHsrpExtSecAddrRowStatus may be set to destroy at any
                time.
                
                Entries may not be created via SNMP without explicitly setting
                cHsrpExtSecAddrRowStatus to either 'createAndGo'
                or 'createAndWait'.
                
                Entries can be created and modified via the management
                protocol or by the device's local management interface.
                
                If the row is not active, and a local management interface
                command modifies that row, the row may transition to active
                state.
                
                A row which is not in active state will timeout after a
                configurable period (five minutes by default). This timeout
                period can be changed by setting cHsrpConfigTimeout.
                
                Before creation of a cHsrpExtSecAddrEntry row,
                either cHsrpGrpConfiguredVirtualIpAddr or 
                cHsrpGrpLearnedVirtualIpAddr must have a valid IP Address.
                This is because a secondary ip address cannot be created
                unless the primary ip address has already been set.
                
                To create a new cHsrpExtSecAddrEntry row, a management 
                station should choose the ifIndex of the interface which is to 
                be added as part of an HSRP group. Also, an HSRP group number 
                and a cHsrpExtSecAddrAddress should be chosen.
                
                Deleting a {ifIndex, cHsrpGrpNumber} row in the
                cHsrpGrpTable will delete all corresponding
                rows in the cHsrpExtSecAddrTable.
                Deleting a primary address value in the cHsrpGrpEntry row
                will delete all secondary addresses for the same
                {ifIndex, cHsrpGrpNumber} pair.
                ''',
                'chsrpextsecaddrentry',
                'CISCO-HSRP-EXT-MIB', False),
            ],
            'CISCO-HSRP-EXT-MIB',
            'cHsrpExtSecAddrTable',
            _yang_ns._namespaces['CISCO-HSRP-EXT-MIB'],
        'ydk.models.hsrp.CISCO_HSRP_EXT_MIB'
        ),
    },
    'CISCOHSRPEXTMIB' : {
        'meta_info' : _MetaInfoClass('CISCOHSRPEXTMIB',
            False, 
            [
            _MetaInfoClassMember('cHsrpExtIfStandbyTable', REFERENCE_CLASS, 'CHsrpExtIfStandbyTable' , 'ydk.models.hsrp.CISCO_HSRP_EXT_MIB', 'CISCOHSRPEXTMIB.CHsrpExtIfStandbyTable', 
                [], [], 
                '''                A table containing information about standby
                interfaces per HSRP group.
                ''',
                'chsrpextifstandbytable',
                'CISCO-HSRP-EXT-MIB', False),
            _MetaInfoClassMember('cHsrpExtIfTable', REFERENCE_CLASS, 'CHsrpExtIfTable' , 'ydk.models.hsrp.CISCO_HSRP_EXT_MIB', 'CISCOHSRPEXTMIB.CHsrpExtIfTable', 
                [], [], 
                '''                HSRP-specific configurations for each physical interface.
                ''',
                'chsrpextiftable',
                'CISCO-HSRP-EXT-MIB', False),
            _MetaInfoClassMember('cHsrpExtIfTrackedTable', REFERENCE_CLASS, 'CHsrpExtIfTrackedTable' , 'ydk.models.hsrp.CISCO_HSRP_EXT_MIB', 'CISCOHSRPEXTMIB.CHsrpExtIfTrackedTable', 
                [], [], 
                '''                A table containing information about tracked interfaces per
                HSRP group.
                ''',
                'chsrpextiftrackedtable',
                'CISCO-HSRP-EXT-MIB', False),
            _MetaInfoClassMember('cHsrpExtSecAddrTable', REFERENCE_CLASS, 'CHsrpExtSecAddrTable' , 'ydk.models.hsrp.CISCO_HSRP_EXT_MIB', 'CISCOHSRPEXTMIB.CHsrpExtSecAddrTable', 
                [], [], 
                '''                A table containing information about secondary HSRP IP
                Addresses per interface and group.
                ''',
                'chsrpextsecaddrtable',
                'CISCO-HSRP-EXT-MIB', False),
            ],
            'CISCO-HSRP-EXT-MIB',
            'CISCO-HSRP-EXT-MIB',
            _yang_ns._namespaces['CISCO-HSRP-EXT-MIB'],
        'ydk.models.hsrp.CISCO_HSRP_EXT_MIB'
        ),
    },
}
_meta_table['CISCOHSRPEXTMIB.CHsrpExtIfStandbyTable.CHsrpExtIfStandbyEntry']['meta_info'].parent =_meta_table['CISCOHSRPEXTMIB.CHsrpExtIfStandbyTable']['meta_info']
_meta_table['CISCOHSRPEXTMIB.CHsrpExtIfTable.CHsrpExtIfEntry']['meta_info'].parent =_meta_table['CISCOHSRPEXTMIB.CHsrpExtIfTable']['meta_info']
_meta_table['CISCOHSRPEXTMIB.CHsrpExtIfTrackedTable.CHsrpExtIfTrackedEntry']['meta_info'].parent =_meta_table['CISCOHSRPEXTMIB.CHsrpExtIfTrackedTable']['meta_info']
_meta_table['CISCOHSRPEXTMIB.CHsrpExtSecAddrTable.CHsrpExtSecAddrEntry']['meta_info'].parent =_meta_table['CISCOHSRPEXTMIB.CHsrpExtSecAddrTable']['meta_info']
_meta_table['CISCOHSRPEXTMIB.CHsrpExtIfStandbyTable']['meta_info'].parent =_meta_table['CISCOHSRPEXTMIB']['meta_info']
_meta_table['CISCOHSRPEXTMIB.CHsrpExtIfTable']['meta_info'].parent =_meta_table['CISCOHSRPEXTMIB']['meta_info']
_meta_table['CISCOHSRPEXTMIB.CHsrpExtIfTrackedTable']['meta_info'].parent =_meta_table['CISCOHSRPEXTMIB']['meta_info']
_meta_table['CISCOHSRPEXTMIB.CHsrpExtSecAddrTable']['meta_info'].parent =_meta_table['CISCOHSRPEXTMIB']['meta_info']

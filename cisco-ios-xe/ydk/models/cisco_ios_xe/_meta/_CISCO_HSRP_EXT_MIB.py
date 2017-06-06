


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoHsrpExtMib.Chsrpextiftrackedtable.Chsrpextiftrackedentry' : {
        'meta_info' : _MetaInfoClass('CiscoHsrpExtMib.Chsrpextiftrackedtable.Chsrpextiftrackedentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-HSRP-EXT-MIB', True),
            _MetaInfoClassMember('cHsrpGrpNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                ''',
                'chsrpgrpnumber',
                'CISCO-HSRP-EXT-MIB', True),
            _MetaInfoClassMember('cHsrpExtIfTracked', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The ifIndex value of the tracked interface.
                ''',
                'chsrpextiftracked',
                'CISCO-HSRP-EXT-MIB', True),
            _MetaInfoClassMember('cHsrpExtIfTrackedIpNone', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies the disable HSRP IPv4 virtual
                IP address.
                ''',
                'chsrpextiftrackedipnone',
                'CISCO-HSRP-EXT-MIB', False),
            _MetaInfoClassMember('cHsrpExtIfTrackedPriority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
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
            _MetaInfoClassMember('cHsrpExtIfTrackedRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
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
        'ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB'
        ),
    },
    'CiscoHsrpExtMib.Chsrpextiftrackedtable' : {
        'meta_info' : _MetaInfoClass('CiscoHsrpExtMib.Chsrpextiftrackedtable',
            False, 
            [
            _MetaInfoClassMember('cHsrpExtIfTrackedEntry', REFERENCE_LIST, 'Chsrpextiftrackedentry' , 'ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB', 'CiscoHsrpExtMib.Chsrpextiftrackedtable.Chsrpextiftrackedentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB'
        ),
    },
    'CiscoHsrpExtMib.Chsrpextsecaddrtable.Chsrpextsecaddrentry' : {
        'meta_info' : _MetaInfoClass('CiscoHsrpExtMib.Chsrpextsecaddrtable.Chsrpextsecaddrentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-HSRP-EXT-MIB', True),
            _MetaInfoClassMember('cHsrpGrpNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                ''',
                'chsrpgrpnumber',
                'CISCO-HSRP-EXT-MIB', True),
            _MetaInfoClassMember('cHsrpExtSecAddrAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                A secondary IpAddress for the {ifIndex, cHsrpGrpNumber} pair.
                As explained in the DESCRIPTION for cHsrpExtSecAddrEntry, a
                primary address must exist before a secondary address for 
                the same {ifIndex, cHsrpGrpNumber} pair can be created.
                ''',
                'chsrpextsecaddraddress',
                'CISCO-HSRP-EXT-MIB', True),
            _MetaInfoClassMember('cHsrpExtSecAddrRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
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
        'ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB'
        ),
    },
    'CiscoHsrpExtMib.Chsrpextsecaddrtable' : {
        'meta_info' : _MetaInfoClass('CiscoHsrpExtMib.Chsrpextsecaddrtable',
            False, 
            [
            _MetaInfoClassMember('cHsrpExtSecAddrEntry', REFERENCE_LIST, 'Chsrpextsecaddrentry' , 'ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB', 'CiscoHsrpExtMib.Chsrpextsecaddrtable.Chsrpextsecaddrentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB'
        ),
    },
    'CiscoHsrpExtMib.Chsrpextifstandbytable.Chsrpextifstandbyentry' : {
        'meta_info' : _MetaInfoClass('CiscoHsrpExtMib.Chsrpextifstandbytable.Chsrpextifstandbyentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-HSRP-EXT-MIB', True),
            _MetaInfoClassMember('cHsrpGrpNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                ''',
                'chsrpgrpnumber',
                'CISCO-HSRP-EXT-MIB', True),
            _MetaInfoClassMember('cHsrpExtIfStandbyIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4')], [], 
                '''                This object defines the index of the standby table.
                ''',
                'chsrpextifstandbyindex',
                'CISCO-HSRP-EXT-MIB', True),
            _MetaInfoClassMember('cHsrpExtIfStandbyDestAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the destination IP address of
                the standby router.
                ''',
                'chsrpextifstandbydestaddr',
                'CISCO-HSRP-EXT-MIB', False),
            _MetaInfoClassMember('cHsrpExtIfStandbyDestAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                This object specifies the type of Internet address
                denoted by cHsrpExtIfStandbyDestAddr.
                ''',
                'chsrpextifstandbydestaddrtype',
                'CISCO-HSRP-EXT-MIB', False),
            _MetaInfoClassMember('cHsrpExtIfStandbyRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
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
            _MetaInfoClassMember('cHsrpExtIfStandbySourceAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
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
        'ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB'
        ),
    },
    'CiscoHsrpExtMib.Chsrpextifstandbytable' : {
        'meta_info' : _MetaInfoClass('CiscoHsrpExtMib.Chsrpextifstandbytable',
            False, 
            [
            _MetaInfoClassMember('cHsrpExtIfStandbyEntry', REFERENCE_LIST, 'Chsrpextifstandbyentry' , 'ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB', 'CiscoHsrpExtMib.Chsrpextifstandbytable.Chsrpextifstandbyentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB'
        ),
    },
    'CiscoHsrpExtMib.Chsrpextiftable.Chsrpextifentry' : {
        'meta_info' : _MetaInfoClass('CiscoHsrpExtMib.Chsrpextiftable.Chsrpextifentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-HSRP-EXT-MIB', True),
            _MetaInfoClassMember('cHsrpExtIfRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
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
        'ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB'
        ),
    },
    'CiscoHsrpExtMib.Chsrpextiftable' : {
        'meta_info' : _MetaInfoClass('CiscoHsrpExtMib.Chsrpextiftable',
            False, 
            [
            _MetaInfoClassMember('cHsrpExtIfEntry', REFERENCE_LIST, 'Chsrpextifentry' , 'ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB', 'CiscoHsrpExtMib.Chsrpextiftable.Chsrpextifentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB'
        ),
    },
    'CiscoHsrpExtMib' : {
        'meta_info' : _MetaInfoClass('CiscoHsrpExtMib',
            False, 
            [
            _MetaInfoClassMember('cHsrpExtIfStandbyTable', REFERENCE_CLASS, 'Chsrpextifstandbytable' , 'ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB', 'CiscoHsrpExtMib.Chsrpextifstandbytable', 
                [], [], 
                '''                A table containing information about standby
                interfaces per HSRP group.
                ''',
                'chsrpextifstandbytable',
                'CISCO-HSRP-EXT-MIB', False),
            _MetaInfoClassMember('cHsrpExtIfTable', REFERENCE_CLASS, 'Chsrpextiftable' , 'ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB', 'CiscoHsrpExtMib.Chsrpextiftable', 
                [], [], 
                '''                HSRP-specific configurations for each physical interface.
                ''',
                'chsrpextiftable',
                'CISCO-HSRP-EXT-MIB', False),
            _MetaInfoClassMember('cHsrpExtIfTrackedTable', REFERENCE_CLASS, 'Chsrpextiftrackedtable' , 'ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB', 'CiscoHsrpExtMib.Chsrpextiftrackedtable', 
                [], [], 
                '''                A table containing information about tracked interfaces per
                HSRP group.
                ''',
                'chsrpextiftrackedtable',
                'CISCO-HSRP-EXT-MIB', False),
            _MetaInfoClassMember('cHsrpExtSecAddrTable', REFERENCE_CLASS, 'Chsrpextsecaddrtable' , 'ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB', 'CiscoHsrpExtMib.Chsrpextsecaddrtable', 
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
        'ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB'
        ),
    },
}
_meta_table['CiscoHsrpExtMib.Chsrpextiftrackedtable.Chsrpextiftrackedentry']['meta_info'].parent =_meta_table['CiscoHsrpExtMib.Chsrpextiftrackedtable']['meta_info']
_meta_table['CiscoHsrpExtMib.Chsrpextsecaddrtable.Chsrpextsecaddrentry']['meta_info'].parent =_meta_table['CiscoHsrpExtMib.Chsrpextsecaddrtable']['meta_info']
_meta_table['CiscoHsrpExtMib.Chsrpextifstandbytable.Chsrpextifstandbyentry']['meta_info'].parent =_meta_table['CiscoHsrpExtMib.Chsrpextifstandbytable']['meta_info']
_meta_table['CiscoHsrpExtMib.Chsrpextiftable.Chsrpextifentry']['meta_info'].parent =_meta_table['CiscoHsrpExtMib.Chsrpextiftable']['meta_info']
_meta_table['CiscoHsrpExtMib.Chsrpextiftrackedtable']['meta_info'].parent =_meta_table['CiscoHsrpExtMib']['meta_info']
_meta_table['CiscoHsrpExtMib.Chsrpextsecaddrtable']['meta_info'].parent =_meta_table['CiscoHsrpExtMib']['meta_info']
_meta_table['CiscoHsrpExtMib.Chsrpextifstandbytable']['meta_info'].parent =_meta_table['CiscoHsrpExtMib']['meta_info']
_meta_table['CiscoHsrpExtMib.Chsrpextiftable']['meta_info'].parent =_meta_table['CiscoHsrpExtMib']['meta_info']




import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IgmpStdMib.Igmpinterfacetable.Igmpinterfaceentry' : {
        'meta_info' : _MetaInfoClass('IgmpStdMib.Igmpinterfacetable.Igmpinterfaceentry',
            False, 
            [
            _MetaInfoClassMember('igmpInterfaceIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The ifIndex value of the interface for which IGMP is
                enabled.
                ''',
                'igmpinterfaceifindex',
                'IGMP-STD-MIB', True),
            _MetaInfoClassMember('igmpInterfaceGroups', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The current number of entries for this interface in the
                Cache Table.
                ''',
                'igmpinterfacegroups',
                'IGMP-STD-MIB', False),
            _MetaInfoClassMember('igmpInterfaceJoins', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times a group membership has been added on
                this interface; that is, the number of times an entry for
                this interface has been added to the Cache Table.  This
                object gives an indication of the amount of IGMP activity
                over the lifetime of the row entry.
                ''',
                'igmpinterfacejoins',
                'IGMP-STD-MIB', False),
            _MetaInfoClassMember('igmpInterfaceLastMembQueryIntvl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The Last Member Query Interval is the Max Response Time
                inserted into Group-Specific Queries sent in response to
                Leave Group messages, and is also the amount of time between
                Group-Specific Query messages.  This value may be tuned to
                modify the leave latency of the network.  A reduced value
                results in reduced time to detect the loss of the last
                member of a group.  The value of this object is irrelevant
                if igmpInterfaceVersion is 1.
                ''',
                'igmpinterfacelastmembqueryintvl',
                'IGMP-STD-MIB', False),
            _MetaInfoClassMember('igmpInterfaceProxyIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Some devices implement a form of IGMP proxying whereby
                memberships learned on the interface represented by this
                row, cause IGMP Host Membership Reports to be sent on the
                interface whose ifIndex value is given by this object.  Such
                a device would implement the igmpV2RouterMIBGroup only on
                its router interfaces (those interfaces with non-zero
                igmpInterfaceProxyIfIndex).  Typically, the value of this
                object is 0, indicating that no proxying is being done.
                ''',
                'igmpinterfaceproxyifindex',
                'IGMP-STD-MIB', False),
            _MetaInfoClassMember('igmpInterfaceQuerier', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The address of the IGMP Querier on the IP subnet to which
                
                
                
                
                
                this interface is attached.
                ''',
                'igmpinterfacequerier',
                'IGMP-STD-MIB', False),
            _MetaInfoClassMember('igmpInterfaceQuerierExpiryTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The amount of time remaining before the Other Querier
                Present Timer expires.  If the local system is the querier,
                the value of this object is zero.
                ''',
                'igmpinterfacequerierexpirytime',
                'IGMP-STD-MIB', False),
            _MetaInfoClassMember('igmpInterfaceQuerierUpTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time since igmpInterfaceQuerier was last changed.
                ''',
                'igmpinterfacequerieruptime',
                'IGMP-STD-MIB', False),
            _MetaInfoClassMember('igmpInterfaceQueryInterval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The frequency at which IGMP Host-Query packets are
                transmitted on this interface.
                ''',
                'igmpinterfacequeryinterval',
                'IGMP-STD-MIB', False),
            _MetaInfoClassMember('igmpInterfaceQueryMaxResponseTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The maximum query response time advertised in IGMPv2
                queries on this interface.
                ''',
                'igmpinterfacequerymaxresponsetime',
                'IGMP-STD-MIB', False),
            _MetaInfoClassMember('igmpInterfaceRobustness', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                The Robustness Variable allows tuning for the expected
                packet loss on a subnet.  If a subnet is expected to be
                lossy, the Robustness Variable may be increased.  IGMP is
                robust to (Robustness Variable-1) packet losses.
                ''',
                'igmpinterfacerobustness',
                'IGMP-STD-MIB', False),
            _MetaInfoClassMember('igmpInterfaceStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The activation of a row enables IGMP on the interface.  The
                destruction of a row disables IGMP on the interface.
                ''',
                'igmpinterfacestatus',
                'IGMP-STD-MIB', False),
            _MetaInfoClassMember('igmpInterfaceVersion', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The version of IGMP which is running on this interface.
                This object can be used to configure a router capable of
                running either value.  For IGMP to function correctly, all
                routers on a LAN must be configured to run the same version
                of IGMP on that LAN.
                ''',
                'igmpinterfaceversion',
                'IGMP-STD-MIB', False),
            _MetaInfoClassMember('igmpInterfaceVersion1QuerierTimer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time remaining until the host assumes that there are no
                IGMPv1 routers present on the interface.  While this is non-
                zero, the host will reply to all queries with version 1
                membership reports.
                ''',
                'igmpinterfaceversion1queriertimer',
                'IGMP-STD-MIB', False),
            _MetaInfoClassMember('igmpInterfaceWrongVersionQueries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of queries received whose IGMP version does not
                match igmpInterfaceVersion, over the lifetime of the row
                entry.  IGMP requires that all routers on a LAN be
                configured to run the same version of IGMP.  Thus, if any
                queries are received with the wrong version, this indicates
                a configuration error.
                ''',
                'igmpinterfacewrongversionqueries',
                'IGMP-STD-MIB', False),
            ],
            'IGMP-STD-MIB',
            'igmpInterfaceEntry',
            _yang_ns._namespaces['IGMP-STD-MIB'],
        'ydk.models.cisco_ios_xe.IGMP_STD_MIB'
        ),
    },
    'IgmpStdMib.Igmpinterfacetable' : {
        'meta_info' : _MetaInfoClass('IgmpStdMib.Igmpinterfacetable',
            False, 
            [
            _MetaInfoClassMember('igmpInterfaceEntry', REFERENCE_LIST, 'Igmpinterfaceentry' , 'ydk.models.cisco_ios_xe.IGMP_STD_MIB', 'IgmpStdMib.Igmpinterfacetable.Igmpinterfaceentry', 
                [], [], 
                '''                An entry (conceptual row) representing an interface on
                which IGMP is enabled.
                ''',
                'igmpinterfaceentry',
                'IGMP-STD-MIB', False),
            ],
            'IGMP-STD-MIB',
            'igmpInterfaceTable',
            _yang_ns._namespaces['IGMP-STD-MIB'],
        'ydk.models.cisco_ios_xe.IGMP_STD_MIB'
        ),
    },
    'IgmpStdMib.Igmpcachetable.Igmpcacheentry' : {
        'meta_info' : _MetaInfoClass('IgmpStdMib.Igmpcachetable.Igmpcacheentry',
            False, 
            [
            _MetaInfoClassMember('igmpCacheAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP multicast group address for which this entry
                contains information.
                ''',
                'igmpcacheaddress',
                'IGMP-STD-MIB', True),
            _MetaInfoClassMember('igmpCacheIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The interface for which this entry contains information for
                an IP multicast group address.
                ''',
                'igmpcacheifindex',
                'IGMP-STD-MIB', True),
            _MetaInfoClassMember('igmpCacheExpiryTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The minimum amount of time remaining before this entry will
                be aged out.  A value of 0 indicates that the entry is only
                present because igmpCacheSelf is true and that if the router
                left the group, this entry would be aged out immediately.
                Note that some implementations may process membership
                reports from the local system in the same way as reports
                from other hosts, so a value of 0 is not required.
                ''',
                'igmpcacheexpirytime',
                'IGMP-STD-MIB', False),
            _MetaInfoClassMember('igmpCacheLastReporter', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of the source of the last membership report
                received for this IP Multicast group address on this
                interface.  If no membership report has been received, this
                object has the value 0.0.0.0.
                ''',
                'igmpcachelastreporter',
                'IGMP-STD-MIB', False),
            _MetaInfoClassMember('igmpCacheSelf', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An indication of whether the local system is a member of
                this group address on this interface.
                ''',
                'igmpcacheself',
                'IGMP-STD-MIB', False),
            _MetaInfoClassMember('igmpCacheStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this entry.
                ''',
                'igmpcachestatus',
                'IGMP-STD-MIB', False),
            _MetaInfoClassMember('igmpCacheUpTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time elapsed since this entry was created.
                ''',
                'igmpcacheuptime',
                'IGMP-STD-MIB', False),
            _MetaInfoClassMember('igmpCacheVersion1HostTimer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time remaining until the local router will assume that
                there are no longer any IGMP version 1 members on the IP
                subnet attached to this interface.  Upon hearing any IGMPv1
                Membership Report, this value is reset to the group
                membership timer.  While this time remaining is non-zero,
                the local router ignores any IGMPv2 Leave messages for this
                group that it receives on this interface.
                ''',
                'igmpcacheversion1hosttimer',
                'IGMP-STD-MIB', False),
            ],
            'IGMP-STD-MIB',
            'igmpCacheEntry',
            _yang_ns._namespaces['IGMP-STD-MIB'],
        'ydk.models.cisco_ios_xe.IGMP_STD_MIB'
        ),
    },
    'IgmpStdMib.Igmpcachetable' : {
        'meta_info' : _MetaInfoClass('IgmpStdMib.Igmpcachetable',
            False, 
            [
            _MetaInfoClassMember('igmpCacheEntry', REFERENCE_LIST, 'Igmpcacheentry' , 'ydk.models.cisco_ios_xe.IGMP_STD_MIB', 'IgmpStdMib.Igmpcachetable.Igmpcacheentry', 
                [], [], 
                '''                An entry (conceptual row) in the igmpCacheTable.
                ''',
                'igmpcacheentry',
                'IGMP-STD-MIB', False),
            ],
            'IGMP-STD-MIB',
            'igmpCacheTable',
            _yang_ns._namespaces['IGMP-STD-MIB'],
        'ydk.models.cisco_ios_xe.IGMP_STD_MIB'
        ),
    },
    'IgmpStdMib' : {
        'meta_info' : _MetaInfoClass('IgmpStdMib',
            False, 
            [
            _MetaInfoClassMember('igmpCacheTable', REFERENCE_CLASS, 'Igmpcachetable' , 'ydk.models.cisco_ios_xe.IGMP_STD_MIB', 'IgmpStdMib.Igmpcachetable', 
                [], [], 
                '''                The (conceptual) table listing the IP multicast groups for
                which there are members on a particular interface.
                ''',
                'igmpcachetable',
                'IGMP-STD-MIB', False),
            _MetaInfoClassMember('igmpInterfaceTable', REFERENCE_CLASS, 'Igmpinterfacetable' , 'ydk.models.cisco_ios_xe.IGMP_STD_MIB', 'IgmpStdMib.Igmpinterfacetable', 
                [], [], 
                '''                The (conceptual) table listing the interfaces on which IGMP
                is enabled.
                ''',
                'igmpinterfacetable',
                'IGMP-STD-MIB', False),
            ],
            'IGMP-STD-MIB',
            'IGMP-STD-MIB',
            _yang_ns._namespaces['IGMP-STD-MIB'],
        'ydk.models.cisco_ios_xe.IGMP_STD_MIB'
        ),
    },
}
_meta_table['IgmpStdMib.Igmpinterfacetable.Igmpinterfaceentry']['meta_info'].parent =_meta_table['IgmpStdMib.Igmpinterfacetable']['meta_info']
_meta_table['IgmpStdMib.Igmpcachetable.Igmpcacheentry']['meta_info'].parent =_meta_table['IgmpStdMib.Igmpcachetable']['meta_info']
_meta_table['IgmpStdMib.Igmpinterfacetable']['meta_info'].parent =_meta_table['IgmpStdMib']['meta_info']
_meta_table['IgmpStdMib.Igmpcachetable']['meta_info'].parent =_meta_table['IgmpStdMib']['meta_info']

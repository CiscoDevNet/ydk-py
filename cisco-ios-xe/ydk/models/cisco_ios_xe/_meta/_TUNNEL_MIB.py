


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'TunnelMib.Tunneliftable.Tunnelifentry.TunnelifsecurityEnum' : _MetaInfoEnum('TunnelifsecurityEnum', 'ydk.models.cisco_ios_xe.TUNNEL_MIB',
        {
            'none':'none',
            'ipsec':'ipsec',
            'other':'other',
        }, 'TUNNEL-MIB', _yang_ns._namespaces['TUNNEL-MIB']),
    'TunnelMib.Tunneliftable.Tunnelifentry' : {
        'meta_info' : _MetaInfoClass('TunnelMib.Tunneliftable.Tunnelifentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'TUNNEL-MIB', True),
            _MetaInfoClassMember('tunnelIfAddressType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The type of address in the corresponding
                tunnelIfLocalInetAddress and tunnelIfRemoteInetAddress
                objects.
                ''',
                'tunnelifaddresstype',
                'TUNNEL-MIB', False),
            _MetaInfoClassMember('tunnelIfEncapsLimit', ATTRIBUTE, 'int' , None, None, 
                [('-1', '255')], [], 
                '''                The maximum number of additional encapsulations
                permitted for packets undergoing encapsulation at this
                node.  A value of -1 indicates that no limit is
                present (except as a result of the packet size).
                ''',
                'tunnelifencapslimit',
                'TUNNEL-MIB', False),
            _MetaInfoClassMember('tunnelIfEncapsMethod', REFERENCE_ENUM_CLASS, 'IanatunneltypeEnum' , 'ydk.models.cisco_ios_xe.IANAifType_MIB', 'IanatunneltypeEnum', 
                [], [], 
                '''                The encapsulation method used by the tunnel.
                ''',
                'tunnelifencapsmethod',
                'TUNNEL-MIB', False),
            _MetaInfoClassMember('tunnelIfFlowLabel', ATTRIBUTE, 'int' , None, None, 
                [('-1', '100')], [], 
                '''                The method used to set the IPv6 Flow Label value.
                This object need not be present in rows where
                tunnelIfAddressType indicates the tunnel is not over
                IPv6.  A value of -1 indicates that a traffic
                conditioner is invoked and more information may be
                available in a traffic conditioner MIB.  Any other
                value indicates that the Flow Label field is set to
                the indicated value.
                ''',
                'tunnelifflowlabel',
                'TUNNEL-MIB', False),
            _MetaInfoClassMember('tunnelIfHopLimit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The IPv4 TTL or IPv6 Hop Limit to use in the outer IP
                header.  A value of 0 indicates that the value is
                copied from the payload's header.
                ''',
                'tunnelifhoplimit',
                'TUNNEL-MIB', False),
            _MetaInfoClassMember('tunnelIfLocalAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The address of the local endpoint of the tunnel
                (i.e., the source address used in the outer IP
                header), or 0.0.0.0 if unknown or if the tunnel is
                over IPv6.
                
                Since this object does not support IPv6, it is
                deprecated in favor of tunnelIfLocalInetAddress.
                ''',
                'tunneliflocaladdress',
                'TUNNEL-MIB', False),
            _MetaInfoClassMember('tunnelIfLocalInetAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The address of the local endpoint of the tunnel
                (i.e., the source address used in the outer IP
                header).  If the address is unknown, the value is
                
                0.0.0.0 for IPv4 or :: for IPv6.  The type of this
                object is given by tunnelIfAddressType.
                ''',
                'tunneliflocalinetaddress',
                'TUNNEL-MIB', False),
            _MetaInfoClassMember('tunnelIfRemoteAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The address of the remote endpoint of the tunnel
                (i.e., the destination address used in the outer IP
                header), or 0.0.0.0 if unknown, or an IPv6 address, or
                
                the tunnel is not a point-to-point link (e.g., if it
                is a 6to4 tunnel).
                
                Since this object does not support IPv6, it is
                deprecated in favor of tunnelIfRemoteInetAddress.
                ''',
                'tunnelifremoteaddress',
                'TUNNEL-MIB', False),
            _MetaInfoClassMember('tunnelIfRemoteInetAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The address of the remote endpoint of the tunnel
                (i.e., the destination address used in the outer IP
                header).  If the address is unknown or the tunnel is
                not a point-to-point link (e.g., if it is a 6to4
                tunnel), the value is 0.0.0.0 for tunnels over IPv4 or
                :: for tunnels over IPv6.  The type of this object is
                given by tunnelIfAddressType.
                ''',
                'tunnelifremoteinetaddress',
                'TUNNEL-MIB', False),
            _MetaInfoClassMember('tunnelIfSecurity', REFERENCE_ENUM_CLASS, 'TunnelifsecurityEnum' , 'ydk.models.cisco_ios_xe.TUNNEL_MIB', 'TunnelMib.Tunneliftable.Tunnelifentry.TunnelifsecurityEnum', 
                [], [], 
                '''                The method used by the tunnel to secure the outer IP
                header.  The value ipsec indicates that IPsec is used
                between the tunnel endpoints for authentication or
                encryption or both.  More specific security-related
                information may be available in a MIB module for the
                security protocol in use.
                ''',
                'tunnelifsecurity',
                'TUNNEL-MIB', False),
            _MetaInfoClassMember('tunnelIfTOS', ATTRIBUTE, 'int' , None, None, 
                [('-2', '63')], [], 
                '''                The method used to set the high 6 bits (the
                
                differentiated services codepoint) of the IPv4 TOS or
                IPv6 Traffic Class in the outer IP header.  A value of
                -1 indicates that the bits are copied from the
                payload's header.  A value of -2 indicates that a
                traffic conditioner is invoked and more information
                may be available in a traffic conditioner MIB module.
                A value between 0 and 63 inclusive indicates that the
                bit field is set to the indicated value.
                
                Note: instead of the name tunnelIfTOS, a better name
                would have been tunnelIfDSCPMethod, but the existing
                name appeared in RFC 2667 and existing objects cannot
                be renamed.
                ''',
                'tunneliftos',
                'TUNNEL-MIB', False),
            ],
            'TUNNEL-MIB',
            'tunnelIfEntry',
            _yang_ns._namespaces['TUNNEL-MIB'],
        'ydk.models.cisco_ios_xe.TUNNEL_MIB'
        ),
    },
    'TunnelMib.Tunneliftable' : {
        'meta_info' : _MetaInfoClass('TunnelMib.Tunneliftable',
            False, 
            [
            _MetaInfoClassMember('tunnelIfEntry', REFERENCE_LIST, 'Tunnelifentry' , 'ydk.models.cisco_ios_xe.TUNNEL_MIB', 'TunnelMib.Tunneliftable.Tunnelifentry', 
                [], [], 
                '''                An entry (conceptual row) containing the information
                on a particular configured tunnel.
                ''',
                'tunnelifentry',
                'TUNNEL-MIB', False),
            ],
            'TUNNEL-MIB',
            'tunnelIfTable',
            _yang_ns._namespaces['TUNNEL-MIB'],
        'ydk.models.cisco_ios_xe.TUNNEL_MIB'
        ),
    },
    'TunnelMib.Tunnelconfigtable.Tunnelconfigentry' : {
        'meta_info' : _MetaInfoClass('TunnelMib.Tunnelconfigtable.Tunnelconfigentry',
            False, 
            [
            _MetaInfoClassMember('tunnelConfigLocalAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The address of the local endpoint of the tunnel, or
                0.0.0.0 if the device is free to choose any of its
                addresses at tunnel establishment time.
                
                Since this object does not support IPv6, it is
                deprecated in favor of tunnelInetConfigLocalAddress.
                ''',
                'tunnelconfiglocaladdress',
                'TUNNEL-MIB', True),
            _MetaInfoClassMember('tunnelConfigRemoteAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The address of the remote endpoint of the tunnel.
                
                Since this object does not support IPv6, it is
                deprecated in favor of tunnelInetConfigRemoteAddress.
                ''',
                'tunnelconfigremoteaddress',
                'TUNNEL-MIB', True),
            _MetaInfoClassMember('tunnelConfigEncapsMethod', REFERENCE_ENUM_CLASS, 'IanatunneltypeEnum' , 'ydk.models.cisco_ios_xe.IANAifType_MIB', 'IanatunneltypeEnum', 
                [], [], 
                '''                The encapsulation method used by the tunnel.
                
                Since this object does not support IPv6, it is
                deprecated in favor of tunnelInetConfigEncapsMethod.
                ''',
                'tunnelconfigencapsmethod',
                'TUNNEL-MIB', True),
            _MetaInfoClassMember('tunnelConfigID', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                An identifier used to distinguish between multiple
                tunnels of the same encapsulation method, with the
                same endpoints.  If the encapsulation protocol only
                allows one tunnel per set of endpoint addresses (such
                as for GRE or IP-in-IP), the value of this object is
                1.  For encapsulation methods (such as L2F) which
                allow multiple parallel tunnels, the manager is
                responsible for choosing any ID which does not
                conflict with an existing row, such as choosing a
                random number.
                
                Since this object does not support IPv6, it is
                deprecated in favor of tunnelInetConfigID.
                ''',
                'tunnelconfigid',
                'TUNNEL-MIB', True),
            _MetaInfoClassMember('tunnelConfigIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                If the value of tunnelConfigStatus for this row is
                active, then this object contains the value of ifIndex
                corresponding to the tunnel interface.  A value of 0
                is not legal in the active state, and means that the
                interface index has not yet been assigned.
                
                Since this object does not support IPv6, it is
                deprecated in favor of tunnelInetConfigIfIndex.
                ''',
                'tunnelconfigifindex',
                'TUNNEL-MIB', False),
            _MetaInfoClassMember('tunnelConfigStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this row, by which new entries may be
                created, or old entries deleted from this table.  The
                agent need not support setting this object to
                createAndWait or notInService since there are no other
                writable objects in this table, and writable objects
                in rows of corresponding tables such as the
                tunnelIfTable may be modified while this row is
                active.
                
                To create a row in this table for an encapsulation
                method which does not support multiple parallel
                tunnels with the same endpoints, the management
                station should simply use a tunnelConfigID of 1, and
                set tunnelConfigStatus to createAndGo.  For
                encapsulation methods such as L2F which allow multiple
                parallel tunnels, the management station may select a
                pseudo-random number to use as the tunnelConfigID and
                set tunnelConfigStatus to createAndGo.  In the event
                that this ID is already in use and an
                inconsistentValue is returned in response to the set
                operation, the management station should simply select
                a new pseudo-random number and retry the operation.
                
                Creating a row in this table will cause an interface
                index to be assigned by the agent in an
                implementation-dependent manner, and corresponding
                rows will be instantiated in the ifTable and the
                tunnelIfTable.  The status of this row will become
                active as soon as the agent assigns the interface
                index, regardless of whether the interface is
                operationally up.
                
                Deleting a row in this table will likewise delete the
                corresponding row in the ifTable and in the
                tunnelIfTable.
                
                Since this object does not support IPv6, it is
                deprecated in favor of tunnelInetConfigStatus.
                ''',
                'tunnelconfigstatus',
                'TUNNEL-MIB', False),
            ],
            'TUNNEL-MIB',
            'tunnelConfigEntry',
            _yang_ns._namespaces['TUNNEL-MIB'],
        'ydk.models.cisco_ios_xe.TUNNEL_MIB'
        ),
    },
    'TunnelMib.Tunnelconfigtable' : {
        'meta_info' : _MetaInfoClass('TunnelMib.Tunnelconfigtable',
            False, 
            [
            _MetaInfoClassMember('tunnelConfigEntry', REFERENCE_LIST, 'Tunnelconfigentry' , 'ydk.models.cisco_ios_xe.TUNNEL_MIB', 'TunnelMib.Tunnelconfigtable.Tunnelconfigentry', 
                [], [], 
                '''                An entry (conceptual row) containing the information
                on a particular configured tunnel.
                
                Since this entry does not support IPv6, it is
                deprecated in favor of tunnelInetConfigEntry.
                ''',
                'tunnelconfigentry',
                'TUNNEL-MIB', False),
            ],
            'TUNNEL-MIB',
            'tunnelConfigTable',
            _yang_ns._namespaces['TUNNEL-MIB'],
        'ydk.models.cisco_ios_xe.TUNNEL_MIB'
        ),
    },
    'TunnelMib.Tunnelinetconfigtable.Tunnelinetconfigentry' : {
        'meta_info' : _MetaInfoClass('TunnelMib.Tunnelinetconfigtable.Tunnelinetconfigentry',
            False, 
            [
            _MetaInfoClassMember('tunnelInetConfigAddressType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The address type over which the tunnel encapsulates
                packets.
                ''',
                'tunnelinetconfigaddresstype',
                'TUNNEL-MIB', True),
            _MetaInfoClassMember('tunnelInetConfigLocalAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The address of the local endpoint of the tunnel, or
                0.0.0.0 (for IPv4) or :: (for IPv6) if the device is
                free to choose any of its addresses at tunnel
                establishment time.
                ''',
                'tunnelinetconfiglocaladdress',
                'TUNNEL-MIB', True),
            _MetaInfoClassMember('tunnelInetConfigRemoteAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The address of the remote endpoint of the tunnel.
                ''',
                'tunnelinetconfigremoteaddress',
                'TUNNEL-MIB', True),
            _MetaInfoClassMember('tunnelInetConfigEncapsMethod', REFERENCE_ENUM_CLASS, 'IanatunneltypeEnum' , 'ydk.models.cisco_ios_xe.IANAifType_MIB', 'IanatunneltypeEnum', 
                [], [], 
                '''                The encapsulation method used by the tunnel.
                ''',
                'tunnelinetconfigencapsmethod',
                'TUNNEL-MIB', True),
            _MetaInfoClassMember('tunnelInetConfigID', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                An identifier used to distinguish between multiple
                tunnels of the same encapsulation method, with the
                same endpoints.  If the encapsulation protocol only
                allows one tunnel per set of endpoint addresses (such
                as for GRE or IP-in-IP), the value of this object is
                1.  For encapsulation methods (such as L2F) which
                allow multiple parallel tunnels, the manager is
                responsible for choosing any ID which does not
                
                conflict with an existing row, such as choosing a
                random number.
                ''',
                'tunnelinetconfigid',
                'TUNNEL-MIB', True),
            _MetaInfoClassMember('tunnelInetConfigIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                If the value of tunnelInetConfigStatus for this row
                is active, then this object contains the value of
                ifIndex corresponding to the tunnel interface.  A
                value of 0 is not legal in the active state, and means
                that the interface index has not yet been assigned.
                ''',
                'tunnelinetconfigifindex',
                'TUNNEL-MIB', False),
            _MetaInfoClassMember('tunnelInetConfigStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this row, by which new entries may be
                created, or old entries deleted from this table.  The
                agent need not support setting this object to
                createAndWait or notInService since there are no other
                writable objects in this table, and writable objects
                in rows of corresponding tables such as the
                tunnelIfTable may be modified while this row is
                active.
                
                To create a row in this table for an encapsulation
                method which does not support multiple parallel
                tunnels with the same endpoints, the management
                station should simply use a tunnelInetConfigID of 1,
                and set tunnelInetConfigStatus to createAndGo.  For
                encapsulation methods such as L2F which allow multiple
                parallel tunnels, the management station may select a
                pseudo-random number to use as the tunnelInetConfigID
                and set tunnelInetConfigStatus to createAndGo.  In the
                event that this ID is already in use and an
                inconsistentValue is returned in response to the set
                operation, the management station should simply select
                a new pseudo-random number and retry the operation.
                
                Creating a row in this table will cause an interface
                index to be assigned by the agent in an
                implementation-dependent manner, and corresponding
                rows will be instantiated in the ifTable and the
                
                tunnelIfTable.  The status of this row will become
                active as soon as the agent assigns the interface
                index, regardless of whether the interface is
                operationally up.
                
                Deleting a row in this table will likewise delete the
                corresponding row in the ifTable and in the
                tunnelIfTable.
                ''',
                'tunnelinetconfigstatus',
                'TUNNEL-MIB', False),
            _MetaInfoClassMember('tunnelInetConfigStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type of this row.  If the row is
                permanent(4), no objects in the row need be writable.
                ''',
                'tunnelinetconfigstoragetype',
                'TUNNEL-MIB', False),
            ],
            'TUNNEL-MIB',
            'tunnelInetConfigEntry',
            _yang_ns._namespaces['TUNNEL-MIB'],
        'ydk.models.cisco_ios_xe.TUNNEL_MIB'
        ),
    },
    'TunnelMib.Tunnelinetconfigtable' : {
        'meta_info' : _MetaInfoClass('TunnelMib.Tunnelinetconfigtable',
            False, 
            [
            _MetaInfoClassMember('tunnelInetConfigEntry', REFERENCE_LIST, 'Tunnelinetconfigentry' , 'ydk.models.cisco_ios_xe.TUNNEL_MIB', 'TunnelMib.Tunnelinetconfigtable.Tunnelinetconfigentry', 
                [], [], 
                '''                An entry (conceptual row) containing the information
                on a particular configured tunnel.  Note that there is
                a 128 subid maximum for object OIDs.  Implementers
                need to be aware that if the total number of octets in
                tunnelInetConfigLocalAddress and
                tunnelInetConfigRemoteAddress exceeds 110 then OIDs of
                column instances in this table will have more than 128
                sub-identifiers and cannot be accessed using SNMPv1,
                SNMPv2c, or SNMPv3.  In practice this is not expected
                to be a problem since IPv4 and IPv6 addresses will not
                cause the limit to be reached, but if other types are
                supported by an agent, care must be taken to ensure
                that the sum of the lengths do not cause the limit to
                be exceeded.
                ''',
                'tunnelinetconfigentry',
                'TUNNEL-MIB', False),
            ],
            'TUNNEL-MIB',
            'tunnelInetConfigTable',
            _yang_ns._namespaces['TUNNEL-MIB'],
        'ydk.models.cisco_ios_xe.TUNNEL_MIB'
        ),
    },
    'TunnelMib' : {
        'meta_info' : _MetaInfoClass('TunnelMib',
            False, 
            [
            _MetaInfoClassMember('tunnelConfigTable', REFERENCE_CLASS, 'Tunnelconfigtable' , 'ydk.models.cisco_ios_xe.TUNNEL_MIB', 'TunnelMib.Tunnelconfigtable', 
                [], [], 
                '''                The (conceptual) table containing information on
                configured tunnels.  This table can be used to map a
                set of tunnel endpoints to the associated ifIndex
                value.  It can also be used for row creation.  Note
                that every row in the tunnelIfTable with a fixed IPv4
                destination address should have a corresponding row in
                the tunnelConfigTable, regardless of whether it was
                created via SNMP.
                
                Since this table does not support IPv6, it is
                deprecated in favor of tunnelInetConfigTable.
                ''',
                'tunnelconfigtable',
                'TUNNEL-MIB', False),
            _MetaInfoClassMember('tunnelIfTable', REFERENCE_CLASS, 'Tunneliftable' , 'ydk.models.cisco_ios_xe.TUNNEL_MIB', 'TunnelMib.Tunneliftable', 
                [], [], 
                '''                The (conceptual) table containing information on
                configured tunnels.
                ''',
                'tunneliftable',
                'TUNNEL-MIB', False),
            _MetaInfoClassMember('tunnelInetConfigTable', REFERENCE_CLASS, 'Tunnelinetconfigtable' , 'ydk.models.cisco_ios_xe.TUNNEL_MIB', 'TunnelMib.Tunnelinetconfigtable', 
                [], [], 
                '''                The (conceptual) table containing information on
                configured tunnels.  This table can be used to map a
                set of tunnel endpoints to the associated ifIndex
                value.  It can also be used for row creation.  Note
                that every row in the tunnelIfTable with a fixed
                destination address should have a corresponding row in
                the tunnelInetConfigTable, regardless of whether it
                was created via SNMP.
                ''',
                'tunnelinetconfigtable',
                'TUNNEL-MIB', False),
            ],
            'TUNNEL-MIB',
            'TUNNEL-MIB',
            _yang_ns._namespaces['TUNNEL-MIB'],
        'ydk.models.cisco_ios_xe.TUNNEL_MIB'
        ),
    },
}
_meta_table['TunnelMib.Tunneliftable.Tunnelifentry']['meta_info'].parent =_meta_table['TunnelMib.Tunneliftable']['meta_info']
_meta_table['TunnelMib.Tunnelconfigtable.Tunnelconfigentry']['meta_info'].parent =_meta_table['TunnelMib.Tunnelconfigtable']['meta_info']
_meta_table['TunnelMib.Tunnelinetconfigtable.Tunnelinetconfigentry']['meta_info'].parent =_meta_table['TunnelMib.Tunnelinetconfigtable']['meta_info']
_meta_table['TunnelMib.Tunneliftable']['meta_info'].parent =_meta_table['TunnelMib']['meta_info']
_meta_table['TunnelMib.Tunnelconfigtable']['meta_info'].parent =_meta_table['TunnelMib']['meta_info']
_meta_table['TunnelMib.Tunnelinetconfigtable']['meta_info'].parent =_meta_table['TunnelMib']['meta_info']

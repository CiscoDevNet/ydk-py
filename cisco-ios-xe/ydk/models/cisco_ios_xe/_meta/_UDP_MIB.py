


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'UdpMib.Udp' : {
        'meta_info' : _MetaInfoClass('UdpMib.Udp',
            False, 
            [
            _MetaInfoClassMember('udpHCInDatagrams', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of UDP datagrams delivered to UDP
                users, for devices that can receive more than 1
                million UDP datagrams per second.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by discontinuities in the
                value of sysUpTime.
                ''',
                'udphcindatagrams',
                'UDP-MIB', False),
            _MetaInfoClassMember('udpHCOutDatagrams', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of UDP datagrams sent from this
                entity, for devices that can transmit more than 1
                million UDP datagrams per second.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by discontinuities in the
                value of sysUpTime.
                ''',
                'udphcoutdatagrams',
                'UDP-MIB', False),
            _MetaInfoClassMember('udpInDatagrams', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of UDP datagrams delivered to UDP
                users.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by discontinuities in the
                value of sysUpTime.
                ''',
                'udpindatagrams',
                'UDP-MIB', False),
            _MetaInfoClassMember('udpInErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of received UDP datagrams that could not be
                delivered for reasons other than the lack of an
                application at the destination port.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by discontinuities in the
                value of sysUpTime.
                ''',
                'udpinerrors',
                'UDP-MIB', False),
            _MetaInfoClassMember('udpNoPorts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of received UDP datagrams for which
                there was no application at the destination port.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by discontinuities in the
                value of sysUpTime.
                ''',
                'udpnoports',
                'UDP-MIB', False),
            _MetaInfoClassMember('udpOutDatagrams', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of UDP datagrams sent from this
                entity.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by discontinuities in the
                value of sysUpTime.
                ''',
                'udpoutdatagrams',
                'UDP-MIB', False),
            ],
            'UDP-MIB',
            'udp',
            _yang_ns._namespaces['UDP-MIB'],
        'ydk.models.cisco_ios_xe.UDP_MIB'
        ),
    },
    'UdpMib.Udptable.Udpentry' : {
        'meta_info' : _MetaInfoClass('UdpMib.Udptable.Udpentry',
            False, 
            [
            _MetaInfoClassMember('udpLocalAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The local IP address for this UDP listener.  In the
                case of a UDP listener that is willing to accept
                datagrams for any IP interface associated with the
                node, the value 0.0.0.0 is used.
                ''',
                'udplocaladdress',
                'UDP-MIB', True),
            _MetaInfoClassMember('udpLocalPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The local port number for this UDP listener.
                ''',
                'udplocalport',
                'UDP-MIB', True),
            ],
            'UDP-MIB',
            'udpEntry',
            _yang_ns._namespaces['UDP-MIB'],
        'ydk.models.cisco_ios_xe.UDP_MIB'
        ),
    },
    'UdpMib.Udptable' : {
        'meta_info' : _MetaInfoClass('UdpMib.Udptable',
            False, 
            [
            _MetaInfoClassMember('udpEntry', REFERENCE_LIST, 'Udpentry' , 'ydk.models.cisco_ios_xe.UDP_MIB', 'UdpMib.Udptable.Udpentry', 
                [], [], 
                '''                Information about a particular current UDP listener.
                ''',
                'udpentry',
                'UDP-MIB', False),
            ],
            'UDP-MIB',
            'udpTable',
            _yang_ns._namespaces['UDP-MIB'],
        'ydk.models.cisco_ios_xe.UDP_MIB'
        ),
    },
    'UdpMib.Udpendpointtable.Udpendpointentry' : {
        'meta_info' : _MetaInfoClass('UdpMib.Udpendpointtable.Udpendpointentry',
            False, 
            [
            _MetaInfoClassMember('udpEndpointLocalAddressType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The address type of udpEndpointLocalAddress.  Only
                IPv4, IPv4z, IPv6, and IPv6z addresses are expected, or
                unknown(0) if datagrams for all local IP addresses are
                accepted.
                ''',
                'udpendpointlocaladdresstype',
                'UDP-MIB', True),
            _MetaInfoClassMember('udpEndpointLocalAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The local IP address for this UDP endpoint.
                
                The value of this object can be represented in three
                
                possible ways, depending on the characteristics of the
                listening application:
                
                1. For an application that is willing to accept both
                   IPv4 and IPv6 datagrams, the value of this object
                   must be ''h (a zero-length octet-string), with
                   the value of the corresponding instance of the
                   udpEndpointLocalAddressType object being unknown(0).
                
                2. For an application that is willing to accept only IPv4
                   or only IPv6 datagrams, the value of this object
                   must be '0.0.0.0' or '::', respectively, while the
                   corresponding instance of the
                   udpEndpointLocalAddressType object represents the
                   appropriate address type.
                
                3. For an application that is listening for data
                   destined only to a specific IP address, the value
                   of this object is the specific IP address for which
                   this node is receiving packets, with the
                   corresponding instance of the
                   udpEndpointLocalAddressType object representing the
                   appropriate address type.
                
                As this object is used in the index for the
                udpEndpointTable, implementors of this table should be
                careful not to create entries that would result in OIDs
                with more than 128 subidentifiers; else the information
                cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3.
                ''',
                'udpendpointlocaladdress',
                'UDP-MIB', True),
            _MetaInfoClassMember('udpEndpointLocalPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The local port number for this UDP endpoint.
                ''',
                'udpendpointlocalport',
                'UDP-MIB', True),
            _MetaInfoClassMember('udpEndpointRemoteAddressType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The address type of udpEndpointRemoteAddress.  Only
                IPv4, IPv4z, IPv6, and IPv6z addresses are expected, or
                unknown(0) if datagrams for all remote IP addresses are
                accepted.  Also, note that some combinations of
                
                udpEndpointLocalAdressType and
                udpEndpointRemoteAddressType are not supported.  In
                particular, if the value of this object is not
                unknown(0), it is expected to always refer to the
                same IP version as udpEndpointLocalAddressType.
                ''',
                'udpendpointremoteaddresstype',
                'UDP-MIB', True),
            _MetaInfoClassMember('udpEndpointRemoteAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The remote IP address for this UDP endpoint.  If
                datagrams from any remote system are to be accepted,
                this value is ''h (a zero-length octet-string).
                Otherwise, it has the type described by
                udpEndpointRemoteAddressType and is the address of the
                remote system from which datagrams are to be accepted
                (or to which all datagrams will be sent).
                
                As this object is used in the index for the
                udpEndpointTable, implementors of this table should be
                careful not to create entries that would result in OIDs
                with more than 128 subidentifiers; else the information
                cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3.
                ''',
                'udpendpointremoteaddress',
                'UDP-MIB', True),
            _MetaInfoClassMember('udpEndpointRemotePort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The remote port number for this UDP endpoint.  If
                datagrams from any remote system are to be accepted,
                this value is zero.
                ''',
                'udpendpointremoteport',
                'UDP-MIB', True),
            _MetaInfoClassMember('udpEndpointInstance', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                The instance of this tuple.  This object is used to
                distinguish among multiple processes 'connected' to
                the same UDP endpoint.  For example, on a system
                implementing the BSD sockets interface, this would be
                used to support the SO_REUSEADDR and SO_REUSEPORT
                socket options.
                ''',
                'udpendpointinstance',
                'UDP-MIB', True),
            _MetaInfoClassMember('udpEndpointProcess', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The system's process ID for the process associated with
                this endpoint, or zero if there is no such process.
                This value is expected to be the same as
                HOST-RESOURCES-MIB::hrSWRunIndex or SYSAPPL-MIB::
                sysApplElmtRunIndex for some row in the appropriate
                tables.
                ''',
                'udpendpointprocess',
                'UDP-MIB', False),
            ],
            'UDP-MIB',
            'udpEndpointEntry',
            _yang_ns._namespaces['UDP-MIB'],
        'ydk.models.cisco_ios_xe.UDP_MIB'
        ),
    },
    'UdpMib.Udpendpointtable' : {
        'meta_info' : _MetaInfoClass('UdpMib.Udpendpointtable',
            False, 
            [
            _MetaInfoClassMember('udpEndpointEntry', REFERENCE_LIST, 'Udpendpointentry' , 'ydk.models.cisco_ios_xe.UDP_MIB', 'UdpMib.Udpendpointtable.Udpendpointentry', 
                [], [], 
                '''                Information about a particular current UDP endpoint.
                
                Implementers need to be aware that if the total number
                of elements (octets or sub-identifiers) in
                udpEndpointLocalAddress and udpEndpointRemoteAddress
                exceeds 111, then OIDs of column instances in this table
                will have more than 128 sub-identifiers and cannot be
                accessed using SNMPv1, SNMPv2c, or SNMPv3.
                ''',
                'udpendpointentry',
                'UDP-MIB', False),
            ],
            'UDP-MIB',
            'udpEndpointTable',
            _yang_ns._namespaces['UDP-MIB'],
        'ydk.models.cisco_ios_xe.UDP_MIB'
        ),
    },
    'UdpMib' : {
        'meta_info' : _MetaInfoClass('UdpMib',
            False, 
            [
            _MetaInfoClassMember('udp', REFERENCE_CLASS, 'Udp' , 'ydk.models.cisco_ios_xe.UDP_MIB', 'UdpMib.Udp', 
                [], [], 
                '''                ''',
                'udp',
                'UDP-MIB', False),
            _MetaInfoClassMember('udpEndpointTable', REFERENCE_CLASS, 'Udpendpointtable' , 'ydk.models.cisco_ios_xe.UDP_MIB', 'UdpMib.Udpendpointtable', 
                [], [], 
                '''                A table containing information about this entity's UDP
                endpoints on which a local application is currently
                accepting or sending datagrams.
                
                The address type in this table represents the address
                type used for the communication, irrespective of the
                higher-layer abstraction.  For example, an application
                using IPv6 'sockets' to communicate via IPv4 between
                ::ffff:10.0.0.1 and ::ffff:10.0.0.2 would use
                InetAddressType ipv4(1).
                
                Unlike the udpTable in RFC 2013, this table also allows
                the representation of an application that completely
                specifies both local and remote addresses and ports.  A
                listening application is represented in three possible
                ways:
                
                1) An application that is willing to accept both IPv4
                   and IPv6 datagrams is represented by a
                   udpEndpointLocalAddressType of unknown(0) and a
                   udpEndpointLocalAddress of ''h (a zero-length
                   octet-string).
                
                2) An application that is willing to accept only IPv4
                   or only IPv6 datagrams is represented by a
                   udpEndpointLocalAddressType of the appropriate
                   address type and a udpEndpointLocalAddress of
                   '0.0.0.0' or '::' respectively.
                
                3) An application that is listening for datagrams only
                   for a specific IP address but from any remote
                   system is represented by a
                   udpEndpointLocalAddressType of the appropriate
                   address type, with udpEndpointLocalAddress
                   specifying the local address.
                
                In all cases where the remote is a wildcard, the
                udpEndpointRemoteAddressType is unknown(0), the
                udpEndpointRemoteAddress is ''h (a zero-length
                octet-string), and the udpEndpointRemotePort is 0.
                
                If the operating system is demultiplexing UDP packets
                by remote address and port, or if the application has
                'connected' the socket specifying a default remote
                address and port, the udpEndpointRemote* values should
                be used to reflect this.
                ''',
                'udpendpointtable',
                'UDP-MIB', False),
            _MetaInfoClassMember('udpTable', REFERENCE_CLASS, 'Udptable' , 'ydk.models.cisco_ios_xe.UDP_MIB', 'UdpMib.Udptable', 
                [], [], 
                '''                A table containing IPv4-specific UDP listener
                information.  It contains information about all local
                IPv4 UDP end-points on which an application is
                currently accepting datagrams.  This table has been
                deprecated in favor of the version neutral
                udpEndpointTable.
                ''',
                'udptable',
                'UDP-MIB', False),
            ],
            'UDP-MIB',
            'UDP-MIB',
            _yang_ns._namespaces['UDP-MIB'],
        'ydk.models.cisco_ios_xe.UDP_MIB'
        ),
    },
}
_meta_table['UdpMib.Udptable.Udpentry']['meta_info'].parent =_meta_table['UdpMib.Udptable']['meta_info']
_meta_table['UdpMib.Udpendpointtable.Udpendpointentry']['meta_info'].parent =_meta_table['UdpMib.Udpendpointtable']['meta_info']
_meta_table['UdpMib.Udp']['meta_info'].parent =_meta_table['UdpMib']['meta_info']
_meta_table['UdpMib.Udptable']['meta_info'].parent =_meta_table['UdpMib']['meta_info']
_meta_table['UdpMib.Udpendpointtable']['meta_info'].parent =_meta_table['UdpMib']['meta_info']

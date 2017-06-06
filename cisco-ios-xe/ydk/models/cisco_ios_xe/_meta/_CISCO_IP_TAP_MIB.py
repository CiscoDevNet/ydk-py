


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoIpTapMib.Citapstreamencodepacket' : {
        'meta_info' : _MetaInfoClass('CiscoIpTapMib.Citapstreamencodepacket',
            False, 
            [
            _MetaInfoClassMember('citapStreamCapabilities', REFERENCE_BITS, 'Citapstreamcapabilities' , 'ydk.models.cisco_ios_xe.CISCO_IP_TAP_MIB', 'CiscoIpTapMib.Citapstreamencodepacket.Citapstreamcapabilities', 
                [], [], 
                '''                This object displays what types of intercept streams can be
                configured on this type of device. This may be dependent on
                hardware capabilities, software capabilities. The following
                fields may be supported:
                    tapEnable:   set if table entries with
                                 cTap2StreamInterceptEnable set to 'false'
                                 are used to pre-screen packets for intercept;
                                 otherwise these entries are ignored.
                    interface:   SNMP ifIndex Value may be used to select
                                 interception of all data crossing an
                                 interface or set of interfaces.
                    ipV4:        IPv4 Address or prefix may be used to select
                                 traffic to be intercepted.
                    ipV6:        IPv6 Address or prefix may be used to select
                                 traffic to be intercepted.
                    l4Port:      TCP/UDP Ports may be used to select traffic
                                 to be intercepted.
                    dscp:        DSCP (Differentiated Services Code Point) may
                                 be used to select traffic to be intercepted.
                    voip:        packets belonging to a voice session may
                                 be intercepted using source IPv4 address and
                                 source UDP port.
                ''',
                'citapstreamcapabilities',
                'CISCO-IP-TAP-MIB', False),
            ],
            'CISCO-IP-TAP-MIB',
            'citapStreamEncodePacket',
            _yang_ns._namespaces['CISCO-IP-TAP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_TAP_MIB'
        ),
    },
    'CiscoIpTapMib.Citapstreamtable.Citapstreamentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpTapMib.Citapstreamtable.Citapstreamentry',
            False, 
            [
            _MetaInfoClassMember('cTap2MediationContentId', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ctap2mediationcontentid',
                'CISCO-IP-TAP-MIB', True),
            _MetaInfoClassMember('cTap2StreamIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ctap2streamindex',
                'CISCO-IP-TAP-MIB', True),
            _MetaInfoClassMember('citapStreamAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The type of address, used in packet selection.
                ''',
                'citapstreamaddrtype',
                'CISCO-IP-TAP-MIB', False),
            _MetaInfoClassMember('citapStreamDestinationAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The Destination address or prefix used in packet selection.
                This address will be of the type specified in
                citapStreamAddrType.
                ''',
                'citapstreamdestinationaddress',
                'CISCO-IP-TAP-MIB', False),
            _MetaInfoClassMember('citapStreamDestinationLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '2040')], [], 
                '''                The length of the Destination Prefix. A value of zero causes
                all addresses to match.  This prefix length will be consistent
                with the type specified in citapStreamAddrType.
                ''',
                'citapstreamdestinationlength',
                'CISCO-IP-TAP-MIB', False),
            _MetaInfoClassMember('citapStreamDestL4PortMax', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The maximum value that the layer-4 destination port number in
                the packet must have in order to match this classifier entry.
                This value must be equal to or greater than the value specified
                for this entry in citapStreamDestL4PortMin.
                
                
                If both citapStreamDestL4PortMin and citapStreamDestL4PortMax
                are at their default values, the port number is effectively
                unused.
                ''',
                'citapstreamdestl4portmax',
                'CISCO-IP-TAP-MIB', False),
            _MetaInfoClassMember('citapStreamDestL4PortMin', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The minimum value that the layer-4 destination port number in
                the packet must have in order to match.  This value must be
                equal to or less than the value specified for this entry in
                citapStreamDestL4PortMax.
                
                
                If both citapStreamDestL4PortMin and citapStreamDestL4PortMax
                are at their default values, the port number is effectively
                unused.
                ''',
                'citapstreamdestl4portmin',
                'CISCO-IP-TAP-MIB', False),
            _MetaInfoClassMember('citapStreamFlowId', ATTRIBUTE, 'int' , None, None, 
                [('-1', '1048575')], [], 
                '''                The flow identifier in an IPv6 header. -1 indicates that the
                Flow Id is unused.
                ''',
                'citapstreamflowid',
                'CISCO-IP-TAP-MIB', False),
            _MetaInfoClassMember('citapStreamInterface', ATTRIBUTE, 'int' , None, None, 
                [('-2', '2147483647')], [], 
                '''                The ifIndex value of the interface over which traffic to be
                intercepted is received or transmitted. The interface may be
                physical or virtual. If this is the only parameter specified,
                and it is other than -2, -1 or 0, all traffic on the selected
                interface will be chosen.
                
                
                If the value is zero, matching traffic may be received or
                transmitted on any interface.  Additional selection parameters
                must be selected to limit the scope of traffic intercepted.
                This is most useful on non-routing platforms or on intercepts
                placed elsewhere than a subscriber interface.
                
                
                If the value is -1, one or both of
                citapStreamDestinationAddress and citapStreamSourceAddress
                must be specified with prefix length greater than zero.
                Matching traffic on the interface pointed to by ipRouteIfIndex
                or ipCidrRouteIfIndex values associated with those values is
                intercepted, whichever is specified to be more focused than a
                default route.  If routing changes, either by operator action
                or by routing protocol events, the interface will change with
                it. This is primarily intended for use on subscriber interfaces
                and other places where routing is guaranteed to be
                symmetrical.
                
                
                In both of these cases, it is possible to have the same packet
                selected for intersection on both its ingress and egress
                interface.  Nonetheless, only one instance of the packet is
                sent to the Mediation Device.
                
                
                If the value is -2, packets belonging to a Voice over IP (VoIP)
                session identified by citapStreamSourceAddress, 
                citapStreamSourceLen and citapStreamSourceL4PortMin may be 
                intercepted, as a specific voice session can be identified 
                with source IP address and udp port number. Other selection 
                parameters may be not considered, even if they are set by 
                the Mediation Device.
                
                
                This value must be set when creating a stream entry, either to
                select an interface, to select all interfaces, or to select the
                interface that routing chooses. Some platforms may not
                implement the entire range of options.
                ''',
                'citapstreaminterface',
                'CISCO-IP-TAP-MIB', False),
            _MetaInfoClassMember('citapStreamProtocol', ATTRIBUTE, 'int' , None, None, 
                [('-1', '255')], [], 
                '''                The IP protocol to match against the IPv4 protocol number or
                the IPv6 Next- Header number in the packet. -1 means 'any IP
                protocol'.
                ''',
                'citapstreamprotocol',
                'CISCO-IP-TAP-MIB', False),
            _MetaInfoClassMember('citapStreamSourceAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The Source Address used in packet selection. This address will
                be of the type specified in citapStreamAddrType.
                ''',
                'citapstreamsourceaddress',
                'CISCO-IP-TAP-MIB', False),
            _MetaInfoClassMember('citapStreamSourceL4PortMax', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The maximum value that the layer-4 destination port number in
                the packet must have in order to match this classifier entry.
                This value must be equal to or greater than the value specified
                for this entry in citapStreamSourceL4PortMin.
                
                
                If both citapStreamSourceL4PortMin and
                citapStreamSourceL4PortMax are at their default values, the
                port number is effectively unused.
                ''',
                'citapstreamsourcel4portmax',
                'CISCO-IP-TAP-MIB', False),
            _MetaInfoClassMember('citapStreamSourceL4PortMin', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The minimum value that the layer-4 destination port number in
                the packet must have in order to match.  This value must be
                equal to or less than the value specified for this entry in
                citapStreamSourceL4PortMax.
                
                
                If both citapStreamSourceL4PortMin and
                citapStreamSourceL4PortMax are at their default values, the
                port number is effectively unused.
                ''',
                'citapstreamsourcel4portmin',
                'CISCO-IP-TAP-MIB', False),
            _MetaInfoClassMember('citapStreamSourceLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '2040')], [], 
                '''                The length of the Source Prefix. A value of zero causes all
                addresses to match. This prefix length will be consistent with
                the type specified in citapStreamAddrType.
                ''',
                'citapstreamsourcelength',
                'CISCO-IP-TAP-MIB', False),
            _MetaInfoClassMember('citapStreamStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row. This object manages
                creation, modification, and deletion of rows in this table.
                When any rows must be changed, citapStreamStatus must be first 
                set to 'notInService'.
                ''',
                'citapstreamstatus',
                'CISCO-IP-TAP-MIB', False),
            _MetaInfoClassMember('citapStreamTosByte', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The value of the TOS byte, when masked with
                citapStreamTosByteMask, of traffic to be intercepted.  If
                citapStreamTosByte&(~citapStreamTosByteMask)!=0,
                configuration is rejected.
                ''',
                'citapstreamtosbyte',
                'CISCO-IP-TAP-MIB', False),
            _MetaInfoClassMember('citapStreamTosByteMask', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The value of the TOS byte in an IPv4 or IPv6 header is ANDed
                with citapStreamTosByteMask and compared with
                citapStreamTosByte.  If the values are equal, the comparison
                is equal. If the mask is zero and the TosByte value is zero,
                the result is to always accept.
                ''',
                'citapstreamtosbytemask',
                'CISCO-IP-TAP-MIB', False),
            _MetaInfoClassMember('citapStreamVRF', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                An ASCII string, which is the name of a Virtual Routing
                and Forwarding (VRF) table comprising the routing context
                of a Virtual Private Network. The interface or set of 
                interfaces on which the packet might be found should be 
                selected from the set of interfaces in the VRF table. 
                A string length of zero implies that global routing table
                be used for selection of interfaces on which the packet
                might be found.
                ''',
                'citapstreamvrf',
                'CISCO-IP-TAP-MIB', False),
            ],
            'CISCO-IP-TAP-MIB',
            'citapStreamEntry',
            _yang_ns._namespaces['CISCO-IP-TAP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_TAP_MIB'
        ),
    },
    'CiscoIpTapMib.Citapstreamtable' : {
        'meta_info' : _MetaInfoClass('CiscoIpTapMib.Citapstreamtable',
            False, 
            [
            _MetaInfoClassMember('citapStreamEntry', REFERENCE_LIST, 'Citapstreamentry' , 'ydk.models.cisco_ios_xe.CISCO_IP_TAP_MIB', 'CiscoIpTapMib.Citapstreamtable.Citapstreamentry', 
                [], [], 
                '''                A stream entry indicates a single data stream to be
                intercepted to a Mediation Device. Many selected data
                streams may go to the same application interface, and many
                application interfaces are supported.
                ''',
                'citapstreamentry',
                'CISCO-IP-TAP-MIB', False),
            ],
            'CISCO-IP-TAP-MIB',
            'citapStreamTable',
            _yang_ns._namespaces['CISCO-IP-TAP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_TAP_MIB'
        ),
    },
    'CiscoIpTapMib' : {
        'meta_info' : _MetaInfoClass('CiscoIpTapMib',
            False, 
            [
            _MetaInfoClassMember('citapStreamEncodePacket', REFERENCE_CLASS, 'Citapstreamencodepacket' , 'ydk.models.cisco_ios_xe.CISCO_IP_TAP_MIB', 'CiscoIpTapMib.Citapstreamencodepacket', 
                [], [], 
                '''                ''',
                'citapstreamencodepacket',
                'CISCO-IP-TAP-MIB', False),
            _MetaInfoClassMember('citapStreamTable', REFERENCE_CLASS, 'Citapstreamtable' , 'ydk.models.cisco_ios_xe.CISCO_IP_TAP_MIB', 'CiscoIpTapMib.Citapstreamtable', 
                [], [], 
                '''                The Intercept Stream IP Table lists the IPv4 and IPv6 streams
                to be intercepted.  The same data stream may be required by
                multiple taps, and one might assume that often the intercepted
                stream is a small subset of the traffic that could be
                intercepted.
                
                
                This essentially provides options for packet selection, only
                some of which might be used. For example, if all traffic to or
                from a given interface is to be intercepted, one would
                configure an entry which lists the interface, and wild-card
                everything else.  If all traffic to or from a given IP Address
                is to be intercepted, one would configure two such entries
                listing the IP Address as source and destination respectively,
                and wild-card everything else.  If a particular voice on a
                teleconference is to be intercepted, on the other hand, one
                would extract the multicast (destination) IP address, the
                source IP Address, the protocol (UDP), and the source and
                destination ports from the call control exchange and list all
                necessary information.
                
                
                The first index indicates which Mediation Device the
                intercepted traffic will be diverted to. The second index
                permits multiple classifiers to be used together, such as
                having an IP address as source or destination. The value of the
                second index is that of the stream's counter entry in the 
                cTap2StreamTable.
                
                Entries are added to this table via citapStreamStatus in 
                accordance with the RowStatus convention.
                ''',
                'citapstreamtable',
                'CISCO-IP-TAP-MIB', False),
            ],
            'CISCO-IP-TAP-MIB',
            'CISCO-IP-TAP-MIB',
            _yang_ns._namespaces['CISCO-IP-TAP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_TAP_MIB'
        ),
    },
}
_meta_table['CiscoIpTapMib.Citapstreamtable.Citapstreamentry']['meta_info'].parent =_meta_table['CiscoIpTapMib.Citapstreamtable']['meta_info']
_meta_table['CiscoIpTapMib.Citapstreamencodepacket']['meta_info'].parent =_meta_table['CiscoIpTapMib']['meta_info']
_meta_table['CiscoIpTapMib.Citapstreamtable']['meta_info'].parent =_meta_table['CiscoIpTapMib']['meta_info']

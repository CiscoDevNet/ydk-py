


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoOspfMib.Cospfgeneralgroup' : {
        'meta_info' : _MetaInfoClass('CiscoOspfMib.Cospfgeneralgroup',
            False, 
            [
            _MetaInfoClassMember('cospfOpaqueASLsaCksumSum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The 32-bit unsigned sum of the Opaque AS 
                link-state advertisements' LS checksums contained
                link state database.
                ''',
                'cospfopaqueaslsacksumsum',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfOpaqueASLsaCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of Opaque AS link-state
                advertisements in the link state database.
                ''',
                'cospfopaqueaslsacount',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfOpaqueLsaSupport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The router's support for Opaque LSA types.
                ''',
                'cospfopaquelsasupport',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfRFC1583Compatibility', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates metrics used to choose among multiple AS-
                external-LSAs. When cospfRFC1583Compatibility is set to
                enabled, only cost will be used when choosing among
                multiple AS-external-LSAs advertising the same
                destination. When cospfRFC1583Compatibility is set to
                disabled, preference will be driven first by type of
                path using cost only to break ties.
                ''',
                'cospfrfc1583compatibility',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfTrafficEngineeringSupport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The router's support for OSPF traffic engineering.
                ''',
                'cospftrafficengineeringsupport',
                'CISCO-OSPF-MIB', False),
            ],
            'CISCO-OSPF-MIB',
            'cospfGeneralGroup',
            _yang_ns._namespaces['CISCO-OSPF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB'
        ),
    },
    'CiscoOspfMib.Cospflsdbtable.Cospflsdbentry.CospflsdbtypeEnum' : _MetaInfoEnum('CospflsdbtypeEnum', 'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB',
        {
            'areaOpaqueLink':'areaOpaqueLink',
            'asOpaqueLink':'asOpaqueLink',
        }, 'CISCO-OSPF-MIB', _yang_ns._namespaces['CISCO-OSPF-MIB']),
    'CiscoOspfMib.Cospflsdbtable.Cospflsdbentry' : {
        'meta_info' : _MetaInfoClass('CiscoOspfMib.Cospflsdbtable.Cospflsdbentry',
            False, 
            [
            _MetaInfoClassMember('ospfLsdbAreaId', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                ''',
                'ospflsdbareaid',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('cospfLsdbType', REFERENCE_ENUM_CLASS, 'CospflsdbtypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB', 'CiscoOspfMib.Cospflsdbtable.Cospflsdbentry.CospflsdbtypeEnum', 
                [], [], 
                '''                The type of the link state advertisement.
                Each link state type has a separate advertisement format.
                ''',
                'cospflsdbtype',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('ospfLsdbLsid', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                ''',
                'ospflsdblsid',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('ospfLsdbRouterId', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                ''',
                'ospflsdbrouterid',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('cospfLsdbAdvertisement', ATTRIBUTE, 'str' , None, None, 
                [(1, 65535)], [], 
                '''                The entire Link State Advertisement, including
                its header.
                ''',
                'cospflsdbadvertisement',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfLsdbAge', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This field is the age of the link state advertisement in
                seconds.
                ''',
                'cospflsdbage',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfLsdbChecksum', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This field is the  checksum  of  the  complete
                contents  of  the  advertisement, excepting the
                age field.  The age field is excepted  so  that
                an   advertisement's  age  can  be  incremented
                without updating the  checksum.   The  checksum
                used  is  the same that is used for ISO connectionless
                datagrams; it is commonly referred  to
                as the Fletcher checksum.
                ''',
                'cospflsdbchecksum',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfLsdbSequence', ATTRIBUTE, 'int' , None, None, 
                [('1', '147483647')], [], 
                '''                The sequence number field is a  signed  32-bit
                integer.   It  is used to detect old and duplicate
                link state advertisements.  The  space  of
                sequence  numbers  is  linearly  ordered.   The
                larger the sequence number the more recent  the
                advertisement.
                ''',
                'cospflsdbsequence',
                'CISCO-OSPF-MIB', False),
            ],
            'CISCO-OSPF-MIB',
            'cospfLsdbEntry',
            _yang_ns._namespaces['CISCO-OSPF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB'
        ),
    },
    'CiscoOspfMib.Cospflsdbtable' : {
        'meta_info' : _MetaInfoClass('CiscoOspfMib.Cospflsdbtable',
            False, 
            [
            _MetaInfoClassMember('cospfLsdbEntry', REFERENCE_LIST, 'Cospflsdbentry' , 'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB', 'CiscoOspfMib.Cospflsdbtable.Cospflsdbentry', 
                [], [], 
                '''                A single Link State Advertisement.
                ''',
                'cospflsdbentry',
                'CISCO-OSPF-MIB', False),
            ],
            'CISCO-OSPF-MIB',
            'cospfLsdbTable',
            _yang_ns._namespaces['CISCO-OSPF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB'
        ),
    },
    'CiscoOspfMib.Cospfshamlinktable.Cospfshamlinkentry.CospfshamlinkstateEnum' : _MetaInfoEnum('CospfshamlinkstateEnum', 'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB',
        {
            'down':'down',
            'pointToPoint':'pointToPoint',
        }, 'CISCO-OSPF-MIB', _yang_ns._namespaces['CISCO-OSPF-MIB']),
    'CiscoOspfMib.Cospfshamlinktable.Cospfshamlinkentry' : {
        'meta_info' : _MetaInfoClass('CiscoOspfMib.Cospfshamlinktable.Cospfshamlinkentry',
            False, 
            [
            _MetaInfoClassMember('cospfShamLinkAreaId', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The  Transit  Area  that  the   Virtual   Link
                traverses.  By definition, this is not 0.0.0.0
                ''',
                'cospfshamlinkareaid',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('cospfShamLinkLocalIpAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The Local IP address of the sham link.
                ''',
                'cospfshamlinklocalipaddress',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('cospfShamLinkNeighborId', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The Router ID of the other end router of the sham
                link.
                ''',
                'cospfshamlinkneighborid',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('cospfShamLinkEvents', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of state changes or error events on
                this sham link
                ''',
                'cospfshamlinkevents',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfShamLinkHelloInterval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The length of time, in  seconds,  between  the
                Hello  packets that the router sends on the sham
                link.
                ''',
                'cospfshamlinkhellointerval',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfShamLinkMetric', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The Metric to be advertised.
                ''',
                'cospfshamlinkmetric',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfShamLinkRetransInterval', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                The number of seconds between  link-state  advertisement
                retransmissions,  for  adjacencies
                belonging to this  link.   This  value  is also
                used when retransmitting database description  
                and  link-state  request  packets. This value  
                should  be well over the expected round trip
                time.
                ''',
                'cospfshamlinkretransinterval',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfShamLinkRtrDeadInterval', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The number of seconds that  a  router's  Hello
                packets  have  not been seen before it's neighbors
                declare the router down.  This  should  be
                some  multiple  of  the  Hello  interval.
                ''',
                'cospfshamlinkrtrdeadinterval',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfShamLinkState', REFERENCE_ENUM_CLASS, 'CospfshamlinkstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB', 'CiscoOspfMib.Cospfshamlinktable.Cospfshamlinkentry.CospfshamlinkstateEnum', 
                [], [], 
                '''                OSPF sham link states.
                ''',
                'cospfshamlinkstate',
                'CISCO-OSPF-MIB', False),
            ],
            'CISCO-OSPF-MIB',
            'cospfShamLinkEntry',
            _yang_ns._namespaces['CISCO-OSPF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB'
        ),
    },
    'CiscoOspfMib.Cospfshamlinktable' : {
        'meta_info' : _MetaInfoClass('CiscoOspfMib.Cospfshamlinktable',
            False, 
            [
            _MetaInfoClassMember('cospfShamLinkEntry', REFERENCE_LIST, 'Cospfshamlinkentry' , 'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB', 'CiscoOspfMib.Cospfshamlinktable.Cospfshamlinkentry', 
                [], [], 
                '''                Information about a single sham link
                ''',
                'cospfshamlinkentry',
                'CISCO-OSPF-MIB', False),
            ],
            'CISCO-OSPF-MIB',
            'cospfShamLinkTable',
            _yang_ns._namespaces['CISCO-OSPF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB'
        ),
    },
    'CiscoOspfMib.Cospflocallsdbtable.Cospflocallsdbentry.CospflocallsdbtypeEnum' : _MetaInfoEnum('CospflocallsdbtypeEnum', 'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB',
        {
            'localOpaqueLink':'localOpaqueLink',
        }, 'CISCO-OSPF-MIB', _yang_ns._namespaces['CISCO-OSPF-MIB']),
    'CiscoOspfMib.Cospflocallsdbtable.Cospflocallsdbentry' : {
        'meta_info' : _MetaInfoClass('CiscoOspfMib.Cospflocallsdbtable.Cospflocallsdbentry',
            False, 
            [
            _MetaInfoClassMember('cospfLocalLsdbIpAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP Address of the interface from
                which the LSA was received if the interface is
                numbered.
                ''',
                'cospflocallsdbipaddress',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('cospfLocalLsdbAddressLessIf', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The Interface Index of the interface from
                which the LSA was received if the interface is
                unnumbered.
                ''',
                'cospflocallsdbaddresslessif',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('cospfLocalLsdbType', REFERENCE_ENUM_CLASS, 'CospflocallsdbtypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB', 'CiscoOspfMib.Cospflocallsdbtable.Cospflocallsdbentry.CospflocallsdbtypeEnum', 
                [], [], 
                '''                The type of the link state advertisement.
                Each link state type has a separate advertisement format.
                ''',
                'cospflocallsdbtype',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('cospfLocalLsdbLsid', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The Link State ID is an LS Type Specific field
                containing a 32 bit identifier in IP address format;
                it identifies the piece of the routing domain
                that is being described by the advertisement.
                ''',
                'cospflocallsdblsid',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('cospfLocalLsdbRouterId', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The 32 bit number that uniquely identifies the
                originating router in the Autonomous System.
                ''',
                'cospflocallsdbrouterid',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('cospfLocalLsdbAdvertisement', ATTRIBUTE, 'str' , None, None, 
                [(1, 65535)], [], 
                '''                The entire Link State Advertisement, including
                its header.
                ''',
                'cospflocallsdbadvertisement',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfLocalLsdbAge', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                This field is the age of the link state advertisement 
                in seconds.
                ''',
                'cospflocallsdbage',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfLocalLsdbChecksum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This field is the checksum of the complete
                contents of the advertisement, excepting the
                age field. The age field is excepted so that
                an advertisement's age can be incremented
                without updating the checksum. The checksum
                used is the same that is used for ISO connectionless
                datagrams; it is commonly referred  to
                as the Fletcher checksum.
                ''',
                'cospflocallsdbchecksum',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfLocalLsdbSequence', ATTRIBUTE, 'int' , None, None, 
                [('-2147483647', '2147483647')], [], 
                '''                The sequence number field is a signed 32-bit
                integer. It is used to detect old and duplicate link
                state advertisements. The space of
                sequence numbers is linearly ordered. The
                larger the sequence number the more recent the
                advertisement.
                ''',
                'cospflocallsdbsequence',
                'CISCO-OSPF-MIB', False),
            ],
            'CISCO-OSPF-MIB',
            'cospfLocalLsdbEntry',
            _yang_ns._namespaces['CISCO-OSPF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB'
        ),
    },
    'CiscoOspfMib.Cospflocallsdbtable' : {
        'meta_info' : _MetaInfoClass('CiscoOspfMib.Cospflocallsdbtable',
            False, 
            [
            _MetaInfoClassMember('cospfLocalLsdbEntry', REFERENCE_LIST, 'Cospflocallsdbentry' , 'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB', 'CiscoOspfMib.Cospflocallsdbtable.Cospflocallsdbentry', 
                [], [], 
                '''                A single Link State Advertisement.
                ''',
                'cospflocallsdbentry',
                'CISCO-OSPF-MIB', False),
            ],
            'CISCO-OSPF-MIB',
            'cospfLocalLsdbTable',
            _yang_ns._namespaces['CISCO-OSPF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB'
        ),
    },
    'CiscoOspfMib.Cospfvirtlocallsdbtable.Cospfvirtlocallsdbentry.CospfvirtlocallsdbtypeEnum' : _MetaInfoEnum('CospfvirtlocallsdbtypeEnum', 'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB',
        {
            'localOpaqueLink':'localOpaqueLink',
        }, 'CISCO-OSPF-MIB', _yang_ns._namespaces['CISCO-OSPF-MIB']),
    'CiscoOspfMib.Cospfvirtlocallsdbtable.Cospfvirtlocallsdbentry' : {
        'meta_info' : _MetaInfoClass('CiscoOspfMib.Cospfvirtlocallsdbtable.Cospfvirtlocallsdbentry',
            False, 
            [
            _MetaInfoClassMember('cospfVirtLocalLsdbTransitArea', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The Transit Area that the Virtual Link
                traverses. By definition, this is not 0.0.0.0
                ''',
                'cospfvirtlocallsdbtransitarea',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('cospfVirtLocalLsdbNeighbor', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The Router ID of the Virtual Neighbor.
                ''',
                'cospfvirtlocallsdbneighbor',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('cospfVirtLocalLsdbType', REFERENCE_ENUM_CLASS, 'CospfvirtlocallsdbtypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB', 'CiscoOspfMib.Cospfvirtlocallsdbtable.Cospfvirtlocallsdbentry.CospfvirtlocallsdbtypeEnum', 
                [], [], 
                '''                The type of the link state advertisement.
                Each  link state type has a separate advertisement format.
                ''',
                'cospfvirtlocallsdbtype',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('cospfVirtLocalLsdbLsid', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The Link State ID is an LS Type Specific field
                containing a 32 bit identifier in IP address format;
                it identifies the piece of the routing domain
                that is being described by the advertisement.
                ''',
                'cospfvirtlocallsdblsid',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('cospfVirtLocalLsdbRouterId', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The 32 bit number that uniquely identifies the
                originating router in the Autonomous System.
                ''',
                'cospfvirtlocallsdbrouterid',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('cospfVirtLocalLsdbAdvertisement', ATTRIBUTE, 'str' , None, None, 
                [(1, 65535)], [], 
                '''                The entire Link State Advertisement, including
                its header.
                ''',
                'cospfvirtlocallsdbadvertisement',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfVirtLocalLsdbAge', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                This field is the age of the link state advertisement
                in seconds.
                ''',
                'cospfvirtlocallsdbage',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfVirtLocalLsdbChecksum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This field is the checksum of the complete
                contents of the advertisement, excepting the
                age field. The age field is excepted so that
                an advertisement's age can be incremented
                without updating the checksum. The checksum
                used is the same that is used for ISO connectionless
                datagrams; it is commonly referred  to
                as the Fletcher checksum.
                ''',
                'cospfvirtlocallsdbchecksum',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfVirtLocalLsdbSequence', ATTRIBUTE, 'int' , None, None, 
                [('-2147483647', '2147483647')], [], 
                '''                The sequence number field is a  signed  32-bit
                integer. It is used to detect old and duplicate
                link state advertisements. The space of
                sequence numbers is linearly ordered. The
                larger the sequence number the more recent the
                advertisement.
                ''',
                'cospfvirtlocallsdbsequence',
                'CISCO-OSPF-MIB', False),
            ],
            'CISCO-OSPF-MIB',
            'cospfVirtLocalLsdbEntry',
            _yang_ns._namespaces['CISCO-OSPF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB'
        ),
    },
    'CiscoOspfMib.Cospfvirtlocallsdbtable' : {
        'meta_info' : _MetaInfoClass('CiscoOspfMib.Cospfvirtlocallsdbtable',
            False, 
            [
            _MetaInfoClassMember('cospfVirtLocalLsdbEntry', REFERENCE_LIST, 'Cospfvirtlocallsdbentry' , 'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB', 'CiscoOspfMib.Cospfvirtlocallsdbtable.Cospfvirtlocallsdbentry', 
                [], [], 
                '''                A single Link State Advertisement.
                ''',
                'cospfvirtlocallsdbentry',
                'CISCO-OSPF-MIB', False),
            ],
            'CISCO-OSPF-MIB',
            'cospfVirtLocalLsdbTable',
            _yang_ns._namespaces['CISCO-OSPF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB'
        ),
    },
    'CiscoOspfMib.Cospfshamlinknbrtable.Cospfshamlinknbrentry.CospfshamlinknbrstateEnum' : _MetaInfoEnum('CospfshamlinknbrstateEnum', 'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB',
        {
            'down':'down',
            'attempt':'attempt',
            'init':'init',
            'twoWay':'twoWay',
            'exchangeStart':'exchangeStart',
            'exchange':'exchange',
            'loading':'loading',
            'full':'full',
        }, 'CISCO-OSPF-MIB', _yang_ns._namespaces['CISCO-OSPF-MIB']),
    'CiscoOspfMib.Cospfshamlinknbrtable.Cospfshamlinknbrentry' : {
        'meta_info' : _MetaInfoClass('CiscoOspfMib.Cospfshamlinknbrtable.Cospfshamlinknbrentry',
            False, 
            [
            _MetaInfoClassMember('cospfShamLinksLocalIpAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                ''',
                'cospfshamlinkslocalipaddrtype',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('cospfShamLinksLocalIpAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                ''',
                'cospfshamlinkslocalipaddr',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('cospfShamLinkNbrArea', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The area to which the sham link is part of.
                ''',
                'cospfshamlinknbrarea',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('cospfShamLinkNbrIpAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The type of internet address of this sham link neighbor's
                IP address.
                ''',
                'cospfshamlinknbripaddrtype',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('cospfShamLinkNbrIpAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The IP address this sham link neighbor is using.
                ''',
                'cospfshamlinknbripaddr',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('cospfShamLinkNbrEvents', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of  times  this sham link has changed
                state or an error has occurred.
                ''',
                'cospfshamlinknbrevents',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfShamLinkNbrHelloSuppressed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether Hellos are being  suppressed
                to the neighbor.
                ''',
                'cospfshamlinknbrhellosuppressed',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfShamLinkNbrLsRetransQLen', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The  current  length  of  the   retransmission
                queue. The retransmission queue is maintained for
                LSAs that have been flooded but not acknowledged
                on this adjacency.
                ''',
                'cospfshamlinknbrlsretransqlen',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfShamLinkNbrOptions', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                A Bit Mask corresponding to the neighbor's options
                field.
                
                Bit 1, if set, indicates that the  system  will
                operate  on  Type of Service metrics other than
                TOS 0.  If zero, the neighbor will  ignore  all
                metrics except the TOS 0 metric.
                
                Bit 2, if set, indicates  that  the  system  is
                Network  Multicast  capable; ie, that it implements 
                OSPF Multicast Routing.
                ''',
                'cospfshamlinknbroptions',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfShamLinkNbrRtrId', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                A 32-bit integer uniquely identifying the neighboring
                router.
                ''',
                'cospfshamlinknbrrtrid',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfShamLinkNbrState', REFERENCE_ENUM_CLASS, 'CospfshamlinknbrstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB', 'CiscoOspfMib.Cospfshamlinknbrtable.Cospfshamlinknbrentry.CospfshamlinknbrstateEnum', 
                [], [], 
                '''                The state of this sham link neighbor relation-
                ship.
                ''',
                'cospfshamlinknbrstate',
                'CISCO-OSPF-MIB', False),
            ],
            'CISCO-OSPF-MIB',
            'cospfShamLinkNbrEntry',
            _yang_ns._namespaces['CISCO-OSPF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB'
        ),
    },
    'CiscoOspfMib.Cospfshamlinknbrtable' : {
        'meta_info' : _MetaInfoClass('CiscoOspfMib.Cospfshamlinknbrtable',
            False, 
            [
            _MetaInfoClassMember('cospfShamLinkNbrEntry', REFERENCE_LIST, 'Cospfshamlinknbrentry' , 'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB', 'CiscoOspfMib.Cospfshamlinknbrtable.Cospfshamlinknbrentry', 
                [], [], 
                '''                Sham link neighbor information.
                ''',
                'cospfshamlinknbrentry',
                'CISCO-OSPF-MIB', False),
            ],
            'CISCO-OSPF-MIB',
            'cospfShamLinkNbrTable',
            _yang_ns._namespaces['CISCO-OSPF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB'
        ),
    },
    'CiscoOspfMib.Cospfshamlinkstable.Cospfshamlinksentry.CospfshamlinksstateEnum' : _MetaInfoEnum('CospfshamlinksstateEnum', 'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB',
        {
            'down':'down',
            'pointToPoint':'pointToPoint',
        }, 'CISCO-OSPF-MIB', _yang_ns._namespaces['CISCO-OSPF-MIB']),
    'CiscoOspfMib.Cospfshamlinkstable.Cospfshamlinksentry' : {
        'meta_info' : _MetaInfoClass('CiscoOspfMib.Cospfshamlinkstable.Cospfshamlinksentry',
            False, 
            [
            _MetaInfoClassMember('cospfShamLinksAreaId', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The area that this sham link is part of.
                ''',
                'cospfshamlinksareaid',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('cospfShamLinksLocalIpAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The type of internet address of this sham link's local IP
                address.
                ''',
                'cospfshamlinkslocalipaddrtype',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('cospfShamLinksLocalIpAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The Local IP address of the sham link.
                ''',
                'cospfshamlinkslocalipaddr',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('cospfShamLinksRemoteIpAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The type of internet address of this sham link's remote IP
                address.
                ''',
                'cospfshamlinksremoteipaddrtype',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('cospfShamLinksRemoteIpAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The IP address of the other end router of the sham link.
                ''',
                'cospfshamlinksremoteipaddr',
                'CISCO-OSPF-MIB', True),
            _MetaInfoClassMember('cospfShamLinksEvents', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of state changes or error events on
                this sham link
                ''',
                'cospfshamlinksevents',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfShamLinksHelloInterval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The length of time, in  seconds,  between  the
                Hello  packets that the router sends on the sham
                link.
                ''',
                'cospfshamlinkshellointerval',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfShamLinksMetric', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The Metric to be advertised.
                ''',
                'cospfshamlinksmetric',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfShamLinksRetransInterval', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                The number of seconds between  link-state  advertisement
                retransmissions, for adjacencies belonging to this link.
                This value is also used when retransmitting database 
                description and link-state request packets. This value
                should be well over the expected round trip time.
                ''',
                'cospfshamlinksretransinterval',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfShamLinksRtrDeadInterval', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The number of seconds that  a  router's  Hello
                packets  have  not been seen before it's neighbors
                declare the router down.  This  should  be
                some  multiple  of  the  Hello  interval.
                ''',
                'cospfshamlinksrtrdeadinterval',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfShamLinksState', REFERENCE_ENUM_CLASS, 'CospfshamlinksstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB', 'CiscoOspfMib.Cospfshamlinkstable.Cospfshamlinksentry.CospfshamlinksstateEnum', 
                [], [], 
                '''                OSPF sham link states.
                ''',
                'cospfshamlinksstate',
                'CISCO-OSPF-MIB', False),
            ],
            'CISCO-OSPF-MIB',
            'cospfShamLinksEntry',
            _yang_ns._namespaces['CISCO-OSPF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB'
        ),
    },
    'CiscoOspfMib.Cospfshamlinkstable' : {
        'meta_info' : _MetaInfoClass('CiscoOspfMib.Cospfshamlinkstable',
            False, 
            [
            _MetaInfoClassMember('cospfShamLinksEntry', REFERENCE_LIST, 'Cospfshamlinksentry' , 'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB', 'CiscoOspfMib.Cospfshamlinkstable.Cospfshamlinksentry', 
                [], [], 
                '''                Information about a single sham link.
                ''',
                'cospfshamlinksentry',
                'CISCO-OSPF-MIB', False),
            ],
            'CISCO-OSPF-MIB',
            'cospfShamLinksTable',
            _yang_ns._namespaces['CISCO-OSPF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB'
        ),
    },
    'CiscoOspfMib' : {
        'meta_info' : _MetaInfoClass('CiscoOspfMib',
            False, 
            [
            _MetaInfoClassMember('cospfGeneralGroup', REFERENCE_CLASS, 'Cospfgeneralgroup' , 'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB', 'CiscoOspfMib.Cospfgeneralgroup', 
                [], [], 
                '''                ''',
                'cospfgeneralgroup',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfLocalLsdbTable', REFERENCE_CLASS, 'Cospflocallsdbtable' , 'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB', 'CiscoOspfMib.Cospflocallsdbtable', 
                [], [], 
                '''                The OSPF Process's Link-Local Link State Database
                for non-virtual links.
                ''',
                'cospflocallsdbtable',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfLsdbTable', REFERENCE_CLASS, 'Cospflsdbtable' , 'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB', 'CiscoOspfMib.Cospflsdbtable', 
                [], [], 
                '''                The OSPF Process's Link State Database. This 
                table is meant for Opaque LSA's
                ''',
                'cospflsdbtable',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfShamLinkNbrTable', REFERENCE_CLASS, 'Cospfshamlinknbrtable' , 'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB', 'CiscoOspfMib.Cospfshamlinknbrtable', 
                [], [], 
                '''                A table of sham link neighbor information.
                ''',
                'cospfshamlinknbrtable',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfShamLinksTable', REFERENCE_CLASS, 'Cospfshamlinkstable' , 'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB', 'CiscoOspfMib.Cospfshamlinkstable', 
                [], [], 
                '''                Information about this router's sham links.
                ''',
                'cospfshamlinkstable',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfShamLinkTable', REFERENCE_CLASS, 'Cospfshamlinktable' , 'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB', 'CiscoOspfMib.Cospfshamlinktable', 
                [], [], 
                '''                Information about this router's sham links
                ''',
                'cospfshamlinktable',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfVirtLocalLsdbTable', REFERENCE_CLASS, 'Cospfvirtlocallsdbtable' , 'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB', 'CiscoOspfMib.Cospfvirtlocallsdbtable', 
                [], [], 
                '''                The OSPF Process's Link-Local Link State Database
                for virtual links.
                ''',
                'cospfvirtlocallsdbtable',
                'CISCO-OSPF-MIB', False),
            ],
            'CISCO-OSPF-MIB',
            'CISCO-OSPF-MIB',
            _yang_ns._namespaces['CISCO-OSPF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_OSPF_MIB'
        ),
    },
}
_meta_table['CiscoOspfMib.Cospflsdbtable.Cospflsdbentry']['meta_info'].parent =_meta_table['CiscoOspfMib.Cospflsdbtable']['meta_info']
_meta_table['CiscoOspfMib.Cospfshamlinktable.Cospfshamlinkentry']['meta_info'].parent =_meta_table['CiscoOspfMib.Cospfshamlinktable']['meta_info']
_meta_table['CiscoOspfMib.Cospflocallsdbtable.Cospflocallsdbentry']['meta_info'].parent =_meta_table['CiscoOspfMib.Cospflocallsdbtable']['meta_info']
_meta_table['CiscoOspfMib.Cospfvirtlocallsdbtable.Cospfvirtlocallsdbentry']['meta_info'].parent =_meta_table['CiscoOspfMib.Cospfvirtlocallsdbtable']['meta_info']
_meta_table['CiscoOspfMib.Cospfshamlinknbrtable.Cospfshamlinknbrentry']['meta_info'].parent =_meta_table['CiscoOspfMib.Cospfshamlinknbrtable']['meta_info']
_meta_table['CiscoOspfMib.Cospfshamlinkstable.Cospfshamlinksentry']['meta_info'].parent =_meta_table['CiscoOspfMib.Cospfshamlinkstable']['meta_info']
_meta_table['CiscoOspfMib.Cospfgeneralgroup']['meta_info'].parent =_meta_table['CiscoOspfMib']['meta_info']
_meta_table['CiscoOspfMib.Cospflsdbtable']['meta_info'].parent =_meta_table['CiscoOspfMib']['meta_info']
_meta_table['CiscoOspfMib.Cospfshamlinktable']['meta_info'].parent =_meta_table['CiscoOspfMib']['meta_info']
_meta_table['CiscoOspfMib.Cospflocallsdbtable']['meta_info'].parent =_meta_table['CiscoOspfMib']['meta_info']
_meta_table['CiscoOspfMib.Cospfvirtlocallsdbtable']['meta_info'].parent =_meta_table['CiscoOspfMib']['meta_info']
_meta_table['CiscoOspfMib.Cospfshamlinknbrtable']['meta_info'].parent =_meta_table['CiscoOspfMib']['meta_info']
_meta_table['CiscoOspfMib.Cospfshamlinkstable']['meta_info'].parent =_meta_table['CiscoOspfMib']['meta_info']

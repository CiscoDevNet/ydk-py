


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Attachment' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Attachment',
            False, 
            [
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'SpanTrafficDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg', 'SpanTrafficDirectionEnum', 
                [], [], 
                '''                Specify the direction of traffic to replicate
                (optional)
                ''',
                'direction',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('port-level-enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable port level traffic mirroring
                ''',
                'port_level_enable',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 79)], [], 
                '''                Session Name
                ''',
                'session_name',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg',
            'attachment',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession',
            False, 
            [
            _MetaInfoClassMember('session-class', REFERENCE_ENUM_CLASS, 'SpanSessionClassEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes', 'SpanSessionClassEnum', 
                [], [], 
                '''                Session Class
                ''',
                'session_class',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', True),
            _MetaInfoClassMember('acl', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ACL matching for traffic mirroring
                ''',
                'acl',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('attachment', REFERENCE_CLASS, 'Attachment' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Attachment', 
                [], [], 
                '''                Attach the interface to a Monitor Session
                ''',
                'attachment',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('mirror-first', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Mirror a specified number of bytes from start of
                packet
                ''',
                'mirror_first',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('mirror-interval', REFERENCE_ENUM_CLASS, 'SpanMirrorIntervalEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg', 'SpanMirrorIntervalEnum', 
                [], [], 
                '''                Specify the mirror interval
                ''',
                'mirror_interval',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg',
            'span-monitor-session',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.SpanMonitorSessions' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.SpanMonitorSessions',
            False, 
            [
            _MetaInfoClassMember('span-monitor-session', REFERENCE_LIST, 'SpanMonitorSession' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession', 
                [], [], 
                '''                Configuration for a particular class of Monitor
                Session
                ''',
                'span_monitor_session',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg',
            'span-monitor-sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Outbound' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Outbound',
            False, 
            [
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('hardware-count', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'hardware_count',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                IPv4 Packet Filter Name to be applied to
                Outbound packets.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'outbound',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Inbound' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Inbound',
            False, 
            [
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('hardware-count', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'hardware_count',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                IPv4 Packet Filter Name to be applied to
                Inbound packets NOTE: This parameter is
                mandatory if 'CommonACLName' is not specified.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'inbound',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter',
            False, 
            [
            _MetaInfoClassMember('inbound', REFERENCE_CLASS, 'Inbound' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Inbound', 
                [], [], 
                '''                IPv4 Packet filter to be applied to inbound
                packets
                ''',
                'inbound',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('outbound', REFERENCE_CLASS, 'Outbound' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Outbound', 
                [], [], 
                '''                IPv4 Packet filter to be applied to outbound
                packets
                ''',
                'outbound',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'ipv4-packet-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Inbound' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Inbound',
            False, 
            [
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                IPv6 Packet Filter Name to be applied to
                Inbound  NOTE: This parameter is mandatory if
                'CommonACLName' is not specified.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'inbound',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Outbound' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Outbound',
            False, 
            [
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                IPv6 Packet Filter Name to be applied to
                Outbound packets.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'outbound',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter',
            False, 
            [
            _MetaInfoClassMember('inbound', REFERENCE_CLASS, 'Inbound' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Inbound', 
                [], [], 
                '''                IPv6 Packet filter to be applied to inbound
                packets
                ''',
                'inbound',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('outbound', REFERENCE_CLASS, 'Outbound' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Outbound', 
                [], [], 
                '''                IPv6 Packet filter to be applied to outbound
                packets
                ''',
                'outbound',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'ipv6-packet-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf.ExplicitTracking' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf.ExplicitTracking',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access list specifying tracking group range
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable, when value is TRUE or
                FALSE respectively
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg',
            'explicit-tracking',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf',
            False, 
            [
            _MetaInfoClassMember('access-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access list specifying access-list group range
                ''',
                'access_group',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False),
            _MetaInfoClassMember('explicit-tracking', REFERENCE_CLASS, 'ExplicitTracking' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf.ExplicitTracking', 
                [], [], 
                '''                IGMPv3 explicit host tracking
                ''',
                'explicit_tracking',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False),
            _MetaInfoClassMember('max-groups', ATTRIBUTE, 'int' , None, None, 
                [('1', '40000')], [], 
                '''                IGMP Max Groups
                ''',
                'max_groups',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False),
            _MetaInfoClassMember('multicast', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Configure Multicast mode variable
                ''',
                'multicast',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False),
            _MetaInfoClassMember('query-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                Query interval in seconds
                ''',
                'query_interval',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False),
            _MetaInfoClassMember('query-max-response-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '12')], [], 
                '''                Query response value in seconds
                ''',
                'query_max_response_time',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False),
            _MetaInfoClassMember('robustness', ATTRIBUTE, 'int' , None, None, 
                [('2', '10')], [], 
                '''                Configure IGMP Robustness variable
                ''',
                'robustness',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                IGMP Version
                ''',
                'version',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg',
            'default-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Igmp' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Igmp',
            False, 
            [
            _MetaInfoClassMember('default-vrf', REFERENCE_CLASS, 'DefaultVrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf', 
                [], [], 
                '''                Default VRF
                ''',
                'default_vrf',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg',
            'igmp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv4Network' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv4Network',
            False, 
            [
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('68', '65535')], [], 
                '''                The IP Maximum Transmission Unit
                ''',
                'mtu',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False),
            _MetaInfoClassMember('rpf', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if enabled, FALSE if disabled
                ''',
                'rpf',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False),
            _MetaInfoClassMember('unnumbered', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Enable IP processing without an explicit
                address
                ''',
                'unnumbered',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if enabled, FALSE if disabled
                ''',
                'unreachables',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ma-subscriber-cfg',
            'ipv4-network',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The flag to enable auto ipv6 interface
                configuration
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-subscriber-cfg',
            'auto-configuration',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses',
            False, 
            [
            _MetaInfoClassMember('auto-configuration', REFERENCE_CLASS, 'AutoConfiguration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration', 
                [], [], 
                '''                Auto IPv6 Interface Configuration
                ''',
                'auto_configuration',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-subscriber-cfg',
            'addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv6Network' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv6Network',
            False, 
            [
            _MetaInfoClassMember('addresses', REFERENCE_CLASS, 'Addresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses', 
                [], [], 
                '''                Set the IPv6 address of an interface
                ''',
                'addresses',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('1280', '65535')], [], 
                '''                MTU Setting of Interface
                ''',
                'mtu',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Override Sending of ICMP Unreachable Messages
                ''',
                'unreachables',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            _MetaInfoClassMember('verify', REFERENCE_ENUM_CLASS, 'Ipv6ReachableViaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_subscriber_cfg', 'Ipv6ReachableViaEnum', 
                [], [], 
                '''                IPv6 Verify Unicast Souce Reachable
                ''',
                'verify',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-subscriber-cfg',
            'ipv6-network',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.FramedPrefix' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.FramedPrefix',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IPV6 framed prefix address
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                IPv6 framed prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'framed-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.DuplicateAddressDetection' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.DuplicateAddressDetection',
            False, 
            [
            _MetaInfoClassMember('attempts', ATTRIBUTE, 'int' , None, None, 
                [('0', '600')], [], 
                '''                Set IPv6 duplicate address detection transmits
                ''',
                'attempts',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'duplicate-address-detection',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInitial' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInitial',
            False, 
            [
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                Initial RA count
                ''',
                'count',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('4', '1800')], [], 
                '''                Initial RA interval in seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'ra-initial',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Ipv6Neighbor' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Ipv6Neighbor',
            False, 
            [
            _MetaInfoClassMember('duplicate-address-detection', REFERENCE_CLASS, 'DuplicateAddressDetection' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.DuplicateAddressDetection', 
                [], [], 
                '''                Duplicate Address Detection (DAD)
                ''',
                'duplicate_address_detection',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('framed-prefix', REFERENCE_CLASS, 'FramedPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.FramedPrefix', 
                [], [], 
                '''                Set the IPv6 framed ipv6 prefix for a
                subscriber interface 
                ''',
                'framed_prefix',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('framed-prefix-pool', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set the IPv6 framed ipv6 prefix pool for a
                subscriber interface 
                ''',
                'framed_prefix_pool',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('managed-config', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Host to use stateful protocol for address
                configuration
                ''',
                'managed_config',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ns-interval', ATTRIBUTE, 'int' , None, None, 
                [('1000', '3600000')], [], 
                '''                Set advertised NS retransmission interval in
                milliseconds
                ''',
                'ns_interval',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('nud-enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                NUD enable
                ''',
                'nud_enable',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('other-config', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Host to use stateful protocol for non-address
                configuration
                ''',
                'other_config',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-hop-limit', REFERENCE_ENUM_CLASS, 'Ipv6NdHopLimitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_subscriber_cfg', 'Ipv6NdHopLimitEnum', 
                [], [], 
                '''                IPv6 ND RA HopLimit
                ''',
                'ra_hop_limit',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-initial', REFERENCE_CLASS, 'RaInitial' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInitial', 
                [], [], 
                '''                IPv6 ND RA Initial
                ''',
                'ra_initial',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '1800')], [], 
                '''                Set IPv6 Router Advertisement (RA) interval in
                seconds
                ''',
                'ra_interval',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '9000')], [], 
                '''                Set IPv6 Router Advertisement (RA) lifetime in
                seconds
                ''',
                'ra_lifetime',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-suppress', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable suppress IPv6 router advertisement
                ''',
                'ra_suppress',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-suppress-mtu', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RA suppress MTU flag
                ''',
                'ra_suppress_mtu',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-unicast', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable RA unicast Flag
                ''',
                'ra_unicast',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('reachable-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600000')], [], 
                '''                Set advertised reachability time in
                milliseconds
                ''',
                'reachable_time',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('router-preference', REFERENCE_ENUM_CLASS, 'Ipv6NdRouterPrefTemplateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_subscriber_cfg', 'Ipv6NdRouterPrefTemplateEnum', 
                [], [], 
                '''                RA Router Preference
                ''',
                'router_preference',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('start-ra-on-ipv6-enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Start RA on ipv6-enable config
                ''',
                'start_ra_on_ipv6_enable',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('suppress-cache-learning', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Suppress cache learning flag
                ''',
                'suppress_cache_learning',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'ipv6-neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Dhcpv6.DelegatedPrefix' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Dhcpv6.DelegatedPrefix',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                PD Prefix Length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg',
            'delegated-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Dhcpv6' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Dhcpv6',
            False, 
            [
            _MetaInfoClassMember('address-pool', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The pool to be used for Address assignment
                ''',
                'address_pool',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('class', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The class to be used for proxy/server profile
                ''',
                'class_',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('delegated-prefix', REFERENCE_CLASS, 'DelegatedPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Dhcpv6.DelegatedPrefix', 
                [], [], 
                '''                The prefix to be used for Prefix Delegation
                ''',
                'delegated_prefix',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('delegated-prefix-pool', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The pool to be used for Prefix Delegation
                ''',
                'delegated_prefix_pool',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('dns-ipv6address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Dns IPv6 Address
                ''',
                'dns_ipv6address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('stateful-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Stateful IPv6 Address
                ''',
                'stateful_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg',
            'dhcpv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicy' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicy',
            False, 
            [
            _MetaInfoClassMember('input', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ingress service policy
                ''',
                'input',
                'Cisco-IOS-XR-pbr-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-pbr-subscriber-cfg',
            'service-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Pbr' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Pbr',
            False, 
            [
            _MetaInfoClassMember('service-policy', REFERENCE_CLASS, 'ServicePolicy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicy', 
                [], [], 
                '''                PBR service policy configuration
                ''',
                'service_policy',
                'Cisco-IOS-XR-pbr-subscriber-cfg', False),
            _MetaInfoClassMember('service-policy-in', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Class for subscriber ingress policy
                ''',
                'service_policy_in',
                'Cisco-IOS-XR-pbr-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-pbr-subscriber-cfg',
            'pbr',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Input' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Input',
            False, 
            [
            _MetaInfoClassMember('account-stats', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE for account stats enabled for
                service-policy applied on dynamic template.
                Note: account stats not supported for
                subscriber type 'ppp' and 'ipsubscriber'.
                ''',
                'account_stats',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('merge', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE for merge enabled for service-policy
                applied on dynamic template.
                ''',
                'merge',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('merge-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Merge ID value
                ''',
                'merge_id',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of policy-map
                ''',
                'policy_name',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('spi-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the SPI
                ''',
                'spi_name',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-bng-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Output' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Output',
            False, 
            [
            _MetaInfoClassMember('account-stats', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE for account stats enabled for
                service-policy applied on dynamic template.
                Note: account stats not supported for
                subscriber type 'ppp' and 'ipsubscriber'.
                ''',
                'account_stats',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('merge', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE for merge enabled for service-policy
                applied on dynamic template.
                ''',
                'merge',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('merge-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Merge ID value
                ''',
                'merge_id',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of policy-map
                ''',
                'policy_name',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('spi-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the SPI
                ''',
                'spi_name',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-bng-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Input', 
                [], [], 
                '''                Subscriber ingress policy
                ''',
                'input',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Output', 
                [], [], 
                '''                Subscriber egress policy
                ''',
                'output',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'service-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-bng-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Qos.Account' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Qos.Account',
            False, 
            [
            _MetaInfoClassMember('aal', REFERENCE_ENUM_CLASS, 'Qosl2DataLinkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg', 'Qosl2DataLinkEnum', 
                [], [], 
                '''                ATM adaptation layer AAL
                ''',
                'aal',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('atm-cell-tax', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ATM cell tax to L2 overhead
                ''',
                'atm_cell_tax',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('encapsulation', REFERENCE_ENUM_CLASS, 'Qosl2EncapEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg', 'Qosl2EncapEnum', 
                [], [], 
                '''                Specify encapsulation type
                ''',
                'encapsulation',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('user-defined', ATTRIBUTE, 'int' , None, None, 
                [('-63', '63')], [], 
                '''                Numeric L2 overhead offset
                ''',
                'user_defined',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'account',
            _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-bng-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Qos.Output' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Qos.Output',
            False, 
            [
            _MetaInfoClassMember('minimum-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Minimum bandwidth value for the subscriber (in
                kbps)
                ''',
                'minimum_bandwidth',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-bng-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp.Qos' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp.Qos',
            False, 
            [
            _MetaInfoClassMember('account', REFERENCE_CLASS, 'Account' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Qos.Account', 
                [], [], 
                '''                QoS L2 overhead accounting
                ''',
                'account',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Qos.Output', 
                [], [], 
                '''                QoS to be applied in egress direction
                ''',
                'output',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('service-policy', REFERENCE_CLASS, 'ServicePolicy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy', 
                [], [], 
                '''                Service policy to be applied in ingress/egress
                direction
                ''',
                'service_policy',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'qos',
            _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-bng-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps.Ppp' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps.Ppp',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the template
                ''',
                'template_name',
                'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg', True),
            _MetaInfoClassMember('dhcpv6', REFERENCE_CLASS, 'Dhcpv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Dhcpv6', 
                [], [], 
                '''                Interface dhcpv6 configuration data
                ''',
                'dhcpv6',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('igmp', REFERENCE_CLASS, 'Igmp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Igmp', 
                [], [], 
                '''                IGMPconfiguration
                ''',
                'igmp',
                'Cisco-IOS-XR-ipv4-igmp-dyn-tmpl-cfg', False),
            _MetaInfoClassMember('ipv4-network', REFERENCE_CLASS, 'Ipv4Network' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv4Network', 
                [], [], 
                '''                Interface IPv4 Network configuration data
                ''',
                'ipv4_network',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False),
            _MetaInfoClassMember('ipv4-packet-filter', REFERENCE_CLASS, 'Ipv4PacketFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter', 
                [], [], 
                '''                IPv4 Packet Filtering configuration for the
                template
                ''',
                'ipv4_packet_filter',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('ipv6-neighbor', REFERENCE_CLASS, 'Ipv6Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv6Neighbor', 
                [], [], 
                '''                Interface IPv6 Network configuration data
                ''',
                'ipv6_neighbor',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ipv6-network', REFERENCE_CLASS, 'Ipv6Network' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv6Network', 
                [], [], 
                '''                Interface IPv6 Network configuration data
                ''',
                'ipv6_network',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            _MetaInfoClassMember('ipv6-packet-filter', REFERENCE_CLASS, 'Ipv6PacketFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter', 
                [], [], 
                '''                IPv6 Packet Filtering configuration for the
                interface
                ''',
                'ipv6_packet_filter',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('pbr', REFERENCE_CLASS, 'Pbr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Pbr', 
                [], [], 
                '''                Dynamic Template PBR configuration
                ''',
                'pbr',
                'Cisco-IOS-XR-pbr-subscriber-cfg', False),
            _MetaInfoClassMember('qos', REFERENCE_CLASS, 'Qos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.Qos', 
                [], [], 
                '''                QoS dynamically applied configuration template
                ''',
                'qos',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('span-monitor-sessions', REFERENCE_CLASS, 'SpanMonitorSessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp.SpanMonitorSessions', 
                [], [], 
                '''                Monitor Session container for this template
                ''',
                'span_monitor_sessions',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                Assign the interface to a VRF 
                ''',
                'vrf',
                'Cisco-IOS-XR-infra-rsi-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg',
            'ppp',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.Ppps' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.Ppps',
            False, 
            [
            _MetaInfoClassMember('ppp', REFERENCE_LIST, 'Ppp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps.Ppp', 
                [], [], 
                '''                A Template of the PPP Type
                ''',
                'ppp',
                'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg',
            'ppps',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Attachment' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Attachment',
            False, 
            [
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'SpanTrafficDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg', 'SpanTrafficDirectionEnum', 
                [], [], 
                '''                Specify the direction of traffic to replicate
                (optional)
                ''',
                'direction',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('port-level-enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable port level traffic mirroring
                ''',
                'port_level_enable',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 79)], [], 
                '''                Session Name
                ''',
                'session_name',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg',
            'attachment',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession',
            False, 
            [
            _MetaInfoClassMember('session-class', REFERENCE_ENUM_CLASS, 'SpanSessionClassEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes', 'SpanSessionClassEnum', 
                [], [], 
                '''                Session Class
                ''',
                'session_class',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', True),
            _MetaInfoClassMember('acl', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ACL matching for traffic mirroring
                ''',
                'acl',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('attachment', REFERENCE_CLASS, 'Attachment' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Attachment', 
                [], [], 
                '''                Attach the interface to a Monitor Session
                ''',
                'attachment',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('mirror-first', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Mirror a specified number of bytes from start of
                packet
                ''',
                'mirror_first',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('mirror-interval', REFERENCE_ENUM_CLASS, 'SpanMirrorIntervalEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg', 'SpanMirrorIntervalEnum', 
                [], [], 
                '''                Specify the mirror interval
                ''',
                'mirror_interval',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg',
            'span-monitor-session',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions',
            False, 
            [
            _MetaInfoClassMember('span-monitor-session', REFERENCE_LIST, 'SpanMonitorSession' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession', 
                [], [], 
                '''                Configuration for a particular class of Monitor
                Session
                ''',
                'span_monitor_session',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg',
            'span-monitor-sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Outbound' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Outbound',
            False, 
            [
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('hardware-count', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'hardware_count',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                IPv4 Packet Filter Name to be applied to
                Outbound packets.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'outbound',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Inbound' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Inbound',
            False, 
            [
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('hardware-count', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'hardware_count',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                IPv4 Packet Filter Name to be applied to
                Inbound packets NOTE: This parameter is
                mandatory if 'CommonACLName' is not specified.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'inbound',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter',
            False, 
            [
            _MetaInfoClassMember('inbound', REFERENCE_CLASS, 'Inbound' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Inbound', 
                [], [], 
                '''                IPv4 Packet filter to be applied to inbound
                packets
                ''',
                'inbound',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('outbound', REFERENCE_CLASS, 'Outbound' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Outbound', 
                [], [], 
                '''                IPv4 Packet filter to be applied to outbound
                packets
                ''',
                'outbound',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'ipv4-packet-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Inbound' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Inbound',
            False, 
            [
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                IPv6 Packet Filter Name to be applied to
                Inbound  NOTE: This parameter is mandatory if
                'CommonACLName' is not specified.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'inbound',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Outbound' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Outbound',
            False, 
            [
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                IPv6 Packet Filter Name to be applied to
                Outbound packets.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'outbound',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter',
            False, 
            [
            _MetaInfoClassMember('inbound', REFERENCE_CLASS, 'Inbound' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Inbound', 
                [], [], 
                '''                IPv6 Packet filter to be applied to inbound
                packets
                ''',
                'inbound',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('outbound', REFERENCE_CLASS, 'Outbound' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Outbound', 
                [], [], 
                '''                IPv6 Packet filter to be applied to outbound
                packets
                ''',
                'outbound',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'ipv6-packet-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4Network' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4Network',
            False, 
            [
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('68', '65535')], [], 
                '''                The IP Maximum Transmission Unit
                ''',
                'mtu',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False),
            _MetaInfoClassMember('rpf', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if enabled, FALSE if disabled
                ''',
                'rpf',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False),
            _MetaInfoClassMember('unnumbered', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Enable IP processing without an explicit
                address
                ''',
                'unnumbered',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if enabled, FALSE if disabled
                ''',
                'unreachables',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ma-subscriber-cfg',
            'ipv4-network',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The flag to enable auto ipv6 interface
                configuration
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-subscriber-cfg',
            'auto-configuration',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses',
            False, 
            [
            _MetaInfoClassMember('auto-configuration', REFERENCE_CLASS, 'AutoConfiguration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration', 
                [], [], 
                '''                Auto IPv6 Interface Configuration
                ''',
                'auto_configuration',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-subscriber-cfg',
            'addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network',
            False, 
            [
            _MetaInfoClassMember('addresses', REFERENCE_CLASS, 'Addresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses', 
                [], [], 
                '''                Set the IPv6 address of an interface
                ''',
                'addresses',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('1280', '65535')], [], 
                '''                MTU Setting of Interface
                ''',
                'mtu',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Override Sending of ICMP Unreachable Messages
                ''',
                'unreachables',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            _MetaInfoClassMember('verify', REFERENCE_ENUM_CLASS, 'Ipv6ReachableViaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_subscriber_cfg', 'Ipv6ReachableViaEnum', 
                [], [], 
                '''                IPv6 Verify Unicast Souce Reachable
                ''',
                'verify',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-subscriber-cfg',
            'ipv6-network',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.FramedPrefix' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.FramedPrefix',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IPV6 framed prefix address
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                IPv6 framed prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'framed-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.DuplicateAddressDetection' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.DuplicateAddressDetection',
            False, 
            [
            _MetaInfoClassMember('attempts', ATTRIBUTE, 'int' , None, None, 
                [('0', '600')], [], 
                '''                Set IPv6 duplicate address detection transmits
                ''',
                'attempts',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'duplicate-address-detection',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInitial' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInitial',
            False, 
            [
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                Initial RA count
                ''',
                'count',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('4', '1800')], [], 
                '''                Initial RA interval in seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'ra-initial',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor',
            False, 
            [
            _MetaInfoClassMember('duplicate-address-detection', REFERENCE_CLASS, 'DuplicateAddressDetection' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.DuplicateAddressDetection', 
                [], [], 
                '''                Duplicate Address Detection (DAD)
                ''',
                'duplicate_address_detection',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('framed-prefix', REFERENCE_CLASS, 'FramedPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.FramedPrefix', 
                [], [], 
                '''                Set the IPv6 framed ipv6 prefix for a
                subscriber interface 
                ''',
                'framed_prefix',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('framed-prefix-pool', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set the IPv6 framed ipv6 prefix pool for a
                subscriber interface 
                ''',
                'framed_prefix_pool',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('managed-config', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Host to use stateful protocol for address
                configuration
                ''',
                'managed_config',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ns-interval', ATTRIBUTE, 'int' , None, None, 
                [('1000', '3600000')], [], 
                '''                Set advertised NS retransmission interval in
                milliseconds
                ''',
                'ns_interval',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('nud-enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                NUD enable
                ''',
                'nud_enable',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('other-config', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Host to use stateful protocol for non-address
                configuration
                ''',
                'other_config',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-hop-limit', REFERENCE_ENUM_CLASS, 'Ipv6NdHopLimitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_subscriber_cfg', 'Ipv6NdHopLimitEnum', 
                [], [], 
                '''                IPv6 ND RA HopLimit
                ''',
                'ra_hop_limit',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-initial', REFERENCE_CLASS, 'RaInitial' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInitial', 
                [], [], 
                '''                IPv6 ND RA Initial
                ''',
                'ra_initial',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '1800')], [], 
                '''                Set IPv6 Router Advertisement (RA) interval in
                seconds
                ''',
                'ra_interval',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '9000')], [], 
                '''                Set IPv6 Router Advertisement (RA) lifetime in
                seconds
                ''',
                'ra_lifetime',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-suppress', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable suppress IPv6 router advertisement
                ''',
                'ra_suppress',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-suppress-mtu', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RA suppress MTU flag
                ''',
                'ra_suppress_mtu',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-unicast', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable RA unicast Flag
                ''',
                'ra_unicast',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('reachable-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600000')], [], 
                '''                Set advertised reachability time in
                milliseconds
                ''',
                'reachable_time',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('router-preference', REFERENCE_ENUM_CLASS, 'Ipv6NdRouterPrefTemplateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_subscriber_cfg', 'Ipv6NdRouterPrefTemplateEnum', 
                [], [], 
                '''                RA Router Preference
                ''',
                'router_preference',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('start-ra-on-ipv6-enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Start RA on ipv6-enable config
                ''',
                'start_ra_on_ipv6_enable',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('suppress-cache-learning', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Suppress cache learning flag
                ''',
                'suppress_cache_learning',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'ipv6-neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6.DelegatedPrefix' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6.DelegatedPrefix',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                PD Prefix Length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg',
            'delegated-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6',
            False, 
            [
            _MetaInfoClassMember('address-pool', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The pool to be used for Address assignment
                ''',
                'address_pool',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('class', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The class to be used for proxy/server profile
                ''',
                'class_',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('delegated-prefix', REFERENCE_CLASS, 'DelegatedPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6.DelegatedPrefix', 
                [], [], 
                '''                The prefix to be used for Prefix Delegation
                ''',
                'delegated_prefix',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('delegated-prefix-pool', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The pool to be used for Prefix Delegation
                ''',
                'delegated_prefix_pool',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('dns-ipv6address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Dns IPv6 Address
                ''',
                'dns_ipv6address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('stateful-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Stateful IPv6 Address
                ''',
                'stateful_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg',
            'dhcpv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicy' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicy',
            False, 
            [
            _MetaInfoClassMember('input', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ingress service policy
                ''',
                'input',
                'Cisco-IOS-XR-pbr-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-pbr-subscriber-cfg',
            'service-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Pbr' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Pbr',
            False, 
            [
            _MetaInfoClassMember('service-policy', REFERENCE_CLASS, 'ServicePolicy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicy', 
                [], [], 
                '''                PBR service policy configuration
                ''',
                'service_policy',
                'Cisco-IOS-XR-pbr-subscriber-cfg', False),
            _MetaInfoClassMember('service-policy-in', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Class for subscriber ingress policy
                ''',
                'service_policy_in',
                'Cisco-IOS-XR-pbr-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-pbr-subscriber-cfg',
            'pbr',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Input' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Input',
            False, 
            [
            _MetaInfoClassMember('account-stats', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE for account stats enabled for
                service-policy applied on dynamic template.
                Note: account stats not supported for
                subscriber type 'ppp' and 'ipsubscriber'.
                ''',
                'account_stats',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('merge', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE for merge enabled for service-policy
                applied on dynamic template.
                ''',
                'merge',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('merge-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Merge ID value
                ''',
                'merge_id',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of policy-map
                ''',
                'policy_name',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('spi-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the SPI
                ''',
                'spi_name',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-bng-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Output' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Output',
            False, 
            [
            _MetaInfoClassMember('account-stats', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE for account stats enabled for
                service-policy applied on dynamic template.
                Note: account stats not supported for
                subscriber type 'ppp' and 'ipsubscriber'.
                ''',
                'account_stats',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('merge', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE for merge enabled for service-policy
                applied on dynamic template.
                ''',
                'merge',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('merge-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Merge ID value
                ''',
                'merge_id',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of policy-map
                ''',
                'policy_name',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('spi-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the SPI
                ''',
                'spi_name',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-bng-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Input', 
                [], [], 
                '''                Subscriber ingress policy
                ''',
                'input',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Output', 
                [], [], 
                '''                Subscriber egress policy
                ''',
                'output',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'service-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-bng-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Account' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Account',
            False, 
            [
            _MetaInfoClassMember('aal', REFERENCE_ENUM_CLASS, 'Qosl2DataLinkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg', 'Qosl2DataLinkEnum', 
                [], [], 
                '''                ATM adaptation layer AAL
                ''',
                'aal',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('atm-cell-tax', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ATM cell tax to L2 overhead
                ''',
                'atm_cell_tax',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('encapsulation', REFERENCE_ENUM_CLASS, 'Qosl2EncapEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg', 'Qosl2EncapEnum', 
                [], [], 
                '''                Specify encapsulation type
                ''',
                'encapsulation',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('user-defined', ATTRIBUTE, 'int' , None, None, 
                [('-63', '63')], [], 
                '''                Numeric L2 overhead offset
                ''',
                'user_defined',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'account',
            _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-bng-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Output' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Output',
            False, 
            [
            _MetaInfoClassMember('minimum-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Minimum bandwidth value for the subscriber (in
                kbps)
                ''',
                'minimum_bandwidth',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-bng-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber.Qos' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber.Qos',
            False, 
            [
            _MetaInfoClassMember('account', REFERENCE_CLASS, 'Account' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Account', 
                [], [], 
                '''                QoS L2 overhead accounting
                ''',
                'account',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Output', 
                [], [], 
                '''                QoS to be applied in egress direction
                ''',
                'output',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('service-policy', REFERENCE_CLASS, 'ServicePolicy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy', 
                [], [], 
                '''                Service policy to be applied in ingress/egress
                direction
                ''',
                'service_policy',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'qos',
            _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-bng-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers.IpSubscriber' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers.IpSubscriber',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the template
                ''',
                'template_name',
                'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg', True),
            _MetaInfoClassMember('dhcpv6', REFERENCE_CLASS, 'Dhcpv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6', 
                [], [], 
                '''                Interface dhcpv6 configuration data
                ''',
                'dhcpv6',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-subscriber-cfg', False),
            _MetaInfoClassMember('ipv4-network', REFERENCE_CLASS, 'Ipv4Network' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4Network', 
                [], [], 
                '''                Interface IPv4 Network configuration data
                ''',
                'ipv4_network',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False),
            _MetaInfoClassMember('ipv4-packet-filter', REFERENCE_CLASS, 'Ipv4PacketFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter', 
                [], [], 
                '''                IPv4 Packet Filtering configuration for the
                template
                ''',
                'ipv4_packet_filter',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('ipv6-neighbor', REFERENCE_CLASS, 'Ipv6Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor', 
                [], [], 
                '''                Interface IPv6 Network configuration data
                ''',
                'ipv6_neighbor',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ipv6-network', REFERENCE_CLASS, 'Ipv6Network' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network', 
                [], [], 
                '''                Interface IPv6 Network configuration data
                ''',
                'ipv6_network',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            _MetaInfoClassMember('ipv6-packet-filter', REFERENCE_CLASS, 'Ipv6PacketFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter', 
                [], [], 
                '''                IPv6 Packet Filtering configuration for the
                interface
                ''',
                'ipv6_packet_filter',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('pbr', REFERENCE_CLASS, 'Pbr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Pbr', 
                [], [], 
                '''                Dynamic Template PBR configuration
                ''',
                'pbr',
                'Cisco-IOS-XR-pbr-subscriber-cfg', False),
            _MetaInfoClassMember('qos', REFERENCE_CLASS, 'Qos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.Qos', 
                [], [], 
                '''                QoS dynamically applied configuration template
                ''',
                'qos',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('span-monitor-sessions', REFERENCE_CLASS, 'SpanMonitorSessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions', 
                [], [], 
                '''                Monitor Session container for this template
                ''',
                'span_monitor_sessions',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                Assign the interface to a VRF 
                ''',
                'vrf',
                'Cisco-IOS-XR-infra-rsi-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg',
            'ip-subscriber',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.IpSubscribers' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.IpSubscribers',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber', REFERENCE_LIST, 'IpSubscriber' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers.IpSubscriber', 
                [], [], 
                '''                A IP Subscriber Type Template 
                ''',
                'ip_subscriber',
                'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg',
            'ip-subscribers',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Attachment' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Attachment',
            False, 
            [
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'SpanTrafficDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg', 'SpanTrafficDirectionEnum', 
                [], [], 
                '''                Specify the direction of traffic to replicate
                (optional)
                ''',
                'direction',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('port-level-enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable port level traffic mirroring
                ''',
                'port_level_enable',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 79)], [], 
                '''                Session Name
                ''',
                'session_name',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg',
            'attachment',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession',
            False, 
            [
            _MetaInfoClassMember('session-class', REFERENCE_ENUM_CLASS, 'SpanSessionClassEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes', 'SpanSessionClassEnum', 
                [], [], 
                '''                Session Class
                ''',
                'session_class',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', True),
            _MetaInfoClassMember('acl', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ACL matching for traffic mirroring
                ''',
                'acl',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('attachment', REFERENCE_CLASS, 'Attachment' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Attachment', 
                [], [], 
                '''                Attach the interface to a Monitor Session
                ''',
                'attachment',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('mirror-first', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Mirror a specified number of bytes from start of
                packet
                ''',
                'mirror_first',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('mirror-interval', REFERENCE_ENUM_CLASS, 'SpanMirrorIntervalEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg', 'SpanMirrorIntervalEnum', 
                [], [], 
                '''                Specify the mirror interval
                ''',
                'mirror_interval',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg',
            'span-monitor-session',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions',
            False, 
            [
            _MetaInfoClassMember('span-monitor-session', REFERENCE_LIST, 'SpanMonitorSession' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession', 
                [], [], 
                '''                Configuration for a particular class of Monitor
                Session
                ''',
                'span_monitor_session',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg',
            'span-monitor-sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Outbound' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Outbound',
            False, 
            [
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('hardware-count', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'hardware_count',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                IPv4 Packet Filter Name to be applied to
                Outbound packets.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'outbound',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Inbound' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Inbound',
            False, 
            [
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('hardware-count', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'hardware_count',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                IPv4 Packet Filter Name to be applied to
                Inbound packets NOTE: This parameter is
                mandatory if 'CommonACLName' is not specified.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'inbound',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter',
            False, 
            [
            _MetaInfoClassMember('inbound', REFERENCE_CLASS, 'Inbound' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Inbound', 
                [], [], 
                '''                IPv4 Packet filter to be applied to inbound
                packets
                ''',
                'inbound',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('outbound', REFERENCE_CLASS, 'Outbound' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Outbound', 
                [], [], 
                '''                IPv4 Packet filter to be applied to outbound
                packets
                ''',
                'outbound',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'ipv4-packet-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Inbound' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Inbound',
            False, 
            [
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                IPv6 Packet Filter Name to be applied to
                Inbound  NOTE: This parameter is mandatory if
                'CommonACLName' is not specified.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'inbound',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Outbound' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Outbound',
            False, 
            [
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                IPv6 Packet Filter Name to be applied to
                Outbound packets.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'outbound',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter',
            False, 
            [
            _MetaInfoClassMember('inbound', REFERENCE_CLASS, 'Inbound' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Inbound', 
                [], [], 
                '''                IPv6 Packet filter to be applied to inbound
                packets
                ''',
                'inbound',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('outbound', REFERENCE_CLASS, 'Outbound' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Outbound', 
                [], [], 
                '''                IPv6 Packet filter to be applied to outbound
                packets
                ''',
                'outbound',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-subscriber-cfg',
            'ipv6-packet-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv4Network' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv4Network',
            False, 
            [
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('68', '65535')], [], 
                '''                The IP Maximum Transmission Unit
                ''',
                'mtu',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False),
            _MetaInfoClassMember('rpf', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if enabled, FALSE if disabled
                ''',
                'rpf',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False),
            _MetaInfoClassMember('unnumbered', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Enable IP processing without an explicit
                address
                ''',
                'unnumbered',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if enabled, FALSE if disabled
                ''',
                'unreachables',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ma-subscriber-cfg',
            'ipv4-network',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The flag to enable auto ipv6 interface
                configuration
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-subscriber-cfg',
            'auto-configuration',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses',
            False, 
            [
            _MetaInfoClassMember('auto-configuration', REFERENCE_CLASS, 'AutoConfiguration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration', 
                [], [], 
                '''                Auto IPv6 Interface Configuration
                ''',
                'auto_configuration',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-subscriber-cfg',
            'addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network',
            False, 
            [
            _MetaInfoClassMember('addresses', REFERENCE_CLASS, 'Addresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses', 
                [], [], 
                '''                Set the IPv6 address of an interface
                ''',
                'addresses',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('1280', '65535')], [], 
                '''                MTU Setting of Interface
                ''',
                'mtu',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Override Sending of ICMP Unreachable Messages
                ''',
                'unreachables',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            _MetaInfoClassMember('verify', REFERENCE_ENUM_CLASS, 'Ipv6ReachableViaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_subscriber_cfg', 'Ipv6ReachableViaEnum', 
                [], [], 
                '''                IPv6 Verify Unicast Souce Reachable
                ''',
                'verify',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-subscriber-cfg',
            'ipv6-network',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.FramedPrefix' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.FramedPrefix',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IPV6 framed prefix address
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                IPv6 framed prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'framed-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.DuplicateAddressDetection' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.DuplicateAddressDetection',
            False, 
            [
            _MetaInfoClassMember('attempts', ATTRIBUTE, 'int' , None, None, 
                [('0', '600')], [], 
                '''                Set IPv6 duplicate address detection transmits
                ''',
                'attempts',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'duplicate-address-detection',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInitial' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInitial',
            False, 
            [
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                Initial RA count
                ''',
                'count',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('4', '1800')], [], 
                '''                Initial RA interval in seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'ra-initial',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor',
            False, 
            [
            _MetaInfoClassMember('duplicate-address-detection', REFERENCE_CLASS, 'DuplicateAddressDetection' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.DuplicateAddressDetection', 
                [], [], 
                '''                Duplicate Address Detection (DAD)
                ''',
                'duplicate_address_detection',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('framed-prefix', REFERENCE_CLASS, 'FramedPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.FramedPrefix', 
                [], [], 
                '''                Set the IPv6 framed ipv6 prefix for a
                subscriber interface 
                ''',
                'framed_prefix',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('framed-prefix-pool', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set the IPv6 framed ipv6 prefix pool for a
                subscriber interface 
                ''',
                'framed_prefix_pool',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('managed-config', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Host to use stateful protocol for address
                configuration
                ''',
                'managed_config',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ns-interval', ATTRIBUTE, 'int' , None, None, 
                [('1000', '3600000')], [], 
                '''                Set advertised NS retransmission interval in
                milliseconds
                ''',
                'ns_interval',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('nud-enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                NUD enable
                ''',
                'nud_enable',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('other-config', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Host to use stateful protocol for non-address
                configuration
                ''',
                'other_config',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-hop-limit', REFERENCE_ENUM_CLASS, 'Ipv6NdHopLimitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_subscriber_cfg', 'Ipv6NdHopLimitEnum', 
                [], [], 
                '''                IPv6 ND RA HopLimit
                ''',
                'ra_hop_limit',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-initial', REFERENCE_CLASS, 'RaInitial' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInitial', 
                [], [], 
                '''                IPv6 ND RA Initial
                ''',
                'ra_initial',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '1800')], [], 
                '''                Set IPv6 Router Advertisement (RA) interval in
                seconds
                ''',
                'ra_interval',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '9000')], [], 
                '''                Set IPv6 Router Advertisement (RA) lifetime in
                seconds
                ''',
                'ra_lifetime',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-suppress', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable suppress IPv6 router advertisement
                ''',
                'ra_suppress',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-suppress-mtu', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RA suppress MTU flag
                ''',
                'ra_suppress_mtu',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ra-unicast', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable RA unicast Flag
                ''',
                'ra_unicast',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('reachable-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600000')], [], 
                '''                Set advertised reachability time in
                milliseconds
                ''',
                'reachable_time',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('router-preference', REFERENCE_ENUM_CLASS, 'Ipv6NdRouterPrefTemplateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_subscriber_cfg', 'Ipv6NdRouterPrefTemplateEnum', 
                [], [], 
                '''                RA Router Preference
                ''',
                'router_preference',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('start-ra-on-ipv6-enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Start RA on ipv6-enable config
                ''',
                'start_ra_on_ipv6_enable',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('suppress-cache-learning', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Suppress cache learning flag
                ''',
                'suppress_cache_learning',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-subscriber-cfg',
            'ipv6-neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicy' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicy',
            False, 
            [
            _MetaInfoClassMember('input', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ingress service policy
                ''',
                'input',
                'Cisco-IOS-XR-pbr-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-pbr-subscriber-cfg',
            'service-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Pbr' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Pbr',
            False, 
            [
            _MetaInfoClassMember('service-policy', REFERENCE_CLASS, 'ServicePolicy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicy', 
                [], [], 
                '''                PBR service policy configuration
                ''',
                'service_policy',
                'Cisco-IOS-XR-pbr-subscriber-cfg', False),
            _MetaInfoClassMember('service-policy-in', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Class for subscriber ingress policy
                ''',
                'service_policy_in',
                'Cisco-IOS-XR-pbr-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-pbr-subscriber-cfg',
            'pbr',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-subscriber-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Input' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Input',
            False, 
            [
            _MetaInfoClassMember('account-stats', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE for account stats enabled for
                service-policy applied on dynamic template.
                Note: account stats not supported for
                subscriber type 'ppp' and 'ipsubscriber'.
                ''',
                'account_stats',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('merge', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE for merge enabled for service-policy
                applied on dynamic template.
                ''',
                'merge',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('merge-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Merge ID value
                ''',
                'merge_id',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of policy-map
                ''',
                'policy_name',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('spi-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the SPI
                ''',
                'spi_name',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-bng-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Output' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Output',
            False, 
            [
            _MetaInfoClassMember('account-stats', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE for account stats enabled for
                service-policy applied on dynamic template.
                Note: account stats not supported for
                subscriber type 'ppp' and 'ipsubscriber'.
                ''',
                'account_stats',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('merge', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE for merge enabled for service-policy
                applied on dynamic template.
                ''',
                'merge',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('merge-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Merge ID value
                ''',
                'merge_id',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of policy-map
                ''',
                'policy_name',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('spi-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the SPI
                ''',
                'spi_name',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-bng-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Input', 
                [], [], 
                '''                Subscriber ingress policy
                ''',
                'input',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Output', 
                [], [], 
                '''                Subscriber egress policy
                ''',
                'output',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'service-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-bng-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Qos.Account' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Qos.Account',
            False, 
            [
            _MetaInfoClassMember('aal', REFERENCE_ENUM_CLASS, 'Qosl2DataLinkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg', 'Qosl2DataLinkEnum', 
                [], [], 
                '''                ATM adaptation layer AAL
                ''',
                'aal',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('atm-cell-tax', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ATM cell tax to L2 overhead
                ''',
                'atm_cell_tax',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('encapsulation', REFERENCE_ENUM_CLASS, 'Qosl2EncapEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_bng_cfg', 'Qosl2EncapEnum', 
                [], [], 
                '''                Specify encapsulation type
                ''',
                'encapsulation',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('user-defined', ATTRIBUTE, 'int' , None, None, 
                [('-63', '63')], [], 
                '''                Numeric L2 overhead offset
                ''',
                'user_defined',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'account',
            _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-bng-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Qos.Output' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Qos.Output',
            False, 
            [
            _MetaInfoClassMember('minimum-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Minimum bandwidth value for the subscriber (in
                kbps)
                ''',
                'minimum_bandwidth',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-bng-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService.Qos' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService.Qos',
            False, 
            [
            _MetaInfoClassMember('account', REFERENCE_CLASS, 'Account' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Qos.Account', 
                [], [], 
                '''                QoS L2 overhead accounting
                ''',
                'account',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Qos.Output', 
                [], [], 
                '''                QoS to be applied in egress direction
                ''',
                'output',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('service-policy', REFERENCE_CLASS, 'ServicePolicy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy', 
                [], [], 
                '''                Service policy to be applied in ingress/egress
                direction
                ''',
                'service_policy',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-bng-cfg',
            'qos',
            _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-bng-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices.SubscriberService' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices.SubscriberService',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the template
                ''',
                'template_name',
                'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg', True),
            _MetaInfoClassMember('ipv4-network', REFERENCE_CLASS, 'Ipv4Network' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv4Network', 
                [], [], 
                '''                Interface IPv4 Network configuration data
                ''',
                'ipv4_network',
                'Cisco-IOS-XR-ipv4-ma-subscriber-cfg', False),
            _MetaInfoClassMember('ipv4-packet-filter', REFERENCE_CLASS, 'Ipv4PacketFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter', 
                [], [], 
                '''                IPv4 Packet Filtering configuration for the
                template
                ''',
                'ipv4_packet_filter',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('ipv6-neighbor', REFERENCE_CLASS, 'Ipv6Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor', 
                [], [], 
                '''                Interface IPv6 Network configuration data
                ''',
                'ipv6_neighbor',
                'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', False),
            _MetaInfoClassMember('ipv6-network', REFERENCE_CLASS, 'Ipv6Network' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network', 
                [], [], 
                '''                Interface IPv6 Network configuration data
                ''',
                'ipv6_network',
                'Cisco-IOS-XR-ipv6-ma-subscriber-cfg', False),
            _MetaInfoClassMember('ipv6-packet-filter', REFERENCE_CLASS, 'Ipv6PacketFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter', 
                [], [], 
                '''                IPv6 Packet Filtering configuration for the
                interface
                ''',
                'ipv6_packet_filter',
                'Cisco-IOS-XR-ip-pfilter-subscriber-cfg', False),
            _MetaInfoClassMember('pbr', REFERENCE_CLASS, 'Pbr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Pbr', 
                [], [], 
                '''                Dynamic Template PBR configuration
                ''',
                'pbr',
                'Cisco-IOS-XR-pbr-subscriber-cfg', False),
            _MetaInfoClassMember('qos', REFERENCE_CLASS, 'Qos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.Qos', 
                [], [], 
                '''                QoS dynamically applied configuration template
                ''',
                'qos',
                'Cisco-IOS-XR-qos-ma-bng-cfg', False),
            _MetaInfoClassMember('span-monitor-sessions', REFERENCE_CLASS, 'SpanMonitorSessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions', 
                [], [], 
                '''                Monitor Session container for this template
                ''',
                'span_monitor_sessions',
                'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                Assign the interface to a VRF 
                ''',
                'vrf',
                'Cisco-IOS-XR-infra-rsi-subscriber-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg',
            'subscriber-service',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate.SubscriberServices' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate.SubscriberServices',
            False, 
            [
            _MetaInfoClassMember('subscriber-service', REFERENCE_LIST, 'SubscriberService' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices.SubscriberService', 
                [], [], 
                '''                A Service Type Template 
                ''',
                'subscriber_service',
                'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg',
            'subscriber-services',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
    'DynamicTemplate' : {
        'meta_info' : _MetaInfoClass('DynamicTemplate',
            False, 
            [
            _MetaInfoClassMember('ip-subscribers', REFERENCE_CLASS, 'IpSubscribers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.IpSubscribers', 
                [], [], 
                '''                The IP Subscriber Template Table
                ''',
                'ip_subscribers',
                'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg', False),
            _MetaInfoClassMember('ppps', REFERENCE_CLASS, 'Ppps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.Ppps', 
                [], [], 
                '''                Templates of the PPP Type
                ''',
                'ppps',
                'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg', False),
            _MetaInfoClassMember('subscriber-services', REFERENCE_CLASS, 'SubscriberServices' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg', 'DynamicTemplate.SubscriberServices', 
                [], [], 
                '''                The Service Type Template Table
                ''',
                'subscriber_services',
                'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg',
            'dynamic-template',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-infra-tmplmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_infra_tmplmgr_cfg'
        ),
    },
}
_meta_table['DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession.Attachment']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.SpanMonitorSessions.SpanMonitorSession']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.SpanMonitorSessions']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Outbound']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter.Inbound']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Inbound']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter.Outbound']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf.ExplicitTracking']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Igmp.DefaultVrf']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Igmp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses.AutoConfiguration']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Network.Addresses']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Network']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.FramedPrefix']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Neighbor']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.DuplicateAddressDetection']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Neighbor']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Neighbor.RaInitial']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Neighbor']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Dhcpv6.DelegatedPrefix']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Dhcpv6']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Pbr.ServicePolicy']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Pbr']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Input']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy.Output']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Qos.ServicePolicy']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Qos']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Qos.Account']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Qos']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Qos.Output']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp.Qos']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.SpanMonitorSessions']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv4PacketFilter']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6PacketFilter']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Igmp']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv4Network']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Network']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Ipv6Neighbor']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Dhcpv6']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Pbr']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp.Qos']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps.Ppp']['meta_info']
_meta_table['DynamicTemplate.Ppps.Ppp']['meta_info'].parent =_meta_table['DynamicTemplate.Ppps']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession.Attachment']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions.SpanMonitorSession']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Outbound']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter.Inbound']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Inbound']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter.Outbound']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses.AutoConfiguration']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network.Addresses']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.FramedPrefix']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.DuplicateAddressDetection']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor.RaInitial']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6.DelegatedPrefix']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Pbr.ServicePolicy']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Pbr']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Input']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy.Output']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos.ServicePolicy']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Account']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos.Output']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.SpanMonitorSessions']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4PacketFilter']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6PacketFilter']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv4Network']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Network']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Ipv6Neighbor']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Dhcpv6']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Pbr']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber.Qos']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers.IpSubscriber']['meta_info'].parent =_meta_table['DynamicTemplate.IpSubscribers']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession.Attachment']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions.SpanMonitorSession']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Outbound']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter.Inbound']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Inbound']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter.Outbound']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses.AutoConfiguration']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network.Addresses']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.FramedPrefix']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.DuplicateAddressDetection']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor.RaInitial']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Pbr.ServicePolicy']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Pbr']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Input']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy.Output']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos.ServicePolicy']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos.Account']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos.Output']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.SpanMonitorSessions']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv4PacketFilter']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6PacketFilter']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv4Network']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Network']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Ipv6Neighbor']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Pbr']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService.Qos']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices.SubscriberService']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices.SubscriberService']['meta_info'].parent =_meta_table['DynamicTemplate.SubscriberServices']['meta_info']
_meta_table['DynamicTemplate.Ppps']['meta_info'].parent =_meta_table['DynamicTemplate']['meta_info']
_meta_table['DynamicTemplate.IpSubscribers']['meta_info'].parent =_meta_table['DynamicTemplate']['meta_info']
_meta_table['DynamicTemplate.SubscriberServices']['meta_info'].parent =_meta_table['DynamicTemplate']['meta_info']

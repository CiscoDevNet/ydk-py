


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'PortDownFlushEnum' : _MetaInfoEnum('PortDownFlushEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'port-down-flush':'port_down_flush',
            'enable-port-down-flush':'enable_port_down_flush',
            'disable-port-down-flush':'disable_port_down_flush',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'ErpapsEnum' : _MetaInfoEnum('ErpapsEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'interface':'interface',
            'bridge-domain':'bridge_domain',
            'xconnect':'xconnect',
            'none':'none',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'MacNotificationEnum' : _MetaInfoEnum('MacNotificationEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'no-notif':'no_notif',
            'syslog':'syslog',
            'trap':'trap',
            'syslog-snmp':'syslog_snmp',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'InterworkingEnum' : _MetaInfoEnum('InterworkingEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'ethernet':'ethernet',
            'ipv4':'ipv4',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'MacLimitActionEnum' : _MetaInfoEnum('MacLimitActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'none':'none',
            'flood':'flood',
            'no-flood':'no_flood',
            'shutdown':'shutdown',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'ErpPortEnum' : _MetaInfoEnum('ErpPortEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'none':'none',
            'virtual':'virtual',
            'interface':'interface',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'BgpRouteTargetRoleEnum' : _MetaInfoEnum('BgpRouteTargetRoleEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'both':'both',
            'import':'import_',
            'export':'export',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'MplsSignalingProtocolEnum' : _MetaInfoEnum('MplsSignalingProtocolEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'none':'none',
            'ldp':'ldp',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'LdpVplsIdEnum' : _MetaInfoEnum('LdpVplsIdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'two-byte-as':'two_byte_as',
            'ipv4-address':'ipv4_address',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'RplRoleEnum' : _MetaInfoEnum('RplRoleEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'owner':'owner',
            'neighbor':'neighbor',
            'next-neighbor':'next_neighbor',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'PreferredPathEnum' : _MetaInfoEnum('PreferredPathEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'te-tunnel':'te_tunnel',
            'ip-tunnel':'ip_tunnel',
            'tp-tunnel':'tp_tunnel',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'MacSecureActionEnum' : _MetaInfoEnum('MacSecureActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'restrict':'restrict',
            'none':'none',
            'shutdown':'shutdown',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'L2VpnVerificationEnum' : _MetaInfoEnum('L2VpnVerificationEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'enable':'enable',
            'disable':'disable',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'PwSwitchingPointTlvEnum' : _MetaInfoEnum('PwSwitchingPointTlvEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'hide':'hide',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'VccvVerificationEnum' : _MetaInfoEnum('VccvVerificationEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'none':'none',
            'lsp-ping':'lsp_ping',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'MacLearnEnum' : _MetaInfoEnum('MacLearnEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'default-learning':'default_learning',
            'enable-learning':'enable_learning',
            'disable-learning':'disable_learning',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'EthernetSegmentIdentifierEnum' : _MetaInfoEnum('EthernetSegmentIdentifierEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'type0':'type0',
            'legacy':'legacy',
            'override':'override',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'BdmacLearnEnum' : _MetaInfoEnum('BdmacLearnEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'disable-learning':'disable_learning',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'L2Tpv3SequencingEnum' : _MetaInfoEnum('L2Tpv3SequencingEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'off':'off',
            'both':'both',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'StormControlEnum' : _MetaInfoEnum('StormControlEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'unicast':'unicast',
            'multicast':'multicast',
            'broadcast':'broadcast',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'InterfaceTrafficFloodEnum' : _MetaInfoEnum('InterfaceTrafficFloodEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'traffic-flooding':'traffic_flooding',
            'enable-flooding':'enable_flooding',
            'disable-flooding':'disable_flooding',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'ErpPort1Enum' : _MetaInfoEnum('ErpPort1Enum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'port0':'port0',
            'port1':'port1',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'BgpRouteTargetFormatEnum' : _MetaInfoEnum('BgpRouteTargetFormatEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'none':'none',
            'two-byte-as':'two_byte_as',
            'four-byte-as':'four_byte_as',
            'ipv4-address':'ipv4_address',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'L2VpnLoggingEnum' : _MetaInfoEnum('L2VpnLoggingEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'enable':'enable',
            'disable':'disable',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'FlowLabelLoadBalanceEnum' : _MetaInfoEnum('FlowLabelLoadBalanceEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'off':'off',
            'receive':'receive',
            'transmit':'transmit',
            'both':'both',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'MplsSequencingEnum' : _MetaInfoEnum('MplsSequencingEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'off':'off',
            'transmit':'transmit',
            'receive':'receive',
            'both':'both',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'InterfaceProfileEnum' : _MetaInfoEnum('InterfaceProfileEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'snoop':'snoop',
            'dhcp-protocol':'dhcp_protocol',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'BridgeDomainTransportModeEnum' : _MetaInfoEnum('BridgeDomainTransportModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'vlan-passthrough':'vlan_passthrough',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'L2VpnCapabilityModeEnum' : _MetaInfoEnum('L2VpnCapabilityModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'high-mode':'high_mode',
            'single-mode':'single_mode',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'LoadBalanceEnum' : _MetaInfoEnum('LoadBalanceEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'source-dest-mac':'source_dest_mac',
            'source-dest-ip':'source_dest_ip',
            'pseudowire-label':'pseudowire_label',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'TransportModeEnum' : _MetaInfoEnum('TransportModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'ethernet':'ethernet',
            'vlan':'vlan',
            'vlan-passthrough':'vlan_passthrough',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'ControlWordEnum' : _MetaInfoEnum('ControlWordEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'enable':'enable',
            'disable':'disable',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'FlowLabelTlvCodeEnum' : _MetaInfoEnum('FlowLabelTlvCodeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            '17':'Y_17',
            'disable':'disable',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'BackupDisableEnum' : _MetaInfoEnum('BackupDisableEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'never':'never',
            'delay':'delay',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'BgpRouteDistinguisherEnum' : _MetaInfoEnum('BgpRouteDistinguisherEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'auto':'auto',
            'two-byte-as':'two_byte_as',
            'four-byte-as':'four_byte_as',
            'ipv4-address':'ipv4_address',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'L2EncapsulationEnum' : _MetaInfoEnum('L2EncapsulationEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'vlan':'vlan',
            'ethernet':'ethernet',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'L2TpCookieSizeEnum' : _MetaInfoEnum('L2TpCookieSizeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'zero':'zero',
            'four':'four',
            'eight':'eight',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'TypeOfServiceModeEnum' : _MetaInfoEnum('TypeOfServiceModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'none':'none',
            'reflect':'reflect',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'MacWithdrawBehaviorEnum' : _MetaInfoEnum('MacWithdrawBehaviorEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'legacy':'legacy',
            'optimized':'optimized',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'L2TpSignalingProtocolEnum' : _MetaInfoEnum('L2TpSignalingProtocolEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'none':'none',
            'l2tpv3':'l2tpv3',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'BgpRouteTargetEnum' : _MetaInfoEnum('BgpRouteTargetEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'no-stitching':'no_stitching',
            'stitching':'stitching',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'MacAgingEnum' : _MetaInfoEnum('MacAgingEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg',
        {
            'absolute':'absolute',
            'inactivity':'inactivity',
        }, 'Cisco-IOS-XR-l2vpn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg']),
    'L2Vpn.PwRouting.PwRoutingBgp.EvpnRouteDistinguisher' : {
        'meta_info' : _MetaInfoClass('L2Vpn.PwRouting.PwRoutingBgp.EvpnRouteDistinguisher',
            False, 
            [
            _MetaInfoClassMember('addr-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Addr index
                ''',
                'addr_index',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV4 address
                ''',
                'address',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Two byte or 4 byte AS number
                ''',
                'as_',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('as-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS:nn (hex or decimal format)
                ''',
                'as_index',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BgpRouteDistinguisherEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'BgpRouteDistinguisherEnum', 
                [], [], 
                '''                Router Distinguisher Type
                ''',
                'type',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpn-route-distinguisher',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.PwRouting.PwRoutingBgp' : {
        'meta_info' : _MetaInfoClass('L2Vpn.PwRouting.PwRoutingBgp',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Autodiscovery BGP
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpn-route-distinguisher', REFERENCE_CLASS, 'EvpnRouteDistinguisher' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.PwRouting.PwRoutingBgp.EvpnRouteDistinguisher', 
                [], [], 
                '''                Route Distinguisher
                ''',
                'evpn_route_distinguisher',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pw-routing-bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.PwRouting' : {
        'meta_info' : _MetaInfoClass('L2Vpn.PwRouting',
            False, 
            [
            _MetaInfoClassMember('pw-routing-bgp', REFERENCE_CLASS, 'PwRoutingBgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.PwRouting.PwRoutingBgp', 
                [], [], 
                '''                Enable Autodiscovery BGP Pseudowire-routing BGP
                ''',
                'pw_routing_bgp',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pw-routing-global-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Pseudowire-routing Global ID
                ''',
                'pw_routing_global_id',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pw-routing',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Neighbor' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Neighbor',
            False, 
            [
            _MetaInfoClassMember('ldp-flap', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable targetted LDP session flap action
                ''',
                'ldp_flap',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S.ErpPort0' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S.ErpPort0',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Port0 interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('monitor', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Ethernet ring protection port0 monitor
                ''',
                'monitor',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'erp-port0',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S',
            False, 
            [
            _MetaInfoClassMember('erp-port0', REFERENCE_LIST, 'ErpPort0' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S.ErpPort0', 
                [], [], 
                '''                Configure ERP main port0
                ''',
                'erp_port0',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'erp-port0s',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Rpl' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Rpl',
            False, 
            [
            _MetaInfoClassMember('port', REFERENCE_ENUM_CLASS, 'ErpPort1Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'ErpPort1Enum', 
                [], [], 
                '''                ERP main port number
                ''',
                'port',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('role', REFERENCE_ENUM_CLASS, 'RplRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'RplRoleEnum', 
                [], [], 
                '''                RPL role
                ''',
                'role',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'rpl',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps.Port1' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps.Port1',
            False, 
            [
            _MetaInfoClassMember('aps-channel', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Port1 APS channel in the format of
                InterfaceName, BDName or XconnectName
                ''',
                'aps_channel',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('aps-type', REFERENCE_ENUM_CLASS, 'ErpapsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'ErpapsEnum', 
                [], [], 
                '''                Port1 APS type
                ''',
                'aps_type',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'port1',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable automatic protection switching
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Automatic protection switching level
                ''',
                'level',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('port0', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Port0 APS channel in the format of
                InterfaceName
                ''',
                'port0',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('port1', REFERENCE_CLASS, 'Port1' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps.Port1', 
                [], [], 
                '''                APS channel for ERP port1
                ''',
                'port1',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'aps',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance',
            False, 
            [
            _MetaInfoClassMember('erp-instance-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '2')], [], 
                '''                ERP instance number
                ''',
                'erp_instance_id',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('aps', REFERENCE_CLASS, 'Aps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps', 
                [], [], 
                '''                Automatic protection switching
                ''',
                'aps',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Ethernet ring protection instance
                description
                ''',
                'description',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('inclusion-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Associates a set of VLAN IDs with the G
                .8032 instance
                ''',
                'inclusion_list',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('profile', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Ethernet ring protection instance profile
                ''',
                'profile',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('rpl', REFERENCE_CLASS, 'Rpl' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Rpl', 
                [], [], 
                '''                Ring protection link
                ''',
                'rpl',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'erp-instance',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances',
            False, 
            [
            _MetaInfoClassMember('erp-instance', REFERENCE_LIST, 'ErpInstance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance', 
                [], [], 
                '''                Ethernet ring protection instance
                ''',
                'erp_instance',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'erp-instances',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.NoneOrVirtual' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.NoneOrVirtual',
            False, 
            [
            _MetaInfoClassMember('monitor', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Ethernet ring protection port1 monitor
                ''',
                'monitor',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'none-or-virtual',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.Interface' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Port1 interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('monitor', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Ethernet ring protection port1 monitor
                ''',
                'monitor',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1',
            False, 
            [
            _MetaInfoClassMember('erp-port-type', REFERENCE_ENUM_CLASS, 'ErpPortEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'ErpPortEnum', 
                [], [], 
                '''                Port1 type
                ''',
                'erp_port_type',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.Interface', 
                [], [], 
                '''                interface
                ''',
                'interface',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('none-or-virtual', REFERENCE_CLASS, 'NoneOrVirtual' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.NoneOrVirtual', 
                [], [], 
                '''                none or virtual
                ''',
                'none_or_virtual',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'erp-port1',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S',
            False, 
            [
            _MetaInfoClassMember('erp-port1', REFERENCE_LIST, 'ErpPort1' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1', 
                [], [], 
                '''                Ethernet ring protection port1
                ''',
                'erp_port1',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'erp-port1s',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.G8032Rings.G8032Ring' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.G8032Rings.G8032Ring',
            False, 
            [
            _MetaInfoClassMember('g8032-ring-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Name of the G8032 ring
                ''',
                'g8032_ring_name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('erp-instances', REFERENCE_CLASS, 'ErpInstances' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances', 
                [], [], 
                '''                List of ethernet ring protection instance
                ''',
                'erp_instances',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('erp-port0s', REFERENCE_CLASS, 'ErpPort0S' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S', 
                [], [], 
                '''                Ethernet ring protection port0
                ''',
                'erp_port0s',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('erp-port1s', REFERENCE_CLASS, 'ErpPort1S' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S', 
                [], [], 
                '''                Ethernet ring protection port0
                ''',
                'erp_port1s',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('erp-provider-bridge', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Ethernet ring protection provider bridge
                ''',
                'erp_provider_bridge',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('exclusion-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Vlan IDs in the format of a-b,c,d,e-f,g
                ,untagged
                ''',
                'exclusion_list',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('open-ring', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify the G.8032 instance as open ring
                ''',
                'open_ring',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'g8032-ring',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.G8032Rings' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.G8032Rings',
            False, 
            [
            _MetaInfoClassMember('g8032-ring', REFERENCE_LIST, 'G8032Ring' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.G8032Rings.G8032Ring', 
                [], [], 
                '''                G8032 Ring
                ''',
                'g8032_ring',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'g8032-rings',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits.BackupAttachmentCircuit' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits.BackupAttachmentCircuit',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of the attachment circuit interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'backup-attachment-circuit',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits',
            False, 
            [
            _MetaInfoClassMember('backup-attachment-circuit', REFERENCE_LIST, 'BackupAttachmentCircuit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits.BackupAttachmentCircuit', 
                [], [], 
                '''                Backup attachment circuit
                ''',
                'backup_attachment_circuit',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'backup-attachment-circuits',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns.PseudowireEvpn' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns.PseudowireEvpn',
            False, 
            [
            _MetaInfoClassMember('eviid', ATTRIBUTE, 'int' , None, None, 
                [('1', '65534')], [], 
                '''                Ethernet VPN ID
                ''',
                'eviid',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('remote-acid', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777215')], [], 
                '''                Remote AC ID
                ''',
                'remote_acid',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('source-acid', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777215')], [], 
                '''                Source AC ID
                ''',
                'source_acid',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pseudowire-evpn',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns',
            False, 
            [
            _MetaInfoClassMember('pseudowire-evpn', REFERENCE_LIST, 'PseudowireEvpn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns.PseudowireEvpn', 
                [], [], 
                '''                EVPN P2P Service Configuration
                ''',
                'pseudowire_evpn',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pseudowire-evpns',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.MplsStaticLabels' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.MplsStaticLabels',
            False, 
            [
            _MetaInfoClassMember('local-static-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Pseudowire local static label
                ''',
                'local_static_label',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('remote-static-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Pseudowire remote static label
                ''',
                'remote_static_label',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'mpls-static-labels',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels',
            False, 
            [
            _MetaInfoClassMember('local-static-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Pseudowire local static label
                ''',
                'local_static_label',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('remote-static-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Pseudowire remote static label
                ''',
                'remote_static_label',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'backup-mpls-static-labels',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire',
            False, 
            [
            _MetaInfoClassMember('neighbor', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor IP address
                ''',
                'neighbor',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('pseudowire-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Pseudowire ID
                ''',
                'pseudowire_id',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('backup-mpls-static-labels', REFERENCE_CLASS, 'BackupMplsStaticLabels' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels', 
                [], [], 
                '''                MPLS static labels
                ''',
                'backup_mpls_static_labels',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('backup-pw-class', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                PW class template name to use for the
                backup PW
                ''',
                'backup_pw_class',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'backup-pseudowire',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires',
            False, 
            [
            _MetaInfoClassMember('backup-pseudowire', REFERENCE_LIST, 'BackupPseudowire' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire', 
                [], [], 
                '''                Backup pseudowire for the cross connect
                ''',
                'backup_pseudowire',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'backup-pseudowires',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpRemoteCookie' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpRemoteCookie',
            False, 
            [
            _MetaInfoClassMember('higher-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Higher remote cookie value
                ''',
                'higher_value',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('lower-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lower remote cookie value
                ''',
                'lower_value',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('size', REFERENCE_ENUM_CLASS, 'L2TpCookieSizeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2TpCookieSizeEnum', 
                [], [], 
                '''                Remote cookie size
                ''',
                'size',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'l2tp-remote-cookie',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpSecondaryLocalCookie' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpSecondaryLocalCookie',
            False, 
            [
            _MetaInfoClassMember('higher-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Higher local cookie value
                ''',
                'higher_value',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('lower-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lower local cookie value
                ''',
                'lower_value',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('size', REFERENCE_ENUM_CLASS, 'L2TpCookieSizeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2TpCookieSizeEnum', 
                [], [], 
                '''                Local cookie size
                ''',
                'size',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'l2tp-secondary-local-cookie',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpLocalCookie' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpLocalCookie',
            False, 
            [
            _MetaInfoClassMember('higher-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Higher local cookie value
                ''',
                'higher_value',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('lower-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lower local cookie value
                ''',
                'lower_value',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('size', REFERENCE_ENUM_CLASS, 'L2TpCookieSizeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2TpCookieSizeEnum', 
                [], [], 
                '''                Local cookie size
                ''',
                'size',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'l2tp-local-cookie',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes',
            False, 
            [
            _MetaInfoClassMember('l2tp-local-cookie', REFERENCE_CLASS, 'L2TpLocalCookie' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpLocalCookie', 
                [], [], 
                '''                L2TP local cookie
                ''',
                'l2tp_local_cookie',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('l2tp-local-session-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                L2TP local session ID
                ''',
                'l2tp_local_session_id',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('l2tp-remote-cookie', REFERENCE_CLASS, 'L2TpRemoteCookie' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpRemoteCookie', 
                [], [], 
                '''                L2TP remote cookie
                ''',
                'l2tp_remote_cookie',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('l2tp-remote-session-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                L2TP remote session ID
                ''',
                'l2tp_remote_session_id',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('l2tp-secondary-local-cookie', REFERENCE_CLASS, 'L2TpSecondaryLocalCookie' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpSecondaryLocalCookie', 
                [], [], 
                '''                L2TP secondary local cookie
                ''',
                'l2tp_secondary_local_cookie',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'l2tp-static-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStatic' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStatic',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable pseudowire L2TPv3 static
                configuration
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'l2tp-static',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Pseudowire IPv4 address
                ''',
                'neighbor',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('backup-pseudowires', REFERENCE_CLASS, 'BackupPseudowires' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires', 
                [], [], 
                '''                List of pseudowires
                ''',
                'backup_pseudowires',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Pseudowire Bandwidth
                ''',
                'bandwidth',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('class', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Name of the pseudowire class
                ''',
                'class_',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('l2tp-static', REFERENCE_CLASS, 'L2TpStatic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStatic', 
                [], [], 
                '''                Pseudowire L2TPv3 static configuration
                ''',
                'l2tp_static',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('l2tp-static-attributes', REFERENCE_CLASS, 'L2TpStaticAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes', 
                [], [], 
                '''                L2TP Static Attributes
                ''',
                'l2tp_static_attributes',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('mpls-static-labels', REFERENCE_CLASS, 'MplsStaticLabels' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.MplsStaticLabels', 
                [], [], 
                '''                MPLS static labels
                ''',
                'mpls_static_labels',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Value of the Pseudowire source address.
                Must be IPv6 only.
                ''',
                'source_address',
                'Cisco-IOS-XR-l2vpn-cfg', False, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Value of the Pseudowire source address.
                        Must be IPv6 only.
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-l2vpn-cfg', False),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Value of the Pseudowire source address.
                        Must be IPv6 only.
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-l2vpn-cfg', False),
                ]),
            _MetaInfoClassMember('tag-impose', ATTRIBUTE, 'int' , None, None, 
                [('1', '4094')], [], 
                '''                Tag Impose vlan tagged mode
                ''',
                'tag_impose',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.MplsStaticLabels' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.MplsStaticLabels',
            False, 
            [
            _MetaInfoClassMember('local-static-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Pseudowire local static label
                ''',
                'local_static_label',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('remote-static-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Pseudowire remote static label
                ''',
                'remote_static_label',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'mpls-static-labels',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels',
            False, 
            [
            _MetaInfoClassMember('local-static-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Pseudowire local static label
                ''',
                'local_static_label',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('remote-static-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Pseudowire remote static label
                ''',
                'remote_static_label',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'backup-mpls-static-labels',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire',
            False, 
            [
            _MetaInfoClassMember('neighbor', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor IP address
                ''',
                'neighbor',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('pseudowire-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Pseudowire ID
                ''',
                'pseudowire_id',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('backup-mpls-static-labels', REFERENCE_CLASS, 'BackupMplsStaticLabels' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels', 
                [], [], 
                '''                MPLS static labels
                ''',
                'backup_mpls_static_labels',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('backup-pw-class', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                PW class template name to use for the
                backup PW
                ''',
                'backup_pw_class',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'backup-pseudowire',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires',
            False, 
            [
            _MetaInfoClassMember('backup-pseudowire', REFERENCE_LIST, 'BackupPseudowire' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire', 
                [], [], 
                '''                Backup pseudowire for the cross connect
                ''',
                'backup_pseudowire',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'backup-pseudowires',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpRemoteCookie' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpRemoteCookie',
            False, 
            [
            _MetaInfoClassMember('higher-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Higher remote cookie value
                ''',
                'higher_value',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('lower-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lower remote cookie value
                ''',
                'lower_value',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('size', REFERENCE_ENUM_CLASS, 'L2TpCookieSizeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2TpCookieSizeEnum', 
                [], [], 
                '''                Remote cookie size
                ''',
                'size',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'l2tp-remote-cookie',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpSecondaryLocalCookie' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpSecondaryLocalCookie',
            False, 
            [
            _MetaInfoClassMember('higher-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Higher local cookie value
                ''',
                'higher_value',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('lower-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lower local cookie value
                ''',
                'lower_value',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('size', REFERENCE_ENUM_CLASS, 'L2TpCookieSizeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2TpCookieSizeEnum', 
                [], [], 
                '''                Local cookie size
                ''',
                'size',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'l2tp-secondary-local-cookie',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpLocalCookie' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpLocalCookie',
            False, 
            [
            _MetaInfoClassMember('higher-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Higher local cookie value
                ''',
                'higher_value',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('lower-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lower local cookie value
                ''',
                'lower_value',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('size', REFERENCE_ENUM_CLASS, 'L2TpCookieSizeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2TpCookieSizeEnum', 
                [], [], 
                '''                Local cookie size
                ''',
                'size',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'l2tp-local-cookie',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes',
            False, 
            [
            _MetaInfoClassMember('l2tp-local-cookie', REFERENCE_CLASS, 'L2TpLocalCookie' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpLocalCookie', 
                [], [], 
                '''                L2TP local cookie
                ''',
                'l2tp_local_cookie',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('l2tp-local-session-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                L2TP local session ID
                ''',
                'l2tp_local_session_id',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('l2tp-remote-cookie', REFERENCE_CLASS, 'L2TpRemoteCookie' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpRemoteCookie', 
                [], [], 
                '''                L2TP remote cookie
                ''',
                'l2tp_remote_cookie',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('l2tp-remote-session-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                L2TP remote session ID
                ''',
                'l2tp_remote_session_id',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('l2tp-secondary-local-cookie', REFERENCE_CLASS, 'L2TpSecondaryLocalCookie' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpSecondaryLocalCookie', 
                [], [], 
                '''                L2TP secondary local cookie
                ''',
                'l2tp_secondary_local_cookie',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'l2tp-static-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStatic' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStatic',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable pseudowire L2TPv3 static
                configuration
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'l2tp-static',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress',
            False, 
            [
            _MetaInfoClassMember('pseudowire-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Pseudowire IPv6 address. A pseudowire
                can have only one address: IPv4 or IPv6
                ''',
                'pseudowire_address',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('backup-pseudowires', REFERENCE_CLASS, 'BackupPseudowires' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires', 
                [], [], 
                '''                List of pseudowires
                ''',
                'backup_pseudowires',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Pseudowire Bandwidth
                ''',
                'bandwidth',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('class', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Name of the pseudowire class
                ''',
                'class_',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('l2tp-static', REFERENCE_CLASS, 'L2TpStatic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStatic', 
                [], [], 
                '''                Pseudowire L2TPv3 static configuration
                ''',
                'l2tp_static',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('l2tp-static-attributes', REFERENCE_CLASS, 'L2TpStaticAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes', 
                [], [], 
                '''                L2TP Static Attributes
                ''',
                'l2tp_static_attributes',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('mpls-static-labels', REFERENCE_CLASS, 'MplsStaticLabels' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.MplsStaticLabels', 
                [], [], 
                '''                MPLS static labels
                ''',
                'mpls_static_labels',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Value of the Pseudowire source address.
                Must be IPv6 only.
                ''',
                'source_address',
                'Cisco-IOS-XR-l2vpn-cfg', False, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Value of the Pseudowire source address.
                        Must be IPv6 only.
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-l2vpn-cfg', False),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Value of the Pseudowire source address.
                        Must be IPv6 only.
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-l2vpn-cfg', False),
                ]),
            _MetaInfoClassMember('tag-impose', ATTRIBUTE, 'int' , None, None, 
                [('1', '4094')], [], 
                '''                Tag Impose vlan tagged mode
                ''',
                'tag_impose',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pseudowire-address',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire',
            False, 
            [
            _MetaInfoClassMember('pseudowire-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Pseudowire ID
                ''',
                'pseudowire_id',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor', 
                [], [], 
                '''                keys: neighbor
                ''',
                'neighbor',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pseudowire-address', REFERENCE_LIST, 'PseudowireAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress', 
                [], [], 
                '''                keys: pseudowire-address
                ''',
                'pseudowire_address',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pseudowire',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires',
            False, 
            [
            _MetaInfoClassMember('pseudowire', REFERENCE_LIST, 'Pseudowire' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire', 
                [], [], 
                '''                Pseudowire configuration
                ''',
                'pseudowire',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pseudowires',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions.MonitorSession' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions.MonitorSession',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Name of the monitor session
                ''',
                'name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable monitor session segment 
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'monitor-session',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions',
            False, 
            [
            _MetaInfoClassMember('monitor-session', REFERENCE_LIST, 'MonitorSession' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions.MonitorSession', 
                [], [], 
                '''                Monitor session segment
                ''',
                'monitor_session',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'monitor-sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds.PseudowireRouted' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds.PseudowireRouted',
            False, 
            [
            _MetaInfoClassMember('global-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Target Global ID
                ''',
                'global_id',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Target Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('acid', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Target AC ID
                ''',
                'acid',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('sacid', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Source AC ID
                ''',
                'sacid',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('class', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Name of the pseudowire class
                ''',
                'class_',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('tag-impose', ATTRIBUTE, 'int' , None, None, 
                [('1', '4094')], [], 
                '''                Tag Impose vlan tagged mode
                ''',
                'tag_impose',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pseudowire-routed',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds',
            False, 
            [
            _MetaInfoClassMember('pseudowire-routed', REFERENCE_LIST, 'PseudowireRouted' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds.PseudowireRouted', 
                [], [], 
                '''                Pseudowire configuration
                ''',
                'pseudowire_routed',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pseudowire-routeds',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits.AttachmentCircuit' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits.AttachmentCircuit',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of the attachment circuit interface
                ''',
                'name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable attachment circuit interface
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'attachment-circuit',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits',
            False, 
            [
            _MetaInfoClassMember('attachment-circuit', REFERENCE_LIST, 'AttachmentCircuit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits.AttachmentCircuit', 
                [], [], 
                '''                Attachment circuit interface
                ''',
                'attachment_circuit',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'attachment-circuits',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 38)], [], 
                '''                Name of the point to point xconnect
                ''',
                'name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('attachment-circuits', REFERENCE_CLASS, 'AttachmentCircuits' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits', 
                [], [], 
                '''                List of attachment circuits
                ''',
                'attachment_circuits',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('backup-attachment-circuits', REFERENCE_CLASS, 'BackupAttachmentCircuits' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits', 
                [], [], 
                '''                List of backup attachment circuits
                ''',
                'backup_attachment_circuits',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('interworking', REFERENCE_ENUM_CLASS, 'InterworkingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'InterworkingEnum', 
                [], [], 
                '''                Interworking
                ''',
                'interworking',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('monitor-sessions', REFERENCE_CLASS, 'MonitorSessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions', 
                [], [], 
                '''                List of Monitor session segments
                ''',
                'monitor_sessions',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('p2p-description', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                cross connect description Name
                ''',
                'p2p_description',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pseudowire-evpns', REFERENCE_CLASS, 'PseudowireEvpns' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns', 
                [], [], 
                '''                List of EVPN Services
                ''',
                'pseudowire_evpns',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pseudowire-routeds', REFERENCE_CLASS, 'PseudowireRouteds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds', 
                [], [], 
                '''                List of pseudowire-routed
                ''',
                'pseudowire_routeds',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pseudowires', REFERENCE_CLASS, 'Pseudowires' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires', 
                [], [], 
                '''                List of pseudowires
                ''',
                'pseudowires',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'p2p-xconnect',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects',
            False, 
            [
            _MetaInfoClassMember('p2p-xconnect', REFERENCE_LIST, 'P2PXconnect' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect', 
                [], [], 
                '''                Point to point xconnect
                ''',
                'p2p_xconnect',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'p2p-xconnects',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.RouteDistinguisher' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.RouteDistinguisher',
            False, 
            [
            _MetaInfoClassMember('addr-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Addr index
                ''',
                'addr_index',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV4 address
                ''',
                'address',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Two byte or 4 byte AS number
                ''',
                'as_',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('as-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS:nn (hex or decimal format)
                ''',
                'as_index',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BgpRouteDistinguisherEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'BgpRouteDistinguisherEnum', 
                [], [], 
                '''                Router distinguisher type
                ''',
                'type',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'route-distinguisher',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRoutePolicy' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRoutePolicy',
            False, 
            [
            _MetaInfoClassMember('export', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Export route policy
                ''',
                'export',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'mp2mp-route-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.TwoByteAsOrFourByteAs' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.TwoByteAsOrFourByteAs',
            False, 
            [
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Two byte or 4 byte AS number
                ''',
                'as_',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('as-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS:nn (hex or decimal format)
                ''',
                'as_index',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'two-byte-as-or-four-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.Ipv4Address' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.Ipv4Address',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV4 address
                ''',
                'address',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('addr-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Addr index
                ''',
                'addr_index',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'ipv4-address',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget',
            False, 
            [
            _MetaInfoClassMember('role', REFERENCE_ENUM_CLASS, 'BgpRouteTargetRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'BgpRouteTargetRoleEnum', 
                [], [], 
                '''                Role of the router target type
                ''',
                'role',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('format', REFERENCE_ENUM_CLASS, 'BgpRouteTargetFormatEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'BgpRouteTargetFormatEnum', 
                [], [], 
                '''                Format of the route target
                ''',
                'format',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('ipv4-address', REFERENCE_LIST, 'Ipv4Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.Ipv4Address', 
                [], [], 
                '''                ipv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('two-byte-as-or-four-byte-as', REFERENCE_LIST, 'TwoByteAsOrFourByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.TwoByteAsOrFourByteAs', 
                [], [], 
                '''                two byte as or four byte as
                ''',
                'two_byte_as_or_four_byte_as',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'mp2mp-route-target',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets',
            False, 
            [
            _MetaInfoClassMember('mp2mp-route-target', REFERENCE_LIST, 'Mp2MpRouteTarget' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget', 
                [], [], 
                '''                Name of the Route Target
                ''',
                'mp2mp_route_target',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'mp2mp-route-targets',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.FlowLabelLoadBalance' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.FlowLabelLoadBalance',
            False, 
            [
            _MetaInfoClassMember('flow-label', REFERENCE_ENUM_CLASS, 'FlowLabelLoadBalanceEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'FlowLabelLoadBalanceEnum', 
                [], [], 
                '''                Flow Label load balance type
                ''',
                'flow_label',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('static', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Static Flow Label
                ''',
                'static',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'flow-label-load-balance',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits.RemoteCeidAttachmentCircuit' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits.RemoteCeidAttachmentCircuit',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the Attachment Circuit
                ''',
                'name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('remote-ce-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '16384')], [], 
                '''                Remote Customer Edge Identifier
                ''',
                'remote_ce_id',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'remote-ceid-attachment-circuit',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits',
            False, 
            [
            _MetaInfoClassMember('remote-ceid-attachment-circuit', REFERENCE_LIST, 'RemoteCeidAttachmentCircuit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits.RemoteCeidAttachmentCircuit', 
                [], [], 
                '''                AC And Remote Customer Edge Identifier
                ''',
                'remote_ceid_attachment_circuit',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'remote-ceid-attachment-circuits',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid',
            False, 
            [
            _MetaInfoClassMember('ce-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '16384')], [], 
                '''                Local Customer Edge Identifier
                ''',
                'ce_id',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('remote-ceid-attachment-circuits', REFERENCE_CLASS, 'RemoteCeidAttachmentCircuits' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits', 
                [], [], 
                '''                AC And Remote Customer Edge Identifier
                Table
                ''',
                'remote_ceid_attachment_circuits',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'ceid',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids',
            False, 
            [
            _MetaInfoClassMember('ceid', REFERENCE_LIST, 'Ceid' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid', 
                [], [], 
                '''                Local Customer Edge Identifier 
                ''',
                'ceid',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'ceids',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol',
            False, 
            [
            _MetaInfoClassMember('ce-range', ATTRIBUTE, 'int' , None, None, 
                [('11', '100')], [], 
                '''                Local Customer Edge Identifier
                ''',
                'ce_range',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('ceids', REFERENCE_CLASS, 'Ceids' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids', 
                [], [], 
                '''                Local Customer Edge Identifier Table
                ''',
                'ceids',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable signaling protocol
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('flow-label-load-balance', REFERENCE_CLASS, 'FlowLabelLoadBalance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.FlowLabelLoadBalance', 
                [], [], 
                '''                Enable Flow Label based load balancing
                ''',
                'flow_label_load_balance',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'mp2mp-signaling-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable auto-discovery
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('mp2mp-route-policy', REFERENCE_CLASS, 'Mp2MpRoutePolicy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRoutePolicy', 
                [], [], 
                '''                Route policy
                ''',
                'mp2mp_route_policy',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('mp2mp-route-targets', REFERENCE_CLASS, 'Mp2MpRouteTargets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets', 
                [], [], 
                '''                Route Target
                ''',
                'mp2mp_route_targets',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('mp2mp-signaling-protocol', REFERENCE_CLASS, 'Mp2MpSignalingProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol', 
                [], [], 
                '''                signaling protocol in this MP2MP
                ''',
                'mp2mp_signaling_protocol',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('route-distinguisher', REFERENCE_CLASS, 'RouteDistinguisher' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.RouteDistinguisher', 
                [], [], 
                '''                Route Distinguisher
                ''',
                'route_distinguisher',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'mp2mp-auto-discovery',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 26)], [], 
                '''                Name of the multi point to multi point
                xconnect
                ''',
                'name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('mp2mp-auto-discovery', REFERENCE_CLASS, 'Mp2MpAutoDiscovery' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery', 
                [], [], 
                '''                auto-discovery in this MP2MP
                ''',
                'mp2mp_auto_discovery',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('mp2mp-control-word', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable control word
                ''',
                'mp2mp_control_word',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('mp2mp-interworking', REFERENCE_ENUM_CLASS, 'InterworkingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'InterworkingEnum', 
                [], [], 
                '''                Interworking
                ''',
                'mp2mp_interworking',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('mp2mp-shutdown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                shutdown this MP2MP VPWS instance
                ''',
                'mp2mp_shutdown',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('mp2mpl2-encapsulation', REFERENCE_ENUM_CLASS, 'L2EncapsulationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2EncapsulationEnum', 
                [], [], 
                '''                Configure Layer 2 Encapsulation
                ''',
                'mp2mpl2_encapsulation',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('mp2mpmtu', ATTRIBUTE, 'int' , None, None, 
                [('64', '65535')], [], 
                '''                Maximum transmission unit for this MP2MP
                VPWS instance
                ''',
                'mp2mpmtu',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('mp2mpvpn-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                VPN Identifier
                ''',
                'mp2mpvpn_id',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'mp2mp-xconnect',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects',
            False, 
            [
            _MetaInfoClassMember('mp2mp-xconnect', REFERENCE_LIST, 'Mp2MpXconnect' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect', 
                [], [], 
                '''                Multi point to multi point xconnect
                ''',
                'mp2mp_xconnect',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'mp2mp-xconnects',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups.XconnectGroup' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups.XconnectGroup',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Name of the xconnect group
                ''',
                'name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('mp2mp-xconnects', REFERENCE_CLASS, 'Mp2MpXconnects' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects', 
                [], [], 
                '''                List of multi point to multi point xconnects
                ''',
                'mp2mp_xconnects',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('p2p-xconnects', REFERENCE_CLASS, 'P2PXconnects' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects', 
                [], [], 
                '''                List of point to point xconnects
                ''',
                'p2p_xconnects',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'xconnect-group',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.XconnectGroups' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.XconnectGroups',
            False, 
            [
            _MetaInfoClassMember('xconnect-group', REFERENCE_LIST, 'XconnectGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups.XconnectGroup', 
                [], [], 
                '''                Xconnect group
                ''',
                'xconnect_group',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'xconnect-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl.StormControlUnit' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl.StormControlUnit',
            False, 
            [
            _MetaInfoClassMember('kbits-per-sec', ATTRIBUTE, 'int' , None, None, 
                [('64', '1280000')], [], 
                '''                Kilobits Per Second, PktsPerSec and KbitsPerSec
                cannot be configured together
                ''',
                'kbits_per_sec',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pkts-per-sec', ATTRIBUTE, 'int' , None, None, 
                [('1', '160000')], [], 
                '''                Packets Per Second, PktsPerSec and KbitsPerSec
                cannot be configured together
                ''',
                'pkts_per_sec',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'storm-control-unit',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl',
            False, 
            [
            _MetaInfoClassMember('sctype', REFERENCE_ENUM_CLASS, 'StormControlEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'StormControlEnum', 
                [], [], 
                '''                Storm Control Type
                ''',
                'sctype',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('storm-control-unit', REFERENCE_CLASS, 'StormControlUnit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl.StormControlUnit', 
                [], [], 
                '''                Specify units for Storm Control Configuration
                ''',
                'storm_control_unit',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bd-storm-control',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls',
            False, 
            [
            _MetaInfoClassMember('bd-storm-control', REFERENCE_LIST, 'BdStormControl' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl', 
                [], [], 
                '''                Storm Control Type
                ''',
                'bd_storm_control',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bd-storm-controls',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses.MemberVniStaticMacAddress' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses.MemberVniStaticMacAddress',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Static MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('next-hop-ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Enable Static Mac Address Configuration
                ''',
                'next_hop_ip',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'member-vni-static-mac-address',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses',
            False, 
            [
            _MetaInfoClassMember('member-vni-static-mac-address', REFERENCE_LIST, 'MemberVniStaticMacAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses.MemberVniStaticMacAddress', 
                [], [], 
                '''                Static Mac Address Configuration
                ''',
                'member_vni_static_mac_address',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'member-vni-static-mac-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni',
            False, 
            [
            _MetaInfoClassMember('vni', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777215')], [], 
                '''                VxLAN Network Identifier number
                ''',
                'vni',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('member-vni-static-mac-addresses', REFERENCE_CLASS, 'MemberVniStaticMacAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses', 
                [], [], 
                '''                Static Mac Address Table
                ''',
                'member_vni_static_mac_addresses',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'member-vni',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis',
            False, 
            [
            _MetaInfoClassMember('member-vni', REFERENCE_LIST, 'MemberVni' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni', 
                [], [], 
                '''                Bridge Domain Member VxLAN Network
                Identifier 
                ''',
                'member_vni',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'member-vnis',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacLimit' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacLimit',
            False, 
            [
            _MetaInfoClassMember('bd-mac-limit-action', REFERENCE_ENUM_CLASS, 'MacLimitActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MacLimitActionEnum', 
                [], [], 
                '''                MAC address limit enforcement action
                ''',
                'bd_mac_limit_action',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bd-mac-limit-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of MAC addresses after which MAC
                limit action is taken
                ''',
                'bd_mac_limit_max',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bd-mac-limit-notif', REFERENCE_ENUM_CLASS, 'MacNotificationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MacNotificationEnum', 
                [], [], 
                '''                Mac Address Limit Notification
                ''',
                'bd_mac_limit_notif',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bd-mac-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters.BdMacFilter' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters.BdMacFilter',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Static MAC address
                ''',
                'address',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('drop', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                MAC address for filtering
                ''',
                'drop',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bd-mac-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters',
            False, 
            [
            _MetaInfoClassMember('bd-mac-filter', REFERENCE_LIST, 'BdMacFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters.BdMacFilter', 
                [], [], 
                '''                Static MAC address
                ''',
                'bd_mac_filter',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bd-mac-filters',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.MacSecure' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.MacSecure',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'MacSecureActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MacSecureActionEnum', 
                [], [], 
                '''                MAC secure enforcement action
                ''',
                'action',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MAC Secure
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('logging', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                MAC Secure Logging
                ''',
                'logging',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'mac-secure',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacAging' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacAging',
            False, 
            [
            _MetaInfoClassMember('bd-mac-aging-time', ATTRIBUTE, 'int' , None, None, 
                [('300', '30000')], [], 
                '''                Mac Aging Time
                ''',
                'bd_mac_aging_time',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bd-mac-aging-type', REFERENCE_ENUM_CLASS, 'MacAgingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MacAgingEnum', 
                [], [], 
                '''                MAC address aging type
                ''',
                'bd_mac_aging_type',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bd-mac-aging',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac',
            False, 
            [
            _MetaInfoClassMember('bd-mac-aging', REFERENCE_CLASS, 'BdMacAging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacAging', 
                [], [], 
                '''                MAC-Aging configuration commands
                ''',
                'bd_mac_aging',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bd-mac-filters', REFERENCE_CLASS, 'BdMacFilters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters', 
                [], [], 
                '''                Filter Mac Address
                ''',
                'bd_mac_filters',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bd-mac-learn', REFERENCE_ENUM_CLASS, 'BdmacLearnEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'BdmacLearnEnum', 
                [], [], 
                '''                Mac Learning Type
                ''',
                'bd_mac_learn',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bd-mac-limit', REFERENCE_CLASS, 'BdMacLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacLimit', 
                [], [], 
                '''                MAC-Limit configuration commands
                ''',
                'bd_mac_limit',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bd-mac-port-down-flush', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable MAC Flush when Port goes Down
                ''',
                'bd_mac_port_down_flush',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bd-mac-withdraw', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable Mac Withdraw
                ''',
                'bd_mac_withdraw',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bd-mac-withdraw-access-pw-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                MAC withdraw on Access PW
                ''',
                'bd_mac_withdraw_access_pw_disable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bd-mac-withdraw-behavior', REFERENCE_ENUM_CLASS, 'MacWithdrawBehaviorEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MacWithdrawBehaviorEnum', 
                [], [], 
                '''                MAC withdraw sent on bridge port down
                ''',
                'bd_mac_withdraw_behavior',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bd-mac-withdraw-relay', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Mac withdraw sent from access PW to access
                PW
                ''',
                'bd_mac_withdraw_relay',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('mac-secure', REFERENCE_CLASS, 'MacSecure' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.MacSecure', 
                [], [], 
                '''                MAC Secure
                ''',
                'mac_secure',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bridge-domain-mac',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.NvSatellite' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.NvSatellite',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable nV Satellite Settings
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('offload-ipv4-multicast-enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable IPv4 Multicast Offload to Satellite
                Nodes
                ''',
                'offload_ipv4_multicast_enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'nv-satellite',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeSplitHorizonGroup' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeSplitHorizonGroup',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable split horizon group
                ''',
                'disable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pbb-edge-split-horizon-group',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings.PbbStaticMacMapping' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings.PbbStaticMacMapping',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Static MAC address
                ''',
                'address',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('pbb-static-mac-mapping-bmac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Static backbone MAC address to map
                with
                ''',
                'pbb_static_mac_mapping_bmac',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pbb-static-mac-mapping',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings',
            False, 
            [
            _MetaInfoClassMember('pbb-static-mac-mapping', REFERENCE_LIST, 'PbbStaticMacMapping' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings.PbbStaticMacMapping', 
                [], [], 
                '''                PBB Static Mac Address Mapping
                Configuration
                ''',
                'pbb_static_mac_mapping',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pbb-static-mac-mappings',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeDhcpProfile' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeDhcpProfile',
            False, 
            [
            _MetaInfoClassMember('dhcp-snooping-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Disable DHCP snooping
                ''',
                'dhcp_snooping_id',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('profile-id', REFERENCE_ENUM_CLASS, 'InterfaceProfileEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'InterfaceProfileEnum', 
                [], [], 
                '''                Set the snooping profile
                ''',
                'profile_id',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pbb-edge-dhcp-profile',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacLimit' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacLimit',
            False, 
            [
            _MetaInfoClassMember('pbb-edge-mac-limit-action', REFERENCE_ENUM_CLASS, 'MacLimitActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MacLimitActionEnum', 
                [], [], 
                '''                MAC address limit enforcement action
                ''',
                'pbb_edge_mac_limit_action',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pbb-edge-mac-limit-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of MAC addresses after which
                MAC limit action is taken
                ''',
                'pbb_edge_mac_limit_max',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pbb-edge-mac-limit-notif', REFERENCE_ENUM_CLASS, 'MacNotificationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MacNotificationEnum', 
                [], [], 
                '''                MAC address limit notification action
                ''',
                'pbb_edge_mac_limit_notif',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pbb-edge-mac-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacAging' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacAging',
            False, 
            [
            _MetaInfoClassMember('pbb-edge-mac-aging-time', ATTRIBUTE, 'int' , None, None, 
                [('300', '30000')], [], 
                '''                Mac Aging Time
                ''',
                'pbb_edge_mac_aging_time',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pbb-edge-mac-aging-type', REFERENCE_ENUM_CLASS, 'MacAgingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MacAgingEnum', 
                [], [], 
                '''                MAC address aging type
                ''',
                'pbb_edge_mac_aging_type',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pbb-edge-mac-aging',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacSecure' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacSecure',
            False, 
            [
            _MetaInfoClassMember('accept-shutdown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Accept Virtual instance port to be
                shutdown on mac violation
                ''',
                'accept_shutdown',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'MacSecureActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MacSecureActionEnum', 
                [], [], 
                '''                MAC secure enforcement action
                ''',
                'action',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable Virtual instance port MAC
                Secure
                ''',
                'disable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MAC Secure
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_ENUM_CLASS, 'L2VpnLoggingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2VpnLoggingEnum', 
                [], [], 
                '''                MAC Secure Logging
                ''',
                'logging',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pbb-edge-mac-secure',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac',
            False, 
            [
            _MetaInfoClassMember('pbb-edge-mac-aging', REFERENCE_CLASS, 'PbbEdgeMacAging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacAging', 
                [], [], 
                '''                MAC-Aging configuration commands
                ''',
                'pbb_edge_mac_aging',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pbb-edge-mac-learning', REFERENCE_ENUM_CLASS, 'MacLearnEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MacLearnEnum', 
                [], [], 
                '''                Enable Mac Learning
                ''',
                'pbb_edge_mac_learning',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pbb-edge-mac-limit', REFERENCE_CLASS, 'PbbEdgeMacLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacLimit', 
                [], [], 
                '''                MAC-Limit configuration commands
                ''',
                'pbb_edge_mac_limit',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pbb-edge-mac-secure', REFERENCE_CLASS, 'PbbEdgeMacSecure' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacSecure', 
                [], [], 
                '''                MAC Secure
                ''',
                'pbb_edge_mac_secure',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pbb-edge-mac',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge',
            False, 
            [
            _MetaInfoClassMember('isid', ATTRIBUTE, 'int' , None, None, 
                [('256', '16777214')], [], 
                '''                ISID
                ''',
                'isid',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('core-bd-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 27)], [], 
                '''                Core BD Name
                ''',
                'core_bd_name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('pbb-edge-dhcp-profile', REFERENCE_CLASS, 'PbbEdgeDhcpProfile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeDhcpProfile', 
                [], [], 
                '''                Attach a DHCP profile
                ''',
                'pbb_edge_dhcp_profile',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pbb-edge-igmp-profile', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Attach a IGMP Snooping profile
                ''',
                'pbb_edge_igmp_profile',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pbb-edge-mac', REFERENCE_CLASS, 'PbbEdgeMac' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac', 
                [], [], 
                '''                MAC configuration commands
                ''',
                'pbb_edge_mac',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pbb-edge-split-horizon-group', REFERENCE_CLASS, 'PbbEdgeSplitHorizonGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeSplitHorizonGroup', 
                [], [], 
                '''                Split Horizon Group
                ''',
                'pbb_edge_split_horizon_group',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pbb-static-mac-mappings', REFERENCE_CLASS, 'PbbStaticMacMappings' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings', 
                [], [], 
                '''                PBB Static Mac Address Mapping Table
                ''',
                'pbb_static_mac_mappings',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('unknown-unicast-bmac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Configure Unknown Unicast BMAC address
                for PBB Edge Port
                ''',
                'unknown_unicast_bmac',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pbb-edge',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges',
            False, 
            [
            _MetaInfoClassMember('pbb-edge', REFERENCE_LIST, 'PbbEdge' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge', 
                [], [], 
                '''                Configure BD as PBB Edge with ISID and
                associated PBB Core BD
                ''',
                'pbb_edge',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pbb-edges',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacAging' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacAging',
            False, 
            [
            _MetaInfoClassMember('pbb-core-mac-aging-time', ATTRIBUTE, 'int' , None, None, 
                [('300', '30000')], [], 
                '''                Mac Aging Time
                ''',
                'pbb_core_mac_aging_time',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pbb-core-mac-aging-type', REFERENCE_ENUM_CLASS, 'MacAgingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MacAgingEnum', 
                [], [], 
                '''                MAC address aging type
                ''',
                'pbb_core_mac_aging_type',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pbb-core-mac-aging',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacLimit' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacLimit',
            False, 
            [
            _MetaInfoClassMember('pbb-core-mac-limit-action', REFERENCE_ENUM_CLASS, 'MacLimitActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MacLimitActionEnum', 
                [], [], 
                '''                MAC address limit enforcement action
                ''',
                'pbb_core_mac_limit_action',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pbb-core-mac-limit-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of MAC addresses after which MAC
                limit action is taken
                ''',
                'pbb_core_mac_limit_max',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pbb-core-mac-limit-notif', REFERENCE_ENUM_CLASS, 'MacNotificationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MacNotificationEnum', 
                [], [], 
                '''                MAC address limit notification action
                ''',
                'pbb_core_mac_limit_notif',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pbb-core-mac-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac',
            False, 
            [
            _MetaInfoClassMember('pbb-core-mac-aging', REFERENCE_CLASS, 'PbbCoreMacAging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacAging', 
                [], [], 
                '''                MAC-Aging configuration commands
                ''',
                'pbb_core_mac_aging',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pbb-core-mac-learning', REFERENCE_ENUM_CLASS, 'MacLearnEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MacLearnEnum', 
                [], [], 
                '''                Enable Mac Learning
                ''',
                'pbb_core_mac_learning',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pbb-core-mac-limit', REFERENCE_CLASS, 'PbbCoreMacLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacLimit', 
                [], [], 
                '''                MAC-Limit configuration commands
                ''',
                'pbb_core_mac_limit',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pbb-core-mac',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis.PbbCoreEvi' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis.PbbCoreEvi',
            False, 
            [
            _MetaInfoClassMember('eviid', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Ethernet VPN ID
                ''',
                'eviid',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pbb-core-evi',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis',
            False, 
            [
            _MetaInfoClassMember('pbb-core-evi', REFERENCE_LIST, 'PbbCoreEvi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis.PbbCoreEvi', 
                [], [], 
                '''                PBB Core EVI
                ''',
                'pbb_core_evi',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pbb-core-evis',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreDhcpProfile' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreDhcpProfile',
            False, 
            [
            _MetaInfoClassMember('dhcp-snooping-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Disable DHCP snooping
                ''',
                'dhcp_snooping_id',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('profile-id', REFERENCE_ENUM_CLASS, 'InterfaceProfileEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'InterfaceProfileEnum', 
                [], [], 
                '''                Set the snooping profile
                ''',
                'profile_id',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pbb-core-dhcp-profile',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Bridge Domain PBB Core
                Configuration
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pbb-core-dhcp-profile', REFERENCE_CLASS, 'PbbCoreDhcpProfile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreDhcpProfile', 
                [], [], 
                '''                Attach a DHCP profile
                ''',
                'pbb_core_dhcp_profile',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pbb-core-evis', REFERENCE_CLASS, 'PbbCoreEvis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis', 
                [], [], 
                '''                PBB Core EVI Table
                ''',
                'pbb_core_evis',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pbb-core-igmp-profile', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Attach a IGMP Snooping profile
                ''',
                'pbb_core_igmp_profile',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pbb-core-mac', REFERENCE_CLASS, 'PbbCoreMac' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac', 
                [], [], 
                '''                MAC configuration commands
                ''',
                'pbb_core_mac',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pbb-core-mmrp-flood-optimization', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enabling MMRP PBB-VPLS Flood Optimization
                ''',
                'pbb_core_mmrp_flood_optimization',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4094')], [], 
                '''                VLAN ID to push
                ''',
                'vlan_id',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pbb-core',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb',
            False, 
            [
            _MetaInfoClassMember('pbb-core', REFERENCE_CLASS, 'PbbCore' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore', 
                [], [], 
                '''                PBB Core
                ''',
                'pbb_core',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pbb-edges', REFERENCE_CLASS, 'PbbEdges' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges', 
                [], [], 
                '''                PBB Edge
                ''',
                'pbb_edges',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bridge-domain-pbb',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis.BridgeDomainEvi' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis.BridgeDomainEvi',
            False, 
            [
            _MetaInfoClassMember('eviid', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Ethernet VPN ID
                ''',
                'eviid',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bridge-domain-evi',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis',
            False, 
            [
            _MetaInfoClassMember('bridge-domain-evi', REFERENCE_LIST, 'BridgeDomainEvi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis.BridgeDomainEvi', 
                [], [], 
                '''                Bridge Domain EVI
                ''',
                'bridge_domain_evi',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bridge-domain-evis',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses.AccessVfiPseudowireStaticMacAddress' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses.AccessVfiPseudowireStaticMacAddress',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Static MAC address
                ''',
                'address',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'access-vfi-pseudowire-static-mac-address',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses',
            False, 
            [
            _MetaInfoClassMember('access-vfi-pseudowire-static-mac-address', REFERENCE_LIST, 'AccessVfiPseudowireStaticMacAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses.AccessVfiPseudowireStaticMacAddress', 
                [], [], 
                '''                Static Mac Address Configuration
                ''',
                'access_vfi_pseudowire_static_mac_address',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'access-vfi-pseudowire-static-mac-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire',
            False, 
            [
            _MetaInfoClassMember('neighbor', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor IP address
                ''',
                'neighbor',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('pseudowire-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Pseudowire ID
                ''',
                'pseudowire_id',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('access-vfi-pseudowire-static-mac-addresses', REFERENCE_CLASS, 'AccessVfiPseudowireStaticMacAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses', 
                [], [], 
                '''                Static Mac Address Table
                ''',
                'access_vfi_pseudowire_static_mac_addresses',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'access-vfi-pseudowire',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires',
            False, 
            [
            _MetaInfoClassMember('access-vfi-pseudowire', REFERENCE_LIST, 'AccessVfiPseudowire' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire', 
                [], [], 
                '''                Pseudowire configuration
                ''',
                'access_vfi_pseudowire',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'access-vfi-pseudowires',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Name of the AccessVirtual Forwarding
                Interface
                ''',
                'name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('access-vfi-pseudowires', REFERENCE_CLASS, 'AccessVfiPseudowires' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires', 
                [], [], 
                '''                List of pseudowires
                ''',
                'access_vfi_pseudowires',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'access-vfi',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis',
            False, 
            [
            _MetaInfoClassMember('access-vfi', REFERENCE_LIST, 'AccessVfi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi', 
                [], [], 
                '''                Name of the Acess Virtual Forwarding
                Interface
                ''',
                'access_vfi',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'access-vfis',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai.PseudowireDaiAddressValidation' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai.PseudowireDaiAddressValidation',
            False, 
            [
            _MetaInfoClassMember('destination-mac-verification', REFERENCE_ENUM_CLASS, 'L2VpnVerificationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2VpnVerificationEnum', 
                [], [], 
                '''                Destination MAC Verification
                ''',
                'destination_mac_verification',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('ipv4-verification', REFERENCE_ENUM_CLASS, 'L2VpnVerificationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2VpnVerificationEnum', 
                [], [], 
                '''                IPv4 Verification
                ''',
                'ipv4_verification',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('source-mac-verification', REFERENCE_ENUM_CLASS, 'L2VpnVerificationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2VpnVerificationEnum', 
                [], [], 
                '''                Source MAC Verification
                ''',
                'source_mac_verification',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pseudowire-dai-address-validation',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable Dynamic ARP Inspection
                ''',
                'disable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Access Pseudowire Dynamic ARP
                Inspection
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_ENUM_CLASS, 'L2VpnLoggingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2VpnLoggingEnum', 
                [], [], 
                '''                Logging Type
                ''',
                'logging',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pseudowire-dai-address-validation', REFERENCE_CLASS, 'PseudowireDaiAddressValidation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai.PseudowireDaiAddressValidation', 
                [], [], 
                '''                Address Validation
                ''',
                'pseudowire_dai_address_validation',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pseudowire-dai',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType.StormControlUnit' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType.StormControlUnit',
            False, 
            [
            _MetaInfoClassMember('kbits-per-sec', ATTRIBUTE, 'int' , None, None, 
                [('64', '1280000')], [], 
                '''                Kilobits Per Second, PktsPerSec and KbitsPerSec
                cannot be configured together
                ''',
                'kbits_per_sec',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pkts-per-sec', ATTRIBUTE, 'int' , None, None, 
                [('1', '160000')], [], 
                '''                Packets Per Second, PktsPerSec and KbitsPerSec
                cannot be configured together
                ''',
                'pkts_per_sec',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'storm-control-unit',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType',
            False, 
            [
            _MetaInfoClassMember('sctype', REFERENCE_ENUM_CLASS, 'StormControlEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'StormControlEnum', 
                [], [], 
                '''                Storm Control Type
                ''',
                'sctype',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('storm-control-unit', REFERENCE_CLASS, 'StormControlUnit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType.StormControlUnit', 
                [], [], 
                '''                Specify units for Storm Control Configuration
                ''',
                'storm_control_unit',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bdpw-storm-control-type',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes',
            False, 
            [
            _MetaInfoClassMember('bdpw-storm-control-type', REFERENCE_LIST, 'BdpwStormControlType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType', 
                [], [], 
                '''                Storm Control Type
                ''',
                'bdpw_storm_control_type',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bdpw-storm-control-types',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireProfile' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireProfile',
            False, 
            [
            _MetaInfoClassMember('dhcp-snooping-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Disable DHCP snooping
                ''',
                'dhcp_snooping_id',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('profile-id', REFERENCE_ENUM_CLASS, 'InterfaceProfileEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'InterfaceProfileEnum', 
                [], [], 
                '''                Set the snooping profile
                ''',
                'profile_id',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pseudowire-profile',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses.BdPwStaticMacAddress' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses.BdPwStaticMacAddress',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Static MAC address
                ''',
                'address',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bd-pw-static-mac-address',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses',
            False, 
            [
            _MetaInfoClassMember('bd-pw-static-mac-address', REFERENCE_LIST, 'BdPwStaticMacAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses.BdPwStaticMacAddress', 
                [], [], 
                '''                Static Mac Address Configuration
                ''',
                'bd_pw_static_mac_address',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bd-pw-static-mac-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireIpSourceGuard' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireIpSourceGuard',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable Dynamic IP source guard
                ''',
                'disable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable IP Source Guard
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_ENUM_CLASS, 'L2VpnLoggingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2VpnLoggingEnum', 
                [], [], 
                '''                Logging Type
                ''',
                'logging',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pseudowire-ip-source-guard',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacSecure' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacSecure',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'MacSecureActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MacSecureActionEnum', 
                [], [], 
                '''                MAC secure enforcement action
                ''',
                'action',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable L2 Pseudowire MAC Secure
                ''',
                'disable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MAC Secure
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_ENUM_CLASS, 'L2VpnLoggingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2VpnLoggingEnum', 
                [], [], 
                '''                MAC Secure Logging
                ''',
                'logging',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pseudowire-mac-secure',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacAging' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacAging',
            False, 
            [
            _MetaInfoClassMember('pseudowire-mac-aging-time', ATTRIBUTE, 'int' , None, None, 
                [('300', '30000')], [], 
                '''                MAC Aging Time
                ''',
                'pseudowire_mac_aging_time',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pseudowire-mac-aging-type', REFERENCE_ENUM_CLASS, 'MacAgingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MacAgingEnum', 
                [], [], 
                '''                MAC address aging type
                ''',
                'pseudowire_mac_aging_type',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pseudowire-mac-aging',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacLimit' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacLimit',
            False, 
            [
            _MetaInfoClassMember('pseudowire-mac-limit-action', REFERENCE_ENUM_CLASS, 'MacLimitActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MacLimitActionEnum', 
                [], [], 
                '''                Bridge Access Pseudowire MAC address
                limit enforcement action
                ''',
                'pseudowire_mac_limit_action',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pseudowire-mac-limit-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of MAC addresses on a Bridge
                Access Pseudowire after which MAC limit
                action is taken
                ''',
                'pseudowire_mac_limit_max',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pseudowire-mac-limit-notif', REFERENCE_ENUM_CLASS, 'MacNotificationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MacNotificationEnum', 
                [], [], 
                '''                MAC address limit notification action
                in a Bridge Access Pseudowire
                ''',
                'pseudowire_mac_limit_notif',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pseudowire-mac-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Bridge-domain Pseudowire MAC
                configuration mode
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pseudowire-mac-aging', REFERENCE_CLASS, 'PseudowireMacAging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacAging', 
                [], [], 
                '''                MAC-Aging configuration commands
                ''',
                'pseudowire_mac_aging',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pseudowire-mac-learning', REFERENCE_ENUM_CLASS, 'MacLearnEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MacLearnEnum', 
                [], [], 
                '''                Enable MAC Learning
                ''',
                'pseudowire_mac_learning',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pseudowire-mac-limit', REFERENCE_CLASS, 'PseudowireMacLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacLimit', 
                [], [], 
                '''                MAC-Limit configuration commands
                ''',
                'pseudowire_mac_limit',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pseudowire-mac-port-down-flush', REFERENCE_ENUM_CLASS, 'PortDownFlushEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'PortDownFlushEnum', 
                [], [], 
                '''                Enable/Disable MAC Flush When Port goes
                down
                ''',
                'pseudowire_mac_port_down_flush',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pseudowire-mac-secure', REFERENCE_CLASS, 'PseudowireMacSecure' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacSecure', 
                [], [], 
                '''                MAC Secure
                ''',
                'pseudowire_mac_secure',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pseudowire-mac',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon.BdPwSplitHorizonGroup' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon.BdPwSplitHorizonGroup',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable split horizon group
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bd-pw-split-horizon-group',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon',
            False, 
            [
            _MetaInfoClassMember('bd-pw-split-horizon-group', REFERENCE_CLASS, 'BdPwSplitHorizonGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon.BdPwSplitHorizonGroup', 
                [], [], 
                '''                Split Horizon Group
                ''',
                'bd_pw_split_horizon_group',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bd-pw-split-horizon',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwMplsStaticLabels' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwMplsStaticLabels',
            False, 
            [
            _MetaInfoClassMember('local-static-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Pseudowire local static label
                ''',
                'local_static_label',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('remote-static-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Pseudowire remote static label
                ''',
                'remote_static_label',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bd-pw-mpls-static-labels',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires.BridgeDomainBackupPseudowire' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires.BridgeDomainBackupPseudowire',
            False, 
            [
            _MetaInfoClassMember('neighbor', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor IP address
                ''',
                'neighbor',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('pseudowire-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Pseudowire ID
                ''',
                'pseudowire_id',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('bridge-domain-backup-pw-class', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                PW class template name to use for this
                pseudowire
                ''',
                'bridge_domain_backup_pw_class',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bridge-domain-backup-pseudowire',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires',
            False, 
            [
            _MetaInfoClassMember('bridge-domain-backup-pseudowire', REFERENCE_LIST, 'BridgeDomainBackupPseudowire' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires.BridgeDomainBackupPseudowire', 
                [], [], 
                '''                Backup pseudowire configuration
                ''',
                'bridge_domain_backup_pseudowire',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bridge-domain-backup-pseudowires',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire',
            False, 
            [
            _MetaInfoClassMember('neighbor', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor IP address
                ''',
                'neighbor',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('pseudowire-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Pseudowire ID
                ''',
                'pseudowire_id',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('bd-pw-class', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                PW class template name to use for this
                pseudowire
                ''',
                'bd_pw_class',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bd-pw-mpls-static-labels', REFERENCE_CLASS, 'BdPwMplsStaticLabels' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwMplsStaticLabels', 
                [], [], 
                '''                MPLS static labels
                ''',
                'bd_pw_mpls_static_labels',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bd-pw-split-horizon', REFERENCE_CLASS, 'BdPwSplitHorizon' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon', 
                [], [], 
                '''                Split Horizon
                ''',
                'bd_pw_split_horizon',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bd-pw-static-mac-addresses', REFERENCE_CLASS, 'BdPwStaticMacAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses', 
                [], [], 
                '''                Static Mac Address Table
                ''',
                'bd_pw_static_mac_addresses',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bdpw-storm-control-types', REFERENCE_CLASS, 'BdpwStormControlTypes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes', 
                [], [], 
                '''                Storm Control
                ''',
                'bdpw_storm_control_types',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bridge-domain-backup-pseudowires', REFERENCE_CLASS, 'BridgeDomainBackupPseudowires' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires', 
                [], [], 
                '''                List of pseudowires
                ''',
                'bridge_domain_backup_pseudowires',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pseudowire-dai', REFERENCE_CLASS, 'PseudowireDai' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai', 
                [], [], 
                '''                Access Pseudowire Dynamic ARP Inspection
                ''',
                'pseudowire_dai',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pseudowire-flooding', REFERENCE_ENUM_CLASS, 'InterfaceTrafficFloodEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'InterfaceTrafficFloodEnum', 
                [], [], 
                '''                Bridge-domain Pseudowire flooding
                ''',
                'pseudowire_flooding',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pseudowire-flooding-unknown-unicast', REFERENCE_ENUM_CLASS, 'InterfaceTrafficFloodEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'InterfaceTrafficFloodEnum', 
                [], [], 
                '''                Bridge-domain Pseudowire flooding Unknown
                Unicast
                ''',
                'pseudowire_flooding_unknown_unicast',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pseudowire-igmp-snoop', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Attach a IGMP Snooping profile
                ''',
                'pseudowire_igmp_snoop',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pseudowire-ip-source-guard', REFERENCE_CLASS, 'PseudowireIpSourceGuard' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireIpSourceGuard', 
                [], [], 
                '''                IP Source Guard
                ''',
                'pseudowire_ip_source_guard',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pseudowire-mac', REFERENCE_CLASS, 'PseudowireMac' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac', 
                [], [], 
                '''                Bridge-domain Pseudowire MAC
                configuration commands
                ''',
                'pseudowire_mac',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pseudowire-mld-snoop', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Attach a MLD Snooping profile
                ''',
                'pseudowire_mld_snoop',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pseudowire-profile', REFERENCE_CLASS, 'PseudowireProfile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireProfile', 
                [], [], 
                '''                Attach a DHCP profile
                ''',
                'pseudowire_profile',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bd-pseudowire',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires',
            False, 
            [
            _MetaInfoClassMember('bd-pseudowire', REFERENCE_LIST, 'BdPseudowire' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire', 
                [], [], 
                '''                Pseudowire configuration
                ''',
                'bd_pseudowire',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bd-pseudowires',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports.Transport' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports.Transport',
            False, 
            [
            _MetaInfoClassMember('transport-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(RSVP_TE)'], 
                '''                Transport Type
                ''',
                'transport_name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('attribute-set-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Multicast P2MP TE Attribute Set Name
                ''',
                'attribute_set_name',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'transport',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports',
            False, 
            [
            _MetaInfoClassMember('transport', REFERENCE_LIST, 'Transport' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports.Transport', 
                [], [], 
                '''                Multicast P2MP Transport Type
                ''',
                'transport',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'transports',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings.Signaling' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings.Signaling',
            False, 
            [
            _MetaInfoClassMember('signaling-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(BGP)'], 
                '''                Signaling Type
                ''',
                'signaling_name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'signaling',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings',
            False, 
            [
            _MetaInfoClassMember('signaling', REFERENCE_LIST, 'Signaling' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings.Signaling', 
                [], [], 
                '''                Multicast P2MP Signaling Type
                ''',
                'signaling',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'signalings',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Autodiscovery P2MP
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('signalings', REFERENCE_CLASS, 'Signalings' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings', 
                [], [], 
                '''                Multicast P2MP Signaling Type
                ''',
                'signalings',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('transports', REFERENCE_CLASS, 'Transports' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports', 
                [], [], 
                '''                Multicast P2MP Transport
                ''',
                'transports',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'multicast-p2mp',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwDhcpSnoop' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwDhcpSnoop',
            False, 
            [
            _MetaInfoClassMember('dhcp-snooping-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Disable DHCP snooping
                ''',
                'dhcp_snooping_id',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('profile-id', REFERENCE_ENUM_CLASS, 'InterfaceProfileEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'InterfaceProfileEnum', 
                [], [], 
                '''                Set the snooping profile
                ''',
                'profile_id',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'vfi-pw-dhcp-snoop',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwMplsStaticLabels' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwMplsStaticLabels',
            False, 
            [
            _MetaInfoClassMember('local-static-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Pseudowire local static label
                ''',
                'local_static_label',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('remote-static-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Pseudowire remote static label
                ''',
                'remote_static_label',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'vfi-pw-mpls-static-labels',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses.PseudowireStaticMacAddress' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses.PseudowireStaticMacAddress',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Static MAC address
                ''',
                'address',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pseudowire-static-mac-address',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses',
            False, 
            [
            _MetaInfoClassMember('pseudowire-static-mac-address', REFERENCE_LIST, 'PseudowireStaticMacAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses.PseudowireStaticMacAddress', 
                [], [], 
                '''                Static Mac Address Configuration
                ''',
                'pseudowire_static_mac_address',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pseudowire-static-mac-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire',
            False, 
            [
            _MetaInfoClassMember('neighbor', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor IP address
                ''',
                'neighbor',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('pseudowire-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Pseudowire ID
                ''',
                'pseudowire_id',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('pseudowire-static-mac-addresses', REFERENCE_CLASS, 'PseudowireStaticMacAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses', 
                [], [], 
                '''                Static Mac Address Table
                ''',
                'pseudowire_static_mac_addresses',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('vfi-pw-class', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                PW class template name to use for this
                pseudowire
                ''',
                'vfi_pw_class',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('vfi-pw-dhcp-snoop', REFERENCE_CLASS, 'VfiPwDhcpSnoop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwDhcpSnoop', 
                [], [], 
                '''                Attach a DHCP Snooping profile
                ''',
                'vfi_pw_dhcp_snoop',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('vfi-pw-igmp-snoop', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Attach a IGMP Snooping profile
                ''',
                'vfi_pw_igmp_snoop',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('vfi-pw-mld-snoop', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Attach a MLD Snooping profile
                ''',
                'vfi_pw_mld_snoop',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('vfi-pw-mpls-static-labels', REFERENCE_CLASS, 'VfiPwMplsStaticLabels' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwMplsStaticLabels', 
                [], [], 
                '''                MPLS static labels
                ''',
                'vfi_pw_mpls_static_labels',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'vfi-pseudowire',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires',
            False, 
            [
            _MetaInfoClassMember('vfi-pseudowire', REFERENCE_LIST, 'VfiPseudowire' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire', 
                [], [], 
                '''                Pseudowire configuration
                ''',
                'vfi_pseudowire',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'vfi-pseudowires',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.Vplsid' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.Vplsid',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV4 address
                ''',
                'address',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('address-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '32767')], [], 
                '''                Address index
                ''',
                'address_index',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Two byte AS number
                ''',
                'as_',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('as-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS index
                ''',
                'as_index',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'LdpVplsIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'LdpVplsIdEnum', 
                [], [], 
                '''                VPLS-ID Type
                ''',
                'type',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'vplsid',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.FlowLabelLoadBalance' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.FlowLabelLoadBalance',
            False, 
            [
            _MetaInfoClassMember('flow-label', REFERENCE_ENUM_CLASS, 'FlowLabelLoadBalanceEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'FlowLabelLoadBalanceEnum', 
                [], [], 
                '''                Flow Label load balance type
                ''',
                'flow_label',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('static', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Static Flow Label
                ''',
                'static',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'flow-label-load-balance',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable LDP as Signaling Protocol
                .Deletion of this object also causes
                deletion of all objects under
                LDPSignalingProtocol.
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('flow-label-load-balance', REFERENCE_CLASS, 'FlowLabelLoadBalance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.FlowLabelLoadBalance', 
                [], [], 
                '''                Enable Flow Label based load balancing
                ''',
                'flow_label_load_balance',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('vplsid', REFERENCE_CLASS, 'Vplsid' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.Vplsid', 
                [], [], 
                '''                VPLS ID
                ''',
                'vplsid',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'ldp-signaling-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpRoutePolicy' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpRoutePolicy',
            False, 
            [
            _MetaInfoClassMember('export', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Export route policy
                ''',
                'export',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bgp-route-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteDistinguisher' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteDistinguisher',
            False, 
            [
            _MetaInfoClassMember('addr-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Addr index
                ''',
                'addr_index',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV4 address
                ''',
                'address',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Two byte or 4 byte AS number
                ''',
                'as_',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('as-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS:nn (hex or decimal format)
                ''',
                'as_index',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BgpRouteDistinguisherEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'BgpRouteDistinguisherEnum', 
                [], [], 
                '''                Router Distinguisher Type
                ''',
                'type',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'route-distinguisher',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol.FlowLabelLoadBalance' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol.FlowLabelLoadBalance',
            False, 
            [
            _MetaInfoClassMember('flow-label', REFERENCE_ENUM_CLASS, 'FlowLabelLoadBalanceEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'FlowLabelLoadBalanceEnum', 
                [], [], 
                '''                Flow Label load balance type
                ''',
                'flow_label',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('static', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Static Flow Label
                ''',
                'static',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'flow-label-load-balance',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable BGP as Signaling Protocol
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('flow-label-load-balance', REFERENCE_CLASS, 'FlowLabelLoadBalance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol.FlowLabelLoadBalance', 
                [], [], 
                '''                Enable Flow Label based load balancing
                ''',
                'flow_label_load_balance',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('ve-range', ATTRIBUTE, 'int' , None, None, 
                [('11', '100')], [], 
                '''                Local Virtual Edge Block Configurable
                Range
                ''',
                've_range',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('veid', ATTRIBUTE, 'int' , None, None, 
                [('1', '16384')], [], 
                '''                Local Virtual Edge Identifier
                ''',
                'veid',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bgp-signaling-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.TwoByteAsOrFourByteAs' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.TwoByteAsOrFourByteAs',
            False, 
            [
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Two byte or 4 byte AS number
                ''',
                'as_',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('as-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS:nn (hex or decimal format)
                ''',
                'as_index',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'two-byte-as-or-four-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.Ipv4Address' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.Ipv4Address',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV4 address
                ''',
                'address',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('addr-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Addr index
                ''',
                'addr_index',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'ipv4-address',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget',
            False, 
            [
            _MetaInfoClassMember('role', REFERENCE_ENUM_CLASS, 'BgpRouteTargetRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'BgpRouteTargetRoleEnum', 
                [], [], 
                '''                Role of the router target type
                ''',
                'role',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('format', REFERENCE_ENUM_CLASS, 'BgpRouteTargetFormatEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'BgpRouteTargetFormatEnum', 
                [], [], 
                '''                Format of the route target
                ''',
                'format',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('ipv4-address', REFERENCE_LIST, 'Ipv4Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.Ipv4Address', 
                [], [], 
                '''                ipv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('two-byte-as-or-four-byte-as', REFERENCE_LIST, 'TwoByteAsOrFourByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.TwoByteAsOrFourByteAs', 
                [], [], 
                '''                two byte as or four byte as
                ''',
                'two_byte_as_or_four_byte_as',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'route-target',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets',
            False, 
            [
            _MetaInfoClassMember('route-target', REFERENCE_LIST, 'RouteTarget' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget', 
                [], [], 
                '''                Name of the Route Target
                ''',
                'route_target',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'route-targets',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery',
            False, 
            [
            _MetaInfoClassMember('ad-control-word', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable control-word for this VFI
                ''',
                'ad_control_word',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bgp-route-policy', REFERENCE_CLASS, 'BgpRoutePolicy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpRoutePolicy', 
                [], [], 
                '''                Route policy
                ''',
                'bgp_route_policy',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bgp-signaling-protocol', REFERENCE_CLASS, 'BgpSignalingProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol', 
                [], [], 
                '''                Enable Signaling Protocol BGP in this
                VFI
                ''',
                'bgp_signaling_protocol',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Autodiscovery BGP
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('ldp-signaling-protocol', REFERENCE_CLASS, 'LdpSignalingProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol', 
                [], [], 
                '''                Signaling Protocol LDP in this VFI
                configuration
                ''',
                'ldp_signaling_protocol',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('route-distinguisher', REFERENCE_CLASS, 'RouteDistinguisher' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteDistinguisher', 
                [], [], 
                '''                Route Distinguisher
                ''',
                'route_distinguisher',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('route-targets', REFERENCE_CLASS, 'RouteTargets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets', 
                [], [], 
                '''                Route Target
                ''',
                'route_targets',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('table-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Table Policy for installation of
                forwarding data to L2FIB
                ''',
                'table_policy',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bgp-auto-discovery',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Name of the Virtual Forwarding Interface
                ''',
                'name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('bgp-auto-discovery', REFERENCE_CLASS, 'BgpAutoDiscovery' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery', 
                [], [], 
                '''                Enable Autodiscovery BGP in this VFI
                ''',
                'bgp_auto_discovery',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('multicast-p2mp', REFERENCE_CLASS, 'MulticastP2Mp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp', 
                [], [], 
                '''                Enable Multicast P2MP in this VFI
                ''',
                'multicast_p2mp',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('vfi-pseudowires', REFERENCE_CLASS, 'VfiPseudowires' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires', 
                [], [], 
                '''                List of pseudowires
                ''',
                'vfi_pseudowires',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('vfi-shutdown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enabling Shutdown
                ''',
                'vfi_shutdown',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('vpnid', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                VPN Identifier
                ''',
                'vpnid',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'vfi',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis',
            False, 
            [
            _MetaInfoClassMember('vfi', REFERENCE_LIST, 'Vfi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi', 
                [], [], 
                '''                Name of the Virtual Forwarding Interface
                ''',
                'vfi',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'vfis',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceIpSourceGuard' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceIpSourceGuard',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable L2 Interface Dynamic IP source
                guard
                ''',
                'disable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable IP Source Guard
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_ENUM_CLASS, 'L2VpnLoggingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2VpnLoggingEnum', 
                [], [], 
                '''                Logging Type
                ''',
                'logging',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'interface-ip-source-guard',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai.InterfaceDaiAddressValidation' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai.InterfaceDaiAddressValidation',
            False, 
            [
            _MetaInfoClassMember('destination-mac-verification', REFERENCE_ENUM_CLASS, 'L2VpnVerificationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2VpnVerificationEnum', 
                [], [], 
                '''                Destination MAC Verification
                ''',
                'destination_mac_verification',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Address Validation
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('ipv4-verification', REFERENCE_ENUM_CLASS, 'L2VpnVerificationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2VpnVerificationEnum', 
                [], [], 
                '''                IPv4 Verification
                ''',
                'ipv4_verification',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('source-mac-verification', REFERENCE_ENUM_CLASS, 'L2VpnVerificationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2VpnVerificationEnum', 
                [], [], 
                '''                Source MAC Verification
                ''',
                'source_mac_verification',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'interface-dai-address-validation',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable L2 Interface Dynamic ARP
                Inspection
                ''',
                'disable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable L2 Interface Dynamic ARP
                Inspection
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('interface-dai-address-validation', REFERENCE_CLASS, 'InterfaceDaiAddressValidation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai.InterfaceDaiAddressValidation', 
                [], [], 
                '''                Address Validation
                ''',
                'interface_dai_address_validation',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_ENUM_CLASS, 'L2VpnLoggingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2VpnLoggingEnum', 
                [], [], 
                '''                Logging Type
                ''',
                'logging',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'interface-dai',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceProfile' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceProfile',
            False, 
            [
            _MetaInfoClassMember('dhcp-snooping-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Disable DHCP snooping
                ''',
                'dhcp_snooping_id',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('profile-id', REFERENCE_ENUM_CLASS, 'InterfaceProfileEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'InterfaceProfileEnum', 
                [], [], 
                '''                Set the snooping profile
                ''',
                'profile_id',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'interface-profile',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType.StormControlUnit' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType.StormControlUnit',
            False, 
            [
            _MetaInfoClassMember('kbits-per-sec', ATTRIBUTE, 'int' , None, None, 
                [('64', '1280000')], [], 
                '''                Kilobits Per Second, PktsPerSec and KbitsPerSec
                cannot be configured together
                ''',
                'kbits_per_sec',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pkts-per-sec', ATTRIBUTE, 'int' , None, None, 
                [('1', '160000')], [], 
                '''                Packets Per Second, PktsPerSec and KbitsPerSec
                cannot be configured together
                ''',
                'pkts_per_sec',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'storm-control-unit',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType',
            False, 
            [
            _MetaInfoClassMember('sctype', REFERENCE_ENUM_CLASS, 'StormControlEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'StormControlEnum', 
                [], [], 
                '''                Storm Control Type
                ''',
                'sctype',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('storm-control-unit', REFERENCE_CLASS, 'StormControlUnit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType.StormControlUnit', 
                [], [], 
                '''                Specify units for Storm Control Configuration
                ''',
                'storm_control_unit',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bdac-storm-control-type',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes',
            False, 
            [
            _MetaInfoClassMember('bdac-storm-control-type', REFERENCE_LIST, 'BdacStormControlType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType', 
                [], [], 
                '''                Storm Control Type
                ''',
                'bdac_storm_control_type',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bdac-storm-control-types',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon.SplitHorizonGroupId' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon.SplitHorizonGroupId',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable split horizon group
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'split-horizon-group-id',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon',
            False, 
            [
            _MetaInfoClassMember('split-horizon-group-id', REFERENCE_CLASS, 'SplitHorizonGroupId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon.SplitHorizonGroupId', 
                [], [], 
                '''                Split Horizon Group ID
                ''',
                'split_horizon_group_id',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'split-horizon',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses.StaticMacAddress' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses.StaticMacAddress',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Static MAC address
                ''',
                'address',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'static-mac-address',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses',
            False, 
            [
            _MetaInfoClassMember('static-mac-address', REFERENCE_LIST, 'StaticMacAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses.StaticMacAddress', 
                [], [], 
                '''                Static Mac Address Configuration
                ''',
                'static_mac_address',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'static-mac-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacAging' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacAging',
            False, 
            [
            _MetaInfoClassMember('interface-mac-aging-time', ATTRIBUTE, 'int' , None, None, 
                [('300', '30000')], [], 
                '''                Mac Aging Time
                ''',
                'interface_mac_aging_time',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('interface-mac-aging-type', REFERENCE_ENUM_CLASS, 'MacAgingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MacAgingEnum', 
                [], [], 
                '''                MAC address aging type
                ''',
                'interface_mac_aging_type',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'interface-mac-aging',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacSecure' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacSecure',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'MacSecureActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MacSecureActionEnum', 
                [], [], 
                '''                MAC secure enforcement action
                ''',
                'action',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable L2 Interface MAC Secure
                ''',
                'disable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MAC Secure
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_ENUM_CLASS, 'L2VpnLoggingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2VpnLoggingEnum', 
                [], [], 
                '''                MAC Secure Logging
                ''',
                'logging',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'interface-mac-secure',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacLimit' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacLimit',
            False, 
            [
            _MetaInfoClassMember('interface-mac-limit-action', REFERENCE_ENUM_CLASS, 'MacLimitActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MacLimitActionEnum', 
                [], [], 
                '''                Interface MAC address limit enforcement
                action
                ''',
                'interface_mac_limit_action',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('interface-mac-limit-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of MAC addresses on an Interface
                after which MAC limit action is taken
                ''',
                'interface_mac_limit_max',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('interface-mac-limit-notif', REFERENCE_ENUM_CLASS, 'MacNotificationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MacNotificationEnum', 
                [], [], 
                '''                MAC address limit notification action
                in a Interface
                ''',
                'interface_mac_limit_notif',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'interface-mac-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac',
            False, 
            [
            _MetaInfoClassMember('interface-mac-aging', REFERENCE_CLASS, 'InterfaceMacAging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacAging', 
                [], [], 
                '''                MAC-Aging configuration commands
                ''',
                'interface_mac_aging',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('interface-mac-learning', REFERENCE_ENUM_CLASS, 'MacLearnEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MacLearnEnum', 
                [], [], 
                '''                Enable Mac Learning
                ''',
                'interface_mac_learning',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('interface-mac-limit', REFERENCE_CLASS, 'InterfaceMacLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacLimit', 
                [], [], 
                '''                MAC-Limit configuration commands
                ''',
                'interface_mac_limit',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('interface-mac-port-down-flush', REFERENCE_ENUM_CLASS, 'PortDownFlushEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'PortDownFlushEnum', 
                [], [], 
                '''                Enable/Disable MAC Flush When Port goes
                down
                ''',
                'interface_mac_port_down_flush',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('interface-mac-secure', REFERENCE_CLASS, 'InterfaceMacSecure' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacSecure', 
                [], [], 
                '''                MAC Secure
                ''',
                'interface_mac_secure',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'interface-mac',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the Attachment Circuit
                ''',
                'name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('bdac-storm-control-types', REFERENCE_CLASS, 'BdacStormControlTypes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes', 
                [], [], 
                '''                Storm Control
                ''',
                'bdac_storm_control_types',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('interface-dai', REFERENCE_CLASS, 'InterfaceDai' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai', 
                [], [], 
                '''                L2 Interface Dynamic ARP Inspection
                ''',
                'interface_dai',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('interface-flooding', REFERENCE_ENUM_CLASS, 'InterfaceTrafficFloodEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'InterfaceTrafficFloodEnum', 
                [], [], 
                '''                Enable or Disable Flooding
                ''',
                'interface_flooding',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('interface-flooding-unknown-unicast', REFERENCE_ENUM_CLASS, 'InterfaceTrafficFloodEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'InterfaceTrafficFloodEnum', 
                [], [], 
                '''                Enable or Disable Unknown Unicast
                Flooding
                ''',
                'interface_flooding_unknown_unicast',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('interface-igmp-snoop', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Attach a IGMP Snooping profile
                ''',
                'interface_igmp_snoop',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('interface-ip-source-guard', REFERENCE_CLASS, 'InterfaceIpSourceGuard' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceIpSourceGuard', 
                [], [], 
                '''                IP Source Guard
                ''',
                'interface_ip_source_guard',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('interface-mac', REFERENCE_CLASS, 'InterfaceMac' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac', 
                [], [], 
                '''                MAC configuration commands
                ''',
                'interface_mac',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('interface-mld-snoop', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Attach a MLD Snooping profile
                ''',
                'interface_mld_snoop',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('interface-profile', REFERENCE_CLASS, 'InterfaceProfile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceProfile', 
                [], [], 
                '''                Attach a DHCP profile
                ''',
                'interface_profile',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('split-horizon', REFERENCE_CLASS, 'SplitHorizon' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon', 
                [], [], 
                '''                Split Horizon
                ''',
                'split_horizon',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('static-mac-addresses', REFERENCE_CLASS, 'StaticMacAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses', 
                [], [], 
                '''                Static Mac Address Table
                ''',
                'static_mac_addresses',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bd-attachment-circuit',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits',
            False, 
            [
            _MetaInfoClassMember('bd-attachment-circuit', REFERENCE_LIST, 'BdAttachmentCircuit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit', 
                [], [], 
                '''                Name of the Attachment Circuit
                ''',
                'bd_attachment_circuit',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bd-attachment-circuits',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns.BdPseudowireEvpn' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns.BdPseudowireEvpn',
            False, 
            [
            _MetaInfoClassMember('eviid', ATTRIBUTE, 'int' , None, None, 
                [('1', '65534')], [], 
                '''                Ethernet VPN ID
                ''',
                'eviid',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('acid', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                AC ID
                ''',
                'acid',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bd-pseudowire-evpn',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns',
            False, 
            [
            _MetaInfoClassMember('bd-pseudowire-evpn', REFERENCE_LIST, 'BdPseudowireEvpn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns.BdPseudowireEvpn', 
                [], [], 
                '''                EVPN Pseudowire configuration
                ''',
                'bd_pseudowire_evpn',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bd-pseudowire-evpns',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.IpSourceGuard' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.IpSourceGuard',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable IP Source Guard
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('logging', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Logging
                ''',
                'logging',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'ip-source-guard',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai.DaiAddressValidation' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai.DaiAddressValidation',
            False, 
            [
            _MetaInfoClassMember('destination-mac-verification', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Destination MAC Verification
                ''',
                'destination_mac_verification',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Address Validation
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('ipv4-verification', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable IPv4 Verification
                ''',
                'ipv4_verification',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('source-mac-verification', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Source MAC Verification
                ''',
                'source_mac_verification',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'dai-address-validation',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai',
            False, 
            [
            _MetaInfoClassMember('dai-address-validation', REFERENCE_CLASS, 'DaiAddressValidation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai.DaiAddressValidation', 
                [], [], 
                '''                Address Validation
                ''',
                'dai_address_validation',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Dynamic ARP Inspection
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('logging', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Logging
                ''',
                'logging',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'dai',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface.RoutedInterfaceSplitHorizonGroup' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface.RoutedInterfaceSplitHorizonGroup',
            False, 
            [
            _MetaInfoClassMember('routed-interface-split-horizon-group-core', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure BVI under SHG 1
                ''',
                'routed_interface_split_horizon_group_core',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'routed-interface-split-horizon-group',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the Routed Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('routed-interface-split-horizon-group', REFERENCE_CLASS, 'RoutedInterfaceSplitHorizonGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface.RoutedInterfaceSplitHorizonGroup', 
                [], [], 
                '''                Routed interface split horizon group
                ''',
                'routed_interface_split_horizon_group',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'routed-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces',
            False, 
            [
            _MetaInfoClassMember('routed-interface', REFERENCE_LIST, 'RoutedInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface', 
                [], [], 
                '''                Bridge Domain Routed Interface
                ''',
                'routed_interface',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'routed-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 27)], [], 
                '''                Name of the bridge domain
                ''',
                'name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('access-vfis', REFERENCE_CLASS, 'AccessVfis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis', 
                [], [], 
                '''                Specify the access virtual forwarding
                interface name
                ''',
                'access_vfis',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bd-attachment-circuits', REFERENCE_CLASS, 'BdAttachmentCircuits' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits', 
                [], [], 
                '''                Attachment Circuit table
                ''',
                'bd_attachment_circuits',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bd-pseudowire-evpns', REFERENCE_CLASS, 'BdPseudowireEvpns' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns', 
                [], [], 
                '''                List of EVPN pseudowires
                ''',
                'bd_pseudowire_evpns',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bd-pseudowires', REFERENCE_CLASS, 'BdPseudowires' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires', 
                [], [], 
                '''                List of pseudowires
                ''',
                'bd_pseudowires',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bd-storm-controls', REFERENCE_CLASS, 'BdStormControls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls', 
                [], [], 
                '''                Storm Control
                ''',
                'bd_storm_controls',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bridge-description', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Bridge-domain description Name
                ''',
                'bridge_description',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bridge-domain-evis', REFERENCE_CLASS, 'BridgeDomainEvis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis', 
                [], [], 
                '''                Bridge Domain EVI Table
                ''',
                'bridge_domain_evis',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bridge-domain-mac', REFERENCE_CLASS, 'BridgeDomainMac' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac', 
                [], [], 
                '''                MAC configuration commands
                ''',
                'bridge_domain_mac',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bridge-domain-mtu', ATTRIBUTE, 'int' , None, None, 
                [('46', '65535')], [], 
                '''                Maximum transmission unit for this Bridge
                Domain
                ''',
                'bridge_domain_mtu',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bridge-domain-pbb', REFERENCE_CLASS, 'BridgeDomainPbb' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb', 
                [], [], 
                '''                Bridge Domain PBB
                ''',
                'bridge_domain_pbb',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('coupled-mode', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Coupled-mode configuration
                ''',
                'coupled_mode',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('dai', REFERENCE_CLASS, 'Dai' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai', 
                [], [], 
                '''                Dynamic ARP Inspection
                ''',
                'dai',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('dhcp', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                DHCPv4 Snooping profile name
                ''',
                'dhcp',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('flooding', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable flooding
                ''',
                'flooding',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('flooding-unknown-unicast', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable Unknown Unicast flooding
                ''',
                'flooding_unknown_unicast',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('igmp-snooping', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Attach IGMP Snooping Profile Name
                ''',
                'igmp_snooping',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('igmp-snooping-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable IGMP Snooping
                ''',
                'igmp_snooping_disable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('ip-source-guard', REFERENCE_CLASS, 'IpSourceGuard' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.IpSourceGuard', 
                [], [], 
                '''                IP Source Guard
                ''',
                'ip_source_guard',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('member-vnis', REFERENCE_CLASS, 'MemberVnis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis', 
                [], [], 
                '''                Bridge Domain VxLAN Network Identifier
                Table
                ''',
                'member_vnis',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('mld-snooping', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Attach MLD Snooping Profile Name
                ''',
                'mld_snooping',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('nv-satellite', REFERENCE_CLASS, 'NvSatellite' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.NvSatellite', 
                [], [], 
                '''                nV Satellite
                ''',
                'nv_satellite',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('routed-interfaces', REFERENCE_CLASS, 'RoutedInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces', 
                [], [], 
                '''                Bridge Domain Routed Interface Table
                ''',
                'routed_interfaces',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('shutdown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                shutdown the Bridge Domain
                ''',
                'shutdown',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('transport-mode', REFERENCE_ENUM_CLASS, 'BridgeDomainTransportModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'BridgeDomainTransportModeEnum', 
                [], [], 
                '''                Bridge Domain Transport mode
                ''',
                'transport_mode',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('vfis', REFERENCE_CLASS, 'Vfis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis', 
                [], [], 
                '''                Specify the virtual forwarding interface
                name
                ''',
                'vfis',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bridge-domain',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains',
            False, 
            [
            _MetaInfoClassMember('bridge-domain', REFERENCE_LIST, 'BridgeDomain' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain', 
                [], [], 
                '''                bridge domain
                ''',
                'bridge_domain',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bridge-domains',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Name of the Bridge group
                ''',
                'name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('bridge-domains', REFERENCE_CLASS, 'BridgeDomains' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains', 
                [], [], 
                '''                List of Bridge Domain
                ''',
                'bridge_domains',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bridge-domain-group',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.BridgeDomainGroups' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.BridgeDomainGroups',
            False, 
            [
            _MetaInfoClassMember('bridge-domain-group', REFERENCE_LIST, 'BridgeDomainGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup', 
                [], [], 
                '''                Bridge group
                ''',
                'bridge_domain_group',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bridge-domain-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.Sequencing' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.Sequencing',
            False, 
            [
            _MetaInfoClassMember('resync-threshold', ATTRIBUTE, 'int' , None, None, 
                [('5', '65535')], [], 
                '''                Out of sequence threshold
                ''',
                'resync_threshold',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('sequencing', REFERENCE_ENUM_CLASS, 'L2Tpv3SequencingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Tpv3SequencingEnum', 
                [], [], 
                '''                Sequencing
                ''',
                'sequencing',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'sequencing',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.TypeOfService' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.TypeOfService',
            False, 
            [
            _MetaInfoClassMember('type-of-service-mode', REFERENCE_ENUM_CLASS, 'TypeOfServiceModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'TypeOfServiceModeEnum', 
                [], [], 
                '''                Type of service mode
                ''',
                'type_of_service_mode',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('type-of-service-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Type of service value
                ''',
                'type_of_service_value',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'type-of-service',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.SignalingProtocol' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.SignalingProtocol',
            False, 
            [
            _MetaInfoClassMember('l2tpv3-class-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Name of the L2TPv3 class name
                ''',
                'l2tpv3_class_name',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('protocol', REFERENCE_ENUM_CLASS, 'L2TpSignalingProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2TpSignalingProtocolEnum', 
                [], [], 
                '''                L2TPv3 signaling protocol
                ''',
                'protocol',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'signaling-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.PathMtu' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.PathMtu',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable path MTU
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('max-path-mtu', ATTRIBUTE, 'int' , None, None, 
                [('68', '65535')], [], 
                '''                Maximum path maximum transmission unit
                ''',
                'max_path_mtu',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'path-mtu',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation',
            False, 
            [
            _MetaInfoClassMember('cookie-size', REFERENCE_ENUM_CLASS, 'L2TpCookieSizeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2TpCookieSizeEnum', 
                [], [], 
                '''                Cookie size
                ''',
                'cookie_size',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('df-bit-set', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Set the do not fragment bit to 1
                ''',
                'df_bit_set',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable L2TPv3 encapsulation
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('path-mtu', REFERENCE_CLASS, 'PathMtu' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.PathMtu', 
                [], [], 
                '''                Path maximum transmission unit
                ''',
                'path_mtu',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('sequencing', REFERENCE_CLASS, 'Sequencing' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.Sequencing', 
                [], [], 
                '''                Sequencing
                ''',
                'sequencing',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('signaling-protocol', REFERENCE_CLASS, 'SignalingProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.SignalingProtocol', 
                [], [], 
                '''                L2TPv3 signaling protocol
                ''',
                'signaling_protocol',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source IP address
                ''',
                'source_address',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('time-to-live', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Time to live
                ''',
                'time_to_live',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('transport-mode', REFERENCE_ENUM_CLASS, 'TransportModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'TransportModeEnum', 
                [], [], 
                '''                Transport mode
                ''',
                'transport_mode',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('type-of-service', REFERENCE_CLASS, 'TypeOfService' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.TypeOfService', 
                [], [], 
                '''                Type of service
                ''',
                'type_of_service',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'l2tpv3-encapsulation',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.PseudowireClasses.PseudowireClass.BackupDisableDelay' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.PseudowireClasses.PseudowireClass.BackupDisableDelay',
            False, 
            [
            _MetaInfoClassMember('disable-backup', ATTRIBUTE, 'int' , None, None, 
                [('0', '180')], [], 
                '''                Disable backup delay
                ''',
                'disable_backup',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BackupDisableEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'BackupDisableEnum', 
                [], [], 
                '''                Delay or Never
                ''',
                'type',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'backup-disable-delay',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.Sequencing' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.Sequencing',
            False, 
            [
            _MetaInfoClassMember('resync-threshold', ATTRIBUTE, 'int' , None, None, 
                [('5', '65535')], [], 
                '''                Out of sequence threshold
                ''',
                'resync_threshold',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('sequencing', REFERENCE_ENUM_CLASS, 'MplsSequencingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MplsSequencingEnum', 
                [], [], 
                '''                Sequencing
                ''',
                'sequencing',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'sequencing',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.MplsRedundancy' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.MplsRedundancy',
            False, 
            [
            _MetaInfoClassMember('redundancy-initial-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '120')], [], 
                '''                Initial delay before activating the
                redundant PW, in seconds
                ''',
                'redundancy_initial_delay',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('redundancy-one-way', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Force one-way PW redundancy behavior in
                Redundancy Group
                ''',
                'redundancy_one_way',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'mpls-redundancy',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.PreferredPath' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.PreferredPath',
            False, 
            [
            _MetaInfoClassMember('fallback-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Fallback disable
                ''',
                'fallback_disable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('interface-tunnel-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Interface Tunnel number for preferred path
                ''',
                'interface_tunnel_number',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'PreferredPathEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'PreferredPathEnum', 
                [], [], 
                '''                Preferred Path Type
                ''',
                'type',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'preferred-path',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup.FlowLabelLoadBalance' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup.FlowLabelLoadBalance',
            False, 
            [
            _MetaInfoClassMember('flow-label', REFERENCE_ENUM_CLASS, 'FlowLabelLoadBalanceEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'FlowLabelLoadBalanceEnum', 
                [], [], 
                '''                Flow Label load balance type
                ''',
                'flow_label',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('static', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Static Flow Label
                ''',
                'static',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'flow-label-load-balance',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup',
            False, 
            [
            _MetaInfoClassMember('flow-label-load-balance', REFERENCE_CLASS, 'FlowLabelLoadBalance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup.FlowLabelLoadBalance', 
                [], [], 
                '''                Enable Flow Label based load balancing
                ''',
                'flow_label_load_balance',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('flow-label-load-balance-code', REFERENCE_ENUM_CLASS, 'FlowLabelTlvCodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'FlowLabelTlvCodeEnum', 
                [], [], 
                '''                Enable Legacy Flow Label TLV code
                ''',
                'flow_label_load_balance_code',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pw-label-load-balance', REFERENCE_ENUM_CLASS, 'LoadBalanceEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'LoadBalanceEnum', 
                [], [], 
                '''                Enable PW Label based Load Balancing
                ''',
                'pw_label_load_balance',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'load-balance-group',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation',
            False, 
            [
            _MetaInfoClassMember('control-word', REFERENCE_ENUM_CLASS, 'ControlWordEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'ControlWordEnum', 
                [], [], 
                '''                Enable control word
                ''',
                'control_word',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS encapsulation
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('load-balance-group', REFERENCE_CLASS, 'LoadBalanceGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup', 
                [], [], 
                '''                Load Balancing
                ''',
                'load_balance_group',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('mpls-redundancy', REFERENCE_CLASS, 'MplsRedundancy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.MplsRedundancy', 
                [], [], 
                '''                Redundancy options for MPLS encapsulation
                ''',
                'mpls_redundancy',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('preferred-path', REFERENCE_CLASS, 'PreferredPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.PreferredPath', 
                [], [], 
                '''                Preferred path
                ''',
                'preferred_path',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pw-switching-tlv', REFERENCE_ENUM_CLASS, 'PwSwitchingPointTlvEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'PwSwitchingPointTlvEnum', 
                [], [], 
                '''                Pseudowire Switching Point Tlv
                ''',
                'pw_switching_tlv',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('sequencing', REFERENCE_CLASS, 'Sequencing' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.Sequencing', 
                [], [], 
                '''                Sequencing
                ''',
                'sequencing',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('signaling-protocol', REFERENCE_ENUM_CLASS, 'MplsSignalingProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'MplsSignalingProtocolEnum', 
                [], [], 
                '''                MPLS signaling protocol
                ''',
                'signaling_protocol',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source IP address
                ''',
                'source_address',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('static-tag-rewrite', ATTRIBUTE, 'int' , None, None, 
                [('1', '4094')], [], 
                '''                Static Tag rewrite
                ''',
                'static_tag_rewrite',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('transport-mode', REFERENCE_ENUM_CLASS, 'TransportModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'TransportModeEnum', 
                [], [], 
                '''                Transport mode
                ''',
                'transport_mode',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('vccv-type', REFERENCE_ENUM_CLASS, 'VccvVerificationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'VccvVerificationEnum', 
                [], [], 
                '''                VCCV verification type
                ''',
                'vccv_type',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'mpls-encapsulation',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.PseudowireClasses.PseudowireClass' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.PseudowireClasses.PseudowireClass',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Name of the pseudowire class
                ''',
                'name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('backup-disable-delay', REFERENCE_CLASS, 'BackupDisableDelay' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.PseudowireClasses.PseudowireClass.BackupDisableDelay', 
                [], [], 
                '''                Back Up Pseudowire class
                ''',
                'backup_disable_delay',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable pseudowire class
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('l2tpv3-encapsulation', REFERENCE_CLASS, 'L2Tpv3Encapsulation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation', 
                [], [], 
                '''                L2TPv3 encapsulation
                ''',
                'l2tpv3_encapsulation',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('mac-withdraw', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable backup MAC withdraw
                ''',
                'mac_withdraw',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('mpls-encapsulation', REFERENCE_CLASS, 'MplsEncapsulation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation', 
                [], [], 
                '''                MPLS encapsulation
                ''',
                'mpls_encapsulation',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pseudowire-class',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.PseudowireClasses' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.PseudowireClasses',
            False, 
            [
            _MetaInfoClassMember('pseudowire-class', REFERENCE_LIST, 'PseudowireClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.PseudowireClasses.PseudowireClass', 
                [], [], 
                '''                Pseudowire class
                ''',
                'pseudowire_class',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pseudowire-classes',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits.VlanUnawareFxcAttachmentCircuit' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits.VlanUnawareFxcAttachmentCircuit',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of the attachment circuit interface
                ''',
                'name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'vlan-unaware-fxc-attachment-circuit',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits',
            False, 
            [
            _MetaInfoClassMember('vlan-unaware-fxc-attachment-circuit', REFERENCE_LIST, 'VlanUnawareFxcAttachmentCircuit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits.VlanUnawareFxcAttachmentCircuit', 
                [], [], 
                '''                Attachment circuit interface
                ''',
                'vlan_unaware_fxc_attachment_circuit',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'vlan-unaware-fxc-attachment-circuits',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns.VlanUnawareFxcPseudowireEvpn' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns.VlanUnawareFxcPseudowireEvpn',
            False, 
            [
            _MetaInfoClassMember('eviid', ATTRIBUTE, 'int' , None, None, 
                [('1', '65534')], [], 
                '''                Ethernet VPN ID
                ''',
                'eviid',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('acid', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                AC ID
                ''',
                'acid',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'vlan-unaware-fxc-pseudowire-evpn',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns',
            False, 
            [
            _MetaInfoClassMember('vlan-unaware-fxc-pseudowire-evpn', REFERENCE_LIST, 'VlanUnawareFxcPseudowireEvpn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns.VlanUnawareFxcPseudowireEvpn', 
                [], [], 
                '''                EVPN FXC Service Configuration
                ''',
                'vlan_unaware_fxc_pseudowire_evpn',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'vlan-unaware-fxc-pseudowire-evpns',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 23)], [], 
                '''                Name of the Flexible XConnect Service
                ''',
                'name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('vlan-unaware-fxc-attachment-circuits', REFERENCE_CLASS, 'VlanUnawareFxcAttachmentCircuits' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits', 
                [], [], 
                '''                List of attachment circuits
                ''',
                'vlan_unaware_fxc_attachment_circuits',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('vlan-unaware-fxc-pseudowire-evpns', REFERENCE_CLASS, 'VlanUnawareFxcPseudowireEvpns' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns', 
                [], [], 
                '''                List of EVPN Services
                ''',
                'vlan_unaware_fxc_pseudowire_evpns',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'vlan-unaware-flexible-xconnect-service',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices',
            False, 
            [
            _MetaInfoClassMember('vlan-unaware-flexible-xconnect-service', REFERENCE_LIST, 'VlanUnawareFlexibleXconnectService' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService', 
                [], [], 
                '''                Flexible XConnect Service
                ''',
                'vlan_unaware_flexible_xconnect_service',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'vlan-unaware-flexible-xconnect-services',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits.VlanAwareFxcAttachmentCircuit' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits.VlanAwareFxcAttachmentCircuit',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of the attachment circuit interface
                ''',
                'name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'vlan-aware-fxc-attachment-circuit',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits',
            False, 
            [
            _MetaInfoClassMember('vlan-aware-fxc-attachment-circuit', REFERENCE_LIST, 'VlanAwareFxcAttachmentCircuit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits.VlanAwareFxcAttachmentCircuit', 
                [], [], 
                '''                Attachment circuit interface
                ''',
                'vlan_aware_fxc_attachment_circuit',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'vlan-aware-fxc-attachment-circuits',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService',
            False, 
            [
            _MetaInfoClassMember('eviid', ATTRIBUTE, 'int' , None, None, 
                [('1', '65534')], [], 
                '''                Ethernet VPN ID
                ''',
                'eviid',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('vlan-aware-fxc-attachment-circuits', REFERENCE_CLASS, 'VlanAwareFxcAttachmentCircuits' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits', 
                [], [], 
                '''                List of attachment circuits
                ''',
                'vlan_aware_fxc_attachment_circuits',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'vlan-aware-flexible-xconnect-service',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices',
            False, 
            [
            _MetaInfoClassMember('vlan-aware-flexible-xconnect-service', REFERENCE_LIST, 'VlanAwareFlexibleXconnectService' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService', 
                [], [], 
                '''                Flexible XConnect Service
                ''',
                'vlan_aware_flexible_xconnect_service',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'vlan-aware-flexible-xconnect-services',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.FlexibleXconnectServiceTable' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.FlexibleXconnectServiceTable',
            False, 
            [
            _MetaInfoClassMember('vlan-aware-flexible-xconnect-services', REFERENCE_CLASS, 'VlanAwareFlexibleXconnectServices' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices', 
                [], [], 
                '''                List of Vlan-Aware Flexible XConnect Services
                ''',
                'vlan_aware_flexible_xconnect_services',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('vlan-unaware-flexible-xconnect-services', REFERENCE_CLASS, 'VlanUnawareFlexibleXconnectServices' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices', 
                [], [], 
                '''                List of Vlan-Unaware Flexible XConnect
                Services
                ''',
                'vlan_unaware_flexible_xconnect_services',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'flexible-xconnect-service-table',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces.IccpInterface' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces.IccpInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('mac-flush-tcn', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable STP-TCN MAC flushing
                ''',
                'mac_flush_tcn',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('primary-vlan-range', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Primary VLAN range, in the form of 1-3,5
                ,8-11
                ''',
                'primary_vlan_range',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('recovery-delay', ATTRIBUTE, 'int' , None, None, 
                [('30', '3600')], [], 
                '''                Failure clear recovery delay
                ''',
                'recovery_delay',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('secondary-vlan-range', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Secondary VLAN range, in the form of 1-3,5
                ,8-11
                ''',
                'secondary_vlan_range',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'iccp-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces',
            False, 
            [
            _MetaInfoClassMember('iccp-interface', REFERENCE_LIST, 'IccpInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces.IccpInterface', 
                [], [], 
                '''                Interface name
                ''',
                'iccp_interface',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'iccp-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Group ID
                ''',
                'group_id',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('iccp-interfaces', REFERENCE_CLASS, 'IccpInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces', 
                [], [], 
                '''                List of interfaces
                ''',
                'iccp_interfaces',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('multi-homing-node-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '254')], [], 
                '''                ICCP-based service multi-homing node ID
                ''',
                'multi_homing_node_id',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'iccp-redundancy-group',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.Redundancy.IccpRedundancyGroups' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.Redundancy.IccpRedundancyGroups',
            False, 
            [
            _MetaInfoClassMember('iccp-redundancy-group', REFERENCE_LIST, 'IccpRedundancyGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup', 
                [], [], 
                '''                ICCP Redundancy group
                ''',
                'iccp_redundancy_group',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'iccp-redundancy-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database.Redundancy' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database.Redundancy',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable redundancy groups
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('iccp-redundancy-groups', REFERENCE_CLASS, 'IccpRedundancyGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.Redundancy.IccpRedundancyGroups', 
                [], [], 
                '''                List of Inter-Chassis Communication Protocol
                redundancy groups
                ''',
                'iccp_redundancy_groups',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'redundancy',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Database' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Database',
            False, 
            [
            _MetaInfoClassMember('bridge-domain-groups', REFERENCE_CLASS, 'BridgeDomainGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.BridgeDomainGroups', 
                [], [], 
                '''                List of bridge  groups
                ''',
                'bridge_domain_groups',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('flexible-xconnect-service-table', REFERENCE_CLASS, 'FlexibleXconnectServiceTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.FlexibleXconnectServiceTable', 
                [], [], 
                '''                List of Flexible XConnect Services
                ''',
                'flexible_xconnect_service_table',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('g8032-rings', REFERENCE_CLASS, 'G8032Rings' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.G8032Rings', 
                [], [], 
                '''                List of G8032 Ring
                ''',
                'g8032_rings',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pseudowire-classes', REFERENCE_CLASS, 'PseudowireClasses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.PseudowireClasses', 
                [], [], 
                '''                List of pseudowire classes
                ''',
                'pseudowire_classes',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('redundancy', REFERENCE_CLASS, 'Redundancy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.Redundancy', 
                [], [], 
                '''                Redundancy groups
                ''',
                'redundancy',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('xconnect-groups', REFERENCE_CLASS, 'XconnectGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database.XconnectGroups', 
                [], [], 
                '''                List of xconnect groups
                ''',
                'xconnect_groups',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'database',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Pbb' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Pbb',
            False, 
            [
            _MetaInfoClassMember('backbone-source-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Backbone Source MAC
                ''',
                'backbone_source_mac',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pbb',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.AutoDiscovery.BgpSignaling' : {
        'meta_info' : _MetaInfoClass('L2Vpn.AutoDiscovery.BgpSignaling',
            False, 
            [
            _MetaInfoClassMember('mtu-mismatch-ignore', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Ignore MTU mismatch for auto-discovered
                pseudowires
                ''',
                'mtu_mismatch_ignore',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'bgp-signaling',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.AutoDiscovery' : {
        'meta_info' : _MetaInfoClass('L2Vpn.AutoDiscovery',
            False, 
            [
            _MetaInfoClassMember('bgp-signaling', REFERENCE_CLASS, 'BgpSignaling' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.AutoDiscovery.BgpSignaling', 
                [], [], 
                '''                Global bgp signaling attributes
                ''',
                'bgp_signaling',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'auto-discovery',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Utility.Logging' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Utility.Logging',
            False, 
            [
            _MetaInfoClassMember('bridge-domain-state-change', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Bridge Domain state change logging
                ''',
                'bridge_domain_state_change',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('nsr-state-change', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Non Stop Routing state change logging
                ''',
                'nsr_state_change',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pseudowire-state-change', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable pseudowire state change logging
                ''',
                'pseudowire_state_change',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pwhe-replication-state-change', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable PW-HE Replication state change logging
                ''',
                'pwhe_replication_state_change',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('vfi', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable VFI state change logging
                ''',
                'vfi',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'logging',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Utility' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Utility',
            False, 
            [
            _MetaInfoClassMember('logging', REFERENCE_CLASS, 'Logging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Utility.Logging', 
                [], [], 
                '''                L2VPN logging utility
                ''',
                'logging',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'utility',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Snmp.Mib.MibInterface.Format' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Snmp.Mib.MibInterface.Format',
            False, 
            [
            _MetaInfoClassMember('external-interface-format', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Set MIB interface name output in slash
                format (/)
                ''',
                'external_interface_format',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'format',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Snmp.Mib.MibInterface' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Snmp.Mib.MibInterface',
            False, 
            [
            _MetaInfoClassMember('format', REFERENCE_CLASS, 'Format' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Snmp.Mib.MibInterface.Format', 
                [], [], 
                '''                MIB interface name output format
                ''',
                'format',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'mib-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Snmp.Mib.MibPseudowire' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Snmp.Mib.MibPseudowire',
            False, 
            [
            _MetaInfoClassMember('statistics', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable pseudowire statistics in MIB output
                ''',
                'statistics',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'mib-pseudowire',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Snmp.Mib' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Snmp.Mib',
            False, 
            [
            _MetaInfoClassMember('mib-interface', REFERENCE_CLASS, 'MibInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Snmp.Mib.MibInterface', 
                [], [], 
                '''                Interface related configuration for MIB
                ''',
                'mib_interface',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('mib-pseudowire', REFERENCE_CLASS, 'MibPseudowire' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Snmp.Mib.MibPseudowire', 
                [], [], 
                '''                Pseudowire related configuration for MIB
                ''',
                'mib_pseudowire',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'mib',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn.Snmp' : {
        'meta_info' : _MetaInfoClass('L2Vpn.Snmp',
            False, 
            [
            _MetaInfoClassMember('mib', REFERENCE_CLASS, 'Mib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Snmp.Mib', 
                [], [], 
                '''                MIB related configuration
                ''',
                'mib',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'snmp',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'L2Vpn' : {
        'meta_info' : _MetaInfoClass('L2Vpn',
            False, 
            [
            _MetaInfoClassMember('auto-discovery', REFERENCE_CLASS, 'AutoDiscovery' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.AutoDiscovery', 
                [], [], 
                '''                Global auto-discovery attributes
                ''',
                'auto_discovery',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('capability', REFERENCE_ENUM_CLASS, 'L2VpnCapabilityModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2VpnCapabilityModeEnum', 
                [], [], 
                '''                L2VPN Capability Mode
                ''',
                'capability',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('database', REFERENCE_CLASS, 'Database' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Database', 
                [], [], 
                '''                L2VPN databases
                ''',
                'database',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable L2VPN feature
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('l2vpn-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Global L2VPN Router ID
                ''',
                'l2vpn_router_id',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('load-balance', REFERENCE_ENUM_CLASS, 'LoadBalanceEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'LoadBalanceEnum', 
                [], [], 
                '''                Enable flow load balancing on l2vpn bridges
                ''',
                'load_balance',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('mspw-description', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                MS-PW global description
                ''',
                'mspw_description',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('mtu-mismatch-ignore', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Ignore MTU Mismatch for XCs
                ''',
                'mtu_mismatch_ignore',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('neighbor', REFERENCE_CLASS, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Neighbor', 
                [], [], 
                '''                L2VPN neighbor submode
                ''',
                'neighbor',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('nsr', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Non-Stop Routing
                ''',
                'nsr',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pbb', REFERENCE_CLASS, 'Pbb' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Pbb', 
                [], [], 
                '''                L2VPN PBB Global
                ''',
                'pbb',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pw-grouping', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable PW grouping
                ''',
                'pw_grouping',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pw-routing', REFERENCE_CLASS, 'PwRouting' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.PwRouting', 
                [], [], 
                '''                Pseudowire-routing attributes
                ''',
                'pw_routing',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pw-status-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable PW status
                ''',
                'pw_status_disable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pwoam-refresh', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Configure PW OAM refresh interval
                ''',
                'pwoam_refresh',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('snmp', REFERENCE_CLASS, 'Snmp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Snmp', 
                [], [], 
                '''                SNMP related configuration
                ''',
                'snmp',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('tcn-propagation', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Topology change notification propagation
                ''',
                'tcn_propagation',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('utility', REFERENCE_CLASS, 'Utility' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'L2Vpn.Utility', 
                [], [], 
                '''                L2VPN utilities
                ''',
                'utility',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'l2vpn',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'GenericInterfaceLists.GenericInterface.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('GenericInterfaceLists.GenericInterface.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable interface
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'GenericInterfaceLists.GenericInterface.Interfaces' : {
        'meta_info' : _MetaInfoClass('GenericInterfaceLists.GenericInterface.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'GenericInterfaceLists.GenericInterface.Interfaces.Interface', 
                [], [], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'GenericInterfaceLists.GenericInterface' : {
        'meta_info' : _MetaInfoClass('GenericInterfaceLists.GenericInterface',
            False, 
            [
            _MetaInfoClassMember('generic-interface-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Name of the interface list
                ''',
                'generic_interface_list_name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable interface list
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'GenericInterfaceLists.GenericInterface.Interfaces', 
                [], [], 
                '''                Interface table
                ''',
                'interfaces',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'generic-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'GenericInterfaceLists' : {
        'meta_info' : _MetaInfoClass('GenericInterfaceLists',
            False, 
            [
            _MetaInfoClassMember('generic-interface', REFERENCE_LIST, 'GenericInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'GenericInterfaceLists.GenericInterface', 
                [], [], 
                '''                Bridge group
                ''',
                'generic_interface',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'generic-interface-lists',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.EvpnTimers' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.EvpnTimers',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable EVPN timers
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpn-peering', ATTRIBUTE, 'int' , None, None, 
                [('0', '300')], [], 
                '''                Global Peering timer
                ''',
                'evpn_peering',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpn-recovery', ATTRIBUTE, 'int' , None, None, 
                [('20', '3600')], [], 
                '''                Global Recovery timer
                ''',
                'evpn_recovery',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpn-timers',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.Evpnevis.Evpnevi.EviLoadBalancing' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.Evpnevis.Evpnevi.EviLoadBalancing',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable EVI Loadbalancing
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evi-flow-label', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Flow Label based load balancing
                ''',
                'evi_flow_label',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evi-load-balancing',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetAs' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetAs',
            False, 
            [
            _MetaInfoClassMember('format', REFERENCE_ENUM_CLASS, 'BgpRouteTargetFormatEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'BgpRouteTargetFormatEnum', 
                [], [], 
                '''                Format of the route target
                ''',
                'format',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('role', REFERENCE_ENUM_CLASS, 'BgpRouteTargetRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'BgpRouteTargetRoleEnum', 
                [], [], 
                '''                Role of the router target type
                ''',
                'role',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Two byte or 4 byte AS number
                ''',
                'as_',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('as-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS:nn (hex or decimal format)
                ''',
                'as_index',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('stitching', REFERENCE_ENUM_CLASS, 'BgpRouteTargetEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'BgpRouteTargetEnum', 
                [], [], 
                '''                whether RT is Stitching RT
                ''',
                'stitching',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpn-route-target-as',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetNone' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetNone',
            False, 
            [
            _MetaInfoClassMember('format', REFERENCE_ENUM_CLASS, 'BgpRouteTargetFormatEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'BgpRouteTargetFormatEnum', 
                [], [], 
                '''                Format of the route target
                ''',
                'format',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('role', REFERENCE_ENUM_CLASS, 'BgpRouteTargetRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'BgpRouteTargetRoleEnum', 
                [], [], 
                '''                Role of the router target type
                ''',
                'role',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('stitching', REFERENCE_ENUM_CLASS, 'BgpRouteTargetEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'BgpRouteTargetEnum', 
                [], [], 
                '''                whether RT is Stitching RT
                ''',
                'stitching',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpn-route-target-none',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetIpv4Address' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetIpv4Address',
            False, 
            [
            _MetaInfoClassMember('format', REFERENCE_ENUM_CLASS, 'BgpRouteTargetFormatEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'BgpRouteTargetFormatEnum', 
                [], [], 
                '''                Format of the route target
                ''',
                'format',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('role', REFERENCE_ENUM_CLASS, 'BgpRouteTargetRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'BgpRouteTargetRoleEnum', 
                [], [], 
                '''                Role of the router target type
                ''',
                'role',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV4 address
                ''',
                'address',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('addr-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Addr index
                ''',
                'addr_index',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('stitching', REFERENCE_ENUM_CLASS, 'BgpRouteTargetEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'BgpRouteTargetEnum', 
                [], [], 
                '''                whether RT is Stitching RT
                ''',
                'stitching',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpn-route-target-ipv4-address',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets',
            False, 
            [
            _MetaInfoClassMember('evpn-route-target-as', REFERENCE_LIST, 'EvpnRouteTargetAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetAs', 
                [], [], 
                '''                Name of the Route Target
                ''',
                'evpn_route_target_as',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpn-route-target-ipv4-address', REFERENCE_LIST, 'EvpnRouteTargetIpv4Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetIpv4Address', 
                [], [], 
                '''                Name of the Route Target
                ''',
                'evpn_route_target_ipv4_address',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpn-route-target-none', REFERENCE_LIST, 'EvpnRouteTargetNone' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetNone', 
                [], [], 
                '''                Name of the Route Target
                ''',
                'evpn_route_target_none',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpn-route-targets',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteDistinguisher' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteDistinguisher',
            False, 
            [
            _MetaInfoClassMember('addr-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Addr index
                ''',
                'addr_index',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV4 address
                ''',
                'address',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Two byte or 4 byte AS number
                ''',
                'as_',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('as-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS:nn (hex or decimal format)
                ''',
                'as_index',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BgpRouteDistinguisherEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'BgpRouteDistinguisherEnum', 
                [], [], 
                '''                Router Distinguisher Type
                ''',
                'type',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpn-route-distinguisher',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Autodiscovery BGP
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpn-route-distinguisher', REFERENCE_CLASS, 'EvpnRouteDistinguisher' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteDistinguisher', 
                [], [], 
                '''                Route Distinguisher
                ''',
                'evpn_route_distinguisher',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpn-route-targets', REFERENCE_CLASS, 'EvpnRouteTargets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets', 
                [], [], 
                '''                Route Target
                ''',
                'evpn_route_targets',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('table-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Table Policy for installation of forwarding
                data to L2FIB
                ''',
                'table_policy',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpnevibgp-auto-discovery',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.Evpnevis.Evpnevi' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.Evpnevis.Evpnevi',
            False, 
            [
            _MetaInfoClassMember('eviid', ATTRIBUTE, 'int' , None, None, 
                [('1', '65534')], [], 
                '''                EVI ID
                ''',
                'eviid',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('evi-advertise-mac', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Advertise MAC only routes
                ''',
                'evi_advertise_mac',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evi-load-balancing', REFERENCE_CLASS, 'EviLoadBalancing' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.Evpnevis.Evpnevi.EviLoadBalancing', 
                [], [], 
                '''                Enter EVI Loadbalancing configuration submode
                ''',
                'evi_load_balancing',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evi-reorig-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable route re-origination
                ''',
                'evi_reorig_disable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evi-stitching', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable RT stitching for MPLS fabric
                ''',
                'evi_stitching',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evi-unknown-unicast-flooding-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable Unknown Unicast Flooding on this EVI
                ''',
                'evi_unknown_unicast_flooding_disable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpn-evi-cw-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                CW disable for EVPN EVI
                ''',
                'evpn_evi_cw_disable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpnevi-description', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Description for EVPN EVI
                ''',
                'evpnevi_description',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpnevibgp-auto-discovery', REFERENCE_CLASS, 'EvpnevibgpAutoDiscovery' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery', 
                [], [], 
                '''                Enable Autodiscovery BGP in EVPN EVI
                ''',
                'evpnevibgp_auto_discovery',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpnevi',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.Evpnevis' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.Evpnevis',
            False, 
            [
            _MetaInfoClassMember('evpnevi', REFERENCE_LIST, 'Evpnevi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.Evpnevis.Evpnevi', 
                [], [], 
                '''                Enter EVPN EVI configuration submode
                ''',
                'evpnevi',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpnevis',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualAccessVfiTimers' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualAccessVfiTimers',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Virtual Forwarding Interface timers
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpn-virtual-access-vfi-peering', ATTRIBUTE, 'int' , None, None, 
                [('0', '300')], [], 
                '''                Virtual Forwarding Interface-specific
                Peering timer
                ''',
                'evpn_virtual_access_vfi_peering',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpn-virtual-access-vfi-recovery', ATTRIBUTE, 'int' , None, None, 
                [('20', '3600')], [], 
                '''                Virtual Forwarding Interface-specific
                Recovery timer
                ''',
                'evpn_virtual_access_vfi_recovery',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpn-virtual-access-vfi-timers',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.Identifier' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.Identifier',
            False, 
            [
            _MetaInfoClassMember('bytes01', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Type 0's 1st Byte or Type Byte and 1st Byte
                ''',
                'bytes01',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bytes23', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                2nd and 3rd Bytes
                ''',
                'bytes23',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bytes45', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                4th and 5th Bytes
                ''',
                'bytes45',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bytes67', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                6th and 7th Bytes
                ''',
                'bytes67',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bytes89', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                8th and 9th Bytes
                ''',
                'bytes89',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'EthernetSegmentIdentifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'EthernetSegmentIdentifierEnum', 
                [], [], 
                '''                Ethernet segment identifier type
                ''',
                'type',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'identifier',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Ethernet Segment
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('es-import-route-target', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                ES-Import Route Target
                ''',
                'es_import_route_target',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('identifier', REFERENCE_CLASS, 'Identifier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.Identifier', 
                [], [], 
                '''                Ethernet segment identifier
                ''',
                'identifier',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpn-virtual-ethernet-segment',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Name of the Virtual Access VFI
                ''',
                'name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('evpn-virtual-access-vfi-timers', REFERENCE_CLASS, 'EvpnVirtualAccessVfiTimers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualAccessVfiTimers', 
                [], [], 
                '''                Enter Virtual Forwarding Interface timers
                configuration submode
                ''',
                'evpn_virtual_access_vfi_timers',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpn-virtual-ethernet-segment', REFERENCE_CLASS, 'EvpnVirtualEthernetSegment' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment', 
                [], [], 
                '''                Enter Ethernet Segment configuration submode
                ''',
                'evpn_virtual_ethernet_segment',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpn-virtual-access-vfi',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.EvpnVirtualAccessVfis' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.EvpnVirtualAccessVfis',
            False, 
            [
            _MetaInfoClassMember('evpn-virtual-access-vfi', REFERENCE_LIST, 'EvpnVirtualAccessVfi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi', 
                [], [], 
                '''                Virtual Access VFI
                ''',
                'evpn_virtual_access_vfi',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpn-virtual-access-vfis',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.EvpnLoadBalancing' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.EvpnLoadBalancing',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable EVPN Loadbalancing
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpn-flow-label', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Flow Label based load balancing
                ''',
                'evpn_flow_label',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpn-load-balancing',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.EvpnbgpAutoDiscovery.EvpnRouteDistinguisher' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.EvpnbgpAutoDiscovery.EvpnRouteDistinguisher',
            False, 
            [
            _MetaInfoClassMember('addr-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Addr index
                ''',
                'addr_index',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV4 address
                ''',
                'address',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Two byte or 4 byte AS number
                ''',
                'as_',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('as-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS:nn (hex or decimal format)
                ''',
                'as_index',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BgpRouteDistinguisherEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'BgpRouteDistinguisherEnum', 
                [], [], 
                '''                Router Distinguisher Type
                ''',
                'type',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpn-route-distinguisher',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.EvpnbgpAutoDiscovery' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.EvpnbgpAutoDiscovery',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Autodiscovery BGP
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpn-route-distinguisher', REFERENCE_CLASS, 'EvpnRouteDistinguisher' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.EvpnbgpAutoDiscovery.EvpnRouteDistinguisher', 
                [], [], 
                '''                Route Distinguisher
                ''',
                'evpn_route_distinguisher',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpnbgp-auto-discovery',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.EvpnLogging' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.EvpnLogging',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable EVPN Logging
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpn-df-election', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Designated Forwarder election logging
                ''',
                'evpn_df_election',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpn-logging',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment.ManualServiceCarving.ServiceList' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment.ManualServiceCarving.ServiceList',
            False, 
            [
            _MetaInfoClassMember('primary', ATTRIBUTE, 'str' , None, None, 
                [(1, 150)], [], 
                '''                Primary services list
                ''',
                'primary',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('secondary', ATTRIBUTE, 'str' , None, None, 
                [(1, 150)], [], 
                '''                Secondary services list
                ''',
                'secondary',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'service-list',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment.ManualServiceCarving' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment.ManualServiceCarving',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Manual service carving
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('service-list', REFERENCE_CLASS, 'ServiceList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment.ManualServiceCarving.ServiceList', 
                [], [], 
                '''                Manual service carving primary,secondary
                lists
                ''',
                'service_list',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'manual-service-carving',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment.Identifier' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment.Identifier',
            False, 
            [
            _MetaInfoClassMember('bytes01', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Type 0's 1st Byte or Type Byte and 1st Byte
                ''',
                'bytes01',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bytes23', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                2nd and 3rd Bytes
                ''',
                'bytes23',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bytes45', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                4th and 5th Bytes
                ''',
                'bytes45',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bytes67', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                6th and 7th Bytes
                ''',
                'bytes67',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bytes89', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                8th and 9th Bytes
                ''',
                'bytes89',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'EthernetSegmentIdentifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'EthernetSegmentIdentifierEnum', 
                [], [], 
                '''                Ethernet segment identifier type
                ''',
                'type',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'identifier',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment',
            False, 
            [
            _MetaInfoClassMember('backbone-source-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Backbone Source MAC
                ''',
                'backbone_source_mac',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Ethernet Segment
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('es-import-route-target', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                ES-Import Route Target
                ''',
                'es_import_route_target',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('force-single-homed', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Force ethernet segment to remain
                single-homed
                ''',
                'force_single_homed',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('identifier', REFERENCE_CLASS, 'Identifier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment.Identifier', 
                [], [], 
                '''                Ethernet segment identifier
                ''',
                'identifier',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('load-balancing-single-active', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable single-active load balancing mode
                ''',
                'load_balancing_single_active',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('manual-service-carving', REFERENCE_CLASS, 'ManualServiceCarving' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment.ManualServiceCarving', 
                [], [], 
                '''                Enter Manual service carving configuration
                submode
                ''',
                'manual_service_carving',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpn-interface-ethernet-segment',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnacTimers' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnacTimers',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Interface-specific timers
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpnac-peering', ATTRIBUTE, 'int' , None, None, 
                [('0', '300')], [], 
                '''                Interface-specific Peering timer
                ''',
                'evpnac_peering',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpnac-recovery', ATTRIBUTE, 'int' , None, None, 
                [('20', '3600')], [], 
                '''                Interface-specific Recovery timer
                ''',
                'evpnac_recovery',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpnac-timers',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.EvpnInterfaces.EvpnInterface' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.EvpnInterfaces.EvpnInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of the attachment circuit interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('evpn-interface-ethernet-segment', REFERENCE_CLASS, 'EvpnInterfaceEthernetSegment' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment', 
                [], [], 
                '''                Enter Ethernet Segment configuration submode
                ''',
                'evpn_interface_ethernet_segment',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpnac-timers', REFERENCE_CLASS, 'EvpnacTimers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnacTimers', 
                [], [], 
                '''                Enter Interface-specific timers configuration
                submode
                ''',
                'evpnac_timers',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('mac-flush', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MVRP MAC Flush mode
                ''',
                'mac_flush',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpn-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.EvpnInterfaces' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.EvpnInterfaces',
            False, 
            [
            _MetaInfoClassMember('evpn-interface', REFERENCE_LIST, 'EvpnInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.EvpnInterfaces.EvpnInterface', 
                [], [], 
                '''                Attachment circuit interface
                ''',
                'evpn_interface',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpn-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualAccessPwTimers' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualAccessPwTimers',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Virtual Access Pseudowire-specific
                timers
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpn-virtual-access-pw-peering', ATTRIBUTE, 'int' , None, None, 
                [('0', '300')], [], 
                '''                Virtual Access Pseudowire-specific Peering
                timer
                ''',
                'evpn_virtual_access_pw_peering',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpn-virtual-access-pw-recovery', ATTRIBUTE, 'int' , None, None, 
                [('20', '3600')], [], 
                '''                Virtual Access Pseudowire-specific Recovery
                timer
                ''',
                'evpn_virtual_access_pw_recovery',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpn-virtual-access-pw-timers',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.Identifier' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.Identifier',
            False, 
            [
            _MetaInfoClassMember('bytes01', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Type 0's 1st Byte or Type Byte and 1st Byte
                ''',
                'bytes01',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bytes23', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                2nd and 3rd Bytes
                ''',
                'bytes23',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bytes45', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                4th and 5th Bytes
                ''',
                'bytes45',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bytes67', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                6th and 7th Bytes
                ''',
                'bytes67',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('bytes89', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                8th and 9th Bytes
                ''',
                'bytes89',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'EthernetSegmentIdentifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'EthernetSegmentIdentifierEnum', 
                [], [], 
                '''                Ethernet segment identifier type
                ''',
                'type',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'identifier',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Ethernet Segment
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('es-import-route-target', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                ES-Import Route Target
                ''',
                'es_import_route_target',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('identifier', REFERENCE_CLASS, 'Identifier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.Identifier', 
                [], [], 
                '''                Ethernet segment identifier
                ''',
                'identifier',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpn-virtual-ethernet-segment',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw',
            False, 
            [
            _MetaInfoClassMember('neighbor', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor IP address
                ''',
                'neighbor',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('pseudowire-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Pseudowire ID
                ''',
                'pseudowire_id',
                'Cisco-IOS-XR-l2vpn-cfg', True),
            _MetaInfoClassMember('evpn-virtual-access-pw-timers', REFERENCE_CLASS, 'EvpnVirtualAccessPwTimers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualAccessPwTimers', 
                [], [], 
                '''                Enter Virtual Access Pseudowire-specific
                timers configuration submode
                ''',
                'evpn_virtual_access_pw_timers',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpn-virtual-ethernet-segment', REFERENCE_CLASS, 'EvpnVirtualEthernetSegment' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment', 
                [], [], 
                '''                Enter Ethernet Segment configuration submode
                ''',
                'evpn_virtual_ethernet_segment',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpn-virtual-access-pw',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables.EvpnVirtualAccessPws' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables.EvpnVirtualAccessPws',
            False, 
            [
            _MetaInfoClassMember('evpn-virtual-access-pw', REFERENCE_LIST, 'EvpnVirtualAccessPw' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw', 
                [], [], 
                '''                Virtual Access Pseudowire
                ''',
                'evpn_virtual_access_pw',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpn-virtual-access-pws',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn.EvpnTables' : {
        'meta_info' : _MetaInfoClass('Evpn.EvpnTables',
            False, 
            [
            _MetaInfoClassMember('evpn-interfaces', REFERENCE_CLASS, 'EvpnInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.EvpnInterfaces', 
                [], [], 
                '''                Attachment Circuit interfaces
                ''',
                'evpn_interfaces',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpn-load-balancing', REFERENCE_CLASS, 'EvpnLoadBalancing' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.EvpnLoadBalancing', 
                [], [], 
                '''                Enter EVPN Loadbalancing configuration submode
                ''',
                'evpn_load_balancing',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpn-logging', REFERENCE_CLASS, 'EvpnLogging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.EvpnLogging', 
                [], [], 
                '''                Enter EVPN Logging configuration submode
                ''',
                'evpn_logging',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpn-source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Configure EVPN router-id implicitly through
                Loopback Interface
                ''',
                'evpn_source_interface',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpn-timers', REFERENCE_CLASS, 'EvpnTimers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.EvpnTimers', 
                [], [], 
                '''                Enter EVPN timers configuration submode
                ''',
                'evpn_timers',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpn-virtual-access-pws', REFERENCE_CLASS, 'EvpnVirtualAccessPws' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.EvpnVirtualAccessPws', 
                [], [], 
                '''                Virtual Access Pseudowire interfaces
                ''',
                'evpn_virtual_access_pws',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpn-virtual-access-vfis', REFERENCE_CLASS, 'EvpnVirtualAccessVfis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.EvpnVirtualAccessVfis', 
                [], [], 
                '''                Virtual Access VFI interfaces
                ''',
                'evpn_virtual_access_vfis',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpnbgp-auto-discovery', REFERENCE_CLASS, 'EvpnbgpAutoDiscovery' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.EvpnbgpAutoDiscovery', 
                [], [], 
                '''                Enable Autodiscovery BGP in EVPN
                ''',
                'evpnbgp_auto_discovery',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpnevis', REFERENCE_CLASS, 'Evpnevis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables.Evpnevis', 
                [], [], 
                '''                Enter EVPN EVI configuration submode
                ''',
                'evpnevis',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpn-tables',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
    'Evpn' : {
        'meta_info' : _MetaInfoClass('Evpn',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable EVPN feature
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('evpn-tables', REFERENCE_CLASS, 'EvpnTables' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg', 'Evpn.EvpnTables', 
                [], [], 
                '''                EVPN submodes
                ''',
                'evpn_tables',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'evpn',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2vpn_cfg'
        ),
    },
}
_meta_table['L2Vpn.PwRouting.PwRoutingBgp.EvpnRouteDistinguisher']['meta_info'].parent =_meta_table['L2Vpn.PwRouting.PwRoutingBgp']['meta_info']
_meta_table['L2Vpn.PwRouting.PwRoutingBgp']['meta_info'].parent =_meta_table['L2Vpn.PwRouting']['meta_info']
_meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S.ErpPort0']['meta_info'].parent =_meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S']['meta_info']
_meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps.Port1']['meta_info'].parent =_meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps']['meta_info']
_meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Rpl']['meta_info'].parent =_meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance']['meta_info']
_meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps']['meta_info'].parent =_meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance']['meta_info']
_meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance']['meta_info'].parent =_meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances']['meta_info']
_meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.NoneOrVirtual']['meta_info'].parent =_meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1']['meta_info']
_meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1.Interface']['meta_info'].parent =_meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1']['meta_info']
_meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S.ErpPort1']['meta_info'].parent =_meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S']['meta_info']
_meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpPort0S']['meta_info'].parent =_meta_table['L2Vpn.Database.G8032Rings.G8032Ring']['meta_info']
_meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpInstances']['meta_info'].parent =_meta_table['L2Vpn.Database.G8032Rings.G8032Ring']['meta_info']
_meta_table['L2Vpn.Database.G8032Rings.G8032Ring.ErpPort1S']['meta_info'].parent =_meta_table['L2Vpn.Database.G8032Rings.G8032Ring']['meta_info']
_meta_table['L2Vpn.Database.G8032Rings.G8032Ring']['meta_info'].parent =_meta_table['L2Vpn.Database.G8032Rings']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits.BackupAttachmentCircuit']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns.PseudowireEvpn']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpRemoteCookie']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpSecondaryLocalCookie']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes.L2TpLocalCookie']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.MplsStaticLabels']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStaticAttributes']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor.L2TpStatic']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpRemoteCookie']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpSecondaryLocalCookie']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes.L2TpLocalCookie']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.MplsStaticLabels']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStaticAttributes']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2TpStatic']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.Neighbor']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire.PseudowireAddress']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires.Pseudowire']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions.MonitorSession']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds.PseudowireRouted']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits.AttachmentCircuit']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.BackupAttachmentCircuits']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireEvpns']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.Pseudowires']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.MonitorSessions']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.PseudowireRouteds']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect.AttachmentCircuits']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects.P2PXconnect']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.TwoByteAsOrFourByteAs']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget.Ipv4Address']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets.Mp2MpRouteTarget']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits.RemoteCeidAttachmentCircuit']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids.Ceid']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.FlowLabelLoadBalance']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol.Ceids']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.RouteDistinguisher']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRoutePolicy']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpRouteTargets']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery.Mp2MpSignalingProtocol']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect.Mp2MpAutoDiscovery']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects.Mp2MpXconnect']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.P2PXconnects']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup.Mp2MpXconnects']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups.XconnectGroup']['meta_info'].parent =_meta_table['L2Vpn.Database.XconnectGroups']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl.StormControlUnit']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses.MemberVniStaticMacAddress']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni.MemberVniStaticMacAddresses']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters.BdMacFilter']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacLimit']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.MacSecure']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacAging']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings.PbbStaticMacMapping']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacLimit']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacAging']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacSecure']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeSplitHorizonGroup']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeDhcpProfile']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacAging']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacLimit']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis.PbbCoreEvi']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreEvis']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreDhcpProfile']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis.BridgeDomainEvi']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses.AccessVfiPseudowireStaticMacAddress']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire.AccessVfiPseudowireStaticMacAddresses']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires.AccessVfiPseudowire']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi.AccessVfiPseudowires']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis.AccessVfi']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai.PseudowireDaiAddressValidation']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType.StormControlUnit']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses.BdPwStaticMacAddress']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacSecure']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacAging']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacLimit']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon.BdPwSplitHorizonGroup']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires.BridgeDomainBackupPseudowire']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireProfile']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireIpSourceGuard']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwMplsStaticLabels']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports.Transport']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings.Signaling']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Transports']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp.Signalings']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses.PseudowireStaticMacAddress']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwDhcpSnoop']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwMplsStaticLabels']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.Vplsid']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.FlowLabelLoadBalance']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol.FlowLabelLoadBalance']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.TwoByteAsOrFourByteAs']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.Ipv4Address']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpRoutePolicy']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteDistinguisher']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2Mp']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai.InterfaceDaiAddressValidation']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType.StormControlUnit']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon.SplitHorizonGroupId']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses.StaticMacAddress']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacAging']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacSecure']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacLimit']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceIpSourceGuard']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceProfile']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns.BdPseudowireEvpn']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai.DaiAddressValidation']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface.RoutedInterfaceSplitHorizonGroup']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.NvSatellite']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainEvis']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.AccessVfis']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowireEvpns']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.IpSourceGuard']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups.BridgeDomainGroup']['meta_info'].parent =_meta_table['L2Vpn.Database.BridgeDomainGroups']['meta_info']
_meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.Sequencing']['meta_info'].parent =_meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation']['meta_info']
_meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.TypeOfService']['meta_info'].parent =_meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation']['meta_info']
_meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.SignalingProtocol']['meta_info'].parent =_meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation']['meta_info']
_meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation.PathMtu']['meta_info'].parent =_meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation']['meta_info']
_meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup.FlowLabelLoadBalance']['meta_info'].parent =_meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup']['meta_info']
_meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.Sequencing']['meta_info'].parent =_meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation']['meta_info']
_meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.MplsRedundancy']['meta_info'].parent =_meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation']['meta_info']
_meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.PreferredPath']['meta_info'].parent =_meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation']['meta_info']
_meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup']['meta_info'].parent =_meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation']['meta_info']
_meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.L2Tpv3Encapsulation']['meta_info'].parent =_meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass']['meta_info']
_meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.BackupDisableDelay']['meta_info'].parent =_meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass']['meta_info']
_meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation']['meta_info'].parent =_meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass']['meta_info']
_meta_table['L2Vpn.Database.PseudowireClasses.PseudowireClass']['meta_info'].parent =_meta_table['L2Vpn.Database.PseudowireClasses']['meta_info']
_meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits.VlanUnawareFxcAttachmentCircuit']['meta_info'].parent =_meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits']['meta_info']
_meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns.VlanUnawareFxcPseudowireEvpn']['meta_info'].parent =_meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns']['meta_info']
_meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcAttachmentCircuits']['meta_info'].parent =_meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService']['meta_info']
_meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService.VlanUnawareFxcPseudowireEvpns']['meta_info'].parent =_meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService']['meta_info']
_meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices.VlanUnawareFlexibleXconnectService']['meta_info'].parent =_meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices']['meta_info']
_meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits.VlanAwareFxcAttachmentCircuit']['meta_info'].parent =_meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits']['meta_info']
_meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService.VlanAwareFxcAttachmentCircuits']['meta_info'].parent =_meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService']['meta_info']
_meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices.VlanAwareFlexibleXconnectService']['meta_info'].parent =_meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices']['meta_info']
_meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanUnawareFlexibleXconnectServices']['meta_info'].parent =_meta_table['L2Vpn.Database.FlexibleXconnectServiceTable']['meta_info']
_meta_table['L2Vpn.Database.FlexibleXconnectServiceTable.VlanAwareFlexibleXconnectServices']['meta_info'].parent =_meta_table['L2Vpn.Database.FlexibleXconnectServiceTable']['meta_info']
_meta_table['L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces.IccpInterface']['meta_info'].parent =_meta_table['L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces']['meta_info']
_meta_table['L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces']['meta_info'].parent =_meta_table['L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup']['meta_info']
_meta_table['L2Vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup']['meta_info'].parent =_meta_table['L2Vpn.Database.Redundancy.IccpRedundancyGroups']['meta_info']
_meta_table['L2Vpn.Database.Redundancy.IccpRedundancyGroups']['meta_info'].parent =_meta_table['L2Vpn.Database.Redundancy']['meta_info']
_meta_table['L2Vpn.Database.G8032Rings']['meta_info'].parent =_meta_table['L2Vpn.Database']['meta_info']
_meta_table['L2Vpn.Database.XconnectGroups']['meta_info'].parent =_meta_table['L2Vpn.Database']['meta_info']
_meta_table['L2Vpn.Database.BridgeDomainGroups']['meta_info'].parent =_meta_table['L2Vpn.Database']['meta_info']
_meta_table['L2Vpn.Database.PseudowireClasses']['meta_info'].parent =_meta_table['L2Vpn.Database']['meta_info']
_meta_table['L2Vpn.Database.FlexibleXconnectServiceTable']['meta_info'].parent =_meta_table['L2Vpn.Database']['meta_info']
_meta_table['L2Vpn.Database.Redundancy']['meta_info'].parent =_meta_table['L2Vpn.Database']['meta_info']
_meta_table['L2Vpn.AutoDiscovery.BgpSignaling']['meta_info'].parent =_meta_table['L2Vpn.AutoDiscovery']['meta_info']
_meta_table['L2Vpn.Utility.Logging']['meta_info'].parent =_meta_table['L2Vpn.Utility']['meta_info']
_meta_table['L2Vpn.Snmp.Mib.MibInterface.Format']['meta_info'].parent =_meta_table['L2Vpn.Snmp.Mib.MibInterface']['meta_info']
_meta_table['L2Vpn.Snmp.Mib.MibInterface']['meta_info'].parent =_meta_table['L2Vpn.Snmp.Mib']['meta_info']
_meta_table['L2Vpn.Snmp.Mib.MibPseudowire']['meta_info'].parent =_meta_table['L2Vpn.Snmp.Mib']['meta_info']
_meta_table['L2Vpn.Snmp.Mib']['meta_info'].parent =_meta_table['L2Vpn.Snmp']['meta_info']
_meta_table['L2Vpn.PwRouting']['meta_info'].parent =_meta_table['L2Vpn']['meta_info']
_meta_table['L2Vpn.Neighbor']['meta_info'].parent =_meta_table['L2Vpn']['meta_info']
_meta_table['L2Vpn.Database']['meta_info'].parent =_meta_table['L2Vpn']['meta_info']
_meta_table['L2Vpn.Pbb']['meta_info'].parent =_meta_table['L2Vpn']['meta_info']
_meta_table['L2Vpn.AutoDiscovery']['meta_info'].parent =_meta_table['L2Vpn']['meta_info']
_meta_table['L2Vpn.Utility']['meta_info'].parent =_meta_table['L2Vpn']['meta_info']
_meta_table['L2Vpn.Snmp']['meta_info'].parent =_meta_table['L2Vpn']['meta_info']
_meta_table['GenericInterfaceLists.GenericInterface.Interfaces.Interface']['meta_info'].parent =_meta_table['GenericInterfaceLists.GenericInterface.Interfaces']['meta_info']
_meta_table['GenericInterfaceLists.GenericInterface.Interfaces']['meta_info'].parent =_meta_table['GenericInterfaceLists.GenericInterface']['meta_info']
_meta_table['GenericInterfaceLists.GenericInterface']['meta_info'].parent =_meta_table['GenericInterfaceLists']['meta_info']
_meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetAs']['meta_info'].parent =_meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets']['meta_info']
_meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetNone']['meta_info'].parent =_meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets']['meta_info']
_meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTargetIpv4Address']['meta_info'].parent =_meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets']['meta_info']
_meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets']['meta_info'].parent =_meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery']['meta_info']
_meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteDistinguisher']['meta_info'].parent =_meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery']['meta_info']
_meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EviLoadBalancing']['meta_info'].parent =_meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi']['meta_info']
_meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery']['meta_info'].parent =_meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi']['meta_info']
_meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi']['meta_info'].parent =_meta_table['Evpn.EvpnTables.Evpnevis']['meta_info']
_meta_table['Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment.Identifier']['meta_info'].parent =_meta_table['Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment']['meta_info']
_meta_table['Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualAccessVfiTimers']['meta_info'].parent =_meta_table['Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi']['meta_info']
_meta_table['Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi.EvpnVirtualEthernetSegment']['meta_info'].parent =_meta_table['Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi']['meta_info']
_meta_table['Evpn.EvpnTables.EvpnVirtualAccessVfis.EvpnVirtualAccessVfi']['meta_info'].parent =_meta_table['Evpn.EvpnTables.EvpnVirtualAccessVfis']['meta_info']
_meta_table['Evpn.EvpnTables.EvpnbgpAutoDiscovery.EvpnRouteDistinguisher']['meta_info'].parent =_meta_table['Evpn.EvpnTables.EvpnbgpAutoDiscovery']['meta_info']
_meta_table['Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment.ManualServiceCarving.ServiceList']['meta_info'].parent =_meta_table['Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment.ManualServiceCarving']['meta_info']
_meta_table['Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment.ManualServiceCarving']['meta_info'].parent =_meta_table['Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment']['meta_info']
_meta_table['Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment.Identifier']['meta_info'].parent =_meta_table['Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment']['meta_info']
_meta_table['Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnInterfaceEthernetSegment']['meta_info'].parent =_meta_table['Evpn.EvpnTables.EvpnInterfaces.EvpnInterface']['meta_info']
_meta_table['Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnacTimers']['meta_info'].parent =_meta_table['Evpn.EvpnTables.EvpnInterfaces.EvpnInterface']['meta_info']
_meta_table['Evpn.EvpnTables.EvpnInterfaces.EvpnInterface']['meta_info'].parent =_meta_table['Evpn.EvpnTables.EvpnInterfaces']['meta_info']
_meta_table['Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment.Identifier']['meta_info'].parent =_meta_table['Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment']['meta_info']
_meta_table['Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualAccessPwTimers']['meta_info'].parent =_meta_table['Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw']['meta_info']
_meta_table['Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw.EvpnVirtualEthernetSegment']['meta_info'].parent =_meta_table['Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw']['meta_info']
_meta_table['Evpn.EvpnTables.EvpnVirtualAccessPws.EvpnVirtualAccessPw']['meta_info'].parent =_meta_table['Evpn.EvpnTables.EvpnVirtualAccessPws']['meta_info']
_meta_table['Evpn.EvpnTables.EvpnTimers']['meta_info'].parent =_meta_table['Evpn.EvpnTables']['meta_info']
_meta_table['Evpn.EvpnTables.Evpnevis']['meta_info'].parent =_meta_table['Evpn.EvpnTables']['meta_info']
_meta_table['Evpn.EvpnTables.EvpnVirtualAccessVfis']['meta_info'].parent =_meta_table['Evpn.EvpnTables']['meta_info']
_meta_table['Evpn.EvpnTables.EvpnLoadBalancing']['meta_info'].parent =_meta_table['Evpn.EvpnTables']['meta_info']
_meta_table['Evpn.EvpnTables.EvpnbgpAutoDiscovery']['meta_info'].parent =_meta_table['Evpn.EvpnTables']['meta_info']
_meta_table['Evpn.EvpnTables.EvpnLogging']['meta_info'].parent =_meta_table['Evpn.EvpnTables']['meta_info']
_meta_table['Evpn.EvpnTables.EvpnInterfaces']['meta_info'].parent =_meta_table['Evpn.EvpnTables']['meta_info']
_meta_table['Evpn.EvpnTables.EvpnVirtualAccessPws']['meta_info'].parent =_meta_table['Evpn.EvpnTables']['meta_info']
_meta_table['Evpn.EvpnTables']['meta_info'].parent =_meta_table['Evpn']['meta_info']

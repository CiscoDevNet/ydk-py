


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'RsvpBc0Enum' : _MetaInfoEnum('RsvpBc0Enum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg',
        {
            'bc0':'bc0',
            'global-pool':'global_pool',
            'not-specified':'not_specified',
        }, 'Cisco-IOS-XR-ip-rsvp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg']),
    'RsvpBwCfgEnum' : _MetaInfoEnum('RsvpBwCfgEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg',
        {
            'absolute':'absolute',
            'percentage':'percentage',
        }, 'Cisco-IOS-XR-ip-rsvp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg']),
    'RsvpRdmEnum' : _MetaInfoEnum('RsvpRdmEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg',
        {
            'rdm':'rdm',
            'not-specified':'not_specified',
            'use-default-bandwidth':'use_default_bandwidth',
        }, 'Cisco-IOS-XR-ip-rsvp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg']),
    'RsvpBc1Enum' : _MetaInfoEnum('RsvpBc1Enum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg',
        {
            'bc1':'bc1',
            'sub-pool':'sub_pool',
        }, 'Cisco-IOS-XR-ip-rsvp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg']),
    'Rsvp.Neighbors.Neighbor.Authentication' : {
        'meta_info' : _MetaInfoClass('Rsvp.Neighbors.Neighbor.Authentication',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable RSVP authentication
                ''',
                'enable',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('key-chain', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Key chain to authenticate RSVP signalling
                messages
                ''',
                'key_chain',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('life-time', ATTRIBUTE, 'int' , None, None, 
                [('30', '86400')], [], 
                '''                Life time (in seconds) for each security
                association
                ''',
                'life_time',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('window-size', ATTRIBUTE, 'int' , None, None, 
                [('1', '64')], [], 
                '''                Window-size to limit number of out-of-order
                messages
                ''',
                'window_size',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('Rsvp.Neighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor IP address
                ''',
                'neighbor',
                'Cisco-IOS-XR-ip-rsvp-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.Neighbors.Neighbor.Authentication', 
                [], [], 
                '''                Configure RSVP authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.Neighbors' : {
        'meta_info' : _MetaInfoClass('Rsvp.Neighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.Neighbors.Neighbor', 
                [], [], 
                '''                RSVP neighbor configuration
                ''',
                'neighbor',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.Controllers.Controller.CntlSignalling.OutOfBand' : {
        'meta_info' : _MetaInfoClass('Rsvp.Controllers.Controller.CntlSignalling.OutOfBand',
            False, 
            [
            _MetaInfoClassMember('missed-messages', ATTRIBUTE, 'int' , None, None, 
                [('1', '110000')], [], 
                '''                Configure max number of consecutive missed
                messages for state expiry for out-of-band
                tunnels
                ''',
                'missed_messages',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('refresh-interval', ATTRIBUTE, 'int' , None, None, 
                [('180', '86400')], [], 
                '''                Configure interval between successive refreshes
                for out-of-band tunnels
                ''',
                'refresh_interval',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'out-of-band',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.Controllers.Controller.CntlSignalling' : {
        'meta_info' : _MetaInfoClass('Rsvp.Controllers.Controller.CntlSignalling',
            False, 
            [
            _MetaInfoClassMember('out-of-band', REFERENCE_CLASS, 'OutOfBand' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.Controllers.Controller.CntlSignalling.OutOfBand', 
                [], [], 
                '''                Configure RSVP out-of-band signalling parameters
                ''',
                'out_of_band',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'cntl-signalling',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.Controllers.Controller' : {
        'meta_info' : _MetaInfoClass('Rsvp.Controllers.Controller',
            False, 
            [
            _MetaInfoClassMember('controller-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of controller
                ''',
                'controller_name',
                'Cisco-IOS-XR-ip-rsvp-cfg', True),
            _MetaInfoClassMember('cntl-signalling', REFERENCE_CLASS, 'CntlSignalling' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.Controllers.Controller.CntlSignalling', 
                [], [], 
                '''                Configure RSVP signalling parameters
                ''',
                'cntl_signalling',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable RSVP on an interface
                ''',
                'enable',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'controller',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.Controllers' : {
        'meta_info' : _MetaInfoClass('Rsvp.Controllers',
            False, 
            [
            _MetaInfoClassMember('controller', REFERENCE_LIST, 'Controller' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.Controllers.Controller', 
                [], [], 
                '''                Controller configuration
                ''',
                'controller',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'controllers',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.GlobalLogging' : {
        'meta_info' : _MetaInfoClass('Rsvp.GlobalLogging',
            False, 
            [
            _MetaInfoClassMember('log-issu-status', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ISSU Status Logging
                ''',
                'log_issu_status',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('log-nsr-status', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable NSR Status Logging
                ''',
                'log_nsr_status',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'global-logging',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.GlobalBandwidth.DefaultInterfacePercent.Mam' : {
        'meta_info' : _MetaInfoClass('Rsvp.GlobalBandwidth.DefaultInterfacePercent.Mam',
            False, 
            [
            _MetaInfoClassMember('bc0-percent', ATTRIBUTE, 'int' , None, None, 
                [('0', '10000')], [], 
                '''                Default BC0 pool I/F % B/W 
                ''',
                'bc0_percent',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('bc1-percent', ATTRIBUTE, 'int' , None, None, 
                [('0', '10000')], [], 
                '''                Default BC1 pool I/F % B/W 
                ''',
                'bc1_percent',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('max-res-percent', ATTRIBUTE, 'int' , None, None, 
                [('0', '10000')], [], 
                '''                Default maximum reservable I/F % B/W 
                ''',
                'max_res_percent',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'mam',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.GlobalBandwidth.DefaultInterfacePercent.Rdm' : {
        'meta_info' : _MetaInfoClass('Rsvp.GlobalBandwidth.DefaultInterfacePercent.Rdm',
            False, 
            [
            _MetaInfoClassMember('bc0-percent', ATTRIBUTE, 'int' , None, None, 
                [('0', '10000')], [], 
                '''                Default BC0 pool I/F % B/W 
                ''',
                'bc0_percent',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('bc1-percent', ATTRIBUTE, 'int' , None, None, 
                [('0', '10000')], [], 
                '''                Default BC1 pool I/F % B/W 
                ''',
                'bc1_percent',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'rdm',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.GlobalBandwidth.DefaultInterfacePercent' : {
        'meta_info' : _MetaInfoClass('Rsvp.GlobalBandwidth.DefaultInterfacePercent',
            False, 
            [
            _MetaInfoClassMember('mam', REFERENCE_CLASS, 'Mam' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.GlobalBandwidth.DefaultInterfacePercent.Mam', 
                [], [], 
                '''                Configure global default MAM I/F percent
                bandwidth parameters
                ''',
                'mam',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('rdm', REFERENCE_CLASS, 'Rdm' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.GlobalBandwidth.DefaultInterfacePercent.Rdm', 
                [], [], 
                '''                Configure global default RDM I/F percent
                bandwidth parameters
                ''',
                'rdm',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'default-interface-percent',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.GlobalBandwidth' : {
        'meta_info' : _MetaInfoClass('Rsvp.GlobalBandwidth',
            False, 
            [
            _MetaInfoClassMember('default-interface-percent', REFERENCE_CLASS, 'DefaultInterfacePercent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.GlobalBandwidth.DefaultInterfacePercent', 
                [], [], 
                '''                Configure Global RSVP signalling parameters
                ''',
                'default_interface_percent',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'global-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.Interfaces.Interface.IfSignalling.RefreshReduction' : {
        'meta_info' : _MetaInfoClass('Rsvp.Interfaces.Interface.IfSignalling.RefreshReduction',
            False, 
            [
            _MetaInfoClassMember('bundle-message-max-size', ATTRIBUTE, 'int' , None, None, 
                [('512', '65000')], [], 
                '''                Configure maximum size of a single RSVP
                Bundle message
                ''',
                'bundle_message_max_size',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable refresh reduction
                ''',
                'disable',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('reliable-ack-hold-time', ATTRIBUTE, 'int' , None, None, 
                [('100', '5000')], [], 
                '''                Configure hold time for sending RSVP ACK
                message(s)
                ''',
                'reliable_ack_hold_time',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('reliable-ack-max-size', ATTRIBUTE, 'int' , None, None, 
                [('20', '65000')], [], 
                '''                Configure max size of a single RSVP ACK
                message
                ''',
                'reliable_ack_max_size',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('reliable-retransmit-time', ATTRIBUTE, 'int' , None, None, 
                [('100', '10000')], [], 
                '''                Configure min delay to wait for an ACK
                before a retransmit
                ''',
                'reliable_retransmit_time',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('reliable-s-refresh', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure use of reliable messaging for
                summary refresh
                ''',
                'reliable_s_refresh',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('summary-max-size', ATTRIBUTE, 'int' , None, None, 
                [('20', '65000')], [], 
                '''                Configure max size of a single RSVP summary
                refresh message
                ''',
                'summary_max_size',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'refresh-reduction',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.Interfaces.Interface.IfSignalling.IntervalRate' : {
        'meta_info' : _MetaInfoClass('Rsvp.Interfaces.Interface.IfSignalling.IntervalRate',
            False, 
            [
            _MetaInfoClassMember('interval-size', ATTRIBUTE, 'int' , None, None, 
                [('250', '2000')], [], 
                '''                Size of an interval (milliseconds)
                ''',
                'interval_size',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('messages-per-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '500')], [], 
                '''                Number of messages to be sent per interval
                ''',
                'messages_per_interval',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'interval-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.Interfaces.Interface.IfSignalling.OutOfBand' : {
        'meta_info' : _MetaInfoClass('Rsvp.Interfaces.Interface.IfSignalling.OutOfBand',
            False, 
            [
            _MetaInfoClassMember('missed-messages', ATTRIBUTE, 'int' , None, None, 
                [('1', '110000')], [], 
                '''                Configure max number of consecutive missed
                messages for state expiry for out-of-band
                tunnels
                ''',
                'missed_messages',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('refresh-interval', ATTRIBUTE, 'int' , None, None, 
                [('180', '86400')], [], 
                '''                Configure interval between successive refreshes
                for out-of-band tunnels
                ''',
                'refresh_interval',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'out-of-band',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.Interfaces.Interface.IfSignalling' : {
        'meta_info' : _MetaInfoClass('Rsvp.Interfaces.Interface.IfSignalling',
            False, 
            [
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                Differentiated Services Code Point (DSCP)
                ''',
                'dscp',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('hello-graceful-restart-if-based', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable IF-based Hello adjacency on a RSVP
                interface
                ''',
                'hello_graceful_restart_if_based',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('interval-rate', REFERENCE_CLASS, 'IntervalRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.Interfaces.Interface.IfSignalling.IntervalRate', 
                [], [], 
                '''                Configure number of messages to be sent per
                interval
                ''',
                'interval_rate',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('missed-messages', ATTRIBUTE, 'int' , None, None, 
                [('1', '8')], [], 
                '''                Configure max number of consecutive missed
                messages for state expiry
                ''',
                'missed_messages',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('out-of-band', REFERENCE_CLASS, 'OutOfBand' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.Interfaces.Interface.IfSignalling.OutOfBand', 
                [], [], 
                '''                Configure RSVP out-of-band signalling parameters
                ''',
                'out_of_band',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('pacing', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable rate-limiting on the interface
                ''',
                'pacing',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('refresh-interval', ATTRIBUTE, 'int' , None, None, 
                [('10', '180')], [], 
                '''                Configure interval between successive
                refreshes
                ''',
                'refresh_interval',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('refresh-reduction', REFERENCE_CLASS, 'RefreshReduction' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.Interfaces.Interface.IfSignalling.RefreshReduction', 
                [], [], 
                '''                Configure RSVP Refresh Reduction parameters
                ''',
                'refresh_reduction',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'if-signalling',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.Interfaces.Interface.Bandwidth.Mam' : {
        'meta_info' : _MetaInfoClass('Rsvp.Interfaces.Interface.Bandwidth.Mam',
            False, 
            [
            _MetaInfoClassMember('bandwidth-mode', REFERENCE_ENUM_CLASS, 'RsvpBwCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'RsvpBwCfgEnum', 
                [], [], 
                '''                Absolute or Percentage bandwidth mode
                ''',
                'bandwidth_mode',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('bc0-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reservable bandwidth in BC0 (Kbps or percent
                of physical bandwidth)
                ''',
                'bc0_bandwidth',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('bc1-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reservable bandwidth in BC1 (Kbps or percent
                of physical bandwidth)
                ''',
                'bc1_bandwidth',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('max-resv-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum reservable bandwidth (Kbps or
                percent of physical bandwidth)
                ''',
                'max_resv_bandwidth',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('max-resv-flow', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Largest reservable flow (Kbps or percent of
                physical bandwidth)
                ''',
                'max_resv_flow',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'mam',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.Interfaces.Interface.Bandwidth.Rdm' : {
        'meta_info' : _MetaInfoClass('Rsvp.Interfaces.Interface.Bandwidth.Rdm',
            False, 
            [
            _MetaInfoClassMember('bandwidth-mode', REFERENCE_ENUM_CLASS, 'RsvpBwCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'RsvpBwCfgEnum', 
                [], [], 
                '''                Absolute or Percentage bandwidth mode
                ''',
                'bandwidth_mode',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('bc0-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reservable bandwidth in BC0 (Kbps or percent
                of physical bandwidth)
                ''',
                'bc0_bandwidth',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('bc0-keyword', REFERENCE_ENUM_CLASS, 'RsvpBc0Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'RsvpBc0Enum', 
                [], [], 
                '''                Set requests should always use BC0
                ''',
                'bc0_keyword',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('bc1-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reservable bandwidth in BC1 (Kbps or percent
                of physical bandwidth)
                ''',
                'bc1_bandwidth',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('bc1-keyword', REFERENCE_ENUM_CLASS, 'RsvpBc1Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'RsvpBc1Enum', 
                [], [], 
                '''                Set requests should always use BC1
                ''',
                'bc1_keyword',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('max-resv-flow', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Largest reservable flow (Kbps or percent of
                physical bandwidth)
                ''',
                'max_resv_flow',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('rdm-keyword', REFERENCE_ENUM_CLASS, 'RsvpRdmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'RsvpRdmEnum', 
                [], [], 
                '''                Set requests should always use RDM
                ''',
                'rdm_keyword',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'rdm',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.Interfaces.Interface.Bandwidth' : {
        'meta_info' : _MetaInfoClass('Rsvp.Interfaces.Interface.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('mam', REFERENCE_CLASS, 'Mam' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.Interfaces.Interface.Bandwidth.Mam', 
                [], [], 
                '''                Configure MAM bandwidth parameters
                ''',
                'mam',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('rdm', REFERENCE_CLASS, 'Rdm' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.Interfaces.Interface.Bandwidth.Rdm', 
                [], [], 
                '''                Configure RDM bandwidth parameters
                ''',
                'rdm',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.Interfaces.Interface.Authentication' : {
        'meta_info' : _MetaInfoClass('Rsvp.Interfaces.Interface.Authentication',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable RSVP authentication
                ''',
                'enable',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('key-chain', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Key chain to authenticate RSVP signalling
                messages
                ''',
                'key_chain',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('life-time', ATTRIBUTE, 'int' , None, None, 
                [('30', '86400')], [], 
                '''                Life time (in seconds) for each security
                association
                ''',
                'life_time',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('window-size', ATTRIBUTE, 'int' , None, None, 
                [('1', '64')], [], 
                '''                Window-size to limit number of out-of-order
                messages
                ''',
                'window_size',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Rsvp.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of interface
                ''',
                'name',
                'Cisco-IOS-XR-ip-rsvp-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.Interfaces.Interface.Authentication', 
                [], [], 
                '''                Configure RSVP authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.Interfaces.Interface.Bandwidth', 
                [], [], 
                '''                Configure Bandwidth
                ''',
                'bandwidth',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable RSVP on an interface
                ''',
                'enable',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('if-signalling', REFERENCE_CLASS, 'IfSignalling' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.Interfaces.Interface.IfSignalling', 
                [], [], 
                '''                Configure RSVP signalling parameters
                ''',
                'if_signalling',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.Interfaces' : {
        'meta_info' : _MetaInfoClass('Rsvp.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.Interfaces.Interface', 
                [], [], 
                '''                Interface configuration
                ''',
                'interface',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.Signalling.GlobalOutOfBand' : {
        'meta_info' : _MetaInfoClass('Rsvp.Signalling.GlobalOutOfBand',
            False, 
            [
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                VRF used for out-of-band control signalling
                ''',
                'vrf',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'global-out-of-band',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.Signalling.GracefulRestart' : {
        'meta_info' : _MetaInfoClass('Rsvp.Signalling.GracefulRestart',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable RSVP graceful restart
                ''',
                'enable',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('recovery-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Graceful restart recovery time (seconds)
                ''',
                'recovery_time',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('restart-time', ATTRIBUTE, 'int' , None, None, 
                [('60', '3600')], [], 
                '''                Graceful restart time (seconds)
                ''',
                'restart_time',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'graceful-restart',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.Signalling.PrefixFiltering.DefaultDenyAction' : {
        'meta_info' : _MetaInfoClass('Rsvp.Signalling.PrefixFiltering.DefaultDenyAction',
            False, 
            [
            _MetaInfoClassMember('drop', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure RSVP to drop packets when ACL match
                yields a default (implicit) deny
                ''',
                'drop',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'default-deny-action',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.Signalling.PrefixFiltering' : {
        'meta_info' : _MetaInfoClass('Rsvp.Signalling.PrefixFiltering',
            False, 
            [
            _MetaInfoClassMember('acl', ATTRIBUTE, 'str' , None, None, 
                [(1, 65)], [], 
                '''                Configure an ACL to perform prefix filtering
                of RSVP Router Alert messages
                ''',
                'acl',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('default-deny-action', REFERENCE_CLASS, 'DefaultDenyAction' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.Signalling.PrefixFiltering.DefaultDenyAction', 
                [], [], 
                '''                Configure RSVP behaviour for scenarios where
                ACL match yields a default (implicit) deny
                ''',
                'default_deny_action',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'prefix-filtering',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.Signalling.Pesr' : {
        'meta_info' : _MetaInfoClass('Rsvp.Signalling.Pesr',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable RSVP PESR
                ''',
                'disable',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'pesr',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.Signalling.Checksum' : {
        'meta_info' : _MetaInfoClass('Rsvp.Signalling.Checksum',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable RSVP message checksum computation
                ''',
                'disable',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'checksum',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.Signalling' : {
        'meta_info' : _MetaInfoClass('Rsvp.Signalling',
            False, 
            [
            _MetaInfoClassMember('checksum', REFERENCE_CLASS, 'Checksum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.Signalling.Checksum', 
                [], [], 
                '''                RSVP message checksum computation
                ''',
                'checksum',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('global-out-of-band', REFERENCE_CLASS, 'GlobalOutOfBand' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.Signalling.GlobalOutOfBand', 
                [], [], 
                '''                Configure out-of-band signalling parameters
                ''',
                'global_out_of_band',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('graceful-restart', REFERENCE_CLASS, 'GracefulRestart' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.Signalling.GracefulRestart', 
                [], [], 
                '''                Configure RSVP Graceful-Restart parameters
                ''',
                'graceful_restart',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('hello-graceful-restart-interval', ATTRIBUTE, 'int' , None, None, 
                [('3000', '30000')], [], 
                '''                Configure interval between successive Hello
                messages
                ''',
                'hello_graceful_restart_interval',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('hello-graceful-restart-misses', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                Configure max number of consecutive missed
                Hello messages
                ''',
                'hello_graceful_restart_misses',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('pesr', REFERENCE_CLASS, 'Pesr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.Signalling.Pesr', 
                [], [], 
                '''                Sending Path Error with State-Removal flag
                ''',
                'pesr',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('prefix-filtering', REFERENCE_CLASS, 'PrefixFiltering' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.Signalling.PrefixFiltering', 
                [], [], 
                '''                Configure prefix filtering parameters
                ''',
                'prefix_filtering',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'signalling',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp.Authentication' : {
        'meta_info' : _MetaInfoClass('Rsvp.Authentication',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable RSVP authentication
                ''',
                'enable',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('key-chain', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Key chain to authenticate RSVP signalling
                messages
                ''',
                'key_chain',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('life-time', ATTRIBUTE, 'int' , None, None, 
                [('30', '86400')], [], 
                '''                Life time (in seconds) for each security
                association
                ''',
                'life_time',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('window-size', ATTRIBUTE, 'int' , None, None, 
                [('1', '64')], [], 
                '''                Window-size to limit number of out-of-order
                messages
                ''',
                'window_size',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
    'Rsvp' : {
        'meta_info' : _MetaInfoClass('Rsvp',
            False, 
            [
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.Authentication', 
                [], [], 
                '''                Configure RSVP authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('controllers', REFERENCE_CLASS, 'Controllers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.Controllers', 
                [], [], 
                '''                Controller table
                ''',
                'controllers',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('global-bandwidth', REFERENCE_CLASS, 'GlobalBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.GlobalBandwidth', 
                [], [], 
                '''                Configure Global Bandwidth Parameters
                ''',
                'global_bandwidth',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('global-logging', REFERENCE_CLASS, 'GlobalLogging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.GlobalLogging', 
                [], [], 
                '''                Global Logging
                ''',
                'global_logging',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.Interfaces', 
                [], [], 
                '''                Interface table
                ''',
                'interfaces',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.Neighbors', 
                [], [], 
                '''                RSVP Neighbor Table
                ''',
                'neighbors',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('signalling', REFERENCE_CLASS, 'Signalling' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg', 'Rsvp.Signalling', 
                [], [], 
                '''                Configure Global RSVP signalling parameters
                ''',
                'signalling',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'rsvp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg'
        ),
    },
}
_meta_table['Rsvp.Neighbors.Neighbor.Authentication']['meta_info'].parent =_meta_table['Rsvp.Neighbors.Neighbor']['meta_info']
_meta_table['Rsvp.Neighbors.Neighbor']['meta_info'].parent =_meta_table['Rsvp.Neighbors']['meta_info']
_meta_table['Rsvp.Controllers.Controller.CntlSignalling.OutOfBand']['meta_info'].parent =_meta_table['Rsvp.Controllers.Controller.CntlSignalling']['meta_info']
_meta_table['Rsvp.Controllers.Controller.CntlSignalling']['meta_info'].parent =_meta_table['Rsvp.Controllers.Controller']['meta_info']
_meta_table['Rsvp.Controllers.Controller']['meta_info'].parent =_meta_table['Rsvp.Controllers']['meta_info']
_meta_table['Rsvp.GlobalBandwidth.DefaultInterfacePercent.Mam']['meta_info'].parent =_meta_table['Rsvp.GlobalBandwidth.DefaultInterfacePercent']['meta_info']
_meta_table['Rsvp.GlobalBandwidth.DefaultInterfacePercent.Rdm']['meta_info'].parent =_meta_table['Rsvp.GlobalBandwidth.DefaultInterfacePercent']['meta_info']
_meta_table['Rsvp.GlobalBandwidth.DefaultInterfacePercent']['meta_info'].parent =_meta_table['Rsvp.GlobalBandwidth']['meta_info']
_meta_table['Rsvp.Interfaces.Interface.IfSignalling.RefreshReduction']['meta_info'].parent =_meta_table['Rsvp.Interfaces.Interface.IfSignalling']['meta_info']
_meta_table['Rsvp.Interfaces.Interface.IfSignalling.IntervalRate']['meta_info'].parent =_meta_table['Rsvp.Interfaces.Interface.IfSignalling']['meta_info']
_meta_table['Rsvp.Interfaces.Interface.IfSignalling.OutOfBand']['meta_info'].parent =_meta_table['Rsvp.Interfaces.Interface.IfSignalling']['meta_info']
_meta_table['Rsvp.Interfaces.Interface.Bandwidth.Mam']['meta_info'].parent =_meta_table['Rsvp.Interfaces.Interface.Bandwidth']['meta_info']
_meta_table['Rsvp.Interfaces.Interface.Bandwidth.Rdm']['meta_info'].parent =_meta_table['Rsvp.Interfaces.Interface.Bandwidth']['meta_info']
_meta_table['Rsvp.Interfaces.Interface.IfSignalling']['meta_info'].parent =_meta_table['Rsvp.Interfaces.Interface']['meta_info']
_meta_table['Rsvp.Interfaces.Interface.Bandwidth']['meta_info'].parent =_meta_table['Rsvp.Interfaces.Interface']['meta_info']
_meta_table['Rsvp.Interfaces.Interface.Authentication']['meta_info'].parent =_meta_table['Rsvp.Interfaces.Interface']['meta_info']
_meta_table['Rsvp.Interfaces.Interface']['meta_info'].parent =_meta_table['Rsvp.Interfaces']['meta_info']
_meta_table['Rsvp.Signalling.PrefixFiltering.DefaultDenyAction']['meta_info'].parent =_meta_table['Rsvp.Signalling.PrefixFiltering']['meta_info']
_meta_table['Rsvp.Signalling.GlobalOutOfBand']['meta_info'].parent =_meta_table['Rsvp.Signalling']['meta_info']
_meta_table['Rsvp.Signalling.GracefulRestart']['meta_info'].parent =_meta_table['Rsvp.Signalling']['meta_info']
_meta_table['Rsvp.Signalling.PrefixFiltering']['meta_info'].parent =_meta_table['Rsvp.Signalling']['meta_info']
_meta_table['Rsvp.Signalling.Pesr']['meta_info'].parent =_meta_table['Rsvp.Signalling']['meta_info']
_meta_table['Rsvp.Signalling.Checksum']['meta_info'].parent =_meta_table['Rsvp.Signalling']['meta_info']
_meta_table['Rsvp.Neighbors']['meta_info'].parent =_meta_table['Rsvp']['meta_info']
_meta_table['Rsvp.Controllers']['meta_info'].parent =_meta_table['Rsvp']['meta_info']
_meta_table['Rsvp.GlobalLogging']['meta_info'].parent =_meta_table['Rsvp']['meta_info']
_meta_table['Rsvp.GlobalBandwidth']['meta_info'].parent =_meta_table['Rsvp']['meta_info']
_meta_table['Rsvp.Interfaces']['meta_info'].parent =_meta_table['Rsvp']['meta_info']
_meta_table['Rsvp.Signalling']['meta_info'].parent =_meta_table['Rsvp']['meta_info']
_meta_table['Rsvp.Authentication']['meta_info'].parent =_meta_table['Rsvp']['meta_info']

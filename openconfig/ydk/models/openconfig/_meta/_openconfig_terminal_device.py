


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'TerminalDevice.Config' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.Config',
            False, 
            [
            ],
            'openconfig-terminal-device',
            'config',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.State' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.State',
            False, 
            [
            ],
            'openconfig-terminal-device',
            'state',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.Config' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.Config',
            False, 
            [
            _MetaInfoClassMember('admin-state', REFERENCE_ENUM_CLASS, 'AdminStateTypeEnum' , 'ydk.models.openconfig.openconfig_transport_types', 'AdminStateTypeEnum', 
                [], [], 
                '''                Sets the admin state of the logical channel
                ''',
                'admin_state',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description of the logical channel
                ''',
                'description',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index of the current logical channel
                ''',
                'index',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('logical-channel-type', REFERENCE_IDENTITY_CLASS, 'Logical_Element_Protocol_TypeIdentity' , 'ydk.models.openconfig.openconfig_transport_types', 'Logical_Element_Protocol_TypeIdentity', 
                [], [], 
                '''                The type / stage of the logical element determines the
                configuration and operational state parameters (PMs)
                available for the logical element
                ''',
                'logical_channel_type',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('loopback-mode', REFERENCE_ENUM_CLASS, 'LoopbackModeTypeEnum' , 'ydk.models.openconfig.openconfig_transport_types', 'LoopbackModeTypeEnum', 
                [], [], 
                '''                Sets the loopback type on the logical channel. Setting the
                mode to something besides NONE activates the loopback in
                the specified mode.
                ''',
                'loopback_mode',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('rate-class', REFERENCE_IDENTITY_CLASS, 'Tributary_Rate_Class_TypeIdentity' , 'ydk.models.openconfig.openconfig_transport_types', 'Tributary_Rate_Class_TypeIdentity', 
                [], [], 
                '''                Rounded bit rate of the tributary signal. Exact bit rate
                will be refined by protocol selection.
                ''',
                'rate_class',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('trib-protocol', REFERENCE_IDENTITY_CLASS, 'Tributary_Protocol_TypeIdentity' , 'ydk.models.openconfig.openconfig_transport_types', 'Tributary_Protocol_TypeIdentity', 
                [], [], 
                '''                Protocol framing of the tributary signal. If this
                LogicalChannel is directly connected to a Client-Port or
                Optical-Channel, this is the protocol of the associated port.
                If the LogicalChannel is connected to other LogicalChannels,
                the TributaryProtocol of the LogicalChannels will define a
                specific mapping/demapping or multiplexing/demultiplexing
                function.
                
                Not all protocols are valid, depending on the value
                of trib-rate-class.  The expectation is that the NMS
                will validate that a correct combination of rate class
                and protocol are specfied.  Basic combinations are:
                
                rate class: 1G
                protocols: 1GE
                
                rate class: 2.5G
                protocols: OC48, STM16
                
                rate class: 10G
                protocols:  10GE LAN, 10GE WAN, OC192, STM64, OTU2, OTU2e,
                           OTU1e, ODU2, ODU2e, ODU1e
                
                rate class: 40G
                protocols:  40GE, OC768, STM256, OTU3, ODU3
                
                rate class: 100G
                protocols:  100GE, 100G MLG, OTU4, OTUCn, ODU4
                ''',
                'trib_protocol',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'config',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.State.LinkStateEnum' : _MetaInfoEnum('LinkStateEnum', 'ydk.models.openconfig.openconfig_terminal_device',
        {
            'UP':'UP',
            'DOWN':'DOWN',
        }, 'openconfig-terminal-device', _yang_ns._namespaces['openconfig-terminal-device']),
    'TerminalDevice.LogicalChannels.Channel.State' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.State',
            False, 
            [
            _MetaInfoClassMember('admin-state', REFERENCE_ENUM_CLASS, 'AdminStateTypeEnum' , 'ydk.models.openconfig.openconfig_transport_types', 'AdminStateTypeEnum', 
                [], [], 
                '''                Sets the admin state of the logical channel
                ''',
                'admin_state',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description of the logical channel
                ''',
                'description',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index of the current logical channel
                ''',
                'index',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('link-state', REFERENCE_ENUM_CLASS, 'LinkStateEnum' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.State.LinkStateEnum', 
                [], [], 
                '''                Link-state of the Ethernet protocol on the logical channel,
                SONET / SDH framed signal, etc.
                ''',
                'link_state',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('logical-channel-type', REFERENCE_IDENTITY_CLASS, 'Logical_Element_Protocol_TypeIdentity' , 'ydk.models.openconfig.openconfig_transport_types', 'Logical_Element_Protocol_TypeIdentity', 
                [], [], 
                '''                The type / stage of the logical element determines the
                configuration and operational state parameters (PMs)
                available for the logical element
                ''',
                'logical_channel_type',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('loopback-mode', REFERENCE_ENUM_CLASS, 'LoopbackModeTypeEnum' , 'ydk.models.openconfig.openconfig_transport_types', 'LoopbackModeTypeEnum', 
                [], [], 
                '''                Sets the loopback type on the logical channel. Setting the
                mode to something besides NONE activates the loopback in
                the specified mode.
                ''',
                'loopback_mode',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('rate-class', REFERENCE_IDENTITY_CLASS, 'Tributary_Rate_Class_TypeIdentity' , 'ydk.models.openconfig.openconfig_transport_types', 'Tributary_Rate_Class_TypeIdentity', 
                [], [], 
                '''                Rounded bit rate of the tributary signal. Exact bit rate
                will be refined by protocol selection.
                ''',
                'rate_class',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('trib-protocol', REFERENCE_IDENTITY_CLASS, 'Tributary_Protocol_TypeIdentity' , 'ydk.models.openconfig.openconfig_transport_types', 'Tributary_Protocol_TypeIdentity', 
                [], [], 
                '''                Protocol framing of the tributary signal. If this
                LogicalChannel is directly connected to a Client-Port or
                Optical-Channel, this is the protocol of the associated port.
                If the LogicalChannel is connected to other LogicalChannels,
                the TributaryProtocol of the LogicalChannels will define a
                specific mapping/demapping or multiplexing/demultiplexing
                function.
                
                Not all protocols are valid, depending on the value
                of trib-rate-class.  The expectation is that the NMS
                will validate that a correct combination of rate class
                and protocol are specfied.  Basic combinations are:
                
                rate class: 1G
                protocols: 1GE
                
                rate class: 2.5G
                protocols: OC48, STM16
                
                rate class: 10G
                protocols:  10GE LAN, 10GE WAN, OC192, STM64, OTU2, OTU2e,
                           OTU1e, ODU2, ODU2e, ODU1e
                
                rate class: 40G
                protocols:  40GE, OC768, STM256, OTU3, ODU3
                
                rate class: 100G
                protocols:  100GE, 100G MLG, OTU4, OTUCn, ODU4
                ''',
                'trib_protocol',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'state',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.Otn.Config' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.Otn.Config',
            False, 
            [
            _MetaInfoClassMember('tti-msg-auto', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Trail trace identifier (TTI) transmit message automatically created.
                If True, then setting a custom transmit message would be invalid.
                ''',
                'tti_msg_auto',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('tti-msg-expected', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trail trace identifier (TTI) message expected
                ''',
                'tti_msg_expected',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('tti-msg-transmit', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trail trace identifier (TTI) message transmitted
                ''',
                'tti_msg_transmit',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'config',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.Otn.State.PreFecBer' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.Otn.State.PreFecBer',
            False, 
            [
            _MetaInfoClassMember('avg', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The arithmetic mean value of the statistic over the
                sampling period.
                ''',
                'avg',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('instant', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The instantaneous value of the statistic.
                ''',
                'instant',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('max', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The maximum value of the statitic over the sampling
                period
                ''',
                'max',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('min', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The minimum value of the statistic over the sampling
                period
                ''',
                'min',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'pre-fec-ber',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.Otn.State.PostFecBer' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.Otn.State.PostFecBer',
            False, 
            [
            _MetaInfoClassMember('avg', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The arithmetic mean value of the statistic over the
                sampling period.
                ''',
                'avg',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('instant', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The instantaneous value of the statistic.
                ''',
                'instant',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('max', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The maximum value of the statitic over the sampling
                period
                ''',
                'max',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('min', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The minimum value of the statistic over the sampling
                period
                ''',
                'min',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'post-fec-ber',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.Otn.State.QValue' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.Otn.State.QValue',
            False, 
            [
            _MetaInfoClassMember('avg', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The arithmetic mean value of the statistic over the
                sampling period.
                ''',
                'avg',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('instant', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The instantaneous value of the statistic.
                ''',
                'instant',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('max', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The maximum value of the statitic over the sampling
                period
                ''',
                'max',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('min', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The minimum value of the statistic over the sampling
                period
                ''',
                'min',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'q-value',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr',
            False, 
            [
            _MetaInfoClassMember('avg', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The arithmetic mean value of the statistic over the
                sampling period.
                ''',
                'avg',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('instant', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The instantaneous value of the statistic.
                ''',
                'instant',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('max', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The maximum value of the statitic over the sampling
                period
                ''',
                'max',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('min', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The minimum value of the statistic over the sampling
                period
                ''',
                'min',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'esnr',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.Otn.State' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.Otn.State',
            False, 
            [
            _MetaInfoClassMember('background-block-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of background block errors
                ''',
                'background_block_errors',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('code-violations', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                For ethernet or fiberchannel links, the number of 8b/10b
                coding violations. For SONET/SDH, the number of BIP (bit
                interleaved parity) errors
                ''',
                'code_violations',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('errored-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of seconds that at least one errored blocks occurs,
                at least one code violation occurs, loss of sync is detected or
                loss of signal is detected
                ''',
                'errored_seconds',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('esnr', REFERENCE_CLASS, 'Esnr' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr', 
                [], [], 
                '''                Electrical signal to noise ratio. Baud rate
                normalized signal to noise ratio based on
                error vector magnitude
                ''',
                'esnr',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('fec-corrected-bits', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of bits that were corrected by the FEC
                ''',
                'fec_corrected_bits',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('fec-corrected-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of bytes that were corrected by the FEC
                ''',
                'fec_corrected_bytes',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('fec-uncorrectable-words', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number words that were uncorrectable by the FEC
                ''',
                'fec_uncorrectable_words',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('post-fec-ber', REFERENCE_CLASS, 'PostFecBer' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.Otn.State.PostFecBer', 
                [], [], 
                '''                Bit error rate after forward error correction -- computed
                value
                ''',
                'post_fec_ber',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('pre-fec-ber', REFERENCE_CLASS, 'PreFecBer' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.Otn.State.PreFecBer', 
                [], [], 
                '''                Bit error rate before forward error correction -- computed
                value
                ''',
                'pre_fec_ber',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('q-value', REFERENCE_CLASS, 'QValue' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.Otn.State.QValue', 
                [], [], 
                '''                Quality value (factor) of a channel
                ''',
                'q_value',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('rdi-msg', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Remote defect indication (RDI) message received
                ''',
                'rdi_msg',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('severely-errored-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of seconds that loss of frame is detected OR
                the number of errored blocks, code violations, loss of sync or
                loss of signal is detected exceeds a predefined threshold
                ''',
                'severely_errored_seconds',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('tti-msg-auto', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Trail trace identifier (TTI) transmit message automatically created.
                If True, then setting a custom transmit message would be invalid.
                ''',
                'tti_msg_auto',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('tti-msg-expected', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trail trace identifier (TTI) message expected
                ''',
                'tti_msg_expected',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('tti-msg-recv', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trail trace identifier (TTI) message received
                ''',
                'tti_msg_recv',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('tti-msg-transmit', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trail trace identifier (TTI) message transmitted
                ''',
                'tti_msg_transmit',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('unavailable-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of seconds during which the link is unavailable
                ''',
                'unavailable_seconds',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'state',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.Otn' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.Otn',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.Otn.Config', 
                [], [], 
                '''                Configuration data for OTN protocol framing
                ''',
                'config',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.Otn.State', 
                [], [], 
                '''                Operational state data for OTN protocol PMs, statistics,
                etc.
                ''',
                'state',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'otn',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.Ethernet.Config' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.Ethernet.Config',
            False, 
            [
            ],
            'openconfig-terminal-device',
            'config',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.Ethernet.State' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.Ethernet.State',
            False, 
            [
            _MetaInfoClassMember('in-8021q-frames', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of 802.1q tagged frames received on the interface
                ''',
                'in_8021q_frames',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('in-crc-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of receive error events due to FCS/CRC check
                failure
                ''',
                'in_crc_errors',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('in-fragment-frames', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of fragment frames received on the interface.
                ''',
                'in_fragment_frames',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('in-jabber-frames', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of jabber frames received on the
                interface.  Jabber frames are typically defined as oversize
                frames which also have a bad CRC.  Implementations may use
                slightly different definitions of what constitutes a jabber
                frame.  Often indicative of a NIC hardware problem.
                ''',
                'in_jabber_frames',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('in-mac-control-frames', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                MAC layer control frames received on the interface
                ''',
                'in_mac_control_frames',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('in-mac-pause-frames', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                MAC layer PAUSE frames received on the interface
                ''',
                'in_mac_pause_frames',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('in-oversize-frames', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of oversize frames received on the interface
                ''',
                'in_oversize_frames',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('out-8021q-frames', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of 802.1q tagged frames sent on the interface
                ''',
                'out_8021q_frames',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('out-mac-control-frames', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                MAC layer control frames sent on the interface
                ''',
                'out_mac_control_frames',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('out-mac-pause-frames', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                MAC layer PAUSE frames sent on the interface
                ''',
                'out_mac_pause_frames',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'state',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.Ethernet' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.Ethernet',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.Ethernet.Config', 
                [], [], 
                '''                Configuration data for Ethernet protocol framing on logical
                channels
                ''',
                'config',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.Ethernet.State', 
                [], [], 
                '''                Operational state data for Ethernet protocol framing on logical
                channels
                ''',
                'state',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'ethernet',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.Ingress.Config' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.Ingress.Config',
            False, 
            [
            _MetaInfoClassMember('physical-channel', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This list should be populated with references
                to the client physical channels that feed this logical
                channel from the transceiver specified in the 'transceiver'
                leaf, which must be specified.  If this leaf-list is empty,
                all physical channels in the transceiver are assumed to be
                mapped to the logical channel.
                ''',
                'physical_channel',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('transceiver', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the transceiver carrying the input signal
                for the logical channel.  If specific physical channels
                are mapped to the logical channel (as opposed to all
                physical channels carried by the transceiver), they can be
                specified in the list of physical channel references.
                ''',
                'transceiver',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'config',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.Ingress.State' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.Ingress.State',
            False, 
            [
            _MetaInfoClassMember('physical-channel', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This list should be populated with references
                to the client physical channels that feed this logical
                channel from the transceiver specified in the 'transceiver'
                leaf, which must be specified.  If this leaf-list is empty,
                all physical channels in the transceiver are assumed to be
                mapped to the logical channel.
                ''',
                'physical_channel',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('transceiver', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the transceiver carrying the input signal
                for the logical channel.  If specific physical channels
                are mapped to the logical channel (as opposed to all
                physical channels carried by the transceiver), they can be
                specified in the list of physical channel references.
                ''',
                'transceiver',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'state',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.Ingress' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.Ingress',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.Ingress.Config', 
                [], [], 
                '''                Configuration data for the signal source for the
                logical channel
                ''',
                'config',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.Ingress.State', 
                [], [], 
                '''                Operational state data for the signal source for the
                logical channel
                ''',
                'state',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'ingress',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config.AssignmentTypeEnum' : _MetaInfoEnum('AssignmentTypeEnum', 'ydk.models.openconfig.openconfig_terminal_device',
        {
            'LOGICAL_CHANNEL':'LOGICAL_CHANNEL',
            'OPTICAL_CHANNEL':'OPTICAL_CHANNEL',
        }, 'openconfig-terminal-device', _yang_ns._namespaces['openconfig-terminal-device']),
    'TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config',
            False, 
            [
            _MetaInfoClassMember('allocation', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-9223372036854775.808', '9223372036854775.807')], [], 
                '''                Allocation of the logical client channel to the tributary
                or sub-channel, expressed in Gbps
                ''',
                'allocation',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('assignment-type', REFERENCE_ENUM_CLASS, 'AssignmentTypeEnum' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config.AssignmentTypeEnum', 
                [], [], 
                '''                Each logical channel element may be assigned to subsequent
                stages of logical elements to implement further grooming, or
                can be assigned to a line-side optical channel for
                transmission.  Each assignment also has an associated
                bandwidth allocation.
                ''',
                'assignment_type',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to the logical client channel
                ''',
                'description',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index of the current logical client channel to tributary
                mapping
                ''',
                'index',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('logical-channel', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reference to another stage of logical channel elements.
                ''',
                'logical_channel',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('optical-channel', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the line-side optical channel that should
                carry the current logical channel element.  Use this
                reference to exit the logical element stage.
                ''',
                'optical_channel',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'config',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State.AssignmentTypeEnum' : _MetaInfoEnum('AssignmentTypeEnum', 'ydk.models.openconfig.openconfig_terminal_device',
        {
            'LOGICAL_CHANNEL':'LOGICAL_CHANNEL',
            'OPTICAL_CHANNEL':'OPTICAL_CHANNEL',
        }, 'openconfig-terminal-device', _yang_ns._namespaces['openconfig-terminal-device']),
    'TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State',
            False, 
            [
            _MetaInfoClassMember('allocation', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-9223372036854775.808', '9223372036854775.807')], [], 
                '''                Allocation of the logical client channel to the tributary
                or sub-channel, expressed in Gbps
                ''',
                'allocation',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('assignment-type', REFERENCE_ENUM_CLASS, 'AssignmentTypeEnum' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State.AssignmentTypeEnum', 
                [], [], 
                '''                Each logical channel element may be assigned to subsequent
                stages of logical elements to implement further grooming, or
                can be assigned to a line-side optical channel for
                transmission.  Each assignment also has an associated
                bandwidth allocation.
                ''',
                'assignment_type',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to the logical client channel
                ''',
                'description',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index of the current logical client channel to tributary
                mapping
                ''',
                'index',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('logical-channel', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reference to another stage of logical channel elements.
                ''',
                'logical_channel',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('optical-channel', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the line-side optical channel that should
                carry the current logical channel element.  Use this
                reference to exit the logical element stage.
                ''',
                'optical_channel',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'state',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reference to the index for the current tributary
                assignment
                ''',
                'index',
                'openconfig-terminal-device', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config', 
                [], [], 
                '''                Configuration data for tributary assignments
                ''',
                'config',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State', 
                [], [], 
                '''                Operational state data for tributary assignments
                ''',
                'state',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'assignment',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments',
            False, 
            [
            _MetaInfoClassMember('assignment', REFERENCE_LIST, 'Assignment' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment', 
                [], [], 
                '''                Logical channel elements may be assigned directly to
                optical channels for line-side transmission, or can be
                further groomed into additional stages of logical channel
                elements.  The grooming can multiplex (i.e., split the
                current element into multiple elements in the subsequent
                stage) or de-multiplex (i.e., combine the current element
                with other elements into the same element in the subsequent
                stage) logical elements in each stage.
                
                Note that to support the ability to groom the logical
                elements, the list of logical channel elements should be
                populated with an entry for the logical elements at
                each stage, starting with the initial assignment from the
                respective client physical port.
                
                Each logical element assignment consists of a pointer to
                an element in the next stage, or to an optical channel,
                along with a bandwidth allocation for the corresponding
                assignment (e.g., to split or combine signal).
                ''',
                'assignment',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'logical-channel-assignments',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reference to the index of the logical channel
                ''',
                'index',
                'openconfig-terminal-device', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.Config', 
                [], [], 
                '''                Configuration data for logical channels
                ''',
                'config',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('ethernet', REFERENCE_CLASS, 'Ethernet' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.Ethernet', 
                [], [], 
                '''                Top level container for data related to Ethernet framing
                for the logical channel
                ''',
                'ethernet',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('ingress', REFERENCE_CLASS, 'Ingress' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.Ingress', 
                [], [], 
                '''                Top-level container for specifying references to the
                source of signal for the logical channel, either a
                transceiver or individual physical channels
                ''',
                'ingress',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('logical-channel-assignments', REFERENCE_CLASS, 'LogicalChannelAssignments' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments', 
                [], [], 
                '''                Enclosing container for tributary assignments
                ''',
                'logical_channel_assignments',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('otn', REFERENCE_CLASS, 'Otn' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.Otn', 
                [], [], 
                '''                Top level container for OTU configuration when logical
                channel framing is using an OTU protocol, e.g., OTU1, OTU3,
                etc.
                ''',
                'otn',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.State', 
                [], [], 
                '''                Operational state data for logical channels
                ''',
                'state',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'channel',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels',
            False, 
            [
            _MetaInfoClassMember('channel', REFERENCE_LIST, 'Channel' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel', 
                [], [], 
                '''                List of logical channels
                ''',
                'channel',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'logical-channels',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.OperationalModes.Mode.Config' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.OperationalModes.Mode.Config',
            False, 
            [
            ],
            'openconfig-terminal-device',
            'config',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.OperationalModes.Mode.State' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.OperationalModes.Mode.State',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Vendor-supplied textual description of the characteristics
                of this operational mode to enable operators to select the
                appropriate mode for the application.
                ''',
                'description',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('mode-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Two-octet encoding of the vendor-defined operational
                mode
                ''',
                'mode_id',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('vendor-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Identifier to represent the vendor / supplier of the
                platform and the associated operational mode information
                ''',
                'vendor_id',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'state',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.OperationalModes.Mode' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.OperationalModes.Mode',
            False, 
            [
            _MetaInfoClassMember('mode-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Reference to mode-id
                ''',
                'mode_id',
                'openconfig-terminal-device', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.OperationalModes.Mode.Config', 
                [], [], 
                '''                Configuration data for operational mode
                ''',
                'config',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.OperationalModes.Mode.State', 
                [], [], 
                '''                Operational state data for the platform-defined
                operational mode
                ''',
                'state',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'mode',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.OperationalModes' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.OperationalModes',
            False, 
            [
            _MetaInfoClassMember('mode', REFERENCE_LIST, 'Mode' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.OperationalModes.Mode', 
                [], [], 
                '''                List of operational modes supported by the platform.
                The operational mode provides a platform-defined summary
                of information such as symbol rate, modulation, pulse
                shaping, etc.
                ''',
                'mode',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'operational-modes',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice' : {
        'meta_info' : _MetaInfoClass('TerminalDevice',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.Config', 
                [], [], 
                '''                Configuration data for global terminal-device
                ''',
                'config',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('logical-channels', REFERENCE_CLASS, 'LogicalChannels' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels', 
                [], [], 
                '''                Enclosing container the list of logical channels
                ''',
                'logical_channels',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('operational-modes', REFERENCE_CLASS, 'OperationalModes' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.OperationalModes', 
                [], [], 
                '''                Enclosing container for list of operational modes
                ''',
                'operational_modes',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.State', 
                [], [], 
                '''                Operational state data for global terminal device
                ''',
                'state',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'terminal-device',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
}
_meta_table['TerminalDevice.LogicalChannels.Channel.Otn.State.PreFecBer']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel.Otn.State']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.Otn.State.PostFecBer']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel.Otn.State']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.Otn.State.QValue']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel.Otn.State']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel.Otn.State']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.Otn.Config']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel.Otn']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.Otn.State']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel.Otn']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.Ethernet.Config']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel.Ethernet']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.Ethernet.State']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel.Ethernet']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.Ingress.Config']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel.Ingress']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.Ingress.State']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel.Ingress']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.Config']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.State']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.Otn']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.Ethernet']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.Ingress']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels']['meta_info']
_meta_table['TerminalDevice.OperationalModes.Mode.Config']['meta_info'].parent =_meta_table['TerminalDevice.OperationalModes.Mode']['meta_info']
_meta_table['TerminalDevice.OperationalModes.Mode.State']['meta_info'].parent =_meta_table['TerminalDevice.OperationalModes.Mode']['meta_info']
_meta_table['TerminalDevice.OperationalModes.Mode']['meta_info'].parent =_meta_table['TerminalDevice.OperationalModes']['meta_info']
_meta_table['TerminalDevice.Config']['meta_info'].parent =_meta_table['TerminalDevice']['meta_info']
_meta_table['TerminalDevice.State']['meta_info'].parent =_meta_table['TerminalDevice']['meta_info']
_meta_table['TerminalDevice.LogicalChannels']['meta_info'].parent =_meta_table['TerminalDevice']['meta_info']
_meta_table['TerminalDevice.OperationalModes']['meta_info'].parent =_meta_table['TerminalDevice']['meta_info']

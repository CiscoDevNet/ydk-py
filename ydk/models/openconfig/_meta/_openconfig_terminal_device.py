


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

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
    'TerminalDevice.ClientPorts.Port.Config' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.ClientPorts.Port.Config',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the physical client port
                ''',
                'name',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Text description for the physical client port
                ''',
                'description',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'config',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.ClientPorts.Port.State' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.ClientPorts.Port.State',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the physical client port
                ''',
                'name',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Text description for the physical client port
                ''',
                'description',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('output-power', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The output optical power of this port in units of 0.01dBm.
                If the port is an aggregate of multiple physical channels,
                this attribute is the total power or sum of all channels.
                ''',
                'output_power',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('input-power', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The input optical power of this port in units of 0.01dBm.
                If the port is an aggregate of multiple physical channels,
                this attribute is the total power or sum of all channels.
                ''',
                'input_power',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('ethernet-compliance-code', REFERENCE_IDENTITY_CLASS, 'EthernetPmdType_Identity' , 'ydk.models.openconfig.openconfig_transport_types', 'EthernetPmdType_Identity', 
                [], [], 
                '''                Ethernet PMD that the transceiver supports. The SFF/QSFP
                MSAs have registers for this and CFP MSA has similar.
                ''',
                'ethernet_compliance_code',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('sonet-sdh-compliance-code', REFERENCE_IDENTITY_CLASS, 'SonetApplicationCode_Identity' , 'ydk.models.openconfig.openconfig_transport_types', 'SonetApplicationCode_Identity', 
                [], [], 
                '''                SONET/SDH application code supported by the port
                ''',
                'sonet_sdh_compliance_code',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('otn-compliance-code', REFERENCE_IDENTITY_CLASS, 'OtnApplicationCode_Identity' , 'ydk.models.openconfig.openconfig_transport_types', 'OtnApplicationCode_Identity', 
                [], [], 
                '''                OTN application code supported by the port
                ''',
                'otn_compliance_code',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'state',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.ClientPorts.Port.Transceiver.Config' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.ClientPorts.Port.Transceiver.Config',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Turns power on / off to the transceiver -- provides a means
                to power on/off the transceiver (in the case of SFP, SFP+,
                QSFP,...) or enable high-power mode (in the case of CFP,
                CFP2, CFP4) and is optionally supported (device can choose to
                always enable).  True = power on / high power, False =
                powered off
                ''',
                'enabled',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'config',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.ClientPorts.Port.Transceiver.State.PresentEnum' : _MetaInfoEnum('PresentEnum', 'ydk.models.openconfig.openconfig_terminal_device',
        {
            'PRESENT':'PRESENT',
            'NOT_PRESENT':'NOT_PRESENT',
        }, 'openconfig-terminal-device', _yang_ns._namespaces['openconfig-terminal-device']),
    'TerminalDevice.ClientPorts.Port.Transceiver.State' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.ClientPorts.Port.Transceiver.State',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Turns power on / off to the transceiver -- provides a means
                to power on/off the transceiver (in the case of SFP, SFP+,
                QSFP,...) or enable high-power mode (in the case of CFP,
                CFP2, CFP4) and is optionally supported (device can choose to
                always enable).  True = power on / high power, False =
                powered off
                ''',
                'enabled',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('present', REFERENCE_ENUM_CLASS, 'PresentEnum' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.ClientPorts.Port.Transceiver.State.PresentEnum', 
                [], [], 
                '''                Indicates whether a transceiver is present in
                the specified client port.
                ''',
                'present',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('form-factor', REFERENCE_IDENTITY_CLASS, 'TransceiverFormFactorType_Identity' , 'ydk.models.openconfig.openconfig_transport_types', 'TransceiverFormFactorType_Identity', 
                [], [], 
                '''                Indicates the type of optical transceiver used on this
                port.  If the client port is built into the device and not
                plugable, then non-pluggable is the corresponding state. If
                a device port supports multiple form factors (e.g. QSFP28
                and QSFP+, then the value of the transceiver installed shall
                be reported. If no transceiver is present, then the value of
                the highest rate form factor shall be reported
                (QSFP28, for example).
                ''',
                'form_factor',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('connector-type', REFERENCE_IDENTITY_CLASS, 'FiberConnectorType_Identity' , 'ydk.models.openconfig.openconfig_transport_types', 'FiberConnectorType_Identity', 
                [], [], 
                '''                Connector type used on this port
                ''',
                'connector_type',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('internal-temp', ATTRIBUTE, 'int' , None, None, 
                [(-40, 125)], [], 
                '''                Internally measured temperature in degrees Celsius. MSA
                valid range is between -40 and +125C. Accuracy shall be
                better than +/- 3 degC over the whole temperature range.
                ''',
                'internal_temp',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('vendor', ATTRIBUTE, 'str' , None, None, 
                [(1, 16)], [], 
                '''                Full name of transceiver vendor. 16-octet field that
                contains ASCII characters, left-aligned and padded on the
                right with ASCII spaces (20h)
                ''',
                'vendor',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('vendor-part', ATTRIBUTE, 'str' , None, None, 
                [(1, 16)], [], 
                '''                Transceiver vendor's part number. 16-octet field that
                contains ASCII characters, left-aligned and padded on the
                right with ASCII spaces (20h). If part number is undefined,
                all 16 octets = 0h
                ''',
                'vendor_part',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('vendor-rev', ATTRIBUTE, 'str' , None, None, 
                [(1, 2)], [], 
                '''                Transceiver vendor's revision number. 2-octet field that
                contains ASCII characters, left-aligned and padded on the
                right with ASCII spaces (20h)
                ''',
                'vendor_rev',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('serial-no', ATTRIBUTE, 'str' , None, None, 
                [(1, 16)], [], 
                '''                Transceiver serial number. 16-octet field that contains
                ASCII characters, left-aligned and padded on the right with
                ASCII spaces (20h). If part serial number is undefined, all
                16 octets = 0h
                ''',
                'serial_no',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('date-code', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Representation of the transceiver date code, typically
                stored as YYMMDD.  The time portion of the value is
                undefined and not intended to be read.
                ''',
                'date_code',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('fault-condition', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates if a fault condition exists in the transceiver
                ''',
                'fault_condition',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'state',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.ClientPorts.Port.Transceiver' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.ClientPorts.Port.Transceiver',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.ClientPorts.Port.Transceiver.Config', 
                [], [], 
                '''                Configuration data for client port transceivers
                ''',
                'config',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.ClientPorts.Port.Transceiver.State', 
                [], [], 
                '''                Operational state data for client port transceivers
                ''',
                'state',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'transceiver',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.ClientPorts.Port.PhysicalChannels.Channel.Config' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.ClientPorts.Port.PhysicalChannels.Channel.Config',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Index of the physical channnel or lane within a physical
                client port
                ''',
                'index',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Text description for the client physical channel
                ''',
                'description',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('tx-laser', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable (true) or disable (false) the transmit label for the
                channel
                ''',
                'tx_laser',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'config',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.ClientPorts.Port.PhysicalChannels.Channel.State' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.ClientPorts.Port.PhysicalChannels.Channel.State',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Index of the physical channnel or lane within a physical
                client port
                ''',
                'index',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Text description for the client physical channel
                ''',
                'description',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('tx-laser', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable (true) or disable (false) the transmit label for the
                channel
                ''',
                'tx_laser',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('output-power', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The output optical power of this port in units of 0.01dBm.
                If the port is an aggregate of multiple physical channels,
                this attribute is the total power or sum of all channels.
                ''',
                'output_power',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('output-frequency', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The frequency in MHz of the individual physical channel
                (e.g. ITU C50 - 195.0THz and would be reported as
                195,000,000 MHz in this model). This attribute is not
                configurable on most client ports.
                ''',
                'output_frequency',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'state',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.ClientPorts.Port.PhysicalChannels.Channel' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.ClientPorts.Port.PhysicalChannels.Channel',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Reference to the index number of the client channel
                ''',
                'index',
                'openconfig-terminal-device', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.ClientPorts.Port.PhysicalChannels.Channel.Config', 
                [], [], 
                '''                Configuration data 
                ''',
                'config',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.ClientPorts.Port.PhysicalChannels.Channel.State', 
                [], [], 
                '''                Operational state data for client channels
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
    'TerminalDevice.ClientPorts.Port.PhysicalChannels' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.ClientPorts.Port.PhysicalChannels',
            False, 
            [
            _MetaInfoClassMember('channel', REFERENCE_LIST, 'Channel' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.ClientPorts.Port.PhysicalChannels.Channel', 
                [], [], 
                '''                List of client channels, keyed by index within a physical
                client port.  A physical port with a single channel would
                have a single zero-indexed element
                ''',
                'channel',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'physical-channels',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.ClientPorts.Port.LogicalChannelAssignments.Assignment.Config' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.ClientPorts.Port.LogicalChannelAssignments.Assignment.Config',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Index of the client port assignment
                ''',
                'index',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Descriptive name for the client port-to-logical channel
                mapping
                ''',
                'description',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('logical-channel', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Reference to the logical channel for this
                assignment
                ''',
                'logical_channel',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('allocation', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-9223372036854775.808', '9223372036854775.807')], [], 
                '''                Allocation of the client physical port to the assigned
                logical channel expressed in Gbps.  In most cases,
                the full client physical port rate is assigned to a single
                logical channel.
                ''',
                'allocation',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'config',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.ClientPorts.Port.LogicalChannelAssignments.Assignment.State' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.ClientPorts.Port.LogicalChannelAssignments.Assignment.State',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Index of the client port assignment
                ''',
                'index',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Descriptive name for the client port-to-logical channel
                mapping
                ''',
                'description',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('logical-channel', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Reference to the logical channel for this
                assignment
                ''',
                'logical_channel',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('allocation', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-9223372036854775.808', '9223372036854775.807')], [], 
                '''                Allocation of the client physical port to the assigned
                logical channel expressed in Gbps.  In most cases,
                the full client physical port rate is assigned to a single
                logical channel.
                ''',
                'allocation',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'state',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.ClientPorts.Port.LogicalChannelAssignments.Assignment' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.ClientPorts.Port.LogicalChannelAssignments.Assignment',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Reference to the index of this logical client
                assignment
                ''',
                'index',
                'openconfig-terminal-device', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.ClientPorts.Port.LogicalChannelAssignments.Assignment.Config', 
                [], [], 
                '''                Configuration data for the logical client assignment
                ''',
                'config',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.ClientPorts.Port.LogicalChannelAssignments.Assignment.State', 
                [], [], 
                '''                Operational state data for the logical client
                assignment
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
    'TerminalDevice.ClientPorts.Port.LogicalChannelAssignments' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.ClientPorts.Port.LogicalChannelAssignments',
            False, 
            [
            _MetaInfoClassMember('assignment', REFERENCE_LIST, 'Assignment' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.ClientPorts.Port.LogicalChannelAssignments.Assignment', 
                [], [], 
                '''                List of assignments to logical clients
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
    'TerminalDevice.ClientPorts.Port' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.ClientPorts.Port',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the name of the client port
                ''',
                'name',
                'openconfig-terminal-device', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.ClientPorts.Port.Config', 
                [], [], 
                '''                Configuration data for client physical ports
                ''',
                'config',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.ClientPorts.Port.State', 
                [], [], 
                '''                Operational state data for client physical ports
                ''',
                'state',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('transceiver', REFERENCE_CLASS, 'Transceiver' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.ClientPorts.Port.Transceiver', 
                [], [], 
                '''                Top-level container for client port transceiver data
                ''',
                'transceiver',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('physical-channels', REFERENCE_CLASS, 'PhysicalChannels' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.ClientPorts.Port.PhysicalChannels', 
                [], [], 
                '''                Enclosing container for client channels
                ''',
                'physical_channels',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('logical-channel-assignments', REFERENCE_CLASS, 'LogicalChannelAssignments' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.ClientPorts.Port.LogicalChannelAssignments', 
                [], [], 
                '''                Enclosing container for client port to logical client
                mappings
                ''',
                'logical_channel_assignments',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'port',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.ClientPorts' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.ClientPorts',
            False, 
            [
            _MetaInfoClassMember('port', REFERENCE_LIST, 'Port' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.ClientPorts.Port', 
                [], [], 
                '''                List of client physical ports on the terminal device
                ''',
                'port',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'client-ports',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.Config' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.Config',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Index of the current logical client channel
                ''',
                'index',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description of the client logical channel
                ''',
                'description',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('trib-rate-class', REFERENCE_IDENTITY_CLASS, 'TributaryRateClassType_Identity' , 'ydk.models.openconfig.openconfig_transport_types', 'TributaryRateClassType_Identity', 
                [], [], 
                '''                Rounded bit rate of the tributary signal. Exact bit rate
                will be refined by protocol selection.
                ''',
                'trib_rate_class',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('trib-protocol', REFERENCE_IDENTITY_CLASS, 'TributaryProtocolType_Identity' , 'ydk.models.openconfig.openconfig_transport_types', 'TributaryProtocolType_Identity', 
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
            _MetaInfoClassMember('protocol-type', REFERENCE_IDENTITY_CLASS, 'LogicalElementProtocolType_Identity' , 'ydk.models.openconfig.openconfig_transport_types', 'LogicalElementProtocolType_Identity', 
                [], [], 
                '''                The type / stage of the logical element determines the
                configuration and operational state parameters (PMs)
                available for the logical element
                ''',
                'protocol_type',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'config',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.State.Ethernet' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.State.Ethernet',
            False, 
            [
            _MetaInfoClassMember('in-mac-control-frames', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                MAC layer control frames received on the interface
                ''',
                'in_mac_control_frames',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('in-mac-pause-frames', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                MAC layer PAUSE frames received on the interface
                ''',
                'in_mac_pause_frames',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('in-oversize-frames', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of oversize frames received on the interface
                ''',
                'in_oversize_frames',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('in-jabber-frames', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of jabber frames received on the
                interface.  Jabber frames are typically defined as oversize
                frames which also have a bad CRC.  Implementations may use
                slightly different definitions of what constitutes a jabber
                frame.  Often indicative of a NIC hardware problem.
                ''',
                'in_jabber_frames',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('in-fragment-frames', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of fragment frames received on the interface.
                ''',
                'in_fragment_frames',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('in-8021q-frames', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of 802.1q tagged frames received on the interface
                ''',
                'in_8021q_frames',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('in-crc-errors', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of receive error events due to FCS/CRC check
                failure
                ''',
                'in_crc_errors',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('out-mac-control-frames', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                MAC layer control frames sent on the interface
                ''',
                'out_mac_control_frames',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('out-mac-pause-frames', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                MAC layer PAUSE frames sent on the interface
                ''',
                'out_mac_pause_frames',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('out-8021q-frames', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of 802.1q tagged frames sent on the interface
                ''',
                'out_8021q_frames',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'ethernet',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.State.Otn.PreFecBer' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.State.Otn.PreFecBer',
            False, 
            [
            _MetaInfoClassMember('avg', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The arithmetic mean value of the statistic over the
                sampling period.
                ''',
                'avg',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('min', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The minimum value of the statistic over the sampling
                period
                ''',
                'min',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('max', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The maximum value of the statitic over the sampling
                period
                ''',
                'max',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'pre-fec-ber',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.State.Otn.PostFecBer' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.State.Otn.PostFecBer',
            False, 
            [
            _MetaInfoClassMember('avg', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The arithmetic mean value of the statistic over the
                sampling period.
                ''',
                'avg',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('min', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The minimum value of the statistic over the sampling
                period
                ''',
                'min',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('max', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The maximum value of the statitic over the sampling
                period
                ''',
                'max',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'post-fec-ber',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.State.Otn' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.State.Otn',
            False, 
            [
            _MetaInfoClassMember('pre-fec-ber', REFERENCE_CLASS, 'PreFecBer' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.State.Otn.PreFecBer', 
                [], [], 
                '''                Bit error rate before forward error correction -- computed
                value
                ''',
                'pre_fec_ber',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('post-fec-ber', REFERENCE_CLASS, 'PostFecBer' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.State.Otn.PostFecBer', 
                [], [], 
                '''                Bit error rate after forward error correction -- computed
                value
                ''',
                'post_fec_ber',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('tti-msg', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trail trace identifier (TTI) message received
                ''',
                'tti_msg',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('rdi-msg', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Remote defect indication (RDI) message received
                ''',
                'rdi_msg',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'otn',
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
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Index of the current logical client channel
                ''',
                'index',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description of the client logical channel
                ''',
                'description',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('trib-rate-class', REFERENCE_IDENTITY_CLASS, 'TributaryRateClassType_Identity' , 'ydk.models.openconfig.openconfig_transport_types', 'TributaryRateClassType_Identity', 
                [], [], 
                '''                Rounded bit rate of the tributary signal. Exact bit rate
                will be refined by protocol selection.
                ''',
                'trib_rate_class',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('trib-protocol', REFERENCE_IDENTITY_CLASS, 'TributaryProtocolType_Identity' , 'ydk.models.openconfig.openconfig_transport_types', 'TributaryProtocolType_Identity', 
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
            _MetaInfoClassMember('protocol-type', REFERENCE_IDENTITY_CLASS, 'LogicalElementProtocolType_Identity' , 'ydk.models.openconfig.openconfig_transport_types', 'LogicalElementProtocolType_Identity', 
                [], [], 
                '''                The type / stage of the logical element determines the
                configuration and operational state parameters (PMs)
                available for the logical element
                ''',
                'protocol_type',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('link-state', REFERENCE_ENUM_CLASS, 'LinkStateEnum' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.State.LinkStateEnum', 
                [], [], 
                '''                Link-state of the Ethernet protocol on the logical channel,
                SONET / SDH framed signal, etc.
                ''',
                'link_state',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('ethernet', REFERENCE_CLASS, 'Ethernet' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.State.Ethernet', 
                [], [], 
                '''                PMs and counters for Ethernet protocol channels
                ''',
                'ethernet',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('otn', REFERENCE_CLASS, 'Otn' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.State.Otn', 
                [], [], 
                '''                PMs and statistics for OTN protocol channels
                ''',
                'otn',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'state',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Index of the current logical client channel to tributary
                mapping
                ''',
                'index',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to the logical client channel
                ''',
                'description',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('logical-channel', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Reference to another stage of logical channel elements.
                ''',
                'logical_channel',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('optical-channel', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Reference to the line-side optical channel that should
                carry the current logical channel element.  Use this
                reference to exit the logical element stage.
                ''',
                'optical_channel',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('allocation', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-9223372036854775.808', '9223372036854775.807')], [], 
                '''                Allocation of the logical client channel to the tributary
                or sub-channel, expressed in Gbps
                ''',
                'allocation',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'config',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Index of the current logical client channel to tributary
                mapping
                ''',
                'index',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to the logical client channel
                ''',
                'description',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('logical-channel', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Reference to another stage of logical channel elements.
                ''',
                'logical_channel',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('optical-channel', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Reference to the line-side optical channel that should
                carry the current logical channel element.  Use this
                reference to exit the logical element stage.
                ''',
                'optical_channel',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('allocation', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-9223372036854775.808', '9223372036854775.807')], [], 
                '''                Allocation of the logical client channel to the tributary
                or sub-channel, expressed in Gbps
                ''',
                'allocation',
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
                [(0, 4294967295)], [], 
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
                [(0, 4294967295)], [], 
                '''                Reference to the index of the logical client channel
                ''',
                'index',
                'openconfig-terminal-device', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.Config', 
                [], [], 
                '''                Configuration data for logical client channels
                ''',
                'config',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.State', 
                [], [], 
                '''                Operational state data for logical client channels
                ''',
                'state',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('logical-channel-assignments', REFERENCE_CLASS, 'LogicalChannelAssignments' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments', 
                [], [], 
                '''                Enclosing container for tributary assignments
                ''',
                'logical_channel_assignments',
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
    'TerminalDevice.OpticalChannels.OpticalChannel.Config' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.OpticalChannels.OpticalChannel.Config',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Index number assigned to the optical channel.  The index
                must be unique on the local system.
                ''',
                'index',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('frequency', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Frequency of the optical channel
                ''',
                'frequency',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('power', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Power level of the optical channel
                ''',
                'power',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('operational-mode', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Vendor-specific mode identifier -- sets the operational
                mode for the channel
                ''',
                'operational_mode',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('line-port', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the line-side physical port that carries
                this optical channel
                ''',
                'line_port',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'config',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.OpticalChannels.OpticalChannel.State' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.OpticalChannels.OpticalChannel.State',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Index number assigned to the optical channel.  The index
                must be unique on the local system.
                ''',
                'index',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('frequency', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Frequency of the optical channel
                ''',
                'frequency',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('power', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Power level of the optical channel
                ''',
                'power',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('operational-mode', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Vendor-specific mode identifier -- sets the operational
                mode for the channel
                ''',
                'operational_mode',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('line-port', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the line-side physical port that carries
                this optical channel
                ''',
                'line_port',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'state',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.OpticalChannels.OpticalChannel' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.OpticalChannels.OpticalChannel',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                 
                ''',
                'index',
                'openconfig-terminal-device', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.OpticalChannels.OpticalChannel.Config', 
                [], [], 
                '''                Configuration data 
                ''',
                'config',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.OpticalChannels.OpticalChannel.State', 
                [], [], 
                '''                Operational state data 
                ''',
                'state',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'optical-channel',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.OpticalChannels' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.OpticalChannels',
            False, 
            [
            _MetaInfoClassMember('optical-channel', REFERENCE_LIST, 'OpticalChannel' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.OpticalChannels.OpticalChannel', 
                [], [], 
                '''                List of 
                ''',
                'optical_channel',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'optical-channels',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LinePorts.Port.Config' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LinePorts.Port.Config',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the line port
                ''',
                'name',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('output-power', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The output optical power of this port in units of 0.01dBm.
                If the port is an aggregate of multiple physical channels,
                this attribute is the total power or sum of all channels.
                ''',
                'output_power',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'config',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LinePorts.Port.State' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LinePorts.Port.State',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the line port
                ''',
                'name',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('output-power', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The output optical power of this port in units of 0.01dBm.
                If the port is an aggregate of multiple physical channels,
                this attribute is the total power or sum of all channels.
                ''',
                'output_power',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'state',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LinePorts.Port' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LinePorts.Port',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the name of the line port
                ''',
                'name',
                'openconfig-terminal-device', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LinePorts.Port.Config', 
                [], [], 
                '''                Configuration data for each physical line port
                ''',
                'config',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LinePorts.Port.State', 
                [], [], 
                '''                Operational state data for each physical line port
                ''',
                'state',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'port',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.LinePorts' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.LinePorts',
            False, 
            [
            _MetaInfoClassMember('port', REFERENCE_LIST, 'Port' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LinePorts.Port', 
                [], [], 
                '''                List of line ports
                ''',
                'port',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'line-ports',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.OperationalModes.Config' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.OperationalModes.Config',
            False, 
            [
            ],
            'openconfig-terminal-device',
            'config',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.OperationalModes.State.SupportedModes' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.OperationalModes.State.SupportedModes',
            False, 
            [
            _MetaInfoClassMember('mode-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Two-octet encoding of the vendor-defined operational
                mode
                ''',
                'mode_id',
                'openconfig-terminal-device', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Vendor-supplied textual description of the characteristics
                of this operational mode to enable operators to select the
                appropriate mode for the application.
                ''',
                'description',
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
            'supported-modes',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.OperationalModes.State' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.OperationalModes.State',
            False, 
            [
            _MetaInfoClassMember('supported-modes', REFERENCE_LIST, 'SupportedModes' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.OperationalModes.State.SupportedModes', 
                [], [], 
                '''                List of supported modes and their associated metadata
                ''',
                'supported_modes',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'state',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
    'TerminalDevice.OperationalModes' : {
        'meta_info' : _MetaInfoClass('TerminalDevice.OperationalModes',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.OperationalModes.Config', 
                [], [], 
                '''                Configuration data for operational modes.  This should
                generally be empty, i.e., operational mode information
                is supplied by the platform vendor and is expected to be
                read-only
                ''',
                'config',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.OperationalModes.State', 
                [], [], 
                '''                Operational state data for vendor-specific operational
                modes
                ''',
                'state',
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
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.State', 
                [], [], 
                '''                Operational state data for global terminal device
                ''',
                'state',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('client-ports', REFERENCE_CLASS, 'ClientPorts' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.ClientPorts', 
                [], [], 
                '''                Enclosing container for the list of client ports
                ''',
                'client_ports',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('logical-channels', REFERENCE_CLASS, 'LogicalChannels' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LogicalChannels', 
                [], [], 
                '''                Enclosing container the list of logical channels
                ''',
                'logical_channels',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('optical-channels', REFERENCE_CLASS, 'OpticalChannels' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.OpticalChannels', 
                [], [], 
                '''                Enclosing container 
                ''',
                'optical_channels',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('line-ports', REFERENCE_CLASS, 'LinePorts' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.LinePorts', 
                [], [], 
                '''                Enclosing container for line ports
                ''',
                'line_ports',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('operational-modes', REFERENCE_CLASS, 'OperationalModes' , 'ydk.models.openconfig.openconfig_terminal_device', 'TerminalDevice.OperationalModes', 
                [], [], 
                '''                Top-level container for vendor-specific operational mode
                information
                ''',
                'operational_modes',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'terminal-device',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_terminal_device'
        ),
    },
}
_meta_table['TerminalDevice.ClientPorts.Port.Transceiver.Config']['meta_info'].parent =_meta_table['TerminalDevice.ClientPorts.Port.Transceiver']['meta_info']
_meta_table['TerminalDevice.ClientPorts.Port.Transceiver.State']['meta_info'].parent =_meta_table['TerminalDevice.ClientPorts.Port.Transceiver']['meta_info']
_meta_table['TerminalDevice.ClientPorts.Port.PhysicalChannels.Channel.Config']['meta_info'].parent =_meta_table['TerminalDevice.ClientPorts.Port.PhysicalChannels.Channel']['meta_info']
_meta_table['TerminalDevice.ClientPorts.Port.PhysicalChannels.Channel.State']['meta_info'].parent =_meta_table['TerminalDevice.ClientPorts.Port.PhysicalChannels.Channel']['meta_info']
_meta_table['TerminalDevice.ClientPorts.Port.PhysicalChannels.Channel']['meta_info'].parent =_meta_table['TerminalDevice.ClientPorts.Port.PhysicalChannels']['meta_info']
_meta_table['TerminalDevice.ClientPorts.Port.LogicalChannelAssignments.Assignment.Config']['meta_info'].parent =_meta_table['TerminalDevice.ClientPorts.Port.LogicalChannelAssignments.Assignment']['meta_info']
_meta_table['TerminalDevice.ClientPorts.Port.LogicalChannelAssignments.Assignment.State']['meta_info'].parent =_meta_table['TerminalDevice.ClientPorts.Port.LogicalChannelAssignments.Assignment']['meta_info']
_meta_table['TerminalDevice.ClientPorts.Port.LogicalChannelAssignments.Assignment']['meta_info'].parent =_meta_table['TerminalDevice.ClientPorts.Port.LogicalChannelAssignments']['meta_info']
_meta_table['TerminalDevice.ClientPorts.Port.Config']['meta_info'].parent =_meta_table['TerminalDevice.ClientPorts.Port']['meta_info']
_meta_table['TerminalDevice.ClientPorts.Port.State']['meta_info'].parent =_meta_table['TerminalDevice.ClientPorts.Port']['meta_info']
_meta_table['TerminalDevice.ClientPorts.Port.Transceiver']['meta_info'].parent =_meta_table['TerminalDevice.ClientPorts.Port']['meta_info']
_meta_table['TerminalDevice.ClientPorts.Port.PhysicalChannels']['meta_info'].parent =_meta_table['TerminalDevice.ClientPorts.Port']['meta_info']
_meta_table['TerminalDevice.ClientPorts.Port.LogicalChannelAssignments']['meta_info'].parent =_meta_table['TerminalDevice.ClientPorts.Port']['meta_info']
_meta_table['TerminalDevice.ClientPorts.Port']['meta_info'].parent =_meta_table['TerminalDevice.ClientPorts']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.State.Otn.PreFecBer']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel.State.Otn']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.State.Otn.PostFecBer']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel.State.Otn']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.State.Ethernet']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel.State']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.State.Otn']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel.State']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.Config']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment.State']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments.Assignment']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.Config']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.State']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel.LogicalChannelAssignments']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels.Channel']['meta_info']
_meta_table['TerminalDevice.LogicalChannels.Channel']['meta_info'].parent =_meta_table['TerminalDevice.LogicalChannels']['meta_info']
_meta_table['TerminalDevice.OpticalChannels.OpticalChannel.Config']['meta_info'].parent =_meta_table['TerminalDevice.OpticalChannels.OpticalChannel']['meta_info']
_meta_table['TerminalDevice.OpticalChannels.OpticalChannel.State']['meta_info'].parent =_meta_table['TerminalDevice.OpticalChannels.OpticalChannel']['meta_info']
_meta_table['TerminalDevice.OpticalChannels.OpticalChannel']['meta_info'].parent =_meta_table['TerminalDevice.OpticalChannels']['meta_info']
_meta_table['TerminalDevice.LinePorts.Port.Config']['meta_info'].parent =_meta_table['TerminalDevice.LinePorts.Port']['meta_info']
_meta_table['TerminalDevice.LinePorts.Port.State']['meta_info'].parent =_meta_table['TerminalDevice.LinePorts.Port']['meta_info']
_meta_table['TerminalDevice.LinePorts.Port']['meta_info'].parent =_meta_table['TerminalDevice.LinePorts']['meta_info']
_meta_table['TerminalDevice.OperationalModes.State.SupportedModes']['meta_info'].parent =_meta_table['TerminalDevice.OperationalModes.State']['meta_info']
_meta_table['TerminalDevice.OperationalModes.Config']['meta_info'].parent =_meta_table['TerminalDevice.OperationalModes']['meta_info']
_meta_table['TerminalDevice.OperationalModes.State']['meta_info'].parent =_meta_table['TerminalDevice.OperationalModes']['meta_info']
_meta_table['TerminalDevice.Config']['meta_info'].parent =_meta_table['TerminalDevice']['meta_info']
_meta_table['TerminalDevice.State']['meta_info'].parent =_meta_table['TerminalDevice']['meta_info']
_meta_table['TerminalDevice.ClientPorts']['meta_info'].parent =_meta_table['TerminalDevice']['meta_info']
_meta_table['TerminalDevice.LogicalChannels']['meta_info'].parent =_meta_table['TerminalDevice']['meta_info']
_meta_table['TerminalDevice.OpticalChannels']['meta_info'].parent =_meta_table['TerminalDevice']['meta_info']
_meta_table['TerminalDevice.LinePorts']['meta_info'].parent =_meta_table['TerminalDevice']['meta_info']
_meta_table['TerminalDevice.OperationalModes']['meta_info'].parent =_meta_table['TerminalDevice']['meta_info']

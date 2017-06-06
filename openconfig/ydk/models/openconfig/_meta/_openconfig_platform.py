


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Components.Component.Config' : {
        'meta_info' : _MetaInfoClass('Components.Component.Config',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name for the component -- this will not be a
                configurable parameter on many implementations
                ''',
                'name',
                'openconfig-platform', False),
            ],
            'openconfig-platform',
            'config',
            _yang_ns._namespaces['openconfig-platform'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.State' : {
        'meta_info' : _MetaInfoClass('Components.Component.State',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                System-supplied description of the component
                ''',
                'description',
                'openconfig-platform', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Unique identifier assigned by the system for the
                component
                ''',
                'id',
                'openconfig-platform', False),
            _MetaInfoClassMember('mfg-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                System-supplied identifier for the manufacturer of the
                component.  This data is particularly useful when a
                component manufacturer is different than the overall
                device vendor.
                ''',
                'mfg_name',
                'openconfig-platform', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name for the component -- this will not be a
                configurable parameter on many implementations
                ''',
                'name',
                'openconfig-platform', False),
            _MetaInfoClassMember('part-no', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                System-assigned part number for the component.  This should
                be present in particular if the component is also an FRU
                (field replacable unit)
                ''',
                'part_no',
                'openconfig-platform', False),
            _MetaInfoClassMember('serial-no', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                System-assigned serial number of the component.
                ''',
                'serial_no',
                'openconfig-platform', False),
            _MetaInfoClassMember('type', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Type of component as identified by the system
                ''',
                'type',
                'openconfig-platform', False, [
                    _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'Openconfig_Hardware_ComponentIdentity' , 'ydk.models.openconfig.openconfig_platform_types', 'Openconfig_Hardware_ComponentIdentity', 
                        [], [], 
                        '''                        Type of component as identified by the system
                        ''',
                        'type',
                        'openconfig-platform', False),
                    _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'Openconfig_Software_ComponentIdentity' , 'ydk.models.openconfig.openconfig_platform_types', 'Openconfig_Software_ComponentIdentity', 
                        [], [], 
                        '''                        Type of component as identified by the system
                        ''',
                        'type',
                        'openconfig-platform', False),
                ]),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                System-defined version string for a hardware, firmware,
                or software component.
                ''',
                'version',
                'openconfig-platform', False),
            ],
            'openconfig-platform',
            'state',
            _yang_ns._namespaces['openconfig-platform'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.Properties.Property.Config' : {
        'meta_info' : _MetaInfoClass('Components.Component.Properties.Property.Config',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                System-supplied name of the property -- this is typically
                non-configurable
                ''',
                'name',
                'openconfig-platform', False),
            _MetaInfoClassMember('value', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Property values can take on a variety of types.  Signed and
                unsigned integer types may be provided in smaller sizes,
                e.g., int8, uint16, etc.
                ''',
                'value',
                'openconfig-platform', False, [
                    _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                        [], [], 
                        '''                        Property values can take on a variety of types.  Signed and
                        unsigned integer types may be provided in smaller sizes,
                        e.g., int8, uint16, etc.
                        ''',
                        'value',
                        'openconfig-platform', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'bool' , None, None, 
                        [], [], 
                        '''                        Property values can take on a variety of types.  Signed and
                        unsigned integer types may be provided in smaller sizes,
                        e.g., int8, uint16, etc.
                        ''',
                        'value',
                        'openconfig-platform', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                        [('-9223372036854775808', '9223372036854775807')], [], 
                        '''                        Property values can take on a variety of types.  Signed and
                        unsigned integer types may be provided in smaller sizes,
                        e.g., int8, uint16, etc.
                        ''',
                        'value',
                        'openconfig-platform', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                        [('0', '18446744073709551615')], [], 
                        '''                        Property values can take on a variety of types.  Signed and
                        unsigned integer types may be provided in smaller sizes,
                        e.g., int8, uint16, etc.
                        ''',
                        'value',
                        'openconfig-platform', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'Decimal64' , None, None, 
                        [('-92233720368547758.08', '92233720368547758.07')], [], 
                        '''                        Property values can take on a variety of types.  Signed and
                        unsigned integer types may be provided in smaller sizes,
                        e.g., int8, uint16, etc.
                        ''',
                        'value',
                        'openconfig-platform', False),
                ]),
            ],
            'openconfig-platform',
            'config',
            _yang_ns._namespaces['openconfig-platform'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.Properties.Property.State' : {
        'meta_info' : _MetaInfoClass('Components.Component.Properties.Property.State',
            False, 
            [
            _MetaInfoClassMember('configurable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indication whether the property is user-configurable
                ''',
                'configurable',
                'openconfig-platform', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                System-supplied name of the property -- this is typically
                non-configurable
                ''',
                'name',
                'openconfig-platform', False),
            _MetaInfoClassMember('value', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Property values can take on a variety of types.  Signed and
                unsigned integer types may be provided in smaller sizes,
                e.g., int8, uint16, etc.
                ''',
                'value',
                'openconfig-platform', False, [
                    _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                        [], [], 
                        '''                        Property values can take on a variety of types.  Signed and
                        unsigned integer types may be provided in smaller sizes,
                        e.g., int8, uint16, etc.
                        ''',
                        'value',
                        'openconfig-platform', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'bool' , None, None, 
                        [], [], 
                        '''                        Property values can take on a variety of types.  Signed and
                        unsigned integer types may be provided in smaller sizes,
                        e.g., int8, uint16, etc.
                        ''',
                        'value',
                        'openconfig-platform', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                        [('-9223372036854775808', '9223372036854775807')], [], 
                        '''                        Property values can take on a variety of types.  Signed and
                        unsigned integer types may be provided in smaller sizes,
                        e.g., int8, uint16, etc.
                        ''',
                        'value',
                        'openconfig-platform', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                        [('0', '18446744073709551615')], [], 
                        '''                        Property values can take on a variety of types.  Signed and
                        unsigned integer types may be provided in smaller sizes,
                        e.g., int8, uint16, etc.
                        ''',
                        'value',
                        'openconfig-platform', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'Decimal64' , None, None, 
                        [('-92233720368547758.08', '92233720368547758.07')], [], 
                        '''                        Property values can take on a variety of types.  Signed and
                        unsigned integer types may be provided in smaller sizes,
                        e.g., int8, uint16, etc.
                        ''',
                        'value',
                        'openconfig-platform', False),
                ]),
            ],
            'openconfig-platform',
            'state',
            _yang_ns._namespaces['openconfig-platform'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.Properties.Property' : {
        'meta_info' : _MetaInfoClass('Components.Component.Properties.Property',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the property name.
                ''',
                'name',
                'openconfig-platform', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.Properties.Property.Config', 
                [], [], 
                '''                Configuration data for each property
                ''',
                'config',
                'openconfig-platform', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.Properties.Property.State', 
                [], [], 
                '''                Operational state data for each property
                ''',
                'state',
                'openconfig-platform', False),
            ],
            'openconfig-platform',
            'property',
            _yang_ns._namespaces['openconfig-platform'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.Properties' : {
        'meta_info' : _MetaInfoClass('Components.Component.Properties',
            False, 
            [
            _MetaInfoClassMember('property', REFERENCE_LIST, 'Property' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.Properties.Property', 
                [], [], 
                '''                List of system properties for the component
                ''',
                'property',
                'openconfig-platform', False),
            ],
            'openconfig-platform',
            'properties',
            _yang_ns._namespaces['openconfig-platform'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.Subcomponents.Subcomponent.Config' : {
        'meta_info' : _MetaInfoClass('Components.Component.Subcomponents.Subcomponent.Config',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the name of the subcomponent
                ''',
                'name',
                'openconfig-platform', False),
            ],
            'openconfig-platform',
            'config',
            _yang_ns._namespaces['openconfig-platform'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.Subcomponents.Subcomponent.State' : {
        'meta_info' : _MetaInfoClass('Components.Component.Subcomponents.Subcomponent.State',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the name of the subcomponent
                ''',
                'name',
                'openconfig-platform', False),
            ],
            'openconfig-platform',
            'state',
            _yang_ns._namespaces['openconfig-platform'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.Subcomponents.Subcomponent' : {
        'meta_info' : _MetaInfoClass('Components.Component.Subcomponents.Subcomponent',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the name list key
                ''',
                'name',
                'openconfig-platform', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.Subcomponents.Subcomponent.Config', 
                [], [], 
                '''                Configuration data 
                ''',
                'config',
                'openconfig-platform', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.Subcomponents.Subcomponent.State', 
                [], [], 
                '''                Operational state data 
                ''',
                'state',
                'openconfig-platform', False),
            ],
            'openconfig-platform',
            'subcomponent',
            _yang_ns._namespaces['openconfig-platform'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.Subcomponents' : {
        'meta_info' : _MetaInfoClass('Components.Component.Subcomponents',
            False, 
            [
            _MetaInfoClassMember('subcomponent', REFERENCE_LIST, 'Subcomponent' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.Subcomponents.Subcomponent', 
                [], [], 
                '''                List of subcomponent references
                ''',
                'subcomponent',
                'openconfig-platform', False),
            ],
            'openconfig-platform',
            'subcomponents',
            _yang_ns._namespaces['openconfig-platform'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.Transceiver.Config' : {
        'meta_info' : _MetaInfoClass('Components.Component.Transceiver.Config',
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
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('form-factor', REFERENCE_IDENTITY_CLASS, 'Transceiver_Form_Factor_TypeIdentity' , 'ydk.models.openconfig.openconfig_transport_types', 'Transceiver_Form_Factor_TypeIdentity', 
                [], [], 
                '''                Indicates the type of optical transceiver used on this
                port.  If the client port is built into the device and not
                plugable, then non-pluggable is the corresponding state. If
                a device port supports multiple form factors (e.g. QSFP28
                and QSFP+, then the value of the transceiver installed shall
                be reported. If no transceiver is present, then the value of
                the highest rate form factor shall be reported
                (QSFP28, for example).
                
                The form factor is included in configuration data to allow
                pre-configuring a device with the expected type of
                transceiver ahead of deployment.  The corresponding state
                leaf should reflect the actual transceiver type plugged into
                the system.
                ''',
                'form_factor',
                'openconfig-platform-transceiver', False),
            ],
            'openconfig-platform-transceiver',
            'config',
            _yang_ns._namespaces['openconfig-platform-transceiver'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.Transceiver.State.PresentEnum' : _MetaInfoEnum('PresentEnum', 'ydk.models.openconfig.openconfig_platform',
        {
            'PRESENT':'PRESENT',
            'NOT_PRESENT':'NOT_PRESENT',
        }, 'openconfig-platform-transceiver', _yang_ns._namespaces['openconfig-platform-transceiver']),
    'Components.Component.Transceiver.State' : {
        'meta_info' : _MetaInfoClass('Components.Component.Transceiver.State',
            False, 
            [
            _MetaInfoClassMember('connector-type', REFERENCE_IDENTITY_CLASS, 'Fiber_Connector_TypeIdentity' , 'ydk.models.openconfig.openconfig_transport_types', 'Fiber_Connector_TypeIdentity', 
                [], [], 
                '''                Connector type used on this port
                ''',
                'connector_type',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('date-code', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Representation of the transceiver date code, typically
                stored as YYMMDD.  The time portion of the value is
                undefined and not intended to be read.
                ''',
                'date_code',
                'openconfig-platform-transceiver', False),
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
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('ethernet-compliance-code', REFERENCE_IDENTITY_CLASS, 'Ethernet_Pmd_TypeIdentity' , 'ydk.models.openconfig.openconfig_transport_types', 'Ethernet_Pmd_TypeIdentity', 
                [], [], 
                '''                Ethernet PMD that the transceiver supports. The SFF/QSFP
                MSAs have registers for this and CFP MSA has similar.
                ''',
                'ethernet_compliance_code',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('fault-condition', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates if a fault condition exists in the transceiver
                ''',
                'fault_condition',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('form-factor', REFERENCE_IDENTITY_CLASS, 'Transceiver_Form_Factor_TypeIdentity' , 'ydk.models.openconfig.openconfig_transport_types', 'Transceiver_Form_Factor_TypeIdentity', 
                [], [], 
                '''                Indicates the type of optical transceiver used on this
                port.  If the client port is built into the device and not
                plugable, then non-pluggable is the corresponding state. If
                a device port supports multiple form factors (e.g. QSFP28
                and QSFP+, then the value of the transceiver installed shall
                be reported. If no transceiver is present, then the value of
                the highest rate form factor shall be reported
                (QSFP28, for example).
                
                The form factor is included in configuration data to allow
                pre-configuring a device with the expected type of
                transceiver ahead of deployment.  The corresponding state
                leaf should reflect the actual transceiver type plugged into
                the system.
                ''',
                'form_factor',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('internal-temp', ATTRIBUTE, 'int' , None, None, 
                [('-40', '125')], [], 
                '''                Internally measured temperature in degrees Celsius. MSA
                valid range is between -40 and +125C. Accuracy shall be
                better than +/- 3 degC over the whole temperature range.
                ''',
                'internal_temp',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('otn-compliance-code', REFERENCE_IDENTITY_CLASS, 'Otn_Application_CodeIdentity' , 'ydk.models.openconfig.openconfig_transport_types', 'Otn_Application_CodeIdentity', 
                [], [], 
                '''                OTN application code supported by the port
                ''',
                'otn_compliance_code',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('present', REFERENCE_ENUM_CLASS, 'PresentEnum' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.Transceiver.State.PresentEnum', 
                [], [], 
                '''                Indicates whether a transceiver is present in
                the specified client port.
                ''',
                'present',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('serial-no', ATTRIBUTE, 'str' , None, None, 
                [(1, 16)], [], 
                '''                Transceiver serial number. 16-octet field that contains
                ASCII characters, left-aligned and padded on the right with
                ASCII spaces (20h). If part serial number is undefined, all
                16 octets = 0h
                ''',
                'serial_no',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('sonet-sdh-compliance-code', REFERENCE_IDENTITY_CLASS, 'Sonet_Application_CodeIdentity' , 'ydk.models.openconfig.openconfig_transport_types', 'Sonet_Application_CodeIdentity', 
                [], [], 
                '''                SONET/SDH application code supported by the port
                ''',
                'sonet_sdh_compliance_code',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('vendor', ATTRIBUTE, 'str' , None, None, 
                [(1, 16)], [], 
                '''                Full name of transceiver vendor. 16-octet field that
                contains ASCII characters, left-aligned and padded on the
                right with ASCII spaces (20h)
                ''',
                'vendor',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('vendor-part', ATTRIBUTE, 'str' , None, None, 
                [(1, 16)], [], 
                '''                Transceiver vendor's part number. 16-octet field that
                contains ASCII characters, left-aligned and padded on the
                right with ASCII spaces (20h). If part number is undefined,
                all 16 octets = 0h
                ''',
                'vendor_part',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('vendor-rev', ATTRIBUTE, 'str' , None, None, 
                [(1, 2)], [], 
                '''                Transceiver vendor's revision number. 2-octet field that
                contains ASCII characters, left-aligned and padded on the
                right with ASCII spaces (20h)
                ''',
                'vendor_rev',
                'openconfig-platform-transceiver', False),
            ],
            'openconfig-platform-transceiver',
            'state',
            _yang_ns._namespaces['openconfig-platform-transceiver'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.Transceiver.PhysicalChannels.Channel.Config' : {
        'meta_info' : _MetaInfoClass('Components.Component.Transceiver.PhysicalChannels.Channel.Config',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Text description for the client physical channel
                ''',
                'description',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Index of the physical channnel or lane within a physical
                client port
                ''',
                'index',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('target-output-power', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Target output optical power level of the optical channel,
                expressed in increments of 0.01 dBm (decibel-milliwats)
                ''',
                'target_output_power',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('tx-laser', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable (true) or disable (false) the transmit label for the
                channel
                ''',
                'tx_laser',
                'openconfig-platform-transceiver', False),
            ],
            'openconfig-platform-transceiver',
            'config',
            _yang_ns._namespaces['openconfig-platform-transceiver'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.Transceiver.PhysicalChannels.Channel.State.OutputPower' : {
        'meta_info' : _MetaInfoClass('Components.Component.Transceiver.PhysicalChannels.Channel.State.OutputPower',
            False, 
            [
            _MetaInfoClassMember('avg', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The arithmetic mean value of the statistic over the
                sampling period.
                ''',
                'avg',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('instant', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The instantaneous value of the statistic.
                ''',
                'instant',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('max', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The maximum value of the statitic over the sampling
                period
                ''',
                'max',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('min', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The minimum value of the statistic over the sampling
                period
                ''',
                'min',
                'openconfig-platform-transceiver', False),
            ],
            'openconfig-platform-transceiver',
            'output-power',
            _yang_ns._namespaces['openconfig-platform-transceiver'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.Transceiver.PhysicalChannels.Channel.State.InputPower' : {
        'meta_info' : _MetaInfoClass('Components.Component.Transceiver.PhysicalChannels.Channel.State.InputPower',
            False, 
            [
            _MetaInfoClassMember('avg', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The arithmetic mean value of the statistic over the
                sampling period.
                ''',
                'avg',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('instant', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The instantaneous value of the statistic.
                ''',
                'instant',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('max', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The maximum value of the statitic over the sampling
                period
                ''',
                'max',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('min', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The minimum value of the statistic over the sampling
                period
                ''',
                'min',
                'openconfig-platform-transceiver', False),
            ],
            'openconfig-platform-transceiver',
            'input-power',
            _yang_ns._namespaces['openconfig-platform-transceiver'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.Transceiver.PhysicalChannels.Channel.State.LaserBiasCurrent' : {
        'meta_info' : _MetaInfoClass('Components.Component.Transceiver.PhysicalChannels.Channel.State.LaserBiasCurrent',
            False, 
            [
            _MetaInfoClassMember('avg', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The arithmetic mean value of the statistic over the
                sampling period.
                ''',
                'avg',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('instant', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The instantaneous value of the statistic.
                ''',
                'instant',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('max', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The maximum value of the statitic over the sampling
                period
                ''',
                'max',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('min', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-922337203685477580.8', '922337203685477580.7')], [], 
                '''                The minimum value of the statistic over the sampling
                period
                ''',
                'min',
                'openconfig-platform-transceiver', False),
            ],
            'openconfig-platform-transceiver',
            'laser-bias-current',
            _yang_ns._namespaces['openconfig-platform-transceiver'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.Transceiver.PhysicalChannels.Channel.State' : {
        'meta_info' : _MetaInfoClass('Components.Component.Transceiver.PhysicalChannels.Channel.State',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Text description for the client physical channel
                ''',
                'description',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Index of the physical channnel or lane within a physical
                client port
                ''',
                'index',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('input-power', REFERENCE_CLASS, 'InputPower' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.Transceiver.PhysicalChannels.Channel.State.InputPower', 
                [], [], 
                '''                The input optical power of this port in units of 0.01dBm.
                If the port is an aggregate of multiple physical channels,
                this attribute is the total power or sum of all channels.
                If avg/min/max statistics are not supported, the target is
                expected to just supply the instant value
                ''',
                'input_power',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('laser-bias-current', REFERENCE_CLASS, 'LaserBiasCurrent' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.Transceiver.PhysicalChannels.Channel.State.LaserBiasCurrent', 
                [], [], 
                '''                The current applied by the system to the transmit laser to
                achieve the output power.  The current is expressed in mA
                with up to one decimal precision. If avg/min/max statistics
                are not supported, the target is expected to just supply
                the instant value
                ''',
                'laser_bias_current',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('output-frequency', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The frequency in MHz of the individual physical channel
                (e.g. ITU C50 - 195.0THz and would be reported as
                195,000,000 MHz in this model). This attribute is not
                configurable on most client ports.
                ''',
                'output_frequency',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('output-power', REFERENCE_CLASS, 'OutputPower' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.Transceiver.PhysicalChannels.Channel.State.OutputPower', 
                [], [], 
                '''                The output optical power of this port in units of 0.01dBm.
                If the port is an aggregate of multiple physical channels,
                this attribute is the total power or sum of all channels. If
                avg/min/max statistics are not supported, the target is
                expected to just supply the instant value
                ''',
                'output_power',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('target-output-power', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Target output optical power level of the optical channel,
                expressed in increments of 0.01 dBm (decibel-milliwats)
                ''',
                'target_output_power',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('tx-laser', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable (true) or disable (false) the transmit label for the
                channel
                ''',
                'tx_laser',
                'openconfig-platform-transceiver', False),
            ],
            'openconfig-platform-transceiver',
            'state',
            _yang_ns._namespaces['openconfig-platform-transceiver'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.Transceiver.PhysicalChannels.Channel' : {
        'meta_info' : _MetaInfoClass('Components.Component.Transceiver.PhysicalChannels.Channel',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Reference to the index number of the channel
                ''',
                'index',
                'openconfig-platform-transceiver', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.Transceiver.PhysicalChannels.Channel.Config', 
                [], [], 
                '''                Configuration data for physical channels
                ''',
                'config',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.Transceiver.PhysicalChannels.Channel.State', 
                [], [], 
                '''                Operational state data for channels
                ''',
                'state',
                'openconfig-platform-transceiver', False),
            ],
            'openconfig-platform-transceiver',
            'channel',
            _yang_ns._namespaces['openconfig-platform-transceiver'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.Transceiver.PhysicalChannels' : {
        'meta_info' : _MetaInfoClass('Components.Component.Transceiver.PhysicalChannels',
            False, 
            [
            _MetaInfoClassMember('channel', REFERENCE_LIST, 'Channel' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.Transceiver.PhysicalChannels.Channel', 
                [], [], 
                '''                List of client channels, keyed by index within a physical
                client port.  A physical port with a single channel would
                have a single zero-indexed element
                ''',
                'channel',
                'openconfig-platform-transceiver', False),
            ],
            'openconfig-platform-transceiver',
            'physical-channels',
            _yang_ns._namespaces['openconfig-platform-transceiver'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.Transceiver' : {
        'meta_info' : _MetaInfoClass('Components.Component.Transceiver',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.Transceiver.Config', 
                [], [], 
                '''                Configuration data for client port transceivers
                ''',
                'config',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('physical-channels', REFERENCE_CLASS, 'PhysicalChannels' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.Transceiver.PhysicalChannels', 
                [], [], 
                '''                Enclosing container for client channels
                ''',
                'physical_channels',
                'openconfig-platform-transceiver', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.Transceiver.State', 
                [], [], 
                '''                Operational state data for client port transceivers
                ''',
                'state',
                'openconfig-platform-transceiver', False),
            ],
            'openconfig-platform-transceiver',
            'transceiver',
            _yang_ns._namespaces['openconfig-platform-transceiver'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.OpticalChannel.Config' : {
        'meta_info' : _MetaInfoClass('Components.Component.OpticalChannel.Config',
            False, 
            [
            _MetaInfoClassMember('frequency', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Frequency of the optical channel, expressed in MHz
                ''',
                'frequency',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('line-port', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the line-side physical port that carries
                this optical channel.  The target port should be
                a component in the physical inventory data model.
                ''',
                'line_port',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('operational-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Vendor-specific mode identifier -- sets the operational
                mode for the channel
                ''',
                'operational_mode',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('target-output-power', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Target output optical power level of the optical channel,
                expressed in increments of 0.01 dBm (decibel-milliwats)
                ''',
                'target_output_power',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'config',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.OpticalChannel.State.OutputPower' : {
        'meta_info' : _MetaInfoClass('Components.Component.OpticalChannel.State.OutputPower',
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
            'output-power',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.OpticalChannel.State.InputPower' : {
        'meta_info' : _MetaInfoClass('Components.Component.OpticalChannel.State.InputPower',
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
            'input-power',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.OpticalChannel.State.LaserBiasCurrent' : {
        'meta_info' : _MetaInfoClass('Components.Component.OpticalChannel.State.LaserBiasCurrent',
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
            'laser-bias-current',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.OpticalChannel.State.ChromaticDispersion' : {
        'meta_info' : _MetaInfoClass('Components.Component.OpticalChannel.State.ChromaticDispersion',
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
            'chromatic-dispersion',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.OpticalChannel.State.PolarizationModeDispersion' : {
        'meta_info' : _MetaInfoClass('Components.Component.OpticalChannel.State.PolarizationModeDispersion',
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
            'polarization-mode-dispersion',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.OpticalChannel.State.SecondOrderPolarizationModeDispersion' : {
        'meta_info' : _MetaInfoClass('Components.Component.OpticalChannel.State.SecondOrderPolarizationModeDispersion',
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
            'second-order-polarization-mode-dispersion',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.OpticalChannel.State.PolarizationDependentLoss' : {
        'meta_info' : _MetaInfoClass('Components.Component.OpticalChannel.State.PolarizationDependentLoss',
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
            'polarization-dependent-loss',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.OpticalChannel.State' : {
        'meta_info' : _MetaInfoClass('Components.Component.OpticalChannel.State',
            False, 
            [
            _MetaInfoClassMember('chromatic-dispersion', REFERENCE_CLASS, 'ChromaticDispersion' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.OpticalChannel.State.ChromaticDispersion', 
                [], [], 
                '''                Chromatic Dispersion of an optical channel
                in ps/nm as reported by receiver
                ''',
                'chromatic_dispersion',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('frequency', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Frequency of the optical channel, expressed in MHz
                ''',
                'frequency',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                If the device places constraints on which optical
                channels must be managed together (e.g., transmitted on the
                same line port), it can indicate that by setting the group-id
                to the same value across related optical channels.
                ''',
                'group_id',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('input-power', REFERENCE_CLASS, 'InputPower' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.OpticalChannel.State.InputPower', 
                [], [], 
                '''                The input optical power of this port in units of 0.01dBm.
                If the port is an aggregate of multiple physical channels,
                this attribute is the total power or sum of all channels.
                If avg/min/max statistics are not supported, the target is
                expected to just supply the instant value
                ''',
                'input_power',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('laser-bias-current', REFERENCE_CLASS, 'LaserBiasCurrent' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.OpticalChannel.State.LaserBiasCurrent', 
                [], [], 
                '''                The current applied by the system to the transmit laser to
                achieve the output power.  The current is expressed in mA
                with up to one decimal precision. If avg/min/max statistics
                are not supported, the target is expected to just supply
                the instant value
                ''',
                'laser_bias_current',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('line-port', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the line-side physical port that carries
                this optical channel.  The target port should be
                a component in the physical inventory data model.
                ''',
                'line_port',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('operational-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Vendor-specific mode identifier -- sets the operational
                mode for the channel
                ''',
                'operational_mode',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('output-power', REFERENCE_CLASS, 'OutputPower' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.OpticalChannel.State.OutputPower', 
                [], [], 
                '''                The output optical power of this port in units of 0.01dBm.
                If the port is an aggregate of multiple physical channels,
                this attribute is the total power or sum of all channels. If
                avg/min/max statistics are not supported, the target is
                expected to just supply the instant value
                ''',
                'output_power',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('polarization-dependent-loss', REFERENCE_CLASS, 'PolarizationDependentLoss' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.OpticalChannel.State.PolarizationDependentLoss', 
                [], [], 
                '''                Polarization Dependent Loss of an optical channel
                in dB as reported by receiver
                ''',
                'polarization_dependent_loss',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('polarization-mode-dispersion', REFERENCE_CLASS, 'PolarizationModeDispersion' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.OpticalChannel.State.PolarizationModeDispersion', 
                [], [], 
                '''                Polarization Mode Dispersion of an optical channel
                in ps as reported by receiver
                ''',
                'polarization_mode_dispersion',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('second-order-polarization-mode-dispersion', REFERENCE_CLASS, 'SecondOrderPolarizationModeDispersion' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.OpticalChannel.State.SecondOrderPolarizationModeDispersion', 
                [], [], 
                '''                Second Order Polarization Mode Dispersion of an optical
                channel in ps^2 as reported by receiver
                ''',
                'second_order_polarization_mode_dispersion',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('target-output-power', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Target output optical power level of the optical channel,
                expressed in increments of 0.01 dBm (decibel-milliwats)
                ''',
                'target_output_power',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'state',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component.OpticalChannel' : {
        'meta_info' : _MetaInfoClass('Components.Component.OpticalChannel',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.OpticalChannel.Config', 
                [], [], 
                '''                Configuration data for optical channels
                ''',
                'config',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.OpticalChannel.State', 
                [], [], 
                '''                Operational state data for optical channels
                ''',
                'state',
                'openconfig-terminal-device', False),
            ],
            'openconfig-terminal-device',
            'optical-channel',
            _yang_ns._namespaces['openconfig-terminal-device'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components.Component' : {
        'meta_info' : _MetaInfoClass('Components.Component',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                References the component name
                ''',
                'name',
                'openconfig-platform', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.Config', 
                [], [], 
                '''                Configuration data for each component
                ''',
                'config',
                'openconfig-platform', False),
            _MetaInfoClassMember('optical-channel', REFERENCE_CLASS, 'OpticalChannel' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.OpticalChannel', 
                [], [], 
                '''                Enclosing container for the list of optical channels
                ''',
                'optical_channel',
                'openconfig-terminal-device', False),
            _MetaInfoClassMember('properties', REFERENCE_CLASS, 'Properties' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.Properties', 
                [], [], 
                '''                Enclosing container 
                ''',
                'properties',
                'openconfig-platform', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.State', 
                [], [], 
                '''                Operational state data for each component
                ''',
                'state',
                'openconfig-platform', False),
            _MetaInfoClassMember('subcomponents', REFERENCE_CLASS, 'Subcomponents' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.Subcomponents', 
                [], [], 
                '''                Enclosing container for subcomponent references
                ''',
                'subcomponents',
                'openconfig-platform', False),
            _MetaInfoClassMember('transceiver', REFERENCE_CLASS, 'Transceiver' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component.Transceiver', 
                [], [], 
                '''                Top-level container for client port transceiver data
                ''',
                'transceiver',
                'openconfig-platform-transceiver', False),
            ],
            'openconfig-platform',
            'component',
            _yang_ns._namespaces['openconfig-platform'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
    'Components' : {
        'meta_info' : _MetaInfoClass('Components',
            False, 
            [
            _MetaInfoClassMember('component', REFERENCE_LIST, 'Component' , 'ydk.models.openconfig.openconfig_platform', 'Components.Component', 
                [], [], 
                '''                List of components, keyed by component name.
                ''',
                'component',
                'openconfig-platform', False),
            ],
            'openconfig-platform',
            'components',
            _yang_ns._namespaces['openconfig-platform'],
        'ydk.models.openconfig.openconfig_platform'
        ),
    },
}
_meta_table['Components.Component.Properties.Property.Config']['meta_info'].parent =_meta_table['Components.Component.Properties.Property']['meta_info']
_meta_table['Components.Component.Properties.Property.State']['meta_info'].parent =_meta_table['Components.Component.Properties.Property']['meta_info']
_meta_table['Components.Component.Properties.Property']['meta_info'].parent =_meta_table['Components.Component.Properties']['meta_info']
_meta_table['Components.Component.Subcomponents.Subcomponent.Config']['meta_info'].parent =_meta_table['Components.Component.Subcomponents.Subcomponent']['meta_info']
_meta_table['Components.Component.Subcomponents.Subcomponent.State']['meta_info'].parent =_meta_table['Components.Component.Subcomponents.Subcomponent']['meta_info']
_meta_table['Components.Component.Subcomponents.Subcomponent']['meta_info'].parent =_meta_table['Components.Component.Subcomponents']['meta_info']
_meta_table['Components.Component.Transceiver.PhysicalChannels.Channel.State.OutputPower']['meta_info'].parent =_meta_table['Components.Component.Transceiver.PhysicalChannels.Channel.State']['meta_info']
_meta_table['Components.Component.Transceiver.PhysicalChannels.Channel.State.InputPower']['meta_info'].parent =_meta_table['Components.Component.Transceiver.PhysicalChannels.Channel.State']['meta_info']
_meta_table['Components.Component.Transceiver.PhysicalChannels.Channel.State.LaserBiasCurrent']['meta_info'].parent =_meta_table['Components.Component.Transceiver.PhysicalChannels.Channel.State']['meta_info']
_meta_table['Components.Component.Transceiver.PhysicalChannels.Channel.Config']['meta_info'].parent =_meta_table['Components.Component.Transceiver.PhysicalChannels.Channel']['meta_info']
_meta_table['Components.Component.Transceiver.PhysicalChannels.Channel.State']['meta_info'].parent =_meta_table['Components.Component.Transceiver.PhysicalChannels.Channel']['meta_info']
_meta_table['Components.Component.Transceiver.PhysicalChannels.Channel']['meta_info'].parent =_meta_table['Components.Component.Transceiver.PhysicalChannels']['meta_info']
_meta_table['Components.Component.Transceiver.Config']['meta_info'].parent =_meta_table['Components.Component.Transceiver']['meta_info']
_meta_table['Components.Component.Transceiver.State']['meta_info'].parent =_meta_table['Components.Component.Transceiver']['meta_info']
_meta_table['Components.Component.Transceiver.PhysicalChannels']['meta_info'].parent =_meta_table['Components.Component.Transceiver']['meta_info']
_meta_table['Components.Component.OpticalChannel.State.OutputPower']['meta_info'].parent =_meta_table['Components.Component.OpticalChannel.State']['meta_info']
_meta_table['Components.Component.OpticalChannel.State.InputPower']['meta_info'].parent =_meta_table['Components.Component.OpticalChannel.State']['meta_info']
_meta_table['Components.Component.OpticalChannel.State.LaserBiasCurrent']['meta_info'].parent =_meta_table['Components.Component.OpticalChannel.State']['meta_info']
_meta_table['Components.Component.OpticalChannel.State.ChromaticDispersion']['meta_info'].parent =_meta_table['Components.Component.OpticalChannel.State']['meta_info']
_meta_table['Components.Component.OpticalChannel.State.PolarizationModeDispersion']['meta_info'].parent =_meta_table['Components.Component.OpticalChannel.State']['meta_info']
_meta_table['Components.Component.OpticalChannel.State.SecondOrderPolarizationModeDispersion']['meta_info'].parent =_meta_table['Components.Component.OpticalChannel.State']['meta_info']
_meta_table['Components.Component.OpticalChannel.State.PolarizationDependentLoss']['meta_info'].parent =_meta_table['Components.Component.OpticalChannel.State']['meta_info']
_meta_table['Components.Component.OpticalChannel.Config']['meta_info'].parent =_meta_table['Components.Component.OpticalChannel']['meta_info']
_meta_table['Components.Component.OpticalChannel.State']['meta_info'].parent =_meta_table['Components.Component.OpticalChannel']['meta_info']
_meta_table['Components.Component.Config']['meta_info'].parent =_meta_table['Components.Component']['meta_info']
_meta_table['Components.Component.State']['meta_info'].parent =_meta_table['Components.Component']['meta_info']
_meta_table['Components.Component.Properties']['meta_info'].parent =_meta_table['Components.Component']['meta_info']
_meta_table['Components.Component.Subcomponents']['meta_info'].parent =_meta_table['Components.Component']['meta_info']
_meta_table['Components.Component.Transceiver']['meta_info'].parent =_meta_table['Components.Component']['meta_info']
_meta_table['Components.Component.OpticalChannel']['meta_info'].parent =_meta_table['Components.Component']['meta_info']
_meta_table['Components.Component']['meta_info'].parent =_meta_table['Components']['meta_info']

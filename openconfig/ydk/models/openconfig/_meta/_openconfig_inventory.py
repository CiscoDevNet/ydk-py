


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'Components.Component.Config' : {
        'meta_info' : _MetaInfoClass('Components.Component.Config',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name for the component -- this may not be a
                configurable parameter on many implementations
                ''',
                'name',
                'openconfig-inventory', False),
            ],
            'openconfig-inventory',
            'config',
            _yang_ns._namespaces['openconfig-inventory'],
        'ydk.models.openconfig.openconfig_inventory'
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
                'openconfig-inventory', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Unique identifier assigned by the system for the
                component
                ''',
                'id',
                'openconfig-inventory', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name for the component -- this may not be a
                configurable parameter on many implementations
                ''',
                'name',
                'openconfig-inventory', False),
            _MetaInfoClassMember('part_no', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                System-assigned part number for the component.  This should
                be present in particular if the component is also an FRU
                (field replacable unit)
                ''',
                'part_no',
                'openconfig-inventory', False),
            _MetaInfoClassMember('serial_no', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                System-assigned serial number of the component.
                ''',
                'serial_no',
                'openconfig-inventory', False),
            _MetaInfoClassMember('type', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Type of component as identified by the system
                ''',
                'type',
                'openconfig-inventory', False, [
                    _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'OpenconfigHardwareComponentIdentity' , 'ydk.models.openconfig.openconfig_inventory_types', 'OpenconfigHardwareComponentIdentity', 
                        [], [], 
                        '''                        Type of component as identified by the system
                        ''',
                        'type',
                        'openconfig-inventory', False),
                    _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'OpenconfigSoftwareComponentIdentity' , 'ydk.models.openconfig.openconfig_inventory_types', 'OpenconfigSoftwareComponentIdentity', 
                        [], [], 
                        '''                        Type of component as identified by the system
                        ''',
                        'type',
                        'openconfig-inventory', False),
                ]),
            ],
            'openconfig-inventory',
            'state',
            _yang_ns._namespaces['openconfig-inventory'],
        'ydk.models.openconfig.openconfig_inventory'
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
                'openconfig-inventory', False),
            _MetaInfoClassMember('value', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Property values can take on a variety of types.  Signed and
                unsigned integer types may be provided in smaller sizes,
                e.g., int8, uint16, etc.
                ''',
                'value',
                'openconfig-inventory', False, [
                    _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                        [], [], 
                        '''                        Property values can take on a variety of types.  Signed and
                        unsigned integer types may be provided in smaller sizes,
                        e.g., int8, uint16, etc.
                        ''',
                        'value',
                        'openconfig-inventory', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'bool' , None, None, 
                        [], [], 
                        '''                        Property values can take on a variety of types.  Signed and
                        unsigned integer types may be provided in smaller sizes,
                        e.g., int8, uint16, etc.
                        ''',
                        'value',
                        'openconfig-inventory', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                        [(-9223372036854775808, 9223372036854775807)], [], 
                        '''                        Property values can take on a variety of types.  Signed and
                        unsigned integer types may be provided in smaller sizes,
                        e.g., int8, uint16, etc.
                        ''',
                        'value',
                        'openconfig-inventory', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'long' , None, None, 
                        [(0, 18446744073709551615L)], [], 
                        '''                        Property values can take on a variety of types.  Signed and
                        unsigned integer types may be provided in smaller sizes,
                        e.g., int8, uint16, etc.
                        ''',
                        'value',
                        'openconfig-inventory', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'Decimal64' , None, None, 
                        [('-92233720368547758.08', '92233720368547758.07')], [], 
                        '''                        Property values can take on a variety of types.  Signed and
                        unsigned integer types may be provided in smaller sizes,
                        e.g., int8, uint16, etc.
                        ''',
                        'value',
                        'openconfig-inventory', False),
                ]),
            ],
            'openconfig-inventory',
            'config',
            _yang_ns._namespaces['openconfig-inventory'],
        'ydk.models.openconfig.openconfig_inventory'
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
                'openconfig-inventory', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                System-supplied name of the property -- this is typically
                non-configurable
                ''',
                'name',
                'openconfig-inventory', False),
            _MetaInfoClassMember('value', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Property values can take on a variety of types.  Signed and
                unsigned integer types may be provided in smaller sizes,
                e.g., int8, uint16, etc.
                ''',
                'value',
                'openconfig-inventory', False, [
                    _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                        [], [], 
                        '''                        Property values can take on a variety of types.  Signed and
                        unsigned integer types may be provided in smaller sizes,
                        e.g., int8, uint16, etc.
                        ''',
                        'value',
                        'openconfig-inventory', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'bool' , None, None, 
                        [], [], 
                        '''                        Property values can take on a variety of types.  Signed and
                        unsigned integer types may be provided in smaller sizes,
                        e.g., int8, uint16, etc.
                        ''',
                        'value',
                        'openconfig-inventory', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                        [(-9223372036854775808, 9223372036854775807)], [], 
                        '''                        Property values can take on a variety of types.  Signed and
                        unsigned integer types may be provided in smaller sizes,
                        e.g., int8, uint16, etc.
                        ''',
                        'value',
                        'openconfig-inventory', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'long' , None, None, 
                        [(0, 18446744073709551615L)], [], 
                        '''                        Property values can take on a variety of types.  Signed and
                        unsigned integer types may be provided in smaller sizes,
                        e.g., int8, uint16, etc.
                        ''',
                        'value',
                        'openconfig-inventory', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'Decimal64' , None, None, 
                        [('-92233720368547758.08', '92233720368547758.07')], [], 
                        '''                        Property values can take on a variety of types.  Signed and
                        unsigned integer types may be provided in smaller sizes,
                        e.g., int8, uint16, etc.
                        ''',
                        'value',
                        'openconfig-inventory', False),
                ]),
            ],
            'openconfig-inventory',
            'state',
            _yang_ns._namespaces['openconfig-inventory'],
        'ydk.models.openconfig.openconfig_inventory'
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
                'openconfig-inventory', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_inventory', 'Components.Component.Properties.Property.Config', 
                [], [], 
                '''                Configuration data for each property
                ''',
                'config',
                'openconfig-inventory', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_inventory', 'Components.Component.Properties.Property.State', 
                [], [], 
                '''                Operational state data for each property
                ''',
                'state',
                'openconfig-inventory', False),
            ],
            'openconfig-inventory',
            'property',
            _yang_ns._namespaces['openconfig-inventory'],
        'ydk.models.openconfig.openconfig_inventory'
        ),
    },
    'Components.Component.Properties' : {
        'meta_info' : _MetaInfoClass('Components.Component.Properties',
            False, 
            [
            _MetaInfoClassMember('property', REFERENCE_LIST, 'Property' , 'ydk.models.openconfig.openconfig_inventory', 'Components.Component.Properties.Property', 
                [], [], 
                '''                List of system properties for the component
                ''',
                'property',
                'openconfig-inventory', False),
            ],
            'openconfig-inventory',
            'properties',
            _yang_ns._namespaces['openconfig-inventory'],
        'ydk.models.openconfig.openconfig_inventory'
        ),
    },
    'Components.Component.Subcomponents.Subcomponent.Config' : {
        'meta_info' : _MetaInfoClass('Components.Component.Subcomponents.Subcomponent.Config',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the subcomponent -- should reflect the name of
                the referenced component
                ''',
                'name',
                'openconfig-inventory', False),
            ],
            'openconfig-inventory',
            'config',
            _yang_ns._namespaces['openconfig-inventory'],
        'ydk.models.openconfig.openconfig_inventory'
        ),
    },
    'Components.Component.Subcomponents.Subcomponent.State' : {
        'meta_info' : _MetaInfoClass('Components.Component.Subcomponents.Subcomponent.State',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the subcomponent -- should reflect the name of
                the referenced component
                ''',
                'name',
                'openconfig-inventory', False),
            _MetaInfoClassMember('reference', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                References the corresponding component in the overall
                list of inventory components
                ''',
                'reference',
                'openconfig-inventory', False),
            ],
            'openconfig-inventory',
            'state',
            _yang_ns._namespaces['openconfig-inventory'],
        'ydk.models.openconfig.openconfig_inventory'
        ),
    },
    'Components.Component.Subcomponents.Subcomponent' : {
        'meta_info' : _MetaInfoClass('Components.Component.Subcomponents.Subcomponent',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the subcomponent name
                ''',
                'name',
                'openconfig-inventory', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_inventory', 'Components.Component.Subcomponents.Subcomponent.Config', 
                [], [], 
                '''                Configuration data 
                ''',
                'config',
                'openconfig-inventory', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_inventory', 'Components.Component.Subcomponents.Subcomponent.State', 
                [], [], 
                '''                Operational state data 
                ''',
                'state',
                'openconfig-inventory', False),
            ],
            'openconfig-inventory',
            'subcomponent',
            _yang_ns._namespaces['openconfig-inventory'],
        'ydk.models.openconfig.openconfig_inventory'
        ),
    },
    'Components.Component.Subcomponents' : {
        'meta_info' : _MetaInfoClass('Components.Component.Subcomponents',
            False, 
            [
            _MetaInfoClassMember('subcomponent', REFERENCE_LIST, 'Subcomponent' , 'ydk.models.openconfig.openconfig_inventory', 'Components.Component.Subcomponents.Subcomponent', 
                [], [], 
                '''                List of subcomponent references
                ''',
                'subcomponent',
                'openconfig-inventory', False),
            ],
            'openconfig-inventory',
            'subcomponents',
            _yang_ns._namespaces['openconfig-inventory'],
        'ydk.models.openconfig.openconfig_inventory'
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
                'openconfig-inventory', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_inventory', 'Components.Component.Config', 
                [], [], 
                '''                Configuration data for each component
                ''',
                'config',
                'openconfig-inventory', False),
            _MetaInfoClassMember('properties', REFERENCE_CLASS, 'Properties' , 'ydk.models.openconfig.openconfig_inventory', 'Components.Component.Properties', 
                [], [], 
                '''                Enclosing container 
                ''',
                'properties',
                'openconfig-inventory', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_inventory', 'Components.Component.State', 
                [], [], 
                '''                Operational state data for each component
                ''',
                'state',
                'openconfig-inventory', False),
            _MetaInfoClassMember('subcomponents', REFERENCE_CLASS, 'Subcomponents' , 'ydk.models.openconfig.openconfig_inventory', 'Components.Component.Subcomponents', 
                [], [], 
                '''                Enclosing container for subcomponent references
                ''',
                'subcomponents',
                'openconfig-inventory', False),
            ],
            'openconfig-inventory',
            'component',
            _yang_ns._namespaces['openconfig-inventory'],
        'ydk.models.openconfig.openconfig_inventory'
        ),
    },
    'Components' : {
        'meta_info' : _MetaInfoClass('Components',
            False, 
            [
            _MetaInfoClassMember('component', REFERENCE_LIST, 'Component' , 'ydk.models.openconfig.openconfig_inventory', 'Components.Component', 
                [], [], 
                '''                List of components, keyed by component name.
                ''',
                'component',
                'openconfig-inventory', False),
            ],
            'openconfig-inventory',
            'components',
            _yang_ns._namespaces['openconfig-inventory'],
        'ydk.models.openconfig.openconfig_inventory'
        ),
    },
}
_meta_table['Components.Component.Properties.Property.Config']['meta_info'].parent =_meta_table['Components.Component.Properties.Property']['meta_info']
_meta_table['Components.Component.Properties.Property.State']['meta_info'].parent =_meta_table['Components.Component.Properties.Property']['meta_info']
_meta_table['Components.Component.Properties.Property']['meta_info'].parent =_meta_table['Components.Component.Properties']['meta_info']
_meta_table['Components.Component.Subcomponents.Subcomponent.Config']['meta_info'].parent =_meta_table['Components.Component.Subcomponents.Subcomponent']['meta_info']
_meta_table['Components.Component.Subcomponents.Subcomponent.State']['meta_info'].parent =_meta_table['Components.Component.Subcomponents.Subcomponent']['meta_info']
_meta_table['Components.Component.Subcomponents.Subcomponent']['meta_info'].parent =_meta_table['Components.Component.Subcomponents']['meta_info']
_meta_table['Components.Component.Config']['meta_info'].parent =_meta_table['Components.Component']['meta_info']
_meta_table['Components.Component.State']['meta_info'].parent =_meta_table['Components.Component']['meta_info']
_meta_table['Components.Component.Properties']['meta_info'].parent =_meta_table['Components.Component']['meta_info']
_meta_table['Components.Component.Subcomponents']['meta_info'].parent =_meta_table['Components.Component']['meta_info']
_meta_table['Components.Component']['meta_info'].parent =_meta_table['Components']['meta_info']

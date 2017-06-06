


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Interfaces.Interface.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Config',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                A textual description of the interface.
                
                A server implementation MAY map this leaf to the ifAlias
                MIB object.  Such an implementation needs to use some
                mechanism to handle the differences in size and characters
                allowed between this leaf and ifAlias.  The definition of
                such a mechanism is outside the scope of this document.
                
                Since ifAlias is defined to be stored in non-volatile
                storage, the MIB implementation MUST map ifAlias to the
                value of 'description' in the persistently stored
                datastore.
                
                Specifically, if the device supports ':startup', when
                ifAlias is read the device MUST return the value of
                'description' in the 'startup' datastore, and when it is
                written, it MUST be written to the 'running' and 'startup'
                datastores.  Note that it is up to the implementation to
                
                decide whether to modify this single leaf in 'startup' or
                perform an implicit copy-config from 'running' to
                'startup'.
                
                If the device does not support ':startup', ifAlias MUST
                be mapped to the 'description' leaf in the 'running'
                datastore.
                ''',
                'description',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                This leaf contains the configured, desired state of the
                interface.
                
                Systems that implement the IF-MIB use the value of this
                leaf in the 'running' datastore to set
                IF-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry
                has been initialized, as described in RFC 2863.
                
                Changes in this leaf in the 'running' datastore are
                reflected in ifAdminStatus, but if ifAdminStatus is
                changed over SNMP, this leaf is not affected.
                ''',
                'enabled',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Set the max transmission unit size in octets
                for the physical interface.  If this is not set, the mtu is
                set to the operational default -- e.g., 1514 bytes on an
                Ethernet interface.
                ''',
                'mtu',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                The name of the interface.
                
                A device MAY restrict the allowed values for this leaf,
                possibly depending on the type of the interface.
                For system-controlled interfaces, this leaf is the
                device-specific name of the interface.  The 'config false'
                list interfaces/interface[name]/state contains the currently
                existing interfaces on the device.
                
                If a client tries to create configuration for a
                system-controlled interface that is not present in the
                corresponding state list, the server MAY reject
                the request if the implementation does not support
                pre-provisioning of interfaces or if the name refers to
                an interface that can never exist in the system.  A
                NETCONF server MUST reply with an rpc-error with the
                error-tag 'invalid-value' in this case.
                
                The IETF model in RFC 7223 provides YANG features for the
                following (i.e., pre-provisioning and arbitrary-names),
                however they are omitted here:
                
                 If the device supports pre-provisioning of interface
                 configuration, the 'pre-provisioning' feature is
                 advertised.
                
                 If the device allows arbitrarily named user-controlled
                 interfaces, the 'arbitrary-names' feature is advertised.
                
                When a configured user-controlled interface is created by
                the system, it is instantiated with the same name in the
                /interfaces/interface[name]/state list.
                ''',
                'name',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'InterfaceTypeIdentity' , 'ydk.models.ietf.ietf_interfaces', 'InterfaceTypeIdentity', 
                [], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                The type of the interface.
                
                When an interface entry is created, a server MAY
                initialize the type leaf with a valid value, e.g., if it
                is possible to derive the type from the name of the
                interface.
                
                If a client tries to set the type of an interface to a
                value that can never be used by the system, e.g., if the
                type is not supported or if the type does not match the
                name of the interface, the server MUST reject the request.
                A NETCONF server MUST reply with an rpc-error with the
                error-tag 'invalid-value' in this case.
                ''',
                'type',
                'openconfig-interfaces', False),
            ],
            'openconfig-interfaces',
            'config',
            _yang_ns._namespaces['openconfig-interfaces'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.State.Counters' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.State.Counters',
            False, 
            [
            _MetaInfoClassMember('in-broadcast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                The number of packets, delivered by this sub-layer to a
                higher (sub-)layer, that were addressed to a broadcast
                address at this sub-layer.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_broadcast_pkts',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('in-discards', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                Changed the counter type to counter64.
                
                The number of inbound packets that were chosen to be
                discarded even though no errors had been detected to
                prevent their being deliverable to a higher-layer
                protocol.  One possible reason for discarding such a
                packet could be to free up buffer space.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_discards',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('in-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                Changed the counter type to counter64.
                
                For packet-oriented interfaces, the number of inbound
                packets that contained errors preventing them from being
                deliverable to a higher-layer protocol.  For character-
                oriented or fixed-length interfaces, the number of
                inbound transmission units that contained errors
                preventing them from being deliverable to a higher-layer
                protocol.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_errors',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('in-multicast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                
                The number of packets, delivered by this sub-layer to a
                higher (sub-)layer, that were addressed to a multicast
                address at this sub-layer.  For a MAC-layer protocol,
                this includes both Group and Functional addresses.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_multicast_pkts',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('in-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                The total number of octets received on the interface,
                including framing characters.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_octets',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('in-unicast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                The number of packets, delivered by this sub-layer to a
                higher (sub-)layer, that were not addressed to a
                multicast or broadcast address at this sub-layer.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_unicast_pkts',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('in-unknown-protos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                Changed the counter type to counter64.
                
                For packet-oriented interfaces, the number of packets
                received via the interface that were discarded because
                of an unknown or unsupported protocol.  For
                character-oriented or fixed-length interfaces that
                support protocol multiplexing, the number of
                transmission units received via the interface that were
                discarded because of an unknown or unsupported protocol.
                For any interface that does not support protocol
                multiplexing, this counter is not present.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_unknown_protos',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('last-clear', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Indicates the last time the interface counters were
                cleared.
                ''',
                'last_clear',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('out-broadcast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                The total number of packets that higher-level protocols
                requested be transmitted, and that were addressed to a
                broadcast address at this sub-layer, including those
                that were discarded or not sent.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'out_broadcast_pkts',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('out-discards', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                Changed the counter type to counter64.
                
                The number of outbound packets that were chosen to be
                discarded even though no errors had been detected to
                prevent their being transmitted.  One possible reason
                for discarding such a packet could be to free up buffer
                space.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'out_discards',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('out-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                Changed the counter type to counter64.
                
                For packet-oriented interfaces, the number of outbound
                packets that could not be transmitted because of errors.
                For character-oriented or fixed-length interfaces, the
                number of outbound transmission units that could not be
                transmitted because of errors.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'out_errors',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('out-multicast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                Changed the counter type to counter64.
                
                The total number of packets that higher-level protocols
                requested be transmitted, and that were addressed to a
                multicast address at this sub-layer, including those
                that were discarded or not sent.  For a MAC-layer
                protocol, this includes both Group and Functional
                addresses.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'out_multicast_pkts',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('out-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                Changed the counter type to counter64.
                
                The total number of octets transmitted out of the
                interface, including framing characters.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'out_octets',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('out-unicast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                The total number of packets that higher-level protocols
                requested be transmitted, and that were not addressed
                to a multicast or broadcast address at this sub-layer,
                including those that were discarded or not sent.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'out_unicast_pkts',
                'openconfig-interfaces', False),
            ],
            'openconfig-interfaces',
            'counters',
            _yang_ns._namespaces['openconfig-interfaces'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.State.AdminStatusEnum' : _MetaInfoEnum('AdminStatusEnum', 'ydk.models.openconfig.openconfig_interfaces',
        {
            'UP':'UP',
            'DOWN':'DOWN',
            'TESTING':'TESTING',
        }, 'openconfig-interfaces', _yang_ns._namespaces['openconfig-interfaces']),
    'Interfaces.Interface.State.OperStatusEnum' : _MetaInfoEnum('OperStatusEnum', 'ydk.models.openconfig.openconfig_interfaces',
        {
            'UP':'UP',
            'DOWN':'DOWN',
            'TESTING':'TESTING',
            'UNKNOWN':'UNKNOWN',
            'DORMANT':'DORMANT',
            'NOT-PRESENT':'NOT_PRESENT',
            'LOWER-LAYER-DOWN':'LOWER_LAYER_DOWN',
        }, 'openconfig-interfaces', _yang_ns._namespaces['openconfig-interfaces']),
    'Interfaces.Interface.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.State',
            False, 
            [
            _MetaInfoClassMember('admin-status', REFERENCE_ENUM_CLASS, 'AdminStatusEnum' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.State.AdminStatusEnum', 
                [], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                The desired state of the interface.  In RFC 7223 this leaf
                has the same read semantics as ifAdminStatus.  Here, it
                reflects the administrative state as set by enabling or
                disabling the interface.
                ''',
                'admin_status',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.State.Counters', 
                [], [], 
                '''                A collection of interface-related statistics objects.
                ''',
                'counters',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                A textual description of the interface.
                
                A server implementation MAY map this leaf to the ifAlias
                MIB object.  Such an implementation needs to use some
                mechanism to handle the differences in size and characters
                allowed between this leaf and ifAlias.  The definition of
                such a mechanism is outside the scope of this document.
                
                Since ifAlias is defined to be stored in non-volatile
                storage, the MIB implementation MUST map ifAlias to the
                value of 'description' in the persistently stored
                datastore.
                
                Specifically, if the device supports ':startup', when
                ifAlias is read the device MUST return the value of
                'description' in the 'startup' datastore, and when it is
                written, it MUST be written to the 'running' and 'startup'
                datastores.  Note that it is up to the implementation to
                
                decide whether to modify this single leaf in 'startup' or
                perform an implicit copy-config from 'running' to
                'startup'.
                
                If the device does not support ':startup', ifAlias MUST
                be mapped to the 'description' leaf in the 'running'
                datastore.
                ''',
                'description',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                This leaf contains the configured, desired state of the
                interface.
                
                Systems that implement the IF-MIB use the value of this
                leaf in the 'running' datastore to set
                IF-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry
                has been initialized, as described in RFC 2863.
                
                Changes in this leaf in the 'running' datastore are
                reflected in ifAdminStatus, but if ifAdminStatus is
                changed over SNMP, this leaf is not affected.
                ''',
                'enabled',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('hardware-port', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                References the hardware port in the device inventory
                ''',
                'hardware_port',
                'openconfig-platform', False),
            _MetaInfoClassMember('ifindex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                System assigned number for each interface.  Corresponds to
                ifIndex object in SNMP Interface MIB
                ''',
                'ifindex',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('last-change', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Date and time of the last state change of the interface
                (e.g., up-to-down transition).   This corresponds to the
                ifLastChange object in the standard interface MIB.
                ''',
                'last_change',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Set the max transmission unit size in octets
                for the physical interface.  If this is not set, the mtu is
                set to the operational default -- e.g., 1514 bytes on an
                Ethernet interface.
                ''',
                'mtu',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                The name of the interface.
                
                A device MAY restrict the allowed values for this leaf,
                possibly depending on the type of the interface.
                For system-controlled interfaces, this leaf is the
                device-specific name of the interface.  The 'config false'
                list interfaces/interface[name]/state contains the currently
                existing interfaces on the device.
                
                If a client tries to create configuration for a
                system-controlled interface that is not present in the
                corresponding state list, the server MAY reject
                the request if the implementation does not support
                pre-provisioning of interfaces or if the name refers to
                an interface that can never exist in the system.  A
                NETCONF server MUST reply with an rpc-error with the
                error-tag 'invalid-value' in this case.
                
                The IETF model in RFC 7223 provides YANG features for the
                following (i.e., pre-provisioning and arbitrary-names),
                however they are omitted here:
                
                 If the device supports pre-provisioning of interface
                 configuration, the 'pre-provisioning' feature is
                 advertised.
                
                 If the device allows arbitrarily named user-controlled
                 interfaces, the 'arbitrary-names' feature is advertised.
                
                When a configured user-controlled interface is created by
                the system, it is instantiated with the same name in the
                /interfaces/interface[name]/state list.
                ''',
                'name',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('oper-status', REFERENCE_ENUM_CLASS, 'OperStatusEnum' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.State.OperStatusEnum', 
                [], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                The current operational state of the interface.
                
                This leaf has the same semantics as ifOperStatus.
                ''',
                'oper_status',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'InterfaceTypeIdentity' , 'ydk.models.ietf.ietf_interfaces', 'InterfaceTypeIdentity', 
                [], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                The type of the interface.
                
                When an interface entry is created, a server MAY
                initialize the type leaf with a valid value, e.g., if it
                is possible to derive the type from the name of the
                interface.
                
                If a client tries to set the type of an interface to a
                value that can never be used by the system, e.g., if the
                type is not supported or if the type does not match the
                name of the interface, the server MUST reject the request.
                A NETCONF server MUST reply with an rpc-error with the
                error-tag 'invalid-value' in this case.
                ''',
                'type',
                'openconfig-interfaces', False),
            ],
            'openconfig-interfaces',
            'state',
            _yang_ns._namespaces['openconfig-interfaces'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.HoldTime.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.HoldTime.Config',
            False, 
            [
            _MetaInfoClassMember('down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dampens advertisement when the interface transitions from
                up to down.  A zero value means dampening is turned off,
                i.e., immediate notification.
                ''',
                'down',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dampens advertisement when the interface
                transitions from down to up.  A zero value means dampening
                is turned off, i.e., immediate notification.
                ''',
                'up',
                'openconfig-interfaces', False),
            ],
            'openconfig-interfaces',
            'config',
            _yang_ns._namespaces['openconfig-interfaces'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.HoldTime.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.HoldTime.State',
            False, 
            [
            _MetaInfoClassMember('down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dampens advertisement when the interface transitions from
                up to down.  A zero value means dampening is turned off,
                i.e., immediate notification.
                ''',
                'down',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dampens advertisement when the interface
                transitions from down to up.  A zero value means dampening
                is turned off, i.e., immediate notification.
                ''',
                'up',
                'openconfig-interfaces', False),
            ],
            'openconfig-interfaces',
            'state',
            _yang_ns._namespaces['openconfig-interfaces'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.HoldTime' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.HoldTime',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.HoldTime.Config', 
                [], [], 
                '''                Configuration data for interface hold-time settings.
                ''',
                'config',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.HoldTime.State', 
                [], [], 
                '''                Operational state data for interface hold-time.
                ''',
                'state',
                'openconfig-interfaces', False),
            ],
            'openconfig-interfaces',
            'hold-time',
            _yang_ns._namespaces['openconfig-interfaces'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Config',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                A textual description of the interface.
                
                A server implementation MAY map this leaf to the ifAlias
                MIB object.  Such an implementation needs to use some
                mechanism to handle the differences in size and characters
                allowed between this leaf and ifAlias.  The definition of
                such a mechanism is outside the scope of this document.
                
                Since ifAlias is defined to be stored in non-volatile
                storage, the MIB implementation MUST map ifAlias to the
                value of 'description' in the persistently stored
                datastore.
                
                Specifically, if the device supports ':startup', when
                ifAlias is read the device MUST return the value of
                'description' in the 'startup' datastore, and when it is
                written, it MUST be written to the 'running' and 'startup'
                datastores.  Note that it is up to the implementation to
                
                decide whether to modify this single leaf in 'startup' or
                perform an implicit copy-config from 'running' to
                'startup'.
                
                If the device does not support ':startup', ifAlias MUST
                be mapped to the 'description' leaf in the 'running'
                datastore.
                ''',
                'description',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                This leaf contains the configured, desired state of the
                interface.
                
                Systems that implement the IF-MIB use the value of this
                leaf in the 'running' datastore to set
                IF-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry
                has been initialized, as described in RFC 2863.
                
                Changes in this leaf in the 'running' datastore are
                reflected in ifAdminStatus, but if ifAdminStatus is
                changed over SNMP, this leaf is not affected.
                ''',
                'enabled',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The index of the subinterface, or logical interface number.
                On systems with no support for subinterfaces, or not using
                subinterfaces, this value should default to 0, i.e., the
                default subinterface.
                ''',
                'index',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                The name of the interface.
                
                A device MAY restrict the allowed values for this leaf,
                possibly depending on the type of the interface.
                For system-controlled interfaces, this leaf is the
                device-specific name of the interface.  The 'config false'
                list interfaces/interface[name]/state contains the currently
                existing interfaces on the device.
                
                If a client tries to create configuration for a
                system-controlled interface that is not present in the
                corresponding state list, the server MAY reject
                the request if the implementation does not support
                pre-provisioning of interfaces or if the name refers to
                an interface that can never exist in the system.  A
                NETCONF server MUST reply with an rpc-error with the
                error-tag 'invalid-value' in this case.
                
                The IETF model in RFC 7223 provides YANG features for the
                following (i.e., pre-provisioning and arbitrary-names),
                however they are omitted here:
                
                 If the device supports pre-provisioning of interface
                 configuration, the 'pre-provisioning' feature is
                 advertised.
                
                 If the device allows arbitrarily named user-controlled
                 interfaces, the 'arbitrary-names' feature is advertised.
                
                When a configured user-controlled interface is created by
                the system, it is instantiated with the same name in the
                /interfaces/interface[name]/state list.
                ''',
                'name',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('unnumbered', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates that the subinterface is unnumbered, and provides
                a reference to the subinterface that provides the IP
                address information (v4, v6 or both) for the current
                subinterface.
                ''',
                'unnumbered',
                'openconfig-interfaces', False),
            ],
            'openconfig-interfaces',
            'config',
            _yang_ns._namespaces['openconfig-interfaces'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.State.Counters' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.State.Counters',
            False, 
            [
            _MetaInfoClassMember('in-broadcast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                The number of packets, delivered by this sub-layer to a
                higher (sub-)layer, that were addressed to a broadcast
                address at this sub-layer.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_broadcast_pkts',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('in-discards', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                Changed the counter type to counter64.
                
                The number of inbound packets that were chosen to be
                discarded even though no errors had been detected to
                prevent their being deliverable to a higher-layer
                protocol.  One possible reason for discarding such a
                packet could be to free up buffer space.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_discards',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('in-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                Changed the counter type to counter64.
                
                For packet-oriented interfaces, the number of inbound
                packets that contained errors preventing them from being
                deliverable to a higher-layer protocol.  For character-
                oriented or fixed-length interfaces, the number of
                inbound transmission units that contained errors
                preventing them from being deliverable to a higher-layer
                protocol.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_errors',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('in-multicast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                
                The number of packets, delivered by this sub-layer to a
                higher (sub-)layer, that were addressed to a multicast
                address at this sub-layer.  For a MAC-layer protocol,
                this includes both Group and Functional addresses.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_multicast_pkts',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('in-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                The total number of octets received on the interface,
                including framing characters.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_octets',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('in-unicast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                The number of packets, delivered by this sub-layer to a
                higher (sub-)layer, that were not addressed to a
                multicast or broadcast address at this sub-layer.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_unicast_pkts',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('in-unknown-protos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                Changed the counter type to counter64.
                
                For packet-oriented interfaces, the number of packets
                received via the interface that were discarded because
                of an unknown or unsupported protocol.  For
                character-oriented or fixed-length interfaces that
                support protocol multiplexing, the number of
                transmission units received via the interface that were
                discarded because of an unknown or unsupported protocol.
                For any interface that does not support protocol
                multiplexing, this counter is not present.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_unknown_protos',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('last-clear', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Indicates the last time the interface counters were
                cleared.
                ''',
                'last_clear',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('out-broadcast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                The total number of packets that higher-level protocols
                requested be transmitted, and that were addressed to a
                broadcast address at this sub-layer, including those
                that were discarded or not sent.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'out_broadcast_pkts',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('out-discards', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                Changed the counter type to counter64.
                
                The number of outbound packets that were chosen to be
                discarded even though no errors had been detected to
                prevent their being transmitted.  One possible reason
                for discarding such a packet could be to free up buffer
                space.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'out_discards',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('out-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                Changed the counter type to counter64.
                
                For packet-oriented interfaces, the number of outbound
                packets that could not be transmitted because of errors.
                For character-oriented or fixed-length interfaces, the
                number of outbound transmission units that could not be
                transmitted because of errors.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'out_errors',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('out-multicast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                Changed the counter type to counter64.
                
                The total number of packets that higher-level protocols
                requested be transmitted, and that were addressed to a
                multicast address at this sub-layer, including those
                that were discarded or not sent.  For a MAC-layer
                protocol, this includes both Group and Functional
                addresses.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'out_multicast_pkts',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('out-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                Changed the counter type to counter64.
                
                The total number of octets transmitted out of the
                interface, including framing characters.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'out_octets',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('out-unicast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                The total number of packets that higher-level protocols
                requested be transmitted, and that were not addressed
                to a multicast or broadcast address at this sub-layer,
                including those that were discarded or not sent.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'out_unicast_pkts',
                'openconfig-interfaces', False),
            ],
            'openconfig-interfaces',
            'counters',
            _yang_ns._namespaces['openconfig-interfaces'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.State.AdminStatusEnum' : _MetaInfoEnum('AdminStatusEnum', 'ydk.models.openconfig.openconfig_interfaces',
        {
            'UP':'UP',
            'DOWN':'DOWN',
            'TESTING':'TESTING',
        }, 'openconfig-interfaces', _yang_ns._namespaces['openconfig-interfaces']),
    'Interfaces.Interface.Subinterfaces.Subinterface.State.OperStatusEnum' : _MetaInfoEnum('OperStatusEnum', 'ydk.models.openconfig.openconfig_interfaces',
        {
            'UP':'UP',
            'DOWN':'DOWN',
            'TESTING':'TESTING',
            'UNKNOWN':'UNKNOWN',
            'DORMANT':'DORMANT',
            'NOT-PRESENT':'NOT_PRESENT',
            'LOWER-LAYER-DOWN':'LOWER_LAYER_DOWN',
        }, 'openconfig-interfaces', _yang_ns._namespaces['openconfig-interfaces']),
    'Interfaces.Interface.Subinterfaces.Subinterface.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.State',
            False, 
            [
            _MetaInfoClassMember('admin-status', REFERENCE_ENUM_CLASS, 'AdminStatusEnum' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.State.AdminStatusEnum', 
                [], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                The desired state of the interface.  In RFC 7223 this leaf
                has the same read semantics as ifAdminStatus.  Here, it
                reflects the administrative state as set by enabling or
                disabling the interface.
                ''',
                'admin_status',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.State.Counters', 
                [], [], 
                '''                A collection of interface-related statistics objects.
                ''',
                'counters',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                A textual description of the interface.
                
                A server implementation MAY map this leaf to the ifAlias
                MIB object.  Such an implementation needs to use some
                mechanism to handle the differences in size and characters
                allowed between this leaf and ifAlias.  The definition of
                such a mechanism is outside the scope of this document.
                
                Since ifAlias is defined to be stored in non-volatile
                storage, the MIB implementation MUST map ifAlias to the
                value of 'description' in the persistently stored
                datastore.
                
                Specifically, if the device supports ':startup', when
                ifAlias is read the device MUST return the value of
                'description' in the 'startup' datastore, and when it is
                written, it MUST be written to the 'running' and 'startup'
                datastores.  Note that it is up to the implementation to
                
                decide whether to modify this single leaf in 'startup' or
                perform an implicit copy-config from 'running' to
                'startup'.
                
                If the device does not support ':startup', ifAlias MUST
                be mapped to the 'description' leaf in the 'running'
                datastore.
                ''',
                'description',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                This leaf contains the configured, desired state of the
                interface.
                
                Systems that implement the IF-MIB use the value of this
                leaf in the 'running' datastore to set
                IF-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry
                has been initialized, as described in RFC 2863.
                
                Changes in this leaf in the 'running' datastore are
                reflected in ifAdminStatus, but if ifAdminStatus is
                changed over SNMP, this leaf is not affected.
                ''',
                'enabled',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('ifindex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                System assigned number for each interface.  Corresponds to
                ifIndex object in SNMP Interface MIB
                ''',
                'ifindex',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The index of the subinterface, or logical interface number.
                On systems with no support for subinterfaces, or not using
                subinterfaces, this value should default to 0, i.e., the
                default subinterface.
                ''',
                'index',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('last-change', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Date and time of the last state change of the interface
                (e.g., up-to-down transition).   This corresponds to the
                ifLastChange object in the standard interface MIB.
                ''',
                'last_change',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                The name of the interface.
                
                A device MAY restrict the allowed values for this leaf,
                possibly depending on the type of the interface.
                For system-controlled interfaces, this leaf is the
                device-specific name of the interface.  The 'config false'
                list interfaces/interface[name]/state contains the currently
                existing interfaces on the device.
                
                If a client tries to create configuration for a
                system-controlled interface that is not present in the
                corresponding state list, the server MAY reject
                the request if the implementation does not support
                pre-provisioning of interfaces or if the name refers to
                an interface that can never exist in the system.  A
                NETCONF server MUST reply with an rpc-error with the
                error-tag 'invalid-value' in this case.
                
                The IETF model in RFC 7223 provides YANG features for the
                following (i.e., pre-provisioning and arbitrary-names),
                however they are omitted here:
                
                 If the device supports pre-provisioning of interface
                 configuration, the 'pre-provisioning' feature is
                 advertised.
                
                 If the device allows arbitrarily named user-controlled
                 interfaces, the 'arbitrary-names' feature is advertised.
                
                When a configured user-controlled interface is created by
                the system, it is instantiated with the same name in the
                /interfaces/interface[name]/state list.
                ''',
                'name',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('oper-status', REFERENCE_ENUM_CLASS, 'OperStatusEnum' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.State.OperStatusEnum', 
                [], [], 
                '''                [adapted from IETF interfaces model (RFC 7223)]
                
                The current operational state of the interface.
                
                This leaf has the same semantics as ifOperStatus.
                ''',
                'oper_status',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('unnumbered', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates that the subinterface is unnumbered, and provides
                a reference to the subinterface that provides the IP
                address information (v4, v6 or both) for the current
                subinterface.
                ''',
                'unnumbered',
                'openconfig-interfaces', False),
            ],
            'openconfig-interfaces',
            'state',
            _yang_ns._namespaces['openconfig-interfaces'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Vlan.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Vlan.Config',
            False, 
            [
            _MetaInfoClassMember('global-vlan-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                VLAN id for the subinterface -- references a global
                VLAN by name or id.
                ''',
                'global_vlan_id',
                'openconfig-vlan', False, [
                    _MetaInfoClassMember('global-vlan-id', ATTRIBUTE, 'int' , None, None, 
                        [('1', '4094')], [], 
                        '''                        VLAN id for the subinterface -- references a global
                        VLAN by name or id.
                        ''',
                        'global_vlan_id',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('global-vlan-id', ATTRIBUTE, 'str' , None, None, 
                        [], [], 
                        '''                        VLAN id for the subinterface -- references a global
                        VLAN by name or id.
                        ''',
                        'global_vlan_id',
                        'openconfig-vlan', False),
                ]),
            _MetaInfoClassMember('vlan-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                VLAN id for the subinterface -- specified inline for the
                case of a local VLAN
                ''',
                'vlan_id',
                'openconfig-vlan', False, [
                    _MetaInfoClassMember('vlan-id', ATTRIBUTE, 'int' , None, None, 
                        [('1', '4094')], [], 
                        '''                        VLAN id for the subinterface -- specified inline for the
                        case of a local VLAN
                        ''',
                        'vlan_id',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('vlan-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'], 
                        '''                        VLAN id for the subinterface -- specified inline for the
                        case of a local VLAN
                        ''',
                        'vlan_id',
                        'openconfig-vlan', False),
                ]),
            ],
            'openconfig-vlan',
            'config',
            _yang_ns._namespaces['openconfig-vlan'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Vlan.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Vlan.State',
            False, 
            [
            _MetaInfoClassMember('global-vlan-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                VLAN id for the subinterface -- references a global
                VLAN by name or id.
                ''',
                'global_vlan_id',
                'openconfig-vlan', False, [
                    _MetaInfoClassMember('global-vlan-id', ATTRIBUTE, 'int' , None, None, 
                        [('1', '4094')], [], 
                        '''                        VLAN id for the subinterface -- references a global
                        VLAN by name or id.
                        ''',
                        'global_vlan_id',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('global-vlan-id', ATTRIBUTE, 'str' , None, None, 
                        [], [], 
                        '''                        VLAN id for the subinterface -- references a global
                        VLAN by name or id.
                        ''',
                        'global_vlan_id',
                        'openconfig-vlan', False),
                ]),
            _MetaInfoClassMember('vlan-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                VLAN id for the subinterface -- specified inline for the
                case of a local VLAN
                ''',
                'vlan_id',
                'openconfig-vlan', False, [
                    _MetaInfoClassMember('vlan-id', ATTRIBUTE, 'int' , None, None, 
                        [('1', '4094')], [], 
                        '''                        VLAN id for the subinterface -- specified inline for the
                        case of a local VLAN
                        ''',
                        'vlan_id',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('vlan-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'], 
                        '''                        VLAN id for the subinterface -- specified inline for the
                        case of a local VLAN
                        ''',
                        'vlan_id',
                        'openconfig-vlan', False),
                ]),
            ],
            'openconfig-vlan',
            'state',
            _yang_ns._namespaces['openconfig-vlan'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Vlan' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Vlan',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Vlan.Config', 
                [], [], 
                '''                Configuration parameters for VLANs
                ''',
                'config',
                'openconfig-vlan', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Vlan.State', 
                [], [], 
                '''                State variables for VLANs
                ''',
                'state',
                'openconfig-vlan', False),
            ],
            'openconfig-vlan',
            'vlan',
            _yang_ns._namespaces['openconfig-vlan'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Config',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                [adapted from IETF IP model RFC 7277]
                The IPv4 address on the interface.
                ''',
                'ip',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The length of the subnet prefix.
                ''',
                'prefix_length',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'config',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.State',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                [adapted from IETF IP model RFC 7277]
                The IPv4 address on the interface.
                ''',
                'ip',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('origin', REFERENCE_ENUM_CLASS, 'IpAddressOriginEnum' , 'ydk.models.openconfig.openconfig_if_ip', 'IpAddressOriginEnum', 
                [], [], 
                '''                The origin of this address, e.g., statically configured,
                assigned by DHCP, etc..
                ''',
                'origin',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The length of the subnet prefix.
                ''',
                'prefix_length',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'state',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.Config',
            False, 
            [
            _MetaInfoClassMember('accept-mode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Configure whether packets destined for
                virtual addresses are accepted even when the virtual
                address is not owned by the router interface
                ''',
                'accept_mode',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('advertisement-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Sets the interval between successive VRRP
                advertisements -- RFC 5798 defines this as a 12-bit
                value expressed as 0.1 seconds, with default 100, i.e.,
                1 second.  Several implementation express this in units of
                seconds
                ''',
                'advertisement_interval',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('preempt', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set to true, enables preemption by a higher
                priority backup router of a lower priority master router
                ''',
                'preempt',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('preempt-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Set the delay the higher priority router waits
                before preempting
                ''',
                'preempt_delay',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '254')], [], 
                '''                Specifies the sending VRRP interface's priority
                for the virtual router.  Higher values equal higher
                priority
                ''',
                'priority',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('virtual-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Configure one or more virtual addresses for the
                VRRP group
                ''',
                'virtual_address',
                'openconfig-if-ip', False, [
                    _MetaInfoClassMember('virtual-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Configure one or more virtual addresses for the
                        VRRP group
                        ''',
                        'virtual_address',
                        'openconfig-if-ip', False),
                    _MetaInfoClassMember('virtual-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Configure one or more virtual addresses for the
                        VRRP group
                        ''',
                        'virtual_address',
                        'openconfig-if-ip', False),
                ]),
            _MetaInfoClassMember('virtual-router-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Set the virtual router id for use by the VRRP group.  This
                usually also determines the virtual MAC address that is
                generated for the VRRP group
                ''',
                'virtual_router_id',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'config',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.State',
            False, 
            [
            _MetaInfoClassMember('accept-mode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Configure whether packets destined for
                virtual addresses are accepted even when the virtual
                address is not owned by the router interface
                ''',
                'accept_mode',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('advertisement-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Sets the interval between successive VRRP
                advertisements -- RFC 5798 defines this as a 12-bit
                value expressed as 0.1 seconds, with default 100, i.e.,
                1 second.  Several implementation express this in units of
                seconds
                ''',
                'advertisement_interval',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('current-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Operational value of the priority for the
                interface in the VRRP group
                ''',
                'current_priority',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('preempt', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set to true, enables preemption by a higher
                priority backup router of a lower priority master router
                ''',
                'preempt',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('preempt-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Set the delay the higher priority router waits
                before preempting
                ''',
                'preempt_delay',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '254')], [], 
                '''                Specifies the sending VRRP interface's priority
                for the virtual router.  Higher values equal higher
                priority
                ''',
                'priority',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('virtual-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Configure one or more virtual addresses for the
                VRRP group
                ''',
                'virtual_address',
                'openconfig-if-ip', False, [
                    _MetaInfoClassMember('virtual-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Configure one or more virtual addresses for the
                        VRRP group
                        ''',
                        'virtual_address',
                        'openconfig-if-ip', False),
                    _MetaInfoClassMember('virtual-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Configure one or more virtual addresses for the
                        VRRP group
                        ''',
                        'virtual_address',
                        'openconfig-if-ip', False),
                ]),
            _MetaInfoClassMember('virtual-router-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Set the virtual router id for use by the VRRP group.  This
                usually also determines the virtual MAC address that is
                generated for the VRRP group
                ''',
                'virtual_router_id',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'state',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.Config',
            False, 
            [
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int' , None, None, 
                [('0', '254')], [], 
                '''                Set the value to subtract from priority when
                the tracked interface goes down
                ''',
                'priority_decrement',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('track-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sets an interface that should be
                tracked for up/down events to dynamically change the
                priority state of the VRRP group, and potentially
                change the mastership if the tracked interface going
                down lowers the priority sufficiently
                ''',
                'track_interface',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'config',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.State',
            False, 
            [
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int' , None, None, 
                [('0', '254')], [], 
                '''                Set the value to subtract from priority when
                the tracked interface goes down
                ''',
                'priority_decrement',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('track-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sets an interface that should be
                tracked for up/down events to dynamically change the
                priority state of the VRRP group, and potentially
                change the mastership if the tracked interface going
                down lowers the priority sufficiently
                ''',
                'track_interface',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'state',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.Config', 
                [], [], 
                '''                Configuration data for VRRP interface tracking
                ''',
                'config',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.State', 
                [], [], 
                '''                Operational state data for VRRP interface tracking
                ''',
                'state',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'interface-tracking',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup',
            False, 
            [
            _MetaInfoClassMember('virtual-router-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                References the configured virtual router id for this
                VRRP group
                ''',
                'virtual_router_id',
                'openconfig-if-ip', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.Config', 
                [], [], 
                '''                Configuration data for the VRRP group
                ''',
                'config',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('interface-tracking', REFERENCE_CLASS, 'InterfaceTracking' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking', 
                [], [], 
                '''                Top-level container for VRRP interface tracking
                ''',
                'interface_tracking',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.State', 
                [], [], 
                '''                Operational state data for the VRRP group
                ''',
                'state',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'vrrp-group',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp',
            False, 
            [
            _MetaInfoClassMember('vrrp-group', REFERENCE_LIST, 'VrrpGroup' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup', 
                [], [], 
                '''                List of VRRP groups, keyed by virtual router id
                ''',
                'vrrp_group',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'vrrp',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                References the configured IP address
                ''',
                'ip',
                'openconfig-if-ip', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Config', 
                [], [], 
                '''                Configuration data for each configured IPv4
                address on the interface
                ''',
                'config',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.State', 
                [], [], 
                '''                Operational state data for each IPv4 address
                configured on the interface
                ''',
                'state',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('vrrp', REFERENCE_CLASS, 'Vrrp' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp', 
                [], [], 
                '''                Enclosing container for VRRP groups handled by this
                IP interface
                ''',
                'vrrp',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'address',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbor.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbor.Config',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IPv4 address of the neighbor node.
                ''',
                'ip',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('link-layer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                The link-layer address of the neighbor node.
                ''',
                'link_layer_address',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'config',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbor.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbor.State',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IPv4 address of the neighbor node.
                ''',
                'ip',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('link-layer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                The link-layer address of the neighbor node.
                ''',
                'link_layer_address',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('origin', REFERENCE_ENUM_CLASS, 'NeighborOriginEnum' , 'ydk.models.openconfig.openconfig_if_ip', 'NeighborOriginEnum', 
                [], [], 
                '''                The origin of this neighbor entry, static or dynamic.
                ''',
                'origin',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'state',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbor' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbor',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                References the configured IP address
                ''',
                'ip',
                'openconfig-if-ip', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbor.Config', 
                [], [], 
                '''                Configuration data for each configured IPv4
                address on the interface
                ''',
                'config',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbor.State', 
                [], [], 
                '''                Operational state data for each IPv4 address
                configured on the interface
                ''',
                'state',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'neighbor',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Config',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Controls whether IPv4 is enabled or disabled on this
                interface.  When IPv4 is enabled, this interface is
                connected to an IPv4 stack, and the interface can send
                and receive IPv4 packets.
                ''',
                'enabled',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('68', '65535')], [], 
                '''                The size, in octets, of the largest IPv4 packet that the
                interface will send and receive.
                The server may restrict the allowed values for this leaf,
                depending on the interface's type.
                If this leaf is not configured, the operationally used MTU
                depends on the interface's type.
                ''',
                'mtu',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'config',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.State',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Controls whether IPv4 is enabled or disabled on this
                interface.  When IPv4 is enabled, this interface is
                connected to an IPv4 stack, and the interface can send
                and receive IPv4 packets.
                ''',
                'enabled',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('68', '65535')], [], 
                '''                The size, in octets, of the largest IPv4 packet that the
                interface will send and receive.
                The server may restrict the allowed values for this leaf,
                depending on the interface's type.
                If this leaf is not configured, the operationally used MTU
                depends on the interface's type.
                ''',
                'mtu',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'state',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv4',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address', 
                [], [], 
                '''                The list of configured IPv4 addresses on the interface.
                ''',
                'address',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Config', 
                [], [], 
                '''                Top-level IPv4 configuration data for the interface
                ''',
                'config',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbor', 
                [], [], 
                '''                A list of mappings from IPv4 addresses to
                link-layer addresses.
                Entries in this list are used as static entries in the
                ARP Cache.
                ''',
                'neighbor',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.State', 
                [], [], 
                '''                Top level IPv4 operational state data
                ''',
                'state',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'ipv4',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Config',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                [adapted from IETF IP model RFC 7277]
                The IPv6 address on the interface.
                ''',
                'ip',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The length of the subnet prefix.
                ''',
                'prefix_length',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'config',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.State.StatusEnum' : _MetaInfoEnum('StatusEnum', 'ydk.models.openconfig.openconfig_interfaces',
        {
            'PREFERRED':'PREFERRED',
            'DEPRECATED':'DEPRECATED',
            'INVALID':'INVALID',
            'INACCESSIBLE':'INACCESSIBLE',
            'UNKNOWN':'UNKNOWN',
            'TENTATIVE':'TENTATIVE',
            'DUPLICATE':'DUPLICATE',
            'OPTIMISTIC':'OPTIMISTIC',
        }, 'openconfig-if-ip', _yang_ns._namespaces['openconfig-if-ip']),
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.State',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                [adapted from IETF IP model RFC 7277]
                The IPv6 address on the interface.
                ''',
                'ip',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('origin', REFERENCE_ENUM_CLASS, 'IpAddressOriginEnum' , 'ydk.models.openconfig.openconfig_if_ip', 'IpAddressOriginEnum', 
                [], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The origin of this address, e.g., static, dhcp, etc.
                ''',
                'origin',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The length of the subnet prefix.
                ''',
                'prefix_length',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'StatusEnum' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.State.StatusEnum', 
                [], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The status of an address.  Most of the states correspond
                to states from the IPv6 Stateless Address
                Autoconfiguration protocol.
                ''',
                'status',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'state',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.Config',
            False, 
            [
            _MetaInfoClassMember('accept-mode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Configure whether packets destined for
                virtual addresses are accepted even when the virtual
                address is not owned by the router interface
                ''',
                'accept_mode',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('advertisement-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Sets the interval between successive VRRP
                advertisements -- RFC 5798 defines this as a 12-bit
                value expressed as 0.1 seconds, with default 100, i.e.,
                1 second.  Several implementation express this in units of
                seconds
                ''',
                'advertisement_interval',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('preempt', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set to true, enables preemption by a higher
                priority backup router of a lower priority master router
                ''',
                'preempt',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('preempt-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Set the delay the higher priority router waits
                before preempting
                ''',
                'preempt_delay',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '254')], [], 
                '''                Specifies the sending VRRP interface's priority
                for the virtual router.  Higher values equal higher
                priority
                ''',
                'priority',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('virtual-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Configure one or more virtual addresses for the
                VRRP group
                ''',
                'virtual_address',
                'openconfig-if-ip', False, [
                    _MetaInfoClassMember('virtual-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Configure one or more virtual addresses for the
                        VRRP group
                        ''',
                        'virtual_address',
                        'openconfig-if-ip', False),
                    _MetaInfoClassMember('virtual-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Configure one or more virtual addresses for the
                        VRRP group
                        ''',
                        'virtual_address',
                        'openconfig-if-ip', False),
                ]),
            _MetaInfoClassMember('virtual-link-local', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                For VRRP on IPv6 interfaces, sets the virtual link local
                address
                ''',
                'virtual_link_local',
                'openconfig-if-ip', False, [
                    _MetaInfoClassMember('virtual-link-local', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        For VRRP on IPv6 interfaces, sets the virtual link local
                        address
                        ''',
                        'virtual_link_local',
                        'openconfig-if-ip', False),
                    _MetaInfoClassMember('virtual-link-local', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        For VRRP on IPv6 interfaces, sets the virtual link local
                        address
                        ''',
                        'virtual_link_local',
                        'openconfig-if-ip', False),
                ]),
            _MetaInfoClassMember('virtual-router-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Set the virtual router id for use by the VRRP group.  This
                usually also determines the virtual MAC address that is
                generated for the VRRP group
                ''',
                'virtual_router_id',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'config',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.State',
            False, 
            [
            _MetaInfoClassMember('accept-mode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Configure whether packets destined for
                virtual addresses are accepted even when the virtual
                address is not owned by the router interface
                ''',
                'accept_mode',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('advertisement-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Sets the interval between successive VRRP
                advertisements -- RFC 5798 defines this as a 12-bit
                value expressed as 0.1 seconds, with default 100, i.e.,
                1 second.  Several implementation express this in units of
                seconds
                ''',
                'advertisement_interval',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('current-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Operational value of the priority for the
                interface in the VRRP group
                ''',
                'current_priority',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('preempt', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set to true, enables preemption by a higher
                priority backup router of a lower priority master router
                ''',
                'preempt',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('preempt-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Set the delay the higher priority router waits
                before preempting
                ''',
                'preempt_delay',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '254')], [], 
                '''                Specifies the sending VRRP interface's priority
                for the virtual router.  Higher values equal higher
                priority
                ''',
                'priority',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('virtual-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Configure one or more virtual addresses for the
                VRRP group
                ''',
                'virtual_address',
                'openconfig-if-ip', False, [
                    _MetaInfoClassMember('virtual-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Configure one or more virtual addresses for the
                        VRRP group
                        ''',
                        'virtual_address',
                        'openconfig-if-ip', False),
                    _MetaInfoClassMember('virtual-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Configure one or more virtual addresses for the
                        VRRP group
                        ''',
                        'virtual_address',
                        'openconfig-if-ip', False),
                ]),
            _MetaInfoClassMember('virtual-link-local', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                For VRRP on IPv6 interfaces, sets the virtual link local
                address
                ''',
                'virtual_link_local',
                'openconfig-if-ip', False, [
                    _MetaInfoClassMember('virtual-link-local', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        For VRRP on IPv6 interfaces, sets the virtual link local
                        address
                        ''',
                        'virtual_link_local',
                        'openconfig-if-ip', False),
                    _MetaInfoClassMember('virtual-link-local', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        For VRRP on IPv6 interfaces, sets the virtual link local
                        address
                        ''',
                        'virtual_link_local',
                        'openconfig-if-ip', False),
                ]),
            _MetaInfoClassMember('virtual-router-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Set the virtual router id for use by the VRRP group.  This
                usually also determines the virtual MAC address that is
                generated for the VRRP group
                ''',
                'virtual_router_id',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'state',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.Config',
            False, 
            [
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int' , None, None, 
                [('0', '254')], [], 
                '''                Set the value to subtract from priority when
                the tracked interface goes down
                ''',
                'priority_decrement',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('track-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sets an interface that should be
                tracked for up/down events to dynamically change the
                priority state of the VRRP group, and potentially
                change the mastership if the tracked interface going
                down lowers the priority sufficiently
                ''',
                'track_interface',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'config',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.State',
            False, 
            [
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int' , None, None, 
                [('0', '254')], [], 
                '''                Set the value to subtract from priority when
                the tracked interface goes down
                ''',
                'priority_decrement',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('track-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sets an interface that should be
                tracked for up/down events to dynamically change the
                priority state of the VRRP group, and potentially
                change the mastership if the tracked interface going
                down lowers the priority sufficiently
                ''',
                'track_interface',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'state',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.Config', 
                [], [], 
                '''                Configuration data for VRRP interface tracking
                ''',
                'config',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.State', 
                [], [], 
                '''                Operational state data for VRRP interface tracking
                ''',
                'state',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'interface-tracking',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup',
            False, 
            [
            _MetaInfoClassMember('virtual-router-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                References the configured virtual router id for this
                VRRP group
                ''',
                'virtual_router_id',
                'openconfig-if-ip', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.Config', 
                [], [], 
                '''                Configuration data for the VRRP group
                ''',
                'config',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('interface-tracking', REFERENCE_CLASS, 'InterfaceTracking' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking', 
                [], [], 
                '''                Top-level container for VRRP interface tracking
                ''',
                'interface_tracking',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.State', 
                [], [], 
                '''                Operational state data for the VRRP group
                ''',
                'state',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'vrrp-group',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp',
            False, 
            [
            _MetaInfoClassMember('vrrp-group', REFERENCE_LIST, 'VrrpGroup' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup', 
                [], [], 
                '''                List of VRRP groups, keyed by virtual router id
                ''',
                'vrrp_group',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'vrrp',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                References the configured IP address
                ''',
                'ip',
                'openconfig-if-ip', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Config', 
                [], [], 
                '''                Configuration data for each IPv6 address on
                the interface
                ''',
                'config',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.State', 
                [], [], 
                '''                State data for each IPv6 address on the
                interface
                ''',
                'state',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('vrrp', REFERENCE_CLASS, 'Vrrp' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp', 
                [], [], 
                '''                Enclosing container for VRRP groups handled by this
                IP interface
                ''',
                'vrrp',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'address',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor.Config',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                [adapted from IETF IP model RFC 7277]
                The IPv6 address of the neighbor node.
                ''',
                'ip',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('link-layer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                [adapted from IETF IP model RFC 7277]
                The link-layer address of the neighbor node.
                ''',
                'link_layer_address',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'config',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor.State.NeighborStateEnum' : _MetaInfoEnum('NeighborStateEnum', 'ydk.models.openconfig.openconfig_interfaces',
        {
            'INCOMPLETE':'INCOMPLETE',
            'REACHABLE':'REACHABLE',
            'STALE':'STALE',
            'DELAY':'DELAY',
            'PROBE':'PROBE',
        }, 'openconfig-if-ip', _yang_ns._namespaces['openconfig-if-ip']),
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor.State',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                [adapted from IETF IP model RFC 7277]
                The IPv6 address of the neighbor node.
                ''',
                'ip',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('is-router', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                [adapted from IETF IP model RFC 7277]
                Indicates that the neighbor node acts as a router.
                ''',
                'is_router',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('link-layer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                [adapted from IETF IP model RFC 7277]
                The link-layer address of the neighbor node.
                ''',
                'link_layer_address',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('neighbor-state', REFERENCE_ENUM_CLASS, 'NeighborStateEnum' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor.State.NeighborStateEnum', 
                [], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The Neighbor Unreachability Detection state of this
                entry.
                ''',
                'neighbor_state',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('origin', REFERENCE_ENUM_CLASS, 'NeighborOriginEnum' , 'ydk.models.openconfig.openconfig_if_ip', 'NeighborOriginEnum', 
                [], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The origin of this neighbor entry.
                ''',
                'origin',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'state',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                References the configured IP neighbor address
                ''',
                'ip',
                'openconfig-if-ip', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor.Config', 
                [], [], 
                '''                Configuration data for each IPv6 address on
                the interface
                ''',
                'config',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor.State', 
                [], [], 
                '''                State data for each IPv6 address on the
                interface
                ''',
                'state',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'neighbor',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Config',
            False, 
            [
            _MetaInfoClassMember('dup-addr-detect-transmits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The number of consecutive Neighbor Solicitation messages
                sent while performing Duplicate Address Detection on a
                tentative address.  A value of zero indicates that
                Duplicate Address Detection is not performed on
                tentative addresses.  A value of one indicates a single
                transmission with no follow-up retransmissions.
                ''',
                'dup_addr_detect_transmits',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                [adapted from IETF IP model RFC 7277]
                Controls whether IPv6 is enabled or disabled on this
                interface.  When IPv6 is enabled, this interface is
                connected to an IPv6 stack, and the interface can send
                and receive IPv6 packets.
                ''',
                'enabled',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('1280', '4294967295')], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The size, in octets, of the largest IPv6 packet that the
                interface will send and receive.
                The server may restrict the allowed values for this leaf,
                depending on the interface's type.
                If this leaf is not configured, the operationally used MTU
                depends on the interface's type.
                ''',
                'mtu',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'config',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.State',
            False, 
            [
            _MetaInfoClassMember('dup-addr-detect-transmits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The number of consecutive Neighbor Solicitation messages
                sent while performing Duplicate Address Detection on a
                tentative address.  A value of zero indicates that
                Duplicate Address Detection is not performed on
                tentative addresses.  A value of one indicates a single
                transmission with no follow-up retransmissions.
                ''',
                'dup_addr_detect_transmits',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                [adapted from IETF IP model RFC 7277]
                Controls whether IPv6 is enabled or disabled on this
                interface.  When IPv6 is enabled, this interface is
                connected to an IPv6 stack, and the interface can send
                and receive IPv6 packets.
                ''',
                'enabled',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('1280', '4294967295')], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The size, in octets, of the largest IPv6 packet that the
                interface will send and receive.
                The server may restrict the allowed values for this leaf,
                depending on the interface's type.
                If this leaf is not configured, the operationally used MTU
                depends on the interface's type.
                ''',
                'mtu',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'state',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf.Config',
            False, 
            [
            _MetaInfoClassMember('create-global-addresses', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                [adapted from IETF IP model RFC 7277]
                If enabled, the host creates global addresses as
                described in RFC 4862.
                ''',
                'create_global_addresses',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('create-temporary-addresses', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                [adapted from IETF IP model RFC 7277]
                If enabled, the host creates temporary addresses as
                described in RFC 4941.
                ''',
                'create_temporary_addresses',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('temporary-preferred-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The time period during which the temporary address is
                preferred.
                ''',
                'temporary_preferred_lifetime',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('temporary-valid-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The time period during which the temporary address
                is valid.
                ''',
                'temporary_valid_lifetime',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'config',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf.State',
            False, 
            [
            _MetaInfoClassMember('create-global-addresses', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                [adapted from IETF IP model RFC 7277]
                If enabled, the host creates global addresses as
                described in RFC 4862.
                ''',
                'create_global_addresses',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('create-temporary-addresses', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                [adapted from IETF IP model RFC 7277]
                If enabled, the host creates temporary addresses as
                described in RFC 4941.
                ''',
                'create_temporary_addresses',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('temporary-preferred-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The time period during which the temporary address is
                preferred.
                ''',
                'temporary_preferred_lifetime',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('temporary-valid-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The time period during which the temporary address
                is valid.
                ''',
                'temporary_valid_lifetime',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'state',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf.Config', 
                [], [], 
                '''                [adapted from IETF IP model RFC 7277]
                Parameters to control the autoconfiguration of IPv6
                addresses, as described in RFC 4862.
                ''',
                'config',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf.State', 
                [], [], 
                '''                Operational state data 
                ''',
                'state',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'autoconf',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface.Ipv6',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address', 
                [], [], 
                '''                The list of configured IPv6 addresses on the interface.
                ''',
                'address',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('autoconf', REFERENCE_CLASS, 'Autoconf' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf', 
                [], [], 
                '''                Top-level container for IPv6 autoconf
                ''',
                'autoconf',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Config', 
                [], [], 
                '''                Top-level config data for the IPv6 interface
                ''',
                'config',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor', 
                [], [], 
                '''                A list of mappings from IPv6 addresses to
                link-layer addresses.
                Entries in this list are used as static entries in the
                Neighbor Cache.
                ''',
                'neighbor',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.State', 
                [], [], 
                '''                Top-level operational state data for the IPv6 interface
                ''',
                'state',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'ipv6',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces.Subinterface' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces.Subinterface',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The index number of the subinterface -- used to address
                the logical interface
                ''',
                'index',
                'openconfig-interfaces', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Config', 
                [], [], 
                '''                Configurable items at the subinterface level
                ''',
                'config',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4', 
                [], [], 
                '''                Parameters for the IPv4 address family.
                ''',
                'ipv4',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6', 
                [], [], 
                '''                Parameters for the IPv6 address family.
                ''',
                'ipv6',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.State', 
                [], [], 
                '''                Operational state data for logical interfaces
                ''',
                'state',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('vlan', REFERENCE_CLASS, 'Vlan' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface.Vlan', 
                [], [], 
                '''                Enclosing container for VLAN interface-specific
                data on subinterfaces
                ''',
                'vlan',
                'openconfig-vlan', False),
            ],
            'openconfig-interfaces',
            'subinterface',
            _yang_ns._namespaces['openconfig-interfaces'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Subinterfaces' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Subinterfaces',
            False, 
            [
            _MetaInfoClassMember('subinterface', REFERENCE_LIST, 'Subinterface' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces.Subinterface', 
                [], [], 
                '''                The list of subinterfaces (logical interfaces) associated
                with a physical interface
                ''',
                'subinterface',
                'openconfig-interfaces', False),
            ],
            'openconfig-interfaces',
            'subinterfaces',
            _yang_ns._namespaces['openconfig-interfaces'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Ethernet.Config.DuplexModeEnum' : _MetaInfoEnum('DuplexModeEnum', 'ydk.models.openconfig.openconfig_interfaces',
        {
            'FULL':'FULL',
            'HALF':'HALF',
        }, 'openconfig-if-ethernet', _yang_ns._namespaces['openconfig-if-ethernet']),
    'Interfaces.Interface.Ethernet.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Ethernet.Config',
            False, 
            [
            _MetaInfoClassMember('aggregate-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Specify the logical aggregate interface to which
                this interface belongs
                ''',
                'aggregate_id',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('auto-negotiate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE to request the interface to auto-negotiate
                transmission parameters with its peer interface.  When
                set to FALSE, the transmission parameters are specified
                manually.
                ''',
                'auto_negotiate',
                'openconfig-if-ethernet', False),
            _MetaInfoClassMember('duplex-mode', REFERENCE_ENUM_CLASS, 'DuplexModeEnum' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Ethernet.Config.DuplexModeEnum', 
                [], [], 
                '''                When auto-negotiate is TRUE, this optionally sets the
                duplex mode that will be advertised to the peer.  If
                unspecified, the interface should negotiate the duplex mode
                directly (typically full-duplex).  When auto-negotiate is
                FALSE, this sets the duplex mode on the interface directly.
                ''',
                'duplex_mode',
                'openconfig-if-ethernet', False),
            _MetaInfoClassMember('enable-flow-control', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable flow control for this interface.
                Ethernet flow control is a mechanism by which a receiver
                may send PAUSE frames to a sender to stop transmission for
                a specified time.
                
                This setting should override auto-negotiated flow control
                settings.  If left unspecified, and auto-negotiate is TRUE,
                flow control mode is negotiated with the peer interface.
                ''',
                'enable_flow_control',
                'openconfig-if-ethernet', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Assigns a MAC address to the Ethernet interface.  If not
                specified, the corresponding operational state leaf is
                expected to show the system-assigned MAC address.
                ''',
                'mac_address',
                'openconfig-if-ethernet', False),
            _MetaInfoClassMember('port-speed', REFERENCE_IDENTITY_CLASS, 'EthernetSpeedIdentity' , 'ydk.models.openconfig.openconfig_if_ethernet', 'EthernetSpeedIdentity', 
                [], [], 
                '''                When auto-negotiate is TRUE, this optionally sets the
                port-speed mode that will be advertised to the peer for
                negotiation.  If unspecified, it is expected that the
                interface will select the highest speed available based on
                negotiation.  When auto-negotiate is set to FALSE, sets the
                link speed to a fixed value -- supported values are defined
                by ethernet-speed identities
                ''',
                'port_speed',
                'openconfig-if-ethernet', False),
            ],
            'openconfig-if-ethernet',
            'config',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Ethernet.State.Counters' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Ethernet.State.Counters',
            False, 
            [
            _MetaInfoClassMember('in-8021q-frames', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of 802.1q tagged frames received on the interface
                ''',
                'in_8021q_frames',
                'openconfig-if-ethernet', False),
            _MetaInfoClassMember('in-crc-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of receive error events due to FCS/CRC check
                failure
                ''',
                'in_crc_errors',
                'openconfig-if-ethernet', False),
            _MetaInfoClassMember('in-fragment-frames', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of fragment frames received on the interface.
                ''',
                'in_fragment_frames',
                'openconfig-if-ethernet', False),
            _MetaInfoClassMember('in-jabber-frames', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of jabber frames received on the
                interface.  Jabber frames are typically defined as oversize
                frames which also have a bad CRC.  Implementations may use
                slightly different definitions of what constitutes a jabber
                frame.  Often indicative of a NIC hardware problem.
                ''',
                'in_jabber_frames',
                'openconfig-if-ethernet', False),
            _MetaInfoClassMember('in-mac-control-frames', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                MAC layer control frames received on the interface
                ''',
                'in_mac_control_frames',
                'openconfig-if-ethernet', False),
            _MetaInfoClassMember('in-mac-pause-frames', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                MAC layer PAUSE frames received on the interface
                ''',
                'in_mac_pause_frames',
                'openconfig-if-ethernet', False),
            _MetaInfoClassMember('in-oversize-frames', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of oversize frames received on the interface
                ''',
                'in_oversize_frames',
                'openconfig-if-ethernet', False),
            _MetaInfoClassMember('out-8021q-frames', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of 802.1q tagged frames sent on the interface
                ''',
                'out_8021q_frames',
                'openconfig-if-ethernet', False),
            _MetaInfoClassMember('out-mac-control-frames', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                MAC layer control frames sent on the interface
                ''',
                'out_mac_control_frames',
                'openconfig-if-ethernet', False),
            _MetaInfoClassMember('out-mac-pause-frames', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                MAC layer PAUSE frames sent on the interface
                ''',
                'out_mac_pause_frames',
                'openconfig-if-ethernet', False),
            ],
            'openconfig-if-ethernet',
            'counters',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Ethernet.State.DuplexModeEnum' : _MetaInfoEnum('DuplexModeEnum', 'ydk.models.openconfig.openconfig_interfaces',
        {
            'FULL':'FULL',
            'HALF':'HALF',
        }, 'openconfig-if-ethernet', _yang_ns._namespaces['openconfig-if-ethernet']),
    'Interfaces.Interface.Ethernet.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Ethernet.State',
            False, 
            [
            _MetaInfoClassMember('aggregate-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Specify the logical aggregate interface to which
                this interface belongs
                ''',
                'aggregate_id',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('auto-negotiate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE to request the interface to auto-negotiate
                transmission parameters with its peer interface.  When
                set to FALSE, the transmission parameters are specified
                manually.
                ''',
                'auto_negotiate',
                'openconfig-if-ethernet', False),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Ethernet.State.Counters', 
                [], [], 
                '''                Ethernet interface counters
                ''',
                'counters',
                'openconfig-if-ethernet', False),
            _MetaInfoClassMember('duplex-mode', REFERENCE_ENUM_CLASS, 'DuplexModeEnum' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Ethernet.State.DuplexModeEnum', 
                [], [], 
                '''                When auto-negotiate is TRUE, this optionally sets the
                duplex mode that will be advertised to the peer.  If
                unspecified, the interface should negotiate the duplex mode
                directly (typically full-duplex).  When auto-negotiate is
                FALSE, this sets the duplex mode on the interface directly.
                ''',
                'duplex_mode',
                'openconfig-if-ethernet', False),
            _MetaInfoClassMember('enable-flow-control', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable flow control for this interface.
                Ethernet flow control is a mechanism by which a receiver
                may send PAUSE frames to a sender to stop transmission for
                a specified time.
                
                This setting should override auto-negotiated flow control
                settings.  If left unspecified, and auto-negotiate is TRUE,
                flow control mode is negotiated with the peer interface.
                ''',
                'enable_flow_control',
                'openconfig-if-ethernet', False),
            _MetaInfoClassMember('hw-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Represenets the 'burned-in',  or system-assigned, MAC
                address for the Ethernet interface.
                ''',
                'hw_mac_address',
                'openconfig-if-ethernet', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Assigns a MAC address to the Ethernet interface.  If not
                specified, the corresponding operational state leaf is
                expected to show the system-assigned MAC address.
                ''',
                'mac_address',
                'openconfig-if-ethernet', False),
            _MetaInfoClassMember('port-speed', REFERENCE_IDENTITY_CLASS, 'EthernetSpeedIdentity' , 'ydk.models.openconfig.openconfig_if_ethernet', 'EthernetSpeedIdentity', 
                [], [], 
                '''                When auto-negotiate is TRUE, this optionally sets the
                port-speed mode that will be advertised to the peer for
                negotiation.  If unspecified, it is expected that the
                interface will select the highest speed available based on
                negotiation.  When auto-negotiate is set to FALSE, sets the
                link speed to a fixed value -- supported values are defined
                by ethernet-speed identities
                ''',
                'port_speed',
                'openconfig-if-ethernet', False),
            ],
            'openconfig-if-ethernet',
            'state',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Ethernet.Vlan.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Ethernet.Vlan.Config',
            False, 
            [
            _MetaInfoClassMember('access-vlan', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Assign the access vlan to the access port.
                ''',
                'access_vlan',
                'openconfig-vlan', False, [
                    _MetaInfoClassMember('access-vlan', ATTRIBUTE, 'int' , None, None, 
                        [('1', '4094')], [], 
                        '''                        Assign the access vlan to the access port.
                        ''',
                        'access_vlan',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('access-vlan', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'], 
                        '''                        Assign the access vlan to the access port.
                        ''',
                        'access_vlan',
                        'openconfig-vlan', False),
                ]),
            _MetaInfoClassMember('interface-mode', REFERENCE_ENUM_CLASS, 'VlanModeTypeEnum' , 'ydk.models.openconfig.openconfig_vlan', 'VlanModeTypeEnum', 
                [], [], 
                '''                Set the interface to access or trunk mode for
                VLANs
                ''',
                'interface_mode',
                'openconfig-vlan', False),
            _MetaInfoClassMember('native-vlan', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Set the native VLAN id for untagged frames arriving on
                a trunk interface.  This configuration is only valid on
                a trunk interface.
                ''',
                'native_vlan',
                'openconfig-vlan', False, [
                    _MetaInfoClassMember('native-vlan', ATTRIBUTE, 'int' , None, None, 
                        [('1', '4094')], [], 
                        '''                        Set the native VLAN id for untagged frames arriving on
                        a trunk interface.  This configuration is only valid on
                        a trunk interface.
                        ''',
                        'native_vlan',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('native-vlan', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'], 
                        '''                        Set the native VLAN id for untagged frames arriving on
                        a trunk interface.  This configuration is only valid on
                        a trunk interface.
                        ''',
                        'native_vlan',
                        'openconfig-vlan', False),
                ]),
            _MetaInfoClassMember('trunk-vlans', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Specify VLANs, or ranges thereof, that the interface may
                carry when in trunk mode.  If not specified, all VLANs are
                allowed on the interface. Ranges are specified in the form
                x..y, where x<y - ranges are assumed to be inclusive (such
                that the VLAN range is x <= range <= y.
                ''',
                'trunk_vlans',
                'openconfig-vlan', False, [
                    _MetaInfoClassMember('trunk-vlans', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('1', '4094')], [], 
                        '''                        Specify VLANs, or ranges thereof, that the interface may
                        carry when in trunk mode.  If not specified, all VLANs are
                        allowed on the interface. Ranges are specified in the form
                        x..y, where x<y - ranges are assumed to be inclusive (such
                        that the VLAN range is x <= range <= y.
                        ''',
                        'trunk_vlans',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('trunk-vlans', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])'], 
                        '''                        Specify VLANs, or ranges thereof, that the interface may
                        carry when in trunk mode.  If not specified, all VLANs are
                        allowed on the interface. Ranges are specified in the form
                        x..y, where x<y - ranges are assumed to be inclusive (such
                        that the VLAN range is x <= range <= y.
                        ''',
                        'trunk_vlans',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('trunk-vlans', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'], 
                        '''                        Specify VLANs, or ranges thereof, that the interface may
                        carry when in trunk mode.  If not specified, all VLANs are
                        allowed on the interface. Ranges are specified in the form
                        x..y, where x<y - ranges are assumed to be inclusive (such
                        that the VLAN range is x <= range <= y.
                        ''',
                        'trunk_vlans',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('trunk-vlans', REFERENCE_UNION, 'str' , None, None, 
                        [], [], 
                        '''                        Specify VLANs, or ranges thereof, that the interface may
                        carry when in trunk mode.  If not specified, all VLANs are
                        allowed on the interface. Ranges are specified in the form
                        x..y, where x<y - ranges are assumed to be inclusive (such
                        that the VLAN range is x <= range <= y.
                        ''',
                        'trunk_vlans',
                        'openconfig-vlan', False, [
                            _MetaInfoClassMember('trunk-vlans', REFERENCE_LEAFLIST, 'str' , None, None, 
                                [], [b'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'], 
                                '''                                Specify VLANs, or ranges thereof, that the interface may
                                carry when in trunk mode.  If not specified, all VLANs are
                                allowed on the interface. Ranges are specified in the form
                                x..y, where x<y - ranges are assumed to be inclusive (such
                                that the VLAN range is x <= range <= y.
                                ''',
                                'trunk_vlans',
                                'openconfig-vlan', False),
                            _MetaInfoClassMember('trunk-vlans', REFERENCE_LEAFLIST, 'str' , None, None, 
                                [], [b'(\\*|(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9]))\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])'], 
                                '''                                Specify VLANs, or ranges thereof, that the interface may
                                carry when in trunk mode.  If not specified, all VLANs are
                                allowed on the interface. Ranges are specified in the form
                                x..y, where x<y - ranges are assumed to be inclusive (such
                                that the VLAN range is x <= range <= y.
                                ''',
                                'trunk_vlans',
                                'openconfig-vlan', False),
                        ]),
                ]),
            ],
            'openconfig-vlan',
            'config',
            _yang_ns._namespaces['openconfig-vlan'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Ethernet.Vlan.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Ethernet.Vlan.State',
            False, 
            [
            _MetaInfoClassMember('access-vlan', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Assign the access vlan to the access port.
                ''',
                'access_vlan',
                'openconfig-vlan', False, [
                    _MetaInfoClassMember('access-vlan', ATTRIBUTE, 'int' , None, None, 
                        [('1', '4094')], [], 
                        '''                        Assign the access vlan to the access port.
                        ''',
                        'access_vlan',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('access-vlan', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'], 
                        '''                        Assign the access vlan to the access port.
                        ''',
                        'access_vlan',
                        'openconfig-vlan', False),
                ]),
            _MetaInfoClassMember('interface-mode', REFERENCE_ENUM_CLASS, 'VlanModeTypeEnum' , 'ydk.models.openconfig.openconfig_vlan', 'VlanModeTypeEnum', 
                [], [], 
                '''                Set the interface to access or trunk mode for
                VLANs
                ''',
                'interface_mode',
                'openconfig-vlan', False),
            _MetaInfoClassMember('native-vlan', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Set the native VLAN id for untagged frames arriving on
                a trunk interface.  This configuration is only valid on
                a trunk interface.
                ''',
                'native_vlan',
                'openconfig-vlan', False, [
                    _MetaInfoClassMember('native-vlan', ATTRIBUTE, 'int' , None, None, 
                        [('1', '4094')], [], 
                        '''                        Set the native VLAN id for untagged frames arriving on
                        a trunk interface.  This configuration is only valid on
                        a trunk interface.
                        ''',
                        'native_vlan',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('native-vlan', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'], 
                        '''                        Set the native VLAN id for untagged frames arriving on
                        a trunk interface.  This configuration is only valid on
                        a trunk interface.
                        ''',
                        'native_vlan',
                        'openconfig-vlan', False),
                ]),
            _MetaInfoClassMember('trunk-vlans', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Specify VLANs, or ranges thereof, that the interface may
                carry when in trunk mode.  If not specified, all VLANs are
                allowed on the interface. Ranges are specified in the form
                x..y, where x<y - ranges are assumed to be inclusive (such
                that the VLAN range is x <= range <= y.
                ''',
                'trunk_vlans',
                'openconfig-vlan', False, [
                    _MetaInfoClassMember('trunk-vlans', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('1', '4094')], [], 
                        '''                        Specify VLANs, or ranges thereof, that the interface may
                        carry when in trunk mode.  If not specified, all VLANs are
                        allowed on the interface. Ranges are specified in the form
                        x..y, where x<y - ranges are assumed to be inclusive (such
                        that the VLAN range is x <= range <= y.
                        ''',
                        'trunk_vlans',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('trunk-vlans', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])'], 
                        '''                        Specify VLANs, or ranges thereof, that the interface may
                        carry when in trunk mode.  If not specified, all VLANs are
                        allowed on the interface. Ranges are specified in the form
                        x..y, where x<y - ranges are assumed to be inclusive (such
                        that the VLAN range is x <= range <= y.
                        ''',
                        'trunk_vlans',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('trunk-vlans', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'], 
                        '''                        Specify VLANs, or ranges thereof, that the interface may
                        carry when in trunk mode.  If not specified, all VLANs are
                        allowed on the interface. Ranges are specified in the form
                        x..y, where x<y - ranges are assumed to be inclusive (such
                        that the VLAN range is x <= range <= y.
                        ''',
                        'trunk_vlans',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('trunk-vlans', REFERENCE_UNION, 'str' , None, None, 
                        [], [], 
                        '''                        Specify VLANs, or ranges thereof, that the interface may
                        carry when in trunk mode.  If not specified, all VLANs are
                        allowed on the interface. Ranges are specified in the form
                        x..y, where x<y - ranges are assumed to be inclusive (such
                        that the VLAN range is x <= range <= y.
                        ''',
                        'trunk_vlans',
                        'openconfig-vlan', False, [
                            _MetaInfoClassMember('trunk-vlans', REFERENCE_LEAFLIST, 'str' , None, None, 
                                [], [b'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'], 
                                '''                                Specify VLANs, or ranges thereof, that the interface may
                                carry when in trunk mode.  If not specified, all VLANs are
                                allowed on the interface. Ranges are specified in the form
                                x..y, where x<y - ranges are assumed to be inclusive (such
                                that the VLAN range is x <= range <= y.
                                ''',
                                'trunk_vlans',
                                'openconfig-vlan', False),
                            _MetaInfoClassMember('trunk-vlans', REFERENCE_LEAFLIST, 'str' , None, None, 
                                [], [b'(\\*|(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9]))\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])'], 
                                '''                                Specify VLANs, or ranges thereof, that the interface may
                                carry when in trunk mode.  If not specified, all VLANs are
                                allowed on the interface. Ranges are specified in the form
                                x..y, where x<y - ranges are assumed to be inclusive (such
                                that the VLAN range is x <= range <= y.
                                ''',
                                'trunk_vlans',
                                'openconfig-vlan', False),
                        ]),
                ]),
            ],
            'openconfig-vlan',
            'state',
            _yang_ns._namespaces['openconfig-vlan'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Ethernet.Vlan' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Ethernet.Vlan',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Ethernet.Vlan.Config', 
                [], [], 
                '''                Configuration parameters for VLANs
                ''',
                'config',
                'openconfig-vlan', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Ethernet.Vlan.State', 
                [], [], 
                '''                State variables for VLANs
                ''',
                'state',
                'openconfig-vlan', False),
            ],
            'openconfig-vlan',
            'vlan',
            _yang_ns._namespaces['openconfig-vlan'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Ethernet' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Ethernet',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Ethernet.Config', 
                [], [], 
                '''                Configuration data for ethernet interfaces
                ''',
                'config',
                'openconfig-if-ethernet', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Ethernet.State', 
                [], [], 
                '''                State variables for Ethernet interfaces
                ''',
                'state',
                'openconfig-if-ethernet', False),
            _MetaInfoClassMember('vlan', REFERENCE_CLASS, 'Vlan' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Ethernet.Vlan', 
                [], [], 
                '''                Enclosing container for VLAN interface-specific
                data on Ethernet interfaces
                ''',
                'vlan',
                'openconfig-vlan', False),
            ],
            'openconfig-if-ethernet',
            'ethernet',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Aggregation.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Aggregation.Config',
            False, 
            [
            _MetaInfoClassMember('lag-type', REFERENCE_ENUM_CLASS, 'AggregationTypeEnum' , 'ydk.models.openconfig.openconfig_if_aggregate', 'AggregationTypeEnum', 
                [], [], 
                '''                Sets the type of LAG, i.e., how it is
                configured / maintained
                ''',
                'lag_type',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('min-links', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Specifies the mininum number of member
                interfaces that must be active for the aggregate interface
                to be available
                ''',
                'min_links',
                'openconfig-if-aggregate', False),
            ],
            'openconfig-if-aggregate',
            'config',
            _yang_ns._namespaces['openconfig-if-aggregate'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Aggregation.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Aggregation.State',
            False, 
            [
            _MetaInfoClassMember('lag-type', REFERENCE_ENUM_CLASS, 'AggregationTypeEnum' , 'ydk.models.openconfig.openconfig_if_aggregate', 'AggregationTypeEnum', 
                [], [], 
                '''                Sets the type of LAG, i.e., how it is
                configured / maintained
                ''',
                'lag_type',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('members', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                List of current member interfaces for the aggregate,
                expressed as references to existing interfaces
                ''',
                'members',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('min-links', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Specifies the mininum number of member
                interfaces that must be active for the aggregate interface
                to be available
                ''',
                'min_links',
                'openconfig-if-aggregate', False),
            ],
            'openconfig-if-aggregate',
            'state',
            _yang_ns._namespaces['openconfig-if-aggregate'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Aggregation.Lacp.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Aggregation.Lacp.Config',
            False, 
            [
            _MetaInfoClassMember('interval', REFERENCE_ENUM_CLASS, 'LacpPeriodTypeEnum' , 'ydk.models.openconfig.openconfig_if_aggregate', 'LacpPeriodTypeEnum', 
                [], [], 
                '''                Set the period between LACP messages -- uses
                the lacp-period-type enumeration.
                ''',
                'interval',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('lacp-mode', REFERENCE_ENUM_CLASS, 'LacpActivityTypeEnum' , 'ydk.models.openconfig.openconfig_if_aggregate', 'LacpActivityTypeEnum', 
                [], [], 
                '''                ACTIVE is to initiate the transmission of LACP packets.
                PASSIVE is to wait for peer to initiate the transmission of
                LACP packets.
                ''',
                'lacp_mode',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('system-id-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The MAC address portion of the node's System ID. This is
                combined with the system priority to construct the 8-octet
                system-id
                ''',
                'system_id_mac',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('system-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sytem priority used by the node on this LAG interface.
                Lower value is higher priority for determining which node
                is the controlling system.
                ''',
                'system_priority',
                'openconfig-if-aggregate', False),
            ],
            'openconfig-if-aggregate',
            'config',
            _yang_ns._namespaces['openconfig-if-aggregate'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Aggregation.Lacp.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Aggregation.Lacp.State',
            False, 
            [
            _MetaInfoClassMember('interval', REFERENCE_ENUM_CLASS, 'LacpPeriodTypeEnum' , 'ydk.models.openconfig.openconfig_if_aggregate', 'LacpPeriodTypeEnum', 
                [], [], 
                '''                Set the period between LACP messages -- uses
                the lacp-period-type enumeration.
                ''',
                'interval',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('lacp-mode', REFERENCE_ENUM_CLASS, 'LacpActivityTypeEnum' , 'ydk.models.openconfig.openconfig_if_aggregate', 'LacpActivityTypeEnum', 
                [], [], 
                '''                ACTIVE is to initiate the transmission of LACP packets.
                PASSIVE is to wait for peer to initiate the transmission of
                LACP packets.
                ''',
                'lacp_mode',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('system-id-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The MAC address portion of the node's System ID. This is
                combined with the system priority to construct the 8-octet
                system-id
                ''',
                'system_id_mac',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('system-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sytem priority used by the node on this LAG interface.
                Lower value is higher priority for determining which node
                is the controlling system.
                ''',
                'system_priority',
                'openconfig-if-aggregate', False),
            ],
            'openconfig-if-aggregate',
            'state',
            _yang_ns._namespaces['openconfig-if-aggregate'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Aggregation.Lacp.Members.Member.State.Counters' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Aggregation.Lacp.Members.Member.State.Counters',
            False, 
            [
            _MetaInfoClassMember('lacp-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of LACPDU illegal packet errors
                ''',
                'lacp_errors',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('lacp-in-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of LACPDUs received
                ''',
                'lacp_in_pkts',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('lacp-out-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of LACPDUs transmitted
                ''',
                'lacp_out_pkts',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('lacp-rx-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of LACPDU receive packet errors
                ''',
                'lacp_rx_errors',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('lacp-tx-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of LACPDU transmit packet errors
                ''',
                'lacp_tx_errors',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('lacp-unknown-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of LACPDU unknown packet errors
                ''',
                'lacp_unknown_errors',
                'openconfig-if-aggregate', False),
            ],
            'openconfig-if-aggregate',
            'counters',
            _yang_ns._namespaces['openconfig-if-aggregate'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Aggregation.Lacp.Members.Member.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Aggregation.Lacp.Members.Member.State',
            False, 
            [
            _MetaInfoClassMember('activity', REFERENCE_ENUM_CLASS, 'LacpActivityTypeEnum' , 'ydk.models.openconfig.openconfig_if_aggregate', 'LacpActivityTypeEnum', 
                [], [], 
                '''                Indicates participant is active or passive
                ''',
                'activity',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('aggregatable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A true value indicates that the participant will allow
                the link to be used as part of the aggregate. A false
                value indicates the link should be used as an individual
                link
                ''',
                'aggregatable',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('collecting', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If true, the participant is collecting incoming frames
                on the link, otherwise false
                ''',
                'collecting',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Aggregation.Lacp.Members.Member.State.Counters', 
                [], [], 
                '''                LACP protocol counters
                ''',
                'counters',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('distributing', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When true, the participant is distributing outgoing
                frames; when false, distribution is disabled
                ''',
                'distributing',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface member of the LACP aggregate
                ''',
                'interface',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('oper-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Current operational value of the key for the aggregate
                interface
                ''',
                'oper_key',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('partner-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address representing the protocol partner's interface
                system ID
                ''',
                'partner_id',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('partner-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Operational value of the protocol partner's key
                ''',
                'partner_key',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('synchronization', REFERENCE_ENUM_CLASS, 'LacpSynchronizationTypeEnum' , 'ydk.models.openconfig.openconfig_if_aggregate', 'LacpSynchronizationTypeEnum', 
                [], [], 
                '''                Indicates whether the participant is in-sync or
                out-of-sync
                ''',
                'synchronization',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('system-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address that defines the local system ID for the
                aggregate interface
                ''',
                'system_id',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('timeout', REFERENCE_ENUM_CLASS, 'LacpTimeoutTypeEnum' , 'ydk.models.openconfig.openconfig_if_aggregate', 'LacpTimeoutTypeEnum', 
                [], [], 
                '''                The timeout type (short or long) used by the
                participant
                ''',
                'timeout',
                'openconfig-if-aggregate', False),
            ],
            'openconfig-if-aggregate',
            'state',
            _yang_ns._namespaces['openconfig-if-aggregate'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Aggregation.Lacp.Members.Member' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Aggregation.Lacp.Members.Member',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to aggregate member interface
                ''',
                'interface',
                'openconfig-if-aggregate', True),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Aggregation.Lacp.Members.Member.State', 
                [], [], 
                '''                Operational state data for aggregate members
                ''',
                'state',
                'openconfig-if-aggregate', False),
            ],
            'openconfig-if-aggregate',
            'member',
            _yang_ns._namespaces['openconfig-if-aggregate'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Aggregation.Lacp.Members' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Aggregation.Lacp.Members',
            False, 
            [
            _MetaInfoClassMember('member', REFERENCE_LIST, 'Member' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Aggregation.Lacp.Members.Member', 
                [], [], 
                '''                List of member interfaces and their associated status for
                a LACP-controlled aggregate interface.  Member list is not
                configurable here -- each interface indicates items
                its participation in the LAG.
                ''',
                'member',
                'openconfig-if-aggregate', False),
            ],
            'openconfig-if-aggregate',
            'members',
            _yang_ns._namespaces['openconfig-if-aggregate'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Aggregation.Lacp' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Aggregation.Lacp',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Aggregation.Lacp.Config', 
                [], [], 
                '''                Configuration data for LACP
                ''',
                'config',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('members', REFERENCE_CLASS, 'Members' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Aggregation.Lacp.Members', 
                [], [], 
                '''                Enclosing container for the list of members interfaces of
                the aggregate. This list is considered operational state
                only so is labeled config false and has no config container
                ''',
                'members',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Aggregation.Lacp.State', 
                [], [], 
                '''                Operational state data for LACP
                ''',
                'state',
                'openconfig-if-aggregate', False),
            ],
            'openconfig-if-aggregate',
            'lacp',
            _yang_ns._namespaces['openconfig-if-aggregate'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Aggregation.Vlan.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Aggregation.Vlan.Config',
            False, 
            [
            _MetaInfoClassMember('access-vlan', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Assign the access vlan to the access port.
                ''',
                'access_vlan',
                'openconfig-vlan', False, [
                    _MetaInfoClassMember('access-vlan', ATTRIBUTE, 'int' , None, None, 
                        [('1', '4094')], [], 
                        '''                        Assign the access vlan to the access port.
                        ''',
                        'access_vlan',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('access-vlan', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'], 
                        '''                        Assign the access vlan to the access port.
                        ''',
                        'access_vlan',
                        'openconfig-vlan', False),
                ]),
            _MetaInfoClassMember('interface-mode', REFERENCE_ENUM_CLASS, 'VlanModeTypeEnum' , 'ydk.models.openconfig.openconfig_vlan', 'VlanModeTypeEnum', 
                [], [], 
                '''                Set the interface to access or trunk mode for
                VLANs
                ''',
                'interface_mode',
                'openconfig-vlan', False),
            _MetaInfoClassMember('native-vlan', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Set the native VLAN id for untagged frames arriving on
                a trunk interface.  This configuration is only valid on
                a trunk interface.
                ''',
                'native_vlan',
                'openconfig-vlan', False, [
                    _MetaInfoClassMember('native-vlan', ATTRIBUTE, 'int' , None, None, 
                        [('1', '4094')], [], 
                        '''                        Set the native VLAN id for untagged frames arriving on
                        a trunk interface.  This configuration is only valid on
                        a trunk interface.
                        ''',
                        'native_vlan',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('native-vlan', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'], 
                        '''                        Set the native VLAN id for untagged frames arriving on
                        a trunk interface.  This configuration is only valid on
                        a trunk interface.
                        ''',
                        'native_vlan',
                        'openconfig-vlan', False),
                ]),
            _MetaInfoClassMember('trunk-vlans', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Specify VLANs, or ranges thereof, that the interface may
                carry when in trunk mode.  If not specified, all VLANs are
                allowed on the interface. Ranges are specified in the form
                x..y, where x<y - ranges are assumed to be inclusive (such
                that the VLAN range is x <= range <= y.
                ''',
                'trunk_vlans',
                'openconfig-vlan', False, [
                    _MetaInfoClassMember('trunk-vlans', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('1', '4094')], [], 
                        '''                        Specify VLANs, or ranges thereof, that the interface may
                        carry when in trunk mode.  If not specified, all VLANs are
                        allowed on the interface. Ranges are specified in the form
                        x..y, where x<y - ranges are assumed to be inclusive (such
                        that the VLAN range is x <= range <= y.
                        ''',
                        'trunk_vlans',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('trunk-vlans', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])'], 
                        '''                        Specify VLANs, or ranges thereof, that the interface may
                        carry when in trunk mode.  If not specified, all VLANs are
                        allowed on the interface. Ranges are specified in the form
                        x..y, where x<y - ranges are assumed to be inclusive (such
                        that the VLAN range is x <= range <= y.
                        ''',
                        'trunk_vlans',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('trunk-vlans', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'], 
                        '''                        Specify VLANs, or ranges thereof, that the interface may
                        carry when in trunk mode.  If not specified, all VLANs are
                        allowed on the interface. Ranges are specified in the form
                        x..y, where x<y - ranges are assumed to be inclusive (such
                        that the VLAN range is x <= range <= y.
                        ''',
                        'trunk_vlans',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('trunk-vlans', REFERENCE_UNION, 'str' , None, None, 
                        [], [], 
                        '''                        Specify VLANs, or ranges thereof, that the interface may
                        carry when in trunk mode.  If not specified, all VLANs are
                        allowed on the interface. Ranges are specified in the form
                        x..y, where x<y - ranges are assumed to be inclusive (such
                        that the VLAN range is x <= range <= y.
                        ''',
                        'trunk_vlans',
                        'openconfig-vlan', False, [
                            _MetaInfoClassMember('trunk-vlans', REFERENCE_LEAFLIST, 'str' , None, None, 
                                [], [b'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'], 
                                '''                                Specify VLANs, or ranges thereof, that the interface may
                                carry when in trunk mode.  If not specified, all VLANs are
                                allowed on the interface. Ranges are specified in the form
                                x..y, where x<y - ranges are assumed to be inclusive (such
                                that the VLAN range is x <= range <= y.
                                ''',
                                'trunk_vlans',
                                'openconfig-vlan', False),
                            _MetaInfoClassMember('trunk-vlans', REFERENCE_LEAFLIST, 'str' , None, None, 
                                [], [b'(\\*|(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9]))\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])'], 
                                '''                                Specify VLANs, or ranges thereof, that the interface may
                                carry when in trunk mode.  If not specified, all VLANs are
                                allowed on the interface. Ranges are specified in the form
                                x..y, where x<y - ranges are assumed to be inclusive (such
                                that the VLAN range is x <= range <= y.
                                ''',
                                'trunk_vlans',
                                'openconfig-vlan', False),
                        ]),
                ]),
            ],
            'openconfig-vlan',
            'config',
            _yang_ns._namespaces['openconfig-vlan'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Aggregation.Vlan.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Aggregation.Vlan.State',
            False, 
            [
            _MetaInfoClassMember('access-vlan', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Assign the access vlan to the access port.
                ''',
                'access_vlan',
                'openconfig-vlan', False, [
                    _MetaInfoClassMember('access-vlan', ATTRIBUTE, 'int' , None, None, 
                        [('1', '4094')], [], 
                        '''                        Assign the access vlan to the access port.
                        ''',
                        'access_vlan',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('access-vlan', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'], 
                        '''                        Assign the access vlan to the access port.
                        ''',
                        'access_vlan',
                        'openconfig-vlan', False),
                ]),
            _MetaInfoClassMember('interface-mode', REFERENCE_ENUM_CLASS, 'VlanModeTypeEnum' , 'ydk.models.openconfig.openconfig_vlan', 'VlanModeTypeEnum', 
                [], [], 
                '''                Set the interface to access or trunk mode for
                VLANs
                ''',
                'interface_mode',
                'openconfig-vlan', False),
            _MetaInfoClassMember('native-vlan', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Set the native VLAN id for untagged frames arriving on
                a trunk interface.  This configuration is only valid on
                a trunk interface.
                ''',
                'native_vlan',
                'openconfig-vlan', False, [
                    _MetaInfoClassMember('native-vlan', ATTRIBUTE, 'int' , None, None, 
                        [('1', '4094')], [], 
                        '''                        Set the native VLAN id for untagged frames arriving on
                        a trunk interface.  This configuration is only valid on
                        a trunk interface.
                        ''',
                        'native_vlan',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('native-vlan', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'], 
                        '''                        Set the native VLAN id for untagged frames arriving on
                        a trunk interface.  This configuration is only valid on
                        a trunk interface.
                        ''',
                        'native_vlan',
                        'openconfig-vlan', False),
                ]),
            _MetaInfoClassMember('trunk-vlans', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Specify VLANs, or ranges thereof, that the interface may
                carry when in trunk mode.  If not specified, all VLANs are
                allowed on the interface. Ranges are specified in the form
                x..y, where x<y - ranges are assumed to be inclusive (such
                that the VLAN range is x <= range <= y.
                ''',
                'trunk_vlans',
                'openconfig-vlan', False, [
                    _MetaInfoClassMember('trunk-vlans', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('1', '4094')], [], 
                        '''                        Specify VLANs, or ranges thereof, that the interface may
                        carry when in trunk mode.  If not specified, all VLANs are
                        allowed on the interface. Ranges are specified in the form
                        x..y, where x<y - ranges are assumed to be inclusive (such
                        that the VLAN range is x <= range <= y.
                        ''',
                        'trunk_vlans',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('trunk-vlans', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])'], 
                        '''                        Specify VLANs, or ranges thereof, that the interface may
                        carry when in trunk mode.  If not specified, all VLANs are
                        allowed on the interface. Ranges are specified in the form
                        x..y, where x<y - ranges are assumed to be inclusive (such
                        that the VLAN range is x <= range <= y.
                        ''',
                        'trunk_vlans',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('trunk-vlans', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'], 
                        '''                        Specify VLANs, or ranges thereof, that the interface may
                        carry when in trunk mode.  If not specified, all VLANs are
                        allowed on the interface. Ranges are specified in the form
                        x..y, where x<y - ranges are assumed to be inclusive (such
                        that the VLAN range is x <= range <= y.
                        ''',
                        'trunk_vlans',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('trunk-vlans', REFERENCE_UNION, 'str' , None, None, 
                        [], [], 
                        '''                        Specify VLANs, or ranges thereof, that the interface may
                        carry when in trunk mode.  If not specified, all VLANs are
                        allowed on the interface. Ranges are specified in the form
                        x..y, where x<y - ranges are assumed to be inclusive (such
                        that the VLAN range is x <= range <= y.
                        ''',
                        'trunk_vlans',
                        'openconfig-vlan', False, [
                            _MetaInfoClassMember('trunk-vlans', REFERENCE_LEAFLIST, 'str' , None, None, 
                                [], [b'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'], 
                                '''                                Specify VLANs, or ranges thereof, that the interface may
                                carry when in trunk mode.  If not specified, all VLANs are
                                allowed on the interface. Ranges are specified in the form
                                x..y, where x<y - ranges are assumed to be inclusive (such
                                that the VLAN range is x <= range <= y.
                                ''',
                                'trunk_vlans',
                                'openconfig-vlan', False),
                            _MetaInfoClassMember('trunk-vlans', REFERENCE_LEAFLIST, 'str' , None, None, 
                                [], [b'(\\*|(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9]))\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])'], 
                                '''                                Specify VLANs, or ranges thereof, that the interface may
                                carry when in trunk mode.  If not specified, all VLANs are
                                allowed on the interface. Ranges are specified in the form
                                x..y, where x<y - ranges are assumed to be inclusive (such
                                that the VLAN range is x <= range <= y.
                                ''',
                                'trunk_vlans',
                                'openconfig-vlan', False),
                        ]),
                ]),
            ],
            'openconfig-vlan',
            'state',
            _yang_ns._namespaces['openconfig-vlan'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Aggregation.Vlan' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Aggregation.Vlan',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Aggregation.Vlan.Config', 
                [], [], 
                '''                Configuration parameters for VLANs
                ''',
                'config',
                'openconfig-vlan', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Aggregation.Vlan.State', 
                [], [], 
                '''                State variables for VLANs
                ''',
                'state',
                'openconfig-vlan', False),
            ],
            'openconfig-vlan',
            'vlan',
            _yang_ns._namespaces['openconfig-vlan'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.Aggregation' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Aggregation',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Aggregation.Config', 
                [], [], 
                '''                Configuration variables for logical aggregate /
                LAG interfaces
                ''',
                'config',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('lacp', REFERENCE_CLASS, 'Lacp' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Aggregation.Lacp', 
                [], [], 
                '''                Configuration for LACP protocol operation on the
                aggregate interface
                ''',
                'lacp',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Aggregation.State', 
                [], [], 
                '''                Operational state variables for logical
                aggregate / LAG interfaces
                ''',
                'state',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('vlan', REFERENCE_CLASS, 'Vlan' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Aggregation.Vlan', 
                [], [], 
                '''                Enclosing container for VLAN interface-specific
                data on Ethernet interfaces
                ''',
                'vlan',
                'openconfig-vlan', False),
            ],
            'openconfig-if-aggregate',
            'aggregation',
            _yang_ns._namespaces['openconfig-if-aggregate'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Config',
            False, 
            [
            _MetaInfoClassMember('vlan', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                References the VLAN for which this IP interface
                provides routing services -- similar to a switch virtual
                interface (SVI), or integrated routing and bridging interface
                (IRB) in some implementations.
                ''',
                'vlan',
                'openconfig-vlan', False, [
                    _MetaInfoClassMember('vlan', ATTRIBUTE, 'int' , None, None, 
                        [('0', '65535')], [], 
                        '''                        References the VLAN for which this IP interface
                        provides routing services -- similar to a switch virtual
                        interface (SVI), or integrated routing and bridging interface
                        (IRB) in some implementations.
                        ''',
                        'vlan',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('vlan', ATTRIBUTE, 'str' , None, None, 
                        [], [], 
                        '''                        References the VLAN for which this IP interface
                        provides routing services -- similar to a switch virtual
                        interface (SVI), or integrated routing and bridging interface
                        (IRB) in some implementations.
                        ''',
                        'vlan',
                        'openconfig-vlan', False),
                ]),
            ],
            'openconfig-vlan',
            'config',
            _yang_ns._namespaces['openconfig-vlan'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.State',
            False, 
            [
            _MetaInfoClassMember('vlan', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                References the VLAN for which this IP interface
                provides routing services -- similar to a switch virtual
                interface (SVI), or integrated routing and bridging interface
                (IRB) in some implementations.
                ''',
                'vlan',
                'openconfig-vlan', False, [
                    _MetaInfoClassMember('vlan', ATTRIBUTE, 'int' , None, None, 
                        [('0', '65535')], [], 
                        '''                        References the VLAN for which this IP interface
                        provides routing services -- similar to a switch virtual
                        interface (SVI), or integrated routing and bridging interface
                        (IRB) in some implementations.
                        ''',
                        'vlan',
                        'openconfig-vlan', False),
                    _MetaInfoClassMember('vlan', ATTRIBUTE, 'str' , None, None, 
                        [], [], 
                        '''                        References the VLAN for which this IP interface
                        provides routing services -- similar to a switch virtual
                        interface (SVI), or integrated routing and bridging interface
                        (IRB) in some implementations.
                        ''',
                        'vlan',
                        'openconfig-vlan', False),
                ]),
            ],
            'openconfig-vlan',
            'state',
            _yang_ns._namespaces['openconfig-vlan'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv4.Address.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv4.Address.Config',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                [adapted from IETF IP model RFC 7277]
                The IPv4 address on the interface.
                ''',
                'ip',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The length of the subnet prefix.
                ''',
                'prefix_length',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'config',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv4.Address.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv4.Address.State',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                [adapted from IETF IP model RFC 7277]
                The IPv4 address on the interface.
                ''',
                'ip',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('origin', REFERENCE_ENUM_CLASS, 'IpAddressOriginEnum' , 'ydk.models.openconfig.openconfig_if_ip', 'IpAddressOriginEnum', 
                [], [], 
                '''                The origin of this address, e.g., statically configured,
                assigned by DHCP, etc..
                ''',
                'origin',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The length of the subnet prefix.
                ''',
                'prefix_length',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'state',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.Config',
            False, 
            [
            _MetaInfoClassMember('accept-mode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Configure whether packets destined for
                virtual addresses are accepted even when the virtual
                address is not owned by the router interface
                ''',
                'accept_mode',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('advertisement-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Sets the interval between successive VRRP
                advertisements -- RFC 5798 defines this as a 12-bit
                value expressed as 0.1 seconds, with default 100, i.e.,
                1 second.  Several implementation express this in units of
                seconds
                ''',
                'advertisement_interval',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('preempt', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set to true, enables preemption by a higher
                priority backup router of a lower priority master router
                ''',
                'preempt',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('preempt-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Set the delay the higher priority router waits
                before preempting
                ''',
                'preempt_delay',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '254')], [], 
                '''                Specifies the sending VRRP interface's priority
                for the virtual router.  Higher values equal higher
                priority
                ''',
                'priority',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('virtual-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Configure one or more virtual addresses for the
                VRRP group
                ''',
                'virtual_address',
                'openconfig-if-ip', False, [
                    _MetaInfoClassMember('virtual-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Configure one or more virtual addresses for the
                        VRRP group
                        ''',
                        'virtual_address',
                        'openconfig-if-ip', False),
                    _MetaInfoClassMember('virtual-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Configure one or more virtual addresses for the
                        VRRP group
                        ''',
                        'virtual_address',
                        'openconfig-if-ip', False),
                ]),
            _MetaInfoClassMember('virtual-router-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Set the virtual router id for use by the VRRP group.  This
                usually also determines the virtual MAC address that is
                generated for the VRRP group
                ''',
                'virtual_router_id',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'config',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.State',
            False, 
            [
            _MetaInfoClassMember('accept-mode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Configure whether packets destined for
                virtual addresses are accepted even when the virtual
                address is not owned by the router interface
                ''',
                'accept_mode',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('advertisement-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Sets the interval between successive VRRP
                advertisements -- RFC 5798 defines this as a 12-bit
                value expressed as 0.1 seconds, with default 100, i.e.,
                1 second.  Several implementation express this in units of
                seconds
                ''',
                'advertisement_interval',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('current-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Operational value of the priority for the
                interface in the VRRP group
                ''',
                'current_priority',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('preempt', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set to true, enables preemption by a higher
                priority backup router of a lower priority master router
                ''',
                'preempt',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('preempt-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Set the delay the higher priority router waits
                before preempting
                ''',
                'preempt_delay',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '254')], [], 
                '''                Specifies the sending VRRP interface's priority
                for the virtual router.  Higher values equal higher
                priority
                ''',
                'priority',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('virtual-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Configure one or more virtual addresses for the
                VRRP group
                ''',
                'virtual_address',
                'openconfig-if-ip', False, [
                    _MetaInfoClassMember('virtual-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Configure one or more virtual addresses for the
                        VRRP group
                        ''',
                        'virtual_address',
                        'openconfig-if-ip', False),
                    _MetaInfoClassMember('virtual-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Configure one or more virtual addresses for the
                        VRRP group
                        ''',
                        'virtual_address',
                        'openconfig-if-ip', False),
                ]),
            _MetaInfoClassMember('virtual-router-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Set the virtual router id for use by the VRRP group.  This
                usually also determines the virtual MAC address that is
                generated for the VRRP group
                ''',
                'virtual_router_id',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'state',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.Config',
            False, 
            [
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int' , None, None, 
                [('0', '254')], [], 
                '''                Set the value to subtract from priority when
                the tracked interface goes down
                ''',
                'priority_decrement',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('track-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sets an interface that should be
                tracked for up/down events to dynamically change the
                priority state of the VRRP group, and potentially
                change the mastership if the tracked interface going
                down lowers the priority sufficiently
                ''',
                'track_interface',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'config',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.State',
            False, 
            [
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int' , None, None, 
                [('0', '254')], [], 
                '''                Set the value to subtract from priority when
                the tracked interface goes down
                ''',
                'priority_decrement',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('track-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sets an interface that should be
                tracked for up/down events to dynamically change the
                priority state of the VRRP group, and potentially
                change the mastership if the tracked interface going
                down lowers the priority sufficiently
                ''',
                'track_interface',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'state',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.Config', 
                [], [], 
                '''                Configuration data for VRRP interface tracking
                ''',
                'config',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.State', 
                [], [], 
                '''                Operational state data for VRRP interface tracking
                ''',
                'state',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'interface-tracking',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup',
            False, 
            [
            _MetaInfoClassMember('virtual-router-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                References the configured virtual router id for this
                VRRP group
                ''',
                'virtual_router_id',
                'openconfig-if-ip', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.Config', 
                [], [], 
                '''                Configuration data for the VRRP group
                ''',
                'config',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('interface-tracking', REFERENCE_CLASS, 'InterfaceTracking' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking', 
                [], [], 
                '''                Top-level container for VRRP interface tracking
                ''',
                'interface_tracking',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.State', 
                [], [], 
                '''                Operational state data for the VRRP group
                ''',
                'state',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'vrrp-group',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp',
            False, 
            [
            _MetaInfoClassMember('vrrp-group', REFERENCE_LIST, 'VrrpGroup' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup', 
                [], [], 
                '''                List of VRRP groups, keyed by virtual router id
                ''',
                'vrrp_group',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'vrrp',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv4.Address' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv4.Address',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                References the configured IP address
                ''',
                'ip',
                'openconfig-if-ip', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv4.Address.Config', 
                [], [], 
                '''                Configuration data for each configured IPv4
                address on the interface
                ''',
                'config',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv4.Address.State', 
                [], [], 
                '''                Operational state data for each IPv4 address
                configured on the interface
                ''',
                'state',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('vrrp', REFERENCE_CLASS, 'Vrrp' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp', 
                [], [], 
                '''                Enclosing container for VRRP groups handled by this
                IP interface
                ''',
                'vrrp',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'address',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv4.Neighbor.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv4.Neighbor.Config',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IPv4 address of the neighbor node.
                ''',
                'ip',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('link-layer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                The link-layer address of the neighbor node.
                ''',
                'link_layer_address',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'config',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv4.Neighbor.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv4.Neighbor.State',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IPv4 address of the neighbor node.
                ''',
                'ip',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('link-layer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                The link-layer address of the neighbor node.
                ''',
                'link_layer_address',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('origin', REFERENCE_ENUM_CLASS, 'NeighborOriginEnum' , 'ydk.models.openconfig.openconfig_if_ip', 'NeighborOriginEnum', 
                [], [], 
                '''                The origin of this neighbor entry, static or dynamic.
                ''',
                'origin',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'state',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv4.Neighbor' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv4.Neighbor',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                References the configured IP address
                ''',
                'ip',
                'openconfig-if-ip', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv4.Neighbor.Config', 
                [], [], 
                '''                Configuration data for each configured IPv4
                address on the interface
                ''',
                'config',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv4.Neighbor.State', 
                [], [], 
                '''                Operational state data for each IPv4 address
                configured on the interface
                ''',
                'state',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'neighbor',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv4.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv4.Config',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Controls whether IPv4 is enabled or disabled on this
                interface.  When IPv4 is enabled, this interface is
                connected to an IPv4 stack, and the interface can send
                and receive IPv4 packets.
                ''',
                'enabled',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('68', '65535')], [], 
                '''                The size, in octets, of the largest IPv4 packet that the
                interface will send and receive.
                The server may restrict the allowed values for this leaf,
                depending on the interface's type.
                If this leaf is not configured, the operationally used MTU
                depends on the interface's type.
                ''',
                'mtu',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'config',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv4.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv4.State',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Controls whether IPv4 is enabled or disabled on this
                interface.  When IPv4 is enabled, this interface is
                connected to an IPv4 stack, and the interface can send
                and receive IPv4 packets.
                ''',
                'enabled',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('68', '65535')], [], 
                '''                The size, in octets, of the largest IPv4 packet that the
                interface will send and receive.
                The server may restrict the allowed values for this leaf,
                depending on the interface's type.
                If this leaf is not configured, the operationally used MTU
                depends on the interface's type.
                ''',
                'mtu',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'state',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv4' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv4',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv4.Address', 
                [], [], 
                '''                The list of configured IPv4 addresses on the interface.
                ''',
                'address',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv4.Config', 
                [], [], 
                '''                Top-level IPv4 configuration data for the interface
                ''',
                'config',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv4.Neighbor', 
                [], [], 
                '''                A list of mappings from IPv4 addresses to
                link-layer addresses.
                Entries in this list are used as static entries in the
                ARP Cache.
                ''',
                'neighbor',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv4.State', 
                [], [], 
                '''                Top level IPv4 operational state data
                ''',
                'state',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'ipv4',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Address.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv6.Address.Config',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                [adapted from IETF IP model RFC 7277]
                The IPv6 address on the interface.
                ''',
                'ip',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The length of the subnet prefix.
                ''',
                'prefix_length',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'config',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Address.State.StatusEnum' : _MetaInfoEnum('StatusEnum', 'ydk.models.openconfig.openconfig_interfaces',
        {
            'PREFERRED':'PREFERRED',
            'DEPRECATED':'DEPRECATED',
            'INVALID':'INVALID',
            'INACCESSIBLE':'INACCESSIBLE',
            'UNKNOWN':'UNKNOWN',
            'TENTATIVE':'TENTATIVE',
            'DUPLICATE':'DUPLICATE',
            'OPTIMISTIC':'OPTIMISTIC',
        }, 'openconfig-if-ip', _yang_ns._namespaces['openconfig-if-ip']),
    'Interfaces.Interface.RoutedVlan.Ipv6.Address.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv6.Address.State',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                [adapted from IETF IP model RFC 7277]
                The IPv6 address on the interface.
                ''',
                'ip',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('origin', REFERENCE_ENUM_CLASS, 'IpAddressOriginEnum' , 'ydk.models.openconfig.openconfig_if_ip', 'IpAddressOriginEnum', 
                [], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The origin of this address, e.g., static, dhcp, etc.
                ''',
                'origin',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The length of the subnet prefix.
                ''',
                'prefix_length',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'StatusEnum' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv6.Address.State.StatusEnum', 
                [], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The status of an address.  Most of the states correspond
                to states from the IPv6 Stateless Address
                Autoconfiguration protocol.
                ''',
                'status',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'state',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.Config',
            False, 
            [
            _MetaInfoClassMember('accept-mode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Configure whether packets destined for
                virtual addresses are accepted even when the virtual
                address is not owned by the router interface
                ''',
                'accept_mode',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('advertisement-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Sets the interval between successive VRRP
                advertisements -- RFC 5798 defines this as a 12-bit
                value expressed as 0.1 seconds, with default 100, i.e.,
                1 second.  Several implementation express this in units of
                seconds
                ''',
                'advertisement_interval',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('preempt', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set to true, enables preemption by a higher
                priority backup router of a lower priority master router
                ''',
                'preempt',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('preempt-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Set the delay the higher priority router waits
                before preempting
                ''',
                'preempt_delay',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '254')], [], 
                '''                Specifies the sending VRRP interface's priority
                for the virtual router.  Higher values equal higher
                priority
                ''',
                'priority',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('virtual-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Configure one or more virtual addresses for the
                VRRP group
                ''',
                'virtual_address',
                'openconfig-if-ip', False, [
                    _MetaInfoClassMember('virtual-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Configure one or more virtual addresses for the
                        VRRP group
                        ''',
                        'virtual_address',
                        'openconfig-if-ip', False),
                    _MetaInfoClassMember('virtual-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Configure one or more virtual addresses for the
                        VRRP group
                        ''',
                        'virtual_address',
                        'openconfig-if-ip', False),
                ]),
            _MetaInfoClassMember('virtual-link-local', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                For VRRP on IPv6 interfaces, sets the virtual link local
                address
                ''',
                'virtual_link_local',
                'openconfig-if-ip', False, [
                    _MetaInfoClassMember('virtual-link-local', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        For VRRP on IPv6 interfaces, sets the virtual link local
                        address
                        ''',
                        'virtual_link_local',
                        'openconfig-if-ip', False),
                    _MetaInfoClassMember('virtual-link-local', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        For VRRP on IPv6 interfaces, sets the virtual link local
                        address
                        ''',
                        'virtual_link_local',
                        'openconfig-if-ip', False),
                ]),
            _MetaInfoClassMember('virtual-router-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Set the virtual router id for use by the VRRP group.  This
                usually also determines the virtual MAC address that is
                generated for the VRRP group
                ''',
                'virtual_router_id',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'config',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.State',
            False, 
            [
            _MetaInfoClassMember('accept-mode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Configure whether packets destined for
                virtual addresses are accepted even when the virtual
                address is not owned by the router interface
                ''',
                'accept_mode',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('advertisement-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Sets the interval between successive VRRP
                advertisements -- RFC 5798 defines this as a 12-bit
                value expressed as 0.1 seconds, with default 100, i.e.,
                1 second.  Several implementation express this in units of
                seconds
                ''',
                'advertisement_interval',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('current-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Operational value of the priority for the
                interface in the VRRP group
                ''',
                'current_priority',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('preempt', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set to true, enables preemption by a higher
                priority backup router of a lower priority master router
                ''',
                'preempt',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('preempt-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Set the delay the higher priority router waits
                before preempting
                ''',
                'preempt_delay',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '254')], [], 
                '''                Specifies the sending VRRP interface's priority
                for the virtual router.  Higher values equal higher
                priority
                ''',
                'priority',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('virtual-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Configure one or more virtual addresses for the
                VRRP group
                ''',
                'virtual_address',
                'openconfig-if-ip', False, [
                    _MetaInfoClassMember('virtual-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Configure one or more virtual addresses for the
                        VRRP group
                        ''',
                        'virtual_address',
                        'openconfig-if-ip', False),
                    _MetaInfoClassMember('virtual-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Configure one or more virtual addresses for the
                        VRRP group
                        ''',
                        'virtual_address',
                        'openconfig-if-ip', False),
                ]),
            _MetaInfoClassMember('virtual-link-local', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                For VRRP on IPv6 interfaces, sets the virtual link local
                address
                ''',
                'virtual_link_local',
                'openconfig-if-ip', False, [
                    _MetaInfoClassMember('virtual-link-local', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        For VRRP on IPv6 interfaces, sets the virtual link local
                        address
                        ''',
                        'virtual_link_local',
                        'openconfig-if-ip', False),
                    _MetaInfoClassMember('virtual-link-local', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        For VRRP on IPv6 interfaces, sets the virtual link local
                        address
                        ''',
                        'virtual_link_local',
                        'openconfig-if-ip', False),
                ]),
            _MetaInfoClassMember('virtual-router-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Set the virtual router id for use by the VRRP group.  This
                usually also determines the virtual MAC address that is
                generated for the VRRP group
                ''',
                'virtual_router_id',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'state',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.Config',
            False, 
            [
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int' , None, None, 
                [('0', '254')], [], 
                '''                Set the value to subtract from priority when
                the tracked interface goes down
                ''',
                'priority_decrement',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('track-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sets an interface that should be
                tracked for up/down events to dynamically change the
                priority state of the VRRP group, and potentially
                change the mastership if the tracked interface going
                down lowers the priority sufficiently
                ''',
                'track_interface',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'config',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.State',
            False, 
            [
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int' , None, None, 
                [('0', '254')], [], 
                '''                Set the value to subtract from priority when
                the tracked interface goes down
                ''',
                'priority_decrement',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('track-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sets an interface that should be
                tracked for up/down events to dynamically change the
                priority state of the VRRP group, and potentially
                change the mastership if the tracked interface going
                down lowers the priority sufficiently
                ''',
                'track_interface',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'state',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.Config', 
                [], [], 
                '''                Configuration data for VRRP interface tracking
                ''',
                'config',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.State', 
                [], [], 
                '''                Operational state data for VRRP interface tracking
                ''',
                'state',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'interface-tracking',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup',
            False, 
            [
            _MetaInfoClassMember('virtual-router-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                References the configured virtual router id for this
                VRRP group
                ''',
                'virtual_router_id',
                'openconfig-if-ip', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.Config', 
                [], [], 
                '''                Configuration data for the VRRP group
                ''',
                'config',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('interface-tracking', REFERENCE_CLASS, 'InterfaceTracking' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking', 
                [], [], 
                '''                Top-level container for VRRP interface tracking
                ''',
                'interface_tracking',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.State', 
                [], [], 
                '''                Operational state data for the VRRP group
                ''',
                'state',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'vrrp-group',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp',
            False, 
            [
            _MetaInfoClassMember('vrrp-group', REFERENCE_LIST, 'VrrpGroup' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup', 
                [], [], 
                '''                List of VRRP groups, keyed by virtual router id
                ''',
                'vrrp_group',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'vrrp',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Address' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv6.Address',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                References the configured IP address
                ''',
                'ip',
                'openconfig-if-ip', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv6.Address.Config', 
                [], [], 
                '''                Configuration data for each IPv6 address on
                the interface
                ''',
                'config',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv6.Address.State', 
                [], [], 
                '''                State data for each IPv6 address on the
                interface
                ''',
                'state',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('vrrp', REFERENCE_CLASS, 'Vrrp' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp', 
                [], [], 
                '''                Enclosing container for VRRP groups handled by this
                IP interface
                ''',
                'vrrp',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'address',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Neighbor.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv6.Neighbor.Config',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                [adapted from IETF IP model RFC 7277]
                The IPv6 address of the neighbor node.
                ''',
                'ip',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('link-layer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                [adapted from IETF IP model RFC 7277]
                The link-layer address of the neighbor node.
                ''',
                'link_layer_address',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'config',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Neighbor.State.NeighborStateEnum' : _MetaInfoEnum('NeighborStateEnum', 'ydk.models.openconfig.openconfig_interfaces',
        {
            'INCOMPLETE':'INCOMPLETE',
            'REACHABLE':'REACHABLE',
            'STALE':'STALE',
            'DELAY':'DELAY',
            'PROBE':'PROBE',
        }, 'openconfig-if-ip', _yang_ns._namespaces['openconfig-if-ip']),
    'Interfaces.Interface.RoutedVlan.Ipv6.Neighbor.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv6.Neighbor.State',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                [adapted from IETF IP model RFC 7277]
                The IPv6 address of the neighbor node.
                ''',
                'ip',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('is-router', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                [adapted from IETF IP model RFC 7277]
                Indicates that the neighbor node acts as a router.
                ''',
                'is_router',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('link-layer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                [adapted from IETF IP model RFC 7277]
                The link-layer address of the neighbor node.
                ''',
                'link_layer_address',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('neighbor-state', REFERENCE_ENUM_CLASS, 'NeighborStateEnum' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv6.Neighbor.State.NeighborStateEnum', 
                [], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The Neighbor Unreachability Detection state of this
                entry.
                ''',
                'neighbor_state',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('origin', REFERENCE_ENUM_CLASS, 'NeighborOriginEnum' , 'ydk.models.openconfig.openconfig_if_ip', 'NeighborOriginEnum', 
                [], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The origin of this neighbor entry.
                ''',
                'origin',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'state',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Neighbor' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv6.Neighbor',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                References the configured IP neighbor address
                ''',
                'ip',
                'openconfig-if-ip', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv6.Neighbor.Config', 
                [], [], 
                '''                Configuration data for each IPv6 address on
                the interface
                ''',
                'config',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv6.Neighbor.State', 
                [], [], 
                '''                State data for each IPv6 address on the
                interface
                ''',
                'state',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'neighbor',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv6.Config',
            False, 
            [
            _MetaInfoClassMember('dup-addr-detect-transmits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The number of consecutive Neighbor Solicitation messages
                sent while performing Duplicate Address Detection on a
                tentative address.  A value of zero indicates that
                Duplicate Address Detection is not performed on
                tentative addresses.  A value of one indicates a single
                transmission with no follow-up retransmissions.
                ''',
                'dup_addr_detect_transmits',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                [adapted from IETF IP model RFC 7277]
                Controls whether IPv6 is enabled or disabled on this
                interface.  When IPv6 is enabled, this interface is
                connected to an IPv6 stack, and the interface can send
                and receive IPv6 packets.
                ''',
                'enabled',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('1280', '4294967295')], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The size, in octets, of the largest IPv6 packet that the
                interface will send and receive.
                The server may restrict the allowed values for this leaf,
                depending on the interface's type.
                If this leaf is not configured, the operationally used MTU
                depends on the interface's type.
                ''',
                'mtu',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'config',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv6.State',
            False, 
            [
            _MetaInfoClassMember('dup-addr-detect-transmits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The number of consecutive Neighbor Solicitation messages
                sent while performing Duplicate Address Detection on a
                tentative address.  A value of zero indicates that
                Duplicate Address Detection is not performed on
                tentative addresses.  A value of one indicates a single
                transmission with no follow-up retransmissions.
                ''',
                'dup_addr_detect_transmits',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                [adapted from IETF IP model RFC 7277]
                Controls whether IPv6 is enabled or disabled on this
                interface.  When IPv6 is enabled, this interface is
                connected to an IPv6 stack, and the interface can send
                and receive IPv6 packets.
                ''',
                'enabled',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('1280', '4294967295')], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The size, in octets, of the largest IPv6 packet that the
                interface will send and receive.
                The server may restrict the allowed values for this leaf,
                depending on the interface's type.
                If this leaf is not configured, the operationally used MTU
                depends on the interface's type.
                ''',
                'mtu',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'state',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Autoconf.Config' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv6.Autoconf.Config',
            False, 
            [
            _MetaInfoClassMember('create-global-addresses', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                [adapted from IETF IP model RFC 7277]
                If enabled, the host creates global addresses as
                described in RFC 4862.
                ''',
                'create_global_addresses',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('create-temporary-addresses', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                [adapted from IETF IP model RFC 7277]
                If enabled, the host creates temporary addresses as
                described in RFC 4941.
                ''',
                'create_temporary_addresses',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('temporary-preferred-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The time period during which the temporary address is
                preferred.
                ''',
                'temporary_preferred_lifetime',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('temporary-valid-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The time period during which the temporary address
                is valid.
                ''',
                'temporary_valid_lifetime',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'config',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Autoconf.State' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv6.Autoconf.State',
            False, 
            [
            _MetaInfoClassMember('create-global-addresses', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                [adapted from IETF IP model RFC 7277]
                If enabled, the host creates global addresses as
                described in RFC 4862.
                ''',
                'create_global_addresses',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('create-temporary-addresses', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                [adapted from IETF IP model RFC 7277]
                If enabled, the host creates temporary addresses as
                described in RFC 4941.
                ''',
                'create_temporary_addresses',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('temporary-preferred-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The time period during which the temporary address is
                preferred.
                ''',
                'temporary_preferred_lifetime',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('temporary-valid-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                [adapted from IETF IP model RFC 7277]
                The time period during which the temporary address
                is valid.
                ''',
                'temporary_valid_lifetime',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'state',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Autoconf' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv6.Autoconf',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv6.Autoconf.Config', 
                [], [], 
                '''                [adapted from IETF IP model RFC 7277]
                Parameters to control the autoconfiguration of IPv6
                addresses, as described in RFC 4862.
                ''',
                'config',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv6.Autoconf.State', 
                [], [], 
                '''                Operational state data 
                ''',
                'state',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'autoconf',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan.Ipv6' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan.Ipv6',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv6.Address', 
                [], [], 
                '''                The list of configured IPv6 addresses on the interface.
                ''',
                'address',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('autoconf', REFERENCE_CLASS, 'Autoconf' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv6.Autoconf', 
                [], [], 
                '''                Top-level container for IPv6 autoconf
                ''',
                'autoconf',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv6.Config', 
                [], [], 
                '''                Top-level config data for the IPv6 interface
                ''',
                'config',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv6.Neighbor', 
                [], [], 
                '''                A list of mappings from IPv6 addresses to
                link-layer addresses.
                Entries in this list are used as static entries in the
                Neighbor Cache.
                ''',
                'neighbor',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv6.State', 
                [], [], 
                '''                Top-level operational state data for the IPv6 interface
                ''',
                'state',
                'openconfig-if-ip', False),
            ],
            'openconfig-if-ip',
            'ipv6',
            _yang_ns._namespaces['openconfig-if-ip'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface.RoutedVlan' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.RoutedVlan',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Config', 
                [], [], 
                '''                Configuration data for routed vlan interfaces
                ''',
                'config',
                'openconfig-vlan', False),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv4', 
                [], [], 
                '''                Parameters for the IPv4 address family.
                ''',
                'ipv4',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.Ipv6', 
                [], [], 
                '''                Parameters for the IPv6 address family.
                ''',
                'ipv6',
                'openconfig-if-ip', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan.State', 
                [], [], 
                '''                Operational state data 
                ''',
                'state',
                'openconfig-vlan', False),
            ],
            'openconfig-vlan',
            'routed-vlan',
            _yang_ns._namespaces['openconfig-vlan'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                References the configured name of the interface
                ''',
                'name',
                'openconfig-interfaces', True),
            _MetaInfoClassMember('aggregation', REFERENCE_CLASS, 'Aggregation' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Aggregation', 
                [], [], 
                '''                Options for logical interfaces representing
                aggregates
                ''',
                'aggregation',
                'openconfig-if-aggregate', False),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Config', 
                [], [], 
                '''                Configurable items at the global, physical interface
                level
                ''',
                'config',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('ethernet', REFERENCE_CLASS, 'Ethernet' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Ethernet', 
                [], [], 
                '''                Top-level container for ethernet configuration
                and state
                ''',
                'ethernet',
                'openconfig-if-ethernet', False),
            _MetaInfoClassMember('hold-time', REFERENCE_CLASS, 'HoldTime' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.HoldTime', 
                [], [], 
                '''                Top-level container for hold-time settings to enable
                dampening advertisements of interface transitions.
                ''',
                'hold_time',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('routed-vlan', REFERENCE_CLASS, 'RoutedVlan' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.RoutedVlan', 
                [], [], 
                '''                Top-level container for routed vlan interfaces.  These
                logical interfaces are also known as SVI (switched virtual
                interface), IRB (integrated routing and bridging), RVI
                (routed VLAN interface)
                ''',
                'routed_vlan',
                'openconfig-vlan', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.State', 
                [], [], 
                '''                Operational state data at the global interface level
                ''',
                'state',
                'openconfig-interfaces', False),
            _MetaInfoClassMember('subinterfaces', REFERENCE_CLASS, 'Subinterfaces' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface.Subinterfaces', 
                [], [], 
                '''                Enclosing container for the list of subinterfaces associated
                with a physical interface
                ''',
                'subinterfaces',
                'openconfig-interfaces', False),
            ],
            'openconfig-interfaces',
            'interface',
            _yang_ns._namespaces['openconfig-interfaces'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
    'Interfaces' : {
        'meta_info' : _MetaInfoClass('Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.openconfig.openconfig_interfaces', 'Interfaces.Interface', 
                [], [], 
                '''                The list of named interfaces on the device.
                ''',
                'interface',
                'openconfig-interfaces', False),
            ],
            'openconfig-interfaces',
            'interfaces',
            _yang_ns._namespaces['openconfig-interfaces'],
        'ydk.models.openconfig.openconfig_interfaces'
        ),
    },
}
_meta_table['Interfaces.Interface.State.Counters']['meta_info'].parent =_meta_table['Interfaces.Interface.State']['meta_info']
_meta_table['Interfaces.Interface.HoldTime.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.HoldTime']['meta_info']
_meta_table['Interfaces.Interface.HoldTime.State']['meta_info'].parent =_meta_table['Interfaces.Interface.HoldTime']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.State.Counters']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.State']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Vlan.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Vlan']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Vlan.State']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Vlan']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.State']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.State']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.State']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbor.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbor']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbor.State']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbor']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbor']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.State']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.State']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.State']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.State']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor.State']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf.State']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.State']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.State']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Vlan']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces.Subinterface']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces.Subinterface']['meta_info'].parent =_meta_table['Interfaces.Interface.Subinterfaces']['meta_info']
_meta_table['Interfaces.Interface.Ethernet.State.Counters']['meta_info'].parent =_meta_table['Interfaces.Interface.Ethernet.State']['meta_info']
_meta_table['Interfaces.Interface.Ethernet.Vlan.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.Ethernet.Vlan']['meta_info']
_meta_table['Interfaces.Interface.Ethernet.Vlan.State']['meta_info'].parent =_meta_table['Interfaces.Interface.Ethernet.Vlan']['meta_info']
_meta_table['Interfaces.Interface.Ethernet.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.Ethernet']['meta_info']
_meta_table['Interfaces.Interface.Ethernet.State']['meta_info'].parent =_meta_table['Interfaces.Interface.Ethernet']['meta_info']
_meta_table['Interfaces.Interface.Ethernet.Vlan']['meta_info'].parent =_meta_table['Interfaces.Interface.Ethernet']['meta_info']
_meta_table['Interfaces.Interface.Aggregation.Lacp.Members.Member.State.Counters']['meta_info'].parent =_meta_table['Interfaces.Interface.Aggregation.Lacp.Members.Member.State']['meta_info']
_meta_table['Interfaces.Interface.Aggregation.Lacp.Members.Member.State']['meta_info'].parent =_meta_table['Interfaces.Interface.Aggregation.Lacp.Members.Member']['meta_info']
_meta_table['Interfaces.Interface.Aggregation.Lacp.Members.Member']['meta_info'].parent =_meta_table['Interfaces.Interface.Aggregation.Lacp.Members']['meta_info']
_meta_table['Interfaces.Interface.Aggregation.Lacp.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.Aggregation.Lacp']['meta_info']
_meta_table['Interfaces.Interface.Aggregation.Lacp.State']['meta_info'].parent =_meta_table['Interfaces.Interface.Aggregation.Lacp']['meta_info']
_meta_table['Interfaces.Interface.Aggregation.Lacp.Members']['meta_info'].parent =_meta_table['Interfaces.Interface.Aggregation.Lacp']['meta_info']
_meta_table['Interfaces.Interface.Aggregation.Vlan.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.Aggregation.Vlan']['meta_info']
_meta_table['Interfaces.Interface.Aggregation.Vlan.State']['meta_info'].parent =_meta_table['Interfaces.Interface.Aggregation.Vlan']['meta_info']
_meta_table['Interfaces.Interface.Aggregation.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.Aggregation']['meta_info']
_meta_table['Interfaces.Interface.Aggregation.State']['meta_info'].parent =_meta_table['Interfaces.Interface.Aggregation']['meta_info']
_meta_table['Interfaces.Interface.Aggregation.Lacp']['meta_info'].parent =_meta_table['Interfaces.Interface.Aggregation']['meta_info']
_meta_table['Interfaces.Interface.Aggregation.Vlan']['meta_info'].parent =_meta_table['Interfaces.Interface.Aggregation']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.State']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.State']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address.State']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Neighbor.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Neighbor']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Neighbor.State']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Neighbor']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv4']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Neighbor']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv4']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv4']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv4.State']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv4']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.State']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.State']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address.State']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Neighbor.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Neighbor']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Neighbor.State']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Neighbor']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Autoconf.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Autoconf']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Autoconf.State']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Autoconf']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv6']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Neighbor']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv6']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv6']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.State']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv6']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Autoconf']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan.Ipv6']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Config']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.State']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv4']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan.Ipv6']['meta_info'].parent =_meta_table['Interfaces.Interface.RoutedVlan']['meta_info']
_meta_table['Interfaces.Interface.Config']['meta_info'].parent =_meta_table['Interfaces.Interface']['meta_info']
_meta_table['Interfaces.Interface.State']['meta_info'].parent =_meta_table['Interfaces.Interface']['meta_info']
_meta_table['Interfaces.Interface.HoldTime']['meta_info'].parent =_meta_table['Interfaces.Interface']['meta_info']
_meta_table['Interfaces.Interface.Subinterfaces']['meta_info'].parent =_meta_table['Interfaces.Interface']['meta_info']
_meta_table['Interfaces.Interface.Ethernet']['meta_info'].parent =_meta_table['Interfaces.Interface']['meta_info']
_meta_table['Interfaces.Interface.Aggregation']['meta_info'].parent =_meta_table['Interfaces.Interface']['meta_info']
_meta_table['Interfaces.Interface.RoutedVlan']['meta_info'].parent =_meta_table['Interfaces.Interface']['meta_info']
_meta_table['Interfaces.Interface']['meta_info'].parent =_meta_table['Interfaces']['meta_info']

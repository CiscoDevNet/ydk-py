


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'InterfaceTypeIdentity' : {
        'meta_info' : _MetaInfoClass('InterfaceTypeIdentity',
            False, 
            [
            ],
            'ietf-interfaces',
            'interface-type',
            _yang_ns._namespaces['ietf-interfaces'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.LinkUpDownTrapEnableEnum' : _MetaInfoEnum('LinkUpDownTrapEnableEnum', 'ydk.models.ietf.ietf_interfaces',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'ietf-interfaces', _yang_ns._namespaces['ietf-interfaces']),
    'Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the interface.
                
                A device MAY restrict the allowed values for this leaf,
                possibly depending on the type of the interface.
                For system-controlled interfaces, this leaf is the
                device-specific name of the interface.  The 'config false'
                list /interfaces-state/interface contains the currently
                existing interfaces on the device.
                
                If a client tries to create configuration for a
                system-controlled interface that is not present in the
                /interfaces-state/interface list, the server MAY reject
                the request if the implementation does not support
                pre-provisioning of interfaces or if the name refers to
                an interface that can never exist in the system.  A
                NETCONF server MUST reply with an rpc-error with the
                error-tag 'invalid-value' in this case.
                
                If the device supports pre-provisioning of interface
                configuration, the 'pre-provisioning' feature is
                advertised.
                
                If the device allows arbitrarily named user-controlled
                interfaces, the 'arbitrary-names' feature is advertised.
                
                When a configured user-controlled interface is created by
                the system, it is instantiated with the same name in the
                /interface-state/interface list.
                ''',
                'name',
                'ietf-interfaces', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A textual description of the interface.
                
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
                'ietf-interfaces', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf contains the configured, desired state of the
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
                'ietf-interfaces', False),
            _MetaInfoClassMember('link-up-down-trap-enable', REFERENCE_ENUM_CLASS, 'LinkUpDownTrapEnableEnum' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.LinkUpDownTrapEnableEnum', 
                [], [], 
                '''                Controls whether linkUp/linkDown SNMP notifications
                should be generated for this interface.
                
                If this node is not configured, the value 'enabled' is
                operationally used by the server for interfaces that do
                not operate on top of any other interface (i.e., there are
                no 'lower-layer-if' entries), and 'disabled' otherwise.
                ''',
                'link_up_down_trap_enable',
                'ietf-interfaces', False),
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'InterfaceTypeIdentity' , 'ydk.models.ietf.ietf_interfaces', 'InterfaceTypeIdentity', 
                [], [], 
                '''                The type of the interface.
                
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
                'ietf-interfaces', False),
            ],
            'ietf-interfaces',
            'interface',
            _yang_ns._namespaces['ietf-interfaces'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces' : {
        'meta_info' : _MetaInfoClass('Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface', 
                [], [], 
                '''                The list of configured interfaces on the device.
                
                The operational state of an interface is available in the
                /interfaces-state/interface list.  If the configuration of a
                system-controlled interface cannot be used by the system
                (e.g., the interface hardware present does not match the
                interface type), then the configuration is not applied to
                the system-controlled interface shown in the
                /interfaces-state/interface list.  If the configuration
                of a user-controlled interface cannot be used by the system,
                the configured interface is not instantiated in the
                /interfaces-state/interface list.
                ''',
                'interface',
                'ietf-interfaces', False),
            ],
            'ietf-interfaces',
            'interfaces',
            _yang_ns._namespaces['ietf-interfaces'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'InterfacesState.Interface.Statistics' : {
        'meta_info' : _MetaInfoClass('InterfacesState.Interface.Statistics',
            False, 
            [
            _MetaInfoClassMember('discontinuity-time', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                The time on the most recent occasion at which any one or
                more of this interface's counters suffered a
                discontinuity.  If no such discontinuities have occurred
                since the last re-initialization of the local management
                subsystem, then this node contains the time the local
                management subsystem re-initialized itself.
                ''',
                'discontinuity_time',
                'ietf-interfaces', False),
            _MetaInfoClassMember('in-broadcast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of packets, delivered by this sub-layer to a
                higher (sub-)layer, that were addressed to a broadcast
                address at this sub-layer.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_broadcast_pkts',
                'ietf-interfaces', False),
            _MetaInfoClassMember('in-discards', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of inbound packets that were chosen to be
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
                'ietf-interfaces', False),
            _MetaInfoClassMember('in-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                For packet-oriented interfaces, the number of inbound
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
                'ietf-interfaces', False),
            _MetaInfoClassMember('in-multicast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of packets, delivered by this sub-layer to a
                higher (sub-)layer, that were addressed to a multicast
                address at this sub-layer.  For a MAC-layer protocol,
                this includes both Group and Functional addresses.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_multicast_pkts',
                'ietf-interfaces', False),
            _MetaInfoClassMember('in-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of octets received on the interface,
                including framing characters.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_octets',
                'ietf-interfaces', False),
            _MetaInfoClassMember('in-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                total packets input
                ''',
                'in_pkts',
                'ietf-interfaces-ext', False),
            _MetaInfoClassMember('in-unicast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of packets, delivered by this sub-layer to a
                higher (sub-)layer, that were not addressed to a
                multicast or broadcast address at this sub-layer.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_unicast_pkts',
                'ietf-interfaces', False),
            _MetaInfoClassMember('in-unknown-protos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                For packet-oriented interfaces, the number of packets
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
                'ietf-interfaces', False),
            _MetaInfoClassMember('out-broadcast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of packets that higher-level protocols
                requested be transmitted, and that were addressed to a
                broadcast address at this sub-layer, including those
                that were discarded or not sent.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'out_broadcast_pkts',
                'ietf-interfaces', False),
            _MetaInfoClassMember('out-discards', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of outbound packets that were chosen to be
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
                'ietf-interfaces', False),
            _MetaInfoClassMember('out-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                For packet-oriented interfaces, the number of outbound
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
                'ietf-interfaces', False),
            _MetaInfoClassMember('out-multicast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of packets that higher-level protocols
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
                'ietf-interfaces', False),
            _MetaInfoClassMember('out-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of octets transmitted out of the
                interface, including framing characters.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'out_octets',
                'ietf-interfaces', False),
            _MetaInfoClassMember('out-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                total packets output
                ''',
                'out_pkts',
                'ietf-interfaces-ext', False),
            _MetaInfoClassMember('out-unicast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of packets that higher-level protocols
                requested be transmitted, and that were not addressed
                to a multicast or broadcast address at this sub-layer,
                including those that were discarded or not sent.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'out_unicast_pkts',
                'ietf-interfaces', False),
            ],
            'ietf-interfaces',
            'statistics',
            _yang_ns._namespaces['ietf-interfaces'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'InterfacesState.Interface.Bandwidth' : {
        'meta_info' : _MetaInfoClass('InterfacesState.Interface.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('units', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Units of the bandwidth.
                ''',
                'units',
                'ietf-interfaces-ext', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Raw value for the bandwidth.
                ''',
                'value',
                'ietf-interfaces-ext', False),
            ],
            'ietf-interfaces-ext',
            'bandwidth',
            _yang_ns._namespaces['ietf-interfaces-ext'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'InterfacesState.Interface.AdminStatusEnum' : _MetaInfoEnum('AdminStatusEnum', 'ydk.models.ietf.ietf_interfaces',
        {
            'up':'up',
            'down':'down',
            'testing':'testing',
        }, 'ietf-interfaces', _yang_ns._namespaces['ietf-interfaces']),
    'InterfacesState.Interface.OperStatusEnum' : _MetaInfoEnum('OperStatusEnum', 'ydk.models.ietf.ietf_interfaces',
        {
            'up':'up',
            'down':'down',
            'testing':'testing',
            'unknown':'unknown',
            'dormant':'dormant',
            'not-present':'not_present',
            'lower-layer-down':'lower_layer_down',
        }, 'ietf-interfaces', _yang_ns._namespaces['ietf-interfaces']),
    'InterfacesState.Interface' : {
        'meta_info' : _MetaInfoClass('InterfacesState.Interface',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the interface.
                
                A server implementation MAY map this leaf to the ifName
                MIB object.  Such an implementation needs to use some
                mechanism to handle the differences in size and characters
                allowed between this leaf and ifName.  The definition of
                such a mechanism is outside the scope of this document.
                ''',
                'name',
                'ietf-interfaces', True),
            _MetaInfoClassMember('admin-status', REFERENCE_ENUM_CLASS, 'AdminStatusEnum' , 'ydk.models.ietf.ietf_interfaces', 'InterfacesState.Interface.AdminStatusEnum', 
                [], [], 
                '''                The desired state of the interface.
                
                This leaf has the same read semantics as ifAdminStatus.
                ''',
                'admin_status',
                'ietf-interfaces', False),
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.ietf.ietf_interfaces', 'InterfacesState.Interface.Bandwidth', 
                [], [], 
                '''                Bandwidth data for an interface.
                ''',
                'bandwidth',
                'ietf-interfaces-ext', False),
            _MetaInfoClassMember('higher-layer-if', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                A list of references to interfaces layered on top of this
                interface.
                ''',
                'higher_layer_if',
                'ietf-interfaces', False),
            _MetaInfoClassMember('if-index', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The ifIndex value for the ifEntry represented by this
                interface.
                ''',
                'if_index',
                'ietf-interfaces', False),
            _MetaInfoClassMember('last-change', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                The time the interface entered its current operational
                state.  If the current state was entered prior to the
                last re-initialization of the local network management
                subsystem, then this node is not present.
                ''',
                'last_change',
                'ietf-interfaces', False),
            _MetaInfoClassMember('lower-layer-if', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                A list of references to interfaces layered underneath this
                interface.
                ''',
                'lower_layer_if',
                'ietf-interfaces', False),
            _MetaInfoClassMember('oper-status', REFERENCE_ENUM_CLASS, 'OperStatusEnum' , 'ydk.models.ietf.ietf_interfaces', 'InterfacesState.Interface.OperStatusEnum', 
                [], [], 
                '''                The current operational state of the interface.
                
                This leaf has the same semantics as ifOperStatus.
                ''',
                'oper_status',
                'ietf-interfaces', False),
            _MetaInfoClassMember('phys-address', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                The interface's address at its protocol sub-layer.  For
                example, for an 802.x interface, this object normally
                contains a Media Access Control (MAC) address.  The
                interface's media-specific modules must define the bit
                
                
                and byte ordering and the format of the value of this
                object.  For interfaces that do not have such an address
                (e.g., a serial line), this node is not present.
                ''',
                'phys_address',
                'ietf-interfaces', False),
            _MetaInfoClassMember('speed', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                An estimate of the interface's current bandwidth in bits
                per second.  For interfaces that do not vary in
                bandwidth or for those where no accurate estimation can
                be made, this node should contain the nominal bandwidth.
                For interfaces that have no concept of bandwidth, this
                node is not present.
                ''',
                'speed',
                'ietf-interfaces', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.ietf.ietf_interfaces', 'InterfacesState.Interface.Statistics', 
                [], [], 
                '''                A collection of interface-related statistics objects.
                ''',
                'statistics',
                'ietf-interfaces', False),
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'InterfaceTypeIdentity' , 'ydk.models.ietf.ietf_interfaces', 'InterfaceTypeIdentity', 
                [], [], 
                '''                The type of the interface.
                ''',
                'type',
                'ietf-interfaces', False),
            ],
            'ietf-interfaces',
            'interface',
            _yang_ns._namespaces['ietf-interfaces'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'InterfacesState' : {
        'meta_info' : _MetaInfoClass('InterfacesState',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.ietf.ietf_interfaces', 'InterfacesState.Interface', 
                [], [], 
                '''                The list of interfaces on the device.
                
                System-controlled interfaces created by the system are
                always present in this list, whether they are configured or
                not.
                ''',
                'interface',
                'ietf-interfaces', False),
            ],
            'ietf-interfaces',
            'interfaces-state',
            _yang_ns._namespaces['ietf-interfaces'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
}
_meta_table['Interfaces.Interface']['meta_info'].parent =_meta_table['Interfaces']['meta_info']
_meta_table['InterfacesState.Interface.Statistics']['meta_info'].parent =_meta_table['InterfacesState.Interface']['meta_info']
_meta_table['InterfacesState.Interface.Bandwidth']['meta_info'].parent =_meta_table['InterfacesState.Interface']['meta_info']
_meta_table['InterfacesState.Interface']['meta_info'].parent =_meta_table['InterfacesState']['meta_info']

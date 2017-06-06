


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
    'Interfaces.Interface.DiffservTargetEntry' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.DiffservTargetEntry',
            False, 
            [
            _MetaInfoClassMember('direction', REFERENCE_IDENTITY_CLASS, 'DirectionIdentity' , 'ydk.models.ietf.ietf_diffserv_target', 'DirectionIdentity', 
                [], [], 
                '''                Direction fo the traffic flow either inbound or outbound
                ''',
                'direction',
                'ietf-diffserv-target', True),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy entry name
                ''',
                'policy_name',
                'ietf-diffserv-target', True),
            ],
            'ietf-diffserv-target',
            'diffserv-target-entry',
            _yang_ns._namespaces['ietf-diffserv-target'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.Ipv4.Address' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Ipv4.Address',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IPv4 address on the interface.
                ''',
                'ip',
                'ietf-ip', True),
            _MetaInfoClassMember('netmask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                The subnet specified as a netmask.
                ''',
                'netmask',
                'ietf-ip', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                The length of the subnet prefix.
                ''',
                'prefix_length',
                'ietf-ip', False),
            ],
            'ietf-ip',
            'address',
            _yang_ns._namespaces['ietf-ip'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.Ipv4.Neighbor' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Ipv4.Neighbor',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IPv4 address of the neighbor node.
                ''',
                'ip',
                'ietf-ip', True),
            _MetaInfoClassMember('link-layer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                The link-layer address of the neighbor node.
                ''',
                'link_layer_address',
                'ietf-ip', False),
            ],
            'ietf-ip',
            'neighbor',
            _yang_ns._namespaces['ietf-ip'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.Ipv4' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Ipv4',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.Ipv4.Address', 
                [], [], 
                '''                The list of configured IPv4 addresses on the interface.
                ''',
                'address',
                'ietf-ip', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Controls whether IPv4 is enabled or disabled on this
                interface.  When IPv4 is enabled, this interface is
                connected to an IPv4 stack, and the interface can send
                and receive IPv4 packets.
                ''',
                'enabled',
                'ietf-ip', False),
            _MetaInfoClassMember('forwarding', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Controls IPv4 packet forwarding of datagrams received by,
                but not addressed to, this interface.  IPv4 routers
                forward datagrams.  IPv4 hosts do not (except those
                source-routed via the host).
                ''',
                'forwarding',
                'ietf-ip', False),
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
                'ietf-ip', False),
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.Ipv4.Neighbor', 
                [], [], 
                '''                A list of mappings from IPv4 addresses to
                link-layer addresses.
                Entries in this list are used as static entries in the
                ARP Cache.
                ''',
                'neighbor',
                'ietf-ip', False),
            ],
            'ietf-ip',
            'ipv4',
            _yang_ns._namespaces['ietf-ip'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.Ipv6.Address' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Ipv6.Address',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The IPv6 address on the interface.
                ''',
                'ip',
                'ietf-ip', True),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                The length of the subnet prefix.
                ''',
                'prefix_length',
                'ietf-ip', False),
            ],
            'ietf-ip',
            'address',
            _yang_ns._namespaces['ietf-ip'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.Ipv6.Neighbor' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Ipv6.Neighbor',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The IPv6 address of the neighbor node.
                ''',
                'ip',
                'ietf-ip', True),
            _MetaInfoClassMember('link-layer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                The link-layer address of the neighbor node.
                ''',
                'link_layer_address',
                'ietf-ip', False),
            ],
            'ietf-ip',
            'neighbor',
            _yang_ns._namespaces['ietf-ip'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.Ipv6.Autoconf' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Ipv6.Autoconf',
            False, 
            [
            _MetaInfoClassMember('create-global-addresses', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If enabled, the host creates global addresses as
                described in RFC 4862.
                ''',
                'create_global_addresses',
                'ietf-ip', False),
            _MetaInfoClassMember('create-temporary-addresses', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If enabled, the host creates temporary addresses as
                described in RFC 4941.
                ''',
                'create_temporary_addresses',
                'ietf-ip', False),
            _MetaInfoClassMember('temporary-preferred-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time period during which the temporary address is
                preferred.
                ''',
                'temporary_preferred_lifetime',
                'ietf-ip', False),
            _MetaInfoClassMember('temporary-valid-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time period during which the temporary address
                is valid.
                ''',
                'temporary_valid_lifetime',
                'ietf-ip', False),
            ],
            'ietf-ip',
            'autoconf',
            _yang_ns._namespaces['ietf-ip'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList.Prefix' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList.Prefix',
            False, 
            [
            _MetaInfoClassMember('prefix-spec', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                IPv6 address prefix.
                ''',
                'prefix_spec',
                'ietf-ipv6-unicast-routing', True),
            _MetaInfoClassMember('autonomous-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The value to be placed in the Autonomous Flag
                field in the Prefix Information option.
                ''',
                'autonomous_flag',
                'ietf-ipv6-unicast-routing', False),
            _MetaInfoClassMember('no-advertise', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The prefix will not be advertised.
                
                This can be used for removing the prefix from the
                default set of advertised prefixes.
                ''',
                'no_advertise',
                'ietf-ipv6-unicast-routing', False),
            _MetaInfoClassMember('on-link-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The value to be placed in the on-link flag
                ('L-bit') field in the Prefix Information
                option.
                ''',
                'on_link_flag',
                'ietf-ipv6-unicast-routing', False),
            _MetaInfoClassMember('preferred-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value to be placed in the Preferred Lifetime
                in the Prefix Information option. The designated
                value of all 1's (0xffffffff) represents
                infinity.
                ''',
                'preferred_lifetime',
                'ietf-ipv6-unicast-routing', False),
            _MetaInfoClassMember('valid-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value to be placed in the Valid Lifetime in
                the Prefix Information option. The designated
                value of all 1's (0xffffffff) represents
                infinity.
                ''',
                'valid_lifetime',
                'ietf-ipv6-unicast-routing', False),
            ],
            'ietf-ipv6-unicast-routing',
            'prefix',
            _yang_ns._namespaces['ietf-ipv6-unicast-routing'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_LIST, 'Prefix' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList.Prefix', 
                [], [], 
                '''                Configuration of an advertised prefix entry.
                ''',
                'prefix',
                'ietf-ipv6-unicast-routing', False),
            ],
            'ietf-ipv6-unicast-routing',
            'prefix-list',
            _yang_ns._namespaces['ietf-ipv6-unicast-routing'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements',
            False, 
            [
            _MetaInfoClassMember('cur-hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The value to be placed in the Cur Hop Limit field in the
                Router Advertisement messages sent by the router. A value
                of zero means unspecified (by this router).
                
                If this parameter is not configured, the device SHOULD use
                the value specified in IANA Assigned Numbers that was in
                effect at the time of implementation.
                ''',
                'cur_hop_limit',
                'ietf-ipv6-unicast-routing', False),
            _MetaInfoClassMember('default-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '9000')], [], 
                '''                The value to be placed in the Router Lifetime field of
                Router Advertisements sent from the interface, in seconds.
                It MUST be either zero or between max-rtr-adv-interval and
                9000 seconds. A value of zero indicates that the router is
                not to be used as a default router. These limits may be
                overridden by specific documents that describe how IPv6
                operates over different link layers.
                
                If this parameter is not configured, the device SHOULD use
                a value of 3 * max-rtr-adv-interval.
                ''',
                'default_lifetime',
                'ietf-ipv6-unicast-routing', False),
            _MetaInfoClassMember('link-mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value to be placed in MTU options sent by the router.
                A value of zero indicates that no MTU options are sent.
                ''',
                'link_mtu',
                'ietf-ipv6-unicast-routing', False),
            _MetaInfoClassMember('managed-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The value to be placed in the 'Managed address
                configuration' flag field in the Router Advertisement.
                ''',
                'managed_flag',
                'ietf-ipv6-unicast-routing', False),
            _MetaInfoClassMember('max-rtr-adv-interval', ATTRIBUTE, 'int' , None, None, 
                [('4', '1800')], [], 
                '''                The maximum time allowed between sending unsolicited
                multicast Router Advertisements from the interface.
                ''',
                'max_rtr_adv_interval',
                'ietf-ipv6-unicast-routing', False),
            _MetaInfoClassMember('min-rtr-adv-interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '1350')], [], 
                '''                The minimum time allowed between sending unsolicited
                multicast Router Advertisements from the interface.
                
                The default value to be used operationally if this leaf is
                not configured is determined as follows:
                
                - if max-rtr-adv-interval >= 9 seconds, the default value
                  is 0.33 * max-rtr-adv-interval;
                
                - otherwise it is 0.75 * max-rtr-adv-interval.
                ''',
                'min_rtr_adv_interval',
                'ietf-ipv6-unicast-routing', False),
            _MetaInfoClassMember('other-config-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The value to be placed in the 'Other configuration' flag
                field in the Router Advertisement.
                ''',
                'other_config_flag',
                'ietf-ipv6-unicast-routing', False),
            _MetaInfoClassMember('prefix-list', REFERENCE_CLASS, 'PrefixList' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList', 
                [], [], 
                '''                Configuration of prefixes to be placed in Prefix
                Information options in Router Advertisement messages sent
                from the interface.
                
                Prefixes that are advertised by default but do not have
                their entries in the child 'prefix' list are advertised
                with the default values of all parameters.
                
                The link-local prefix SHOULD NOT be included in the list
                of advertised prefixes.
                ''',
                'prefix_list',
                'ietf-ipv6-unicast-routing', False),
            _MetaInfoClassMember('reachable-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600000')], [], 
                '''                The value to be placed in the Reachable Time field in the
                Router Advertisement messages sent by the router. A value
                of zero means unspecified (by this router).
                ''',
                'reachable_time',
                'ietf-ipv6-unicast-routing', False),
            _MetaInfoClassMember('retrans-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value to be placed in the Retrans Timer field in the
                Router Advertisement messages sent by the router. A value
                of zero means unspecified (by this router).
                ''',
                'retrans_timer',
                'ietf-ipv6-unicast-routing', False),
            _MetaInfoClassMember('send-advertisements', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A flag indicating whether or not the router sends periodic
                Router Advertisements and responds to Router
                Solicitations.
                ''',
                'send_advertisements',
                'ietf-ipv6-unicast-routing', False),
            ],
            'ietf-ipv6-unicast-routing',
            'ipv6-router-advertisements',
            _yang_ns._namespaces['ietf-ipv6-unicast-routing'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.Ipv6' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Ipv6',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.Ipv6.Address', 
                [], [], 
                '''                The list of configured IPv6 addresses on the interface.
                ''',
                'address',
                'ietf-ip', False),
            _MetaInfoClassMember('autoconf', REFERENCE_CLASS, 'Autoconf' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.Ipv6.Autoconf', 
                [], [], 
                '''                Parameters to control the autoconfiguration of IPv6
                addresses, as described in RFC 4862.
                ''',
                'autoconf',
                'ietf-ip', False),
            _MetaInfoClassMember('dup-addr-detect-transmits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of consecutive Neighbor Solicitation messages
                sent while performing Duplicate Address Detection on a
                tentative address.  A value of zero indicates that
                Duplicate Address Detection is not performed on
                tentative addresses.  A value of one indicates a single
                transmission with no follow-up retransmissions.
                ''',
                'dup_addr_detect_transmits',
                'ietf-ip', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Controls whether IPv6 is enabled or disabled on this
                interface.  When IPv6 is enabled, this interface is
                connected to an IPv6 stack, and the interface can send
                and receive IPv6 packets.
                ''',
                'enabled',
                'ietf-ip', False),
            _MetaInfoClassMember('forwarding', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Controls IPv6 packet forwarding of datagrams received by,
                but not addressed to, this interface.  IPv6 routers
                forward datagrams.  IPv6 hosts do not (except those
                source-routed via the host).
                ''',
                'forwarding',
                'ietf-ip', False),
            _MetaInfoClassMember('ipv6-router-advertisements', REFERENCE_CLASS, 'Ipv6RouterAdvertisements' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements', 
                [], [], 
                '''                Configuration of IPv6 Router Advertisements.
                ''',
                'ipv6_router_advertisements',
                'ietf-ipv6-unicast-routing', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('1280', '4294967295')], [], 
                '''                The size, in octets, of the largest IPv6 packet that the
                interface will send and receive.
                The server may restrict the allowed values for this leaf,
                depending on the interface's type.
                If this leaf is not configured, the operationally used MTU
                depends on the interface's type.
                ''',
                'mtu',
                'ietf-ip', False),
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.Ipv6.Neighbor', 
                [], [], 
                '''                A list of mappings from IPv6 addresses to
                link-layer addresses.
                Entries in this list are used as static entries in the
                Neighbor Cache.
                ''',
                'neighbor',
                'ietf-ip', False),
            ],
            'ietf-ip',
            'ipv6',
            _yang_ns._namespaces['ietf-ip'],
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
            _MetaInfoClassMember('diffserv-target-entry', REFERENCE_LIST, 'DiffservTargetEntry' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.DiffservTargetEntry', 
                [], [], 
                '''                policy target for inbound or outbound direction
                ''',
                'diffserv_target_entry',
                'ietf-diffserv-target', False),
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
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.Ipv4', 
                [], [], 
                '''                Parameters for the IPv4 address family.
                ''',
                'ipv4',
                'ietf-ip', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.Ipv6', 
                [], [], 
                '''                Parameters for the IPv6 address family.
                ''',
                'ipv6',
                'ietf-ip', False),
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
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
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
    'InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics' : {
        'meta_info' : _MetaInfoClass('InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics',
            False, 
            [
            _MetaInfoClassMember('classified-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                 Number of total bytes which filtered 
                 to the classifier-entry
                ''',
                'classified_bytes',
                'ietf-diffserv-target', False),
            _MetaInfoClassMember('classified-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                 Number of total packets which filtered
                 to the classifier-entry
                ''',
                'classified_pkts',
                'ietf-diffserv-target', False),
            _MetaInfoClassMember('classified-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                 Rate of average data flow through the 
                 classifier-entry
                ''',
                'classified_rate',
                'ietf-diffserv-target', False),
            ],
            'ietf-diffserv-target',
            'classifier-entry-statistics',
            _yang_ns._namespaces['ietf-diffserv-target'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics' : {
        'meta_info' : _MetaInfoClass('InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics',
            False, 
            [
            _MetaInfoClassMember('meter-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Meter Identifier
                ''',
                'meter_id',
                'ietf-diffserv-target', True),
            _MetaInfoClassMember('meter-failed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes of packets which failed the meter
                ''',
                'meter_failed_bytes',
                'ietf-diffserv-target', False),
            _MetaInfoClassMember('meter-failed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets which failed the meter
                ''',
                'meter_failed_pkts',
                'ietf-diffserv-target', False),
            _MetaInfoClassMember('meter-succeed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes of packets which succeed the meter
                ''',
                'meter_succeed_bytes',
                'ietf-diffserv-target', False),
            _MetaInfoClassMember('meter-succeed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets which succeed the meter
                ''',
                'meter_succeed_pkts',
                'ietf-diffserv-target', False),
            ],
            'ietf-diffserv-target',
            'meter-statistics',
            _yang_ns._namespaces['ietf-diffserv-target'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats' : {
        'meta_info' : _MetaInfoClass('InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats',
            False, 
            [
            _MetaInfoClassMember('early-drop-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Early drop bytes 
                ''',
                'early_drop_bytes',
                'ietf-diffserv-target', False),
            _MetaInfoClassMember('early-drop-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Early drop packets 
                ''',
                'early_drop_pkts',
                'ietf-diffserv-target', False),
            ],
            'ietf-diffserv-target',
            'wred-stats',
            _yang_ns._namespaces['ietf-diffserv-target'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics' : {
        'meta_info' : _MetaInfoClass('InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics',
            False, 
            [
            _MetaInfoClassMember('drop-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of bytes dropped 
                ''',
                'drop_bytes',
                'ietf-diffserv-target', False),
            _MetaInfoClassMember('drop-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of packets dropped 
                ''',
                'drop_pkts',
                'ietf-diffserv-target', False),
            _MetaInfoClassMember('output-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of bytes transmitted from queue 
                ''',
                'output_bytes',
                'ietf-diffserv-target', False),
            _MetaInfoClassMember('output-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets transmitted from queue 
                ''',
                'output_pkts',
                'ietf-diffserv-target', False),
            _MetaInfoClassMember('queue-size-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of bytes currently buffered 
                ''',
                'queue_size_bytes',
                'ietf-diffserv-target', False),
            _MetaInfoClassMember('queue-size-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets currently buffered 
                ''',
                'queue_size_pkts',
                'ietf-diffserv-target', False),
            _MetaInfoClassMember('wred-stats', REFERENCE_CLASS, 'WredStats' , 'ydk.models.ietf.ietf_interfaces', 'InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats', 
                [], [], 
                '''                Container for WRED statistics
                ''',
                'wred_stats',
                'ietf-diffserv-target', False),
            ],
            'ietf-diffserv-target',
            'queuing-statistics',
            _yang_ns._namespaces['ietf-diffserv-target'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics' : {
        'meta_info' : _MetaInfoClass('InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics',
            False, 
            [
            _MetaInfoClassMember('classifier-entry-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Classifier Entry Name
                ''',
                'classifier_entry_name',
                'ietf-diffserv-target', True),
            _MetaInfoClassMember('parent-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Path of the Classifier Entry in a hierarchial policy 
                ''',
                'parent_path',
                'ietf-diffserv-target', True),
            _MetaInfoClassMember('classifier-entry-statistics', REFERENCE_CLASS, 'ClassifierEntryStatistics' , 'ydk.models.ietf.ietf_interfaces', 'InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics', 
                [], [], 
                '''                
                This group defines the classifier filter statistics of 
                each classifier entry
                       
                
                ''',
                'classifier_entry_statistics',
                'ietf-diffserv-target', False),
            _MetaInfoClassMember('meter-statistics', REFERENCE_LIST, 'MeterStatistics' , 'ydk.models.ietf.ietf_interfaces', 'InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics', 
                [], [], 
                '''                Meter statistics
                ''',
                'meter_statistics',
                'ietf-diffserv-target', False),
            _MetaInfoClassMember('queuing-statistics', REFERENCE_CLASS, 'QueuingStatistics' , 'ydk.models.ietf.ietf_interfaces', 'InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics', 
                [], [], 
                '''                queue related statistics 
                ''',
                'queuing_statistics',
                'ietf-diffserv-target', False),
            ],
            'ietf-diffserv-target',
            'diffserv-target-classifier-statistics',
            _yang_ns._namespaces['ietf-diffserv-target'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'InterfacesState.Interface.DiffservTargetEntry' : {
        'meta_info' : _MetaInfoClass('InterfacesState.Interface.DiffservTargetEntry',
            False, 
            [
            _MetaInfoClassMember('direction', REFERENCE_IDENTITY_CLASS, 'DirectionIdentity' , 'ydk.models.ietf.ietf_diffserv_target', 'DirectionIdentity', 
                [], [], 
                '''                Direction fo the traffic flow either inbound or outbound
                ''',
                'direction',
                'ietf-diffserv-target', True),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy entry name
                ''',
                'policy_name',
                'ietf-diffserv-target', True),
            _MetaInfoClassMember('diffserv-target-classifier-statistics', REFERENCE_LIST, 'DiffservTargetClassifierStatistics' , 'ydk.models.ietf.ietf_interfaces', 'InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics', 
                [], [], 
                '''                Statistics for each Classifier Entry in a Policy
                ''',
                'diffserv_target_classifier_statistics',
                'ietf-diffserv-target', False),
            ],
            'ietf-diffserv-target',
            'diffserv-target-entry',
            _yang_ns._namespaces['ietf-diffserv-target'],
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
    'InterfacesState.Interface.Ipv4.Address' : {
        'meta_info' : _MetaInfoClass('InterfacesState.Interface.Ipv4.Address',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IPv4 address on the interface.
                ''',
                'ip',
                'ietf-ip', True),
            _MetaInfoClassMember('netmask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                The subnet specified as a netmask.
                ''',
                'netmask',
                'ietf-ip', False),
            _MetaInfoClassMember('origin', REFERENCE_ENUM_CLASS, 'IpAddressOriginEnum' , 'ydk.models.ietf.ietf_ip', 'IpAddressOriginEnum', 
                [], [], 
                '''                The origin of this address.
                ''',
                'origin',
                'ietf-ip', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                The length of the subnet prefix.
                ''',
                'prefix_length',
                'ietf-ip', False),
            ],
            'ietf-ip',
            'address',
            _yang_ns._namespaces['ietf-ip'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'InterfacesState.Interface.Ipv4.Neighbor' : {
        'meta_info' : _MetaInfoClass('InterfacesState.Interface.Ipv4.Neighbor',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IPv4 address of the neighbor node.
                ''',
                'ip',
                'ietf-ip', True),
            _MetaInfoClassMember('link-layer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                The link-layer address of the neighbor node.
                ''',
                'link_layer_address',
                'ietf-ip', False),
            _MetaInfoClassMember('origin', REFERENCE_ENUM_CLASS, 'NeighborOriginEnum' , 'ydk.models.ietf.ietf_ip', 'NeighborOriginEnum', 
                [], [], 
                '''                The origin of this neighbor entry.
                ''',
                'origin',
                'ietf-ip', False),
            ],
            'ietf-ip',
            'neighbor',
            _yang_ns._namespaces['ietf-ip'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'InterfacesState.Interface.Ipv4' : {
        'meta_info' : _MetaInfoClass('InterfacesState.Interface.Ipv4',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address' , 'ydk.models.ietf.ietf_interfaces', 'InterfacesState.Interface.Ipv4.Address', 
                [], [], 
                '''                The list of IPv4 addresses on the interface.
                ''',
                'address',
                'ietf-ip', False),
            _MetaInfoClassMember('forwarding', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether IPv4 packet forwarding is enabled or
                disabled on this interface.
                ''',
                'forwarding',
                'ietf-ip', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('68', '65535')], [], 
                '''                The size, in octets, of the largest IPv4 packet that the
                interface will send and receive.
                ''',
                'mtu',
                'ietf-ip', False),
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.ietf.ietf_interfaces', 'InterfacesState.Interface.Ipv4.Neighbor', 
                [], [], 
                '''                A list of mappings from IPv4 addresses to
                link-layer addresses.
                This list represents the ARP Cache.
                ''',
                'neighbor',
                'ietf-ip', False),
            ],
            'ietf-ip',
            'ipv4',
            _yang_ns._namespaces['ietf-ip'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'InterfacesState.Interface.Ipv6.Address.StatusEnum' : _MetaInfoEnum('StatusEnum', 'ydk.models.ietf.ietf_interfaces',
        {
            'preferred':'preferred',
            'deprecated':'deprecated',
            'invalid':'invalid',
            'inaccessible':'inaccessible',
            'unknown':'unknown',
            'tentative':'tentative',
            'duplicate':'duplicate',
            'optimistic':'optimistic',
        }, 'ietf-ip', _yang_ns._namespaces['ietf-ip']),
    'InterfacesState.Interface.Ipv6.Address' : {
        'meta_info' : _MetaInfoClass('InterfacesState.Interface.Ipv6.Address',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The IPv6 address on the interface.
                ''',
                'ip',
                'ietf-ip', True),
            _MetaInfoClassMember('origin', REFERENCE_ENUM_CLASS, 'IpAddressOriginEnum' , 'ydk.models.ietf.ietf_ip', 'IpAddressOriginEnum', 
                [], [], 
                '''                The origin of this address.
                ''',
                'origin',
                'ietf-ip', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                The length of the subnet prefix.
                ''',
                'prefix_length',
                'ietf-ip', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'StatusEnum' , 'ydk.models.ietf.ietf_interfaces', 'InterfacesState.Interface.Ipv6.Address.StatusEnum', 
                [], [], 
                '''                The status of an address.  Most of the states correspond
                to states from the IPv6 Stateless Address
                Autoconfiguration protocol.
                ''',
                'status',
                'ietf-ip', False),
            ],
            'ietf-ip',
            'address',
            _yang_ns._namespaces['ietf-ip'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'InterfacesState.Interface.Ipv6.Neighbor.StateEnum' : _MetaInfoEnum('StateEnum', 'ydk.models.ietf.ietf_interfaces',
        {
            'incomplete':'incomplete',
            'reachable':'reachable',
            'stale':'stale',
            'delay':'delay',
            'probe':'probe',
        }, 'ietf-ip', _yang_ns._namespaces['ietf-ip']),
    'InterfacesState.Interface.Ipv6.Neighbor' : {
        'meta_info' : _MetaInfoClass('InterfacesState.Interface.Ipv6.Neighbor',
            False, 
            [
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The IPv6 address of the neighbor node.
                ''',
                'ip',
                'ietf-ip', True),
            _MetaInfoClassMember('is-router', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Indicates that the neighbor node acts as a router.
                ''',
                'is_router',
                'ietf-ip', False),
            _MetaInfoClassMember('link-layer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                The link-layer address of the neighbor node.
                ''',
                'link_layer_address',
                'ietf-ip', False),
            _MetaInfoClassMember('origin', REFERENCE_ENUM_CLASS, 'NeighborOriginEnum' , 'ydk.models.ietf.ietf_ip', 'NeighborOriginEnum', 
                [], [], 
                '''                The origin of this neighbor entry.
                ''',
                'origin',
                'ietf-ip', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'StateEnum' , 'ydk.models.ietf.ietf_interfaces', 'InterfacesState.Interface.Ipv6.Neighbor.StateEnum', 
                [], [], 
                '''                The Neighbor Unreachability Detection state of this
                entry.
                ''',
                'state',
                'ietf-ip', False),
            ],
            'ietf-ip',
            'neighbor',
            _yang_ns._namespaces['ietf-ip'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'InterfacesState.Interface.Ipv6' : {
        'meta_info' : _MetaInfoClass('InterfacesState.Interface.Ipv6',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address' , 'ydk.models.ietf.ietf_interfaces', 'InterfacesState.Interface.Ipv6.Address', 
                [], [], 
                '''                The list of IPv6 addresses on the interface.
                ''',
                'address',
                'ietf-ip', False),
            _MetaInfoClassMember('forwarding', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether IPv6 packet forwarding is enabled or
                disabled on this interface.
                ''',
                'forwarding',
                'ietf-ip', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('1280', '4294967295')], [], 
                '''                The size, in octets, of the largest IPv6 packet that the
                interface will send and receive.
                ''',
                'mtu',
                'ietf-ip', False),
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.ietf.ietf_interfaces', 'InterfacesState.Interface.Ipv6.Neighbor', 
                [], [], 
                '''                A list of mappings from IPv6 addresses to
                link-layer addresses.
                This list represents the Neighbor Cache.
                ''',
                'neighbor',
                'ietf-ip', False),
            ],
            'ietf-ip',
            'ipv6',
            _yang_ns._namespaces['ietf-ip'],
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
            _MetaInfoClassMember('diffserv-target-entry', REFERENCE_LIST, 'DiffservTargetEntry' , 'ydk.models.ietf.ietf_interfaces', 'InterfacesState.Interface.DiffservTargetEntry', 
                [], [], 
                '''                policy target for inbound or outbound direction
                ''',
                'diffserv_target_entry',
                'ietf-diffserv-target', False),
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
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.ietf.ietf_interfaces', 'InterfacesState.Interface.Ipv4', 
                [], [], 
                '''                Interface-specific parameters for the IPv4 address family.
                ''',
                'ipv4',
                'ietf-ip', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.ietf.ietf_interfaces', 'InterfacesState.Interface.Ipv6', 
                [], [], 
                '''                Parameters for the IPv6 address family.
                ''',
                'ipv6',
                'ietf-ip', False),
            _MetaInfoClassMember('last-change', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
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
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
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
            _MetaInfoClassMember('routing-instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the routing instance to which the interface is
                assigned.
                ''',
                'routing_instance',
                'ietf-routing', False),
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
_meta_table['Interfaces.Interface.Ipv4.Address']['meta_info'].parent =_meta_table['Interfaces.Interface.Ipv4']['meta_info']
_meta_table['Interfaces.Interface.Ipv4.Neighbor']['meta_info'].parent =_meta_table['Interfaces.Interface.Ipv4']['meta_info']
_meta_table['Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList.Prefix']['meta_info'].parent =_meta_table['Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList']['meta_info']
_meta_table['Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList']['meta_info'].parent =_meta_table['Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements']['meta_info']
_meta_table['Interfaces.Interface.Ipv6.Address']['meta_info'].parent =_meta_table['Interfaces.Interface.Ipv6']['meta_info']
_meta_table['Interfaces.Interface.Ipv6.Neighbor']['meta_info'].parent =_meta_table['Interfaces.Interface.Ipv6']['meta_info']
_meta_table['Interfaces.Interface.Ipv6.Autoconf']['meta_info'].parent =_meta_table['Interfaces.Interface.Ipv6']['meta_info']
_meta_table['Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements']['meta_info'].parent =_meta_table['Interfaces.Interface.Ipv6']['meta_info']
_meta_table['Interfaces.Interface.DiffservTargetEntry']['meta_info'].parent =_meta_table['Interfaces.Interface']['meta_info']
_meta_table['Interfaces.Interface.Ipv4']['meta_info'].parent =_meta_table['Interfaces.Interface']['meta_info']
_meta_table['Interfaces.Interface.Ipv6']['meta_info'].parent =_meta_table['Interfaces.Interface']['meta_info']
_meta_table['Interfaces.Interface']['meta_info'].parent =_meta_table['Interfaces']['meta_info']
_meta_table['InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats']['meta_info'].parent =_meta_table['InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics']['meta_info']
_meta_table['InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics']['meta_info'].parent =_meta_table['InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics']['meta_info']
_meta_table['InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics']['meta_info'].parent =_meta_table['InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics']['meta_info']
_meta_table['InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics']['meta_info'].parent =_meta_table['InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics']['meta_info']
_meta_table['InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics']['meta_info'].parent =_meta_table['InterfacesState.Interface.DiffservTargetEntry']['meta_info']
_meta_table['InterfacesState.Interface.Ipv4.Address']['meta_info'].parent =_meta_table['InterfacesState.Interface.Ipv4']['meta_info']
_meta_table['InterfacesState.Interface.Ipv4.Neighbor']['meta_info'].parent =_meta_table['InterfacesState.Interface.Ipv4']['meta_info']
_meta_table['InterfacesState.Interface.Ipv6.Address']['meta_info'].parent =_meta_table['InterfacesState.Interface.Ipv6']['meta_info']
_meta_table['InterfacesState.Interface.Ipv6.Neighbor']['meta_info'].parent =_meta_table['InterfacesState.Interface.Ipv6']['meta_info']
_meta_table['InterfacesState.Interface.Statistics']['meta_info'].parent =_meta_table['InterfacesState.Interface']['meta_info']
_meta_table['InterfacesState.Interface.DiffservTargetEntry']['meta_info'].parent =_meta_table['InterfacesState.Interface']['meta_info']
_meta_table['InterfacesState.Interface.Bandwidth']['meta_info'].parent =_meta_table['InterfacesState.Interface']['meta_info']
_meta_table['InterfacesState.Interface.Ipv4']['meta_info'].parent =_meta_table['InterfacesState.Interface']['meta_info']
_meta_table['InterfacesState.Interface.Ipv6']['meta_info'].parent =_meta_table['InterfacesState.Interface']['meta_info']
_meta_table['InterfacesState.Interface']['meta_info'].parent =_meta_table['InterfacesState']['meta_info']

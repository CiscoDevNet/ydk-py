


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AuthenticationMethodIdentity' : {
        'meta_info' : _MetaInfoClass('AuthenticationMethodIdentity',
            False, 
            [
            ],
            'ietf-system',
            'authentication-method',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'RadiusAuthenticationTypeIdentity' : {
        'meta_info' : _MetaInfoClass('RadiusAuthenticationTypeIdentity',
            False, 
            [
            ],
            'ietf-system',
            'radius-authentication-type',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'System.Clock' : {
        'meta_info' : _MetaInfoClass('System.Clock',
            False, 
            [
            _MetaInfoClassMember('timezone-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The TZ database name to use for the system, such
                as 'Europe/Stockholm'.
                ''',
                'timezone_name',
                'ietf-system', False),
            _MetaInfoClassMember('timezone-utc-offset', ATTRIBUTE, 'int' , None, None, 
                [('-1500', '1500')], [], 
                '''                The number of minutes to add to UTC time to
                identify the time zone for this system.  For example,
                'UTC - 8:00 hours' would be represented as '-480'.
                Note that automatic daylight saving time adjustment
                is not provided if this object is used.
                ''',
                'timezone_utc_offset',
                'ietf-system', False),
            ],
            'ietf-system',
            'clock',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'System.Ntp.Server.Udp' : {
        'meta_info' : _MetaInfoClass('System.Ntp.Server.Udp',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The address of the NTP server.
                ''',
                'address',
                'ietf-system', False, [
                    _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                        [], [], 
                        '''                        The address of the NTP server.
                        ''',
                        'address',
                        'ietf-system', False, [
                            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                                '''                                The address of the NTP server.
                                ''',
                                'address',
                                'ietf-system', False),
                            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                                '''                                The address of the NTP server.
                                ''',
                                'address',
                                'ietf-system', False),
                        ]),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.'], 
                        '''                        The address of the NTP server.
                        ''',
                        'address',
                        'ietf-system', False),
                ]),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The port number of the NTP server.
                ''',
                'port',
                'ietf-system', False),
            ],
            'ietf-system',
            'udp',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'System.Ntp.Server.AssociationTypeEnum' : _MetaInfoEnum('AssociationTypeEnum', 'ydk.models.ietf.ietf_system',
        {
            'server':'server',
            'peer':'peer',
            'pool':'pool',
        }, 'ietf-system', _yang_ns._namespaces['ietf-system']),
    'System.Ntp.Server' : {
        'meta_info' : _MetaInfoClass('System.Ntp.Server',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                An arbitrary name for the NTP server.
                ''',
                'name',
                'ietf-system', True),
            _MetaInfoClassMember('association-type', REFERENCE_ENUM_CLASS, 'AssociationTypeEnum' , 'ydk.models.ietf.ietf_system', 'System.Ntp.Server.AssociationTypeEnum', 
                [], [], 
                '''                The desired association type for this NTP server.
                ''',
                'association_type',
                'ietf-system', False),
            _MetaInfoClassMember('iburst', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether this server should enable burst
                synchronization or not.
                ''',
                'iburst',
                'ietf-system', False),
            _MetaInfoClassMember('prefer', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether this server should be preferred
                or not.
                ''',
                'prefer',
                'ietf-system', False),
            _MetaInfoClassMember('udp', REFERENCE_CLASS, 'Udp' , 'ydk.models.ietf.ietf_system', 'System.Ntp.Server.Udp', 
                [], [], 
                '''                Contains UDP-specific configuration parameters
                for NTP.
                ''',
                'udp',
                'ietf-system', False),
            ],
            'ietf-system',
            'server',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'System.Ntp' : {
        'meta_info' : _MetaInfoClass('System.Ntp',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates that the system should attempt to
                synchronize the system clock with an NTP server
                from the 'ntp/server' list.
                ''',
                'enabled',
                'ietf-system', False),
            _MetaInfoClassMember('server', REFERENCE_LIST, 'Server' , 'ydk.models.ietf.ietf_system', 'System.Ntp.Server', 
                [], [], 
                '''                List of NTP servers to use for system clock
                synchronization.  If '/system/ntp/enabled'
                is 'true', then the system will attempt to
                contact and utilize the specified NTP servers.
                ''',
                'server',
                'ietf-system', False),
            ],
            'ietf-system',
            'ntp',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'System.DnsResolver.Server.UdpAndTcp' : {
        'meta_info' : _MetaInfoClass('System.DnsResolver.Server.UdpAndTcp',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The address of the DNS server.
                ''',
                'address',
                'ietf-system', False, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The address of the DNS server.
                        ''',
                        'address',
                        'ietf-system', False),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The address of the DNS server.
                        ''',
                        'address',
                        'ietf-system', False),
                ]),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The UDP and TCP port number of the DNS server.
                ''',
                'port',
                'ietf-system', False),
            ],
            'ietf-system',
            'udp-and-tcp',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'System.DnsResolver.Server' : {
        'meta_info' : _MetaInfoClass('System.DnsResolver.Server',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                An arbitrary name for the DNS server.
                ''',
                'name',
                'ietf-system', True),
            _MetaInfoClassMember('udp-and-tcp', REFERENCE_CLASS, 'UdpAndTcp' , 'ydk.models.ietf.ietf_system', 'System.DnsResolver.Server.UdpAndTcp', 
                [], [], 
                '''                Contains UDP- and TCP-specific configuration
                parameters for DNS.
                ''',
                'udp_and_tcp',
                'ietf-system', False),
            ],
            'ietf-system',
            'server',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'System.DnsResolver.Options' : {
        'meta_info' : _MetaInfoClass('System.DnsResolver.Options',
            False, 
            [
            _MetaInfoClassMember('attempts', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                The number of times the resolver will send a query to
                all of its name servers before giving up and returning
                an error to the calling application.
                ''',
                'attempts',
                'ietf-system', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                The amount of time the resolver will wait for a
                response from each remote name server before
                retrying the query via a different name server.
                ''',
                'timeout',
                'ietf-system', False),
            ],
            'ietf-system',
            'options',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'System.DnsResolver' : {
        'meta_info' : _MetaInfoClass('System.DnsResolver',
            False, 
            [
            _MetaInfoClassMember('options', REFERENCE_CLASS, 'Options' , 'ydk.models.ietf.ietf_system', 'System.DnsResolver.Options', 
                [], [], 
                '''                Resolver options.  The set of available options has been
                limited to those that are generally available across
                different resolver implementations and generally useful.
                ''',
                'options',
                'ietf-system', False),
            _MetaInfoClassMember('search', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.'], 
                '''                An ordered list of domains to search when resolving
                a host name.
                ''',
                'search',
                'ietf-system', False),
            _MetaInfoClassMember('server', REFERENCE_LIST, 'Server' , 'ydk.models.ietf.ietf_system', 'System.DnsResolver.Server', 
                [], [], 
                '''                List of the DNS servers that the resolver should query.
                When the resolver is invoked by a calling application, it
                sends the query to the first name server in this list.  If
                no response has been received within 'timeout' seconds,
                the resolver continues with the next server in the list.
                If no response is received from any server, the resolver
                continues with the first server again.  When the resolver
                has traversed the list 'attempts' times without receiving
                any response, it gives up and returns an error to the
                calling application.
                Implementations MAY limit the number of entries in this
                list.
                ''',
                'server',
                'ietf-system', False),
            ],
            'ietf-system',
            'dns-resolver',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'System.Radius.Server.Udp' : {
        'meta_info' : _MetaInfoClass('System.Radius.Server.Udp',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The address of the RADIUS server.
                ''',
                'address',
                'ietf-system', False, [
                    _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                        [], [], 
                        '''                        The address of the RADIUS server.
                        ''',
                        'address',
                        'ietf-system', False, [
                            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                                '''                                The address of the RADIUS server.
                                ''',
                                'address',
                                'ietf-system', False),
                            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                                '''                                The address of the RADIUS server.
                                ''',
                                'address',
                                'ietf-system', False),
                        ]),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.'], 
                        '''                        The address of the RADIUS server.
                        ''',
                        'address',
                        'ietf-system', False),
                ]),
            _MetaInfoClassMember('authentication-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The port number of the RADIUS server.
                ''',
                'authentication_port',
                'ietf-system', False),
            _MetaInfoClassMember('shared-secret', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The shared secret, which is known to both the
                RADIUS client and server.
                ''',
                'shared_secret',
                'ietf-system', False),
            ],
            'ietf-system',
            'udp',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'System.Radius.Server' : {
        'meta_info' : _MetaInfoClass('System.Radius.Server',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                An arbitrary name for the RADIUS server.
                ''',
                'name',
                'ietf-system', True),
            _MetaInfoClassMember('authentication-type', REFERENCE_IDENTITY_CLASS, 'RadiusAuthenticationTypeIdentity' , 'ydk.models.ietf.ietf_system', 'RadiusAuthenticationTypeIdentity', 
                [], [], 
                '''                The authentication type requested from the RADIUS
                server.
                ''',
                'authentication_type',
                'ietf-system', False),
            _MetaInfoClassMember('udp', REFERENCE_CLASS, 'Udp' , 'ydk.models.ietf.ietf_system', 'System.Radius.Server.Udp', 
                [], [], 
                '''                Contains UDP-specific configuration parameters
                for RADIUS.
                ''',
                'udp',
                'ietf-system', False),
            ],
            'ietf-system',
            'server',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'System.Radius.Options' : {
        'meta_info' : _MetaInfoClass('System.Radius.Options',
            False, 
            [
            _MetaInfoClassMember('attempts', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                The number of times the device will send a query to
                all of its RADIUS servers before giving up.
                ''',
                'attempts',
                'ietf-system', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                The number of seconds the device will wait for a
                response from each RADIUS server before trying with a
                different server.
                ''',
                'timeout',
                'ietf-system', False),
            ],
            'ietf-system',
            'options',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'System.Radius' : {
        'meta_info' : _MetaInfoClass('System.Radius',
            False, 
            [
            _MetaInfoClassMember('options', REFERENCE_CLASS, 'Options' , 'ydk.models.ietf.ietf_system', 'System.Radius.Options', 
                [], [], 
                '''                RADIUS client options.
                ''',
                'options',
                'ietf-system', False),
            _MetaInfoClassMember('server', REFERENCE_LIST, 'Server' , 'ydk.models.ietf.ietf_system', 'System.Radius.Server', 
                [], [], 
                '''                List of RADIUS servers used by the device.
                When the RADIUS client is invoked by a calling
                application, it sends the query to the first server in
                this list.  If no response has been received within
                'timeout' seconds, the client continues with the next
                server in the list.  If no response is received from any
                server, the client continues with the first server again.
                When the client has traversed the list 'attempts' times
                without receiving any response, it gives up and returns an
                error to the calling application.
                ''',
                'server',
                'ietf-system', False),
            ],
            'ietf-system',
            'radius',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'System.Authentication.User.AuthorizedKey' : {
        'meta_info' : _MetaInfoClass('System.Authentication.User.AuthorizedKey',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                An arbitrary name for the SSH key.
                ''',
                'name',
                'ietf-system', True),
            _MetaInfoClassMember('algorithm', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The public key algorithm name for this SSH key.
                Valid values are the values in the IANA 'Secure Shell
                (SSH) Protocol Parameters' registry, Public Key
                Algorithm Names.
                ''',
                'algorithm',
                'ietf-system', False),
            _MetaInfoClassMember('key-data', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The binary public key data for this SSH key, as
                specified by RFC 4253, Section 6.6, i.e.:
                  string    certificate or public key format
                            identifier
                  byte[n]   key/certificate data.
                ''',
                'key_data',
                'ietf-system', False),
            ],
            'ietf-system',
            'authorized-key',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'System.Authentication.User' : {
        'meta_info' : _MetaInfoClass('System.Authentication.User',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The user name string identifying this entry.
                ''',
                'name',
                'ietf-system', True),
            _MetaInfoClassMember('authorized-key', REFERENCE_LIST, 'AuthorizedKey' , 'ydk.models.ietf.ietf_system', 'System.Authentication.User.AuthorizedKey', 
                [], [], 
                '''                A list of public SSH keys for this user.  These keys
                are allowed for SSH authentication, as described in
                RFC 4253.
                ''',
                'authorized_key',
                'ietf-system', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'$0$.*|$1$[a-zA-Z0-9./]{1,8}$[a-zA-Z0-9./]{22}|$5$(rounds=\\d+$)?[a-zA-Z0-9./]{1,16}$[a-zA-Z0-9./]{43}|$6$(rounds=\\d+$)?[a-zA-Z0-9./]{1,16}$[a-zA-Z0-9./]{86}'], 
                '''                The password for this entry.
                ''',
                'password',
                'ietf-system', False),
            ],
            'ietf-system',
            'user',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'System.Authentication' : {
        'meta_info' : _MetaInfoClass('System.Authentication',
            False, 
            [
            _MetaInfoClassMember('user', REFERENCE_LIST, 'User' , 'ydk.models.ietf.ietf_system', 'System.Authentication.User', 
                [], [], 
                '''                The list of local users configured on this device.
                ''',
                'user',
                'ietf-system', False),
            _MetaInfoClassMember('user-authentication-order', REFERENCE_LEAFLIST, 'AuthenticationMethodIdentity' , 'ydk.models.ietf.ietf_system', 'AuthenticationMethodIdentity', 
                [], [], 
                '''                When the device authenticates a user with a password,
                it tries the authentication methods in this leaf-list in
                order.  If authentication with one method fails, the next
                method is used.  If no method succeeds, the user is
                denied access.
                An empty user-authentication-order leaf-list still allows
                authentication of users using mechanisms that do not
                involve a password.
                If the 'radius-authentication' feature is advertised by
                the NETCONF server, the 'radius' identity can be added to
                this list.
                If the 'local-users' feature is advertised by the
                NETCONF server, the 'local-users' identity can be
                added to this list.
                ''',
                'user_authentication_order',
                'ietf-system', False),
            ],
            'ietf-system',
            'authentication',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'System' : {
        'meta_info' : _MetaInfoClass('System',
            False, 
            [
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ietf.ietf_system', 'System.Authentication', 
                [], [], 
                '''                The authentication configuration subtree.
                ''',
                'authentication',
                'ietf-system', False),
            _MetaInfoClassMember('clock', REFERENCE_CLASS, 'Clock' , 'ydk.models.ietf.ietf_system', 'System.Clock', 
                [], [], 
                '''                Configuration of the system date and time properties.
                ''',
                'clock',
                'ietf-system', False),
            _MetaInfoClassMember('contact', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The administrator contact information for the system.
                A server implementation MAY map this leaf to the sysContact
                MIB object.  Such an implementation needs to use some
                mechanism to handle the differences in size and characters
                allowed between this leaf and sysContact.  The definition of
                such a mechanism is outside the scope of this document.
                ''',
                'contact',
                'ietf-system', False),
            _MetaInfoClassMember('dns-resolver', REFERENCE_CLASS, 'DnsResolver' , 'ydk.models.ietf.ietf_system', 'System.DnsResolver', 
                [], [], 
                '''                Configuration of the DNS resolver.
                ''',
                'dns_resolver',
                'ietf-system', False),
            _MetaInfoClassMember('hostname', ATTRIBUTE, 'str' , None, None, 
                [], [b'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.'], 
                '''                The name of the host.  This name can be a single domain
                label or the fully qualified domain name of the host.
                ''',
                'hostname',
                'ietf-system', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The system location.
                A server implementation MAY map this leaf to the sysLocation
                MIB object.  Such an implementation needs to use some
                mechanism to handle the differences in size and characters
                allowed between this leaf and sysLocation.  The definition
                of such a mechanism is outside the scope of this document.
                ''',
                'location',
                'ietf-system', False),
            _MetaInfoClassMember('ntp', REFERENCE_CLASS, 'Ntp' , 'ydk.models.ietf.ietf_system', 'System.Ntp', 
                [], [], 
                '''                Configuration of the NTP client.
                ''',
                'ntp',
                'ietf-system', False),
            _MetaInfoClassMember('radius', REFERENCE_CLASS, 'Radius' , 'ydk.models.ietf.ietf_system', 'System.Radius', 
                [], [], 
                '''                Configuration of the RADIUS client.
                ''',
                'radius',
                'ietf-system', False),
            ],
            'ietf-system',
            'system',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'SystemState.Platform' : {
        'meta_info' : _MetaInfoClass('SystemState.Platform',
            False, 
            [
            _MetaInfoClassMember('machine', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A vendor-specific identifier string representing
                the hardware in use.
                ''',
                'machine',
                'ietf-system', False),
            _MetaInfoClassMember('os-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the operating system in use -
                for example, 'Linux'.
                ''',
                'os_name',
                'ietf-system', False),
            _MetaInfoClassMember('os-release', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The current release level of the operating
                system in use.  This string MAY indicate
                the OS source code revision.
                ''',
                'os_release',
                'ietf-system', False),
            _MetaInfoClassMember('os-version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The current version level of the operating
                system in use.  This string MAY indicate
                the specific OS build date and target variant
                information.
                ''',
                'os_version',
                'ietf-system', False),
            ],
            'ietf-system',
            'platform',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'SystemState.Clock' : {
        'meta_info' : _MetaInfoClass('SystemState.Clock',
            False, 
            [
            _MetaInfoClassMember('boot-datetime', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                The system date and time when the system last restarted.
                ''',
                'boot_datetime',
                'ietf-system', False),
            _MetaInfoClassMember('current-datetime', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                The current system date and time.
                ''',
                'current_datetime',
                'ietf-system', False),
            ],
            'ietf-system',
            'clock',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'SystemState' : {
        'meta_info' : _MetaInfoClass('SystemState',
            False, 
            [
            _MetaInfoClassMember('clock', REFERENCE_CLASS, 'Clock' , 'ydk.models.ietf.ietf_system', 'SystemState.Clock', 
                [], [], 
                '''                Monitoring of the system date and time properties.
                ''',
                'clock',
                'ietf-system', False),
            _MetaInfoClassMember('platform', REFERENCE_CLASS, 'Platform' , 'ydk.models.ietf.ietf_system', 'SystemState.Platform', 
                [], [], 
                '''                Contains vendor-specific information for
                identifying the system platform and operating system.
                ''',
                'platform',
                'ietf-system', False),
            ],
            'ietf-system',
            'system-state',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'SetCurrentDatetimeRpc.Input' : {
        'meta_info' : _MetaInfoClass('SetCurrentDatetimeRpc.Input',
            False, 
            [
            _MetaInfoClassMember('current-datetime', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                The current system date and time.
                ''',
                'current_datetime',
                'ietf-system', False),
            ],
            'ietf-system',
            'input',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'SetCurrentDatetimeRpc' : {
        'meta_info' : _MetaInfoClass('SetCurrentDatetimeRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_system', 'SetCurrentDatetimeRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-system', False),
            ],
            'ietf-system',
            'set-current-datetime',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'SystemRestartRpc' : {
        'meta_info' : _MetaInfoClass('SystemRestartRpc',
            False, 
            [
            ],
            'ietf-system',
            'system-restart',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'SystemShutdownRpc' : {
        'meta_info' : _MetaInfoClass('SystemShutdownRpc',
            False, 
            [
            ],
            'ietf-system',
            'system-shutdown',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'LocalUsersIdentity' : {
        'meta_info' : _MetaInfoClass('LocalUsersIdentity',
            False, 
            [
            ],
            'ietf-system',
            'local-users',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'RadiusPapIdentity' : {
        'meta_info' : _MetaInfoClass('RadiusPapIdentity',
            False, 
            [
            ],
            'ietf-system',
            'radius-pap',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'RadiusChapIdentity' : {
        'meta_info' : _MetaInfoClass('RadiusChapIdentity',
            False, 
            [
            ],
            'ietf-system',
            'radius-chap',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
    'RadiusIdentity' : {
        'meta_info' : _MetaInfoClass('RadiusIdentity',
            False, 
            [
            ],
            'ietf-system',
            'radius',
            _yang_ns._namespaces['ietf-system'],
        'ydk.models.ietf.ietf_system'
        ),
    },
}
_meta_table['System.Ntp.Server.Udp']['meta_info'].parent =_meta_table['System.Ntp.Server']['meta_info']
_meta_table['System.Ntp.Server']['meta_info'].parent =_meta_table['System.Ntp']['meta_info']
_meta_table['System.DnsResolver.Server.UdpAndTcp']['meta_info'].parent =_meta_table['System.DnsResolver.Server']['meta_info']
_meta_table['System.DnsResolver.Server']['meta_info'].parent =_meta_table['System.DnsResolver']['meta_info']
_meta_table['System.DnsResolver.Options']['meta_info'].parent =_meta_table['System.DnsResolver']['meta_info']
_meta_table['System.Radius.Server.Udp']['meta_info'].parent =_meta_table['System.Radius.Server']['meta_info']
_meta_table['System.Radius.Server']['meta_info'].parent =_meta_table['System.Radius']['meta_info']
_meta_table['System.Radius.Options']['meta_info'].parent =_meta_table['System.Radius']['meta_info']
_meta_table['System.Authentication.User.AuthorizedKey']['meta_info'].parent =_meta_table['System.Authentication.User']['meta_info']
_meta_table['System.Authentication.User']['meta_info'].parent =_meta_table['System.Authentication']['meta_info']
_meta_table['System.Clock']['meta_info'].parent =_meta_table['System']['meta_info']
_meta_table['System.Ntp']['meta_info'].parent =_meta_table['System']['meta_info']
_meta_table['System.DnsResolver']['meta_info'].parent =_meta_table['System']['meta_info']
_meta_table['System.Radius']['meta_info'].parent =_meta_table['System']['meta_info']
_meta_table['System.Authentication']['meta_info'].parent =_meta_table['System']['meta_info']
_meta_table['SystemState.Platform']['meta_info'].parent =_meta_table['SystemState']['meta_info']
_meta_table['SystemState.Clock']['meta_info'].parent =_meta_table['SystemState']['meta_info']
_meta_table['SetCurrentDatetimeRpc.Input']['meta_info'].parent =_meta_table['SetCurrentDatetimeRpc']['meta_info']

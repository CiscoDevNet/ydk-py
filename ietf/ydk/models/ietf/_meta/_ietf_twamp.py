


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'PaddingFillModeEnum' : _MetaInfoEnum('PaddingFillModeEnum', 'ydk.models.ietf.ietf_twamp',
        {
            'zero':'zero',
            'random':'random',
        }, 'ietf-twamp', _yang_ns._namespaces['ietf-twamp']),
    'ServerCtrlConnectionStateEnum' : _MetaInfoEnum('ServerCtrlConnectionStateEnum', 'ydk.models.ietf.ietf_twamp',
        {
            'active':'active',
            'servwait':'servwait',
        }, 'ietf-twamp', _yang_ns._namespaces['ietf-twamp']),
    'ControlClientConnectionStateEnum' : _MetaInfoEnum('ControlClientConnectionStateEnum', 'ydk.models.ietf.ietf_twamp',
        {
            'active':'active',
            'idle':'idle',
        }, 'ietf-twamp', _yang_ns._namespaces['ietf-twamp']),
    'TestSessionStateEnum' : _MetaInfoEnum('TestSessionStateEnum', 'ydk.models.ietf.ietf_twamp',
        {
            'accepted':'accepted',
            'failed':'failed',
            'internal-error':'internal_error',
            'not-supported':'not_supported',
            'permanent-resource-limit':'permanent_resource_limit',
            'temp-resource-limit':'temp_resource_limit',
        }, 'ietf-twamp', _yang_ns._namespaces['ietf-twamp']),
    'SenderSessionStateEnum' : _MetaInfoEnum('SenderSessionStateEnum', 'ydk.models.ietf.ietf_twamp',
        {
            'active':'active',
            'failure':'failure',
        }, 'ietf-twamp', _yang_ns._namespaces['ietf-twamp']),
    'Twamp.Client.ModePreferenceChain' : {
        'meta_info' : _MetaInfoClass('Twamp.Client.ModePreferenceChain',
            False, 
            [
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Indicates the Control-Client Mode preference priority
                expressed as a 16-bit unsigned integer, where zero is the
                highest priority and subsequent values monotonically
                increasing.
                ''',
                'priority',
                'ietf-twamp', True),
            _MetaInfoClassMember('mode', REFERENCE_BITS, 'TwampModes' , 'ydk.models.ietf.ietf_twamp', 'TwampModes', 
                [], [], 
                '''                The supported TWAMP Mode matching the corresponding
                priority.
                ''',
                'mode',
                'ietf-twamp', False),
            ],
            'ietf-twamp',
            'mode-preference-chain',
            _yang_ns._namespaces['ietf-twamp'],
        'ydk.models.ietf.ietf_twamp'
        ),
    },
    'Twamp.Client.KeyChain' : {
        'meta_info' : _MetaInfoClass('Twamp.Client.KeyChain',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'str' , None, None, 
                [(1, 80)], [], 
                '''                KeyID used for a TWAMP-Control connection. As per
                Section 3.1 of RFC 4656, KeyID is 'a UTF-8 string, up to
                80 octets in length' and is used to select which 'shared
                shared secret the [Control-Client] wishes to use to
                authenticate or encrypt'.
                ''',
                'key_id',
                'ietf-twamp', True),
            _MetaInfoClassMember('secret-key', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The secret key corresponding to the KeyID for this
                TWAMP-Control connection.
                ''',
                'secret_key',
                'ietf-twamp', False),
            ],
            'ietf-twamp',
            'key-chain',
            _yang_ns._namespaces['ietf-twamp'],
        'ydk.models.ietf.ietf_twamp'
        ),
    },
    'Twamp.Client.CtrlConnection.TestSessionRequest.PmRegList' : {
        'meta_info' : _MetaInfoClass('Twamp.Client.CtrlConnection.TestSessionRequest.PmRegList',
            False, 
            [
            _MetaInfoClassMember('pm-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Numerical index value of a Registered Metric
                in the Performance Metric Registry
                (see ietf-ippm-metric-registry). Output statistics
                are specified in the corresponding Registry entry.
                ''',
                'pm_index',
                'ietf-twamp', True),
            ],
            'ietf-twamp',
            'pm-reg-list',
            _yang_ns._namespaces['ietf-twamp'],
        'ydk.models.ietf.ietf_twamp'
        ),
    },
    'Twamp.Client.CtrlConnection.TestSessionRequest.RepeatEnum' : _MetaInfoEnum('RepeatEnum', 'ydk.models.ietf.ietf_twamp',
        {
            'forever':'forever',
        }, 'ietf-twamp', _yang_ns._namespaces['ietf-twamp']),
    'Twamp.Client.CtrlConnection.TestSessionRequest.SenderUdpPortEnum' : _MetaInfoEnum('SenderUdpPortEnum', 'ydk.models.ietf.ietf_twamp',
        {
            'autoallocate':'autoallocate',
        }, 'ietf-twamp', _yang_ns._namespaces['ietf-twamp']),
    'Twamp.Client.CtrlConnection.TestSessionRequest' : {
        'meta_info' : _MetaInfoClass('Twamp.Client.CtrlConnection.TestSessionRequest',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A unique name to be used for identification of
                this TWAMP-Test session on the Control-Client.
                ''',
                'name',
                'ietf-twamp', True),
            _MetaInfoClassMember('padding-length', ATTRIBUTE, 'int' , None, None, 
                [('64', '4096')], [], 
                '''                The number of padding bytes to be added to the
                TWAMP-Test (UDP) packets generated by the
                Session-Sender.
                
                This value will be placed in the Padding Length
                field of the Request-TW-Session message
                (RFC 4656, Section 3.5).
                ''',
                'padding_length',
                'ietf-twamp', False),
            _MetaInfoClassMember('pm-reg-list', REFERENCE_LIST, 'PmRegList' , 'ydk.models.ietf.ietf_twamp', 'Twamp.Client.CtrlConnection.TestSessionRequest.PmRegList', 
                [], [], 
                '''                A list of one or more Performance Metric Registry
                Index values, which communicate packet stream
                characteristics along with one or more metrics
                to be measured.
                
                All members of the pm-reg-list MUST have the same
                stream characteristics, such that they combine
                to specify all metrics that shall be measured on
                a single stream.
                ''',
                'pm_reg_list',
                'ietf-twamp', False),
            _MetaInfoClassMember('reflector-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The IP address belonging to the remote
                Session-Reflector device to which the TWAMP-Test
                session will be initiated. This value will be
                used to populate the receiver address field of
                the Request-TW-Session message.
                ''',
                'reflector_ip',
                'ietf-twamp', False, [
                    _MetaInfoClassMember('reflector-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address belonging to the remote
                        Session-Reflector device to which the TWAMP-Test
                        session will be initiated. This value will be
                        used to populate the receiver address field of
                        the Request-TW-Session message.
                        ''',
                        'reflector_ip',
                        'ietf-twamp', False),
                    _MetaInfoClassMember('reflector-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address belonging to the remote
                        Session-Reflector device to which the TWAMP-Test
                        session will be initiated. This value will be
                        used to populate the receiver address field of
                        the Request-TW-Session message.
                        ''',
                        'reflector_ip',
                        'ietf-twamp', False),
                ]),
            _MetaInfoClassMember('reflector-udp-port', ATTRIBUTE, 'int' , None, None, 
                [('49152', '65535')], [], 
                '''                This parameter defines the UDP port number that
                will be used by the Session-Reflector for
                this TWAMP-Test session. The number is restricted
                to the dynamic port range and is to be placed in
                the Receiver Port field of the Request-TW-Session
                message.
                ''',
                'reflector_udp_port',
                'ietf-twamp', False),
            _MetaInfoClassMember('repeat', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                This value determines if the TWAMP-Test session must
                be repeated. When a test session has completed, the
                repeat parameter is checked.
                
                The default value of 0 indicates that the session
                MUST NOT be repeated.
                
                If the repeat value is 1 through 4,294,967,294
                then the test session SHALL be repeated using the
                information in repeat-interval parameter, and the
                parent TWAMP-Control connection for this test
                session is restarted to negotiate a new instance
                of this TWAMP-Test session. The implementation
                MUST decrement the value of repeat after
                determining a repeated session is expected.
                ''',
                'repeat',
                'ietf-twamp', False, [
                    _MetaInfoClassMember('repeat', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967294')], [], 
                        '''                        This value determines if the TWAMP-Test session must
                        be repeated. When a test session has completed, the
                        repeat parameter is checked.
                        
                        The default value of 0 indicates that the session
                        MUST NOT be repeated.
                        
                        If the repeat value is 1 through 4,294,967,294
                        then the test session SHALL be repeated using the
                        information in repeat-interval parameter, and the
                        parent TWAMP-Control connection for this test
                        session is restarted to negotiate a new instance
                        of this TWAMP-Test session. The implementation
                        MUST decrement the value of repeat after
                        determining a repeated session is expected.
                        ''',
                        'repeat',
                        'ietf-twamp', False),
                    _MetaInfoClassMember('repeat', REFERENCE_ENUM_CLASS, 'Twamp.Client.CtrlConnection.TestSessionRequest.RepeatEnum' , 'ydk.models.ietf.ietf_twamp', 'Twamp.Client.CtrlConnection.TestSessionRequest.RepeatEnum', 
                        [], [], 
                        '''                        This value determines if the TWAMP-Test session must
                        be repeated. When a test session has completed, the
                        repeat parameter is checked.
                        
                        The default value of 0 indicates that the session
                        MUST NOT be repeated.
                        
                        If the repeat value is 1 through 4,294,967,294
                        then the test session SHALL be repeated using the
                        information in repeat-interval parameter, and the
                        parent TWAMP-Control connection for this test
                        session is restarted to negotiate a new instance
                        of this TWAMP-Test session. The implementation
                        MUST decrement the value of repeat after
                        determining a repeated session is expected.
                        ''',
                        'repeat',
                        'ietf-twamp', False),
                ]),
            _MetaInfoClassMember('repeat-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Repeat interval (in seconds).
                ''',
                'repeat_interval',
                'ietf-twamp', False),
            _MetaInfoClassMember('sender-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The IP address of the Session-Sender device,
                which is to be placed in the source IP address
                field of the IP header in TWAMP-Test (UDP) packets
                belonging to this test session. This value will be
                used to populate the sender address field of the
                Request-TW-Session message.
                
                If not configured, the device SHALL choose its own
                source IP address.
                ''',
                'sender_ip',
                'ietf-twamp', False, [
                    _MetaInfoClassMember('sender-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address of the Session-Sender device,
                        which is to be placed in the source IP address
                        field of the IP header in TWAMP-Test (UDP) packets
                        belonging to this test session. This value will be
                        used to populate the sender address field of the
                        Request-TW-Session message.
                        
                        If not configured, the device SHALL choose its own
                        source IP address.
                        ''',
                        'sender_ip',
                        'ietf-twamp', False),
                    _MetaInfoClassMember('sender-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address of the Session-Sender device,
                        which is to be placed in the source IP address
                        field of the IP header in TWAMP-Test (UDP) packets
                        belonging to this test session. This value will be
                        used to populate the sender address field of the
                        Request-TW-Session message.
                        
                        If not configured, the device SHALL choose its own
                        source IP address.
                        ''',
                        'sender_ip',
                        'ietf-twamp', False),
                ]),
            _MetaInfoClassMember('sender-udp-port', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The UDP port number that is to be used by
                the Session-Sender for this TWAMP-Test session.
                The number is restricted to the dynamic port range.
                
                By default the Control-Client SHALL auto-allocate a
                UDP port number for this TWAMP-Test session.
                
                The configured (or auto-allocated) value is advertized
                in the Sender Port field of the Request-TW-session
                message (see Section 3.5 of RFC 5357). Note that
                in the scenario where a device auto-allocates a UDP
                port number for a session, and the repeat parameter
                for that session indicates that it should be
                repeated, the device is free to auto-allocate a
                different UDP port number when it negotiates the
                next (repeated) iteration of this session.
                ''',
                'sender_udp_port',
                'ietf-twamp', False, [
                    _MetaInfoClassMember('sender-udp-port', ATTRIBUTE, 'int' , None, None, 
                        [('49152', '65535')], [], 
                        '''                        The UDP port number that is to be used by
                        the Session-Sender for this TWAMP-Test session.
                        The number is restricted to the dynamic port range.
                        
                        By default the Control-Client SHALL auto-allocate a
                        UDP port number for this TWAMP-Test session.
                        
                        The configured (or auto-allocated) value is advertized
                        in the Sender Port field of the Request-TW-session
                        message (see Section 3.5 of RFC 5357). Note that
                        in the scenario where a device auto-allocates a UDP
                        port number for a session, and the repeat parameter
                        for that session indicates that it should be
                        repeated, the device is free to auto-allocate a
                        different UDP port number when it negotiates the
                        next (repeated) iteration of this session.
                        ''',
                        'sender_udp_port',
                        'ietf-twamp', False),
                    _MetaInfoClassMember('sender-udp-port', REFERENCE_ENUM_CLASS, 'Twamp.Client.CtrlConnection.TestSessionRequest.SenderUdpPortEnum' , 'ydk.models.ietf.ietf_twamp', 'Twamp.Client.CtrlConnection.TestSessionRequest.SenderUdpPortEnum', 
                        [], [], 
                        '''                        The UDP port number that is to be used by
                        the Session-Sender for this TWAMP-Test session.
                        The number is restricted to the dynamic port range.
                        
                        By default the Control-Client SHALL auto-allocate a
                        UDP port number for this TWAMP-Test session.
                        
                        The configured (or auto-allocated) value is advertized
                        in the Sender Port field of the Request-TW-session
                        message (see Section 3.5 of RFC 5357). Note that
                        in the scenario where a device auto-allocates a UDP
                        port number for a session, and the repeat parameter
                        for that session indicates that it should be
                        repeated, the device is free to auto-allocate a
                        different UDP port number when it negotiates the
                        next (repeated) iteration of this session.
                        ''',
                        'sender_udp_port',
                        'ietf-twamp', False),
                ]),
            _MetaInfoClassMember('sid', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The SID allocated by the Server for this TWAMP-Test
                session, and communicated back to the Control-Client
                in the SID field of the Accept-Session message;
                see Section 4.3 of RFC 6038.
                ''',
                'sid',
                'ietf-twamp', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time when the session is to be started
                (but not before the TWAMP Start-Sessions command
                is issued; see Section 3.4 of RFC 5357).
                
                The start-time value is placed in the Start Time
                field of the Request-TW-Session message.
                
                The timestamp format follows RFC 1305 as per
                Section 3.5 of RFC 4656.
                
                The default value of 0 indicates that the session
                will be started as soon as the Start-Sessions message
                is received.
                ''',
                'start_time',
                'ietf-twamp', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'TestSessionStateEnum' , 'ydk.models.ietf.ietf_twamp', 'TestSessionStateEnum', 
                [], [], 
                '''                Indicates the TWAMP-Test session state (accepted or
                indication of an error); see Section 3.5 of
                RFC 5357.
                ''',
                'state',
                'ietf-twamp', False),
            _MetaInfoClassMember('test-packet-dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                The DSCP value to be placed in the IP header
                of TWAMP-Test packets generated by the
                Session-Sender, and in the UDP header of the
                TWAMP-Test response packets generated by the
                Session-Reflector for this test session.
                
                This value will be placed in the Type-P Descriptor
                field of the Request-TW-Session message (RFC 5357).
                ''',
                'test_packet_dscp',
                'ietf-twamp', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The length of time (in seconds) that the
                Session-Reflector should continue to respond to
                packets belonging to this TWAMP-Test session after
                a Stop-Sessions TWAMP-Control message has been
                received (RFC 5357, Section 3.8).
                
                This value will be placed in the Timeout field of
                the Request-TW-Session message.
                ''',
                'timeout',
                'ietf-twamp', False),
            ],
            'ietf-twamp',
            'test-session-request',
            _yang_ns._namespaces['ietf-twamp'],
        'ydk.models.ietf.ietf_twamp'
        ),
    },
    'Twamp.Client.CtrlConnection' : {
        'meta_info' : _MetaInfoClass('Twamp.Client.CtrlConnection',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A unique name used as a key to identify this individual
                TWAMP-Control connection on the Control-Client device.
                ''',
                'name',
                'ietf-twamp', True),
            _MetaInfoClassMember('client-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The IP address of the local Control-Client device,
                to be placed in the source IP address field of the
                IP header in TWAMP-Control (TCP) packets belonging
                to this control connection. If not configured, the
                device SHALL choose its own source IP address.
                ''',
                'client_ip',
                'ietf-twamp', False, [
                    _MetaInfoClassMember('client-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address of the local Control-Client device,
                        to be placed in the source IP address field of the
                        IP header in TWAMP-Control (TCP) packets belonging
                        to this control connection. If not configured, the
                        device SHALL choose its own source IP address.
                        ''',
                        'client_ip',
                        'ietf-twamp', False),
                    _MetaInfoClassMember('client-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address of the local Control-Client device,
                        to be placed in the source IP address field of the
                        IP header in TWAMP-Control (TCP) packets belonging
                        to this control connection. If not configured, the
                        device SHALL choose its own source IP address.
                        ''',
                        'client_ip',
                        'ietf-twamp', False),
                ]),
            _MetaInfoClassMember('client-iv', ATTRIBUTE, 'str' , None, None, 
                [(16, None)], [], 
                '''                Indicates the Control-Client Initialization Vector
                (Client-IV), that is generated randomly by the
                Control-Client. As per RFC 4656:
                
                 Client-IV merely needs to be unique (i.e., it MUST
                 never be repeated for different sessions using the
                 same secret key; a simple way to achieve that without
                 the use of cumbersome state is to generate the
                 Client-IV values using a cryptographically secure
                 pseudo-random number source.
                
                If the Mode defined in RFC 7717 is selected (selected-mode),
                Client-IV is limited to 12 octets.
                ''',
                'client_iv',
                'ietf-twamp', False),
            _MetaInfoClassMember('client-tcp-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Indicates the source TCP port number used in the
                TWAMP-Control packets belonging to this control
                connection.
                ''',
                'client_tcp_port',
                'ietf-twamp', False),
            _MetaInfoClassMember('control-packet-dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                The DSCP value to be placed in the IP header of
                TWAMP-Control (TCP) packets generated by this
                Control-Client.
                ''',
                'control_packet_dscp',
                'ietf-twamp', False),
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'str' , None, None, 
                [(1, 80)], [], 
                '''                Indicates the KeyID value selected for this
                TWAMP-Control connection.
                ''',
                'key_id',
                'ietf-twamp', False),
            _MetaInfoClassMember('max-count', ATTRIBUTE, 'int' , None, None, 
                [('10', '31')], [], 
                '''                This parameter limits the maximum Count value, which MUST
                be a power of 2 and at least 1024 as per RFC 5357. It is
                configured by providing said power. For example,
                configuring 10 here means max count 2^10 = 1024.
                The default is 15, meaning 2^15 = 32768.
                
                A TWAMP Server uses this configured value in the
                Server-Greeting message sent to the Control-Client.
                
                A TWAMP Control-Client uses this configured value to prevent
                denial-of-service (DOS) attacks by closing the control
                connection to the Server if it 'receives a Server-Greeting
                message with Count greater that its maximum configured value',
                as per Section 6 of RFC 5357.
                
                Further, note that according to Section 6 of RFC 5357:
                
                 'If an attacking system sets the maximum value in
                 Count (2**32), then the system under attack would stall
                 for a significant period of time while it attempts to
                 generate keys.
                
                 TWAMP-compliant systems SHOULD have a configuration
                 control to limit the maximum count value. The default
                 max-count value SHOULD be 32768.'
                
                RFC 5357 does not qualify 'significant period' in terms of
                time, but it is clear that this depends on the processing
                capacity available and operators need to pay attention to
                this security consideration.
                ''',
                'max_count',
                'ietf-twamp', False),
            _MetaInfoClassMember('selected-mode', REFERENCE_BITS, 'TwampModes' , 'ydk.models.ietf.ietf_twamp', 'TwampModes', 
                [], [], 
                '''                The TWAMP Mode that the Control-Client has chosen for
                this control connection as set in the Mode field of the
                Set-Up-Response message (RFC 4656, Section 3.1).
                ''',
                'selected_mode',
                'ietf-twamp', False),
            _MetaInfoClassMember('server-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The IP address of the remote Server device, which the
                TWAMP-Control connection will be initiated to.
                ''',
                'server_ip',
                'ietf-twamp', False, [
                    _MetaInfoClassMember('server-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address of the remote Server device, which the
                        TWAMP-Control connection will be initiated to.
                        ''',
                        'server_ip',
                        'ietf-twamp', False),
                    _MetaInfoClassMember('server-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address of the remote Server device, which the
                        TWAMP-Control connection will be initiated to.
                        ''',
                        'server_ip',
                        'ietf-twamp', False),
                ]),
            _MetaInfoClassMember('server-start-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Indicates the Start-Time advertized by the Server in the
                Server-Start message (RFC 4656, Section 3.1),
                representing the time when the current
                instantiation of the Server started operating.
                The timestamp format follows RFC 1305
                according to Section 4.1.2 of RFC 4656.
                ''',
                'server_start_time',
                'ietf-twamp', False),
            _MetaInfoClassMember('server-tcp-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This parameter defines the TCP port number that is
                to be used by this outgoing TWAMP-Control connection.
                Typically, this is the well-known TWAMP-Control
                port number (862) as per RFC 5357 However, there are known
                realizations of TWAMP in the field that were implemented
                before this well-known port number was allocated. These
                early implementations allowed the port number to be
                configured. This parameter is therefore provided for
                backward compatibility reasons.
                ''',
                'server_tcp_port',
                'ietf-twamp', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'ControlClientConnectionStateEnum' , 'ydk.models.ietf.ietf_twamp', 'ControlClientConnectionStateEnum', 
                [], [], 
                '''                Indicates the current state of the TWAMP-Control
                connection state.
                ''',
                'state',
                'ietf-twamp', False),
            _MetaInfoClassMember('test-session-request', REFERENCE_LIST, 'TestSessionRequest' , 'ydk.models.ietf.ietf_twamp', 'Twamp.Client.CtrlConnection.TestSessionRequest', 
                [], [], 
                '''                Information associated with the Control-Client
                for this test session
                ''',
                'test_session_request',
                'ietf-twamp', False),
            _MetaInfoClassMember('token', ATTRIBUTE, 'str' , None, None, 
                [(64, None)], [], 
                '''                This parameter holds the 64 octets containing the
                concatenation of a 16-octet Challenge, a 16-octet AES
                Session-key used for encryption, and a 32-octet
                HMAC-SHA1 Session-key used for authentication; see also
                the last paragraph of Section 6 in RFC 4656.
                
                If the Mode defined in RFC 7717 is selected (selected-mode),
                Token is limited to 16 octets.
                ''',
                'token',
                'ietf-twamp', False),
            ],
            'ietf-twamp',
            'ctrl-connection',
            _yang_ns._namespaces['ietf-twamp'],
        'ydk.models.ietf.ietf_twamp'
        ),
    },
    'Twamp.Client' : {
        'meta_info' : _MetaInfoClass('Twamp.Client',
            False, 
            [
            _MetaInfoClassMember('admin-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether the device is allowed to operate as a
                TWAMP Control-Client.
                ''',
                'admin_state',
                'ietf-twamp', False),
            _MetaInfoClassMember('ctrl-connection', REFERENCE_LIST, 'CtrlConnection' , 'ydk.models.ietf.ietf_twamp', 'Twamp.Client.CtrlConnection', 
                [], [], 
                '''                List of TWAMP Control-Client control connections.
                Each item in the list describes a control connection
                that will be initiated by this Control-Client
                ''',
                'ctrl_connection',
                'ietf-twamp', False),
            _MetaInfoClassMember('key-chain', REFERENCE_LIST, 'KeyChain' , 'ydk.models.ietf.ietf_twamp', 'Twamp.Client.KeyChain', 
                [], [], 
                '''                Relates KeyIDs with their respective secret keys
                in a TWAMP-Control connection.
                ''',
                'key_chain',
                'ietf-twamp', False),
            _MetaInfoClassMember('mode-preference-chain', REFERENCE_LIST, 'ModePreferenceChain' , 'ydk.models.ietf.ietf_twamp', 'Twamp.Client.ModePreferenceChain', 
                [], [], 
                '''                Indicates the Control-Client preferred order of use of
                the supported TWAMP Modes.
                
                Depending on the Modes available in the TWAMP Server
                Greeting message (see Fig. 2 of RFC 7717), the
                this Control-Client MUST choose the highest priority Mode
                from the configured mode-preference-chain list.
                ''',
                'mode_preference_chain',
                'ietf-twamp', False),
            ],
            'ietf-twamp',
            'client',
            _yang_ns._namespaces['ietf-twamp'],
        'ydk.models.ietf.ietf_twamp'
        ),
    },
    'Twamp.Server.KeyChain' : {
        'meta_info' : _MetaInfoClass('Twamp.Server.KeyChain',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'str' , None, None, 
                [(1, 80)], [], 
                '''                KeyID used for a TWAMP-Control connection. As per
                Section 3.1 of RFC 4656, KeyID is 'a UTF-8 string, up to
                80 octets in length' and is used to select which 'shared
                shared secret the [Control-Client] wishes to use to
                authenticate or encrypt'.
                ''',
                'key_id',
                'ietf-twamp', True),
            _MetaInfoClassMember('secret-key', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The secret key corresponding to the KeyID for this
                TWAMP-Control connection.
                ''',
                'secret_key',
                'ietf-twamp', False),
            ],
            'ietf-twamp',
            'key-chain',
            _yang_ns._namespaces['ietf-twamp'],
        'ydk.models.ietf.ietf_twamp'
        ),
    },
    'Twamp.Server.CtrlConnection' : {
        'meta_info' : _MetaInfoClass('Twamp.Server.CtrlConnection',
            False, 
            [
            _MetaInfoClassMember('client-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The IP address on the remote Control-Client device,
                which is the source IP address used in the
                TWAMP-Control (TCP) packets belonging to this control
                connection.
                ''',
                'client_ip',
                'ietf-twamp', True, [
                    _MetaInfoClassMember('client-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address on the remote Control-Client device,
                        which is the source IP address used in the
                        TWAMP-Control (TCP) packets belonging to this control
                        connection.
                        ''',
                        'client_ip',
                        'ietf-twamp', True),
                    _MetaInfoClassMember('client-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address on the remote Control-Client device,
                        which is the source IP address used in the
                        TWAMP-Control (TCP) packets belonging to this control
                        connection.
                        ''',
                        'client_ip',
                        'ietf-twamp', True),
                ]),
            _MetaInfoClassMember('client-tcp-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The source TCP port number used in the TWAMP-Control
                (TCP) packets belonging to this control connection.
                ''',
                'client_tcp_port',
                'ietf-twamp', True),
            _MetaInfoClassMember('server-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The IP address of the local Server device, which is
                the destination IP address used in the
                TWAMP-Control (TCP) packets belonging to this control
                connection.
                ''',
                'server_ip',
                'ietf-twamp', True, [
                    _MetaInfoClassMember('server-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address of the local Server device, which is
                        the destination IP address used in the
                        TWAMP-Control (TCP) packets belonging to this control
                        connection.
                        ''',
                        'server_ip',
                        'ietf-twamp', True),
                    _MetaInfoClassMember('server-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address of the local Server device, which is
                        the destination IP address used in the
                        TWAMP-Control (TCP) packets belonging to this control
                        connection.
                        ''',
                        'server_ip',
                        'ietf-twamp', True),
                ]),
            _MetaInfoClassMember('server-tcp-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The destination TCP port number used in the
                TWAMP-Control (TCP) packets belonging to this
                control connection. This will usually be the
                same value as the server-tcp-port configured
                under twamp/server. However, in the event that
                the user re-configured server/server-tcp-port
                after this control connection was initiated, this
                value will indicate the server-tcp-port that is
                actually in use for this control connection.
                ''',
                'server_tcp_port',
                'ietf-twamp', True),
            _MetaInfoClassMember('challenge', ATTRIBUTE, 'str' , None, None, 
                [(16, None)], [], 
                '''                A random sequence of octets generated by the Server.
                As described in client/token, Challenge is used
                by the Control-Client to prove possession of a
                shared secret.
                ''',
                'challenge',
                'ietf-twamp', False),
            _MetaInfoClassMember('control-packet-dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                The DSCP value used in the IP header of the
                TWAMP-Control (TCP) packets sent by the Server
                for this control connection. This will usually
                be the same value as is configured in the
                control-packet-dscp parameter under the twamp/server
                container.  However, in the event that the user
                re-configures server/dscp after this control
                connection is already in progress, this read-only
                value will show the actual dscp value in use by this
                TWAMP-Control connection.
                ''',
                'control_packet_dscp',
                'ietf-twamp', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('10', '31')], [], 
                '''                Parameter communicated to the Control-Client as part of the
                Server Greeting message and used for deriving a key from a
                shared secret as per Section 3.1 of  RFC 4656:  MUST be a
                power of 2 and at least 1024; SHOULD be increased as more
                computing power becomes common.
                ''',
                'count',
                'ietf-twamp', False),
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'str' , None, None, 
                [(1, 80)], [], 
                '''                The KeyID value that is in use by this TWAMP-Control
                connection as selected by Control-Client.
                ''',
                'key_id',
                'ietf-twamp', False),
            _MetaInfoClassMember('max-count', ATTRIBUTE, 'int' , None, None, 
                [('10', '31')], [], 
                '''                This parameter limits the maximum Count value, which MUST
                be a power of 2 and at least 1024 as per RFC 5357. It is
                configured by providing said power. For example,
                configuring 10 here means max count 2^10 = 1024.
                The default is 15, meaning 2^15 = 32768.
                
                A TWAMP Server uses this configured value in the
                Server-Greeting message sent to the Control-Client.
                
                A TWAMP Control-Client uses this configured value to prevent
                denial-of-service (DOS) attacks by closing the control
                connection to the Server if it 'receives a Server-Greeting
                message with Count greater that its maximum configured value',
                as per Section 6 of RFC 5357.
                
                Further, note that according to Section 6 of RFC 5357:
                
                 'If an attacking system sets the maximum value in
                 Count (2**32), then the system under attack would stall
                 for a significant period of time while it attempts to
                 generate keys.
                
                 TWAMP-compliant systems SHOULD have a configuration
                 control to limit the maximum count value. The default
                 max-count value SHOULD be 32768.'
                
                RFC 5357 does not qualify 'significant period' in terms of
                time, but it is clear that this depends on the processing
                capacity available and operators need to pay attention to
                this security consideration.
                ''',
                'max_count',
                'ietf-twamp', False),
            _MetaInfoClassMember('salt', ATTRIBUTE, 'str' , None, None, 
                [(16, None)], [], 
                '''                A parameter used in deriving a key from a
                shared secret as described in Section 3.1 of RFC 4656.
                It is communicated to the Control-Client as part of
                the Server Greeting message.
                ''',
                'salt',
                'ietf-twamp', False),
            _MetaInfoClassMember('selected-mode', REFERENCE_BITS, 'TwampModes' , 'ydk.models.ietf.ietf_twamp', 'TwampModes', 
                [], [], 
                '''                The Mode that was chosen for this TWAMP-Control
                connection as set in the Mode field of the
                Set-Up-Response message.
                ''',
                'selected_mode',
                'ietf-twamp', False),
            _MetaInfoClassMember('server-iv', ATTRIBUTE, 'str' , None, None, 
                [(16, None)], [], 
                '''                The Server Initialization Vector
                (IV) generated randomly by the Server.
                ''',
                'server_iv',
                'ietf-twamp', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'ServerCtrlConnectionStateEnum' , 'ydk.models.ietf.ietf_twamp', 'ServerCtrlConnectionStateEnum', 
                [], [], 
                '''                Indicates the Server TWAMP-Control connection state.
                ''',
                'state',
                'ietf-twamp', False),
            ],
            'ietf-twamp',
            'ctrl-connection',
            _yang_ns._namespaces['ietf-twamp'],
        'ydk.models.ietf.ietf_twamp'
        ),
    },
    'Twamp.Server' : {
        'meta_info' : _MetaInfoClass('Twamp.Server',
            False, 
            [
            _MetaInfoClassMember('admin-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether the device is allowed to operate
                as a TWAMP Server.
                ''',
                'admin_state',
                'ietf-twamp', False),
            _MetaInfoClassMember('control-packet-dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                The DSCP value to be placed in the IP header of
                TWAMP-Control (TCP) packets generated by the Server.
                
                Section 3.1 of  RFC 5357 specifies that the server
                SHOULD use the DSCP value from the Control-Client's
                TCP SYN. However, for practical purposes TWAMP will
                typically be implemented using a general purpose TCP
                stack provided by the underlying operating system,
                and such a stack may not provide this information to the
                user. Consequently, it is not always possible to
                implement the behavior described in RFC 5357 in an
                OS-portable version of TWAMP.
                
                The default behavior if this item is not set is to use
                the DSCP value from the Control-Client's TCP SYN,
                as per Section 3.1 of RFC 5357.
                ''',
                'control_packet_dscp',
                'ietf-twamp', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('10', '31')], [], 
                '''                Parameter communicated to the Control-Client as part of the
                Server Greeting message and used for deriving a key from a
                shared secret as per Section 3.1 of  RFC 4656:  MUST be a
                power of 2 and at least 1024; SHOULD be increased as more
                computing power becomes common.
                ''',
                'count',
                'ietf-twamp', False),
            _MetaInfoClassMember('ctrl-connection', REFERENCE_LIST, 'CtrlConnection' , 'ydk.models.ietf.ietf_twamp', 'Twamp.Server.CtrlConnection', 
                [], [], 
                '''                List of all incoming TWAMP-Control (TCP) connections.
                ''',
                'ctrl_connection',
                'ietf-twamp', False),
            _MetaInfoClassMember('key-chain', REFERENCE_LIST, 'KeyChain' , 'ydk.models.ietf.ietf_twamp', 'Twamp.Server.KeyChain', 
                [], [], 
                '''                Relates KeyIDs with their respective secret keys
                in a TWAMP-Control connection.
                ''',
                'key_chain',
                'ietf-twamp', False),
            _MetaInfoClassMember('max-count', ATTRIBUTE, 'int' , None, None, 
                [('10', '31')], [], 
                '''                This parameter limits the maximum Count value, which MUST
                be a power of 2 and at least 1024 as per RFC 5357. It is
                configured by providing said power. For example,
                configuring 10 here means max count 2^10 = 1024.
                The default is 15, meaning 2^15 = 32768.
                
                A TWAMP Server uses this configured value in the
                Server-Greeting message sent to the Control-Client.
                
                A TWAMP Control-Client uses this configured value to prevent
                denial-of-service (DOS) attacks by closing the control
                connection to the Server if it 'receives a Server-Greeting
                message with Count greater that its maximum configured value',
                as per Section 6 of RFC 5357.
                
                Further, note that according to Section 6 of RFC 5357:
                
                 'If an attacking system sets the maximum value in
                 Count (2**32), then the system under attack would stall
                 for a significant period of time while it attempts to
                 generate keys.
                
                 TWAMP-compliant systems SHOULD have a configuration
                 control to limit the maximum count value. The default
                 max-count value SHOULD be 32768.'
                
                RFC 5357 does not qualify 'significant period' in terms of
                time, but it is clear that this depends on the processing
                capacity available and operators need to pay attention to
                this security consideration.
                ''',
                'max_count',
                'ietf-twamp', False),
            _MetaInfoClassMember('modes', REFERENCE_BITS, 'TwampModes' , 'ydk.models.ietf.ietf_twamp', 'TwampModes', 
                [], [], 
                '''                The bit mask of TWAMP Modes this Server instance
                is willing to support; see IANA TWAMP Modes Registry.
                ''',
                'modes',
                'ietf-twamp', False),
            _MetaInfoClassMember('server-tcp-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This parameter defines the well known TCP port number
                that is used by TWAMP-Control. The Server will listen
                on this port number for incoming TWAMP-Control
                connections. Although this is defined as a fixed value
                (862) in RFC 5357, there are several realizations of
                TWAMP in the field that were implemented before this
                well-known port number was allocated. These early
                implementations allowed the port number to be
                configured. This parameter is therefore provided for
                backward compatibility reasons.
                ''',
                'server_tcp_port',
                'ietf-twamp', False),
            _MetaInfoClassMember('servwait', ATTRIBUTE, 'int' , None, None, 
                [('1', '604800')], [], 
                '''                TWAMP-Control (TCP) session timeout, in seconds.
                According to Section 3.1 of RFC 5357,
                
                 Server MAY discontinue any established control
                 connection when no packet associated with that
                 connection has been received within SERVWAIT seconds.
                ''',
                'servwait',
                'ietf-twamp', False),
            ],
            'ietf-twamp',
            'server',
            _yang_ns._namespaces['ietf-twamp'],
        'ydk.models.ietf.ietf_twamp'
        ),
    },
    'Twamp.SessionSender.TestSession' : {
        'meta_info' : _MetaInfoClass('Twamp.SessionSender.TestSession',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A unique name for this TWAMP-Test session to be used
                for identifying this test session by the Session-Sender
                logical entity.
                ''',
                'name',
                'ietf-twamp', True),
            _MetaInfoClassMember('ctrl-connection-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the parent TWAMP-Control connection that
                is responsible for negotiating this TWAMP-Test session.
                ''',
                'ctrl_connection_name',
                'ietf-twamp', False),
            _MetaInfoClassMember('fill-mode', REFERENCE_ENUM_CLASS, 'PaddingFillModeEnum' , 'ydk.models.ietf.ietf_twamp', 'PaddingFillModeEnum', 
                [], [], 
                '''                Indicates whether the padding added to the
                TWAMP-Test (UDP) packets will contain pseudo-random
                numbers, or whether it should consist of all zeroes,
                as per Section 4.2.1 of RFC 5357.
                ''',
                'fill_mode',
                'ietf-twamp', False),
            _MetaInfoClassMember('lambda', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547.75808', '92233720368547.75807')], [], 
                '''                Indicates the average time interval (in seconds)
                between packets in the Poisson distribution.
                The packet is calculated using the reciprocal of lambda
                and the TWAMP-Test packet size (which depends on the
                selected Mode and the packet padding).
                ''',
                'lambda_',
                'ietf-twamp', False),
            _MetaInfoClassMember('last-rcv-seq', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the last received sequence number.
                ''',
                'last_rcv_seq',
                'ietf-twamp', False),
            _MetaInfoClassMember('last-sent-seq', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the last sent sequence number.
                ''',
                'last_sent_seq',
                'ietf-twamp', False),
            _MetaInfoClassMember('max-interval', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547.75808', '92233720368547.75807')], [], 
                '''                Indicates the maximum time (in seconds)
                between packet transmissions.
                ''',
                'max_interval',
                'ietf-twamp', False),
            _MetaInfoClassMember('number-of-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The overall number of TWAMP-Test (UDP) packets to be
                transmitted by the Session-Sender for this test session.
                ''',
                'number_of_packets',
                'ietf-twamp', False),
            _MetaInfoClassMember('periodic-interval', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547.75808', '92233720368547.75807')], [], 
                '''                Indicates the time to wait (in seconds) between the
                first bits of TWAMP-Test (UDP) packet transmissions for
                this test session
                ''',
                'periodic_interval',
                'ietf-twamp', False),
            _MetaInfoClassMember('rcv-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of packets received.
                ''',
                'rcv_packets',
                'ietf-twamp', False),
            _MetaInfoClassMember('sent-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of packets sent.
                ''',
                'sent_packets',
                'ietf-twamp', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'SenderSessionStateEnum' , 'ydk.models.ietf.ietf_twamp', 'SenderSessionStateEnum', 
                [], [], 
                '''                Indicates the Session-Sender test session state.
                ''',
                'state',
                'ietf-twamp', False),
            ],
            'ietf-twamp',
            'test-session',
            _yang_ns._namespaces['ietf-twamp'],
        'ydk.models.ietf.ietf_twamp'
        ),
    },
    'Twamp.SessionSender' : {
        'meta_info' : _MetaInfoClass('Twamp.SessionSender',
            False, 
            [
            _MetaInfoClassMember('admin-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether the device is allowed to operate
                as a TWAMP Session-Sender.
                ''',
                'admin_state',
                'ietf-twamp', False),
            _MetaInfoClassMember('test-session', REFERENCE_LIST, 'TestSession' , 'ydk.models.ietf.ietf_twamp', 'Twamp.SessionSender.TestSession', 
                [], [], 
                '''                List of TWAMP Session-Sender test sessions.
                ''',
                'test_session',
                'ietf-twamp', False),
            ],
            'ietf-twamp',
            'session-sender',
            _yang_ns._namespaces['ietf-twamp'],
        'ydk.models.ietf.ietf_twamp'
        ),
    },
    'Twamp.SessionReflector.TestSession' : {
        'meta_info' : _MetaInfoClass('Twamp.SessionReflector.TestSession',
            False, 
            [
            _MetaInfoClassMember('reflector-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The IP address of the local Session-Reflector
                device, which is the destination IP address used
                in the TWAMP-Test (UDP) packets belonging to this test
                session.
                ''',
                'reflector_ip',
                'ietf-twamp', True, [
                    _MetaInfoClassMember('reflector-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address of the local Session-Reflector
                        device, which is the destination IP address used
                        in the TWAMP-Test (UDP) packets belonging to this test
                        session.
                        ''',
                        'reflector_ip',
                        'ietf-twamp', True),
                    _MetaInfoClassMember('reflector-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address of the local Session-Reflector
                        device, which is the destination IP address used
                        in the TWAMP-Test (UDP) packets belonging to this test
                        session.
                        ''',
                        'reflector_ip',
                        'ietf-twamp', True),
                ]),
            _MetaInfoClassMember('reflector-udp-port', ATTRIBUTE, 'int' , None, None, 
                [('49152', '65535')], [], 
                '''                The destination UDP port number used in the
                TWAMP-Test (UDP) test packets belonging to this
                test session.
                ''',
                'reflector_udp_port',
                'ietf-twamp', True),
            _MetaInfoClassMember('sender-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The IP address on the remote device, which is the
                source IP address used in the TWAMP-Test (UDP) packets
                belonging to this test session.
                ''',
                'sender_ip',
                'ietf-twamp', True, [
                    _MetaInfoClassMember('sender-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address on the remote device, which is the
                        source IP address used in the TWAMP-Test (UDP) packets
                        belonging to this test session.
                        ''',
                        'sender_ip',
                        'ietf-twamp', True),
                    _MetaInfoClassMember('sender-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address on the remote device, which is the
                        source IP address used in the TWAMP-Test (UDP) packets
                        belonging to this test session.
                        ''',
                        'sender_ip',
                        'ietf-twamp', True),
                ]),
            _MetaInfoClassMember('sender-udp-port', ATTRIBUTE, 'int' , None, None, 
                [('49152', '65535')], [], 
                '''                The source UDP port used in the TWAMP-Test packets
                belonging to this test session.
                ''',
                'sender_udp_port',
                'ietf-twamp', True),
            _MetaInfoClassMember('last-rcv-seq', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the last received sequence number.
                ''',
                'last_rcv_seq',
                'ietf-twamp', False),
            _MetaInfoClassMember('last-sent-seq', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the last sent sequence number.
                ''',
                'last_sent_seq',
                'ietf-twamp', False),
            _MetaInfoClassMember('parent-connection-client-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The IP address on the Control-Client device, which
                is the source IP address used in the TWAMP-Control
                (TCP) packets belonging to the parent control
                connection that negotiated this test session.
                ''',
                'parent_connection_client_ip',
                'ietf-twamp', False, [
                    _MetaInfoClassMember('parent-connection-client-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address on the Control-Client device, which
                        is the source IP address used in the TWAMP-Control
                        (TCP) packets belonging to the parent control
                        connection that negotiated this test session.
                        ''',
                        'parent_connection_client_ip',
                        'ietf-twamp', False),
                    _MetaInfoClassMember('parent-connection-client-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address on the Control-Client device, which
                        is the source IP address used in the TWAMP-Control
                        (TCP) packets belonging to the parent control
                        connection that negotiated this test session.
                        ''',
                        'parent_connection_client_ip',
                        'ietf-twamp', False),
                ]),
            _MetaInfoClassMember('parent-connection-client-tcp-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The source TCP port number used in the TWAMP-Control
                (TCP) packets belonging to the parent control connection
                that negotiated this test session.
                ''',
                'parent_connection_client_tcp_port',
                'ietf-twamp', False),
            _MetaInfoClassMember('parent-connection-server-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The IP address of the Server device, which is the
                destination IP address used in the TWAMP-Control
                (TCP) packets belonging to the parent control
                connection that negotiated this test session.
                ''',
                'parent_connection_server_ip',
                'ietf-twamp', False, [
                    _MetaInfoClassMember('parent-connection-server-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address of the Server device, which is the
                        destination IP address used in the TWAMP-Control
                        (TCP) packets belonging to the parent control
                        connection that negotiated this test session.
                        ''',
                        'parent_connection_server_ip',
                        'ietf-twamp', False),
                    _MetaInfoClassMember('parent-connection-server-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address of the Server device, which is the
                        destination IP address used in the TWAMP-Control
                        (TCP) packets belonging to the parent control
                        connection that negotiated this test session.
                        ''',
                        'parent_connection_server_ip',
                        'ietf-twamp', False),
                ]),
            _MetaInfoClassMember('parent-connection-server-tcp-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The destination TCP port number used in the TWAMP-Control
                (TCP) packets belonging to the parent control connection
                that negotiated this test session.
                ''',
                'parent_connection_server_tcp_port',
                'ietf-twamp', False),
            _MetaInfoClassMember('rcv-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of packets received.
                ''',
                'rcv_packets',
                'ietf-twamp', False),
            _MetaInfoClassMember('sent-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of packets sent.
                ''',
                'sent_packets',
                'ietf-twamp', False),
            _MetaInfoClassMember('sid', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                An auto-allocated identifier for this TWAMP-Test
                session that is unique within the context of this
                Server/Session-Reflector device only. This value
                is communicated to the Control-Client that
                requested the test session in the SID field of the
                Accept-Session message.
                ''',
                'sid',
                'ietf-twamp', False),
            _MetaInfoClassMember('test-packet-dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                The DSCP value present in the IP header of
                TWAMP-Test (UDP) packets belonging to this session.
                ''',
                'test_packet_dscp',
                'ietf-twamp', False),
            ],
            'ietf-twamp',
            'test-session',
            _yang_ns._namespaces['ietf-twamp'],
        'ydk.models.ietf.ietf_twamp'
        ),
    },
    'Twamp.SessionReflector' : {
        'meta_info' : _MetaInfoClass('Twamp.SessionReflector',
            False, 
            [
            _MetaInfoClassMember('admin-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether the device is allowed to operate
                as a TWAMP Session-Reflector.
                ''',
                'admin_state',
                'ietf-twamp', False),
            _MetaInfoClassMember('refwait', ATTRIBUTE, 'int' , None, None, 
                [('1', '604800')], [], 
                '''                The Session-Reflector MAY discontinue any session that has
                been started when no packet associated with that session has
                been received for REFWAIT seconds. As per Section 3.1 of
                RFC 5357, this timeout allows a Session-Reflector to free up
                resources in case of failure.
                ''',
                'refwait',
                'ietf-twamp', False),
            _MetaInfoClassMember('test-session', REFERENCE_LIST, 'TestSession' , 'ydk.models.ietf.ietf_twamp', 'Twamp.SessionReflector.TestSession', 
                [], [], 
                '''                TWAMP Session-Reflectortest sessions.
                ''',
                'test_session',
                'ietf-twamp', False),
            ],
            'ietf-twamp',
            'session-reflector',
            _yang_ns._namespaces['ietf-twamp'],
        'ydk.models.ietf.ietf_twamp'
        ),
    },
    'Twamp' : {
        'meta_info' : _MetaInfoClass('Twamp',
            False, 
            [
            _MetaInfoClassMember('client', REFERENCE_CLASS, 'Client' , 'ydk.models.ietf.ietf_twamp', 'Twamp.Client', 
                [], [], 
                '''                Configuration of the TWAMP Control-Client logical entity.
                ''',
                'client',
                'ietf-twamp', False),
            _MetaInfoClassMember('server', REFERENCE_CLASS, 'Server' , 'ydk.models.ietf.ietf_twamp', 'Twamp.Server', 
                [], [], 
                '''                Configuration of the TWAMP Server logical entity.
                ''',
                'server',
                'ietf-twamp', False),
            _MetaInfoClassMember('session-reflector', REFERENCE_CLASS, 'SessionReflector' , 'ydk.models.ietf.ietf_twamp', 'Twamp.SessionReflector', 
                [], [], 
                '''                Configuration of the TWAMP Session-Reflector logical entity
                ''',
                'session_reflector',
                'ietf-twamp', False),
            _MetaInfoClassMember('session-sender', REFERENCE_CLASS, 'SessionSender' , 'ydk.models.ietf.ietf_twamp', 'Twamp.SessionSender', 
                [], [], 
                '''                Configuration of the TWAMP Session-Sender logical entity
                ''',
                'session_sender',
                'ietf-twamp', False),
            ],
            'ietf-twamp',
            'twamp',
            _yang_ns._namespaces['ietf-twamp'],
        'ydk.models.ietf.ietf_twamp'
        ),
    },
}
_meta_table['Twamp.Client.CtrlConnection.TestSessionRequest.PmRegList']['meta_info'].parent =_meta_table['Twamp.Client.CtrlConnection.TestSessionRequest']['meta_info']
_meta_table['Twamp.Client.CtrlConnection.TestSessionRequest']['meta_info'].parent =_meta_table['Twamp.Client.CtrlConnection']['meta_info']
_meta_table['Twamp.Client.ModePreferenceChain']['meta_info'].parent =_meta_table['Twamp.Client']['meta_info']
_meta_table['Twamp.Client.KeyChain']['meta_info'].parent =_meta_table['Twamp.Client']['meta_info']
_meta_table['Twamp.Client.CtrlConnection']['meta_info'].parent =_meta_table['Twamp.Client']['meta_info']
_meta_table['Twamp.Server.KeyChain']['meta_info'].parent =_meta_table['Twamp.Server']['meta_info']
_meta_table['Twamp.Server.CtrlConnection']['meta_info'].parent =_meta_table['Twamp.Server']['meta_info']
_meta_table['Twamp.SessionSender.TestSession']['meta_info'].parent =_meta_table['Twamp.SessionSender']['meta_info']
_meta_table['Twamp.SessionReflector.TestSession']['meta_info'].parent =_meta_table['Twamp.SessionReflector']['meta_info']
_meta_table['Twamp.Client']['meta_info'].parent =_meta_table['Twamp']['meta_info']
_meta_table['Twamp.Server']['meta_info'].parent =_meta_table['Twamp']['meta_info']
_meta_table['Twamp.SessionSender']['meta_info'].parent =_meta_table['Twamp']['meta_info']
_meta_table['Twamp.SessionReflector']['meta_info'].parent =_meta_table['Twamp']['meta_info']

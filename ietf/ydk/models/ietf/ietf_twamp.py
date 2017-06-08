""" ietf_twamp 

This YANG module specifies a vendor\-independent data
model for the Two\-Way Active Measurement Protocol (TWAMP).

The data model covers four TWAMP logical entities, namely,
Control\-Client, Server, Session\-Sender, and Session\-Reflector,
as illustrated in the annotated TWAMP logical model (Fig. 1
of draft\-ietf\-ippm\-twamp\-yang).

This YANG module uses features to indicate which of the four
logical entities are supported by a TWAMP implementation.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class ControlClientConnectionStateEnum(Enum):
    """
    ControlClientConnectionStateEnum

    Indicates the Control\-Client TWAMP\-Control connection state.

    .. data:: active = 0

    	Indicates an active TWAMP-Control connection to Server.

    .. data:: idle = 1

    	Indicates an idle TWAMP-Control connection to Server.

    """

    active = 0

    idle = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_twamp as meta
        return meta._meta_table['ControlClientConnectionStateEnum']


class PaddingFillModeEnum(Enum):
    """
    PaddingFillModeEnum

    Indicates what type of packet padding is used in the

    TWAMP\-Test packets.

    .. data:: zero = 0

    	TWAMP-Test packets are padded with all zeros.

    .. data:: random = 1

    	TWAMP-Test packets are padded with pseudo-random

    	numbers.

    """

    zero = 0

    random = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_twamp as meta
        return meta._meta_table['PaddingFillModeEnum']


class SenderSessionStateEnum(Enum):
    """
    SenderSessionStateEnum

    Indicates the Session\-Sender TWAMP\-Test session state.

    .. data:: active = 0

    	Indicates that the TWAMP-Test session is active.

    .. data:: failure = 1

    	Indicates that the TWAMP-Test session has failed.

    """

    active = 0

    failure = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_twamp as meta
        return meta._meta_table['SenderSessionStateEnum']


class ServerCtrlConnectionStateEnum(Enum):
    """
    ServerCtrlConnectionStateEnum

    Indicates the Server TWAMP\-Control connection state.

    .. data:: active = 0

    	Indicates an active TWAMP-Control connection

    	to the Control-Client.

    .. data:: servwait = 1

    	Indicates that the TWAMP-Control connection to the

    	Control-Client is in SERVWAIT as per the definition of

    	Section 3.1 of RFC 5357.

    """

    active = 0

    servwait = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_twamp as meta
        return meta._meta_table['ServerCtrlConnectionStateEnum']


class TestSessionStateEnum(Enum):
    """
    TestSessionStateEnum

    Indicates the Control\-Client TWAMP\-Test session state.

    .. data:: accepted = 0

    	Indicates that accepted TWAMP-Test session request.

    .. data:: failed = 1

    	Indicates a TWAMP-Test session failure due to

    	some unspecified reason (catch-all).

    .. data:: internal_error = 2

    	Indicates a TWAMP-Test session failure due to

    	an internal error.

    .. data:: not_supported = 3

    	Indicates a TWAMP-Test session failure because

    	some aspect of the TWAMP-Test session request

    	is not supported.

    .. data:: permanent_resource_limit = 4

    	Indicates a TWAMP-Test session failure due to

    	permanent resource limitations.

    .. data:: temp_resource_limit = 5

    	Indicates a TWAMP-Test session failure due to

    	temporary resource limitations.

    """

    accepted = 0

    failed = 1

    internal_error = 2

    not_supported = 3

    permanent_resource_limit = 4

    temp_resource_limit = 5


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_twamp as meta
        return meta._meta_table['TestSessionStateEnum']


class TwampModes(FixedBitsDict):
    """
    TwampModes

    Specifies the configurable TWAMP\-Modes supported during a
    TWAMP\-Control Connection setup between a Control\-Client
    and a Server. Section 7 of RFC 7717 summarizes the
    TWAMP\-Modes registry and points to their formal
    specification.
    Keys are:- authenticated , unauthenticated , IKEv2Derived , reflect\-octets , symmetrical\-size , unauth\-test\-encrpyt\-control , individual\-session\-control , encrypted

    """

    def __init__(self):
        self._dictionary = { 
            'authenticated':False,
            'unauthenticated':False,
            'IKEv2Derived':False,
            'reflect-octets':False,
            'symmetrical-size':False,
            'unauth-test-encrpyt-control':False,
            'individual-session-control':False,
            'encrypted':False,
        }
        self._pos_map = { 
            'authenticated':1,
            'unauthenticated':0,
            'IKEv2Derived':7,
            'reflect-octets':5,
            'symmetrical-size':6,
            'unauth-test-encrpyt-control':3,
            'individual-session-control':4,
            'encrypted':2,
        }


class Twamp(object):
    """
    TWAMP logical entity configuration grouping of four models
    which correspond to the four TWAMP logical entities
    Control\-Client, Server, Session\-Sender, and Session\-Reflector
    as illustrated in Fig. 1 of draft\-ietf\-ippm\-twamp\-yang.
    
    .. attribute:: client
    
    	Configuration of the TWAMP Control\-Client logical entity
    	**type**\:   :py:class:`Client <ydk.models.ietf.ietf_twamp.Twamp.Client>`
    
    	**presence node**\: True
    
    .. attribute:: server
    
    	Configuration of the TWAMP Server logical entity
    	**type**\:   :py:class:`Server <ydk.models.ietf.ietf_twamp.Twamp.Server>`
    
    	**presence node**\: True
    
    .. attribute:: session_reflector
    
    	Configuration of the TWAMP Session\-Reflector logical entity
    	**type**\:   :py:class:`SessionReflector <ydk.models.ietf.ietf_twamp.Twamp.SessionReflector>`
    
    	**presence node**\: True
    
    .. attribute:: session_sender
    
    	Configuration of the TWAMP Session\-Sender logical entity
    	**type**\:   :py:class:`SessionSender <ydk.models.ietf.ietf_twamp.Twamp.SessionSender>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'ietf-twamp'
    _revision = '2017-02-22'

    def __init__(self):
        self.client = None
        self.server = None
        self.session_reflector = None
        self.session_sender = None


    class Client(object):
        """
        Configuration of the TWAMP Control\-Client logical entity.
        
        .. attribute:: admin_state
        
        	Indicates whether the device is allowed to operate as a TWAMP Control\-Client
        	**type**\:  bool
        
        	**mandatory**\: True
        
        .. attribute:: ctrl_connection
        
        	List of TWAMP Control\-Client control connections. Each item in the list describes a control connection that will be initiated by this Control\-Client
        	**type**\: list of    :py:class:`CtrlConnection <ydk.models.ietf.ietf_twamp.Twamp.Client.CtrlConnection>`
        
        .. attribute:: key_chain
        
        	Relates KeyIDs with their respective secret keys in a TWAMP\-Control connection
        	**type**\: list of    :py:class:`KeyChain <ydk.models.ietf.ietf_twamp.Twamp.Client.KeyChain>`
        
        .. attribute:: mode_preference_chain
        
        	Indicates the Control\-Client preferred order of use of the supported TWAMP Modes.  Depending on the Modes available in the TWAMP Server Greeting message (see Fig. 2 of RFC 7717), the this Control\-Client MUST choose the highest priority Mode from the configured mode\-preference\-chain list
        	**type**\: list of    :py:class:`ModePreferenceChain <ydk.models.ietf.ietf_twamp.Twamp.Client.ModePreferenceChain>`
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ietf-twamp'
        _revision = '2017-02-22'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.admin_state = None
            self.ctrl_connection = YList()
            self.ctrl_connection.parent = self
            self.ctrl_connection.name = 'ctrl_connection'
            self.key_chain = YList()
            self.key_chain.parent = self
            self.key_chain.name = 'key_chain'
            self.mode_preference_chain = YList()
            self.mode_preference_chain.parent = self
            self.mode_preference_chain.name = 'mode_preference_chain'


        class ModePreferenceChain(object):
            """
            Indicates the Control\-Client preferred order of use of
            the supported TWAMP Modes.
            
            Depending on the Modes available in the TWAMP Server
            Greeting message (see Fig. 2 of RFC 7717), the
            this Control\-Client MUST choose the highest priority Mode
            from the configured mode\-preference\-chain list.
            
            .. attribute:: priority  <key>
            
            	Indicates the Control\-Client Mode preference priority expressed as a 16\-bit unsigned integer, where zero is the highest priority and subsequent values monotonically increasing
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: mode
            
            	The supported TWAMP Mode matching the corresponding priority
            	**type**\:   :py:class:`TwampModes <ydk.models.ietf.ietf_twamp.TwampModes>`
            
            

            """

            _prefix = 'ietf-twamp'
            _revision = '2017-02-22'

            def __init__(self):
                self.parent = None
                self.priority = None
                self.mode = TwampModes()

            @property
            def _common_path(self):
                if self.priority is None:
                    raise YPYModelError('Key property priority is None')

                return '/ietf-twamp:twamp/ietf-twamp:client/ietf-twamp:mode-preference-chain[ietf-twamp:priority = ' + str(self.priority) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.priority is not None:
                    return True

                if self.mode is not None:
                    if self.mode._has_data():
                        return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_twamp as meta
                return meta._meta_table['Twamp.Client.ModePreferenceChain']['meta_info']


        class KeyChain(object):
            """
            Relates KeyIDs with their respective secret keys
            in a TWAMP\-Control connection.
            
            .. attribute:: key_id  <key>
            
            	KeyID used for a TWAMP\-Control connection. As per Section 3.1 of RFC 4656, KeyID is 'a UTF\-8 string, up to 80 octets in length' and is used to select which 'shared shared secret the [Control\-Client] wishes to use to authenticate or encrypt'
            	**type**\:  str
            
            	**length:** 1..80
            
            .. attribute:: secret_key
            
            	The secret key corresponding to the KeyID for this TWAMP\-Control connection
            	**type**\:  str
            
            

            """

            _prefix = 'ietf-twamp'
            _revision = '2017-02-22'

            def __init__(self):
                self.parent = None
                self.key_id = None
                self.secret_key = None

            @property
            def _common_path(self):
                if self.key_id is None:
                    raise YPYModelError('Key property key_id is None')

                return '/ietf-twamp:twamp/ietf-twamp:client/ietf-twamp:key-chain[ietf-twamp:key-id = ' + str(self.key_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.key_id is not None:
                    return True

                if self.secret_key is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_twamp as meta
                return meta._meta_table['Twamp.Client.KeyChain']['meta_info']


        class CtrlConnection(object):
            """
            List of TWAMP Control\-Client control connections.
            Each item in the list describes a control connection
            that will be initiated by this Control\-Client
            
            .. attribute:: name  <key>
            
            	A unique name used as a key to identify this individual TWAMP\-Control connection on the Control\-Client device
            	**type**\:  str
            
            .. attribute:: client_ip
            
            	The IP address of the local Control\-Client device, to be placed in the source IP address field of the IP header in TWAMP\-Control (TCP) packets belonging to this control connection. If not configured, the device SHALL choose its own source IP address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: client_iv
            
            	Indicates the Control\-Client Initialization Vector (Client\-IV), that is generated randomly by the Control\-Client. As per RFC 4656\:   Client\-IV merely needs to be unique (i.e., it MUST  never be repeated for different sessions using the  same secret key; a simple way to achieve that without  the use of cumbersome state is to generate the  Client\-IV values using a cryptographically secure  pseudo\-random number source.  If the Mode defined in RFC 7717 is selected (selected\-mode), Client\-IV is limited to 12 octets
            	**type**\:  str
            
            	**length:** 16
            
            .. attribute:: client_tcp_port
            
            	Indicates the source TCP port number used in the TWAMP\-Control packets belonging to this control connection
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: control_packet_dscp
            
            	The DSCP value to be placed in the IP header of TWAMP\-Control (TCP) packets generated by this Control\-Client
            	**type**\:  int
            
            	**range:** 0..63
            
            	**default value**\: 0
            
            .. attribute:: key_id
            
            	Indicates the KeyID value selected for this TWAMP\-Control connection
            	**type**\:  str
            
            	**length:** 1..80
            
            .. attribute:: max_count
            
            	This parameter limits the maximum Count value, which MUST be a power of 2 and at least 1024 as per RFC 5357. It is configured by providing said power. For example, configuring 10 here means max count 2^10 = 1024. The default is 15, meaning 2^15 = 32768.  A TWAMP Server uses this configured value in the Server\-Greeting message sent to the Control\-Client.  A TWAMP Control\-Client uses this configured value to prevent denial\-of\-service (DOS) attacks by closing the control connection to the Server if it 'receives a Server\-Greeting message with Count greater that its maximum configured value', as per Section 6 of RFC 5357.  Further, note that according to Section 6 of RFC 5357\:   'If an attacking system sets the maximum value in  Count (2\*\*32), then the system under attack would stall  for a significant period of time while it attempts to  generate keys.   TWAMP\-compliant systems SHOULD have a configuration  control to limit the maximum count value. The default  max\-count value SHOULD be 32768.'  RFC 5357 does not qualify 'significant period' in terms of time, but it is clear that this depends on the processing capacity available and operators need to pay attention to this security consideration
            	**type**\:  int
            
            	**range:** 10..31
            
            	**default value**\: 15
            
            .. attribute:: selected_mode
            
            	The TWAMP Mode that the Control\-Client has chosen for this control connection as set in the Mode field of the Set\-Up\-Response message (RFC 4656, Section 3.1)
            	**type**\:   :py:class:`TwampModes <ydk.models.ietf.ietf_twamp.TwampModes>`
            
            .. attribute:: server_ip
            
            	The IP address of the remote Server device, which the TWAMP\-Control connection will be initiated to
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**mandatory**\: True
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            	**mandatory**\: True
            
            
            ----
            .. attribute:: server_start_time
            
            	Indicates the Start\-Time advertized by the Server in the Server\-Start message (RFC 4656, Section 3.1), representing the time when the current instantiation of the Server started operating. The timestamp format follows RFC 1305 according to Section 4.1.2 of RFC 4656
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: server_tcp_port
            
            	This parameter defines the TCP port number that is to be used by this outgoing TWAMP\-Control connection. Typically, this is the well\-known TWAMP\-Control port number (862) as per RFC 5357 However, there are known realizations of TWAMP in the field that were implemented before this well\-known port number was allocated. These early implementations allowed the port number to be configured. This parameter is therefore provided for backward compatibility reasons
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**default value**\: 862
            
            .. attribute:: state
            
            	Indicates the current state of the TWAMP\-Control connection state
            	**type**\:   :py:class:`ControlClientConnectionStateEnum <ydk.models.ietf.ietf_twamp.ControlClientConnectionStateEnum>`
            
            .. attribute:: test_session_request
            
            	Information associated with the Control\-Client for this test session
            	**type**\: list of    :py:class:`TestSessionRequest <ydk.models.ietf.ietf_twamp.Twamp.Client.CtrlConnection.TestSessionRequest>`
            
            .. attribute:: token
            
            	This parameter holds the 64 octets containing the concatenation of a 16\-octet Challenge, a 16\-octet AES Session\-key used for encryption, and a 32\-octet HMAC\-SHA1 Session\-key used for authentication; see also the last paragraph of Section 6 in RFC 4656.  If the Mode defined in RFC 7717 is selected (selected\-mode), Token is limited to 16 octets
            	**type**\:  str
            
            	**length:** 64
            
            

            """

            _prefix = 'ietf-twamp'
            _revision = '2017-02-22'

            def __init__(self):
                self.parent = None
                self.name = None
                self.client_ip = None
                self.client_iv = None
                self.client_tcp_port = None
                self.control_packet_dscp = None
                self.key_id = None
                self.max_count = None
                self.selected_mode = TwampModes()
                self.server_ip = None
                self.server_start_time = None
                self.server_tcp_port = None
                self.state = None
                self.test_session_request = YList()
                self.test_session_request.parent = self
                self.test_session_request.name = 'test_session_request'
                self.token = None


            class TestSessionRequest(object):
                """
                Information associated with the Control\-Client
                for this test session
                
                .. attribute:: name  <key>
                
                	A unique name to be used for identification of this TWAMP\-Test session on the Control\-Client
                	**type**\:  str
                
                .. attribute:: padding_length
                
                	The number of padding bytes to be added to the TWAMP\-Test (UDP) packets generated by the Session\-Sender.  This value will be placed in the Padding Length field of the Request\-TW\-Session message (RFC 4656, Section 3.5)
                	**type**\:  int
                
                	**range:** 64..4096
                
                .. attribute:: pm_reg_list
                
                	A list of one or more Performance Metric Registry Index values, which communicate packet stream characteristics along with one or more metrics to be measured.  All members of the pm\-reg\-list MUST have the same stream characteristics, such that they combine to specify all metrics that shall be measured on a single stream
                	**type**\: list of    :py:class:`PmRegList <ydk.models.ietf.ietf_twamp.Twamp.Client.CtrlConnection.TestSessionRequest.PmRegList>`
                
                .. attribute:: reflector_ip
                
                	The IP address belonging to the remote Session\-Reflector device to which the TWAMP\-Test session will be initiated. This value will be used to populate the receiver address field of the Request\-TW\-Session message
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**mandatory**\: True
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**mandatory**\: True
                
                
                ----
                .. attribute:: reflector_udp_port
                
                	This parameter defines the UDP port number that will be used by the Session\-Reflector for this TWAMP\-Test session. The number is restricted to the dynamic port range and is to be placed in the Receiver Port field of the Request\-TW\-Session message
                	**type**\:  int
                
                	**range:** 49152..65535
                
                .. attribute:: repeat
                
                	This value determines if the TWAMP\-Test session must be repeated. When a test session has completed, the repeat parameter is checked.  The default value of 0 indicates that the session MUST NOT be repeated.  If the repeat value is 1 through 4,294,967,294 then the test session SHALL be repeated using the information in repeat\-interval parameter, and the parent TWAMP\-Control connection for this test session is restarted to negotiate a new instance of this TWAMP\-Test session. The implementation MUST decrement the value of repeat after determining a repeated session is expected
                	**type**\: one of the below types:
                
                	**type**\:  int
                
                	**range:** 0..4294967294
                
                	**default value**\: 0
                
                
                ----
                	**type**\:   :py:class:`RepeatEnum <ydk.models.ietf.ietf_twamp.Twamp.Client.CtrlConnection.TestSessionRequest.RepeatEnum>`
                
                	**default value**\: 0
                
                
                ----
                .. attribute:: repeat_interval
                
                	Repeat interval (in seconds)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: seconds
                
                	**default value**\: 0
                
                .. attribute:: sender_ip
                
                	The IP address of the Session\-Sender device, which is to be placed in the source IP address field of the IP header in TWAMP\-Test (UDP) packets belonging to this test session. This value will be used to populate the sender address field of the Request\-TW\-Session message.  If not configured, the device SHALL choose its own source IP address
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: sender_udp_port
                
                	The UDP port number that is to be used by the Session\-Sender for this TWAMP\-Test session. The number is restricted to the dynamic port range.  By default the Control\-Client SHALL auto\-allocate a UDP port number for this TWAMP\-Test session.  The configured (or auto\-allocated) value is advertized in the Sender Port field of the Request\-TW\-session message (see Section 3.5 of RFC 5357). Note that in the scenario where a device auto\-allocates a UDP port number for a session, and the repeat parameter for that session indicates that it should be repeated, the device is free to auto\-allocate a different UDP port number when it negotiates the next (repeated) iteration of this session
                	**type**\: one of the below types:
                
                	**type**\:  int
                
                	**range:** 49152..65535
                
                	**default value**\: autoallocate
                
                
                ----
                	**type**\:   :py:class:`SenderUdpPortEnum <ydk.models.ietf.ietf_twamp.Twamp.Client.CtrlConnection.TestSessionRequest.SenderUdpPortEnum>`
                
                	**default value**\: autoallocate
                
                
                ----
                .. attribute:: sid
                
                	The SID allocated by the Server for this TWAMP\-Test session, and communicated back to the Control\-Client in the SID field of the Accept\-Session message; see Section 4.3 of RFC 6038
                	**type**\:  str
                
                .. attribute:: start_time
                
                	Time when the session is to be started (but not before the TWAMP Start\-Sessions command is issued; see Section 3.4 of RFC 5357).  The start\-time value is placed in the Start Time field of the Request\-TW\-Session message.  The timestamp format follows RFC 1305 as per Section 3.5 of RFC 4656.  The default value of 0 indicates that the session will be started as soon as the Start\-Sessions message is received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**default value**\: 0
                
                .. attribute:: state
                
                	Indicates the TWAMP\-Test session state (accepted or indication of an error); see Section 3.5 of RFC 5357
                	**type**\:   :py:class:`TestSessionStateEnum <ydk.models.ietf.ietf_twamp.TestSessionStateEnum>`
                
                .. attribute:: test_packet_dscp
                
                	The DSCP value to be placed in the IP header of TWAMP\-Test packets generated by the Session\-Sender, and in the UDP header of the TWAMP\-Test response packets generated by the Session\-Reflector for this test session.  This value will be placed in the Type\-P Descriptor field of the Request\-TW\-Session message (RFC 5357)
                	**type**\:  int
                
                	**range:** 0..63
                
                	**default value**\: 0
                
                .. attribute:: timeout
                
                	The length of time (in seconds) that the Session\-Reflector should continue to respond to packets belonging to this TWAMP\-Test session after a Stop\-Sessions TWAMP\-Control message has been received (RFC 5357, Section 3.8).  This value will be placed in the Timeout field of the Request\-TW\-Session message
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: seconds
                
                	**default value**\: 2
                
                

                """

                _prefix = 'ietf-twamp'
                _revision = '2017-02-22'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.padding_length = None
                    self.pm_reg_list = YList()
                    self.pm_reg_list.parent = self
                    self.pm_reg_list.name = 'pm_reg_list'
                    self.reflector_ip = None
                    self.reflector_udp_port = None
                    self.repeat = None
                    self.repeat_interval = None
                    self.sender_ip = None
                    self.sender_udp_port = None
                    self.sid = None
                    self.start_time = None
                    self.state = None
                    self.test_packet_dscp = None
                    self.timeout = None

                class RepeatEnum(Enum):
                    """
                    RepeatEnum

                    This value determines if the TWAMP\-Test session must

                    be repeated. When a test session has completed, the

                    repeat parameter is checked.

                    The default value of 0 indicates that the session

                    MUST NOT be repeated.

                    If the repeat value is 1 through 4,294,967,294

                    then the test session SHALL be repeated using the

                    information in repeat\-interval parameter, and the

                    parent TWAMP\-Control connection for this test

                    session is restarted to negotiate a new instance

                    of this TWAMP\-Test session. The implementation

                    MUST decrement the value of repeat after

                    determining a repeated session is expected.

                    .. data:: forever = 0

                    	Indicates that the test session SHALL be

                    	repeated *forever* using the information in

                    	repeat-interval parameter, and SHALL NOT

                    	decrement the value.

                    """

                    forever = 0


                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_twamp as meta
                        return meta._meta_table['Twamp.Client.CtrlConnection.TestSessionRequest.RepeatEnum']


                class SenderUdpPortEnum(Enum):
                    """
                    SenderUdpPortEnum

                    The UDP port number that is to be used by

                    the Session\-Sender for this TWAMP\-Test session.

                    The number is restricted to the dynamic port range.

                    By default the Control\-Client SHALL auto\-allocate a

                    UDP port number for this TWAMP\-Test session.

                    The configured (or auto\-allocated) value is advertized

                    in the Sender Port field of the Request\-TW\-session

                    message (see Section 3.5 of RFC 5357). Note that

                    in the scenario where a device auto\-allocates a UDP

                    port number for a session, and the repeat parameter

                    for that session indicates that it should be

                    repeated, the device is free to auto\-allocate a

                    different UDP port number when it negotiates the

                    next (repeated) iteration of this session.

                    .. data:: autoallocate = 0

                    	Indicates that the Contol-Client will

                    	auto-allocate the TWAMP-Test (UDP) port number

                    	from the dynamic port range.

                    """

                    autoallocate = 0


                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_twamp as meta
                        return meta._meta_table['Twamp.Client.CtrlConnection.TestSessionRequest.SenderUdpPortEnum']



                class PmRegList(object):
                    """
                    A list of one or more Performance Metric Registry
                    Index values, which communicate packet stream
                    characteristics along with one or more metrics
                    to be measured.
                    
                    All members of the pm\-reg\-list MUST have the same
                    stream characteristics, such that they combine
                    to specify all metrics that shall be measured on
                    a single stream.
                    
                    .. attribute:: pm_index  <key>
                    
                    	Numerical index value of a Registered Metric in the Performance Metric Registry (see ietf\-ippm\-metric\-registry). Output statistics are specified in the corresponding Registry entry
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'ietf-twamp'
                    _revision = '2017-02-22'

                    def __init__(self):
                        self.parent = None
                        self.pm_index = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.pm_index is None:
                            raise YPYModelError('Key property pm_index is None')

                        return self.parent._common_path +'/ietf-twamp:pm-reg-list[ietf-twamp:pm-index = ' + str(self.pm_index) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.pm_index is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_twamp as meta
                        return meta._meta_table['Twamp.Client.CtrlConnection.TestSessionRequest.PmRegList']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return self.parent._common_path +'/ietf-twamp:test-session-request[ietf-twamp:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.name is not None:
                        return True

                    if self.padding_length is not None:
                        return True

                    if self.pm_reg_list is not None:
                        for child_ref in self.pm_reg_list:
                            if child_ref._has_data():
                                return True

                    if self.reflector_ip is not None:
                        return True

                    if self.reflector_udp_port is not None:
                        return True

                    if self.repeat is not None:
                        return True

                    if self.repeat_interval is not None:
                        return True

                    if self.sender_ip is not None:
                        return True

                    if self.sender_udp_port is not None:
                        return True

                    if self.sid is not None:
                        return True

                    if self.start_time is not None:
                        return True

                    if self.state is not None:
                        return True

                    if self.test_packet_dscp is not None:
                        return True

                    if self.timeout is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_twamp as meta
                    return meta._meta_table['Twamp.Client.CtrlConnection.TestSessionRequest']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/ietf-twamp:twamp/ietf-twamp:client/ietf-twamp:ctrl-connection[ietf-twamp:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.name is not None:
                    return True

                if self.client_ip is not None:
                    return True

                if self.client_iv is not None:
                    return True

                if self.client_tcp_port is not None:
                    return True

                if self.control_packet_dscp is not None:
                    return True

                if self.key_id is not None:
                    return True

                if self.max_count is not None:
                    return True

                if self.selected_mode is not None:
                    if self.selected_mode._has_data():
                        return True

                if self.server_ip is not None:
                    return True

                if self.server_start_time is not None:
                    return True

                if self.server_tcp_port is not None:
                    return True

                if self.state is not None:
                    return True

                if self.test_session_request is not None:
                    for child_ref in self.test_session_request:
                        if child_ref._has_data():
                            return True

                if self.token is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_twamp as meta
                return meta._meta_table['Twamp.Client.CtrlConnection']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-twamp:twamp/ietf-twamp:client'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self._is_presence:
                return True
            if self.admin_state is not None:
                return True

            if self.ctrl_connection is not None:
                for child_ref in self.ctrl_connection:
                    if child_ref._has_data():
                        return True

            if self.key_chain is not None:
                for child_ref in self.key_chain:
                    if child_ref._has_data():
                        return True

            if self.mode_preference_chain is not None:
                for child_ref in self.mode_preference_chain:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_twamp as meta
            return meta._meta_table['Twamp.Client']['meta_info']


    class Server(object):
        """
        Configuration of the TWAMP Server logical entity.
        
        .. attribute:: admin_state
        
        	Indicates whether the device is allowed to operate as a TWAMP Server
        	**type**\:  bool
        
        	**mandatory**\: True
        
        .. attribute:: control_packet_dscp
        
        	The DSCP value to be placed in the IP header of TWAMP\-Control (TCP) packets generated by the Server.  Section 3.1 of  RFC 5357 specifies that the server SHOULD use the DSCP value from the Control\-Client's TCP SYN. However, for practical purposes TWAMP will typically be implemented using a general purpose TCP stack provided by the underlying operating system, and such a stack may not provide this information to the user. Consequently, it is not always possible to implement the behavior described in RFC 5357 in an OS\-portable version of TWAMP.  The default behavior if this item is not set is to use the DSCP value from the Control\-Client's TCP SYN, as per Section 3.1 of RFC 5357
        	**type**\:  int
        
        	**range:** 0..63
        
        .. attribute:: count
        
        	Parameter communicated to the Control\-Client as part of the Server Greeting message and used for deriving a key from a shared secret as per Section 3.1 of  RFC 4656\:  MUST be a power of 2 and at least 1024; SHOULD be increased as more computing power becomes common
        	**type**\:  int
        
        	**range:** 10..31
        
        	**default value**\: 10
        
        .. attribute:: ctrl_connection
        
        	List of all incoming TWAMP\-Control (TCP) connections
        	**type**\: list of    :py:class:`CtrlConnection <ydk.models.ietf.ietf_twamp.Twamp.Server.CtrlConnection>`
        
        .. attribute:: key_chain
        
        	Relates KeyIDs with their respective secret keys in a TWAMP\-Control connection
        	**type**\: list of    :py:class:`KeyChain <ydk.models.ietf.ietf_twamp.Twamp.Server.KeyChain>`
        
        .. attribute:: max_count
        
        	This parameter limits the maximum Count value, which MUST be a power of 2 and at least 1024 as per RFC 5357. It is configured by providing said power. For example, configuring 10 here means max count 2^10 = 1024. The default is 15, meaning 2^15 = 32768.  A TWAMP Server uses this configured value in the Server\-Greeting message sent to the Control\-Client.  A TWAMP Control\-Client uses this configured value to prevent denial\-of\-service (DOS) attacks by closing the control connection to the Server if it 'receives a Server\-Greeting message with Count greater that its maximum configured value', as per Section 6 of RFC 5357.  Further, note that according to Section 6 of RFC 5357\:   'If an attacking system sets the maximum value in  Count (2\*\*32), then the system under attack would stall  for a significant period of time while it attempts to  generate keys.   TWAMP\-compliant systems SHOULD have a configuration  control to limit the maximum count value. The default  max\-count value SHOULD be 32768.'  RFC 5357 does not qualify 'significant period' in terms of time, but it is clear that this depends on the processing capacity available and operators need to pay attention to this security consideration
        	**type**\:  int
        
        	**range:** 10..31
        
        	**default value**\: 15
        
        .. attribute:: modes
        
        	The bit mask of TWAMP Modes this Server instance is willing to support; see IANA TWAMP Modes Registry
        	**type**\:   :py:class:`TwampModes <ydk.models.ietf.ietf_twamp.TwampModes>`
        
        .. attribute:: server_tcp_port
        
        	This parameter defines the well known TCP port number that is used by TWAMP\-Control. The Server will listen on this port number for incoming TWAMP\-Control connections. Although this is defined as a fixed value (862) in RFC 5357, there are several realizations of TWAMP in the field that were implemented before this well\-known port number was allocated. These early implementations allowed the port number to be configured. This parameter is therefore provided for backward compatibility reasons
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**default value**\: 862
        
        .. attribute:: servwait
        
        	TWAMP\-Control (TCP) session timeout, in seconds. According to Section 3.1 of RFC 5357,   Server MAY discontinue any established control  connection when no packet associated with that  connection has been received within SERVWAIT seconds
        	**type**\:  int
        
        	**range:** 1..604800
        
        	**units**\: seconds
        
        	**default value**\: 900
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ietf-twamp'
        _revision = '2017-02-22'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.admin_state = None
            self.control_packet_dscp = None
            self.count = None
            self.ctrl_connection = YList()
            self.ctrl_connection.parent = self
            self.ctrl_connection.name = 'ctrl_connection'
            self.key_chain = YList()
            self.key_chain.parent = self
            self.key_chain.name = 'key_chain'
            self.max_count = None
            self.modes = TwampModes()
            self.server_tcp_port = None
            self.servwait = None


        class KeyChain(object):
            """
            Relates KeyIDs with their respective secret keys
            in a TWAMP\-Control connection.
            
            .. attribute:: key_id  <key>
            
            	KeyID used for a TWAMP\-Control connection. As per Section 3.1 of RFC 4656, KeyID is 'a UTF\-8 string, up to 80 octets in length' and is used to select which 'shared shared secret the [Control\-Client] wishes to use to authenticate or encrypt'
            	**type**\:  str
            
            	**length:** 1..80
            
            .. attribute:: secret_key
            
            	The secret key corresponding to the KeyID for this TWAMP\-Control connection
            	**type**\:  str
            
            

            """

            _prefix = 'ietf-twamp'
            _revision = '2017-02-22'

            def __init__(self):
                self.parent = None
                self.key_id = None
                self.secret_key = None

            @property
            def _common_path(self):
                if self.key_id is None:
                    raise YPYModelError('Key property key_id is None')

                return '/ietf-twamp:twamp/ietf-twamp:server/ietf-twamp:key-chain[ietf-twamp:key-id = ' + str(self.key_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.key_id is not None:
                    return True

                if self.secret_key is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_twamp as meta
                return meta._meta_table['Twamp.Server.KeyChain']['meta_info']


        class CtrlConnection(object):
            """
            List of all incoming TWAMP\-Control (TCP) connections.
            
            .. attribute:: client_ip  <key>
            
            	The IP address on the remote Control\-Client device, which is the source IP address used in the TWAMP\-Control (TCP) packets belonging to this control connection
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: client_tcp_port  <key>
            
            	The source TCP port number used in the TWAMP\-Control (TCP) packets belonging to this control connection
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: server_ip  <key>
            
            	The IP address of the local Server device, which is the destination IP address used in the TWAMP\-Control (TCP) packets belonging to this control connection
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: server_tcp_port  <key>
            
            	The destination TCP port number used in the TWAMP\-Control (TCP) packets belonging to this control connection. This will usually be the same value as the server\-tcp\-port configured under twamp/server. However, in the event that the user re\-configured server/server\-tcp\-port after this control connection was initiated, this value will indicate the server\-tcp\-port that is actually in use for this control connection
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: challenge
            
            	A random sequence of octets generated by the Server. As described in client/token, Challenge is used by the Control\-Client to prove possession of a shared secret
            	**type**\:  str
            
            	**length:** 16
            
            .. attribute:: control_packet_dscp
            
            	The DSCP value used in the IP header of the TWAMP\-Control (TCP) packets sent by the Server for this control connection. This will usually be the same value as is configured in the control\-packet\-dscp parameter under the twamp/server container.  However, in the event that the user re\-configures server/dscp after this control connection is already in progress, this read\-only value will show the actual dscp value in use by this TWAMP\-Control connection
            	**type**\:  int
            
            	**range:** 0..63
            
            .. attribute:: count
            
            	Parameter communicated to the Control\-Client as part of the Server Greeting message and used for deriving a key from a shared secret as per Section 3.1 of  RFC 4656\:  MUST be a power of 2 and at least 1024; SHOULD be increased as more computing power becomes common
            	**type**\:  int
            
            	**range:** 10..31
            
            	**default value**\: 10
            
            .. attribute:: key_id
            
            	The KeyID value that is in use by this TWAMP\-Control connection as selected by Control\-Client
            	**type**\:  str
            
            	**length:** 1..80
            
            .. attribute:: max_count
            
            	This parameter limits the maximum Count value, which MUST be a power of 2 and at least 1024 as per RFC 5357. It is configured by providing said power. For example, configuring 10 here means max count 2^10 = 1024. The default is 15, meaning 2^15 = 32768.  A TWAMP Server uses this configured value in the Server\-Greeting message sent to the Control\-Client.  A TWAMP Control\-Client uses this configured value to prevent denial\-of\-service (DOS) attacks by closing the control connection to the Server if it 'receives a Server\-Greeting message with Count greater that its maximum configured value', as per Section 6 of RFC 5357.  Further, note that according to Section 6 of RFC 5357\:   'If an attacking system sets the maximum value in  Count (2\*\*32), then the system under attack would stall  for a significant period of time while it attempts to  generate keys.   TWAMP\-compliant systems SHOULD have a configuration  control to limit the maximum count value. The default  max\-count value SHOULD be 32768.'  RFC 5357 does not qualify 'significant period' in terms of time, but it is clear that this depends on the processing capacity available and operators need to pay attention to this security consideration
            	**type**\:  int
            
            	**range:** 10..31
            
            	**default value**\: 15
            
            .. attribute:: salt
            
            	A parameter used in deriving a key from a shared secret as described in Section 3.1 of RFC 4656. It is communicated to the Control\-Client as part of the Server Greeting message
            	**type**\:  str
            
            	**length:** 16
            
            .. attribute:: selected_mode
            
            	The Mode that was chosen for this TWAMP\-Control connection as set in the Mode field of the Set\-Up\-Response message
            	**type**\:   :py:class:`TwampModes <ydk.models.ietf.ietf_twamp.TwampModes>`
            
            .. attribute:: server_iv
            
            	The Server Initialization Vector (IV) generated randomly by the Server
            	**type**\:  str
            
            	**length:** 16
            
            .. attribute:: state
            
            	Indicates the Server TWAMP\-Control connection state
            	**type**\:   :py:class:`ServerCtrlConnectionStateEnum <ydk.models.ietf.ietf_twamp.ServerCtrlConnectionStateEnum>`
            
            

            """

            _prefix = 'ietf-twamp'
            _revision = '2017-02-22'

            def __init__(self):
                self.parent = None
                self.client_ip = None
                self.client_tcp_port = None
                self.server_ip = None
                self.server_tcp_port = None
                self.challenge = None
                self.control_packet_dscp = None
                self.count = None
                self.key_id = None
                self.max_count = None
                self.salt = None
                self.selected_mode = TwampModes()
                self.server_iv = None
                self.state = None

            @property
            def _common_path(self):
                if self.client_ip is None:
                    raise YPYModelError('Key property client_ip is None')
                if self.client_tcp_port is None:
                    raise YPYModelError('Key property client_tcp_port is None')
                if self.server_ip is None:
                    raise YPYModelError('Key property server_ip is None')
                if self.server_tcp_port is None:
                    raise YPYModelError('Key property server_tcp_port is None')

                return '/ietf-twamp:twamp/ietf-twamp:server/ietf-twamp:ctrl-connection[ietf-twamp:client-ip = ' + str(self.client_ip) + '][ietf-twamp:client-tcp-port = ' + str(self.client_tcp_port) + '][ietf-twamp:server-ip = ' + str(self.server_ip) + '][ietf-twamp:server-tcp-port = ' + str(self.server_tcp_port) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.client_ip is not None:
                    return True

                if self.client_tcp_port is not None:
                    return True

                if self.server_ip is not None:
                    return True

                if self.server_tcp_port is not None:
                    return True

                if self.challenge is not None:
                    return True

                if self.control_packet_dscp is not None:
                    return True

                if self.count is not None:
                    return True

                if self.key_id is not None:
                    return True

                if self.max_count is not None:
                    return True

                if self.salt is not None:
                    return True

                if self.selected_mode is not None:
                    if self.selected_mode._has_data():
                        return True

                if self.server_iv is not None:
                    return True

                if self.state is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_twamp as meta
                return meta._meta_table['Twamp.Server.CtrlConnection']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-twamp:twamp/ietf-twamp:server'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self._is_presence:
                return True
            if self.admin_state is not None:
                return True

            if self.control_packet_dscp is not None:
                return True

            if self.count is not None:
                return True

            if self.ctrl_connection is not None:
                for child_ref in self.ctrl_connection:
                    if child_ref._has_data():
                        return True

            if self.key_chain is not None:
                for child_ref in self.key_chain:
                    if child_ref._has_data():
                        return True

            if self.max_count is not None:
                return True

            if self.modes is not None:
                if self.modes._has_data():
                    return True

            if self.server_tcp_port is not None:
                return True

            if self.servwait is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_twamp as meta
            return meta._meta_table['Twamp.Server']['meta_info']


    class SessionSender(object):
        """
        Configuration of the TWAMP Session\-Sender logical entity
        
        .. attribute:: admin_state
        
        	Indicates whether the device is allowed to operate as a TWAMP Session\-Sender
        	**type**\:  bool
        
        	**mandatory**\: True
        
        .. attribute:: test_session
        
        	List of TWAMP Session\-Sender test sessions
        	**type**\: list of    :py:class:`TestSession <ydk.models.ietf.ietf_twamp.Twamp.SessionSender.TestSession>`
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ietf-twamp'
        _revision = '2017-02-22'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.admin_state = None
            self.test_session = YList()
            self.test_session.parent = self
            self.test_session.name = 'test_session'


        class TestSession(object):
            """
            List of TWAMP Session\-Sender test sessions.
            
            .. attribute:: name  <key>
            
            	A unique name for this TWAMP\-Test session to be used for identifying this test session by the Session\-Sender logical entity
            	**type**\:  str
            
            .. attribute:: ctrl_connection_name
            
            	The name of the parent TWAMP\-Control connection that is responsible for negotiating this TWAMP\-Test session
            	**type**\:  str
            
            .. attribute:: fill_mode
            
            	Indicates whether the padding added to the TWAMP\-Test (UDP) packets will contain pseudo\-random numbers, or whether it should consist of all zeroes, as per Section 4.2.1 of RFC 5357
            	**type**\:   :py:class:`PaddingFillModeEnum <ydk.models.ietf.ietf_twamp.PaddingFillModeEnum>`
            
            	**default value**\: zero
            
            .. attribute:: lambda_
            
            	Indicates the average time interval (in seconds) between packets in the Poisson distribution. The packet is calculated using the reciprocal of lambda and the TWAMP\-Test packet size (which depends on the selected Mode and the packet padding)
            	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
            
            	**range:** \-92233720368547.75808..92233720368547.75807
            
            	**mandatory**\: True
            
            	**units**\: seconds
            
            .. attribute:: last_rcv_seq
            
            	Indicates the last received sequence number
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: last_sent_seq
            
            	Indicates the last sent sequence number
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: max_interval
            
            	Indicates the maximum time (in seconds) between packet transmissions
            	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
            
            	**range:** \-92233720368547.75808..92233720368547.75807
            
            	**units**\: seconds
            
            .. attribute:: number_of_packets
            
            	The overall number of TWAMP\-Test (UDP) packets to be transmitted by the Session\-Sender for this test session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**mandatory**\: True
            
            .. attribute:: periodic_interval
            
            	Indicates the time to wait (in seconds) between the first bits of TWAMP\-Test (UDP) packet transmissions for this test session
            	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
            
            	**range:** \-92233720368547.75808..92233720368547.75807
            
            	**mandatory**\: True
            
            	**units**\: seconds
            
            .. attribute:: rcv_packets
            
            	Indicates the number of packets received
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sent_packets
            
            	Indicates the number of packets sent
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: state
            
            	Indicates the Session\-Sender test session state
            	**type**\:   :py:class:`SenderSessionStateEnum <ydk.models.ietf.ietf_twamp.SenderSessionStateEnum>`
            
            

            """

            _prefix = 'ietf-twamp'
            _revision = '2017-02-22'

            def __init__(self):
                self.parent = None
                self.name = None
                self.ctrl_connection_name = None
                self.fill_mode = None
                self.lambda_ = None
                self.last_rcv_seq = None
                self.last_sent_seq = None
                self.max_interval = None
                self.number_of_packets = None
                self.periodic_interval = None
                self.rcv_packets = None
                self.sent_packets = None
                self.state = None

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/ietf-twamp:twamp/ietf-twamp:session-sender/ietf-twamp:test-session[ietf-twamp:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.name is not None:
                    return True

                if self.ctrl_connection_name is not None:
                    return True

                if self.fill_mode is not None:
                    return True

                if self.lambda_ is not None:
                    return True

                if self.last_rcv_seq is not None:
                    return True

                if self.last_sent_seq is not None:
                    return True

                if self.max_interval is not None:
                    return True

                if self.number_of_packets is not None:
                    return True

                if self.periodic_interval is not None:
                    return True

                if self.rcv_packets is not None:
                    return True

                if self.sent_packets is not None:
                    return True

                if self.state is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_twamp as meta
                return meta._meta_table['Twamp.SessionSender.TestSession']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-twamp:twamp/ietf-twamp:session-sender'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self._is_presence:
                return True
            if self.admin_state is not None:
                return True

            if self.test_session is not None:
                for child_ref in self.test_session:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_twamp as meta
            return meta._meta_table['Twamp.SessionSender']['meta_info']


    class SessionReflector(object):
        """
        Configuration of the TWAMP Session\-Reflector logical entity
        
        .. attribute:: admin_state
        
        	Indicates whether the device is allowed to operate as a TWAMP Session\-Reflector
        	**type**\:  bool
        
        	**mandatory**\: True
        
        .. attribute:: refwait
        
        	The Session\-Reflector MAY discontinue any session that has been started when no packet associated with that session has been received for REFWAIT seconds. As per Section 3.1 of RFC 5357, this timeout allows a Session\-Reflector to free up resources in case of failure
        	**type**\:  int
        
        	**range:** 1..604800
        
        	**units**\: seconds
        
        	**default value**\: 900
        
        .. attribute:: test_session
        
        	TWAMP Session\-Reflectortest sessions
        	**type**\: list of    :py:class:`TestSession <ydk.models.ietf.ietf_twamp.Twamp.SessionReflector.TestSession>`
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ietf-twamp'
        _revision = '2017-02-22'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.admin_state = None
            self.refwait = None
            self.test_session = YList()
            self.test_session.parent = self
            self.test_session.name = 'test_session'


        class TestSession(object):
            """
            TWAMP Session\-Reflectortest sessions.
            
            .. attribute:: reflector_ip  <key>
            
            	The IP address of the local Session\-Reflector device, which is the destination IP address used in the TWAMP\-Test (UDP) packets belonging to this test session
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: reflector_udp_port  <key>
            
            	The destination UDP port number used in the TWAMP\-Test (UDP) test packets belonging to this test session
            	**type**\:  int
            
            	**range:** 49152..65535
            
            .. attribute:: sender_ip  <key>
            
            	The IP address on the remote device, which is the source IP address used in the TWAMP\-Test (UDP) packets belonging to this test session
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: sender_udp_port  <key>
            
            	The source UDP port used in the TWAMP\-Test packets belonging to this test session
            	**type**\:  int
            
            	**range:** 49152..65535
            
            .. attribute:: last_rcv_seq
            
            	Indicates the last received sequence number
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: last_sent_seq
            
            	Indicates the last sent sequence number
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: parent_connection_client_ip
            
            	The IP address on the Control\-Client device, which is the source IP address used in the TWAMP\-Control (TCP) packets belonging to the parent control connection that negotiated this test session
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: parent_connection_client_tcp_port
            
            	The source TCP port number used in the TWAMP\-Control (TCP) packets belonging to the parent control connection that negotiated this test session
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: parent_connection_server_ip
            
            	The IP address of the Server device, which is the destination IP address used in the TWAMP\-Control (TCP) packets belonging to the parent control connection that negotiated this test session
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: parent_connection_server_tcp_port
            
            	The destination TCP port number used in the TWAMP\-Control (TCP) packets belonging to the parent control connection that negotiated this test session
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: rcv_packets
            
            	Indicates the number of packets received
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sent_packets
            
            	Indicates the number of packets sent
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sid
            
            	An auto\-allocated identifier for this TWAMP\-Test session that is unique within the context of this Server/Session\-Reflector device only. This value is communicated to the Control\-Client that requested the test session in the SID field of the Accept\-Session message
            	**type**\:  str
            
            .. attribute:: test_packet_dscp
            
            	The DSCP value present in the IP header of TWAMP\-Test (UDP) packets belonging to this session
            	**type**\:  int
            
            	**range:** 0..63
            
            

            """

            _prefix = 'ietf-twamp'
            _revision = '2017-02-22'

            def __init__(self):
                self.parent = None
                self.reflector_ip = None
                self.reflector_udp_port = None
                self.sender_ip = None
                self.sender_udp_port = None
                self.last_rcv_seq = None
                self.last_sent_seq = None
                self.parent_connection_client_ip = None
                self.parent_connection_client_tcp_port = None
                self.parent_connection_server_ip = None
                self.parent_connection_server_tcp_port = None
                self.rcv_packets = None
                self.sent_packets = None
                self.sid = None
                self.test_packet_dscp = None

            @property
            def _common_path(self):
                if self.reflector_ip is None:
                    raise YPYModelError('Key property reflector_ip is None')
                if self.reflector_udp_port is None:
                    raise YPYModelError('Key property reflector_udp_port is None')
                if self.sender_ip is None:
                    raise YPYModelError('Key property sender_ip is None')
                if self.sender_udp_port is None:
                    raise YPYModelError('Key property sender_udp_port is None')

                return '/ietf-twamp:twamp/ietf-twamp:session-reflector/ietf-twamp:test-session[ietf-twamp:reflector-ip = ' + str(self.reflector_ip) + '][ietf-twamp:reflector-udp-port = ' + str(self.reflector_udp_port) + '][ietf-twamp:sender-ip = ' + str(self.sender_ip) + '][ietf-twamp:sender-udp-port = ' + str(self.sender_udp_port) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.reflector_ip is not None:
                    return True

                if self.reflector_udp_port is not None:
                    return True

                if self.sender_ip is not None:
                    return True

                if self.sender_udp_port is not None:
                    return True

                if self.last_rcv_seq is not None:
                    return True

                if self.last_sent_seq is not None:
                    return True

                if self.parent_connection_client_ip is not None:
                    return True

                if self.parent_connection_client_tcp_port is not None:
                    return True

                if self.parent_connection_server_ip is not None:
                    return True

                if self.parent_connection_server_tcp_port is not None:
                    return True

                if self.rcv_packets is not None:
                    return True

                if self.sent_packets is not None:
                    return True

                if self.sid is not None:
                    return True

                if self.test_packet_dscp is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_twamp as meta
                return meta._meta_table['Twamp.SessionReflector.TestSession']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-twamp:twamp/ietf-twamp:session-reflector'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self._is_presence:
                return True
            if self.admin_state is not None:
                return True

            if self.refwait is not None:
                return True

            if self.test_session is not None:
                for child_ref in self.test_session:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_twamp as meta
            return meta._meta_table['Twamp.SessionReflector']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-twamp:twamp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.client is not None and self.client._has_data():
            return True

        if self.server is not None and self.server._has_data():
            return True

        if self.session_reflector is not None and self.session_reflector._has_data():
            return True

        if self.session_sender is not None and self.session_sender._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_twamp as meta
        return meta._meta_table['Twamp']['meta_info']



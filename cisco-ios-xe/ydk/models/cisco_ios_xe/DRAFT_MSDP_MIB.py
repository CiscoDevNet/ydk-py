""" DRAFT_MSDP_MIB 

An experimental MIB module for MSDP Management.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class DraftMsdpMib(object):
    """
    
    
    .. attribute:: msdp
    
    	
    	**type**\:   :py:class:`Msdp <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DraftMsdpMib.Msdp>`
    
    .. attribute:: msdppeertable
    
    	The (conceptual) table listing the MSDP speaker's peers
    	**type**\:   :py:class:`Msdppeertable <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DraftMsdpMib.Msdppeertable>`
    
    .. attribute:: msdprequeststable
    
    	The (conceptual) table listing group ranges and MSDP peers used when deciding where to send an SA Request message when required.  If SA Caching is enabled, this table may be empty
    	**type**\:   :py:class:`Msdprequeststable <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DraftMsdpMib.Msdprequeststable>`
    
    .. attribute:: msdpsacachetable
    
    	The (conceptual) table listing the MSDP SA advertisements currently in the MSDP speaker's cache
    	**type**\:   :py:class:`Msdpsacachetable <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DraftMsdpMib.Msdpsacachetable>`
    
    

    """

    _prefix = 'DRAFT-MSDP-MIB'
    _revision = '1999-12-16'

    def __init__(self):
        self.msdp = DraftMsdpMib.Msdp()
        self.msdp.parent = self
        self.msdppeertable = DraftMsdpMib.Msdppeertable()
        self.msdppeertable.parent = self
        self.msdprequeststable = DraftMsdpMib.Msdprequeststable()
        self.msdprequeststable.parent = self
        self.msdpsacachetable = DraftMsdpMib.Msdpsacachetable()
        self.msdpsacachetable.parent = self


    class Msdp(object):
        """
        
        
        .. attribute:: msdpcachelifetime
        
        	The lifetime given to SA cache entries when created or refreshed.  A value of 0 means no SA caching is done by this MSDP speaker
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: msdpenabled
        
        	The state of MSDP on this MSDP speaker \- globally enabled or disabled
        	**type**\:  bool
        
        .. attribute:: msdpnumsacacheentries
        
        	The total number of entries in the SA Cache table
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: msdpsaholddownperiod
        
        	The number of seconds in the MSDP SA Hold\-down period
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        	**units**\: seconds
        
        

        """

        _prefix = 'DRAFT-MSDP-MIB'
        _revision = '1999-12-16'

        def __init__(self):
            self.parent = None
            self.msdpcachelifetime = None
            self.msdpenabled = None
            self.msdpnumsacacheentries = None
            self.msdpsaholddownperiod = None

        @property
        def _common_path(self):

            return '/DRAFT-MSDP-MIB:DRAFT-MSDP-MIB/DRAFT-MSDP-MIB:msdp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.msdpcachelifetime is not None:
                return True

            if self.msdpenabled is not None:
                return True

            if self.msdpnumsacacheentries is not None:
                return True

            if self.msdpsaholddownperiod is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DRAFT_MSDP_MIB as meta
            return meta._meta_table['DraftMsdpMib.Msdp']['meta_info']


    class Msdprequeststable(object):
        """
        The (conceptual) table listing group ranges and MSDP
        peers used when deciding where to send an SA Request
        message when required.  If SA Caching is enabled, this
        table may be empty.
        
        .. attribute:: msdprequestsentry
        
        	An entry (conceptual row) representing a group range used when deciding where to send an SA Request message
        	**type**\: list of    :py:class:`Msdprequestsentry <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DraftMsdpMib.Msdprequeststable.Msdprequestsentry>`
        
        

        """

        _prefix = 'DRAFT-MSDP-MIB'
        _revision = '1999-12-16'

        def __init__(self):
            self.parent = None
            self.msdprequestsentry = YList()
            self.msdprequestsentry.parent = self
            self.msdprequestsentry.name = 'msdprequestsentry'


        class Msdprequestsentry(object):
            """
            An entry (conceptual row) representing a group range
            used when deciding where to send an SA Request
            message.
            
            .. attribute:: msdprequestsgroupaddress  <key>
            
            	The group address that, when combined with the mask in this entry, represents the group range for which this peer will service MSDP SA Requests
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdprequestsgroupmask  <key>
            
            	The mask that, when combined with the group address in this entry, represents the group range for which this peer will service MSDP SA Requests
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdprequestspeer
            
            	The peer to which MSDP SA Requests for groups matching this entry's group range will be sent.  Must match the INDEX of a row in the msdpPeerTable
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdprequestsstatus
            
            	The status of this row, by which new rows may be added to the table
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            

            """

            _prefix = 'DRAFT-MSDP-MIB'
            _revision = '1999-12-16'

            def __init__(self):
                self.parent = None
                self.msdprequestsgroupaddress = None
                self.msdprequestsgroupmask = None
                self.msdprequestspeer = None
                self.msdprequestsstatus = None

            @property
            def _common_path(self):
                if self.msdprequestsgroupaddress is None:
                    raise YPYModelError('Key property msdprequestsgroupaddress is None')
                if self.msdprequestsgroupmask is None:
                    raise YPYModelError('Key property msdprequestsgroupmask is None')

                return '/DRAFT-MSDP-MIB:DRAFT-MSDP-MIB/DRAFT-MSDP-MIB:msdpRequestsTable/DRAFT-MSDP-MIB:msdpRequestsEntry[DRAFT-MSDP-MIB:msdpRequestsGroupAddress = ' + str(self.msdprequestsgroupaddress) + '][DRAFT-MSDP-MIB:msdpRequestsGroupMask = ' + str(self.msdprequestsgroupmask) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.msdprequestsgroupaddress is not None:
                    return True

                if self.msdprequestsgroupmask is not None:
                    return True

                if self.msdprequestspeer is not None:
                    return True

                if self.msdprequestsstatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DRAFT_MSDP_MIB as meta
                return meta._meta_table['DraftMsdpMib.Msdprequeststable.Msdprequestsentry']['meta_info']

        @property
        def _common_path(self):

            return '/DRAFT-MSDP-MIB:DRAFT-MSDP-MIB/DRAFT-MSDP-MIB:msdpRequestsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.msdprequestsentry is not None:
                for child_ref in self.msdprequestsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DRAFT_MSDP_MIB as meta
            return meta._meta_table['DraftMsdpMib.Msdprequeststable']['meta_info']


    class Msdppeertable(object):
        """
        The (conceptual) table listing the MSDP speaker's
        peers.
        
        .. attribute:: msdppeerentry
        
        	An entry (conceptual row) representing an MSDP peer
        	**type**\: list of    :py:class:`Msdppeerentry <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DraftMsdpMib.Msdppeertable.Msdppeerentry>`
        
        

        """

        _prefix = 'DRAFT-MSDP-MIB'
        _revision = '1999-12-16'

        def __init__(self):
            self.parent = None
            self.msdppeerentry = YList()
            self.msdppeerentry.parent = self
            self.msdppeerentry.name = 'msdppeerentry'


        class Msdppeerentry(object):
            """
            An entry (conceptual row) representing an MSDP peer.
            
            .. attribute:: msdppeerremoteaddress  <key>
            
            	The address of the remote MSDP peer
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdppeerconnectionattempts
            
            	The number of times the state machine has transitioned from inactive to connecting
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerconnectretryinterval
            
            	Time interval in seconds for the ConnectRetry timer
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**units**\: seconds
            
            .. attribute:: msdppeerdatattl
            
            	The minimum TTL a packet is required to have before it may be forwarded using SA encapsulation to this peer
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: msdppeerencapsulationstate
            
            	The status of the encapsulation negotiation state machine
            	**type**\:   :py:class:`MsdppeerencapsulationstateEnum <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DraftMsdpMib.Msdppeertable.Msdppeerentry.MsdppeerencapsulationstateEnum>`
            
            .. attribute:: msdppeerencapsulationtype
            
            	The encapsulation in use when encapsulating data in SA messages to this peer
            	**type**\:   :py:class:`MsdppeerencapsulationtypeEnum <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DraftMsdpMib.Msdppeertable.Msdppeerentry.MsdppeerencapsulationtypeEnum>`
            
            .. attribute:: msdppeerfsmestablishedtime
            
            	This timer indicates how long (in seconds) this peer has been in the Established state or how long since this peer was last in the Established state.  It is set to zero when a new peer is configured or the MSDP speaker is booted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: msdppeerfsmestablishedtransitions
            
            	The total number of times the MSDP FSM transitioned into the established state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerholdtimeconfigured
            
            	Time interval in seconds for the Hold Timer configured for this MSDP speaker with this peer
            	**type**\:  int
            
            	**range:** 0..None \| 3..65535
            
            	**units**\: seconds
            
            .. attribute:: msdppeerincontrolmessages
            
            	The total number of MSDP messages received on this TCP connection.  This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerindatapackets
            
            	The total number of encapsulated data packets received from this peer.  This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerinmessageelapsedtime
            
            	Elapsed time in seconds since the last MSDP message was received from the peer.  Each time msdpPeerInControlMessages is incremented, the value of this object is set to zero (0)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: msdppeerinnotifications
            
            	The number of MSDP Notification messages received on this connection.  This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerinsarequests
            
            	The number of MSDP SA\-Request messages received on this connection.  This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerinsaresponses
            
            	The number of MSDP SA\-Response messages received on this connection.  This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerinsas
            
            	The number of MSDP SA messages received on this connection.  This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerkeepaliveconfigured
            
            	Time interval in seconds for the KeepAlive timer configured for this MSDP speaker with this peer.  A reasonable maximum value for this timer would be configured to be one third of that of msdpPeerHoldTimeConfigured.  If the value of this object is zero (0), no periodic KEEPALIVE messages are sent to the peer after the MSDP connection has been established
            	**type**\:  int
            
            	**range:** 0..21845
            
            	**units**\: seconds
            
            .. attribute:: msdppeerlasterror
            
            	The last error code and subcode seen by this peer on this connection.  If no error has occurred, this field is zero.  Otherwise, the first byte of this two byte OCTET STRING contains the error code, and the second byte contains the subcode
            	**type**\:  str
            
            	**length:** 2
            
            .. attribute:: msdppeerlocaladdress
            
            	The local IP address of this entry's MSDP connection
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdppeerlocalport
            
            	The local port for the TCP connection between the MSDP peers
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: msdppeeroutcontrolmessages
            
            	The total number of MSDP messages transmitted on this TCP connection.  This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeeroutdatapackets
            
            	The total number of encapsulated data packets sent to this peer.  This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeeroutnotifications
            
            	The number of MSDP Notification messages transmitted on this connection.  This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeeroutsarequests
            
            	The number of MSDP SA\-Request messages transmitted on this connection.  This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeeroutsaresponses
            
            	The number of MSDP SA Response messages transmitted on this TCP connection.  This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeeroutsas
            
            	The number of MSDP SA messages transmitted on this connection.  This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerprocessrequestsfrom
            
            	This object indicates whether or not to process MSDP SA Request messages from this peer.  If True(1), MSDP SA Request messages from this peer are processed and replied to (if appropriate) with SA Response messages. If False(2), MSDP SA Request messages from this peer are silently ignored.  It defaults to False when msdpCacheLifetime is 0 and True when msdpCacheLifetime is non\-0
            	**type**\:  bool
            
            .. attribute:: msdppeerremoteport
            
            	The remote port for the TCP connection between the MSDP peers
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: msdppeerrpffailures
            
            	The number of RPF failures on SA messages received from this peer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeersaadvperiod
            
            	Time interval in seconds for the MinSAAdvertisementInterval MSDP timer
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**units**\: seconds
            
            .. attribute:: msdppeerstate
            
            	The state of the MSDP TCP connection with this peer
            	**type**\:   :py:class:`MsdppeerstateEnum <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DraftMsdpMib.Msdppeertable.Msdppeerentry.MsdppeerstateEnum>`
            
            .. attribute:: msdppeerstatus
            
            	The RowStatus object by which peers can be added and deleted.  A transition to 'active' will cause the MSDP Start Event to be generated.  A transition out of the 'active' state will cause the MSDP Stop Event to be generated.  Care should be used in providing write access to this object without adequate authentication
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            

            """

            _prefix = 'DRAFT-MSDP-MIB'
            _revision = '1999-12-16'

            def __init__(self):
                self.parent = None
                self.msdppeerremoteaddress = None
                self.msdppeerconnectionattempts = None
                self.msdppeerconnectretryinterval = None
                self.msdppeerdatattl = None
                self.msdppeerencapsulationstate = None
                self.msdppeerencapsulationtype = None
                self.msdppeerfsmestablishedtime = None
                self.msdppeerfsmestablishedtransitions = None
                self.msdppeerholdtimeconfigured = None
                self.msdppeerincontrolmessages = None
                self.msdppeerindatapackets = None
                self.msdppeerinmessageelapsedtime = None
                self.msdppeerinnotifications = None
                self.msdppeerinsarequests = None
                self.msdppeerinsaresponses = None
                self.msdppeerinsas = None
                self.msdppeerkeepaliveconfigured = None
                self.msdppeerlasterror = None
                self.msdppeerlocaladdress = None
                self.msdppeerlocalport = None
                self.msdppeeroutcontrolmessages = None
                self.msdppeeroutdatapackets = None
                self.msdppeeroutnotifications = None
                self.msdppeeroutsarequests = None
                self.msdppeeroutsaresponses = None
                self.msdppeeroutsas = None
                self.msdppeerprocessrequestsfrom = None
                self.msdppeerremoteport = None
                self.msdppeerrpffailures = None
                self.msdppeersaadvperiod = None
                self.msdppeerstate = None
                self.msdppeerstatus = None

            class MsdppeerencapsulationstateEnum(Enum):
                """
                MsdppeerencapsulationstateEnum

                The status of the encapsulation negotiation state

                machine.

                .. data:: default = 1

                .. data:: received = 2

                .. data:: advertising = 3

                .. data:: sent = 4

                .. data:: agreed = 5

                .. data:: failed = 6

                """

                default = 1

                received = 2

                advertising = 3

                sent = 4

                agreed = 5

                failed = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DRAFT_MSDP_MIB as meta
                    return meta._meta_table['DraftMsdpMib.Msdppeertable.Msdppeerentry.MsdppeerencapsulationstateEnum']


            class MsdppeerencapsulationtypeEnum(Enum):
                """
                MsdppeerencapsulationtypeEnum

                The encapsulation in use when encapsulating data in

                SA messages to this peer.

                .. data:: tcp = 1

                .. data:: udp = 2

                .. data:: gre = 3

                """

                tcp = 1

                udp = 2

                gre = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DRAFT_MSDP_MIB as meta
                    return meta._meta_table['DraftMsdpMib.Msdppeertable.Msdppeerentry.MsdppeerencapsulationtypeEnum']


            class MsdppeerstateEnum(Enum):
                """
                MsdppeerstateEnum

                The state of the MSDP TCP connection with this peer.

                .. data:: inactive = 1

                .. data:: listen = 2

                .. data:: connecting = 3

                .. data:: established = 4

                .. data:: disabled = 5

                """

                inactive = 1

                listen = 2

                connecting = 3

                established = 4

                disabled = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DRAFT_MSDP_MIB as meta
                    return meta._meta_table['DraftMsdpMib.Msdppeertable.Msdppeerentry.MsdppeerstateEnum']


            @property
            def _common_path(self):
                if self.msdppeerremoteaddress is None:
                    raise YPYModelError('Key property msdppeerremoteaddress is None')

                return '/DRAFT-MSDP-MIB:DRAFT-MSDP-MIB/DRAFT-MSDP-MIB:msdpPeerTable/DRAFT-MSDP-MIB:msdpPeerEntry[DRAFT-MSDP-MIB:msdpPeerRemoteAddress = ' + str(self.msdppeerremoteaddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.msdppeerremoteaddress is not None:
                    return True

                if self.msdppeerconnectionattempts is not None:
                    return True

                if self.msdppeerconnectretryinterval is not None:
                    return True

                if self.msdppeerdatattl is not None:
                    return True

                if self.msdppeerencapsulationstate is not None:
                    return True

                if self.msdppeerencapsulationtype is not None:
                    return True

                if self.msdppeerfsmestablishedtime is not None:
                    return True

                if self.msdppeerfsmestablishedtransitions is not None:
                    return True

                if self.msdppeerholdtimeconfigured is not None:
                    return True

                if self.msdppeerincontrolmessages is not None:
                    return True

                if self.msdppeerindatapackets is not None:
                    return True

                if self.msdppeerinmessageelapsedtime is not None:
                    return True

                if self.msdppeerinnotifications is not None:
                    return True

                if self.msdppeerinsarequests is not None:
                    return True

                if self.msdppeerinsaresponses is not None:
                    return True

                if self.msdppeerinsas is not None:
                    return True

                if self.msdppeerkeepaliveconfigured is not None:
                    return True

                if self.msdppeerlasterror is not None:
                    return True

                if self.msdppeerlocaladdress is not None:
                    return True

                if self.msdppeerlocalport is not None:
                    return True

                if self.msdppeeroutcontrolmessages is not None:
                    return True

                if self.msdppeeroutdatapackets is not None:
                    return True

                if self.msdppeeroutnotifications is not None:
                    return True

                if self.msdppeeroutsarequests is not None:
                    return True

                if self.msdppeeroutsaresponses is not None:
                    return True

                if self.msdppeeroutsas is not None:
                    return True

                if self.msdppeerprocessrequestsfrom is not None:
                    return True

                if self.msdppeerremoteport is not None:
                    return True

                if self.msdppeerrpffailures is not None:
                    return True

                if self.msdppeersaadvperiod is not None:
                    return True

                if self.msdppeerstate is not None:
                    return True

                if self.msdppeerstatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DRAFT_MSDP_MIB as meta
                return meta._meta_table['DraftMsdpMib.Msdppeertable.Msdppeerentry']['meta_info']

        @property
        def _common_path(self):

            return '/DRAFT-MSDP-MIB:DRAFT-MSDP-MIB/DRAFT-MSDP-MIB:msdpPeerTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.msdppeerentry is not None:
                for child_ref in self.msdppeerentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DRAFT_MSDP_MIB as meta
            return meta._meta_table['DraftMsdpMib.Msdppeertable']['meta_info']


    class Msdpsacachetable(object):
        """
        The (conceptual) table listing the MSDP SA
        advertisements currently in the MSDP speaker's cache.
        
        .. attribute:: msdpsacacheentry
        
        	An entry (conceptual row) representing an MSDP SA advert
        	**type**\: list of    :py:class:`Msdpsacacheentry <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DraftMsdpMib.Msdpsacachetable.Msdpsacacheentry>`
        
        

        """

        _prefix = 'DRAFT-MSDP-MIB'
        _revision = '1999-12-16'

        def __init__(self):
            self.parent = None
            self.msdpsacacheentry = YList()
            self.msdpsacacheentry.parent = self
            self.msdpsacacheentry.name = 'msdpsacacheentry'


        class Msdpsacacheentry(object):
            """
            An entry (conceptual row) representing an MSDP SA
            advert.
            
            .. attribute:: msdpsacachegroupaddr  <key>
            
            	The group address of the SA Cache entry
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdpsacachesourceaddr  <key>
            
            	The source address of the SA Cache entry
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdpsacacheoriginrp  <key>
            
            	The address of the RP which originated the last SA message accepted for this entry
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdpsacacheexpirytime
            
            	The time remaining before this entry will expire from the SA cache
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdpsacacheindatapackets
            
            	The number of MSDP encapsulated data packets received relevant to this cache entry.  This object must be initialized to zero when creating a cache entry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdpsacacheinsas
            
            	The number of MSDP SA messages received relevant to this cache entry.  This object must be initialized to zero when creating a cache entry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdpsacachepeerlearnedfrom
            
            	The peer from which this SA Cache entry was last accepted.  This address must correspond to the msdpPeerRemoteAddress value for a row in the MSDP Peer Table
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdpsacacherpfpeer
            
            	The peer from which an SA message corresponding to this cache entry would be accepted (i.e. the RPF peer for msdpSACacheOriginRP).  This may be different than msdpSACachePeerLearnedFrom if this entry was created by an MSDP SA\-Response.  This address must correspond to the msdpPeerRemoteAddress value for a row in the MSDP Peer Table
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdpsacachestatus
            
            	The status of this row in the table.  The only allowable actions are to retreive the status, which will be `active', or to set the status to `destroy' in order to remove this entry from the cache
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: msdpsacacheuptime
            
            	The time since this entry was placed in the SA cache
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DRAFT-MSDP-MIB'
            _revision = '1999-12-16'

            def __init__(self):
                self.parent = None
                self.msdpsacachegroupaddr = None
                self.msdpsacachesourceaddr = None
                self.msdpsacacheoriginrp = None
                self.msdpsacacheexpirytime = None
                self.msdpsacacheindatapackets = None
                self.msdpsacacheinsas = None
                self.msdpsacachepeerlearnedfrom = None
                self.msdpsacacherpfpeer = None
                self.msdpsacachestatus = None
                self.msdpsacacheuptime = None

            @property
            def _common_path(self):
                if self.msdpsacachegroupaddr is None:
                    raise YPYModelError('Key property msdpsacachegroupaddr is None')
                if self.msdpsacachesourceaddr is None:
                    raise YPYModelError('Key property msdpsacachesourceaddr is None')
                if self.msdpsacacheoriginrp is None:
                    raise YPYModelError('Key property msdpsacacheoriginrp is None')

                return '/DRAFT-MSDP-MIB:DRAFT-MSDP-MIB/DRAFT-MSDP-MIB:msdpSACacheTable/DRAFT-MSDP-MIB:msdpSACacheEntry[DRAFT-MSDP-MIB:msdpSACacheGroupAddr = ' + str(self.msdpsacachegroupaddr) + '][DRAFT-MSDP-MIB:msdpSACacheSourceAddr = ' + str(self.msdpsacachesourceaddr) + '][DRAFT-MSDP-MIB:msdpSACacheOriginRP = ' + str(self.msdpsacacheoriginrp) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.msdpsacachegroupaddr is not None:
                    return True

                if self.msdpsacachesourceaddr is not None:
                    return True

                if self.msdpsacacheoriginrp is not None:
                    return True

                if self.msdpsacacheexpirytime is not None:
                    return True

                if self.msdpsacacheindatapackets is not None:
                    return True

                if self.msdpsacacheinsas is not None:
                    return True

                if self.msdpsacachepeerlearnedfrom is not None:
                    return True

                if self.msdpsacacherpfpeer is not None:
                    return True

                if self.msdpsacachestatus is not None:
                    return True

                if self.msdpsacacheuptime is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DRAFT_MSDP_MIB as meta
                return meta._meta_table['DraftMsdpMib.Msdpsacachetable.Msdpsacacheentry']['meta_info']

        @property
        def _common_path(self):

            return '/DRAFT-MSDP-MIB:DRAFT-MSDP-MIB/DRAFT-MSDP-MIB:msdpSACacheTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.msdpsacacheentry is not None:
                for child_ref in self.msdpsacacheentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DRAFT_MSDP_MIB as meta
            return meta._meta_table['DraftMsdpMib.Msdpsacachetable']['meta_info']

    @property
    def _common_path(self):

        return '/DRAFT-MSDP-MIB:DRAFT-MSDP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.msdp is not None and self.msdp._has_data():
            return True

        if self.msdppeertable is not None and self.msdppeertable._has_data():
            return True

        if self.msdprequeststable is not None and self.msdprequeststable._has_data():
            return True

        if self.msdpsacachetable is not None and self.msdpsacachetable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _DRAFT_MSDP_MIB as meta
        return meta._meta_table['DraftMsdpMib']['meta_info']



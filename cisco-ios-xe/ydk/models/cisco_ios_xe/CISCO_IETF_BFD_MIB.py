""" CISCO_IETF_BFD_MIB 

This document contains the Management information base for
Bidirectional Forwarding Detection(BFD) Protocol as defined
in draft\-ietf\-bfd\-base\-06.txt.

BFD is a protocol intended to detect faults in the
bidirectional path between two forwarding engines, including
interfaces, data link(s), and to the extent possible the forwarding
engines themselves, with potentially very low latency.  It operates
independently of media, data protocols, and routing protocols.

This MIB module is based on the Internet Draft
draft\-ietf\-bfd\-mib\-03.txt and draft\-ietf\-bfd\-mib\-04.txt

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CiscobfddiagEnum(Enum):
    """
    CiscobfddiagEnum

    A common BFD diagnostic code.

    .. data:: noDiagnostic = 0

    .. data:: controlDetectionTimeExpired = 1

    .. data:: echoFunctionFailed = 2

    .. data:: neighborSignaledSessionDown = 3

    .. data:: forwardingPlaneReset = 4

    .. data:: pathDown = 5

    .. data:: concatenatedPathDown = 6

    .. data:: administrativelyDown = 7

    .. data:: reverseConcatenatedPathDown = 8

    """

    noDiagnostic = 0

    controlDetectionTimeExpired = 1

    echoFunctionFailed = 2

    neighborSignaledSessionDown = 3

    forwardingPlaneReset = 4

    pathDown = 5

    concatenatedPathDown = 6

    administrativelyDown = 7

    reverseConcatenatedPathDown = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_BFD_MIB as meta
        return meta._meta_table['CiscobfddiagEnum']



class CiscoIetfBfdMib(object):
    """
    
    
    .. attribute:: ciscobfdscalarobjects
    
    	
    	**type**\:   :py:class:`Ciscobfdscalarobjects <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdscalarobjects>`
    
    .. attribute:: ciscobfdsessdiscmaptable
    
    	The BFD Session Discriminator Mapping Table maps a local discriminator value to associated BFD sessions' CiscoBfdSessIndexTC used in the ciscoBfdSessTable
    	**type**\:   :py:class:`Ciscobfdsessdiscmaptable <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsessdiscmaptable>`
    
    .. attribute:: ciscobfdsessipmaptable
    
    	The BFD Session IP Mapping Table maps given ciscoBfdSessInterface, ciscoBfdSessAddrType, and ciscoBbfdSessAddr to an associated BFD sessions' CiscoBfdSessIndexTC used in the ciscoBfdSessTable. This table SHOULD contains those BFD sessions are of IP type\: singleHop(1) and multiHop(2)
    	**type**\:   :py:class:`Ciscobfdsessipmaptable <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsessipmaptable>`
    
    .. attribute:: ciscobfdsessmaptable
    
    	The BFD Session Mapping Table maps the complex indexing of the BFD sessions to the flat  CiscoBfdSessIndexTC used in the ciscoBfdSessTable
    	**type**\:   :py:class:`Ciscobfdsessmaptable <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsessmaptable>`
    
    .. attribute:: ciscobfdsesstable
    
    	The BFD Session Table describes the BFD sessions
    	**type**\:   :py:class:`Ciscobfdsesstable <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsesstable>`
    
    

    """

    _prefix = 'CISCO-IETF-BFD-MIB'
    _revision = '2011-04-16'

    def __init__(self):
        self.ciscobfdscalarobjects = CiscoIetfBfdMib.Ciscobfdscalarobjects()
        self.ciscobfdscalarobjects.parent = self
        self.ciscobfdsessdiscmaptable = CiscoIetfBfdMib.Ciscobfdsessdiscmaptable()
        self.ciscobfdsessdiscmaptable.parent = self
        self.ciscobfdsessipmaptable = CiscoIetfBfdMib.Ciscobfdsessipmaptable()
        self.ciscobfdsessipmaptable.parent = self
        self.ciscobfdsessmaptable = CiscoIetfBfdMib.Ciscobfdsessmaptable()
        self.ciscobfdsessmaptable.parent = self
        self.ciscobfdsesstable = CiscoIetfBfdMib.Ciscobfdsesstable()
        self.ciscobfdsesstable.parent = self


    class Ciscobfdscalarobjects(object):
        """
        
        
        .. attribute:: ciscobfdadminstatus
        
        	The global administrative status of BFD in this router. The value 'enabled' denotes that the BFD Process is  active on at least one interface; 'disabled' disables   it on all interfaces
        	**type**\:   :py:class:`CiscobfdadminstatusEnum <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdscalarobjects.CiscobfdadminstatusEnum>`
        
        .. attribute:: ciscobfdsessnotificationsenable
        
        	If this object is set to true(1), then it enables the emission of ciscoBfdSessUp and ciscoBfdSessDown  notifications; otherwise these notifications are not  emitted
        	**type**\:  bool
        
        .. attribute:: ciscobfdversionnumber
        
        	The current version number of the BFD protocol
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-IETF-BFD-MIB'
        _revision = '2011-04-16'

        def __init__(self):
            self.parent = None
            self.ciscobfdadminstatus = None
            self.ciscobfdsessnotificationsenable = None
            self.ciscobfdversionnumber = None

        class CiscobfdadminstatusEnum(Enum):
            """
            CiscobfdadminstatusEnum

            The global administrative status of BFD in this router.

            The value 'enabled' denotes that the BFD Process is 

            active on at least one interface; 'disabled' disables  

            it on all interfaces.

            .. data:: enabled = 1

            .. data:: disabled = 2

            """

            enabled = 1

            disabled = 2


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_BFD_MIB as meta
                return meta._meta_table['CiscoIetfBfdMib.Ciscobfdscalarobjects.CiscobfdadminstatusEnum']


        @property
        def _common_path(self):

            return '/CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/CISCO-IETF-BFD-MIB:ciscoBfdScalarObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ciscobfdadminstatus is not None:
                return True

            if self.ciscobfdsessnotificationsenable is not None:
                return True

            if self.ciscobfdversionnumber is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_BFD_MIB as meta
            return meta._meta_table['CiscoIetfBfdMib.Ciscobfdscalarobjects']['meta_info']


    class Ciscobfdsesstable(object):
        """
        The BFD Session Table describes the BFD sessions.
        
        .. attribute:: ciscobfdsessentry
        
        	The BFD Session Entry describes BFD session
        	**type**\: list of    :py:class:`Ciscobfdsessentry <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry>`
        
        

        """

        _prefix = 'CISCO-IETF-BFD-MIB'
        _revision = '2011-04-16'

        def __init__(self):
            self.parent = None
            self.ciscobfdsessentry = YList()
            self.ciscobfdsessentry.parent = self
            self.ciscobfdsessentry.name = 'ciscobfdsessentry'


        class Ciscobfdsessentry(object):
            """
            The BFD Session Entry describes BFD session.
            
            .. attribute:: ciscobfdsessindex  <key>
            
            	This object contains an index used to represent a unique BFD session on this device
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscobfdsessaddr
            
            	This object specifies the neighboring IP address which is being monitored with this BFD session. It can also be used to enabled BFD on a specific   interface. The value is set to zero when BFD session is not   associated with a specific interface
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ciscobfdsessaddrtype
            
            	This object specifies IP address type of the neighboring IP address which is being monitored with this BFD session.  Only values unknown(0), ipv4(1) or ipv6(2)  have to be supported.    A value of unknown(0) is allowed only when   the outgoing interface is of type point\-to\-point, or  when the BFD session is not associated with a specific   interface.   If any other unsupported values are attempted in a set  operation, the agent MUST return an inconsistentValue   error
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: ciscobfdsessapplicationid
            
            	This object contains an index used to indicate a local application which owns or maintains this  BFD session. For instance, the MPLS VPN process may  maintain a subset of the total number of BFD  sessions.  This application ID provides a convenient  way to segregate sessions by the applications which  maintain them
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessauthenticationtype
            
            	The Authentication Type used for this BFD session. This field is valid only when the Authentication Present bit is set
            	**type**\:   :py:class:`CiscobfdsessauthenticationtypeEnum <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry.CiscobfdsessauthenticationtypeEnum>`
            
            .. attribute:: ciscobfdsessauthpresflag
            
            	This object indicates that the local system's desire to use Authentication. Specifically, it is set   to true(1) if the local system wishes the session   to be authenticated or false(0) if not
            	**type**\:  bool
            
            .. attribute:: ciscobfdsesscontrolplanindepflag
            
            	This object indicates that the local system's ability to continue to function through a disruption of   the control plane. Specifically, it is set   to true(1) if the local system BFD implementation is  independent of the control plane. Otherwise, the   value is set to false(0)
            	**type**\:  bool
            
            .. attribute:: ciscobfdsessdemandmodedesiredflag
            
            	This object indicates that the local system's desire to use Demand mode. Specifically, it is set   to true(1) if the local system wishes to use   Demand mode or false(0) if not
            	**type**\:  bool
            
            .. attribute:: ciscobfdsessdesiredmintxinterval
            
            	This object specifies the minimum interval, in microseconds, that the local system would like to use when       transmitting BFD Control packets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessdetectmult
            
            	This object specifies the Detect time multiplier
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessdiag
            
            	A diagnostic code specifying the local system's reason for the last transition of the session from up(1)   to some other state
            	**type**\:   :py:class:`CiscobfddiagEnum <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscobfddiagEnum>`
            
            .. attribute:: ciscobfdsessdiscriminator
            
            	This object specifies the local discriminator for this BFD session, used to uniquely identify it
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscobfdsessechofuncmodedesiredflag
            
            	This object indicates that the local system's desire to use Echo mode. Specifically, it is set   to true(1) if the local system wishes to use   Echo mode or false(0) if not
            	**type**\:  bool
            
            .. attribute:: ciscobfdsessinterface
            
            	This object contains an interface index used to indicate the interface which this BFD session is running on
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciscobfdsessopermode
            
            	This object specifies current operating mode that BFD session is operating in
            	**type**\:   :py:class:`CiscobfdsessopermodeEnum <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry.CiscobfdsessopermodeEnum>`
            
            .. attribute:: ciscobfdsessperfdisctime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of the session counters suffered  a discontinuity.    The relevant counters are the specific instances associated   with this BFD session of any Counter32 object contained in  the ciscoBfdSessPerfTable. If no such discontinuities have occurred   since the last re\-initialization of the local management  subsystem, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessperflastcommlostdiag
            
            	The BFD diag code for the last time communication was lost with the neighbor. If no such down event exists this object   contains a zero value
            	**type**\:   :py:class:`CiscobfddiagEnum <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscobfddiagEnum>`
            
            .. attribute:: ciscobfdsessperflastsessdowntime
            
            	The value of sysUpTime on the most recent occasion at which the last time communication was lost with the neighbor. If   no such down event exist this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessperfpktin
            
            	The total number of BFD messages received for this BFD session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessperfpktinhc
            
            	This value represents the total number of BFD messages received for this BFD session. It MUST be equal to the  least significant 32 bits of ciscoBfdSessPerfPktIn  if ciscoBfdSessPerfPktInHC is supported according to  the rules spelled out in RFC2863
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscobfdsessperfpktout
            
            	The total number of BFD messages sent for this BFD session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessperfpktouthc
            
            	This value represents the total number of total number of BFD messages transmitted for this   BFD session. It MUST be equal to the  least significant 32 bits of ciscoBfdSessPerfPktIn  if ciscoBfdSessPerfPktOutHC is supported according to  the rules spelled out in RFC2863
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscobfdsessperfsessupcount
            
            	The number of times this session has gone into the Up state since the router last rebooted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessremotediscr
            
            	This object specifies the session discriminator chosen by the remote system for this BFD session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessremoteheardflag
            
            	This object specifies status of BFD packet reception from the remote system. Specifically, it is set to true(1) if  the local system is actively receiving BFD packets from the   remote system, and is set to false(0) if the local system   has not received BFD packets recently (within the detection   time) or if the local system is attempting to tear down  the BFD session
            	**type**\:  bool
            
            .. attribute:: ciscobfdsessreqminechorxinterval
            
            	This object specifies the minimum interval, in microseconds, between received BFD Echo packets that this  system is capable of supporting
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessreqminrxinterval
            
            	This object specifies the minimum interval, in microseconds, between received  BFD Control packets the   local system is capable of supporting
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table. When a row in this  table has a row in the active(1) state, no   objects in this row can be modified except the  ciscoBfdSessRowStatus and ciscoBfdSessStorageType
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: ciscobfdsessstate
            
            	The perceived state of the BFD session
            	**type**\:   :py:class:`CiscobfdsessstateEnum <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry.CiscobfdsessstateEnum>`
            
            .. attribute:: ciscobfdsessstortype
            
            	This variable indicates the storage type for this object. Conceptual rows having the value   'permanent' need not allow write\-access to any   columnar objects in the row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            .. attribute:: ciscobfdsesstype
            
            	The type of this BFD session
            	**type**\:   :py:class:`CiscobfdsesstypeEnum <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry.CiscobfdsesstypeEnum>`
            
            .. attribute:: ciscobfdsessudpport
            
            	The destination UDP Port for BFD. The default value is the well\-known value for this port. BFD State failing(5) is only applicable if this BFD session is running version 0
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: ciscobfdsessuptime
            
            	The value of sysUpTime on the most recent occasion at which the session came up. If no such up event exists this object  contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessversionnumber
            
            	The version number of the BFD protocol that this session is running in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-BFD-MIB'
            _revision = '2011-04-16'

            def __init__(self):
                self.parent = None
                self.ciscobfdsessindex = None
                self.ciscobfdsessaddr = None
                self.ciscobfdsessaddrtype = None
                self.ciscobfdsessapplicationid = None
                self.ciscobfdsessauthenticationtype = None
                self.ciscobfdsessauthpresflag = None
                self.ciscobfdsesscontrolplanindepflag = None
                self.ciscobfdsessdemandmodedesiredflag = None
                self.ciscobfdsessdesiredmintxinterval = None
                self.ciscobfdsessdetectmult = None
                self.ciscobfdsessdiag = None
                self.ciscobfdsessdiscriminator = None
                self.ciscobfdsessechofuncmodedesiredflag = None
                self.ciscobfdsessinterface = None
                self.ciscobfdsessopermode = None
                self.ciscobfdsessperfdisctime = None
                self.ciscobfdsessperflastcommlostdiag = None
                self.ciscobfdsessperflastsessdowntime = None
                self.ciscobfdsessperfpktin = None
                self.ciscobfdsessperfpktinhc = None
                self.ciscobfdsessperfpktout = None
                self.ciscobfdsessperfpktouthc = None
                self.ciscobfdsessperfsessupcount = None
                self.ciscobfdsessremotediscr = None
                self.ciscobfdsessremoteheardflag = None
                self.ciscobfdsessreqminechorxinterval = None
                self.ciscobfdsessreqminrxinterval = None
                self.ciscobfdsessrowstatus = None
                self.ciscobfdsessstate = None
                self.ciscobfdsessstortype = None
                self.ciscobfdsesstype = None
                self.ciscobfdsessudpport = None
                self.ciscobfdsessuptime = None
                self.ciscobfdsessversionnumber = None

            class CiscobfdsessauthenticationtypeEnum(Enum):
                """
                CiscobfdsessauthenticationtypeEnum

                The Authentication Type used for this BFD session. This

                field is valid only when the Authentication Present bit is set

                .. data:: simplePassword = 1

                .. data:: keyedMD5 = 2

                .. data:: meticulousKeyedMD5 = 3

                .. data:: keyedSHA1 = 4

                .. data:: meticulousKeyedSHA1 = 5

                """

                simplePassword = 1

                keyedMD5 = 2

                meticulousKeyedMD5 = 3

                keyedSHA1 = 4

                meticulousKeyedSHA1 = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_BFD_MIB as meta
                    return meta._meta_table['CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry.CiscobfdsessauthenticationtypeEnum']


            class CiscobfdsessopermodeEnum(Enum):
                """
                CiscobfdsessopermodeEnum

                This object specifies current operating mode that BFD

                session is operating in.

                .. data:: asyncModeWEchoFun = 1

                .. data:: asynchModeWOEchoFun = 2

                .. data:: demandModeWEchoFunction = 3

                .. data:: demandModeWOEchoFunction = 4

                """

                asyncModeWEchoFun = 1

                asynchModeWOEchoFun = 2

                demandModeWEchoFunction = 3

                demandModeWOEchoFunction = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_BFD_MIB as meta
                    return meta._meta_table['CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry.CiscobfdsessopermodeEnum']


            class CiscobfdsessstateEnum(Enum):
                """
                CiscobfdsessstateEnum

                The perceived state of the BFD session.

                .. data:: adminDown = 1

                .. data:: down = 2

                .. data:: init = 3

                .. data:: up = 4

                .. data:: failing = 5

                """

                adminDown = 1

                down = 2

                init = 3

                up = 4

                failing = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_BFD_MIB as meta
                    return meta._meta_table['CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry.CiscobfdsessstateEnum']


            class CiscobfdsesstypeEnum(Enum):
                """
                CiscobfdsesstypeEnum

                The type of this BFD session.

                .. data:: singleHop = 1

                .. data:: multiHop = 2

                """

                singleHop = 1

                multiHop = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_BFD_MIB as meta
                    return meta._meta_table['CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry.CiscobfdsesstypeEnum']


            @property
            def _common_path(self):
                if self.ciscobfdsessindex is None:
                    raise YPYModelError('Key property ciscobfdsessindex is None')

                return '/CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/CISCO-IETF-BFD-MIB:ciscoBfdSessTable/CISCO-IETF-BFD-MIB:ciscoBfdSessEntry[CISCO-IETF-BFD-MIB:ciscoBfdSessIndex = ' + str(self.ciscobfdsessindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ciscobfdsessindex is not None:
                    return True

                if self.ciscobfdsessaddr is not None:
                    return True

                if self.ciscobfdsessaddrtype is not None:
                    return True

                if self.ciscobfdsessapplicationid is not None:
                    return True

                if self.ciscobfdsessauthenticationtype is not None:
                    return True

                if self.ciscobfdsessauthpresflag is not None:
                    return True

                if self.ciscobfdsesscontrolplanindepflag is not None:
                    return True

                if self.ciscobfdsessdemandmodedesiredflag is not None:
                    return True

                if self.ciscobfdsessdesiredmintxinterval is not None:
                    return True

                if self.ciscobfdsessdetectmult is not None:
                    return True

                if self.ciscobfdsessdiag is not None:
                    return True

                if self.ciscobfdsessdiscriminator is not None:
                    return True

                if self.ciscobfdsessechofuncmodedesiredflag is not None:
                    return True

                if self.ciscobfdsessinterface is not None:
                    return True

                if self.ciscobfdsessopermode is not None:
                    return True

                if self.ciscobfdsessperfdisctime is not None:
                    return True

                if self.ciscobfdsessperflastcommlostdiag is not None:
                    return True

                if self.ciscobfdsessperflastsessdowntime is not None:
                    return True

                if self.ciscobfdsessperfpktin is not None:
                    return True

                if self.ciscobfdsessperfpktinhc is not None:
                    return True

                if self.ciscobfdsessperfpktout is not None:
                    return True

                if self.ciscobfdsessperfpktouthc is not None:
                    return True

                if self.ciscobfdsessperfsessupcount is not None:
                    return True

                if self.ciscobfdsessremotediscr is not None:
                    return True

                if self.ciscobfdsessremoteheardflag is not None:
                    return True

                if self.ciscobfdsessreqminechorxinterval is not None:
                    return True

                if self.ciscobfdsessreqminrxinterval is not None:
                    return True

                if self.ciscobfdsessrowstatus is not None:
                    return True

                if self.ciscobfdsessstate is not None:
                    return True

                if self.ciscobfdsessstortype is not None:
                    return True

                if self.ciscobfdsesstype is not None:
                    return True

                if self.ciscobfdsessudpport is not None:
                    return True

                if self.ciscobfdsessuptime is not None:
                    return True

                if self.ciscobfdsessversionnumber is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_BFD_MIB as meta
                return meta._meta_table['CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/CISCO-IETF-BFD-MIB:ciscoBfdSessTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ciscobfdsessentry is not None:
                for child_ref in self.ciscobfdsessentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_BFD_MIB as meta
            return meta._meta_table['CiscoIetfBfdMib.Ciscobfdsesstable']['meta_info']


    class Ciscobfdsessmaptable(object):
        """
        The BFD Session Mapping Table maps the complex
        indexing of the BFD sessions to the flat 
        CiscoBfdSessIndexTC used in the ciscoBfdSessTable.
        
        .. attribute:: ciscobfdsessmapentry
        
        	The BFD Session Entry describes BFD session that is mapped to this index
        	**type**\: list of    :py:class:`Ciscobfdsessmapentry <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsessmaptable.Ciscobfdsessmapentry>`
        
        

        """

        _prefix = 'CISCO-IETF-BFD-MIB'
        _revision = '2011-04-16'

        def __init__(self):
            self.parent = None
            self.ciscobfdsessmapentry = YList()
            self.ciscobfdsessmapentry.parent = self
            self.ciscobfdsessmapentry.name = 'ciscobfdsessmapentry'


        class Ciscobfdsessmapentry(object):
            """
            The BFD Session Entry describes BFD session
            that is mapped to this index.
            
            .. attribute:: ciscobfdsessapplicationid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`ciscobfdsessapplicationid <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry>`
            
            .. attribute:: ciscobfdsessdiscriminator  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ciscobfdsessdiscriminator <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry>`
            
            .. attribute:: ciscobfdsessaddrtype  <key>
            
            	
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: ciscobfdsessaddr  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..255
            
            	**refers to**\:  :py:class:`ciscobfdsessaddr <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry>`
            
            .. attribute:: ciscobfdsessmapbfdindex
            
            	This object indicates the CiscoBfdSessIndexTC referred to by the indices of this row. In essence, a mapping is  provided between these indices and the ciscoBfdSessTable
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-BFD-MIB'
            _revision = '2011-04-16'

            def __init__(self):
                self.parent = None
                self.ciscobfdsessapplicationid = None
                self.ciscobfdsessdiscriminator = None
                self.ciscobfdsessaddrtype = None
                self.ciscobfdsessaddr = None
                self.ciscobfdsessmapbfdindex = None

            @property
            def _common_path(self):
                if self.ciscobfdsessapplicationid is None:
                    raise YPYModelError('Key property ciscobfdsessapplicationid is None')
                if self.ciscobfdsessdiscriminator is None:
                    raise YPYModelError('Key property ciscobfdsessdiscriminator is None')
                if self.ciscobfdsessaddrtype is None:
                    raise YPYModelError('Key property ciscobfdsessaddrtype is None')
                if self.ciscobfdsessaddr is None:
                    raise YPYModelError('Key property ciscobfdsessaddr is None')

                return '/CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/CISCO-IETF-BFD-MIB:ciscoBfdSessMapTable/CISCO-IETF-BFD-MIB:ciscoBfdSessMapEntry[CISCO-IETF-BFD-MIB:ciscoBfdSessApplicationId = ' + str(self.ciscobfdsessapplicationid) + '][CISCO-IETF-BFD-MIB:ciscoBfdSessDiscriminator = ' + str(self.ciscobfdsessdiscriminator) + '][CISCO-IETF-BFD-MIB:ciscoBfdSessAddrType = ' + str(self.ciscobfdsessaddrtype) + '][CISCO-IETF-BFD-MIB:ciscoBfdSessAddr = ' + str(self.ciscobfdsessaddr) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ciscobfdsessapplicationid is not None:
                    return True

                if self.ciscobfdsessdiscriminator is not None:
                    return True

                if self.ciscobfdsessaddrtype is not None:
                    return True

                if self.ciscobfdsessaddr is not None:
                    return True

                if self.ciscobfdsessmapbfdindex is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_BFD_MIB as meta
                return meta._meta_table['CiscoIetfBfdMib.Ciscobfdsessmaptable.Ciscobfdsessmapentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/CISCO-IETF-BFD-MIB:ciscoBfdSessMapTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ciscobfdsessmapentry is not None:
                for child_ref in self.ciscobfdsessmapentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_BFD_MIB as meta
            return meta._meta_table['CiscoIetfBfdMib.Ciscobfdsessmaptable']['meta_info']


    class Ciscobfdsessdiscmaptable(object):
        """
        The BFD Session Discriminator Mapping Table maps a
        local discriminator value to associated BFD sessions'
        CiscoBfdSessIndexTC used in the ciscoBfdSessTable.
        
        .. attribute:: ciscobfdsessdiscmapentry
        
        	Each row contains a mapping between a local discriminator value to an entry in ciscoBfdSessTable
        	**type**\: list of    :py:class:`Ciscobfdsessdiscmapentry <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsessdiscmaptable.Ciscobfdsessdiscmapentry>`
        
        

        """

        _prefix = 'CISCO-IETF-BFD-MIB'
        _revision = '2011-04-16'

        def __init__(self):
            self.parent = None
            self.ciscobfdsessdiscmapentry = YList()
            self.ciscobfdsessdiscmapentry.parent = self
            self.ciscobfdsessdiscmapentry.name = 'ciscobfdsessdiscmapentry'


        class Ciscobfdsessdiscmapentry(object):
            """
            Each row contains a mapping between a local discriminator
            value to an entry in ciscoBfdSessTable.
            
            .. attribute:: ciscobfdsessdiscriminator  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ciscobfdsessdiscriminator <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry>`
            
            .. attribute:: ciscobfdsessdiscmapindex
            
            	This object indicates the CiscoBfdSessIndexTC referred to by the index of this row. In essence, a mapping is  provided between this index and the ciscoBfdSessTable
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-BFD-MIB'
            _revision = '2011-04-16'

            def __init__(self):
                self.parent = None
                self.ciscobfdsessdiscriminator = None
                self.ciscobfdsessdiscmapindex = None

            @property
            def _common_path(self):
                if self.ciscobfdsessdiscriminator is None:
                    raise YPYModelError('Key property ciscobfdsessdiscriminator is None')

                return '/CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/CISCO-IETF-BFD-MIB:ciscoBfdSessDiscMapTable/CISCO-IETF-BFD-MIB:ciscoBfdSessDiscMapEntry[CISCO-IETF-BFD-MIB:ciscoBfdSessDiscriminator = ' + str(self.ciscobfdsessdiscriminator) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ciscobfdsessdiscriminator is not None:
                    return True

                if self.ciscobfdsessdiscmapindex is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_BFD_MIB as meta
                return meta._meta_table['CiscoIetfBfdMib.Ciscobfdsessdiscmaptable.Ciscobfdsessdiscmapentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/CISCO-IETF-BFD-MIB:ciscoBfdSessDiscMapTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ciscobfdsessdiscmapentry is not None:
                for child_ref in self.ciscobfdsessdiscmapentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_BFD_MIB as meta
            return meta._meta_table['CiscoIetfBfdMib.Ciscobfdsessdiscmaptable']['meta_info']


    class Ciscobfdsessipmaptable(object):
        """
        The BFD Session IP Mapping Table maps given
        ciscoBfdSessInterface, ciscoBfdSessAddrType, and
        ciscoBbfdSessAddr to an associated BFD sessions'
        CiscoBfdSessIndexTC used in the ciscoBfdSessTable.
        This table SHOULD contains those BFD sessions are
        of IP type\: singleHop(1) and multiHop(2).
        
        .. attribute:: ciscobfdsessipmapentry
        
        	Each row contains a mapping between ciscoBfdSessInterface, ciscoBfdSessAddrType and ciscoBfdSessAddr values to an  entry in ciscoBfdSessTable
        	**type**\: list of    :py:class:`Ciscobfdsessipmapentry <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsessipmaptable.Ciscobfdsessipmapentry>`
        
        

        """

        _prefix = 'CISCO-IETF-BFD-MIB'
        _revision = '2011-04-16'

        def __init__(self):
            self.parent = None
            self.ciscobfdsessipmapentry = YList()
            self.ciscobfdsessipmapentry.parent = self
            self.ciscobfdsessipmapentry.name = 'ciscobfdsessipmapentry'


        class Ciscobfdsessipmapentry(object):
            """
            Each row contains a mapping between ciscoBfdSessInterface,
            ciscoBfdSessAddrType and ciscoBfdSessAddr values to an 
            entry in ciscoBfdSessTable.
            
            .. attribute:: ciscobfdsessinterface  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ciscobfdsessinterface <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry>`
            
            .. attribute:: ciscobfdsessaddrtype  <key>
            
            	
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: ciscobfdsessaddr  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..255
            
            	**refers to**\:  :py:class:`ciscobfdsessaddr <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry>`
            
            .. attribute:: ciscobfdsessipmapindex
            
            	This object indicates the CiscoBfdSessIndexTC referred to by the indices of this row. In essence, a mapping is  provided between these indices and an entry in ciscoBfdSessTable
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-BFD-MIB'
            _revision = '2011-04-16'

            def __init__(self):
                self.parent = None
                self.ciscobfdsessinterface = None
                self.ciscobfdsessaddrtype = None
                self.ciscobfdsessaddr = None
                self.ciscobfdsessipmapindex = None

            @property
            def _common_path(self):
                if self.ciscobfdsessinterface is None:
                    raise YPYModelError('Key property ciscobfdsessinterface is None')
                if self.ciscobfdsessaddrtype is None:
                    raise YPYModelError('Key property ciscobfdsessaddrtype is None')
                if self.ciscobfdsessaddr is None:
                    raise YPYModelError('Key property ciscobfdsessaddr is None')

                return '/CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/CISCO-IETF-BFD-MIB:ciscoBfdSessIpMapTable/CISCO-IETF-BFD-MIB:ciscoBfdSessIpMapEntry[CISCO-IETF-BFD-MIB:ciscoBfdSessInterface = ' + str(self.ciscobfdsessinterface) + '][CISCO-IETF-BFD-MIB:ciscoBfdSessAddrType = ' + str(self.ciscobfdsessaddrtype) + '][CISCO-IETF-BFD-MIB:ciscoBfdSessAddr = ' + str(self.ciscobfdsessaddr) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ciscobfdsessinterface is not None:
                    return True

                if self.ciscobfdsessaddrtype is not None:
                    return True

                if self.ciscobfdsessaddr is not None:
                    return True

                if self.ciscobfdsessipmapindex is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_BFD_MIB as meta
                return meta._meta_table['CiscoIetfBfdMib.Ciscobfdsessipmaptable.Ciscobfdsessipmapentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/CISCO-IETF-BFD-MIB:ciscoBfdSessIpMapTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ciscobfdsessipmapentry is not None:
                for child_ref in self.ciscobfdsessipmapentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_BFD_MIB as meta
            return meta._meta_table['CiscoIetfBfdMib.Ciscobfdsessipmaptable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.ciscobfdscalarobjects is not None and self.ciscobfdscalarobjects._has_data():
            return True

        if self.ciscobfdsessdiscmaptable is not None and self.ciscobfdsessdiscmaptable._has_data():
            return True

        if self.ciscobfdsessipmaptable is not None and self.ciscobfdsessipmaptable._has_data():
            return True

        if self.ciscobfdsessmaptable is not None and self.ciscobfdsessmaptable._has_data():
            return True

        if self.ciscobfdsesstable is not None and self.ciscobfdsesstable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_BFD_MIB as meta
        return meta._meta_table['CiscoIetfBfdMib']['meta_info']



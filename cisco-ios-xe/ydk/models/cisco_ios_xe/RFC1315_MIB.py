""" RFC1315_MIB 


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Rfc1315Mib(object):
    """
    
    
    .. attribute:: frame_relay_globals
    
    	
    	**type**\:   :py:class:`FrameRelayGlobals <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.FrameRelayGlobals>`
    
    .. attribute:: frcircuittable
    
    	A table containing information about specific Data Link Connection Identifiers and corresponding virtual circuits
    	**type**\:   :py:class:`Frcircuittable <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.Frcircuittable>`
    
    .. attribute:: frdlcmitable
    
    	The Parameters for the Data Link Connection Management Interface for the frame relay service on this interface
    	**type**\:   :py:class:`Frdlcmitable <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.Frdlcmitable>`
    
    .. attribute:: frerrtable
    
    	A table containing information about Errors on the Frame Relay interface
    	**type**\:   :py:class:`Frerrtable <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.Frerrtable>`
    
    

    """

    _prefix = 'RFC1315-MIB'

    def __init__(self):
        self.frame_relay_globals = Rfc1315Mib.FrameRelayGlobals()
        self.frame_relay_globals.parent = self
        self.frcircuittable = Rfc1315Mib.Frcircuittable()
        self.frcircuittable.parent = self
        self.frdlcmitable = Rfc1315Mib.Frdlcmitable()
        self.frdlcmitable.parent = self
        self.frerrtable = Rfc1315Mib.Frerrtable()
        self.frerrtable.parent = self


    class FrameRelayGlobals(object):
        """
        
        
        .. attribute:: frtrapstate
        
        	This variable  indicates  whether  the  system produces the frDLCIStatusChange trap
        	**type**\:   :py:class:`FrtrapstateEnum <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.FrameRelayGlobals.FrtrapstateEnum>`
        
        

        """

        _prefix = 'RFC1315-MIB'

        def __init__(self):
            self.parent = None
            self.frtrapstate = None

        class FrtrapstateEnum(Enum):
            """
            FrtrapstateEnum

            This variable  indicates  whether  the  system

            produces the frDLCIStatusChange trap.

            .. data:: enabled = 1

            .. data:: disabled = 2

            """

            enabled = 1

            disabled = 2


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _RFC1315_MIB as meta
                return meta._meta_table['Rfc1315Mib.FrameRelayGlobals.FrtrapstateEnum']


        @property
        def _common_path(self):

            return '/RFC1315-MIB:RFC1315-MIB/RFC1315-MIB:frame-relay-globals'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.frtrapstate is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _RFC1315_MIB as meta
            return meta._meta_table['Rfc1315Mib.FrameRelayGlobals']['meta_info']


    class Frdlcmitable(object):
        """
        The Parameters for the Data Link Connection Management
        Interface for the frame relay service on this
        interface.
        
        .. attribute:: frdlcmientry
        
        	The Parameters for a particular Data Link Con\- nection Management Interface
        	**type**\: list of    :py:class:`Frdlcmientry <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.Frdlcmitable.Frdlcmientry>`
        
        

        """

        _prefix = 'RFC1315-MIB'

        def __init__(self):
            self.parent = None
            self.frdlcmientry = YList()
            self.frdlcmientry.parent = self
            self.frdlcmientry.name = 'frdlcmientry'


        class Frdlcmientry(object):
            """
            The Parameters for a particular Data Link Con\-
            nection Management Interface.
            
            .. attribute:: frdlcmiifindex  <key>
            
            	The ifIndex value of the  corresponding  ifEn\- try
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frdlcmiaddress
            
            	This variable states which address  format  is in use on the Frame Relay interface
            	**type**\:   :py:class:`FrdlcmiaddressEnum <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.Frdlcmitable.Frdlcmientry.FrdlcmiaddressEnum>`
            
            .. attribute:: frdlcmiaddresslen
            
            	This variable states which address  length  in octets.  In the case of Q922 format, the length indicates the entire length of the address  in\- cluding the control portion
            	**type**\:   :py:class:`FrdlcmiaddresslenEnum <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.Frdlcmitable.Frdlcmientry.FrdlcmiaddresslenEnum>`
            
            .. attribute:: frdlcmierrorthreshold
            
            	This  is  the  maximum  number  of  unanswered Status Enquiries the equipment shall accept be\- fore declaring the interface down
            	**type**\:  int
            
            	**range:** 1..10
            
            .. attribute:: frdlcmifullenquiryinterval
            
            	Number of status enquiry intervals  that  pass before  issuance  of a full status enquiry mes\- sage
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: frdlcmimaxsupportedvcs
            
            	The maximum number of Virtual Circuits allowed for  this  interface.   Usually dictated by the Frame Relay network.  In response to a SET, if a value less than zero or  higher  than the agent's maximal capability is configured, the agent  should  respond  bad\- Value
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frdlcmimonitoredevents
            
            	This is the number of status polling intervals over which the error threshold is counted.  For example, if within 'MonitoredEvents' number  of events  the  station  receives 'ErrorThreshold' number of errors, the interface  is  marked  as down
            	**type**\:  int
            
            	**range:** 1..10
            
            .. attribute:: frdlcmimulticast
            
            	This indicates whether the Frame Relay  inter\- face is using a multicast service
            	**type**\:   :py:class:`FrdlcmimulticastEnum <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.Frdlcmitable.Frdlcmientry.FrdlcmimulticastEnum>`
            
            .. attribute:: frdlcmipollinginterval
            
            	This is the number of seconds between  succes\- sive status enquiry messages
            	**type**\:  int
            
            	**range:** 5..30
            
            .. attribute:: frdlcmistate
            
            	This variable states which Data  Link  Connec\- tion Management scheme is active (and by impli\- cation, what DLCI it uses) on the  Frame  Relay interface
            	**type**\:   :py:class:`FrdlcmistateEnum <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.Frdlcmitable.Frdlcmientry.FrdlcmistateEnum>`
            
            

            """

            _prefix = 'RFC1315-MIB'

            def __init__(self):
                self.parent = None
                self.frdlcmiifindex = None
                self.frdlcmiaddress = None
                self.frdlcmiaddresslen = None
                self.frdlcmierrorthreshold = None
                self.frdlcmifullenquiryinterval = None
                self.frdlcmimaxsupportedvcs = None
                self.frdlcmimonitoredevents = None
                self.frdlcmimulticast = None
                self.frdlcmipollinginterval = None
                self.frdlcmistate = None

            class FrdlcmiaddressEnum(Enum):
                """
                FrdlcmiaddressEnum

                This variable states which address  format  is

                in use on the Frame Relay interface.

                .. data:: q921 = 1

                .. data:: q922March90 = 2

                .. data:: q922November90 = 3

                .. data:: q922 = 4

                """

                q921 = 1

                q922March90 = 2

                q922November90 = 3

                q922 = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _RFC1315_MIB as meta
                    return meta._meta_table['Rfc1315Mib.Frdlcmitable.Frdlcmientry.FrdlcmiaddressEnum']


            class FrdlcmiaddresslenEnum(Enum):
                """
                FrdlcmiaddresslenEnum

                This variable states which address  length  in

                octets.  In the case of Q922 format, the length

                indicates the entire length of the address  in\-

                cluding the control portion.

                .. data:: two_octets = 2

                .. data:: three_octets = 3

                .. data:: four_octets = 4

                """

                two_octets = 2

                three_octets = 3

                four_octets = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _RFC1315_MIB as meta
                    return meta._meta_table['Rfc1315Mib.Frdlcmitable.Frdlcmientry.FrdlcmiaddresslenEnum']


            class FrdlcmimulticastEnum(Enum):
                """
                FrdlcmimulticastEnum

                This indicates whether the Frame Relay  inter\-

                face is using a multicast service.

                .. data:: nonBroadcast = 1

                .. data:: broadcast = 2

                """

                nonBroadcast = 1

                broadcast = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _RFC1315_MIB as meta
                    return meta._meta_table['Rfc1315Mib.Frdlcmitable.Frdlcmientry.FrdlcmimulticastEnum']


            class FrdlcmistateEnum(Enum):
                """
                FrdlcmistateEnum

                This variable states which Data  Link  Connec\-

                tion Management scheme is active (and by impli\-

                cation, what DLCI it uses) on the  Frame  Relay

                interface.

                .. data:: noLmiConfigured = 1

                .. data:: lmiRev1 = 2

                .. data:: ansiT1_617_D = 3

                .. data:: ansiT1_617_B = 4

                """

                noLmiConfigured = 1

                lmiRev1 = 2

                ansiT1_617_D = 3

                ansiT1_617_B = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _RFC1315_MIB as meta
                    return meta._meta_table['Rfc1315Mib.Frdlcmitable.Frdlcmientry.FrdlcmistateEnum']


            @property
            def _common_path(self):
                if self.frdlcmiifindex is None:
                    raise YPYModelError('Key property frdlcmiifindex is None')

                return '/RFC1315-MIB:RFC1315-MIB/RFC1315-MIB:frDlcmiTable/RFC1315-MIB:frDlcmiEntry[RFC1315-MIB:frDlcmiIfIndex = ' + str(self.frdlcmiifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.frdlcmiifindex is not None:
                    return True

                if self.frdlcmiaddress is not None:
                    return True

                if self.frdlcmiaddresslen is not None:
                    return True

                if self.frdlcmierrorthreshold is not None:
                    return True

                if self.frdlcmifullenquiryinterval is not None:
                    return True

                if self.frdlcmimaxsupportedvcs is not None:
                    return True

                if self.frdlcmimonitoredevents is not None:
                    return True

                if self.frdlcmimulticast is not None:
                    return True

                if self.frdlcmipollinginterval is not None:
                    return True

                if self.frdlcmistate is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _RFC1315_MIB as meta
                return meta._meta_table['Rfc1315Mib.Frdlcmitable.Frdlcmientry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1315-MIB:RFC1315-MIB/RFC1315-MIB:frDlcmiTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.frdlcmientry is not None:
                for child_ref in self.frdlcmientry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _RFC1315_MIB as meta
            return meta._meta_table['Rfc1315Mib.Frdlcmitable']['meta_info']


    class Frcircuittable(object):
        """
        A table containing information about specific Data
        Link Connection Identifiers and corresponding virtual
        circuits.
        
        .. attribute:: frcircuitentry
        
        	The information regarding a single  Data  Link Connection Identifier
        	**type**\: list of    :py:class:`Frcircuitentry <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.Frcircuittable.Frcircuitentry>`
        
        

        """

        _prefix = 'RFC1315-MIB'

        def __init__(self):
            self.parent = None
            self.frcircuitentry = YList()
            self.frcircuitentry.parent = self
            self.frcircuitentry.name = 'frcircuitentry'


        class Frcircuitentry(object):
            """
            The information regarding a single  Data  Link
            Connection Identifier.
            
            .. attribute:: frcircuitifindex  <key>
            
            	The ifIndex Value of the ifEntry this  virtual circuit is layered onto
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frcircuitdlci  <key>
            
            	The Data Link Connection Identifier  for  this virtual circuit
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frcircuitcommittedburst
            
            	This variable indicates the maximum amount  of data,  in  bits,  that  the  network  agrees to transfer under normal  conditions,  during  the measurement interval
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frcircuitcreationtime
            
            	The value of sysUpTime when the  virtual  cir\- cuit was created, whether by the Data Link Con\- nection Management Interface  or  by  a  SetRe\- quest
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitexcessburst
            
            	This variable indicates the maximum amount  of uncommitted data bits that the network will at\- tempt to deliver over the measurement interval.  By default, if not configured when creating the entry, the Excess Information Burst Size is set to the value of ifSpeed
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frcircuitlasttimechange
            
            	The value of sysUpTime when last there  was  a change in the virtual circuit state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceivedbecns
            
            	Number of frames received from the network in\- dicating  backward congestion since the virtual circuit was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceivedfecns
            
            	Number of frames received from the network in\- dicating  forward  congestion since the virtual circuit was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceivedframes
            
            	Number of frames received  over  this  virtual circuit since it was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceivedoctets
            
            	Number of octets received  over  this  virtual circuit since it was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitsentframes
            
            	The number of frames sent  from  this  virtual circuit since it was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitsentoctets
            
            	The number of octets sent  from  this  virtual circuit since it was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitstate
            
            	Indicates whether the particular virtual  cir\- cuit  is operational.  In the absence of a Data Link Connection Management  Interface,  virtual circuit  entries  (rows) may be created by set\- ting virtual  circuit  state  to  'active',  or deleted by changing Circuit state to 'invalid'. Whether or not the row actually  disappears  is left  to the implementation, so this object may actually read as 'invalid' for  some  arbitrary length  of  time.   It is also legal to set the state of a virtual  circuit  to  'inactive'  to temporarily disable a given circuit
            	**type**\:   :py:class:`FrcircuitstateEnum <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.Frcircuittable.Frcircuitentry.FrcircuitstateEnum>`
            
            .. attribute:: frcircuitthroughput
            
            	Throughput is the average number of 'Frame Re\- lay  Information  Field'  bits  transferred per second across a user network interface  in  one direction, measured over the measurement inter\- val.  If the  configured  committed  burst  rate  and throughput  are  both non\-zero, the measurement interval T=frCircuitCommittedBurst/frCircuitThroughput.  If the  configured  committed  burst  rate  and throughput  are  both zero, the measurement in\- terval        T=frCircuitExcessBurst/ifSpeed
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'RFC1315-MIB'

            def __init__(self):
                self.parent = None
                self.frcircuitifindex = None
                self.frcircuitdlci = None
                self.frcircuitcommittedburst = None
                self.frcircuitcreationtime = None
                self.frcircuitexcessburst = None
                self.frcircuitlasttimechange = None
                self.frcircuitreceivedbecns = None
                self.frcircuitreceivedfecns = None
                self.frcircuitreceivedframes = None
                self.frcircuitreceivedoctets = None
                self.frcircuitsentframes = None
                self.frcircuitsentoctets = None
                self.frcircuitstate = None
                self.frcircuitthroughput = None

            class FrcircuitstateEnum(Enum):
                """
                FrcircuitstateEnum

                Indicates whether the particular virtual  cir\-

                cuit  is operational.  In the absence of a Data

                Link Connection Management  Interface,  virtual

                circuit  entries  (rows) may be created by set\-

                ting virtual  circuit  state  to  'active',  or

                deleted by changing Circuit state to 'invalid'.

                Whether or not the row actually  disappears  is

                left  to the implementation, so this object may

                actually read as 'invalid' for  some  arbitrary

                length  of  time.   It is also legal to set the

                state of a virtual  circuit  to  'inactive'  to

                temporarily disable a given circuit.

                .. data:: invalid = 1

                .. data:: active = 2

                .. data:: inactive = 3

                """

                invalid = 1

                active = 2

                inactive = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _RFC1315_MIB as meta
                    return meta._meta_table['Rfc1315Mib.Frcircuittable.Frcircuitentry.FrcircuitstateEnum']


            @property
            def _common_path(self):
                if self.frcircuitifindex is None:
                    raise YPYModelError('Key property frcircuitifindex is None')
                if self.frcircuitdlci is None:
                    raise YPYModelError('Key property frcircuitdlci is None')

                return '/RFC1315-MIB:RFC1315-MIB/RFC1315-MIB:frCircuitTable/RFC1315-MIB:frCircuitEntry[RFC1315-MIB:frCircuitIfIndex = ' + str(self.frcircuitifindex) + '][RFC1315-MIB:frCircuitDlci = ' + str(self.frcircuitdlci) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.frcircuitifindex is not None:
                    return True

                if self.frcircuitdlci is not None:
                    return True

                if self.frcircuitcommittedburst is not None:
                    return True

                if self.frcircuitcreationtime is not None:
                    return True

                if self.frcircuitexcessburst is not None:
                    return True

                if self.frcircuitlasttimechange is not None:
                    return True

                if self.frcircuitreceivedbecns is not None:
                    return True

                if self.frcircuitreceivedfecns is not None:
                    return True

                if self.frcircuitreceivedframes is not None:
                    return True

                if self.frcircuitreceivedoctets is not None:
                    return True

                if self.frcircuitsentframes is not None:
                    return True

                if self.frcircuitsentoctets is not None:
                    return True

                if self.frcircuitstate is not None:
                    return True

                if self.frcircuitthroughput is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _RFC1315_MIB as meta
                return meta._meta_table['Rfc1315Mib.Frcircuittable.Frcircuitentry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1315-MIB:RFC1315-MIB/RFC1315-MIB:frCircuitTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.frcircuitentry is not None:
                for child_ref in self.frcircuitentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _RFC1315_MIB as meta
            return meta._meta_table['Rfc1315Mib.Frcircuittable']['meta_info']


    class Frerrtable(object):
        """
        A table containing information about Errors on the
        Frame Relay interface.
        
        .. attribute:: frerrentry
        
        	The error information for a single frame relay interface
        	**type**\: list of    :py:class:`Frerrentry <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.Frerrtable.Frerrentry>`
        
        

        """

        _prefix = 'RFC1315-MIB'

        def __init__(self):
            self.parent = None
            self.frerrentry = YList()
            self.frerrentry.parent = self
            self.frerrentry.name = 'frerrentry'


        class Frerrentry(object):
            """
            The error information for a single frame relay
            interface.
            
            .. attribute:: frerrifindex  <key>
            
            	The ifIndex Value of the  corresponding  ifEn\- try
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frerrdata
            
            	An octet string containing as much of the  er\- ror  packet as possible.  As a minimum, it must contain the Q.922 Address or  as  much  as  was delivered.   It is desirable to include all in\- formation up to the PDU
            	**type**\:  str
            
            .. attribute:: frerrtime
            
            	The value of sysUpTime at which the error  was detected
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frerrtype
            
            	The type of error that was last seen  on  this interface
            	**type**\:   :py:class:`FrerrtypeEnum <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.Frerrtable.Frerrentry.FrerrtypeEnum>`
            
            

            """

            _prefix = 'RFC1315-MIB'

            def __init__(self):
                self.parent = None
                self.frerrifindex = None
                self.frerrdata = None
                self.frerrtime = None
                self.frerrtype = None

            class FrerrtypeEnum(Enum):
                """
                FrerrtypeEnum

                The type of error that was last seen  on  this

                interface.

                .. data:: unknownError = 1

                .. data:: receiveShort = 2

                .. data:: receiveLong = 3

                .. data:: illegalDLCI = 4

                .. data:: unknownDLCI = 5

                .. data:: dlcmiProtoErr = 6

                .. data:: dlcmiUnknownIE = 7

                .. data:: dlcmiSequenceErr = 8

                .. data:: dlcmiUnknownRpt = 9

                .. data:: noErrorSinceReset = 10

                """

                unknownError = 1

                receiveShort = 2

                receiveLong = 3

                illegalDLCI = 4

                unknownDLCI = 5

                dlcmiProtoErr = 6

                dlcmiUnknownIE = 7

                dlcmiSequenceErr = 8

                dlcmiUnknownRpt = 9

                noErrorSinceReset = 10


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _RFC1315_MIB as meta
                    return meta._meta_table['Rfc1315Mib.Frerrtable.Frerrentry.FrerrtypeEnum']


            @property
            def _common_path(self):
                if self.frerrifindex is None:
                    raise YPYModelError('Key property frerrifindex is None')

                return '/RFC1315-MIB:RFC1315-MIB/RFC1315-MIB:frErrTable/RFC1315-MIB:frErrEntry[RFC1315-MIB:frErrIfIndex = ' + str(self.frerrifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.frerrifindex is not None:
                    return True

                if self.frerrdata is not None:
                    return True

                if self.frerrtime is not None:
                    return True

                if self.frerrtype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _RFC1315_MIB as meta
                return meta._meta_table['Rfc1315Mib.Frerrtable.Frerrentry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1315-MIB:RFC1315-MIB/RFC1315-MIB:frErrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.frerrentry is not None:
                for child_ref in self.frerrentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _RFC1315_MIB as meta
            return meta._meta_table['Rfc1315Mib.Frerrtable']['meta_info']

    @property
    def _common_path(self):

        return '/RFC1315-MIB:RFC1315-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.frame_relay_globals is not None and self.frame_relay_globals._has_data():
            return True

        if self.frcircuittable is not None and self.frcircuittable._has_data():
            return True

        if self.frdlcmitable is not None and self.frdlcmitable._has_data():
            return True

        if self.frerrtable is not None and self.frerrtable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _RFC1315_MIB as meta
        return meta._meta_table['Rfc1315Mib']['meta_info']



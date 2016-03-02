""" RFC1315_MIB 


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class RFC1315MIB(object):
    """
    
    
    .. attribute:: frame_relay_globals
    
    	
    	**type**\: :py:class:`FrameRelayGlobals <ydk.models.rfc1315.RFC1315_MIB.RFC1315MIB.FrameRelayGlobals>`
    
    .. attribute:: frcircuittable
    
    	A table containing information about specific Data Link Connection Identifiers and corresponding virtual circuits
    	**type**\: :py:class:`FrCircuitTable <ydk.models.rfc1315.RFC1315_MIB.RFC1315MIB.FrCircuitTable>`
    
    .. attribute:: frdlcmitable
    
    	The Parameters for the Data Link Connection Management Interface for the frame relay service on this interface
    	**type**\: :py:class:`FrDlcmiTable <ydk.models.rfc1315.RFC1315_MIB.RFC1315MIB.FrDlcmiTable>`
    
    .. attribute:: frerrtable
    
    	A table containing information about Errors on the Frame Relay interface
    	**type**\: :py:class:`FrErrTable <ydk.models.rfc1315.RFC1315_MIB.RFC1315MIB.FrErrTable>`
    
    

    """

    _prefix = 'rfc1315-mib'

    def __init__(self):
        self.frame_relay_globals = RFC1315MIB.FrameRelayGlobals()
        self.frame_relay_globals.parent = self
        self.frcircuittable = RFC1315MIB.FrCircuitTable()
        self.frcircuittable.parent = self
        self.frdlcmitable = RFC1315MIB.FrDlcmiTable()
        self.frdlcmitable.parent = self
        self.frerrtable = RFC1315MIB.FrErrTable()
        self.frerrtable.parent = self


    class FrCircuitTable(object):
        """
        A table containing information about specific Data
        Link Connection Identifiers and corresponding virtual
        circuits.
        
        .. attribute:: frcircuitentry
        
        	The information regarding a single  Data  Link Connection Identifier
        	**type**\: list of :py:class:`FrCircuitEntry <ydk.models.rfc1315.RFC1315_MIB.RFC1315MIB.FrCircuitTable.FrCircuitEntry>`
        
        

        """

        _prefix = 'rfc1315-mib'

        def __init__(self):
            self.parent = None
            self.frcircuitentry = YList()
            self.frcircuitentry.parent = self
            self.frcircuitentry.name = 'frcircuitentry'


        class FrCircuitEntry(object):
            """
            The information regarding a single  Data  Link
            Connection Identifier.
            
            .. attribute:: frcircuitdlci
            
            	The Data Link Connection Identifier  for  this virtual circuit
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frcircuitifindex
            
            	The ifIndex Value of the ifEntry this  virtual circuit is layered onto
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cfrcircuitdeins
            
            	Number of packets received with the Discarded Eligibility indictor (the DE bit) set
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrcircuitdeouts
            
            	Number of packets transmitted with DE bit set
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrcircuitdroppktsouts
            
            	Number of discarded packets that were to be sent
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrcircuittype
            
            	Basic circuit type
            	**type**\: :py:class:`CfrCircuitType_Enum <ydk.models.rfc1315.RFC1315_MIB.RFC1315MIB.FrCircuitTable.FrCircuitEntry.CfrCircuitType_Enum>`
            
            .. attribute:: cfrextcircuitbandwidth
            
            	Bandwidth of the virtual circuit, acquired from  Cisco typed LMI Full Status message
            	**type**\: int
            
            	**range:** 0..16777215
            
            .. attribute:: cfrextcircuitbcastbyteouts
            
            	Total number of bytes sent out to the network in  broadcast packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrextcircuitbcastpktouts
            
            	Total number of broadcast packets sent out to the  network
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrextcircuitbecnouts
            
            	Total number of frames sent out to the network  indicating backward congestion
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrextcircuitcreatetype
            
            	Identify the last source of the circuit's creation
            	**type**\: :py:class:`CfrExtCircuitCreateType_Enum <ydk.models.rfc1315.RFC1315_MIB.RFC1315MIB.FrCircuitTable.FrCircuitEntry.CfrExtCircuitCreateType_Enum>`
            
            .. attribute:: cfrextcircuitfecnouts
            
            	Total number of frames sent out to the network  indicating forward congestion
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrextcircuitifname
            
            	The textual name of the main interface or the  subinterface that this DLCI is associated with. This is the same name string of an interface used in the configuration and all console displays, such as 'serial 0', 'serial 3/0.3', etc
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cfrextcircuitiftype
            
            	Type of the subinterface this DLCI is associated with, if configured
            	**type**\: :py:class:`CfrExtCircuitIfType_Enum <ydk.models.rfc1315.RFC1315_MIB.RFC1315MIB.FrCircuitTable.FrCircuitEntry.CfrExtCircuitIfType_Enum>`
            
            .. attribute:: cfrextcircuitmapstatus
            
            	The mapping protocols (internally considered as the 'link type') applied on this circuit. The value ranges from 0 to 2047. For point\-to\-point DLCI, the value stays zero. Otherwise, the value is a sum. It initially takes the value zero, then, for each type of Protocol, 2 raised to a power is added to the sum. The following table presents respective power and equivalent value for each applicable type\:          Protocol        Power    Value         \-\-\-\-\-\-\-\-        \-\-\-\-\-    \-\-\-\-\-         IP              0        1         IPX             1        2         Appletalk       2        4         XNS             3        8         VINES           4        16         DECnet          5        32         CLNS            6        64         Bridging        7        128         RSRB            8        256         STUN            9        512         LLC2            10       1024  For example, value 3 means the circuit's mapping protocols include IP and IPX. (3 = 2\*\*1 + 2\*\*0, where 0 corresponds to IP and 1 to IPX.) Value 0 means there is currently no mapping protocol for the circuit. See cfrMapTable for more mapping information
            	**type**\: int
            
            	**range:** 0..2047
            
            .. attribute:: cfrextcircuitminthruputin
            
            	Circuit's incoming minimal Throughput based on configuration
            	**type**\: int
            
            	**range:** 9600..1544000
            
            .. attribute:: cfrextcircuitminthruputout
            
            	Circuit's outgoing minimal Throughput based on  configuration
            	**type**\: int
            
            	**range:** 9600..1544000
            
            .. attribute:: cfrextcircuitmulticast
            
            	Indicate if this DLCI is a multicast DLCI
            	**type**\: bool
            
            .. attribute:: cfrextcircuitrcvdatarate
            
            	The average rate (bytes/second) at which data is  received in this circuit. 
            	**type**\: int
            
            	**range:** 1..45000000
            
            .. attribute:: cfrextcircuitrcvpktrate
            
            	The average number of packets received in a second in  this circuit. 
            	**type**\: int
            
            	**range:** 1..45000000
            
            .. attribute:: cfrextcircuitrouteddlci
            
            	The routed DLCI to pair up with this DLCI for switching function. NOTE\: Value zero (0) indicates that there is no such routed DLCI corresponding to this DLCI
            	**type**\: int
            
            	**range:** 0..1023
            
            .. attribute:: cfrextcircuitroutedif
            
            	The interface for the routed DLCI that pairs up with this DLCI for switching. Value greater than 0 is the InterfaceIndex for that interface. Value zero (0) indicates that there is no such routed DLCI corresponding to this DLCI
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cfrextcircuitshapeactive
            
            	Shows whether shaping is active or not
            	**type**\: bool
            
            .. attribute:: cfrextcircuitshapeadapting
            
            	Type of Adaptive Shaping configured. none(1)      \- No adaptive shaping configured becn(2)      \- Backward Explicit Congestion Notification foreSight(3) \- ForeSight is the network traffic control                 software used in Cisco WAN switches
            	**type**\: :py:class:`CfrExtCircuitShapeAdapting_Enum <ydk.models.rfc1315.RFC1315_MIB.RFC1315MIB.FrCircuitTable.FrCircuitEntry.CfrExtCircuitShapeAdapting_Enum>`
            
            .. attribute:: cfrextcircuitshapebyteincrement
            
            	Number of tokens added into the token bucket per time interval in case of traffic shaping
            	**type**\: int
            
            	**range:** 125..2147483647
            
            .. attribute:: cfrextcircuitshapebytelimit
            
            	Maximum number of tokens a token bucket can hold in any time interval in case of traffic shaping
            	**type**\: int
            
            	**range:** 125..2147483647
            
            .. attribute:: cfrextcircuitshapebytes
            
            	Total number of bytes that went through traffic  shaping
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrextcircuitshapebytesdelay
            
            	Total number of bytes that were delayed by the  traffic shaper
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrextcircuitshapeinterval
            
            	Committed rate measurement interval
            	**type**\: int
            
            	**range:** 10..125
            
            .. attribute:: cfrextcircuitshapepkts
            
            	Total number of packets that went through traffic  shaping
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrextcircuitshapepktsdelay
            
            	Total number of packets that were delayed by the  traffic shaper
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrextcircuitsubifindex
            
            	For value greater than zero (0), it indicates the network management interface index for the subinterface associated with this DLCI. Value 0 means the DLCI is not associated with any subinterface
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cfrextcircuittxdatarate
            
            	The average rate (bytes/second) at which data is  transmitted in this circuit. 
            	**type**\: int
            
            	**range:** 1..45000000
            
            .. attribute:: cfrextcircuittxpktrate
            
            	The average number of packets sent in a second in this  circuit
            	**type**\: int
            
            	**range:** 1..45000000
            
            .. attribute:: cfrextcircuituncompressins
            
            	Number of inbound octets of the data packets, accounted at Frame Relay level after FRF.9 payload decompression is applied. In the case of non\-FRF.9, this value could be identical to frCircuitReceivedOctets, unless otherwise noted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrextcircuituncompressouts
            
            	Number of outbound octets of the data packets, accounted at Frame Relay level before FRF.9 payload compression is applied. In the case of non\-FRF.9, this value could be identical to frCircuitSentOctets, unless otherwise noted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitcommittedburst
            
            	This variable indicates the maximum amount  of data,  in  bits,  that  the  network  agrees to transfer under normal  conditions,  during  the measurement interval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frcircuitcreationtime
            
            	The value of sysUpTime when the  virtual  cir\- cuit was created, whether by the Data Link Con\- nection Management Interface  or  by  a  SetRe\- quest
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitexcessburst
            
            	This variable indicates the maximum amount  of uncommitted data bits that the network will at\- tempt to deliver over the measurement interval.  By default, if not configured when creating the entry, the Excess Information Burst Size is set to the value of ifSpeed
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frcircuitlasttimechange
            
            	The value of sysUpTime when last there  was  a change in the virtual circuit state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceivedbecns
            
            	Number of frames received from the network in\- dicating  backward congestion since the virtual circuit was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceivedfecns
            
            	Number of frames received from the network in\- dicating  forward  congestion since the virtual circuit was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceivedframes
            
            	Number of frames received  over  this  virtual circuit since it was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceivedoctets
            
            	Number of octets received  over  this  virtual circuit since it was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitsentframes
            
            	The number of frames sent  from  this  virtual circuit since it was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitsentoctets
            
            	The number of octets sent  from  this  virtual circuit since it was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitstate
            
            	Indicates whether the particular virtual  cir\- cuit  is operational.  In the absence of a Data Link Connection Management  Interface,  virtual circuit  entries  (rows) may be created by set\- ting virtual  circuit  state  to  'active',  or deleted by changing Circuit state to 'invalid'. Whether or not the row actually  disappears  is left  to the implementation, so this object may actually read as 'invalid' for  some  arbitrary length  of  time.   It is also legal to set the state of a virtual  circuit  to  'inactive'  to temporarily disable a given circuit
            	**type**\: :py:class:`FrCircuitState_Enum <ydk.models.rfc1315.RFC1315_MIB.RFC1315MIB.FrCircuitTable.FrCircuitEntry.FrCircuitState_Enum>`
            
            .. attribute:: frcircuitthroughput
            
            	Throughput is the average number of 'Frame Re\- lay  Information  Field'  bits  transferred per second across a user network interface  in  one direction, measured over the measurement inter\- val.  If the  configured  committed  burst  rate  and throughput  are  both non\-zero, the measurement interval T=frCircuitCommittedBurst/frCircuitThroughput.  If the  configured  committed  burst  rate  and throughput  are  both zero, the measurement in\- terval        T=frCircuitExcessBurst/ifSpeed
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'rfc1315-mib'

            def __init__(self):
                self.parent = None
                self.frcircuitdlci = None
                self.frcircuitifindex = None
                self.cfrcircuitdeins = None
                self.cfrcircuitdeouts = None
                self.cfrcircuitdroppktsouts = None
                self.cfrcircuittype = None
                self.cfrextcircuitbandwidth = None
                self.cfrextcircuitbcastbyteouts = None
                self.cfrextcircuitbcastpktouts = None
                self.cfrextcircuitbecnouts = None
                self.cfrextcircuitcreatetype = None
                self.cfrextcircuitfecnouts = None
                self.cfrextcircuitifname = None
                self.cfrextcircuitiftype = None
                self.cfrextcircuitmapstatus = None
                self.cfrextcircuitminthruputin = None
                self.cfrextcircuitminthruputout = None
                self.cfrextcircuitmulticast = None
                self.cfrextcircuitrcvdatarate = None
                self.cfrextcircuitrcvpktrate = None
                self.cfrextcircuitrouteddlci = None
                self.cfrextcircuitroutedif = None
                self.cfrextcircuitshapeactive = None
                self.cfrextcircuitshapeadapting = None
                self.cfrextcircuitshapebyteincrement = None
                self.cfrextcircuitshapebytelimit = None
                self.cfrextcircuitshapebytes = None
                self.cfrextcircuitshapebytesdelay = None
                self.cfrextcircuitshapeinterval = None
                self.cfrextcircuitshapepkts = None
                self.cfrextcircuitshapepktsdelay = None
                self.cfrextcircuitsubifindex = None
                self.cfrextcircuittxdatarate = None
                self.cfrextcircuittxpktrate = None
                self.cfrextcircuituncompressins = None
                self.cfrextcircuituncompressouts = None
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

            class CfrCircuitType_Enum(Enum):
                """
                CfrCircuitType_Enum

                Basic circuit type

                """

                PVC = 1

                SVC = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1315._meta import _RFC1315_MIB as meta
                    return meta._meta_table['RFC1315MIB.FrCircuitTable.FrCircuitEntry.CfrCircuitType_Enum']


            class CfrExtCircuitCreateType_Enum(Enum):
                """
                CfrExtCircuitCreateType_Enum

                Identify the last source of the circuit's creation.

                """

                DYNAMIC = 1

                STATIC = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1315._meta import _RFC1315_MIB as meta
                    return meta._meta_table['RFC1315MIB.FrCircuitTable.FrCircuitEntry.CfrExtCircuitCreateType_Enum']


            class CfrExtCircuitIfType_Enum(Enum):
                """
                CfrExtCircuitIfType_Enum

                Type of the subinterface this DLCI is associated
                with, if configured.

                """

                MAININTERFACE = 1

                POINTTOPOINT = 2

                MULTIPOINT = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1315._meta import _RFC1315_MIB as meta
                    return meta._meta_table['RFC1315MIB.FrCircuitTable.FrCircuitEntry.CfrExtCircuitIfType_Enum']


            class CfrExtCircuitShapeAdapting_Enum(Enum):
                """
                CfrExtCircuitShapeAdapting_Enum

                Type of Adaptive Shaping configured.
                none(1)      \- No adaptive shaping configured
                becn(2)      \- Backward Explicit Congestion Notification
                foreSight(3) \- ForeSight is the network traffic control 
                               software used in Cisco WAN switches

                """

                NONE = 1

                BECN = 2

                FORESIGHT = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1315._meta import _RFC1315_MIB as meta
                    return meta._meta_table['RFC1315MIB.FrCircuitTable.FrCircuitEntry.CfrExtCircuitShapeAdapting_Enum']


            class FrCircuitState_Enum(Enum):
                """
                FrCircuitState_Enum

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

                """

                INVALID = 1

                ACTIVE = 2

                INACTIVE = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1315._meta import _RFC1315_MIB as meta
                    return meta._meta_table['RFC1315MIB.FrCircuitTable.FrCircuitEntry.FrCircuitState_Enum']


            @property
            def _common_path(self):
                if self.frcircuitdlci is None:
                    raise YPYDataValidationError('Key property frcircuitdlci is None')
                if self.frcircuitifindex is None:
                    raise YPYDataValidationError('Key property frcircuitifindex is None')

                return '/RFC1315-MIB:RFC1315-MIB/RFC1315-MIB:frCircuitTable/RFC1315-MIB:frCircuitEntry[RFC1315-MIB:frCircuitDlci = ' + str(self.frcircuitdlci) + '][RFC1315-MIB:frCircuitIfIndex = ' + str(self.frcircuitifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.frcircuitdlci is not None:
                    return True

                if self.frcircuitifindex is not None:
                    return True

                if self.cfrcircuitdeins is not None:
                    return True

                if self.cfrcircuitdeouts is not None:
                    return True

                if self.cfrcircuitdroppktsouts is not None:
                    return True

                if self.cfrcircuittype is not None:
                    return True

                if self.cfrextcircuitbandwidth is not None:
                    return True

                if self.cfrextcircuitbcastbyteouts is not None:
                    return True

                if self.cfrextcircuitbcastpktouts is not None:
                    return True

                if self.cfrextcircuitbecnouts is not None:
                    return True

                if self.cfrextcircuitcreatetype is not None:
                    return True

                if self.cfrextcircuitfecnouts is not None:
                    return True

                if self.cfrextcircuitifname is not None:
                    return True

                if self.cfrextcircuitiftype is not None:
                    return True

                if self.cfrextcircuitmapstatus is not None:
                    return True

                if self.cfrextcircuitminthruputin is not None:
                    return True

                if self.cfrextcircuitminthruputout is not None:
                    return True

                if self.cfrextcircuitmulticast is not None:
                    return True

                if self.cfrextcircuitrcvdatarate is not None:
                    return True

                if self.cfrextcircuitrcvpktrate is not None:
                    return True

                if self.cfrextcircuitrouteddlci is not None:
                    return True

                if self.cfrextcircuitroutedif is not None:
                    return True

                if self.cfrextcircuitshapeactive is not None:
                    return True

                if self.cfrextcircuitshapeadapting is not None:
                    return True

                if self.cfrextcircuitshapebyteincrement is not None:
                    return True

                if self.cfrextcircuitshapebytelimit is not None:
                    return True

                if self.cfrextcircuitshapebytes is not None:
                    return True

                if self.cfrextcircuitshapebytesdelay is not None:
                    return True

                if self.cfrextcircuitshapeinterval is not None:
                    return True

                if self.cfrextcircuitshapepkts is not None:
                    return True

                if self.cfrextcircuitshapepktsdelay is not None:
                    return True

                if self.cfrextcircuitsubifindex is not None:
                    return True

                if self.cfrextcircuittxdatarate is not None:
                    return True

                if self.cfrextcircuittxpktrate is not None:
                    return True

                if self.cfrextcircuituncompressins is not None:
                    return True

                if self.cfrextcircuituncompressouts is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1315._meta import _RFC1315_MIB as meta
                return meta._meta_table['RFC1315MIB.FrCircuitTable.FrCircuitEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1315-MIB:RFC1315-MIB/RFC1315-MIB:frCircuitTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.frcircuitentry is not None:
                for child_ref in self.frcircuitentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1315._meta import _RFC1315_MIB as meta
            return meta._meta_table['RFC1315MIB.FrCircuitTable']['meta_info']


    class FrDlcmiTable(object):
        """
        The Parameters for the Data Link Connection Management
        Interface for the frame relay service on this
        interface.
        
        .. attribute:: frdlcmientry
        
        	The Parameters for a particular Data Link Con\- nection Management Interface
        	**type**\: list of :py:class:`FrDlcmiEntry <ydk.models.rfc1315.RFC1315_MIB.RFC1315MIB.FrDlcmiTable.FrDlcmiEntry>`
        
        

        """

        _prefix = 'rfc1315-mib'

        def __init__(self):
            self.parent = None
            self.frdlcmientry = YList()
            self.frdlcmientry.parent = self
            self.frdlcmientry.name = 'frdlcmientry'


        class FrDlcmiEntry(object):
            """
            The Parameters for a particular Data Link Con\-
            nection Management Interface.
            
            .. attribute:: frdlcmiifindex
            
            	The ifIndex value of the  corresponding  ifEn\- try
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cfrlmienquiryins
            
            	Number of Status Enquiry messages received
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrlmienquiryouts
            
            	Number of Status Enquiry messages sent
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrlmilinkstatus
            
            	Data link status via LMI
            	**type**\: :py:class:`CfrLmiLinkstatus_Enum <ydk.models.rfc1315.RFC1315_MIB.RFC1315MIB.FrDlcmiTable.FrDlcmiEntry.CfrLmiLinkstatus_Enum>`
            
            .. attribute:: cfrlmilinktype
            
            	Frame Relay link type
            	**type**\: :py:class:`CfrLmiLinkType_Enum <ydk.models.rfc1315.RFC1315_MIB.RFC1315MIB.FrDlcmiTable.FrDlcmiEntry.CfrLmiLinkType_Enum>`
            
            .. attribute:: cfrlmin392dce
            
            	LMI error threshold for DCE interface. For DTE, value becomes 0
            	**type**\: int
            
            	**range:** 0..10
            
            .. attribute:: cfrlmin393dce
            
            	LMI monitored event count for DCE interface. For DTE, value becomes zero (0)
            	**type**\: int
            
            	**range:** 0..10
            
            .. attribute:: cfrlmistatusenqtimeouts
            
            	Number of times when timeout occurred on waiting for Status Enquiry message
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrlmistatusins
            
            	Number of Status messages received
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrlmistatusouts
            
            	Number of Status messages sent
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrlmistatustimeouts
            
            	Number of times when timeout occurred on waiting for Status message
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrlmit392dce
            
            	DCE polling verification timer for DCE interface For DTE, the value becomes zero (0)
            	**type**\: int
            
            	**range:** 0..30
            
            .. attribute:: cfrlmiupdatestatusins
            
            	Number of Update Status messages received
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrlmiupdatestatusouts
            
            	Number of Update Status messages sent
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frdlcmiaddress
            
            	This variable states which address  format  is in use on the Frame Relay interface
            	**type**\: :py:class:`FrDlcmiAddress_Enum <ydk.models.rfc1315.RFC1315_MIB.RFC1315MIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiAddress_Enum>`
            
            .. attribute:: frdlcmiaddresslen
            
            	This variable states which address  length  in octets.  In the case of Q922 format, the length indicates the entire length of the address  in\- cluding the control portion
            	**type**\: :py:class:`FrDlcmiAddressLen_Enum <ydk.models.rfc1315.RFC1315_MIB.RFC1315MIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiAddressLen_Enum>`
            
            .. attribute:: frdlcmierrorthreshold
            
            	This  is  the  maximum  number  of  unanswered Status Enquiries the equipment shall accept be\- fore declaring the interface down
            	**type**\: int
            
            	**range:** 1..10
            
            .. attribute:: frdlcmifullenquiryinterval
            
            	Number of status enquiry intervals  that  pass before  issuance  of a full status enquiry mes\- sage
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: frdlcmimaxsupportedvcs
            
            	The maximum number of Virtual Circuits allowed for  this  interface.   Usually dictated by the Frame Relay network.  In response to a SET, if a value less than zero or  higher  than the agent's maximal capability is configured, the agent  should  respond  bad\- Value
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frdlcmimonitoredevents
            
            	This is the number of status polling intervals over which the error threshold is counted.  For example, if within 'MonitoredEvents' number  of events  the  station  receives 'ErrorThreshold' number of errors, the interface  is  marked  as down
            	**type**\: int
            
            	**range:** 1..10
            
            .. attribute:: frdlcmimulticast
            
            	This indicates whether the Frame Relay  inter\- face is using a multicast service
            	**type**\: :py:class:`FrDlcmiMulticast_Enum <ydk.models.rfc1315.RFC1315_MIB.RFC1315MIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiMulticast_Enum>`
            
            .. attribute:: frdlcmipollinginterval
            
            	This is the number of seconds between  succes\- sive status enquiry messages
            	**type**\: int
            
            	**range:** 5..30
            
            .. attribute:: frdlcmistate
            
            	This variable states which Data  Link  Connec\- tion Management scheme is active (and by impli\- cation, what DLCI it uses) on the  Frame  Relay interface
            	**type**\: :py:class:`FrDlcmiState_Enum <ydk.models.rfc1315.RFC1315_MIB.RFC1315MIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiState_Enum>`
            
            

            """

            _prefix = 'rfc1315-mib'

            def __init__(self):
                self.parent = None
                self.frdlcmiifindex = None
                self.cfrlmienquiryins = None
                self.cfrlmienquiryouts = None
                self.cfrlmilinkstatus = None
                self.cfrlmilinktype = None
                self.cfrlmin392dce = None
                self.cfrlmin393dce = None
                self.cfrlmistatusenqtimeouts = None
                self.cfrlmistatusins = None
                self.cfrlmistatusouts = None
                self.cfrlmistatustimeouts = None
                self.cfrlmit392dce = None
                self.cfrlmiupdatestatusins = None
                self.cfrlmiupdatestatusouts = None
                self.frdlcmiaddress = None
                self.frdlcmiaddresslen = None
                self.frdlcmierrorthreshold = None
                self.frdlcmifullenquiryinterval = None
                self.frdlcmimaxsupportedvcs = None
                self.frdlcmimonitoredevents = None
                self.frdlcmimulticast = None
                self.frdlcmipollinginterval = None
                self.frdlcmistate = None

            class CfrLmiLinkType_Enum(Enum):
                """
                CfrLmiLinkType_Enum

                Frame Relay link type.

                """

                DTE = 1

                DCE = 2

                NNI = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1315._meta import _RFC1315_MIB as meta
                    return meta._meta_table['RFC1315MIB.FrDlcmiTable.FrDlcmiEntry.CfrLmiLinkType_Enum']


            class CfrLmiLinkstatus_Enum(Enum):
                """
                CfrLmiLinkstatus_Enum

                Data link status via LMI.

                """

                UP = 1

                DOWN = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1315._meta import _RFC1315_MIB as meta
                    return meta._meta_table['RFC1315MIB.FrDlcmiTable.FrDlcmiEntry.CfrLmiLinkstatus_Enum']


            class FrDlcmiAddressLen_Enum(Enum):
                """
                FrDlcmiAddressLen_Enum

                This variable states which address  length  in
                octets.  In the case of Q922 format, the length
                indicates the entire length of the address  in\-
                cluding the control portion.

                """

                TWO_OCTETS = 2

                THREE_OCTETS = 3

                FOUR_OCTETS = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1315._meta import _RFC1315_MIB as meta
                    return meta._meta_table['RFC1315MIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiAddressLen_Enum']


            class FrDlcmiAddress_Enum(Enum):
                """
                FrDlcmiAddress_Enum

                This variable states which address  format  is
                in use on the Frame Relay interface.

                """

                Q921 = 1

                Q922MARCH90 = 2

                Q922NOVEMBER90 = 3

                Q922 = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1315._meta import _RFC1315_MIB as meta
                    return meta._meta_table['RFC1315MIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiAddress_Enum']


            class FrDlcmiMulticast_Enum(Enum):
                """
                FrDlcmiMulticast_Enum

                This indicates whether the Frame Relay  inter\-
                face is using a multicast service.

                """

                NONBROADCAST = 1

                BROADCAST = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1315._meta import _RFC1315_MIB as meta
                    return meta._meta_table['RFC1315MIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiMulticast_Enum']


            class FrDlcmiState_Enum(Enum):
                """
                FrDlcmiState_Enum

                This variable states which Data  Link  Connec\-
                tion Management scheme is active (and by impli\-
                cation, what DLCI it uses) on the  Frame  Relay
                interface.

                """

                NOLMICONFIGURED = 1

                LMIREV1 = 2

                ANSIT1_617_D = 3

                ANSIT1_617_B = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1315._meta import _RFC1315_MIB as meta
                    return meta._meta_table['RFC1315MIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiState_Enum']


            @property
            def _common_path(self):
                if self.frdlcmiifindex is None:
                    raise YPYDataValidationError('Key property frdlcmiifindex is None')

                return '/RFC1315-MIB:RFC1315-MIB/RFC1315-MIB:frDlcmiTable/RFC1315-MIB:frDlcmiEntry[RFC1315-MIB:frDlcmiIfIndex = ' + str(self.frdlcmiifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.frdlcmiifindex is not None:
                    return True

                if self.cfrlmienquiryins is not None:
                    return True

                if self.cfrlmienquiryouts is not None:
                    return True

                if self.cfrlmilinkstatus is not None:
                    return True

                if self.cfrlmilinktype is not None:
                    return True

                if self.cfrlmin392dce is not None:
                    return True

                if self.cfrlmin393dce is not None:
                    return True

                if self.cfrlmistatusenqtimeouts is not None:
                    return True

                if self.cfrlmistatusins is not None:
                    return True

                if self.cfrlmistatusouts is not None:
                    return True

                if self.cfrlmistatustimeouts is not None:
                    return True

                if self.cfrlmit392dce is not None:
                    return True

                if self.cfrlmiupdatestatusins is not None:
                    return True

                if self.cfrlmiupdatestatusouts is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1315._meta import _RFC1315_MIB as meta
                return meta._meta_table['RFC1315MIB.FrDlcmiTable.FrDlcmiEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1315-MIB:RFC1315-MIB/RFC1315-MIB:frDlcmiTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.frdlcmientry is not None:
                for child_ref in self.frdlcmientry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1315._meta import _RFC1315_MIB as meta
            return meta._meta_table['RFC1315MIB.FrDlcmiTable']['meta_info']


    class FrErrTable(object):
        """
        A table containing information about Errors on the
        Frame Relay interface.
        
        .. attribute:: frerrentry
        
        	The error information for a single frame relay interface
        	**type**\: list of :py:class:`FrErrEntry <ydk.models.rfc1315.RFC1315_MIB.RFC1315MIB.FrErrTable.FrErrEntry>`
        
        

        """

        _prefix = 'rfc1315-mib'

        def __init__(self):
            self.parent = None
            self.frerrentry = YList()
            self.frerrentry.parent = self
            self.frerrentry.name = 'frerrentry'


        class FrErrEntry(object):
            """
            The error information for a single frame relay
            interface.
            
            .. attribute:: frerrifindex
            
            	The ifIndex Value of the  corresponding  ifEn\- try
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frerrdata
            
            	An octet string containing as much of the  er\- ror  packet as possible.  As a minimum, it must contain the Q.922 Address or  as  much  as  was delivered.   It is desirable to include all in\- formation up to the PDU
            	**type**\: str
            
            .. attribute:: frerrtime
            
            	The value of sysUpTime at which the error  was detected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frerrtype
            
            	The type of error that was last seen  on  this interface
            	**type**\: :py:class:`FrErrType_Enum <ydk.models.rfc1315.RFC1315_MIB.RFC1315MIB.FrErrTable.FrErrEntry.FrErrType_Enum>`
            
            

            """

            _prefix = 'rfc1315-mib'

            def __init__(self):
                self.parent = None
                self.frerrifindex = None
                self.frerrdata = None
                self.frerrtime = None
                self.frerrtype = None

            class FrErrType_Enum(Enum):
                """
                FrErrType_Enum

                The type of error that was last seen  on  this
                interface.

                """

                UNKNOWNERROR = 1

                RECEIVESHORT = 2

                RECEIVELONG = 3

                ILLEGALDLCI = 4

                UNKNOWNDLCI = 5

                DLCMIPROTOERR = 6

                DLCMIUNKNOWNIE = 7

                DLCMISEQUENCEERR = 8

                DLCMIUNKNOWNRPT = 9

                NOERRORSINCERESET = 10


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1315._meta import _RFC1315_MIB as meta
                    return meta._meta_table['RFC1315MIB.FrErrTable.FrErrEntry.FrErrType_Enum']


            @property
            def _common_path(self):
                if self.frerrifindex is None:
                    raise YPYDataValidationError('Key property frerrifindex is None')

                return '/RFC1315-MIB:RFC1315-MIB/RFC1315-MIB:frErrTable/RFC1315-MIB:frErrEntry[RFC1315-MIB:frErrIfIndex = ' + str(self.frerrifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.frerrifindex is not None:
                    return True

                if self.frerrdata is not None:
                    return True

                if self.frerrtime is not None:
                    return True

                if self.frerrtype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1315._meta import _RFC1315_MIB as meta
                return meta._meta_table['RFC1315MIB.FrErrTable.FrErrEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1315-MIB:RFC1315-MIB/RFC1315-MIB:frErrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.frerrentry is not None:
                for child_ref in self.frerrentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1315._meta import _RFC1315_MIB as meta
            return meta._meta_table['RFC1315MIB.FrErrTable']['meta_info']


    class FrameRelayGlobals(object):
        """
        
        
        .. attribute:: frtrapstate
        
        	This variable  indicates  whether  the  system produces the frDLCIStatusChange trap
        	**type**\: :py:class:`FrTrapState_Enum <ydk.models.rfc1315.RFC1315_MIB.RFC1315MIB.FrameRelayGlobals.FrTrapState_Enum>`
        
        

        """

        _prefix = 'rfc1315-mib'

        def __init__(self):
            self.parent = None
            self.frtrapstate = None

        class FrTrapState_Enum(Enum):
            """
            FrTrapState_Enum

            This variable  indicates  whether  the  system
            produces the frDLCIStatusChange trap.

            """

            ENABLED = 1

            DISABLED = 2


            @staticmethod
            def _meta_info():
                from ydk.models.rfc1315._meta import _RFC1315_MIB as meta
                return meta._meta_table['RFC1315MIB.FrameRelayGlobals.FrTrapState_Enum']


        @property
        def _common_path(self):

            return '/RFC1315-MIB:RFC1315-MIB/RFC1315-MIB:frame-relay-globals'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.frtrapstate is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1315._meta import _RFC1315_MIB as meta
            return meta._meta_table['RFC1315MIB.FrameRelayGlobals']['meta_info']

    @property
    def _common_path(self):

        return '/RFC1315-MIB:RFC1315-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.frame_relay_globals is not None and self.frame_relay_globals._has_data():
            return True

        if self.frame_relay_globals is not None and self.frame_relay_globals.is_presence():
            return True

        if self.frcircuittable is not None and self.frcircuittable._has_data():
            return True

        if self.frcircuittable is not None and self.frcircuittable.is_presence():
            return True

        if self.frdlcmitable is not None and self.frdlcmitable._has_data():
            return True

        if self.frdlcmitable is not None and self.frdlcmitable.is_presence():
            return True

        if self.frerrtable is not None and self.frerrtable._has_data():
            return True

        if self.frerrtable is not None and self.frerrtable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.rfc1315._meta import _RFC1315_MIB as meta
        return meta._meta_table['RFC1315MIB']['meta_info']



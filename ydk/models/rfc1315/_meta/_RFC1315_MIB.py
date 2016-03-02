


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'RFC1315MIB.FrCircuitTable.FrCircuitEntry.CfrCircuitType_Enum' : _MetaInfoEnum('CfrCircuitType_Enum', 'ydk.models.rfc1315.RFC1315_MIB',
        {
            'pvc':'PVC',
            'svc':'SVC',
        }, 'CISCO-FRAME-RELAY-MIB', _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB']),
    'RFC1315MIB.FrCircuitTable.FrCircuitEntry.CfrExtCircuitCreateType_Enum' : _MetaInfoEnum('CfrExtCircuitCreateType_Enum', 'ydk.models.rfc1315.RFC1315_MIB',
        {
            'dynamic':'DYNAMIC',
            'static':'STATIC',
        }, 'CISCO-FRAME-RELAY-MIB', _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB']),
    'RFC1315MIB.FrCircuitTable.FrCircuitEntry.CfrExtCircuitIfType_Enum' : _MetaInfoEnum('CfrExtCircuitIfType_Enum', 'ydk.models.rfc1315.RFC1315_MIB',
        {
            'mainInterface':'MAININTERFACE',
            'pointToPoint':'POINTTOPOINT',
            'multipoint':'MULTIPOINT',
        }, 'CISCO-FRAME-RELAY-MIB', _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB']),
    'RFC1315MIB.FrCircuitTable.FrCircuitEntry.CfrExtCircuitShapeAdapting_Enum' : _MetaInfoEnum('CfrExtCircuitShapeAdapting_Enum', 'ydk.models.rfc1315.RFC1315_MIB',
        {
            'none':'NONE',
            'becn':'BECN',
            'foreSight':'FORESIGHT',
        }, 'CISCO-FRAME-RELAY-MIB', _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB']),
    'RFC1315MIB.FrCircuitTable.FrCircuitEntry.FrCircuitState_Enum' : _MetaInfoEnum('FrCircuitState_Enum', 'ydk.models.rfc1315.RFC1315_MIB',
        {
            'invalid':'INVALID',
            'active':'ACTIVE',
            'inactive':'INACTIVE',
        }, 'RFC1315-MIB', _yang_ns._namespaces['RFC1315-MIB']),
    'RFC1315MIB.FrCircuitTable.FrCircuitEntry' : {
        'meta_info' : _MetaInfoClass('RFC1315MIB.FrCircuitTable.FrCircuitEntry',
            False, 
            [
            _MetaInfoClassMember('frCircuitDlci', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The Data Link Connection Identifier  for  this
                virtual circuit.
                ''',
                'frcircuitdlci',
                'RFC1315-MIB', True),
            _MetaInfoClassMember('frCircuitIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The ifIndex Value of the ifEntry this  virtual
                circuit is layered onto.
                ''',
                'frcircuitifindex',
                'RFC1315-MIB', True),
            _MetaInfoClassMember('cfrCircuitDEins', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of packets received with the Discarded
                Eligibility indictor (the DE bit) set.
                ''',
                'cfrcircuitdeins',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrCircuitDEouts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of packets transmitted with DE bit set.
                ''',
                'cfrcircuitdeouts',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrCircuitDropPktsOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of discarded packets that were to be sent.
                ''',
                'cfrcircuitdroppktsouts',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrCircuitType', REFERENCE_ENUM_CLASS, 'CfrCircuitType_Enum' , 'ydk.models.rfc1315.RFC1315_MIB', 'RFC1315MIB.FrCircuitTable.FrCircuitEntry.CfrCircuitType_Enum', 
                [], [], 
                '''                Basic circuit type
                ''',
                'cfrcircuittype',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitBandwidth', ATTRIBUTE, 'int' , None, None, 
                [(0, 16777215)], [], 
                '''                Bandwidth of the virtual circuit, acquired from 
                Cisco typed LMI Full Status message.
                ''',
                'cfrextcircuitbandwidth',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitBcastByteOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of bytes sent out to the network in 
                broadcast packets.
                ''',
                'cfrextcircuitbcastbyteouts',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitBcastPktOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of broadcast packets sent out to the 
                network.
                ''',
                'cfrextcircuitbcastpktouts',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitBECNOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of frames sent out to the network 
                indicating backward congestion.
                ''',
                'cfrextcircuitbecnouts',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitCreateType', REFERENCE_ENUM_CLASS, 'CfrExtCircuitCreateType_Enum' , 'ydk.models.rfc1315.RFC1315_MIB', 'RFC1315MIB.FrCircuitTable.FrCircuitEntry.CfrExtCircuitCreateType_Enum', 
                [], [], 
                '''                Identify the last source of the circuit's creation.
                ''',
                'cfrextcircuitcreatetype',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitFECNOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of frames sent out to the network 
                indicating forward congestion.
                ''',
                'cfrextcircuitfecnouts',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitIfName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The textual name of the main interface or the 
                subinterface that this DLCI is associated with.
                This is the same name string of an interface used
                in the configuration and all console displays,
                such as 'serial 0', 'serial 3/0.3', etc.
                ''',
                'cfrextcircuitifname',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitIfType', REFERENCE_ENUM_CLASS, 'CfrExtCircuitIfType_Enum' , 'ydk.models.rfc1315.RFC1315_MIB', 'RFC1315MIB.FrCircuitTable.FrCircuitEntry.CfrExtCircuitIfType_Enum', 
                [], [], 
                '''                Type of the subinterface this DLCI is associated
                with, if configured.
                ''',
                'cfrextcircuitiftype',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitMapStatus', ATTRIBUTE, 'int' , None, None, 
                [(0, 2047)], [], 
                '''                The mapping protocols (internally considered as
                the 'link type') applied on this circuit.
                The value ranges from 0 to 2047.
                For point-to-point DLCI, the value stays zero.
                Otherwise, the value is a sum. It initially takes
                the value zero, then, for each type of Protocol,
                2 raised to a power is added to the sum.
                The following table presents respective power and
                equivalent value for each applicable type:
                
                        Protocol        Power    Value
                        --------        -----    -----
                        IP              0        1
                        IPX             1        2
                        Appletalk       2        4
                        XNS             3        8
                        VINES           4        16
                        DECnet          5        32
                        CLNS            6        64
                        Bridging        7        128
                        RSRB            8        256
                        STUN            9        512
                        LLC2            10       1024
                
                For example, value 3 means the circuit's mapping
                protocols include IP and IPX. (3 = 2**1 + 2**0,
                where 0 corresponds to IP and 1 to IPX.) Value 0
                means there is currently no mapping protocol for
                the circuit.
                See cfrMapTable for more mapping information.
                ''',
                'cfrextcircuitmapstatus',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitMinThruputIn', ATTRIBUTE, 'int' , None, None, 
                [(9600, 1544000)], [], 
                '''                Circuit's incoming minimal Throughput based on
                configuration.
                ''',
                'cfrextcircuitminthruputin',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitMinThruputOut', ATTRIBUTE, 'int' , None, None, 
                [(9600, 1544000)], [], 
                '''                Circuit's outgoing minimal Throughput based on 
                configuration.
                ''',
                'cfrextcircuitminthruputout',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitMulticast', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicate if this DLCI is a multicast DLCI.
                ''',
                'cfrextcircuitmulticast',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitRcvDataRate', ATTRIBUTE, 'int' , None, None, 
                [(1, 45000000)], [], 
                '''                The average rate (bytes/second) at which data is 
                received in this circuit. 
                ''',
                'cfrextcircuitrcvdatarate',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitRcvPktRate', ATTRIBUTE, 'int' , None, None, 
                [(1, 45000000)], [], 
                '''                The average number of packets received in a second in 
                this circuit. 
                ''',
                'cfrextcircuitrcvpktrate',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitRoutedDlci', ATTRIBUTE, 'int' , None, None, 
                [(0, 1023)], [], 
                '''                The routed DLCI to pair up with this DLCI
                for switching function. NOTE: Value zero (0)
                indicates that there is no such routed DLCI
                corresponding to this DLCI.
                ''',
                'cfrextcircuitrouteddlci',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitRoutedIf', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The interface for the routed DLCI that pairs up
                with this DLCI for switching. Value greater than 0
                is the InterfaceIndex for that interface. Value
                zero (0) indicates that there is no such routed DLCI
                corresponding to this DLCI.
                ''',
                'cfrextcircuitroutedif',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitShapeActive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Shows whether shaping is active or not.
                ''',
                'cfrextcircuitshapeactive',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitShapeAdapting', REFERENCE_ENUM_CLASS, 'CfrExtCircuitShapeAdapting_Enum' , 'ydk.models.rfc1315.RFC1315_MIB', 'RFC1315MIB.FrCircuitTable.FrCircuitEntry.CfrExtCircuitShapeAdapting_Enum', 
                [], [], 
                '''                Type of Adaptive Shaping configured.
                none(1)      - No adaptive shaping configured
                becn(2)      - Backward Explicit Congestion Notification
                foreSight(3) - ForeSight is the network traffic control 
                               software used in Cisco WAN switches
                ''',
                'cfrextcircuitshapeadapting',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitShapeByteIncrement', ATTRIBUTE, 'int' , None, None, 
                [(125, 2147483647)], [], 
                '''                Number of tokens added into the token bucket per time
                interval in case of traffic shaping.
                ''',
                'cfrextcircuitshapebyteincrement',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitShapeByteLimit', ATTRIBUTE, 'int' , None, None, 
                [(125, 2147483647)], [], 
                '''                Maximum number of tokens a token bucket can hold in any
                time interval in case of traffic shaping.
                ''',
                'cfrextcircuitshapebytelimit',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitShapeBytes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of bytes that went through traffic 
                shaping.
                ''',
                'cfrextcircuitshapebytes',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitShapeBytesDelay', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of bytes that were delayed by the 
                traffic shaper.
                ''',
                'cfrextcircuitshapebytesdelay',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitShapeInterval', ATTRIBUTE, 'int' , None, None, 
                [(10, 125)], [], 
                '''                Committed rate measurement interval.
                ''',
                'cfrextcircuitshapeinterval',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitShapePkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of packets that went through traffic 
                shaping.
                ''',
                'cfrextcircuitshapepkts',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitShapePktsDelay', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of packets that were delayed by the 
                traffic shaper.
                ''',
                'cfrextcircuitshapepktsdelay',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitSubifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                For value greater than zero (0), it indicates
                the network management interface index
                for the subinterface associated with
                this DLCI. Value 0 means the DLCI is not
                associated with any subinterface.
                ''',
                'cfrextcircuitsubifindex',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitTxDataRate', ATTRIBUTE, 'int' , None, None, 
                [(1, 45000000)], [], 
                '''                The average rate (bytes/second) at which data is 
                transmitted in this circuit. 
                ''',
                'cfrextcircuittxdatarate',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitTxPktRate', ATTRIBUTE, 'int' , None, None, 
                [(1, 45000000)], [], 
                '''                The average number of packets sent in a second in this 
                circuit.
                ''',
                'cfrextcircuittxpktrate',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitUncompressIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of inbound octets of the data packets,
                accounted at Frame Relay level after FRF.9
                payload decompression is applied. In the case of
                non-FRF.9, this value could be identical to
                frCircuitReceivedOctets, unless otherwise noted.
                ''',
                'cfrextcircuituncompressins',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrExtCircuitUncompressOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of outbound octets of the data packets,
                accounted at Frame Relay level before FRF.9
                payload compression is applied. In the case of
                non-FRF.9, this value could be identical to
                frCircuitSentOctets, unless otherwise noted.
                ''',
                'cfrextcircuituncompressouts',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('frCircuitCommittedBurst', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                This variable indicates the maximum amount  of
                data,  in  bits,  that  the  network  agrees to
                transfer under normal  conditions,  during  the
                measurement interval.
                ''',
                'frcircuitcommittedburst',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frCircuitCreationTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime when the  virtual  cir-
                cuit was created, whether by the Data Link Con-
                nection Management Interface  or  by  a  SetRe-
                quest.
                ''',
                'frcircuitcreationtime',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frCircuitExcessBurst', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                This variable indicates the maximum amount  of
                uncommitted data bits that the network will at-
                tempt to deliver over the measurement interval.
                
                By default, if not configured when creating the
                entry, the Excess Information Burst Size is set
                to the value of ifSpeed.
                ''',
                'frcircuitexcessburst',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frCircuitLastTimeChange', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime when last there  was  a
                change in the virtual circuit state
                ''',
                'frcircuitlasttimechange',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frCircuitReceivedBECNs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of frames received from the network in-
                dicating  backward congestion since the virtual
                circuit was created.
                ''',
                'frcircuitreceivedbecns',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frCircuitReceivedFECNs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of frames received from the network in-
                dicating  forward  congestion since the virtual
                circuit was created.
                ''',
                'frcircuitreceivedfecns',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frCircuitReceivedFrames', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of frames received  over  this  virtual
                circuit since it was created.
                ''',
                'frcircuitreceivedframes',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frCircuitReceivedOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of octets received  over  this  virtual
                circuit since it was created.
                ''',
                'frcircuitreceivedoctets',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frCircuitSentFrames', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of frames sent  from  this  virtual
                circuit since it was created.
                ''',
                'frcircuitsentframes',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frCircuitSentOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of octets sent  from  this  virtual
                circuit since it was created.
                ''',
                'frcircuitsentoctets',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frCircuitState', REFERENCE_ENUM_CLASS, 'FrCircuitState_Enum' , 'ydk.models.rfc1315.RFC1315_MIB', 'RFC1315MIB.FrCircuitTable.FrCircuitEntry.FrCircuitState_Enum', 
                [], [], 
                '''                Indicates whether the particular virtual  cir-
                cuit  is operational.  In the absence of a Data
                Link Connection Management  Interface,  virtual
                circuit  entries  (rows) may be created by set-
                ting virtual  circuit  state  to  'active',  or
                deleted by changing Circuit state to 'invalid'.
                Whether or not the row actually  disappears  is
                left  to the implementation, so this object may
                actually read as 'invalid' for  some  arbitrary
                length  of  time.   It is also legal to set the
                state of a virtual  circuit  to  'inactive'  to
                temporarily disable a given circuit.
                ''',
                'frcircuitstate',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frCircuitThroughput', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Throughput is the average number of 'Frame Re-
                lay  Information  Field'  bits  transferred per
                second across a user network interface  in  one
                direction, measured over the measurement inter-
                val.
                
                If the  configured  committed  burst  rate  and
                throughput  are  both non-zero, the measurement
                interval
                T=frCircuitCommittedBurst/frCircuitThroughput.
                
                If the  configured  committed  burst  rate  and
                throughput  are  both zero, the measurement in-
                terval
                       T=frCircuitExcessBurst/ifSpeed.
                ''',
                'frcircuitthroughput',
                'RFC1315-MIB', False),
            ],
            'RFC1315-MIB',
            'frCircuitEntry',
            _yang_ns._namespaces['RFC1315-MIB'],
        'ydk.models.rfc1315.RFC1315_MIB'
        ),
    },
    'RFC1315MIB.FrCircuitTable' : {
        'meta_info' : _MetaInfoClass('RFC1315MIB.FrCircuitTable',
            False, 
            [
            _MetaInfoClassMember('frCircuitEntry', REFERENCE_LIST, 'FrCircuitEntry' , 'ydk.models.rfc1315.RFC1315_MIB', 'RFC1315MIB.FrCircuitTable.FrCircuitEntry', 
                [], [], 
                '''                The information regarding a single  Data  Link
                Connection Identifier.
                ''',
                'frcircuitentry',
                'RFC1315-MIB', False),
            ],
            'RFC1315-MIB',
            'frCircuitTable',
            _yang_ns._namespaces['RFC1315-MIB'],
        'ydk.models.rfc1315.RFC1315_MIB'
        ),
    },
    'RFC1315MIB.FrDlcmiTable.FrDlcmiEntry.CfrLmiLinkType_Enum' : _MetaInfoEnum('CfrLmiLinkType_Enum', 'ydk.models.rfc1315.RFC1315_MIB',
        {
            'dte':'DTE',
            'dce':'DCE',
            'nni':'NNI',
        }, 'CISCO-FRAME-RELAY-MIB', _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB']),
    'RFC1315MIB.FrDlcmiTable.FrDlcmiEntry.CfrLmiLinkstatus_Enum' : _MetaInfoEnum('CfrLmiLinkstatus_Enum', 'ydk.models.rfc1315.RFC1315_MIB',
        {
            'up':'UP',
            'down':'DOWN',
        }, 'CISCO-FRAME-RELAY-MIB', _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB']),
    'RFC1315MIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiAddressLen_Enum' : _MetaInfoEnum('FrDlcmiAddressLen_Enum', 'ydk.models.rfc1315.RFC1315_MIB',
        {
            'two-octets':'TWO_OCTETS',
            'three-octets':'THREE_OCTETS',
            'four-octets':'FOUR_OCTETS',
        }, 'RFC1315-MIB', _yang_ns._namespaces['RFC1315-MIB']),
    'RFC1315MIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiAddress_Enum' : _MetaInfoEnum('FrDlcmiAddress_Enum', 'ydk.models.rfc1315.RFC1315_MIB',
        {
            'q921':'Q921',
            'q922March90':'Q922MARCH90',
            'q922November90':'Q922NOVEMBER90',
            'q922':'Q922',
        }, 'RFC1315-MIB', _yang_ns._namespaces['RFC1315-MIB']),
    'RFC1315MIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiMulticast_Enum' : _MetaInfoEnum('FrDlcmiMulticast_Enum', 'ydk.models.rfc1315.RFC1315_MIB',
        {
            'nonBroadcast':'NONBROADCAST',
            'broadcast':'BROADCAST',
        }, 'RFC1315-MIB', _yang_ns._namespaces['RFC1315-MIB']),
    'RFC1315MIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiState_Enum' : _MetaInfoEnum('FrDlcmiState_Enum', 'ydk.models.rfc1315.RFC1315_MIB',
        {
            'noLmiConfigured':'NOLMICONFIGURED',
            'lmiRev1':'LMIREV1',
            'ansiT1-617-D':'ANSIT1_617_D',
            'ansiT1-617-B':'ANSIT1_617_B',
        }, 'RFC1315-MIB', _yang_ns._namespaces['RFC1315-MIB']),
    'RFC1315MIB.FrDlcmiTable.FrDlcmiEntry' : {
        'meta_info' : _MetaInfoClass('RFC1315MIB.FrDlcmiTable.FrDlcmiEntry',
            False, 
            [
            _MetaInfoClassMember('frDlcmiIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The ifIndex value of the  corresponding  ifEn-
                try.
                ''',
                'frdlcmiifindex',
                'RFC1315-MIB', True),
            _MetaInfoClassMember('cfrLmiEnquiryIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Status Enquiry messages received.
                ''',
                'cfrlmienquiryins',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrLmiEnquiryOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Status Enquiry messages sent.
                ''',
                'cfrlmienquiryouts',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrLmiLinkstatus', REFERENCE_ENUM_CLASS, 'CfrLmiLinkstatus_Enum' , 'ydk.models.rfc1315.RFC1315_MIB', 'RFC1315MIB.FrDlcmiTable.FrDlcmiEntry.CfrLmiLinkstatus_Enum', 
                [], [], 
                '''                Data link status via LMI.
                ''',
                'cfrlmilinkstatus',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrLmiLinkType', REFERENCE_ENUM_CLASS, 'CfrLmiLinkType_Enum' , 'ydk.models.rfc1315.RFC1315_MIB', 'RFC1315MIB.FrDlcmiTable.FrDlcmiEntry.CfrLmiLinkType_Enum', 
                [], [], 
                '''                Frame Relay link type.
                ''',
                'cfrlmilinktype',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrLmiN392Dce', ATTRIBUTE, 'int' , None, None, 
                [(0, 10)], [], 
                '''                LMI error threshold for DCE interface.
                For DTE, value becomes 0.
                ''',
                'cfrlmin392dce',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrLmiN393Dce', ATTRIBUTE, 'int' , None, None, 
                [(0, 10)], [], 
                '''                LMI monitored event count for DCE interface.
                For DTE, value becomes zero (0).
                ''',
                'cfrlmin393dce',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrLmiStatusEnqTimeouts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of times when timeout occurred on waiting
                for Status Enquiry message
                ''',
                'cfrlmistatusenqtimeouts',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrLmiStatusIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Status messages received.
                ''',
                'cfrlmistatusins',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrLmiStatusOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Status messages sent.
                ''',
                'cfrlmistatusouts',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrLmiStatusTimeouts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of times when timeout occurred on waiting
                for Status message
                ''',
                'cfrlmistatustimeouts',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrLmiT392Dce', ATTRIBUTE, 'int' , None, None, 
                [(0, 30)], [], 
                '''                DCE polling verification timer for DCE interface
                For DTE, the value becomes zero (0).
                ''',
                'cfrlmit392dce',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrLmiUpdateStatusIns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Update Status messages received.
                ''',
                'cfrlmiupdatestatusins',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrLmiUpdateStatusOuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Update Status messages sent
                ''',
                'cfrlmiupdatestatusouts',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('frDlcmiAddress', REFERENCE_ENUM_CLASS, 'FrDlcmiAddress_Enum' , 'ydk.models.rfc1315.RFC1315_MIB', 'RFC1315MIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiAddress_Enum', 
                [], [], 
                '''                This variable states which address  format  is
                in use on the Frame Relay interface.
                ''',
                'frdlcmiaddress',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frDlcmiAddressLen', REFERENCE_ENUM_CLASS, 'FrDlcmiAddressLen_Enum' , 'ydk.models.rfc1315.RFC1315_MIB', 'RFC1315MIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiAddressLen_Enum', 
                [], [], 
                '''                This variable states which address  length  in
                octets.  In the case of Q922 format, the length
                indicates the entire length of the address  in-
                cluding the control portion.
                ''',
                'frdlcmiaddresslen',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frDlcmiErrorThreshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 10)], [], 
                '''                This  is  the  maximum  number  of  unanswered
                Status Enquiries the equipment shall accept be-
                fore declaring the interface down.
                ''',
                'frdlcmierrorthreshold',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frDlcmiFullEnquiryInterval', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Number of status enquiry intervals  that  pass
                before  issuance  of a full status enquiry mes-
                sage.
                ''',
                'frdlcmifullenquiryinterval',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frDlcmiMaxSupportedVCs', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The maximum number of Virtual Circuits allowed
                for  this  interface.   Usually dictated by the
                Frame Relay network.
                
                In response to a SET, if a value less than zero
                or  higher  than the agent's maximal capability
                is configured, the agent  should  respond  bad-
                Value
                ''',
                'frdlcmimaxsupportedvcs',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frDlcmiMonitoredEvents', ATTRIBUTE, 'int' , None, None, 
                [(1, 10)], [], 
                '''                This is the number of status polling intervals
                over which the error threshold is counted.  For
                example, if within 'MonitoredEvents' number  of
                events  the  station  receives 'ErrorThreshold'
                number of errors, the interface  is  marked  as
                down.
                ''',
                'frdlcmimonitoredevents',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frDlcmiMulticast', REFERENCE_ENUM_CLASS, 'FrDlcmiMulticast_Enum' , 'ydk.models.rfc1315.RFC1315_MIB', 'RFC1315MIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiMulticast_Enum', 
                [], [], 
                '''                This indicates whether the Frame Relay  inter-
                face is using a multicast service.
                ''',
                'frdlcmimulticast',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frDlcmiPollingInterval', ATTRIBUTE, 'int' , None, None, 
                [(5, 30)], [], 
                '''                This is the number of seconds between  succes-
                sive status enquiry messages.
                ''',
                'frdlcmipollinginterval',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frDlcmiState', REFERENCE_ENUM_CLASS, 'FrDlcmiState_Enum' , 'ydk.models.rfc1315.RFC1315_MIB', 'RFC1315MIB.FrDlcmiTable.FrDlcmiEntry.FrDlcmiState_Enum', 
                [], [], 
                '''                This variable states which Data  Link  Connec-
                tion Management scheme is active (and by impli-
                cation, what DLCI it uses) on the  Frame  Relay
                interface.
                ''',
                'frdlcmistate',
                'RFC1315-MIB', False),
            ],
            'RFC1315-MIB',
            'frDlcmiEntry',
            _yang_ns._namespaces['RFC1315-MIB'],
        'ydk.models.rfc1315.RFC1315_MIB'
        ),
    },
    'RFC1315MIB.FrDlcmiTable' : {
        'meta_info' : _MetaInfoClass('RFC1315MIB.FrDlcmiTable',
            False, 
            [
            _MetaInfoClassMember('frDlcmiEntry', REFERENCE_LIST, 'FrDlcmiEntry' , 'ydk.models.rfc1315.RFC1315_MIB', 'RFC1315MIB.FrDlcmiTable.FrDlcmiEntry', 
                [], [], 
                '''                The Parameters for a particular Data Link Con-
                nection Management Interface.
                ''',
                'frdlcmientry',
                'RFC1315-MIB', False),
            ],
            'RFC1315-MIB',
            'frDlcmiTable',
            _yang_ns._namespaces['RFC1315-MIB'],
        'ydk.models.rfc1315.RFC1315_MIB'
        ),
    },
    'RFC1315MIB.FrErrTable.FrErrEntry.FrErrType_Enum' : _MetaInfoEnum('FrErrType_Enum', 'ydk.models.rfc1315.RFC1315_MIB',
        {
            'unknownError':'UNKNOWNERROR',
            'receiveShort':'RECEIVESHORT',
            'receiveLong':'RECEIVELONG',
            'illegalDLCI':'ILLEGALDLCI',
            'unknownDLCI':'UNKNOWNDLCI',
            'dlcmiProtoErr':'DLCMIPROTOERR',
            'dlcmiUnknownIE':'DLCMIUNKNOWNIE',
            'dlcmiSequenceErr':'DLCMISEQUENCEERR',
            'dlcmiUnknownRpt':'DLCMIUNKNOWNRPT',
            'noErrorSinceReset':'NOERRORSINCERESET',
        }, 'RFC1315-MIB', _yang_ns._namespaces['RFC1315-MIB']),
    'RFC1315MIB.FrErrTable.FrErrEntry' : {
        'meta_info' : _MetaInfoClass('RFC1315MIB.FrErrTable.FrErrEntry',
            False, 
            [
            _MetaInfoClassMember('frErrIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The ifIndex Value of the  corresponding  ifEn-
                try.
                ''',
                'frerrifindex',
                'RFC1315-MIB', True),
            _MetaInfoClassMember('frErrData', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                An octet string containing as much of the  er-
                ror  packet as possible.  As a minimum, it must
                contain the Q.922 Address or  as  much  as  was
                delivered.   It is desirable to include all in-
                formation up to the PDU.
                ''',
                'frerrdata',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frErrTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime at which the error  was
                detected.
                ''',
                'frerrtime',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frErrType', REFERENCE_ENUM_CLASS, 'FrErrType_Enum' , 'ydk.models.rfc1315.RFC1315_MIB', 'RFC1315MIB.FrErrTable.FrErrEntry.FrErrType_Enum', 
                [], [], 
                '''                The type of error that was last seen  on  this
                interface.
                ''',
                'frerrtype',
                'RFC1315-MIB', False),
            ],
            'RFC1315-MIB',
            'frErrEntry',
            _yang_ns._namespaces['RFC1315-MIB'],
        'ydk.models.rfc1315.RFC1315_MIB'
        ),
    },
    'RFC1315MIB.FrErrTable' : {
        'meta_info' : _MetaInfoClass('RFC1315MIB.FrErrTable',
            False, 
            [
            _MetaInfoClassMember('frErrEntry', REFERENCE_LIST, 'FrErrEntry' , 'ydk.models.rfc1315.RFC1315_MIB', 'RFC1315MIB.FrErrTable.FrErrEntry', 
                [], [], 
                '''                The error information for a single frame relay
                interface.
                ''',
                'frerrentry',
                'RFC1315-MIB', False),
            ],
            'RFC1315-MIB',
            'frErrTable',
            _yang_ns._namespaces['RFC1315-MIB'],
        'ydk.models.rfc1315.RFC1315_MIB'
        ),
    },
    'RFC1315MIB.FrameRelayGlobals.FrTrapState_Enum' : _MetaInfoEnum('FrTrapState_Enum', 'ydk.models.rfc1315.RFC1315_MIB',
        {
            'enabled':'ENABLED',
            'disabled':'DISABLED',
        }, 'RFC1315-MIB', _yang_ns._namespaces['RFC1315-MIB']),
    'RFC1315MIB.FrameRelayGlobals' : {
        'meta_info' : _MetaInfoClass('RFC1315MIB.FrameRelayGlobals',
            False, 
            [
            _MetaInfoClassMember('frTrapState', REFERENCE_ENUM_CLASS, 'FrTrapState_Enum' , 'ydk.models.rfc1315.RFC1315_MIB', 'RFC1315MIB.FrameRelayGlobals.FrTrapState_Enum', 
                [], [], 
                '''                This variable  indicates  whether  the  system
                produces the frDLCIStatusChange trap.
                ''',
                'frtrapstate',
                'RFC1315-MIB', False),
            ],
            'RFC1315-MIB',
            'frame-relay-globals',
            _yang_ns._namespaces['RFC1315-MIB'],
        'ydk.models.rfc1315.RFC1315_MIB'
        ),
    },
    'RFC1315MIB' : {
        'meta_info' : _MetaInfoClass('RFC1315MIB',
            False, 
            [
            _MetaInfoClassMember('frame-relay-globals', REFERENCE_CLASS, 'FrameRelayGlobals' , 'ydk.models.rfc1315.RFC1315_MIB', 'RFC1315MIB.FrameRelayGlobals', 
                [], [], 
                '''                ''',
                'frame_relay_globals',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frCircuitTable', REFERENCE_CLASS, 'FrCircuitTable' , 'ydk.models.rfc1315.RFC1315_MIB', 'RFC1315MIB.FrCircuitTable', 
                [], [], 
                '''                A table containing information about specific Data
                Link Connection Identifiers and corresponding virtual
                circuits.
                ''',
                'frcircuittable',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frDlcmiTable', REFERENCE_CLASS, 'FrDlcmiTable' , 'ydk.models.rfc1315.RFC1315_MIB', 'RFC1315MIB.FrDlcmiTable', 
                [], [], 
                '''                The Parameters for the Data Link Connection Management
                Interface for the frame relay service on this
                interface.
                ''',
                'frdlcmitable',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frErrTable', REFERENCE_CLASS, 'FrErrTable' , 'ydk.models.rfc1315.RFC1315_MIB', 'RFC1315MIB.FrErrTable', 
                [], [], 
                '''                A table containing information about Errors on the
                Frame Relay interface.
                ''',
                'frerrtable',
                'RFC1315-MIB', False),
            ],
            'RFC1315-MIB',
            'RFC1315-MIB',
            _yang_ns._namespaces['RFC1315-MIB'],
        'ydk.models.rfc1315.RFC1315_MIB'
        ),
    },
}
_meta_table['RFC1315MIB.FrCircuitTable.FrCircuitEntry']['meta_info'].parent =_meta_table['RFC1315MIB.FrCircuitTable']['meta_info']
_meta_table['RFC1315MIB.FrDlcmiTable.FrDlcmiEntry']['meta_info'].parent =_meta_table['RFC1315MIB.FrDlcmiTable']['meta_info']
_meta_table['RFC1315MIB.FrErrTable.FrErrEntry']['meta_info'].parent =_meta_table['RFC1315MIB.FrErrTable']['meta_info']
_meta_table['RFC1315MIB.FrCircuitTable']['meta_info'].parent =_meta_table['RFC1315MIB']['meta_info']
_meta_table['RFC1315MIB.FrDlcmiTable']['meta_info'].parent =_meta_table['RFC1315MIB']['meta_info']
_meta_table['RFC1315MIB.FrErrTable']['meta_info'].parent =_meta_table['RFC1315MIB']['meta_info']
_meta_table['RFC1315MIB.FrameRelayGlobals']['meta_info'].parent =_meta_table['RFC1315MIB']['meta_info']

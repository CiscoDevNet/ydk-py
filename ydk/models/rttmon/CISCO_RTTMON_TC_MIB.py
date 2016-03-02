""" CISCO_RTTMON_TC_MIB 

This MIB contains textual conventions used by
CISCO\-RTTMON\-MIB, CISCO\-RTTMON\-RTP\-MIB and 
CISCO\-RTTMON\-ICMP\-MIB, but they are not limited 
to only these MIBs. 
These textual conventions were originally defined in 
CISCO\-RTTMON\-MIB.

Acronyms\:
  FEC\: Forward Equivalence Class
  LPD\: Label Path Discovery
  LSP\: Label Switched Path
  MPLS\: Multi Protocol Label Switching
  RTT\: Round Trip Time
  SAA\: Service Assurance Agent
  VPN\: Virtual Private Network
  CFM\: Connection Fault Management

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class RttMonCodecType_Enum(Enum):
    """
    RttMonCodecType_Enum

    Specifies the codec type to be used with the jitter probe.
    The following codec types are defined\:
    
    notApplicable     \- no CodecType is defined
    g711ulaw          \- uses G.711 U Law 64000 bps
    g711alaw          \- uses G.711 A Law 64000 bps
    g729a             \- uses G.729 8000 bps

    """

    NOTAPPLICABLE = 0

    G711ULAW = 1

    G711ALAW = 2

    G729A = 3


    @staticmethod
    def _meta_info():
        from ydk.models.rttmon._meta import _CISCO_RTTMON_TC_MIB as meta
        return meta._meta_table['RttMonCodecType_Enum']


class RttMonLSPPingReplyMode_Enum(Enum):
    """
    RttMonLSPPingReplyMode_Enum

    Specifies the Reply mode for the MPLS LSP Echo request
    packets. The following reply modes are supported\:
    
    replyIpv4Udp(1)         \- an mpls echo request will normally
                             have reply via IPv4 UDP packets.
    replyIpv4UdpRA(2)       \- reply via IPv4 UDP Router Alert. Used
                             when IPv4 return path is deemed 
                             unreliable.

    """

    REPLYIPV4UDP = 1

    REPLYIPV4UDPRA = 2


    @staticmethod
    def _meta_info():
        from ydk.models.rttmon._meta import _CISCO_RTTMON_TC_MIB as meta
        return meta._meta_table['RttMonLSPPingReplyMode_Enum']


class RttMonOperation_Enum(Enum):
    """
    RttMonOperation_Enum

    The following are specific RTT operations for a
    particular probe type\:
    notApplicable(0)         \- This object is not applicable for the
                               probe type.
    httpGet(1)               \- HTTP get request
    httpRaw(2)               \- HTTP request with user defined payload
    ftpGet(3)                \- FTP get request
    ftpPassive(4)            \- FTP passive mode
    ftpActive(5)             \- FTP active mode
    voipDTAlertRinging(6)    \- Voip post dial delay detect point\:
                               Alerting / Ringing
    voipDTConnectOK(7)       \- Voip post dial delay detect point\:
                               Connect /OK

    """

    NOTAPPLICABLE = 0

    HTTPGET = 1

    HTTPRAW = 2

    FTPGET = 3

    FTPPASSIVE = 4

    FTPACTIVE = 5

    VOIPDTALERTRINGING = 6

    VOIPDTCONNECTOK = 7


    @staticmethod
    def _meta_info():
        from ydk.models.rttmon._meta import _CISCO_RTTMON_TC_MIB as meta
        return meta._meta_table['RttMonOperation_Enum']


class RttMonProtocol_Enum(Enum):
    """
    RttMonProtocol_Enum

    Specifies the protocol to be used to perform the timed
    echo request/response.  The following protocols are
    defined\:
    
    NOTE\: All protocols that end in 'Appl' will support
          the asymetric request/response (ARR) protocol.  
          See the DESCRIPTION for ciscoRttMonMIB for a
          complete description of the asymetric 
          request/response protocol.
    
    notApplicable     \- no protocol is defined
    ipIcmpEcho        \- uses Echo Request/Reply as defined
                         in RFC792 for Internet Protocol
                         networks
    ipUdpEchoAppl     \- uses the UDP based echo server
    snaRUEcho         \- uses the REQECHO and ECHOTEST RU's
                         to an SSCP over an SNA LU\-SSCP
                         session
    snaLU0EchoAppl    \- uses test RU's sent to the Echo 
                         Server over an SNA LU0\-LU0 session
    snaLU2EchoAppl    \- uses test RU's sent to the Echo 
                         Server over an SNA LU2\-LU2 session
    snaLU62Echo       \- uses the native appn ping ie. aping 
    snaLU62EchoAppl   \- uses test RU's sent to the ARR
                         Echo Server over an SNA LU6.2\-LU6.2
                         session
    appleTalkEcho     \- uses Echo Request/Reply as defined
                         for appleTalk networks
    appleTalkEchoAppl \- uses the appleTalk based echo
                         server
    decNetEcho        \- uses Echo Request/Reply as defined
                         for DECNet networks
    decNetEchoAppl    \- uses the DECnet based echo server
    ipxEcho           \- uses Echo Request/Reply as defined
                         for Novell IPX networks
    ipxEchoAppl       \- uses the Novel IPX based echo
                         server
    isoClnsEcho       \- uses Echo Request/Reply as defined
                         for ISO CLNS networks
    isoClnsEchoAppl   \- uses the ISO CLNS based echo
                         server
    vinesEcho         \- uses Echo Request/Reply as defined
                         for VINES networks
    vinesEchoAppl     \- uses the VINES based echo server
    xnsEcho           \- uses Echo Request/Reply as defined
                         for XNS networks
    xnsEchoAppl       \- uses the XNS based echo server
    apolloEcho        \- uses Echo Request/Reply as defined
                         for APOLLO networks
    apolloEchoAppl    \- uses the APOLLO based echo
                         server
    netbiosEchoAppl   \- uses the netbios based echo
                         server
    ipTcpConn         \- uses the tcp's connect mechanism
    httpAppl          \- uses udp for name resolution, 
                        tcp connect and tcp data transfer
                        mechanisms for HTTP data download
                        from a particular HTTP Server
    dnsAppl           \- uses udp for name resolution
    jitterAppl        \- uses udp for packet transfers
    dlswAppl          \- uses tcp for sending keepalives
    dhcpAppl          \- uses udp for sending dhcp requests
    ftpAppl           \- uses tcp for connect & data transfer
    mplsLspPingAppl   \- uses MPLS Echo Request/Response as per
                        draft\-ietf\-mpls\-lsp\-ping\-04 ietf
                        standard
    voipAppl          \- uses Symphony infrastructure to measure
                        H.323/SIP call set up time
    rtpAppl           \- uses Symphony infrastructure to measure
                        rtp packets delay variance.
    icmpJitterAppl    \- uses ICMP Timestamp for packet transfer 
                        to measure jitter.
    ethernetPingAppl    \- uses regular 802.1ag loopback frame
    ethernetJitterAppl  \- uses CFM frames .
    videoAppl           \- uses synthetic traffic depending on video 
                                     profile
    y1731dmm            \- used to measure Y1731 delay
    y17311dm            \- used to measure Y1731 1DM
    y1731lmm            \- used to measure Y1731 Loss measurement
    y1731slm            \- used to measure Y1731 Synthetic Loss measurement
    mcastJitterAppl     \- uses udp jitter to measure multicast network
                          performance

    """

    NOTAPPLICABLE = 1

    IPICMPECHO = 2

    IPUDPECHOAPPL = 3

    SNARUECHO = 4

    SNALU0ECHOAPPL = 5

    SNALU2ECHOAPPL = 6

    SNALU62ECHO = 7

    SNALU62ECHOAPPL = 8

    APPLETALKECHO = 9

    APPLETALKECHOAPPL = 10

    DECNETECHO = 11

    DECNETECHOAPPL = 12

    IPXECHO = 13

    IPXECHOAPPL = 14

    ISOCLNSECHO = 15

    ISOCLNSECHOAPPL = 16

    VINESECHO = 17

    VINESECHOAPPL = 18

    XNSECHO = 19

    XNSECHOAPPL = 20

    APOLLOECHO = 21

    APOLLOECHOAPPL = 22

    NETBIOSECHOAPPL = 23

    IPTCPCONN = 24

    HTTPAPPL = 25

    DNSAPPL = 26

    JITTERAPPL = 27

    DLSWAPPL = 28

    DHCPAPPL = 29

    FTPAPPL = 30

    MPLSLSPPINGAPPL = 31

    VOIPAPPL = 32

    RTPAPPL = 33

    ICMPJITTERAPPL = 34

    ETHERNETPINGAPPL = 35

    ETHERNETJITTERAPPL = 36

    VIDEOAPPL = 37

    Y1731DMM = 38

    Y17311DM = 39

    Y1731LMM = 40

    MCASTJITTERAPPL = 41

    Y1731SLM = 42


    @staticmethod
    def _meta_info():
        from ydk.models.rttmon._meta import _CISCO_RTTMON_TC_MIB as meta
        return meta._meta_table['RttMonProtocol_Enum']


class RttMonReactVar_Enum(Enum):
    """
    RttMonReactVar_Enum

    The following are specific Reaction variables for a
    particular probe type\:
     rtt(1)            \- Round Trip Time
     jitterSDAvg(2)    \- Jitter average from source to Destination
     jitterDSAvg(3)    \- Jitter average from destination to source
     packetLossSD(4)   \- Packet loss from source to destination
     packetLossDS(5)   \- Packet loss from destination to source
     mos(6)            \- Mean Opinion Score
     timeout(7)        \- Timeout of the Operation
     connectionLoss(8) \- Connection Failed to the destination
     verifyError(9)    \- Data corruption occurs
     jitterAvg(10)     \- Jitter Average in both the directions
     icpif(11)         \- Calculated Planning Impairment Factor
     packetMIA(12)     \- Missing In Action
     packetLateArrival(13)   \- Packets arriving Late
     packetOutOfSequence(14) \- Packets arriving out of sequence
     maxOfPositiveSD(15)     \- Maximum positive jitter from
                               Source to Destination
     maxOfNegativeSD(16)     \- Maximum negative jitter from
                               Source to Destination
     maxOfPositiveDS(17)     \- Maximum positive jitter from
                               Destination to Source
     maxOfNegativeDS(18)     \- Maximum negative jitter from
                               Destination to Source.
     iaJitterDS(19)          \- Inter arrival jitter from
                               Destination to Source
     frameLossDS(20)         \- Number of frame loss recorded
                               at source DSP
     mosLQDS(21)             \- Listener quality MOS at Source
     mosCQDS(22)             \- Conversational quality MOS at source
     rFactorDS(23)           \- R\-Factor value at Destination.
     successivePacketLoss(24)\- Successive Dropped Packet
     maxOfLatencyDS(25)      \- Maximum Latency from Destination 
                               to Source
     maxOfLatencySD(26)      \- Maximum Latency from Source 
                               to Destination
     latencyDSAvg(27)        \- Latency average from Destination 
                               to Source
     latencySDAvg(28)        \- Latency average from Source 
                               to Destination
     packetLoss(29)          \- Packets loss in both directions
     iaJitterSD(30)          \- Inter arrival jitter from
                               Source to Destination
     mosCQSD(31)             \- Conversational quality MOS at 
                               Destination
     rFactorSD(32)           \- R\-Factor value at Destination.

    """

    RTT = 1

    JITTERSDAVG = 2

    JITTERDSAVG = 3

    PACKETLOSSSD = 4

    PACKETLOSSDS = 5

    MOS = 6

    TIMEOUT = 7

    CONNECTIONLOSS = 8

    VERIFYERROR = 9

    JITTERAVG = 10

    ICPIF = 11

    PACKETMIA = 12

    PACKETLATEARRIVAL = 13

    PACKETOUTOFSEQUENCE = 14

    MAXOFPOSITIVESD = 15

    MAXOFNEGATIVESD = 16

    MAXOFPOSITIVEDS = 17

    MAXOFNEGATIVEDS = 18

    IAJITTERDS = 19

    FRAMELOSSDS = 20

    MOSLQDS = 21

    MOSCQDS = 22

    RFACTORDS = 23

    SUCCESSIVEPACKETLOSS = 24

    MAXOFLATENCYDS = 25

    MAXOFLATENCYSD = 26

    LATENCYDSAVG = 27

    LATENCYSDAVG = 28

    PACKETLOSS = 29

    IAJITTERSD = 30

    MOSCQSD = 31

    RFACTORSD = 32


    @staticmethod
    def _meta_info():
        from ydk.models.rttmon._meta import _CISCO_RTTMON_TC_MIB as meta
        return meta._meta_table['RttMonReactVar_Enum']


class RttMonRttType_Enum(Enum):
    """
    RttMonRttType_Enum

    Specifies the type of RTT operation to be performed.
    
    The value 'echo' will cause the RTT application to
    perform a timed echo request/response operation directed
    at the 'RttMonTargetAddress'.
    
    The value 'pathEcho' will cause the RTT application
    to perform path discovery to the 'RttMonTargetAddress', 
    then it will perform a timed echo request/response 
    operation directed at the each hop along the path.  
    This operation will provide two types of information, 
    first the path and second the time delay along the path.
    
    NOTE\:  The 'pathEcho' time delay operation is a heuristic
           measurement because an intermediate hop may forward
           the different echo request/response at different
           rates.  Thus the time delay difference between two
           hops along a path may contain very little 'true'
           statistical meaning. 
    
    The value 'fileIO' will cause the RTT application to 
    write, read, or write/read a file to a preconfigured 
    file server.
    
    The value 'script' will cause the RTT application to
    execute a preconfigured script.
    
    The value 'udpEcho' will cause the RTT application
    to perform a timed udp packet send/receive operation 
    directed at the 'RttMonTargetAddress'.
    
    The value 'tcpConnect' will cause the RTT application
    to perform a timed tcp connect operation directed at the 
    'RttMonTargetAddress'.
    
    The value 'http' will cause the RTT application
    to perform a download of the object specified in the URL.
    
    The value 'dns' will cause the RTT application
    to perform a name lookup of an IP Address or a hostname.
    
    The value 'jitter' will cause the RTT application
    to perform delay variance analysis.
    
    The value 'dlsw' will cause the RTT application
    to perform a keepalive operation to measure the response 
    time of a DLSw peer.
    
    The value 'dhcp' will cause the RTT application
    to perform an IP Address lease request/teardown operation.
    
    The value 'voip' will cause the RTT application
    to perform call set up operation to measure the response.
    
    The value 'rtp' will cause the RTT application to perform
    delay variance analysis for RTP packet.
    
    The value 'lspGroup' will cause the RTT application to logically
    group Label Switched Paths discovered as part of LSP Path
    Discovery to the target and perform an RTT operation end to end
    over each path in the Group. The type of operation configured
    is determined by rttMplsVpnMonCtrlRttType.
    
    The value 'icmpjitter' will cause the RTT application
    to perform delay variance analysis using ICMP timestamp packets.
    
    The value of 'lspPingIpv4' will cause the RTT application to
    perform ping over LSP path.
    
    The value of 'lspTraceIpv4' will cause the RTT application to
    perform trace over LSP path.
    
    The value of 'ethernetPing' will cause the RTT application to
    perform delay variance analysis using regular 802.1ag loopback
    frame.
    
    The value of 'ethernetJitter' will cause the RTT application to
    perform delay variance analysis using CFM frame.
    
    The value of 'lspPingPseudowire' will cause the RTT application
    to
    perform LSP Ping over Pseudowire and measure response time.
    
    The value 'video' will cause the the RTT application to perform
    a video stream analysis directed at the 'RttMonTargetAddress
    The value 'y1731Delay' will cause the RTT application to perform a ITU\-T standard Y.1731 delay variance analysis
    The value 'y1731Loss' will cause the RTT application to perform a ITU\-T standard Y.1731 loss measure analysis
    The value 'mcastJitter' will cause the RTT application to perform 
    udp jitter stream analysis on a multicast network.

    """

    ECHO = 1

    PATHECHO = 2

    FILEIO = 3

    SCRIPT = 4

    UDPECHO = 5

    TCPCONNECT = 6

    HTTP = 7

    DNS = 8

    JITTER = 9

    DLSW = 10

    DHCP = 11

    FTP = 12

    VOIP = 13

    RTP = 14

    LSPGROUP = 15

    ICMPJITTER = 16

    LSPPING = 17

    LSPTRACE = 18

    ETHERNETPING = 19

    ETHERNETJITTER = 20

    LSPPINGPSEUDOWIRE = 21

    VIDEO = 22

    Y1731DELAY = 23

    Y1731LOSS = 24

    MCASTJITTER = 25


    @staticmethod
    def _meta_info():
        from ydk.models.rttmon._meta import _CISCO_RTTMON_TC_MIB as meta
        return meta._meta_table['RttMonRttType_Enum']


class RttMplsVpnMonLpdFailureSense_Enum(Enum):
    """
    RttMplsVpnMonLpdFailureSense_Enum

    These are the defined values for the causes of failure in
    LSP Path Discovery.
    
    unknown(1)                      \- The cause of failure for the
                                      LSP Path Discovery cannot be
                                      determined. The discovery for
                                      the target PE may not have 
                                      started.
    noPath(2)                       \- No paths were found to the
                                      target FEC while doing the
                                      LSP Path Discovery.
    allPathsBroken(3)               \- All paths to the target FEC
                                      are broken. This means an
                                      untagged interface on the LSP
                                      to the target.
    allPathsUnexplorable(4)         \- All paths to the target FEC are
                                      unexplorable. This identifies
                                      a case where there is some
                                      problem in reaching the next
                                      hop while doing Discovery.
    allPathsBrokenOrUnexplorable(5) \- All paths to the target FEC are
                                      are either broken or
                                      unexplorable.
    timeout(6)                      \- The LSP Path Discovery could
                                      not be completed for the
                                      target FEC within the
                                      configured time.
    error(7)                        \- Error occurred while
                                      performing LSP Path Discovery.
                                      It might be also due to some
                                      reasons unrelated to LSP Path
                                      Discovery.

    """

    UNKNOWN = 1

    NOPATH = 2

    ALLPATHSBROKEN = 3

    ALLPATHSUNEXPLORABLE = 4

    ALLPATHSBROKENORUNEXPLORABLE = 5

    TIMEOUT = 6

    ERROR = 7


    @staticmethod
    def _meta_info():
        from ydk.models.rttmon._meta import _CISCO_RTTMON_TC_MIB as meta
        return meta._meta_table['RttMplsVpnMonLpdFailureSense_Enum']


class RttMplsVpnMonLpdGrpStatus_Enum(Enum):
    """
    RttMplsVpnMonLpdGrpStatus_Enum

    These are the defined values for the status of the LPD Group.
    
    unknown(1) \- This indicates that some/all of the probes which are
                 part of the LPD group have not completed even
                 a single operation, so the group status cannot be
                 identified.
         up(2) \- This state indicates that all the probes which are
                 part of the LPD group are up with latest return
                 code as 'ok'.
    partial(3) \- This state indicates that some probes are up and
                 running fine and some are not 'ok'.
       down(4) \- This state indicates that all the probes to the
                 target are not running fine. This state indicates
                 that there is connectivity problem to the target
                 PE.

    """

    UNKNOWN = 1

    UP = 2

    PARTIAL = 3

    DOWN = 4


    @staticmethod
    def _meta_info():
        from ydk.models.rttmon._meta import _CISCO_RTTMON_TC_MIB as meta
        return meta._meta_table['RttMplsVpnMonLpdGrpStatus_Enum']


class RttMplsVpnMonRttType_Enum(Enum):
    """
    RttMplsVpnMonRttType_Enum

    Specifies the type of RTT operation to be performed for
    Auto SAA L3 MPLS VPN.
    
    The value 'jitter' will cause the Auto SAA L3 MPLS VPN to
    automatically configure jitter operations.
    
    The value 'echo' will cause the Auto SAA L3 MPLS VPN to
    automatically configure jitter operations.
    
    The value 'pathEcho' will cause the Auto SAA L3 MPLS VPN to
    automatically configure jitter operations.

    """

    JITTER = 1

    ECHO = 2

    PATHECHO = 3


    @staticmethod
    def _meta_info():
        from ydk.models.rttmon._meta import _CISCO_RTTMON_TC_MIB as meta
        return meta._meta_table['RttMplsVpnMonRttType_Enum']


class RttReset_Enum(Enum):
    """
    RttReset_Enum

    When the value set to 'reset', the entire RTT application
    goes through a reset sequence, making a best
    effort to revert to its startup condition. At other times,
    the value is 'ready'.

    """

    READY = 1

    RESET = 2


    @staticmethod
    def _meta_info():
        from ydk.models.rttmon._meta import _CISCO_RTTMON_TC_MIB as meta
        return meta._meta_table['RttReset_Enum']


class RttResponseSense_Enum(Enum):
    """
    RttResponseSense_Enum

    These are the defined values for a completion status
    of a RTT operation.  
    
    other(0)         \- the operation is not started or completed
                        or this object is not applicable for
                        the probe type.  
    ok(1)            \- a valid completion occurred and
                        timed successfully
    disconnected(2)  \- the operation did not occur because
                        the connection to the target
                        was lost
    overThreshold(3) \- a valid completion was received but
                        the completion time exceeded a
                        threshold value
    timeout(4)       \- an operation timed out; no completion
                        time recorded
    busy(5)          \- the operation did not occur because a
                        previous operation is still
                        outstanding
    notConnected(6)  \- the operation did not occur because no
                        connection (session) exists with the
                        target
    dropped(7)       \- the operation did not occur due to lack
                        of internal resource
    sequenceError(8) \- a completed operation did not contain 
                        the correct sequence id; no completion
                        time recorded
    verifyError(9)   \- a completed operation was received, but
                        the data it contained did not match
                        the expected data; no completion time 
                        recorded
    applicationSpecific(10) 
                     \- the application generating the operation
                        had a specific error
    dnsServerTimeout(11) 
                     \- DNS Server Timeout
    tcpConnectTimeout(12)
                     \- TCP Connect Timeout
    httpTransactionTimeout(13)
                     \- HTTP Transaction Timeout
    dnsQueryError(14)
                     \- DNS Query error (because of unknown address 
                       etc.,)
    httpError(15)
                     \- HTTP Response StatusCode is not OK (200),
                       or permenent redirect(301), temporary redirect
                       (302) then HTTP error is set.
    error(16)
                     \- if there are socket failures or some other 
                       errors not relavant to the actual probe, they 
                       are recorded under this error
    mplsLspEchoTxError(17)
                     \- MPLS echo request transmission failure.
    mplsLspUnreachable(18)
                     \- MPLS Target FEC not reachable or unsupported
                       mpls echo reply code.
    mplsLspMalformedReq(19)
                     \- MPLS echo request was malformalformed, pointed
                       out by the reply router.
    mplsLspReachButNotFEC(20)
                     \- MPLS echo request processed by the downstream
                       router but not the target.
    enableOk(21) 
                     \- Control enable request OK
    enableNoConnect(22)
                     \- Control enable request fail due to no connection to
                       the target.
    enableVersionFail(23)
                     \- Control enable request version fail.
    enableInternalError(24)
                     \- Control enable request internal error.
    enableAbort(25)
                     \- Control enable request abort.
    enableFail(26)
                     \- Control enable request fail.
    enableAuthFail(27)
                     \- Control enable request fail due to authentication
                       fail.
    enableFormatError(28)
                     \- Control enable request fail due to format error.
    enablePortInUse(29)
                     \- Control enable request fail due to port in use.
    statsRetrieveOk(30)
                     \- Stats retrieve request OK
    statsRetrieveNoConnect(31)
                     \- Stats retrieve request fail due to no connection 
                       to the target.
    statsRetrieveVersionFail(32)
                     \- Stats retrieve request version fail.
    statsRetrieveInternalError(33)
                     \- Stats retrieve request internal error.
    statsRetrieveAbort(34)
                     \- Stats retrieve request abort.
    statsRetrieveFail(35)
                     \- Stats retrieve request fail.
    statsRetrieveAuthFail(36)
                     \- Stats retrieve request fail due to authentication fail.
    statsRetrieveFormatError(37)
                     \- Stats retrieve request fail due to format error.
    statsRetrievePortInUse(38)
                     \- Stats retrieve request fail due to port in use.

    """

    OTHER = 0

    OK = 1

    DISCONNECTED = 2

    OVERTHRESHOLD = 3

    TIMEOUT = 4

    BUSY = 5

    NOTCONNECTED = 6

    DROPPED = 7

    SEQUENCEERROR = 8

    VERIFYERROR = 9

    APPLICATIONSPECIFIC = 10

    DNSSERVERTIMEOUT = 11

    TCPCONNECTTIMEOUT = 12

    HTTPTRANSACTIONTIMEOUT = 13

    DNSQUERYERROR = 14

    HTTPERROR = 15

    ERROR = 16

    MPLSLSPECHOTXERROR = 17

    MPLSLSPUNREACHABLE = 18

    MPLSLSPMALFORMEDREQ = 19

    MPLSLSPREACHBUTNOTFEC = 20

    ENABLEOK = 21

    ENABLENOCONNECT = 22

    ENABLEVERSIONFAIL = 23

    ENABLEINTERNALERROR = 24

    ENABLEABORT = 25

    ENABLEFAIL = 26

    ENABLEAUTHFAIL = 27

    ENABLEFORMATERROR = 28

    ENABLEPORTINUSE = 29

    STATSRETRIEVEOK = 30

    STATSRETRIEVENOCONNECT = 31

    STATSRETRIEVEVERSIONFAIL = 32

    STATSRETRIEVEINTERNALERROR = 33

    STATSRETRIEVEABORT = 34

    STATSRETRIEVEFAIL = 35

    STATSRETRIEVEAUTHFAIL = 36

    STATSRETRIEVEFORMATERROR = 37

    STATSRETRIEVEPORTINUSE = 38


    @staticmethod
    def _meta_info():
        from ydk.models.rttmon._meta import _CISCO_RTTMON_TC_MIB as meta
        return meta._meta_table['RttResponseSense_Enum']




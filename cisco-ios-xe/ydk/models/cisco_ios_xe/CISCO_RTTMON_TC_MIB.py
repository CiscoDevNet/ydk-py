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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Rttmoncodectype(Enum):
    """
    Rttmoncodectype

    Specifies the codec type to be used with the jitter probe.

    The following codec types are defined\:

    notApplicable     \- no CodecType is defined

    g711ulaw          \- uses G.711 U Law 64000 bps

    g711alaw          \- uses G.711 A Law 64000 bps

    g729a             \- uses G.729 8000 bps

    .. data:: notApplicable = 0

    .. data:: g711ulaw = 1

    .. data:: g711alaw = 2

    .. data:: g729a = 3

    """

    notApplicable = Enum.YLeaf(0, "notApplicable")

    g711ulaw = Enum.YLeaf(1, "g711ulaw")

    g711alaw = Enum.YLeaf(2, "g711alaw")

    g729a = Enum.YLeaf(3, "g729a")


class Rttmonlsppingreplymode(Enum):
    """
    Rttmonlsppingreplymode

    Specifies the Reply mode for the MPLS LSP Echo request

    packets. The following reply modes are supported\:

    replyIpv4Udp(1)         \- an mpls echo request will normally

                             have reply via IPv4 UDP packets.

    replyIpv4UdpRA(2)       \- reply via IPv4 UDP Router Alert. Used

                             when IPv4 return path is deemed 

                             unreliable.

    .. data:: replyIpv4Udp = 1

    .. data:: replyIpv4UdpRA = 2

    """

    replyIpv4Udp = Enum.YLeaf(1, "replyIpv4Udp")

    replyIpv4UdpRA = Enum.YLeaf(2, "replyIpv4UdpRA")


class Rttmonoperation(Enum):
    """
    Rttmonoperation

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

    .. data:: notApplicable = 0

    .. data:: httpGet = 1

    .. data:: httpRaw = 2

    .. data:: ftpGet = 3

    .. data:: ftpPassive = 4

    .. data:: ftpActive = 5

    .. data:: voipDTAlertRinging = 6

    .. data:: voipDTConnectOK = 7

    """

    notApplicable = Enum.YLeaf(0, "notApplicable")

    httpGet = Enum.YLeaf(1, "httpGet")

    httpRaw = Enum.YLeaf(2, "httpRaw")

    ftpGet = Enum.YLeaf(3, "ftpGet")

    ftpPassive = Enum.YLeaf(4, "ftpPassive")

    ftpActive = Enum.YLeaf(5, "ftpActive")

    voipDTAlertRinging = Enum.YLeaf(6, "voipDTAlertRinging")

    voipDTConnectOK = Enum.YLeaf(7, "voipDTConnectOK")


class Rttmonprotocol(Enum):
    """
    Rttmonprotocol

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

    .. data:: none = 0

    .. data:: notApplicable = 1

    .. data:: ipIcmpEcho = 2

    .. data:: ipUdpEchoAppl = 3

    .. data:: snaRUEcho = 4

    .. data:: snaLU0EchoAppl = 5

    .. data:: snaLU2EchoAppl = 6

    .. data:: snaLU62Echo = 7

    .. data:: snaLU62EchoAppl = 8

    .. data:: appleTalkEcho = 9

    .. data:: appleTalkEchoAppl = 10

    .. data:: decNetEcho = 11

    .. data:: decNetEchoAppl = 12

    .. data:: ipxEcho = 13

    .. data:: ipxEchoAppl = 14

    .. data:: isoClnsEcho = 15

    .. data:: isoClnsEchoAppl = 16

    .. data:: vinesEcho = 17

    .. data:: vinesEchoAppl = 18

    .. data:: xnsEcho = 19

    .. data:: xnsEchoAppl = 20

    .. data:: apolloEcho = 21

    .. data:: apolloEchoAppl = 22

    .. data:: netbiosEchoAppl = 23

    .. data:: ipTcpConn = 24

    .. data:: httpAppl = 25

    .. data:: dnsAppl = 26

    .. data:: jitterAppl = 27

    .. data:: dlswAppl = 28

    .. data:: dhcpAppl = 29

    .. data:: ftpAppl = 30

    .. data:: mplsLspPingAppl = 31

    .. data:: voipAppl = 32

    .. data:: rtpAppl = 33

    .. data:: icmpJitterAppl = 34

    .. data:: ethernetPingAppl = 35

    .. data:: ethernetJitterAppl = 36

    .. data:: videoAppl = 37

    .. data:: y1731dmm = 38

    .. data:: y17311dm = 39

    .. data:: y1731lmm = 40

    .. data:: mcastJitterAppl = 41

    .. data:: y1731slm = 42

    .. data:: y1731dmmv1 = 43

    """

    none = Enum.YLeaf(0, "none")

    notApplicable = Enum.YLeaf(1, "notApplicable")

    ipIcmpEcho = Enum.YLeaf(2, "ipIcmpEcho")

    ipUdpEchoAppl = Enum.YLeaf(3, "ipUdpEchoAppl")

    snaRUEcho = Enum.YLeaf(4, "snaRUEcho")

    snaLU0EchoAppl = Enum.YLeaf(5, "snaLU0EchoAppl")

    snaLU2EchoAppl = Enum.YLeaf(6, "snaLU2EchoAppl")

    snaLU62Echo = Enum.YLeaf(7, "snaLU62Echo")

    snaLU62EchoAppl = Enum.YLeaf(8, "snaLU62EchoAppl")

    appleTalkEcho = Enum.YLeaf(9, "appleTalkEcho")

    appleTalkEchoAppl = Enum.YLeaf(10, "appleTalkEchoAppl")

    decNetEcho = Enum.YLeaf(11, "decNetEcho")

    decNetEchoAppl = Enum.YLeaf(12, "decNetEchoAppl")

    ipxEcho = Enum.YLeaf(13, "ipxEcho")

    ipxEchoAppl = Enum.YLeaf(14, "ipxEchoAppl")

    isoClnsEcho = Enum.YLeaf(15, "isoClnsEcho")

    isoClnsEchoAppl = Enum.YLeaf(16, "isoClnsEchoAppl")

    vinesEcho = Enum.YLeaf(17, "vinesEcho")

    vinesEchoAppl = Enum.YLeaf(18, "vinesEchoAppl")

    xnsEcho = Enum.YLeaf(19, "xnsEcho")

    xnsEchoAppl = Enum.YLeaf(20, "xnsEchoAppl")

    apolloEcho = Enum.YLeaf(21, "apolloEcho")

    apolloEchoAppl = Enum.YLeaf(22, "apolloEchoAppl")

    netbiosEchoAppl = Enum.YLeaf(23, "netbiosEchoAppl")

    ipTcpConn = Enum.YLeaf(24, "ipTcpConn")

    httpAppl = Enum.YLeaf(25, "httpAppl")

    dnsAppl = Enum.YLeaf(26, "dnsAppl")

    jitterAppl = Enum.YLeaf(27, "jitterAppl")

    dlswAppl = Enum.YLeaf(28, "dlswAppl")

    dhcpAppl = Enum.YLeaf(29, "dhcpAppl")

    ftpAppl = Enum.YLeaf(30, "ftpAppl")

    mplsLspPingAppl = Enum.YLeaf(31, "mplsLspPingAppl")

    voipAppl = Enum.YLeaf(32, "voipAppl")

    rtpAppl = Enum.YLeaf(33, "rtpAppl")

    icmpJitterAppl = Enum.YLeaf(34, "icmpJitterAppl")

    ethernetPingAppl = Enum.YLeaf(35, "ethernetPingAppl")

    ethernetJitterAppl = Enum.YLeaf(36, "ethernetJitterAppl")

    videoAppl = Enum.YLeaf(37, "videoAppl")

    y1731dmm = Enum.YLeaf(38, "y1731dmm")

    y17311dm = Enum.YLeaf(39, "y17311dm")

    y1731lmm = Enum.YLeaf(40, "y1731lmm")

    mcastJitterAppl = Enum.YLeaf(41, "mcastJitterAppl")

    y1731slm = Enum.YLeaf(42, "y1731slm")

    y1731dmmv1 = Enum.YLeaf(43, "y1731dmmv1")


class Rttmonreactvar(Enum):
    """
    Rttmonreactvar

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

    .. data:: rtt = 1

    .. data:: jitterSDAvg = 2

    .. data:: jitterDSAvg = 3

    .. data:: packetLossSD = 4

    .. data:: packetLossDS = 5

    .. data:: mos = 6

    .. data:: timeout = 7

    .. data:: connectionLoss = 8

    .. data:: verifyError = 9

    .. data:: jitterAvg = 10

    .. data:: icpif = 11

    .. data:: packetMIA = 12

    .. data:: packetLateArrival = 13

    .. data:: packetOutOfSequence = 14

    .. data:: maxOfPositiveSD = 15

    .. data:: maxOfNegativeSD = 16

    .. data:: maxOfPositiveDS = 17

    .. data:: maxOfNegativeDS = 18

    .. data:: iaJitterDS = 19

    .. data:: frameLossDS = 20

    .. data:: mosLQDS = 21

    .. data:: mosCQDS = 22

    .. data:: rFactorDS = 23

    .. data:: successivePacketLoss = 24

    .. data:: maxOfLatencyDS = 25

    .. data:: maxOfLatencySD = 26

    .. data:: latencyDSAvg = 27

    .. data:: latencySDAvg = 28

    .. data:: packetLoss = 29

    .. data:: iaJitterSD = 30

    .. data:: mosCQSD = 31

    .. data:: rFactorSD = 32

    """

    rtt = Enum.YLeaf(1, "rtt")

    jitterSDAvg = Enum.YLeaf(2, "jitterSDAvg")

    jitterDSAvg = Enum.YLeaf(3, "jitterDSAvg")

    packetLossSD = Enum.YLeaf(4, "packetLossSD")

    packetLossDS = Enum.YLeaf(5, "packetLossDS")

    mos = Enum.YLeaf(6, "mos")

    timeout = Enum.YLeaf(7, "timeout")

    connectionLoss = Enum.YLeaf(8, "connectionLoss")

    verifyError = Enum.YLeaf(9, "verifyError")

    jitterAvg = Enum.YLeaf(10, "jitterAvg")

    icpif = Enum.YLeaf(11, "icpif")

    packetMIA = Enum.YLeaf(12, "packetMIA")

    packetLateArrival = Enum.YLeaf(13, "packetLateArrival")

    packetOutOfSequence = Enum.YLeaf(14, "packetOutOfSequence")

    maxOfPositiveSD = Enum.YLeaf(15, "maxOfPositiveSD")

    maxOfNegativeSD = Enum.YLeaf(16, "maxOfNegativeSD")

    maxOfPositiveDS = Enum.YLeaf(17, "maxOfPositiveDS")

    maxOfNegativeDS = Enum.YLeaf(18, "maxOfNegativeDS")

    iaJitterDS = Enum.YLeaf(19, "iaJitterDS")

    frameLossDS = Enum.YLeaf(20, "frameLossDS")

    mosLQDS = Enum.YLeaf(21, "mosLQDS")

    mosCQDS = Enum.YLeaf(22, "mosCQDS")

    rFactorDS = Enum.YLeaf(23, "rFactorDS")

    successivePacketLoss = Enum.YLeaf(24, "successivePacketLoss")

    maxOfLatencyDS = Enum.YLeaf(25, "maxOfLatencyDS")

    maxOfLatencySD = Enum.YLeaf(26, "maxOfLatencySD")

    latencyDSAvg = Enum.YLeaf(27, "latencyDSAvg")

    latencySDAvg = Enum.YLeaf(28, "latencySDAvg")

    packetLoss = Enum.YLeaf(29, "packetLoss")

    iaJitterSD = Enum.YLeaf(30, "iaJitterSD")

    mosCQSD = Enum.YLeaf(31, "mosCQSD")

    rFactorSD = Enum.YLeaf(32, "rFactorSD")


class Rttmonrtttype(Enum):
    """
    Rttmonrtttype

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

    .. data:: none = 0

    .. data:: echo = 1

    .. data:: pathEcho = 2

    .. data:: fileIO = 3

    .. data:: script = 4

    .. data:: udpEcho = 5

    .. data:: tcpConnect = 6

    .. data:: http = 7

    .. data:: dns = 8

    .. data:: jitter = 9

    .. data:: dlsw = 10

    .. data:: dhcp = 11

    .. data:: ftp = 12

    .. data:: voip = 13

    .. data:: rtp = 14

    .. data:: lspGroup = 15

    .. data:: icmpjitter = 16

    .. data:: lspPing = 17

    .. data:: lspTrace = 18

    .. data:: ethernetPing = 19

    .. data:: ethernetJitter = 20

    .. data:: lspPingPseudowire = 21

    .. data:: video = 22

    .. data:: y1731Delay = 23

    .. data:: y1731Loss = 24

    .. data:: mcastJitter = 25

    """

    none = Enum.YLeaf(0, "none")

    echo = Enum.YLeaf(1, "echo")

    pathEcho = Enum.YLeaf(2, "pathEcho")

    fileIO = Enum.YLeaf(3, "fileIO")

    script = Enum.YLeaf(4, "script")

    udpEcho = Enum.YLeaf(5, "udpEcho")

    tcpConnect = Enum.YLeaf(6, "tcpConnect")

    http = Enum.YLeaf(7, "http")

    dns = Enum.YLeaf(8, "dns")

    jitter = Enum.YLeaf(9, "jitter")

    dlsw = Enum.YLeaf(10, "dlsw")

    dhcp = Enum.YLeaf(11, "dhcp")

    ftp = Enum.YLeaf(12, "ftp")

    voip = Enum.YLeaf(13, "voip")

    rtp = Enum.YLeaf(14, "rtp")

    lspGroup = Enum.YLeaf(15, "lspGroup")

    icmpjitter = Enum.YLeaf(16, "icmpjitter")

    lspPing = Enum.YLeaf(17, "lspPing")

    lspTrace = Enum.YLeaf(18, "lspTrace")

    ethernetPing = Enum.YLeaf(19, "ethernetPing")

    ethernetJitter = Enum.YLeaf(20, "ethernetJitter")

    lspPingPseudowire = Enum.YLeaf(21, "lspPingPseudowire")

    video = Enum.YLeaf(22, "video")

    y1731Delay = Enum.YLeaf(23, "y1731Delay")

    y1731Loss = Enum.YLeaf(24, "y1731Loss")

    mcastJitter = Enum.YLeaf(25, "mcastJitter")


class Rttmplsvpnmonlpdfailuresense(Enum):
    """
    Rttmplsvpnmonlpdfailuresense

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

    .. data:: unknown = 1

    .. data:: noPath = 2

    .. data:: allPathsBroken = 3

    .. data:: allPathsUnexplorable = 4

    .. data:: allPathsBrokenOrUnexplorable = 5

    .. data:: timeout = 6

    .. data:: error = 7

    """

    unknown = Enum.YLeaf(1, "unknown")

    noPath = Enum.YLeaf(2, "noPath")

    allPathsBroken = Enum.YLeaf(3, "allPathsBroken")

    allPathsUnexplorable = Enum.YLeaf(4, "allPathsUnexplorable")

    allPathsBrokenOrUnexplorable = Enum.YLeaf(5, "allPathsBrokenOrUnexplorable")

    timeout = Enum.YLeaf(6, "timeout")

    error = Enum.YLeaf(7, "error")


class Rttmplsvpnmonlpdgrpstatus(Enum):
    """
    Rttmplsvpnmonlpdgrpstatus

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

    .. data:: unknown = 1

    .. data:: up = 2

    .. data:: partial = 3

    .. data:: down = 4

    """

    unknown = Enum.YLeaf(1, "unknown")

    up = Enum.YLeaf(2, "up")

    partial = Enum.YLeaf(3, "partial")

    down = Enum.YLeaf(4, "down")


class Rttmplsvpnmonrtttype(Enum):
    """
    Rttmplsvpnmonrtttype

    Specifies the type of RTT operation to be performed for

    Auto SAA L3 MPLS VPN.

    The value 'jitter' will cause the Auto SAA L3 MPLS VPN to

    automatically configure jitter operations.

    The value 'echo' will cause the Auto SAA L3 MPLS VPN to

    automatically configure jitter operations.

    The value 'pathEcho' will cause the Auto SAA L3 MPLS VPN to

    automatically configure jitter operations.

    .. data:: jitter = 1

    .. data:: echo = 2

    .. data:: pathEcho = 3

    """

    jitter = Enum.YLeaf(1, "jitter")

    echo = Enum.YLeaf(2, "echo")

    pathEcho = Enum.YLeaf(3, "pathEcho")


class Rttreset(Enum):
    """
    Rttreset

    When the value set to 'reset', the entire RTT application

    goes through a reset sequence, making a best

    effort to revert to its startup condition. At other times,

    the value is 'ready'.

    .. data:: ready = 1

    .. data:: reset = 2

    """

    ready = Enum.YLeaf(1, "ready")

    reset = Enum.YLeaf(2, "reset")


class Rttresponsesense(Enum):
    """
    Rttresponsesense

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

    .. data:: other = 0

    .. data:: ok = 1

    .. data:: disconnected = 2

    .. data:: overThreshold = 3

    .. data:: timeout = 4

    .. data:: busy = 5

    .. data:: notConnected = 6

    .. data:: dropped = 7

    .. data:: sequenceError = 8

    .. data:: verifyError = 9

    .. data:: applicationSpecific = 10

    .. data:: dnsServerTimeout = 11

    .. data:: tcpConnectTimeout = 12

    .. data:: httpTransactionTimeout = 13

    .. data:: dnsQueryError = 14

    .. data:: httpError = 15

    .. data:: error = 16

    .. data:: mplsLspEchoTxError = 17

    .. data:: mplsLspUnreachable = 18

    .. data:: mplsLspMalformedReq = 19

    .. data:: mplsLspReachButNotFEC = 20

    .. data:: enableOk = 21

    .. data:: enableNoConnect = 22

    .. data:: enableVersionFail = 23

    .. data:: enableInternalError = 24

    .. data:: enableAbort = 25

    .. data:: enableFail = 26

    .. data:: enableAuthFail = 27

    .. data:: enableFormatError = 28

    .. data:: enablePortInUse = 29

    .. data:: statsRetrieveOk = 30

    .. data:: statsRetrieveNoConnect = 31

    .. data:: statsRetrieveVersionFail = 32

    .. data:: statsRetrieveInternalError = 33

    .. data:: statsRetrieveAbort = 34

    .. data:: statsRetrieveFail = 35

    .. data:: statsRetrieveAuthFail = 36

    .. data:: statsRetrieveFormatError = 37

    .. data:: statsRetrievePortInUse = 38

    """

    other = Enum.YLeaf(0, "other")

    ok = Enum.YLeaf(1, "ok")

    disconnected = Enum.YLeaf(2, "disconnected")

    overThreshold = Enum.YLeaf(3, "overThreshold")

    timeout = Enum.YLeaf(4, "timeout")

    busy = Enum.YLeaf(5, "busy")

    notConnected = Enum.YLeaf(6, "notConnected")

    dropped = Enum.YLeaf(7, "dropped")

    sequenceError = Enum.YLeaf(8, "sequenceError")

    verifyError = Enum.YLeaf(9, "verifyError")

    applicationSpecific = Enum.YLeaf(10, "applicationSpecific")

    dnsServerTimeout = Enum.YLeaf(11, "dnsServerTimeout")

    tcpConnectTimeout = Enum.YLeaf(12, "tcpConnectTimeout")

    httpTransactionTimeout = Enum.YLeaf(13, "httpTransactionTimeout")

    dnsQueryError = Enum.YLeaf(14, "dnsQueryError")

    httpError = Enum.YLeaf(15, "httpError")

    error = Enum.YLeaf(16, "error")

    mplsLspEchoTxError = Enum.YLeaf(17, "mplsLspEchoTxError")

    mplsLspUnreachable = Enum.YLeaf(18, "mplsLspUnreachable")

    mplsLspMalformedReq = Enum.YLeaf(19, "mplsLspMalformedReq")

    mplsLspReachButNotFEC = Enum.YLeaf(20, "mplsLspReachButNotFEC")

    enableOk = Enum.YLeaf(21, "enableOk")

    enableNoConnect = Enum.YLeaf(22, "enableNoConnect")

    enableVersionFail = Enum.YLeaf(23, "enableVersionFail")

    enableInternalError = Enum.YLeaf(24, "enableInternalError")

    enableAbort = Enum.YLeaf(25, "enableAbort")

    enableFail = Enum.YLeaf(26, "enableFail")

    enableAuthFail = Enum.YLeaf(27, "enableAuthFail")

    enableFormatError = Enum.YLeaf(28, "enableFormatError")

    enablePortInUse = Enum.YLeaf(29, "enablePortInUse")

    statsRetrieveOk = Enum.YLeaf(30, "statsRetrieveOk")

    statsRetrieveNoConnect = Enum.YLeaf(31, "statsRetrieveNoConnect")

    statsRetrieveVersionFail = Enum.YLeaf(32, "statsRetrieveVersionFail")

    statsRetrieveInternalError = Enum.YLeaf(33, "statsRetrieveInternalError")

    statsRetrieveAbort = Enum.YLeaf(34, "statsRetrieveAbort")

    statsRetrieveFail = Enum.YLeaf(35, "statsRetrieveFail")

    statsRetrieveAuthFail = Enum.YLeaf(36, "statsRetrieveAuthFail")

    statsRetrieveFormatError = Enum.YLeaf(37, "statsRetrieveFormatError")

    statsRetrievePortInUse = Enum.YLeaf(38, "statsRetrievePortInUse")




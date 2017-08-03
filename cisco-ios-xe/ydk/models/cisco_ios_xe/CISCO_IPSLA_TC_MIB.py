""" CISCO_IPSLA_TC_MIB 

This MIB contains textual conventions used by
CISCO IPSLA MIBs.

Acronyms\:
 FEC\: Forward Equivalence Class
 LPD\: Label Path Discovery
 LSP\: Label Switched Path
 MPLS\: Multi Protocol Label Switching
 RTT\: Round Trip Time
 SAA\: Service Assurance Agent
 SLA\: Service Level Agreement
 VPN\: Virtual Private Network
 ICPIF\: Calculated Planning Impairment Factor

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ipslacodectype(Enum):
    """
    Ipslacodectype

    Specifies the IP SLA codec type to be used with the UDP 

    jitter operation. The following codec types are defined\:

    notApplicable(0)     \- no CodecType is defined

    g711ulaw(1)          \- uses G.711 U Law 64000 bps

    g711alaw(2)          \- uses G.711 A Law 64000 bps

    g729a(3)             \- uses G.729 8000 bps

    .. data:: notApplicable = 0

    .. data:: g711ulaw = 1

    .. data:: g711alaw = 2

    .. data:: g729a = 3

    """

    notApplicable = Enum.YLeaf(0, "notApplicable")

    g711ulaw = Enum.YLeaf(1, "g711ulaw")

    g711alaw = Enum.YLeaf(2, "g711alaw")

    g729a = Enum.YLeaf(3, "g729a")


class Ipslaopertype(Enum):
    """
    Ipslaopertype

    Specifies the type of IP SLA operation to be performed.

    icmpEcho(1)   \-  The value 'icmpEcho' will cause the

                     IP SLA application to  perform a timed 

                     ICMP echo request/response operation.

    udpEcho(2)    \-  The value 'udpEcho' will cause the IP SLA 

                     application to perform a timed udp packet 

                     send/receive operation. 

    tcpConnect(3) \-  The value 'tcpConnect' will cause the IP 

                     SLA application to perform a timed TCP 

                     connect operation. 

    udpJitter(4)  \-  The value 'udpjitter' will cause the IP

                     SLA application to perform delay variance

                     analysis using UDP timestamp packets. 

    icmpjitter(5) \-  The value 'icmpjitter' will cause the IP 

                     SLA application to perform delay variance 

                     analysis using ICMP timestamp packets.

    .. data:: icmpEcho = 1

    .. data:: udpEcho = 2

    .. data:: tcpConnect = 3

    .. data:: udpJitter = 4

    .. data:: icmpJitter = 5

    """

    icmpEcho = Enum.YLeaf(1, "icmpEcho")

    udpEcho = Enum.YLeaf(2, "udpEcho")

    tcpConnect = Enum.YLeaf(3, "tcpConnect")

    udpJitter = Enum.YLeaf(4, "udpJitter")

    icmpJitter = Enum.YLeaf(5, "icmpJitter")


class Ipslareactvar(Enum):
    """
    Ipslareactvar

    The following are specific reaction variables for an

    IP SLA operation to react upon\:

     rtt(1)            \- Round Trip Time

     jitterSDAvg(2)    \- Jitter average from source to

                         destination  

     jitterDSAvg(3)    \- Jitter average from destination 

                         to source  

     packetLossSD(4)   \- Packet loss from source to 

                         destination 

     packetLossDS(5)   \- Packet loss from destination 

                         to source 

     mos(6)            \- Mean Opinion Score  

     timeout(7)        \- Timeout of the operation

     connectionLoss(8) \- Connection failed to the destination

     verifyError(9)    \- Data corruption occurs

     jitterAvg(10)     \- Jitter average in both directions

     icpif(11)         \- Calculated Planning Impairment Factor

     packetMIA(12)     \- Missed packets in operation

     packetLateArrival(13)   \- Packets arriving late

     packetOutOfSequence(14) \- Packets arriving out of sequence

     maxOfPositiveSD(15)     \- Maximum positive jitter from

                               source to destination

     maxOfNegativeSD(16)     \- Maximum negative jitter from

                               source to destination

     maxOfPositiveDS(17)     \- Maximum positive jitter from

                               destination to source

     maxOfNegativeDS(18)     \- Maximum negative jitter from

                               destination to source.

     successivePacketLoss(19)\- Successive packet dropped 

     maxOfLatencyDS(20)      \- Maximum Latency from

                               Destination to Source

     maxOfLatencySD(21)      \- Maximum Latency from Source 

                               to Destination

     latencyDSAvg(22)        \- Latency average from Destination 

                               to Source

     latencySDAvg(23)        \- Latency average from Source 

                               to Destination

     packetLoss(24)          \- Packets loss in both directions

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

    .. data:: successivePacketLoss = 19

    .. data:: maxOfLatencyDS = 20

    .. data:: maxOfLatencySD = 21

    .. data:: latencyDSAvg = 22

    .. data:: latencySDAvg = 23

    .. data:: packetLoss = 24

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

    successivePacketLoss = Enum.YLeaf(19, "successivePacketLoss")

    maxOfLatencyDS = Enum.YLeaf(20, "maxOfLatencyDS")

    maxOfLatencySD = Enum.YLeaf(21, "maxOfLatencySD")

    latencyDSAvg = Enum.YLeaf(22, "latencyDSAvg")

    latencySDAvg = Enum.YLeaf(23, "latencySDAvg")

    packetLoss = Enum.YLeaf(24, "packetLoss")




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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class IpslacodectypeEnum(Enum):
    """
    IpslacodectypeEnum

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

    notApplicable = 0

    g711ulaw = 1

    g711alaw = 2

    g729a = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_TC_MIB as meta
        return meta._meta_table['IpslacodectypeEnum']


class IpslaopertypeEnum(Enum):
    """
    IpslaopertypeEnum

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

    icmpEcho = 1

    udpEcho = 2

    tcpConnect = 3

    udpJitter = 4

    icmpJitter = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_TC_MIB as meta
        return meta._meta_table['IpslaopertypeEnum']


class IpslareactvarEnum(Enum):
    """
    IpslareactvarEnum

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

    rtt = 1

    jitterSDAvg = 2

    jitterDSAvg = 3

    packetLossSD = 4

    packetLossDS = 5

    mos = 6

    timeout = 7

    connectionLoss = 8

    verifyError = 9

    jitterAvg = 10

    icpif = 11

    packetMIA = 12

    packetLateArrival = 13

    packetOutOfSequence = 14

    maxOfPositiveSD = 15

    maxOfNegativeSD = 16

    maxOfPositiveDS = 17

    maxOfNegativeDS = 18

    successivePacketLoss = 19

    maxOfLatencyDS = 20

    maxOfLatencySD = 21

    latencyDSAvg = 22

    latencySDAvg = 23

    packetLoss = 24


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IPSLA_TC_MIB as meta
        return meta._meta_table['IpslareactvarEnum']




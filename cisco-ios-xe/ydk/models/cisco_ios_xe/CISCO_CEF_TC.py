""" CISCO_CEF_TC 

This MIB module defines Textual Conventions and
OBJECT\-IDENTITIES for use in documents defining
management information base (MIBs) modules for 
managing Cisco Express Forwarding (CEF).

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Cefadjlinktype(Enum):
    """
    Cefadjlinktype

    Link type for the adjacency. The adjacency link type 

    identifies protocol stack on neighbour device which will 

    process packets fed through adjacency.

    .. data:: ipv4 = 1

    .. data:: ipv6 = 2

    .. data:: mpls = 3

    .. data:: raw = 4

    .. data:: unknown = 5

    """

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")

    mpls = Enum.YLeaf(3, "mpls")

    raw = Enum.YLeaf(4, "raw")

    unknown = Enum.YLeaf(5, "unknown")


class Cefadminstatus(Enum):
    """
    Cefadminstatus

    Admin status of CEF. The admin status of CEF

    may differ from the oper status of CEF depending

    upon the success of the admin operation.

    .. data:: enabled = 1

    .. data:: disabled = 2

    """

    enabled = Enum.YLeaf(1, "enabled")

    disabled = Enum.YLeaf(2, "disabled")


class Cefccaction(Enum):
    """
    Cefccaction

    The action to be performed for the consistency

    checkers.

      ccActionStart(1)   \:  start the Consistency checker

                            operation.

      ccActionAbort(2)   \:  abort the Consistency checker 

                            operation. After aborting, the 

                            active process must recover. 

                            This can take some time, and 

                            during this period, the scan 

                            cannot be restarted.

      ccActionNone(3)    \:  no operation is being performed 

                            on consistency checkers.

    .. data:: ccActionStart = 1

    .. data:: ccActionAbort = 2

    .. data:: ccActionNone = 3

    """

    ccActionStart = Enum.YLeaf(1, "ccActionStart")

    ccActionAbort = Enum.YLeaf(2, "ccActionAbort")

    ccActionNone = Enum.YLeaf(3, "ccActionNone")


class Cefccstatus(Enum):
    """
    Cefccstatus

    The status of consistency checker operation. 

    The description of each state is given below\:

      ccStatusIdle(1)    \:  this state signifies that

                            no consistency checker request

                            is being performed.

      ccStatusRunning(2) \:  this state signifies that 

                            consistency checker request is 

                            in progress.

      ccStatusDone(3)     \: this state signifies that 

                            consistency checker request is 

                            over. 

    .. data:: ccStatusIdle = 1

    .. data:: ccStatusRunning = 2

    .. data:: ccStatusDone = 3

    """

    ccStatusIdle = Enum.YLeaf(1, "ccStatusIdle")

    ccStatusRunning = Enum.YLeaf(2, "ccStatusRunning")

    ccStatusDone = Enum.YLeaf(3, "ccStatusDone")


class Cefcctype(Enum):
    """
    Cefcctype

    Type of the consistency checker.

    lcDetect         \: This is an active consistency checker

                       which is triggered when a packet cannot 

                       be forwarded because the prefix is not

                       in the forwarding table. It Detects 

                       missing prefixes on the linecard CEF 

                       database by sending the missing prefixes 

                       to the RP.

    scanFibLcRp      \: This is an passive consistency checker

                       which performs a passive scan check of

                       the table on the line card.

                       This consistency checker operates on 

                       the line card by examining the FIB table 

                       for a configurable time period and sending 

                       the next n prefixes to the RP. 

    scanFibRpLc      \: This is an passive consistency checker

                       which performs a passive scan check of

                       RP by examining the FIB table for 

                       a configurable period and

                       sending the next n prefixes to the 

                       line card. 

    scanRibFib       \: This is an passive consistency checker

                       which compares routing information base 

                       (RIB) to the FIB table at a configurable

                       interval and provides the number of 

                       entries missing from the FIB table. 

    scanFibRib       \: This is an passive consistency checker

                       which compares FIB Tables to the 

                       routing information base (RIB) 

                       at a configurable interval and provides 

                       the number of entries missing from the 

                       FIB table. 

    scanFibHwSw      \: This is an passive consistency checker

                       which compares FIB Tables in hardware

                       to the FIB Tables in RP.

    scanFibSwHw      \: This is an passive consistency checker

                       which compares FIB Tables in RP

                       to the FIB Tables in hardware.

    fullScanRibFib   \: This is an active consistency checker

                       which is triggered by Management Station 

                       request. It compares the entire routing 

                       information base (RIB) to the FIB table

                       and provide the number of entries missing

                        from the FIB Table.

    fullScanFibRib   \: This is an active consistency checker

                       which is triggered by Management Station 

                       request. It compares the FIB table to the 

                       routing information base (RIB)

                       and provide the number of entries missing

                       from the FIB Table.

    fullScanFibRpLc  \: This is an active consistency checker

                       which is triggered by Management Station 

                       request. It compares the RP FIB Table 

                       with FIB Table on each LC and report 

                       inconsistencies.

    fullScanFibLcRp  \: This is an active consistency checker

                       which is triggered by Management Station 

                       request. It compares the Fib Table on LC 

                       with FIB table on RP and report 

                       inconsistencies.

    fullScanFibHwSw  \: This is an active consistency checker

                       which is triggered by Management Station 

                       request. It compares the Fib Table in 

                       hardware with FIB table in RP and report 

                       inconsistencies.

    fullScanFibSwHw  \: This is an active consistency checker

                       which is triggered by Management Station 

                       request. It compares the Fib Table in RP 

                       with FIB table in hardware and report 

                       inconsistencies.

    .. data:: lcDetect = 1

    .. data:: scanFibLcRp = 2

    .. data:: scanFibRpLc = 3

    .. data:: scanRibFib = 4

    .. data:: scanFibRib = 5

    .. data:: scanFibHwSw = 6

    .. data:: scanFibSwHw = 7

    .. data:: fullScanRibFib = 8

    .. data:: fullScanFibRib = 9

    .. data:: fullScanFibRpLc = 10

    .. data:: fullScanFibLcRp = 11

    .. data:: fullScanFibHwSw = 12

    .. data:: fullScanFibSwHw = 13

    """

    lcDetect = Enum.YLeaf(1, "lcDetect")

    scanFibLcRp = Enum.YLeaf(2, "scanFibLcRp")

    scanFibRpLc = Enum.YLeaf(3, "scanFibRpLc")

    scanRibFib = Enum.YLeaf(4, "scanRibFib")

    scanFibRib = Enum.YLeaf(5, "scanFibRib")

    scanFibHwSw = Enum.YLeaf(6, "scanFibHwSw")

    scanFibSwHw = Enum.YLeaf(7, "scanFibSwHw")

    fullScanRibFib = Enum.YLeaf(8, "fullScanRibFib")

    fullScanFibRib = Enum.YLeaf(9, "fullScanFibRib")

    fullScanFibRpLc = Enum.YLeaf(10, "fullScanFibRpLc")

    fullScanFibLcRp = Enum.YLeaf(11, "fullScanFibLcRp")

    fullScanFibHwSw = Enum.YLeaf(12, "fullScanFibHwSw")

    fullScanFibSwHw = Enum.YLeaf(13, "fullScanFibSwHw")


class Ceffailurereason(Enum):
    """
    Ceffailurereason

    Reason of CEF Failure\:

    none(1)                \: no failure 

    mallocFailure(2)       \: memory allocation failed for CEF

    hwFailure(3)           \: hardware interface failure 

                             for CEF

    keepaliveFailure(4)    \: keepalive was not received from 

                             the CEF peer entity

    noMsgBuffer(5)         \: message buffers were exhausted 

                             while preparing IPC message to be 

                             sent to the CEF peer entity

    invalidMsgSize(6)      \: IPC message was received with 

                             invalid size from the

                             CEF peer entity

    internalError(7)       \: Some other internal error was 

                             detected for CEF

    .. data:: none = 1

    .. data:: mallocFailure = 2

    .. data:: hwFailure = 3

    .. data:: keepaliveFailure = 4

    .. data:: noMsgBuffer = 5

    .. data:: invalidMsgSize = 6

    .. data:: internalError = 7

    """

    none = Enum.YLeaf(1, "none")

    mallocFailure = Enum.YLeaf(2, "mallocFailure")

    hwFailure = Enum.YLeaf(3, "hwFailure")

    keepaliveFailure = Enum.YLeaf(4, "keepaliveFailure")

    noMsgBuffer = Enum.YLeaf(5, "noMsgBuffer")

    invalidMsgSize = Enum.YLeaf(6, "invalidMsgSize")

    internalError = Enum.YLeaf(7, "internalError")


class Cefforwardingelementspecialtype(Enum):
    """
    Cefforwardingelementspecialtype

    Type of special forwarding element 

    illegal(1)   \: illegal special forwarding element.

                   the packet will be dropped.

    punt(2)      \: the packet will be punted to the

                   next switching path

    drop(3)      \: not supported for Destination IP to next hop

                   interface and the packet will be dropped

    discard(4)   \: the packet is for Destination IP through

                   next hop interface and it will be discarded

    null(5)      \: the packet is for Destination IP to null0,

                   it will be dropped

    glean(6)     \: an attempt will be made to complete the

                   encapsulation string through address 

                   resolution

    unResolved(7)\: unresolved forwarding element.

                   the packet will be dropped unconditionally. 

    noRoute(8)   \: no route forwarding element.

                   This forwarding element will result

                   in rate limited punts to the next

                   switching path(to generate ICMP 

                   no route message) 

    none(9)      \: not a special forwarding element and

                   the value of this object should be

                   ignored 

    .. data:: illegal = 1

    .. data:: punt = 2

    .. data:: drop = 3

    .. data:: discard = 4

    .. data:: null = 5

    .. data:: glean = 6

    .. data:: unresolved = 7

    .. data:: noRoute = 8

    .. data:: none = 9

    """

    illegal = Enum.YLeaf(1, "illegal")

    punt = Enum.YLeaf(2, "punt")

    drop = Enum.YLeaf(3, "drop")

    discard = Enum.YLeaf(4, "discard")

    null = Enum.YLeaf(5, "null")

    glean = Enum.YLeaf(6, "glean")

    unresolved = Enum.YLeaf(7, "unresolved")

    noRoute = Enum.YLeaf(8, "noRoute")

    none = Enum.YLeaf(9, "none")


class Cefipversion(Enum):
    """
    Cefipversion

    The version of CEF IP forwarding.

    .. data:: ipv4 = 1

    .. data:: ipv6 = 2

    """

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")


class Cefoperstatus(Enum):
    """
    Cefoperstatus

    Operational status of CEF.

    .. data:: up = 1

    .. data:: down = 2

    """

    up = Enum.YLeaf(1, "up")

    down = Enum.YLeaf(2, "down")


class Cefpathtype(Enum):
    """
    Cefpathtype

    Type of the CEF Path.

    receive(1)          \: path for the address

                          configured on any of the

                          interface in the device.

    connectedPrefix(2)  \: connected prefix path

    attachedPrefix(3)   \: attached prefix path

    attachedHost(4)     \: attached host path 

    attachedNexthop(5)  \: attached next hop path

    recursiveNexthop(6) \: recursive next hop path

    adjacencyPrefix(7)  \: adjacency prefix path

    specialPrefix(8)    \: special prefix path

    unknown(9)\:         \: unknown  path

    .

    .. data:: receive = 1

    .. data:: connectedPrefix = 2

    .. data:: attachedPrefix = 3

    .. data:: attachedHost = 4

    .. data:: attachedNexthop = 5

    .. data:: recursiveNexthop = 6

    .. data:: adjacencyPrefix = 7

    .. data:: specialPrefix = 8

    .. data:: unknown = 9

    """

    receive = Enum.YLeaf(1, "receive")

    connectedPrefix = Enum.YLeaf(2, "connectedPrefix")

    attachedPrefix = Enum.YLeaf(3, "attachedPrefix")

    attachedHost = Enum.YLeaf(4, "attachedHost")

    attachedNexthop = Enum.YLeaf(5, "attachedNexthop")

    recursiveNexthop = Enum.YLeaf(6, "recursiveNexthop")

    adjacencyPrefix = Enum.YLeaf(7, "adjacencyPrefix")

    specialPrefix = Enum.YLeaf(8, "specialPrefix")

    unknown = Enum.YLeaf(9, "unknown")


class Cefprefixsearchstate(Enum):
    """
    Cefprefixsearchstate

    The state of prefix search operation. 

    The description of each state is given below\:

      running(1)      \: this state signifies that a prefix 

                        search request is running.

      matchFound(2)   \: this state signifies that a prefix 

                        search request is completed and a prefix

                        match has been found.

      noMatchFound(3) \: this state signifies that a prefix 

                        search request is completed and a prefix

                        match has not been found.

    .. data:: running = 1

    .. data:: matchFound = 2

    .. data:: noMatchFound = 3

    """

    running = Enum.YLeaf(1, "running")

    matchFound = Enum.YLeaf(2, "matchFound")

    noMatchFound = Enum.YLeaf(3, "noMatchFound")


class Cefadjacencysource(Bits):
    """
    Cefadjacencysource

    The mechanism by which the adjacency is learned.
    As the mechanism of learning the adjacency can be
    multiple (e.g. 'arp' and 'atmPVC'), hence the 
    value of this object represents the bit mask of
    adjacency sources.
    Keys are:- ipPseudowireAdj , nbma , multicast , linkRawAdj , ipv6ND , arp , fibLc , cmcc , atom , unknown , ipv6SixtoFourTunnel , frMap , atmSVC , atmBundle , lec , virtual , atmTVC , atmPVC , ipv6IsaTapTunnel , ipv6AutoTunnel , p2pAdj , nhrp , mpoa

    """

    def __init__(self):
        super(Cefadjacencysource, self).__init__()



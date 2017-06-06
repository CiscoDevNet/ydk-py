""" CISCO_CEF_TC 

This MIB module defines Textual Conventions and
OBJECT\-IDENTITIES for use in documents defining
management information base (MIBs) modules for 
managing Cisco Express Forwarding (CEF).

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CefadjlinktypeEnum(Enum):
    """
    CefadjlinktypeEnum

    Link type for the adjacency. The adjacency link type 

    identifies protocol stack on neighbour device which will 

    process packets fed through adjacency.

    .. data:: ipv4 = 1

    .. data:: ipv6 = 2

    .. data:: mpls = 3

    .. data:: raw = 4

    .. data:: unknown = 5

    """

    ipv4 = 1

    ipv6 = 2

    mpls = 3

    raw = 4

    unknown = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_CEF_TC as meta
        return meta._meta_table['CefadjlinktypeEnum']


class CefadminstatusEnum(Enum):
    """
    CefadminstatusEnum

    Admin status of CEF. The admin status of CEF

    may differ from the oper status of CEF depending

    upon the success of the admin operation.

    .. data:: enabled = 1

    .. data:: disabled = 2

    """

    enabled = 1

    disabled = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_CEF_TC as meta
        return meta._meta_table['CefadminstatusEnum']


class CefccactionEnum(Enum):
    """
    CefccactionEnum

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

    ccActionStart = 1

    ccActionAbort = 2

    ccActionNone = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_CEF_TC as meta
        return meta._meta_table['CefccactionEnum']


class CefccstatusEnum(Enum):
    """
    CefccstatusEnum

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

    ccStatusIdle = 1

    ccStatusRunning = 2

    ccStatusDone = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_CEF_TC as meta
        return meta._meta_table['CefccstatusEnum']


class CefcctypeEnum(Enum):
    """
    CefcctypeEnum

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

    lcDetect = 1

    scanFibLcRp = 2

    scanFibRpLc = 3

    scanRibFib = 4

    scanFibRib = 5

    scanFibHwSw = 6

    scanFibSwHw = 7

    fullScanRibFib = 8

    fullScanFibRib = 9

    fullScanFibRpLc = 10

    fullScanFibLcRp = 11

    fullScanFibHwSw = 12

    fullScanFibSwHw = 13


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_CEF_TC as meta
        return meta._meta_table['CefcctypeEnum']


class CeffailurereasonEnum(Enum):
    """
    CeffailurereasonEnum

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

    none = 1

    mallocFailure = 2

    hwFailure = 3

    keepaliveFailure = 4

    noMsgBuffer = 5

    invalidMsgSize = 6

    internalError = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_CEF_TC as meta
        return meta._meta_table['CeffailurereasonEnum']


class CefforwardingelementspecialtypeEnum(Enum):
    """
    CefforwardingelementspecialtypeEnum

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

    illegal = 1

    punt = 2

    drop = 3

    discard = 4

    null = 5

    glean = 6

    unresolved = 7

    noRoute = 8

    none = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_CEF_TC as meta
        return meta._meta_table['CefforwardingelementspecialtypeEnum']


class CefipversionEnum(Enum):
    """
    CefipversionEnum

    The version of CEF IP forwarding.

    .. data:: ipv4 = 1

    .. data:: ipv6 = 2

    """

    ipv4 = 1

    ipv6 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_CEF_TC as meta
        return meta._meta_table['CefipversionEnum']


class CefoperstatusEnum(Enum):
    """
    CefoperstatusEnum

    Operational status of CEF.

    .. data:: up = 1

    .. data:: down = 2

    """

    up = 1

    down = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_CEF_TC as meta
        return meta._meta_table['CefoperstatusEnum']


class CefpathtypeEnum(Enum):
    """
    CefpathtypeEnum

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

    receive = 1

    connectedPrefix = 2

    attachedPrefix = 3

    attachedHost = 4

    attachedNexthop = 5

    recursiveNexthop = 6

    adjacencyPrefix = 7

    specialPrefix = 8

    unknown = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_CEF_TC as meta
        return meta._meta_table['CefpathtypeEnum']


class CefprefixsearchstateEnum(Enum):
    """
    CefprefixsearchstateEnum

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

    running = 1

    matchFound = 2

    noMatchFound = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_CEF_TC as meta
        return meta._meta_table['CefprefixsearchstateEnum']


class Cefadjacencysource(FixedBitsDict):
    """
    Cefadjacencysource

    The mechanism by which the adjacency is learned.
    As the mechanism of learning the adjacency can be
    multiple (e.g. 'arp' and 'atmPVC'), hence the 
    value of this object represents the bit mask of
    adjacency sources.
    Keys are:- atom , unknown , arp , fibLc , ipv6ND , atmTVC , atmPVC , p2pAdj , linkRawAdj , ipv6SixtoFourTunnel , multicast , nbma , nhrp , ipv6IsaTapTunnel , virtual , atmSVC , cmcc , atmBundle , mpoa , ipPseudowireAdj , lec , frMap , ipv6AutoTunnel

    """

    def __init__(self):
        self._dictionary = { 
            'atom':False,
            'unknown':False,
            'arp':False,
            'fibLc':False,
            'ipv6ND':False,
            'atmTVC':False,
            'atmPVC':False,
            'p2pAdj':False,
            'linkRawAdj':False,
            'ipv6SixtoFourTunnel':False,
            'multicast':False,
            'nbma':False,
            'nhrp':False,
            'ipv6IsaTapTunnel':False,
            'virtual':False,
            'atmSVC':False,
            'cmcc':False,
            'atmBundle':False,
            'mpoa':False,
            'ipPseudowireAdj':False,
            'lec':False,
            'frMap':False,
            'ipv6AutoTunnel':False,
        }
        self._pos_map = { 
            'atom':0,
            'unknown':22,
            'arp':3,
            'fibLc':19,
            'ipv6ND':14,
            'atmTVC':8,
            'atmPVC':6,
            'p2pAdj':4,
            'linkRawAdj':1,
            'ipv6SixtoFourTunnel':16,
            'multicast':21,
            'nbma':9,
            'nhrp':13,
            'ipv6IsaTapTunnel':17,
            'virtual':20,
            'atmSVC':7,
            'cmcc':15,
            'atmBundle':11,
            'mpoa':10,
            'ipPseudowireAdj':2,
            'lec':12,
            'frMap':5,
            'ipv6AutoTunnel':18,
        }



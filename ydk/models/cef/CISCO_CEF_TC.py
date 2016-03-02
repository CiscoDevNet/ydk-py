""" CISCO_CEF_TC 

This MIB module defines Textual Conventions and
OBJECT\-IDENTITIES for use in documents defining
management information base (MIBs) modules for 
managing Cisco Express Forwarding (CEF).

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class CefAdjLinkType_Enum(Enum):
    """
    CefAdjLinkType_Enum

    Link type for the adjacency. The adjacency link type 
    identifies protocol stack on neighbour device which will 
    process packets fed through adjacency.

    """

    IPV4 = 1

    IPV6 = 2

    MPLS = 3

    RAW = 4

    UNKNOWN = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cef._meta import _CISCO_CEF_TC as meta
        return meta._meta_table['CefAdjLinkType_Enum']


class CefAdminStatus_Enum(Enum):
    """
    CefAdminStatus_Enum

    Admin status of CEF. The admin status of CEF
    may differ from the oper status of CEF depending
    upon the success of the admin operation.

    """

    ENABLED = 1

    DISABLED = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cef._meta import _CISCO_CEF_TC as meta
        return meta._meta_table['CefAdminStatus_Enum']


class CefCCAction_Enum(Enum):
    """
    CefCCAction_Enum

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

    """

    CCACTIONSTART = 1

    CCACTIONABORT = 2

    CCACTIONNONE = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cef._meta import _CISCO_CEF_TC as meta
        return meta._meta_table['CefCCAction_Enum']


class CefCCStatus_Enum(Enum):
    """
    CefCCStatus_Enum

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
                          

    """

    CCSTATUSIDLE = 1

    CCSTATUSRUNNING = 2

    CCSTATUSDONE = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cef._meta import _CISCO_CEF_TC as meta
        return meta._meta_table['CefCCStatus_Enum']


class CefCCType_Enum(Enum):
    """
    CefCCType_Enum

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

    """

    LCDETECT = 1

    SCANFIBLCRP = 2

    SCANFIBRPLC = 3

    SCANRIBFIB = 4

    SCANFIBRIB = 5

    SCANFIBHWSW = 6

    SCANFIBSWHW = 7

    FULLSCANRIBFIB = 8

    FULLSCANFIBRIB = 9

    FULLSCANFIBRPLC = 10

    FULLSCANFIBLCRP = 11

    FULLSCANFIBHWSW = 12

    FULLSCANFIBSWHW = 13


    @staticmethod
    def _meta_info():
        from ydk.models.cef._meta import _CISCO_CEF_TC as meta
        return meta._meta_table['CefCCType_Enum']


class CefFailureReason_Enum(Enum):
    """
    CefFailureReason_Enum

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

    """

    NONE = 1

    MALLOCFAILURE = 2

    HWFAILURE = 3

    KEEPALIVEFAILURE = 4

    NOMSGBUFFER = 5

    INVALIDMSGSIZE = 6

    INTERNALERROR = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cef._meta import _CISCO_CEF_TC as meta
        return meta._meta_table['CefFailureReason_Enum']


class CefForwardingElementSpecialType_Enum(Enum):
    """
    CefForwardingElementSpecialType_Enum

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

    """

    ILLEGAL = 1

    PUNT = 2

    DROP = 3

    DISCARD = 4

    NULL = 5

    GLEAN = 6

    UNRESOLVED = 7

    NOROUTE = 8

    NONE = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cef._meta import _CISCO_CEF_TC as meta
        return meta._meta_table['CefForwardingElementSpecialType_Enum']


class CefIpVersion_Enum(Enum):
    """
    CefIpVersion_Enum

    The version of CEF IP forwarding.

    """

    IPV4 = 1

    IPV6 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cef._meta import _CISCO_CEF_TC as meta
        return meta._meta_table['CefIpVersion_Enum']


class CefOperStatus_Enum(Enum):
    """
    CefOperStatus_Enum

    Operational status of CEF.

    """

    UP = 1

    DOWN = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cef._meta import _CISCO_CEF_TC as meta
        return meta._meta_table['CefOperStatus_Enum']


class CefPathType_Enum(Enum):
    """
    CefPathType_Enum

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

    """

    RECEIVE = 1

    CONNECTEDPREFIX = 2

    ATTACHEDPREFIX = 3

    ATTACHEDHOST = 4

    ATTACHEDNEXTHOP = 5

    RECURSIVENEXTHOP = 6

    ADJACENCYPREFIX = 7

    SPECIALPREFIX = 8

    UNKNOWN = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cef._meta import _CISCO_CEF_TC as meta
        return meta._meta_table['CefPathType_Enum']


class CefPrefixSearchState_Enum(Enum):
    """
    CefPrefixSearchState_Enum

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

    """

    RUNNING = 1

    MATCHFOUND = 2

    NOMATCHFOUND = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cef._meta import _CISCO_CEF_TC as meta
        return meta._meta_table['CefPrefixSearchState_Enum']


class CefAdjacencySource_Bits(FixedBitsDict):
    """
    CefAdjacencySource_Bits

    The mechanism by which the adjacency is learned.
    As the mechanism of learning the adjacency can be
    multiple (e.g. 'arp' and 'atmPVC'), hence the 
    value of this object represents the bit mask of
    adjacency sources.
    Keys are:- arp , atmSVC , ipv6AutoTunnel , atom , atmPVC , fibLc , nbma , unknown , virtual , atmTVC , mpoa , lec , ipv6ND , nhrp , linkRawAdj , ipv6IsaTapTunnel , ipv6SixtoFourTunnel , atmBundle , ipPseudowireAdj , frMap , cmcc , p2pAdj , multicast

    """

    def __init__(self):
        self._dictionary = { 
            'arp':False,
            'atmSVC':False,
            'ipv6AutoTunnel':False,
            'atom':False,
            'atmPVC':False,
            'fibLc':False,
            'nbma':False,
            'unknown':False,
            'virtual':False,
            'atmTVC':False,
            'mpoa':False,
            'lec':False,
            'ipv6ND':False,
            'nhrp':False,
            'linkRawAdj':False,
            'ipv6IsaTapTunnel':False,
            'ipv6SixtoFourTunnel':False,
            'atmBundle':False,
            'ipPseudowireAdj':False,
            'frMap':False,
            'cmcc':False,
            'p2pAdj':False,
            'multicast':False,
        }
        self._pos_map = { 
            'arp':3,
            'atmSVC':7,
            'ipv6AutoTunnel':18,
            'atom':0,
            'atmPVC':6,
            'fibLc':19,
            'nbma':9,
            'unknown':22,
            'virtual':20,
            'atmTVC':8,
            'mpoa':10,
            'lec':12,
            'ipv6ND':14,
            'nhrp':13,
            'linkRawAdj':1,
            'ipv6IsaTapTunnel':17,
            'ipv6SixtoFourTunnel':16,
            'atmBundle':11,
            'ipPseudowireAdj':2,
            'frMap':5,
            'cmcc':15,
            'p2pAdj':4,
            'multicast':21,
        }



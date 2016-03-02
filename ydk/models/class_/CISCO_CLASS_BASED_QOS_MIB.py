""" CISCO_CLASS_BASED_QOS_MIB 

Cisco Class\-Based QoS MIB

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
            Overview
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
This MIB provides read access to Quality of Service (QoS) 
configuration and statistics information for Cisco 
platforms that support the Modular Quality of Service 
Command\-line Interface (Modular QoS CLI).  We recommend 
users of this MIB to review the user documentation of 
MQC based QoS features.

Configuration information available through this MIB includes
all ClassMap, PolicyMap, Match Statements, and Feature 
Actions configuration parameters. The definitions of each
objects mentioned above are explained in the QoS objects
section.

Statistics available through this MIB include summary
counts/rates by traffic class before and after any configured
QoS policies are enforced.  In addition, detailed
feature\-specific statistics are available for select
PolicyMap features.

Contact your Cisco representative to determine on which
platforms the MIB is currently supported.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
           QoS  Acronyms
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
BECN\: Frame Relay Backward Explicit Congestion Notification
CIR \: Committed Information Rate
DSCP\: Differentiated Service Code Point
EB  \: Estimate Bandwidth
ECN \: Explicite Congestion Notification
FECN\: Frame Relay Forward Explicit Congestion Notification
IPHC\: Internet Protocol Header Compression 
IPSLAs\: IP Service Level Agreement Technologies
PIR \: Peak Information Rate
PREC\: Precedence
QoS \: Quality Of Services
RED \: Random Early Detect
SRP \: Spatial Reuse Protocol
WRED\: Weighted Random Early Detect
C3PL\: Cisco Common Classification Programming Language

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
            MIB Objects
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
This MIB consists of the following object groups\:
1 \:  cbQosServicePolicy
2 \:  cbQosInterfacePolicy
3 \:  cbQosFrameRelayVCPolicy
4 \:  cbQosATMPVCPolicy
5 \:  cbQosObjects
6 \:  cbQosPolicyMapCfg
7 \:  cbQosClassMapCfg
8 \:  cbQosMatchStmtCfg
9 \:  cbQosQueueingCfg
10\:  cbQosREDCfg
11\:  cbQosREDClassCfg
12\:  cbQosPoliceCfg
13\:  cbQosTSCfg
14\:  cbQosSetCfg
15\:  cbQosClassMapStats
16\:  cbQosMatchStmtStats
17\:  cbQosPoliceStats
18\:  cbQosQueueingStats
19\:  cbQosTSStats
20\:  cbQosREDClassStats
21\:  cbQosPoliceActionCfg
22\:  cbQosIPHCCfg
23\:  cbQosIPHCStats
24\:  cbQosSetStats
25\:  cbQosPoliceColorStats
26\:  cbQosTableMapCfg
27\:  cbQosTableMapValueCfg
28\:  cbQosTableMapSetCfg
29\:  cbQosEBCfg
30\:  cbQosEBStats
31\:  cbQosMeasureIPSLACfg
32\:  cbQosC3plAccountCfg
33\:  cbQosC3plAccountStats

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
          Definitions
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
A logical interface in the context of this MIB is either
a main\-interface, a sub\-interface, a Frame Relay DLCI,
an ATM virtual circuit or the control\-plane on the router.

The (aggregate) control\-plane on the router is defined as 
a collection of processes running at process level on the
platform (route) processor. This includes the functions 
related to networking control capabilities such as routing,
signaling, provisioning, as well as resource and service 
discovery. Also includes process switched traffic on the
device. 

The term distributed control plane, in the context of 
this mib, represents the control\-plane functionality at
the level of individual linecards. This is only
applicable for the case of distributed platforms.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
           QoS Objects
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
To understand Class\-Based QoS features and how to navigate 
the MIB tables above, the key element is to comprehend the 
relationships among the different QoS objects. QoS objects 
consist of ClassMaps, Match Statements and PolicyMaps, 
and each Feature Actions. 

Match Statement \- The specific match criteria to identify
packets for classification purposes.

ClassMap \- A user\-defined traffic class that contains
one or many match statements used to classify packets into
different categories.

Feature Action \- An action is a QoS feature. Features 
include police, traffic\-shaping, queueing, random detect 
and packet marking(set). After the traffic is being 
classified, based on the traffic classification, we can 
apply these action to each traffic class.

PolicyMap \- A user\-defined policy that associates each QoS 
action to the user\-defined traffic class (ClassMap).

Service Policy \- Service policy is a policymap
that is being attached to a logical interface. Because a
policymap can also be a part of the hierarchical structure 
(inside a classmap), only a policymap that is directly 
attached to a logical interface is considered a service 
policy.  Each service policy is uniquely identified by an 
index called cbQosPolicyIndex. This number is usually 
identical to its cbQosObjectsIndex as a policymap.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Runtime Instance vs Configuration objects
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Each QoS objects have 2 sets of behaviours \: 
1\: A configuration instance
\- Each QoS objects has it's configuration portion of
  information attached to it. This information does
  not change whether this object is attached on multiple
  logical interfaces and used multiple times. We
  uniquely identify each QoS object with identical
  configuration with the same index \- cbQosConfigIndex.
  This index is used in all configuration related
  tables. 

2\: A runtime instance
\- Each QoS objects has it's statistical portion of
  information attached to it. This information changes
  when this object is attached on multiple logical 
  interfaces and used in various different places. We
  uniquely identify each QoS runtime object instance 
  with an index that is unique across multiple 
  instances of the identical object \- cbQosObjectsIndex.
  This index is used in all statistical related tables. 

In summary, a QoS object has 2 indexes associated with it\:
cbQosConfigIndex is used to identify it's configuration, 
which does not change regardless of number of times and
where it is being used; and cbQosObjectsIndex is used 
to identify it's runtime statistics, depending on which
logical interface and where in a given PolicyMap hierarchy
this object is used, it may have multiple unique 
identifiers to distinguish each unique usage (instance) of
the same object.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
            Navigation
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
The recommended method of navigating through all of the MIB 
tables is to start by learning the cbQosServicePolicyTable 
and cbQosObjectsTable MIB tables. In particular, Cisco 
Systems recommends understanding the cbQosObjectsIndex and 
cbQosParentObjectsIndex of each QoS feature.

The cbQosPolicyIndex and cbQosObjectsIndex are 
system\-assigned numbers that identify each unique instance 
of a QoS feature. These indexes are never reused between 
router reboots, even when changes are made to the QoS 
configuration. The cbQosPolicyIndex is designed to identify 
the service policies attached to logical interfaces, while 
the cbQosObjectsIndex is designed to identify each QoS 
feature on a specified device.

The cbQosParentObjectsIndex is designed to show the 
hierarchical relationship of each QoS feature. 

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
        cbQosServicePolicyTable
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Accessing cbQosServicePolicyTable requires 
cbQosPolicyIndex. This index is a system\-assigned number 
to uniquely identify each service policy hanging off of
each logical interface. Given cbQosPolicyIndex the tables
provide the type of logical interface/media type on which
this policy is applied, the direction in which this policy
is enforced, and the SNMP interface index and/or the entity
index of the underlying interface/entity. In the case of a
policy being applied on a Frame Relay DLCI, the cbQosFrDLCI
gives you the Frame Relay DLCI number to which this policy
is attached. In the case of policy being attached to an ATM
VC, cbQosAtmVPI and cbQosAtmVCI display the VPI and VCI of 
the ATM interface respectively.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
        cbQosObjectsTable
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Accessing cbQosObjectsTable requires two indexes, 
cbQosPolicyIndex and cbQosObjectsIndex. 

Given a particular service policy on a given logical 
interface, there could be PolicyMaps, ClassMaps, Match 
Statements and Feature Actions being used. Each instance 
of these objects is uniquely identified by
cbQosObjectsIndex.

Users need to decide which QoS object is interesting 
and use the cbQosPolicyIndex and cbQosObjectsIndex to
locate the right element of interest. This tables provides 
cbQosObjectsType, cbQosConfigIndex, and 
cbQosParentObjectsIndex. 

To understand the relationship of cbQosObjectsIndex, 
cbQosParentObjectsIndex and the hierarchical relationship 
of the QoS objects, consider the following QoS 
configuration example\:

Interface ethernet 0/1
Input Service Policy cntlWebTraffic
        ClassMap http
                match ip http
                set ip precedence 5

Output Service Policy cntlSNMP\_Telnet
        ClassMap snmp
                match ip snmp
                shape average 8000 32 32
        ClassMap Telnet
                match ip telnet
                shape average 10000 32 32

Interface ethernet 0/2
Input Service Policy cntlWebTraffic
        ClassMap http
                match ip http
                set ip precedence 5

Output Service Policy cntlSNMP\_Telnet
        ClassMap snmp
                match ip snmp
                shape average 8000 32 32
        ClassMap Telnet
                match ip telnet
                shape average 10000 32 32

\*\*\* In Ethernet 0/1 \*\*\*
Assume the router assigned a cbQosConfigIndex=1024 and 
cbQosObjectsIndex=1084 to Policy cntlWebTraffic. 
Because it is attached to an interface, it has no parent 
QoS object, and thus cbQosParentObjectsIndex=0. 
In addition, because cntlWebTraffic is also the service 
policy of the interface, it has a unique cbQosPolicyIndex 
assigned to it. In most cases, it would be the same as 
the cbQosObjectsIndex, which is 1084 in this case. 
Therefore, the indexes are\:
cbQosPolicyIndex = 1084
cbQosObjectsIndex = 1084
cbQosConfigIndex = 1024

Assuming the router assigned a cbQosObjectsIndex=1085 
and cbQosConfigIndex=1025 to ClassMap http, it is 
directly being used by Policy cntlWebTraffic, and therefore
the cbQosParentObjectsIndex of ClassMap http will be 1084. 

Assuming the router assigned a cbQosConfigIndex=1026 and
cbQosObjectsIndex=1086 to match ip http, it is directly 
used by ClassMap http, therefore the 
cbQosParentObjectsIndex of match ip http will be 1085.

Assuming the router assigned a cbQosConfigIndex=1027 and
cbQosObjectsIndex=1087 to set ip precedence 5, it is 
directly used by ClassMap http, therefore the 
cbQosParentObjectsIndex of match ip http will be 1085.

Assuming the router assigned a cbQosConfigIndex=1028 and 
cbQosObjectsIndex=1088 to Policy cntlSNMP\_Telnet. 
Because it is attached to an interface, it has no parent 
QoS object, and thus cbQosParentObjectsIndex=0. 
In addition, because cntlSNMP\_Telnet is also the service 
policy of the interface, it has a unique cbQosPolicyIndex 
assigned to it. In most cases, it would be the same as 
the cbQosObjectsIndex, which is 1088 in this case.

Assuming the router assigned a cbQosConfigIndex=1029 and
cbQosObjectsIndex=1089 to ClassMap snmp, it is 
directly being used by Policy cntlSNMP\_Telnet, and 
therefore the cbQosParentObjectsIndex of ClassMap snmp 
will be 1088. 

Assuming the router assigned a cbQosConfigIndex=1030 and
cbQosObjectsIndex=1090 to match ip snmp, it is directly 
used by ClassMap snmp, and therefore the 
cbQosParentObjectsIndex of match ip snmp will be 1089.

Assuming the router assigned a cbQosConfigIndex=1031 and
cbQosObjectsIndex=1091 to shape average 8000 32 32, 
it is directly used by ClassMap snmp, therefore the 
cbQosParentObjectsIndex of match ip snmp will be 1089.

Assuming the router assigned a cbQosConfigIndex=1032 and
cbQosObjectsIndex=1092 to ClassMap Telnet, it is 
directly being used by Policy cntlSNMP\_Telnet, and 
therefore the cbQosParentObjectsIndex of 
ClassMap Telnet will be 1088. 

Assuming the router assigned a cbQosConfigIndex=1033 and
cbQosObjectsIndex=1093 to match ip telnet, it is 
directly used by ClassMap Telnet, and therefore the 
cbQosParentObjectsIndex of match ip telnet will be 1092.

Assuming the router assigned a cbQosConfigIndex=1034 and
cbQosObjectsIndex=1094 to shape 10000 32 32, it is 
directly used by ClassMap telnet, therefore the 
cbQosParentObjectsIndex of match ip telnet will be 1092.

\*\*\* In Ethernet 0/2 \*\*\*
Every objects will have a unique combination of
cbQosPolicyIndex and cbQosObjectsIndex, but
cbQosConfigIndex will be shared across the same
objects that are applied in different places.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
         All Config Tables
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Accessing config related tables requires the same index 
\- cbQosConfigIndex.  (Per precedence based tables requires 
a second index, which is IP precedence value) Users 
should have already gone through the cbQosObjectsTable 
at this point and understood each cbQosConfigIndex and the 
corresponding QoS objects.  Users can uniquely identify 
each QoS object defined on the router and query the 
entries in each stats table on a per QoS object basis.  

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
         All Stats Tables
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Accessing all stats related tables requires the same 
2 indexes. They are cbQosPolicyIndex and cbQosObjectsIndex.
(Per precedence based tables requires a third index, which 
is IP precedence value) Users should have already gone 
through the cbQosObjectsTable at this point and understood 
the relationship of each cbQosPolicyIndex and 
cbQosObjectsIndex pair and the corresponding QoS objects. 
Users can uniquely identify each QoS object defined on the 
router and query the entries in each stats table on a per 
QoS object basis.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class CbQosEBType_Enum(Enum):
    """
    CbQosEBType_Enum

    A value that indicates the type of bandwidth
    estimate algorithm.
    typeNone         no algorithm is selected
    typeCorvil         algorithm based on Corvil
                     bandwidth calculation.

    """

    TYPENONE = 0

    TYPECORVIL = 1


    @staticmethod
    def _meta_info():
        from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
        return meta._meta_table['CbQosEBType_Enum']


class CbQosQueueUnitType_Enum(Enum):
    """
    CbQosQueueUnitType_Enum

    A value that represents an unit type of queue
    size.
    
    packets(1)    Represents the UNITS of 'packets' for
                  queue size.
    
    cells(2)      Represents the UNITS of 'cells' for 
                  queue size.
    
    bytes(3)      Represents the UNITS of 'bytes' for 
                  queue size.
    
    ms(4)         Represents the UNITS of 'milli\-seconds' for
                  queue size
    
    us(5)         Represents the UNITS of 'micro\-seconds' for
                  queue size
    
    percentage(6) Represents the UNITS of 'percentage' for
                  queue size
    
    To support future extensions, the CbQosQueueUnitType 
    textual convention SHOULD NOT be sub\-typed in object
    type definitions.
    
    It MAY be sub\-typed in compliance statements in order to
    require only a subset of these queue size types for a 
    compliant implementation.
    
    Implementations must ensure that CbQosQueueUnitType 
    objects and any dependent object (e.g. CbQosQueueDepth) 
    are consistent. An inconsistentValue error must be 
    generated if an attempt to change an CbQosQueueUnitType 
    object would lead to an undefined CbQosQueueDepth value.
    In particular, CbQoSQueueUnitType/CbQosQueueDepth pairs 
    must be changed together if the CbQosQueueUnitType
    type changes (e.g. from packets(1) to cells(2)).

    """

    PACKETS = 1

    CELLS = 2

    BYTES = 3

    MS = 4

    US = 5

    PERCENTAGE = 6


    @staticmethod
    def _meta_info():
        from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
        return meta._meta_table['CbQosQueueUnitType_Enum']


class CbQosRateType_Enum(Enum):
    """
    CbQosRateType_Enum

    The type of rate.  Rate type can be either an
    absolute bps number, or be expressed as a percentage 
    of the available interface bandwidth, or an absolute
    cps number.
    
    bps             Bits Per Second
    percentage      %
    cps             Cells Per Second
    perThousand     Parts Per Thousand
    perMillion      Parts Per Million

    """

    BPS = 1

    PERCENTAGE = 2

    CPS = 3

    PERTHOUSAND = 4

    PERMILLION = 5


    @staticmethod
    def _meta_info():
        from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
        return meta._meta_table['CbQosRateType_Enum']


class CbQosTMSetType_Enum(Enum):
    """
    CbQosTMSetType_Enum

    The available packet marking types which can use
    tablemap to establish to\-from relationship for
    enhanced packeting marking.

    """

    NONE = 0

    IPDSCP = 1

    IPPRECEDENCE = 2

    QOSGROUP = 3

    L2COS = 4

    MPLSEXPIMP = 5

    MPLSEXPTOP = 6


    @staticmethod
    def _meta_info():
        from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
        return meta._meta_table['CbQosTMSetType_Enum']


class IPHCOption_Enum(Enum):
    """
    IPHCOption_Enum

    Enums to indicate the type of IP header compression.
    rtp(1)         UDP/RTP compression.
    tcp(2)         TCP compression.
    bothRtpTcp(3)  Both UDP/RTP and TCP compression.

    """

    RTP = 1

    TCP = 2

    BOTHRTPTCP = 3


    @staticmethod
    def _meta_info():
        from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
        return meta._meta_table['IPHCOption_Enum']


class InterfaceType_Enum(Enum):
    """
    InterfaceType_Enum

    Enums to indicate the type of logical interface to which
    a particular service policy is attached.
    Main Interface   \- Service policy is attached on the main 
                  interface.
    Sub Interface    \- Service policy is attached on the sub 
                  interface.
    Frame Relay DLCI \- Service policy is attached on the a 
                  Frame Relay DLCI.
    ATM VC           \- Service policy is attached on the an ATM 
                  Virtual Circuit.
    Control Plane    \- Service policy is attached to the control
                  plane of the device.
    Vlan Port        \- Service policy is attached to a particular
                  vlan of a layer 2 interface that can carry
                  traffic on multiple vlans.
    EVC              \- Service policy is attached to the Ethernet
                       Virtual Connections.

    """

    MAININTERFACE = 1

    SUBINTERFACE = 2

    FRDLCI = 3

    ATMPVC = 4

    CONTROLPLANE = 5

    VLANPORT = 6

    EVC = 7


    @staticmethod
    def _meta_info():
        from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
        return meta._meta_table['InterfaceType_Enum']


class PoliceAction_Enum(Enum):
    """
    PoliceAction_Enum

    The available actions taken on packets upon
    conforming, exceeding or violating the configured 
    police rate.
    
    Transmit \- Transmit the packet if the packet conforms 
               or exceeds the configured police rate.
    Set IP DSCP \- Set the IP DSCP value if the packet
                  conforms or exceeds the configured police
                  rate.
    Set IP Precedence \- Set the IP precedence value if
                        the packet conforms or exceeds 
                        the configured police rate.
    Set Qos Group \- Set the QoS Group value if
                    the packet conforms or exceeds 
                    the configured police rate.
    Set MPLS Exp \- Set the MPLS Experimental Imposition
                   vaule for the applicable action.
    Set ATM CLP  \- Set the ATM CLP bit for the
                   applicable action.
    Set FR DE    \- Set the FR DE bit for the
                   applicable action.
    Set L2 COS   \- Set the 802.1p priority field in 802.1Q 
                   VLAN tag for the applicable action.
    Set Discard Class \- Set the Discard Class value for the
                   applicable action.              
    Drop \- Drop the packet if the packet conforms or 
           exceeds the configured police rate.
    Set MPLS Exp TopMost \- Set the MPLS Experimental 
           TopMost vaule for the applicable action.
    Set IP DSCP Tunnel \- Set the IP DSCP Tunnel
                         value for the applicable action.
    Set IP Precedence Tunnel \- Set the IP Precedence Tunnel 
                               value for the applicable action.   
    Set Inner L2 COS   \- Set the 802.1p priority field in inner 
                   802.1q VLAN tag (QinQ) for the applicable
                   action.
    Unconfigured \- No action is set for this police.
    Set Dei   \- Set the DEI(Discard Eligiable Indicator) bit in the
                topmost 802.1ad header.
    Set Dei Imposition \- Set the DEI bit on all imposed 802.1ad 
                         header.
    Set SRP Priority \- Sets the spatial reuse protocol (SRP)
                       priority value of an outgoing packet.

    """

    TRANSMIT = 1

    SETIPDSCP = 2

    SETIPPRECEDENCE = 3

    SETQOSGROUP = 4

    DROP = 5

    SETMPLSEXP = 6

    SETATMCLP = 7

    SETFRDE = 8

    SETL2COS = 9

    SETDISCARDCLASS = 10

    SETMPLSEXPTOPMOST = 11

    SETIPDSCPTUNNEL = 12

    SETIPPRECEDENCETUNNEL = 13

    SETL2COSINNER = 14

    UNCONFIGURED = 15

    SETDEI = 16

    SETDEIIMPOSITION = 17

    SETSRPPRIORITY = 18


    @staticmethod
    def _meta_info():
        from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
        return meta._meta_table['PoliceAction_Enum']


class QosClassInfo_Enum(Enum):
    """
    QosClassInfo_Enum

    Enums to indicate whether the Classmap is for
    Match All or Match Any.

    """

    NONE = 1

    MATCHALL = 2

    MATCHANY = 3


    @staticmethod
    def _meta_info():
        from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
        return meta._meta_table['QosClassInfo_Enum']


class QosMatchInfo_Enum(Enum):
    """
    QosMatchInfo_Enum

    Enums to indicate whether the MatchStatement is matching
    on negated criteria (Match Not).

    """

    NONE = 1

    MATCHNOT = 2


    @staticmethod
    def _meta_info():
        from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
        return meta._meta_table['QosMatchInfo_Enum']


class QosObjectType_Enum(Enum):
    """
    QosObjectType_Enum

    Enums to indicate different QoS objects .
    policymap      \- The object in query is a PolicyMap, being
                     attached on a logical interface.
    classmap       \- The object in query is a ClassMap, being
                     used by it's parent PolicyMap.
    matchStatement \- The object in query is a Match Statement,
                     being used by it's parent ClassMap.
    queueing       \- The object in query is a queueing feature being
                     applied on the parent ClassMap.
    randomDetect   \- The object in query is a Random Detect feature 
                     being applied on the parent ClassMap.
    trafficShaping \- The object in query is a traffic\-shaping 
                     feature being applied on the parent ClassMap.
    police         \- The object in query is a Police feature being 
                     applied on the parent ClassMap.
    set            \- The object in query is a Packet Marking 
                     feature being applied on the parent ClassMap.
    compression    \- The object in query is a IP header compression
                     feature being applied on the parent ClassMap.
    ipslaMeasure   \- The object in query is Measure IPSLAs feature  
                     being applied on the parent ClassMap.
    account         \- The object in query is C3Pl\_Account feature being
                     applied on the parent ClassMap.

    """

    POLICYMAP = 1

    CLASSMAP = 2

    MATCHSTATEMENT = 3

    QUEUEING = 4

    RANDOMDETECT = 5

    TRAFFICSHAPING = 6

    POLICE = 7

    SET = 8

    COMPRESSION = 9

    IPSLAMEASURE = 10

    ACCOUNT = 11


    @staticmethod
    def _meta_info():
        from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
        return meta._meta_table['QosObjectType_Enum']


class QueueMechanism_Enum(Enum):
    """
    QueueMechanism_Enum

    This denotes which mechanism is used with QueueLimit.
    
    precedence      Based on IP precedence
    dscp            Based on DSCP values
    discardClass    Based on discard class
    qosGroup        Based on qosgroup class
    atmClp          Based on atm\-clp class
    mplsExp         Based on MPLS Experimental class

    """

    PRECEDENCE = 1

    DSCP = 2

    DISCARDCLASS = 3

    QOSGROUP = 4

    ATMCLP = 5

    MPLSEXP = 6


    @staticmethod
    def _meta_info():
        from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
        return meta._meta_table['QueueMechanism_Enum']


class QueueingBandwidthUnits_Enum(Enum):
    """
    QueueingBandwidthUnits_Enum

    The units of the bandwidth, used to allocate
    bandwidth. Bandwidth can be either an absolute kbps 
    number, or be expressed as a percentage of the 
    available bandwidth.  
    
    kbps                Allocated bandwidth in Kilo bits Per Second
    
    percentage          Allocated bandwidth as percentage of 
                        reference  bandwidth.
    
    percentageRemaining Percentage of unallocated bandwidth
                        reserved for this class.
    
    ratioRemaining      Ratio of unallocated bandwidth reserved 
                        for this class (in relation to other 
                        classes).
    
    perThousand         Allocated bandwidth in Parts Per Thousand
    
    perMillion          Allocated bandwidth in Parts Per Million.

    """

    KBPS = 1

    PERCENTAGE = 2

    PERCENTAGEREMAINING = 3

    RATIOREMAINING = 4

    PERTHOUSAND = 5

    PERMILLION = 6


    @staticmethod
    def _meta_info():
        from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
        return meta._meta_table['QueueingBandwidthUnits_Enum']


class REDMechanism_Enum(Enum):
    """
    REDMechanism_Enum

    This denotes which mechanism is used with RED.
    
    precedence      Based on IP precedence
    dscp            Based on DSCP values
    discardClass    Based on discard class
    l2Cos           Based on L2\-COS class
    atmClp          Based on ATM\-CLP class
    mplsExp         Based on MPLS Experimental values
    redDefault      Default RED profile
    redUserDefault  User specified Default RED profile
    dei             Based on DEI bit

    """

    PRECEDENCE = 1

    DSCP = 2

    DISCARDCLASS = 3

    L2COS = 4

    ATMCLP = 5

    MPLSEXP = 6

    REDDEFAULT = 7

    REDUSERDEFAULT = 8

    DEI = 9


    @staticmethod
    def _meta_info():
        from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
        return meta._meta_table['REDMechanism_Enum']


class SetC3plAccountFeatureType_Enum(Enum):
    """
    SetC3plAccountFeatureType_Enum

    Enums to indicate drop types for C3PL Account action.

    """

    QUEUEING = 0

    WRED = 1

    POLICE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
        return meta._meta_table['SetC3plAccountFeatureType_Enum']


class TrafficDirection_Enum(Enum):
    """
    TrafficDirection_Enum

    Enums to indicate whether the Policymap is for
    Input or Output direction.

    """

    INPUT = 1

    OUTPUT = 2


    @staticmethod
    def _meta_info():
        from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
        return meta._meta_table['TrafficDirection_Enum']


class TrafficShapingLimit_Enum(Enum):
    """
    TrafficShapingLimit_Enum

    The limit used by the traffic\-shaping feature.
    This value may be 'average' or 'peak',
    which indicates whether it is shaping by average
    rate or peak rate.

    """

    AVERAGE = 1

    PEAK = 2


    @staticmethod
    def _meta_info():
        from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
        return meta._meta_table['TrafficShapingLimit_Enum']


class SetFeatureType_Bits(FixedBitsDict):
    """
    SetFeatureType_Bits

    Bit\-wise representation of packet marking feature available
    today.  For historical reason, both packet marking and SET
    terms have been used across Cisco Class\-Based QOS, but they
    have the same meaning.  This feature is used to mark/set
    appropriate fields(e.g, dscp, precedence, mpls\-experimental
    \-topmost,l2CosInner) for applicable packets.
      ipDscp             Packet set/mark with DSCP bit
      ipPrecedence       Packet set/mark with Precedence bit
      qosGroupNumber     Packet set/mark with QosGroup bit
      frDeBit            Packet set/mark with FR\-DE  bit
      l2Cos              Packet set/mark with COS bit
      mplsExp            Packet set/mark with MPLS Experimental bit
      discardClass       Packet set/mark with discard class bit
      mplsExpTopMost     Packet set/mark with MPLS Experimental   
                         topmost bit             
      srpPriority        Packet set/mark with srp priority bit
      frFecnBecn         Packet set/mark with FECN bit
      ipDscpTunnel       Packet set/mark with DSCP tunnel bit
      ipPrecedenceTunnel Packet set/mark with Precedence tunnel bit
      l2CosInner         Packet set/mark with COS inner bit
      dei                Packet set/mark with DEI bit
      deiImposition      Packet set/mark with DEI Imposition bit
    Keys are:- dei , qosGroupNumber , frFecnBecn , ipDscpTunnel , l2CosInner , ipPrecedenceTunnel , deiImposition , discardClass , ipPrecedence , mplsExpTopMost , l2Cos , ipDscp , frDeBit , atmClpBit , mplsExp , srpPriority

    """

    def __init__(self):
        self._dictionary = { 
            'dei':False,
            'qosGroupNumber':False,
            'frFecnBecn':False,
            'ipDscpTunnel':False,
            'l2CosInner':False,
            'ipPrecedenceTunnel':False,
            'deiImposition':False,
            'discardClass':False,
            'ipPrecedence':False,
            'mplsExpTopMost':False,
            'l2Cos':False,
            'ipDscp':False,
            'frDeBit':False,
            'atmClpBit':False,
            'mplsExp':False,
            'srpPriority':False,
        }
        self._pos_map = { 
            'dei':14,
            'qosGroupNumber':2,
            'frFecnBecn':10,
            'ipDscpTunnel':11,
            'l2CosInner':13,
            'ipPrecedenceTunnel':12,
            'deiImposition':15,
            'discardClass':7,
            'ipPrecedence':1,
            'mplsExpTopMost':8,
            'l2Cos':5,
            'ipDscp':0,
            'frDeBit':3,
            'atmClpBit':4,
            'mplsExp':6,
            'srpPriority':9,
        }


class CISCOCLASSBASEDQOSMIB(object):
    """
    
    
    .. attribute:: cbqosatmpvcpolicytable
    
    	This table describes the policies that are attached to a ATM PVC
    	**type**\: :py:class:`CbQosATMPVCPolicyTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosATMPVCPolicyTable>`
    
    .. attribute:: cbqosc3placcountcfgtable
    
    	This table specifies C3pl Account Action configuration information
    	**type**\: :py:class:`CbQosC3plAccountCfgTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosC3plAccountCfgTable>`
    
    .. attribute:: cbqosc3placcountstatstable
    
    	This table specifies C3pl Account Action related statistics information
    	**type**\: :py:class:`CbQosC3plAccountStatsTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosC3plAccountStatsTable>`
    
    .. attribute:: cbqoscmcfgtable
    
    	This table specifies ClassMap configuration information
    	**type**\: :py:class:`CbQosCMCfgTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosCMCfgTable>`
    
    .. attribute:: cbqoscmstatstable
    
    	This table specifies ClassMap related Statistical information
    	**type**\: :py:class:`CbQosCMStatsTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosCMStatsTable>`
    
    .. attribute:: cbqosebcfgtable
    
    	This table specifies Estimate Bandwidth related configuration information
    	**type**\: :py:class:`CbQosEBCfgTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosEBCfgTable>`
    
    .. attribute:: cbqosebstatstable
    
    	This table specifies Estimate Bandwidth related statistical information
    	**type**\: :py:class:`CbQosEBStatsTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosEBStatsTable>`
    
    .. attribute:: cbqosframerelaypolicytable
    
    	This table describes the service polices that are attached to Frame Relay DLCIs
    	**type**\: :py:class:`CbQosFrameRelayPolicyTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosFrameRelayPolicyTable>`
    
    .. attribute:: cbqosinterfacepolicytable
    
    	This table describes the service polices that are attached to main and sub interfaces
    	**type**\: :py:class:`CbQosInterfacePolicyTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosInterfacePolicyTable>`
    
    .. attribute:: cbqosiphccfgtable
    
    	This table specifies IP Header Compression configuration information
    	**type**\: :py:class:`CbQosIPHCCfgTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosIPHCCfgTable>`
    
    .. attribute:: cbqosiphcstatstable
    
    	This table specifies IP Header Compression statistical information
    	**type**\: :py:class:`CbQosIPHCStatsTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosIPHCStatsTable>`
    
    .. attribute:: cbqosmatchstmtcfgtable
    
    	This table specifies ClassMap configuration information
    	**type**\: :py:class:`CbQosMatchStmtCfgTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosMatchStmtCfgTable>`
    
    .. attribute:: cbqosmatchstmtstatstable
    
    	This table specifies Match Statement related statistical information
    	**type**\: :py:class:`CbQosMatchStmtStatsTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosMatchStmtStatsTable>`
    
    .. attribute:: cbqosmeasureipslacfgtable
    
    	This table specifies configuration information for measure type IPSLA action. The measure action relates the policy class to a specific IPSLAs auto group. Configuration of measure action of type IPSLA results in automatic generation of IPSLAs synthetic test operations when the policy is attached to interface. The operations are created according to the characteristics specified and to the destinations specified in IPSLA auto group. The IPSLAs sythentic test operations measure network statistics such as latency, packet loss and jitter. This table is to be used only for retrieving the measure action configuration information
    	**type**\: :py:class:`CbQosMeasureIPSLACfgTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosMeasureIPSLACfgTable>`
    
    .. attribute:: cbqosobjectstable
    
    	This table specifies QoS objects (classmap, policymap, match statements, and actions) hierarchy. This table also  provide relationship between each PolicyIndex/ObjectsIndex  pair and the ConfigIndex. ConfigIndex is essential for  querying any configuration tables
    	**type**\: :py:class:`CbQosObjectsTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosObjectsTable>`
    
    .. attribute:: cbqospoliceactioncfgtable
    
    	This table specifies Police Action configuration information
    	**type**\: :py:class:`CbQosPoliceActionCfgTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosPoliceActionCfgTable>`
    
    .. attribute:: cbqospolicecfgtable
    
    	This table specifies Police Action configuration information
    	**type**\: :py:class:`CbQosPoliceCfgTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosPoliceCfgTable>`
    
    .. attribute:: cbqospolicecolorstatstable
    
    	This table specifies Police Action related Statistical information for two rate color aware marker
    	**type**\: :py:class:`CbQosPoliceColorStatsTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosPoliceColorStatsTable>`
    
    .. attribute:: cbqospolicestatstable
    
    	This table specifies Police Action related Statistical information
    	**type**\: :py:class:`CbQosPoliceStatsTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosPoliceStatsTable>`
    
    .. attribute:: cbqospolicymapcfgtable
    
    	This table specifies Policymap configuration information
    	**type**\: :py:class:`CbQosPolicyMapCfgTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosPolicyMapCfgTable>`
    
    .. attribute:: cbqosqueueingcfgtable
    
    	This table specifies Queueing Action configuration information
    	**type**\: :py:class:`CbQosQueueingCfgTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosQueueingCfgTable>`
    
    .. attribute:: cbqosqueueingclasscfgtable
    
    	This table specifies the configuration information for weighted queue limit action per IP precedence basis
    	**type**\: :py:class:`CbQosQueueingClassCfgTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosQueueingClassCfgTable>`
    
    .. attribute:: cbqosqueueingstatstable
    
    	This table specifies Queueing Action related Statistical information
    	**type**\: :py:class:`CbQosQueueingStatsTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosQueueingStatsTable>`
    
    .. attribute:: cbqosredcfgtable
    
    	This table specifies WRED Action configuration information
    	**type**\: :py:class:`CbQosREDCfgTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosREDCfgTable>`
    
    .. attribute:: cbqosredclasscfgtable
    
    	This table specifies WRED Action configuration information on a per IP precedence basis
    	**type**\: :py:class:`CbQosREDClassCfgTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosREDClassCfgTable>`
    
    .. attribute:: cbqosredclassstatstable
    
    	This table specifies per Precedence WRED Action related Statistical information
    	**type**\: :py:class:`CbQosREDClassStatsTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosREDClassStatsTable>`
    
    .. attribute:: cbqosservicepolicytable
    
    	This table describes the logical interfaces/media types and the policymap that are attached to it
    	**type**\: :py:class:`CbQosServicePolicyTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosServicePolicyTable>`
    
    .. attribute:: cbqossetcfgtable
    
    	This table specifies Packet Marking Action configuration information
    	**type**\: :py:class:`CbQosSetCfgTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosSetCfgTable>`
    
    .. attribute:: cbqossetstatstable
    
    	This table specifies packet marking statistical information
    	**type**\: :py:class:`CbQosSetStatsTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosSetStatsTable>`
    
    .. attribute:: cbqostablemapcfgtable
    
    	This table specifies Table Map basic configuration information
    	**type**\: :py:class:`CbQosTableMapCfgTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosTableMapCfgTable>`
    
    .. attribute:: cbqostablemapsetcfgtable
    
    	This table specifies enhanced packet marking configuration using a pre\-defined tablemap
    	**type**\: :py:class:`CbQosTableMapSetCfgTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosTableMapSetCfgTable>`
    
    .. attribute:: cbqostablemapvaluecfgtable
    
    	This table specifies the from\-value to to\-value conversion pairs for a tablemap
    	**type**\: :py:class:`CbQosTableMapValueCfgTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosTableMapValueCfgTable>`
    
    .. attribute:: cbqostscfgtable
    
    	This table specifies traffic\-shaping Action configuration information
    	**type**\: :py:class:`CbQosTSCfgTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosTSCfgTable>`
    
    .. attribute:: cbqostsstatstable
    
    	This table specifies traffic\-shaping Action related Statistical information
    	**type**\: :py:class:`CbQosTSStatsTable <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosTSStatsTable>`
    
    

    """

    _prefix = 'cisco-class'
    _revision = '2014-01-24'

    def __init__(self):
        self.cbqosatmpvcpolicytable = CISCOCLASSBASEDQOSMIB.CbQosATMPVCPolicyTable()
        self.cbqosatmpvcpolicytable.parent = self
        self.cbqosc3placcountcfgtable = CISCOCLASSBASEDQOSMIB.CbQosC3plAccountCfgTable()
        self.cbqosc3placcountcfgtable.parent = self
        self.cbqosc3placcountstatstable = CISCOCLASSBASEDQOSMIB.CbQosC3plAccountStatsTable()
        self.cbqosc3placcountstatstable.parent = self
        self.cbqoscmcfgtable = CISCOCLASSBASEDQOSMIB.CbQosCMCfgTable()
        self.cbqoscmcfgtable.parent = self
        self.cbqoscmstatstable = CISCOCLASSBASEDQOSMIB.CbQosCMStatsTable()
        self.cbqoscmstatstable.parent = self
        self.cbqosebcfgtable = CISCOCLASSBASEDQOSMIB.CbQosEBCfgTable()
        self.cbqosebcfgtable.parent = self
        self.cbqosebstatstable = CISCOCLASSBASEDQOSMIB.CbQosEBStatsTable()
        self.cbqosebstatstable.parent = self
        self.cbqosframerelaypolicytable = CISCOCLASSBASEDQOSMIB.CbQosFrameRelayPolicyTable()
        self.cbqosframerelaypolicytable.parent = self
        self.cbqosinterfacepolicytable = CISCOCLASSBASEDQOSMIB.CbQosInterfacePolicyTable()
        self.cbqosinterfacepolicytable.parent = self
        self.cbqosiphccfgtable = CISCOCLASSBASEDQOSMIB.CbQosIPHCCfgTable()
        self.cbqosiphccfgtable.parent = self
        self.cbqosiphcstatstable = CISCOCLASSBASEDQOSMIB.CbQosIPHCStatsTable()
        self.cbqosiphcstatstable.parent = self
        self.cbqosmatchstmtcfgtable = CISCOCLASSBASEDQOSMIB.CbQosMatchStmtCfgTable()
        self.cbqosmatchstmtcfgtable.parent = self
        self.cbqosmatchstmtstatstable = CISCOCLASSBASEDQOSMIB.CbQosMatchStmtStatsTable()
        self.cbqosmatchstmtstatstable.parent = self
        self.cbqosmeasureipslacfgtable = CISCOCLASSBASEDQOSMIB.CbQosMeasureIPSLACfgTable()
        self.cbqosmeasureipslacfgtable.parent = self
        self.cbqosobjectstable = CISCOCLASSBASEDQOSMIB.CbQosObjectsTable()
        self.cbqosobjectstable.parent = self
        self.cbqospoliceactioncfgtable = CISCOCLASSBASEDQOSMIB.CbQosPoliceActionCfgTable()
        self.cbqospoliceactioncfgtable.parent = self
        self.cbqospolicecfgtable = CISCOCLASSBASEDQOSMIB.CbQosPoliceCfgTable()
        self.cbqospolicecfgtable.parent = self
        self.cbqospolicecolorstatstable = CISCOCLASSBASEDQOSMIB.CbQosPoliceColorStatsTable()
        self.cbqospolicecolorstatstable.parent = self
        self.cbqospolicestatstable = CISCOCLASSBASEDQOSMIB.CbQosPoliceStatsTable()
        self.cbqospolicestatstable.parent = self
        self.cbqospolicymapcfgtable = CISCOCLASSBASEDQOSMIB.CbQosPolicyMapCfgTable()
        self.cbqospolicymapcfgtable.parent = self
        self.cbqosqueueingcfgtable = CISCOCLASSBASEDQOSMIB.CbQosQueueingCfgTable()
        self.cbqosqueueingcfgtable.parent = self
        self.cbqosqueueingclasscfgtable = CISCOCLASSBASEDQOSMIB.CbQosQueueingClassCfgTable()
        self.cbqosqueueingclasscfgtable.parent = self
        self.cbqosqueueingstatstable = CISCOCLASSBASEDQOSMIB.CbQosQueueingStatsTable()
        self.cbqosqueueingstatstable.parent = self
        self.cbqosredcfgtable = CISCOCLASSBASEDQOSMIB.CbQosREDCfgTable()
        self.cbqosredcfgtable.parent = self
        self.cbqosredclasscfgtable = CISCOCLASSBASEDQOSMIB.CbQosREDClassCfgTable()
        self.cbqosredclasscfgtable.parent = self
        self.cbqosredclassstatstable = CISCOCLASSBASEDQOSMIB.CbQosREDClassStatsTable()
        self.cbqosredclassstatstable.parent = self
        self.cbqosservicepolicytable = CISCOCLASSBASEDQOSMIB.CbQosServicePolicyTable()
        self.cbqosservicepolicytable.parent = self
        self.cbqossetcfgtable = CISCOCLASSBASEDQOSMIB.CbQosSetCfgTable()
        self.cbqossetcfgtable.parent = self
        self.cbqossetstatstable = CISCOCLASSBASEDQOSMIB.CbQosSetStatsTable()
        self.cbqossetstatstable.parent = self
        self.cbqostablemapcfgtable = CISCOCLASSBASEDQOSMIB.CbQosTableMapCfgTable()
        self.cbqostablemapcfgtable.parent = self
        self.cbqostablemapsetcfgtable = CISCOCLASSBASEDQOSMIB.CbQosTableMapSetCfgTable()
        self.cbqostablemapsetcfgtable.parent = self
        self.cbqostablemapvaluecfgtable = CISCOCLASSBASEDQOSMIB.CbQosTableMapValueCfgTable()
        self.cbqostablemapvaluecfgtable.parent = self
        self.cbqostscfgtable = CISCOCLASSBASEDQOSMIB.CbQosTSCfgTable()
        self.cbqostscfgtable.parent = self
        self.cbqostsstatstable = CISCOCLASSBASEDQOSMIB.CbQosTSStatsTable()
        self.cbqostsstatstable.parent = self


    class CbQosATMPVCPolicyTable(object):
        """
        This table describes the policies that are attached to a
        ATM PVC.
        
        .. attribute:: cbqosatmpvcpolicyentry
        
        	Using ifIndex, VPI, VCI, and Direction, each unique index combination translates to a service policy that  is attached to a ATM VC, for particular traffic direction
        	**type**\: list of :py:class:`CbQosATMPVCPolicyEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosATMPVCPolicyTable.CbQosATMPVCPolicyEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqosatmpvcpolicyentry = YList()
            self.cbqosatmpvcpolicyentry.parent = self
            self.cbqosatmpvcpolicyentry.name = 'cbqosatmpvcpolicyentry'


        class CbQosATMPVCPolicyEntry(object):
            """
            Using ifIndex, VPI, VCI, and Direction, each unique
            index combination translates to a service policy that 
            is attached to a ATM VC, for particular traffic direction.
            
            .. attribute:: cbqosatmvci
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cbqosatmvpi
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: cbqospolicydirection
            
            	
            	**type**\: :py:class:`TrafficDirection_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.TrafficDirection_Enum>`
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cbqosatmpolicyindex
            
            	An arbitrary (system\-assigned) index for all Service Policies.  This is identical to cbQosPolicyIndex
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosatmvci = None
                self.cbqosatmvpi = None
                self.cbqospolicydirection = None
                self.ifindex = None
                self.cbqosatmpolicyindex = None

            @property
            def _common_path(self):
                if self.cbqosatmvci is None:
                    raise YPYDataValidationError('Key property cbqosatmvci is None')
                if self.cbqosatmvpi is None:
                    raise YPYDataValidationError('Key property cbqosatmvpi is None')
                if self.cbqospolicydirection is None:
                    raise YPYDataValidationError('Key property cbqospolicydirection is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosATMPVCPolicyTable/CISCO-CLASS-BASED-QOS-MIB:cbQosATMPVCPolicyEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosAtmVCI = ' + str(self.cbqosatmvci) + '][CISCO-CLASS-BASED-QOS-MIB:cbQosAtmVPI = ' + str(self.cbqosatmvpi) + '][CISCO-CLASS-BASED-QOS-MIB:cbQosPolicyDirection = ' + str(self.cbqospolicydirection) + '][CISCO-CLASS-BASED-QOS-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosatmvci is not None:
                    return True

                if self.cbqosatmvpi is not None:
                    return True

                if self.cbqospolicydirection is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.cbqosatmpolicyindex is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosATMPVCPolicyTable.CbQosATMPVCPolicyEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosATMPVCPolicyTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqosatmpvcpolicyentry is not None:
                for child_ref in self.cbqosatmpvcpolicyentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosATMPVCPolicyTable']['meta_info']


    class CbQosC3plAccountCfgTable(object):
        """
        This table specifies C3pl Account Action configuration
        information
        
        .. attribute:: cbqosc3placcountcfgentry
        
        	Each entry in this table describes configuration information about a c3pl account action. The information includes\: feature type.  This table contains configuration information only, no statistics associated with it. Therefore, it is indexed by the cbQosConfigIndex of each C3pl Account Action
        	**type**\: list of :py:class:`CbQosC3plAccountCfgEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosC3plAccountCfgTable.CbQosC3plAccountCfgEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqosc3placcountcfgentry = YList()
            self.cbqosc3placcountcfgentry.parent = self
            self.cbqosc3placcountcfgentry.name = 'cbqosc3placcountcfgentry'


        class CbQosC3plAccountCfgEntry(object):
            """
            Each entry in this table describes configuration
            information about a c3pl account action. The information
            includes\: feature type.
            
            This table contains configuration information only,
            no statistics associated with it. Therefore, it is indexed
            by the cbQosConfigIndex of each C3pl Account Action.
            
            .. attribute:: cbqosconfigindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosc3placcountfeaturetype
            
            	The feature type is used to indicated different drop statistics
            	**type**\: :py:class:`SetC3plAccountFeatureType_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.SetC3plAccountFeatureType_Enum>`
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosconfigindex = None
                self.cbqosc3placcountfeaturetype = None

            @property
            def _common_path(self):
                if self.cbqosconfigindex is None:
                    raise YPYDataValidationError('Key property cbqosconfigindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosC3plAccountCfgTable/CISCO-CLASS-BASED-QOS-MIB:cbQosC3plAccountCfgEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosConfigIndex = ' + str(self.cbqosconfigindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosconfigindex is not None:
                    return True

                if self.cbqosc3placcountfeaturetype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosC3plAccountCfgTable.CbQosC3plAccountCfgEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosC3plAccountCfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqosc3placcountcfgentry is not None:
                for child_ref in self.cbqosc3placcountcfgentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosC3plAccountCfgTable']['meta_info']


    class CbQosC3plAccountStatsTable(object):
        """
        This table specifies C3pl Account Action related
        statistics information.
        
        .. attribute:: cbqosc3placcountstatsentry
        
        	Each entry in this table describes the statistical information about C3pl Account Action. Account action specific information you can find in this table are \: queueing drop pkt/byte counters, wred drop pkt/byte counters, police pkt/byte counters.  This table contains statistical information only, no configuration information associated with it. Therefore, it is indexed by the instance specific IDs, such as cbQosPolicyIndex, cbQosObjectsIndex, and cbQosC3plAccountFeatureType
        	**type**\: list of :py:class:`CbQosC3plAccountStatsEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosC3plAccountStatsTable.CbQosC3plAccountStatsEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqosc3placcountstatsentry = YList()
            self.cbqosc3placcountstatsentry.parent = self
            self.cbqosc3placcountstatsentry.name = 'cbqosc3placcountstatsentry'


        class CbQosC3plAccountStatsEntry(object):
            """
            Each entry in this table describes the statistical
            information about C3pl Account Action. Account action
            specific information you can find in this table are \:
            queueing drop pkt/byte counters, wred drop pkt/byte
            counters, police pkt/byte counters.
            
            This table contains statistical information only,
            no configuration information associated with it.
            Therefore, it is indexed by the instance specific IDs,
            such as cbQosPolicyIndex, cbQosObjectsIndex, and
            cbQosC3plAccountFeatureType.
            
            .. attribute:: cbqosc3placcountfeaturetype
            
            	
            	**type**\: :py:class:`SetC3plAccountFeatureType_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.SetC3plAccountFeatureType_Enum>`
            
            .. attribute:: cbqosobjectsindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospolicyindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosc3placcountdropbyte
            
            	The lower 32 bits count of bytes dropped when the number of packets in the associated queue was greater than the minimum threshold and less than the maximum threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosc3placcountdropbyte64
            
            	The 64 bits count of bytes dropped when the number of packets in the associated queue was greater than the minimum threshold and less than the maximum threshold
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosc3placcountdropbyteoverflow
            
            	The upper 32 bits count of bytes dropped when the number of packets in the associated queue was greater than the minimum threshold and less than the maximum threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosc3placcountdroppkt
            
            	The lower 32 bits count of packets dropped when the number of packets in the associated queue was greater than the minimum threshold and less than the maximum threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosc3placcountdroppkt64
            
            	The 64 bits count of packets dropped when the number of packets in the associated queue was greater than the minimum threshold and less than the maximum threshold
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosc3placcountdroppktoverflow
            
            	The upper 32 bits count of packets dropped when the number of packets in the associated queue was greater than the minimum threshold and less than the maximum threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosc3placcounttaildropbyte
            
            	The lower 32 bits count of bytes dropped when the number of packets in the associated queue was greater than the maximum threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosc3placcounttaildropbyte64
            
            	The 64 bits count of bytes dropped when the number of packets in the associated queue was greater than the maximum threshold
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosc3placcounttaildropbyteoverflow
            
            	The upper 32 bits count of bytes dropped when the number of packets in the associated queue was greater than the maximum threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosc3placcounttaildroppkt
            
            	The lower 32 bits count of packets dropped when the number of packets in the associated queue was greater than the maximum threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosc3placcounttaildroppkt64
            
            	The 64 bits count of packets dropped when the number of packets in the associated queue was greater than the maximum threshold
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosc3placcounttaildroppktoverflow
            
            	The upper 32 bits count of packets dropped when the number of packets in the associated queue was greater than the maximum threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosc3placcountfeaturetype = None
                self.cbqosobjectsindex = None
                self.cbqospolicyindex = None
                self.cbqosc3placcountdropbyte = None
                self.cbqosc3placcountdropbyte64 = None
                self.cbqosc3placcountdropbyteoverflow = None
                self.cbqosc3placcountdroppkt = None
                self.cbqosc3placcountdroppkt64 = None
                self.cbqosc3placcountdroppktoverflow = None
                self.cbqosc3placcounttaildropbyte = None
                self.cbqosc3placcounttaildropbyte64 = None
                self.cbqosc3placcounttaildropbyteoverflow = None
                self.cbqosc3placcounttaildroppkt = None
                self.cbqosc3placcounttaildroppkt64 = None
                self.cbqosc3placcounttaildroppktoverflow = None

            @property
            def _common_path(self):
                if self.cbqosc3placcountfeaturetype is None:
                    raise YPYDataValidationError('Key property cbqosc3placcountfeaturetype is None')
                if self.cbqosobjectsindex is None:
                    raise YPYDataValidationError('Key property cbqosobjectsindex is None')
                if self.cbqospolicyindex is None:
                    raise YPYDataValidationError('Key property cbqospolicyindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosC3plAccountStatsTable/CISCO-CLASS-BASED-QOS-MIB:cbQosC3plAccountStatsEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosC3plAccountFeatureType = ' + str(self.cbqosc3placcountfeaturetype) + '][CISCO-CLASS-BASED-QOS-MIB:cbQosObjectsIndex = ' + str(self.cbqosobjectsindex) + '][CISCO-CLASS-BASED-QOS-MIB:cbQosPolicyIndex = ' + str(self.cbqospolicyindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosc3placcountfeaturetype is not None:
                    return True

                if self.cbqosobjectsindex is not None:
                    return True

                if self.cbqospolicyindex is not None:
                    return True

                if self.cbqosc3placcountdropbyte is not None:
                    return True

                if self.cbqosc3placcountdropbyte64 is not None:
                    return True

                if self.cbqosc3placcountdropbyteoverflow is not None:
                    return True

                if self.cbqosc3placcountdroppkt is not None:
                    return True

                if self.cbqosc3placcountdroppkt64 is not None:
                    return True

                if self.cbqosc3placcountdroppktoverflow is not None:
                    return True

                if self.cbqosc3placcounttaildropbyte is not None:
                    return True

                if self.cbqosc3placcounttaildropbyte64 is not None:
                    return True

                if self.cbqosc3placcounttaildropbyteoverflow is not None:
                    return True

                if self.cbqosc3placcounttaildroppkt is not None:
                    return True

                if self.cbqosc3placcounttaildroppkt64 is not None:
                    return True

                if self.cbqosc3placcounttaildroppktoverflow is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosC3plAccountStatsTable.CbQosC3plAccountStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosC3plAccountStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqosc3placcountstatsentry is not None:
                for child_ref in self.cbqosc3placcountstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosC3plAccountStatsTable']['meta_info']


    class CbQosCMCfgTable(object):
        """
        This table specifies ClassMap configuration information
        
        .. attribute:: cbqoscmcfgentry
        
        	Each entry in this table describes configuration information about a classmap. The information includes\: Name, and it's description and whether it is a Match\-All or Match\-Any class. This table contains configuration information only, no statistics associated with it. Therefore, it is indexed by the cbQosConfigIndex of each ClassMap
        	**type**\: list of :py:class:`CbQosCMCfgEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosCMCfgTable.CbQosCMCfgEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqoscmcfgentry = YList()
            self.cbqoscmcfgentry.parent = self
            self.cbqoscmcfgentry.name = 'cbqoscmcfgentry'


        class CbQosCMCfgEntry(object):
            """
            Each entry in this table describes configuration information
            about a classmap. The information includes\: Name, and it's
            description and whether it is a Match\-All or Match\-Any
            class. This table contains configuration information only,
            no statistics associated with it. Therefore, it is indexed
            by the cbQosConfigIndex of each ClassMap.
            
            .. attribute:: cbqosconfigindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqoscmdesc
            
            	Description of the Classmap
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cbqoscminfo
            
            	Match all vs Match any in a given class
            	**type**\: :py:class:`QosClassInfo_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.QosClassInfo_Enum>`
            
            .. attribute:: cbqoscmname
            
            	Name of the Classmap
            	**type**\: str
            
            	**range:** 0..255
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosconfigindex = None
                self.cbqoscmdesc = None
                self.cbqoscminfo = None
                self.cbqoscmname = None

            @property
            def _common_path(self):
                if self.cbqosconfigindex is None:
                    raise YPYDataValidationError('Key property cbqosconfigindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosCMCfgTable/CISCO-CLASS-BASED-QOS-MIB:cbQosCMCfgEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosConfigIndex = ' + str(self.cbqosconfigindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosconfigindex is not None:
                    return True

                if self.cbqoscmdesc is not None:
                    return True

                if self.cbqoscminfo is not None:
                    return True

                if self.cbqoscmname is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosCMCfgTable.CbQosCMCfgEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosCMCfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqoscmcfgentry is not None:
                for child_ref in self.cbqoscmcfgentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosCMCfgTable']['meta_info']


    class CbQosCMStatsTable(object):
        """
        This table specifies ClassMap related Statistical
        information.
        
        .. attribute:: cbqoscmstatsentry
        
        	Each entry in this table describes the statistical information about ClassMap. ClassMap specific information you can find in this table are \: pre/post policy pkt/byte counts, bit rates, drop pkt/bytes and no buffer drops.  This table contains statistical information only, no configuration information associated with it. Therefore,  it is indexed by the instance specific IDs, such as  cbQosPolicyIndex and cbQosObjectsIndex
        	**type**\: list of :py:class:`CbQosCMStatsEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosCMStatsTable.CbQosCMStatsEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqoscmstatsentry = YList()
            self.cbqoscmstatsentry.parent = self
            self.cbqoscmstatsentry.name = 'cbqoscmstatsentry'


        class CbQosCMStatsEntry(object):
            """
            Each entry in this table describes the statistical
            information about ClassMap. ClassMap specific information
            you can find in this table are \: pre/post policy pkt/byte
            counts, bit rates, drop pkt/bytes and no buffer drops.
            
            This table contains statistical information only,
            no configuration information associated with it. Therefore, 
            it is indexed by the instance specific IDs, such as 
            cbQosPolicyIndex and cbQosObjectsIndex.
            
            .. attribute:: cbqosobjectsindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospolicyindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqoscmdropbitrate
            
            	The bit rate of the drops per class as the result of all features that can produce drops  (e.g., police, random detect, etc.)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqoscmdropbitrate64
            
            	The bit rate of the drops per class as the result of all features that can produce drops  (e.g., police, random detect, etc.). This object is a 64\-bit version of cbQosCMDropBitRate
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqoscmdropbyte
            
            	The lower 32 bits counter of dropped bytes per class as the result of all features that can produce drops  (e.g., police, random detect, etc.)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqoscmdropbyte64
            
            	The 64 bits counter of dropped bytes per class as the result of all features that can produce drops   (e.g., police, random detect, etc.)
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqoscmdropbyteoverflow
            
            	The upper 32 bits counter of dropped bytes per class as the result of all features that can produce drops  (e.g., police, random detect, etc.)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqoscmdroppkt
            
            	The lower 32 bits counter of dropped pkts per class as the result of all features that can produce drops  (e.g., police, random detect, etc.)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqoscmdroppkt64
            
            	The 64 bits counter of dropped pkts per class as the result of all features that can produce drops   (e.g., police, random detect, etc.)
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqoscmdroppktoverflow
            
            	The upper 32 bits counter of dropped pkts per class as the result of all features that can produce drops  (e.g., police, random detect, etc.)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqoscmfragmentbyte
            
            	The lower 32 bits counter for aggregate fragment bytes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqoscmfragmentbyte64
            
            	The 64 bits counter for aggregate fragment bytes
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqoscmfragmentbyteoverflow
            
            	The upper 32 bits counter for aggregate fragment bytes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqoscmfragmentpkt
            
            	The lower 32 bits counter for aggregate fragment pkts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqoscmfragmentpkt64
            
            	The 64 bits counter for aggregate fragment pkts
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqoscmfragmentpktoverflow
            
            	The upper 32 bits counter for aggregate fragment pkts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqoscmnobufdroppkt
            
            	The lower 32 bits drop packet count which occured due to a lack of SRAM buffers during output processing on  an interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqoscmnobufdroppkt64
            
            	The 64 bits drop packet count which occured due to a lack of SRAM buffers during output processing on an  interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqoscmnobufdroppktoverflow
            
            	The upper 32 bits drop packet count which occured due to a lack of SRAM buffers during output processing  on an interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqoscmpostpolicybitrate
            
            	The bit rate of the traffic after executing QoS policies
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqoscmpostpolicybitrate64
            
            	The bit rate of the traffic after executing QoS policies. This object is a 64\-bit version of cbQosCMPostPolicyBitRate
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqoscmpostpolicybyte
            
            	The lower 32 bits count of outbound octets after executing QoS policies
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqoscmpostpolicybyte64
            
            	The 64 bits count of outbound octets after executing QoS policies
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqoscmpostpolicybyteoverflow
            
            	The upper 32 bits count of outbound octets after executing QoS policies
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqoscmprepolicybitrate
            
            	The bit rate of the traffic prior to executing any QoS policies
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqoscmprepolicybitrate64
            
            	The bit rate of the traffic prior to executing any QoS policies.This object is a 64\-bit version of cbQosCMPrePolicyBitRate
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqoscmprepolicybyte
            
            	The lower 32 bits count of inbound octets prior to executing any QoS policies
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqoscmprepolicybyte64
            
            	The 64 bits count of inbound octets prior to executing any QoS policies
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqoscmprepolicybyteoverflow
            
            	The upper 32 bits count of inbound octets prior to executing any QoS policies
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqoscmprepolicypkt
            
            	The lower 32 bits count of inbound packets prior to executing any QoS policies
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqoscmprepolicypkt64
            
            	The 64 bits count of inbound packets prior to executing any QoS policies
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqoscmprepolicypktoverflow
            
            	The upper 32 bits count of inbound packets prior to executing any QoS policies
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosobjectsindex = None
                self.cbqospolicyindex = None
                self.cbqoscmdropbitrate = None
                self.cbqoscmdropbitrate64 = None
                self.cbqoscmdropbyte = None
                self.cbqoscmdropbyte64 = None
                self.cbqoscmdropbyteoverflow = None
                self.cbqoscmdroppkt = None
                self.cbqoscmdroppkt64 = None
                self.cbqoscmdroppktoverflow = None
                self.cbqoscmfragmentbyte = None
                self.cbqoscmfragmentbyte64 = None
                self.cbqoscmfragmentbyteoverflow = None
                self.cbqoscmfragmentpkt = None
                self.cbqoscmfragmentpkt64 = None
                self.cbqoscmfragmentpktoverflow = None
                self.cbqoscmnobufdroppkt = None
                self.cbqoscmnobufdroppkt64 = None
                self.cbqoscmnobufdroppktoverflow = None
                self.cbqoscmpostpolicybitrate = None
                self.cbqoscmpostpolicybitrate64 = None
                self.cbqoscmpostpolicybyte = None
                self.cbqoscmpostpolicybyte64 = None
                self.cbqoscmpostpolicybyteoverflow = None
                self.cbqoscmprepolicybitrate = None
                self.cbqoscmprepolicybitrate64 = None
                self.cbqoscmprepolicybyte = None
                self.cbqoscmprepolicybyte64 = None
                self.cbqoscmprepolicybyteoverflow = None
                self.cbqoscmprepolicypkt = None
                self.cbqoscmprepolicypkt64 = None
                self.cbqoscmprepolicypktoverflow = None

            @property
            def _common_path(self):
                if self.cbqosobjectsindex is None:
                    raise YPYDataValidationError('Key property cbqosobjectsindex is None')
                if self.cbqospolicyindex is None:
                    raise YPYDataValidationError('Key property cbqospolicyindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosCMStatsTable/CISCO-CLASS-BASED-QOS-MIB:cbQosCMStatsEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosObjectsIndex = ' + str(self.cbqosobjectsindex) + '][CISCO-CLASS-BASED-QOS-MIB:cbQosPolicyIndex = ' + str(self.cbqospolicyindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosobjectsindex is not None:
                    return True

                if self.cbqospolicyindex is not None:
                    return True

                if self.cbqoscmdropbitrate is not None:
                    return True

                if self.cbqoscmdropbitrate64 is not None:
                    return True

                if self.cbqoscmdropbyte is not None:
                    return True

                if self.cbqoscmdropbyte64 is not None:
                    return True

                if self.cbqoscmdropbyteoverflow is not None:
                    return True

                if self.cbqoscmdroppkt is not None:
                    return True

                if self.cbqoscmdroppkt64 is not None:
                    return True

                if self.cbqoscmdroppktoverflow is not None:
                    return True

                if self.cbqoscmfragmentbyte is not None:
                    return True

                if self.cbqoscmfragmentbyte64 is not None:
                    return True

                if self.cbqoscmfragmentbyteoverflow is not None:
                    return True

                if self.cbqoscmfragmentpkt is not None:
                    return True

                if self.cbqoscmfragmentpkt64 is not None:
                    return True

                if self.cbqoscmfragmentpktoverflow is not None:
                    return True

                if self.cbqoscmnobufdroppkt is not None:
                    return True

                if self.cbqoscmnobufdroppkt64 is not None:
                    return True

                if self.cbqoscmnobufdroppktoverflow is not None:
                    return True

                if self.cbqoscmpostpolicybitrate is not None:
                    return True

                if self.cbqoscmpostpolicybitrate64 is not None:
                    return True

                if self.cbqoscmpostpolicybyte is not None:
                    return True

                if self.cbqoscmpostpolicybyte64 is not None:
                    return True

                if self.cbqoscmpostpolicybyteoverflow is not None:
                    return True

                if self.cbqoscmprepolicybitrate is not None:
                    return True

                if self.cbqoscmprepolicybitrate64 is not None:
                    return True

                if self.cbqoscmprepolicybyte is not None:
                    return True

                if self.cbqoscmprepolicybyte64 is not None:
                    return True

                if self.cbqoscmprepolicybyteoverflow is not None:
                    return True

                if self.cbqoscmprepolicypkt is not None:
                    return True

                if self.cbqoscmprepolicypkt64 is not None:
                    return True

                if self.cbqoscmprepolicypktoverflow is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosCMStatsTable.CbQosCMStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosCMStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqoscmstatsentry is not None:
                for child_ref in self.cbqoscmstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosCMStatsTable']['meta_info']


    class CbQosEBCfgTable(object):
        """
        This table specifies Estimate Bandwidth related
        configuration information.
        
        .. attribute:: cbqosebcfgentry
        
        	Each entry in this table describes configuration information about Estimate Bandwidth. It includes\:  drop target, delay target and delay threshold.  This table contains configuration information only. It is indexed by the cbQosConfigIndex
        	**type**\: list of :py:class:`CbQosEBCfgEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosEBCfgTable.CbQosEBCfgEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqosebcfgentry = YList()
            self.cbqosebcfgentry.parent = self
            self.cbqosebcfgentry.name = 'cbqosebcfgentry'


        class CbQosEBCfgEntry(object):
            """
            Each entry in this table describes configuration
            information about Estimate Bandwidth. It includes\: 
            drop target, delay target and delay threshold.
            
            This table contains configuration information only.
            It is indexed by the cbQosConfigIndex.
            
            .. attribute:: cbqosconfigindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosebcfgdelaytarget
            
            	One\-in\-Number target indicating that no more than one packet in (this) number will exceed the delay  threshold specified by cbQosEBCfgDelayThreshold
            	**type**\: int
            
            	**range:** 50..1000000
            
            .. attribute:: cbqosebcfgdelaythreshold
            
            	The time in milliseconds for the delay threshold
            	**type**\: int
            
            	**range:** 16..1000
            
            .. attribute:: cbqosebcfgdroptarget
            
            	One\-in\-Number target indicating that no more than one packet in (this) number will be dropped
            	**type**\: int
            
            	**range:** 50..1000000
            
            .. attribute:: cbqosebcfgmechanism
            
            	Bandwidth estimate algorithm type
            	**type**\: :py:class:`CbQosEBType_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CbQosEBType_Enum>`
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosconfigindex = None
                self.cbqosebcfgdelaytarget = None
                self.cbqosebcfgdelaythreshold = None
                self.cbqosebcfgdroptarget = None
                self.cbqosebcfgmechanism = None

            @property
            def _common_path(self):
                if self.cbqosconfigindex is None:
                    raise YPYDataValidationError('Key property cbqosconfigindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosEBCfgTable/CISCO-CLASS-BASED-QOS-MIB:cbQosEBCfgEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosConfigIndex = ' + str(self.cbqosconfigindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosconfigindex is not None:
                    return True

                if self.cbqosebcfgdelaytarget is not None:
                    return True

                if self.cbqosebcfgdelaythreshold is not None:
                    return True

                if self.cbqosebcfgdroptarget is not None:
                    return True

                if self.cbqosebcfgmechanism is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosEBCfgTable.CbQosEBCfgEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosEBCfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqosebcfgentry is not None:
                for child_ref in self.cbqosebcfgentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosEBCfgTable']['meta_info']


    class CbQosEBStatsTable(object):
        """
        This table specifies Estimate Bandwidth related
        statistical information.
        
        .. attribute:: cbqosebstatsentry
        
        	Each entry in this table describes Estimate Bandwidth related statistical information
        	**type**\: list of :py:class:`CbQosEBStatsEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosEBStatsTable.CbQosEBStatsEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqosebstatsentry = YList()
            self.cbqosebstatsentry.parent = self
            self.cbqosebstatsentry.name = 'cbqosebstatsentry'


        class CbQosEBStatsEntry(object):
            """
            Each entry in this table describes Estimate Bandwidth
            related statistical information.
            
            .. attribute:: cbqosobjectsindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospolicyindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosebstatscorvilctd
            
            	The Corvil CTD value defined by CbQosEBCtd
            	**type**\: str
            
            .. attribute:: cbqosebstatscorvilebstatus
            
            	Boolean to indicate if Corvil EB is ready. true  \- Bandwidth estimate is available. false \- Bandwidth estimate is not available
            	**type**\: bool
            
            .. attribute:: cbqosebstatscorvilebvalue
            
            	The current Corvil EB bandwidth value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosobjectsindex = None
                self.cbqospolicyindex = None
                self.cbqosebstatscorvilctd = None
                self.cbqosebstatscorvilebstatus = None
                self.cbqosebstatscorvilebvalue = None

            @property
            def _common_path(self):
                if self.cbqosobjectsindex is None:
                    raise YPYDataValidationError('Key property cbqosobjectsindex is None')
                if self.cbqospolicyindex is None:
                    raise YPYDataValidationError('Key property cbqospolicyindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosEBStatsTable/CISCO-CLASS-BASED-QOS-MIB:cbQosEBStatsEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosObjectsIndex = ' + str(self.cbqosobjectsindex) + '][CISCO-CLASS-BASED-QOS-MIB:cbQosPolicyIndex = ' + str(self.cbqospolicyindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosobjectsindex is not None:
                    return True

                if self.cbqospolicyindex is not None:
                    return True

                if self.cbqosebstatscorvilctd is not None:
                    return True

                if self.cbqosebstatscorvilebstatus is not None:
                    return True

                if self.cbqosebstatscorvilebvalue is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosEBStatsTable.CbQosEBStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosEBStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqosebstatsentry is not None:
                for child_ref in self.cbqosebstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosEBStatsTable']['meta_info']


    class CbQosFrameRelayPolicyTable(object):
        """
        This table describes the service polices that are
        attached to Frame Relay DLCIs.
        
        .. attribute:: cbqosframerelaypolicyentry
        
        	Using ifIndex, FR DLCI, and Direction, each unique index combination translates to a service policy that  is attached to a FR DLCI, for particular traffic direction
        	**type**\: list of :py:class:`CbQosFrameRelayPolicyEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosFrameRelayPolicyTable.CbQosFrameRelayPolicyEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqosframerelaypolicyentry = YList()
            self.cbqosframerelaypolicyentry.parent = self
            self.cbqosframerelaypolicyentry.name = 'cbqosframerelaypolicyentry'


        class CbQosFrameRelayPolicyEntry(object):
            """
            Using ifIndex, FR DLCI, and Direction, each unique
            index combination translates to a service policy that 
            is attached to a FR DLCI, for particular traffic direction.
            
            .. attribute:: cbqosfrdlci
            
            	
            	**type**\: int
            
            	**range:** 0..1023
            
            .. attribute:: cbqospolicydirection
            
            	
            	**type**\: :py:class:`TrafficDirection_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.TrafficDirection_Enum>`
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cbqosfrpolicyindex
            
            	An arbitrary (system\-assigned) index for all Service Policies.  This is identical to cbQosPolicyIndex
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosfrdlci = None
                self.cbqospolicydirection = None
                self.ifindex = None
                self.cbqosfrpolicyindex = None

            @property
            def _common_path(self):
                if self.cbqosfrdlci is None:
                    raise YPYDataValidationError('Key property cbqosfrdlci is None')
                if self.cbqospolicydirection is None:
                    raise YPYDataValidationError('Key property cbqospolicydirection is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosFrameRelayPolicyTable/CISCO-CLASS-BASED-QOS-MIB:cbQosFrameRelayPolicyEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosFrDLCI = ' + str(self.cbqosfrdlci) + '][CISCO-CLASS-BASED-QOS-MIB:cbQosPolicyDirection = ' + str(self.cbqospolicydirection) + '][CISCO-CLASS-BASED-QOS-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosfrdlci is not None:
                    return True

                if self.cbqospolicydirection is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.cbqosfrpolicyindex is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosFrameRelayPolicyTable.CbQosFrameRelayPolicyEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosFrameRelayPolicyTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqosframerelaypolicyentry is not None:
                for child_ref in self.cbqosframerelaypolicyentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosFrameRelayPolicyTable']['meta_info']


    class CbQosIPHCCfgTable(object):
        """
        This table specifies IP Header Compression
        configuration information.
        
        .. attribute:: cbqosiphccfgentry
        
        	Each entry in this table describes configuration information about IP Header compression. This includes the compression option of UDP/RTP header, TCP header or both.  This table contains configuration information only, no statistics associated with it. Therefore, it is indexed by cbQosConfigIndex
        	**type**\: list of :py:class:`CbQosIPHCCfgEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosIPHCCfgTable.CbQosIPHCCfgEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqosiphccfgentry = YList()
            self.cbqosiphccfgentry.parent = self
            self.cbqosiphccfgentry.name = 'cbqosiphccfgentry'


        class CbQosIPHCCfgEntry(object):
            """
            Each entry in this table describes configuration
            information about IP Header compression. This
            includes the compression option of UDP/RTP header,
            TCP header or both.
            
            This table contains configuration information only,
            no statistics associated with it. Therefore, it is
            indexed by cbQosConfigIndex.
            
            .. attribute:: cbqosconfigindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosiphccfgenabled
            
            	Boolean to indicate if IPHC is enabled for policy class
            	**type**\: bool
            
            .. attribute:: cbqosiphccfgoption
            
            	The configured IP header compression option. The value is defined by IPHCOption
            	**type**\: :py:class:`IPHCOption_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.IPHCOption_Enum>`
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosconfigindex = None
                self.cbqosiphccfgenabled = None
                self.cbqosiphccfgoption = None

            @property
            def _common_path(self):
                if self.cbqosconfigindex is None:
                    raise YPYDataValidationError('Key property cbqosconfigindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosIPHCCfgTable/CISCO-CLASS-BASED-QOS-MIB:cbQosIPHCCfgEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosConfigIndex = ' + str(self.cbqosconfigindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosconfigindex is not None:
                    return True

                if self.cbqosiphccfgenabled is not None:
                    return True

                if self.cbqosiphccfgoption is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosIPHCCfgTable.CbQosIPHCCfgEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosIPHCCfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqosiphccfgentry is not None:
                for child_ref in self.cbqosiphccfgentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosIPHCCfgTable']['meta_info']


    class CbQosIPHCStatsTable(object):
        """
        This table specifies IP Header Compression
        statistical information.
        
        .. attribute:: cbqosiphcstatsentry
        
        	Each entry in this table describes statistical information about IP Header compression.  This table contains statistical information only, no configuration information associated with it. Therefore, it is indexed by the instance specific IDs, namely cbQosPolicyIndex and cbQosObjectsIndex
        	**type**\: list of :py:class:`CbQosIPHCStatsEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosIPHCStatsTable.CbQosIPHCStatsEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqosiphcstatsentry = YList()
            self.cbqosiphcstatsentry.parent = self
            self.cbqosiphcstatsentry.name = 'cbqosiphcstatsentry'


        class CbQosIPHCStatsEntry(object):
            """
            Each entry in this table describes statistical
            information about IP Header compression.
            
            This table contains statistical information only,
            no configuration information associated with it.
            Therefore, it is indexed by the instance specific IDs,
            namely cbQosPolicyIndex and cbQosObjectsIndex.
            
            .. attribute:: cbqosobjectsindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospolicyindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosiphcrtpcmprsoutpkt
            
            	The lower 32 bits count of outbound compressed UDP/RTP packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosiphcrtpcmprsoutpkt64
            
            	The 64 bits count of outbound compressed UDP/RTP packets
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosiphcrtpcmprsoutpktoverflow
            
            	The upper 32 bits count of outbound compressed UDP/RTP packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosiphcrtpfullhdrsentpkt
            
            	The lower 32 bits count of total full header UDP/RTP packets sent out
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosiphcrtpfullhdrsentpkt64
            
            	The 64 bits count of total fullheader UDP/RTP packets sent out
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosiphcrtpfullhdrsentpktoverflow
            
            	The upper 32 bits count of total full header UDP/RTP packets sent out
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosiphcrtpsavedbyte
            
            	The lower 32 bits count of UDP/RTP bytes that saved due to IPHC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosiphcrtpsavedbyte64
            
            	The 64 bits count of UDP/RTP bytes that saved due to IPHC
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosiphcrtpsavedbyteoverflow
            
            	The upper 32 bits count of UDP/RTP bytes that saved due to IPHC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosiphcrtpsentbyte
            
            	The lower 32 bits count of outbound UDP/RTP bytes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosiphcrtpsentbyte64
            
            	The 64 bits count of outbound UDP/RTP bytes
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosiphcrtpsentbyteoverflow
            
            	The upper 32 bits count of outbound UDP/RTP bytes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosiphcrtpsentbyterate
            
            	The 32 bits count of outbound UDP/RTP byte rate
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosiphcrtpsentpkt
            
            	The lower 32 bits count of outbound UDP/RTP packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosiphcrtpsentpkt64
            
            	The 64 bits count of outbound UDP/RTP packets
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosiphcrtpsentpktoverflow
            
            	The upper 32 bits count of outbound UDP/RTP packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosiphctcpcmprsoutpkt
            
            	The lower 32 bits count of outbound compressed TCP packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosiphctcpcmprsoutpkt64
            
            	The 64 bits count of outbound compressed TCP packets
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosiphctcpcmprsoutpktoverflow
            
            	The upper 32 bits count of outbound compressed TCP packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosiphctcpfullhdrsentpkt
            
            	The lower 32 bits count of total fullheader TCP packets sent out
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosiphctcpfullhdrsentpkt64
            
            	The 64 bits count of total fullheader TCP packets sent out
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosiphctcpfullhdrsentpktoverflow
            
            	The upper 32 bits count of total fullheader TCP packets sent out
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosiphctcpsavedbyte
            
            	The lower 32 bits count of TCP bytes that saved due to IPHC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosiphctcpsavedbyte64
            
            	The 64 bits count of TCP bytes that saved due to IPHC
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosiphctcpsavedbyteoverflow
            
            	The upper 32 bits count of TCP bytes that saved due to IPHC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosiphctcpsentbyte
            
            	The lower 32 bits count of outbound TCP bytes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosiphctcpsentbyte64
            
            	The 64 bits count of outbound TCP bytes
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosiphctcpsentbyteoverflow
            
            	The upper 32 bits count of outbound TCP bytes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosiphctcpsentbyterate
            
            	The 32 bits count of outbound TCP byte rate
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosiphctcpsentpkt
            
            	The lower 32 bits count of outbound TCP packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosiphctcpsentpkt64
            
            	The 64 bits count of outbound TCP packets
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosiphctcpsentpktoverflow
            
            	The upper 32 bits count of outbound TCP packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosobjectsindex = None
                self.cbqospolicyindex = None
                self.cbqosiphcrtpcmprsoutpkt = None
                self.cbqosiphcrtpcmprsoutpkt64 = None
                self.cbqosiphcrtpcmprsoutpktoverflow = None
                self.cbqosiphcrtpfullhdrsentpkt = None
                self.cbqosiphcrtpfullhdrsentpkt64 = None
                self.cbqosiphcrtpfullhdrsentpktoverflow = None
                self.cbqosiphcrtpsavedbyte = None
                self.cbqosiphcrtpsavedbyte64 = None
                self.cbqosiphcrtpsavedbyteoverflow = None
                self.cbqosiphcrtpsentbyte = None
                self.cbqosiphcrtpsentbyte64 = None
                self.cbqosiphcrtpsentbyteoverflow = None
                self.cbqosiphcrtpsentbyterate = None
                self.cbqosiphcrtpsentpkt = None
                self.cbqosiphcrtpsentpkt64 = None
                self.cbqosiphcrtpsentpktoverflow = None
                self.cbqosiphctcpcmprsoutpkt = None
                self.cbqosiphctcpcmprsoutpkt64 = None
                self.cbqosiphctcpcmprsoutpktoverflow = None
                self.cbqosiphctcpfullhdrsentpkt = None
                self.cbqosiphctcpfullhdrsentpkt64 = None
                self.cbqosiphctcpfullhdrsentpktoverflow = None
                self.cbqosiphctcpsavedbyte = None
                self.cbqosiphctcpsavedbyte64 = None
                self.cbqosiphctcpsavedbyteoverflow = None
                self.cbqosiphctcpsentbyte = None
                self.cbqosiphctcpsentbyte64 = None
                self.cbqosiphctcpsentbyteoverflow = None
                self.cbqosiphctcpsentbyterate = None
                self.cbqosiphctcpsentpkt = None
                self.cbqosiphctcpsentpkt64 = None
                self.cbqosiphctcpsentpktoverflow = None

            @property
            def _common_path(self):
                if self.cbqosobjectsindex is None:
                    raise YPYDataValidationError('Key property cbqosobjectsindex is None')
                if self.cbqospolicyindex is None:
                    raise YPYDataValidationError('Key property cbqospolicyindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosIPHCStatsTable/CISCO-CLASS-BASED-QOS-MIB:cbQosIPHCStatsEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosObjectsIndex = ' + str(self.cbqosobjectsindex) + '][CISCO-CLASS-BASED-QOS-MIB:cbQosPolicyIndex = ' + str(self.cbqospolicyindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosobjectsindex is not None:
                    return True

                if self.cbqospolicyindex is not None:
                    return True

                if self.cbqosiphcrtpcmprsoutpkt is not None:
                    return True

                if self.cbqosiphcrtpcmprsoutpkt64 is not None:
                    return True

                if self.cbqosiphcrtpcmprsoutpktoverflow is not None:
                    return True

                if self.cbqosiphcrtpfullhdrsentpkt is not None:
                    return True

                if self.cbqosiphcrtpfullhdrsentpkt64 is not None:
                    return True

                if self.cbqosiphcrtpfullhdrsentpktoverflow is not None:
                    return True

                if self.cbqosiphcrtpsavedbyte is not None:
                    return True

                if self.cbqosiphcrtpsavedbyte64 is not None:
                    return True

                if self.cbqosiphcrtpsavedbyteoverflow is not None:
                    return True

                if self.cbqosiphcrtpsentbyte is not None:
                    return True

                if self.cbqosiphcrtpsentbyte64 is not None:
                    return True

                if self.cbqosiphcrtpsentbyteoverflow is not None:
                    return True

                if self.cbqosiphcrtpsentbyterate is not None:
                    return True

                if self.cbqosiphcrtpsentpkt is not None:
                    return True

                if self.cbqosiphcrtpsentpkt64 is not None:
                    return True

                if self.cbqosiphcrtpsentpktoverflow is not None:
                    return True

                if self.cbqosiphctcpcmprsoutpkt is not None:
                    return True

                if self.cbqosiphctcpcmprsoutpkt64 is not None:
                    return True

                if self.cbqosiphctcpcmprsoutpktoverflow is not None:
                    return True

                if self.cbqosiphctcpfullhdrsentpkt is not None:
                    return True

                if self.cbqosiphctcpfullhdrsentpkt64 is not None:
                    return True

                if self.cbqosiphctcpfullhdrsentpktoverflow is not None:
                    return True

                if self.cbqosiphctcpsavedbyte is not None:
                    return True

                if self.cbqosiphctcpsavedbyte64 is not None:
                    return True

                if self.cbqosiphctcpsavedbyteoverflow is not None:
                    return True

                if self.cbqosiphctcpsentbyte is not None:
                    return True

                if self.cbqosiphctcpsentbyte64 is not None:
                    return True

                if self.cbqosiphctcpsentbyteoverflow is not None:
                    return True

                if self.cbqosiphctcpsentbyterate is not None:
                    return True

                if self.cbqosiphctcpsentpkt is not None:
                    return True

                if self.cbqosiphctcpsentpkt64 is not None:
                    return True

                if self.cbqosiphctcpsentpktoverflow is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosIPHCStatsTable.CbQosIPHCStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosIPHCStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqosiphcstatsentry is not None:
                for child_ref in self.cbqosiphcstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosIPHCStatsTable']['meta_info']


    class CbQosInterfacePolicyTable(object):
        """
        This table describes the service polices that are
        attached to main and sub interfaces.
        
        .. attribute:: cbqosinterfacepolicyentry
        
        	Using ifIndex and Direction, each unique index pair translates to a service policy that is attached to a  main/sub interface, for particular traffic direction
        	**type**\: list of :py:class:`CbQosInterfacePolicyEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosInterfacePolicyTable.CbQosInterfacePolicyEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqosinterfacepolicyentry = YList()
            self.cbqosinterfacepolicyentry.parent = self
            self.cbqosinterfacepolicyentry.name = 'cbqosinterfacepolicyentry'


        class CbQosInterfacePolicyEntry(object):
            """
            Using ifIndex and Direction, each unique index pair
            translates to a service policy that is attached to a 
            main/sub interface, for particular traffic direction.
            
            .. attribute:: cbqospolicydirection
            
            	
            	**type**\: :py:class:`TrafficDirection_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.TrafficDirection_Enum>`
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cbqosifpolicyindex
            
            	An arbitrary (system\-assigned) index for all Service Policies.   This is identical to cbQosPolicyIndex
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqospolicydirection = None
                self.ifindex = None
                self.cbqosifpolicyindex = None

            @property
            def _common_path(self):
                if self.cbqospolicydirection is None:
                    raise YPYDataValidationError('Key property cbqospolicydirection is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosInterfacePolicyTable/CISCO-CLASS-BASED-QOS-MIB:cbQosInterfacePolicyEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosPolicyDirection = ' + str(self.cbqospolicydirection) + '][CISCO-CLASS-BASED-QOS-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqospolicydirection is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.cbqosifpolicyindex is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosInterfacePolicyTable.CbQosInterfacePolicyEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosInterfacePolicyTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqosinterfacepolicyentry is not None:
                for child_ref in self.cbqosinterfacepolicyentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosInterfacePolicyTable']['meta_info']


    class CbQosMatchStmtCfgTable(object):
        """
        This table specifies ClassMap configuration information
        
        .. attribute:: cbqosmatchstmtcfgentry
        
        	Each entry in this table describes configuration information about a MatchStatement. The information includes\: Name,  and whether it is a Match or Match\-Not statement. This table contains configuration information  only, no statistics associated with it. Therefore, it is  indexed by the cbQosConfigIndex of each MatchStatement
        	**type**\: list of :py:class:`CbQosMatchStmtCfgEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosMatchStmtCfgTable.CbQosMatchStmtCfgEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqosmatchstmtcfgentry = YList()
            self.cbqosmatchstmtcfgentry.parent = self
            self.cbqosmatchstmtcfgentry.name = 'cbqosmatchstmtcfgentry'


        class CbQosMatchStmtCfgEntry(object):
            """
            Each entry in this table describes configuration information
            about a MatchStatement. The information includes\: Name, 
            and whether it is a Match or Match\-Not
            statement. This table contains configuration information 
            only, no statistics associated with it. Therefore, it is 
            indexed by the cbQosConfigIndex of each MatchStatement.
            
            .. attribute:: cbqosconfigindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosmatchstmtinfo
            
            	Match vs Match Not in a given class
            	**type**\: :py:class:`QosMatchInfo_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.QosMatchInfo_Enum>`
            
            .. attribute:: cbqosmatchstmtname
            
            	Name of the Match Statement
            	**type**\: str
            
            	**range:** 0..255
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosconfigindex = None
                self.cbqosmatchstmtinfo = None
                self.cbqosmatchstmtname = None

            @property
            def _common_path(self):
                if self.cbqosconfigindex is None:
                    raise YPYDataValidationError('Key property cbqosconfigindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosMatchStmtCfgTable/CISCO-CLASS-BASED-QOS-MIB:cbQosMatchStmtCfgEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosConfigIndex = ' + str(self.cbqosconfigindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosconfigindex is not None:
                    return True

                if self.cbqosmatchstmtinfo is not None:
                    return True

                if self.cbqosmatchstmtname is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosMatchStmtCfgTable.CbQosMatchStmtCfgEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosMatchStmtCfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqosmatchstmtcfgentry is not None:
                for child_ref in self.cbqosmatchstmtcfgentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosMatchStmtCfgTable']['meta_info']


    class CbQosMatchStmtStatsTable(object):
        """
        This table specifies Match Statement related statistical
        information.
        
        .. attribute:: cbqosmatchstmtstatsentry
        
        	Each entry in this table describes the statistical information about Match Statement. Match Statement specific  information you can find in this table are \:  Pre policy pkt/byte counters, and bit rates.  This table contains statistical information only, no configuration information associated with it. Therefore,  it is indexed by the instance specific IDs, such as  cbQosPolicyIndex and cbQosObjectsIndex
        	**type**\: list of :py:class:`CbQosMatchStmtStatsEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosMatchStmtStatsTable.CbQosMatchStmtStatsEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqosmatchstmtstatsentry = YList()
            self.cbqosmatchstmtstatsentry.parent = self
            self.cbqosmatchstmtstatsentry.name = 'cbqosmatchstmtstatsentry'


        class CbQosMatchStmtStatsEntry(object):
            """
            Each entry in this table describes the statistical
            information about Match Statement. Match Statement specific 
            information you can find in this table are \: 
            Pre policy pkt/byte counters, and bit rates.
            
            This table contains statistical information only,
            no configuration information associated with it. Therefore, 
            it is indexed by the instance specific IDs, such as 
            cbQosPolicyIndex and cbQosObjectsIndex.
            
            .. attribute:: cbqosobjectsindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospolicyindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosmatchprepolicybitrate
            
            	The bit rate of the traffic prior to executing any QoS policies
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosmatchprepolicybyte
            
            	The lower 32 bits count of inbound octets prior to executing any QoS policies
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosmatchprepolicybyte64
            
            	The 64 bits count of inbound octets prior to executing any QoS policies
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosmatchprepolicybyteoverflow
            
            	The upper 32 bits count of inbound octets prior to executing any QoS policies
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosmatchprepolicypkt
            
            	The lower 32 bits count of inbound packets prior to executing any QoS policies
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosmatchprepolicypkt64
            
            	The 64 bits count of inbound packets prior to executing any QoS policies
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosmatchprepolicypktoverflow
            
            	The upper 32 bits count of inbound packets prior to executing any QoS policies
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosobjectsindex = None
                self.cbqospolicyindex = None
                self.cbqosmatchprepolicybitrate = None
                self.cbqosmatchprepolicybyte = None
                self.cbqosmatchprepolicybyte64 = None
                self.cbqosmatchprepolicybyteoverflow = None
                self.cbqosmatchprepolicypkt = None
                self.cbqosmatchprepolicypkt64 = None
                self.cbqosmatchprepolicypktoverflow = None

            @property
            def _common_path(self):
                if self.cbqosobjectsindex is None:
                    raise YPYDataValidationError('Key property cbqosobjectsindex is None')
                if self.cbqospolicyindex is None:
                    raise YPYDataValidationError('Key property cbqospolicyindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosMatchStmtStatsTable/CISCO-CLASS-BASED-QOS-MIB:cbQosMatchStmtStatsEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosObjectsIndex = ' + str(self.cbqosobjectsindex) + '][CISCO-CLASS-BASED-QOS-MIB:cbQosPolicyIndex = ' + str(self.cbqospolicyindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosobjectsindex is not None:
                    return True

                if self.cbqospolicyindex is not None:
                    return True

                if self.cbqosmatchprepolicybitrate is not None:
                    return True

                if self.cbqosmatchprepolicybyte is not None:
                    return True

                if self.cbqosmatchprepolicybyte64 is not None:
                    return True

                if self.cbqosmatchprepolicybyteoverflow is not None:
                    return True

                if self.cbqosmatchprepolicypkt is not None:
                    return True

                if self.cbqosmatchprepolicypkt64 is not None:
                    return True

                if self.cbqosmatchprepolicypktoverflow is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosMatchStmtStatsTable.CbQosMatchStmtStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosMatchStmtStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqosmatchstmtstatsentry is not None:
                for child_ref in self.cbqosmatchstmtstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosMatchStmtStatsTable']['meta_info']


    class CbQosMeasureIPSLACfgTable(object):
        """
        This table specifies configuration information for measure type
        IPSLA action. The measure action relates the policy class to a
        specific IPSLAs auto group. Configuration of measure action of
        type IPSLA results in automatic generation of IPSLAs synthetic
        test operations when the policy is attached to interface. The
        operations are created according to the characteristics
        specified and to the destinations specified in IPSLA auto group.
        The IPSLAs sythentic test operations measure network statistics
        such as latency, packet loss and jitter.
        This table is to be used only for retrieving the measure
        action configuration information.
        
        .. attribute:: cbqosmeasureipslacfgentry
        
        	Each entry describes configuration information about one instance of IPSLAs measure action in the policy map. The table is indexed by the cbQosConfigIndex and cbQosMeasureIPSLACfgGroupIndex
        	**type**\: list of :py:class:`CbQosMeasureIPSLACfgEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosMeasureIPSLACfgTable.CbQosMeasureIPSLACfgEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqosmeasureipslacfgentry = YList()
            self.cbqosmeasureipslacfgentry.parent = self
            self.cbqosmeasureipslacfgentry.name = 'cbqosmeasureipslacfgentry'


        class CbQosMeasureIPSLACfgEntry(object):
            """
            Each entry describes configuration information about
            one instance of IPSLAs measure action in the policy map.
            The table is indexed by the cbQosConfigIndex and
            cbQosMeasureIPSLACfgGroupIndex.
            
            .. attribute:: cbqosconfigindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosmeasureipslacfggroupindex
            
            	An arbitrary (system\-assigned) index for each instance of IPSLAs measure action. The index is unique for each instance for a particular class in particular policy\-map. For example consider following configuration\:      policy\-map p1         class c1           measure type ip\-sla group g1           measure type ip\-sla group g2         class c2           measure type ip\-sla group g3  In this case the cbQosMeasureIPSLACfgGroupIndex value for first measure action instance under class c1 will be 1, for second instance it will be 1, and so on. The value for the index will start over again from 1 for class c2
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosmeasureipslacfggroupname
            
            	IPSLAs auto group name. Group is an aggregation of operations sharing the same type, for example udp\-jitter type, with common characteristics like frequency, interval etc.  Groups are formed by policies dictated either by customer, or by service level or any other requirements
            	**type**\: str
            
            	**range:** 0..64
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosconfigindex = None
                self.cbqosmeasureipslacfggroupindex = None
                self.cbqosmeasureipslacfggroupname = None

            @property
            def _common_path(self):
                if self.cbqosconfigindex is None:
                    raise YPYDataValidationError('Key property cbqosconfigindex is None')
                if self.cbqosmeasureipslacfggroupindex is None:
                    raise YPYDataValidationError('Key property cbqosmeasureipslacfggroupindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosMeasureIPSLACfgTable/CISCO-CLASS-BASED-QOS-MIB:cbQosMeasureIPSLACfgEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosConfigIndex = ' + str(self.cbqosconfigindex) + '][CISCO-CLASS-BASED-QOS-MIB:cbQosMeasureIPSLACfgGroupIndex = ' + str(self.cbqosmeasureipslacfggroupindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosconfigindex is not None:
                    return True

                if self.cbqosmeasureipslacfggroupindex is not None:
                    return True

                if self.cbqosmeasureipslacfggroupname is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosMeasureIPSLACfgTable.CbQosMeasureIPSLACfgEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosMeasureIPSLACfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqosmeasureipslacfgentry is not None:
                for child_ref in self.cbqosmeasureipslacfgentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosMeasureIPSLACfgTable']['meta_info']


    class CbQosObjectsTable(object):
        """
        This table specifies QoS objects (classmap, policymap,
        match statements, and actions) hierarchy. This table also 
        provide relationship between each PolicyIndex/ObjectsIndex 
        pair and the ConfigIndex. ConfigIndex is essential for 
        querying any configuration tables.
        
        .. attribute:: cbqosobjectsentry
        
        	A QoS object entry. Objects covered in this table are PolicyMap, ClassMap, Match Statements, and Actions. Each entry is indexed by system\-generated cbQosPolicyIndex, and cbQosObjectsIndex, which represents a runtime instance  of a QoS object. In conjunction with the  cbQosParentObjectsIndex, a management station can  determine the hierarchical relationship of those QoS  objects. Given that classmaps and service policies can  be nested entites, each entry in this table represents a  unique instance of such object. Each runtime object  instance has a corresponding config object, which contains the configuration information of such QoS object. The config object is indexed by cbQosConfigIndex
        	**type**\: list of :py:class:`CbQosObjectsEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosObjectsTable.CbQosObjectsEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqosobjectsentry = YList()
            self.cbqosobjectsentry.parent = self
            self.cbqosobjectsentry.name = 'cbqosobjectsentry'


        class CbQosObjectsEntry(object):
            """
            A QoS object entry. Objects covered in this table are
            PolicyMap, ClassMap, Match Statements, and Actions.
            Each entry is indexed by system\-generated cbQosPolicyIndex,
            and cbQosObjectsIndex, which represents a runtime instance 
            of a QoS object. In conjunction with the 
            cbQosParentObjectsIndex, a management station can 
            determine the hierarchical relationship of those QoS 
            objects. Given that classmaps and service policies can 
            be nested entites, each entry in this table represents a 
            unique instance of such object. Each runtime object 
            instance has a corresponding config object, which contains
            the configuration information of such QoS object. The
            config object is indexed by cbQosConfigIndex.
            
            .. attribute:: cbqosobjectsindex
            
            	An arbitrary (system\-assigned) instance specific index for cbQosObjectsEntry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospolicyindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosconfigindex
            
            	An arbitrary (system\-assigned) config (instance independent) index for each Object. Each objects having the same configuration share the same config index
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosobjectstype
            
            	The type of the QoS object
            	**type**\: :py:class:`QosObjectType_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.QosObjectType_Enum>`
            
            .. attribute:: cbqosparentobjectsindex
            
            	The parent instance index of a QoS object.  For a ClassMap, the parent index would be the index of  the attached PolicyMap.  For a Match Statement, the parent index would be the  index of the ClassMap that uses this Match Statement.  For an action, the parent index would be the  index of the ClassMap that applies such Action.  For a non\-hierarchical PolicyMap, the parent would be  the logical interface to which the policy is attached, thus the parent index would be 0.  For a hierarchical PolicyMap, the parent index would  be the index of the ClassMap to which the nested  policy is attached
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosobjectsindex = None
                self.cbqospolicyindex = None
                self.cbqosconfigindex = None
                self.cbqosobjectstype = None
                self.cbqosparentobjectsindex = None

            @property
            def _common_path(self):
                if self.cbqosobjectsindex is None:
                    raise YPYDataValidationError('Key property cbqosobjectsindex is None')
                if self.cbqospolicyindex is None:
                    raise YPYDataValidationError('Key property cbqospolicyindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosObjectsTable/CISCO-CLASS-BASED-QOS-MIB:cbQosObjectsEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosObjectsIndex = ' + str(self.cbqosobjectsindex) + '][CISCO-CLASS-BASED-QOS-MIB:cbQosPolicyIndex = ' + str(self.cbqospolicyindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosobjectsindex is not None:
                    return True

                if self.cbqospolicyindex is not None:
                    return True

                if self.cbqosconfigindex is not None:
                    return True

                if self.cbqosobjectstype is not None:
                    return True

                if self.cbqosparentobjectsindex is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosObjectsTable.CbQosObjectsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosObjectsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqosobjectsentry is not None:
                for child_ref in self.cbqosobjectsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosObjectsTable']['meta_info']


    class CbQosPoliceActionCfgTable(object):
        """
        This table specifies Police Action configuration
        information.
        
        .. attribute:: cbqospoliceactioncfgentry
        
        	Each entry in this table describes configuration information about Actions for one Police.  The table holds Police  action specific configuration parameters. This table is a sub\-table for cbQosPoliceCfgTable. There is a 1\-to\-1 association between one entry here and one entry in  cbQosPoliceCfgTable.  This table contains configuration information only, no statistics associated with it.  This table has two indices. The first is cbQosConfigIndex  which is drived directly from cbQosPoliceCfgTable to keep the 1\-to\-1 mapping nature between two tables.  The second is cbQosPoliceActionCfgIndex used to reference  the actual actions configured. The maximum number of actions supported is determined by the system, which is 5 currently
        	**type**\: list of :py:class:`CbQosPoliceActionCfgEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosPoliceActionCfgTable.CbQosPoliceActionCfgEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqospoliceactioncfgentry = YList()
            self.cbqospoliceactioncfgentry.parent = self
            self.cbqospoliceactioncfgentry.name = 'cbqospoliceactioncfgentry'


        class CbQosPoliceActionCfgEntry(object):
            """
            Each entry in this table describes configuration information
            about Actions for one Police.  The table holds Police 
            action specific configuration parameters.
            This table is a sub\-table for cbQosPoliceCfgTable. There is
            a 1\-to\-1 association between one entry here and one entry in 
            cbQosPoliceCfgTable. 
            This table contains configuration information only,
            no statistics associated with it. 
            This table has two indices. The first is cbQosConfigIndex 
            which is drived directly from cbQosPoliceCfgTable to keep the
            1\-to\-1 mapping nature between two tables. 
            The second is cbQosPoliceActionCfgIndex used to reference 
            the actual actions configured. The maximum number of actions
            supported is determined by the system, which is 5 currently.
            
            .. attribute:: cbqosconfigindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospoliceactioncfgindex
            
            	An arbitrary (system\-assigned) index for police actions that are defined by a police configuration
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospoliceactioncfgconform
            
            	Action to be taken when the traffic exceeds the conform and exceed token buckets
            	**type**\: :py:class:`PoliceAction_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.PoliceAction_Enum>`
            
            .. attribute:: cbqospoliceactioncfgconformsetvalue
            
            	New packet attribute values for each packet set by police action defined in cbQosPoliceActionCfgConform. This object will be set to zero if the corresponding police action does not require a set value, such as  no action, drop action or transmit action
            	**type**\: int
            
            	**range:** 0..99
            
            .. attribute:: cbqospoliceactioncfgexceed
            
            	Action to be taken when the traffic exceeds the conform and exceed token buckets
            	**type**\: :py:class:`PoliceAction_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.PoliceAction_Enum>`
            
            .. attribute:: cbqospoliceactioncfgexceedsetvalue
            
            	New packet attribute values for each packet set by police action defined in cbQosPoliceActionCfgExceed. This object will be set to zero if the corresponding police action does not require a set value, such as  no action, drop action or transmit action
            	**type**\: int
            
            	**range:** 0..99
            
            .. attribute:: cbqospoliceactioncfgviolate
            
            	Action to be taken when the traffic exceeds the conform and exceed token buckets
            	**type**\: :py:class:`PoliceAction_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.PoliceAction_Enum>`
            
            .. attribute:: cbqospoliceactioncfgviolatesetvalue
            
            	New packet attribute values for each packet set by police action defined in cbQosPoliceActionCfgViolate. This object will be set to zero if the corresponding police action does not require a set value, such as  no action, drop action or transmit action
            	**type**\: int
            
            	**range:** 0..99
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosconfigindex = None
                self.cbqospoliceactioncfgindex = None
                self.cbqospoliceactioncfgconform = None
                self.cbqospoliceactioncfgconformsetvalue = None
                self.cbqospoliceactioncfgexceed = None
                self.cbqospoliceactioncfgexceedsetvalue = None
                self.cbqospoliceactioncfgviolate = None
                self.cbqospoliceactioncfgviolatesetvalue = None

            @property
            def _common_path(self):
                if self.cbqosconfigindex is None:
                    raise YPYDataValidationError('Key property cbqosconfigindex is None')
                if self.cbqospoliceactioncfgindex is None:
                    raise YPYDataValidationError('Key property cbqospoliceactioncfgindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosPoliceActionCfgTable/CISCO-CLASS-BASED-QOS-MIB:cbQosPoliceActionCfgEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosConfigIndex = ' + str(self.cbqosconfigindex) + '][CISCO-CLASS-BASED-QOS-MIB:cbQosPoliceActionCfgIndex = ' + str(self.cbqospoliceactioncfgindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosconfigindex is not None:
                    return True

                if self.cbqospoliceactioncfgindex is not None:
                    return True

                if self.cbqospoliceactioncfgconform is not None:
                    return True

                if self.cbqospoliceactioncfgconformsetvalue is not None:
                    return True

                if self.cbqospoliceactioncfgexceed is not None:
                    return True

                if self.cbqospoliceactioncfgexceedsetvalue is not None:
                    return True

                if self.cbqospoliceactioncfgviolate is not None:
                    return True

                if self.cbqospoliceactioncfgviolatesetvalue is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosPoliceActionCfgTable.CbQosPoliceActionCfgEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosPoliceActionCfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqospoliceactioncfgentry is not None:
                for child_ref in self.cbqospoliceactioncfgentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosPoliceActionCfgTable']['meta_info']


    class CbQosPoliceCfgTable(object):
        """
        This table specifies Police Action configuration
        information.
        
        .. attribute:: cbqospolicecfgentry
        
        	Each entry in this table describes configuration information about a Police Action.  The table holds Policy  configuration parameters, such as rate, burst size, and  actions based on traffic rates.  This table contains configuration information only, no statistics associated with it. Therefore, it is indexed by the cbQosConfigIndex
        	**type**\: list of :py:class:`CbQosPoliceCfgEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosPoliceCfgTable.CbQosPoliceCfgEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqospolicecfgentry = YList()
            self.cbqospolicecfgentry.parent = self
            self.cbqospolicecfgentry.name = 'cbqospolicecfgentry'


        class CbQosPoliceCfgEntry(object):
            """
            Each entry in this table describes configuration information
            about a Police Action.  The table holds Policy 
            configuration parameters, such as rate, burst size, and 
            actions based on traffic rates.
            
            This table contains configuration information only,
            no statistics associated with it. Therefore, it is indexed
            by the cbQosConfigIndex.
            
            .. attribute:: cbqosconfigindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospolicecfgburstcell
            
            	The amount of traffic, in cells, in excess of the committed policing rate that will be permitted by the policing feature
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospolicecfgburstsize
            
            	The amount of traffic, in bytes, in excess of the committed policing rate that will be permitted by  the policing feature.  cbQosPoliceCfgBurstSize object is superseded by cbQosPoliceCfgBurstSize64
            	**type**\: int
            
            	**range:** 1000..512000000
            
            .. attribute:: cbqospolicecfgburstsize64
            
            	This object indicated the amount of traffic, in bytes, in excess of the committed policing rate that will be permitted by  the policing feature.   If a device implements cbQosPoliceCfgBurstSize64, then it should not implement cbQosPoliceCfgBurstSize
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospolicecfgbursttime
            
            	The amount of traffic time, in ms, in excess of the committed policing rate that will be permitted by the policing feature.  The milli\-second value is internally converted to bytes by using the bandwidth that is available for the class
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospolicecfgcdvt
            
            	The ATM Cell Delay Variation Tolerance value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospolicecfgcellpir
            
            	The peak policing rate in cells/second.  Its value is valid only when cbQosPoliceCfgRateType equals to 3
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospolicecfgcellrate
            
            	The committed policing rate in cells/second.  Its value is valid only when cbQosPoliceCfgRateType equals to 3
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospolicecfgconditional
            
            	This object is use to depict weather police is configured as a conditioniler policer or not
            	**type**\: bool
            
            .. attribute:: cbqospolicecfgconformaction
            
            	Action to be taken when the traffic is within the configured rate, that is, the traffic rate is  conforming.  cbQosPoliceCfgConformAction object is superseded by cbQosPoliceActionCfgConform
            	**type**\: :py:class:`PoliceAction_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.PoliceAction_Enum>`
            
            .. attribute:: cbqospolicecfgconformcolor
            
            	The Classmap name used in AF color\-aware mode to specify the conform\-color for the incoming packets which was marked by the previous node.  At least conform\-color must be specified.  If only  conform\-color is specified, all other packets are assumed to be marked exceed.  See RFC 2697, A Single Rate Three Color Marker. See RFC 2698, A Two Rate Three Color Marker
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cbqospolicecfgconformsetvalue
            
            	New packet attribute values for each packets that conforms to the configured Police rate.  cbQosPoliceCfgConformSetValue object is superseded by cbQosPoliceActionCfgConformSetValue
            	**type**\: int
            
            	**range:** 1..99
            
            .. attribute:: cbqospolicecfgexceedaction
            
            	Action to be taken when the traffic exceeds the configured rate, that is, the traffic is  non\-conforming.  cbQosPoliceCfgExceedAction object is superseded by cbQosPoliceActionCfgExceed
            	**type**\: :py:class:`PoliceAction_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.PoliceAction_Enum>`
            
            .. attribute:: cbqospolicecfgexceedcolor
            
            	The Classmap name used in AF color\-aware mode to specify the exceed\-color for the incoming packets which was marked by the previous node.  If both conform\-color and exceed\-color are specified, all other packets are assumed to be marked violate. Violate\-color configuration is not needed
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cbqospolicecfgexceedsetvalue
            
            	New packet attribute values for each packets that conforms to the configured Police rate.  cbQosPoliceCfgExceedSetValue object is superseded by cbQosPoliceActionCfgExceedSetValue
            	**type**\: int
            
            	**range:** 1..99
            
            .. attribute:: cbqospolicecfgextburstcell
            
            	The amount of traffic, in cells, in excess of the burst limit, which may be conditionally permitted by the policing feature. The probability that the traffic is not permitted increases as the received burst size increases
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospolicecfgextburstsize
            
            	The amount of traffic, in bytes, in excess of the burst limit, which may be conditionally permitted  by the policing feature. The probability that the  traffic is not permitted increases as the received  burst size increases.  cbQosPoliceCfgExtBurstSize object is superseded by cbQosPoliceCfgExtBurstSize64
            	**type**\: int
            
            	**range:** 1000..512000000
            
            .. attribute:: cbqospolicecfgextburstsize64
            
            	This object indicated the amount of traffic, in bytes, in excess of the burst limit, which may be conditionally permitted  by the policing feature. The probability that the  traffic is not permitted increases as the received  burst size increases.   If a device implements cbQosPoliceCfgBurstSize64, then it should not implement cbQosPoliceCfgBurstSize
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospolicecfgextbursttime
            
            	The amount of traffic time, in ms, in excess of the burst limit, which may be conditionally permitted by the policing feature. The probability that the traffic is not permitted increases as the received burst size increases.  The milli\-second value is  internally converted to bytes by using the bandwidth that is available for the class
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospolicecfgpercentpirvalue
            
            	The peak policing rate in percentage. Its value is valid only when cbQosPoliceCfgRateType equals to 2
            	**type**\: int
            
            	**range:** 0..100
            
            .. attribute:: cbqospolicecfgpercentratevalue
            
            	The committed policing rate in percentage.  Its value is valid only when cbQosPoliceCfgRateType equals to 2
            	**type**\: int
            
            	**range:** 0..100
            
            .. attribute:: cbqospolicecfgpir
            
            	The committed policing rate. This is the peak rate permitted by two rate policing.  cbQosPoliceCfgPir object is superseded by cbQosPoliceCfgPir64
            	**type**\: int
            
            	**range:** 8000..2000000000
            
            .. attribute:: cbqospolicecfgpir64
            
            	This object indicates the committed policing rate. This is the peak rate permitted by two rate policing.   If a device implements cbQosPoliceCfgPir64, then it should not implement cbQosPoliceCfgPir
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospolicecfgrate
            
            	The committed policing rate. This is the sustained rate permitted by policing.  If a committed policing rate greater than 4294967295 is configurable on the system, then the configured rate is available in cbQosPoliceCfgRate64
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospolicecfgrate64
            
            	The committed policing rate. This is the sustained rate permitted by policing
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospolicecfgratetype
            
            	The rate type that configured for CIR & PIR. 1 means rates are configured in bps. 2 means rates are configured in percentage. 3 means rates are configured in cps. 4 means rates are configured in parts per\-thousand. 5 means rates are configured in parts per\-million
            	**type**\: :py:class:`CbQosRateType_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CbQosRateType_Enum>`
            
            .. attribute:: cbqospolicecfgviolateaction
            
            	Action to be taken when the traffic exceeds the conform and exceed token buckets.  cbQosPoliceCfgViolateAction object is superseded by cbQosPoliceActionCfgViolate
            	**type**\: :py:class:`PoliceAction_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.PoliceAction_Enum>`
            
            .. attribute:: cbqospolicecfgviolatesetvalue
            
            	New packet attribute values for each packets that conforms to the Police violate action. The packet attibute values depend on the action that is taken for the particular packet. For example, if the  action was to set the dscp value, this entry describes the value it is set to.   cbQosPoliceCfgViolateSetValue object is superseded by cbQosPoliceActionCfgViolateSetValue
            	**type**\: int
            
            	**range:** 1..99
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosconfigindex = None
                self.cbqospolicecfgburstcell = None
                self.cbqospolicecfgburstsize = None
                self.cbqospolicecfgburstsize64 = None
                self.cbqospolicecfgbursttime = None
                self.cbqospolicecfgcdvt = None
                self.cbqospolicecfgcellpir = None
                self.cbqospolicecfgcellrate = None
                self.cbqospolicecfgconditional = None
                self.cbqospolicecfgconformaction = None
                self.cbqospolicecfgconformcolor = None
                self.cbqospolicecfgconformsetvalue = None
                self.cbqospolicecfgexceedaction = None
                self.cbqospolicecfgexceedcolor = None
                self.cbqospolicecfgexceedsetvalue = None
                self.cbqospolicecfgextburstcell = None
                self.cbqospolicecfgextburstsize = None
                self.cbqospolicecfgextburstsize64 = None
                self.cbqospolicecfgextbursttime = None
                self.cbqospolicecfgpercentpirvalue = None
                self.cbqospolicecfgpercentratevalue = None
                self.cbqospolicecfgpir = None
                self.cbqospolicecfgpir64 = None
                self.cbqospolicecfgrate = None
                self.cbqospolicecfgrate64 = None
                self.cbqospolicecfgratetype = None
                self.cbqospolicecfgviolateaction = None
                self.cbqospolicecfgviolatesetvalue = None

            @property
            def _common_path(self):
                if self.cbqosconfigindex is None:
                    raise YPYDataValidationError('Key property cbqosconfigindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosPoliceCfgTable/CISCO-CLASS-BASED-QOS-MIB:cbQosPoliceCfgEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosConfigIndex = ' + str(self.cbqosconfigindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosconfigindex is not None:
                    return True

                if self.cbqospolicecfgburstcell is not None:
                    return True

                if self.cbqospolicecfgburstsize is not None:
                    return True

                if self.cbqospolicecfgburstsize64 is not None:
                    return True

                if self.cbqospolicecfgbursttime is not None:
                    return True

                if self.cbqospolicecfgcdvt is not None:
                    return True

                if self.cbqospolicecfgcellpir is not None:
                    return True

                if self.cbqospolicecfgcellrate is not None:
                    return True

                if self.cbqospolicecfgconditional is not None:
                    return True

                if self.cbqospolicecfgconformaction is not None:
                    return True

                if self.cbqospolicecfgconformcolor is not None:
                    return True

                if self.cbqospolicecfgconformsetvalue is not None:
                    return True

                if self.cbqospolicecfgexceedaction is not None:
                    return True

                if self.cbqospolicecfgexceedcolor is not None:
                    return True

                if self.cbqospolicecfgexceedsetvalue is not None:
                    return True

                if self.cbqospolicecfgextburstcell is not None:
                    return True

                if self.cbqospolicecfgextburstsize is not None:
                    return True

                if self.cbqospolicecfgextburstsize64 is not None:
                    return True

                if self.cbqospolicecfgextbursttime is not None:
                    return True

                if self.cbqospolicecfgpercentpirvalue is not None:
                    return True

                if self.cbqospolicecfgpercentratevalue is not None:
                    return True

                if self.cbqospolicecfgpir is not None:
                    return True

                if self.cbqospolicecfgpir64 is not None:
                    return True

                if self.cbqospolicecfgrate is not None:
                    return True

                if self.cbqospolicecfgrate64 is not None:
                    return True

                if self.cbqospolicecfgratetype is not None:
                    return True

                if self.cbqospolicecfgviolateaction is not None:
                    return True

                if self.cbqospolicecfgviolatesetvalue is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosPoliceCfgTable.CbQosPoliceCfgEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosPoliceCfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqospolicecfgentry is not None:
                for child_ref in self.cbqospolicecfgentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosPoliceCfgTable']['meta_info']


    class CbQosPoliceColorStatsTable(object):
        """
        This table specifies Police Action related Statistical
        information for two rate color aware marker.
        
        .. attribute:: cbqospolicecolorstatsentry
        
        	Each entry in this table describes the statistical information about Police Action for Two Rate Color Aware Marker.  This table contains statistical information only, no configuration information associated with it. Therefore, it is indexed by the instance specific IDs, such as cbQosPolicyIndex and cbQosObjectsIndex
        	**type**\: list of :py:class:`CbQosPoliceColorStatsEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosPoliceColorStatsTable.CbQosPoliceColorStatsEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqospolicecolorstatsentry = YList()
            self.cbqospolicecolorstatsentry.parent = self
            self.cbqospolicecolorstatsentry.name = 'cbqospolicecolorstatsentry'


        class CbQosPoliceColorStatsEntry(object):
            """
            Each entry in this table describes the statistical
            information about Police Action for Two Rate Color
            Aware Marker.
            
            This table contains statistical information only,
            no configuration information associated with it.
            Therefore, it is indexed by the instance specific IDs,
            such as cbQosPolicyIndex and cbQosObjectsIndex.
            
            .. attribute:: cbqosobjectsindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospolicyindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospolicecfmcolorcfmbitrate
            
            	The bit rate of conform color class conform rate
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospolicecfmcolorcfmbyte64
            
            	The 64 bits count of bytes which are marked as Conform\-Color by previous node and treated as conforming by the policing feature on this node
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospolicecfmcolorcfmpkt64
            
            	The 64 bits count of packets which are marked as Conform\-Color by previous node and treated as conforming by the policing feature on this node
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospolicecfmcolorexdbitrate
            
            	The bit rate of conform color class exceed rate
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospolicecfmcolorexdbyte64
            
            	The 64 bits count of bytes which are marked as Conform\-Color by previous node and treated as exceeding by the policing feature on this node
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospolicecfmcolorexdpkt64
            
            	The 64 bits count of packets which are marked as Conform\-Color by previous node and treated as exceeding by the policing feature on this node
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospolicecfmcolorvltbitrate
            
            	The bit rate of conform color class violate rate
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospolicecfmcolorvltbyte64
            
            	The 64 bits count of bytes which are marked as Conform\-Color by previous node and treated as violating by the policing feature on this node
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospolicecfmcolorvltpkt64
            
            	The 64 bits count of packets which are marked as Conform\-Color by previous node and treated as violating by the policing feature on this node
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospoliceexdcolorexdbitrate
            
            	The bit rate of exceed color class exceed rate
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospoliceexdcolorexdbyte64
            
            	The 64 bits count of bytes which are marked as Exceed\-Color by previous node and treated as exceeding by the policing feature on this node
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospoliceexdcolorexdpkt64
            
            	The 64 bits count of packets which are marked as Exceed\-Color by previous node and treated as exceeding by the policing feature on this node
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospoliceexdcolorvltbitrate
            
            	The bit rate of exceed color class violate rate
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospoliceexdcolorvltbyte64
            
            	The 64 bits count of bytes which are marked as Exceed\-Color by previous node and treated as violating by the policing feature on this node
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospoliceexdcolorvltpkt64
            
            	The 64 bits count of packets which are marked as Exceed\-Color by previous node and treated as violating by the policing feature on this node
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospolicevltcolorvltbitrate
            
            	The bit rate of violate color class violate rate
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospolicevltcolorvltbyte64
            
            	The 64 bits count of bytes which are marked as Violate\-Color by previous node and treated as violating by the policing feature on this node
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospolicevltcolorvltpkt64
            
            	The 64 bits count of packets which are marked as Violate\-Color by previous node and treated as violating by the policing feature on this node
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosobjectsindex = None
                self.cbqospolicyindex = None
                self.cbqospolicecfmcolorcfmbitrate = None
                self.cbqospolicecfmcolorcfmbyte64 = None
                self.cbqospolicecfmcolorcfmpkt64 = None
                self.cbqospolicecfmcolorexdbitrate = None
                self.cbqospolicecfmcolorexdbyte64 = None
                self.cbqospolicecfmcolorexdpkt64 = None
                self.cbqospolicecfmcolorvltbitrate = None
                self.cbqospolicecfmcolorvltbyte64 = None
                self.cbqospolicecfmcolorvltpkt64 = None
                self.cbqospoliceexdcolorexdbitrate = None
                self.cbqospoliceexdcolorexdbyte64 = None
                self.cbqospoliceexdcolorexdpkt64 = None
                self.cbqospoliceexdcolorvltbitrate = None
                self.cbqospoliceexdcolorvltbyte64 = None
                self.cbqospoliceexdcolorvltpkt64 = None
                self.cbqospolicevltcolorvltbitrate = None
                self.cbqospolicevltcolorvltbyte64 = None
                self.cbqospolicevltcolorvltpkt64 = None

            @property
            def _common_path(self):
                if self.cbqosobjectsindex is None:
                    raise YPYDataValidationError('Key property cbqosobjectsindex is None')
                if self.cbqospolicyindex is None:
                    raise YPYDataValidationError('Key property cbqospolicyindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosPoliceColorStatsTable/CISCO-CLASS-BASED-QOS-MIB:cbQosPoliceColorStatsEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosObjectsIndex = ' + str(self.cbqosobjectsindex) + '][CISCO-CLASS-BASED-QOS-MIB:cbQosPolicyIndex = ' + str(self.cbqospolicyindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosobjectsindex is not None:
                    return True

                if self.cbqospolicyindex is not None:
                    return True

                if self.cbqospolicecfmcolorcfmbitrate is not None:
                    return True

                if self.cbqospolicecfmcolorcfmbyte64 is not None:
                    return True

                if self.cbqospolicecfmcolorcfmpkt64 is not None:
                    return True

                if self.cbqospolicecfmcolorexdbitrate is not None:
                    return True

                if self.cbqospolicecfmcolorexdbyte64 is not None:
                    return True

                if self.cbqospolicecfmcolorexdpkt64 is not None:
                    return True

                if self.cbqospolicecfmcolorvltbitrate is not None:
                    return True

                if self.cbqospolicecfmcolorvltbyte64 is not None:
                    return True

                if self.cbqospolicecfmcolorvltpkt64 is not None:
                    return True

                if self.cbqospoliceexdcolorexdbitrate is not None:
                    return True

                if self.cbqospoliceexdcolorexdbyte64 is not None:
                    return True

                if self.cbqospoliceexdcolorexdpkt64 is not None:
                    return True

                if self.cbqospoliceexdcolorvltbitrate is not None:
                    return True

                if self.cbqospoliceexdcolorvltbyte64 is not None:
                    return True

                if self.cbqospoliceexdcolorvltpkt64 is not None:
                    return True

                if self.cbqospolicevltcolorvltbitrate is not None:
                    return True

                if self.cbqospolicevltcolorvltbyte64 is not None:
                    return True

                if self.cbqospolicevltcolorvltpkt64 is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosPoliceColorStatsTable.CbQosPoliceColorStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosPoliceColorStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqospolicecolorstatsentry is not None:
                for child_ref in self.cbqospolicecolorstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosPoliceColorStatsTable']['meta_info']


    class CbQosPoliceStatsTable(object):
        """
        This table specifies Police Action related Statistical
        information.
        
        .. attribute:: cbqospolicestatsentry
        
        	Each entry in this table describes the statistical information about Police Action. Police Action specific  information you can find in this table are \:  Conformed/Exceeded pkt/byte counters,  bit rates.  This table contains statistical information only, no configuration information associated with it.  Therefore, it is indexed by the instance specific IDs,  such as cbQosPolicyIndex and cbQosObjectsIndex
        	**type**\: list of :py:class:`CbQosPoliceStatsEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosPoliceStatsTable.CbQosPoliceStatsEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqospolicestatsentry = YList()
            self.cbqospolicestatsentry.parent = self
            self.cbqospolicestatsentry.name = 'cbqospolicestatsentry'


        class CbQosPoliceStatsEntry(object):
            """
            Each entry in this table describes the statistical
            information about Police Action. Police Action specific 
            information you can find in this table are \: 
            Conformed/Exceeded pkt/byte counters,  bit rates.
            
            This table contains statistical information only,
            no configuration information associated with it. 
            Therefore, it is indexed by the instance specific IDs, 
            such as cbQosPolicyIndex and cbQosObjectsIndex.
            
            .. attribute:: cbqosobjectsindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospolicyindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospoliceconformedbitrate
            
            	The bit rate of conforming traffic
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospoliceconformedbitrate64
            
            	The bit rate of conforming traffic. This object is a 64\-bit version of cbQosPoliceConformedBitRate
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospoliceconformedbyte
            
            	The lower 32 bits count of octets treated as conforming by the policing feature
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospoliceconformedbyte64
            
            	The 64 bits count of octets treated as conforming by the policing feature
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospoliceconformedbyteoverflow
            
            	The upper 32 bits count of octets treated as conforming by the policing feature
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospoliceconformedpkt
            
            	The lower 32 bits count of packets treated as conforming by the policing feature
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospoliceconformedpkt64
            
            	The 64 bits count of packets treated as conforming by the policing feature
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospoliceconformedpktoverflow
            
            	The upper 32 bits count of packets treated as conforming by the policing feature
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospoliceexceededbitrate
            
            	The bit rate of the non\-conforming traffic
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospoliceexceededbitrate64
            
            	The bit rate of non\-conforming traffic. This object is a 64\-bit version of cbQosPoliceExceededBitRate
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospoliceexceededbyte
            
            	The lower 32 bits count of octets treated as non\-conforming by the policing feature
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospoliceexceededbyte64
            
            	The 64 bits count of octets treated as non\-conforming by the policing feature
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospoliceexceededbyteoverflow
            
            	The upper 32 bits count of octets treated as non\-conforming by the policing feature
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospoliceexceededpkt
            
            	The 32 bits count of packets treated as non\-conforming by the policing feature
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospoliceexceededpkt64
            
            	The 64 bits count of packets treated as non\-conforming by the policing feature
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospoliceexceededpktoverflow
            
            	The upper 32 bits count of packets treated as non\-conforming by the policing feature
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospoliceviolatedbitrate
            
            	The bit rate of the violating traffic
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospoliceviolatedbitrate64
            
            	The bit rate of the violating traffic. This object is a 64\-bit version of cbQosPoliceViolatedBitRate
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospoliceviolatedbyte
            
            	The lower 32 bits count of octets treated as violated by the policing feature
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospoliceviolatedbyte64
            
            	The 64 bits count of octets treated as violated by the policing feature
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospoliceviolatedbyteoverflow
            
            	The upper 32 bits count of octets treated as violated by the policing feature
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospoliceviolatedpkt
            
            	The 32 bits count of packets treated as violated by the policing feature
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospoliceviolatedpkt64
            
            	The 64 bits count of packets treated as violated by the policing feature
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqospoliceviolatedpktoverflow
            
            	The upper 32 bits count of packets treated as violated by the policing feature
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosobjectsindex = None
                self.cbqospolicyindex = None
                self.cbqospoliceconformedbitrate = None
                self.cbqospoliceconformedbitrate64 = None
                self.cbqospoliceconformedbyte = None
                self.cbqospoliceconformedbyte64 = None
                self.cbqospoliceconformedbyteoverflow = None
                self.cbqospoliceconformedpkt = None
                self.cbqospoliceconformedpkt64 = None
                self.cbqospoliceconformedpktoverflow = None
                self.cbqospoliceexceededbitrate = None
                self.cbqospoliceexceededbitrate64 = None
                self.cbqospoliceexceededbyte = None
                self.cbqospoliceexceededbyte64 = None
                self.cbqospoliceexceededbyteoverflow = None
                self.cbqospoliceexceededpkt = None
                self.cbqospoliceexceededpkt64 = None
                self.cbqospoliceexceededpktoverflow = None
                self.cbqospoliceviolatedbitrate = None
                self.cbqospoliceviolatedbitrate64 = None
                self.cbqospoliceviolatedbyte = None
                self.cbqospoliceviolatedbyte64 = None
                self.cbqospoliceviolatedbyteoverflow = None
                self.cbqospoliceviolatedpkt = None
                self.cbqospoliceviolatedpkt64 = None
                self.cbqospoliceviolatedpktoverflow = None

            @property
            def _common_path(self):
                if self.cbqosobjectsindex is None:
                    raise YPYDataValidationError('Key property cbqosobjectsindex is None')
                if self.cbqospolicyindex is None:
                    raise YPYDataValidationError('Key property cbqospolicyindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosPoliceStatsTable/CISCO-CLASS-BASED-QOS-MIB:cbQosPoliceStatsEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosObjectsIndex = ' + str(self.cbqosobjectsindex) + '][CISCO-CLASS-BASED-QOS-MIB:cbQosPolicyIndex = ' + str(self.cbqospolicyindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosobjectsindex is not None:
                    return True

                if self.cbqospolicyindex is not None:
                    return True

                if self.cbqospoliceconformedbitrate is not None:
                    return True

                if self.cbqospoliceconformedbitrate64 is not None:
                    return True

                if self.cbqospoliceconformedbyte is not None:
                    return True

                if self.cbqospoliceconformedbyte64 is not None:
                    return True

                if self.cbqospoliceconformedbyteoverflow is not None:
                    return True

                if self.cbqospoliceconformedpkt is not None:
                    return True

                if self.cbqospoliceconformedpkt64 is not None:
                    return True

                if self.cbqospoliceconformedpktoverflow is not None:
                    return True

                if self.cbqospoliceexceededbitrate is not None:
                    return True

                if self.cbqospoliceexceededbitrate64 is not None:
                    return True

                if self.cbqospoliceexceededbyte is not None:
                    return True

                if self.cbqospoliceexceededbyte64 is not None:
                    return True

                if self.cbqospoliceexceededbyteoverflow is not None:
                    return True

                if self.cbqospoliceexceededpkt is not None:
                    return True

                if self.cbqospoliceexceededpkt64 is not None:
                    return True

                if self.cbqospoliceexceededpktoverflow is not None:
                    return True

                if self.cbqospoliceviolatedbitrate is not None:
                    return True

                if self.cbqospoliceviolatedbitrate64 is not None:
                    return True

                if self.cbqospoliceviolatedbyte is not None:
                    return True

                if self.cbqospoliceviolatedbyte64 is not None:
                    return True

                if self.cbqospoliceviolatedbyteoverflow is not None:
                    return True

                if self.cbqospoliceviolatedpkt is not None:
                    return True

                if self.cbqospoliceviolatedpkt64 is not None:
                    return True

                if self.cbqospoliceviolatedpktoverflow is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosPoliceStatsTable.CbQosPoliceStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosPoliceStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqospolicestatsentry is not None:
                for child_ref in self.cbqospolicestatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosPoliceStatsTable']['meta_info']


    class CbQosPolicyMapCfgTable(object):
        """
        This table specifies Policymap configuration information
        
        .. attribute:: cbqospolicymapcfgentry
        
        	Each entry in this table describes configuration information about a policymap. The information includes\: Name, and it's description. This table contains configuration information  only, no statistics associated with it. Therefore, it is  indexed by the cbQosConfigIndex of each PolicyMap
        	**type**\: list of :py:class:`CbQosPolicyMapCfgEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosPolicyMapCfgTable.CbQosPolicyMapCfgEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqospolicymapcfgentry = YList()
            self.cbqospolicymapcfgentry.parent = self
            self.cbqospolicymapcfgentry.name = 'cbqospolicymapcfgentry'


        class CbQosPolicyMapCfgEntry(object):
            """
            Each entry in this table describes configuration information
            about a policymap. The information includes\: Name, and it's
            description. This table contains configuration information 
            only, no statistics associated with it. Therefore, it is 
            indexed by the cbQosConfigIndex of each PolicyMap.
            
            .. attribute:: cbqosconfigindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospolicymapdesc
            
            	Description of the PolicyMap
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cbqospolicymapname
            
            	Name of the Policymap
            	**type**\: str
            
            	**range:** 0..255
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosconfigindex = None
                self.cbqospolicymapdesc = None
                self.cbqospolicymapname = None

            @property
            def _common_path(self):
                if self.cbqosconfigindex is None:
                    raise YPYDataValidationError('Key property cbqosconfigindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosPolicyMapCfgTable/CISCO-CLASS-BASED-QOS-MIB:cbQosPolicyMapCfgEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosConfigIndex = ' + str(self.cbqosconfigindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosconfigindex is not None:
                    return True

                if self.cbqospolicymapdesc is not None:
                    return True

                if self.cbqospolicymapname is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosPolicyMapCfgTable.CbQosPolicyMapCfgEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosPolicyMapCfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqospolicymapcfgentry is not None:
                for child_ref in self.cbqospolicymapcfgentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosPolicyMapCfgTable']['meta_info']


    class CbQosQueueingCfgTable(object):
        """
        This table specifies Queueing Action configuration
        information
        
        .. attribute:: cbqosqueueingcfgentry
        
        	Each entry in this table describes configuration information about a queueing action. The information  includes\: Bandwidth, Units, Flow Enabled, Priority Enabled,  and Q size.  This table contains configuration information only, no statistics associated with it. Therefore, it is indexed by the cbQosConfigIndex of each Queueing Action
        	**type**\: list of :py:class:`CbQosQueueingCfgEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosQueueingCfgTable.CbQosQueueingCfgEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqosqueueingcfgentry = YList()
            self.cbqosqueueingcfgentry.parent = self
            self.cbqosqueueingcfgentry.name = 'cbqosqueueingcfgentry'


        class CbQosQueueingCfgEntry(object):
            """
            Each entry in this table describes configuration
            information about a queueing action. The information 
            includes\: Bandwidth, Units, Flow Enabled, Priority Enabled, 
            and Q size.
            
            This table contains configuration information only,
            no statistics associated with it. Therefore, it is indexed
            by the cbQosConfigIndex of each Queueing Action.
            
            .. attribute:: cbqosconfigindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosqueueingcfgaggregateqlimit
            
            	Maximum allowed queue size for all the individual queues associated with this class. When the queue size exceed this value, the packets will be dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosqueueingcfgaggregateqsize
            
            	Maximum number of packets that can be held in all the individual queues associated with this class before packets are dropped.  cbQosQueueingCfgAggregateQSize object is superseded by  cbQosQueueingCfgAggregateQLimit
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cbqosqueueingcfgaggrqlimittime
            
            	Maximum allowed queue size in milli\-seconds for all individual queues associated with this class.  It is internally converted to bytes by using the bandwidth that is available for the class
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosqueueingcfgbandwidth
            
            	The type of bandwidth configuration value represented by this object is indicated by the value of cbQosQueueingCfgBandwidthUnits for this entry.   If the cbQosQueueingCfgBandwidthUnits value is 'kbps(1)' or  'percentage(2)', this object represents the configured   bandwidth allocated to this traffic class.In the case of a   bandwidth policy, this value represents a minimum bandwidth   guarantee for the traffic class. In the case of a priority   policy, this value represents the maximum rate at which   priority service is guaranteed.   If the cbQosQueueingCfgBandwidthUnits value is   'percentageRemaining(3)', this object represents the   the percentage of the unallocated bandwidth to allocate to  this class.  If the cbQosQueueingCfgBandwidthUnits value is   'ratioRemaining(4)', this object represents the ratio value,  relative to other class' configured ratio values, used to   determine the portion of the unallocated bandwidth to apply to  this class.  cbQosQueueingCfgBandwidth object is superseded by cbQosQueueingCfgBandwidth64
            	**type**\: int
            
            	**range:** 0..2000000
            
            .. attribute:: cbqosqueueingcfgbandwidth64
            
            	This object indicates the guaranteed bandwidth for a particular traffic class.  The type of bandwidth configuration value represented by this object is indicated by the value of cbQosQueueingCfgBandwidthUnits.   If the cbQosQueueingCfgBandwidthUnits value is 'kbps(1)' or  'percentage(2)', this object represents the configured   bandwidth allocated to this traffic class.In the case of a   bandwidth policy, this value represents a minimum bandwidth   guarantee for the traffic class. In the case of a priority   policy, this value represents the maximum rate at which   priority service is guaranteed.   If the cbQosQueueingCfgBandwidthUnits value is   'percentageRemaining(3)', this object represents the   the percentage of the unallocated bandwidth to allocate to  this class.  If the cbQosQueueingCfgBandwidthUnits value is   'ratioRemaining(4)', this object represents the ratio value,  relative to other class' configured ratio values, used to   determine the portion of the unallocated bandwidth to apply to  this class.  If a device implements cbQosQueueingCfgBandwidth64, it should not implement cbQosQueueingCfgBandwidth
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosqueueingcfgbandwidthunits
            
            	Units of the accompanying cbQosQueueingCfgbandwidth parameter
            	**type**\: :py:class:`QueueingBandwidthUnits_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.QueueingBandwidthUnits_Enum>`
            
            .. attribute:: cbqosqueueingcfgdynamicqnumber
            
            	Number of dynamic queues supported when flow\-based fair\-queue is in use
            	**type**\: int
            
            	**range:** 1..32768
            
            .. attribute:: cbqosqueueingcfgflowenabled
            
            	Boolean to indicate if flow\-based fair\-queue is enabled for this class
            	**type**\: bool
            
            .. attribute:: cbqosqueueingcfgindividualqsize
            
            	Maximum number of packets that can be held in an individual Flow\-based fair\-queue associated with this  class before it drops packets (once the AggregateQSize has been reached).  This field only makes sense in the context of  Flow\-based fair\-queueing.  cbQosQueueingCfgIndividualQSize object is superseded by cbQosQueueingCfgIndividualQSize64
            	**type**\: int
            
            	**range:** 1..32768
            
            .. attribute:: cbqosqueueingcfgindividualqsize64
            
            	Maximum number of packets that can be held in an individual Flow\-based fair\-queue associated with this  class before it drops packets (once the AggregateQSize has been reached).  If a device implements cbQosQueueingCfgIndividualQSize64, then it should not implement cbQosQueueingCfgIndividualQSize
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosqueueingcfgprioburstsize
            
            	In the priority queue, this is the number of bytes allowed in a single burst.  This parameter only makes sense if Priority is enabled
            	**type**\: int
            
            	**range:** 32..64000000
            
            .. attribute:: cbqosqueueingcfgpriorityenabled
            
            	Boolean to indicate if low latency queueing (priority) is enabled for this class
            	**type**\: bool
            
            .. attribute:: cbqosqueueingcfgprioritylevel
            
            	The priority level of the queue into which packets matching this  class are queued into. A larger priority level indicates higher  priority
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosqueueingcfgqlimitunits
            
            	Represents the unit type of cbQosQueueingCfgAggregateQLimit object
            	**type**\: :py:class:`CbQosQueueUnitType_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CbQosQueueUnitType_Enum>`
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosconfigindex = None
                self.cbqosqueueingcfgaggregateqlimit = None
                self.cbqosqueueingcfgaggregateqsize = None
                self.cbqosqueueingcfgaggrqlimittime = None
                self.cbqosqueueingcfgbandwidth = None
                self.cbqosqueueingcfgbandwidth64 = None
                self.cbqosqueueingcfgbandwidthunits = None
                self.cbqosqueueingcfgdynamicqnumber = None
                self.cbqosqueueingcfgflowenabled = None
                self.cbqosqueueingcfgindividualqsize = None
                self.cbqosqueueingcfgindividualqsize64 = None
                self.cbqosqueueingcfgprioburstsize = None
                self.cbqosqueueingcfgpriorityenabled = None
                self.cbqosqueueingcfgprioritylevel = None
                self.cbqosqueueingcfgqlimitunits = None

            @property
            def _common_path(self):
                if self.cbqosconfigindex is None:
                    raise YPYDataValidationError('Key property cbqosconfigindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosQueueingCfgTable/CISCO-CLASS-BASED-QOS-MIB:cbQosQueueingCfgEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosConfigIndex = ' + str(self.cbqosconfigindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosconfigindex is not None:
                    return True

                if self.cbqosqueueingcfgaggregateqlimit is not None:
                    return True

                if self.cbqosqueueingcfgaggregateqsize is not None:
                    return True

                if self.cbqosqueueingcfgaggrqlimittime is not None:
                    return True

                if self.cbqosqueueingcfgbandwidth is not None:
                    return True

                if self.cbqosqueueingcfgbandwidth64 is not None:
                    return True

                if self.cbqosqueueingcfgbandwidthunits is not None:
                    return True

                if self.cbqosqueueingcfgdynamicqnumber is not None:
                    return True

                if self.cbqosqueueingcfgflowenabled is not None:
                    return True

                if self.cbqosqueueingcfgindividualqsize is not None:
                    return True

                if self.cbqosqueueingcfgindividualqsize64 is not None:
                    return True

                if self.cbqosqueueingcfgprioburstsize is not None:
                    return True

                if self.cbqosqueueingcfgpriorityenabled is not None:
                    return True

                if self.cbqosqueueingcfgprioritylevel is not None:
                    return True

                if self.cbqosqueueingcfgqlimitunits is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosQueueingCfgTable.CbQosQueueingCfgEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosQueueingCfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqosqueueingcfgentry is not None:
                for child_ref in self.cbqosqueueingcfgentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosQueueingCfgTable']['meta_info']


    class CbQosQueueingClassCfgTable(object):
        """
        This table specifies the configuration information for weighted
        queue limit action per IP precedence basis.
        
        .. attribute:: cbqosqueueingclasscfgentry
        
        	Each entry in this table describes configuration information about a weighted queueing action. The information includes\: Threshold value, Units and wieght Type (ip,dscp,mplsExp)  This table contains configuration information only, no statistics associated with it. Therefore, it is indexed by the cbQosConfigIndex(which refers to cbQosConfigIndex of cbQosQueueingCfgEntry) and cbQosQueueingClassConfigIndex cbQosQlimitWeightValue   i.e(prec,dscp,discard\-class,qos\-group,atm\-clp, mplsExp) of each Weighted Queueing Action
        	**type**\: list of :py:class:`CbQosQueueingClassCfgEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosQueueingClassCfgTable.CbQosQueueingClassCfgEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqosqueueingclasscfgentry = YList()
            self.cbqosqueueingclasscfgentry.parent = self
            self.cbqosqueueingclasscfgentry.name = 'cbqosqueueingclasscfgentry'


        class CbQosQueueingClassCfgEntry(object):
            """
            Each entry in this table describes configuration
            information about a weighted queueing action. The information
            includes\: Threshold value, Units and wieght Type
            (ip,dscp,mplsExp)
            
            This table contains configuration information only,
            no statistics associated with it. Therefore, it is indexed
            by the cbQosConfigIndex(which refers to cbQosConfigIndex of
            cbQosQueueingCfgEntry) and cbQosQueueingClassConfigIndex
            cbQosQlimitWeightValue  
            i.e(prec,dscp,discard\-class,qos\-group,atm\-clp,
            mplsExp) of each Weighted Queueing Action.
            
            .. attribute:: cbqosconfigindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosqlimitweightvalue
            
            	This object depict the weight value configured for weighted Queue\-limit. The Weight value is IP precedence or IP DSCP of this entry
            	**type**\: int
            
            	**range:** 0..63
            
            .. attribute:: cbqosqueueingclassconfigindex
            
            	This objects depict the config index for Weighted  Queue limit configured
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cbqosqueueingclasscfgqlimitweight
            
            	This objects depict the weight value for Weighted Queue limit configured i.e(precedence,dscp,qos\-group,atm\-clp,discard\-class,mplsExp)      
            	**type**\: :py:class:`QueueMechanism_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.QueueMechanism_Enum>`
            
            .. attribute:: cbqosqueueingclasscfgthreshold
            
            	This object is used to depict the Threshold value for the Weighted Queue Limit
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosqueueingclasscfgthresholdunit
            
            	This object is used to depict the Threshold Unit for the Weighted Queue Limit
            	**type**\: :py:class:`CbQosQueueUnitType_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CbQosQueueUnitType_Enum>`
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosconfigindex = None
                self.cbqosqlimitweightvalue = None
                self.cbqosqueueingclassconfigindex = None
                self.cbqosqueueingclasscfgqlimitweight = None
                self.cbqosqueueingclasscfgthreshold = None
                self.cbqosqueueingclasscfgthresholdunit = None

            @property
            def _common_path(self):
                if self.cbqosconfigindex is None:
                    raise YPYDataValidationError('Key property cbqosconfigindex is None')
                if self.cbqosqlimitweightvalue is None:
                    raise YPYDataValidationError('Key property cbqosqlimitweightvalue is None')
                if self.cbqosqueueingclassconfigindex is None:
                    raise YPYDataValidationError('Key property cbqosqueueingclassconfigindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosQueueingClassCfgTable/CISCO-CLASS-BASED-QOS-MIB:cbQosQueueingClassCfgEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosConfigIndex = ' + str(self.cbqosconfigindex) + '][CISCO-CLASS-BASED-QOS-MIB:cbQosQlimitWeightValue = ' + str(self.cbqosqlimitweightvalue) + '][CISCO-CLASS-BASED-QOS-MIB:cbQosQueueingClassConfigIndex = ' + str(self.cbqosqueueingclassconfigindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosconfigindex is not None:
                    return True

                if self.cbqosqlimitweightvalue is not None:
                    return True

                if self.cbqosqueueingclassconfigindex is not None:
                    return True

                if self.cbqosqueueingclasscfgqlimitweight is not None:
                    return True

                if self.cbqosqueueingclasscfgthreshold is not None:
                    return True

                if self.cbqosqueueingclasscfgthresholdunit is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosQueueingClassCfgTable.CbQosQueueingClassCfgEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosQueueingClassCfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqosqueueingclasscfgentry is not None:
                for child_ref in self.cbqosqueueingclasscfgentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosQueueingClassCfgTable']['meta_info']


    class CbQosQueueingStatsTable(object):
        """
        This table specifies Queueing Action related Statistical
        information.
        
        .. attribute:: cbqosqueueingstatsentry
        
        	Each entry in this table describes the statistical information about queueing action. Queueing action specific  information you can find in this table are \:  various Q depth, and discard pkt/byte counters.  This table contains statistical information only, no configuration information associated with it.  Therefore, it is indexed by the instance specific IDs,  such as cbQosPolicyIndex and cbQosObjectsIndex
        	**type**\: list of :py:class:`CbQosQueueingStatsEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosQueueingStatsTable.CbQosQueueingStatsEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqosqueueingstatsentry = YList()
            self.cbqosqueueingstatsentry.parent = self
            self.cbqosqueueingstatsentry.name = 'cbqosqueueingstatsentry'


        class CbQosQueueingStatsEntry(object):
            """
            Each entry in this table describes the statistical
            information about queueing action. Queueing action specific 
            information you can find in this table are \: 
            various Q depth, and discard pkt/byte counters.
            
            This table contains statistical information only,
            no configuration information associated with it. 
            Therefore, it is indexed by the instance specific IDs, 
            such as cbQosPolicyIndex and cbQosObjectsIndex.
            
            .. attribute:: cbqosobjectsindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospolicyindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosqueueingcurrentqdepth
            
            	The current depth of the queue
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosqueueingcurrentqdepthpkt
            
            	The current number of packets sitting in the queue
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosqueueingdiscardbyte
            
            	The lower 32 bits count of octets, associated with this class, that were dropped by queueing
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosqueueingdiscardbyte64
            
            	The count of octets, associated with this class, that were dropped by queueing
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosqueueingdiscardbyteoverflow
            
            	The upper 32 bit count of octets, associated with this class, that were dropped by queueing
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosqueueingdiscardpkt
            
            	The number of packets, associated with this class, that were dropped by queueing
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosqueueingdiscardpkt64
            
            	The number of packets, associated with this class, that were dropped by queueing
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosqueueingdiscardpktoverflow
            
            	The upper 32 bits count of packets, associated with this class, that were dropped by queueing
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosqueueingmaxqdepth
            
            	The maximum depth of the queue
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosqueueingmaxqdepthpkt
            
            	The maximum depth of the queue in packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosqueueingtransmitbyte64
            
            	The count of octets, associated with this class, that were transmitted by queueing
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosqueueingtransmitpkt64
            
            	The number of packets, associated with this class, that were transmitted by queueing
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosobjectsindex = None
                self.cbqospolicyindex = None
                self.cbqosqueueingcurrentqdepth = None
                self.cbqosqueueingcurrentqdepthpkt = None
                self.cbqosqueueingdiscardbyte = None
                self.cbqosqueueingdiscardbyte64 = None
                self.cbqosqueueingdiscardbyteoverflow = None
                self.cbqosqueueingdiscardpkt = None
                self.cbqosqueueingdiscardpkt64 = None
                self.cbqosqueueingdiscardpktoverflow = None
                self.cbqosqueueingmaxqdepth = None
                self.cbqosqueueingmaxqdepthpkt = None
                self.cbqosqueueingtransmitbyte64 = None
                self.cbqosqueueingtransmitpkt64 = None

            @property
            def _common_path(self):
                if self.cbqosobjectsindex is None:
                    raise YPYDataValidationError('Key property cbqosobjectsindex is None')
                if self.cbqospolicyindex is None:
                    raise YPYDataValidationError('Key property cbqospolicyindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosQueueingStatsTable/CISCO-CLASS-BASED-QOS-MIB:cbQosQueueingStatsEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosObjectsIndex = ' + str(self.cbqosobjectsindex) + '][CISCO-CLASS-BASED-QOS-MIB:cbQosPolicyIndex = ' + str(self.cbqospolicyindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosobjectsindex is not None:
                    return True

                if self.cbqospolicyindex is not None:
                    return True

                if self.cbqosqueueingcurrentqdepth is not None:
                    return True

                if self.cbqosqueueingcurrentqdepthpkt is not None:
                    return True

                if self.cbqosqueueingdiscardbyte is not None:
                    return True

                if self.cbqosqueueingdiscardbyte64 is not None:
                    return True

                if self.cbqosqueueingdiscardbyteoverflow is not None:
                    return True

                if self.cbqosqueueingdiscardpkt is not None:
                    return True

                if self.cbqosqueueingdiscardpkt64 is not None:
                    return True

                if self.cbqosqueueingdiscardpktoverflow is not None:
                    return True

                if self.cbqosqueueingmaxqdepth is not None:
                    return True

                if self.cbqosqueueingmaxqdepthpkt is not None:
                    return True

                if self.cbqosqueueingtransmitbyte64 is not None:
                    return True

                if self.cbqosqueueingtransmitpkt64 is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosQueueingStatsTable.CbQosQueueingStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosQueueingStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqosqueueingstatsentry is not None:
                for child_ref in self.cbqosqueueingstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosQueueingStatsTable']['meta_info']


    class CbQosREDCfgTable(object):
        """
        This table specifies WRED Action configuration
        information
        
        .. attribute:: cbqosredcfgentry
        
        	Each entry in this table describes configuration information about a WRED Action.  The table holds global  (per traffic class) configuration like\: Expon Weight and Mean Q size.  This table contains configuration information only, no statistics associated with it. Therefore, it is indexed by the cbQosConfigIndex of each WRED Action
        	**type**\: list of :py:class:`CbQosREDCfgEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosREDCfgTable.CbQosREDCfgEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqosredcfgentry = YList()
            self.cbqosredcfgentry.parent = self
            self.cbqosredcfgentry.name = 'cbqosredcfgentry'


        class CbQosREDCfgEntry(object):
            """
            Each entry in this table describes configuration
            information about a WRED Action.  The table holds global 
            (per traffic class) configuration like\: Expon Weight
            and Mean Q size.
            
            This table contains configuration information only,
            no statistics associated with it. Therefore, it is indexed
            by the cbQosConfigIndex of each WRED Action.
            
            .. attribute:: cbqosconfigindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosredcfgdscpprec
            
            	The Classification mechanism used by RED
            	**type**\: :py:class:`REDMechanism_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.REDMechanism_Enum>`
            
            .. attribute:: cbqosredcfgecnenabled
            
            	Boolean to indicate if explicit congestion notification enabled for this class
            	**type**\: bool
            
            .. attribute:: cbqosredcfgexponweight
            
            	The decay factor for the queue average calculation. The decay factor is equal to raising 2 to the power  of N, where N could be up to 16.  The smaller the number, the faster it decays
            	**type**\: int
            
            	**range:** 1..16
            
            .. attribute:: cbqosredcfgmeanqsize
            
            	The average queue size, computed and used by the WRED algorithm. cbQosREDCfgMeanQsize object is superseded by  cbQosREDMeanQsize
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosconfigindex = None
                self.cbqosredcfgdscpprec = None
                self.cbqosredcfgecnenabled = None
                self.cbqosredcfgexponweight = None
                self.cbqosredcfgmeanqsize = None

            @property
            def _common_path(self):
                if self.cbqosconfigindex is None:
                    raise YPYDataValidationError('Key property cbqosconfigindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosREDCfgTable/CISCO-CLASS-BASED-QOS-MIB:cbQosREDCfgEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosConfigIndex = ' + str(self.cbqosconfigindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosconfigindex is not None:
                    return True

                if self.cbqosredcfgdscpprec is not None:
                    return True

                if self.cbqosredcfgecnenabled is not None:
                    return True

                if self.cbqosredcfgexponweight is not None:
                    return True

                if self.cbqosredcfgmeanqsize is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosREDCfgTable.CbQosREDCfgEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosREDCfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqosredcfgentry is not None:
                for child_ref in self.cbqosredcfgentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosREDCfgTable']['meta_info']


    class CbQosREDClassCfgTable(object):
        """
        This table specifies WRED Action configuration
        information on a per IP precedence basis.
        
        .. attribute:: cbqosredclasscfgentry
        
        	Each entry in this table describes configuration information about a WRED Action.  The table holds the per IP precedence based WRED configuration parameters.   This table contains configuration information only, no statistics associated with it. Therefore, it is indexed by the cbQosConfigIndex and cbQosREDValue  of each WRED Action
        	**type**\: list of :py:class:`CbQosREDClassCfgEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosREDClassCfgTable.CbQosREDClassCfgEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqosredclasscfgentry = YList()
            self.cbqosredclasscfgentry.parent = self
            self.cbqosredclasscfgentry.name = 'cbqosredclasscfgentry'


        class CbQosREDClassCfgEntry(object):
            """
            Each entry in this table describes configuration information
            about a WRED Action.  The table holds the per IP precedence
            based WRED configuration parameters. 
            
            This table contains configuration information only,
            no statistics associated with it. Therefore, it is indexed
            by the cbQosConfigIndex and cbQosREDValue 
            of each WRED Action.
            
            .. attribute:: cbqosconfigindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosredvalue
            
            	The IP precedence or IP DSCP of this entry
            	**type**\: int
            
            	**range:** 0..63
            
            .. attribute:: cbqosredcfgmaxthreshold
            
            	Maximum threshold in number of packets. When the average queue length exceeds this number, WRED drops  all packets with the specified IP precedence. cbQosREDCfgMaxThreshold object is superseded by  cbQosREDClassCfgMaxThreshold
            	**type**\: int
            
            	**range:** 1..32768
            
            .. attribute:: cbqosredcfgminthreshold
            
            	Minimum threshold in number of packets. When the average queue length reaches this number, WRED begins  to drop packets with the specified IP precedence. cbQosREDCfgMinThreshold object is superseded by  cbQosREDClassCfgMinThreshold
            	**type**\: int
            
            	**range:** 1..32768
            
            .. attribute:: cbqosredcfgpktdropprob
            
            	Denominator for the fraction of packets dropped when the average queue depth is MaxDepthThreshold. For  example, if the denominator is 10, one out of every 10 packets is dropped when the average queue is at the  MaxDepthThreshold
            	**type**\: int
            
            	**range:** 1..65536
            
            .. attribute:: cbqosredclasscfgmaxthreshold
            
            	The maximum WRED threshold value. When the average queue length exceeds this number, WRED drops all  packets according to REDMechanism specificed in cbQosREDCfgDscpPrec
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosredclasscfgmaxthresholdtime
            
            	The maximum WRED threshold value specified in milli\-seconds.  The milli\-second value is internally converted to bytes by using the bandwidth that is available for the class
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosredclasscfgmaxthresholdunit
            
            	Represents the unit type to measure the RED Maximum thresholds. The objects covered is cbQosREDClassCfgMaxThreshold
            	**type**\: :py:class:`CbQosQueueUnitType_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CbQosQueueUnitType_Enum>`
            
            .. attribute:: cbqosredclasscfgminthreshold
            
            	The minimum WRED threshold value. When the average queue length reaches this number, WRED begins to  drop packets according to REDMechanism specificed in cbQosREDCfgDscpPrec
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosredclasscfgminthresholdtime
            
            	The minimum WRED threshold value specified in milli\-seconds.  The milli\-second value is internally converted to bytes by using the bandwidth that is available for the class
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosredclasscfgminthresholdunit
            
            	Represents the unit type to measure the RED Minimum thresholds. The objects covered is cbQosREDClassCfgMinThreshold
            	**type**\: :py:class:`CbQosQueueUnitType_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CbQosQueueUnitType_Enum>`
            
            .. attribute:: cbqosredclasscfgthresholdunit
            
            	Represents the unit type to measure the RED thresholds. The objects covered are cbQosREDClassCfgMinThreshold and cbQosREDClassCfgMaxThreshold cbQosREDClassCfgThresholdUnit object is superseded by  cbQosREDClassCfgMinThreshold, cbQosREDClassCfgMaxThreshold
            	**type**\: :py:class:`CbQosQueueUnitType_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CbQosQueueUnitType_Enum>`
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosconfigindex = None
                self.cbqosredvalue = None
                self.cbqosredcfgmaxthreshold = None
                self.cbqosredcfgminthreshold = None
                self.cbqosredcfgpktdropprob = None
                self.cbqosredclasscfgmaxthreshold = None
                self.cbqosredclasscfgmaxthresholdtime = None
                self.cbqosredclasscfgmaxthresholdunit = None
                self.cbqosredclasscfgminthreshold = None
                self.cbqosredclasscfgminthresholdtime = None
                self.cbqosredclasscfgminthresholdunit = None
                self.cbqosredclasscfgthresholdunit = None

            @property
            def _common_path(self):
                if self.cbqosconfigindex is None:
                    raise YPYDataValidationError('Key property cbqosconfigindex is None')
                if self.cbqosredvalue is None:
                    raise YPYDataValidationError('Key property cbqosredvalue is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosREDClassCfgTable/CISCO-CLASS-BASED-QOS-MIB:cbQosREDClassCfgEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosConfigIndex = ' + str(self.cbqosconfigindex) + '][CISCO-CLASS-BASED-QOS-MIB:cbQosREDValue = ' + str(self.cbqosredvalue) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosconfigindex is not None:
                    return True

                if self.cbqosredvalue is not None:
                    return True

                if self.cbqosredcfgmaxthreshold is not None:
                    return True

                if self.cbqosredcfgminthreshold is not None:
                    return True

                if self.cbqosredcfgpktdropprob is not None:
                    return True

                if self.cbqosredclasscfgmaxthreshold is not None:
                    return True

                if self.cbqosredclasscfgmaxthresholdtime is not None:
                    return True

                if self.cbqosredclasscfgmaxthresholdunit is not None:
                    return True

                if self.cbqosredclasscfgminthreshold is not None:
                    return True

                if self.cbqosredclasscfgminthresholdtime is not None:
                    return True

                if self.cbqosredclasscfgminthresholdunit is not None:
                    return True

                if self.cbqosredclasscfgthresholdunit is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosREDClassCfgTable.CbQosREDClassCfgEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosREDClassCfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqosredclasscfgentry is not None:
                for child_ref in self.cbqosredclasscfgentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosREDClassCfgTable']['meta_info']


    class CbQosREDClassStatsTable(object):
        """
        This table specifies per Precedence WRED Action related
        Statistical information.
        
        .. attribute:: cbqosredclassstatsentry
        
        	Each entry in this table describes the statistical information about per Precedence WRED Action. per Precedence WRED Action specific information you can find in this table  are \: Random pkt/byte counters, and Tail drop pkt/byte  counters.  This table contains per Precedence/dscp based statistical  information only, no configuration information associated  with it.  Therefore, it is indexed by the instance specific  IDs, and a per Precedence identifier\:  cbQosPolicyIndex, cbQosObjectsIndex and cbQosREDValue
        	**type**\: list of :py:class:`CbQosREDClassStatsEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosREDClassStatsTable.CbQosREDClassStatsEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqosredclassstatsentry = YList()
            self.cbqosredclassstatsentry.parent = self
            self.cbqosredclassstatsentry.name = 'cbqosredclassstatsentry'


        class CbQosREDClassStatsEntry(object):
            """
            Each entry in this table describes the statistical
            information about per Precedence WRED Action. per Precedence
            WRED Action specific information you can find in this table 
            are \: Random pkt/byte counters, and Tail drop pkt/byte 
            counters.
            
            This table contains per Precedence/dscp based statistical 
            information only, no configuration information associated 
            with it.  Therefore, it is indexed by the instance specific 
            IDs, and a per Precedence identifier\: 
            cbQosPolicyIndex, cbQosObjectsIndex and cbQosREDValue.
            
            .. attribute:: cbqosobjectsindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospolicyindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosredvalue
            
            	
            	**type**\: int
            
            	**range:** 0..63
            
            .. attribute:: cbqosredecnmarkbyte
            
            	The lower 32 bits count of bytes ecn marked when the number of packets in the associated queue was  greater than the minimum threshold and less than the maximum threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosredecnmarkbyte64
            
            	The 64 bits count of bytes ecn marked when the number of packets in the associated queue was  greater than the minimum threshold and less than the maximum threshold
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosredecnmarkbyteoverflow
            
            	The upper 32 bits count of bytes ecn marked when the number of packets in the associated queue was  greater than the minimum threshold and less than the maximum threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosredecnmarkpkt
            
            	The lower 32 bits count of packets ecn marked when the number of packets in the associated queue was  greater than the minimum threshold and less than the maximum threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosredecnmarkpkt64
            
            	The 64 bits count of packets ecn marked when the number of packets in the associated queue was  greater than the minimum threshold and less than  the maximum threshold
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosredecnmarkpktoverflow
            
            	The upper 32 bits count of packets ecn marked when the number of packets in the associated queue was greater than the minimum threshold and less than the maximum threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosredmeanqsize
            
            	The average queue size computed and used by the WRED algorithm
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosredmeanqsizeunits
            
            	Represents the unit type of cbQosREDMeanQSize object
            	**type**\: :py:class:`CbQosQueueUnitType_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CbQosQueueUnitType_Enum>`
            
            .. attribute:: cbqosredrandomdropbyte
            
            	The lower 32 bits count of bytes dropped when the number of packets in the associated queue was  greater than the minimum threshold and less than the maximum threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosredrandomdropbyte64
            
            	The 64 bits count of bytes dropped when the number of packets in the associated queue was greater than the minimum threshold and less than the maximum threshold
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosredrandomdropbyteoverflow
            
            	The upper 32 bits count of bytes dropped when the number of packets in the associated queue was greater than the minimum threshold and less than the maximum threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosredrandomdroppkt
            
            	The lower 32 bits count of packets dropped when the number of packets in the associated queue was  greater than the minimum threshold and less than the maximum threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosredrandomdroppkt64
            
            	The 64 bits count of packets dropped when the number of packets in the associated queue was greater  than the minimum threshold and less than the maximum threshold
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosredrandomdroppktoverflow
            
            	The upper 32 bits count of packets dropped when the number of packets in the associated queue was greater than the minimum threshold and less than the maximum threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosredtaildropbyte
            
            	The lower 32 bits count of bytes dropped when the number of packets in the associated queue was greater than the maximum threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosredtaildropbyte64
            
            	The 64 bits count of bytes dropped when the number of packets in the associated queue was greater than the maximum threshold
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosredtaildropbyteoverflow
            
            	The upper 32 bits count of bytes dropped when the number of packets in the associated queue was greater than the maximum threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosredtaildroppkt
            
            	The lower 32 bits count of packets dropped when the number of packets in the associated queue was greater than the maximum threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosredtaildroppkt64
            
            	The 64 bits count of packets dropped when the number of packets in the associated queue was greater than the maximum threshold
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosredtaildroppktoverflow
            
            	The upper 32 bits count of packets dropped when the number of packets in the associated queue was greater than the maximum threshold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosredtransmitbyte
            
            	The lower 32 bits count of octets trasmitted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosredtransmitbyte64
            
            	The 64 bits count of octets transmitted
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosredtransmitbyteoverflow
            
            	The upper 32 bits count of octets transmitted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosredtransmitpkt
            
            	The lower 32 bits count of bytes trasmitted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosredtransmitpkt64
            
            	The 64 bits count of packets transmitted
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqosredtransmitpktoverflow
            
            	The upper 32 bits count of bytes transmitted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosobjectsindex = None
                self.cbqospolicyindex = None
                self.cbqosredvalue = None
                self.cbqosredecnmarkbyte = None
                self.cbqosredecnmarkbyte64 = None
                self.cbqosredecnmarkbyteoverflow = None
                self.cbqosredecnmarkpkt = None
                self.cbqosredecnmarkpkt64 = None
                self.cbqosredecnmarkpktoverflow = None
                self.cbqosredmeanqsize = None
                self.cbqosredmeanqsizeunits = None
                self.cbqosredrandomdropbyte = None
                self.cbqosredrandomdropbyte64 = None
                self.cbqosredrandomdropbyteoverflow = None
                self.cbqosredrandomdroppkt = None
                self.cbqosredrandomdroppkt64 = None
                self.cbqosredrandomdroppktoverflow = None
                self.cbqosredtaildropbyte = None
                self.cbqosredtaildropbyte64 = None
                self.cbqosredtaildropbyteoverflow = None
                self.cbqosredtaildroppkt = None
                self.cbqosredtaildroppkt64 = None
                self.cbqosredtaildroppktoverflow = None
                self.cbqosredtransmitbyte = None
                self.cbqosredtransmitbyte64 = None
                self.cbqosredtransmitbyteoverflow = None
                self.cbqosredtransmitpkt = None
                self.cbqosredtransmitpkt64 = None
                self.cbqosredtransmitpktoverflow = None

            @property
            def _common_path(self):
                if self.cbqosobjectsindex is None:
                    raise YPYDataValidationError('Key property cbqosobjectsindex is None')
                if self.cbqospolicyindex is None:
                    raise YPYDataValidationError('Key property cbqospolicyindex is None')
                if self.cbqosredvalue is None:
                    raise YPYDataValidationError('Key property cbqosredvalue is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosREDClassStatsTable/CISCO-CLASS-BASED-QOS-MIB:cbQosREDClassStatsEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosObjectsIndex = ' + str(self.cbqosobjectsindex) + '][CISCO-CLASS-BASED-QOS-MIB:cbQosPolicyIndex = ' + str(self.cbqospolicyindex) + '][CISCO-CLASS-BASED-QOS-MIB:cbQosREDValue = ' + str(self.cbqosredvalue) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosobjectsindex is not None:
                    return True

                if self.cbqospolicyindex is not None:
                    return True

                if self.cbqosredvalue is not None:
                    return True

                if self.cbqosredecnmarkbyte is not None:
                    return True

                if self.cbqosredecnmarkbyte64 is not None:
                    return True

                if self.cbqosredecnmarkbyteoverflow is not None:
                    return True

                if self.cbqosredecnmarkpkt is not None:
                    return True

                if self.cbqosredecnmarkpkt64 is not None:
                    return True

                if self.cbqosredecnmarkpktoverflow is not None:
                    return True

                if self.cbqosredmeanqsize is not None:
                    return True

                if self.cbqosredmeanqsizeunits is not None:
                    return True

                if self.cbqosredrandomdropbyte is not None:
                    return True

                if self.cbqosredrandomdropbyte64 is not None:
                    return True

                if self.cbqosredrandomdropbyteoverflow is not None:
                    return True

                if self.cbqosredrandomdroppkt is not None:
                    return True

                if self.cbqosredrandomdroppkt64 is not None:
                    return True

                if self.cbqosredrandomdroppktoverflow is not None:
                    return True

                if self.cbqosredtaildropbyte is not None:
                    return True

                if self.cbqosredtaildropbyte64 is not None:
                    return True

                if self.cbqosredtaildropbyteoverflow is not None:
                    return True

                if self.cbqosredtaildroppkt is not None:
                    return True

                if self.cbqosredtaildroppkt64 is not None:
                    return True

                if self.cbqosredtaildroppktoverflow is not None:
                    return True

                if self.cbqosredtransmitbyte is not None:
                    return True

                if self.cbqosredtransmitbyte64 is not None:
                    return True

                if self.cbqosredtransmitbyteoverflow is not None:
                    return True

                if self.cbqosredtransmitpkt is not None:
                    return True

                if self.cbqosredtransmitpkt64 is not None:
                    return True

                if self.cbqosredtransmitpktoverflow is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosREDClassStatsTable.CbQosREDClassStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosREDClassStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqosredclassstatsentry is not None:
                for child_ref in self.cbqosredclassstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosREDClassStatsTable']['meta_info']


    class CbQosServicePolicyTable(object):
        """
        This table describes the logical interfaces/media types
        and the policymap that are attached to it.
        
        .. attribute:: cbqosservicepolicyentry
        
        	Each entry in this table describes to which a logical interface a given policymap is attached.  Depending on  the logical interface/media type, some fields may have meaningful values, and some may not.  Please see each individual descriptions
        	**type**\: list of :py:class:`CbQosServicePolicyEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosServicePolicyTable.CbQosServicePolicyEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqosservicepolicyentry = YList()
            self.cbqosservicepolicyentry.parent = self
            self.cbqosservicepolicyentry.name = 'cbqosservicepolicyentry'


        class CbQosServicePolicyEntry(object):
            """
            Each entry in this table describes to which a logical
            interface a given policymap is attached.  Depending on 
            the logical interface/media type, some fields may have
            meaningful values, and some may not.  Please see each
            individual descriptions.
            
            .. attribute:: cbqospolicyindex
            
            	An arbitrary (system\-assigned) index for all service policies (PolicyMap that has been attached to a given logical interface)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosatmvci
            
            	VCI for the ATMVC to which this service is attached. This field only make sense if the service policy is attached to a ATM VC
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cbqosatmvpi
            
            	VPI for the ATMVC to which this service is attached. This field only make sense if the service policy is attached to a ATM VC
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: cbqosentityindex
            
            	In cases where the policy is attached to an entity e.g. control\-plane, this object represents the entity physical index of the entity to which the policy has been attached. A value zero may be  returned if the policy is not attached to a physical entity or the entPhysicalTable is not supported on  the SNMP agent
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cbqosevc
            
            	for the EVC to which this service is attached. This field only make sense if the service policy is attached to an EVC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosfrdlci
            
            	DLCI for the FRVC to which this service is attached. This field only make sense if the service policy is attached to a Frame Relay DLCI
            	**type**\: int
            
            	**range:** 0..1023
            
            .. attribute:: cbqosifindex
            
            	ifIndex for the interface to which this service is attached. This field makes sense only if the logical interface has a snmp ifIndex. For e.g. the value of this field is meaningless when the cbQosIfType is controlPlane
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cbqosiftype
            
            	This describes the logical interface/media type to which this service policy is attached
            	**type**\: :py:class:`InterfaceType_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.InterfaceType_Enum>`
            
            .. attribute:: cbqosparentpolicyindex
            
            	The value refering to service\-policy index of a virtual interface on which PolicyMap applied directly. Value set would imply the entry is for a physical interface which is a member of a virtual interface. Value zero implies the entry is for a  interface on which PolicyMap applied directly
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospolicydirection
            
            	This indicates the direction of traffic for which this service policy is applied
            	**type**\: :py:class:`TrafficDirection_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.TrafficDirection_Enum>`
            
            .. attribute:: cbqospolicydiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more objects of cbQosServicePolicyEntry table for a given instance suffered a discontinuity. If no such discontinuities have occurred since the last re\-initialization of the local management subsystem, this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqosvlanindex
            
            	If the service policy is attached to a particular vlan on a trunk or multi\-vlan access port, then this object specifies the corresponding VLAN. In all other cases the value of this object is '0'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqospolicyindex = None
                self.cbqosatmvci = None
                self.cbqosatmvpi = None
                self.cbqosentityindex = None
                self.cbqosevc = None
                self.cbqosfrdlci = None
                self.cbqosifindex = None
                self.cbqosiftype = None
                self.cbqosparentpolicyindex = None
                self.cbqospolicydirection = None
                self.cbqospolicydiscontinuitytime = None
                self.cbqosvlanindex = None

            @property
            def _common_path(self):
                if self.cbqospolicyindex is None:
                    raise YPYDataValidationError('Key property cbqospolicyindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosServicePolicyTable/CISCO-CLASS-BASED-QOS-MIB:cbQosServicePolicyEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosPolicyIndex = ' + str(self.cbqospolicyindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqospolicyindex is not None:
                    return True

                if self.cbqosatmvci is not None:
                    return True

                if self.cbqosatmvpi is not None:
                    return True

                if self.cbqosentityindex is not None:
                    return True

                if self.cbqosevc is not None:
                    return True

                if self.cbqosfrdlci is not None:
                    return True

                if self.cbqosifindex is not None:
                    return True

                if self.cbqosiftype is not None:
                    return True

                if self.cbqosparentpolicyindex is not None:
                    return True

                if self.cbqospolicydirection is not None:
                    return True

                if self.cbqospolicydiscontinuitytime is not None:
                    return True

                if self.cbqosvlanindex is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosServicePolicyTable.CbQosServicePolicyEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosServicePolicyTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqosservicepolicyentry is not None:
                for child_ref in self.cbqosservicepolicyentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosServicePolicyTable']['meta_info']


    class CbQosSetCfgTable(object):
        """
        This table specifies Packet Marking Action configuration
        information.
        
        .. attribute:: cbqossetcfgentry
        
        	Each entry in this table describes configuration information about a Packet Marking Action.  The table holds Packet Marking configuration parameters, such as type of packet marking and values being set to.  This table contains configuration information only, no statistics associated with it. Therefore, it is indexed by the cbQosConfigIndex
        	**type**\: list of :py:class:`CbQosSetCfgEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosSetCfgTable.CbQosSetCfgEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqossetcfgentry = YList()
            self.cbqossetcfgentry.parent = self
            self.cbqossetcfgentry.name = 'cbqossetcfgentry'


        class CbQosSetCfgEntry(object):
            """
            Each entry in this table describes configuration information
            about a Packet Marking Action.  The table holds Packet
            Marking configuration parameters, such as type of packet
            marking and values being set to.
            
            This table contains configuration information only,
            no statistics associated with it. Therefore, it is indexed
            by the cbQosConfigIndex.
            
            .. attribute:: cbqosconfigindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqossetcfgdei
            
            	Indicates whether the DEI bit is set in the topmost 802.1ad header
            	**type**\: bool
            
            .. attribute:: cbqossetcfgdeiimposition
            
            	Indicates whether the DEI bit is set in the imposed 802.1ad header
            	**type**\: bool
            
            .. attribute:: cbqossetcfgdiscardclassvalue
            
            	The Discard Class value at which the packet is being set by the packet marking feature
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: cbqossetcfgfeature
            
            	The bit\-wise position of each packet marking feature
            	**type**\: :py:class:`SetFeatureType_Bits <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.SetFeatureType_Bits>`
            
            .. attribute:: cbqossetcfgfrde
            
            	The Discard Eligibility (DE) bit is used to indicate that a frame has lower importance than other frames. The DE bit is part of the Address field in the Frame Relay frame header.     DTE devices can set the value of the DE bit of a frame to 1 to indicate that the frame has lower importance than other frames. When the network becomes congested, DCE devices will discard frames with the DE bit set before discarding those that do not. This reduces the likelihood of critical data being dropped by Frame Relay DCE devices during periods of congestion
            	**type**\: bool
            
            .. attribute:: cbqossetcfgfrfecnbecn
            
            	This is a configurable parameter in percentage of the queue size.  When the current queue size out of the queue limit is greater than this parameter, both  Frame Relay FECN and BECN bits will be set for Frame Relay congestion notification mechanism
            	**type**\: int
            
            	**range:** 0..99
            
            .. attribute:: cbqossetcfgipdscptunnelvalue
            
            	The IP DSCP value at which the packet is being set by the packet marking feature
            	**type**\: int
            
            	**range:** 0..63
            
            .. attribute:: cbqossetcfgipdscpvalue
            
            	The IP DSCP value at which the packet is being set by the packet marking feature
            	**type**\: int
            
            	**range:** 0..63
            
            .. attribute:: cbqossetcfgipprecedencetunnelvalue
            
            	The IP precedence value at which the packet is being set by the packet marking feature
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: cbqossetcfgipprecedencevalue
            
            	The IP precedence value at which the packet is being set by the packet marking feature
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: cbqossetcfgl2cosinnervalue
            
            	The value to be set in the 802.1p priority field in the inner 802.1q VLAN tag (QinQ).  This object is applicable when cbQosSetCfgFeature has the 'l2CosInner' bit set
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: cbqossetcfgl2cosvalue
            
            	The Layer 2 Cos value at which the packet is being set by the packet marking feature
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: cbqossetcfgmplsexptopmostvalue
            
            	The MPLS experimental value on the topmost label at which the packet is being set by the packet marking feature
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: cbqossetcfgmplsexpvalue
            
            	The MPLS experimental value at which the packet is being set by the packet marking feature
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: cbqossetcfgqosgroupvalue
            
            	The QoS Group number at which the packet is being set by the packet marking feature
            	**type**\: int
            
            	**range:** 0..99
            
            .. attribute:: cbqossetcfgsrppriority
            
            	The SRP Priority value at which the packet is being set by the packet marking feature.  The higher the value the higher the priority.  SRP is a Cisco developed protocol. RFC 2892\: The Cisco SRP MAC Layer Protocol
            	**type**\: int
            
            	**range:** 0..7
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosconfigindex = None
                self.cbqossetcfgdei = None
                self.cbqossetcfgdeiimposition = None
                self.cbqossetcfgdiscardclassvalue = None
                self.cbqossetcfgfeature = SetFeatureType_Bits()
                self.cbqossetcfgfrde = None
                self.cbqossetcfgfrfecnbecn = None
                self.cbqossetcfgipdscptunnelvalue = None
                self.cbqossetcfgipdscpvalue = None
                self.cbqossetcfgipprecedencetunnelvalue = None
                self.cbqossetcfgipprecedencevalue = None
                self.cbqossetcfgl2cosinnervalue = None
                self.cbqossetcfgl2cosvalue = None
                self.cbqossetcfgmplsexptopmostvalue = None
                self.cbqossetcfgmplsexpvalue = None
                self.cbqossetcfgqosgroupvalue = None
                self.cbqossetcfgsrppriority = None

            @property
            def _common_path(self):
                if self.cbqosconfigindex is None:
                    raise YPYDataValidationError('Key property cbqosconfigindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosSetCfgTable/CISCO-CLASS-BASED-QOS-MIB:cbQosSetCfgEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosConfigIndex = ' + str(self.cbqosconfigindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosconfigindex is not None:
                    return True

                if self.cbqossetcfgdei is not None:
                    return True

                if self.cbqossetcfgdeiimposition is not None:
                    return True

                if self.cbqossetcfgdiscardclassvalue is not None:
                    return True

                if self.cbqossetcfgfeature is not None:
                    if self.cbqossetcfgfeature._has_data():
                        return True

                if self.cbqossetcfgfrde is not None:
                    return True

                if self.cbqossetcfgfrfecnbecn is not None:
                    return True

                if self.cbqossetcfgipdscptunnelvalue is not None:
                    return True

                if self.cbqossetcfgipdscpvalue is not None:
                    return True

                if self.cbqossetcfgipprecedencetunnelvalue is not None:
                    return True

                if self.cbqossetcfgipprecedencevalue is not None:
                    return True

                if self.cbqossetcfgl2cosinnervalue is not None:
                    return True

                if self.cbqossetcfgl2cosvalue is not None:
                    return True

                if self.cbqossetcfgmplsexptopmostvalue is not None:
                    return True

                if self.cbqossetcfgmplsexpvalue is not None:
                    return True

                if self.cbqossetcfgqosgroupvalue is not None:
                    return True

                if self.cbqossetcfgsrppriority is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosSetCfgTable.CbQosSetCfgEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosSetCfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqossetcfgentry is not None:
                for child_ref in self.cbqossetcfgentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosSetCfgTable']['meta_info']


    class CbQosSetStatsTable(object):
        """
        This table specifies packet marking statistical
        information.
        
        .. attribute:: cbqossetstatsentry
        
        	Each entry in this table describes the packets that marked by each marking type.  This table contains statistical information only, no configuration information associated with it. Therefore, it is indexed by the instance specific IDs, namely cbQosPolicyIndex and cbQosObjectsIndex
        	**type**\: list of :py:class:`CbQosSetStatsEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosSetStatsTable.CbQosSetStatsEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqossetstatsentry = YList()
            self.cbqossetstatsentry.parent = self
            self.cbqossetstatsentry.name = 'cbqossetstatsentry'


        class CbQosSetStatsEntry(object):
            """
            Each entry in this table describes the packets that
            marked by each marking type.
            
            This table contains statistical information only,
            no configuration information associated with it.
            Therefore, it is indexed by the instance specific
            IDs, namely cbQosPolicyIndex and cbQosObjectsIndex.
            
            .. attribute:: cbqosobjectsindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospolicyindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqossetatmclppkt64
            
            	The 64 bits count of packets whose ATM CLP Bit is marked by Set feature
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqossetdiscardclasspkt64
            
            	The 64 bits count of packets whose Discard Class field is marked by Set feature
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqossetdscppkt64
            
            	The 64 bits count of packets whose DSCP field is marked by Set feature
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqossetdscptunnelpkt64
            
            	The 64 bits count of packets whose DSCP Tunnel field is marked by Set feature
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqossetfrdepkt64
            
            	The 64 bits count of packets whose Frame Relay DE Bit is marked by Set feature
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqossetfrfecnbecnpkt64
            
            	The 64 bits count of packets whose Frame Relay FECN BECN field is marked by Set feature
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqossetl2cospkt64
            
            	The 64 bits count of packets whose Layer 2 Cos field is marked by Set feature
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqossetmplsexpimpositionpkt64
            
            	The 64 bits count of packets whose MPLS Experimental Imposition field is marked by Set feature
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqossetmplsexptopmostpkt64
            
            	The 64 bits count of packets whose MPLS Experimental TopMost field is marked by Set feature
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqossetprecedencepkt64
            
            	The 64 bits count of packets whose Precedence field is marked by Set feature
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqossetprecedencetunnelpkt64
            
            	The 64 bits count of packets whose Precedence Tunnel field is marked by Set feature
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqossetqosgrouppkt64
            
            	The 64 bits count of packets whose Qos Group field is marked by Set feature
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqossetsrpprioritypkt64
            
            	The 64 bits count of packets whose SRP Priority field is marked by Set feature
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosobjectsindex = None
                self.cbqospolicyindex = None
                self.cbqossetatmclppkt64 = None
                self.cbqossetdiscardclasspkt64 = None
                self.cbqossetdscppkt64 = None
                self.cbqossetdscptunnelpkt64 = None
                self.cbqossetfrdepkt64 = None
                self.cbqossetfrfecnbecnpkt64 = None
                self.cbqossetl2cospkt64 = None
                self.cbqossetmplsexpimpositionpkt64 = None
                self.cbqossetmplsexptopmostpkt64 = None
                self.cbqossetprecedencepkt64 = None
                self.cbqossetprecedencetunnelpkt64 = None
                self.cbqossetqosgrouppkt64 = None
                self.cbqossetsrpprioritypkt64 = None

            @property
            def _common_path(self):
                if self.cbqosobjectsindex is None:
                    raise YPYDataValidationError('Key property cbqosobjectsindex is None')
                if self.cbqospolicyindex is None:
                    raise YPYDataValidationError('Key property cbqospolicyindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosSetStatsTable/CISCO-CLASS-BASED-QOS-MIB:cbQosSetStatsEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosObjectsIndex = ' + str(self.cbqosobjectsindex) + '][CISCO-CLASS-BASED-QOS-MIB:cbQosPolicyIndex = ' + str(self.cbqospolicyindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosobjectsindex is not None:
                    return True

                if self.cbqospolicyindex is not None:
                    return True

                if self.cbqossetatmclppkt64 is not None:
                    return True

                if self.cbqossetdiscardclasspkt64 is not None:
                    return True

                if self.cbqossetdscppkt64 is not None:
                    return True

                if self.cbqossetdscptunnelpkt64 is not None:
                    return True

                if self.cbqossetfrdepkt64 is not None:
                    return True

                if self.cbqossetfrfecnbecnpkt64 is not None:
                    return True

                if self.cbqossetl2cospkt64 is not None:
                    return True

                if self.cbqossetmplsexpimpositionpkt64 is not None:
                    return True

                if self.cbqossetmplsexptopmostpkt64 is not None:
                    return True

                if self.cbqossetprecedencepkt64 is not None:
                    return True

                if self.cbqossetprecedencetunnelpkt64 is not None:
                    return True

                if self.cbqossetqosgrouppkt64 is not None:
                    return True

                if self.cbqossetsrpprioritypkt64 is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosSetStatsTable.CbQosSetStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosSetStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqossetstatsentry is not None:
                for child_ref in self.cbqossetstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosSetStatsTable']['meta_info']


    class CbQosTSCfgTable(object):
        """
        This table specifies traffic\-shaping Action configuration
        information.
        
        .. attribute:: cbqostscfgentry
        
        	Each entry in this table describes configuration information about a traffic\-shaping Action.  The table holds Traffic Shaping configuration parameters, such as rate, burst size,  and Shaping types.  This table contains configuration information only, no statistics associated with it. Therefore, it is indexed by the cbQosConfigIndex
        	**type**\: list of :py:class:`CbQosTSCfgEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosTSCfgTable.CbQosTSCfgEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqostscfgentry = YList()
            self.cbqostscfgentry.parent = self
            self.cbqostscfgentry.name = 'cbqostscfgentry'


        class CbQosTSCfgEntry(object):
            """
            Each entry in this table describes configuration information
            about a traffic\-shaping Action.  The table holds Traffic
            Shaping configuration parameters, such as rate, burst size, 
            and Shaping types.
            
            This table contains configuration information only,
            no statistics associated with it. Therefore, it is indexed
            by the cbQosConfigIndex.
            
            .. attribute:: cbqosconfigindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqostscfgadaptiveenabled
            
            	This object indicates is adaptive traffic\-shaping has been enabled
            	**type**\: bool
            
            .. attribute:: cbqostscfgadaptiverate
            
            	This object represents the current adaptive traffic shaping rate
            	**type**\: int
            
            	**range:** 8000..154400000
            
            .. attribute:: cbqostscfgburstsize
            
            	The amount of traffic, in bits, in excess of the committed traffic\-shaping rate that will be instantaneously permitted by this feature.  cbQosTSCfgBurstSize object is superseded by cbQosTSCfgBurstSize64
            	**type**\: int
            
            	**range:** 256..154400000
            
            .. attribute:: cbqostscfgburstsize64
            
            	This object indicates the the amount of traffic, in bits, in excess of the committed traffic\-shaping rate that will be instantaneously permitted by this feature.  If a device implements cbQosTSCfgBurstSize64, then it should not implement cbQosTSCfgBurstSize
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqostscfgbursttime
            
            	The amount of traffic, in ms, in excess of the committed traffic\-shaping rate that will be instantaneously permitted by this feature. The milli\-second value is internally converted to bits by using the bandwidth that is available for the class
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqostscfgextburstsize
            
            	The amount of traffic, in bits, in excess of the burst limit, which may be conditionally permitted by traffic\-shaping feature.  cbQosTSCfgExtBurstSize object is superseded by cbQosTSCfgExtBurstSize64
            	**type**\: int
            
            	**range:** 0..154400000
            
            .. attribute:: cbqostscfgextburstsize64
            
            	This object indicates the amount of traffic, in bits, in excess of the burst limit, which may be conditionally permitted by traffic\-shaping feature.   If a device implements cbQosTSCfgExtBurstSize64, then it should not implement cbQosTSCfgExtBurstSize
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqostscfgextbursttime
            
            	The amount of traffic, in ms, in excess of the burst limit, which may be conditionnally permitted by traffic\-shaping feature. The milli\-second value is internally converted to bits by using the bandwidth that is available for the class
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqostscfglimittype
            
            	This object indicates if traffic\-shaping is limiting traffic based on the peak rate or the average rate
            	**type**\: :py:class:`TrafficShapingLimit_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.TrafficShapingLimit_Enum>`
            
            .. attribute:: cbqostscfgpercentratevalue
            
            	The committed traffic\-shaping rate in percentage. Its value is valid only when cbQosTSCfgRateType  equals to 2
            	**type**\: int
            
            	**range:** 0..100
            
            .. attribute:: cbqostscfgrate
            
            	The committed traffic\-shaping rate.  This is the sustained rate permitted by the traffic\-shaping
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cbqostscfgrate64
            
            	The committed shape rate. This is the sustained rate permitted by shaping. This object represents  the 64 bit value of object cbQosTSCfgRate
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqostscfgratetype
            
            	The rate type that configured for traffic\-shaping. 1 means rate is configured in bps. 2 means rate is configured in percentage. 4 means rates are configured in parts per\-thousand. 5 means rates are configured in parts per\-million
            	**type**\: :py:class:`CbQosRateType_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CbQosRateType_Enum>`
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosconfigindex = None
                self.cbqostscfgadaptiveenabled = None
                self.cbqostscfgadaptiverate = None
                self.cbqostscfgburstsize = None
                self.cbqostscfgburstsize64 = None
                self.cbqostscfgbursttime = None
                self.cbqostscfgextburstsize = None
                self.cbqostscfgextburstsize64 = None
                self.cbqostscfgextbursttime = None
                self.cbqostscfglimittype = None
                self.cbqostscfgpercentratevalue = None
                self.cbqostscfgrate = None
                self.cbqostscfgrate64 = None
                self.cbqostscfgratetype = None

            @property
            def _common_path(self):
                if self.cbqosconfigindex is None:
                    raise YPYDataValidationError('Key property cbqosconfigindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosTSCfgTable/CISCO-CLASS-BASED-QOS-MIB:cbQosTSCfgEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosConfigIndex = ' + str(self.cbqosconfigindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosconfigindex is not None:
                    return True

                if self.cbqostscfgadaptiveenabled is not None:
                    return True

                if self.cbqostscfgadaptiverate is not None:
                    return True

                if self.cbqostscfgburstsize is not None:
                    return True

                if self.cbqostscfgburstsize64 is not None:
                    return True

                if self.cbqostscfgbursttime is not None:
                    return True

                if self.cbqostscfgextburstsize is not None:
                    return True

                if self.cbqostscfgextburstsize64 is not None:
                    return True

                if self.cbqostscfgextbursttime is not None:
                    return True

                if self.cbqostscfglimittype is not None:
                    return True

                if self.cbqostscfgpercentratevalue is not None:
                    return True

                if self.cbqostscfgrate is not None:
                    return True

                if self.cbqostscfgrate64 is not None:
                    return True

                if self.cbqostscfgratetype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosTSCfgTable.CbQosTSCfgEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosTSCfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqostscfgentry is not None:
                for child_ref in self.cbqostscfgentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosTSCfgTable']['meta_info']


    class CbQosTSStatsTable(object):
        """
        This table specifies traffic\-shaping Action related
        Statistical information.
        
        .. attribute:: cbqostsstatsentry
        
        	Each entry in this table describes the statistical information about traffic\-shaping Action. Traffic\-shaping  Action specific information you can find in this table are \:  various delay/drop pkt/byte counters, state of feature, and Q size.  This table contains statistical information only, no configuration information associated with it.  Therefore, it is indexed by the instance specific IDs,  such as cbQosPolicyIndex and cbQosObjectsIndex
        	**type**\: list of :py:class:`CbQosTSStatsEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosTSStatsTable.CbQosTSStatsEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqostsstatsentry = YList()
            self.cbqostsstatsentry.parent = self
            self.cbqostsstatsentry.name = 'cbqostsstatsentry'


        class CbQosTSStatsEntry(object):
            """
            Each entry in this table describes the statistical
            information about traffic\-shaping Action. Traffic\-shaping 
            Action specific information you can find in this table are \: 
            various delay/drop pkt/byte counters, state of feature,
            and Q size.
            
            This table contains statistical information only,
            no configuration information associated with it. 
            Therefore, it is indexed by the instance specific IDs, 
            such as cbQosPolicyIndex and cbQosObjectsIndex.
            
            .. attribute:: cbqosobjectsindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqospolicyindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqostsstatsactive
            
            	This object indicates the current traffic\-shaping state. When traffic\-shaping is enabled and the traffic  rate exceeds the shape rate, traffic\-shaping is considered to be active.  Otherwise, it is  considered inactive
            	**type**\: bool
            
            .. attribute:: cbqostsstatscurrentqsize
            
            	This object indicates the current traffic\-shaping queue depth in packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqostsstatsdelayedbyte
            
            	This object represents the lower 32 bits counter of octets that have been delayed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqostsstatsdelayedbyte64
            
            	This object represents the 64 bits counter of octets that have been delayed
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqostsstatsdelayedbyteoverflow
            
            	This object represents the upper 32 bits counter of octets that have been delayed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqostsstatsdelayedpkt
            
            	This object represents the lower 32 bits counter of packets that have been delayed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqostsstatsdelayedpkt64
            
            	This object represents the 64 bits counter of packets that have been delayed
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqostsstatsdelayedpktoverflow
            
            	This object represents the upper 32 bits counter of packets that have been delayed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqostsstatsdropbyte
            
            	This object represents the lower 32 bits counter of octets that have been dropped during shaping
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqostsstatsdropbyte64
            
            	This object represents the 64 bits counter of octets that have been dropped during shaping
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqostsstatsdropbyteoverflow
            
            	This object represents the upper 32 bits counter of octets that have been dropped during shaping
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqostsstatsdroppkt
            
            	This object represents the lower 32 bits counter of packets that have been dropped during shaping
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqostsstatsdroppkt64
            
            	This object represents the 64 bits counter of packets that have been dropped during shaping
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbqostsstatsdroppktoverflow
            
            	This object represents the upper 32 bits counter of packets that have been dropped during shaping
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosobjectsindex = None
                self.cbqospolicyindex = None
                self.cbqostsstatsactive = None
                self.cbqostsstatscurrentqsize = None
                self.cbqostsstatsdelayedbyte = None
                self.cbqostsstatsdelayedbyte64 = None
                self.cbqostsstatsdelayedbyteoverflow = None
                self.cbqostsstatsdelayedpkt = None
                self.cbqostsstatsdelayedpkt64 = None
                self.cbqostsstatsdelayedpktoverflow = None
                self.cbqostsstatsdropbyte = None
                self.cbqostsstatsdropbyte64 = None
                self.cbqostsstatsdropbyteoverflow = None
                self.cbqostsstatsdroppkt = None
                self.cbqostsstatsdroppkt64 = None
                self.cbqostsstatsdroppktoverflow = None

            @property
            def _common_path(self):
                if self.cbqosobjectsindex is None:
                    raise YPYDataValidationError('Key property cbqosobjectsindex is None')
                if self.cbqospolicyindex is None:
                    raise YPYDataValidationError('Key property cbqospolicyindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosTSStatsTable/CISCO-CLASS-BASED-QOS-MIB:cbQosTSStatsEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosObjectsIndex = ' + str(self.cbqosobjectsindex) + '][CISCO-CLASS-BASED-QOS-MIB:cbQosPolicyIndex = ' + str(self.cbqospolicyindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosobjectsindex is not None:
                    return True

                if self.cbqospolicyindex is not None:
                    return True

                if self.cbqostsstatsactive is not None:
                    return True

                if self.cbqostsstatscurrentqsize is not None:
                    return True

                if self.cbqostsstatsdelayedbyte is not None:
                    return True

                if self.cbqostsstatsdelayedbyte64 is not None:
                    return True

                if self.cbqostsstatsdelayedbyteoverflow is not None:
                    return True

                if self.cbqostsstatsdelayedpkt is not None:
                    return True

                if self.cbqostsstatsdelayedpkt64 is not None:
                    return True

                if self.cbqostsstatsdelayedpktoverflow is not None:
                    return True

                if self.cbqostsstatsdropbyte is not None:
                    return True

                if self.cbqostsstatsdropbyte64 is not None:
                    return True

                if self.cbqostsstatsdropbyteoverflow is not None:
                    return True

                if self.cbqostsstatsdroppkt is not None:
                    return True

                if self.cbqostsstatsdroppkt64 is not None:
                    return True

                if self.cbqostsstatsdroppktoverflow is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosTSStatsTable.CbQosTSStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosTSStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqostsstatsentry is not None:
                for child_ref in self.cbqostsstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosTSStatsTable']['meta_info']


    class CbQosTableMapCfgTable(object):
        """
        This table specifies Table Map basic configuration
        information.
        
        .. attribute:: cbqostablemapcfgentry
        
        	Each entry in this table describes configuration information about a tablemap name, behavior and default value.  Each cbQosTableMapCfgName is a unique character string in QOS.  This table contains configuration information only, no statistics associated with it
        	**type**\: list of :py:class:`CbQosTableMapCfgEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosTableMapCfgTable.CbQosTableMapCfgEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqostablemapcfgentry = YList()
            self.cbqostablemapcfgentry.parent = self
            self.cbqostablemapcfgentry.name = 'cbqostablemapcfgentry'


        class CbQosTableMapCfgEntry(object):
            """
            Each entry in this table describes configuration
            information about a tablemap name, behavior and default
            value.  Each cbQosTableMapCfgName is a unique character
            string in QOS.  This table contains configuration
            information only, no statistics associated with it.
            
            .. attribute:: cbqostablemapcfgindex
            
            	An arbitrary (system\-assigned) index for tablemap
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqostablemapcfgbehavior
            
            	The behavior of a tablemap. value(1)    Always set to\-value to be a configurable             default value <0\-99> which is defined in             cbQosTableMapCfgDftValue.  copy(2)     Always copy from\-value to to\-value in case             the from\-value is not found in the tablemap.             This is the default behavior for a tablemap.  ignore(3)   Ignore to set to\-value when from\-value             is not found in the tablemap
            	**type**\: :py:class:`CbQosTableMapCfgBehavior_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosTableMapCfgTable.CbQosTableMapCfgEntry.CbQosTableMapCfgBehavior_Enum>`
            
            .. attribute:: cbqostablemapcfgdftvalue
            
            	The configurable default value used when cbQosTableMapCfgBehavior is value(1)
            	**type**\: int
            
            	**range:** 0..99
            
            .. attribute:: cbqostablemapcfgname
            
            	Name of the tablemap
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqostablemapcfgindex = None
                self.cbqostablemapcfgbehavior = None
                self.cbqostablemapcfgdftvalue = None
                self.cbqostablemapcfgname = None

            class CbQosTableMapCfgBehavior_Enum(Enum):
                """
                CbQosTableMapCfgBehavior_Enum

                The behavior of a tablemap.
                value(1)    Always set to\-value to be a configurable
                            default value <0\-99> which is defined in
                            cbQosTableMapCfgDftValue.
                
                copy(2)     Always copy from\-value to to\-value in case
                            the from\-value is not found in the tablemap.
                            This is the default behavior for a tablemap.
                
                ignore(3)   Ignore to set to\-value when from\-value
                            is not found in the tablemap.

                """

                VALUE = 1

                COPY = 2

                IGNORE = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                    return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosTableMapCfgTable.CbQosTableMapCfgEntry.CbQosTableMapCfgBehavior_Enum']


            @property
            def _common_path(self):
                if self.cbqostablemapcfgindex is None:
                    raise YPYDataValidationError('Key property cbqostablemapcfgindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosTableMapCfgTable/CISCO-CLASS-BASED-QOS-MIB:cbQosTableMapCfgEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosTableMapCfgIndex = ' + str(self.cbqostablemapcfgindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqostablemapcfgindex is not None:
                    return True

                if self.cbqostablemapcfgbehavior is not None:
                    return True

                if self.cbqostablemapcfgdftvalue is not None:
                    return True

                if self.cbqostablemapcfgname is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosTableMapCfgTable.CbQosTableMapCfgEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosTableMapCfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqostablemapcfgentry is not None:
                for child_ref in self.cbqostablemapcfgentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosTableMapCfgTable']['meta_info']


    class CbQosTableMapSetCfgTable(object):
        """
        This table specifies enhanced packet marking
        configuration using a pre\-defined tablemap.
        
        .. attribute:: cbqostablemapsetcfgentry
        
        	Each entry in this table describes configuration information for an Enhanced Packet Marking Action. The enhanced packet marking action uses a pre\-configured table\-map to do the from\-value to to\-value conversion. The packet marking to\-type and from\-type relationship can be established by using the table\-map. Following is an example\: cbQosTMSetIpDscpFromType == qosGroup(3) cbQosTMSetIpDscpMapName == 'MyTableMap', it means that table\-map 'MyTableMap' will be used to convert the QosGroup value and the converted value will be used to set IpDSCP.  cbQosConfigIndex is drived directly from cbQosSetCfgTable to keep the 1\-to\-1 mapping between two tables.  This table contains configuration information only, no statistics associated with it
        	**type**\: list of :py:class:`CbQosTableMapSetCfgEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosTableMapSetCfgTable.CbQosTableMapSetCfgEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqostablemapsetcfgentry = YList()
            self.cbqostablemapsetcfgentry.parent = self
            self.cbqostablemapsetcfgentry.name = 'cbqostablemapsetcfgentry'


        class CbQosTableMapSetCfgEntry(object):
            """
            Each entry in this table describes configuration
            information for an Enhanced Packet Marking Action.
            The enhanced packet marking action uses a pre\-configured
            table\-map to do the from\-value to to\-value conversion.
            The packet marking to\-type and from\-type relationship
            can be established by using the table\-map.
            Following is an example\:
            cbQosTMSetIpDscpFromType == qosGroup(3)
            cbQosTMSetIpDscpMapName == 'MyTableMap',
            it means that table\-map 'MyTableMap' will be used to
            convert the QosGroup value and the converted value will
            be used to set IpDSCP.
            
            cbQosConfigIndex is drived directly from
            cbQosSetCfgTable to keep the 1\-to\-1 mapping between
            two tables.  This table contains configuration
            information only, no statistics associated with it.
            
            .. attribute:: cbqosconfigindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqostmsetipdscpfromtype
            
            	The packet marking type whose value will be converted to a to\-value based on a pre\-configured table\-map.  The to\-value will then be used to set IpDSCP
            	**type**\: :py:class:`CbQosTMSetType_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CbQosTMSetType_Enum>`
            
            .. attribute:: cbqostmsetipdscpmapname
            
            	The name of a pre\-configured table\-map used to convert and set IpDSCP value
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cbqostmsetipprecedencefromtype
            
            	The packet marking type whose value will be converted to a to\-value based on a pre\-configured table\-map.  The to\-value will then be used to set IpPrecedence
            	**type**\: :py:class:`CbQosTMSetType_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CbQosTMSetType_Enum>`
            
            .. attribute:: cbqostmsetipprecedencemapname
            
            	The name of a pre\-configured table\-map used to convert and set IpPrecedence value
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cbqostmsetl2cosfromtype
            
            	The packet marking type whose value will be converted to a to\-value based on a pre\-configured table\-map.  The to\-value will then be used to set L2Cos
            	**type**\: :py:class:`CbQosTMSetType_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CbQosTMSetType_Enum>`
            
            .. attribute:: cbqostmsetl2cosmapname
            
            	The name of a pre\-configured table\-map used to convert and set L2Cos value
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cbqostmsetmplsexpimpfromtype
            
            	The packet marking type whose value will be converted to a to\-value based on a pre\-configured table\-map.  The to\-value will then be used to set MplsExpImposition
            	**type**\: :py:class:`CbQosTMSetType_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CbQosTMSetType_Enum>`
            
            .. attribute:: cbqostmsetmplsexpimpmapname
            
            	The name of a pre\-configured table\-map used to convert and set MplsExpImposition value
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cbqostmsetmplsexptopfromtype
            
            	The packet marking type whose value will be converted to a to\-value based on a pre\-configured table\-map.  The to\-value will then be used to set MplsExpTopMost
            	**type**\: :py:class:`CbQosTMSetType_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CbQosTMSetType_Enum>`
            
            .. attribute:: cbqostmsetmplsexptopmapname
            
            	The name of a pre\-configured table\-map used to convert and set MplsExpTopMost value
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cbqostmsetqosgroupfromtype
            
            	The packet marking type whose value will be converted to a to\-value based on a pre\-configured table\-map.  The to\-value will then be used to set QosGroup
            	**type**\: :py:class:`CbQosTMSetType_Enum <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CbQosTMSetType_Enum>`
            
            .. attribute:: cbqostmsetqosgroupmapname
            
            	The name of a pre\-configured table\-map used to convert and set QosGroup value
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqosconfigindex = None
                self.cbqostmsetipdscpfromtype = None
                self.cbqostmsetipdscpmapname = None
                self.cbqostmsetipprecedencefromtype = None
                self.cbqostmsetipprecedencemapname = None
                self.cbqostmsetl2cosfromtype = None
                self.cbqostmsetl2cosmapname = None
                self.cbqostmsetmplsexpimpfromtype = None
                self.cbqostmsetmplsexpimpmapname = None
                self.cbqostmsetmplsexptopfromtype = None
                self.cbqostmsetmplsexptopmapname = None
                self.cbqostmsetqosgroupfromtype = None
                self.cbqostmsetqosgroupmapname = None

            @property
            def _common_path(self):
                if self.cbqosconfigindex is None:
                    raise YPYDataValidationError('Key property cbqosconfigindex is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosTableMapSetCfgTable/CISCO-CLASS-BASED-QOS-MIB:cbQosTableMapSetCfgEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosConfigIndex = ' + str(self.cbqosconfigindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqosconfigindex is not None:
                    return True

                if self.cbqostmsetipdscpfromtype is not None:
                    return True

                if self.cbqostmsetipdscpmapname is not None:
                    return True

                if self.cbqostmsetipprecedencefromtype is not None:
                    return True

                if self.cbqostmsetipprecedencemapname is not None:
                    return True

                if self.cbqostmsetl2cosfromtype is not None:
                    return True

                if self.cbqostmsetl2cosmapname is not None:
                    return True

                if self.cbqostmsetmplsexpimpfromtype is not None:
                    return True

                if self.cbqostmsetmplsexpimpmapname is not None:
                    return True

                if self.cbqostmsetmplsexptopfromtype is not None:
                    return True

                if self.cbqostmsetmplsexptopmapname is not None:
                    return True

                if self.cbqostmsetqosgroupfromtype is not None:
                    return True

                if self.cbqostmsetqosgroupmapname is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosTableMapSetCfgTable.CbQosTableMapSetCfgEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosTableMapSetCfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqostablemapsetcfgentry is not None:
                for child_ref in self.cbqostablemapsetcfgentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosTableMapSetCfgTable']['meta_info']


    class CbQosTableMapValueCfgTable(object):
        """
        This table specifies the from\-value to to\-value
        conversion pairs for a tablemap.
        
        .. attribute:: cbqostablemapvaluecfgentry
        
        	Each entry in this table specifies a from\-value to to\-value conversion pair for a given tablemap. This table contains configuration information only, no statistics associated with it
        	**type**\: list of :py:class:`CbQosTableMapValueCfgEntry <ydk.models.class_.CISCO_CLASS_BASED_QOS_MIB.CISCOCLASSBASEDQOSMIB.CbQosTableMapValueCfgTable.CbQosTableMapValueCfgEntry>`
        
        

        """

        _prefix = 'cisco-class'
        _revision = '2014-01-24'

        def __init__(self):
            self.parent = None
            self.cbqostablemapvaluecfgentry = YList()
            self.cbqostablemapvaluecfgentry.parent = self
            self.cbqostablemapvaluecfgentry.name = 'cbqostablemapvaluecfgentry'


        class CbQosTableMapValueCfgEntry(object):
            """
            Each entry in this table specifies a from\-value to
            to\-value conversion pair for a given tablemap.
            This table contains configuration information only,
            no statistics associated with it.
            
            .. attribute:: cbqostablemapcfgindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqostablemapvaluecfgfrom
            
            	This is the from\-value in the tablemap.  If cbQosTableMapCfgBehavior equals to either copy(2) or ignore(3), when the content in the from\-type(e.g., cbQosTMSetIpDscpFromType) equals to this value, the value in the to\-type(e.g., IpDscp) will be set to cbQosTableMapValueCfgTo.  Each tablemap can configure multiple from\-value/to\-value pairs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbqostablemapvaluecfgto
            
            	This is the to\-value in the tablemap.  Its usage is described in cbQosTableMapValueCfgFrom
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-class'
            _revision = '2014-01-24'

            def __init__(self):
                self.parent = None
                self.cbqostablemapcfgindex = None
                self.cbqostablemapvaluecfgfrom = None
                self.cbqostablemapvaluecfgto = None

            @property
            def _common_path(self):
                if self.cbqostablemapcfgindex is None:
                    raise YPYDataValidationError('Key property cbqostablemapcfgindex is None')
                if self.cbqostablemapvaluecfgfrom is None:
                    raise YPYDataValidationError('Key property cbqostablemapvaluecfgfrom is None')

                return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosTableMapValueCfgTable/CISCO-CLASS-BASED-QOS-MIB:cbQosTableMapValueCfgEntry[CISCO-CLASS-BASED-QOS-MIB:cbQosTableMapCfgIndex = ' + str(self.cbqostablemapcfgindex) + '][CISCO-CLASS-BASED-QOS-MIB:cbQosTableMapValueCfgFrom = ' + str(self.cbqostablemapvaluecfgfrom) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbqostablemapcfgindex is not None:
                    return True

                if self.cbqostablemapvaluecfgfrom is not None:
                    return True

                if self.cbqostablemapvaluecfgto is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
                return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosTableMapValueCfgTable.CbQosTableMapValueCfgEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB/CISCO-CLASS-BASED-QOS-MIB:cbQosTableMapValueCfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbqostablemapvaluecfgentry is not None:
                for child_ref in self.cbqostablemapvaluecfgentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
            return meta._meta_table['CISCOCLASSBASEDQOSMIB.CbQosTableMapValueCfgTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-CLASS-BASED-QOS-MIB:CISCO-CLASS-BASED-QOS-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cbqosatmpvcpolicytable is not None and self.cbqosatmpvcpolicytable._has_data():
            return True

        if self.cbqosatmpvcpolicytable is not None and self.cbqosatmpvcpolicytable.is_presence():
            return True

        if self.cbqosc3placcountcfgtable is not None and self.cbqosc3placcountcfgtable._has_data():
            return True

        if self.cbqosc3placcountcfgtable is not None and self.cbqosc3placcountcfgtable.is_presence():
            return True

        if self.cbqosc3placcountstatstable is not None and self.cbqosc3placcountstatstable._has_data():
            return True

        if self.cbqosc3placcountstatstable is not None and self.cbqosc3placcountstatstable.is_presence():
            return True

        if self.cbqoscmcfgtable is not None and self.cbqoscmcfgtable._has_data():
            return True

        if self.cbqoscmcfgtable is not None and self.cbqoscmcfgtable.is_presence():
            return True

        if self.cbqoscmstatstable is not None and self.cbqoscmstatstable._has_data():
            return True

        if self.cbqoscmstatstable is not None and self.cbqoscmstatstable.is_presence():
            return True

        if self.cbqosebcfgtable is not None and self.cbqosebcfgtable._has_data():
            return True

        if self.cbqosebcfgtable is not None and self.cbqosebcfgtable.is_presence():
            return True

        if self.cbqosebstatstable is not None and self.cbqosebstatstable._has_data():
            return True

        if self.cbqosebstatstable is not None and self.cbqosebstatstable.is_presence():
            return True

        if self.cbqosframerelaypolicytable is not None and self.cbqosframerelaypolicytable._has_data():
            return True

        if self.cbqosframerelaypolicytable is not None and self.cbqosframerelaypolicytable.is_presence():
            return True

        if self.cbqosinterfacepolicytable is not None and self.cbqosinterfacepolicytable._has_data():
            return True

        if self.cbqosinterfacepolicytable is not None and self.cbqosinterfacepolicytable.is_presence():
            return True

        if self.cbqosiphccfgtable is not None and self.cbqosiphccfgtable._has_data():
            return True

        if self.cbqosiphccfgtable is not None and self.cbqosiphccfgtable.is_presence():
            return True

        if self.cbqosiphcstatstable is not None and self.cbqosiphcstatstable._has_data():
            return True

        if self.cbqosiphcstatstable is not None and self.cbqosiphcstatstable.is_presence():
            return True

        if self.cbqosmatchstmtcfgtable is not None and self.cbqosmatchstmtcfgtable._has_data():
            return True

        if self.cbqosmatchstmtcfgtable is not None and self.cbqosmatchstmtcfgtable.is_presence():
            return True

        if self.cbqosmatchstmtstatstable is not None and self.cbqosmatchstmtstatstable._has_data():
            return True

        if self.cbqosmatchstmtstatstable is not None and self.cbqosmatchstmtstatstable.is_presence():
            return True

        if self.cbqosmeasureipslacfgtable is not None and self.cbqosmeasureipslacfgtable._has_data():
            return True

        if self.cbqosmeasureipslacfgtable is not None and self.cbqosmeasureipslacfgtable.is_presence():
            return True

        if self.cbqosobjectstable is not None and self.cbqosobjectstable._has_data():
            return True

        if self.cbqosobjectstable is not None and self.cbqosobjectstable.is_presence():
            return True

        if self.cbqospoliceactioncfgtable is not None and self.cbqospoliceactioncfgtable._has_data():
            return True

        if self.cbqospoliceactioncfgtable is not None and self.cbqospoliceactioncfgtable.is_presence():
            return True

        if self.cbqospolicecfgtable is not None and self.cbqospolicecfgtable._has_data():
            return True

        if self.cbqospolicecfgtable is not None and self.cbqospolicecfgtable.is_presence():
            return True

        if self.cbqospolicecolorstatstable is not None and self.cbqospolicecolorstatstable._has_data():
            return True

        if self.cbqospolicecolorstatstable is not None and self.cbqospolicecolorstatstable.is_presence():
            return True

        if self.cbqospolicestatstable is not None and self.cbqospolicestatstable._has_data():
            return True

        if self.cbqospolicestatstable is not None and self.cbqospolicestatstable.is_presence():
            return True

        if self.cbqospolicymapcfgtable is not None and self.cbqospolicymapcfgtable._has_data():
            return True

        if self.cbqospolicymapcfgtable is not None and self.cbqospolicymapcfgtable.is_presence():
            return True

        if self.cbqosqueueingcfgtable is not None and self.cbqosqueueingcfgtable._has_data():
            return True

        if self.cbqosqueueingcfgtable is not None and self.cbqosqueueingcfgtable.is_presence():
            return True

        if self.cbqosqueueingclasscfgtable is not None and self.cbqosqueueingclasscfgtable._has_data():
            return True

        if self.cbqosqueueingclasscfgtable is not None and self.cbqosqueueingclasscfgtable.is_presence():
            return True

        if self.cbqosqueueingstatstable is not None and self.cbqosqueueingstatstable._has_data():
            return True

        if self.cbqosqueueingstatstable is not None and self.cbqosqueueingstatstable.is_presence():
            return True

        if self.cbqosredcfgtable is not None and self.cbqosredcfgtable._has_data():
            return True

        if self.cbqosredcfgtable is not None and self.cbqosredcfgtable.is_presence():
            return True

        if self.cbqosredclasscfgtable is not None and self.cbqosredclasscfgtable._has_data():
            return True

        if self.cbqosredclasscfgtable is not None and self.cbqosredclasscfgtable.is_presence():
            return True

        if self.cbqosredclassstatstable is not None and self.cbqosredclassstatstable._has_data():
            return True

        if self.cbqosredclassstatstable is not None and self.cbqosredclassstatstable.is_presence():
            return True

        if self.cbqosservicepolicytable is not None and self.cbqosservicepolicytable._has_data():
            return True

        if self.cbqosservicepolicytable is not None and self.cbqosservicepolicytable.is_presence():
            return True

        if self.cbqossetcfgtable is not None and self.cbqossetcfgtable._has_data():
            return True

        if self.cbqossetcfgtable is not None and self.cbqossetcfgtable.is_presence():
            return True

        if self.cbqossetstatstable is not None and self.cbqossetstatstable._has_data():
            return True

        if self.cbqossetstatstable is not None and self.cbqossetstatstable.is_presence():
            return True

        if self.cbqostablemapcfgtable is not None and self.cbqostablemapcfgtable._has_data():
            return True

        if self.cbqostablemapcfgtable is not None and self.cbqostablemapcfgtable.is_presence():
            return True

        if self.cbqostablemapsetcfgtable is not None and self.cbqostablemapsetcfgtable._has_data():
            return True

        if self.cbqostablemapsetcfgtable is not None and self.cbqostablemapsetcfgtable.is_presence():
            return True

        if self.cbqostablemapvaluecfgtable is not None and self.cbqostablemapvaluecfgtable._has_data():
            return True

        if self.cbqostablemapvaluecfgtable is not None and self.cbqostablemapvaluecfgtable.is_presence():
            return True

        if self.cbqostscfgtable is not None and self.cbqostscfgtable._has_data():
            return True

        if self.cbqostscfgtable is not None and self.cbqostscfgtable.is_presence():
            return True

        if self.cbqostsstatstable is not None and self.cbqostsstatstable._has_data():
            return True

        if self.cbqostsstatstable is not None and self.cbqostsstatstable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.class_._meta import _CISCO_CLASS_BASED_QOS_MIB as meta
        return meta._meta_table['CISCOCLASSBASEDQOSMIB']['meta_info']



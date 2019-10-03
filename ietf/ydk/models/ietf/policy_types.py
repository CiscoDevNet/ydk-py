""" policy_types 

This module contains a collection of YANG groupings 
in filter configurations for policy model.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error

from ydk.models.ietf.ietf_diffserv_classifier import FilterType


class Direction(Enum):
    """
    Direction (Enum Class)

    This typedef defines directional enums used in c3pl.

    inbound\:         Incoming direction.

    outbound\:        Outgoing direction.

    .. data:: inbound = 0

    .. data:: outbound = 1

    """

    inbound = Enum.YLeaf(0, "inbound")

    outbound = Enum.YLeaf(1, "outbound")


class Metric(Enum):
    """
    Metric (Enum Class)

    metric

    .. data:: none = 0

    .. data:: peta = 1

    .. data:: tera = 2

    .. data:: giga = 3

    .. data:: mega = 4

    .. data:: kilo = 5

    .. data:: milli = 6

    .. data:: nano = 7

    """

    none = Enum.YLeaf(0, "none")

    peta = Enum.YLeaf(1, "peta")

    tera = Enum.YLeaf(2, "tera")

    giga = Enum.YLeaf(3, "giga")

    mega = Enum.YLeaf(4, "mega")

    kilo = Enum.YLeaf(5, "kilo")

    milli = Enum.YLeaf(6, "milli")

    nano = Enum.YLeaf(7, "nano")


class RateUnit(Enum):
    """
    RateUnit (Enum Class)

    Unit for traffic rate\:

    pps\:     packets per sec

    cps\:     cells per sec

    bps\:     bits per sec

    perc\:    percentage

    ratio\:   ratio

    .. data:: pps = 0

    .. data:: cps = 1

    .. data:: bps = 2

    .. data:: perc = 3

    .. data:: ratio = 4

    """

    pps = Enum.YLeaf(0, "pps")

    cps = Enum.YLeaf(1, "cps")

    bps = Enum.YLeaf(2, "bps")

    perc = Enum.YLeaf(3, "perc")

    ratio = Enum.YLeaf(4, "ratio")



class InputInterface(FilterType):
    """
    Input interface
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:input-interface"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(InputInterface, self).__init__(ns, pref, tag)



class SrcMac(FilterType):
    """
    Source MAC address
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:src-mac"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SrcMac, self).__init__(ns, pref, tag)



class Application(FilterType):
    """
    application
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:application"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Application, self).__init__(ns, pref, tag)



class SecurityGroupName(FilterType):
    """
    security group name
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:security-group-name"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SecurityGroupName, self).__init__(ns, pref, tag)



class Ipv4AclName(FilterType):
    """
    IPV4 access group list
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:ipv4-acl-name"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Ipv4AclName, self).__init__(ns, pref, tag)



class FlowDlci(FilterType):
    """
    Frame\-relay DLCI
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:flow-dlci"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FlowDlci, self).__init__(ns, pref, tag)



class Dei(FilterType):
    """
    Frame\-relay DE bit
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:dei"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Dei, self).__init__(ns, pref, tag)



class Prec(FilterType):
    """
    IP precendence
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:prec"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Prec, self).__init__(ns, pref, tag)



class PacketLength(FilterType):
    """
    Layer 3 packet length
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:packet-length"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PacketLength, self).__init__(ns, pref, tag)



class Ipv4Acl(FilterType):
    """
    IPV4 access group Index
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:ipv4-acl"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Ipv4Acl, self).__init__(ns, pref, tag)



class FlowDe(FilterType):
    """
    Flow DE
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:flow-de"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FlowDe, self).__init__(ns, pref, tag)



class FlowIp(FilterType):
    """
    Flow IP
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:flow-ip"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FlowIp, self).__init__(ns, pref, tag)



class FlowRecord(FilterType):
    """
    FLow record
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:flow-record"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(FlowRecord, self).__init__(ns, pref, tag)



class VlanInner(FilterType):
    """
    Vlan\-inner
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:vlan-inner"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(VlanInner, self).__init__(ns, pref, tag)



class Metadata(FilterType):
    """
    metadata
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:metadata"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Metadata, self).__init__(ns, pref, tag)



class Vlan(FilterType):
    """
    Vlan
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:vlan"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Vlan, self).__init__(ns, pref, tag)



class AtmVci(FilterType):
    """
    ATM VCI number
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:atm-vci"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AtmVci, self).__init__(ns, pref, tag)



class ClassMap(FilterType):
    """
    class\-map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:class-map"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ClassMap, self).__init__(ns, pref, tag)



class QosGroup(FilterType):
    """
    QOS group
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:qos-group"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(QosGroup, self).__init__(ns, pref, tag)



class WlanUserPriority(FilterType):
    """
    WLAN user priority
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:wlan-user-priority"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(WlanUserPriority, self).__init__(ns, pref, tag)



class IpRtp(FilterType):
    """
    IP RTP port
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:ip-rtp"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IpRtp, self).__init__(ns, pref, tag)



class Ipv6Acl(FilterType):
    """
    IPV6 access group Index
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:ipv6-acl"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Ipv6Acl, self).__init__(ns, pref, tag)



class AtmClp(FilterType):
    """
    ATM CLP bit
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:atm-clp"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AtmClp, self).__init__(ns, pref, tag)



class DstMac(FilterType):
    """
    Destination MAC address
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:dst-mac"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DstMac, self).__init__(ns, pref, tag)



class Cos(FilterType):
    """
    
    Filter\-type IEEE 802.1Q/ISL class of service/user 
    priority values
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:cos"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Cos, self).__init__(ns, pref, tag)



class DeiInner(FilterType):
    """
    Frame\-relay inner DE bit
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:dei-inner"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DeiInner, self).__init__(ns, pref, tag)



class MplsExpTop(FilterType):
    """
    Multi Protocol Label Switching experimental 
    topmost specific values
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:mpls-exp-top"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(MplsExpTop, self).__init__(ns, pref, tag)



class CosInner(FilterType):
    """
    ATM VC configured as Access VC
    class of service/user priority values
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:cos-inner"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(CosInner, self).__init__(ns, pref, tag)



class Ipv6AclName(FilterType):
    """
    IPV6 access group list
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:ipv6-acl-name"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Ipv6AclName, self).__init__(ns, pref, tag)



class MplsExpImp(FilterType):
    """
    Multi Protocol Label Switching experimental 
    imposition specific values
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:mpls-exp-imp"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(MplsExpImp, self).__init__(ns, pref, tag)



class SecurityGroupTag(FilterType):
    """
    security group tag
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:security-group-tag"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SecurityGroupTag, self).__init__(ns, pref, tag)



class ClassType(Identity):
    """
     
    This is identity of base class\-type
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:class-type"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ClassType, self).__init__(ns, pref, tag)



class DiscardClass(FilterType):
    """
    Discard behavior identifier
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:discard-class"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DiscardClass, self).__init__(ns, pref, tag)



class Vpls(FilterType):
    """
    VPLS
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:vpls"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Vpls, self).__init__(ns, pref, tag)



class PolicyType(Identity):
    """
     
    This is identity of base policy\-type
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:policy-type"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PolicyType, self).__init__(ns, pref, tag)



class Control(PolicyType):
    """
    
    Policy\-type control policy\-map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:control"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Control, self).__init__(ns, pref, tag)



class Qos(PolicyType):
    """
    
    Policy\-type QOS (quality of service)
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:qos"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Qos, self).__init__(ns, pref, tag)



class PerfMon(PolicyType):
    """
    
    Policy\-type PERF\-MON (performance monitoring)
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:perf-mon"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PerfMon, self).__init__(ns, pref, tag)



class PacketService(PolicyType):
    """
    
    Policy\-type Packet Service Policy Map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:packet-service"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PacketService, self).__init__(ns, pref, tag)



class QosClass(ClassType):
    """
    
    QOS class\-map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:qos-class"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(QosClass, self).__init__(ns, pref, tag)



class ControlClass(ClassType):
    """
    
    Control policy class\-map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:control-class"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ControlClass, self).__init__(ns, pref, tag)



class InspectClass(ClassType):
    """
    
    Firewall Class Map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:inspect-class"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(InspectClass, self).__init__(ns, pref, tag)



class AppnavClass(ClassType):
    """
    
    APPNAV Class Map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:appnav-class"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AppnavClass, self).__init__(ns, pref, tag)



class Service(PolicyType):
    """
    
    Policy\-type policymap service configuration
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:service"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Service, self).__init__(ns, pref, tag)



class AccessControlClass(ClassType):
    """
    
    Access\-control specific class\-map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:access-control-class"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AccessControlClass, self).__init__(ns, pref, tag)



class AccessControl(PolicyType):
    """
    
    Policy\-type access\-control specific policy\-map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:access-control"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(AccessControl, self).__init__(ns, pref, tag)



class Appnav(PolicyType):
    """
    
    Policy\-type APPNAV Policy Map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:appnav"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Appnav, self).__init__(ns, pref, tag)



class Inspect(PolicyType):
    """
    
    Policy\-type Firewall Policy Map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:inspect"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Inspect, self).__init__(ns, pref, tag)



class Pbr(PolicyType):
    """
    
    Policy\-type PBR (policy based routing)
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:c3pl-types", pref="policy-types", tag="policy-types:pbr"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(Pbr, self).__init__(ns, pref, tag)




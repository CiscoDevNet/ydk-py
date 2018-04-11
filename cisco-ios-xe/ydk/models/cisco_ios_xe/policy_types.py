""" policy_types 

This module contains a collection of YANG groupings 
in filter configurations for policy model.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


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



class PolicyType(Identity):
    """
     
    This is identity of base policy\-type
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(PolicyType, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:policy-type")


class ClassType(Identity):
    """
     
    This is identity of base class\-type
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(ClassType, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:class-type")


class Cos(Identity):
    """
    
    Filter\-type IEEE 802.1Q/ISL class of service/user 
    priority values
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(Cos, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:cos")


class CosInner(Identity):
    """
    ATM VC configured as Access VC
    class of service/user priority values
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(CosInner, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:cos-inner")


class Ipv4AclName(Identity):
    """
    IPV4 access group list
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(Ipv4AclName, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:ipv4-acl-name")


class Ipv6AclName(Identity):
    """
    IPV6 access group list
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(Ipv6AclName, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:ipv6-acl-name")


class Ipv4Acl(Identity):
    """
    IPV4 access group Index
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(Ipv4Acl, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:ipv4-acl")


class Ipv6Acl(Identity):
    """
    IPV6 access group Index
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(Ipv6Acl, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:ipv6-acl")


class InputInterface(Identity):
    """
    Input interface
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(InputInterface, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:input-interface")


class SrcMac(Identity):
    """
    Source MAC address
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(SrcMac, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:src-mac")


class DstMac(Identity):
    """
    Destination MAC address
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(DstMac, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:dst-mac")


class MplsExpTop(Identity):
    """
    Multi Protocol Label Switching experimental 
    topmost specific values
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(MplsExpTop, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:mpls-exp-top")


class MplsExpImp(Identity):
    """
    Multi Protocol Label Switching experimental 
    imposition specific values
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(MplsExpImp, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:mpls-exp-imp")


class PacketLength(Identity):
    """
    Layer 3 packet length
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(PacketLength, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:packet-length")


class Prec(Identity):
    """
    IP precendence
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(Prec, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:prec")


class QosGroup(Identity):
    """
    QOS group
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(QosGroup, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:qos-group")


class Vlan(Identity):
    """
    Vlan
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(Vlan, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:vlan")


class VlanInner(Identity):
    """
    Vlan\-inner
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(VlanInner, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:vlan-inner")


class AtmClp(Identity):
    """
    ATM CLP bit
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(AtmClp, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:atm-clp")


class AtmVci(Identity):
    """
    ATM VCI number
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(AtmVci, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:atm-vci")


class Dei(Identity):
    """
    Frame\-relay DE bit
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(Dei, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:dei")


class DeiInner(Identity):
    """
    Frame\-relay inner DE bit
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(DeiInner, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:dei-inner")


class FlowIp(Identity):
    """
    Flow IP
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(FlowIp, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:flow-ip")


class FlowRecord(Identity):
    """
    FLow record
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(FlowRecord, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:flow-record")


class FlowDe(Identity):
    """
    Flow DE
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(FlowDe, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:flow-de")


class FlowDlci(Identity):
    """
    Frame\-relay DLCI
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(FlowDlci, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:flow-dlci")


class WlanUserPriority(Identity):
    """
    WLAN user priority
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(WlanUserPriority, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:wlan-user-priority")


class DiscardClass(Identity):
    """
    Discard behavior identifier
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(DiscardClass, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:discard-class")


class ClassMap(Identity):
    """
    class\-map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(ClassMap, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:class-map")


class Metadata(Identity):
    """
    metadata
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(Metadata, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:metadata")


class Application(Identity):
    """
    application
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(Application, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:application")


class SecurityGroupName(Identity):
    """
    security group name
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(SecurityGroupName, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:security-group-name")


class SecurityGroupTag(Identity):
    """
    security group tag
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(SecurityGroupTag, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:security-group-tag")


class IpRtp(Identity):
    """
    IP RTP port
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(IpRtp, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:ip-rtp")


class Vpls(Identity):
    """
    VPLS
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(Vpls, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:vpls")


class Qos(Identity):
    """
    
    Policy\-type QOS (quality of service)
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(Qos, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:qos")


class Pbr(Identity):
    """
    
    Policy\-type PBR (policy based routing)
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(Pbr, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:pbr")


class PerfMon(Identity):
    """
    
    Policy\-type PERF\-MON (performance monitoring)
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(PerfMon, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:perf-mon")


class AccessControl(Identity):
    """
    
    Policy\-type access\-control specific policy\-map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(AccessControl, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:access-control")


class Appnav(Identity):
    """
    
    Policy\-type APPNAV Policy Map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(Appnav, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:appnav")


class Control(Identity):
    """
    
    Policy\-type control policy\-map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(Control, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:control")


class Inspect(Identity):
    """
    
    Policy\-type Firewall Policy Map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(Inspect, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:inspect")


class PacketService(Identity):
    """
    
    Policy\-type Packet Service Policy Map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(PacketService, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:packet-service")


class Service(Identity):
    """
    
    Policy\-type policymap service configuration
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(Service, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:service")


class QosClass(Identity):
    """
    
    QOS class\-map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(QosClass, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:qos-class")


class AccessControlClass(Identity):
    """
    
    Access\-control specific class\-map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(AccessControlClass, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:access-control-class")


class AppnavClass(Identity):
    """
    
    APPNAV Class Map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(AppnavClass, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:appnav-class")


class ControlClass(Identity):
    """
    
    Control policy class\-map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(ControlClass, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:control-class")


class InspectClass(Identity):
    """
    
    Firewall Class Map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        super(InspectClass, self).__init__("urn:ietf:params:xml:ns:yang:c3pl-types", "policy-types", "policy-types:inspect-class")



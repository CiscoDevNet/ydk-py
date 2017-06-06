""" policy_types 

This module contains a collection of YANG groupings 
in filter configurations for policy model.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError


from ydk.models.ietf.ietf_diffserv_classifier import FilterTypeIdentity

class DirectionEnum(Enum):
    """
    DirectionEnum

    This typedef defines directional enums used in c3pl.

    inbound\:         Incoming direction.

    outbound\:        Outgoing direction.

    .. data:: inbound = 0

    .. data:: outbound = 1

    """

    inbound = 0

    outbound = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['DirectionEnum']


class MetricEnum(Enum):
    """
    MetricEnum

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

    none = 0

    peta = 1

    tera = 2

    giga = 3

    mega = 4

    kilo = 5

    milli = 6

    nano = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['MetricEnum']


class RateUnitEnum(Enum):
    """
    RateUnitEnum

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

    pps = 0

    cps = 1

    bps = 2

    perc = 3

    ratio = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['RateUnitEnum']



class MplsExpTopIdentity(FilterTypeIdentity):
    """
    Multi Protocol Label Switching experimental 
    topmost specific values
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['MplsExpTopIdentity']['meta_info']


class AtmVciIdentity(FilterTypeIdentity):
    """
    ATM VCI number
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['AtmVciIdentity']['meta_info']


class PacketLengthIdentity(FilterTypeIdentity):
    """
    Layer 3 packet length
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['PacketLengthIdentity']['meta_info']


class SecurityGroupNameIdentity(FilterTypeIdentity):
    """
    security group name
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['SecurityGroupNameIdentity']['meta_info']


class FlowDlciIdentity(FilterTypeIdentity):
    """
    Frame\-relay DLCI
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['FlowDlciIdentity']['meta_info']


class VlanInnerIdentity(FilterTypeIdentity):
    """
    Vlan\-inner
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['VlanInnerIdentity']['meta_info']


class Ipv4AclNameIdentity(FilterTypeIdentity):
    """
    IPV4 access group list
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['Ipv4AclNameIdentity']['meta_info']


class CosIdentity(FilterTypeIdentity):
    """
    
    Filter\-type IEEE 802.1Q/ISL class of service/user 
    priority values
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['CosIdentity']['meta_info']


class SecurityGroupTagIdentity(FilterTypeIdentity):
    """
    security group tag
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['SecurityGroupTagIdentity']['meta_info']


class ApplicationIdentity(FilterTypeIdentity):
    """
    application
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['ApplicationIdentity']['meta_info']


class QosGroupIdentity(FilterTypeIdentity):
    """
    QOS group
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['QosGroupIdentity']['meta_info']


class VplsIdentity(FilterTypeIdentity):
    """
    VPLS
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['VplsIdentity']['meta_info']


class Ipv4AclIdentity(FilterTypeIdentity):
    """
    IPV4 access group Index
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['Ipv4AclIdentity']['meta_info']


class FlowRecordIdentity(FilterTypeIdentity):
    """
    FLow record
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['FlowRecordIdentity']['meta_info']


class Ipv6AclNameIdentity(FilterTypeIdentity):
    """
    IPV6 access group list
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['Ipv6AclNameIdentity']['meta_info']


class VlanIdentity(FilterTypeIdentity):
    """
    Vlan
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['VlanIdentity']['meta_info']


class FlowDeIdentity(FilterTypeIdentity):
    """
    Flow DE
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['FlowDeIdentity']['meta_info']


class CosInnerIdentity(FilterTypeIdentity):
    """
    ATM VC configured as Access VC
    class of service/user priority values
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['CosInnerIdentity']['meta_info']


class IpRtpIdentity(FilterTypeIdentity):
    """
    IP RTP port
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['IpRtpIdentity']['meta_info']


class DiscardClassIdentity(FilterTypeIdentity):
    """
    Discard behavior identifier
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['DiscardClassIdentity']['meta_info']


class DstMacIdentity(FilterTypeIdentity):
    """
    Destination MAC address
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['DstMacIdentity']['meta_info']


class Ipv6AclIdentity(FilterTypeIdentity):
    """
    IPV6 access group Index
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['Ipv6AclIdentity']['meta_info']


class MetadataIdentity(FilterTypeIdentity):
    """
    metadata
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['MetadataIdentity']['meta_info']


class InputInterfaceIdentity(FilterTypeIdentity):
    """
    Input interface
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['InputInterfaceIdentity']['meta_info']


class FlowIpIdentity(FilterTypeIdentity):
    """
    Flow IP
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['FlowIpIdentity']['meta_info']


class WlanUserPriorityIdentity(FilterTypeIdentity):
    """
    WLAN user priority
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['WlanUserPriorityIdentity']['meta_info']


class DeiInnerIdentity(FilterTypeIdentity):
    """
    Frame\-relay inner DE bit
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['DeiInnerIdentity']['meta_info']


class ClassTypeIdentity(object):
    """
     
    This is identity of base class\-type
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['ClassTypeIdentity']['meta_info']


class AtmClpIdentity(FilterTypeIdentity):
    """
    ATM CLP bit
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['AtmClpIdentity']['meta_info']


class PolicyTypeIdentity(object):
    """
     
    This is identity of base policy\-type
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['PolicyTypeIdentity']['meta_info']


class MplsExpImpIdentity(FilterTypeIdentity):
    """
    Multi Protocol Label Switching experimental 
    imposition specific values
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['MplsExpImpIdentity']['meta_info']


class SrcMacIdentity(FilterTypeIdentity):
    """
    Source MAC address
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['SrcMacIdentity']['meta_info']


class ClassMapIdentity(FilterTypeIdentity):
    """
    class\-map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['ClassMapIdentity']['meta_info']


class PrecIdentity(FilterTypeIdentity):
    """
    IP precendence
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['PrecIdentity']['meta_info']


class DeiIdentity(FilterTypeIdentity):
    """
    Frame\-relay DE bit
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        FilterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['DeiIdentity']['meta_info']


class AppnavIdentity(PolicyTypeIdentity):
    """
    
    Policy\-type APPNAV Policy Map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        PolicyTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['AppnavIdentity']['meta_info']


class PacketServiceIdentity(PolicyTypeIdentity):
    """
    
    Policy\-type Packet Service Policy Map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        PolicyTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['PacketServiceIdentity']['meta_info']


class ControlIdentity(PolicyTypeIdentity):
    """
    
    Policy\-type control policy\-map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        PolicyTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['ControlIdentity']['meta_info']


class ControlClassIdentity(ClassTypeIdentity):
    """
    
    Control policy class\-map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        ClassTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['ControlClassIdentity']['meta_info']


class AccessControlIdentity(PolicyTypeIdentity):
    """
    
    Policy\-type access\-control specific policy\-map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        PolicyTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['AccessControlIdentity']['meta_info']


class InspectIdentity(PolicyTypeIdentity):
    """
    
    Policy\-type Firewall Policy Map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        PolicyTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['InspectIdentity']['meta_info']


class AccessControlClassIdentity(ClassTypeIdentity):
    """
    
    Access\-control specific class\-map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        ClassTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['AccessControlClassIdentity']['meta_info']


class AppnavClassIdentity(ClassTypeIdentity):
    """
    
    APPNAV Class Map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        ClassTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['AppnavClassIdentity']['meta_info']


class ServiceIdentity(PolicyTypeIdentity):
    """
    
    Policy\-type policymap service configuration
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        PolicyTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['ServiceIdentity']['meta_info']


class QosIdentity(PolicyTypeIdentity):
    """
    
    Policy\-type QOS (quality of service)
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        PolicyTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['QosIdentity']['meta_info']


class InspectClassIdentity(ClassTypeIdentity):
    """
    
    Firewall Class Map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        ClassTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['InspectClassIdentity']['meta_info']


class PbrIdentity(PolicyTypeIdentity):
    """
    
    Policy\-type PBR (policy based routing)
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        PolicyTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['PbrIdentity']['meta_info']


class QosClassIdentity(ClassTypeIdentity):
    """
    
    QOS class\-map
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        ClassTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['QosClassIdentity']['meta_info']


class PerfMonIdentity(PolicyTypeIdentity):
    """
    
    Policy\-type PERF\-MON (performance monitoring)
    
    

    """

    _prefix = 'policy-types'
    _revision = '2013-10-07'

    def __init__(self):
        PolicyTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _policy_types as meta
        return meta._meta_table['PerfMonIdentity']['meta_info']



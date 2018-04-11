""" openconfig_isis_lsdb_types 

This module contains general LSDB type definitions for use in ISIS YANG
model. 

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ISISTLVTYPE(Identity):
    """
    Base identity for an ISIS TLV type.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISISTLVTYPE, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:ISIS_TLV_TYPE")


class ISISSUBTLVTYPE(Identity):
    """
    Base identity for an ISIS SUB\-TLV type.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISISSUBTLVTYPE, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:ISIS_SUBTLV_TYPE")


class ISREACHABILITYSUBTLVSTYPE(Identity):
    """
    Base identity for an ISIS TLV 22, 23, 222, 223, 141 SUB\-TLV
    type.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISREACHABILITYSUBTLVSTYPE, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IS_REACHABILITY_SUBTLVS_TYPE")


class IPREACHABILITYSUBTLVSTYPE(Identity):
    """
    Base identity for an ISIS TLV 135, 235, 236, 237 SUB\-TLV
    type.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(IPREACHABILITYSUBTLVSTYPE, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IP_REACHABILITY_SUBTLVS_TYPE")


class ROUTERCAPABILITYSUBTLVSTYPE(Identity):
    """
    Base identity for an ISIS TLV 242 SUB\-TLV type.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ROUTERCAPABILITYSUBTLVSTYPE, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:ROUTER_CAPABILITY_SUBTLVS_TYPE")


class AREAADDRESSES(Identity):
    """
    ISIS TLV 1. Intermediate System to Intermediate System Intra\-
    Domain Routeing Exchange Protocol for use in Conjunction with
    the Protocol for Providing the Connectionless\-mode Network
    Service (ISO 8473), International Standard 10589\: 2002, Second
    Edition, 2002.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(AREAADDRESSES, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:AREA_ADDRESSES")


class IISNEIGHBORS(Identity):
    """
    ISIS TLV 2. Intermediate System to Intermediate System Intra\-
    Domain Routeing Exchange Protocol for use in Conjunction with
    the Protocol for Providing the Connectionless\-mode Network
    Service (ISO 8473), International Standard 10589\: 2002, Second
    Edition, 2002.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(IISNEIGHBORS, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IIS_NEIGHBORS")


class INSTANCEID(Identity):
    """
    ISIS TLV 7. An Instance Identifier (IID) to uniquely
    identify an IS\-IS instance. When the IID = 0, the list of
    supported ITIDs MUST NOT be present. An IID\-TLV with IID = 0
    MUST NOT appear in an SNP or LSP. When the TLV appears (with a
    non\-zero IID) in an SNP or LSP, exactly one ITID. MUST be
    present indicating the topology with which the PDU is
    associated. If no ITIDs or multiple ITIDs are present or the
    IID is zero, then the PDU MUST be ignored
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(INSTANCEID, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:INSTANCE_ID")


class AUTHENTICATION(Identity):
    """
    ISIS TLV 10.Intermediate System to Intermediate System Intra\-
    Domain Routeing Exchange Protocol for use in Conjunction with
    the Protocol for Providing the Connectionless\-mode Network
    Service (ISO 8473) International Standard 10589\: 2002, Second
    Edition, 2002.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(AUTHENTICATION, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:AUTHENTICATION")


class PURGEOI(Identity):
    """
    ISIS TLV 13. If an IS generates a purge, it SHOULD include
    this TLV in the purge with its own system ID.  If an IS
    receives a purge that does not include this TLV, then it SHOULD
    add this TLV with both its own system ID and the system ID of
    the IS from which it received the purge.  This allows ISs
    receiving purges to log the system ID of the originator, or the
    upstream source of the purge.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(PURGEOI, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:PURGE_OI")


class EXTENDEDISREACHABILITY(Identity):
    """
    ISIS TLV 22. An extended IS reachability TLV that has a
    different data structure to TLV 2 that introduces the use of
    sub\-TLV object\-group.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(EXTENDEDISREACHABILITY, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:EXTENDED_IS_REACHABILITY")


class ISNEIGHBORATTRIBUTE(Identity):
    """
    ISIS TLV 23. Identical in format to TLV 22 and included in
    Original LSPs or Extended LSPs. Regardless of the type of LSP
    in which the TLVs appear, the information pertains to the
    neighbor relationship between the Originating System and the IS
    identified in the TLV
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISNEIGHBORATTRIBUTE, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IS_NEIGHBOR_ATTRIBUTE")


class ISISALIASID(Identity):
    """
    ISIS TLV 24. IS\-Alias TLV which extension\-capable ISs to
    recognize the Originating System of an Extended LSP set. It
    identifies the Normal system\-id of the Originating System
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISISALIASID, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:ISIS_ALIAS_ID")


class IPV4INTERNALREACHABILITY(Identity):
    """
    ISIS TLV 128. TLV defines IP addresses within the routing
    domain reachable directly via one or more interfaces on this
    Intermediate system
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(IPV4INTERNALREACHABILITY, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IPV4_INTERNAL_REACHABILITY")


class NLPID(Identity):
    """
    ISIS TLV 129. TLV defines the set Network Layer Protocol
    Identifiers for Network Layer protocols that this Intermediate
    System is capable of relaying
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(NLPID, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:NLPID")


class IPV4EXTERNALREACHABILITY(Identity):
    """
    ISIS TLV 130. TLV defines IP addresses outside the routing domain
    reachable via interfaces on this Intermediate system. This is permitted to
    appear multiple times, and in an LSP with any LSP number. However,
    this field must not appear in pseudonode LSPs
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(IPV4EXTERNALREACHABILITY, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IPV4_EXTERNAL_REACHABILITY")


class IPV4INTERFACEADDRESSES(Identity):
    """
    ISIS TLV 132. The IP address of one or more interfaces corresponding to
    the SNPAs enabled on this Intermediate system (i.e., one or more IP
    addresses of this router). This is permitted to appear multiple times,
    and in an LSP with any LSP number.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(IPV4INTERFACEADDRESSES, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IPV4_INTERFACE_ADDRESSES")


class IPV4TEROUTERID(Identity):
    """
    ISIS TLV 134. Traffic Engineering router ID TLV that contains the 4\-octet
    router ID of the router originating the LSP
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(IPV4TEROUTERID, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IPV4_TE_ROUTER_ID")


class EXTENDEDIPV4REACHABILITY(Identity):
    """
    ISIS TLV 135. Extended IP reachability TLV that provides for a 32\-bit
    metric and adds one bit to indicate that a prefix has been redistributed
    \_down\_ in the hierarchy
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(EXTENDEDIPV4REACHABILITY, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:EXTENDED_IPV4_REACHABILITY")


class DYNAMICNAME(Identity):
    """
    ISIS TLV 137. The Dynamic hostname TLV is optional.  This TLV may be
    present in any fragment of a non\-pseudonode LSP.  The value field
    identifies the symbolic name of the router originating the LSP.  This
    symbolic name can be the FQDN for the router, it can be a subset of the
    FQDN, or it can be any string operators want to use for the router.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(DYNAMICNAME, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:DYNAMIC_NAME")


class IPV4SRLG(Identity):
    """
    ISIS TLV 138. IPv4 Shared Risk Link Group TLV
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(IPV4SRLG, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IPV4_SRLG")


class IPV6SRLG(Identity):
    """
    ISIS TLV 139. IPv6 Shared Risk Link Group
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(IPV6SRLG, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IPV6_SRLG")


class IPV6TEROUTERID(Identity):
    """
    ISIS TLV 140. The IPv6 TE Router ID TLV contains a 16\-octet IPv6 address.
    A stable global IPv6 address MUST be used, so that the router ID provides
    a routable address, regardless of the state of a node's interfaces. If a
    router does not implement traffic engineering, it MAY include or omit the
    IPv6 TE Router ID TLV.  If a router implements traffic engineering for
    IPv6, it MUST include this TLV in its LSP.  This TLV MUST NOT be included
    more than once in an LSP.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(IPV6TEROUTERID, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IPV6_TE_ROUTER_ID")


class MTISN(Identity):
    """
    ISIS TLV 222. TLV is aligned with extended IS reachability TLV type 22
    beside an additional two bytes in front at the beginning of the TLV that.
    indicate MT membership.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(MTISN, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:MT_ISN")


class MTISNEIGHBORATTRIBUTE(Identity):
    """
    ISIS TLV 223. Is is identical in format to TLV 222. In the event that
    there is a need to advertise in Extended LSPs such information associated
    with neighbors of the Originating System, it is necessary to define new
    TLVs to carry the sub\-TLV information.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(MTISNEIGHBORATTRIBUTE, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:MT_IS_NEIGHBOR_ATTRIBUTE")


class MULTITOPOLOGY(Identity):
    """
    ISIS TLV 229. This MT TLV can advertise up to 127 MTs.  It is announced
    in IIHs and LSP fragment 0, and can occur multiple times.  The resulting
    MT set SHOULD be the union of all the MT TLV occurrences in the packet.
    Any other IS\-IS PDU occurrence of this TLV MUST be ignored.  Lack of MT
    TLV in hellos and fragment zero LSPs MUST be interpreted as participation
    of the advertising interface or router in MT ID #0 only.  If a router
    advertises MT TLV, it has to advertise all the MTs it participates in,
    specifically including topology ID #0 also.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(MULTITOPOLOGY, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:MULTI_TOPOLOGY")


class IPV6INTERFACEADDRESSES(Identity):
    """
    ISIS TLV 232. IPv6 Interface Address TLV that maps directly to the IP
    Interface Address TLV in [RFC1195]. We necessarily modify the contents to
    be 0\-15 16\-octet IPv6 interface addresses instead of 0\-63 4\-octet IPv4
    interface addresses
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(IPV6INTERFACEADDRESSES, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IPV6_INTERFACE_ADDRESSES")


class MTIPV4REACHABILITY(Identity):
    """
    ISIS TLV 235. TLV is aligned with extended IP reachability TLV type 135
    beside an additional two bytes in front to indicate MT membership
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(MTIPV4REACHABILITY, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:MT_IPV4_REACHABILITY")


class IPV6REACHABILITY(Identity):
    """
    ISIS TLV 236. The IPv6 Reachability TLV describes network reachability
    through the specification of a routing prefix, metric information, a bit
    to indicate if the prefix is being advertised down from a higher level, a
    bit to indicate if the prefix is being distributed from another routing
    protocol, and OPTIONALLY the existence of Sub\-TLVs to allow for later
    extension.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(IPV6REACHABILITY, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IPV6_REACHABILITY")


class MTIPV6REACHABILITY(Identity):
    """
    ISIS TLV 237. TLV is aligned with IPv6 Reachability TLV type 236 beside
    an additional two bytes in front to indicate MT membership.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(MTIPV6REACHABILITY, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:MT_IPV6_REACHABILITY")


class ROUTERCAPABILITY(Identity):
    """
    ISIS TLV 242. IS\-IS TLV named CAPABILITY, formed of multiple sub\-TLVs,
    which allows a router to announce its capabilities within an IS\-IS level
    or the entire routing domain.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ROUTERCAPABILITY, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:ROUTER_CAPABILITY")


class ISREACHABILITYADMINGROUP(Identity):
    """
    sub\-TLV 3. Administrative group(color).
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISREACHABILITYADMINGROUP, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IS_REACHABILITY_ADMIN_GROUP")


class ISREACHABILITYIPV4INTERFACEADDRESS(Identity):
    """
    sub\-TLV 6. IPv4 Interface Address.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISREACHABILITYIPV4INTERFACEADDRESS, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IS_REACHABILITY_IPV4_INTERFACE_ADDRESS")


class ISREACHABILITYIPV4NEIGHBORADDRESS(Identity):
    """
    sub\-TLV 6. IPv4 Neighbor Address.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISREACHABILITYIPV4NEIGHBORADDRESS, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IS_REACHABILITY_IPV4_NEIGHBOR_ADDRESS")


class ISREACHABILITYMAXLINKBANDWIDTH(Identity):
    """
    sub\-TLV 9. Maximum Link Bandwidth.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISREACHABILITYMAXLINKBANDWIDTH, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IS_REACHABILITY_MAX_LINK_BANDWIDTH")


class ISREACHABILITYMAXRESERVABLEBANDWIDTH(Identity):
    """
    sub\-TLV 10. Maximum Reservable Bandwidth.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISREACHABILITYMAXRESERVABLEBANDWIDTH, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IS_REACHABILITY_MAX_RESERVABLE_BANDWIDTH")


class ISREACHABILITYUNRESERVEDBANDWIDTH(Identity):
    """
    sub\-TLV 11. Unreserved bandwidth.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISREACHABILITYUNRESERVEDBANDWIDTH, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IS_REACHABILITY_UNRESERVED_BANDWIDTH")


class ISREACHABILITYIPV6INTERFACEADDRESS(Identity):
    """
    sub\-TLV 12. IPv6 Interface Address.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISREACHABILITYIPV6INTERFACEADDRESS, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IS_REACHABILITY_IPV6_INTERFACE_ADDRESS")


class ISREACHABILITYIPV6NEIGHBORADDRESS(Identity):
    """
    sub\-TLV 13. IPv6 Neighbor Address.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISREACHABILITYIPV6NEIGHBORADDRESS, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IS_REACHABILITY_IPV6_NEIGHBOR_ADDRESS")


class ISREACHABILITYEXTENDEDADMINGROUP(Identity):
    """
    sub\-TLV 14. Extended Administrative Group.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISREACHABILITYEXTENDEDADMINGROUP, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IS_REACHABILITY_EXTENDED_ADMIN_GROUP")


class ISREACHABILITYTEDEFAULTMETRIC(Identity):
    """
    sub\-TLV 18. TE Default Metric.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISREACHABILITYTEDEFAULTMETRIC, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IS_REACHABILITY_TE_DEFAULT_METRIC")


class ISREACHABILITYLINKATTRIBUTES(Identity):
    """
    sub\-TLV 19. Link Attributes.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISREACHABILITYLINKATTRIBUTES, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IS_REACHABILITY_LINK_ATTRIBUTES")


class ISREACHABILITYLINKPROTECTIONTYPE(Identity):
    """
    sub\-TLV 20. Link Protection Type.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISREACHABILITYLINKPROTECTIONTYPE, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IS_REACHABILITY_LINK_PROTECTION_TYPE")


class ISREACHABILITYBANDWIDTHCONSTRAINTS(Identity):
    """
    sub\-TLV 22. Bandwidth Constraints.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISREACHABILITYBANDWIDTHCONSTRAINTS, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IS_REACHABILITY_BANDWIDTH_CONSTRAINTS")


class ISREACHABILITYUNCONSTRAINEDLSP(Identity):
    """
    sub\-TLV 23. Unconstrained LSP.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISREACHABILITYUNCONSTRAINEDLSP, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IS_REACHABILITY_UNCONSTRAINED_LSP")


class ISREACHABILITYADJSID(Identity):
    """
    sub\-TLV 31. Adjacency Segment Identifier.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISREACHABILITYADJSID, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IS_REACHABILITY_ADJ_SID")


class ISREACHABILITYADJLANSID(Identity):
    """
    sub\-TLV 32. Adjacency LAN Segment Identifier.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISREACHABILITYADJLANSID, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IS_REACHABILITY_ADJ_LAN_SID")


class ISREACHABILITYLINKDELAY(Identity):
    """
    sub\-TLV 33. Unidirectional Link Delay.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISREACHABILITYLINKDELAY, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IS_REACHABILITY_LINK_DELAY")


class ISREACHABILITYMINMAXLINKDELAY(Identity):
    """
    sub\-TLV 34. Min/Max Unidirectional Link Delay.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISREACHABILITYMINMAXLINKDELAY, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IS_REACHABILITY_MIN_MAX_LINK_DELAY")


class ISREACHABILITYLINKDELAYVARIATION(Identity):
    """
    sub\-TLV 35. Unidirectional Link Delay Variation.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISREACHABILITYLINKDELAYVARIATION, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IS_REACHABILITY_LINK_DELAY_VARIATION")


class ISREACHABILITYLINKLOSS(Identity):
    """
    sub\-TLV 36. Unidirectional Link Loss Delay.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISREACHABILITYLINKLOSS, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IS_REACHABILITY_LINK_LOSS")


class ISREACHABILITYRESIDUALBANDWIDTH(Identity):
    """
    sub\-TLV 37. Unidirectional Residual Bandwidth.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISREACHABILITYRESIDUALBANDWIDTH, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IS_REACHABILITY_RESIDUAL_BANDWIDTH")


class ISREACHABILITYAVAILABLEBANDWIDTH(Identity):
    """
    sub\-TLV 38. Unidirectional Available Bandwidth.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISREACHABILITYAVAILABLEBANDWIDTH, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IS_REACHABILITY_AVAILABLE_BANDWIDTH")


class ISREACHABILITYUTILIZEDBANDWIDTH(Identity):
    """
    sub\-TLV 39. Unidirectional Utilized Bandwidth.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ISREACHABILITYUTILIZEDBANDWIDTH, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IS_REACHABILITY_UTILIZED_BANDWIDTH")


class IPREACHABILITYTAG(Identity):
    """
    sub\-TLV 1. 32\-bit Administrative Tag.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(IPREACHABILITYTAG, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IP_REACHABILITY_TAG")


class IPREACHABILITYTAG64(Identity):
    """
    sub\-TLV 2. 64\-bit Administrative Tag.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(IPREACHABILITYTAG64, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IP_REACHABILITY_TAG64")


class IPREACHABILITYPREFIXSID(Identity):
    """
    sub\-TLV 3. Prefix Segment Identifier.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(IPREACHABILITYPREFIXSID, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IP_REACHABILITY_PREFIX_SID")


class IPREACHABILITYPREFIXFLAGS(Identity):
    """
    sub\-TLV 4. Prefix Attribute Flags.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(IPREACHABILITYPREFIXFLAGS, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IP_REACHABILITY_PREFIX_FLAGS")


class IPREACHABILITYIPV4ROUTERID(Identity):
    """
    sub\-TLV 11. IPv4 Source Router ID.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(IPREACHABILITYIPV4ROUTERID, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IP_REACHABILITY_IPV4_ROUTER_ID")


class IPREACHABILITYIPV6ROUTERID(Identity):
    """
    sub\-TLV 12. IPv6 Source Router ID.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(IPREACHABILITYIPV6ROUTERID, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:IP_REACHABILITY_IPV6_ROUTER_ID")


class ROUTERCAPABILITYSRCAPABILITY(Identity):
    """
    sub\-TLV 2. Segment Routing Capability.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ROUTERCAPABILITYSRCAPABILITY, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:ROUTER_CAPABILITY_SR_CAPABILITY")


class ROUTERCAPABILITYSRALGORITHM(Identity):
    """
    sub\-TLV 19. Segment Routing Algorithm.
    
    

    """

    _prefix = 'oc-isis-lsdb-types'
    _revision = '2017-05-15'

    def __init__(self):
        super(ROUTERCAPABILITYSRALGORITHM, self).__init__("http://openconfig.net/yang/isis-lsdb-types", "openconfig-isis-lsdb-types", "openconfig-isis-lsdb-types:ROUTER_CAPABILITY_SR_ALGORITHM")



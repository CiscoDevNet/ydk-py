""" Cisco_IOS_XR_infra_xtc_agent_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-xtc\-agent package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-segment\-routing\-ms\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class XtcAddressFamily(Enum):
    """
    XtcAddressFamily (Enum Class)

    Xtc address family

    .. data:: af_type_ipv4 = 1

    	IPv4 address family

    .. data:: xtc_af_type_ipv6 = 2

    	IPv6 address family

    """

    af_type_ipv4 = Enum.YLeaf(1, "af-type-ipv4")

    xtc_af_type_ipv6 = Enum.YLeaf(2, "xtc-af-type-ipv6")


class XtcAffinityRule(Enum):
    """
    XtcAffinityRule (Enum Class)

    Xtc affinity rule

    .. data:: affinity_include_all = 0

    	Include-all affinity rule

    .. data:: affinity_exclude_any = 1

    	Exclude-any affinity rule

    .. data:: affinity_include_any = 2

    	Include-any affinity rule

    """

    affinity_include_all = Enum.YLeaf(0, "affinity-include-all")

    affinity_exclude_any = Enum.YLeaf(1, "affinity-exclude-any")

    affinity_include_any = Enum.YLeaf(2, "affinity-include-any")


class XtcAutoRouteMetric(Enum):
    """
    XtcAutoRouteMetric (Enum Class)

    Xtc auto route metric

    .. data:: relative = 1

    	Autoroute relative metric type

    .. data:: constant = 3

    	Autoroute constant metric type

    """

    relative = Enum.YLeaf(1, "relative")

    constant = Enum.YLeaf(3, "constant")


class XtcBindingSid(Enum):
    """
    XtcBindingSid (Enum Class)

    Xtc binding sid

    .. data:: mpls_label_specified = 1

    	Use specified BSID MPLS label

    .. data:: mpls_label_any = 2

    	Allocate BSID MPLS label

    """

    mpls_label_specified = Enum.YLeaf(1, "mpls-label-specified")

    mpls_label_any = Enum.YLeaf(2, "mpls-label-any")


class XtcBindingSidexplicitRule(Enum):
    """
    XtcBindingSidexplicitRule (Enum Class)

    Xtc binding sidexplicit rule

    .. data:: fallback_dynamic = 1

    	Fallback dynamic option

    .. data:: enforce_srlb = 2

    	SRLB enforcement option

    """

    fallback_dynamic = Enum.YLeaf(1, "fallback-dynamic")

    enforce_srlb = Enum.YLeaf(2, "enforce-srlb")


class XtcDisjointness(Enum):
    """
    XtcDisjointness (Enum Class)

    Xtc disjointness

    .. data:: link = 1

    	Link Disjointness

    .. data:: node = 2

    	Node Disjointness

    .. data:: srlg = 3

    	SRLG Disjointness

    .. data:: srlg_node = 4

    	SRLG Node Disjointness

    """

    link = Enum.YLeaf(1, "link")

    node = Enum.YLeaf(2, "node")

    srlg = Enum.YLeaf(3, "srlg")

    srlg_node = Enum.YLeaf(4, "srlg-node")


class XtcEndPoint(Enum):
    """
    XtcEndPoint (Enum Class)

    Xtc end point

    .. data:: end_point_type_ipv4 = 1

    	IPv4 endpoint address

    .. data:: end_point_type_ipv6 = 2

    	IPv6 endpoint address

    """

    end_point_type_ipv4 = Enum.YLeaf(1, "end-point-type-ipv4")

    end_point_type_ipv6 = Enum.YLeaf(2, "end-point-type-ipv6")


class XtcMetric(Enum):
    """
    XtcMetric (Enum Class)

    Xtc metric

    .. data:: igp = 1

    	IGP metric type

    .. data:: te = 2

    	TE metric type

    .. data:: latency = 3

    	Latency metric type

    """

    igp = Enum.YLeaf(1, "igp")

    te = Enum.YLeaf(2, "te")

    latency = Enum.YLeaf(3, "latency")


class XtcMetricValue(Enum):
    """
    XtcMetricValue (Enum Class)

    Xtc metric value

    .. data:: relative = 1

    	Relative metric value

    .. data:: absolute = 2

    	Absolute metric value

    """

    relative = Enum.YLeaf(1, "relative")

    absolute = Enum.YLeaf(2, "absolute")


class XtcPath(Enum):
    """
    XtcPath (Enum Class)

    Xtc path

    .. data:: explicit = 1

    	Explicit

    .. data:: dynamic = 2

    	Dynamic

    """

    explicit = Enum.YLeaf(1, "explicit")

    dynamic = Enum.YLeaf(2, "dynamic")


class XtcPathHop(Enum):
    """
    XtcPathHop (Enum Class)

    Xtc path hop

    .. data:: mpls = 1

    	Segment-routing MPLS

    .. data:: srv6 = 2

    	Segment-routing v6

    """

    mpls = Enum.YLeaf(1, "mpls")

    srv6 = Enum.YLeaf(2, "srv6")


class XtcSegment(Enum):
    """
    XtcSegment (Enum Class)

    Xtc segment

    .. data:: ipv4_address = 1

    	IPv4 Address

    .. data:: mpls_label = 3

    	MPLS Label

    """

    ipv4_address = Enum.YLeaf(1, "ipv4-address")

    mpls_label = Enum.YLeaf(3, "mpls-label")


class XtcSteeringApplication(Enum):
    """
    XtcSteeringApplication (Enum Class)

    Xtc steering application

    .. data:: bgp = 1

    	BGP as steering client

    .. data:: isis = 2

    	ISIS as steering client

    .. data:: ospf = 3

    	OSPF as steering client

    """

    bgp = Enum.YLeaf(1, "bgp")

    isis = Enum.YLeaf(2, "isis")

    ospf = Enum.YLeaf(3, "ospf")




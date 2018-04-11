""" OSPF_MIB 

The MIB module to describe the OSPF Version 2
Protocol.  Note that some objects in this MIB
module may pose a significant security risk.
Refer to the Security Considerations section
in RFC 4750 for more information.

Copyright (C) The IETF Trust (2006).
This version of this MIB module is part of
RFC 4750;  see the RFC itself for full legal
notices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class OspfAuthenticationType(Enum):
    """
    OspfAuthenticationType (Enum Class)

    The authentication type.

    .. data:: none = 0

    .. data:: simplePassword = 1

    .. data:: md5 = 2

    """

    none = Enum.YLeaf(0, "none")

    simplePassword = Enum.YLeaf(1, "simplePassword")

    md5 = Enum.YLeaf(2, "md5")


class Status(Enum):
    """
    Status (Enum Class)

    An indication of the operability of an OSPF

    function or feature.  For example, the status

    of an interface\: 'enabled' indicates that

    it is willing to communicate with other OSPF routers,

    and 'disabled' indicates that it is not.

    .. data:: enabled = 1

    .. data:: disabled = 2

    """

    enabled = Enum.YLeaf(1, "enabled")

    disabled = Enum.YLeaf(2, "disabled")



class OSPFMIB(Entity):
    """
    
    
    .. attribute:: ospfgeneralgroup
    
    	
    	**type**\:  :py:class:`Ospfgeneralgroup <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfgeneralgroup>`
    
    .. attribute:: ospfareatable
    
    	Information describing the configured parameters and cumulative statistics of the router's attached areas. The interfaces and virtual links are configured as part of these areas.  Area 0.0.0.0, by definition, is the backbone area
    	**type**\:  :py:class:`Ospfareatable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfareatable>`
    
    .. attribute:: ospfstubareatable
    
    	The set of metrics that will be advertised by a default Area Border Router into a stub area
    	**type**\:  :py:class:`Ospfstubareatable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfstubareatable>`
    
    .. attribute:: ospflsdbtable
    
    	The OSPF Process's link state database (LSDB). The LSDB contains the link state advertisements from throughout the areas that the device is attached to
    	**type**\:  :py:class:`Ospflsdbtable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospflsdbtable>`
    
    .. attribute:: ospfarearangetable
    
    	The Address Range Table acts as an adjunct to the Area Table.  It describes those Address Range Summaries that are configured to be propagated from an Area to reduce the amount of information about it that is known beyond its borders.  It contains a set of IP address ranges specified by an IP address/IP network mask pair. For example, class B address range of X.X.X.X with a network mask of 255.255.0.0 includes all IP addresses from X.X.0.0 to X.X.255.255.  Note that this table is obsoleted and is replaced by the Area Aggregate Table
    	**type**\:  :py:class:`Ospfarearangetable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfarearangetable>`
    
    	**status**\: obsolete
    
    .. attribute:: ospfhosttable
    
    	The Host/Metric Table indicates what hosts are directly  attached to the router, what metrics and types of service should be advertised for them, and what areas they are found within
    	**type**\:  :py:class:`Ospfhosttable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfhosttable>`
    
    .. attribute:: ospfiftable
    
    	The OSPF Interface Table describes the interfaces from the viewpoint of OSPF. It augments the ipAddrTable with OSPF specific information
    	**type**\:  :py:class:`Ospfiftable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfiftable>`
    
    .. attribute:: ospfifmetrictable
    
    	The Metric Table describes the metrics to be advertised for a specified interface at the various types of service. As such, this table is an adjunct of the OSPF Interface Table.  Types of service, as defined by RFC 791, have the ability to request low delay, high bandwidth, or reliable linkage.  For the purposes of this specification, the measure of bandwidth\:  Metric = referenceBandwidth / ifSpeed  is the default value. The default reference bandwidth is 10^8. For multiple link interfaces, note that ifSpeed is the sum of the individual link speeds.  This yields a number having the following typical values\:  Network Type/bit rate   Metric  >= 100 MBPS                 1 Ethernet/802.3             10 E1                         48 T1 (ESF)                   65 64 KBPS                    1562 56 KBPS                    1785 19.2 KBPS                  5208 9.6 KBPS                   10416  Routes that are not specified use the default (TOS 0) metric.  Note that the default reference bandwidth can be configured using the general group object ospfReferenceBandwidth
    	**type**\:  :py:class:`Ospfifmetrictable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfifmetrictable>`
    
    .. attribute:: ospfvirtiftable
    
    	Information about this router's virtual interfaces that the OSPF Process is configured to carry on
    	**type**\:  :py:class:`Ospfvirtiftable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfvirtiftable>`
    
    .. attribute:: ospfnbrtable
    
    	A table describing all non\-virtual neighbors in the locality of the OSPF router
    	**type**\:  :py:class:`Ospfnbrtable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfnbrtable>`
    
    .. attribute:: ospfvirtnbrtable
    
    	This table describes all virtual neighbors. Since virtual links are configured in the Virtual Interface Table, this table is read\-only
    	**type**\:  :py:class:`Ospfvirtnbrtable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfvirtnbrtable>`
    
    .. attribute:: ospfextlsdbtable
    
    	The OSPF Process's external LSA link state database.  This table is identical to the OSPF LSDB Table in format, but contains only external link state advertisements.  The purpose is to allow external  LSAs to be displayed once for the router rather than once in each non\-stub area.  Note that external LSAs are also in the AS\-scope link state database
    	**type**\:  :py:class:`Ospfextlsdbtable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfextlsdbtable>`
    
    	**status**\: deprecated
    
    .. attribute:: ospfareaaggregatetable
    
    	The Area Aggregate Table acts as an adjunct to the Area Table.  It describes those address aggregates that are configured to be propagated from an area. Its purpose is to reduce the amount of information that is known beyond an Area's borders.  It contains a set of IP address ranges specified by an IP address/IP network mask pair. For example, a class B address range of X.X.X.X with a network mask of 255.255.0.0 includes all IP addresses from X.X.0.0 to X.X.255.255.  Note that if ranges are configured such that one range subsumes another range (e.g., 10.0.0.0 mask 255.0.0.0 and 10.1.0.0 mask 255.255.0.0), the most specific match is the preferred one
    	**type**\:  :py:class:`Ospfareaaggregatetable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfareaaggregatetable>`
    
    .. attribute:: ospflocallsdbtable
    
    	The OSPF Process's link\-local link state database for non\-virtual links. This table is identical to the OSPF LSDB Table in format, but contains only link\-local Link State Advertisements for non\-virtual links.  The purpose is to allow link\-local LSAs to be displayed for each non\-virtual interface.  This table is implemented to support type\-9 LSAs that are defined in 'The OSPF Opaque LSA Option'
    	**type**\:  :py:class:`Ospflocallsdbtable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospflocallsdbtable>`
    
    .. attribute:: ospfvirtlocallsdbtable
    
    	The OSPF Process's link\-local link state database for virtual links.  This table is identical to the OSPF LSDB Table in format, but contains only link\-local Link State Advertisements for virtual links.  The purpose is to allow link\-local LSAs to be displayed for each virtual interface.  This table is implemented to support type\-9 LSAs that are defined in 'The OSPF Opaque LSA Option'
    	**type**\:  :py:class:`Ospfvirtlocallsdbtable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfvirtlocallsdbtable>`
    
    .. attribute:: ospfaslsdbtable
    
    	The OSPF Process's AS\-scope LSA link state database. The database contains the AS\-scope Link State Advertisements from throughout the areas that the device is attached to.  This table is identical to the OSPF LSDB Table in format, but contains only AS\-scope Link State Advertisements.  The purpose is to allow AS\-scope LSAs to be displayed once for the router rather than once in each non\-stub area
    	**type**\:  :py:class:`Ospfaslsdbtable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfaslsdbtable>`
    
    .. attribute:: ospfarealsacounttable
    
    	This table maintains per\-area, per\-LSA\-type counters
    	**type**\:  :py:class:`Ospfarealsacounttable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfarealsacounttable>`
    
    

    """

    _prefix = 'OSPF-MIB'
    _revision = '2006-11-10'

    def __init__(self):
        super(OSPFMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "OSPF-MIB"
        self.yang_parent_name = "OSPF-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("ospfGeneralGroup", ("ospfgeneralgroup", OSPFMIB.Ospfgeneralgroup)), ("ospfAreaTable", ("ospfareatable", OSPFMIB.Ospfareatable)), ("ospfStubAreaTable", ("ospfstubareatable", OSPFMIB.Ospfstubareatable)), ("ospfLsdbTable", ("ospflsdbtable", OSPFMIB.Ospflsdbtable)), ("ospfAreaRangeTable", ("ospfarearangetable", OSPFMIB.Ospfarearangetable)), ("ospfHostTable", ("ospfhosttable", OSPFMIB.Ospfhosttable)), ("ospfIfTable", ("ospfiftable", OSPFMIB.Ospfiftable)), ("ospfIfMetricTable", ("ospfifmetrictable", OSPFMIB.Ospfifmetrictable)), ("ospfVirtIfTable", ("ospfvirtiftable", OSPFMIB.Ospfvirtiftable)), ("ospfNbrTable", ("ospfnbrtable", OSPFMIB.Ospfnbrtable)), ("ospfVirtNbrTable", ("ospfvirtnbrtable", OSPFMIB.Ospfvirtnbrtable)), ("ospfExtLsdbTable", ("ospfextlsdbtable", OSPFMIB.Ospfextlsdbtable)), ("ospfAreaAggregateTable", ("ospfareaaggregatetable", OSPFMIB.Ospfareaaggregatetable)), ("ospfLocalLsdbTable", ("ospflocallsdbtable", OSPFMIB.Ospflocallsdbtable)), ("ospfVirtLocalLsdbTable", ("ospfvirtlocallsdbtable", OSPFMIB.Ospfvirtlocallsdbtable)), ("ospfAsLsdbTable", ("ospfaslsdbtable", OSPFMIB.Ospfaslsdbtable)), ("ospfAreaLsaCountTable", ("ospfarealsacounttable", OSPFMIB.Ospfarealsacounttable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.ospfgeneralgroup = OSPFMIB.Ospfgeneralgroup()
        self.ospfgeneralgroup.parent = self
        self._children_name_map["ospfgeneralgroup"] = "ospfGeneralGroup"
        self._children_yang_names.add("ospfGeneralGroup")

        self.ospfareatable = OSPFMIB.Ospfareatable()
        self.ospfareatable.parent = self
        self._children_name_map["ospfareatable"] = "ospfAreaTable"
        self._children_yang_names.add("ospfAreaTable")

        self.ospfstubareatable = OSPFMIB.Ospfstubareatable()
        self.ospfstubareatable.parent = self
        self._children_name_map["ospfstubareatable"] = "ospfStubAreaTable"
        self._children_yang_names.add("ospfStubAreaTable")

        self.ospflsdbtable = OSPFMIB.Ospflsdbtable()
        self.ospflsdbtable.parent = self
        self._children_name_map["ospflsdbtable"] = "ospfLsdbTable"
        self._children_yang_names.add("ospfLsdbTable")

        self.ospfarearangetable = OSPFMIB.Ospfarearangetable()
        self.ospfarearangetable.parent = self
        self._children_name_map["ospfarearangetable"] = "ospfAreaRangeTable"
        self._children_yang_names.add("ospfAreaRangeTable")

        self.ospfhosttable = OSPFMIB.Ospfhosttable()
        self.ospfhosttable.parent = self
        self._children_name_map["ospfhosttable"] = "ospfHostTable"
        self._children_yang_names.add("ospfHostTable")

        self.ospfiftable = OSPFMIB.Ospfiftable()
        self.ospfiftable.parent = self
        self._children_name_map["ospfiftable"] = "ospfIfTable"
        self._children_yang_names.add("ospfIfTable")

        self.ospfifmetrictable = OSPFMIB.Ospfifmetrictable()
        self.ospfifmetrictable.parent = self
        self._children_name_map["ospfifmetrictable"] = "ospfIfMetricTable"
        self._children_yang_names.add("ospfIfMetricTable")

        self.ospfvirtiftable = OSPFMIB.Ospfvirtiftable()
        self.ospfvirtiftable.parent = self
        self._children_name_map["ospfvirtiftable"] = "ospfVirtIfTable"
        self._children_yang_names.add("ospfVirtIfTable")

        self.ospfnbrtable = OSPFMIB.Ospfnbrtable()
        self.ospfnbrtable.parent = self
        self._children_name_map["ospfnbrtable"] = "ospfNbrTable"
        self._children_yang_names.add("ospfNbrTable")

        self.ospfvirtnbrtable = OSPFMIB.Ospfvirtnbrtable()
        self.ospfvirtnbrtable.parent = self
        self._children_name_map["ospfvirtnbrtable"] = "ospfVirtNbrTable"
        self._children_yang_names.add("ospfVirtNbrTable")

        self.ospfextlsdbtable = OSPFMIB.Ospfextlsdbtable()
        self.ospfextlsdbtable.parent = self
        self._children_name_map["ospfextlsdbtable"] = "ospfExtLsdbTable"
        self._children_yang_names.add("ospfExtLsdbTable")

        self.ospfareaaggregatetable = OSPFMIB.Ospfareaaggregatetable()
        self.ospfareaaggregatetable.parent = self
        self._children_name_map["ospfareaaggregatetable"] = "ospfAreaAggregateTable"
        self._children_yang_names.add("ospfAreaAggregateTable")

        self.ospflocallsdbtable = OSPFMIB.Ospflocallsdbtable()
        self.ospflocallsdbtable.parent = self
        self._children_name_map["ospflocallsdbtable"] = "ospfLocalLsdbTable"
        self._children_yang_names.add("ospfLocalLsdbTable")

        self.ospfvirtlocallsdbtable = OSPFMIB.Ospfvirtlocallsdbtable()
        self.ospfvirtlocallsdbtable.parent = self
        self._children_name_map["ospfvirtlocallsdbtable"] = "ospfVirtLocalLsdbTable"
        self._children_yang_names.add("ospfVirtLocalLsdbTable")

        self.ospfaslsdbtable = OSPFMIB.Ospfaslsdbtable()
        self.ospfaslsdbtable.parent = self
        self._children_name_map["ospfaslsdbtable"] = "ospfAsLsdbTable"
        self._children_yang_names.add("ospfAsLsdbTable")

        self.ospfarealsacounttable = OSPFMIB.Ospfarealsacounttable()
        self.ospfarealsacounttable.parent = self
        self._children_name_map["ospfarealsacounttable"] = "ospfAreaLsaCountTable"
        self._children_yang_names.add("ospfAreaLsaCountTable")
        self._segment_path = lambda: "OSPF-MIB:OSPF-MIB"


    class Ospfgeneralgroup(Entity):
        """
        
        
        .. attribute:: ospfrouterid
        
        	A 32\-bit integer uniquely identifying the router in the Autonomous System. By convention, to ensure uniqueness, this should default to the value of one of the router's IP interface addresses.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: ospfadminstat
        
        	The administrative status of OSPF in the router.  The value 'enabled' denotes that the OSPF Process is active on at least one interface; 'disabled' disables it on all interfaces.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\:  :py:class:`Status <ydk.models.cisco_ios_xe.OSPF_MIB.Status>`
        
        .. attribute:: ospfversionnumber
        
        	The current version number of the OSPF protocol is 2
        	**type**\:  :py:class:`Ospfversionnumber <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfgeneralgroup.Ospfversionnumber>`
        
        .. attribute:: ospfareabdrrtrstatus
        
        	A flag to note whether this router is an Area Border Router
        	**type**\: bool
        
        .. attribute:: ospfasbdrrtrstatus
        
        	A flag to note whether this router is configured as an Autonomous System Border Router.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\: bool
        
        .. attribute:: ospfexternlsacount
        
        	The number of external (LS type\-5) link state advertisements in the link state database
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ospfexternlsacksumsum
        
        	The 32\-bit sum of the LS checksums of the external link state advertisements contained in the link state database.  This sum can be used to determine if there has been a change in a router's link state database and to compare the link state database of two routers.  The value should be treated as unsigned when comparing two sums of checksums
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: ospftossupport
        
        	The router's support for type\-of\-service routing.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\: bool
        
        .. attribute:: ospforiginatenewlsas
        
        	The number of new link state advertisements that have been originated.  This number is incremented each time the router originates a new LSA.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ospfDiscontinuityTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ospfrxnewlsas
        
        	The number of link state advertisements received that are determined to be new instantiations. This number does not include newer instantiations of self\-originated link state advertisements.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ospfDiscontinuityTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ospfextlsdblimit
        
        	The maximum number of non\-default AS\-external LSAs entries that can be stored in the link state database.  If the value is \-1, then there is no limit.  When the number of non\-default AS\-external LSAs in a router's link state database reaches ospfExtLsdbLimit, the router enters overflow state.  The router never holds more than ospfExtLsdbLimit non\-default AS\-external LSAs in its database.  OspfExtLsdbLimit MUST be set identically in all routers attached to the OSPF backbone and/or any regular OSPF area (i.e., OSPF stub areas and NSSAs are excluded).  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\: int
        
        	**range:** \-1..2147483647
        
        .. attribute:: ospfmulticastextensions
        
        	A bit mask indicating whether the router is forwarding IP multicast (Class D) datagrams based on the algorithms defined in the multicast extensions to OSPF.  Bit 0, if set, indicates that the router can  forward IP multicast datagrams in the router's directly attached areas (called intra\-area multicast routing).  Bit 1, if set, indicates that the router can forward IP multicast datagrams between OSPF areas (called inter\-area multicast routing).  Bit 2, if set, indicates that the router can forward IP multicast datagrams between Autonomous Systems (called inter\-AS multicast routing).  Only certain combinations of bit settings are allowed, namely\: 0 (no multicast forwarding is enabled), 1 (intra\-area multicasting only), 3 (intra\-area and inter\-area multicasting), 5 (intra\-area and inter\-AS multicasting), and 7 (multicasting everywhere).  By default, no multicast forwarding is enabled.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: ospfexitoverflowinterval
        
        	The number of seconds that, after entering OverflowState, a router will attempt to leave OverflowState.  This allows the router to again originate non\-default AS\-external LSAs.  When set to 0, the router will not leave overflow state until restarted.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: ospfdemandextensions
        
        	The router's support for demand routing. This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\: bool
        
        .. attribute:: ospfrfc1583compatibility
        
        	Indicates metrics used to choose among multiple AS\-external LSAs.  When RFC1583Compatibility is set to enabled, only cost will be used when choosing among multiple AS\-external LSAs advertising the same destination.  When RFC1583Compatibility is set to disabled, preference will be driven first by type of path using cost only to break ties.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\: bool
        
        .. attribute:: ospfopaquelsasupport
        
        	The router's support for Opaque LSA types
        	**type**\: bool
        
        .. attribute:: ospfreferencebandwidth
        
        	Reference bandwidth in kilobits/second for  calculating default interface metrics.  The default value is 100,000 KBPS (100 MBPS).  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: kilobits per second
        
        .. attribute:: ospfrestartsupport
        
        	The router's support for OSPF graceful restart. Options include\: no restart support, only planned restarts, or both planned and unplanned restarts.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\:  :py:class:`Ospfrestartsupport <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfgeneralgroup.Ospfrestartsupport>`
        
        .. attribute:: ospfrestartinterval
        
        	Configured OSPF graceful restart timeout interval.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\: int
        
        	**range:** 1..1800
        
        	**units**\: seconds
        
        .. attribute:: ospfrestartstrictlsachecking
        
        	Indicates if strict LSA checking is enabled for graceful restart.  This object is persistent and when written the entity SHOULD save the change to non\-volatile  storage
        	**type**\: bool
        
        .. attribute:: ospfrestartstatus
        
        	Current status of OSPF graceful restart
        	**type**\:  :py:class:`Ospfrestartstatus <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfgeneralgroup.Ospfrestartstatus>`
        
        .. attribute:: ospfrestartage
        
        	Remaining time in current OSPF graceful restart interval
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: seconds
        
        .. attribute:: ospfrestartexitreason
        
        	Describes the outcome of the last attempt at a graceful restart.  If the value is 'none', no restart has yet been attempted.  If the value is 'inProgress', a restart attempt is currently underway
        	**type**\:  :py:class:`Ospfrestartexitreason <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfgeneralgroup.Ospfrestartexitreason>`
        
        .. attribute:: ospfaslsacount
        
        	The number of AS\-scope link state advertisements in the AS\-scope link state database
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ospfaslsacksumsum
        
        	The 32\-bit unsigned sum of the LS checksums of the AS link state advertisements contained in the AS\-scope link state database.  This sum can be used to determine if there has been a change in a router's AS\-scope link state database, and to compare the AS\-scope link state database of two routers
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ospfstubroutersupport
        
        	The router's support for stub router functionality
        	**type**\: bool
        
        .. attribute:: ospfstubrouteradvertisement
        
        	This object controls the advertisement of stub router LSAs by the router.  The value doNotAdvertise will result in the advertisement of a standard router LSA and is the default value.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\:  :py:class:`Ospfstubrouteradvertisement <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfgeneralgroup.Ospfstubrouteradvertisement>`
        
        .. attribute:: ospfdiscontinuitytime
        
        	The value of sysUpTime on the most recent occasion at which any one of this MIB's counters suffered a discontinuity.  If no such discontinuities have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.Ospfgeneralgroup, self).__init__()

            self.yang_name = "ospfGeneralGroup"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ospfrouterid', YLeaf(YType.str, 'ospfRouterId')),
                ('ospfadminstat', YLeaf(YType.enumeration, 'ospfAdminStat')),
                ('ospfversionnumber', YLeaf(YType.enumeration, 'ospfVersionNumber')),
                ('ospfareabdrrtrstatus', YLeaf(YType.boolean, 'ospfAreaBdrRtrStatus')),
                ('ospfasbdrrtrstatus', YLeaf(YType.boolean, 'ospfASBdrRtrStatus')),
                ('ospfexternlsacount', YLeaf(YType.uint32, 'ospfExternLsaCount')),
                ('ospfexternlsacksumsum', YLeaf(YType.int32, 'ospfExternLsaCksumSum')),
                ('ospftossupport', YLeaf(YType.boolean, 'ospfTOSSupport')),
                ('ospforiginatenewlsas', YLeaf(YType.uint32, 'ospfOriginateNewLsas')),
                ('ospfrxnewlsas', YLeaf(YType.uint32, 'ospfRxNewLsas')),
                ('ospfextlsdblimit', YLeaf(YType.int32, 'ospfExtLsdbLimit')),
                ('ospfmulticastextensions', YLeaf(YType.int32, 'ospfMulticastExtensions')),
                ('ospfexitoverflowinterval', YLeaf(YType.int32, 'ospfExitOverflowInterval')),
                ('ospfdemandextensions', YLeaf(YType.boolean, 'ospfDemandExtensions')),
                ('ospfrfc1583compatibility', YLeaf(YType.boolean, 'ospfRFC1583Compatibility')),
                ('ospfopaquelsasupport', YLeaf(YType.boolean, 'ospfOpaqueLsaSupport')),
                ('ospfreferencebandwidth', YLeaf(YType.uint32, 'ospfReferenceBandwidth')),
                ('ospfrestartsupport', YLeaf(YType.enumeration, 'ospfRestartSupport')),
                ('ospfrestartinterval', YLeaf(YType.int32, 'ospfRestartInterval')),
                ('ospfrestartstrictlsachecking', YLeaf(YType.boolean, 'ospfRestartStrictLsaChecking')),
                ('ospfrestartstatus', YLeaf(YType.enumeration, 'ospfRestartStatus')),
                ('ospfrestartage', YLeaf(YType.uint32, 'ospfRestartAge')),
                ('ospfrestartexitreason', YLeaf(YType.enumeration, 'ospfRestartExitReason')),
                ('ospfaslsacount', YLeaf(YType.uint32, 'ospfAsLsaCount')),
                ('ospfaslsacksumsum', YLeaf(YType.uint32, 'ospfAsLsaCksumSum')),
                ('ospfstubroutersupport', YLeaf(YType.boolean, 'ospfStubRouterSupport')),
                ('ospfstubrouteradvertisement', YLeaf(YType.enumeration, 'ospfStubRouterAdvertisement')),
                ('ospfdiscontinuitytime', YLeaf(YType.uint32, 'ospfDiscontinuityTime')),
            ])
            self.ospfrouterid = None
            self.ospfadminstat = None
            self.ospfversionnumber = None
            self.ospfareabdrrtrstatus = None
            self.ospfasbdrrtrstatus = None
            self.ospfexternlsacount = None
            self.ospfexternlsacksumsum = None
            self.ospftossupport = None
            self.ospforiginatenewlsas = None
            self.ospfrxnewlsas = None
            self.ospfextlsdblimit = None
            self.ospfmulticastextensions = None
            self.ospfexitoverflowinterval = None
            self.ospfdemandextensions = None
            self.ospfrfc1583compatibility = None
            self.ospfopaquelsasupport = None
            self.ospfreferencebandwidth = None
            self.ospfrestartsupport = None
            self.ospfrestartinterval = None
            self.ospfrestartstrictlsachecking = None
            self.ospfrestartstatus = None
            self.ospfrestartage = None
            self.ospfrestartexitreason = None
            self.ospfaslsacount = None
            self.ospfaslsacksumsum = None
            self.ospfstubroutersupport = None
            self.ospfstubrouteradvertisement = None
            self.ospfdiscontinuitytime = None
            self._segment_path = lambda: "ospfGeneralGroup"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.Ospfgeneralgroup, ['ospfrouterid', 'ospfadminstat', 'ospfversionnumber', 'ospfareabdrrtrstatus', 'ospfasbdrrtrstatus', 'ospfexternlsacount', 'ospfexternlsacksumsum', 'ospftossupport', 'ospforiginatenewlsas', 'ospfrxnewlsas', 'ospfextlsdblimit', 'ospfmulticastextensions', 'ospfexitoverflowinterval', 'ospfdemandextensions', 'ospfrfc1583compatibility', 'ospfopaquelsasupport', 'ospfreferencebandwidth', 'ospfrestartsupport', 'ospfrestartinterval', 'ospfrestartstrictlsachecking', 'ospfrestartstatus', 'ospfrestartage', 'ospfrestartexitreason', 'ospfaslsacount', 'ospfaslsacksumsum', 'ospfstubroutersupport', 'ospfstubrouteradvertisement', 'ospfdiscontinuitytime'], name, value)

        class Ospfrestartexitreason(Enum):
            """
            Ospfrestartexitreason (Enum Class)

            Describes the outcome of the last attempt at a

            graceful restart.  If the value is 'none', no restart

            has yet been attempted.  If the value is 'inProgress',

            a restart attempt is currently underway.

            .. data:: none = 1

            .. data:: inProgress = 2

            .. data:: completed = 3

            .. data:: timedOut = 4

            .. data:: topologyChanged = 5

            """

            none = Enum.YLeaf(1, "none")

            inProgress = Enum.YLeaf(2, "inProgress")

            completed = Enum.YLeaf(3, "completed")

            timedOut = Enum.YLeaf(4, "timedOut")

            topologyChanged = Enum.YLeaf(5, "topologyChanged")


        class Ospfrestartstatus(Enum):
            """
            Ospfrestartstatus (Enum Class)

            Current status of OSPF graceful restart.

            .. data:: notRestarting = 1

            .. data:: plannedRestart = 2

            .. data:: unplannedRestart = 3

            """

            notRestarting = Enum.YLeaf(1, "notRestarting")

            plannedRestart = Enum.YLeaf(2, "plannedRestart")

            unplannedRestart = Enum.YLeaf(3, "unplannedRestart")


        class Ospfrestartsupport(Enum):
            """
            Ospfrestartsupport (Enum Class)

            The router's support for OSPF graceful restart.

            Options include\: no restart support, only planned

            restarts, or both planned and unplanned restarts.

            This object is persistent and when written

            the entity SHOULD save the change to non\-volatile

            storage.

            .. data:: none = 1

            .. data:: plannedOnly = 2

            .. data:: plannedAndUnplanned = 3

            """

            none = Enum.YLeaf(1, "none")

            plannedOnly = Enum.YLeaf(2, "plannedOnly")

            plannedAndUnplanned = Enum.YLeaf(3, "plannedAndUnplanned")


        class Ospfstubrouteradvertisement(Enum):
            """
            Ospfstubrouteradvertisement (Enum Class)

            This object controls the advertisement of

            stub router LSAs by the router.  The value

            doNotAdvertise will result in the advertisement

            of a standard router LSA and is the default value.

            This object is persistent and when written

            the entity SHOULD save the change to non\-volatile

            storage.

            .. data:: doNotAdvertise = 1

            .. data:: advertise = 2

            """

            doNotAdvertise = Enum.YLeaf(1, "doNotAdvertise")

            advertise = Enum.YLeaf(2, "advertise")


        class Ospfversionnumber(Enum):
            """
            Ospfversionnumber (Enum Class)

            The current version number of the OSPF protocol is 2.

            .. data:: version2 = 2

            """

            version2 = Enum.YLeaf(2, "version2")



    class Ospfareatable(Entity):
        """
        Information describing the configured parameters and
        cumulative statistics of the router's attached areas.
        The interfaces and virtual links are configured
        as part of these areas.  Area 0.0.0.0, by definition,
        is the backbone area.
        
        .. attribute:: ospfareaentry
        
        	Information describing the configured parameters and cumulative statistics of one of the router's attached areas. The interfaces and virtual links are configured as part of these areas.  Area 0.0.0.0, by definition, is the backbone area.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile storage
        	**type**\: list of  		 :py:class:`Ospfareaentry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfareatable.Ospfareaentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.Ospfareatable, self).__init__()

            self.yang_name = "ospfAreaTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ospfAreaEntry", ("ospfareaentry", OSPFMIB.Ospfareatable.Ospfareaentry))])
            self._leafs = OrderedDict()

            self.ospfareaentry = YList(self)
            self._segment_path = lambda: "ospfAreaTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.Ospfareatable, [], name, value)


        class Ospfareaentry(Entity):
            """
            Information describing the configured parameters and
            cumulative statistics of one of the router's attached areas.
            The interfaces and virtual links are configured as part of
            these areas.  Area 0.0.0.0, by definition, is the backbone
            area.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            storage.
            
            .. attribute:: ospfareaid  (key)
            
            	A 32\-bit integer uniquely identifying an area. Area ID 0.0.0.0 is used for the OSPF backbone
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfauthtype
            
            	The authentication type specified for an area
            	**type**\:  :py:class:`OspfAuthenticationType <ydk.models.cisco_ios_xe.OSPF_MIB.OspfAuthenticationType>`
            
            	**status**\: obsolete
            
            .. attribute:: ospfimportasextern
            
            	Indicates if an area is a stub area, NSSA, or standard area.  Type\-5 AS\-external LSAs and type\-11 Opaque LSAs are not imported into stub areas or NSSAs.  NSSAs import AS\-external data as type\-7 LSAs
            	**type**\:  :py:class:`Ospfimportasextern <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfareatable.Ospfareaentry.Ospfimportasextern>`
            
            .. attribute:: ospfspfruns
            
            	The number of times that the intra\-area route table has been calculated using this area's link state database.  This is typically done using Dijkstra's algorithm.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ospfDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfareabdrrtrcount
            
            	The total number of Area Border Routers reachable within this area.  This is initially zero and is calculated in each Shortest Path First (SPF) pass
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfasbdrrtrcount
            
            	The total number of Autonomous System Border Routers reachable within this area.  This is initially zero and is calculated in each SPF pass
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfarealsacount
            
            	The total number of link state advertisements in this area's link state database, excluding AS\-external LSAs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfarealsacksumsum
            
            	The 32\-bit sum of the link state advertisements' LS checksums contained in this area's link state database.  This sum excludes external (LS type\-5) link state advertisements. The sum can be used to determine if there has been a change in a router's link state database, and to compare the link state database of two routers.  The value should be treated as unsigned when comparing two sums of checksums
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospfareasummary
            
            	The variable ospfAreaSummary controls the import of summary LSAs into stub and NSSA areas. It has no effect on other areas.  If it is noAreaSummary, the router will not originate summary LSAs into the stub or NSSA area. It will rely entirely on its default route.  If it is sendAreaSummary, the router will both summarize and propagate summary LSAs
            	**type**\:  :py:class:`Ospfareasummary <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfareatable.Ospfareaentry.Ospfareasummary>`
            
            .. attribute:: ospfareastatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: ospfareanssatranslatorrole
            
            	Indicates an NSSA border router's ability to perform NSSA translation of type\-7 LSAs into type\-5 LSAs
            	**type**\:  :py:class:`Ospfareanssatranslatorrole <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfareatable.Ospfareaentry.Ospfareanssatranslatorrole>`
            
            .. attribute:: ospfareanssatranslatorstate
            
            	Indicates if and how an NSSA border router is performing NSSA translation of type\-7 LSAs into type\-5  LSAs.  When this object is set to enabled, the NSSA Border router's OspfAreaNssaExtTranslatorRole has been set to always.  When this object is set to elected, a candidate NSSA Border router is Translating type\-7 LSAs into type\-5. When this object is set to disabled, a candidate NSSA border router is NOT translating type\-7 LSAs into type\-5
            	**type**\:  :py:class:`Ospfareanssatranslatorstate <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfareatable.Ospfareaentry.Ospfareanssatranslatorstate>`
            
            .. attribute:: ospfareanssatranslatorstabilityinterval
            
            	The number of seconds after an elected translator determines its services are no longer required, that it should continue to perform its translation duties
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: ospfareanssatranslatorevents
            
            	Indicates the number of translator state changes that have occurred since the last boot\-up.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ospfDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfopaquearealsacount
            
            	The total number of Opaque Area and AS link\-state  advertisements in the link state database of this area
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfopaquearealsacksumsum
            
            	The 32\-bit unsigned sum of the Opaque Area and AS  link\-state advertisements' LS checksums contained  link state database of this area.  The sum can be  used to determine if there has been a change in the  link state database for Opaque Area and AS link\-state advertisements
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfareanssatranslatorrole
            
            	Indicates an NSSA Border router's ability to perform NSSA translation of type\-7 LSAs into type\-5 LSAs
            	**type**\:  :py:class:`Cospfareanssatranslatorrole <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfareatable.Ospfareaentry.Cospfareanssatranslatorrole>`
            
            .. attribute:: cospfareanssatranslatorstate
            
            	Indicates if and how an NSSA Border router is performing NSSA translation of type\-7 LSAs into type\-5 LSAs. When this object set to enabled, the NSSA Border router's cospfAreaNssaExtTranslatorRole has been set to always. When this object is set to elected, a candidate NSSA Border router is Translating type\-7 LSAs into type\-5. When this object is set to disabled, a candidate NSSA Border router is NOT translating type\-7 LSAs into type\-5
            	**type**\:  :py:class:`Cospfareanssatranslatorstate <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfareatable.Ospfareaentry.Cospfareanssatranslatorstate>`
            
            .. attribute:: cospfareanssatranslatorevents
            
            	Indicates the number of Translator State changes that have occurred since the last boot\-up
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OSPFMIB.Ospfareatable.Ospfareaentry, self).__init__()

                self.yang_name = "ospfAreaEntry"
                self.yang_parent_name = "ospfAreaTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfareaid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfareaid', YLeaf(YType.str, 'ospfAreaId')),
                    ('ospfauthtype', YLeaf(YType.enumeration, 'ospfAuthType')),
                    ('ospfimportasextern', YLeaf(YType.enumeration, 'ospfImportAsExtern')),
                    ('ospfspfruns', YLeaf(YType.uint32, 'ospfSpfRuns')),
                    ('ospfareabdrrtrcount', YLeaf(YType.uint32, 'ospfAreaBdrRtrCount')),
                    ('ospfasbdrrtrcount', YLeaf(YType.uint32, 'ospfAsBdrRtrCount')),
                    ('ospfarealsacount', YLeaf(YType.uint32, 'ospfAreaLsaCount')),
                    ('ospfarealsacksumsum', YLeaf(YType.int32, 'ospfAreaLsaCksumSum')),
                    ('ospfareasummary', YLeaf(YType.enumeration, 'ospfAreaSummary')),
                    ('ospfareastatus', YLeaf(YType.enumeration, 'ospfAreaStatus')),
                    ('ospfareanssatranslatorrole', YLeaf(YType.enumeration, 'ospfAreaNssaTranslatorRole')),
                    ('ospfareanssatranslatorstate', YLeaf(YType.enumeration, 'ospfAreaNssaTranslatorState')),
                    ('ospfareanssatranslatorstabilityinterval', YLeaf(YType.int32, 'ospfAreaNssaTranslatorStabilityInterval')),
                    ('ospfareanssatranslatorevents', YLeaf(YType.uint32, 'ospfAreaNssaTranslatorEvents')),
                    ('cospfopaquearealsacount', YLeaf(YType.uint32, 'CISCO-OSPF-MIB:cospfOpaqueAreaLsaCount')),
                    ('cospfopaquearealsacksumsum', YLeaf(YType.uint32, 'CISCO-OSPF-MIB:cospfOpaqueAreaLsaCksumSum')),
                    ('cospfareanssatranslatorrole', YLeaf(YType.enumeration, 'CISCO-OSPF-MIB:cospfAreaNssaTranslatorRole')),
                    ('cospfareanssatranslatorstate', YLeaf(YType.enumeration, 'CISCO-OSPF-MIB:cospfAreaNssaTranslatorState')),
                    ('cospfareanssatranslatorevents', YLeaf(YType.uint32, 'CISCO-OSPF-MIB:cospfAreaNssaTranslatorEvents')),
                ])
                self.ospfareaid = None
                self.ospfauthtype = None
                self.ospfimportasextern = None
                self.ospfspfruns = None
                self.ospfareabdrrtrcount = None
                self.ospfasbdrrtrcount = None
                self.ospfarealsacount = None
                self.ospfarealsacksumsum = None
                self.ospfareasummary = None
                self.ospfareastatus = None
                self.ospfareanssatranslatorrole = None
                self.ospfareanssatranslatorstate = None
                self.ospfareanssatranslatorstabilityinterval = None
                self.ospfareanssatranslatorevents = None
                self.cospfopaquearealsacount = None
                self.cospfopaquearealsacksumsum = None
                self.cospfareanssatranslatorrole = None
                self.cospfareanssatranslatorstate = None
                self.cospfareanssatranslatorevents = None
                self._segment_path = lambda: "ospfAreaEntry" + "[ospfAreaId='" + str(self.ospfareaid) + "']"
                self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/ospfAreaTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.Ospfareatable.Ospfareaentry, ['ospfareaid', 'ospfauthtype', 'ospfimportasextern', 'ospfspfruns', 'ospfareabdrrtrcount', 'ospfasbdrrtrcount', 'ospfarealsacount', 'ospfarealsacksumsum', 'ospfareasummary', 'ospfareastatus', 'ospfareanssatranslatorrole', 'ospfareanssatranslatorstate', 'ospfareanssatranslatorstabilityinterval', 'ospfareanssatranslatorevents', 'cospfopaquearealsacount', 'cospfopaquearealsacksumsum', 'cospfareanssatranslatorrole', 'cospfareanssatranslatorstate', 'cospfareanssatranslatorevents'], name, value)

            class Cospfareanssatranslatorrole(Enum):
                """
                Cospfareanssatranslatorrole (Enum Class)

                Indicates an NSSA Border router's ability to

                perform NSSA translation of type\-7 LSAs into

                type\-5 LSAs.

                .. data:: always = 1

                .. data:: candidate = 2

                """

                always = Enum.YLeaf(1, "always")

                candidate = Enum.YLeaf(2, "candidate")


            class Cospfareanssatranslatorstate(Enum):
                """
                Cospfareanssatranslatorstate (Enum Class)

                Indicates if and how an NSSA Border router is

                performing NSSA translation of type\-7 LSAs into type\-5

                LSAs. When this object set to enabled, the NSSA Border

                router's cospfAreaNssaExtTranslatorRole has been set to

                always. When this object is set to elected, a candidate

                NSSA Border router is Translating type\-7 LSAs into type\-5.

                When this object is set to disabled, a candidate NSSA

                Border router is NOT translating type\-7 LSAs into type\-5.

                .. data:: enabled = 1

                .. data:: elected = 2

                .. data:: disabled = 3

                """

                enabled = Enum.YLeaf(1, "enabled")

                elected = Enum.YLeaf(2, "elected")

                disabled = Enum.YLeaf(3, "disabled")


            class Ospfareanssatranslatorrole(Enum):
                """
                Ospfareanssatranslatorrole (Enum Class)

                Indicates an NSSA border router's ability to

                perform NSSA translation of type\-7 LSAs into

                type\-5 LSAs.

                .. data:: always = 1

                .. data:: candidate = 2

                """

                always = Enum.YLeaf(1, "always")

                candidate = Enum.YLeaf(2, "candidate")


            class Ospfareanssatranslatorstate(Enum):
                """
                Ospfareanssatranslatorstate (Enum Class)

                Indicates if and how an NSSA border router is

                performing NSSA translation of type\-7 LSAs into type\-5

                LSAs.  When this object is set to enabled, the NSSA Border

                router's OspfAreaNssaExtTranslatorRole has been set to

                always.  When this object is set to elected, a candidate

                NSSA Border router is Translating type\-7 LSAs into type\-5.

                When this object is set to disabled, a candidate NSSA

                border router is NOT translating type\-7 LSAs into type\-5.

                .. data:: enabled = 1

                .. data:: elected = 2

                .. data:: disabled = 3

                """

                enabled = Enum.YLeaf(1, "enabled")

                elected = Enum.YLeaf(2, "elected")

                disabled = Enum.YLeaf(3, "disabled")


            class Ospfareasummary(Enum):
                """
                Ospfareasummary (Enum Class)

                The variable ospfAreaSummary controls the

                import of summary LSAs into stub and NSSA areas.

                It has no effect on other areas.

                If it is noAreaSummary, the router will not

                originate summary LSAs into the stub or NSSA area.

                It will rely entirely on its default route.

                If it is sendAreaSummary, the router will both

                summarize and propagate summary LSAs.

                .. data:: noAreaSummary = 1

                .. data:: sendAreaSummary = 2

                """

                noAreaSummary = Enum.YLeaf(1, "noAreaSummary")

                sendAreaSummary = Enum.YLeaf(2, "sendAreaSummary")


            class Ospfimportasextern(Enum):
                """
                Ospfimportasextern (Enum Class)

                Indicates if an area is a stub area, NSSA, or standard

                area.  Type\-5 AS\-external LSAs and type\-11 Opaque LSAs are

                not imported into stub areas or NSSAs.  NSSAs import

                AS\-external data as type\-7 LSAs

                .. data:: importExternal = 1

                .. data:: importNoExternal = 2

                .. data:: importNssa = 3

                """

                importExternal = Enum.YLeaf(1, "importExternal")

                importNoExternal = Enum.YLeaf(2, "importNoExternal")

                importNssa = Enum.YLeaf(3, "importNssa")



    class Ospfstubareatable(Entity):
        """
        The set of metrics that will be advertised
        by a default Area Border Router into a stub area.
        
        .. attribute:: ospfstubareaentry
        
        	The metric for a given Type of Service that will be advertised by a default Area Border Router into a stub area.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile storage
        	**type**\: list of  		 :py:class:`Ospfstubareaentry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfstubareatable.Ospfstubareaentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.Ospfstubareatable, self).__init__()

            self.yang_name = "ospfStubAreaTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ospfStubAreaEntry", ("ospfstubareaentry", OSPFMIB.Ospfstubareatable.Ospfstubareaentry))])
            self._leafs = OrderedDict()

            self.ospfstubareaentry = YList(self)
            self._segment_path = lambda: "ospfStubAreaTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.Ospfstubareatable, [], name, value)


        class Ospfstubareaentry(Entity):
            """
            The metric for a given Type of Service that
            will be advertised by a default Area Border
            Router into a stub area.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            storage.
            
            .. attribute:: ospfstubareaid  (key)
            
            	The 32\-bit identifier for the stub area.  On creation, this can be derived from the instance
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfstubtos  (key)
            
            	The Type of Service associated with the metric.  On creation, this can be derived from  the instance
            	**type**\: int
            
            	**range:** 0..30
            
            .. attribute:: ospfstubmetric
            
            	The metric value applied at the indicated Type of Service.  By default, this equals the least metric at the Type of Service among the interfaces to other areas
            	**type**\: int
            
            	**range:** 0..16777215
            
            .. attribute:: ospfstubstatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: ospfstubmetrictype
            
            	This variable displays the type of metric advertised as a default route
            	**type**\:  :py:class:`Ospfstubmetrictype <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfstubareatable.Ospfstubareaentry.Ospfstubmetrictype>`
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OSPFMIB.Ospfstubareatable.Ospfstubareaentry, self).__init__()

                self.yang_name = "ospfStubAreaEntry"
                self.yang_parent_name = "ospfStubAreaTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfstubareaid','ospfstubtos']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfstubareaid', YLeaf(YType.str, 'ospfStubAreaId')),
                    ('ospfstubtos', YLeaf(YType.int32, 'ospfStubTOS')),
                    ('ospfstubmetric', YLeaf(YType.int32, 'ospfStubMetric')),
                    ('ospfstubstatus', YLeaf(YType.enumeration, 'ospfStubStatus')),
                    ('ospfstubmetrictype', YLeaf(YType.enumeration, 'ospfStubMetricType')),
                ])
                self.ospfstubareaid = None
                self.ospfstubtos = None
                self.ospfstubmetric = None
                self.ospfstubstatus = None
                self.ospfstubmetrictype = None
                self._segment_path = lambda: "ospfStubAreaEntry" + "[ospfStubAreaId='" + str(self.ospfstubareaid) + "']" + "[ospfStubTOS='" + str(self.ospfstubtos) + "']"
                self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/ospfStubAreaTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.Ospfstubareatable.Ospfstubareaentry, ['ospfstubareaid', 'ospfstubtos', 'ospfstubmetric', 'ospfstubstatus', 'ospfstubmetrictype'], name, value)

            class Ospfstubmetrictype(Enum):
                """
                Ospfstubmetrictype (Enum Class)

                This variable displays the type of metric

                advertised as a default route.

                .. data:: ospfMetric = 1

                .. data:: comparableCost = 2

                .. data:: nonComparable = 3

                """

                ospfMetric = Enum.YLeaf(1, "ospfMetric")

                comparableCost = Enum.YLeaf(2, "comparableCost")

                nonComparable = Enum.YLeaf(3, "nonComparable")



    class Ospflsdbtable(Entity):
        """
        The OSPF Process's link state database (LSDB).
        The LSDB contains the link state advertisements
        from throughout the areas that the device is attached to.
        
        .. attribute:: ospflsdbentry
        
        	A single link state advertisement
        	**type**\: list of  		 :py:class:`Ospflsdbentry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospflsdbtable.Ospflsdbentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.Ospflsdbtable, self).__init__()

            self.yang_name = "ospfLsdbTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ospfLsdbEntry", ("ospflsdbentry", OSPFMIB.Ospflsdbtable.Ospflsdbentry))])
            self._leafs = OrderedDict()

            self.ospflsdbentry = YList(self)
            self._segment_path = lambda: "ospfLsdbTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.Ospflsdbtable, [], name, value)


        class Ospflsdbentry(Entity):
            """
            A single link state advertisement.
            
            .. attribute:: ospflsdbareaid  (key)
            
            	The 32\-bit identifier of the area from which the LSA was received
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospflsdbtype  (key)
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format.  Note\: External link state advertisements are permitted for backward compatibility, but should be displayed in the ospfAsLsdbTable rather than here
            	**type**\:  :py:class:`Ospflsdbtype <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospflsdbtable.Ospflsdbentry.Ospflsdbtype>`
            
            .. attribute:: ospflsdblsid  (key)
            
            	The Link State ID is an LS Type Specific field containing either a Router ID or an IP address; it identifies the piece of the routing domain that is being described by the advertisement
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospflsdbrouterid  (key)
            
            	The 32\-bit number that uniquely identifies the originating router in the Autonomous System
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospflsdbsequence
            
            	The sequence number field is a signed 32\-bit integer.  It starts with the value '80000001'h, or \-'7FFFFFFF'h, and increments until '7FFFFFFF'h. Thus, a typical sequence number will be very negative. It is used to detect old and duplicate Link State Advertisements.  The space of sequence numbers is linearly ordered.  The larger the sequence number, the more recent the advertisement
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospflsdbage
            
            	This field is the age of the link state advertisement in seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: seconds
            
            .. attribute:: ospflsdbchecksum
            
            	This field is the checksum of the complete contents of the advertisement, excepting the age field.  The age field is excepted so that an advertisement's age can be incremented without updating the checksum.  The checksum used is the same that is used for ISO connectionless  datagrams; it is commonly referred to as the Fletcher checksum
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospflsdbadvertisement
            
            	The entire link state advertisement, including its header.  Note that for variable length LSAs, SNMP agents may not be able to return the largest string size
            	**type**\: str
            
            	**length:** 1..65535
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OSPFMIB.Ospflsdbtable.Ospflsdbentry, self).__init__()

                self.yang_name = "ospfLsdbEntry"
                self.yang_parent_name = "ospfLsdbTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospflsdbareaid','ospflsdbtype','ospflsdblsid','ospflsdbrouterid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospflsdbareaid', YLeaf(YType.str, 'ospfLsdbAreaId')),
                    ('ospflsdbtype', YLeaf(YType.enumeration, 'ospfLsdbType')),
                    ('ospflsdblsid', YLeaf(YType.str, 'ospfLsdbLsid')),
                    ('ospflsdbrouterid', YLeaf(YType.str, 'ospfLsdbRouterId')),
                    ('ospflsdbsequence', YLeaf(YType.int32, 'ospfLsdbSequence')),
                    ('ospflsdbage', YLeaf(YType.int32, 'ospfLsdbAge')),
                    ('ospflsdbchecksum', YLeaf(YType.int32, 'ospfLsdbChecksum')),
                    ('ospflsdbadvertisement', YLeaf(YType.str, 'ospfLsdbAdvertisement')),
                ])
                self.ospflsdbareaid = None
                self.ospflsdbtype = None
                self.ospflsdblsid = None
                self.ospflsdbrouterid = None
                self.ospflsdbsequence = None
                self.ospflsdbage = None
                self.ospflsdbchecksum = None
                self.ospflsdbadvertisement = None
                self._segment_path = lambda: "ospfLsdbEntry" + "[ospfLsdbAreaId='" + str(self.ospflsdbareaid) + "']" + "[ospfLsdbType='" + str(self.ospflsdbtype) + "']" + "[ospfLsdbLsid='" + str(self.ospflsdblsid) + "']" + "[ospfLsdbRouterId='" + str(self.ospflsdbrouterid) + "']"
                self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/ospfLsdbTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.Ospflsdbtable.Ospflsdbentry, ['ospflsdbareaid', 'ospflsdbtype', 'ospflsdblsid', 'ospflsdbrouterid', 'ospflsdbsequence', 'ospflsdbage', 'ospflsdbchecksum', 'ospflsdbadvertisement'], name, value)

            class Ospflsdbtype(Enum):
                """
                Ospflsdbtype (Enum Class)

                The type of the link state advertisement.

                Each link state type has a separate advertisement

                format.

                Note\: External link state advertisements are permitted

                for backward compatibility, but should be displayed

                in the ospfAsLsdbTable rather than here.

                .. data:: routerLink = 1

                .. data:: networkLink = 2

                .. data:: summaryLink = 3

                .. data:: asSummaryLink = 4

                .. data:: asExternalLink = 5

                .. data:: multicastLink = 6

                .. data:: nssaExternalLink = 7

                .. data:: areaOpaqueLink = 10

                """

                routerLink = Enum.YLeaf(1, "routerLink")

                networkLink = Enum.YLeaf(2, "networkLink")

                summaryLink = Enum.YLeaf(3, "summaryLink")

                asSummaryLink = Enum.YLeaf(4, "asSummaryLink")

                asExternalLink = Enum.YLeaf(5, "asExternalLink")

                multicastLink = Enum.YLeaf(6, "multicastLink")

                nssaExternalLink = Enum.YLeaf(7, "nssaExternalLink")

                areaOpaqueLink = Enum.YLeaf(10, "areaOpaqueLink")



    class Ospfarearangetable(Entity):
        """
        The Address Range Table acts as an adjunct to the Area
        Table.  It describes those Address Range Summaries that
        are configured to be propagated from an Area to reduce
        the amount of information about it that is known beyond
        its borders.  It contains a set of IP address ranges
        specified by an IP address/IP network mask pair.
        For example, class B address range of X.X.X.X
        with a network mask of 255.255.0.0 includes all IP
        addresses from X.X.0.0 to X.X.255.255.
        
        Note that this table is obsoleted and is replaced
        by the Area Aggregate Table.
        
        .. attribute:: ospfarearangeentry
        
        	A single area address range.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile storage
        	**type**\: list of  		 :py:class:`Ospfarearangeentry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfarearangetable.Ospfarearangeentry>`
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.Ospfarearangetable, self).__init__()

            self.yang_name = "ospfAreaRangeTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ospfAreaRangeEntry", ("ospfarearangeentry", OSPFMIB.Ospfarearangetable.Ospfarearangeentry))])
            self._leafs = OrderedDict()

            self.ospfarearangeentry = YList(self)
            self._segment_path = lambda: "ospfAreaRangeTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.Ospfarearangetable, [], name, value)


        class Ospfarearangeentry(Entity):
            """
            A single area address range.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            storage.
            
            .. attribute:: ospfarearangeareaid  (key)
            
            	The area that the address range is to be found within
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: obsolete
            
            .. attribute:: ospfarearangenet  (key)
            
            	The IP address of the net or subnet indicated by the range
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: obsolete
            
            .. attribute:: ospfarearangemask
            
            	The subnet mask that pertains to the net or subnet
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: obsolete
            
            .. attribute:: ospfarearangestatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**status**\: obsolete
            
            .. attribute:: ospfarearangeeffect
            
            	Subnets subsumed by ranges either trigger the advertisement of the indicated summary (advertiseMatching) or result in the subnet's not being advertised at all outside the area
            	**type**\:  :py:class:`Ospfarearangeeffect <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfarearangetable.Ospfarearangeentry.Ospfarearangeeffect>`
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OSPFMIB.Ospfarearangetable.Ospfarearangeentry, self).__init__()

                self.yang_name = "ospfAreaRangeEntry"
                self.yang_parent_name = "ospfAreaRangeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfarearangeareaid','ospfarearangenet']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfarearangeareaid', YLeaf(YType.str, 'ospfAreaRangeAreaId')),
                    ('ospfarearangenet', YLeaf(YType.str, 'ospfAreaRangeNet')),
                    ('ospfarearangemask', YLeaf(YType.str, 'ospfAreaRangeMask')),
                    ('ospfarearangestatus', YLeaf(YType.enumeration, 'ospfAreaRangeStatus')),
                    ('ospfarearangeeffect', YLeaf(YType.enumeration, 'ospfAreaRangeEffect')),
                ])
                self.ospfarearangeareaid = None
                self.ospfarearangenet = None
                self.ospfarearangemask = None
                self.ospfarearangestatus = None
                self.ospfarearangeeffect = None
                self._segment_path = lambda: "ospfAreaRangeEntry" + "[ospfAreaRangeAreaId='" + str(self.ospfarearangeareaid) + "']" + "[ospfAreaRangeNet='" + str(self.ospfarearangenet) + "']"
                self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/ospfAreaRangeTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.Ospfarearangetable.Ospfarearangeentry, ['ospfarearangeareaid', 'ospfarearangenet', 'ospfarearangemask', 'ospfarearangestatus', 'ospfarearangeeffect'], name, value)

            class Ospfarearangeeffect(Enum):
                """
                Ospfarearangeeffect (Enum Class)

                Subnets subsumed by ranges either trigger the

                advertisement of the indicated summary

                (advertiseMatching) or result in the subnet's not

                being advertised at all outside the area.

                .. data:: advertiseMatching = 1

                .. data:: doNotAdvertiseMatching = 2

                """

                advertiseMatching = Enum.YLeaf(1, "advertiseMatching")

                doNotAdvertiseMatching = Enum.YLeaf(2, "doNotAdvertiseMatching")



    class Ospfhosttable(Entity):
        """
        The Host/Metric Table indicates what hosts are directly
        
        attached to the router, what metrics and types
        of service should be advertised for them,
        and what areas they are found within.
        
        .. attribute:: ospfhostentry
        
        	A metric to be advertised, for a given type of service, when a given host is reachable.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile storage
        	**type**\: list of  		 :py:class:`Ospfhostentry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfhosttable.Ospfhostentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.Ospfhosttable, self).__init__()

            self.yang_name = "ospfHostTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ospfHostEntry", ("ospfhostentry", OSPFMIB.Ospfhosttable.Ospfhostentry))])
            self._leafs = OrderedDict()

            self.ospfhostentry = YList(self)
            self._segment_path = lambda: "ospfHostTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.Ospfhosttable, [], name, value)


        class Ospfhostentry(Entity):
            """
            A metric to be advertised, for a given type of
            service, when a given host is reachable.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            storage.
            
            .. attribute:: ospfhostipaddress  (key)
            
            	The IP address of the host
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfhosttos  (key)
            
            	The Type of Service of the route being configured
            	**type**\: int
            
            	**range:** 0..30
            
            .. attribute:: ospfhostmetric
            
            	The metric to be advertised
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: ospfhoststatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: ospfhostareaid
            
            	The OSPF area to which the host belongs. Deprecated by ospfHostCfgAreaID
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: ospfhostcfgareaid
            
            	To configure the OSPF area to which the host belongs
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OSPFMIB.Ospfhosttable.Ospfhostentry, self).__init__()

                self.yang_name = "ospfHostEntry"
                self.yang_parent_name = "ospfHostTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfhostipaddress','ospfhosttos']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfhostipaddress', YLeaf(YType.str, 'ospfHostIpAddress')),
                    ('ospfhosttos', YLeaf(YType.int32, 'ospfHostTOS')),
                    ('ospfhostmetric', YLeaf(YType.int32, 'ospfHostMetric')),
                    ('ospfhoststatus', YLeaf(YType.enumeration, 'ospfHostStatus')),
                    ('ospfhostareaid', YLeaf(YType.str, 'ospfHostAreaID')),
                    ('ospfhostcfgareaid', YLeaf(YType.str, 'ospfHostCfgAreaID')),
                ])
                self.ospfhostipaddress = None
                self.ospfhosttos = None
                self.ospfhostmetric = None
                self.ospfhoststatus = None
                self.ospfhostareaid = None
                self.ospfhostcfgareaid = None
                self._segment_path = lambda: "ospfHostEntry" + "[ospfHostIpAddress='" + str(self.ospfhostipaddress) + "']" + "[ospfHostTOS='" + str(self.ospfhosttos) + "']"
                self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/ospfHostTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.Ospfhosttable.Ospfhostentry, ['ospfhostipaddress', 'ospfhosttos', 'ospfhostmetric', 'ospfhoststatus', 'ospfhostareaid', 'ospfhostcfgareaid'], name, value)


    class Ospfiftable(Entity):
        """
        The OSPF Interface Table describes the interfaces
        from the viewpoint of OSPF.
        It augments the ipAddrTable with OSPF specific information.
        
        .. attribute:: ospfifentry
        
        	The OSPF interface entry describes one interface from the viewpoint of OSPF.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile storage
        	**type**\: list of  		 :py:class:`Ospfifentry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfiftable.Ospfifentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.Ospfiftable, self).__init__()

            self.yang_name = "ospfIfTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ospfIfEntry", ("ospfifentry", OSPFMIB.Ospfiftable.Ospfifentry))])
            self._leafs = OrderedDict()

            self.ospfifentry = YList(self)
            self._segment_path = lambda: "ospfIfTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.Ospfiftable, [], name, value)


        class Ospfifentry(Entity):
            """
            The OSPF interface entry describes one interface
            from the viewpoint of OSPF.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            storage.
            
            .. attribute:: ospfifipaddress  (key)
            
            	The IP address of this OSPF interface
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfaddresslessif  (key)
            
            	For the purpose of easing the instancing of addressed and addressless interfaces; this variable takes the value 0 on interfaces with IP addresses and the corresponding value of ifIndex for interfaces having no IP address
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ospfifareaid
            
            	A 32\-bit integer uniquely identifying the area to which the interface connects.  Area ID 0.0.0.0 is used for the OSPF backbone
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfiftype
            
            	The OSPF interface type. By way of a default, this field may be intuited from the corresponding value of ifType. Broadcast LANs, such as Ethernet and IEEE 802.5, take the value 'broadcast', X.25 and similar technologies take the value 'nbma', and links that are definitively point to point take the value 'pointToPoint'
            	**type**\:  :py:class:`Ospfiftype <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfiftable.Ospfifentry.Ospfiftype>`
            
            .. attribute:: ospfifadminstat
            
            	The OSPF interface's administrative status. The value formed on the interface, and the interface will be advertised as an internal route to some area. The value 'disabled' denotes that the interface is external to OSPF
            	**type**\:  :py:class:`Status <ydk.models.cisco_ios_xe.OSPF_MIB.Status>`
            
            .. attribute:: ospfifrtrpriority
            
            	The priority of this interface.  Used in multi\-access networks, this field is used in the designated router election algorithm.  The value 0 signifies that the router is not eligible to become the designated router on this particular network.  In the event of a tie in this value, routers will use their Router ID as a tie breaker
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: ospfiftransitdelay
            
            	The estimated number of seconds it takes to transmit a link state update packet over this interface.  Note that the minimal value SHOULD be 1 second
            	**type**\: int
            
            	**range:** 0..3600
            
            	**units**\: seconds
            
            .. attribute:: ospfifretransinterval
            
            	The number of seconds between link state advertisement retransmissions, for adjacencies belonging to this interface.  This value is also used when retransmitting  database description and Link State request packets. Note that minimal value SHOULD be 1 second
            	**type**\: int
            
            	**range:** 0..3600
            
            	**units**\: seconds
            
            .. attribute:: ospfifhellointerval
            
            	The length of time, in seconds, between the Hello packets that the router sends on the interface.  This value must be the same for all routers attached to a common network
            	**type**\: int
            
            	**range:** 1..65535
            
            	**units**\: seconds
            
            .. attribute:: ospfifrtrdeadinterval
            
            	The number of seconds that a router's Hello packets have not been seen before its neighbors declare the router down. This should be some multiple of the Hello interval.  This value must be the same for all routers attached to a common network
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: ospfifpollinterval
            
            	The larger time interval, in seconds, between the Hello packets sent to an inactive non\-broadcast multi\-access neighbor
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: ospfifstate
            
            	The OSPF Interface State
            	**type**\:  :py:class:`Ospfifstate <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfiftable.Ospfifentry.Ospfifstate>`
            
            .. attribute:: ospfifdesignatedrouter
            
            	The IP address of the designated router
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfifbackupdesignatedrouter
            
            	The IP address of the backup designated router
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfifevents
            
            	The number of times this OSPF interface has changed its state or an error has occurred.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ospfDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfifauthkey
            
            	The cleartext password used as an OSPF authentication key when simplePassword security is enabled.  This object does not access any OSPF cryptogaphic (e.g., MD5) authentication key under any circumstance.  If the key length is shorter than 8 octets, the agent will left adjust and zero fill to 8 octets.  Unauthenticated interfaces need no authentication key, and simple password authentication cannot use a key of more than 8 octets.  Note that the use of simplePassword authentication is NOT recommended when there is concern regarding attack upon the OSPF system.  SimplePassword authentication is only sufficient to protect against accidental misconfigurations because it re\-uses cleartext passwords [RFC1704].  When read, ospfIfAuthKey always returns an octet string of length zero
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: ospfifstatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: ospfifmulticastforwarding
            
            	The way multicasts should be forwarded on this interface\: not forwarded, forwarded as data link multicasts, or forwarded as data link unicasts.  Data link multicasting is not meaningful on point\-to\-point and NBMA interfaces, and setting ospfMulticastForwarding to 0 effectively disables all multicast forwarding
            	**type**\:  :py:class:`Ospfifmulticastforwarding <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfiftable.Ospfifentry.Ospfifmulticastforwarding>`
            
            .. attribute:: ospfifdemand
            
            	Indicates whether Demand OSPF procedures (hello suppression to FULL neighbors and setting the DoNotAge flag on propagated LSAs) should be performed on this interface
            	**type**\: bool
            
            .. attribute:: ospfifauthtype
            
            	The authentication type specified for an interface.  Note that this object can be used to engage in significant attacks against an OSPF router
            	**type**\:  :py:class:`OspfAuthenticationType <ydk.models.cisco_ios_xe.OSPF_MIB.OspfAuthenticationType>`
            
            .. attribute:: ospfiflsacount
            
            	The total number of link\-local link state advertisements in this interface's link\-local link state database
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfiflsacksumsum
            
            	The 32\-bit unsigned sum of the Link State Advertisements' LS checksums contained in this interface's link\-local link state database. The sum can be used to determine if there has been a change in the interface's link state database and to compare the interface link state database of routers attached to the same subnet
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfifdesignatedrouterid
            
            	The Router ID of the designated router
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfifbackupdesignatedrouterid
            
            	The Router ID of the backup designated router
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfiflsacount
            
            	The total number of link\-local link state advertisements in this interface's link\-local link state database
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfiflsacksumsum
            
            	The 32\-bit unsigned sum of the link\-state advertisements' LS checksums contained in this interface's link\-local link  state database. The sum can be used to determine if there has been a change in the interface's link state database, and to compare the interface link\-state database of routers  attached to the same subnet
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OSPFMIB.Ospfiftable.Ospfifentry, self).__init__()

                self.yang_name = "ospfIfEntry"
                self.yang_parent_name = "ospfIfTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfifipaddress','ospfaddresslessif']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfifipaddress', YLeaf(YType.str, 'ospfIfIpAddress')),
                    ('ospfaddresslessif', YLeaf(YType.int32, 'ospfAddressLessIf')),
                    ('ospfifareaid', YLeaf(YType.str, 'ospfIfAreaId')),
                    ('ospfiftype', YLeaf(YType.enumeration, 'ospfIfType')),
                    ('ospfifadminstat', YLeaf(YType.enumeration, 'ospfIfAdminStat')),
                    ('ospfifrtrpriority', YLeaf(YType.int32, 'ospfIfRtrPriority')),
                    ('ospfiftransitdelay', YLeaf(YType.int32, 'ospfIfTransitDelay')),
                    ('ospfifretransinterval', YLeaf(YType.int32, 'ospfIfRetransInterval')),
                    ('ospfifhellointerval', YLeaf(YType.int32, 'ospfIfHelloInterval')),
                    ('ospfifrtrdeadinterval', YLeaf(YType.int32, 'ospfIfRtrDeadInterval')),
                    ('ospfifpollinterval', YLeaf(YType.int32, 'ospfIfPollInterval')),
                    ('ospfifstate', YLeaf(YType.enumeration, 'ospfIfState')),
                    ('ospfifdesignatedrouter', YLeaf(YType.str, 'ospfIfDesignatedRouter')),
                    ('ospfifbackupdesignatedrouter', YLeaf(YType.str, 'ospfIfBackupDesignatedRouter')),
                    ('ospfifevents', YLeaf(YType.uint32, 'ospfIfEvents')),
                    ('ospfifauthkey', YLeaf(YType.str, 'ospfIfAuthKey')),
                    ('ospfifstatus', YLeaf(YType.enumeration, 'ospfIfStatus')),
                    ('ospfifmulticastforwarding', YLeaf(YType.enumeration, 'ospfIfMulticastForwarding')),
                    ('ospfifdemand', YLeaf(YType.boolean, 'ospfIfDemand')),
                    ('ospfifauthtype', YLeaf(YType.enumeration, 'ospfIfAuthType')),
                    ('ospfiflsacount', YLeaf(YType.uint32, 'ospfIfLsaCount')),
                    ('ospfiflsacksumsum', YLeaf(YType.uint32, 'ospfIfLsaCksumSum')),
                    ('ospfifdesignatedrouterid', YLeaf(YType.str, 'ospfIfDesignatedRouterId')),
                    ('ospfifbackupdesignatedrouterid', YLeaf(YType.str, 'ospfIfBackupDesignatedRouterId')),
                    ('cospfiflsacount', YLeaf(YType.uint32, 'CISCO-OSPF-MIB:cospfIfLsaCount')),
                    ('cospfiflsacksumsum', YLeaf(YType.uint32, 'CISCO-OSPF-MIB:cospfIfLsaCksumSum')),
                ])
                self.ospfifipaddress = None
                self.ospfaddresslessif = None
                self.ospfifareaid = None
                self.ospfiftype = None
                self.ospfifadminstat = None
                self.ospfifrtrpriority = None
                self.ospfiftransitdelay = None
                self.ospfifretransinterval = None
                self.ospfifhellointerval = None
                self.ospfifrtrdeadinterval = None
                self.ospfifpollinterval = None
                self.ospfifstate = None
                self.ospfifdesignatedrouter = None
                self.ospfifbackupdesignatedrouter = None
                self.ospfifevents = None
                self.ospfifauthkey = None
                self.ospfifstatus = None
                self.ospfifmulticastforwarding = None
                self.ospfifdemand = None
                self.ospfifauthtype = None
                self.ospfiflsacount = None
                self.ospfiflsacksumsum = None
                self.ospfifdesignatedrouterid = None
                self.ospfifbackupdesignatedrouterid = None
                self.cospfiflsacount = None
                self.cospfiflsacksumsum = None
                self._segment_path = lambda: "ospfIfEntry" + "[ospfIfIpAddress='" + str(self.ospfifipaddress) + "']" + "[ospfAddressLessIf='" + str(self.ospfaddresslessif) + "']"
                self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/ospfIfTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.Ospfiftable.Ospfifentry, ['ospfifipaddress', 'ospfaddresslessif', 'ospfifareaid', 'ospfiftype', 'ospfifadminstat', 'ospfifrtrpriority', 'ospfiftransitdelay', 'ospfifretransinterval', 'ospfifhellointerval', 'ospfifrtrdeadinterval', 'ospfifpollinterval', 'ospfifstate', 'ospfifdesignatedrouter', 'ospfifbackupdesignatedrouter', 'ospfifevents', 'ospfifauthkey', 'ospfifstatus', 'ospfifmulticastforwarding', 'ospfifdemand', 'ospfifauthtype', 'ospfiflsacount', 'ospfiflsacksumsum', 'ospfifdesignatedrouterid', 'ospfifbackupdesignatedrouterid', 'cospfiflsacount', 'cospfiflsacksumsum'], name, value)

            class Ospfifmulticastforwarding(Enum):
                """
                Ospfifmulticastforwarding (Enum Class)

                The way multicasts should be forwarded on this

                interface\: not forwarded, forwarded as data

                link multicasts, or forwarded as data link

                unicasts.  Data link multicasting is not

                meaningful on point\-to\-point and NBMA interfaces,

                and setting ospfMulticastForwarding to 0 effectively

                disables all multicast forwarding.

                .. data:: blocked = 1

                .. data:: multicast = 2

                .. data:: unicast = 3

                """

                blocked = Enum.YLeaf(1, "blocked")

                multicast = Enum.YLeaf(2, "multicast")

                unicast = Enum.YLeaf(3, "unicast")


            class Ospfifstate(Enum):
                """
                Ospfifstate (Enum Class)

                The OSPF Interface State.

                .. data:: down = 1

                .. data:: loopback = 2

                .. data:: waiting = 3

                .. data:: pointToPoint = 4

                .. data:: designatedRouter = 5

                .. data:: backupDesignatedRouter = 6

                .. data:: otherDesignatedRouter = 7

                """

                down = Enum.YLeaf(1, "down")

                loopback = Enum.YLeaf(2, "loopback")

                waiting = Enum.YLeaf(3, "waiting")

                pointToPoint = Enum.YLeaf(4, "pointToPoint")

                designatedRouter = Enum.YLeaf(5, "designatedRouter")

                backupDesignatedRouter = Enum.YLeaf(6, "backupDesignatedRouter")

                otherDesignatedRouter = Enum.YLeaf(7, "otherDesignatedRouter")


            class Ospfiftype(Enum):
                """
                Ospfiftype (Enum Class)

                The OSPF interface type.

                By way of a default, this field may be intuited

                from the corresponding value of ifType.

                Broadcast LANs, such as Ethernet and IEEE 802.5,

                take the value 'broadcast', X.25 and similar

                technologies take the value 'nbma', and links

                that are definitively point to point take the

                value 'pointToPoint'.

                .. data:: broadcast = 1

                .. data:: nbma = 2

                .. data:: pointToPoint = 3

                .. data:: pointToMultipoint = 5

                """

                broadcast = Enum.YLeaf(1, "broadcast")

                nbma = Enum.YLeaf(2, "nbma")

                pointToPoint = Enum.YLeaf(3, "pointToPoint")

                pointToMultipoint = Enum.YLeaf(5, "pointToMultipoint")



    class Ospfifmetrictable(Entity):
        """
        The Metric Table describes the metrics to be advertised
        for a specified interface at the various types of service.
        As such, this table is an adjunct of the OSPF Interface
        Table.
        
        Types of service, as defined by RFC 791, have the ability
        to request low delay, high bandwidth, or reliable linkage.
        
        For the purposes of this specification, the measure of
        bandwidth\:
        
        Metric = referenceBandwidth / ifSpeed
        
        is the default value.
        The default reference bandwidth is 10^8.
        For multiple link interfaces, note that ifSpeed is the sum
        of the individual link speeds.  This yields a number having
        the following typical values\:
        
        Network Type/bit rate   Metric
        
        >= 100 MBPS                 1
        Ethernet/802.3             10
        E1                         48
        T1 (ESF)                   65
        64 KBPS                    1562
        56 KBPS                    1785
        19.2 KBPS                  5208
        9.6 KBPS                   10416
        
        Routes that are not specified use the default
        (TOS 0) metric.
        
        Note that the default reference bandwidth can be configured
        using the general group object ospfReferenceBandwidth.
        
        .. attribute:: ospfifmetricentry
        
        	A particular TOS metric for a non\-virtual interface identified by the interface index.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile storage
        	**type**\: list of  		 :py:class:`Ospfifmetricentry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfifmetrictable.Ospfifmetricentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.Ospfifmetrictable, self).__init__()

            self.yang_name = "ospfIfMetricTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ospfIfMetricEntry", ("ospfifmetricentry", OSPFMIB.Ospfifmetrictable.Ospfifmetricentry))])
            self._leafs = OrderedDict()

            self.ospfifmetricentry = YList(self)
            self._segment_path = lambda: "ospfIfMetricTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.Ospfifmetrictable, [], name, value)


        class Ospfifmetricentry(Entity):
            """
            A particular TOS metric for a non\-virtual interface
            identified by the interface index.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            storage.
            
            .. attribute:: ospfifmetricipaddress  (key)
            
            	The IP address of this OSPF interface.  On row creation, this can be derived from the instance
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfifmetricaddresslessif  (key)
            
            	For the purpose of easing the instancing of addressed and addressless interfaces; this variable takes the value 0 on interfaces with IP addresses and the value of ifIndex for interfaces having no IP address.  On row creation, this can be derived from the instance
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ospfifmetrictos  (key)
            
            	The Type of Service metric being referenced. On row creation, this can be derived from the instance
            	**type**\: int
            
            	**range:** 0..30
            
            .. attribute:: ospfifmetricvalue
            
            	The metric of using this Type of Service on this interface.  The default value of the TOS 0 metric is 10^8 / ifSpeed
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: ospfifmetricstatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OSPFMIB.Ospfifmetrictable.Ospfifmetricentry, self).__init__()

                self.yang_name = "ospfIfMetricEntry"
                self.yang_parent_name = "ospfIfMetricTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfifmetricipaddress','ospfifmetricaddresslessif','ospfifmetrictos']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfifmetricipaddress', YLeaf(YType.str, 'ospfIfMetricIpAddress')),
                    ('ospfifmetricaddresslessif', YLeaf(YType.int32, 'ospfIfMetricAddressLessIf')),
                    ('ospfifmetrictos', YLeaf(YType.int32, 'ospfIfMetricTOS')),
                    ('ospfifmetricvalue', YLeaf(YType.int32, 'ospfIfMetricValue')),
                    ('ospfifmetricstatus', YLeaf(YType.enumeration, 'ospfIfMetricStatus')),
                ])
                self.ospfifmetricipaddress = None
                self.ospfifmetricaddresslessif = None
                self.ospfifmetrictos = None
                self.ospfifmetricvalue = None
                self.ospfifmetricstatus = None
                self._segment_path = lambda: "ospfIfMetricEntry" + "[ospfIfMetricIpAddress='" + str(self.ospfifmetricipaddress) + "']" + "[ospfIfMetricAddressLessIf='" + str(self.ospfifmetricaddresslessif) + "']" + "[ospfIfMetricTOS='" + str(self.ospfifmetrictos) + "']"
                self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/ospfIfMetricTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.Ospfifmetrictable.Ospfifmetricentry, ['ospfifmetricipaddress', 'ospfifmetricaddresslessif', 'ospfifmetrictos', 'ospfifmetricvalue', 'ospfifmetricstatus'], name, value)


    class Ospfvirtiftable(Entity):
        """
        Information about this router's virtual interfaces
        that the OSPF Process is configured to carry on.
        
        .. attribute:: ospfvirtifentry
        
        	Information about a single virtual interface.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile storage
        	**type**\: list of  		 :py:class:`Ospfvirtifentry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfvirtiftable.Ospfvirtifentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.Ospfvirtiftable, self).__init__()

            self.yang_name = "ospfVirtIfTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ospfVirtIfEntry", ("ospfvirtifentry", OSPFMIB.Ospfvirtiftable.Ospfvirtifentry))])
            self._leafs = OrderedDict()

            self.ospfvirtifentry = YList(self)
            self._segment_path = lambda: "ospfVirtIfTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.Ospfvirtiftable, [], name, value)


        class Ospfvirtifentry(Entity):
            """
            Information about a single virtual interface.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            storage.
            
            .. attribute:: ospfvirtifareaid  (key)
            
            	The transit area that the virtual link traverses.  By definition, this is not 0.0.0.0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfvirtifneighbor  (key)
            
            	The Router ID of the virtual neighbor
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfvirtiftransitdelay
            
            	The estimated number of seconds it takes to transmit a Link State update packet over this interface.  Note that the minimal value SHOULD be 1 second
            	**type**\: int
            
            	**range:** 0..3600
            
            	**units**\: seconds
            
            .. attribute:: ospfvirtifretransinterval
            
            	The number of seconds between link state avertisement retransmissions, for adjacencies belonging to this interface.  This value is also used when retransmitting database description and Link State request packets.  This value should be well over the expected round\-trip time.  Note that the minimal value SHOULD be 1 second
            	**type**\: int
            
            	**range:** 0..3600
            
            	**units**\: seconds
            
            .. attribute:: ospfvirtifhellointerval
            
            	The length of time, in seconds, between the Hello packets that the router sends on the interface.  This value must be the same for the virtual neighbor
            	**type**\: int
            
            	**range:** 1..65535
            
            	**units**\: seconds
            
            .. attribute:: ospfvirtifrtrdeadinterval
            
            	The number of seconds that a router's Hello packets have not been seen before its neighbors declare the router down.  This should be some multiple of the Hello interval.  This value must be the same for the virtual neighbor
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: ospfvirtifstate
            
            	OSPF virtual interface states
            	**type**\:  :py:class:`Ospfvirtifstate <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfvirtiftable.Ospfvirtifentry.Ospfvirtifstate>`
            
            .. attribute:: ospfvirtifevents
            
            	The number of state changes or error events on this virtual link.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ospfDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfvirtifauthkey
            
            	The cleartext password used as an OSPF authentication key when simplePassword security is enabled.  This object does not access any OSPF cryptogaphic (e.g., MD5) authentication key under any circumstance.  If the key length is shorter than 8 octets, the agent will left adjust and zero fill to 8 octets.  Unauthenticated interfaces need no authentication key, and simple password authentication cannot use a key of more than 8 octets.  Note that the use of simplePassword authentication is NOT recommended when there is concern regarding attack upon the OSPF system.  SimplePassword authentication is only sufficient to protect against accidental misconfigurations because it re\-uses cleartext passwords.  [RFC1704]  When read, ospfIfAuthKey always returns an octet string of length zero
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: ospfvirtifstatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: ospfvirtifauthtype
            
            	The authentication type specified for a virtual interface.  Note that this object can be used to engage in significant attacks against an OSPF router
            	**type**\:  :py:class:`OspfAuthenticationType <ydk.models.cisco_ios_xe.OSPF_MIB.OspfAuthenticationType>`
            
            .. attribute:: ospfvirtiflsacount
            
            	The total number of link\-local link state advertisements in this virtual interface's link\-local link state database
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfvirtiflsacksumsum
            
            	The 32\-bit unsigned sum of the link state advertisements' LS checksums contained in this virtual interface's link\-local link state database. The sum can be used to determine if there has been a change in the virtual interface's link state database, and to compare the virtual interface link state database of the virtual neighbors
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfvirtiflsacount
            
            	The total number of link\-local link state advertisements in this virtual interface's link\-local link state database
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfvirtiflsacksumsum
            
            	The 32\-bit unsigned sum of the link\-state advertisements' LS checksums contained in this virtual interface's link\-local link state database. The sum can be used to determine if there has been a change in the virtual interface's link state database, and to compare the virtual interface link\-state database of the virtual neighbors
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OSPFMIB.Ospfvirtiftable.Ospfvirtifentry, self).__init__()

                self.yang_name = "ospfVirtIfEntry"
                self.yang_parent_name = "ospfVirtIfTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfvirtifareaid','ospfvirtifneighbor']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfvirtifareaid', YLeaf(YType.str, 'ospfVirtIfAreaId')),
                    ('ospfvirtifneighbor', YLeaf(YType.str, 'ospfVirtIfNeighbor')),
                    ('ospfvirtiftransitdelay', YLeaf(YType.int32, 'ospfVirtIfTransitDelay')),
                    ('ospfvirtifretransinterval', YLeaf(YType.int32, 'ospfVirtIfRetransInterval')),
                    ('ospfvirtifhellointerval', YLeaf(YType.int32, 'ospfVirtIfHelloInterval')),
                    ('ospfvirtifrtrdeadinterval', YLeaf(YType.int32, 'ospfVirtIfRtrDeadInterval')),
                    ('ospfvirtifstate', YLeaf(YType.enumeration, 'ospfVirtIfState')),
                    ('ospfvirtifevents', YLeaf(YType.uint32, 'ospfVirtIfEvents')),
                    ('ospfvirtifauthkey', YLeaf(YType.str, 'ospfVirtIfAuthKey')),
                    ('ospfvirtifstatus', YLeaf(YType.enumeration, 'ospfVirtIfStatus')),
                    ('ospfvirtifauthtype', YLeaf(YType.enumeration, 'ospfVirtIfAuthType')),
                    ('ospfvirtiflsacount', YLeaf(YType.uint32, 'ospfVirtIfLsaCount')),
                    ('ospfvirtiflsacksumsum', YLeaf(YType.uint32, 'ospfVirtIfLsaCksumSum')),
                    ('cospfvirtiflsacount', YLeaf(YType.uint32, 'CISCO-OSPF-MIB:cospfVirtIfLsaCount')),
                    ('cospfvirtiflsacksumsum', YLeaf(YType.uint32, 'CISCO-OSPF-MIB:cospfVirtIfLsaCksumSum')),
                ])
                self.ospfvirtifareaid = None
                self.ospfvirtifneighbor = None
                self.ospfvirtiftransitdelay = None
                self.ospfvirtifretransinterval = None
                self.ospfvirtifhellointerval = None
                self.ospfvirtifrtrdeadinterval = None
                self.ospfvirtifstate = None
                self.ospfvirtifevents = None
                self.ospfvirtifauthkey = None
                self.ospfvirtifstatus = None
                self.ospfvirtifauthtype = None
                self.ospfvirtiflsacount = None
                self.ospfvirtiflsacksumsum = None
                self.cospfvirtiflsacount = None
                self.cospfvirtiflsacksumsum = None
                self._segment_path = lambda: "ospfVirtIfEntry" + "[ospfVirtIfAreaId='" + str(self.ospfvirtifareaid) + "']" + "[ospfVirtIfNeighbor='" + str(self.ospfvirtifneighbor) + "']"
                self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/ospfVirtIfTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.Ospfvirtiftable.Ospfvirtifentry, ['ospfvirtifareaid', 'ospfvirtifneighbor', 'ospfvirtiftransitdelay', 'ospfvirtifretransinterval', 'ospfvirtifhellointerval', 'ospfvirtifrtrdeadinterval', 'ospfvirtifstate', 'ospfvirtifevents', 'ospfvirtifauthkey', 'ospfvirtifstatus', 'ospfvirtifauthtype', 'ospfvirtiflsacount', 'ospfvirtiflsacksumsum', 'cospfvirtiflsacount', 'cospfvirtiflsacksumsum'], name, value)

            class Ospfvirtifstate(Enum):
                """
                Ospfvirtifstate (Enum Class)

                OSPF virtual interface states.

                .. data:: down = 1

                .. data:: pointToPoint = 4

                """

                down = Enum.YLeaf(1, "down")

                pointToPoint = Enum.YLeaf(4, "pointToPoint")



    class Ospfnbrtable(Entity):
        """
        A table describing all non\-virtual neighbors
        in the locality of the OSPF router.
        
        .. attribute:: ospfnbrentry
        
        	The information regarding a single neighbor.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile  storage
        	**type**\: list of  		 :py:class:`Ospfnbrentry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfnbrtable.Ospfnbrentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.Ospfnbrtable, self).__init__()

            self.yang_name = "ospfNbrTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ospfNbrEntry", ("ospfnbrentry", OSPFMIB.Ospfnbrtable.Ospfnbrentry))])
            self._leafs = OrderedDict()

            self.ospfnbrentry = YList(self)
            self._segment_path = lambda: "ospfNbrTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.Ospfnbrtable, [], name, value)


        class Ospfnbrentry(Entity):
            """
            The information regarding a single neighbor.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            
            storage.
            
            .. attribute:: ospfnbripaddr  (key)
            
            	The IP address this neighbor is using in its IP source address.  Note that, on addressless links, this will not be 0.0.0.0 but the  address of another of the neighbor's interfaces
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfnbraddresslessindex  (key)
            
            	On an interface having an IP address, zero. On addressless interfaces, the corresponding value of ifIndex in the Internet Standard MIB. On row creation, this can be derived from the instance
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ospfnbrrtrid
            
            	A 32\-bit integer (represented as a type IpAddress) uniquely identifying the neighboring router in the Autonomous System
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfnbroptions
            
            	A bit mask corresponding to the neighbor's options field.  Bit 0, if set, indicates that the system will operate on Type of Service metrics other than TOS 0.  If zero, the neighbor will ignore all metrics except the TOS 0 metric.  Bit 1, if set, indicates that the associated area accepts and operates on external information; if zero, it is a stub area.  Bit 2, if set, indicates that the system is capable of routing IP multicast datagrams, that is that it implements the multicast extensions to OSPF.  Bit 3, if set, indicates that the associated area is an NSSA.  These areas are capable of carrying type\-7 external advertisements, which are translated into type\-5 external advertisements at NSSA borders
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospfnbrpriority
            
            	The priority of this neighbor in the designated router election algorithm.  The value 0 signifies that the neighbor is not eligible to become the designated router on this particular network
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: ospfnbrstate
            
            	The state of the relationship with this neighbor
            	**type**\:  :py:class:`Ospfnbrstate <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfnbrtable.Ospfnbrentry.Ospfnbrstate>`
            
            .. attribute:: ospfnbrevents
            
            	The number of times this neighbor relationship has changed state or an error has occurred.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ospfDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfnbrlsretransqlen
            
            	The current length of the retransmission queue
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfnbmanbrstatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: ospfnbmanbrpermanence
            
            	This variable displays the status of the entry; 'dynamic' and 'permanent' refer to how the neighbor became known
            	**type**\:  :py:class:`Ospfnbmanbrpermanence <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfnbrtable.Ospfnbrentry.Ospfnbmanbrpermanence>`
            
            .. attribute:: ospfnbrhellosuppressed
            
            	Indicates whether Hellos are being suppressed to the neighbor
            	**type**\: bool
            
            .. attribute:: ospfnbrrestarthelperstatus
            
            	Indicates whether the router is acting as a graceful restart helper for the neighbor
            	**type**\:  :py:class:`Ospfnbrrestarthelperstatus <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfnbrtable.Ospfnbrentry.Ospfnbrrestarthelperstatus>`
            
            .. attribute:: ospfnbrrestarthelperage
            
            	Remaining time in current OSPF graceful restart interval, if the router is acting as a restart helper for the neighbor
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: ospfnbrrestarthelperexitreason
            
            	Describes the outcome of the last attempt at acting as a graceful restart helper for the neighbor
            	**type**\:  :py:class:`Ospfnbrrestarthelperexitreason <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfnbrtable.Ospfnbrentry.Ospfnbrrestarthelperexitreason>`
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OSPFMIB.Ospfnbrtable.Ospfnbrentry, self).__init__()

                self.yang_name = "ospfNbrEntry"
                self.yang_parent_name = "ospfNbrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfnbripaddr','ospfnbraddresslessindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfnbripaddr', YLeaf(YType.str, 'ospfNbrIpAddr')),
                    ('ospfnbraddresslessindex', YLeaf(YType.int32, 'ospfNbrAddressLessIndex')),
                    ('ospfnbrrtrid', YLeaf(YType.str, 'ospfNbrRtrId')),
                    ('ospfnbroptions', YLeaf(YType.int32, 'ospfNbrOptions')),
                    ('ospfnbrpriority', YLeaf(YType.int32, 'ospfNbrPriority')),
                    ('ospfnbrstate', YLeaf(YType.enumeration, 'ospfNbrState')),
                    ('ospfnbrevents', YLeaf(YType.uint32, 'ospfNbrEvents')),
                    ('ospfnbrlsretransqlen', YLeaf(YType.uint32, 'ospfNbrLsRetransQLen')),
                    ('ospfnbmanbrstatus', YLeaf(YType.enumeration, 'ospfNbmaNbrStatus')),
                    ('ospfnbmanbrpermanence', YLeaf(YType.enumeration, 'ospfNbmaNbrPermanence')),
                    ('ospfnbrhellosuppressed', YLeaf(YType.boolean, 'ospfNbrHelloSuppressed')),
                    ('ospfnbrrestarthelperstatus', YLeaf(YType.enumeration, 'ospfNbrRestartHelperStatus')),
                    ('ospfnbrrestarthelperage', YLeaf(YType.uint32, 'ospfNbrRestartHelperAge')),
                    ('ospfnbrrestarthelperexitreason', YLeaf(YType.enumeration, 'ospfNbrRestartHelperExitReason')),
                ])
                self.ospfnbripaddr = None
                self.ospfnbraddresslessindex = None
                self.ospfnbrrtrid = None
                self.ospfnbroptions = None
                self.ospfnbrpriority = None
                self.ospfnbrstate = None
                self.ospfnbrevents = None
                self.ospfnbrlsretransqlen = None
                self.ospfnbmanbrstatus = None
                self.ospfnbmanbrpermanence = None
                self.ospfnbrhellosuppressed = None
                self.ospfnbrrestarthelperstatus = None
                self.ospfnbrrestarthelperage = None
                self.ospfnbrrestarthelperexitreason = None
                self._segment_path = lambda: "ospfNbrEntry" + "[ospfNbrIpAddr='" + str(self.ospfnbripaddr) + "']" + "[ospfNbrAddressLessIndex='" + str(self.ospfnbraddresslessindex) + "']"
                self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/ospfNbrTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.Ospfnbrtable.Ospfnbrentry, ['ospfnbripaddr', 'ospfnbraddresslessindex', 'ospfnbrrtrid', 'ospfnbroptions', 'ospfnbrpriority', 'ospfnbrstate', 'ospfnbrevents', 'ospfnbrlsretransqlen', 'ospfnbmanbrstatus', 'ospfnbmanbrpermanence', 'ospfnbrhellosuppressed', 'ospfnbrrestarthelperstatus', 'ospfnbrrestarthelperage', 'ospfnbrrestarthelperexitreason'], name, value)

            class Ospfnbmanbrpermanence(Enum):
                """
                Ospfnbmanbrpermanence (Enum Class)

                This variable displays the status of the entry;

                'dynamic' and 'permanent' refer to how the neighbor

                became known.

                .. data:: dynamic = 1

                .. data:: permanent = 2

                """

                dynamic = Enum.YLeaf(1, "dynamic")

                permanent = Enum.YLeaf(2, "permanent")


            class Ospfnbrrestarthelperexitreason(Enum):
                """
                Ospfnbrrestarthelperexitreason (Enum Class)

                Describes the outcome of the last attempt at acting

                as a graceful restart helper for the neighbor.

                .. data:: none = 1

                .. data:: inProgress = 2

                .. data:: completed = 3

                .. data:: timedOut = 4

                .. data:: topologyChanged = 5

                """

                none = Enum.YLeaf(1, "none")

                inProgress = Enum.YLeaf(2, "inProgress")

                completed = Enum.YLeaf(3, "completed")

                timedOut = Enum.YLeaf(4, "timedOut")

                topologyChanged = Enum.YLeaf(5, "topologyChanged")


            class Ospfnbrrestarthelperstatus(Enum):
                """
                Ospfnbrrestarthelperstatus (Enum Class)

                Indicates whether the router is acting

                as a graceful restart helper for the neighbor.

                .. data:: notHelping = 1

                .. data:: helping = 2

                """

                notHelping = Enum.YLeaf(1, "notHelping")

                helping = Enum.YLeaf(2, "helping")


            class Ospfnbrstate(Enum):
                """
                Ospfnbrstate (Enum Class)

                The state of the relationship with this neighbor.

                .. data:: down = 1

                .. data:: attempt = 2

                .. data:: init = 3

                .. data:: twoWay = 4

                .. data:: exchangeStart = 5

                .. data:: exchange = 6

                .. data:: loading = 7

                .. data:: full = 8

                """

                down = Enum.YLeaf(1, "down")

                attempt = Enum.YLeaf(2, "attempt")

                init = Enum.YLeaf(3, "init")

                twoWay = Enum.YLeaf(4, "twoWay")

                exchangeStart = Enum.YLeaf(5, "exchangeStart")

                exchange = Enum.YLeaf(6, "exchange")

                loading = Enum.YLeaf(7, "loading")

                full = Enum.YLeaf(8, "full")



    class Ospfvirtnbrtable(Entity):
        """
        This table describes all virtual neighbors.
        Since virtual links are configured
        in the Virtual Interface Table, this table is read\-only.
        
        .. attribute:: ospfvirtnbrentry
        
        	Virtual neighbor information
        	**type**\: list of  		 :py:class:`Ospfvirtnbrentry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfvirtnbrtable.Ospfvirtnbrentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.Ospfvirtnbrtable, self).__init__()

            self.yang_name = "ospfVirtNbrTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ospfVirtNbrEntry", ("ospfvirtnbrentry", OSPFMIB.Ospfvirtnbrtable.Ospfvirtnbrentry))])
            self._leafs = OrderedDict()

            self.ospfvirtnbrentry = YList(self)
            self._segment_path = lambda: "ospfVirtNbrTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.Ospfvirtnbrtable, [], name, value)


        class Ospfvirtnbrentry(Entity):
            """
            Virtual neighbor information.
            
            .. attribute:: ospfvirtnbrarea  (key)
            
            	The Transit Area Identifier
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfvirtnbrrtrid  (key)
            
            	A 32\-bit integer uniquely identifying the neighboring router in the Autonomous System
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfvirtnbripaddr
            
            	The IP address this virtual neighbor is using
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfvirtnbroptions
            
            	A bit mask corresponding to the neighbor's options field.  Bit 1, if set, indicates that the system will operate on Type of Service metrics other than TOS 0.  If zero, the neighbor will ignore all metrics except the TOS 0 metric.  Bit 2, if set, indicates that the system is network multicast capable, i.e., that it implements OSPF multicast routing
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospfvirtnbrstate
            
            	The state of the virtual neighbor relationship
            	**type**\:  :py:class:`Ospfvirtnbrstate <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfvirtnbrtable.Ospfvirtnbrentry.Ospfvirtnbrstate>`
            
            .. attribute:: ospfvirtnbrevents
            
            	The number of times this virtual link has changed its state or an error has occurred.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ospfDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfvirtnbrlsretransqlen
            
            	The current length of the retransmission queue
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfvirtnbrhellosuppressed
            
            	Indicates whether Hellos are being suppressed to the neighbor
            	**type**\: bool
            
            .. attribute:: ospfvirtnbrrestarthelperstatus
            
            	Indicates whether the router is acting as a graceful restart helper for the neighbor
            	**type**\:  :py:class:`Ospfvirtnbrrestarthelperstatus <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfvirtnbrtable.Ospfvirtnbrentry.Ospfvirtnbrrestarthelperstatus>`
            
            .. attribute:: ospfvirtnbrrestarthelperage
            
            	Remaining time in current OSPF graceful restart interval, if the router is acting as a restart helper for the neighbor
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: ospfvirtnbrrestarthelperexitreason
            
            	Describes the outcome of the last attempt at acting as a graceful restart helper for the neighbor
            	**type**\:  :py:class:`Ospfvirtnbrrestarthelperexitreason <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfvirtnbrtable.Ospfvirtnbrentry.Ospfvirtnbrrestarthelperexitreason>`
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OSPFMIB.Ospfvirtnbrtable.Ospfvirtnbrentry, self).__init__()

                self.yang_name = "ospfVirtNbrEntry"
                self.yang_parent_name = "ospfVirtNbrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfvirtnbrarea','ospfvirtnbrrtrid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfvirtnbrarea', YLeaf(YType.str, 'ospfVirtNbrArea')),
                    ('ospfvirtnbrrtrid', YLeaf(YType.str, 'ospfVirtNbrRtrId')),
                    ('ospfvirtnbripaddr', YLeaf(YType.str, 'ospfVirtNbrIpAddr')),
                    ('ospfvirtnbroptions', YLeaf(YType.int32, 'ospfVirtNbrOptions')),
                    ('ospfvirtnbrstate', YLeaf(YType.enumeration, 'ospfVirtNbrState')),
                    ('ospfvirtnbrevents', YLeaf(YType.uint32, 'ospfVirtNbrEvents')),
                    ('ospfvirtnbrlsretransqlen', YLeaf(YType.uint32, 'ospfVirtNbrLsRetransQLen')),
                    ('ospfvirtnbrhellosuppressed', YLeaf(YType.boolean, 'ospfVirtNbrHelloSuppressed')),
                    ('ospfvirtnbrrestarthelperstatus', YLeaf(YType.enumeration, 'ospfVirtNbrRestartHelperStatus')),
                    ('ospfvirtnbrrestarthelperage', YLeaf(YType.uint32, 'ospfVirtNbrRestartHelperAge')),
                    ('ospfvirtnbrrestarthelperexitreason', YLeaf(YType.enumeration, 'ospfVirtNbrRestartHelperExitReason')),
                ])
                self.ospfvirtnbrarea = None
                self.ospfvirtnbrrtrid = None
                self.ospfvirtnbripaddr = None
                self.ospfvirtnbroptions = None
                self.ospfvirtnbrstate = None
                self.ospfvirtnbrevents = None
                self.ospfvirtnbrlsretransqlen = None
                self.ospfvirtnbrhellosuppressed = None
                self.ospfvirtnbrrestarthelperstatus = None
                self.ospfvirtnbrrestarthelperage = None
                self.ospfvirtnbrrestarthelperexitreason = None
                self._segment_path = lambda: "ospfVirtNbrEntry" + "[ospfVirtNbrArea='" + str(self.ospfvirtnbrarea) + "']" + "[ospfVirtNbrRtrId='" + str(self.ospfvirtnbrrtrid) + "']"
                self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/ospfVirtNbrTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.Ospfvirtnbrtable.Ospfvirtnbrentry, ['ospfvirtnbrarea', 'ospfvirtnbrrtrid', 'ospfvirtnbripaddr', 'ospfvirtnbroptions', 'ospfvirtnbrstate', 'ospfvirtnbrevents', 'ospfvirtnbrlsretransqlen', 'ospfvirtnbrhellosuppressed', 'ospfvirtnbrrestarthelperstatus', 'ospfvirtnbrrestarthelperage', 'ospfvirtnbrrestarthelperexitreason'], name, value)

            class Ospfvirtnbrrestarthelperexitreason(Enum):
                """
                Ospfvirtnbrrestarthelperexitreason (Enum Class)

                Describes the outcome of the last attempt at acting

                as a graceful restart helper for the neighbor.

                .. data:: none = 1

                .. data:: inProgress = 2

                .. data:: completed = 3

                .. data:: timedOut = 4

                .. data:: topologyChanged = 5

                """

                none = Enum.YLeaf(1, "none")

                inProgress = Enum.YLeaf(2, "inProgress")

                completed = Enum.YLeaf(3, "completed")

                timedOut = Enum.YLeaf(4, "timedOut")

                topologyChanged = Enum.YLeaf(5, "topologyChanged")


            class Ospfvirtnbrrestarthelperstatus(Enum):
                """
                Ospfvirtnbrrestarthelperstatus (Enum Class)

                Indicates whether the router is acting

                as a graceful restart helper for the neighbor.

                .. data:: notHelping = 1

                .. data:: helping = 2

                """

                notHelping = Enum.YLeaf(1, "notHelping")

                helping = Enum.YLeaf(2, "helping")


            class Ospfvirtnbrstate(Enum):
                """
                Ospfvirtnbrstate (Enum Class)

                The state of the virtual neighbor relationship.

                .. data:: down = 1

                .. data:: attempt = 2

                .. data:: init = 3

                .. data:: twoWay = 4

                .. data:: exchangeStart = 5

                .. data:: exchange = 6

                .. data:: loading = 7

                .. data:: full = 8

                """

                down = Enum.YLeaf(1, "down")

                attempt = Enum.YLeaf(2, "attempt")

                init = Enum.YLeaf(3, "init")

                twoWay = Enum.YLeaf(4, "twoWay")

                exchangeStart = Enum.YLeaf(5, "exchangeStart")

                exchange = Enum.YLeaf(6, "exchange")

                loading = Enum.YLeaf(7, "loading")

                full = Enum.YLeaf(8, "full")



    class Ospfextlsdbtable(Entity):
        """
        The OSPF Process's external LSA link state database.
        
        This table is identical to the OSPF LSDB Table
        in format, but contains only external link state
        advertisements.  The purpose is to allow external
        
        LSAs to be displayed once for the router rather
        than once in each non\-stub area.
        
        Note that external LSAs are also in the AS\-scope link state
        database.
        
        .. attribute:: ospfextlsdbentry
        
        	A single link state advertisement
        	**type**\: list of  		 :py:class:`Ospfextlsdbentry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfextlsdbtable.Ospfextlsdbentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.Ospfextlsdbtable, self).__init__()

            self.yang_name = "ospfExtLsdbTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ospfExtLsdbEntry", ("ospfextlsdbentry", OSPFMIB.Ospfextlsdbtable.Ospfextlsdbentry))])
            self._leafs = OrderedDict()

            self.ospfextlsdbentry = YList(self)
            self._segment_path = lambda: "ospfExtLsdbTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.Ospfextlsdbtable, [], name, value)


        class Ospfextlsdbentry(Entity):
            """
            A single link state advertisement.
            
            .. attribute:: ospfextlsdbtype  (key)
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\:  :py:class:`Ospfextlsdbtype <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfextlsdbtable.Ospfextlsdbentry.Ospfextlsdbtype>`
            
            	**status**\: deprecated
            
            .. attribute:: ospfextlsdblsid  (key)
            
            	The Link State ID is an LS Type Specific field containing either a Router ID or an IP address; it identifies the piece of the routing domain that is being described by the advertisement
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: ospfextlsdbrouterid  (key)
            
            	The 32\-bit number that uniquely identifies the originating router in the Autonomous System
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: ospfextlsdbsequence
            
            	The sequence number field is a signed 32\-bit integer.  It starts with the value '80000001'h, or \-'7FFFFFFF'h, and increments until '7FFFFFFF'h. Thus, a typical sequence number will be very negative. It is used to detect old and duplicate link state advertisements.  The space of sequence numbers is linearly ordered.  The larger the sequence number, the more recent the advertisement
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: ospfextlsdbage
            
            	This field is the age of the link state advertisement in seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: seconds
            
            	**status**\: deprecated
            
            .. attribute:: ospfextlsdbchecksum
            
            	This field is the checksum of the complete contents of the advertisement, excepting the age field.  The age field is excepted so that an advertisement's age can be incremented without updating the checksum.  The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred to as the Fletcher checksum
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: ospfextlsdbadvertisement
            
            	The entire link state advertisement, including its header
            	**type**\: str
            
            	**length:** 36
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OSPFMIB.Ospfextlsdbtable.Ospfextlsdbentry, self).__init__()

                self.yang_name = "ospfExtLsdbEntry"
                self.yang_parent_name = "ospfExtLsdbTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfextlsdbtype','ospfextlsdblsid','ospfextlsdbrouterid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfextlsdbtype', YLeaf(YType.enumeration, 'ospfExtLsdbType')),
                    ('ospfextlsdblsid', YLeaf(YType.str, 'ospfExtLsdbLsid')),
                    ('ospfextlsdbrouterid', YLeaf(YType.str, 'ospfExtLsdbRouterId')),
                    ('ospfextlsdbsequence', YLeaf(YType.int32, 'ospfExtLsdbSequence')),
                    ('ospfextlsdbage', YLeaf(YType.int32, 'ospfExtLsdbAge')),
                    ('ospfextlsdbchecksum', YLeaf(YType.int32, 'ospfExtLsdbChecksum')),
                    ('ospfextlsdbadvertisement', YLeaf(YType.str, 'ospfExtLsdbAdvertisement')),
                ])
                self.ospfextlsdbtype = None
                self.ospfextlsdblsid = None
                self.ospfextlsdbrouterid = None
                self.ospfextlsdbsequence = None
                self.ospfextlsdbage = None
                self.ospfextlsdbchecksum = None
                self.ospfextlsdbadvertisement = None
                self._segment_path = lambda: "ospfExtLsdbEntry" + "[ospfExtLsdbType='" + str(self.ospfextlsdbtype) + "']" + "[ospfExtLsdbLsid='" + str(self.ospfextlsdblsid) + "']" + "[ospfExtLsdbRouterId='" + str(self.ospfextlsdbrouterid) + "']"
                self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/ospfExtLsdbTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.Ospfextlsdbtable.Ospfextlsdbentry, ['ospfextlsdbtype', 'ospfextlsdblsid', 'ospfextlsdbrouterid', 'ospfextlsdbsequence', 'ospfextlsdbage', 'ospfextlsdbchecksum', 'ospfextlsdbadvertisement'], name, value)

            class Ospfextlsdbtype(Enum):
                """
                Ospfextlsdbtype (Enum Class)

                The type of the link state advertisement.

                Each link state type has a separate advertisement

                format.

                .. data:: asExternalLink = 5

                """

                asExternalLink = Enum.YLeaf(5, "asExternalLink")



    class Ospfareaaggregatetable(Entity):
        """
        The Area Aggregate Table acts as an adjunct
        to the Area Table.  It describes those address aggregates
        that are configured to be propagated from an area.
        Its purpose is to reduce the amount of information
        that is known beyond an Area's borders.
        
        It contains a set of IP address ranges
        specified by an IP address/IP network mask pair.
        For example, a class B address range of X.X.X.X
        with a network mask of 255.255.0.0 includes all IP
        addresses from X.X.0.0 to X.X.255.255.
        
        Note that if ranges are configured such that one range
        subsumes another range (e.g., 10.0.0.0 mask 255.0.0.0
        and 10.1.0.0 mask 255.255.0.0),
        the most specific match is the preferred one.
        
        .. attribute:: ospfareaaggregateentry
        
        	A single area aggregate entry.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile storage
        	**type**\: list of  		 :py:class:`Ospfareaaggregateentry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfareaaggregatetable.Ospfareaaggregateentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.Ospfareaaggregatetable, self).__init__()

            self.yang_name = "ospfAreaAggregateTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ospfAreaAggregateEntry", ("ospfareaaggregateentry", OSPFMIB.Ospfareaaggregatetable.Ospfareaaggregateentry))])
            self._leafs = OrderedDict()

            self.ospfareaaggregateentry = YList(self)
            self._segment_path = lambda: "ospfAreaAggregateTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.Ospfareaaggregatetable, [], name, value)


        class Ospfareaaggregateentry(Entity):
            """
            A single area aggregate entry.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            storage.
            
            .. attribute:: ospfareaaggregateareaid  (key)
            
            	The area within which the address aggregate is to be found
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfareaaggregatelsdbtype  (key)
            
            	The type of the address aggregate.  This field specifies the Lsdb type that this address aggregate applies to
            	**type**\:  :py:class:`Ospfareaaggregatelsdbtype <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfareaaggregatetable.Ospfareaaggregateentry.Ospfareaaggregatelsdbtype>`
            
            .. attribute:: ospfareaaggregatenet  (key)
            
            	The IP address of the net or subnet indicated by the range
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfareaaggregatemask  (key)
            
            	The subnet mask that pertains to the net or subnet
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfareaaggregatestatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: ospfareaaggregateeffect
            
            	Subnets subsumed by ranges either trigger the advertisement of the indicated aggregate (advertiseMatching) or result in the subnet's not being advertised at all outside the area
            	**type**\:  :py:class:`Ospfareaaggregateeffect <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfareaaggregatetable.Ospfareaaggregateentry.Ospfareaaggregateeffect>`
            
            .. attribute:: ospfareaaggregateextroutetag
            
            	External route tag to be included in NSSA (type\-7) LSAs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OSPFMIB.Ospfareaaggregatetable.Ospfareaaggregateentry, self).__init__()

                self.yang_name = "ospfAreaAggregateEntry"
                self.yang_parent_name = "ospfAreaAggregateTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfareaaggregateareaid','ospfareaaggregatelsdbtype','ospfareaaggregatenet','ospfareaaggregatemask']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfareaaggregateareaid', YLeaf(YType.str, 'ospfAreaAggregateAreaID')),
                    ('ospfareaaggregatelsdbtype', YLeaf(YType.enumeration, 'ospfAreaAggregateLsdbType')),
                    ('ospfareaaggregatenet', YLeaf(YType.str, 'ospfAreaAggregateNet')),
                    ('ospfareaaggregatemask', YLeaf(YType.str, 'ospfAreaAggregateMask')),
                    ('ospfareaaggregatestatus', YLeaf(YType.enumeration, 'ospfAreaAggregateStatus')),
                    ('ospfareaaggregateeffect', YLeaf(YType.enumeration, 'ospfAreaAggregateEffect')),
                    ('ospfareaaggregateextroutetag', YLeaf(YType.uint32, 'ospfAreaAggregateExtRouteTag')),
                ])
                self.ospfareaaggregateareaid = None
                self.ospfareaaggregatelsdbtype = None
                self.ospfareaaggregatenet = None
                self.ospfareaaggregatemask = None
                self.ospfareaaggregatestatus = None
                self.ospfareaaggregateeffect = None
                self.ospfareaaggregateextroutetag = None
                self._segment_path = lambda: "ospfAreaAggregateEntry" + "[ospfAreaAggregateAreaID='" + str(self.ospfareaaggregateareaid) + "']" + "[ospfAreaAggregateLsdbType='" + str(self.ospfareaaggregatelsdbtype) + "']" + "[ospfAreaAggregateNet='" + str(self.ospfareaaggregatenet) + "']" + "[ospfAreaAggregateMask='" + str(self.ospfareaaggregatemask) + "']"
                self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/ospfAreaAggregateTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.Ospfareaaggregatetable.Ospfareaaggregateentry, ['ospfareaaggregateareaid', 'ospfareaaggregatelsdbtype', 'ospfareaaggregatenet', 'ospfareaaggregatemask', 'ospfareaaggregatestatus', 'ospfareaaggregateeffect', 'ospfareaaggregateextroutetag'], name, value)

            class Ospfareaaggregateeffect(Enum):
                """
                Ospfareaaggregateeffect (Enum Class)

                Subnets subsumed by ranges either trigger the

                advertisement of the indicated aggregate

                (advertiseMatching) or result in the subnet's not

                being advertised at all outside the area.

                .. data:: advertiseMatching = 1

                .. data:: doNotAdvertiseMatching = 2

                """

                advertiseMatching = Enum.YLeaf(1, "advertiseMatching")

                doNotAdvertiseMatching = Enum.YLeaf(2, "doNotAdvertiseMatching")


            class Ospfareaaggregatelsdbtype(Enum):
                """
                Ospfareaaggregatelsdbtype (Enum Class)

                The type of the address aggregate.  This field

                specifies the Lsdb type that this address

                aggregate applies to.

                .. data:: summaryLink = 3

                .. data:: nssaExternalLink = 7

                """

                summaryLink = Enum.YLeaf(3, "summaryLink")

                nssaExternalLink = Enum.YLeaf(7, "nssaExternalLink")



    class Ospflocallsdbtable(Entity):
        """
        The OSPF Process's link\-local link state database
        for non\-virtual links.
        This table is identical to the OSPF LSDB Table
        in format, but contains only link\-local Link State
        Advertisements for non\-virtual links.  The purpose is
        to allow link\-local LSAs to be displayed for each
        non\-virtual interface.  This table is implemented to
        support type\-9 LSAs that are defined
        in 'The OSPF Opaque LSA Option'.
        
        .. attribute:: ospflocallsdbentry
        
        	A single link state advertisement
        	**type**\: list of  		 :py:class:`Ospflocallsdbentry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospflocallsdbtable.Ospflocallsdbentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.Ospflocallsdbtable, self).__init__()

            self.yang_name = "ospfLocalLsdbTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ospfLocalLsdbEntry", ("ospflocallsdbentry", OSPFMIB.Ospflocallsdbtable.Ospflocallsdbentry))])
            self._leafs = OrderedDict()

            self.ospflocallsdbentry = YList(self)
            self._segment_path = lambda: "ospfLocalLsdbTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.Ospflocallsdbtable, [], name, value)


        class Ospflocallsdbentry(Entity):
            """
            A single link state advertisement.
            
            .. attribute:: ospflocallsdbipaddress  (key)
            
            	The IP address of the interface from which the LSA was received if the interface is numbered
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospflocallsdbaddresslessif  (key)
            
            	The interface index of the interface from which the LSA was received if the interface is unnumbered
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ospflocallsdbtype  (key)
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\:  :py:class:`Ospflocallsdbtype <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospflocallsdbtable.Ospflocallsdbentry.Ospflocallsdbtype>`
            
            .. attribute:: ospflocallsdblsid  (key)
            
            	The Link State ID is an LS Type Specific field containing a 32\-bit identifier in IP address format; it identifies the piece of the routing domain that is being described by the advertisement
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospflocallsdbrouterid  (key)
            
            	The 32\-bit number that uniquely identifies the originating router in the Autonomous System
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospflocallsdbsequence
            
            	The sequence number field is a signed 32\-bit integer.  It starts with the value '80000001'h, or \-'7FFFFFFF'h, and increments until '7FFFFFFF'h. Thus, a typical sequence number will be very negative. It is used to detect old and duplicate link state advertisements.  The space of sequence numbers is linearly ordered.  The larger the sequence number, the more recent the advertisement
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospflocallsdbage
            
            	This field is the age of the link state advertisement in seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: seconds
            
            .. attribute:: ospflocallsdbchecksum
            
            	This field is the checksum of the complete contents of the advertisement, excepting the age field.  The age field is excepted so that an advertisement's age can be incremented without updating the checksum.  The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred to as the Fletcher checksum
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospflocallsdbadvertisement
            
            	The entire link state advertisement, including its header.  Note that for variable length LSAs, SNMP agents may not be able to return the largest string size
            	**type**\: str
            
            	**length:** 1..65535
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OSPFMIB.Ospflocallsdbtable.Ospflocallsdbentry, self).__init__()

                self.yang_name = "ospfLocalLsdbEntry"
                self.yang_parent_name = "ospfLocalLsdbTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospflocallsdbipaddress','ospflocallsdbaddresslessif','ospflocallsdbtype','ospflocallsdblsid','ospflocallsdbrouterid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospflocallsdbipaddress', YLeaf(YType.str, 'ospfLocalLsdbIpAddress')),
                    ('ospflocallsdbaddresslessif', YLeaf(YType.int32, 'ospfLocalLsdbAddressLessIf')),
                    ('ospflocallsdbtype', YLeaf(YType.enumeration, 'ospfLocalLsdbType')),
                    ('ospflocallsdblsid', YLeaf(YType.str, 'ospfLocalLsdbLsid')),
                    ('ospflocallsdbrouterid', YLeaf(YType.str, 'ospfLocalLsdbRouterId')),
                    ('ospflocallsdbsequence', YLeaf(YType.int32, 'ospfLocalLsdbSequence')),
                    ('ospflocallsdbage', YLeaf(YType.int32, 'ospfLocalLsdbAge')),
                    ('ospflocallsdbchecksum', YLeaf(YType.int32, 'ospfLocalLsdbChecksum')),
                    ('ospflocallsdbadvertisement', YLeaf(YType.str, 'ospfLocalLsdbAdvertisement')),
                ])
                self.ospflocallsdbipaddress = None
                self.ospflocallsdbaddresslessif = None
                self.ospflocallsdbtype = None
                self.ospflocallsdblsid = None
                self.ospflocallsdbrouterid = None
                self.ospflocallsdbsequence = None
                self.ospflocallsdbage = None
                self.ospflocallsdbchecksum = None
                self.ospflocallsdbadvertisement = None
                self._segment_path = lambda: "ospfLocalLsdbEntry" + "[ospfLocalLsdbIpAddress='" + str(self.ospflocallsdbipaddress) + "']" + "[ospfLocalLsdbAddressLessIf='" + str(self.ospflocallsdbaddresslessif) + "']" + "[ospfLocalLsdbType='" + str(self.ospflocallsdbtype) + "']" + "[ospfLocalLsdbLsid='" + str(self.ospflocallsdblsid) + "']" + "[ospfLocalLsdbRouterId='" + str(self.ospflocallsdbrouterid) + "']"
                self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/ospfLocalLsdbTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.Ospflocallsdbtable.Ospflocallsdbentry, ['ospflocallsdbipaddress', 'ospflocallsdbaddresslessif', 'ospflocallsdbtype', 'ospflocallsdblsid', 'ospflocallsdbrouterid', 'ospflocallsdbsequence', 'ospflocallsdbage', 'ospflocallsdbchecksum', 'ospflocallsdbadvertisement'], name, value)

            class Ospflocallsdbtype(Enum):
                """
                Ospflocallsdbtype (Enum Class)

                The type of the link state advertisement.

                Each link state type has a separate

                advertisement format.

                .. data:: localOpaqueLink = 9

                """

                localOpaqueLink = Enum.YLeaf(9, "localOpaqueLink")



    class Ospfvirtlocallsdbtable(Entity):
        """
        The OSPF Process's link\-local link state database
        for virtual links.
        
        This table is identical to the OSPF LSDB Table
        in format, but contains only link\-local Link State
        Advertisements for virtual links.  The purpose is to
        allow link\-local LSAs to be displayed for each virtual
        interface.  This table is implemented to support type\-9 LSAs
        that are defined in 'The OSPF Opaque LSA Option'.
        
        .. attribute:: ospfvirtlocallsdbentry
        
        	A single link state advertisement
        	**type**\: list of  		 :py:class:`Ospfvirtlocallsdbentry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfvirtlocallsdbtable.Ospfvirtlocallsdbentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.Ospfvirtlocallsdbtable, self).__init__()

            self.yang_name = "ospfVirtLocalLsdbTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ospfVirtLocalLsdbEntry", ("ospfvirtlocallsdbentry", OSPFMIB.Ospfvirtlocallsdbtable.Ospfvirtlocallsdbentry))])
            self._leafs = OrderedDict()

            self.ospfvirtlocallsdbentry = YList(self)
            self._segment_path = lambda: "ospfVirtLocalLsdbTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.Ospfvirtlocallsdbtable, [], name, value)


        class Ospfvirtlocallsdbentry(Entity):
            """
            A single link state advertisement.
            
            .. attribute:: ospfvirtlocallsdbtransitarea  (key)
            
            	The transit area that the virtual link traverses.  By definition, this is not 0.0.0.0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfvirtlocallsdbneighbor  (key)
            
            	The Router ID of the virtual neighbor
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfvirtlocallsdbtype  (key)
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\:  :py:class:`Ospfvirtlocallsdbtype <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfvirtlocallsdbtable.Ospfvirtlocallsdbentry.Ospfvirtlocallsdbtype>`
            
            .. attribute:: ospfvirtlocallsdblsid  (key)
            
            	The Link State ID is an LS Type Specific field containing a 32\-bit identifier in IP address format; it identifies the piece of the routing domain that is being described by the advertisement
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfvirtlocallsdbrouterid  (key)
            
            	The 32\-bit number that uniquely identifies the originating router in the Autonomous System
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfvirtlocallsdbsequence
            
            	The sequence number field is a signed 32\-bit integer.  It starts with the value '80000001'h, or \-'7FFFFFFF'h, and increments until '7FFFFFFF'h. Thus, a typical sequence number will be very negative. It is used to detect old and duplicate link state advertisements.  The space of sequence numbers is linearly ordered.  The larger the sequence number, the more recent the advertisement
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospfvirtlocallsdbage
            
            	This field is the age of the link state advertisement in seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: seconds
            
            .. attribute:: ospfvirtlocallsdbchecksum
            
            	This field is the checksum of the complete contents of the advertisement, excepting the age field.  The age field is excepted so that  an advertisement's age can be incremented without updating the checksum.  The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred to as the Fletcher checksum
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospfvirtlocallsdbadvertisement
            
            	The entire link state advertisement, including its header
            	**type**\: str
            
            	**length:** 1..65535
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OSPFMIB.Ospfvirtlocallsdbtable.Ospfvirtlocallsdbentry, self).__init__()

                self.yang_name = "ospfVirtLocalLsdbEntry"
                self.yang_parent_name = "ospfVirtLocalLsdbTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfvirtlocallsdbtransitarea','ospfvirtlocallsdbneighbor','ospfvirtlocallsdbtype','ospfvirtlocallsdblsid','ospfvirtlocallsdbrouterid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfvirtlocallsdbtransitarea', YLeaf(YType.str, 'ospfVirtLocalLsdbTransitArea')),
                    ('ospfvirtlocallsdbneighbor', YLeaf(YType.str, 'ospfVirtLocalLsdbNeighbor')),
                    ('ospfvirtlocallsdbtype', YLeaf(YType.enumeration, 'ospfVirtLocalLsdbType')),
                    ('ospfvirtlocallsdblsid', YLeaf(YType.str, 'ospfVirtLocalLsdbLsid')),
                    ('ospfvirtlocallsdbrouterid', YLeaf(YType.str, 'ospfVirtLocalLsdbRouterId')),
                    ('ospfvirtlocallsdbsequence', YLeaf(YType.int32, 'ospfVirtLocalLsdbSequence')),
                    ('ospfvirtlocallsdbage', YLeaf(YType.int32, 'ospfVirtLocalLsdbAge')),
                    ('ospfvirtlocallsdbchecksum', YLeaf(YType.int32, 'ospfVirtLocalLsdbChecksum')),
                    ('ospfvirtlocallsdbadvertisement', YLeaf(YType.str, 'ospfVirtLocalLsdbAdvertisement')),
                ])
                self.ospfvirtlocallsdbtransitarea = None
                self.ospfvirtlocallsdbneighbor = None
                self.ospfvirtlocallsdbtype = None
                self.ospfvirtlocallsdblsid = None
                self.ospfvirtlocallsdbrouterid = None
                self.ospfvirtlocallsdbsequence = None
                self.ospfvirtlocallsdbage = None
                self.ospfvirtlocallsdbchecksum = None
                self.ospfvirtlocallsdbadvertisement = None
                self._segment_path = lambda: "ospfVirtLocalLsdbEntry" + "[ospfVirtLocalLsdbTransitArea='" + str(self.ospfvirtlocallsdbtransitarea) + "']" + "[ospfVirtLocalLsdbNeighbor='" + str(self.ospfvirtlocallsdbneighbor) + "']" + "[ospfVirtLocalLsdbType='" + str(self.ospfvirtlocallsdbtype) + "']" + "[ospfVirtLocalLsdbLsid='" + str(self.ospfvirtlocallsdblsid) + "']" + "[ospfVirtLocalLsdbRouterId='" + str(self.ospfvirtlocallsdbrouterid) + "']"
                self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/ospfVirtLocalLsdbTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.Ospfvirtlocallsdbtable.Ospfvirtlocallsdbentry, ['ospfvirtlocallsdbtransitarea', 'ospfvirtlocallsdbneighbor', 'ospfvirtlocallsdbtype', 'ospfvirtlocallsdblsid', 'ospfvirtlocallsdbrouterid', 'ospfvirtlocallsdbsequence', 'ospfvirtlocallsdbage', 'ospfvirtlocallsdbchecksum', 'ospfvirtlocallsdbadvertisement'], name, value)

            class Ospfvirtlocallsdbtype(Enum):
                """
                Ospfvirtlocallsdbtype (Enum Class)

                The type of the link state advertisement.

                Each link state type has a separate

                advertisement format.

                .. data:: localOpaqueLink = 9

                """

                localOpaqueLink = Enum.YLeaf(9, "localOpaqueLink")



    class Ospfaslsdbtable(Entity):
        """
        The OSPF Process's AS\-scope LSA link state database.
        The database contains the AS\-scope Link State
        Advertisements from throughout the areas that
        the device is attached to.
        
        This table is identical to the OSPF LSDB Table
        in format, but contains only AS\-scope Link State
        Advertisements.  The purpose is to allow AS\-scope
        LSAs to be displayed once for the router rather
        than once in each non\-stub area.
        
        .. attribute:: ospfaslsdbentry
        
        	A single link state advertisement
        	**type**\: list of  		 :py:class:`Ospfaslsdbentry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfaslsdbtable.Ospfaslsdbentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.Ospfaslsdbtable, self).__init__()

            self.yang_name = "ospfAsLsdbTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ospfAsLsdbEntry", ("ospfaslsdbentry", OSPFMIB.Ospfaslsdbtable.Ospfaslsdbentry))])
            self._leafs = OrderedDict()

            self.ospfaslsdbentry = YList(self)
            self._segment_path = lambda: "ospfAsLsdbTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.Ospfaslsdbtable, [], name, value)


        class Ospfaslsdbentry(Entity):
            """
            A single link state advertisement.
            
            .. attribute:: ospfaslsdbtype  (key)
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\:  :py:class:`Ospfaslsdbtype <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfaslsdbtable.Ospfaslsdbentry.Ospfaslsdbtype>`
            
            .. attribute:: ospfaslsdblsid  (key)
            
            	The Link State ID is an LS Type Specific field containing either a Router ID or an IP address;  it identifies the piece of the routing domain that is being described by the advertisement
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfaslsdbrouterid  (key)
            
            	The 32\-bit number that uniquely identifies the originating router in the Autonomous System
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfaslsdbsequence
            
            	The sequence number field is a signed 32\-bit integer.  It starts with the value '80000001'h, or \-'7FFFFFFF'h, and increments until '7FFFFFFF'h. Thus, a typical sequence number will be very negative. It is used to detect old and duplicate link state advertisements.  The space of sequence numbers is linearly ordered.  The larger the sequence number, the more recent the advertisement
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospfaslsdbage
            
            	This field is the age of the link state advertisement in seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: seconds
            
            .. attribute:: ospfaslsdbchecksum
            
            	This field is the checksum of the complete contents of the advertisement, excepting the age field.  The age field is excepted so that an advertisement's age can be incremented without updating the checksum.  The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred to as the Fletcher checksum
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospfaslsdbadvertisement
            
            	The entire link state advertisement, including its header
            	**type**\: str
            
            	**length:** 1..65535
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OSPFMIB.Ospfaslsdbtable.Ospfaslsdbentry, self).__init__()

                self.yang_name = "ospfAsLsdbEntry"
                self.yang_parent_name = "ospfAsLsdbTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfaslsdbtype','ospfaslsdblsid','ospfaslsdbrouterid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfaslsdbtype', YLeaf(YType.enumeration, 'ospfAsLsdbType')),
                    ('ospfaslsdblsid', YLeaf(YType.str, 'ospfAsLsdbLsid')),
                    ('ospfaslsdbrouterid', YLeaf(YType.str, 'ospfAsLsdbRouterId')),
                    ('ospfaslsdbsequence', YLeaf(YType.int32, 'ospfAsLsdbSequence')),
                    ('ospfaslsdbage', YLeaf(YType.int32, 'ospfAsLsdbAge')),
                    ('ospfaslsdbchecksum', YLeaf(YType.int32, 'ospfAsLsdbChecksum')),
                    ('ospfaslsdbadvertisement', YLeaf(YType.str, 'ospfAsLsdbAdvertisement')),
                ])
                self.ospfaslsdbtype = None
                self.ospfaslsdblsid = None
                self.ospfaslsdbrouterid = None
                self.ospfaslsdbsequence = None
                self.ospfaslsdbage = None
                self.ospfaslsdbchecksum = None
                self.ospfaslsdbadvertisement = None
                self._segment_path = lambda: "ospfAsLsdbEntry" + "[ospfAsLsdbType='" + str(self.ospfaslsdbtype) + "']" + "[ospfAsLsdbLsid='" + str(self.ospfaslsdblsid) + "']" + "[ospfAsLsdbRouterId='" + str(self.ospfaslsdbrouterid) + "']"
                self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/ospfAsLsdbTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.Ospfaslsdbtable.Ospfaslsdbentry, ['ospfaslsdbtype', 'ospfaslsdblsid', 'ospfaslsdbrouterid', 'ospfaslsdbsequence', 'ospfaslsdbage', 'ospfaslsdbchecksum', 'ospfaslsdbadvertisement'], name, value)

            class Ospfaslsdbtype(Enum):
                """
                Ospfaslsdbtype (Enum Class)

                The type of the link state advertisement.

                Each link state type has a separate

                advertisement format.

                .. data:: asExternalLink = 5

                .. data:: asOpaqueLink = 11

                """

                asExternalLink = Enum.YLeaf(5, "asExternalLink")

                asOpaqueLink = Enum.YLeaf(11, "asOpaqueLink")



    class Ospfarealsacounttable(Entity):
        """
        This table maintains per\-area, per\-LSA\-type counters
        
        .. attribute:: ospfarealsacountentry
        
        	An entry with a number of link advertisements  of a given type for a given area
        	**type**\: list of  		 :py:class:`Ospfarealsacountentry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfarealsacounttable.Ospfarealsacountentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.Ospfarealsacounttable, self).__init__()

            self.yang_name = "ospfAreaLsaCountTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ospfAreaLsaCountEntry", ("ospfarealsacountentry", OSPFMIB.Ospfarealsacounttable.Ospfarealsacountentry))])
            self._leafs = OrderedDict()

            self.ospfarealsacountentry = YList(self)
            self._segment_path = lambda: "ospfAreaLsaCountTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.Ospfarealsacounttable, [], name, value)


        class Ospfarealsacountentry(Entity):
            """
            An entry with a number of link advertisements
            
            of a given type for a given area.
            
            .. attribute:: ospfarealsacountareaid  (key)
            
            	This entry Area ID
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfarealsacountlsatype  (key)
            
            	This entry LSA type
            	**type**\:  :py:class:`Ospfarealsacountlsatype <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospfarealsacounttable.Ospfarealsacountentry.Ospfarealsacountlsatype>`
            
            .. attribute:: ospfarealsacountnumber
            
            	Number of LSAs of a given type for a given area
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OSPFMIB.Ospfarealsacounttable.Ospfarealsacountentry, self).__init__()

                self.yang_name = "ospfAreaLsaCountEntry"
                self.yang_parent_name = "ospfAreaLsaCountTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfarealsacountareaid','ospfarealsacountlsatype']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfarealsacountareaid', YLeaf(YType.str, 'ospfAreaLsaCountAreaId')),
                    ('ospfarealsacountlsatype', YLeaf(YType.enumeration, 'ospfAreaLsaCountLsaType')),
                    ('ospfarealsacountnumber', YLeaf(YType.uint32, 'ospfAreaLsaCountNumber')),
                ])
                self.ospfarealsacountareaid = None
                self.ospfarealsacountlsatype = None
                self.ospfarealsacountnumber = None
                self._segment_path = lambda: "ospfAreaLsaCountEntry" + "[ospfAreaLsaCountAreaId='" + str(self.ospfarealsacountareaid) + "']" + "[ospfAreaLsaCountLsaType='" + str(self.ospfarealsacountlsatype) + "']"
                self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/ospfAreaLsaCountTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.Ospfarealsacounttable.Ospfarealsacountentry, ['ospfarealsacountareaid', 'ospfarealsacountlsatype', 'ospfarealsacountnumber'], name, value)

            class Ospfarealsacountlsatype(Enum):
                """
                Ospfarealsacountlsatype (Enum Class)

                This entry LSA type.

                .. data:: routerLink = 1

                .. data:: networkLink = 2

                .. data:: summaryLink = 3

                .. data:: asSummaryLink = 4

                .. data:: multicastLink = 6

                .. data:: nssaExternalLink = 7

                .. data:: areaOpaqueLink = 10

                """

                routerLink = Enum.YLeaf(1, "routerLink")

                networkLink = Enum.YLeaf(2, "networkLink")

                summaryLink = Enum.YLeaf(3, "summaryLink")

                asSummaryLink = Enum.YLeaf(4, "asSummaryLink")

                multicastLink = Enum.YLeaf(6, "multicastLink")

                nssaExternalLink = Enum.YLeaf(7, "nssaExternalLink")

                areaOpaqueLink = Enum.YLeaf(10, "areaOpaqueLink")


    def clone_ptr(self):
        self._top_entity = OSPFMIB()
        return self._top_entity


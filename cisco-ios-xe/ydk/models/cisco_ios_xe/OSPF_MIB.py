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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ospfauthenticationtype(Enum):
    """
    Ospfauthenticationtype

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
    Status

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



class OspfMib(Entity):
    """
    
    
    .. attribute:: ospfareaaggregatetable
    
    	The Area Aggregate Table acts as an adjunct to the Area Table.  It describes those address aggregates that are configured to be propagated from an area. Its purpose is to reduce the amount of information that is known beyond an Area's borders.  It contains a set of IP address ranges specified by an IP address/IP network mask pair. For example, a class B address range of X.X.X.X with a network mask of 255.255.0.0 includes all IP addresses from X.X.0.0 to X.X.255.255.  Note that if ranges are configured such that one range subsumes another range (e.g., 10.0.0.0 mask 255.0.0.0 and 10.1.0.0 mask 255.255.0.0), the most specific match is the preferred one
    	**type**\:   :py:class:`Ospfareaaggregatetable <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfareaaggregatetable>`
    
    .. attribute:: ospfarealsacounttable
    
    	This table maintains per\-area, per\-LSA\-type counters
    	**type**\:   :py:class:`Ospfarealsacounttable <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfarealsacounttable>`
    
    .. attribute:: ospfarearangetable
    
    	The Address Range Table acts as an adjunct to the Area Table.  It describes those Address Range Summaries that are configured to be propagated from an Area to reduce the amount of information about it that is known beyond its borders.  It contains a set of IP address ranges specified by an IP address/IP network mask pair. For example, class B address range of X.X.X.X with a network mask of 255.255.0.0 includes all IP addresses from X.X.0.0 to X.X.255.255.  Note that this table is obsoleted and is replaced by the Area Aggregate Table
    	**type**\:   :py:class:`Ospfarearangetable <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfarearangetable>`
    
    	**status**\: obsolete
    
    .. attribute:: ospfareatable
    
    	Information describing the configured parameters and cumulative statistics of the router's attached areas. The interfaces and virtual links are configured as part of these areas.  Area 0.0.0.0, by definition, is the backbone area
    	**type**\:   :py:class:`Ospfareatable <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfareatable>`
    
    .. attribute:: ospfaslsdbtable
    
    	The OSPF Process's AS\-scope LSA link state database. The database contains the AS\-scope Link State Advertisements from throughout the areas that the device is attached to.  This table is identical to the OSPF LSDB Table in format, but contains only AS\-scope Link State Advertisements.  The purpose is to allow AS\-scope LSAs to be displayed once for the router rather than once in each non\-stub area
    	**type**\:   :py:class:`Ospfaslsdbtable <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfaslsdbtable>`
    
    .. attribute:: ospfextlsdbtable
    
    	The OSPF Process's external LSA link state database.  This table is identical to the OSPF LSDB Table in format, but contains only external link state advertisements.  The purpose is to allow external  LSAs to be displayed once for the router rather than once in each non\-stub area.  Note that external LSAs are also in the AS\-scope link state database
    	**type**\:   :py:class:`Ospfextlsdbtable <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfextlsdbtable>`
    
    	**status**\: deprecated
    
    .. attribute:: ospfgeneralgroup
    
    	
    	**type**\:   :py:class:`Ospfgeneralgroup <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfgeneralgroup>`
    
    .. attribute:: ospfhosttable
    
    	The Host/Metric Table indicates what hosts are directly  attached to the router, what metrics and types of service should be advertised for them, and what areas they are found within
    	**type**\:   :py:class:`Ospfhosttable <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfhosttable>`
    
    .. attribute:: ospfifmetrictable
    
    	The Metric Table describes the metrics to be advertised for a specified interface at the various types of service. As such, this table is an adjunct of the OSPF Interface Table.  Types of service, as defined by RFC 791, have the ability to request low delay, high bandwidth, or reliable linkage.  For the purposes of this specification, the measure of bandwidth\:  Metric = referenceBandwidth / ifSpeed  is the default value. The default reference bandwidth is 10^8. For multiple link interfaces, note that ifSpeed is the sum of the individual link speeds.  This yields a number having the following typical values\:  Network Type/bit rate   Metric  >= 100 MBPS                 1 Ethernet/802.3             10 E1                         48 T1 (ESF)                   65 64 KBPS                    1562 56 KBPS                    1785 19.2 KBPS                  5208 9.6 KBPS                   10416  Routes that are not specified use the default (TOS 0) metric.  Note that the default reference bandwidth can be configured using the general group object ospfReferenceBandwidth
    	**type**\:   :py:class:`Ospfifmetrictable <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfifmetrictable>`
    
    .. attribute:: ospfiftable
    
    	The OSPF Interface Table describes the interfaces from the viewpoint of OSPF. It augments the ipAddrTable with OSPF specific information
    	**type**\:   :py:class:`Ospfiftable <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfiftable>`
    
    .. attribute:: ospflocallsdbtable
    
    	The OSPF Process's link\-local link state database for non\-virtual links. This table is identical to the OSPF LSDB Table in format, but contains only link\-local Link State Advertisements for non\-virtual links.  The purpose is to allow link\-local LSAs to be displayed for each non\-virtual interface.  This table is implemented to support type\-9 LSAs that are defined in 'The OSPF Opaque LSA Option'
    	**type**\:   :py:class:`Ospflocallsdbtable <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospflocallsdbtable>`
    
    .. attribute:: ospflsdbtable
    
    	The OSPF Process's link state database (LSDB). The LSDB contains the link state advertisements from throughout the areas that the device is attached to
    	**type**\:   :py:class:`Ospflsdbtable <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospflsdbtable>`
    
    .. attribute:: ospfnbrtable
    
    	A table describing all non\-virtual neighbors in the locality of the OSPF router
    	**type**\:   :py:class:`Ospfnbrtable <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfnbrtable>`
    
    .. attribute:: ospfstubareatable
    
    	The set of metrics that will be advertised by a default Area Border Router into a stub area
    	**type**\:   :py:class:`Ospfstubareatable <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfstubareatable>`
    
    .. attribute:: ospfvirtiftable
    
    	Information about this router's virtual interfaces that the OSPF Process is configured to carry on
    	**type**\:   :py:class:`Ospfvirtiftable <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfvirtiftable>`
    
    .. attribute:: ospfvirtlocallsdbtable
    
    	The OSPF Process's link\-local link state database for virtual links.  This table is identical to the OSPF LSDB Table in format, but contains only link\-local Link State Advertisements for virtual links.  The purpose is to allow link\-local LSAs to be displayed for each virtual interface.  This table is implemented to support type\-9 LSAs that are defined in 'The OSPF Opaque LSA Option'
    	**type**\:   :py:class:`Ospfvirtlocallsdbtable <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfvirtlocallsdbtable>`
    
    .. attribute:: ospfvirtnbrtable
    
    	This table describes all virtual neighbors. Since virtual links are configured in the Virtual Interface Table, this table is read\-only
    	**type**\:   :py:class:`Ospfvirtnbrtable <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfvirtnbrtable>`
    
    

    """

    _prefix = 'OSPF-MIB'
    _revision = '2006-11-10'

    def __init__(self):
        super(OspfMib, self).__init__()
        self._top_entity = None

        self.yang_name = "OSPF-MIB"
        self.yang_parent_name = "OSPF-MIB"

        self.ospfareaaggregatetable = OspfMib.Ospfareaaggregatetable()
        self.ospfareaaggregatetable.parent = self
        self._children_name_map["ospfareaaggregatetable"] = "ospfAreaAggregateTable"
        self._children_yang_names.add("ospfAreaAggregateTable")

        self.ospfarealsacounttable = OspfMib.Ospfarealsacounttable()
        self.ospfarealsacounttable.parent = self
        self._children_name_map["ospfarealsacounttable"] = "ospfAreaLsaCountTable"
        self._children_yang_names.add("ospfAreaLsaCountTable")

        self.ospfarearangetable = OspfMib.Ospfarearangetable()
        self.ospfarearangetable.parent = self
        self._children_name_map["ospfarearangetable"] = "ospfAreaRangeTable"
        self._children_yang_names.add("ospfAreaRangeTable")

        self.ospfareatable = OspfMib.Ospfareatable()
        self.ospfareatable.parent = self
        self._children_name_map["ospfareatable"] = "ospfAreaTable"
        self._children_yang_names.add("ospfAreaTable")

        self.ospfaslsdbtable = OspfMib.Ospfaslsdbtable()
        self.ospfaslsdbtable.parent = self
        self._children_name_map["ospfaslsdbtable"] = "ospfAsLsdbTable"
        self._children_yang_names.add("ospfAsLsdbTable")

        self.ospfextlsdbtable = OspfMib.Ospfextlsdbtable()
        self.ospfextlsdbtable.parent = self
        self._children_name_map["ospfextlsdbtable"] = "ospfExtLsdbTable"
        self._children_yang_names.add("ospfExtLsdbTable")

        self.ospfgeneralgroup = OspfMib.Ospfgeneralgroup()
        self.ospfgeneralgroup.parent = self
        self._children_name_map["ospfgeneralgroup"] = "ospfGeneralGroup"
        self._children_yang_names.add("ospfGeneralGroup")

        self.ospfhosttable = OspfMib.Ospfhosttable()
        self.ospfhosttable.parent = self
        self._children_name_map["ospfhosttable"] = "ospfHostTable"
        self._children_yang_names.add("ospfHostTable")

        self.ospfifmetrictable = OspfMib.Ospfifmetrictable()
        self.ospfifmetrictable.parent = self
        self._children_name_map["ospfifmetrictable"] = "ospfIfMetricTable"
        self._children_yang_names.add("ospfIfMetricTable")

        self.ospfiftable = OspfMib.Ospfiftable()
        self.ospfiftable.parent = self
        self._children_name_map["ospfiftable"] = "ospfIfTable"
        self._children_yang_names.add("ospfIfTable")

        self.ospflocallsdbtable = OspfMib.Ospflocallsdbtable()
        self.ospflocallsdbtable.parent = self
        self._children_name_map["ospflocallsdbtable"] = "ospfLocalLsdbTable"
        self._children_yang_names.add("ospfLocalLsdbTable")

        self.ospflsdbtable = OspfMib.Ospflsdbtable()
        self.ospflsdbtable.parent = self
        self._children_name_map["ospflsdbtable"] = "ospfLsdbTable"
        self._children_yang_names.add("ospfLsdbTable")

        self.ospfnbrtable = OspfMib.Ospfnbrtable()
        self.ospfnbrtable.parent = self
        self._children_name_map["ospfnbrtable"] = "ospfNbrTable"
        self._children_yang_names.add("ospfNbrTable")

        self.ospfstubareatable = OspfMib.Ospfstubareatable()
        self.ospfstubareatable.parent = self
        self._children_name_map["ospfstubareatable"] = "ospfStubAreaTable"
        self._children_yang_names.add("ospfStubAreaTable")

        self.ospfvirtiftable = OspfMib.Ospfvirtiftable()
        self.ospfvirtiftable.parent = self
        self._children_name_map["ospfvirtiftable"] = "ospfVirtIfTable"
        self._children_yang_names.add("ospfVirtIfTable")

        self.ospfvirtlocallsdbtable = OspfMib.Ospfvirtlocallsdbtable()
        self.ospfvirtlocallsdbtable.parent = self
        self._children_name_map["ospfvirtlocallsdbtable"] = "ospfVirtLocalLsdbTable"
        self._children_yang_names.add("ospfVirtLocalLsdbTable")

        self.ospfvirtnbrtable = OspfMib.Ospfvirtnbrtable()
        self.ospfvirtnbrtable.parent = self
        self._children_name_map["ospfvirtnbrtable"] = "ospfVirtNbrTable"
        self._children_yang_names.add("ospfVirtNbrTable")


    class Ospfgeneralgroup(Entity):
        """
        
        
        .. attribute:: ospfadminstat
        
        	The administrative status of OSPF in the router.  The value 'enabled' denotes that the OSPF Process is active on at least one interface; 'disabled' disables it on all interfaces.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\:   :py:class:`Status <ydk.models.cisco_ios_xe.OSPF_MIB.Status>`
        
        .. attribute:: ospfareabdrrtrstatus
        
        	A flag to note whether this router is an Area Border Router
        	**type**\:  bool
        
        .. attribute:: ospfasbdrrtrstatus
        
        	A flag to note whether this router is configured as an Autonomous System Border Router.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\:  bool
        
        .. attribute:: ospfaslsacksumsum
        
        	The 32\-bit unsigned sum of the LS checksums of the AS link state advertisements contained in the AS\-scope link state database.  This sum can be used to determine if there has been a change in a router's AS\-scope link state database, and to compare the AS\-scope link state database of two routers
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ospfaslsacount
        
        	The number of AS\-scope link state advertisements in the AS\-scope link state database
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ospfdemandextensions
        
        	The router's support for demand routing. This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\:  bool
        
        .. attribute:: ospfdiscontinuitytime
        
        	The value of sysUpTime on the most recent occasion at which any one of this MIB's counters suffered a discontinuity.  If no such discontinuities have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ospfexitoverflowinterval
        
        	The number of seconds that, after entering OverflowState, a router will attempt to leave OverflowState.  This allows the router to again originate non\-default AS\-external LSAs.  When set to 0, the router will not leave overflow state until restarted.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: ospfexternlsacksumsum
        
        	The 32\-bit sum of the LS checksums of the external link state advertisements contained in the link state database.  This sum can be used to determine if there has been a change in a router's link state database and to compare the link state database of two routers.  The value should be treated as unsigned when comparing two sums of checksums
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: ospfexternlsacount
        
        	The number of external (LS type\-5) link state advertisements in the link state database
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ospfextlsdblimit
        
        	The maximum number of non\-default AS\-external LSAs entries that can be stored in the link state database.  If the value is \-1, then there is no limit.  When the number of non\-default AS\-external LSAs in a router's link state database reaches ospfExtLsdbLimit, the router enters overflow state.  The router never holds more than ospfExtLsdbLimit non\-default AS\-external LSAs in its database.  OspfExtLsdbLimit MUST be set identically in all routers attached to the OSPF backbone and/or any regular OSPF area (i.e., OSPF stub areas and NSSAs are excluded).  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\:  int
        
        	**range:** \-1..2147483647
        
        .. attribute:: ospfmulticastextensions
        
        	A bit mask indicating whether the router is forwarding IP multicast (Class D) datagrams based on the algorithms defined in the multicast extensions to OSPF.  Bit 0, if set, indicates that the router can  forward IP multicast datagrams in the router's directly attached areas (called intra\-area multicast routing).  Bit 1, if set, indicates that the router can forward IP multicast datagrams between OSPF areas (called inter\-area multicast routing).  Bit 2, if set, indicates that the router can forward IP multicast datagrams between Autonomous Systems (called inter\-AS multicast routing).  Only certain combinations of bit settings are allowed, namely\: 0 (no multicast forwarding is enabled), 1 (intra\-area multicasting only), 3 (intra\-area and inter\-area multicasting), 5 (intra\-area and inter\-AS multicasting), and 7 (multicasting everywhere).  By default, no multicast forwarding is enabled.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: ospfopaquelsasupport
        
        	The router's support for Opaque LSA types
        	**type**\:  bool
        
        .. attribute:: ospforiginatenewlsas
        
        	The number of new link state advertisements that have been originated.  This number is incremented each time the router originates a new LSA.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ospfDiscontinuityTime
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ospfreferencebandwidth
        
        	Reference bandwidth in kilobits/second for  calculating default interface metrics.  The default value is 100,000 KBPS (100 MBPS).  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: kilobits per second
        
        .. attribute:: ospfrestartage
        
        	Remaining time in current OSPF graceful restart interval
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: seconds
        
        .. attribute:: ospfrestartexitreason
        
        	Describes the outcome of the last attempt at a graceful restart.  If the value is 'none', no restart has yet been attempted.  If the value is 'inProgress', a restart attempt is currently underway
        	**type**\:   :py:class:`Ospfrestartexitreason <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfgeneralgroup.Ospfrestartexitreason>`
        
        .. attribute:: ospfrestartinterval
        
        	Configured OSPF graceful restart timeout interval.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\:  int
        
        	**range:** 1..1800
        
        	**units**\: seconds
        
        .. attribute:: ospfrestartstatus
        
        	Current status of OSPF graceful restart
        	**type**\:   :py:class:`Ospfrestartstatus <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfgeneralgroup.Ospfrestartstatus>`
        
        .. attribute:: ospfrestartstrictlsachecking
        
        	Indicates if strict LSA checking is enabled for graceful restart.  This object is persistent and when written the entity SHOULD save the change to non\-volatile  storage
        	**type**\:  bool
        
        .. attribute:: ospfrestartsupport
        
        	The router's support for OSPF graceful restart. Options include\: no restart support, only planned restarts, or both planned and unplanned restarts.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\:   :py:class:`Ospfrestartsupport <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfgeneralgroup.Ospfrestartsupport>`
        
        .. attribute:: ospfrfc1583compatibility
        
        	Indicates metrics used to choose among multiple AS\-external LSAs.  When RFC1583Compatibility is set to enabled, only cost will be used when choosing among multiple AS\-external LSAs advertising the same destination.  When RFC1583Compatibility is set to disabled, preference will be driven first by type of path using cost only to break ties.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\:  bool
        
        .. attribute:: ospfrouterid
        
        	A 32\-bit integer uniquely identifying the router in the Autonomous System. By convention, to ensure uniqueness, this should default to the value of one of the router's IP interface addresses.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: ospfrxnewlsas
        
        	The number of link state advertisements received that are determined to be new instantiations. This number does not include newer instantiations of self\-originated link state advertisements.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ospfDiscontinuityTime
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ospfstubrouteradvertisement
        
        	This object controls the advertisement of stub router LSAs by the router.  The value doNotAdvertise will result in the advertisement of a standard router LSA and is the default value.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\:   :py:class:`Ospfstubrouteradvertisement <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfgeneralgroup.Ospfstubrouteradvertisement>`
        
        .. attribute:: ospfstubroutersupport
        
        	The router's support for stub router functionality
        	**type**\:  bool
        
        .. attribute:: ospftossupport
        
        	The router's support for type\-of\-service routing.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\:  bool
        
        .. attribute:: ospfversionnumber
        
        	The current version number of the OSPF protocol is 2
        	**type**\:   :py:class:`Ospfversionnumber <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfgeneralgroup.Ospfversionnumber>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OspfMib.Ospfgeneralgroup, self).__init__()

            self.yang_name = "ospfGeneralGroup"
            self.yang_parent_name = "OSPF-MIB"

            self.ospfadminstat = YLeaf(YType.enumeration, "ospfAdminStat")

            self.ospfareabdrrtrstatus = YLeaf(YType.boolean, "ospfAreaBdrRtrStatus")

            self.ospfasbdrrtrstatus = YLeaf(YType.boolean, "ospfASBdrRtrStatus")

            self.ospfaslsacksumsum = YLeaf(YType.uint32, "ospfAsLsaCksumSum")

            self.ospfaslsacount = YLeaf(YType.uint32, "ospfAsLsaCount")

            self.ospfdemandextensions = YLeaf(YType.boolean, "ospfDemandExtensions")

            self.ospfdiscontinuitytime = YLeaf(YType.uint32, "ospfDiscontinuityTime")

            self.ospfexitoverflowinterval = YLeaf(YType.int32, "ospfExitOverflowInterval")

            self.ospfexternlsacksumsum = YLeaf(YType.int32, "ospfExternLsaCksumSum")

            self.ospfexternlsacount = YLeaf(YType.uint32, "ospfExternLsaCount")

            self.ospfextlsdblimit = YLeaf(YType.int32, "ospfExtLsdbLimit")

            self.ospfmulticastextensions = YLeaf(YType.int32, "ospfMulticastExtensions")

            self.ospfopaquelsasupport = YLeaf(YType.boolean, "ospfOpaqueLsaSupport")

            self.ospforiginatenewlsas = YLeaf(YType.uint32, "ospfOriginateNewLsas")

            self.ospfreferencebandwidth = YLeaf(YType.uint32, "ospfReferenceBandwidth")

            self.ospfrestartage = YLeaf(YType.uint32, "ospfRestartAge")

            self.ospfrestartexitreason = YLeaf(YType.enumeration, "ospfRestartExitReason")

            self.ospfrestartinterval = YLeaf(YType.int32, "ospfRestartInterval")

            self.ospfrestartstatus = YLeaf(YType.enumeration, "ospfRestartStatus")

            self.ospfrestartstrictlsachecking = YLeaf(YType.boolean, "ospfRestartStrictLsaChecking")

            self.ospfrestartsupport = YLeaf(YType.enumeration, "ospfRestartSupport")

            self.ospfrfc1583compatibility = YLeaf(YType.boolean, "ospfRFC1583Compatibility")

            self.ospfrouterid = YLeaf(YType.str, "ospfRouterId")

            self.ospfrxnewlsas = YLeaf(YType.uint32, "ospfRxNewLsas")

            self.ospfstubrouteradvertisement = YLeaf(YType.enumeration, "ospfStubRouterAdvertisement")

            self.ospfstubroutersupport = YLeaf(YType.boolean, "ospfStubRouterSupport")

            self.ospftossupport = YLeaf(YType.boolean, "ospfTOSSupport")

            self.ospfversionnumber = YLeaf(YType.enumeration, "ospfVersionNumber")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ospfadminstat",
                            "ospfareabdrrtrstatus",
                            "ospfasbdrrtrstatus",
                            "ospfaslsacksumsum",
                            "ospfaslsacount",
                            "ospfdemandextensions",
                            "ospfdiscontinuitytime",
                            "ospfexitoverflowinterval",
                            "ospfexternlsacksumsum",
                            "ospfexternlsacount",
                            "ospfextlsdblimit",
                            "ospfmulticastextensions",
                            "ospfopaquelsasupport",
                            "ospforiginatenewlsas",
                            "ospfreferencebandwidth",
                            "ospfrestartage",
                            "ospfrestartexitreason",
                            "ospfrestartinterval",
                            "ospfrestartstatus",
                            "ospfrestartstrictlsachecking",
                            "ospfrestartsupport",
                            "ospfrfc1583compatibility",
                            "ospfrouterid",
                            "ospfrxnewlsas",
                            "ospfstubrouteradvertisement",
                            "ospfstubroutersupport",
                            "ospftossupport",
                            "ospfversionnumber") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(OspfMib.Ospfgeneralgroup, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(OspfMib.Ospfgeneralgroup, self).__setattr__(name, value)

        class Ospfrestartexitreason(Enum):
            """
            Ospfrestartexitreason

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
            Ospfrestartstatus

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
            Ospfrestartsupport

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
            Ospfstubrouteradvertisement

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
            Ospfversionnumber

            The current version number of the OSPF protocol is 2.

            .. data:: version2 = 2

            """

            version2 = Enum.YLeaf(2, "version2")


        def has_data(self):
            return (
                self.ospfadminstat.is_set or
                self.ospfareabdrrtrstatus.is_set or
                self.ospfasbdrrtrstatus.is_set or
                self.ospfaslsacksumsum.is_set or
                self.ospfaslsacount.is_set or
                self.ospfdemandextensions.is_set or
                self.ospfdiscontinuitytime.is_set or
                self.ospfexitoverflowinterval.is_set or
                self.ospfexternlsacksumsum.is_set or
                self.ospfexternlsacount.is_set or
                self.ospfextlsdblimit.is_set or
                self.ospfmulticastextensions.is_set or
                self.ospfopaquelsasupport.is_set or
                self.ospforiginatenewlsas.is_set or
                self.ospfreferencebandwidth.is_set or
                self.ospfrestartage.is_set or
                self.ospfrestartexitreason.is_set or
                self.ospfrestartinterval.is_set or
                self.ospfrestartstatus.is_set or
                self.ospfrestartstrictlsachecking.is_set or
                self.ospfrestartsupport.is_set or
                self.ospfrfc1583compatibility.is_set or
                self.ospfrouterid.is_set or
                self.ospfrxnewlsas.is_set or
                self.ospfstubrouteradvertisement.is_set or
                self.ospfstubroutersupport.is_set or
                self.ospftossupport.is_set or
                self.ospfversionnumber.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ospfadminstat.yfilter != YFilter.not_set or
                self.ospfareabdrrtrstatus.yfilter != YFilter.not_set or
                self.ospfasbdrrtrstatus.yfilter != YFilter.not_set or
                self.ospfaslsacksumsum.yfilter != YFilter.not_set or
                self.ospfaslsacount.yfilter != YFilter.not_set or
                self.ospfdemandextensions.yfilter != YFilter.not_set or
                self.ospfdiscontinuitytime.yfilter != YFilter.not_set or
                self.ospfexitoverflowinterval.yfilter != YFilter.not_set or
                self.ospfexternlsacksumsum.yfilter != YFilter.not_set or
                self.ospfexternlsacount.yfilter != YFilter.not_set or
                self.ospfextlsdblimit.yfilter != YFilter.not_set or
                self.ospfmulticastextensions.yfilter != YFilter.not_set or
                self.ospfopaquelsasupport.yfilter != YFilter.not_set or
                self.ospforiginatenewlsas.yfilter != YFilter.not_set or
                self.ospfreferencebandwidth.yfilter != YFilter.not_set or
                self.ospfrestartage.yfilter != YFilter.not_set or
                self.ospfrestartexitreason.yfilter != YFilter.not_set or
                self.ospfrestartinterval.yfilter != YFilter.not_set or
                self.ospfrestartstatus.yfilter != YFilter.not_set or
                self.ospfrestartstrictlsachecking.yfilter != YFilter.not_set or
                self.ospfrestartsupport.yfilter != YFilter.not_set or
                self.ospfrfc1583compatibility.yfilter != YFilter.not_set or
                self.ospfrouterid.yfilter != YFilter.not_set or
                self.ospfrxnewlsas.yfilter != YFilter.not_set or
                self.ospfstubrouteradvertisement.yfilter != YFilter.not_set or
                self.ospfstubroutersupport.yfilter != YFilter.not_set or
                self.ospftossupport.yfilter != YFilter.not_set or
                self.ospfversionnumber.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ospfGeneralGroup" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "OSPF-MIB:OSPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ospfadminstat.is_set or self.ospfadminstat.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfadminstat.get_name_leafdata())
            if (self.ospfareabdrrtrstatus.is_set or self.ospfareabdrrtrstatus.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfareabdrrtrstatus.get_name_leafdata())
            if (self.ospfasbdrrtrstatus.is_set or self.ospfasbdrrtrstatus.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfasbdrrtrstatus.get_name_leafdata())
            if (self.ospfaslsacksumsum.is_set or self.ospfaslsacksumsum.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfaslsacksumsum.get_name_leafdata())
            if (self.ospfaslsacount.is_set or self.ospfaslsacount.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfaslsacount.get_name_leafdata())
            if (self.ospfdemandextensions.is_set or self.ospfdemandextensions.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfdemandextensions.get_name_leafdata())
            if (self.ospfdiscontinuitytime.is_set or self.ospfdiscontinuitytime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfdiscontinuitytime.get_name_leafdata())
            if (self.ospfexitoverflowinterval.is_set or self.ospfexitoverflowinterval.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfexitoverflowinterval.get_name_leafdata())
            if (self.ospfexternlsacksumsum.is_set or self.ospfexternlsacksumsum.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfexternlsacksumsum.get_name_leafdata())
            if (self.ospfexternlsacount.is_set or self.ospfexternlsacount.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfexternlsacount.get_name_leafdata())
            if (self.ospfextlsdblimit.is_set or self.ospfextlsdblimit.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfextlsdblimit.get_name_leafdata())
            if (self.ospfmulticastextensions.is_set or self.ospfmulticastextensions.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfmulticastextensions.get_name_leafdata())
            if (self.ospfopaquelsasupport.is_set or self.ospfopaquelsasupport.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfopaquelsasupport.get_name_leafdata())
            if (self.ospforiginatenewlsas.is_set or self.ospforiginatenewlsas.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospforiginatenewlsas.get_name_leafdata())
            if (self.ospfreferencebandwidth.is_set or self.ospfreferencebandwidth.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfreferencebandwidth.get_name_leafdata())
            if (self.ospfrestartage.is_set or self.ospfrestartage.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfrestartage.get_name_leafdata())
            if (self.ospfrestartexitreason.is_set or self.ospfrestartexitreason.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfrestartexitreason.get_name_leafdata())
            if (self.ospfrestartinterval.is_set or self.ospfrestartinterval.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfrestartinterval.get_name_leafdata())
            if (self.ospfrestartstatus.is_set or self.ospfrestartstatus.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfrestartstatus.get_name_leafdata())
            if (self.ospfrestartstrictlsachecking.is_set or self.ospfrestartstrictlsachecking.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfrestartstrictlsachecking.get_name_leafdata())
            if (self.ospfrestartsupport.is_set or self.ospfrestartsupport.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfrestartsupport.get_name_leafdata())
            if (self.ospfrfc1583compatibility.is_set or self.ospfrfc1583compatibility.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfrfc1583compatibility.get_name_leafdata())
            if (self.ospfrouterid.is_set or self.ospfrouterid.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfrouterid.get_name_leafdata())
            if (self.ospfrxnewlsas.is_set or self.ospfrxnewlsas.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfrxnewlsas.get_name_leafdata())
            if (self.ospfstubrouteradvertisement.is_set or self.ospfstubrouteradvertisement.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfstubrouteradvertisement.get_name_leafdata())
            if (self.ospfstubroutersupport.is_set or self.ospfstubroutersupport.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfstubroutersupport.get_name_leafdata())
            if (self.ospftossupport.is_set or self.ospftossupport.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospftossupport.get_name_leafdata())
            if (self.ospfversionnumber.is_set or self.ospfversionnumber.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfversionnumber.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ospfAdminStat" or name == "ospfAreaBdrRtrStatus" or name == "ospfASBdrRtrStatus" or name == "ospfAsLsaCksumSum" or name == "ospfAsLsaCount" or name == "ospfDemandExtensions" or name == "ospfDiscontinuityTime" or name == "ospfExitOverflowInterval" or name == "ospfExternLsaCksumSum" or name == "ospfExternLsaCount" or name == "ospfExtLsdbLimit" or name == "ospfMulticastExtensions" or name == "ospfOpaqueLsaSupport" or name == "ospfOriginateNewLsas" or name == "ospfReferenceBandwidth" or name == "ospfRestartAge" or name == "ospfRestartExitReason" or name == "ospfRestartInterval" or name == "ospfRestartStatus" or name == "ospfRestartStrictLsaChecking" or name == "ospfRestartSupport" or name == "ospfRFC1583Compatibility" or name == "ospfRouterId" or name == "ospfRxNewLsas" or name == "ospfStubRouterAdvertisement" or name == "ospfStubRouterSupport" or name == "ospfTOSSupport" or name == "ospfVersionNumber"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ospfAdminStat"):
                self.ospfadminstat = value
                self.ospfadminstat.value_namespace = name_space
                self.ospfadminstat.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfAreaBdrRtrStatus"):
                self.ospfareabdrrtrstatus = value
                self.ospfareabdrrtrstatus.value_namespace = name_space
                self.ospfareabdrrtrstatus.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfASBdrRtrStatus"):
                self.ospfasbdrrtrstatus = value
                self.ospfasbdrrtrstatus.value_namespace = name_space
                self.ospfasbdrrtrstatus.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfAsLsaCksumSum"):
                self.ospfaslsacksumsum = value
                self.ospfaslsacksumsum.value_namespace = name_space
                self.ospfaslsacksumsum.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfAsLsaCount"):
                self.ospfaslsacount = value
                self.ospfaslsacount.value_namespace = name_space
                self.ospfaslsacount.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfDemandExtensions"):
                self.ospfdemandextensions = value
                self.ospfdemandextensions.value_namespace = name_space
                self.ospfdemandextensions.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfDiscontinuityTime"):
                self.ospfdiscontinuitytime = value
                self.ospfdiscontinuitytime.value_namespace = name_space
                self.ospfdiscontinuitytime.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfExitOverflowInterval"):
                self.ospfexitoverflowinterval = value
                self.ospfexitoverflowinterval.value_namespace = name_space
                self.ospfexitoverflowinterval.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfExternLsaCksumSum"):
                self.ospfexternlsacksumsum = value
                self.ospfexternlsacksumsum.value_namespace = name_space
                self.ospfexternlsacksumsum.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfExternLsaCount"):
                self.ospfexternlsacount = value
                self.ospfexternlsacount.value_namespace = name_space
                self.ospfexternlsacount.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfExtLsdbLimit"):
                self.ospfextlsdblimit = value
                self.ospfextlsdblimit.value_namespace = name_space
                self.ospfextlsdblimit.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfMulticastExtensions"):
                self.ospfmulticastextensions = value
                self.ospfmulticastextensions.value_namespace = name_space
                self.ospfmulticastextensions.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfOpaqueLsaSupport"):
                self.ospfopaquelsasupport = value
                self.ospfopaquelsasupport.value_namespace = name_space
                self.ospfopaquelsasupport.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfOriginateNewLsas"):
                self.ospforiginatenewlsas = value
                self.ospforiginatenewlsas.value_namespace = name_space
                self.ospforiginatenewlsas.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfReferenceBandwidth"):
                self.ospfreferencebandwidth = value
                self.ospfreferencebandwidth.value_namespace = name_space
                self.ospfreferencebandwidth.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfRestartAge"):
                self.ospfrestartage = value
                self.ospfrestartage.value_namespace = name_space
                self.ospfrestartage.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfRestartExitReason"):
                self.ospfrestartexitreason = value
                self.ospfrestartexitreason.value_namespace = name_space
                self.ospfrestartexitreason.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfRestartInterval"):
                self.ospfrestartinterval = value
                self.ospfrestartinterval.value_namespace = name_space
                self.ospfrestartinterval.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfRestartStatus"):
                self.ospfrestartstatus = value
                self.ospfrestartstatus.value_namespace = name_space
                self.ospfrestartstatus.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfRestartStrictLsaChecking"):
                self.ospfrestartstrictlsachecking = value
                self.ospfrestartstrictlsachecking.value_namespace = name_space
                self.ospfrestartstrictlsachecking.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfRestartSupport"):
                self.ospfrestartsupport = value
                self.ospfrestartsupport.value_namespace = name_space
                self.ospfrestartsupport.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfRFC1583Compatibility"):
                self.ospfrfc1583compatibility = value
                self.ospfrfc1583compatibility.value_namespace = name_space
                self.ospfrfc1583compatibility.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfRouterId"):
                self.ospfrouterid = value
                self.ospfrouterid.value_namespace = name_space
                self.ospfrouterid.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfRxNewLsas"):
                self.ospfrxnewlsas = value
                self.ospfrxnewlsas.value_namespace = name_space
                self.ospfrxnewlsas.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfStubRouterAdvertisement"):
                self.ospfstubrouteradvertisement = value
                self.ospfstubrouteradvertisement.value_namespace = name_space
                self.ospfstubrouteradvertisement.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfStubRouterSupport"):
                self.ospfstubroutersupport = value
                self.ospfstubroutersupport.value_namespace = name_space
                self.ospfstubroutersupport.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfTOSSupport"):
                self.ospftossupport = value
                self.ospftossupport.value_namespace = name_space
                self.ospftossupport.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfVersionNumber"):
                self.ospfversionnumber = value
                self.ospfversionnumber.value_namespace = name_space
                self.ospfversionnumber.value_namespace_prefix = name_space_prefix


    class Ospfareatable(Entity):
        """
        Information describing the configured parameters and
        cumulative statistics of the router's attached areas.
        The interfaces and virtual links are configured
        as part of these areas.  Area 0.0.0.0, by definition,
        is the backbone area.
        
        .. attribute:: ospfareaentry
        
        	Information describing the configured parameters and cumulative statistics of one of the router's attached areas. The interfaces and virtual links are configured as part of these areas.  Area 0.0.0.0, by definition, is the backbone area.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile storage
        	**type**\: list of    :py:class:`Ospfareaentry <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfareatable.Ospfareaentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OspfMib.Ospfareatable, self).__init__()

            self.yang_name = "ospfAreaTable"
            self.yang_parent_name = "OSPF-MIB"

            self.ospfareaentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(OspfMib.Ospfareatable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(OspfMib.Ospfareatable, self).__setattr__(name, value)


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
            
            .. attribute:: ospfareaid  <key>
            
            	A 32\-bit integer uniquely identifying an area. Area ID 0.0.0.0 is used for the OSPF backbone
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfareanssatranslatorevents
            
            	Indicates the number of Translator State changes that have occurred since the last boot\-up
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfareanssatranslatorrole
            
            	Indicates an NSSA Border router's ability to perform NSSA translation of type\-7 LSAs into type\-5 LSAs
            	**type**\:   :py:class:`Cospfareanssatranslatorrole <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfareatable.Ospfareaentry.Cospfareanssatranslatorrole>`
            
            .. attribute:: cospfareanssatranslatorstate
            
            	Indicates if and how an NSSA Border router is performing NSSA translation of type\-7 LSAs into type\-5 LSAs. When this object set to enabled, the NSSA Border router's cospfAreaNssaExtTranslatorRole has been set to always. When this object is set to elected, a candidate NSSA Border router is Translating type\-7 LSAs into type\-5. When this object is set to disabled, a candidate NSSA Border router is NOT translating type\-7 LSAs into type\-5
            	**type**\:   :py:class:`Cospfareanssatranslatorstate <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfareatable.Ospfareaentry.Cospfareanssatranslatorstate>`
            
            .. attribute:: cospfopaquearealsacksumsum
            
            	The 32\-bit unsigned sum of the Opaque Area and AS  link\-state advertisements' LS checksums contained  link state database of this area.  The sum can be  used to determine if there has been a change in the  link state database for Opaque Area and AS link\-state advertisements
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfopaquearealsacount
            
            	The total number of Opaque Area and AS link\-state  advertisements in the link state database of this area
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfareabdrrtrcount
            
            	The total number of Area Border Routers reachable within this area.  This is initially zero and is calculated in each Shortest Path First (SPF) pass
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfarealsacksumsum
            
            	The 32\-bit sum of the link state advertisements' LS checksums contained in this area's link state database.  This sum excludes external (LS type\-5) link state advertisements. The sum can be used to determine if there has been a change in a router's link state database, and to compare the link state database of two routers.  The value should be treated as unsigned when comparing two sums of checksums
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospfarealsacount
            
            	The total number of link state advertisements in this area's link state database, excluding AS\-external LSAs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfareanssatranslatorevents
            
            	Indicates the number of translator state changes that have occurred since the last boot\-up.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ospfDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfareanssatranslatorrole
            
            	Indicates an NSSA border router's ability to perform NSSA translation of type\-7 LSAs into type\-5 LSAs
            	**type**\:   :py:class:`Ospfareanssatranslatorrole <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfareatable.Ospfareaentry.Ospfareanssatranslatorrole>`
            
            .. attribute:: ospfareanssatranslatorstabilityinterval
            
            	The number of seconds after an elected translator determines its services are no longer required, that it should continue to perform its translation duties
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: ospfareanssatranslatorstate
            
            	Indicates if and how an NSSA border router is performing NSSA translation of type\-7 LSAs into type\-5  LSAs.  When this object is set to enabled, the NSSA Border router's OspfAreaNssaExtTranslatorRole has been set to always.  When this object is set to elected, a candidate NSSA Border router is Translating type\-7 LSAs into type\-5. When this object is set to disabled, a candidate NSSA border router is NOT translating type\-7 LSAs into type\-5
            	**type**\:   :py:class:`Ospfareanssatranslatorstate <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfareatable.Ospfareaentry.Ospfareanssatranslatorstate>`
            
            .. attribute:: ospfareastatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: ospfareasummary
            
            	The variable ospfAreaSummary controls the import of summary LSAs into stub and NSSA areas. It has no effect on other areas.  If it is noAreaSummary, the router will not originate summary LSAs into the stub or NSSA area. It will rely entirely on its default route.  If it is sendAreaSummary, the router will both summarize and propagate summary LSAs
            	**type**\:   :py:class:`Ospfareasummary <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfareatable.Ospfareaentry.Ospfareasummary>`
            
            .. attribute:: ospfasbdrrtrcount
            
            	The total number of Autonomous System Border Routers reachable within this area.  This is initially zero and is calculated in each SPF pass
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfauthtype
            
            	The authentication type specified for an area
            	**type**\:   :py:class:`Ospfauthenticationtype <ydk.models.cisco_ios_xe.OSPF_MIB.Ospfauthenticationtype>`
            
            	**status**\: obsolete
            
            .. attribute:: ospfimportasextern
            
            	Indicates if an area is a stub area, NSSA, or standard area.  Type\-5 AS\-external LSAs and type\-11 Opaque LSAs are not imported into stub areas or NSSAs.  NSSAs import AS\-external data as type\-7 LSAs
            	**type**\:   :py:class:`Ospfimportasextern <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfareatable.Ospfareaentry.Ospfimportasextern>`
            
            .. attribute:: ospfspfruns
            
            	The number of times that the intra\-area route table has been calculated using this area's link state database.  This is typically done using Dijkstra's algorithm.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ospfDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OspfMib.Ospfareatable.Ospfareaentry, self).__init__()

                self.yang_name = "ospfAreaEntry"
                self.yang_parent_name = "ospfAreaTable"

                self.ospfareaid = YLeaf(YType.str, "ospfAreaId")

                self.cospfareanssatranslatorevents = YLeaf(YType.uint32, "CISCO-OSPF-MIB:cospfAreaNssaTranslatorEvents")

                self.cospfareanssatranslatorrole = YLeaf(YType.enumeration, "CISCO-OSPF-MIB:cospfAreaNssaTranslatorRole")

                self.cospfareanssatranslatorstate = YLeaf(YType.enumeration, "CISCO-OSPF-MIB:cospfAreaNssaTranslatorState")

                self.cospfopaquearealsacksumsum = YLeaf(YType.uint32, "CISCO-OSPF-MIB:cospfOpaqueAreaLsaCksumSum")

                self.cospfopaquearealsacount = YLeaf(YType.uint32, "CISCO-OSPF-MIB:cospfOpaqueAreaLsaCount")

                self.ospfareabdrrtrcount = YLeaf(YType.uint32, "ospfAreaBdrRtrCount")

                self.ospfarealsacksumsum = YLeaf(YType.int32, "ospfAreaLsaCksumSum")

                self.ospfarealsacount = YLeaf(YType.uint32, "ospfAreaLsaCount")

                self.ospfareanssatranslatorevents = YLeaf(YType.uint32, "ospfAreaNssaTranslatorEvents")

                self.ospfareanssatranslatorrole = YLeaf(YType.enumeration, "ospfAreaNssaTranslatorRole")

                self.ospfareanssatranslatorstabilityinterval = YLeaf(YType.int32, "ospfAreaNssaTranslatorStabilityInterval")

                self.ospfareanssatranslatorstate = YLeaf(YType.enumeration, "ospfAreaNssaTranslatorState")

                self.ospfareastatus = YLeaf(YType.enumeration, "ospfAreaStatus")

                self.ospfareasummary = YLeaf(YType.enumeration, "ospfAreaSummary")

                self.ospfasbdrrtrcount = YLeaf(YType.uint32, "ospfAsBdrRtrCount")

                self.ospfauthtype = YLeaf(YType.enumeration, "ospfAuthType")

                self.ospfimportasextern = YLeaf(YType.enumeration, "ospfImportAsExtern")

                self.ospfspfruns = YLeaf(YType.uint32, "ospfSpfRuns")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ospfareaid",
                                "cospfareanssatranslatorevents",
                                "cospfareanssatranslatorrole",
                                "cospfareanssatranslatorstate",
                                "cospfopaquearealsacksumsum",
                                "cospfopaquearealsacount",
                                "ospfareabdrrtrcount",
                                "ospfarealsacksumsum",
                                "ospfarealsacount",
                                "ospfareanssatranslatorevents",
                                "ospfareanssatranslatorrole",
                                "ospfareanssatranslatorstabilityinterval",
                                "ospfareanssatranslatorstate",
                                "ospfareastatus",
                                "ospfareasummary",
                                "ospfasbdrrtrcount",
                                "ospfauthtype",
                                "ospfimportasextern",
                                "ospfspfruns") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(OspfMib.Ospfareatable.Ospfareaentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(OspfMib.Ospfareatable.Ospfareaentry, self).__setattr__(name, value)

            class Cospfareanssatranslatorrole(Enum):
                """
                Cospfareanssatranslatorrole

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
                Cospfareanssatranslatorstate

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
                Ospfareanssatranslatorrole

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
                Ospfareanssatranslatorstate

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
                Ospfareasummary

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
                Ospfimportasextern

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


            def has_data(self):
                return (
                    self.ospfareaid.is_set or
                    self.cospfareanssatranslatorevents.is_set or
                    self.cospfareanssatranslatorrole.is_set or
                    self.cospfareanssatranslatorstate.is_set or
                    self.cospfopaquearealsacksumsum.is_set or
                    self.cospfopaquearealsacount.is_set or
                    self.ospfareabdrrtrcount.is_set or
                    self.ospfarealsacksumsum.is_set or
                    self.ospfarealsacount.is_set or
                    self.ospfareanssatranslatorevents.is_set or
                    self.ospfareanssatranslatorrole.is_set or
                    self.ospfareanssatranslatorstabilityinterval.is_set or
                    self.ospfareanssatranslatorstate.is_set or
                    self.ospfareastatus.is_set or
                    self.ospfareasummary.is_set or
                    self.ospfasbdrrtrcount.is_set or
                    self.ospfauthtype.is_set or
                    self.ospfimportasextern.is_set or
                    self.ospfspfruns.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ospfareaid.yfilter != YFilter.not_set or
                    self.cospfareanssatranslatorevents.yfilter != YFilter.not_set or
                    self.cospfareanssatranslatorrole.yfilter != YFilter.not_set or
                    self.cospfareanssatranslatorstate.yfilter != YFilter.not_set or
                    self.cospfopaquearealsacksumsum.yfilter != YFilter.not_set or
                    self.cospfopaquearealsacount.yfilter != YFilter.not_set or
                    self.ospfareabdrrtrcount.yfilter != YFilter.not_set or
                    self.ospfarealsacksumsum.yfilter != YFilter.not_set or
                    self.ospfarealsacount.yfilter != YFilter.not_set or
                    self.ospfareanssatranslatorevents.yfilter != YFilter.not_set or
                    self.ospfareanssatranslatorrole.yfilter != YFilter.not_set or
                    self.ospfareanssatranslatorstabilityinterval.yfilter != YFilter.not_set or
                    self.ospfareanssatranslatorstate.yfilter != YFilter.not_set or
                    self.ospfareastatus.yfilter != YFilter.not_set or
                    self.ospfareasummary.yfilter != YFilter.not_set or
                    self.ospfasbdrrtrcount.yfilter != YFilter.not_set or
                    self.ospfauthtype.yfilter != YFilter.not_set or
                    self.ospfimportasextern.yfilter != YFilter.not_set or
                    self.ospfspfruns.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ospfAreaEntry" + "[ospfAreaId='" + self.ospfareaid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "OSPF-MIB:OSPF-MIB/ospfAreaTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ospfareaid.is_set or self.ospfareaid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfareaid.get_name_leafdata())
                if (self.cospfareanssatranslatorevents.is_set or self.cospfareanssatranslatorevents.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfareanssatranslatorevents.get_name_leafdata())
                if (self.cospfareanssatranslatorrole.is_set or self.cospfareanssatranslatorrole.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfareanssatranslatorrole.get_name_leafdata())
                if (self.cospfareanssatranslatorstate.is_set or self.cospfareanssatranslatorstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfareanssatranslatorstate.get_name_leafdata())
                if (self.cospfopaquearealsacksumsum.is_set or self.cospfopaquearealsacksumsum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfopaquearealsacksumsum.get_name_leafdata())
                if (self.cospfopaquearealsacount.is_set or self.cospfopaquearealsacount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfopaquearealsacount.get_name_leafdata())
                if (self.ospfareabdrrtrcount.is_set or self.ospfareabdrrtrcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfareabdrrtrcount.get_name_leafdata())
                if (self.ospfarealsacksumsum.is_set or self.ospfarealsacksumsum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfarealsacksumsum.get_name_leafdata())
                if (self.ospfarealsacount.is_set or self.ospfarealsacount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfarealsacount.get_name_leafdata())
                if (self.ospfareanssatranslatorevents.is_set or self.ospfareanssatranslatorevents.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfareanssatranslatorevents.get_name_leafdata())
                if (self.ospfareanssatranslatorrole.is_set or self.ospfareanssatranslatorrole.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfareanssatranslatorrole.get_name_leafdata())
                if (self.ospfareanssatranslatorstabilityinterval.is_set or self.ospfareanssatranslatorstabilityinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfareanssatranslatorstabilityinterval.get_name_leafdata())
                if (self.ospfareanssatranslatorstate.is_set or self.ospfareanssatranslatorstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfareanssatranslatorstate.get_name_leafdata())
                if (self.ospfareastatus.is_set or self.ospfareastatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfareastatus.get_name_leafdata())
                if (self.ospfareasummary.is_set or self.ospfareasummary.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfareasummary.get_name_leafdata())
                if (self.ospfasbdrrtrcount.is_set or self.ospfasbdrrtrcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfasbdrrtrcount.get_name_leafdata())
                if (self.ospfauthtype.is_set or self.ospfauthtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfauthtype.get_name_leafdata())
                if (self.ospfimportasextern.is_set or self.ospfimportasextern.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfimportasextern.get_name_leafdata())
                if (self.ospfspfruns.is_set or self.ospfspfruns.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfspfruns.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ospfAreaId" or name == "cospfAreaNssaTranslatorEvents" or name == "cospfAreaNssaTranslatorRole" or name == "cospfAreaNssaTranslatorState" or name == "cospfOpaqueAreaLsaCksumSum" or name == "cospfOpaqueAreaLsaCount" or name == "ospfAreaBdrRtrCount" or name == "ospfAreaLsaCksumSum" or name == "ospfAreaLsaCount" or name == "ospfAreaNssaTranslatorEvents" or name == "ospfAreaNssaTranslatorRole" or name == "ospfAreaNssaTranslatorStabilityInterval" or name == "ospfAreaNssaTranslatorState" or name == "ospfAreaStatus" or name == "ospfAreaSummary" or name == "ospfAsBdrRtrCount" or name == "ospfAuthType" or name == "ospfImportAsExtern" or name == "ospfSpfRuns"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ospfAreaId"):
                    self.ospfareaid = value
                    self.ospfareaid.value_namespace = name_space
                    self.ospfareaid.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfAreaNssaTranslatorEvents"):
                    self.cospfareanssatranslatorevents = value
                    self.cospfareanssatranslatorevents.value_namespace = name_space
                    self.cospfareanssatranslatorevents.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfAreaNssaTranslatorRole"):
                    self.cospfareanssatranslatorrole = value
                    self.cospfareanssatranslatorrole.value_namespace = name_space
                    self.cospfareanssatranslatorrole.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfAreaNssaTranslatorState"):
                    self.cospfareanssatranslatorstate = value
                    self.cospfareanssatranslatorstate.value_namespace = name_space
                    self.cospfareanssatranslatorstate.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfOpaqueAreaLsaCksumSum"):
                    self.cospfopaquearealsacksumsum = value
                    self.cospfopaquearealsacksumsum.value_namespace = name_space
                    self.cospfopaquearealsacksumsum.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfOpaqueAreaLsaCount"):
                    self.cospfopaquearealsacount = value
                    self.cospfopaquearealsacount.value_namespace = name_space
                    self.cospfopaquearealsacount.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAreaBdrRtrCount"):
                    self.ospfareabdrrtrcount = value
                    self.ospfareabdrrtrcount.value_namespace = name_space
                    self.ospfareabdrrtrcount.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAreaLsaCksumSum"):
                    self.ospfarealsacksumsum = value
                    self.ospfarealsacksumsum.value_namespace = name_space
                    self.ospfarealsacksumsum.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAreaLsaCount"):
                    self.ospfarealsacount = value
                    self.ospfarealsacount.value_namespace = name_space
                    self.ospfarealsacount.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAreaNssaTranslatorEvents"):
                    self.ospfareanssatranslatorevents = value
                    self.ospfareanssatranslatorevents.value_namespace = name_space
                    self.ospfareanssatranslatorevents.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAreaNssaTranslatorRole"):
                    self.ospfareanssatranslatorrole = value
                    self.ospfareanssatranslatorrole.value_namespace = name_space
                    self.ospfareanssatranslatorrole.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAreaNssaTranslatorStabilityInterval"):
                    self.ospfareanssatranslatorstabilityinterval = value
                    self.ospfareanssatranslatorstabilityinterval.value_namespace = name_space
                    self.ospfareanssatranslatorstabilityinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAreaNssaTranslatorState"):
                    self.ospfareanssatranslatorstate = value
                    self.ospfareanssatranslatorstate.value_namespace = name_space
                    self.ospfareanssatranslatorstate.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAreaStatus"):
                    self.ospfareastatus = value
                    self.ospfareastatus.value_namespace = name_space
                    self.ospfareastatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAreaSummary"):
                    self.ospfareasummary = value
                    self.ospfareasummary.value_namespace = name_space
                    self.ospfareasummary.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAsBdrRtrCount"):
                    self.ospfasbdrrtrcount = value
                    self.ospfasbdrrtrcount.value_namespace = name_space
                    self.ospfasbdrrtrcount.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAuthType"):
                    self.ospfauthtype = value
                    self.ospfauthtype.value_namespace = name_space
                    self.ospfauthtype.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfImportAsExtern"):
                    self.ospfimportasextern = value
                    self.ospfimportasextern.value_namespace = name_space
                    self.ospfimportasextern.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfSpfRuns"):
                    self.ospfspfruns = value
                    self.ospfspfruns.value_namespace = name_space
                    self.ospfspfruns.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ospfareaentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ospfareaentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ospfAreaTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "OSPF-MIB:OSPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ospfAreaEntry"):
                for c in self.ospfareaentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = OspfMib.Ospfareatable.Ospfareaentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ospfareaentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ospfAreaEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ospfstubareatable(Entity):
        """
        The set of metrics that will be advertised
        by a default Area Border Router into a stub area.
        
        .. attribute:: ospfstubareaentry
        
        	The metric for a given Type of Service that will be advertised by a default Area Border Router into a stub area.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile storage
        	**type**\: list of    :py:class:`Ospfstubareaentry <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfstubareatable.Ospfstubareaentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OspfMib.Ospfstubareatable, self).__init__()

            self.yang_name = "ospfStubAreaTable"
            self.yang_parent_name = "OSPF-MIB"

            self.ospfstubareaentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(OspfMib.Ospfstubareatable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(OspfMib.Ospfstubareatable, self).__setattr__(name, value)


        class Ospfstubareaentry(Entity):
            """
            The metric for a given Type of Service that
            will be advertised by a default Area Border
            Router into a stub area.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            storage.
            
            .. attribute:: ospfstubareaid  <key>
            
            	The 32\-bit identifier for the stub area.  On creation, this can be derived from the instance
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfstubtos  <key>
            
            	The Type of Service associated with the metric.  On creation, this can be derived from  the instance
            	**type**\:  int
            
            	**range:** 0..30
            
            .. attribute:: ospfstubmetric
            
            	The metric value applied at the indicated Type of Service.  By default, this equals the least metric at the Type of Service among the interfaces to other areas
            	**type**\:  int
            
            	**range:** 0..16777215
            
            .. attribute:: ospfstubmetrictype
            
            	This variable displays the type of metric advertised as a default route
            	**type**\:   :py:class:`Ospfstubmetrictype <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfstubareatable.Ospfstubareaentry.Ospfstubmetrictype>`
            
            .. attribute:: ospfstubstatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OspfMib.Ospfstubareatable.Ospfstubareaentry, self).__init__()

                self.yang_name = "ospfStubAreaEntry"
                self.yang_parent_name = "ospfStubAreaTable"

                self.ospfstubareaid = YLeaf(YType.str, "ospfStubAreaId")

                self.ospfstubtos = YLeaf(YType.int32, "ospfStubTOS")

                self.ospfstubmetric = YLeaf(YType.int32, "ospfStubMetric")

                self.ospfstubmetrictype = YLeaf(YType.enumeration, "ospfStubMetricType")

                self.ospfstubstatus = YLeaf(YType.enumeration, "ospfStubStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ospfstubareaid",
                                "ospfstubtos",
                                "ospfstubmetric",
                                "ospfstubmetrictype",
                                "ospfstubstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(OspfMib.Ospfstubareatable.Ospfstubareaentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(OspfMib.Ospfstubareatable.Ospfstubareaentry, self).__setattr__(name, value)

            class Ospfstubmetrictype(Enum):
                """
                Ospfstubmetrictype

                This variable displays the type of metric

                advertised as a default route.

                .. data:: ospfMetric = 1

                .. data:: comparableCost = 2

                .. data:: nonComparable = 3

                """

                ospfMetric = Enum.YLeaf(1, "ospfMetric")

                comparableCost = Enum.YLeaf(2, "comparableCost")

                nonComparable = Enum.YLeaf(3, "nonComparable")


            def has_data(self):
                return (
                    self.ospfstubareaid.is_set or
                    self.ospfstubtos.is_set or
                    self.ospfstubmetric.is_set or
                    self.ospfstubmetrictype.is_set or
                    self.ospfstubstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ospfstubareaid.yfilter != YFilter.not_set or
                    self.ospfstubtos.yfilter != YFilter.not_set or
                    self.ospfstubmetric.yfilter != YFilter.not_set or
                    self.ospfstubmetrictype.yfilter != YFilter.not_set or
                    self.ospfstubstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ospfStubAreaEntry" + "[ospfStubAreaId='" + self.ospfstubareaid.get() + "']" + "[ospfStubTOS='" + self.ospfstubtos.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "OSPF-MIB:OSPF-MIB/ospfStubAreaTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ospfstubareaid.is_set or self.ospfstubareaid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfstubareaid.get_name_leafdata())
                if (self.ospfstubtos.is_set or self.ospfstubtos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfstubtos.get_name_leafdata())
                if (self.ospfstubmetric.is_set or self.ospfstubmetric.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfstubmetric.get_name_leafdata())
                if (self.ospfstubmetrictype.is_set or self.ospfstubmetrictype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfstubmetrictype.get_name_leafdata())
                if (self.ospfstubstatus.is_set or self.ospfstubstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfstubstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ospfStubAreaId" or name == "ospfStubTOS" or name == "ospfStubMetric" or name == "ospfStubMetricType" or name == "ospfStubStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ospfStubAreaId"):
                    self.ospfstubareaid = value
                    self.ospfstubareaid.value_namespace = name_space
                    self.ospfstubareaid.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfStubTOS"):
                    self.ospfstubtos = value
                    self.ospfstubtos.value_namespace = name_space
                    self.ospfstubtos.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfStubMetric"):
                    self.ospfstubmetric = value
                    self.ospfstubmetric.value_namespace = name_space
                    self.ospfstubmetric.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfStubMetricType"):
                    self.ospfstubmetrictype = value
                    self.ospfstubmetrictype.value_namespace = name_space
                    self.ospfstubmetrictype.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfStubStatus"):
                    self.ospfstubstatus = value
                    self.ospfstubstatus.value_namespace = name_space
                    self.ospfstubstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ospfstubareaentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ospfstubareaentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ospfStubAreaTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "OSPF-MIB:OSPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ospfStubAreaEntry"):
                for c in self.ospfstubareaentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = OspfMib.Ospfstubareatable.Ospfstubareaentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ospfstubareaentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ospfStubAreaEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ospflsdbtable(Entity):
        """
        The OSPF Process's link state database (LSDB).
        The LSDB contains the link state advertisements
        from throughout the areas that the device is attached to.
        
        .. attribute:: ospflsdbentry
        
        	A single link state advertisement
        	**type**\: list of    :py:class:`Ospflsdbentry <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospflsdbtable.Ospflsdbentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OspfMib.Ospflsdbtable, self).__init__()

            self.yang_name = "ospfLsdbTable"
            self.yang_parent_name = "OSPF-MIB"

            self.ospflsdbentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(OspfMib.Ospflsdbtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(OspfMib.Ospflsdbtable, self).__setattr__(name, value)


        class Ospflsdbentry(Entity):
            """
            A single link state advertisement.
            
            .. attribute:: ospflsdbareaid  <key>
            
            	The 32\-bit identifier of the area from which the LSA was received
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospflsdbtype  <key>
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format.  Note\: External link state advertisements are permitted for backward compatibility, but should be displayed in the ospfAsLsdbTable rather than here
            	**type**\:   :py:class:`Ospflsdbtype <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospflsdbtable.Ospflsdbentry.Ospflsdbtype>`
            
            .. attribute:: ospflsdblsid  <key>
            
            	The Link State ID is an LS Type Specific field containing either a Router ID or an IP address; it identifies the piece of the routing domain that is being described by the advertisement
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospflsdbrouterid  <key>
            
            	The 32\-bit number that uniquely identifies the originating router in the Autonomous System
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospflsdbadvertisement
            
            	The entire link state advertisement, including its header.  Note that for variable length LSAs, SNMP agents may not be able to return the largest string size
            	**type**\:  str
            
            	**length:** 1..65535
            
            .. attribute:: ospflsdbage
            
            	This field is the age of the link state advertisement in seconds
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: seconds
            
            .. attribute:: ospflsdbchecksum
            
            	This field is the checksum of the complete contents of the advertisement, excepting the age field.  The age field is excepted so that an advertisement's age can be incremented without updating the checksum.  The checksum used is the same that is used for ISO connectionless  datagrams; it is commonly referred to as the Fletcher checksum
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospflsdbsequence
            
            	The sequence number field is a signed 32\-bit integer.  It starts with the value '80000001'h, or \-'7FFFFFFF'h, and increments until '7FFFFFFF'h. Thus, a typical sequence number will be very negative. It is used to detect old and duplicate Link State Advertisements.  The space of sequence numbers is linearly ordered.  The larger the sequence number, the more recent the advertisement
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OspfMib.Ospflsdbtable.Ospflsdbentry, self).__init__()

                self.yang_name = "ospfLsdbEntry"
                self.yang_parent_name = "ospfLsdbTable"

                self.ospflsdbareaid = YLeaf(YType.str, "ospfLsdbAreaId")

                self.ospflsdbtype = YLeaf(YType.enumeration, "ospfLsdbType")

                self.ospflsdblsid = YLeaf(YType.str, "ospfLsdbLsid")

                self.ospflsdbrouterid = YLeaf(YType.str, "ospfLsdbRouterId")

                self.ospflsdbadvertisement = YLeaf(YType.str, "ospfLsdbAdvertisement")

                self.ospflsdbage = YLeaf(YType.int32, "ospfLsdbAge")

                self.ospflsdbchecksum = YLeaf(YType.int32, "ospfLsdbChecksum")

                self.ospflsdbsequence = YLeaf(YType.int32, "ospfLsdbSequence")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ospflsdbareaid",
                                "ospflsdbtype",
                                "ospflsdblsid",
                                "ospflsdbrouterid",
                                "ospflsdbadvertisement",
                                "ospflsdbage",
                                "ospflsdbchecksum",
                                "ospflsdbsequence") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(OspfMib.Ospflsdbtable.Ospflsdbentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(OspfMib.Ospflsdbtable.Ospflsdbentry, self).__setattr__(name, value)

            class Ospflsdbtype(Enum):
                """
                Ospflsdbtype

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


            def has_data(self):
                return (
                    self.ospflsdbareaid.is_set or
                    self.ospflsdbtype.is_set or
                    self.ospflsdblsid.is_set or
                    self.ospflsdbrouterid.is_set or
                    self.ospflsdbadvertisement.is_set or
                    self.ospflsdbage.is_set or
                    self.ospflsdbchecksum.is_set or
                    self.ospflsdbsequence.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ospflsdbareaid.yfilter != YFilter.not_set or
                    self.ospflsdbtype.yfilter != YFilter.not_set or
                    self.ospflsdblsid.yfilter != YFilter.not_set or
                    self.ospflsdbrouterid.yfilter != YFilter.not_set or
                    self.ospflsdbadvertisement.yfilter != YFilter.not_set or
                    self.ospflsdbage.yfilter != YFilter.not_set or
                    self.ospflsdbchecksum.yfilter != YFilter.not_set or
                    self.ospflsdbsequence.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ospfLsdbEntry" + "[ospfLsdbAreaId='" + self.ospflsdbareaid.get() + "']" + "[ospfLsdbType='" + self.ospflsdbtype.get() + "']" + "[ospfLsdbLsid='" + self.ospflsdblsid.get() + "']" + "[ospfLsdbRouterId='" + self.ospflsdbrouterid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "OSPF-MIB:OSPF-MIB/ospfLsdbTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ospflsdbareaid.is_set or self.ospflsdbareaid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospflsdbareaid.get_name_leafdata())
                if (self.ospflsdbtype.is_set or self.ospflsdbtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospflsdbtype.get_name_leafdata())
                if (self.ospflsdblsid.is_set or self.ospflsdblsid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospflsdblsid.get_name_leafdata())
                if (self.ospflsdbrouterid.is_set or self.ospflsdbrouterid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospflsdbrouterid.get_name_leafdata())
                if (self.ospflsdbadvertisement.is_set or self.ospflsdbadvertisement.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospflsdbadvertisement.get_name_leafdata())
                if (self.ospflsdbage.is_set or self.ospflsdbage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospflsdbage.get_name_leafdata())
                if (self.ospflsdbchecksum.is_set or self.ospflsdbchecksum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospflsdbchecksum.get_name_leafdata())
                if (self.ospflsdbsequence.is_set or self.ospflsdbsequence.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospflsdbsequence.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ospfLsdbAreaId" or name == "ospfLsdbType" or name == "ospfLsdbLsid" or name == "ospfLsdbRouterId" or name == "ospfLsdbAdvertisement" or name == "ospfLsdbAge" or name == "ospfLsdbChecksum" or name == "ospfLsdbSequence"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ospfLsdbAreaId"):
                    self.ospflsdbareaid = value
                    self.ospflsdbareaid.value_namespace = name_space
                    self.ospflsdbareaid.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfLsdbType"):
                    self.ospflsdbtype = value
                    self.ospflsdbtype.value_namespace = name_space
                    self.ospflsdbtype.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfLsdbLsid"):
                    self.ospflsdblsid = value
                    self.ospflsdblsid.value_namespace = name_space
                    self.ospflsdblsid.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfLsdbRouterId"):
                    self.ospflsdbrouterid = value
                    self.ospflsdbrouterid.value_namespace = name_space
                    self.ospflsdbrouterid.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfLsdbAdvertisement"):
                    self.ospflsdbadvertisement = value
                    self.ospflsdbadvertisement.value_namespace = name_space
                    self.ospflsdbadvertisement.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfLsdbAge"):
                    self.ospflsdbage = value
                    self.ospflsdbage.value_namespace = name_space
                    self.ospflsdbage.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfLsdbChecksum"):
                    self.ospflsdbchecksum = value
                    self.ospflsdbchecksum.value_namespace = name_space
                    self.ospflsdbchecksum.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfLsdbSequence"):
                    self.ospflsdbsequence = value
                    self.ospflsdbsequence.value_namespace = name_space
                    self.ospflsdbsequence.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ospflsdbentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ospflsdbentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ospfLsdbTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "OSPF-MIB:OSPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ospfLsdbEntry"):
                for c in self.ospflsdbentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = OspfMib.Ospflsdbtable.Ospflsdbentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ospflsdbentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ospfLsdbEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Ospfarearangeentry <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfarearangetable.Ospfarearangeentry>`
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OspfMib.Ospfarearangetable, self).__init__()

            self.yang_name = "ospfAreaRangeTable"
            self.yang_parent_name = "OSPF-MIB"

            self.ospfarearangeentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(OspfMib.Ospfarearangetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(OspfMib.Ospfarearangetable, self).__setattr__(name, value)


        class Ospfarearangeentry(Entity):
            """
            A single area address range.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            storage.
            
            .. attribute:: ospfarearangeareaid  <key>
            
            	The area that the address range is to be found within
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: obsolete
            
            .. attribute:: ospfarearangenet  <key>
            
            	The IP address of the net or subnet indicated by the range
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: obsolete
            
            .. attribute:: ospfarearangeeffect
            
            	Subnets subsumed by ranges either trigger the advertisement of the indicated summary (advertiseMatching) or result in the subnet's not being advertised at all outside the area
            	**type**\:   :py:class:`Ospfarearangeeffect <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfarearangetable.Ospfarearangeentry.Ospfarearangeeffect>`
            
            	**status**\: obsolete
            
            .. attribute:: ospfarearangemask
            
            	The subnet mask that pertains to the net or subnet
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: obsolete
            
            .. attribute:: ospfarearangestatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OspfMib.Ospfarearangetable.Ospfarearangeentry, self).__init__()

                self.yang_name = "ospfAreaRangeEntry"
                self.yang_parent_name = "ospfAreaRangeTable"

                self.ospfarearangeareaid = YLeaf(YType.str, "ospfAreaRangeAreaId")

                self.ospfarearangenet = YLeaf(YType.str, "ospfAreaRangeNet")

                self.ospfarearangeeffect = YLeaf(YType.enumeration, "ospfAreaRangeEffect")

                self.ospfarearangemask = YLeaf(YType.str, "ospfAreaRangeMask")

                self.ospfarearangestatus = YLeaf(YType.enumeration, "ospfAreaRangeStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ospfarearangeareaid",
                                "ospfarearangenet",
                                "ospfarearangeeffect",
                                "ospfarearangemask",
                                "ospfarearangestatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(OspfMib.Ospfarearangetable.Ospfarearangeentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(OspfMib.Ospfarearangetable.Ospfarearangeentry, self).__setattr__(name, value)

            class Ospfarearangeeffect(Enum):
                """
                Ospfarearangeeffect

                Subnets subsumed by ranges either trigger the

                advertisement of the indicated summary

                (advertiseMatching) or result in the subnet's not

                being advertised at all outside the area.

                .. data:: advertiseMatching = 1

                .. data:: doNotAdvertiseMatching = 2

                """

                advertiseMatching = Enum.YLeaf(1, "advertiseMatching")

                doNotAdvertiseMatching = Enum.YLeaf(2, "doNotAdvertiseMatching")


            def has_data(self):
                return (
                    self.ospfarearangeareaid.is_set or
                    self.ospfarearangenet.is_set or
                    self.ospfarearangeeffect.is_set or
                    self.ospfarearangemask.is_set or
                    self.ospfarearangestatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ospfarearangeareaid.yfilter != YFilter.not_set or
                    self.ospfarearangenet.yfilter != YFilter.not_set or
                    self.ospfarearangeeffect.yfilter != YFilter.not_set or
                    self.ospfarearangemask.yfilter != YFilter.not_set or
                    self.ospfarearangestatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ospfAreaRangeEntry" + "[ospfAreaRangeAreaId='" + self.ospfarearangeareaid.get() + "']" + "[ospfAreaRangeNet='" + self.ospfarearangenet.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "OSPF-MIB:OSPF-MIB/ospfAreaRangeTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ospfarearangeareaid.is_set or self.ospfarearangeareaid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfarearangeareaid.get_name_leafdata())
                if (self.ospfarearangenet.is_set or self.ospfarearangenet.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfarearangenet.get_name_leafdata())
                if (self.ospfarearangeeffect.is_set or self.ospfarearangeeffect.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfarearangeeffect.get_name_leafdata())
                if (self.ospfarearangemask.is_set or self.ospfarearangemask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfarearangemask.get_name_leafdata())
                if (self.ospfarearangestatus.is_set or self.ospfarearangestatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfarearangestatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ospfAreaRangeAreaId" or name == "ospfAreaRangeNet" or name == "ospfAreaRangeEffect" or name == "ospfAreaRangeMask" or name == "ospfAreaRangeStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ospfAreaRangeAreaId"):
                    self.ospfarearangeareaid = value
                    self.ospfarearangeareaid.value_namespace = name_space
                    self.ospfarearangeareaid.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAreaRangeNet"):
                    self.ospfarearangenet = value
                    self.ospfarearangenet.value_namespace = name_space
                    self.ospfarearangenet.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAreaRangeEffect"):
                    self.ospfarearangeeffect = value
                    self.ospfarearangeeffect.value_namespace = name_space
                    self.ospfarearangeeffect.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAreaRangeMask"):
                    self.ospfarearangemask = value
                    self.ospfarearangemask.value_namespace = name_space
                    self.ospfarearangemask.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAreaRangeStatus"):
                    self.ospfarearangestatus = value
                    self.ospfarearangestatus.value_namespace = name_space
                    self.ospfarearangestatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ospfarearangeentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ospfarearangeentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ospfAreaRangeTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "OSPF-MIB:OSPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ospfAreaRangeEntry"):
                for c in self.ospfarearangeentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = OspfMib.Ospfarearangetable.Ospfarearangeentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ospfarearangeentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ospfAreaRangeEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ospfhosttable(Entity):
        """
        The Host/Metric Table indicates what hosts are directly
        
        attached to the router, what metrics and types
        of service should be advertised for them,
        and what areas they are found within.
        
        .. attribute:: ospfhostentry
        
        	A metric to be advertised, for a given type of service, when a given host is reachable.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile storage
        	**type**\: list of    :py:class:`Ospfhostentry <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfhosttable.Ospfhostentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OspfMib.Ospfhosttable, self).__init__()

            self.yang_name = "ospfHostTable"
            self.yang_parent_name = "OSPF-MIB"

            self.ospfhostentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(OspfMib.Ospfhosttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(OspfMib.Ospfhosttable, self).__setattr__(name, value)


        class Ospfhostentry(Entity):
            """
            A metric to be advertised, for a given type of
            service, when a given host is reachable.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            storage.
            
            .. attribute:: ospfhostipaddress  <key>
            
            	The IP address of the host
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfhosttos  <key>
            
            	The Type of Service of the route being configured
            	**type**\:  int
            
            	**range:** 0..30
            
            .. attribute:: ospfhostareaid
            
            	The OSPF area to which the host belongs. Deprecated by ospfHostCfgAreaID
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: ospfhostcfgareaid
            
            	To configure the OSPF area to which the host belongs
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfhostmetric
            
            	The metric to be advertised
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: ospfhoststatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OspfMib.Ospfhosttable.Ospfhostentry, self).__init__()

                self.yang_name = "ospfHostEntry"
                self.yang_parent_name = "ospfHostTable"

                self.ospfhostipaddress = YLeaf(YType.str, "ospfHostIpAddress")

                self.ospfhosttos = YLeaf(YType.int32, "ospfHostTOS")

                self.ospfhostareaid = YLeaf(YType.str, "ospfHostAreaID")

                self.ospfhostcfgareaid = YLeaf(YType.str, "ospfHostCfgAreaID")

                self.ospfhostmetric = YLeaf(YType.int32, "ospfHostMetric")

                self.ospfhoststatus = YLeaf(YType.enumeration, "ospfHostStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ospfhostipaddress",
                                "ospfhosttos",
                                "ospfhostareaid",
                                "ospfhostcfgareaid",
                                "ospfhostmetric",
                                "ospfhoststatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(OspfMib.Ospfhosttable.Ospfhostentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(OspfMib.Ospfhosttable.Ospfhostentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ospfhostipaddress.is_set or
                    self.ospfhosttos.is_set or
                    self.ospfhostareaid.is_set or
                    self.ospfhostcfgareaid.is_set or
                    self.ospfhostmetric.is_set or
                    self.ospfhoststatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ospfhostipaddress.yfilter != YFilter.not_set or
                    self.ospfhosttos.yfilter != YFilter.not_set or
                    self.ospfhostareaid.yfilter != YFilter.not_set or
                    self.ospfhostcfgareaid.yfilter != YFilter.not_set or
                    self.ospfhostmetric.yfilter != YFilter.not_set or
                    self.ospfhoststatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ospfHostEntry" + "[ospfHostIpAddress='" + self.ospfhostipaddress.get() + "']" + "[ospfHostTOS='" + self.ospfhosttos.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "OSPF-MIB:OSPF-MIB/ospfHostTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ospfhostipaddress.is_set or self.ospfhostipaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfhostipaddress.get_name_leafdata())
                if (self.ospfhosttos.is_set or self.ospfhosttos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfhosttos.get_name_leafdata())
                if (self.ospfhostareaid.is_set or self.ospfhostareaid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfhostareaid.get_name_leafdata())
                if (self.ospfhostcfgareaid.is_set or self.ospfhostcfgareaid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfhostcfgareaid.get_name_leafdata())
                if (self.ospfhostmetric.is_set or self.ospfhostmetric.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfhostmetric.get_name_leafdata())
                if (self.ospfhoststatus.is_set or self.ospfhoststatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfhoststatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ospfHostIpAddress" or name == "ospfHostTOS" or name == "ospfHostAreaID" or name == "ospfHostCfgAreaID" or name == "ospfHostMetric" or name == "ospfHostStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ospfHostIpAddress"):
                    self.ospfhostipaddress = value
                    self.ospfhostipaddress.value_namespace = name_space
                    self.ospfhostipaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfHostTOS"):
                    self.ospfhosttos = value
                    self.ospfhosttos.value_namespace = name_space
                    self.ospfhosttos.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfHostAreaID"):
                    self.ospfhostareaid = value
                    self.ospfhostareaid.value_namespace = name_space
                    self.ospfhostareaid.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfHostCfgAreaID"):
                    self.ospfhostcfgareaid = value
                    self.ospfhostcfgareaid.value_namespace = name_space
                    self.ospfhostcfgareaid.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfHostMetric"):
                    self.ospfhostmetric = value
                    self.ospfhostmetric.value_namespace = name_space
                    self.ospfhostmetric.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfHostStatus"):
                    self.ospfhoststatus = value
                    self.ospfhoststatus.value_namespace = name_space
                    self.ospfhoststatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ospfhostentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ospfhostentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ospfHostTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "OSPF-MIB:OSPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ospfHostEntry"):
                for c in self.ospfhostentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = OspfMib.Ospfhosttable.Ospfhostentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ospfhostentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ospfHostEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ospfiftable(Entity):
        """
        The OSPF Interface Table describes the interfaces
        from the viewpoint of OSPF.
        It augments the ipAddrTable with OSPF specific information.
        
        .. attribute:: ospfifentry
        
        	The OSPF interface entry describes one interface from the viewpoint of OSPF.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile storage
        	**type**\: list of    :py:class:`Ospfifentry <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfiftable.Ospfifentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OspfMib.Ospfiftable, self).__init__()

            self.yang_name = "ospfIfTable"
            self.yang_parent_name = "OSPF-MIB"

            self.ospfifentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(OspfMib.Ospfiftable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(OspfMib.Ospfiftable, self).__setattr__(name, value)


        class Ospfifentry(Entity):
            """
            The OSPF interface entry describes one interface
            from the viewpoint of OSPF.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            storage.
            
            .. attribute:: ospfifipaddress  <key>
            
            	The IP address of this OSPF interface
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfaddresslessif  <key>
            
            	For the purpose of easing the instancing of addressed and addressless interfaces; this variable takes the value 0 on interfaces with IP addresses and the corresponding value of ifIndex for interfaces having no IP address
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cospfiflsacksumsum
            
            	The 32\-bit unsigned sum of the link\-state advertisements' LS checksums contained in this interface's link\-local link  state database. The sum can be used to determine if there has been a change in the interface's link state database, and to compare the interface link\-state database of routers  attached to the same subnet
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfiflsacount
            
            	The total number of link\-local link state advertisements in this interface's link\-local link state database
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfifadminstat
            
            	The OSPF interface's administrative status. The value formed on the interface, and the interface will be advertised as an internal route to some area. The value 'disabled' denotes that the interface is external to OSPF
            	**type**\:   :py:class:`Status <ydk.models.cisco_ios_xe.OSPF_MIB.Status>`
            
            .. attribute:: ospfifareaid
            
            	A 32\-bit integer uniquely identifying the area to which the interface connects.  Area ID 0.0.0.0 is used for the OSPF backbone
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfifauthkey
            
            	The cleartext password used as an OSPF authentication key when simplePassword security is enabled.  This object does not access any OSPF cryptogaphic (e.g., MD5) authentication key under any circumstance.  If the key length is shorter than 8 octets, the agent will left adjust and zero fill to 8 octets.  Unauthenticated interfaces need no authentication key, and simple password authentication cannot use a key of more than 8 octets.  Note that the use of simplePassword authentication is NOT recommended when there is concern regarding attack upon the OSPF system.  SimplePassword authentication is only sufficient to protect against accidental misconfigurations because it re\-uses cleartext passwords [RFC1704].  When read, ospfIfAuthKey always returns an octet string of length zero
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: ospfifauthtype
            
            	The authentication type specified for an interface.  Note that this object can be used to engage in significant attacks against an OSPF router
            	**type**\:   :py:class:`Ospfauthenticationtype <ydk.models.cisco_ios_xe.OSPF_MIB.Ospfauthenticationtype>`
            
            .. attribute:: ospfifbackupdesignatedrouter
            
            	The IP address of the backup designated router
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfifbackupdesignatedrouterid
            
            	The Router ID of the backup designated router
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfifdemand
            
            	Indicates whether Demand OSPF procedures (hello suppression to FULL neighbors and setting the DoNotAge flag on propagated LSAs) should be performed on this interface
            	**type**\:  bool
            
            .. attribute:: ospfifdesignatedrouter
            
            	The IP address of the designated router
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfifdesignatedrouterid
            
            	The Router ID of the designated router
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfifevents
            
            	The number of times this OSPF interface has changed its state or an error has occurred.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ospfDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfifhellointerval
            
            	The length of time, in seconds, between the Hello packets that the router sends on the interface.  This value must be the same for all routers attached to a common network
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**units**\: seconds
            
            .. attribute:: ospfiflsacksumsum
            
            	The 32\-bit unsigned sum of the Link State Advertisements' LS checksums contained in this interface's link\-local link state database. The sum can be used to determine if there has been a change in the interface's link state database and to compare the interface link state database of routers attached to the same subnet
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfiflsacount
            
            	The total number of link\-local link state advertisements in this interface's link\-local link state database
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfifmulticastforwarding
            
            	The way multicasts should be forwarded on this interface\: not forwarded, forwarded as data link multicasts, or forwarded as data link unicasts.  Data link multicasting is not meaningful on point\-to\-point and NBMA interfaces, and setting ospfMulticastForwarding to 0 effectively disables all multicast forwarding
            	**type**\:   :py:class:`Ospfifmulticastforwarding <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfiftable.Ospfifentry.Ospfifmulticastforwarding>`
            
            .. attribute:: ospfifpollinterval
            
            	The larger time interval, in seconds, between the Hello packets sent to an inactive non\-broadcast multi\-access neighbor
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: ospfifretransinterval
            
            	The number of seconds between link state advertisement retransmissions, for adjacencies belonging to this interface.  This value is also used when retransmitting  database description and Link State request packets. Note that minimal value SHOULD be 1 second
            	**type**\:  int
            
            	**range:** 0..3600
            
            	**units**\: seconds
            
            .. attribute:: ospfifrtrdeadinterval
            
            	The number of seconds that a router's Hello packets have not been seen before its neighbors declare the router down. This should be some multiple of the Hello interval.  This value must be the same for all routers attached to a common network
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: ospfifrtrpriority
            
            	The priority of this interface.  Used in multi\-access networks, this field is used in the designated router election algorithm.  The value 0 signifies that the router is not eligible to become the designated router on this particular network.  In the event of a tie in this value, routers will use their Router ID as a tie breaker
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: ospfifstate
            
            	The OSPF Interface State
            	**type**\:   :py:class:`Ospfifstate <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfiftable.Ospfifentry.Ospfifstate>`
            
            .. attribute:: ospfifstatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: ospfiftransitdelay
            
            	The estimated number of seconds it takes to transmit a link state update packet over this interface.  Note that the minimal value SHOULD be 1 second
            	**type**\:  int
            
            	**range:** 0..3600
            
            	**units**\: seconds
            
            .. attribute:: ospfiftype
            
            	The OSPF interface type. By way of a default, this field may be intuited from the corresponding value of ifType. Broadcast LANs, such as Ethernet and IEEE 802.5, take the value 'broadcast', X.25 and similar technologies take the value 'nbma', and links that are definitively point to point take the value 'pointToPoint'
            	**type**\:   :py:class:`Ospfiftype <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfiftable.Ospfifentry.Ospfiftype>`
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OspfMib.Ospfiftable.Ospfifentry, self).__init__()

                self.yang_name = "ospfIfEntry"
                self.yang_parent_name = "ospfIfTable"

                self.ospfifipaddress = YLeaf(YType.str, "ospfIfIpAddress")

                self.ospfaddresslessif = YLeaf(YType.int32, "ospfAddressLessIf")

                self.cospfiflsacksumsum = YLeaf(YType.uint32, "CISCO-OSPF-MIB:cospfIfLsaCksumSum")

                self.cospfiflsacount = YLeaf(YType.uint32, "CISCO-OSPF-MIB:cospfIfLsaCount")

                self.ospfifadminstat = YLeaf(YType.enumeration, "ospfIfAdminStat")

                self.ospfifareaid = YLeaf(YType.str, "ospfIfAreaId")

                self.ospfifauthkey = YLeaf(YType.str, "ospfIfAuthKey")

                self.ospfifauthtype = YLeaf(YType.enumeration, "ospfIfAuthType")

                self.ospfifbackupdesignatedrouter = YLeaf(YType.str, "ospfIfBackupDesignatedRouter")

                self.ospfifbackupdesignatedrouterid = YLeaf(YType.str, "ospfIfBackupDesignatedRouterId")

                self.ospfifdemand = YLeaf(YType.boolean, "ospfIfDemand")

                self.ospfifdesignatedrouter = YLeaf(YType.str, "ospfIfDesignatedRouter")

                self.ospfifdesignatedrouterid = YLeaf(YType.str, "ospfIfDesignatedRouterId")

                self.ospfifevents = YLeaf(YType.uint32, "ospfIfEvents")

                self.ospfifhellointerval = YLeaf(YType.int32, "ospfIfHelloInterval")

                self.ospfiflsacksumsum = YLeaf(YType.uint32, "ospfIfLsaCksumSum")

                self.ospfiflsacount = YLeaf(YType.uint32, "ospfIfLsaCount")

                self.ospfifmulticastforwarding = YLeaf(YType.enumeration, "ospfIfMulticastForwarding")

                self.ospfifpollinterval = YLeaf(YType.int32, "ospfIfPollInterval")

                self.ospfifretransinterval = YLeaf(YType.int32, "ospfIfRetransInterval")

                self.ospfifrtrdeadinterval = YLeaf(YType.int32, "ospfIfRtrDeadInterval")

                self.ospfifrtrpriority = YLeaf(YType.int32, "ospfIfRtrPriority")

                self.ospfifstate = YLeaf(YType.enumeration, "ospfIfState")

                self.ospfifstatus = YLeaf(YType.enumeration, "ospfIfStatus")

                self.ospfiftransitdelay = YLeaf(YType.int32, "ospfIfTransitDelay")

                self.ospfiftype = YLeaf(YType.enumeration, "ospfIfType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ospfifipaddress",
                                "ospfaddresslessif",
                                "cospfiflsacksumsum",
                                "cospfiflsacount",
                                "ospfifadminstat",
                                "ospfifareaid",
                                "ospfifauthkey",
                                "ospfifauthtype",
                                "ospfifbackupdesignatedrouter",
                                "ospfifbackupdesignatedrouterid",
                                "ospfifdemand",
                                "ospfifdesignatedrouter",
                                "ospfifdesignatedrouterid",
                                "ospfifevents",
                                "ospfifhellointerval",
                                "ospfiflsacksumsum",
                                "ospfiflsacount",
                                "ospfifmulticastforwarding",
                                "ospfifpollinterval",
                                "ospfifretransinterval",
                                "ospfifrtrdeadinterval",
                                "ospfifrtrpriority",
                                "ospfifstate",
                                "ospfifstatus",
                                "ospfiftransitdelay",
                                "ospfiftype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(OspfMib.Ospfiftable.Ospfifentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(OspfMib.Ospfiftable.Ospfifentry, self).__setattr__(name, value)

            class Ospfifmulticastforwarding(Enum):
                """
                Ospfifmulticastforwarding

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
                Ospfifstate

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
                Ospfiftype

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


            def has_data(self):
                return (
                    self.ospfifipaddress.is_set or
                    self.ospfaddresslessif.is_set or
                    self.cospfiflsacksumsum.is_set or
                    self.cospfiflsacount.is_set or
                    self.ospfifadminstat.is_set or
                    self.ospfifareaid.is_set or
                    self.ospfifauthkey.is_set or
                    self.ospfifauthtype.is_set or
                    self.ospfifbackupdesignatedrouter.is_set or
                    self.ospfifbackupdesignatedrouterid.is_set or
                    self.ospfifdemand.is_set or
                    self.ospfifdesignatedrouter.is_set or
                    self.ospfifdesignatedrouterid.is_set or
                    self.ospfifevents.is_set or
                    self.ospfifhellointerval.is_set or
                    self.ospfiflsacksumsum.is_set or
                    self.ospfiflsacount.is_set or
                    self.ospfifmulticastforwarding.is_set or
                    self.ospfifpollinterval.is_set or
                    self.ospfifretransinterval.is_set or
                    self.ospfifrtrdeadinterval.is_set or
                    self.ospfifrtrpriority.is_set or
                    self.ospfifstate.is_set or
                    self.ospfifstatus.is_set or
                    self.ospfiftransitdelay.is_set or
                    self.ospfiftype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ospfifipaddress.yfilter != YFilter.not_set or
                    self.ospfaddresslessif.yfilter != YFilter.not_set or
                    self.cospfiflsacksumsum.yfilter != YFilter.not_set or
                    self.cospfiflsacount.yfilter != YFilter.not_set or
                    self.ospfifadminstat.yfilter != YFilter.not_set or
                    self.ospfifareaid.yfilter != YFilter.not_set or
                    self.ospfifauthkey.yfilter != YFilter.not_set or
                    self.ospfifauthtype.yfilter != YFilter.not_set or
                    self.ospfifbackupdesignatedrouter.yfilter != YFilter.not_set or
                    self.ospfifbackupdesignatedrouterid.yfilter != YFilter.not_set or
                    self.ospfifdemand.yfilter != YFilter.not_set or
                    self.ospfifdesignatedrouter.yfilter != YFilter.not_set or
                    self.ospfifdesignatedrouterid.yfilter != YFilter.not_set or
                    self.ospfifevents.yfilter != YFilter.not_set or
                    self.ospfifhellointerval.yfilter != YFilter.not_set or
                    self.ospfiflsacksumsum.yfilter != YFilter.not_set or
                    self.ospfiflsacount.yfilter != YFilter.not_set or
                    self.ospfifmulticastforwarding.yfilter != YFilter.not_set or
                    self.ospfifpollinterval.yfilter != YFilter.not_set or
                    self.ospfifretransinterval.yfilter != YFilter.not_set or
                    self.ospfifrtrdeadinterval.yfilter != YFilter.not_set or
                    self.ospfifrtrpriority.yfilter != YFilter.not_set or
                    self.ospfifstate.yfilter != YFilter.not_set or
                    self.ospfifstatus.yfilter != YFilter.not_set or
                    self.ospfiftransitdelay.yfilter != YFilter.not_set or
                    self.ospfiftype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ospfIfEntry" + "[ospfIfIpAddress='" + self.ospfifipaddress.get() + "']" + "[ospfAddressLessIf='" + self.ospfaddresslessif.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "OSPF-MIB:OSPF-MIB/ospfIfTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ospfifipaddress.is_set or self.ospfifipaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfifipaddress.get_name_leafdata())
                if (self.ospfaddresslessif.is_set or self.ospfaddresslessif.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfaddresslessif.get_name_leafdata())
                if (self.cospfiflsacksumsum.is_set or self.cospfiflsacksumsum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfiflsacksumsum.get_name_leafdata())
                if (self.cospfiflsacount.is_set or self.cospfiflsacount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfiflsacount.get_name_leafdata())
                if (self.ospfifadminstat.is_set or self.ospfifadminstat.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfifadminstat.get_name_leafdata())
                if (self.ospfifareaid.is_set or self.ospfifareaid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfifareaid.get_name_leafdata())
                if (self.ospfifauthkey.is_set or self.ospfifauthkey.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfifauthkey.get_name_leafdata())
                if (self.ospfifauthtype.is_set or self.ospfifauthtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfifauthtype.get_name_leafdata())
                if (self.ospfifbackupdesignatedrouter.is_set or self.ospfifbackupdesignatedrouter.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfifbackupdesignatedrouter.get_name_leafdata())
                if (self.ospfifbackupdesignatedrouterid.is_set or self.ospfifbackupdesignatedrouterid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfifbackupdesignatedrouterid.get_name_leafdata())
                if (self.ospfifdemand.is_set or self.ospfifdemand.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfifdemand.get_name_leafdata())
                if (self.ospfifdesignatedrouter.is_set or self.ospfifdesignatedrouter.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfifdesignatedrouter.get_name_leafdata())
                if (self.ospfifdesignatedrouterid.is_set or self.ospfifdesignatedrouterid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfifdesignatedrouterid.get_name_leafdata())
                if (self.ospfifevents.is_set or self.ospfifevents.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfifevents.get_name_leafdata())
                if (self.ospfifhellointerval.is_set or self.ospfifhellointerval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfifhellointerval.get_name_leafdata())
                if (self.ospfiflsacksumsum.is_set or self.ospfiflsacksumsum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfiflsacksumsum.get_name_leafdata())
                if (self.ospfiflsacount.is_set or self.ospfiflsacount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfiflsacount.get_name_leafdata())
                if (self.ospfifmulticastforwarding.is_set or self.ospfifmulticastforwarding.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfifmulticastforwarding.get_name_leafdata())
                if (self.ospfifpollinterval.is_set or self.ospfifpollinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfifpollinterval.get_name_leafdata())
                if (self.ospfifretransinterval.is_set or self.ospfifretransinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfifretransinterval.get_name_leafdata())
                if (self.ospfifrtrdeadinterval.is_set or self.ospfifrtrdeadinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfifrtrdeadinterval.get_name_leafdata())
                if (self.ospfifrtrpriority.is_set or self.ospfifrtrpriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfifrtrpriority.get_name_leafdata())
                if (self.ospfifstate.is_set or self.ospfifstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfifstate.get_name_leafdata())
                if (self.ospfifstatus.is_set or self.ospfifstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfifstatus.get_name_leafdata())
                if (self.ospfiftransitdelay.is_set or self.ospfiftransitdelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfiftransitdelay.get_name_leafdata())
                if (self.ospfiftype.is_set or self.ospfiftype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfiftype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ospfIfIpAddress" or name == "ospfAddressLessIf" or name == "cospfIfLsaCksumSum" or name == "cospfIfLsaCount" or name == "ospfIfAdminStat" or name == "ospfIfAreaId" or name == "ospfIfAuthKey" or name == "ospfIfAuthType" or name == "ospfIfBackupDesignatedRouter" or name == "ospfIfBackupDesignatedRouterId" or name == "ospfIfDemand" or name == "ospfIfDesignatedRouter" or name == "ospfIfDesignatedRouterId" or name == "ospfIfEvents" or name == "ospfIfHelloInterval" or name == "ospfIfLsaCksumSum" or name == "ospfIfLsaCount" or name == "ospfIfMulticastForwarding" or name == "ospfIfPollInterval" or name == "ospfIfRetransInterval" or name == "ospfIfRtrDeadInterval" or name == "ospfIfRtrPriority" or name == "ospfIfState" or name == "ospfIfStatus" or name == "ospfIfTransitDelay" or name == "ospfIfType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ospfIfIpAddress"):
                    self.ospfifipaddress = value
                    self.ospfifipaddress.value_namespace = name_space
                    self.ospfifipaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAddressLessIf"):
                    self.ospfaddresslessif = value
                    self.ospfaddresslessif.value_namespace = name_space
                    self.ospfaddresslessif.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfIfLsaCksumSum"):
                    self.cospfiflsacksumsum = value
                    self.cospfiflsacksumsum.value_namespace = name_space
                    self.cospfiflsacksumsum.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfIfLsaCount"):
                    self.cospfiflsacount = value
                    self.cospfiflsacount.value_namespace = name_space
                    self.cospfiflsacount.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfAdminStat"):
                    self.ospfifadminstat = value
                    self.ospfifadminstat.value_namespace = name_space
                    self.ospfifadminstat.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfAreaId"):
                    self.ospfifareaid = value
                    self.ospfifareaid.value_namespace = name_space
                    self.ospfifareaid.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfAuthKey"):
                    self.ospfifauthkey = value
                    self.ospfifauthkey.value_namespace = name_space
                    self.ospfifauthkey.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfAuthType"):
                    self.ospfifauthtype = value
                    self.ospfifauthtype.value_namespace = name_space
                    self.ospfifauthtype.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfBackupDesignatedRouter"):
                    self.ospfifbackupdesignatedrouter = value
                    self.ospfifbackupdesignatedrouter.value_namespace = name_space
                    self.ospfifbackupdesignatedrouter.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfBackupDesignatedRouterId"):
                    self.ospfifbackupdesignatedrouterid = value
                    self.ospfifbackupdesignatedrouterid.value_namespace = name_space
                    self.ospfifbackupdesignatedrouterid.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfDemand"):
                    self.ospfifdemand = value
                    self.ospfifdemand.value_namespace = name_space
                    self.ospfifdemand.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfDesignatedRouter"):
                    self.ospfifdesignatedrouter = value
                    self.ospfifdesignatedrouter.value_namespace = name_space
                    self.ospfifdesignatedrouter.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfDesignatedRouterId"):
                    self.ospfifdesignatedrouterid = value
                    self.ospfifdesignatedrouterid.value_namespace = name_space
                    self.ospfifdesignatedrouterid.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfEvents"):
                    self.ospfifevents = value
                    self.ospfifevents.value_namespace = name_space
                    self.ospfifevents.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfHelloInterval"):
                    self.ospfifhellointerval = value
                    self.ospfifhellointerval.value_namespace = name_space
                    self.ospfifhellointerval.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfLsaCksumSum"):
                    self.ospfiflsacksumsum = value
                    self.ospfiflsacksumsum.value_namespace = name_space
                    self.ospfiflsacksumsum.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfLsaCount"):
                    self.ospfiflsacount = value
                    self.ospfiflsacount.value_namespace = name_space
                    self.ospfiflsacount.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfMulticastForwarding"):
                    self.ospfifmulticastforwarding = value
                    self.ospfifmulticastforwarding.value_namespace = name_space
                    self.ospfifmulticastforwarding.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfPollInterval"):
                    self.ospfifpollinterval = value
                    self.ospfifpollinterval.value_namespace = name_space
                    self.ospfifpollinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfRetransInterval"):
                    self.ospfifretransinterval = value
                    self.ospfifretransinterval.value_namespace = name_space
                    self.ospfifretransinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfRtrDeadInterval"):
                    self.ospfifrtrdeadinterval = value
                    self.ospfifrtrdeadinterval.value_namespace = name_space
                    self.ospfifrtrdeadinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfRtrPriority"):
                    self.ospfifrtrpriority = value
                    self.ospfifrtrpriority.value_namespace = name_space
                    self.ospfifrtrpriority.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfState"):
                    self.ospfifstate = value
                    self.ospfifstate.value_namespace = name_space
                    self.ospfifstate.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfStatus"):
                    self.ospfifstatus = value
                    self.ospfifstatus.value_namespace = name_space
                    self.ospfifstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfTransitDelay"):
                    self.ospfiftransitdelay = value
                    self.ospfiftransitdelay.value_namespace = name_space
                    self.ospfiftransitdelay.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfType"):
                    self.ospfiftype = value
                    self.ospfiftype.value_namespace = name_space
                    self.ospfiftype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ospfifentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ospfifentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ospfIfTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "OSPF-MIB:OSPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ospfIfEntry"):
                for c in self.ospfifentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = OspfMib.Ospfiftable.Ospfifentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ospfifentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ospfIfEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Ospfifmetricentry <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfifmetrictable.Ospfifmetricentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OspfMib.Ospfifmetrictable, self).__init__()

            self.yang_name = "ospfIfMetricTable"
            self.yang_parent_name = "OSPF-MIB"

            self.ospfifmetricentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(OspfMib.Ospfifmetrictable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(OspfMib.Ospfifmetrictable, self).__setattr__(name, value)


        class Ospfifmetricentry(Entity):
            """
            A particular TOS metric for a non\-virtual interface
            identified by the interface index.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            storage.
            
            .. attribute:: ospfifmetricipaddress  <key>
            
            	The IP address of this OSPF interface.  On row creation, this can be derived from the instance
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfifmetricaddresslessif  <key>
            
            	For the purpose of easing the instancing of addressed and addressless interfaces; this variable takes the value 0 on interfaces with IP addresses and the value of ifIndex for interfaces having no IP address.  On row creation, this can be derived from the instance
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ospfifmetrictos  <key>
            
            	The Type of Service metric being referenced. On row creation, this can be derived from the instance
            	**type**\:  int
            
            	**range:** 0..30
            
            .. attribute:: ospfifmetricstatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: ospfifmetricvalue
            
            	The metric of using this Type of Service on this interface.  The default value of the TOS 0 metric is 10^8 / ifSpeed
            	**type**\:  int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OspfMib.Ospfifmetrictable.Ospfifmetricentry, self).__init__()

                self.yang_name = "ospfIfMetricEntry"
                self.yang_parent_name = "ospfIfMetricTable"

                self.ospfifmetricipaddress = YLeaf(YType.str, "ospfIfMetricIpAddress")

                self.ospfifmetricaddresslessif = YLeaf(YType.int32, "ospfIfMetricAddressLessIf")

                self.ospfifmetrictos = YLeaf(YType.int32, "ospfIfMetricTOS")

                self.ospfifmetricstatus = YLeaf(YType.enumeration, "ospfIfMetricStatus")

                self.ospfifmetricvalue = YLeaf(YType.int32, "ospfIfMetricValue")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ospfifmetricipaddress",
                                "ospfifmetricaddresslessif",
                                "ospfifmetrictos",
                                "ospfifmetricstatus",
                                "ospfifmetricvalue") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(OspfMib.Ospfifmetrictable.Ospfifmetricentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(OspfMib.Ospfifmetrictable.Ospfifmetricentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ospfifmetricipaddress.is_set or
                    self.ospfifmetricaddresslessif.is_set or
                    self.ospfifmetrictos.is_set or
                    self.ospfifmetricstatus.is_set or
                    self.ospfifmetricvalue.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ospfifmetricipaddress.yfilter != YFilter.not_set or
                    self.ospfifmetricaddresslessif.yfilter != YFilter.not_set or
                    self.ospfifmetrictos.yfilter != YFilter.not_set or
                    self.ospfifmetricstatus.yfilter != YFilter.not_set or
                    self.ospfifmetricvalue.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ospfIfMetricEntry" + "[ospfIfMetricIpAddress='" + self.ospfifmetricipaddress.get() + "']" + "[ospfIfMetricAddressLessIf='" + self.ospfifmetricaddresslessif.get() + "']" + "[ospfIfMetricTOS='" + self.ospfifmetrictos.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "OSPF-MIB:OSPF-MIB/ospfIfMetricTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ospfifmetricipaddress.is_set or self.ospfifmetricipaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfifmetricipaddress.get_name_leafdata())
                if (self.ospfifmetricaddresslessif.is_set or self.ospfifmetricaddresslessif.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfifmetricaddresslessif.get_name_leafdata())
                if (self.ospfifmetrictos.is_set or self.ospfifmetrictos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfifmetrictos.get_name_leafdata())
                if (self.ospfifmetricstatus.is_set or self.ospfifmetricstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfifmetricstatus.get_name_leafdata())
                if (self.ospfifmetricvalue.is_set or self.ospfifmetricvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfifmetricvalue.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ospfIfMetricIpAddress" or name == "ospfIfMetricAddressLessIf" or name == "ospfIfMetricTOS" or name == "ospfIfMetricStatus" or name == "ospfIfMetricValue"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ospfIfMetricIpAddress"):
                    self.ospfifmetricipaddress = value
                    self.ospfifmetricipaddress.value_namespace = name_space
                    self.ospfifmetricipaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfMetricAddressLessIf"):
                    self.ospfifmetricaddresslessif = value
                    self.ospfifmetricaddresslessif.value_namespace = name_space
                    self.ospfifmetricaddresslessif.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfMetricTOS"):
                    self.ospfifmetrictos = value
                    self.ospfifmetrictos.value_namespace = name_space
                    self.ospfifmetrictos.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfMetricStatus"):
                    self.ospfifmetricstatus = value
                    self.ospfifmetricstatus.value_namespace = name_space
                    self.ospfifmetricstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfIfMetricValue"):
                    self.ospfifmetricvalue = value
                    self.ospfifmetricvalue.value_namespace = name_space
                    self.ospfifmetricvalue.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ospfifmetricentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ospfifmetricentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ospfIfMetricTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "OSPF-MIB:OSPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ospfIfMetricEntry"):
                for c in self.ospfifmetricentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = OspfMib.Ospfifmetrictable.Ospfifmetricentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ospfifmetricentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ospfIfMetricEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ospfvirtiftable(Entity):
        """
        Information about this router's virtual interfaces
        that the OSPF Process is configured to carry on.
        
        .. attribute:: ospfvirtifentry
        
        	Information about a single virtual interface.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile storage
        	**type**\: list of    :py:class:`Ospfvirtifentry <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfvirtiftable.Ospfvirtifentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OspfMib.Ospfvirtiftable, self).__init__()

            self.yang_name = "ospfVirtIfTable"
            self.yang_parent_name = "OSPF-MIB"

            self.ospfvirtifentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(OspfMib.Ospfvirtiftable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(OspfMib.Ospfvirtiftable, self).__setattr__(name, value)


        class Ospfvirtifentry(Entity):
            """
            Information about a single virtual interface.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            storage.
            
            .. attribute:: ospfvirtifareaid  <key>
            
            	The transit area that the virtual link traverses.  By definition, this is not 0.0.0.0
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfvirtifneighbor  <key>
            
            	The Router ID of the virtual neighbor
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfvirtiflsacksumsum
            
            	The 32\-bit unsigned sum of the link\-state advertisements' LS checksums contained in this virtual interface's link\-local link state database. The sum can be used to determine if there has been a change in the virtual interface's link state database, and to compare the virtual interface link\-state database of the virtual neighbors
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfvirtiflsacount
            
            	The total number of link\-local link state advertisements in this virtual interface's link\-local link state database
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfvirtifauthkey
            
            	The cleartext password used as an OSPF authentication key when simplePassword security is enabled.  This object does not access any OSPF cryptogaphic (e.g., MD5) authentication key under any circumstance.  If the key length is shorter than 8 octets, the agent will left adjust and zero fill to 8 octets.  Unauthenticated interfaces need no authentication key, and simple password authentication cannot use a key of more than 8 octets.  Note that the use of simplePassword authentication is NOT recommended when there is concern regarding attack upon the OSPF system.  SimplePassword authentication is only sufficient to protect against accidental misconfigurations because it re\-uses cleartext passwords.  [RFC1704]  When read, ospfIfAuthKey always returns an octet string of length zero
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: ospfvirtifauthtype
            
            	The authentication type specified for a virtual interface.  Note that this object can be used to engage in significant attacks against an OSPF router
            	**type**\:   :py:class:`Ospfauthenticationtype <ydk.models.cisco_ios_xe.OSPF_MIB.Ospfauthenticationtype>`
            
            .. attribute:: ospfvirtifevents
            
            	The number of state changes or error events on this virtual link.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ospfDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfvirtifhellointerval
            
            	The length of time, in seconds, between the Hello packets that the router sends on the interface.  This value must be the same for the virtual neighbor
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**units**\: seconds
            
            .. attribute:: ospfvirtiflsacksumsum
            
            	The 32\-bit unsigned sum of the link state advertisements' LS checksums contained in this virtual interface's link\-local link state database. The sum can be used to determine if there has been a change in the virtual interface's link state database, and to compare the virtual interface link state database of the virtual neighbors
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfvirtiflsacount
            
            	The total number of link\-local link state advertisements in this virtual interface's link\-local link state database
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfvirtifretransinterval
            
            	The number of seconds between link state avertisement retransmissions, for adjacencies belonging to this interface.  This value is also used when retransmitting database description and Link State request packets.  This value should be well over the expected round\-trip time.  Note that the minimal value SHOULD be 1 second
            	**type**\:  int
            
            	**range:** 0..3600
            
            	**units**\: seconds
            
            .. attribute:: ospfvirtifrtrdeadinterval
            
            	The number of seconds that a router's Hello packets have not been seen before its neighbors declare the router down.  This should be some multiple of the Hello interval.  This value must be the same for the virtual neighbor
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: ospfvirtifstate
            
            	OSPF virtual interface states
            	**type**\:   :py:class:`Ospfvirtifstate <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfvirtiftable.Ospfvirtifentry.Ospfvirtifstate>`
            
            .. attribute:: ospfvirtifstatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: ospfvirtiftransitdelay
            
            	The estimated number of seconds it takes to transmit a Link State update packet over this interface.  Note that the minimal value SHOULD be 1 second
            	**type**\:  int
            
            	**range:** 0..3600
            
            	**units**\: seconds
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OspfMib.Ospfvirtiftable.Ospfvirtifentry, self).__init__()

                self.yang_name = "ospfVirtIfEntry"
                self.yang_parent_name = "ospfVirtIfTable"

                self.ospfvirtifareaid = YLeaf(YType.str, "ospfVirtIfAreaId")

                self.ospfvirtifneighbor = YLeaf(YType.str, "ospfVirtIfNeighbor")

                self.cospfvirtiflsacksumsum = YLeaf(YType.uint32, "CISCO-OSPF-MIB:cospfVirtIfLsaCksumSum")

                self.cospfvirtiflsacount = YLeaf(YType.uint32, "CISCO-OSPF-MIB:cospfVirtIfLsaCount")

                self.ospfvirtifauthkey = YLeaf(YType.str, "ospfVirtIfAuthKey")

                self.ospfvirtifauthtype = YLeaf(YType.enumeration, "ospfVirtIfAuthType")

                self.ospfvirtifevents = YLeaf(YType.uint32, "ospfVirtIfEvents")

                self.ospfvirtifhellointerval = YLeaf(YType.int32, "ospfVirtIfHelloInterval")

                self.ospfvirtiflsacksumsum = YLeaf(YType.uint32, "ospfVirtIfLsaCksumSum")

                self.ospfvirtiflsacount = YLeaf(YType.uint32, "ospfVirtIfLsaCount")

                self.ospfvirtifretransinterval = YLeaf(YType.int32, "ospfVirtIfRetransInterval")

                self.ospfvirtifrtrdeadinterval = YLeaf(YType.int32, "ospfVirtIfRtrDeadInterval")

                self.ospfvirtifstate = YLeaf(YType.enumeration, "ospfVirtIfState")

                self.ospfvirtifstatus = YLeaf(YType.enumeration, "ospfVirtIfStatus")

                self.ospfvirtiftransitdelay = YLeaf(YType.int32, "ospfVirtIfTransitDelay")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ospfvirtifareaid",
                                "ospfvirtifneighbor",
                                "cospfvirtiflsacksumsum",
                                "cospfvirtiflsacount",
                                "ospfvirtifauthkey",
                                "ospfvirtifauthtype",
                                "ospfvirtifevents",
                                "ospfvirtifhellointerval",
                                "ospfvirtiflsacksumsum",
                                "ospfvirtiflsacount",
                                "ospfvirtifretransinterval",
                                "ospfvirtifrtrdeadinterval",
                                "ospfvirtifstate",
                                "ospfvirtifstatus",
                                "ospfvirtiftransitdelay") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(OspfMib.Ospfvirtiftable.Ospfvirtifentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(OspfMib.Ospfvirtiftable.Ospfvirtifentry, self).__setattr__(name, value)

            class Ospfvirtifstate(Enum):
                """
                Ospfvirtifstate

                OSPF virtual interface states.

                .. data:: down = 1

                .. data:: pointToPoint = 4

                """

                down = Enum.YLeaf(1, "down")

                pointToPoint = Enum.YLeaf(4, "pointToPoint")


            def has_data(self):
                return (
                    self.ospfvirtifareaid.is_set or
                    self.ospfvirtifneighbor.is_set or
                    self.cospfvirtiflsacksumsum.is_set or
                    self.cospfvirtiflsacount.is_set or
                    self.ospfvirtifauthkey.is_set or
                    self.ospfvirtifauthtype.is_set or
                    self.ospfvirtifevents.is_set or
                    self.ospfvirtifhellointerval.is_set or
                    self.ospfvirtiflsacksumsum.is_set or
                    self.ospfvirtiflsacount.is_set or
                    self.ospfvirtifretransinterval.is_set or
                    self.ospfvirtifrtrdeadinterval.is_set or
                    self.ospfvirtifstate.is_set or
                    self.ospfvirtifstatus.is_set or
                    self.ospfvirtiftransitdelay.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ospfvirtifareaid.yfilter != YFilter.not_set or
                    self.ospfvirtifneighbor.yfilter != YFilter.not_set or
                    self.cospfvirtiflsacksumsum.yfilter != YFilter.not_set or
                    self.cospfvirtiflsacount.yfilter != YFilter.not_set or
                    self.ospfvirtifauthkey.yfilter != YFilter.not_set or
                    self.ospfvirtifauthtype.yfilter != YFilter.not_set or
                    self.ospfvirtifevents.yfilter != YFilter.not_set or
                    self.ospfvirtifhellointerval.yfilter != YFilter.not_set or
                    self.ospfvirtiflsacksumsum.yfilter != YFilter.not_set or
                    self.ospfvirtiflsacount.yfilter != YFilter.not_set or
                    self.ospfvirtifretransinterval.yfilter != YFilter.not_set or
                    self.ospfvirtifrtrdeadinterval.yfilter != YFilter.not_set or
                    self.ospfvirtifstate.yfilter != YFilter.not_set or
                    self.ospfvirtifstatus.yfilter != YFilter.not_set or
                    self.ospfvirtiftransitdelay.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ospfVirtIfEntry" + "[ospfVirtIfAreaId='" + self.ospfvirtifareaid.get() + "']" + "[ospfVirtIfNeighbor='" + self.ospfvirtifneighbor.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "OSPF-MIB:OSPF-MIB/ospfVirtIfTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ospfvirtifareaid.is_set or self.ospfvirtifareaid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtifareaid.get_name_leafdata())
                if (self.ospfvirtifneighbor.is_set or self.ospfvirtifneighbor.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtifneighbor.get_name_leafdata())
                if (self.cospfvirtiflsacksumsum.is_set or self.cospfvirtiflsacksumsum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfvirtiflsacksumsum.get_name_leafdata())
                if (self.cospfvirtiflsacount.is_set or self.cospfvirtiflsacount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfvirtiflsacount.get_name_leafdata())
                if (self.ospfvirtifauthkey.is_set or self.ospfvirtifauthkey.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtifauthkey.get_name_leafdata())
                if (self.ospfvirtifauthtype.is_set or self.ospfvirtifauthtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtifauthtype.get_name_leafdata())
                if (self.ospfvirtifevents.is_set or self.ospfvirtifevents.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtifevents.get_name_leafdata())
                if (self.ospfvirtifhellointerval.is_set or self.ospfvirtifhellointerval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtifhellointerval.get_name_leafdata())
                if (self.ospfvirtiflsacksumsum.is_set or self.ospfvirtiflsacksumsum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtiflsacksumsum.get_name_leafdata())
                if (self.ospfvirtiflsacount.is_set or self.ospfvirtiflsacount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtiflsacount.get_name_leafdata())
                if (self.ospfvirtifretransinterval.is_set or self.ospfvirtifretransinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtifretransinterval.get_name_leafdata())
                if (self.ospfvirtifrtrdeadinterval.is_set or self.ospfvirtifrtrdeadinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtifrtrdeadinterval.get_name_leafdata())
                if (self.ospfvirtifstate.is_set or self.ospfvirtifstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtifstate.get_name_leafdata())
                if (self.ospfvirtifstatus.is_set or self.ospfvirtifstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtifstatus.get_name_leafdata())
                if (self.ospfvirtiftransitdelay.is_set or self.ospfvirtiftransitdelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtiftransitdelay.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ospfVirtIfAreaId" or name == "ospfVirtIfNeighbor" or name == "cospfVirtIfLsaCksumSum" or name == "cospfVirtIfLsaCount" or name == "ospfVirtIfAuthKey" or name == "ospfVirtIfAuthType" or name == "ospfVirtIfEvents" or name == "ospfVirtIfHelloInterval" or name == "ospfVirtIfLsaCksumSum" or name == "ospfVirtIfLsaCount" or name == "ospfVirtIfRetransInterval" or name == "ospfVirtIfRtrDeadInterval" or name == "ospfVirtIfState" or name == "ospfVirtIfStatus" or name == "ospfVirtIfTransitDelay"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ospfVirtIfAreaId"):
                    self.ospfvirtifareaid = value
                    self.ospfvirtifareaid.value_namespace = name_space
                    self.ospfvirtifareaid.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtIfNeighbor"):
                    self.ospfvirtifneighbor = value
                    self.ospfvirtifneighbor.value_namespace = name_space
                    self.ospfvirtifneighbor.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfVirtIfLsaCksumSum"):
                    self.cospfvirtiflsacksumsum = value
                    self.cospfvirtiflsacksumsum.value_namespace = name_space
                    self.cospfvirtiflsacksumsum.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfVirtIfLsaCount"):
                    self.cospfvirtiflsacount = value
                    self.cospfvirtiflsacount.value_namespace = name_space
                    self.cospfvirtiflsacount.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtIfAuthKey"):
                    self.ospfvirtifauthkey = value
                    self.ospfvirtifauthkey.value_namespace = name_space
                    self.ospfvirtifauthkey.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtIfAuthType"):
                    self.ospfvirtifauthtype = value
                    self.ospfvirtifauthtype.value_namespace = name_space
                    self.ospfvirtifauthtype.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtIfEvents"):
                    self.ospfvirtifevents = value
                    self.ospfvirtifevents.value_namespace = name_space
                    self.ospfvirtifevents.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtIfHelloInterval"):
                    self.ospfvirtifhellointerval = value
                    self.ospfvirtifhellointerval.value_namespace = name_space
                    self.ospfvirtifhellointerval.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtIfLsaCksumSum"):
                    self.ospfvirtiflsacksumsum = value
                    self.ospfvirtiflsacksumsum.value_namespace = name_space
                    self.ospfvirtiflsacksumsum.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtIfLsaCount"):
                    self.ospfvirtiflsacount = value
                    self.ospfvirtiflsacount.value_namespace = name_space
                    self.ospfvirtiflsacount.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtIfRetransInterval"):
                    self.ospfvirtifretransinterval = value
                    self.ospfvirtifretransinterval.value_namespace = name_space
                    self.ospfvirtifretransinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtIfRtrDeadInterval"):
                    self.ospfvirtifrtrdeadinterval = value
                    self.ospfvirtifrtrdeadinterval.value_namespace = name_space
                    self.ospfvirtifrtrdeadinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtIfState"):
                    self.ospfvirtifstate = value
                    self.ospfvirtifstate.value_namespace = name_space
                    self.ospfvirtifstate.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtIfStatus"):
                    self.ospfvirtifstatus = value
                    self.ospfvirtifstatus.value_namespace = name_space
                    self.ospfvirtifstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtIfTransitDelay"):
                    self.ospfvirtiftransitdelay = value
                    self.ospfvirtiftransitdelay.value_namespace = name_space
                    self.ospfvirtiftransitdelay.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ospfvirtifentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ospfvirtifentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ospfVirtIfTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "OSPF-MIB:OSPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ospfVirtIfEntry"):
                for c in self.ospfvirtifentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = OspfMib.Ospfvirtiftable.Ospfvirtifentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ospfvirtifentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ospfVirtIfEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ospfnbrtable(Entity):
        """
        A table describing all non\-virtual neighbors
        in the locality of the OSPF router.
        
        .. attribute:: ospfnbrentry
        
        	The information regarding a single neighbor.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile  storage
        	**type**\: list of    :py:class:`Ospfnbrentry <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfnbrtable.Ospfnbrentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OspfMib.Ospfnbrtable, self).__init__()

            self.yang_name = "ospfNbrTable"
            self.yang_parent_name = "OSPF-MIB"

            self.ospfnbrentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(OspfMib.Ospfnbrtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(OspfMib.Ospfnbrtable, self).__setattr__(name, value)


        class Ospfnbrentry(Entity):
            """
            The information regarding a single neighbor.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            
            storage.
            
            .. attribute:: ospfnbripaddr  <key>
            
            	The IP address this neighbor is using in its IP source address.  Note that, on addressless links, this will not be 0.0.0.0 but the  address of another of the neighbor's interfaces
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfnbraddresslessindex  <key>
            
            	On an interface having an IP address, zero. On addressless interfaces, the corresponding value of ifIndex in the Internet Standard MIB. On row creation, this can be derived from the instance
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ospfnbmanbrpermanence
            
            	This variable displays the status of the entry; 'dynamic' and 'permanent' refer to how the neighbor became known
            	**type**\:   :py:class:`Ospfnbmanbrpermanence <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfnbrtable.Ospfnbrentry.Ospfnbmanbrpermanence>`
            
            .. attribute:: ospfnbmanbrstatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: ospfnbrevents
            
            	The number of times this neighbor relationship has changed state or an error has occurred.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ospfDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfnbrhellosuppressed
            
            	Indicates whether Hellos are being suppressed to the neighbor
            	**type**\:  bool
            
            .. attribute:: ospfnbrlsretransqlen
            
            	The current length of the retransmission queue
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfnbroptions
            
            	A bit mask corresponding to the neighbor's options field.  Bit 0, if set, indicates that the system will operate on Type of Service metrics other than TOS 0.  If zero, the neighbor will ignore all metrics except the TOS 0 metric.  Bit 1, if set, indicates that the associated area accepts and operates on external information; if zero, it is a stub area.  Bit 2, if set, indicates that the system is capable of routing IP multicast datagrams, that is that it implements the multicast extensions to OSPF.  Bit 3, if set, indicates that the associated area is an NSSA.  These areas are capable of carrying type\-7 external advertisements, which are translated into type\-5 external advertisements at NSSA borders
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospfnbrpriority
            
            	The priority of this neighbor in the designated router election algorithm.  The value 0 signifies that the neighbor is not eligible to become the designated router on this particular network
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: ospfnbrrestarthelperage
            
            	Remaining time in current OSPF graceful restart interval, if the router is acting as a restart helper for the neighbor
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: ospfnbrrestarthelperexitreason
            
            	Describes the outcome of the last attempt at acting as a graceful restart helper for the neighbor
            	**type**\:   :py:class:`Ospfnbrrestarthelperexitreason <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfnbrtable.Ospfnbrentry.Ospfnbrrestarthelperexitreason>`
            
            .. attribute:: ospfnbrrestarthelperstatus
            
            	Indicates whether the router is acting as a graceful restart helper for the neighbor
            	**type**\:   :py:class:`Ospfnbrrestarthelperstatus <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfnbrtable.Ospfnbrentry.Ospfnbrrestarthelperstatus>`
            
            .. attribute:: ospfnbrrtrid
            
            	A 32\-bit integer (represented as a type IpAddress) uniquely identifying the neighboring router in the Autonomous System
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfnbrstate
            
            	The state of the relationship with this neighbor
            	**type**\:   :py:class:`Ospfnbrstate <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfnbrtable.Ospfnbrentry.Ospfnbrstate>`
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OspfMib.Ospfnbrtable.Ospfnbrentry, self).__init__()

                self.yang_name = "ospfNbrEntry"
                self.yang_parent_name = "ospfNbrTable"

                self.ospfnbripaddr = YLeaf(YType.str, "ospfNbrIpAddr")

                self.ospfnbraddresslessindex = YLeaf(YType.int32, "ospfNbrAddressLessIndex")

                self.ospfnbmanbrpermanence = YLeaf(YType.enumeration, "ospfNbmaNbrPermanence")

                self.ospfnbmanbrstatus = YLeaf(YType.enumeration, "ospfNbmaNbrStatus")

                self.ospfnbrevents = YLeaf(YType.uint32, "ospfNbrEvents")

                self.ospfnbrhellosuppressed = YLeaf(YType.boolean, "ospfNbrHelloSuppressed")

                self.ospfnbrlsretransqlen = YLeaf(YType.uint32, "ospfNbrLsRetransQLen")

                self.ospfnbroptions = YLeaf(YType.int32, "ospfNbrOptions")

                self.ospfnbrpriority = YLeaf(YType.int32, "ospfNbrPriority")

                self.ospfnbrrestarthelperage = YLeaf(YType.uint32, "ospfNbrRestartHelperAge")

                self.ospfnbrrestarthelperexitreason = YLeaf(YType.enumeration, "ospfNbrRestartHelperExitReason")

                self.ospfnbrrestarthelperstatus = YLeaf(YType.enumeration, "ospfNbrRestartHelperStatus")

                self.ospfnbrrtrid = YLeaf(YType.str, "ospfNbrRtrId")

                self.ospfnbrstate = YLeaf(YType.enumeration, "ospfNbrState")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ospfnbripaddr",
                                "ospfnbraddresslessindex",
                                "ospfnbmanbrpermanence",
                                "ospfnbmanbrstatus",
                                "ospfnbrevents",
                                "ospfnbrhellosuppressed",
                                "ospfnbrlsretransqlen",
                                "ospfnbroptions",
                                "ospfnbrpriority",
                                "ospfnbrrestarthelperage",
                                "ospfnbrrestarthelperexitreason",
                                "ospfnbrrestarthelperstatus",
                                "ospfnbrrtrid",
                                "ospfnbrstate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(OspfMib.Ospfnbrtable.Ospfnbrentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(OspfMib.Ospfnbrtable.Ospfnbrentry, self).__setattr__(name, value)

            class Ospfnbmanbrpermanence(Enum):
                """
                Ospfnbmanbrpermanence

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
                Ospfnbrrestarthelperexitreason

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
                Ospfnbrrestarthelperstatus

                Indicates whether the router is acting

                as a graceful restart helper for the neighbor.

                .. data:: notHelping = 1

                .. data:: helping = 2

                """

                notHelping = Enum.YLeaf(1, "notHelping")

                helping = Enum.YLeaf(2, "helping")


            class Ospfnbrstate(Enum):
                """
                Ospfnbrstate

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


            def has_data(self):
                return (
                    self.ospfnbripaddr.is_set or
                    self.ospfnbraddresslessindex.is_set or
                    self.ospfnbmanbrpermanence.is_set or
                    self.ospfnbmanbrstatus.is_set or
                    self.ospfnbrevents.is_set or
                    self.ospfnbrhellosuppressed.is_set or
                    self.ospfnbrlsretransqlen.is_set or
                    self.ospfnbroptions.is_set or
                    self.ospfnbrpriority.is_set or
                    self.ospfnbrrestarthelperage.is_set or
                    self.ospfnbrrestarthelperexitreason.is_set or
                    self.ospfnbrrestarthelperstatus.is_set or
                    self.ospfnbrrtrid.is_set or
                    self.ospfnbrstate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ospfnbripaddr.yfilter != YFilter.not_set or
                    self.ospfnbraddresslessindex.yfilter != YFilter.not_set or
                    self.ospfnbmanbrpermanence.yfilter != YFilter.not_set or
                    self.ospfnbmanbrstatus.yfilter != YFilter.not_set or
                    self.ospfnbrevents.yfilter != YFilter.not_set or
                    self.ospfnbrhellosuppressed.yfilter != YFilter.not_set or
                    self.ospfnbrlsretransqlen.yfilter != YFilter.not_set or
                    self.ospfnbroptions.yfilter != YFilter.not_set or
                    self.ospfnbrpriority.yfilter != YFilter.not_set or
                    self.ospfnbrrestarthelperage.yfilter != YFilter.not_set or
                    self.ospfnbrrestarthelperexitreason.yfilter != YFilter.not_set or
                    self.ospfnbrrestarthelperstatus.yfilter != YFilter.not_set or
                    self.ospfnbrrtrid.yfilter != YFilter.not_set or
                    self.ospfnbrstate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ospfNbrEntry" + "[ospfNbrIpAddr='" + self.ospfnbripaddr.get() + "']" + "[ospfNbrAddressLessIndex='" + self.ospfnbraddresslessindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "OSPF-MIB:OSPF-MIB/ospfNbrTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ospfnbripaddr.is_set or self.ospfnbripaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfnbripaddr.get_name_leafdata())
                if (self.ospfnbraddresslessindex.is_set or self.ospfnbraddresslessindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfnbraddresslessindex.get_name_leafdata())
                if (self.ospfnbmanbrpermanence.is_set or self.ospfnbmanbrpermanence.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfnbmanbrpermanence.get_name_leafdata())
                if (self.ospfnbmanbrstatus.is_set or self.ospfnbmanbrstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfnbmanbrstatus.get_name_leafdata())
                if (self.ospfnbrevents.is_set or self.ospfnbrevents.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfnbrevents.get_name_leafdata())
                if (self.ospfnbrhellosuppressed.is_set or self.ospfnbrhellosuppressed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfnbrhellosuppressed.get_name_leafdata())
                if (self.ospfnbrlsretransqlen.is_set or self.ospfnbrlsretransqlen.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfnbrlsretransqlen.get_name_leafdata())
                if (self.ospfnbroptions.is_set or self.ospfnbroptions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfnbroptions.get_name_leafdata())
                if (self.ospfnbrpriority.is_set or self.ospfnbrpriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfnbrpriority.get_name_leafdata())
                if (self.ospfnbrrestarthelperage.is_set or self.ospfnbrrestarthelperage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfnbrrestarthelperage.get_name_leafdata())
                if (self.ospfnbrrestarthelperexitreason.is_set or self.ospfnbrrestarthelperexitreason.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfnbrrestarthelperexitreason.get_name_leafdata())
                if (self.ospfnbrrestarthelperstatus.is_set or self.ospfnbrrestarthelperstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfnbrrestarthelperstatus.get_name_leafdata())
                if (self.ospfnbrrtrid.is_set or self.ospfnbrrtrid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfnbrrtrid.get_name_leafdata())
                if (self.ospfnbrstate.is_set or self.ospfnbrstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfnbrstate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ospfNbrIpAddr" or name == "ospfNbrAddressLessIndex" or name == "ospfNbmaNbrPermanence" or name == "ospfNbmaNbrStatus" or name == "ospfNbrEvents" or name == "ospfNbrHelloSuppressed" or name == "ospfNbrLsRetransQLen" or name == "ospfNbrOptions" or name == "ospfNbrPriority" or name == "ospfNbrRestartHelperAge" or name == "ospfNbrRestartHelperExitReason" or name == "ospfNbrRestartHelperStatus" or name == "ospfNbrRtrId" or name == "ospfNbrState"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ospfNbrIpAddr"):
                    self.ospfnbripaddr = value
                    self.ospfnbripaddr.value_namespace = name_space
                    self.ospfnbripaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfNbrAddressLessIndex"):
                    self.ospfnbraddresslessindex = value
                    self.ospfnbraddresslessindex.value_namespace = name_space
                    self.ospfnbraddresslessindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfNbmaNbrPermanence"):
                    self.ospfnbmanbrpermanence = value
                    self.ospfnbmanbrpermanence.value_namespace = name_space
                    self.ospfnbmanbrpermanence.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfNbmaNbrStatus"):
                    self.ospfnbmanbrstatus = value
                    self.ospfnbmanbrstatus.value_namespace = name_space
                    self.ospfnbmanbrstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfNbrEvents"):
                    self.ospfnbrevents = value
                    self.ospfnbrevents.value_namespace = name_space
                    self.ospfnbrevents.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfNbrHelloSuppressed"):
                    self.ospfnbrhellosuppressed = value
                    self.ospfnbrhellosuppressed.value_namespace = name_space
                    self.ospfnbrhellosuppressed.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfNbrLsRetransQLen"):
                    self.ospfnbrlsretransqlen = value
                    self.ospfnbrlsretransqlen.value_namespace = name_space
                    self.ospfnbrlsretransqlen.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfNbrOptions"):
                    self.ospfnbroptions = value
                    self.ospfnbroptions.value_namespace = name_space
                    self.ospfnbroptions.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfNbrPriority"):
                    self.ospfnbrpriority = value
                    self.ospfnbrpriority.value_namespace = name_space
                    self.ospfnbrpriority.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfNbrRestartHelperAge"):
                    self.ospfnbrrestarthelperage = value
                    self.ospfnbrrestarthelperage.value_namespace = name_space
                    self.ospfnbrrestarthelperage.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfNbrRestartHelperExitReason"):
                    self.ospfnbrrestarthelperexitreason = value
                    self.ospfnbrrestarthelperexitreason.value_namespace = name_space
                    self.ospfnbrrestarthelperexitreason.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfNbrRestartHelperStatus"):
                    self.ospfnbrrestarthelperstatus = value
                    self.ospfnbrrestarthelperstatus.value_namespace = name_space
                    self.ospfnbrrestarthelperstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfNbrRtrId"):
                    self.ospfnbrrtrid = value
                    self.ospfnbrrtrid.value_namespace = name_space
                    self.ospfnbrrtrid.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfNbrState"):
                    self.ospfnbrstate = value
                    self.ospfnbrstate.value_namespace = name_space
                    self.ospfnbrstate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ospfnbrentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ospfnbrentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ospfNbrTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "OSPF-MIB:OSPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ospfNbrEntry"):
                for c in self.ospfnbrentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = OspfMib.Ospfnbrtable.Ospfnbrentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ospfnbrentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ospfNbrEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ospfvirtnbrtable(Entity):
        """
        This table describes all virtual neighbors.
        Since virtual links are configured
        in the Virtual Interface Table, this table is read\-only.
        
        .. attribute:: ospfvirtnbrentry
        
        	Virtual neighbor information
        	**type**\: list of    :py:class:`Ospfvirtnbrentry <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfvirtnbrtable.Ospfvirtnbrentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OspfMib.Ospfvirtnbrtable, self).__init__()

            self.yang_name = "ospfVirtNbrTable"
            self.yang_parent_name = "OSPF-MIB"

            self.ospfvirtnbrentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(OspfMib.Ospfvirtnbrtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(OspfMib.Ospfvirtnbrtable, self).__setattr__(name, value)


        class Ospfvirtnbrentry(Entity):
            """
            Virtual neighbor information.
            
            .. attribute:: ospfvirtnbrarea  <key>
            
            	The Transit Area Identifier
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfvirtnbrrtrid  <key>
            
            	A 32\-bit integer uniquely identifying the neighboring router in the Autonomous System
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfvirtnbrevents
            
            	The number of times this virtual link has changed its state or an error has occurred.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ospfDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfvirtnbrhellosuppressed
            
            	Indicates whether Hellos are being suppressed to the neighbor
            	**type**\:  bool
            
            .. attribute:: ospfvirtnbripaddr
            
            	The IP address this virtual neighbor is using
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfvirtnbrlsretransqlen
            
            	The current length of the retransmission queue
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfvirtnbroptions
            
            	A bit mask corresponding to the neighbor's options field.  Bit 1, if set, indicates that the system will operate on Type of Service metrics other than TOS 0.  If zero, the neighbor will ignore all metrics except the TOS 0 metric.  Bit 2, if set, indicates that the system is network multicast capable, i.e., that it implements OSPF multicast routing
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospfvirtnbrrestarthelperage
            
            	Remaining time in current OSPF graceful restart interval, if the router is acting as a restart helper for the neighbor
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: ospfvirtnbrrestarthelperexitreason
            
            	Describes the outcome of the last attempt at acting as a graceful restart helper for the neighbor
            	**type**\:   :py:class:`Ospfvirtnbrrestarthelperexitreason <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfvirtnbrtable.Ospfvirtnbrentry.Ospfvirtnbrrestarthelperexitreason>`
            
            .. attribute:: ospfvirtnbrrestarthelperstatus
            
            	Indicates whether the router is acting as a graceful restart helper for the neighbor
            	**type**\:   :py:class:`Ospfvirtnbrrestarthelperstatus <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfvirtnbrtable.Ospfvirtnbrentry.Ospfvirtnbrrestarthelperstatus>`
            
            .. attribute:: ospfvirtnbrstate
            
            	The state of the virtual neighbor relationship
            	**type**\:   :py:class:`Ospfvirtnbrstate <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfvirtnbrtable.Ospfvirtnbrentry.Ospfvirtnbrstate>`
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OspfMib.Ospfvirtnbrtable.Ospfvirtnbrentry, self).__init__()

                self.yang_name = "ospfVirtNbrEntry"
                self.yang_parent_name = "ospfVirtNbrTable"

                self.ospfvirtnbrarea = YLeaf(YType.str, "ospfVirtNbrArea")

                self.ospfvirtnbrrtrid = YLeaf(YType.str, "ospfVirtNbrRtrId")

                self.ospfvirtnbrevents = YLeaf(YType.uint32, "ospfVirtNbrEvents")

                self.ospfvirtnbrhellosuppressed = YLeaf(YType.boolean, "ospfVirtNbrHelloSuppressed")

                self.ospfvirtnbripaddr = YLeaf(YType.str, "ospfVirtNbrIpAddr")

                self.ospfvirtnbrlsretransqlen = YLeaf(YType.uint32, "ospfVirtNbrLsRetransQLen")

                self.ospfvirtnbroptions = YLeaf(YType.int32, "ospfVirtNbrOptions")

                self.ospfvirtnbrrestarthelperage = YLeaf(YType.uint32, "ospfVirtNbrRestartHelperAge")

                self.ospfvirtnbrrestarthelperexitreason = YLeaf(YType.enumeration, "ospfVirtNbrRestartHelperExitReason")

                self.ospfvirtnbrrestarthelperstatus = YLeaf(YType.enumeration, "ospfVirtNbrRestartHelperStatus")

                self.ospfvirtnbrstate = YLeaf(YType.enumeration, "ospfVirtNbrState")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ospfvirtnbrarea",
                                "ospfvirtnbrrtrid",
                                "ospfvirtnbrevents",
                                "ospfvirtnbrhellosuppressed",
                                "ospfvirtnbripaddr",
                                "ospfvirtnbrlsretransqlen",
                                "ospfvirtnbroptions",
                                "ospfvirtnbrrestarthelperage",
                                "ospfvirtnbrrestarthelperexitreason",
                                "ospfvirtnbrrestarthelperstatus",
                                "ospfvirtnbrstate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(OspfMib.Ospfvirtnbrtable.Ospfvirtnbrentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(OspfMib.Ospfvirtnbrtable.Ospfvirtnbrentry, self).__setattr__(name, value)

            class Ospfvirtnbrrestarthelperexitreason(Enum):
                """
                Ospfvirtnbrrestarthelperexitreason

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
                Ospfvirtnbrrestarthelperstatus

                Indicates whether the router is acting

                as a graceful restart helper for the neighbor.

                .. data:: notHelping = 1

                .. data:: helping = 2

                """

                notHelping = Enum.YLeaf(1, "notHelping")

                helping = Enum.YLeaf(2, "helping")


            class Ospfvirtnbrstate(Enum):
                """
                Ospfvirtnbrstate

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


            def has_data(self):
                return (
                    self.ospfvirtnbrarea.is_set or
                    self.ospfvirtnbrrtrid.is_set or
                    self.ospfvirtnbrevents.is_set or
                    self.ospfvirtnbrhellosuppressed.is_set or
                    self.ospfvirtnbripaddr.is_set or
                    self.ospfvirtnbrlsretransqlen.is_set or
                    self.ospfvirtnbroptions.is_set or
                    self.ospfvirtnbrrestarthelperage.is_set or
                    self.ospfvirtnbrrestarthelperexitreason.is_set or
                    self.ospfvirtnbrrestarthelperstatus.is_set or
                    self.ospfvirtnbrstate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ospfvirtnbrarea.yfilter != YFilter.not_set or
                    self.ospfvirtnbrrtrid.yfilter != YFilter.not_set or
                    self.ospfvirtnbrevents.yfilter != YFilter.not_set or
                    self.ospfvirtnbrhellosuppressed.yfilter != YFilter.not_set or
                    self.ospfvirtnbripaddr.yfilter != YFilter.not_set or
                    self.ospfvirtnbrlsretransqlen.yfilter != YFilter.not_set or
                    self.ospfvirtnbroptions.yfilter != YFilter.not_set or
                    self.ospfvirtnbrrestarthelperage.yfilter != YFilter.not_set or
                    self.ospfvirtnbrrestarthelperexitreason.yfilter != YFilter.not_set or
                    self.ospfvirtnbrrestarthelperstatus.yfilter != YFilter.not_set or
                    self.ospfvirtnbrstate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ospfVirtNbrEntry" + "[ospfVirtNbrArea='" + self.ospfvirtnbrarea.get() + "']" + "[ospfVirtNbrRtrId='" + self.ospfvirtnbrrtrid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "OSPF-MIB:OSPF-MIB/ospfVirtNbrTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ospfvirtnbrarea.is_set or self.ospfvirtnbrarea.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtnbrarea.get_name_leafdata())
                if (self.ospfvirtnbrrtrid.is_set or self.ospfvirtnbrrtrid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtnbrrtrid.get_name_leafdata())
                if (self.ospfvirtnbrevents.is_set or self.ospfvirtnbrevents.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtnbrevents.get_name_leafdata())
                if (self.ospfvirtnbrhellosuppressed.is_set or self.ospfvirtnbrhellosuppressed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtnbrhellosuppressed.get_name_leafdata())
                if (self.ospfvirtnbripaddr.is_set or self.ospfvirtnbripaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtnbripaddr.get_name_leafdata())
                if (self.ospfvirtnbrlsretransqlen.is_set or self.ospfvirtnbrlsretransqlen.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtnbrlsretransqlen.get_name_leafdata())
                if (self.ospfvirtnbroptions.is_set or self.ospfvirtnbroptions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtnbroptions.get_name_leafdata())
                if (self.ospfvirtnbrrestarthelperage.is_set or self.ospfvirtnbrrestarthelperage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtnbrrestarthelperage.get_name_leafdata())
                if (self.ospfvirtnbrrestarthelperexitreason.is_set or self.ospfvirtnbrrestarthelperexitreason.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtnbrrestarthelperexitreason.get_name_leafdata())
                if (self.ospfvirtnbrrestarthelperstatus.is_set or self.ospfvirtnbrrestarthelperstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtnbrrestarthelperstatus.get_name_leafdata())
                if (self.ospfvirtnbrstate.is_set or self.ospfvirtnbrstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtnbrstate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ospfVirtNbrArea" or name == "ospfVirtNbrRtrId" or name == "ospfVirtNbrEvents" or name == "ospfVirtNbrHelloSuppressed" or name == "ospfVirtNbrIpAddr" or name == "ospfVirtNbrLsRetransQLen" or name == "ospfVirtNbrOptions" or name == "ospfVirtNbrRestartHelperAge" or name == "ospfVirtNbrRestartHelperExitReason" or name == "ospfVirtNbrRestartHelperStatus" or name == "ospfVirtNbrState"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ospfVirtNbrArea"):
                    self.ospfvirtnbrarea = value
                    self.ospfvirtnbrarea.value_namespace = name_space
                    self.ospfvirtnbrarea.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtNbrRtrId"):
                    self.ospfvirtnbrrtrid = value
                    self.ospfvirtnbrrtrid.value_namespace = name_space
                    self.ospfvirtnbrrtrid.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtNbrEvents"):
                    self.ospfvirtnbrevents = value
                    self.ospfvirtnbrevents.value_namespace = name_space
                    self.ospfvirtnbrevents.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtNbrHelloSuppressed"):
                    self.ospfvirtnbrhellosuppressed = value
                    self.ospfvirtnbrhellosuppressed.value_namespace = name_space
                    self.ospfvirtnbrhellosuppressed.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtNbrIpAddr"):
                    self.ospfvirtnbripaddr = value
                    self.ospfvirtnbripaddr.value_namespace = name_space
                    self.ospfvirtnbripaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtNbrLsRetransQLen"):
                    self.ospfvirtnbrlsretransqlen = value
                    self.ospfvirtnbrlsretransqlen.value_namespace = name_space
                    self.ospfvirtnbrlsretransqlen.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtNbrOptions"):
                    self.ospfvirtnbroptions = value
                    self.ospfvirtnbroptions.value_namespace = name_space
                    self.ospfvirtnbroptions.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtNbrRestartHelperAge"):
                    self.ospfvirtnbrrestarthelperage = value
                    self.ospfvirtnbrrestarthelperage.value_namespace = name_space
                    self.ospfvirtnbrrestarthelperage.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtNbrRestartHelperExitReason"):
                    self.ospfvirtnbrrestarthelperexitreason = value
                    self.ospfvirtnbrrestarthelperexitreason.value_namespace = name_space
                    self.ospfvirtnbrrestarthelperexitreason.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtNbrRestartHelperStatus"):
                    self.ospfvirtnbrrestarthelperstatus = value
                    self.ospfvirtnbrrestarthelperstatus.value_namespace = name_space
                    self.ospfvirtnbrrestarthelperstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtNbrState"):
                    self.ospfvirtnbrstate = value
                    self.ospfvirtnbrstate.value_namespace = name_space
                    self.ospfvirtnbrstate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ospfvirtnbrentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ospfvirtnbrentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ospfVirtNbrTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "OSPF-MIB:OSPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ospfVirtNbrEntry"):
                for c in self.ospfvirtnbrentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = OspfMib.Ospfvirtnbrtable.Ospfvirtnbrentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ospfvirtnbrentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ospfVirtNbrEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Ospfextlsdbentry <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfextlsdbtable.Ospfextlsdbentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OspfMib.Ospfextlsdbtable, self).__init__()

            self.yang_name = "ospfExtLsdbTable"
            self.yang_parent_name = "OSPF-MIB"

            self.ospfextlsdbentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(OspfMib.Ospfextlsdbtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(OspfMib.Ospfextlsdbtable, self).__setattr__(name, value)


        class Ospfextlsdbentry(Entity):
            """
            A single link state advertisement.
            
            .. attribute:: ospfextlsdbtype  <key>
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\:   :py:class:`Ospfextlsdbtype <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfextlsdbtable.Ospfextlsdbentry.Ospfextlsdbtype>`
            
            	**status**\: deprecated
            
            .. attribute:: ospfextlsdblsid  <key>
            
            	The Link State ID is an LS Type Specific field containing either a Router ID or an IP address; it identifies the piece of the routing domain that is being described by the advertisement
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: ospfextlsdbrouterid  <key>
            
            	The 32\-bit number that uniquely identifies the originating router in the Autonomous System
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: ospfextlsdbadvertisement
            
            	The entire link state advertisement, including its header
            	**type**\:  str
            
            	**length:** 36
            
            	**status**\: deprecated
            
            .. attribute:: ospfextlsdbage
            
            	This field is the age of the link state advertisement in seconds
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: seconds
            
            	**status**\: deprecated
            
            .. attribute:: ospfextlsdbchecksum
            
            	This field is the checksum of the complete contents of the advertisement, excepting the age field.  The age field is excepted so that an advertisement's age can be incremented without updating the checksum.  The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred to as the Fletcher checksum
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: ospfextlsdbsequence
            
            	The sequence number field is a signed 32\-bit integer.  It starts with the value '80000001'h, or \-'7FFFFFFF'h, and increments until '7FFFFFFF'h. Thus, a typical sequence number will be very negative. It is used to detect old and duplicate link state advertisements.  The space of sequence numbers is linearly ordered.  The larger the sequence number, the more recent the advertisement
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OspfMib.Ospfextlsdbtable.Ospfextlsdbentry, self).__init__()

                self.yang_name = "ospfExtLsdbEntry"
                self.yang_parent_name = "ospfExtLsdbTable"

                self.ospfextlsdbtype = YLeaf(YType.enumeration, "ospfExtLsdbType")

                self.ospfextlsdblsid = YLeaf(YType.str, "ospfExtLsdbLsid")

                self.ospfextlsdbrouterid = YLeaf(YType.str, "ospfExtLsdbRouterId")

                self.ospfextlsdbadvertisement = YLeaf(YType.str, "ospfExtLsdbAdvertisement")

                self.ospfextlsdbage = YLeaf(YType.int32, "ospfExtLsdbAge")

                self.ospfextlsdbchecksum = YLeaf(YType.int32, "ospfExtLsdbChecksum")

                self.ospfextlsdbsequence = YLeaf(YType.int32, "ospfExtLsdbSequence")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ospfextlsdbtype",
                                "ospfextlsdblsid",
                                "ospfextlsdbrouterid",
                                "ospfextlsdbadvertisement",
                                "ospfextlsdbage",
                                "ospfextlsdbchecksum",
                                "ospfextlsdbsequence") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(OspfMib.Ospfextlsdbtable.Ospfextlsdbentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(OspfMib.Ospfextlsdbtable.Ospfextlsdbentry, self).__setattr__(name, value)

            class Ospfextlsdbtype(Enum):
                """
                Ospfextlsdbtype

                The type of the link state advertisement.

                Each link state type has a separate advertisement

                format.

                .. data:: asExternalLink = 5

                """

                asExternalLink = Enum.YLeaf(5, "asExternalLink")


            def has_data(self):
                return (
                    self.ospfextlsdbtype.is_set or
                    self.ospfextlsdblsid.is_set or
                    self.ospfextlsdbrouterid.is_set or
                    self.ospfextlsdbadvertisement.is_set or
                    self.ospfextlsdbage.is_set or
                    self.ospfextlsdbchecksum.is_set or
                    self.ospfextlsdbsequence.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ospfextlsdbtype.yfilter != YFilter.not_set or
                    self.ospfextlsdblsid.yfilter != YFilter.not_set or
                    self.ospfextlsdbrouterid.yfilter != YFilter.not_set or
                    self.ospfextlsdbadvertisement.yfilter != YFilter.not_set or
                    self.ospfextlsdbage.yfilter != YFilter.not_set or
                    self.ospfextlsdbchecksum.yfilter != YFilter.not_set or
                    self.ospfextlsdbsequence.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ospfExtLsdbEntry" + "[ospfExtLsdbType='" + self.ospfextlsdbtype.get() + "']" + "[ospfExtLsdbLsid='" + self.ospfextlsdblsid.get() + "']" + "[ospfExtLsdbRouterId='" + self.ospfextlsdbrouterid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "OSPF-MIB:OSPF-MIB/ospfExtLsdbTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ospfextlsdbtype.is_set or self.ospfextlsdbtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfextlsdbtype.get_name_leafdata())
                if (self.ospfextlsdblsid.is_set or self.ospfextlsdblsid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfextlsdblsid.get_name_leafdata())
                if (self.ospfextlsdbrouterid.is_set or self.ospfextlsdbrouterid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfextlsdbrouterid.get_name_leafdata())
                if (self.ospfextlsdbadvertisement.is_set or self.ospfextlsdbadvertisement.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfextlsdbadvertisement.get_name_leafdata())
                if (self.ospfextlsdbage.is_set or self.ospfextlsdbage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfextlsdbage.get_name_leafdata())
                if (self.ospfextlsdbchecksum.is_set or self.ospfextlsdbchecksum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfextlsdbchecksum.get_name_leafdata())
                if (self.ospfextlsdbsequence.is_set or self.ospfextlsdbsequence.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfextlsdbsequence.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ospfExtLsdbType" or name == "ospfExtLsdbLsid" or name == "ospfExtLsdbRouterId" or name == "ospfExtLsdbAdvertisement" or name == "ospfExtLsdbAge" or name == "ospfExtLsdbChecksum" or name == "ospfExtLsdbSequence"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ospfExtLsdbType"):
                    self.ospfextlsdbtype = value
                    self.ospfextlsdbtype.value_namespace = name_space
                    self.ospfextlsdbtype.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfExtLsdbLsid"):
                    self.ospfextlsdblsid = value
                    self.ospfextlsdblsid.value_namespace = name_space
                    self.ospfextlsdblsid.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfExtLsdbRouterId"):
                    self.ospfextlsdbrouterid = value
                    self.ospfextlsdbrouterid.value_namespace = name_space
                    self.ospfextlsdbrouterid.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfExtLsdbAdvertisement"):
                    self.ospfextlsdbadvertisement = value
                    self.ospfextlsdbadvertisement.value_namespace = name_space
                    self.ospfextlsdbadvertisement.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfExtLsdbAge"):
                    self.ospfextlsdbage = value
                    self.ospfextlsdbage.value_namespace = name_space
                    self.ospfextlsdbage.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfExtLsdbChecksum"):
                    self.ospfextlsdbchecksum = value
                    self.ospfextlsdbchecksum.value_namespace = name_space
                    self.ospfextlsdbchecksum.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfExtLsdbSequence"):
                    self.ospfextlsdbsequence = value
                    self.ospfextlsdbsequence.value_namespace = name_space
                    self.ospfextlsdbsequence.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ospfextlsdbentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ospfextlsdbentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ospfExtLsdbTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "OSPF-MIB:OSPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ospfExtLsdbEntry"):
                for c in self.ospfextlsdbentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = OspfMib.Ospfextlsdbtable.Ospfextlsdbentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ospfextlsdbentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ospfExtLsdbEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Ospfareaaggregateentry <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfareaaggregatetable.Ospfareaaggregateentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OspfMib.Ospfareaaggregatetable, self).__init__()

            self.yang_name = "ospfAreaAggregateTable"
            self.yang_parent_name = "OSPF-MIB"

            self.ospfareaaggregateentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(OspfMib.Ospfareaaggregatetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(OspfMib.Ospfareaaggregatetable, self).__setattr__(name, value)


        class Ospfareaaggregateentry(Entity):
            """
            A single area aggregate entry.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            storage.
            
            .. attribute:: ospfareaaggregateareaid  <key>
            
            	The area within which the address aggregate is to be found
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfareaaggregatelsdbtype  <key>
            
            	The type of the address aggregate.  This field specifies the Lsdb type that this address aggregate applies to
            	**type**\:   :py:class:`Ospfareaaggregatelsdbtype <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfareaaggregatetable.Ospfareaaggregateentry.Ospfareaaggregatelsdbtype>`
            
            .. attribute:: ospfareaaggregatenet  <key>
            
            	The IP address of the net or subnet indicated by the range
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfareaaggregatemask  <key>
            
            	The subnet mask that pertains to the net or subnet
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfareaaggregateeffect
            
            	Subnets subsumed by ranges either trigger the advertisement of the indicated aggregate (advertiseMatching) or result in the subnet's not being advertised at all outside the area
            	**type**\:   :py:class:`Ospfareaaggregateeffect <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfareaaggregatetable.Ospfareaaggregateentry.Ospfareaaggregateeffect>`
            
            .. attribute:: ospfareaaggregateextroutetag
            
            	External route tag to be included in NSSA (type\-7) LSAs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfareaaggregatestatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OspfMib.Ospfareaaggregatetable.Ospfareaaggregateentry, self).__init__()

                self.yang_name = "ospfAreaAggregateEntry"
                self.yang_parent_name = "ospfAreaAggregateTable"

                self.ospfareaaggregateareaid = YLeaf(YType.str, "ospfAreaAggregateAreaID")

                self.ospfareaaggregatelsdbtype = YLeaf(YType.enumeration, "ospfAreaAggregateLsdbType")

                self.ospfareaaggregatenet = YLeaf(YType.str, "ospfAreaAggregateNet")

                self.ospfareaaggregatemask = YLeaf(YType.str, "ospfAreaAggregateMask")

                self.ospfareaaggregateeffect = YLeaf(YType.enumeration, "ospfAreaAggregateEffect")

                self.ospfareaaggregateextroutetag = YLeaf(YType.uint32, "ospfAreaAggregateExtRouteTag")

                self.ospfareaaggregatestatus = YLeaf(YType.enumeration, "ospfAreaAggregateStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ospfareaaggregateareaid",
                                "ospfareaaggregatelsdbtype",
                                "ospfareaaggregatenet",
                                "ospfareaaggregatemask",
                                "ospfareaaggregateeffect",
                                "ospfareaaggregateextroutetag",
                                "ospfareaaggregatestatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(OspfMib.Ospfareaaggregatetable.Ospfareaaggregateentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(OspfMib.Ospfareaaggregatetable.Ospfareaaggregateentry, self).__setattr__(name, value)

            class Ospfareaaggregateeffect(Enum):
                """
                Ospfareaaggregateeffect

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
                Ospfareaaggregatelsdbtype

                The type of the address aggregate.  This field

                specifies the Lsdb type that this address

                aggregate applies to.

                .. data:: summaryLink = 3

                .. data:: nssaExternalLink = 7

                """

                summaryLink = Enum.YLeaf(3, "summaryLink")

                nssaExternalLink = Enum.YLeaf(7, "nssaExternalLink")


            def has_data(self):
                return (
                    self.ospfareaaggregateareaid.is_set or
                    self.ospfareaaggregatelsdbtype.is_set or
                    self.ospfareaaggregatenet.is_set or
                    self.ospfareaaggregatemask.is_set or
                    self.ospfareaaggregateeffect.is_set or
                    self.ospfareaaggregateextroutetag.is_set or
                    self.ospfareaaggregatestatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ospfareaaggregateareaid.yfilter != YFilter.not_set or
                    self.ospfareaaggregatelsdbtype.yfilter != YFilter.not_set or
                    self.ospfareaaggregatenet.yfilter != YFilter.not_set or
                    self.ospfareaaggregatemask.yfilter != YFilter.not_set or
                    self.ospfareaaggregateeffect.yfilter != YFilter.not_set or
                    self.ospfareaaggregateextroutetag.yfilter != YFilter.not_set or
                    self.ospfareaaggregatestatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ospfAreaAggregateEntry" + "[ospfAreaAggregateAreaID='" + self.ospfareaaggregateareaid.get() + "']" + "[ospfAreaAggregateLsdbType='" + self.ospfareaaggregatelsdbtype.get() + "']" + "[ospfAreaAggregateNet='" + self.ospfareaaggregatenet.get() + "']" + "[ospfAreaAggregateMask='" + self.ospfareaaggregatemask.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "OSPF-MIB:OSPF-MIB/ospfAreaAggregateTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ospfareaaggregateareaid.is_set or self.ospfareaaggregateareaid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfareaaggregateareaid.get_name_leafdata())
                if (self.ospfareaaggregatelsdbtype.is_set or self.ospfareaaggregatelsdbtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfareaaggregatelsdbtype.get_name_leafdata())
                if (self.ospfareaaggregatenet.is_set or self.ospfareaaggregatenet.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfareaaggregatenet.get_name_leafdata())
                if (self.ospfareaaggregatemask.is_set or self.ospfareaaggregatemask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfareaaggregatemask.get_name_leafdata())
                if (self.ospfareaaggregateeffect.is_set or self.ospfareaaggregateeffect.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfareaaggregateeffect.get_name_leafdata())
                if (self.ospfareaaggregateextroutetag.is_set or self.ospfareaaggregateextroutetag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfareaaggregateextroutetag.get_name_leafdata())
                if (self.ospfareaaggregatestatus.is_set or self.ospfareaaggregatestatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfareaaggregatestatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ospfAreaAggregateAreaID" or name == "ospfAreaAggregateLsdbType" or name == "ospfAreaAggregateNet" or name == "ospfAreaAggregateMask" or name == "ospfAreaAggregateEffect" or name == "ospfAreaAggregateExtRouteTag" or name == "ospfAreaAggregateStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ospfAreaAggregateAreaID"):
                    self.ospfareaaggregateareaid = value
                    self.ospfareaaggregateareaid.value_namespace = name_space
                    self.ospfareaaggregateareaid.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAreaAggregateLsdbType"):
                    self.ospfareaaggregatelsdbtype = value
                    self.ospfareaaggregatelsdbtype.value_namespace = name_space
                    self.ospfareaaggregatelsdbtype.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAreaAggregateNet"):
                    self.ospfareaaggregatenet = value
                    self.ospfareaaggregatenet.value_namespace = name_space
                    self.ospfareaaggregatenet.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAreaAggregateMask"):
                    self.ospfareaaggregatemask = value
                    self.ospfareaaggregatemask.value_namespace = name_space
                    self.ospfareaaggregatemask.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAreaAggregateEffect"):
                    self.ospfareaaggregateeffect = value
                    self.ospfareaaggregateeffect.value_namespace = name_space
                    self.ospfareaaggregateeffect.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAreaAggregateExtRouteTag"):
                    self.ospfareaaggregateextroutetag = value
                    self.ospfareaaggregateextroutetag.value_namespace = name_space
                    self.ospfareaaggregateextroutetag.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAreaAggregateStatus"):
                    self.ospfareaaggregatestatus = value
                    self.ospfareaaggregatestatus.value_namespace = name_space
                    self.ospfareaaggregatestatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ospfareaaggregateentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ospfareaaggregateentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ospfAreaAggregateTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "OSPF-MIB:OSPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ospfAreaAggregateEntry"):
                for c in self.ospfareaaggregateentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = OspfMib.Ospfareaaggregatetable.Ospfareaaggregateentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ospfareaaggregateentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ospfAreaAggregateEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Ospflocallsdbentry <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospflocallsdbtable.Ospflocallsdbentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OspfMib.Ospflocallsdbtable, self).__init__()

            self.yang_name = "ospfLocalLsdbTable"
            self.yang_parent_name = "OSPF-MIB"

            self.ospflocallsdbentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(OspfMib.Ospflocallsdbtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(OspfMib.Ospflocallsdbtable, self).__setattr__(name, value)


        class Ospflocallsdbentry(Entity):
            """
            A single link state advertisement.
            
            .. attribute:: ospflocallsdbipaddress  <key>
            
            	The IP address of the interface from which the LSA was received if the interface is numbered
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospflocallsdbaddresslessif  <key>
            
            	The interface index of the interface from which the LSA was received if the interface is unnumbered
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ospflocallsdbtype  <key>
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\:   :py:class:`Ospflocallsdbtype <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospflocallsdbtable.Ospflocallsdbentry.Ospflocallsdbtype>`
            
            .. attribute:: ospflocallsdblsid  <key>
            
            	The Link State ID is an LS Type Specific field containing a 32\-bit identifier in IP address format; it identifies the piece of the routing domain that is being described by the advertisement
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospflocallsdbrouterid  <key>
            
            	The 32\-bit number that uniquely identifies the originating router in the Autonomous System
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospflocallsdbadvertisement
            
            	The entire link state advertisement, including its header.  Note that for variable length LSAs, SNMP agents may not be able to return the largest string size
            	**type**\:  str
            
            	**length:** 1..65535
            
            .. attribute:: ospflocallsdbage
            
            	This field is the age of the link state advertisement in seconds
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: seconds
            
            .. attribute:: ospflocallsdbchecksum
            
            	This field is the checksum of the complete contents of the advertisement, excepting the age field.  The age field is excepted so that an advertisement's age can be incremented without updating the checksum.  The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred to as the Fletcher checksum
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospflocallsdbsequence
            
            	The sequence number field is a signed 32\-bit integer.  It starts with the value '80000001'h, or \-'7FFFFFFF'h, and increments until '7FFFFFFF'h. Thus, a typical sequence number will be very negative. It is used to detect old and duplicate link state advertisements.  The space of sequence numbers is linearly ordered.  The larger the sequence number, the more recent the advertisement
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OspfMib.Ospflocallsdbtable.Ospflocallsdbentry, self).__init__()

                self.yang_name = "ospfLocalLsdbEntry"
                self.yang_parent_name = "ospfLocalLsdbTable"

                self.ospflocallsdbipaddress = YLeaf(YType.str, "ospfLocalLsdbIpAddress")

                self.ospflocallsdbaddresslessif = YLeaf(YType.int32, "ospfLocalLsdbAddressLessIf")

                self.ospflocallsdbtype = YLeaf(YType.enumeration, "ospfLocalLsdbType")

                self.ospflocallsdblsid = YLeaf(YType.str, "ospfLocalLsdbLsid")

                self.ospflocallsdbrouterid = YLeaf(YType.str, "ospfLocalLsdbRouterId")

                self.ospflocallsdbadvertisement = YLeaf(YType.str, "ospfLocalLsdbAdvertisement")

                self.ospflocallsdbage = YLeaf(YType.int32, "ospfLocalLsdbAge")

                self.ospflocallsdbchecksum = YLeaf(YType.int32, "ospfLocalLsdbChecksum")

                self.ospflocallsdbsequence = YLeaf(YType.int32, "ospfLocalLsdbSequence")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ospflocallsdbipaddress",
                                "ospflocallsdbaddresslessif",
                                "ospflocallsdbtype",
                                "ospflocallsdblsid",
                                "ospflocallsdbrouterid",
                                "ospflocallsdbadvertisement",
                                "ospflocallsdbage",
                                "ospflocallsdbchecksum",
                                "ospflocallsdbsequence") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(OspfMib.Ospflocallsdbtable.Ospflocallsdbentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(OspfMib.Ospflocallsdbtable.Ospflocallsdbentry, self).__setattr__(name, value)

            class Ospflocallsdbtype(Enum):
                """
                Ospflocallsdbtype

                The type of the link state advertisement.

                Each link state type has a separate

                advertisement format.

                .. data:: localOpaqueLink = 9

                """

                localOpaqueLink = Enum.YLeaf(9, "localOpaqueLink")


            def has_data(self):
                return (
                    self.ospflocallsdbipaddress.is_set or
                    self.ospflocallsdbaddresslessif.is_set or
                    self.ospflocallsdbtype.is_set or
                    self.ospflocallsdblsid.is_set or
                    self.ospflocallsdbrouterid.is_set or
                    self.ospflocallsdbadvertisement.is_set or
                    self.ospflocallsdbage.is_set or
                    self.ospflocallsdbchecksum.is_set or
                    self.ospflocallsdbsequence.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ospflocallsdbipaddress.yfilter != YFilter.not_set or
                    self.ospflocallsdbaddresslessif.yfilter != YFilter.not_set or
                    self.ospflocallsdbtype.yfilter != YFilter.not_set or
                    self.ospflocallsdblsid.yfilter != YFilter.not_set or
                    self.ospflocallsdbrouterid.yfilter != YFilter.not_set or
                    self.ospflocallsdbadvertisement.yfilter != YFilter.not_set or
                    self.ospflocallsdbage.yfilter != YFilter.not_set or
                    self.ospflocallsdbchecksum.yfilter != YFilter.not_set or
                    self.ospflocallsdbsequence.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ospfLocalLsdbEntry" + "[ospfLocalLsdbIpAddress='" + self.ospflocallsdbipaddress.get() + "']" + "[ospfLocalLsdbAddressLessIf='" + self.ospflocallsdbaddresslessif.get() + "']" + "[ospfLocalLsdbType='" + self.ospflocallsdbtype.get() + "']" + "[ospfLocalLsdbLsid='" + self.ospflocallsdblsid.get() + "']" + "[ospfLocalLsdbRouterId='" + self.ospflocallsdbrouterid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "OSPF-MIB:OSPF-MIB/ospfLocalLsdbTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ospflocallsdbipaddress.is_set or self.ospflocallsdbipaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospflocallsdbipaddress.get_name_leafdata())
                if (self.ospflocallsdbaddresslessif.is_set or self.ospflocallsdbaddresslessif.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospflocallsdbaddresslessif.get_name_leafdata())
                if (self.ospflocallsdbtype.is_set or self.ospflocallsdbtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospflocallsdbtype.get_name_leafdata())
                if (self.ospflocallsdblsid.is_set or self.ospflocallsdblsid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospflocallsdblsid.get_name_leafdata())
                if (self.ospflocallsdbrouterid.is_set or self.ospflocallsdbrouterid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospflocallsdbrouterid.get_name_leafdata())
                if (self.ospflocallsdbadvertisement.is_set or self.ospflocallsdbadvertisement.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospflocallsdbadvertisement.get_name_leafdata())
                if (self.ospflocallsdbage.is_set or self.ospflocallsdbage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospflocallsdbage.get_name_leafdata())
                if (self.ospflocallsdbchecksum.is_set or self.ospflocallsdbchecksum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospflocallsdbchecksum.get_name_leafdata())
                if (self.ospflocallsdbsequence.is_set or self.ospflocallsdbsequence.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospflocallsdbsequence.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ospfLocalLsdbIpAddress" or name == "ospfLocalLsdbAddressLessIf" or name == "ospfLocalLsdbType" or name == "ospfLocalLsdbLsid" or name == "ospfLocalLsdbRouterId" or name == "ospfLocalLsdbAdvertisement" or name == "ospfLocalLsdbAge" or name == "ospfLocalLsdbChecksum" or name == "ospfLocalLsdbSequence"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ospfLocalLsdbIpAddress"):
                    self.ospflocallsdbipaddress = value
                    self.ospflocallsdbipaddress.value_namespace = name_space
                    self.ospflocallsdbipaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfLocalLsdbAddressLessIf"):
                    self.ospflocallsdbaddresslessif = value
                    self.ospflocallsdbaddresslessif.value_namespace = name_space
                    self.ospflocallsdbaddresslessif.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfLocalLsdbType"):
                    self.ospflocallsdbtype = value
                    self.ospflocallsdbtype.value_namespace = name_space
                    self.ospflocallsdbtype.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfLocalLsdbLsid"):
                    self.ospflocallsdblsid = value
                    self.ospflocallsdblsid.value_namespace = name_space
                    self.ospflocallsdblsid.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfLocalLsdbRouterId"):
                    self.ospflocallsdbrouterid = value
                    self.ospflocallsdbrouterid.value_namespace = name_space
                    self.ospflocallsdbrouterid.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfLocalLsdbAdvertisement"):
                    self.ospflocallsdbadvertisement = value
                    self.ospflocallsdbadvertisement.value_namespace = name_space
                    self.ospflocallsdbadvertisement.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfLocalLsdbAge"):
                    self.ospflocallsdbage = value
                    self.ospflocallsdbage.value_namespace = name_space
                    self.ospflocallsdbage.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfLocalLsdbChecksum"):
                    self.ospflocallsdbchecksum = value
                    self.ospflocallsdbchecksum.value_namespace = name_space
                    self.ospflocallsdbchecksum.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfLocalLsdbSequence"):
                    self.ospflocallsdbsequence = value
                    self.ospflocallsdbsequence.value_namespace = name_space
                    self.ospflocallsdbsequence.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ospflocallsdbentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ospflocallsdbentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ospfLocalLsdbTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "OSPF-MIB:OSPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ospfLocalLsdbEntry"):
                for c in self.ospflocallsdbentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = OspfMib.Ospflocallsdbtable.Ospflocallsdbentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ospflocallsdbentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ospfLocalLsdbEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Ospfvirtlocallsdbentry <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfvirtlocallsdbtable.Ospfvirtlocallsdbentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OspfMib.Ospfvirtlocallsdbtable, self).__init__()

            self.yang_name = "ospfVirtLocalLsdbTable"
            self.yang_parent_name = "OSPF-MIB"

            self.ospfvirtlocallsdbentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(OspfMib.Ospfvirtlocallsdbtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(OspfMib.Ospfvirtlocallsdbtable, self).__setattr__(name, value)


        class Ospfvirtlocallsdbentry(Entity):
            """
            A single link state advertisement.
            
            .. attribute:: ospfvirtlocallsdbtransitarea  <key>
            
            	The transit area that the virtual link traverses.  By definition, this is not 0.0.0.0
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfvirtlocallsdbneighbor  <key>
            
            	The Router ID of the virtual neighbor
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfvirtlocallsdbtype  <key>
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\:   :py:class:`Ospfvirtlocallsdbtype <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfvirtlocallsdbtable.Ospfvirtlocallsdbentry.Ospfvirtlocallsdbtype>`
            
            .. attribute:: ospfvirtlocallsdblsid  <key>
            
            	The Link State ID is an LS Type Specific field containing a 32\-bit identifier in IP address format; it identifies the piece of the routing domain that is being described by the advertisement
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfvirtlocallsdbrouterid  <key>
            
            	The 32\-bit number that uniquely identifies the originating router in the Autonomous System
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfvirtlocallsdbadvertisement
            
            	The entire link state advertisement, including its header
            	**type**\:  str
            
            	**length:** 1..65535
            
            .. attribute:: ospfvirtlocallsdbage
            
            	This field is the age of the link state advertisement in seconds
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: seconds
            
            .. attribute:: ospfvirtlocallsdbchecksum
            
            	This field is the checksum of the complete contents of the advertisement, excepting the age field.  The age field is excepted so that  an advertisement's age can be incremented without updating the checksum.  The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred to as the Fletcher checksum
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospfvirtlocallsdbsequence
            
            	The sequence number field is a signed 32\-bit integer.  It starts with the value '80000001'h, or \-'7FFFFFFF'h, and increments until '7FFFFFFF'h. Thus, a typical sequence number will be very negative. It is used to detect old and duplicate link state advertisements.  The space of sequence numbers is linearly ordered.  The larger the sequence number, the more recent the advertisement
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OspfMib.Ospfvirtlocallsdbtable.Ospfvirtlocallsdbentry, self).__init__()

                self.yang_name = "ospfVirtLocalLsdbEntry"
                self.yang_parent_name = "ospfVirtLocalLsdbTable"

                self.ospfvirtlocallsdbtransitarea = YLeaf(YType.str, "ospfVirtLocalLsdbTransitArea")

                self.ospfvirtlocallsdbneighbor = YLeaf(YType.str, "ospfVirtLocalLsdbNeighbor")

                self.ospfvirtlocallsdbtype = YLeaf(YType.enumeration, "ospfVirtLocalLsdbType")

                self.ospfvirtlocallsdblsid = YLeaf(YType.str, "ospfVirtLocalLsdbLsid")

                self.ospfvirtlocallsdbrouterid = YLeaf(YType.str, "ospfVirtLocalLsdbRouterId")

                self.ospfvirtlocallsdbadvertisement = YLeaf(YType.str, "ospfVirtLocalLsdbAdvertisement")

                self.ospfvirtlocallsdbage = YLeaf(YType.int32, "ospfVirtLocalLsdbAge")

                self.ospfvirtlocallsdbchecksum = YLeaf(YType.int32, "ospfVirtLocalLsdbChecksum")

                self.ospfvirtlocallsdbsequence = YLeaf(YType.int32, "ospfVirtLocalLsdbSequence")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ospfvirtlocallsdbtransitarea",
                                "ospfvirtlocallsdbneighbor",
                                "ospfvirtlocallsdbtype",
                                "ospfvirtlocallsdblsid",
                                "ospfvirtlocallsdbrouterid",
                                "ospfvirtlocallsdbadvertisement",
                                "ospfvirtlocallsdbage",
                                "ospfvirtlocallsdbchecksum",
                                "ospfvirtlocallsdbsequence") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(OspfMib.Ospfvirtlocallsdbtable.Ospfvirtlocallsdbentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(OspfMib.Ospfvirtlocallsdbtable.Ospfvirtlocallsdbentry, self).__setattr__(name, value)

            class Ospfvirtlocallsdbtype(Enum):
                """
                Ospfvirtlocallsdbtype

                The type of the link state advertisement.

                Each link state type has a separate

                advertisement format.

                .. data:: localOpaqueLink = 9

                """

                localOpaqueLink = Enum.YLeaf(9, "localOpaqueLink")


            def has_data(self):
                return (
                    self.ospfvirtlocallsdbtransitarea.is_set or
                    self.ospfvirtlocallsdbneighbor.is_set or
                    self.ospfvirtlocallsdbtype.is_set or
                    self.ospfvirtlocallsdblsid.is_set or
                    self.ospfvirtlocallsdbrouterid.is_set or
                    self.ospfvirtlocallsdbadvertisement.is_set or
                    self.ospfvirtlocallsdbage.is_set or
                    self.ospfvirtlocallsdbchecksum.is_set or
                    self.ospfvirtlocallsdbsequence.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ospfvirtlocallsdbtransitarea.yfilter != YFilter.not_set or
                    self.ospfvirtlocallsdbneighbor.yfilter != YFilter.not_set or
                    self.ospfvirtlocallsdbtype.yfilter != YFilter.not_set or
                    self.ospfvirtlocallsdblsid.yfilter != YFilter.not_set or
                    self.ospfvirtlocallsdbrouterid.yfilter != YFilter.not_set or
                    self.ospfvirtlocallsdbadvertisement.yfilter != YFilter.not_set or
                    self.ospfvirtlocallsdbage.yfilter != YFilter.not_set or
                    self.ospfvirtlocallsdbchecksum.yfilter != YFilter.not_set or
                    self.ospfvirtlocallsdbsequence.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ospfVirtLocalLsdbEntry" + "[ospfVirtLocalLsdbTransitArea='" + self.ospfvirtlocallsdbtransitarea.get() + "']" + "[ospfVirtLocalLsdbNeighbor='" + self.ospfvirtlocallsdbneighbor.get() + "']" + "[ospfVirtLocalLsdbType='" + self.ospfvirtlocallsdbtype.get() + "']" + "[ospfVirtLocalLsdbLsid='" + self.ospfvirtlocallsdblsid.get() + "']" + "[ospfVirtLocalLsdbRouterId='" + self.ospfvirtlocallsdbrouterid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "OSPF-MIB:OSPF-MIB/ospfVirtLocalLsdbTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ospfvirtlocallsdbtransitarea.is_set or self.ospfvirtlocallsdbtransitarea.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtlocallsdbtransitarea.get_name_leafdata())
                if (self.ospfvirtlocallsdbneighbor.is_set or self.ospfvirtlocallsdbneighbor.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtlocallsdbneighbor.get_name_leafdata())
                if (self.ospfvirtlocallsdbtype.is_set or self.ospfvirtlocallsdbtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtlocallsdbtype.get_name_leafdata())
                if (self.ospfvirtlocallsdblsid.is_set or self.ospfvirtlocallsdblsid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtlocallsdblsid.get_name_leafdata())
                if (self.ospfvirtlocallsdbrouterid.is_set or self.ospfvirtlocallsdbrouterid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtlocallsdbrouterid.get_name_leafdata())
                if (self.ospfvirtlocallsdbadvertisement.is_set or self.ospfvirtlocallsdbadvertisement.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtlocallsdbadvertisement.get_name_leafdata())
                if (self.ospfvirtlocallsdbage.is_set or self.ospfvirtlocallsdbage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtlocallsdbage.get_name_leafdata())
                if (self.ospfvirtlocallsdbchecksum.is_set or self.ospfvirtlocallsdbchecksum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtlocallsdbchecksum.get_name_leafdata())
                if (self.ospfvirtlocallsdbsequence.is_set or self.ospfvirtlocallsdbsequence.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfvirtlocallsdbsequence.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ospfVirtLocalLsdbTransitArea" or name == "ospfVirtLocalLsdbNeighbor" or name == "ospfVirtLocalLsdbType" or name == "ospfVirtLocalLsdbLsid" or name == "ospfVirtLocalLsdbRouterId" or name == "ospfVirtLocalLsdbAdvertisement" or name == "ospfVirtLocalLsdbAge" or name == "ospfVirtLocalLsdbChecksum" or name == "ospfVirtLocalLsdbSequence"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ospfVirtLocalLsdbTransitArea"):
                    self.ospfvirtlocallsdbtransitarea = value
                    self.ospfvirtlocallsdbtransitarea.value_namespace = name_space
                    self.ospfvirtlocallsdbtransitarea.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtLocalLsdbNeighbor"):
                    self.ospfvirtlocallsdbneighbor = value
                    self.ospfvirtlocallsdbneighbor.value_namespace = name_space
                    self.ospfvirtlocallsdbneighbor.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtLocalLsdbType"):
                    self.ospfvirtlocallsdbtype = value
                    self.ospfvirtlocallsdbtype.value_namespace = name_space
                    self.ospfvirtlocallsdbtype.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtLocalLsdbLsid"):
                    self.ospfvirtlocallsdblsid = value
                    self.ospfvirtlocallsdblsid.value_namespace = name_space
                    self.ospfvirtlocallsdblsid.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtLocalLsdbRouterId"):
                    self.ospfvirtlocallsdbrouterid = value
                    self.ospfvirtlocallsdbrouterid.value_namespace = name_space
                    self.ospfvirtlocallsdbrouterid.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtLocalLsdbAdvertisement"):
                    self.ospfvirtlocallsdbadvertisement = value
                    self.ospfvirtlocallsdbadvertisement.value_namespace = name_space
                    self.ospfvirtlocallsdbadvertisement.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtLocalLsdbAge"):
                    self.ospfvirtlocallsdbage = value
                    self.ospfvirtlocallsdbage.value_namespace = name_space
                    self.ospfvirtlocallsdbage.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtLocalLsdbChecksum"):
                    self.ospfvirtlocallsdbchecksum = value
                    self.ospfvirtlocallsdbchecksum.value_namespace = name_space
                    self.ospfvirtlocallsdbchecksum.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfVirtLocalLsdbSequence"):
                    self.ospfvirtlocallsdbsequence = value
                    self.ospfvirtlocallsdbsequence.value_namespace = name_space
                    self.ospfvirtlocallsdbsequence.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ospfvirtlocallsdbentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ospfvirtlocallsdbentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ospfVirtLocalLsdbTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "OSPF-MIB:OSPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ospfVirtLocalLsdbEntry"):
                for c in self.ospfvirtlocallsdbentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = OspfMib.Ospfvirtlocallsdbtable.Ospfvirtlocallsdbentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ospfvirtlocallsdbentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ospfVirtLocalLsdbEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Ospfaslsdbentry <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfaslsdbtable.Ospfaslsdbentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OspfMib.Ospfaslsdbtable, self).__init__()

            self.yang_name = "ospfAsLsdbTable"
            self.yang_parent_name = "OSPF-MIB"

            self.ospfaslsdbentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(OspfMib.Ospfaslsdbtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(OspfMib.Ospfaslsdbtable, self).__setattr__(name, value)


        class Ospfaslsdbentry(Entity):
            """
            A single link state advertisement.
            
            .. attribute:: ospfaslsdbtype  <key>
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\:   :py:class:`Ospfaslsdbtype <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfaslsdbtable.Ospfaslsdbentry.Ospfaslsdbtype>`
            
            .. attribute:: ospfaslsdblsid  <key>
            
            	The Link State ID is an LS Type Specific field containing either a Router ID or an IP address;  it identifies the piece of the routing domain that is being described by the advertisement
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfaslsdbrouterid  <key>
            
            	The 32\-bit number that uniquely identifies the originating router in the Autonomous System
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfaslsdbadvertisement
            
            	The entire link state advertisement, including its header
            	**type**\:  str
            
            	**length:** 1..65535
            
            .. attribute:: ospfaslsdbage
            
            	This field is the age of the link state advertisement in seconds
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: seconds
            
            .. attribute:: ospfaslsdbchecksum
            
            	This field is the checksum of the complete contents of the advertisement, excepting the age field.  The age field is excepted so that an advertisement's age can be incremented without updating the checksum.  The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred to as the Fletcher checksum
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospfaslsdbsequence
            
            	The sequence number field is a signed 32\-bit integer.  It starts with the value '80000001'h, or \-'7FFFFFFF'h, and increments until '7FFFFFFF'h. Thus, a typical sequence number will be very negative. It is used to detect old and duplicate link state advertisements.  The space of sequence numbers is linearly ordered.  The larger the sequence number, the more recent the advertisement
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OspfMib.Ospfaslsdbtable.Ospfaslsdbentry, self).__init__()

                self.yang_name = "ospfAsLsdbEntry"
                self.yang_parent_name = "ospfAsLsdbTable"

                self.ospfaslsdbtype = YLeaf(YType.enumeration, "ospfAsLsdbType")

                self.ospfaslsdblsid = YLeaf(YType.str, "ospfAsLsdbLsid")

                self.ospfaslsdbrouterid = YLeaf(YType.str, "ospfAsLsdbRouterId")

                self.ospfaslsdbadvertisement = YLeaf(YType.str, "ospfAsLsdbAdvertisement")

                self.ospfaslsdbage = YLeaf(YType.int32, "ospfAsLsdbAge")

                self.ospfaslsdbchecksum = YLeaf(YType.int32, "ospfAsLsdbChecksum")

                self.ospfaslsdbsequence = YLeaf(YType.int32, "ospfAsLsdbSequence")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ospfaslsdbtype",
                                "ospfaslsdblsid",
                                "ospfaslsdbrouterid",
                                "ospfaslsdbadvertisement",
                                "ospfaslsdbage",
                                "ospfaslsdbchecksum",
                                "ospfaslsdbsequence") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(OspfMib.Ospfaslsdbtable.Ospfaslsdbentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(OspfMib.Ospfaslsdbtable.Ospfaslsdbentry, self).__setattr__(name, value)

            class Ospfaslsdbtype(Enum):
                """
                Ospfaslsdbtype

                The type of the link state advertisement.

                Each link state type has a separate

                advertisement format.

                .. data:: asExternalLink = 5

                .. data:: asOpaqueLink = 11

                """

                asExternalLink = Enum.YLeaf(5, "asExternalLink")

                asOpaqueLink = Enum.YLeaf(11, "asOpaqueLink")


            def has_data(self):
                return (
                    self.ospfaslsdbtype.is_set or
                    self.ospfaslsdblsid.is_set or
                    self.ospfaslsdbrouterid.is_set or
                    self.ospfaslsdbadvertisement.is_set or
                    self.ospfaslsdbage.is_set or
                    self.ospfaslsdbchecksum.is_set or
                    self.ospfaslsdbsequence.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ospfaslsdbtype.yfilter != YFilter.not_set or
                    self.ospfaslsdblsid.yfilter != YFilter.not_set or
                    self.ospfaslsdbrouterid.yfilter != YFilter.not_set or
                    self.ospfaslsdbadvertisement.yfilter != YFilter.not_set or
                    self.ospfaslsdbage.yfilter != YFilter.not_set or
                    self.ospfaslsdbchecksum.yfilter != YFilter.not_set or
                    self.ospfaslsdbsequence.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ospfAsLsdbEntry" + "[ospfAsLsdbType='" + self.ospfaslsdbtype.get() + "']" + "[ospfAsLsdbLsid='" + self.ospfaslsdblsid.get() + "']" + "[ospfAsLsdbRouterId='" + self.ospfaslsdbrouterid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "OSPF-MIB:OSPF-MIB/ospfAsLsdbTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ospfaslsdbtype.is_set or self.ospfaslsdbtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfaslsdbtype.get_name_leafdata())
                if (self.ospfaslsdblsid.is_set or self.ospfaslsdblsid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfaslsdblsid.get_name_leafdata())
                if (self.ospfaslsdbrouterid.is_set or self.ospfaslsdbrouterid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfaslsdbrouterid.get_name_leafdata())
                if (self.ospfaslsdbadvertisement.is_set or self.ospfaslsdbadvertisement.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfaslsdbadvertisement.get_name_leafdata())
                if (self.ospfaslsdbage.is_set or self.ospfaslsdbage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfaslsdbage.get_name_leafdata())
                if (self.ospfaslsdbchecksum.is_set or self.ospfaslsdbchecksum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfaslsdbchecksum.get_name_leafdata())
                if (self.ospfaslsdbsequence.is_set or self.ospfaslsdbsequence.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfaslsdbsequence.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ospfAsLsdbType" or name == "ospfAsLsdbLsid" or name == "ospfAsLsdbRouterId" or name == "ospfAsLsdbAdvertisement" or name == "ospfAsLsdbAge" or name == "ospfAsLsdbChecksum" or name == "ospfAsLsdbSequence"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ospfAsLsdbType"):
                    self.ospfaslsdbtype = value
                    self.ospfaslsdbtype.value_namespace = name_space
                    self.ospfaslsdbtype.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAsLsdbLsid"):
                    self.ospfaslsdblsid = value
                    self.ospfaslsdblsid.value_namespace = name_space
                    self.ospfaslsdblsid.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAsLsdbRouterId"):
                    self.ospfaslsdbrouterid = value
                    self.ospfaslsdbrouterid.value_namespace = name_space
                    self.ospfaslsdbrouterid.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAsLsdbAdvertisement"):
                    self.ospfaslsdbadvertisement = value
                    self.ospfaslsdbadvertisement.value_namespace = name_space
                    self.ospfaslsdbadvertisement.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAsLsdbAge"):
                    self.ospfaslsdbage = value
                    self.ospfaslsdbage.value_namespace = name_space
                    self.ospfaslsdbage.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAsLsdbChecksum"):
                    self.ospfaslsdbchecksum = value
                    self.ospfaslsdbchecksum.value_namespace = name_space
                    self.ospfaslsdbchecksum.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAsLsdbSequence"):
                    self.ospfaslsdbsequence = value
                    self.ospfaslsdbsequence.value_namespace = name_space
                    self.ospfaslsdbsequence.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ospfaslsdbentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ospfaslsdbentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ospfAsLsdbTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "OSPF-MIB:OSPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ospfAsLsdbEntry"):
                for c in self.ospfaslsdbentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = OspfMib.Ospfaslsdbtable.Ospfaslsdbentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ospfaslsdbentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ospfAsLsdbEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ospfarealsacounttable(Entity):
        """
        This table maintains per\-area, per\-LSA\-type counters
        
        .. attribute:: ospfarealsacountentry
        
        	An entry with a number of link advertisements  of a given type for a given area
        	**type**\: list of    :py:class:`Ospfarealsacountentry <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfarealsacounttable.Ospfarealsacountentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OspfMib.Ospfarealsacounttable, self).__init__()

            self.yang_name = "ospfAreaLsaCountTable"
            self.yang_parent_name = "OSPF-MIB"

            self.ospfarealsacountentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(OspfMib.Ospfarealsacounttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(OspfMib.Ospfarealsacounttable, self).__setattr__(name, value)


        class Ospfarealsacountentry(Entity):
            """
            An entry with a number of link advertisements
            
            of a given type for a given area.
            
            .. attribute:: ospfarealsacountareaid  <key>
            
            	This entry Area ID
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfarealsacountlsatype  <key>
            
            	This entry LSA type
            	**type**\:   :py:class:`Ospfarealsacountlsatype <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfarealsacounttable.Ospfarealsacountentry.Ospfarealsacountlsatype>`
            
            .. attribute:: ospfarealsacountnumber
            
            	Number of LSAs of a given type for a given area
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OspfMib.Ospfarealsacounttable.Ospfarealsacountentry, self).__init__()

                self.yang_name = "ospfAreaLsaCountEntry"
                self.yang_parent_name = "ospfAreaLsaCountTable"

                self.ospfarealsacountareaid = YLeaf(YType.str, "ospfAreaLsaCountAreaId")

                self.ospfarealsacountlsatype = YLeaf(YType.enumeration, "ospfAreaLsaCountLsaType")

                self.ospfarealsacountnumber = YLeaf(YType.uint32, "ospfAreaLsaCountNumber")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ospfarealsacountareaid",
                                "ospfarealsacountlsatype",
                                "ospfarealsacountnumber") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(OspfMib.Ospfarealsacounttable.Ospfarealsacountentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(OspfMib.Ospfarealsacounttable.Ospfarealsacountentry, self).__setattr__(name, value)

            class Ospfarealsacountlsatype(Enum):
                """
                Ospfarealsacountlsatype

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


            def has_data(self):
                return (
                    self.ospfarealsacountareaid.is_set or
                    self.ospfarealsacountlsatype.is_set or
                    self.ospfarealsacountnumber.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ospfarealsacountareaid.yfilter != YFilter.not_set or
                    self.ospfarealsacountlsatype.yfilter != YFilter.not_set or
                    self.ospfarealsacountnumber.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ospfAreaLsaCountEntry" + "[ospfAreaLsaCountAreaId='" + self.ospfarealsacountareaid.get() + "']" + "[ospfAreaLsaCountLsaType='" + self.ospfarealsacountlsatype.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "OSPF-MIB:OSPF-MIB/ospfAreaLsaCountTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ospfarealsacountareaid.is_set or self.ospfarealsacountareaid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfarealsacountareaid.get_name_leafdata())
                if (self.ospfarealsacountlsatype.is_set or self.ospfarealsacountlsatype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfarealsacountlsatype.get_name_leafdata())
                if (self.ospfarealsacountnumber.is_set or self.ospfarealsacountnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospfarealsacountnumber.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ospfAreaLsaCountAreaId" or name == "ospfAreaLsaCountLsaType" or name == "ospfAreaLsaCountNumber"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ospfAreaLsaCountAreaId"):
                    self.ospfarealsacountareaid = value
                    self.ospfarealsacountareaid.value_namespace = name_space
                    self.ospfarealsacountareaid.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAreaLsaCountLsaType"):
                    self.ospfarealsacountlsatype = value
                    self.ospfarealsacountlsatype.value_namespace = name_space
                    self.ospfarealsacountlsatype.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfAreaLsaCountNumber"):
                    self.ospfarealsacountnumber = value
                    self.ospfarealsacountnumber.value_namespace = name_space
                    self.ospfarealsacountnumber.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ospfarealsacountentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ospfarealsacountentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ospfAreaLsaCountTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "OSPF-MIB:OSPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ospfAreaLsaCountEntry"):
                for c in self.ospfarealsacountentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = OspfMib.Ospfarealsacounttable.Ospfarealsacountentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ospfarealsacountentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ospfAreaLsaCountEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.ospfareaaggregatetable is not None and self.ospfareaaggregatetable.has_data()) or
            (self.ospfarealsacounttable is not None and self.ospfarealsacounttable.has_data()) or
            (self.ospfarearangetable is not None and self.ospfarearangetable.has_data()) or
            (self.ospfareatable is not None and self.ospfareatable.has_data()) or
            (self.ospfaslsdbtable is not None and self.ospfaslsdbtable.has_data()) or
            (self.ospfextlsdbtable is not None and self.ospfextlsdbtable.has_data()) or
            (self.ospfgeneralgroup is not None and self.ospfgeneralgroup.has_data()) or
            (self.ospfhosttable is not None and self.ospfhosttable.has_data()) or
            (self.ospfifmetrictable is not None and self.ospfifmetrictable.has_data()) or
            (self.ospfiftable is not None and self.ospfiftable.has_data()) or
            (self.ospflocallsdbtable is not None and self.ospflocallsdbtable.has_data()) or
            (self.ospflsdbtable is not None and self.ospflsdbtable.has_data()) or
            (self.ospfnbrtable is not None and self.ospfnbrtable.has_data()) or
            (self.ospfstubareatable is not None and self.ospfstubareatable.has_data()) or
            (self.ospfvirtiftable is not None and self.ospfvirtiftable.has_data()) or
            (self.ospfvirtlocallsdbtable is not None and self.ospfvirtlocallsdbtable.has_data()) or
            (self.ospfvirtnbrtable is not None and self.ospfvirtnbrtable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ospfareaaggregatetable is not None and self.ospfareaaggregatetable.has_operation()) or
            (self.ospfarealsacounttable is not None and self.ospfarealsacounttable.has_operation()) or
            (self.ospfarearangetable is not None and self.ospfarearangetable.has_operation()) or
            (self.ospfareatable is not None and self.ospfareatable.has_operation()) or
            (self.ospfaslsdbtable is not None and self.ospfaslsdbtable.has_operation()) or
            (self.ospfextlsdbtable is not None and self.ospfextlsdbtable.has_operation()) or
            (self.ospfgeneralgroup is not None and self.ospfgeneralgroup.has_operation()) or
            (self.ospfhosttable is not None and self.ospfhosttable.has_operation()) or
            (self.ospfifmetrictable is not None and self.ospfifmetrictable.has_operation()) or
            (self.ospfiftable is not None and self.ospfiftable.has_operation()) or
            (self.ospflocallsdbtable is not None and self.ospflocallsdbtable.has_operation()) or
            (self.ospflsdbtable is not None and self.ospflsdbtable.has_operation()) or
            (self.ospfnbrtable is not None and self.ospfnbrtable.has_operation()) or
            (self.ospfstubareatable is not None and self.ospfstubareatable.has_operation()) or
            (self.ospfvirtiftable is not None and self.ospfvirtiftable.has_operation()) or
            (self.ospfvirtlocallsdbtable is not None and self.ospfvirtlocallsdbtable.has_operation()) or
            (self.ospfvirtnbrtable is not None and self.ospfvirtnbrtable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "OSPF-MIB:OSPF-MIB" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "ospfAreaAggregateTable"):
            if (self.ospfareaaggregatetable is None):
                self.ospfareaaggregatetable = OspfMib.Ospfareaaggregatetable()
                self.ospfareaaggregatetable.parent = self
                self._children_name_map["ospfareaaggregatetable"] = "ospfAreaAggregateTable"
            return self.ospfareaaggregatetable

        if (child_yang_name == "ospfAreaLsaCountTable"):
            if (self.ospfarealsacounttable is None):
                self.ospfarealsacounttable = OspfMib.Ospfarealsacounttable()
                self.ospfarealsacounttable.parent = self
                self._children_name_map["ospfarealsacounttable"] = "ospfAreaLsaCountTable"
            return self.ospfarealsacounttable

        if (child_yang_name == "ospfAreaRangeTable"):
            if (self.ospfarearangetable is None):
                self.ospfarearangetable = OspfMib.Ospfarearangetable()
                self.ospfarearangetable.parent = self
                self._children_name_map["ospfarearangetable"] = "ospfAreaRangeTable"
            return self.ospfarearangetable

        if (child_yang_name == "ospfAreaTable"):
            if (self.ospfareatable is None):
                self.ospfareatable = OspfMib.Ospfareatable()
                self.ospfareatable.parent = self
                self._children_name_map["ospfareatable"] = "ospfAreaTable"
            return self.ospfareatable

        if (child_yang_name == "ospfAsLsdbTable"):
            if (self.ospfaslsdbtable is None):
                self.ospfaslsdbtable = OspfMib.Ospfaslsdbtable()
                self.ospfaslsdbtable.parent = self
                self._children_name_map["ospfaslsdbtable"] = "ospfAsLsdbTable"
            return self.ospfaslsdbtable

        if (child_yang_name == "ospfExtLsdbTable"):
            if (self.ospfextlsdbtable is None):
                self.ospfextlsdbtable = OspfMib.Ospfextlsdbtable()
                self.ospfextlsdbtable.parent = self
                self._children_name_map["ospfextlsdbtable"] = "ospfExtLsdbTable"
            return self.ospfextlsdbtable

        if (child_yang_name == "ospfGeneralGroup"):
            if (self.ospfgeneralgroup is None):
                self.ospfgeneralgroup = OspfMib.Ospfgeneralgroup()
                self.ospfgeneralgroup.parent = self
                self._children_name_map["ospfgeneralgroup"] = "ospfGeneralGroup"
            return self.ospfgeneralgroup

        if (child_yang_name == "ospfHostTable"):
            if (self.ospfhosttable is None):
                self.ospfhosttable = OspfMib.Ospfhosttable()
                self.ospfhosttable.parent = self
                self._children_name_map["ospfhosttable"] = "ospfHostTable"
            return self.ospfhosttable

        if (child_yang_name == "ospfIfMetricTable"):
            if (self.ospfifmetrictable is None):
                self.ospfifmetrictable = OspfMib.Ospfifmetrictable()
                self.ospfifmetrictable.parent = self
                self._children_name_map["ospfifmetrictable"] = "ospfIfMetricTable"
            return self.ospfifmetrictable

        if (child_yang_name == "ospfIfTable"):
            if (self.ospfiftable is None):
                self.ospfiftable = OspfMib.Ospfiftable()
                self.ospfiftable.parent = self
                self._children_name_map["ospfiftable"] = "ospfIfTable"
            return self.ospfiftable

        if (child_yang_name == "ospfLocalLsdbTable"):
            if (self.ospflocallsdbtable is None):
                self.ospflocallsdbtable = OspfMib.Ospflocallsdbtable()
                self.ospflocallsdbtable.parent = self
                self._children_name_map["ospflocallsdbtable"] = "ospfLocalLsdbTable"
            return self.ospflocallsdbtable

        if (child_yang_name == "ospfLsdbTable"):
            if (self.ospflsdbtable is None):
                self.ospflsdbtable = OspfMib.Ospflsdbtable()
                self.ospflsdbtable.parent = self
                self._children_name_map["ospflsdbtable"] = "ospfLsdbTable"
            return self.ospflsdbtable

        if (child_yang_name == "ospfNbrTable"):
            if (self.ospfnbrtable is None):
                self.ospfnbrtable = OspfMib.Ospfnbrtable()
                self.ospfnbrtable.parent = self
                self._children_name_map["ospfnbrtable"] = "ospfNbrTable"
            return self.ospfnbrtable

        if (child_yang_name == "ospfStubAreaTable"):
            if (self.ospfstubareatable is None):
                self.ospfstubareatable = OspfMib.Ospfstubareatable()
                self.ospfstubareatable.parent = self
                self._children_name_map["ospfstubareatable"] = "ospfStubAreaTable"
            return self.ospfstubareatable

        if (child_yang_name == "ospfVirtIfTable"):
            if (self.ospfvirtiftable is None):
                self.ospfvirtiftable = OspfMib.Ospfvirtiftable()
                self.ospfvirtiftable.parent = self
                self._children_name_map["ospfvirtiftable"] = "ospfVirtIfTable"
            return self.ospfvirtiftable

        if (child_yang_name == "ospfVirtLocalLsdbTable"):
            if (self.ospfvirtlocallsdbtable is None):
                self.ospfvirtlocallsdbtable = OspfMib.Ospfvirtlocallsdbtable()
                self.ospfvirtlocallsdbtable.parent = self
                self._children_name_map["ospfvirtlocallsdbtable"] = "ospfVirtLocalLsdbTable"
            return self.ospfvirtlocallsdbtable

        if (child_yang_name == "ospfVirtNbrTable"):
            if (self.ospfvirtnbrtable is None):
                self.ospfvirtnbrtable = OspfMib.Ospfvirtnbrtable()
                self.ospfvirtnbrtable.parent = self
                self._children_name_map["ospfvirtnbrtable"] = "ospfVirtNbrTable"
            return self.ospfvirtnbrtable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ospfAreaAggregateTable" or name == "ospfAreaLsaCountTable" or name == "ospfAreaRangeTable" or name == "ospfAreaTable" or name == "ospfAsLsdbTable" or name == "ospfExtLsdbTable" or name == "ospfGeneralGroup" or name == "ospfHostTable" or name == "ospfIfMetricTable" or name == "ospfIfTable" or name == "ospfLocalLsdbTable" or name == "ospfLsdbTable" or name == "ospfNbrTable" or name == "ospfStubAreaTable" or name == "ospfVirtIfTable" or name == "ospfVirtLocalLsdbTable" or name == "ospfVirtNbrTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = OspfMib()
        return self._top_entity


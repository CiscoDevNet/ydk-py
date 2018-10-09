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
    
    	
    	**type**\:  :py:class:`OspfGeneralGroup <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfGeneralGroup>`
    
    .. attribute:: ospfareatable
    
    	Information describing the configured parameters and cumulative statistics of the router's attached areas. The interfaces and virtual links are configured as part of these areas.  Area 0.0.0.0, by definition, is the backbone area
    	**type**\:  :py:class:`OspfAreaTable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfAreaTable>`
    
    .. attribute:: ospfstubareatable
    
    	The set of metrics that will be advertised by a default Area Border Router into a stub area
    	**type**\:  :py:class:`OspfStubAreaTable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfStubAreaTable>`
    
    .. attribute:: ospflsdbtable
    
    	The OSPF Process's link state database (LSDB). The LSDB contains the link state advertisements from throughout the areas that the device is attached to
    	**type**\:  :py:class:`OspfLsdbTable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfLsdbTable>`
    
    .. attribute:: ospfarearangetable
    
    	The Address Range Table acts as an adjunct to the Area Table.  It describes those Address Range Summaries that are configured to be propagated from an Area to reduce the amount of information about it that is known beyond its borders.  It contains a set of IP address ranges specified by an IP address/IP network mask pair. For example, class B address range of X.X.X.X with a network mask of 255.255.0.0 includes all IP addresses from X.X.0.0 to X.X.255.255.  Note that this table is obsoleted and is replaced by the Area Aggregate Table
    	**type**\:  :py:class:`OspfAreaRangeTable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfAreaRangeTable>`
    
    	**status**\: obsolete
    
    .. attribute:: ospfhosttable
    
    	The Host/Metric Table indicates what hosts are directly  attached to the router, what metrics and types of service should be advertised for them, and what areas they are found within
    	**type**\:  :py:class:`OspfHostTable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfHostTable>`
    
    .. attribute:: ospfiftable
    
    	The OSPF Interface Table describes the interfaces from the viewpoint of OSPF. It augments the ipAddrTable with OSPF specific information
    	**type**\:  :py:class:`OspfIfTable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfIfTable>`
    
    .. attribute:: ospfifmetrictable
    
    	The Metric Table describes the metrics to be advertised for a specified interface at the various types of service. As such, this table is an adjunct of the OSPF Interface Table.  Types of service, as defined by RFC 791, have the ability to request low delay, high bandwidth, or reliable linkage.  For the purposes of this specification, the measure of bandwidth\:  Metric = referenceBandwidth / ifSpeed  is the default value. The default reference bandwidth is 10^8. For multiple link interfaces, note that ifSpeed is the sum of the individual link speeds.  This yields a number having the following typical values\:  Network Type/bit rate   Metric  >= 100 MBPS                 1 Ethernet/802.3             10 E1                         48 T1 (ESF)                   65 64 KBPS                    1562 56 KBPS                    1785 19.2 KBPS                  5208 9.6 KBPS                   10416  Routes that are not specified use the default (TOS 0) metric.  Note that the default reference bandwidth can be configured using the general group object ospfReferenceBandwidth
    	**type**\:  :py:class:`OspfIfMetricTable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfIfMetricTable>`
    
    .. attribute:: ospfvirtiftable
    
    	Information about this router's virtual interfaces that the OSPF Process is configured to carry on
    	**type**\:  :py:class:`OspfVirtIfTable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfVirtIfTable>`
    
    .. attribute:: ospfnbrtable
    
    	A table describing all non\-virtual neighbors in the locality of the OSPF router
    	**type**\:  :py:class:`OspfNbrTable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfNbrTable>`
    
    .. attribute:: ospfvirtnbrtable
    
    	This table describes all virtual neighbors. Since virtual links are configured in the Virtual Interface Table, this table is read\-only
    	**type**\:  :py:class:`OspfVirtNbrTable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfVirtNbrTable>`
    
    .. attribute:: ospfextlsdbtable
    
    	The OSPF Process's external LSA link state database.  This table is identical to the OSPF LSDB Table in format, but contains only external link state advertisements.  The purpose is to allow external  LSAs to be displayed once for the router rather than once in each non\-stub area.  Note that external LSAs are also in the AS\-scope link state database
    	**type**\:  :py:class:`OspfExtLsdbTable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfExtLsdbTable>`
    
    	**status**\: deprecated
    
    .. attribute:: ospfareaaggregatetable
    
    	The Area Aggregate Table acts as an adjunct to the Area Table.  It describes those address aggregates that are configured to be propagated from an area. Its purpose is to reduce the amount of information that is known beyond an Area's borders.  It contains a set of IP address ranges specified by an IP address/IP network mask pair. For example, a class B address range of X.X.X.X with a network mask of 255.255.0.0 includes all IP addresses from X.X.0.0 to X.X.255.255.  Note that if ranges are configured such that one range subsumes another range (e.g., 10.0.0.0 mask 255.0.0.0 and 10.1.0.0 mask 255.255.0.0), the most specific match is the preferred one
    	**type**\:  :py:class:`OspfAreaAggregateTable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfAreaAggregateTable>`
    
    .. attribute:: ospflocallsdbtable
    
    	The OSPF Process's link\-local link state database for non\-virtual links. This table is identical to the OSPF LSDB Table in format, but contains only link\-local Link State Advertisements for non\-virtual links.  The purpose is to allow link\-local LSAs to be displayed for each non\-virtual interface.  This table is implemented to support type\-9 LSAs that are defined in 'The OSPF Opaque LSA Option'
    	**type**\:  :py:class:`OspfLocalLsdbTable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfLocalLsdbTable>`
    
    .. attribute:: ospfvirtlocallsdbtable
    
    	The OSPF Process's link\-local link state database for virtual links.  This table is identical to the OSPF LSDB Table in format, but contains only link\-local Link State Advertisements for virtual links.  The purpose is to allow link\-local LSAs to be displayed for each virtual interface.  This table is implemented to support type\-9 LSAs that are defined in 'The OSPF Opaque LSA Option'
    	**type**\:  :py:class:`OspfVirtLocalLsdbTable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfVirtLocalLsdbTable>`
    
    .. attribute:: ospfaslsdbtable
    
    	The OSPF Process's AS\-scope LSA link state database. The database contains the AS\-scope Link State Advertisements from throughout the areas that the device is attached to.  This table is identical to the OSPF LSDB Table in format, but contains only AS\-scope Link State Advertisements.  The purpose is to allow AS\-scope LSAs to be displayed once for the router rather than once in each non\-stub area
    	**type**\:  :py:class:`OspfAsLsdbTable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfAsLsdbTable>`
    
    .. attribute:: ospfarealsacounttable
    
    	This table maintains per\-area, per\-LSA\-type counters
    	**type**\:  :py:class:`OspfAreaLsaCountTable <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfAreaLsaCountTable>`
    
    

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
        self._child_classes = OrderedDict([("ospfGeneralGroup", ("ospfgeneralgroup", OSPFMIB.OspfGeneralGroup)), ("ospfAreaTable", ("ospfareatable", OSPFMIB.OspfAreaTable)), ("ospfStubAreaTable", ("ospfstubareatable", OSPFMIB.OspfStubAreaTable)), ("ospfLsdbTable", ("ospflsdbtable", OSPFMIB.OspfLsdbTable)), ("ospfAreaRangeTable", ("ospfarearangetable", OSPFMIB.OspfAreaRangeTable)), ("ospfHostTable", ("ospfhosttable", OSPFMIB.OspfHostTable)), ("ospfIfTable", ("ospfiftable", OSPFMIB.OspfIfTable)), ("ospfIfMetricTable", ("ospfifmetrictable", OSPFMIB.OspfIfMetricTable)), ("ospfVirtIfTable", ("ospfvirtiftable", OSPFMIB.OspfVirtIfTable)), ("ospfNbrTable", ("ospfnbrtable", OSPFMIB.OspfNbrTable)), ("ospfVirtNbrTable", ("ospfvirtnbrtable", OSPFMIB.OspfVirtNbrTable)), ("ospfExtLsdbTable", ("ospfextlsdbtable", OSPFMIB.OspfExtLsdbTable)), ("ospfAreaAggregateTable", ("ospfareaaggregatetable", OSPFMIB.OspfAreaAggregateTable)), ("ospfLocalLsdbTable", ("ospflocallsdbtable", OSPFMIB.OspfLocalLsdbTable)), ("ospfVirtLocalLsdbTable", ("ospfvirtlocallsdbtable", OSPFMIB.OspfVirtLocalLsdbTable)), ("ospfAsLsdbTable", ("ospfaslsdbtable", OSPFMIB.OspfAsLsdbTable)), ("ospfAreaLsaCountTable", ("ospfarealsacounttable", OSPFMIB.OspfAreaLsaCountTable))])
        self._leafs = OrderedDict()

        self.ospfgeneralgroup = OSPFMIB.OspfGeneralGroup()
        self.ospfgeneralgroup.parent = self
        self._children_name_map["ospfgeneralgroup"] = "ospfGeneralGroup"

        self.ospfareatable = OSPFMIB.OspfAreaTable()
        self.ospfareatable.parent = self
        self._children_name_map["ospfareatable"] = "ospfAreaTable"

        self.ospfstubareatable = OSPFMIB.OspfStubAreaTable()
        self.ospfstubareatable.parent = self
        self._children_name_map["ospfstubareatable"] = "ospfStubAreaTable"

        self.ospflsdbtable = OSPFMIB.OspfLsdbTable()
        self.ospflsdbtable.parent = self
        self._children_name_map["ospflsdbtable"] = "ospfLsdbTable"

        self.ospfarearangetable = OSPFMIB.OspfAreaRangeTable()
        self.ospfarearangetable.parent = self
        self._children_name_map["ospfarearangetable"] = "ospfAreaRangeTable"

        self.ospfhosttable = OSPFMIB.OspfHostTable()
        self.ospfhosttable.parent = self
        self._children_name_map["ospfhosttable"] = "ospfHostTable"

        self.ospfiftable = OSPFMIB.OspfIfTable()
        self.ospfiftable.parent = self
        self._children_name_map["ospfiftable"] = "ospfIfTable"

        self.ospfifmetrictable = OSPFMIB.OspfIfMetricTable()
        self.ospfifmetrictable.parent = self
        self._children_name_map["ospfifmetrictable"] = "ospfIfMetricTable"

        self.ospfvirtiftable = OSPFMIB.OspfVirtIfTable()
        self.ospfvirtiftable.parent = self
        self._children_name_map["ospfvirtiftable"] = "ospfVirtIfTable"

        self.ospfnbrtable = OSPFMIB.OspfNbrTable()
        self.ospfnbrtable.parent = self
        self._children_name_map["ospfnbrtable"] = "ospfNbrTable"

        self.ospfvirtnbrtable = OSPFMIB.OspfVirtNbrTable()
        self.ospfvirtnbrtable.parent = self
        self._children_name_map["ospfvirtnbrtable"] = "ospfVirtNbrTable"

        self.ospfextlsdbtable = OSPFMIB.OspfExtLsdbTable()
        self.ospfextlsdbtable.parent = self
        self._children_name_map["ospfextlsdbtable"] = "ospfExtLsdbTable"

        self.ospfareaaggregatetable = OSPFMIB.OspfAreaAggregateTable()
        self.ospfareaaggregatetable.parent = self
        self._children_name_map["ospfareaaggregatetable"] = "ospfAreaAggregateTable"

        self.ospflocallsdbtable = OSPFMIB.OspfLocalLsdbTable()
        self.ospflocallsdbtable.parent = self
        self._children_name_map["ospflocallsdbtable"] = "ospfLocalLsdbTable"

        self.ospfvirtlocallsdbtable = OSPFMIB.OspfVirtLocalLsdbTable()
        self.ospfvirtlocallsdbtable.parent = self
        self._children_name_map["ospfvirtlocallsdbtable"] = "ospfVirtLocalLsdbTable"

        self.ospfaslsdbtable = OSPFMIB.OspfAsLsdbTable()
        self.ospfaslsdbtable.parent = self
        self._children_name_map["ospfaslsdbtable"] = "ospfAsLsdbTable"

        self.ospfarealsacounttable = OSPFMIB.OspfAreaLsaCountTable()
        self.ospfarealsacounttable.parent = self
        self._children_name_map["ospfarealsacounttable"] = "ospfAreaLsaCountTable"
        self._segment_path = lambda: "OSPF-MIB:OSPF-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(OSPFMIB, [], name, value)


    class OspfGeneralGroup(Entity):
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
        	**type**\:  :py:class:`OspfVersionNumber <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfGeneralGroup.OspfVersionNumber>`
        
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
        	**type**\:  :py:class:`OspfRestartSupport <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfGeneralGroup.OspfRestartSupport>`
        
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
        	**type**\:  :py:class:`OspfRestartStatus <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfGeneralGroup.OspfRestartStatus>`
        
        .. attribute:: ospfrestartage
        
        	Remaining time in current OSPF graceful restart interval
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: seconds
        
        .. attribute:: ospfrestartexitreason
        
        	Describes the outcome of the last attempt at a graceful restart.  If the value is 'none', no restart has yet been attempted.  If the value is 'inProgress', a restart attempt is currently underway
        	**type**\:  :py:class:`OspfRestartExitReason <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfGeneralGroup.OspfRestartExitReason>`
        
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
        	**type**\:  :py:class:`OspfStubRouterAdvertisement <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfGeneralGroup.OspfStubRouterAdvertisement>`
        
        .. attribute:: ospfdiscontinuitytime
        
        	The value of sysUpTime on the most recent occasion at which any one of this MIB's counters suffered a discontinuity.  If no such discontinuities have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.OspfGeneralGroup, self).__init__()

            self.yang_name = "ospfGeneralGroup"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ospfrouterid', (YLeaf(YType.str, 'ospfRouterId'), ['str'])),
                ('ospfadminstat', (YLeaf(YType.enumeration, 'ospfAdminStat'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'Status', '')])),
                ('ospfversionnumber', (YLeaf(YType.enumeration, 'ospfVersionNumber'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfGeneralGroup.OspfVersionNumber')])),
                ('ospfareabdrrtrstatus', (YLeaf(YType.boolean, 'ospfAreaBdrRtrStatus'), ['bool'])),
                ('ospfasbdrrtrstatus', (YLeaf(YType.boolean, 'ospfASBdrRtrStatus'), ['bool'])),
                ('ospfexternlsacount', (YLeaf(YType.uint32, 'ospfExternLsaCount'), ['int'])),
                ('ospfexternlsacksumsum', (YLeaf(YType.int32, 'ospfExternLsaCksumSum'), ['int'])),
                ('ospftossupport', (YLeaf(YType.boolean, 'ospfTOSSupport'), ['bool'])),
                ('ospforiginatenewlsas', (YLeaf(YType.uint32, 'ospfOriginateNewLsas'), ['int'])),
                ('ospfrxnewlsas', (YLeaf(YType.uint32, 'ospfRxNewLsas'), ['int'])),
                ('ospfextlsdblimit', (YLeaf(YType.int32, 'ospfExtLsdbLimit'), ['int'])),
                ('ospfmulticastextensions', (YLeaf(YType.int32, 'ospfMulticastExtensions'), ['int'])),
                ('ospfexitoverflowinterval', (YLeaf(YType.int32, 'ospfExitOverflowInterval'), ['int'])),
                ('ospfdemandextensions', (YLeaf(YType.boolean, 'ospfDemandExtensions'), ['bool'])),
                ('ospfrfc1583compatibility', (YLeaf(YType.boolean, 'ospfRFC1583Compatibility'), ['bool'])),
                ('ospfopaquelsasupport', (YLeaf(YType.boolean, 'ospfOpaqueLsaSupport'), ['bool'])),
                ('ospfreferencebandwidth', (YLeaf(YType.uint32, 'ospfReferenceBandwidth'), ['int'])),
                ('ospfrestartsupport', (YLeaf(YType.enumeration, 'ospfRestartSupport'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfGeneralGroup.OspfRestartSupport')])),
                ('ospfrestartinterval', (YLeaf(YType.int32, 'ospfRestartInterval'), ['int'])),
                ('ospfrestartstrictlsachecking', (YLeaf(YType.boolean, 'ospfRestartStrictLsaChecking'), ['bool'])),
                ('ospfrestartstatus', (YLeaf(YType.enumeration, 'ospfRestartStatus'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfGeneralGroup.OspfRestartStatus')])),
                ('ospfrestartage', (YLeaf(YType.uint32, 'ospfRestartAge'), ['int'])),
                ('ospfrestartexitreason', (YLeaf(YType.enumeration, 'ospfRestartExitReason'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfGeneralGroup.OspfRestartExitReason')])),
                ('ospfaslsacount', (YLeaf(YType.uint32, 'ospfAsLsaCount'), ['int'])),
                ('ospfaslsacksumsum', (YLeaf(YType.uint32, 'ospfAsLsaCksumSum'), ['int'])),
                ('ospfstubroutersupport', (YLeaf(YType.boolean, 'ospfStubRouterSupport'), ['bool'])),
                ('ospfstubrouteradvertisement', (YLeaf(YType.enumeration, 'ospfStubRouterAdvertisement'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfGeneralGroup.OspfStubRouterAdvertisement')])),
                ('ospfdiscontinuitytime', (YLeaf(YType.uint32, 'ospfDiscontinuityTime'), ['int'])),
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
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.OspfGeneralGroup, [u'ospfrouterid', u'ospfadminstat', u'ospfversionnumber', u'ospfareabdrrtrstatus', u'ospfasbdrrtrstatus', u'ospfexternlsacount', u'ospfexternlsacksumsum', u'ospftossupport', u'ospforiginatenewlsas', u'ospfrxnewlsas', u'ospfextlsdblimit', u'ospfmulticastextensions', u'ospfexitoverflowinterval', u'ospfdemandextensions', u'ospfrfc1583compatibility', u'ospfopaquelsasupport', u'ospfreferencebandwidth', u'ospfrestartsupport', u'ospfrestartinterval', u'ospfrestartstrictlsachecking', u'ospfrestartstatus', u'ospfrestartage', u'ospfrestartexitreason', u'ospfaslsacount', u'ospfaslsacksumsum', u'ospfstubroutersupport', u'ospfstubrouteradvertisement', u'ospfdiscontinuitytime'], name, value)

        class OspfRestartExitReason(Enum):
            """
            OspfRestartExitReason (Enum Class)

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


        class OspfRestartStatus(Enum):
            """
            OspfRestartStatus (Enum Class)

            Current status of OSPF graceful restart.

            .. data:: notRestarting = 1

            .. data:: plannedRestart = 2

            .. data:: unplannedRestart = 3

            """

            notRestarting = Enum.YLeaf(1, "notRestarting")

            plannedRestart = Enum.YLeaf(2, "plannedRestart")

            unplannedRestart = Enum.YLeaf(3, "unplannedRestart")


        class OspfRestartSupport(Enum):
            """
            OspfRestartSupport (Enum Class)

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


        class OspfStubRouterAdvertisement(Enum):
            """
            OspfStubRouterAdvertisement (Enum Class)

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


        class OspfVersionNumber(Enum):
            """
            OspfVersionNumber (Enum Class)

            The current version number of the OSPF protocol is 2.

            .. data:: version2 = 2

            """

            version2 = Enum.YLeaf(2, "version2")



    class OspfAreaTable(Entity):
        """
        Information describing the configured parameters and
        cumulative statistics of the router's attached areas.
        The interfaces and virtual links are configured
        as part of these areas.  Area 0.0.0.0, by definition,
        is the backbone area.
        
        .. attribute:: ospfareaentry
        
        	Information describing the configured parameters and cumulative statistics of one of the router's attached areas. The interfaces and virtual links are configured as part of these areas.  Area 0.0.0.0, by definition, is the backbone area.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile storage
        	**type**\: list of  		 :py:class:`OspfAreaEntry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfAreaTable.OspfAreaEntry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.OspfAreaTable, self).__init__()

            self.yang_name = "ospfAreaTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ospfAreaEntry", ("ospfareaentry", OSPFMIB.OspfAreaTable.OspfAreaEntry))])
            self._leafs = OrderedDict()

            self.ospfareaentry = YList(self)
            self._segment_path = lambda: "ospfAreaTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.OspfAreaTable, [], name, value)


        class OspfAreaEntry(Entity):
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
            	**type**\:  :py:class:`OspfImportAsExtern <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfAreaTable.OspfAreaEntry.OspfImportAsExtern>`
            
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
            	**type**\:  :py:class:`OspfAreaSummary <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfAreaTable.OspfAreaEntry.OspfAreaSummary>`
            
            .. attribute:: ospfareastatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: ospfareanssatranslatorrole
            
            	Indicates an NSSA border router's ability to perform NSSA translation of type\-7 LSAs into type\-5 LSAs
            	**type**\:  :py:class:`OspfAreaNssaTranslatorRole <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfAreaTable.OspfAreaEntry.OspfAreaNssaTranslatorRole>`
            
            .. attribute:: ospfareanssatranslatorstate
            
            	Indicates if and how an NSSA border router is performing NSSA translation of type\-7 LSAs into type\-5  LSAs.  When this object is set to enabled, the NSSA Border router's OspfAreaNssaExtTranslatorRole has been set to always.  When this object is set to elected, a candidate NSSA Border router is Translating type\-7 LSAs into type\-5. When this object is set to disabled, a candidate NSSA border router is NOT translating type\-7 LSAs into type\-5
            	**type**\:  :py:class:`OspfAreaNssaTranslatorState <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfAreaTable.OspfAreaEntry.OspfAreaNssaTranslatorState>`
            
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
            	**type**\:  :py:class:`CospfAreaNssaTranslatorRole <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfAreaTable.OspfAreaEntry.CospfAreaNssaTranslatorRole>`
            
            .. attribute:: cospfareanssatranslatorstate
            
            	Indicates if and how an NSSA Border router is performing NSSA translation of type\-7 LSAs into type\-5 LSAs. When this object set to enabled, the NSSA Border router's cospfAreaNssaExtTranslatorRole has been set to always. When this object is set to elected, a candidate NSSA Border router is Translating type\-7 LSAs into type\-5. When this object is set to disabled, a candidate NSSA Border router is NOT translating type\-7 LSAs into type\-5
            	**type**\:  :py:class:`CospfAreaNssaTranslatorState <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfAreaTable.OspfAreaEntry.CospfAreaNssaTranslatorState>`
            
            .. attribute:: cospfareanssatranslatorevents
            
            	Indicates the number of Translator State changes that have occurred since the last boot\-up
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OSPFMIB.OspfAreaTable.OspfAreaEntry, self).__init__()

                self.yang_name = "ospfAreaEntry"
                self.yang_parent_name = "ospfAreaTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfareaid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfareaid', (YLeaf(YType.str, 'ospfAreaId'), ['str'])),
                    ('ospfauthtype', (YLeaf(YType.enumeration, 'ospfAuthType'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfAuthenticationType', '')])),
                    ('ospfimportasextern', (YLeaf(YType.enumeration, 'ospfImportAsExtern'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfAreaTable.OspfAreaEntry.OspfImportAsExtern')])),
                    ('ospfspfruns', (YLeaf(YType.uint32, 'ospfSpfRuns'), ['int'])),
                    ('ospfareabdrrtrcount', (YLeaf(YType.uint32, 'ospfAreaBdrRtrCount'), ['int'])),
                    ('ospfasbdrrtrcount', (YLeaf(YType.uint32, 'ospfAsBdrRtrCount'), ['int'])),
                    ('ospfarealsacount', (YLeaf(YType.uint32, 'ospfAreaLsaCount'), ['int'])),
                    ('ospfarealsacksumsum', (YLeaf(YType.int32, 'ospfAreaLsaCksumSum'), ['int'])),
                    ('ospfareasummary', (YLeaf(YType.enumeration, 'ospfAreaSummary'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfAreaTable.OspfAreaEntry.OspfAreaSummary')])),
                    ('ospfareastatus', (YLeaf(YType.enumeration, 'ospfAreaStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('ospfareanssatranslatorrole', (YLeaf(YType.enumeration, 'ospfAreaNssaTranslatorRole'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfAreaTable.OspfAreaEntry.OspfAreaNssaTranslatorRole')])),
                    ('ospfareanssatranslatorstate', (YLeaf(YType.enumeration, 'ospfAreaNssaTranslatorState'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfAreaTable.OspfAreaEntry.OspfAreaNssaTranslatorState')])),
                    ('ospfareanssatranslatorstabilityinterval', (YLeaf(YType.int32, 'ospfAreaNssaTranslatorStabilityInterval'), ['int'])),
                    ('ospfareanssatranslatorevents', (YLeaf(YType.uint32, 'ospfAreaNssaTranslatorEvents'), ['int'])),
                    ('cospfopaquearealsacount', (YLeaf(YType.uint32, 'CISCO-OSPF-MIB:cospfOpaqueAreaLsaCount'), ['int'])),
                    ('cospfopaquearealsacksumsum', (YLeaf(YType.uint32, 'CISCO-OSPF-MIB:cospfOpaqueAreaLsaCksumSum'), ['int'])),
                    ('cospfareanssatranslatorrole', (YLeaf(YType.enumeration, 'CISCO-OSPF-MIB:cospfAreaNssaTranslatorRole'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfAreaTable.OspfAreaEntry.CospfAreaNssaTranslatorRole')])),
                    ('cospfareanssatranslatorstate', (YLeaf(YType.enumeration, 'CISCO-OSPF-MIB:cospfAreaNssaTranslatorState'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfAreaTable.OspfAreaEntry.CospfAreaNssaTranslatorState')])),
                    ('cospfareanssatranslatorevents', (YLeaf(YType.uint32, 'CISCO-OSPF-MIB:cospfAreaNssaTranslatorEvents'), ['int'])),
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
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.OspfAreaTable.OspfAreaEntry, [u'ospfareaid', u'ospfauthtype', u'ospfimportasextern', u'ospfspfruns', u'ospfareabdrrtrcount', u'ospfasbdrrtrcount', u'ospfarealsacount', u'ospfarealsacksumsum', u'ospfareasummary', u'ospfareastatus', u'ospfareanssatranslatorrole', u'ospfareanssatranslatorstate', u'ospfareanssatranslatorstabilityinterval', u'ospfareanssatranslatorevents', u'cospfopaquearealsacount', u'cospfopaquearealsacksumsum', u'cospfareanssatranslatorrole', u'cospfareanssatranslatorstate', u'cospfareanssatranslatorevents'], name, value)

            class CospfAreaNssaTranslatorRole(Enum):
                """
                CospfAreaNssaTranslatorRole (Enum Class)

                Indicates an NSSA Border router's ability to

                perform NSSA translation of type\-7 LSAs into

                type\-5 LSAs.

                .. data:: always = 1

                .. data:: candidate = 2

                """

                always = Enum.YLeaf(1, "always")

                candidate = Enum.YLeaf(2, "candidate")


            class CospfAreaNssaTranslatorState(Enum):
                """
                CospfAreaNssaTranslatorState (Enum Class)

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


            class OspfAreaNssaTranslatorRole(Enum):
                """
                OspfAreaNssaTranslatorRole (Enum Class)

                Indicates an NSSA border router's ability to

                perform NSSA translation of type\-7 LSAs into

                type\-5 LSAs.

                .. data:: always = 1

                .. data:: candidate = 2

                """

                always = Enum.YLeaf(1, "always")

                candidate = Enum.YLeaf(2, "candidate")


            class OspfAreaNssaTranslatorState(Enum):
                """
                OspfAreaNssaTranslatorState (Enum Class)

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


            class OspfAreaSummary(Enum):
                """
                OspfAreaSummary (Enum Class)

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


            class OspfImportAsExtern(Enum):
                """
                OspfImportAsExtern (Enum Class)

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



    class OspfStubAreaTable(Entity):
        """
        The set of metrics that will be advertised
        by a default Area Border Router into a stub area.
        
        .. attribute:: ospfstubareaentry
        
        	The metric for a given Type of Service that will be advertised by a default Area Border Router into a stub area.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile storage
        	**type**\: list of  		 :py:class:`OspfStubAreaEntry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfStubAreaTable.OspfStubAreaEntry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.OspfStubAreaTable, self).__init__()

            self.yang_name = "ospfStubAreaTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ospfStubAreaEntry", ("ospfstubareaentry", OSPFMIB.OspfStubAreaTable.OspfStubAreaEntry))])
            self._leafs = OrderedDict()

            self.ospfstubareaentry = YList(self)
            self._segment_path = lambda: "ospfStubAreaTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.OspfStubAreaTable, [], name, value)


        class OspfStubAreaEntry(Entity):
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
            	**type**\:  :py:class:`OspfStubMetricType <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfStubAreaTable.OspfStubAreaEntry.OspfStubMetricType>`
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OSPFMIB.OspfStubAreaTable.OspfStubAreaEntry, self).__init__()

                self.yang_name = "ospfStubAreaEntry"
                self.yang_parent_name = "ospfStubAreaTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfstubareaid','ospfstubtos']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfstubareaid', (YLeaf(YType.str, 'ospfStubAreaId'), ['str'])),
                    ('ospfstubtos', (YLeaf(YType.int32, 'ospfStubTOS'), ['int'])),
                    ('ospfstubmetric', (YLeaf(YType.int32, 'ospfStubMetric'), ['int'])),
                    ('ospfstubstatus', (YLeaf(YType.enumeration, 'ospfStubStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('ospfstubmetrictype', (YLeaf(YType.enumeration, 'ospfStubMetricType'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfStubAreaTable.OspfStubAreaEntry.OspfStubMetricType')])),
                ])
                self.ospfstubareaid = None
                self.ospfstubtos = None
                self.ospfstubmetric = None
                self.ospfstubstatus = None
                self.ospfstubmetrictype = None
                self._segment_path = lambda: "ospfStubAreaEntry" + "[ospfStubAreaId='" + str(self.ospfstubareaid) + "']" + "[ospfStubTOS='" + str(self.ospfstubtos) + "']"
                self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/ospfStubAreaTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.OspfStubAreaTable.OspfStubAreaEntry, [u'ospfstubareaid', u'ospfstubtos', u'ospfstubmetric', u'ospfstubstatus', u'ospfstubmetrictype'], name, value)

            class OspfStubMetricType(Enum):
                """
                OspfStubMetricType (Enum Class)

                This variable displays the type of metric

                advertised as a default route.

                .. data:: ospfMetric = 1

                .. data:: comparableCost = 2

                .. data:: nonComparable = 3

                """

                ospfMetric = Enum.YLeaf(1, "ospfMetric")

                comparableCost = Enum.YLeaf(2, "comparableCost")

                nonComparable = Enum.YLeaf(3, "nonComparable")



    class OspfLsdbTable(Entity):
        """
        The OSPF Process's link state database (LSDB).
        The LSDB contains the link state advertisements
        from throughout the areas that the device is attached to.
        
        .. attribute:: ospflsdbentry
        
        	A single link state advertisement
        	**type**\: list of  		 :py:class:`OspfLsdbEntry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfLsdbTable.OspfLsdbEntry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.OspfLsdbTable, self).__init__()

            self.yang_name = "ospfLsdbTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ospfLsdbEntry", ("ospflsdbentry", OSPFMIB.OspfLsdbTable.OspfLsdbEntry))])
            self._leafs = OrderedDict()

            self.ospflsdbentry = YList(self)
            self._segment_path = lambda: "ospfLsdbTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.OspfLsdbTable, [], name, value)


        class OspfLsdbEntry(Entity):
            """
            A single link state advertisement.
            
            .. attribute:: ospflsdbareaid  (key)
            
            	The 32\-bit identifier of the area from which the LSA was received
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospflsdbtype  (key)
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format.  Note\: External link state advertisements are permitted for backward compatibility, but should be displayed in the ospfAsLsdbTable rather than here
            	**type**\:  :py:class:`OspfLsdbType <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfLsdbTable.OspfLsdbEntry.OspfLsdbType>`
            
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
                super(OSPFMIB.OspfLsdbTable.OspfLsdbEntry, self).__init__()

                self.yang_name = "ospfLsdbEntry"
                self.yang_parent_name = "ospfLsdbTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospflsdbareaid','ospflsdbtype','ospflsdblsid','ospflsdbrouterid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospflsdbareaid', (YLeaf(YType.str, 'ospfLsdbAreaId'), ['str'])),
                    ('ospflsdbtype', (YLeaf(YType.enumeration, 'ospfLsdbType'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfLsdbTable.OspfLsdbEntry.OspfLsdbType')])),
                    ('ospflsdblsid', (YLeaf(YType.str, 'ospfLsdbLsid'), ['str'])),
                    ('ospflsdbrouterid', (YLeaf(YType.str, 'ospfLsdbRouterId'), ['str'])),
                    ('ospflsdbsequence', (YLeaf(YType.int32, 'ospfLsdbSequence'), ['int'])),
                    ('ospflsdbage', (YLeaf(YType.int32, 'ospfLsdbAge'), ['int'])),
                    ('ospflsdbchecksum', (YLeaf(YType.int32, 'ospfLsdbChecksum'), ['int'])),
                    ('ospflsdbadvertisement', (YLeaf(YType.str, 'ospfLsdbAdvertisement'), ['str'])),
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
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.OspfLsdbTable.OspfLsdbEntry, [u'ospflsdbareaid', u'ospflsdbtype', u'ospflsdblsid', u'ospflsdbrouterid', u'ospflsdbsequence', u'ospflsdbage', u'ospflsdbchecksum', u'ospflsdbadvertisement'], name, value)

            class OspfLsdbType(Enum):
                """
                OspfLsdbType (Enum Class)

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



    class OspfAreaRangeTable(Entity):
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
        	**type**\: list of  		 :py:class:`OspfAreaRangeEntry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfAreaRangeTable.OspfAreaRangeEntry>`
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.OspfAreaRangeTable, self).__init__()

            self.yang_name = "ospfAreaRangeTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ospfAreaRangeEntry", ("ospfarearangeentry", OSPFMIB.OspfAreaRangeTable.OspfAreaRangeEntry))])
            self._leafs = OrderedDict()

            self.ospfarearangeentry = YList(self)
            self._segment_path = lambda: "ospfAreaRangeTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.OspfAreaRangeTable, [], name, value)


        class OspfAreaRangeEntry(Entity):
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
            	**type**\:  :py:class:`OspfAreaRangeEffect <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfAreaRangeTable.OspfAreaRangeEntry.OspfAreaRangeEffect>`
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OSPFMIB.OspfAreaRangeTable.OspfAreaRangeEntry, self).__init__()

                self.yang_name = "ospfAreaRangeEntry"
                self.yang_parent_name = "ospfAreaRangeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfarearangeareaid','ospfarearangenet']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfarearangeareaid', (YLeaf(YType.str, 'ospfAreaRangeAreaId'), ['str'])),
                    ('ospfarearangenet', (YLeaf(YType.str, 'ospfAreaRangeNet'), ['str'])),
                    ('ospfarearangemask', (YLeaf(YType.str, 'ospfAreaRangeMask'), ['str'])),
                    ('ospfarearangestatus', (YLeaf(YType.enumeration, 'ospfAreaRangeStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('ospfarearangeeffect', (YLeaf(YType.enumeration, 'ospfAreaRangeEffect'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfAreaRangeTable.OspfAreaRangeEntry.OspfAreaRangeEffect')])),
                ])
                self.ospfarearangeareaid = None
                self.ospfarearangenet = None
                self.ospfarearangemask = None
                self.ospfarearangestatus = None
                self.ospfarearangeeffect = None
                self._segment_path = lambda: "ospfAreaRangeEntry" + "[ospfAreaRangeAreaId='" + str(self.ospfarearangeareaid) + "']" + "[ospfAreaRangeNet='" + str(self.ospfarearangenet) + "']"
                self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/ospfAreaRangeTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.OspfAreaRangeTable.OspfAreaRangeEntry, [u'ospfarearangeareaid', u'ospfarearangenet', u'ospfarearangemask', u'ospfarearangestatus', u'ospfarearangeeffect'], name, value)

            class OspfAreaRangeEffect(Enum):
                """
                OspfAreaRangeEffect (Enum Class)

                Subnets subsumed by ranges either trigger the

                advertisement of the indicated summary

                (advertiseMatching) or result in the subnet's not

                being advertised at all outside the area.

                .. data:: advertiseMatching = 1

                .. data:: doNotAdvertiseMatching = 2

                """

                advertiseMatching = Enum.YLeaf(1, "advertiseMatching")

                doNotAdvertiseMatching = Enum.YLeaf(2, "doNotAdvertiseMatching")



    class OspfHostTable(Entity):
        """
        The Host/Metric Table indicates what hosts are directly
        
        attached to the router, what metrics and types
        of service should be advertised for them,
        and what areas they are found within.
        
        .. attribute:: ospfhostentry
        
        	A metric to be advertised, for a given type of service, when a given host is reachable.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile storage
        	**type**\: list of  		 :py:class:`OspfHostEntry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfHostTable.OspfHostEntry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.OspfHostTable, self).__init__()

            self.yang_name = "ospfHostTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ospfHostEntry", ("ospfhostentry", OSPFMIB.OspfHostTable.OspfHostEntry))])
            self._leafs = OrderedDict()

            self.ospfhostentry = YList(self)
            self._segment_path = lambda: "ospfHostTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.OspfHostTable, [], name, value)


        class OspfHostEntry(Entity):
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
                super(OSPFMIB.OspfHostTable.OspfHostEntry, self).__init__()

                self.yang_name = "ospfHostEntry"
                self.yang_parent_name = "ospfHostTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfhostipaddress','ospfhosttos']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfhostipaddress', (YLeaf(YType.str, 'ospfHostIpAddress'), ['str'])),
                    ('ospfhosttos', (YLeaf(YType.int32, 'ospfHostTOS'), ['int'])),
                    ('ospfhostmetric', (YLeaf(YType.int32, 'ospfHostMetric'), ['int'])),
                    ('ospfhoststatus', (YLeaf(YType.enumeration, 'ospfHostStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('ospfhostareaid', (YLeaf(YType.str, 'ospfHostAreaID'), ['str'])),
                    ('ospfhostcfgareaid', (YLeaf(YType.str, 'ospfHostCfgAreaID'), ['str'])),
                ])
                self.ospfhostipaddress = None
                self.ospfhosttos = None
                self.ospfhostmetric = None
                self.ospfhoststatus = None
                self.ospfhostareaid = None
                self.ospfhostcfgareaid = None
                self._segment_path = lambda: "ospfHostEntry" + "[ospfHostIpAddress='" + str(self.ospfhostipaddress) + "']" + "[ospfHostTOS='" + str(self.ospfhosttos) + "']"
                self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/ospfHostTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.OspfHostTable.OspfHostEntry, [u'ospfhostipaddress', u'ospfhosttos', u'ospfhostmetric', u'ospfhoststatus', u'ospfhostareaid', u'ospfhostcfgareaid'], name, value)


    class OspfIfTable(Entity):
        """
        The OSPF Interface Table describes the interfaces
        from the viewpoint of OSPF.
        It augments the ipAddrTable with OSPF specific information.
        
        .. attribute:: ospfifentry
        
        	The OSPF interface entry describes one interface from the viewpoint of OSPF.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile storage
        	**type**\: list of  		 :py:class:`OspfIfEntry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfIfTable.OspfIfEntry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.OspfIfTable, self).__init__()

            self.yang_name = "ospfIfTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ospfIfEntry", ("ospfifentry", OSPFMIB.OspfIfTable.OspfIfEntry))])
            self._leafs = OrderedDict()

            self.ospfifentry = YList(self)
            self._segment_path = lambda: "ospfIfTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.OspfIfTable, [], name, value)


        class OspfIfEntry(Entity):
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
            	**type**\:  :py:class:`OspfIfType <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfIfTable.OspfIfEntry.OspfIfType>`
            
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
            	**type**\:  :py:class:`OspfIfState <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfIfTable.OspfIfEntry.OspfIfState>`
            
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
            	**type**\:  :py:class:`OspfIfMulticastForwarding <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfIfTable.OspfIfEntry.OspfIfMulticastForwarding>`
            
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
                super(OSPFMIB.OspfIfTable.OspfIfEntry, self).__init__()

                self.yang_name = "ospfIfEntry"
                self.yang_parent_name = "ospfIfTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfifipaddress','ospfaddresslessif']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfifipaddress', (YLeaf(YType.str, 'ospfIfIpAddress'), ['str'])),
                    ('ospfaddresslessif', (YLeaf(YType.int32, 'ospfAddressLessIf'), ['int'])),
                    ('ospfifareaid', (YLeaf(YType.str, 'ospfIfAreaId'), ['str'])),
                    ('ospfiftype', (YLeaf(YType.enumeration, 'ospfIfType'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfIfTable.OspfIfEntry.OspfIfType')])),
                    ('ospfifadminstat', (YLeaf(YType.enumeration, 'ospfIfAdminStat'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'Status', '')])),
                    ('ospfifrtrpriority', (YLeaf(YType.int32, 'ospfIfRtrPriority'), ['int'])),
                    ('ospfiftransitdelay', (YLeaf(YType.int32, 'ospfIfTransitDelay'), ['int'])),
                    ('ospfifretransinterval', (YLeaf(YType.int32, 'ospfIfRetransInterval'), ['int'])),
                    ('ospfifhellointerval', (YLeaf(YType.int32, 'ospfIfHelloInterval'), ['int'])),
                    ('ospfifrtrdeadinterval', (YLeaf(YType.int32, 'ospfIfRtrDeadInterval'), ['int'])),
                    ('ospfifpollinterval', (YLeaf(YType.int32, 'ospfIfPollInterval'), ['int'])),
                    ('ospfifstate', (YLeaf(YType.enumeration, 'ospfIfState'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfIfTable.OspfIfEntry.OspfIfState')])),
                    ('ospfifdesignatedrouter', (YLeaf(YType.str, 'ospfIfDesignatedRouter'), ['str'])),
                    ('ospfifbackupdesignatedrouter', (YLeaf(YType.str, 'ospfIfBackupDesignatedRouter'), ['str'])),
                    ('ospfifevents', (YLeaf(YType.uint32, 'ospfIfEvents'), ['int'])),
                    ('ospfifauthkey', (YLeaf(YType.str, 'ospfIfAuthKey'), ['str'])),
                    ('ospfifstatus', (YLeaf(YType.enumeration, 'ospfIfStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('ospfifmulticastforwarding', (YLeaf(YType.enumeration, 'ospfIfMulticastForwarding'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfIfTable.OspfIfEntry.OspfIfMulticastForwarding')])),
                    ('ospfifdemand', (YLeaf(YType.boolean, 'ospfIfDemand'), ['bool'])),
                    ('ospfifauthtype', (YLeaf(YType.enumeration, 'ospfIfAuthType'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfAuthenticationType', '')])),
                    ('ospfiflsacount', (YLeaf(YType.uint32, 'ospfIfLsaCount'), ['int'])),
                    ('ospfiflsacksumsum', (YLeaf(YType.uint32, 'ospfIfLsaCksumSum'), ['int'])),
                    ('ospfifdesignatedrouterid', (YLeaf(YType.str, 'ospfIfDesignatedRouterId'), ['str'])),
                    ('ospfifbackupdesignatedrouterid', (YLeaf(YType.str, 'ospfIfBackupDesignatedRouterId'), ['str'])),
                    ('cospfiflsacount', (YLeaf(YType.uint32, 'CISCO-OSPF-MIB:cospfIfLsaCount'), ['int'])),
                    ('cospfiflsacksumsum', (YLeaf(YType.uint32, 'CISCO-OSPF-MIB:cospfIfLsaCksumSum'), ['int'])),
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
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.OspfIfTable.OspfIfEntry, [u'ospfifipaddress', u'ospfaddresslessif', u'ospfifareaid', u'ospfiftype', u'ospfifadminstat', u'ospfifrtrpriority', u'ospfiftransitdelay', u'ospfifretransinterval', u'ospfifhellointerval', u'ospfifrtrdeadinterval', u'ospfifpollinterval', u'ospfifstate', u'ospfifdesignatedrouter', u'ospfifbackupdesignatedrouter', u'ospfifevents', u'ospfifauthkey', u'ospfifstatus', u'ospfifmulticastforwarding', u'ospfifdemand', u'ospfifauthtype', u'ospfiflsacount', u'ospfiflsacksumsum', u'ospfifdesignatedrouterid', u'ospfifbackupdesignatedrouterid', u'cospfiflsacount', u'cospfiflsacksumsum'], name, value)

            class OspfIfMulticastForwarding(Enum):
                """
                OspfIfMulticastForwarding (Enum Class)

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


            class OspfIfState(Enum):
                """
                OspfIfState (Enum Class)

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


            class OspfIfType(Enum):
                """
                OspfIfType (Enum Class)

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



    class OspfIfMetricTable(Entity):
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
        	**type**\: list of  		 :py:class:`OspfIfMetricEntry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfIfMetricTable.OspfIfMetricEntry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.OspfIfMetricTable, self).__init__()

            self.yang_name = "ospfIfMetricTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ospfIfMetricEntry", ("ospfifmetricentry", OSPFMIB.OspfIfMetricTable.OspfIfMetricEntry))])
            self._leafs = OrderedDict()

            self.ospfifmetricentry = YList(self)
            self._segment_path = lambda: "ospfIfMetricTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.OspfIfMetricTable, [], name, value)


        class OspfIfMetricEntry(Entity):
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
                super(OSPFMIB.OspfIfMetricTable.OspfIfMetricEntry, self).__init__()

                self.yang_name = "ospfIfMetricEntry"
                self.yang_parent_name = "ospfIfMetricTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfifmetricipaddress','ospfifmetricaddresslessif','ospfifmetrictos']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfifmetricipaddress', (YLeaf(YType.str, 'ospfIfMetricIpAddress'), ['str'])),
                    ('ospfifmetricaddresslessif', (YLeaf(YType.int32, 'ospfIfMetricAddressLessIf'), ['int'])),
                    ('ospfifmetrictos', (YLeaf(YType.int32, 'ospfIfMetricTOS'), ['int'])),
                    ('ospfifmetricvalue', (YLeaf(YType.int32, 'ospfIfMetricValue'), ['int'])),
                    ('ospfifmetricstatus', (YLeaf(YType.enumeration, 'ospfIfMetricStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.ospfifmetricipaddress = None
                self.ospfifmetricaddresslessif = None
                self.ospfifmetrictos = None
                self.ospfifmetricvalue = None
                self.ospfifmetricstatus = None
                self._segment_path = lambda: "ospfIfMetricEntry" + "[ospfIfMetricIpAddress='" + str(self.ospfifmetricipaddress) + "']" + "[ospfIfMetricAddressLessIf='" + str(self.ospfifmetricaddresslessif) + "']" + "[ospfIfMetricTOS='" + str(self.ospfifmetrictos) + "']"
                self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/ospfIfMetricTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.OspfIfMetricTable.OspfIfMetricEntry, [u'ospfifmetricipaddress', u'ospfifmetricaddresslessif', u'ospfifmetrictos', u'ospfifmetricvalue', u'ospfifmetricstatus'], name, value)


    class OspfVirtIfTable(Entity):
        """
        Information about this router's virtual interfaces
        that the OSPF Process is configured to carry on.
        
        .. attribute:: ospfvirtifentry
        
        	Information about a single virtual interface.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile storage
        	**type**\: list of  		 :py:class:`OspfVirtIfEntry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfVirtIfTable.OspfVirtIfEntry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.OspfVirtIfTable, self).__init__()

            self.yang_name = "ospfVirtIfTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ospfVirtIfEntry", ("ospfvirtifentry", OSPFMIB.OspfVirtIfTable.OspfVirtIfEntry))])
            self._leafs = OrderedDict()

            self.ospfvirtifentry = YList(self)
            self._segment_path = lambda: "ospfVirtIfTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.OspfVirtIfTable, [], name, value)


        class OspfVirtIfEntry(Entity):
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
            	**type**\:  :py:class:`OspfVirtIfState <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfVirtIfTable.OspfVirtIfEntry.OspfVirtIfState>`
            
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
                super(OSPFMIB.OspfVirtIfTable.OspfVirtIfEntry, self).__init__()

                self.yang_name = "ospfVirtIfEntry"
                self.yang_parent_name = "ospfVirtIfTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfvirtifareaid','ospfvirtifneighbor']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfvirtifareaid', (YLeaf(YType.str, 'ospfVirtIfAreaId'), ['str'])),
                    ('ospfvirtifneighbor', (YLeaf(YType.str, 'ospfVirtIfNeighbor'), ['str'])),
                    ('ospfvirtiftransitdelay', (YLeaf(YType.int32, 'ospfVirtIfTransitDelay'), ['int'])),
                    ('ospfvirtifretransinterval', (YLeaf(YType.int32, 'ospfVirtIfRetransInterval'), ['int'])),
                    ('ospfvirtifhellointerval', (YLeaf(YType.int32, 'ospfVirtIfHelloInterval'), ['int'])),
                    ('ospfvirtifrtrdeadinterval', (YLeaf(YType.int32, 'ospfVirtIfRtrDeadInterval'), ['int'])),
                    ('ospfvirtifstate', (YLeaf(YType.enumeration, 'ospfVirtIfState'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfVirtIfTable.OspfVirtIfEntry.OspfVirtIfState')])),
                    ('ospfvirtifevents', (YLeaf(YType.uint32, 'ospfVirtIfEvents'), ['int'])),
                    ('ospfvirtifauthkey', (YLeaf(YType.str, 'ospfVirtIfAuthKey'), ['str'])),
                    ('ospfvirtifstatus', (YLeaf(YType.enumeration, 'ospfVirtIfStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('ospfvirtifauthtype', (YLeaf(YType.enumeration, 'ospfVirtIfAuthType'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfAuthenticationType', '')])),
                    ('ospfvirtiflsacount', (YLeaf(YType.uint32, 'ospfVirtIfLsaCount'), ['int'])),
                    ('ospfvirtiflsacksumsum', (YLeaf(YType.uint32, 'ospfVirtIfLsaCksumSum'), ['int'])),
                    ('cospfvirtiflsacount', (YLeaf(YType.uint32, 'CISCO-OSPF-MIB:cospfVirtIfLsaCount'), ['int'])),
                    ('cospfvirtiflsacksumsum', (YLeaf(YType.uint32, 'CISCO-OSPF-MIB:cospfVirtIfLsaCksumSum'), ['int'])),
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
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.OspfVirtIfTable.OspfVirtIfEntry, [u'ospfvirtifareaid', u'ospfvirtifneighbor', u'ospfvirtiftransitdelay', u'ospfvirtifretransinterval', u'ospfvirtifhellointerval', u'ospfvirtifrtrdeadinterval', u'ospfvirtifstate', u'ospfvirtifevents', u'ospfvirtifauthkey', u'ospfvirtifstatus', u'ospfvirtifauthtype', u'ospfvirtiflsacount', u'ospfvirtiflsacksumsum', u'cospfvirtiflsacount', u'cospfvirtiflsacksumsum'], name, value)

            class OspfVirtIfState(Enum):
                """
                OspfVirtIfState (Enum Class)

                OSPF virtual interface states.

                .. data:: down = 1

                .. data:: pointToPoint = 4

                """

                down = Enum.YLeaf(1, "down")

                pointToPoint = Enum.YLeaf(4, "pointToPoint")



    class OspfNbrTable(Entity):
        """
        A table describing all non\-virtual neighbors
        in the locality of the OSPF router.
        
        .. attribute:: ospfnbrentry
        
        	The information regarding a single neighbor.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile  storage
        	**type**\: list of  		 :py:class:`OspfNbrEntry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfNbrTable.OspfNbrEntry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.OspfNbrTable, self).__init__()

            self.yang_name = "ospfNbrTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ospfNbrEntry", ("ospfnbrentry", OSPFMIB.OspfNbrTable.OspfNbrEntry))])
            self._leafs = OrderedDict()

            self.ospfnbrentry = YList(self)
            self._segment_path = lambda: "ospfNbrTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.OspfNbrTable, [], name, value)


        class OspfNbrEntry(Entity):
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
            	**type**\:  :py:class:`OspfNbrState <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfNbrTable.OspfNbrEntry.OspfNbrState>`
            
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
            	**type**\:  :py:class:`OspfNbmaNbrPermanence <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfNbrTable.OspfNbrEntry.OspfNbmaNbrPermanence>`
            
            .. attribute:: ospfnbrhellosuppressed
            
            	Indicates whether Hellos are being suppressed to the neighbor
            	**type**\: bool
            
            .. attribute:: ospfnbrrestarthelperstatus
            
            	Indicates whether the router is acting as a graceful restart helper for the neighbor
            	**type**\:  :py:class:`OspfNbrRestartHelperStatus <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfNbrTable.OspfNbrEntry.OspfNbrRestartHelperStatus>`
            
            .. attribute:: ospfnbrrestarthelperage
            
            	Remaining time in current OSPF graceful restart interval, if the router is acting as a restart helper for the neighbor
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: ospfnbrrestarthelperexitreason
            
            	Describes the outcome of the last attempt at acting as a graceful restart helper for the neighbor
            	**type**\:  :py:class:`OspfNbrRestartHelperExitReason <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfNbrTable.OspfNbrEntry.OspfNbrRestartHelperExitReason>`
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OSPFMIB.OspfNbrTable.OspfNbrEntry, self).__init__()

                self.yang_name = "ospfNbrEntry"
                self.yang_parent_name = "ospfNbrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfnbripaddr','ospfnbraddresslessindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfnbripaddr', (YLeaf(YType.str, 'ospfNbrIpAddr'), ['str'])),
                    ('ospfnbraddresslessindex', (YLeaf(YType.int32, 'ospfNbrAddressLessIndex'), ['int'])),
                    ('ospfnbrrtrid', (YLeaf(YType.str, 'ospfNbrRtrId'), ['str'])),
                    ('ospfnbroptions', (YLeaf(YType.int32, 'ospfNbrOptions'), ['int'])),
                    ('ospfnbrpriority', (YLeaf(YType.int32, 'ospfNbrPriority'), ['int'])),
                    ('ospfnbrstate', (YLeaf(YType.enumeration, 'ospfNbrState'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfNbrTable.OspfNbrEntry.OspfNbrState')])),
                    ('ospfnbrevents', (YLeaf(YType.uint32, 'ospfNbrEvents'), ['int'])),
                    ('ospfnbrlsretransqlen', (YLeaf(YType.uint32, 'ospfNbrLsRetransQLen'), ['int'])),
                    ('ospfnbmanbrstatus', (YLeaf(YType.enumeration, 'ospfNbmaNbrStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('ospfnbmanbrpermanence', (YLeaf(YType.enumeration, 'ospfNbmaNbrPermanence'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfNbrTable.OspfNbrEntry.OspfNbmaNbrPermanence')])),
                    ('ospfnbrhellosuppressed', (YLeaf(YType.boolean, 'ospfNbrHelloSuppressed'), ['bool'])),
                    ('ospfnbrrestarthelperstatus', (YLeaf(YType.enumeration, 'ospfNbrRestartHelperStatus'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfNbrTable.OspfNbrEntry.OspfNbrRestartHelperStatus')])),
                    ('ospfnbrrestarthelperage', (YLeaf(YType.uint32, 'ospfNbrRestartHelperAge'), ['int'])),
                    ('ospfnbrrestarthelperexitreason', (YLeaf(YType.enumeration, 'ospfNbrRestartHelperExitReason'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfNbrTable.OspfNbrEntry.OspfNbrRestartHelperExitReason')])),
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
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.OspfNbrTable.OspfNbrEntry, [u'ospfnbripaddr', u'ospfnbraddresslessindex', u'ospfnbrrtrid', u'ospfnbroptions', u'ospfnbrpriority', u'ospfnbrstate', u'ospfnbrevents', u'ospfnbrlsretransqlen', u'ospfnbmanbrstatus', u'ospfnbmanbrpermanence', u'ospfnbrhellosuppressed', u'ospfnbrrestarthelperstatus', u'ospfnbrrestarthelperage', u'ospfnbrrestarthelperexitreason'], name, value)

            class OspfNbmaNbrPermanence(Enum):
                """
                OspfNbmaNbrPermanence (Enum Class)

                This variable displays the status of the entry;

                'dynamic' and 'permanent' refer to how the neighbor

                became known.

                .. data:: dynamic = 1

                .. data:: permanent = 2

                """

                dynamic = Enum.YLeaf(1, "dynamic")

                permanent = Enum.YLeaf(2, "permanent")


            class OspfNbrRestartHelperExitReason(Enum):
                """
                OspfNbrRestartHelperExitReason (Enum Class)

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


            class OspfNbrRestartHelperStatus(Enum):
                """
                OspfNbrRestartHelperStatus (Enum Class)

                Indicates whether the router is acting

                as a graceful restart helper for the neighbor.

                .. data:: notHelping = 1

                .. data:: helping = 2

                """

                notHelping = Enum.YLeaf(1, "notHelping")

                helping = Enum.YLeaf(2, "helping")


            class OspfNbrState(Enum):
                """
                OspfNbrState (Enum Class)

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



    class OspfVirtNbrTable(Entity):
        """
        This table describes all virtual neighbors.
        Since virtual links are configured
        in the Virtual Interface Table, this table is read\-only.
        
        .. attribute:: ospfvirtnbrentry
        
        	Virtual neighbor information
        	**type**\: list of  		 :py:class:`OspfVirtNbrEntry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfVirtNbrTable.OspfVirtNbrEntry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.OspfVirtNbrTable, self).__init__()

            self.yang_name = "ospfVirtNbrTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ospfVirtNbrEntry", ("ospfvirtnbrentry", OSPFMIB.OspfVirtNbrTable.OspfVirtNbrEntry))])
            self._leafs = OrderedDict()

            self.ospfvirtnbrentry = YList(self)
            self._segment_path = lambda: "ospfVirtNbrTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.OspfVirtNbrTable, [], name, value)


        class OspfVirtNbrEntry(Entity):
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
            	**type**\:  :py:class:`OspfVirtNbrState <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfVirtNbrTable.OspfVirtNbrEntry.OspfVirtNbrState>`
            
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
            	**type**\:  :py:class:`OspfVirtNbrRestartHelperStatus <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfVirtNbrTable.OspfVirtNbrEntry.OspfVirtNbrRestartHelperStatus>`
            
            .. attribute:: ospfvirtnbrrestarthelperage
            
            	Remaining time in current OSPF graceful restart interval, if the router is acting as a restart helper for the neighbor
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: ospfvirtnbrrestarthelperexitreason
            
            	Describes the outcome of the last attempt at acting as a graceful restart helper for the neighbor
            	**type**\:  :py:class:`OspfVirtNbrRestartHelperExitReason <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfVirtNbrTable.OspfVirtNbrEntry.OspfVirtNbrRestartHelperExitReason>`
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OSPFMIB.OspfVirtNbrTable.OspfVirtNbrEntry, self).__init__()

                self.yang_name = "ospfVirtNbrEntry"
                self.yang_parent_name = "ospfVirtNbrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfvirtnbrarea','ospfvirtnbrrtrid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfvirtnbrarea', (YLeaf(YType.str, 'ospfVirtNbrArea'), ['str'])),
                    ('ospfvirtnbrrtrid', (YLeaf(YType.str, 'ospfVirtNbrRtrId'), ['str'])),
                    ('ospfvirtnbripaddr', (YLeaf(YType.str, 'ospfVirtNbrIpAddr'), ['str'])),
                    ('ospfvirtnbroptions', (YLeaf(YType.int32, 'ospfVirtNbrOptions'), ['int'])),
                    ('ospfvirtnbrstate', (YLeaf(YType.enumeration, 'ospfVirtNbrState'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfVirtNbrTable.OspfVirtNbrEntry.OspfVirtNbrState')])),
                    ('ospfvirtnbrevents', (YLeaf(YType.uint32, 'ospfVirtNbrEvents'), ['int'])),
                    ('ospfvirtnbrlsretransqlen', (YLeaf(YType.uint32, 'ospfVirtNbrLsRetransQLen'), ['int'])),
                    ('ospfvirtnbrhellosuppressed', (YLeaf(YType.boolean, 'ospfVirtNbrHelloSuppressed'), ['bool'])),
                    ('ospfvirtnbrrestarthelperstatus', (YLeaf(YType.enumeration, 'ospfVirtNbrRestartHelperStatus'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfVirtNbrTable.OspfVirtNbrEntry.OspfVirtNbrRestartHelperStatus')])),
                    ('ospfvirtnbrrestarthelperage', (YLeaf(YType.uint32, 'ospfVirtNbrRestartHelperAge'), ['int'])),
                    ('ospfvirtnbrrestarthelperexitreason', (YLeaf(YType.enumeration, 'ospfVirtNbrRestartHelperExitReason'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfVirtNbrTable.OspfVirtNbrEntry.OspfVirtNbrRestartHelperExitReason')])),
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
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.OspfVirtNbrTable.OspfVirtNbrEntry, [u'ospfvirtnbrarea', u'ospfvirtnbrrtrid', u'ospfvirtnbripaddr', u'ospfvirtnbroptions', u'ospfvirtnbrstate', u'ospfvirtnbrevents', u'ospfvirtnbrlsretransqlen', u'ospfvirtnbrhellosuppressed', u'ospfvirtnbrrestarthelperstatus', u'ospfvirtnbrrestarthelperage', u'ospfvirtnbrrestarthelperexitreason'], name, value)

            class OspfVirtNbrRestartHelperExitReason(Enum):
                """
                OspfVirtNbrRestartHelperExitReason (Enum Class)

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


            class OspfVirtNbrRestartHelperStatus(Enum):
                """
                OspfVirtNbrRestartHelperStatus (Enum Class)

                Indicates whether the router is acting

                as a graceful restart helper for the neighbor.

                .. data:: notHelping = 1

                .. data:: helping = 2

                """

                notHelping = Enum.YLeaf(1, "notHelping")

                helping = Enum.YLeaf(2, "helping")


            class OspfVirtNbrState(Enum):
                """
                OspfVirtNbrState (Enum Class)

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



    class OspfExtLsdbTable(Entity):
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
        	**type**\: list of  		 :py:class:`OspfExtLsdbEntry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfExtLsdbTable.OspfExtLsdbEntry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.OspfExtLsdbTable, self).__init__()

            self.yang_name = "ospfExtLsdbTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ospfExtLsdbEntry", ("ospfextlsdbentry", OSPFMIB.OspfExtLsdbTable.OspfExtLsdbEntry))])
            self._leafs = OrderedDict()

            self.ospfextlsdbentry = YList(self)
            self._segment_path = lambda: "ospfExtLsdbTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.OspfExtLsdbTable, [], name, value)


        class OspfExtLsdbEntry(Entity):
            """
            A single link state advertisement.
            
            .. attribute:: ospfextlsdbtype  (key)
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\:  :py:class:`OspfExtLsdbType <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfExtLsdbTable.OspfExtLsdbEntry.OspfExtLsdbType>`
            
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
                super(OSPFMIB.OspfExtLsdbTable.OspfExtLsdbEntry, self).__init__()

                self.yang_name = "ospfExtLsdbEntry"
                self.yang_parent_name = "ospfExtLsdbTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfextlsdbtype','ospfextlsdblsid','ospfextlsdbrouterid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfextlsdbtype', (YLeaf(YType.enumeration, 'ospfExtLsdbType'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfExtLsdbTable.OspfExtLsdbEntry.OspfExtLsdbType')])),
                    ('ospfextlsdblsid', (YLeaf(YType.str, 'ospfExtLsdbLsid'), ['str'])),
                    ('ospfextlsdbrouterid', (YLeaf(YType.str, 'ospfExtLsdbRouterId'), ['str'])),
                    ('ospfextlsdbsequence', (YLeaf(YType.int32, 'ospfExtLsdbSequence'), ['int'])),
                    ('ospfextlsdbage', (YLeaf(YType.int32, 'ospfExtLsdbAge'), ['int'])),
                    ('ospfextlsdbchecksum', (YLeaf(YType.int32, 'ospfExtLsdbChecksum'), ['int'])),
                    ('ospfextlsdbadvertisement', (YLeaf(YType.str, 'ospfExtLsdbAdvertisement'), ['str'])),
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
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.OspfExtLsdbTable.OspfExtLsdbEntry, [u'ospfextlsdbtype', u'ospfextlsdblsid', u'ospfextlsdbrouterid', u'ospfextlsdbsequence', u'ospfextlsdbage', u'ospfextlsdbchecksum', u'ospfextlsdbadvertisement'], name, value)

            class OspfExtLsdbType(Enum):
                """
                OspfExtLsdbType (Enum Class)

                The type of the link state advertisement.

                Each link state type has a separate advertisement

                format.

                .. data:: asExternalLink = 5

                """

                asExternalLink = Enum.YLeaf(5, "asExternalLink")



    class OspfAreaAggregateTable(Entity):
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
        	**type**\: list of  		 :py:class:`OspfAreaAggregateEntry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfAreaAggregateTable.OspfAreaAggregateEntry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.OspfAreaAggregateTable, self).__init__()

            self.yang_name = "ospfAreaAggregateTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ospfAreaAggregateEntry", ("ospfareaaggregateentry", OSPFMIB.OspfAreaAggregateTable.OspfAreaAggregateEntry))])
            self._leafs = OrderedDict()

            self.ospfareaaggregateentry = YList(self)
            self._segment_path = lambda: "ospfAreaAggregateTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.OspfAreaAggregateTable, [], name, value)


        class OspfAreaAggregateEntry(Entity):
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
            	**type**\:  :py:class:`OspfAreaAggregateLsdbType <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfAreaAggregateTable.OspfAreaAggregateEntry.OspfAreaAggregateLsdbType>`
            
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
            	**type**\:  :py:class:`OspfAreaAggregateEffect <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfAreaAggregateTable.OspfAreaAggregateEntry.OspfAreaAggregateEffect>`
            
            .. attribute:: ospfareaaggregateextroutetag
            
            	External route tag to be included in NSSA (type\-7) LSAs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OSPFMIB.OspfAreaAggregateTable.OspfAreaAggregateEntry, self).__init__()

                self.yang_name = "ospfAreaAggregateEntry"
                self.yang_parent_name = "ospfAreaAggregateTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfareaaggregateareaid','ospfareaaggregatelsdbtype','ospfareaaggregatenet','ospfareaaggregatemask']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfareaaggregateareaid', (YLeaf(YType.str, 'ospfAreaAggregateAreaID'), ['str'])),
                    ('ospfareaaggregatelsdbtype', (YLeaf(YType.enumeration, 'ospfAreaAggregateLsdbType'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfAreaAggregateTable.OspfAreaAggregateEntry.OspfAreaAggregateLsdbType')])),
                    ('ospfareaaggregatenet', (YLeaf(YType.str, 'ospfAreaAggregateNet'), ['str'])),
                    ('ospfareaaggregatemask', (YLeaf(YType.str, 'ospfAreaAggregateMask'), ['str'])),
                    ('ospfareaaggregatestatus', (YLeaf(YType.enumeration, 'ospfAreaAggregateStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('ospfareaaggregateeffect', (YLeaf(YType.enumeration, 'ospfAreaAggregateEffect'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfAreaAggregateTable.OspfAreaAggregateEntry.OspfAreaAggregateEffect')])),
                    ('ospfareaaggregateextroutetag', (YLeaf(YType.uint32, 'ospfAreaAggregateExtRouteTag'), ['int'])),
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
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.OspfAreaAggregateTable.OspfAreaAggregateEntry, [u'ospfareaaggregateareaid', u'ospfareaaggregatelsdbtype', u'ospfareaaggregatenet', u'ospfareaaggregatemask', u'ospfareaaggregatestatus', u'ospfareaaggregateeffect', u'ospfareaaggregateextroutetag'], name, value)

            class OspfAreaAggregateEffect(Enum):
                """
                OspfAreaAggregateEffect (Enum Class)

                Subnets subsumed by ranges either trigger the

                advertisement of the indicated aggregate

                (advertiseMatching) or result in the subnet's not

                being advertised at all outside the area.

                .. data:: advertiseMatching = 1

                .. data:: doNotAdvertiseMatching = 2

                """

                advertiseMatching = Enum.YLeaf(1, "advertiseMatching")

                doNotAdvertiseMatching = Enum.YLeaf(2, "doNotAdvertiseMatching")


            class OspfAreaAggregateLsdbType(Enum):
                """
                OspfAreaAggregateLsdbType (Enum Class)

                The type of the address aggregate.  This field

                specifies the Lsdb type that this address

                aggregate applies to.

                .. data:: summaryLink = 3

                .. data:: nssaExternalLink = 7

                """

                summaryLink = Enum.YLeaf(3, "summaryLink")

                nssaExternalLink = Enum.YLeaf(7, "nssaExternalLink")



    class OspfLocalLsdbTable(Entity):
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
        	**type**\: list of  		 :py:class:`OspfLocalLsdbEntry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfLocalLsdbTable.OspfLocalLsdbEntry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.OspfLocalLsdbTable, self).__init__()

            self.yang_name = "ospfLocalLsdbTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ospfLocalLsdbEntry", ("ospflocallsdbentry", OSPFMIB.OspfLocalLsdbTable.OspfLocalLsdbEntry))])
            self._leafs = OrderedDict()

            self.ospflocallsdbentry = YList(self)
            self._segment_path = lambda: "ospfLocalLsdbTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.OspfLocalLsdbTable, [], name, value)


        class OspfLocalLsdbEntry(Entity):
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
            	**type**\:  :py:class:`OspfLocalLsdbType <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfLocalLsdbTable.OspfLocalLsdbEntry.OspfLocalLsdbType>`
            
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
                super(OSPFMIB.OspfLocalLsdbTable.OspfLocalLsdbEntry, self).__init__()

                self.yang_name = "ospfLocalLsdbEntry"
                self.yang_parent_name = "ospfLocalLsdbTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospflocallsdbipaddress','ospflocallsdbaddresslessif','ospflocallsdbtype','ospflocallsdblsid','ospflocallsdbrouterid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospflocallsdbipaddress', (YLeaf(YType.str, 'ospfLocalLsdbIpAddress'), ['str'])),
                    ('ospflocallsdbaddresslessif', (YLeaf(YType.int32, 'ospfLocalLsdbAddressLessIf'), ['int'])),
                    ('ospflocallsdbtype', (YLeaf(YType.enumeration, 'ospfLocalLsdbType'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfLocalLsdbTable.OspfLocalLsdbEntry.OspfLocalLsdbType')])),
                    ('ospflocallsdblsid', (YLeaf(YType.str, 'ospfLocalLsdbLsid'), ['str'])),
                    ('ospflocallsdbrouterid', (YLeaf(YType.str, 'ospfLocalLsdbRouterId'), ['str'])),
                    ('ospflocallsdbsequence', (YLeaf(YType.int32, 'ospfLocalLsdbSequence'), ['int'])),
                    ('ospflocallsdbage', (YLeaf(YType.int32, 'ospfLocalLsdbAge'), ['int'])),
                    ('ospflocallsdbchecksum', (YLeaf(YType.int32, 'ospfLocalLsdbChecksum'), ['int'])),
                    ('ospflocallsdbadvertisement', (YLeaf(YType.str, 'ospfLocalLsdbAdvertisement'), ['str'])),
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
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.OspfLocalLsdbTable.OspfLocalLsdbEntry, [u'ospflocallsdbipaddress', u'ospflocallsdbaddresslessif', u'ospflocallsdbtype', u'ospflocallsdblsid', u'ospflocallsdbrouterid', u'ospflocallsdbsequence', u'ospflocallsdbage', u'ospflocallsdbchecksum', u'ospflocallsdbadvertisement'], name, value)

            class OspfLocalLsdbType(Enum):
                """
                OspfLocalLsdbType (Enum Class)

                The type of the link state advertisement.

                Each link state type has a separate

                advertisement format.

                .. data:: localOpaqueLink = 9

                """

                localOpaqueLink = Enum.YLeaf(9, "localOpaqueLink")



    class OspfVirtLocalLsdbTable(Entity):
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
        	**type**\: list of  		 :py:class:`OspfVirtLocalLsdbEntry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfVirtLocalLsdbTable.OspfVirtLocalLsdbEntry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.OspfVirtLocalLsdbTable, self).__init__()

            self.yang_name = "ospfVirtLocalLsdbTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ospfVirtLocalLsdbEntry", ("ospfvirtlocallsdbentry", OSPFMIB.OspfVirtLocalLsdbTable.OspfVirtLocalLsdbEntry))])
            self._leafs = OrderedDict()

            self.ospfvirtlocallsdbentry = YList(self)
            self._segment_path = lambda: "ospfVirtLocalLsdbTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.OspfVirtLocalLsdbTable, [], name, value)


        class OspfVirtLocalLsdbEntry(Entity):
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
            	**type**\:  :py:class:`OspfVirtLocalLsdbType <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfVirtLocalLsdbTable.OspfVirtLocalLsdbEntry.OspfVirtLocalLsdbType>`
            
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
                super(OSPFMIB.OspfVirtLocalLsdbTable.OspfVirtLocalLsdbEntry, self).__init__()

                self.yang_name = "ospfVirtLocalLsdbEntry"
                self.yang_parent_name = "ospfVirtLocalLsdbTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfvirtlocallsdbtransitarea','ospfvirtlocallsdbneighbor','ospfvirtlocallsdbtype','ospfvirtlocallsdblsid','ospfvirtlocallsdbrouterid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfvirtlocallsdbtransitarea', (YLeaf(YType.str, 'ospfVirtLocalLsdbTransitArea'), ['str'])),
                    ('ospfvirtlocallsdbneighbor', (YLeaf(YType.str, 'ospfVirtLocalLsdbNeighbor'), ['str'])),
                    ('ospfvirtlocallsdbtype', (YLeaf(YType.enumeration, 'ospfVirtLocalLsdbType'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfVirtLocalLsdbTable.OspfVirtLocalLsdbEntry.OspfVirtLocalLsdbType')])),
                    ('ospfvirtlocallsdblsid', (YLeaf(YType.str, 'ospfVirtLocalLsdbLsid'), ['str'])),
                    ('ospfvirtlocallsdbrouterid', (YLeaf(YType.str, 'ospfVirtLocalLsdbRouterId'), ['str'])),
                    ('ospfvirtlocallsdbsequence', (YLeaf(YType.int32, 'ospfVirtLocalLsdbSequence'), ['int'])),
                    ('ospfvirtlocallsdbage', (YLeaf(YType.int32, 'ospfVirtLocalLsdbAge'), ['int'])),
                    ('ospfvirtlocallsdbchecksum', (YLeaf(YType.int32, 'ospfVirtLocalLsdbChecksum'), ['int'])),
                    ('ospfvirtlocallsdbadvertisement', (YLeaf(YType.str, 'ospfVirtLocalLsdbAdvertisement'), ['str'])),
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
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.OspfVirtLocalLsdbTable.OspfVirtLocalLsdbEntry, [u'ospfvirtlocallsdbtransitarea', u'ospfvirtlocallsdbneighbor', u'ospfvirtlocallsdbtype', u'ospfvirtlocallsdblsid', u'ospfvirtlocallsdbrouterid', u'ospfvirtlocallsdbsequence', u'ospfvirtlocallsdbage', u'ospfvirtlocallsdbchecksum', u'ospfvirtlocallsdbadvertisement'], name, value)

            class OspfVirtLocalLsdbType(Enum):
                """
                OspfVirtLocalLsdbType (Enum Class)

                The type of the link state advertisement.

                Each link state type has a separate

                advertisement format.

                .. data:: localOpaqueLink = 9

                """

                localOpaqueLink = Enum.YLeaf(9, "localOpaqueLink")



    class OspfAsLsdbTable(Entity):
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
        	**type**\: list of  		 :py:class:`OspfAsLsdbEntry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfAsLsdbTable.OspfAsLsdbEntry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.OspfAsLsdbTable, self).__init__()

            self.yang_name = "ospfAsLsdbTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ospfAsLsdbEntry", ("ospfaslsdbentry", OSPFMIB.OspfAsLsdbTable.OspfAsLsdbEntry))])
            self._leafs = OrderedDict()

            self.ospfaslsdbentry = YList(self)
            self._segment_path = lambda: "ospfAsLsdbTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.OspfAsLsdbTable, [], name, value)


        class OspfAsLsdbEntry(Entity):
            """
            A single link state advertisement.
            
            .. attribute:: ospfaslsdbtype  (key)
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\:  :py:class:`OspfAsLsdbType <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfAsLsdbTable.OspfAsLsdbEntry.OspfAsLsdbType>`
            
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
                super(OSPFMIB.OspfAsLsdbTable.OspfAsLsdbEntry, self).__init__()

                self.yang_name = "ospfAsLsdbEntry"
                self.yang_parent_name = "ospfAsLsdbTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfaslsdbtype','ospfaslsdblsid','ospfaslsdbrouterid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfaslsdbtype', (YLeaf(YType.enumeration, 'ospfAsLsdbType'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfAsLsdbTable.OspfAsLsdbEntry.OspfAsLsdbType')])),
                    ('ospfaslsdblsid', (YLeaf(YType.str, 'ospfAsLsdbLsid'), ['str'])),
                    ('ospfaslsdbrouterid', (YLeaf(YType.str, 'ospfAsLsdbRouterId'), ['str'])),
                    ('ospfaslsdbsequence', (YLeaf(YType.int32, 'ospfAsLsdbSequence'), ['int'])),
                    ('ospfaslsdbage', (YLeaf(YType.int32, 'ospfAsLsdbAge'), ['int'])),
                    ('ospfaslsdbchecksum', (YLeaf(YType.int32, 'ospfAsLsdbChecksum'), ['int'])),
                    ('ospfaslsdbadvertisement', (YLeaf(YType.str, 'ospfAsLsdbAdvertisement'), ['str'])),
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
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.OspfAsLsdbTable.OspfAsLsdbEntry, [u'ospfaslsdbtype', u'ospfaslsdblsid', u'ospfaslsdbrouterid', u'ospfaslsdbsequence', u'ospfaslsdbage', u'ospfaslsdbchecksum', u'ospfaslsdbadvertisement'], name, value)

            class OspfAsLsdbType(Enum):
                """
                OspfAsLsdbType (Enum Class)

                The type of the link state advertisement.

                Each link state type has a separate

                advertisement format.

                .. data:: asExternalLink = 5

                .. data:: asOpaqueLink = 11

                """

                asExternalLink = Enum.YLeaf(5, "asExternalLink")

                asOpaqueLink = Enum.YLeaf(11, "asOpaqueLink")



    class OspfAreaLsaCountTable(Entity):
        """
        This table maintains per\-area, per\-LSA\-type counters
        
        .. attribute:: ospfarealsacountentry
        
        	An entry with a number of link advertisements  of a given type for a given area
        	**type**\: list of  		 :py:class:`OspfAreaLsaCountEntry <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfAreaLsaCountTable.OspfAreaLsaCountEntry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFMIB.OspfAreaLsaCountTable, self).__init__()

            self.yang_name = "ospfAreaLsaCountTable"
            self.yang_parent_name = "OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ospfAreaLsaCountEntry", ("ospfarealsacountentry", OSPFMIB.OspfAreaLsaCountTable.OspfAreaLsaCountEntry))])
            self._leafs = OrderedDict()

            self.ospfarealsacountentry = YList(self)
            self._segment_path = lambda: "ospfAreaLsaCountTable"
            self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFMIB.OspfAreaLsaCountTable, [], name, value)


        class OspfAreaLsaCountEntry(Entity):
            """
            An entry with a number of link advertisements
            
            of a given type for a given area.
            
            .. attribute:: ospfarealsacountareaid  (key)
            
            	This entry Area ID
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfarealsacountlsatype  (key)
            
            	This entry LSA type
            	**type**\:  :py:class:`OspfAreaLsaCountLsaType <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfAreaLsaCountTable.OspfAreaLsaCountEntry.OspfAreaLsaCountLsaType>`
            
            .. attribute:: ospfarealsacountnumber
            
            	Number of LSAs of a given type for a given area
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                super(OSPFMIB.OspfAreaLsaCountTable.OspfAreaLsaCountEntry, self).__init__()

                self.yang_name = "ospfAreaLsaCountEntry"
                self.yang_parent_name = "ospfAreaLsaCountTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospfarealsacountareaid','ospfarealsacountlsatype']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospfarealsacountareaid', (YLeaf(YType.str, 'ospfAreaLsaCountAreaId'), ['str'])),
                    ('ospfarealsacountlsatype', (YLeaf(YType.enumeration, 'ospfAreaLsaCountLsaType'), [('ydk.models.cisco_ios_xe.OSPF_MIB', 'OSPFMIB', 'OspfAreaLsaCountTable.OspfAreaLsaCountEntry.OspfAreaLsaCountLsaType')])),
                    ('ospfarealsacountnumber', (YLeaf(YType.uint32, 'ospfAreaLsaCountNumber'), ['int'])),
                ])
                self.ospfarealsacountareaid = None
                self.ospfarealsacountlsatype = None
                self.ospfarealsacountnumber = None
                self._segment_path = lambda: "ospfAreaLsaCountEntry" + "[ospfAreaLsaCountAreaId='" + str(self.ospfarealsacountareaid) + "']" + "[ospfAreaLsaCountLsaType='" + str(self.ospfarealsacountlsatype) + "']"
                self._absolute_path = lambda: "OSPF-MIB:OSPF-MIB/ospfAreaLsaCountTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OSPFMIB.OspfAreaLsaCountTable.OspfAreaLsaCountEntry, [u'ospfarealsacountareaid', u'ospfarealsacountlsatype', u'ospfarealsacountnumber'], name, value)

            class OspfAreaLsaCountLsaType(Enum):
                """
                OspfAreaLsaCountLsaType (Enum Class)

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


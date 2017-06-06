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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class OspfauthenticationtypeEnum(Enum):
    """
    OspfauthenticationtypeEnum

    The authentication type.

    .. data:: none = 0

    .. data:: simplePassword = 1

    .. data:: md5 = 2

    """

    none = 0

    simplePassword = 1

    md5 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
        return meta._meta_table['OspfauthenticationtypeEnum']


class StatusEnum(Enum):
    """
    StatusEnum

    An indication of the operability of an OSPF

    function or feature.  For example, the status

    of an interface\: 'enabled' indicates that

    it is willing to communicate with other OSPF routers,

    and 'disabled' indicates that it is not.

    .. data:: enabled = 1

    .. data:: disabled = 2

    """

    enabled = 1

    disabled = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
        return meta._meta_table['StatusEnum']



class OspfMib(object):
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
        self.ospfareaaggregatetable = OspfMib.Ospfareaaggregatetable()
        self.ospfareaaggregatetable.parent = self
        self.ospfarealsacounttable = OspfMib.Ospfarealsacounttable()
        self.ospfarealsacounttable.parent = self
        self.ospfarearangetable = OspfMib.Ospfarearangetable()
        self.ospfarearangetable.parent = self
        self.ospfareatable = OspfMib.Ospfareatable()
        self.ospfareatable.parent = self
        self.ospfaslsdbtable = OspfMib.Ospfaslsdbtable()
        self.ospfaslsdbtable.parent = self
        self.ospfextlsdbtable = OspfMib.Ospfextlsdbtable()
        self.ospfextlsdbtable.parent = self
        self.ospfgeneralgroup = OspfMib.Ospfgeneralgroup()
        self.ospfgeneralgroup.parent = self
        self.ospfhosttable = OspfMib.Ospfhosttable()
        self.ospfhosttable.parent = self
        self.ospfifmetrictable = OspfMib.Ospfifmetrictable()
        self.ospfifmetrictable.parent = self
        self.ospfiftable = OspfMib.Ospfiftable()
        self.ospfiftable.parent = self
        self.ospflocallsdbtable = OspfMib.Ospflocallsdbtable()
        self.ospflocallsdbtable.parent = self
        self.ospflsdbtable = OspfMib.Ospflsdbtable()
        self.ospflsdbtable.parent = self
        self.ospfnbrtable = OspfMib.Ospfnbrtable()
        self.ospfnbrtable.parent = self
        self.ospfstubareatable = OspfMib.Ospfstubareatable()
        self.ospfstubareatable.parent = self
        self.ospfvirtiftable = OspfMib.Ospfvirtiftable()
        self.ospfvirtiftable.parent = self
        self.ospfvirtlocallsdbtable = OspfMib.Ospfvirtlocallsdbtable()
        self.ospfvirtlocallsdbtable.parent = self
        self.ospfvirtnbrtable = OspfMib.Ospfvirtnbrtable()
        self.ospfvirtnbrtable.parent = self


    class Ospfgeneralgroup(object):
        """
        
        
        .. attribute:: ospfadminstat
        
        	The administrative status of OSPF in the router.  The value 'enabled' denotes that the OSPF Process is active on at least one interface; 'disabled' disables it on all interfaces.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\:   :py:class:`StatusEnum <ydk.models.cisco_ios_xe.OSPF_MIB.StatusEnum>`
        
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
        	**type**\:   :py:class:`OspfrestartexitreasonEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfgeneralgroup.OspfrestartexitreasonEnum>`
        
        .. attribute:: ospfrestartinterval
        
        	Configured OSPF graceful restart timeout interval.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\:  int
        
        	**range:** 1..1800
        
        	**units**\: seconds
        
        .. attribute:: ospfrestartstatus
        
        	Current status of OSPF graceful restart
        	**type**\:   :py:class:`OspfrestartstatusEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfgeneralgroup.OspfrestartstatusEnum>`
        
        .. attribute:: ospfrestartstrictlsachecking
        
        	Indicates if strict LSA checking is enabled for graceful restart.  This object is persistent and when written the entity SHOULD save the change to non\-volatile  storage
        	**type**\:  bool
        
        .. attribute:: ospfrestartsupport
        
        	The router's support for OSPF graceful restart. Options include\: no restart support, only planned restarts, or both planned and unplanned restarts.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\:   :py:class:`OspfrestartsupportEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfgeneralgroup.OspfrestartsupportEnum>`
        
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
        	**type**\:   :py:class:`OspfstubrouteradvertisementEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfgeneralgroup.OspfstubrouteradvertisementEnum>`
        
        .. attribute:: ospfstubroutersupport
        
        	The router's support for stub router functionality
        	**type**\:  bool
        
        .. attribute:: ospftossupport
        
        	The router's support for type\-of\-service routing.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\:  bool
        
        .. attribute:: ospfversionnumber
        
        	The current version number of the OSPF protocol is 2
        	**type**\:   :py:class:`OspfversionnumberEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfgeneralgroup.OspfversionnumberEnum>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            self.parent = None
            self.ospfadminstat = None
            self.ospfareabdrrtrstatus = None
            self.ospfasbdrrtrstatus = None
            self.ospfaslsacksumsum = None
            self.ospfaslsacount = None
            self.ospfdemandextensions = None
            self.ospfdiscontinuitytime = None
            self.ospfexitoverflowinterval = None
            self.ospfexternlsacksumsum = None
            self.ospfexternlsacount = None
            self.ospfextlsdblimit = None
            self.ospfmulticastextensions = None
            self.ospfopaquelsasupport = None
            self.ospforiginatenewlsas = None
            self.ospfreferencebandwidth = None
            self.ospfrestartage = None
            self.ospfrestartexitreason = None
            self.ospfrestartinterval = None
            self.ospfrestartstatus = None
            self.ospfrestartstrictlsachecking = None
            self.ospfrestartsupport = None
            self.ospfrfc1583compatibility = None
            self.ospfrouterid = None
            self.ospfrxnewlsas = None
            self.ospfstubrouteradvertisement = None
            self.ospfstubroutersupport = None
            self.ospftossupport = None
            self.ospfversionnumber = None

        class OspfrestartexitreasonEnum(Enum):
            """
            OspfrestartexitreasonEnum

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

            none = 1

            inProgress = 2

            completed = 3

            timedOut = 4

            topologyChanged = 5


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                return meta._meta_table['OspfMib.Ospfgeneralgroup.OspfrestartexitreasonEnum']


        class OspfrestartstatusEnum(Enum):
            """
            OspfrestartstatusEnum

            Current status of OSPF graceful restart.

            .. data:: notRestarting = 1

            .. data:: plannedRestart = 2

            .. data:: unplannedRestart = 3

            """

            notRestarting = 1

            plannedRestart = 2

            unplannedRestart = 3


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                return meta._meta_table['OspfMib.Ospfgeneralgroup.OspfrestartstatusEnum']


        class OspfrestartsupportEnum(Enum):
            """
            OspfrestartsupportEnum

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

            none = 1

            plannedOnly = 2

            plannedAndUnplanned = 3


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                return meta._meta_table['OspfMib.Ospfgeneralgroup.OspfrestartsupportEnum']


        class OspfstubrouteradvertisementEnum(Enum):
            """
            OspfstubrouteradvertisementEnum

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

            doNotAdvertise = 1

            advertise = 2


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                return meta._meta_table['OspfMib.Ospfgeneralgroup.OspfstubrouteradvertisementEnum']


        class OspfversionnumberEnum(Enum):
            """
            OspfversionnumberEnum

            The current version number of the OSPF protocol is 2.

            .. data:: version2 = 2

            """

            version2 = 2


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                return meta._meta_table['OspfMib.Ospfgeneralgroup.OspfversionnumberEnum']


        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfGeneralGroup'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ospfadminstat is not None:
                return True

            if self.ospfareabdrrtrstatus is not None:
                return True

            if self.ospfasbdrrtrstatus is not None:
                return True

            if self.ospfaslsacksumsum is not None:
                return True

            if self.ospfaslsacount is not None:
                return True

            if self.ospfdemandextensions is not None:
                return True

            if self.ospfdiscontinuitytime is not None:
                return True

            if self.ospfexitoverflowinterval is not None:
                return True

            if self.ospfexternlsacksumsum is not None:
                return True

            if self.ospfexternlsacount is not None:
                return True

            if self.ospfextlsdblimit is not None:
                return True

            if self.ospfmulticastextensions is not None:
                return True

            if self.ospfopaquelsasupport is not None:
                return True

            if self.ospforiginatenewlsas is not None:
                return True

            if self.ospfreferencebandwidth is not None:
                return True

            if self.ospfrestartage is not None:
                return True

            if self.ospfrestartexitreason is not None:
                return True

            if self.ospfrestartinterval is not None:
                return True

            if self.ospfrestartstatus is not None:
                return True

            if self.ospfrestartstrictlsachecking is not None:
                return True

            if self.ospfrestartsupport is not None:
                return True

            if self.ospfrfc1583compatibility is not None:
                return True

            if self.ospfrouterid is not None:
                return True

            if self.ospfrxnewlsas is not None:
                return True

            if self.ospfstubrouteradvertisement is not None:
                return True

            if self.ospfstubroutersupport is not None:
                return True

            if self.ospftossupport is not None:
                return True

            if self.ospfversionnumber is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
            return meta._meta_table['OspfMib.Ospfgeneralgroup']['meta_info']


    class Ospfareatable(object):
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
            self.parent = None
            self.ospfareaentry = YList()
            self.ospfareaentry.parent = self
            self.ospfareaentry.name = 'ospfareaentry'


        class Ospfareaentry(object):
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
            	**type**\:   :py:class:`CospfareanssatranslatorroleEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfareatable.Ospfareaentry.CospfareanssatranslatorroleEnum>`
            
            .. attribute:: cospfareanssatranslatorstate
            
            	Indicates if and how an NSSA Border router is performing NSSA translation of type\-7 LSAs into type\-5 LSAs. When this object set to enabled, the NSSA Border router's cospfAreaNssaExtTranslatorRole has been set to always. When this object is set to elected, a candidate NSSA Border router is Translating type\-7 LSAs into type\-5. When this object is set to disabled, a candidate NSSA Border router is NOT translating type\-7 LSAs into type\-5
            	**type**\:   :py:class:`CospfareanssatranslatorstateEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfareatable.Ospfareaentry.CospfareanssatranslatorstateEnum>`
            
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
            	**type**\:   :py:class:`OspfareanssatranslatorroleEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfareatable.Ospfareaentry.OspfareanssatranslatorroleEnum>`
            
            .. attribute:: ospfareanssatranslatorstabilityinterval
            
            	The number of seconds after an elected translator determines its services are no longer required, that it should continue to perform its translation duties
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: ospfareanssatranslatorstate
            
            	Indicates if and how an NSSA border router is performing NSSA translation of type\-7 LSAs into type\-5  LSAs.  When this object is set to enabled, the NSSA Border router's OspfAreaNssaExtTranslatorRole has been set to always.  When this object is set to elected, a candidate NSSA Border router is Translating type\-7 LSAs into type\-5. When this object is set to disabled, a candidate NSSA border router is NOT translating type\-7 LSAs into type\-5
            	**type**\:   :py:class:`OspfareanssatranslatorstateEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfareatable.Ospfareaentry.OspfareanssatranslatorstateEnum>`
            
            .. attribute:: ospfareastatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: ospfareasummary
            
            	The variable ospfAreaSummary controls the import of summary LSAs into stub and NSSA areas. It has no effect on other areas.  If it is noAreaSummary, the router will not originate summary LSAs into the stub or NSSA area. It will rely entirely on its default route.  If it is sendAreaSummary, the router will both summarize and propagate summary LSAs
            	**type**\:   :py:class:`OspfareasummaryEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfareatable.Ospfareaentry.OspfareasummaryEnum>`
            
            .. attribute:: ospfasbdrrtrcount
            
            	The total number of Autonomous System Border Routers reachable within this area.  This is initially zero and is calculated in each SPF pass
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfauthtype
            
            	The authentication type specified for an area
            	**type**\:   :py:class:`OspfauthenticationtypeEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfauthenticationtypeEnum>`
            
            	**status**\: obsolete
            
            .. attribute:: ospfimportasextern
            
            	Indicates if an area is a stub area, NSSA, or standard area.  Type\-5 AS\-external LSAs and type\-11 Opaque LSAs are not imported into stub areas or NSSAs.  NSSAs import AS\-external data as type\-7 LSAs
            	**type**\:   :py:class:`OspfimportasexternEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfareatable.Ospfareaentry.OspfimportasexternEnum>`
            
            .. attribute:: ospfspfruns
            
            	The number of times that the intra\-area route table has been calculated using this area's link state database.  This is typically done using Dijkstra's algorithm.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ospfDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                self.parent = None
                self.ospfareaid = None
                self.cospfareanssatranslatorevents = None
                self.cospfareanssatranslatorrole = None
                self.cospfareanssatranslatorstate = None
                self.cospfopaquearealsacksumsum = None
                self.cospfopaquearealsacount = None
                self.ospfareabdrrtrcount = None
                self.ospfarealsacksumsum = None
                self.ospfarealsacount = None
                self.ospfareanssatranslatorevents = None
                self.ospfareanssatranslatorrole = None
                self.ospfareanssatranslatorstabilityinterval = None
                self.ospfareanssatranslatorstate = None
                self.ospfareastatus = None
                self.ospfareasummary = None
                self.ospfasbdrrtrcount = None
                self.ospfauthtype = None
                self.ospfimportasextern = None
                self.ospfspfruns = None

            class CospfareanssatranslatorroleEnum(Enum):
                """
                CospfareanssatranslatorroleEnum

                Indicates an NSSA Border router's ability to

                perform NSSA translation of type\-7 LSAs into

                type\-5 LSAs.

                .. data:: always = 1

                .. data:: candidate = 2

                """

                always = 1

                candidate = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospfareatable.Ospfareaentry.CospfareanssatranslatorroleEnum']


            class CospfareanssatranslatorstateEnum(Enum):
                """
                CospfareanssatranslatorstateEnum

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

                enabled = 1

                elected = 2

                disabled = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospfareatable.Ospfareaentry.CospfareanssatranslatorstateEnum']


            class OspfareanssatranslatorroleEnum(Enum):
                """
                OspfareanssatranslatorroleEnum

                Indicates an NSSA border router's ability to

                perform NSSA translation of type\-7 LSAs into

                type\-5 LSAs.

                .. data:: always = 1

                .. data:: candidate = 2

                """

                always = 1

                candidate = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospfareatable.Ospfareaentry.OspfareanssatranslatorroleEnum']


            class OspfareanssatranslatorstateEnum(Enum):
                """
                OspfareanssatranslatorstateEnum

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

                enabled = 1

                elected = 2

                disabled = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospfareatable.Ospfareaentry.OspfareanssatranslatorstateEnum']


            class OspfareasummaryEnum(Enum):
                """
                OspfareasummaryEnum

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

                noAreaSummary = 1

                sendAreaSummary = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospfareatable.Ospfareaentry.OspfareasummaryEnum']


            class OspfimportasexternEnum(Enum):
                """
                OspfimportasexternEnum

                Indicates if an area is a stub area, NSSA, or standard

                area.  Type\-5 AS\-external LSAs and type\-11 Opaque LSAs are

                not imported into stub areas or NSSAs.  NSSAs import

                AS\-external data as type\-7 LSAs

                .. data:: importExternal = 1

                .. data:: importNoExternal = 2

                .. data:: importNssa = 3

                """

                importExternal = 1

                importNoExternal = 2

                importNssa = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospfareatable.Ospfareaentry.OspfimportasexternEnum']


            @property
            def _common_path(self):
                if self.ospfareaid is None:
                    raise YPYModelError('Key property ospfareaid is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfAreaTable/OSPF-MIB:ospfAreaEntry[OSPF-MIB:ospfAreaId = ' + str(self.ospfareaid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ospfareaid is not None:
                    return True

                if self.cospfareanssatranslatorevents is not None:
                    return True

                if self.cospfareanssatranslatorrole is not None:
                    return True

                if self.cospfareanssatranslatorstate is not None:
                    return True

                if self.cospfopaquearealsacksumsum is not None:
                    return True

                if self.cospfopaquearealsacount is not None:
                    return True

                if self.ospfareabdrrtrcount is not None:
                    return True

                if self.ospfarealsacksumsum is not None:
                    return True

                if self.ospfarealsacount is not None:
                    return True

                if self.ospfareanssatranslatorevents is not None:
                    return True

                if self.ospfareanssatranslatorrole is not None:
                    return True

                if self.ospfareanssatranslatorstabilityinterval is not None:
                    return True

                if self.ospfareanssatranslatorstate is not None:
                    return True

                if self.ospfareastatus is not None:
                    return True

                if self.ospfareasummary is not None:
                    return True

                if self.ospfasbdrrtrcount is not None:
                    return True

                if self.ospfauthtype is not None:
                    return True

                if self.ospfimportasextern is not None:
                    return True

                if self.ospfspfruns is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                return meta._meta_table['OspfMib.Ospfareatable.Ospfareaentry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfAreaTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ospfareaentry is not None:
                for child_ref in self.ospfareaentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
            return meta._meta_table['OspfMib.Ospfareatable']['meta_info']


    class Ospfstubareatable(object):
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
            self.parent = None
            self.ospfstubareaentry = YList()
            self.ospfstubareaentry.parent = self
            self.ospfstubareaentry.name = 'ospfstubareaentry'


        class Ospfstubareaentry(object):
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
            	**type**\:   :py:class:`OspfstubmetrictypeEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfstubareatable.Ospfstubareaentry.OspfstubmetrictypeEnum>`
            
            .. attribute:: ospfstubstatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                self.parent = None
                self.ospfstubareaid = None
                self.ospfstubtos = None
                self.ospfstubmetric = None
                self.ospfstubmetrictype = None
                self.ospfstubstatus = None

            class OspfstubmetrictypeEnum(Enum):
                """
                OspfstubmetrictypeEnum

                This variable displays the type of metric

                advertised as a default route.

                .. data:: ospfMetric = 1

                .. data:: comparableCost = 2

                .. data:: nonComparable = 3

                """

                ospfMetric = 1

                comparableCost = 2

                nonComparable = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospfstubareatable.Ospfstubareaentry.OspfstubmetrictypeEnum']


            @property
            def _common_path(self):
                if self.ospfstubareaid is None:
                    raise YPYModelError('Key property ospfstubareaid is None')
                if self.ospfstubtos is None:
                    raise YPYModelError('Key property ospfstubtos is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfStubAreaTable/OSPF-MIB:ospfStubAreaEntry[OSPF-MIB:ospfStubAreaId = ' + str(self.ospfstubareaid) + '][OSPF-MIB:ospfStubTOS = ' + str(self.ospfstubtos) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ospfstubareaid is not None:
                    return True

                if self.ospfstubtos is not None:
                    return True

                if self.ospfstubmetric is not None:
                    return True

                if self.ospfstubmetrictype is not None:
                    return True

                if self.ospfstubstatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                return meta._meta_table['OspfMib.Ospfstubareatable.Ospfstubareaentry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfStubAreaTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ospfstubareaentry is not None:
                for child_ref in self.ospfstubareaentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
            return meta._meta_table['OspfMib.Ospfstubareatable']['meta_info']


    class Ospflsdbtable(object):
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
            self.parent = None
            self.ospflsdbentry = YList()
            self.ospflsdbentry.parent = self
            self.ospflsdbentry.name = 'ospflsdbentry'


        class Ospflsdbentry(object):
            """
            A single link state advertisement.
            
            .. attribute:: ospflsdbareaid  <key>
            
            	The 32\-bit identifier of the area from which the LSA was received
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospflsdbtype  <key>
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format.  Note\: External link state advertisements are permitted for backward compatibility, but should be displayed in the ospfAsLsdbTable rather than here
            	**type**\:   :py:class:`OspflsdbtypeEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospflsdbtable.Ospflsdbentry.OspflsdbtypeEnum>`
            
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
                self.parent = None
                self.ospflsdbareaid = None
                self.ospflsdbtype = None
                self.ospflsdblsid = None
                self.ospflsdbrouterid = None
                self.ospflsdbadvertisement = None
                self.ospflsdbage = None
                self.ospflsdbchecksum = None
                self.ospflsdbsequence = None

            class OspflsdbtypeEnum(Enum):
                """
                OspflsdbtypeEnum

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

                routerLink = 1

                networkLink = 2

                summaryLink = 3

                asSummaryLink = 4

                asExternalLink = 5

                multicastLink = 6

                nssaExternalLink = 7

                areaOpaqueLink = 10


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospflsdbtable.Ospflsdbentry.OspflsdbtypeEnum']


            @property
            def _common_path(self):
                if self.ospflsdbareaid is None:
                    raise YPYModelError('Key property ospflsdbareaid is None')
                if self.ospflsdbtype is None:
                    raise YPYModelError('Key property ospflsdbtype is None')
                if self.ospflsdblsid is None:
                    raise YPYModelError('Key property ospflsdblsid is None')
                if self.ospflsdbrouterid is None:
                    raise YPYModelError('Key property ospflsdbrouterid is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfLsdbTable/OSPF-MIB:ospfLsdbEntry[OSPF-MIB:ospfLsdbAreaId = ' + str(self.ospflsdbareaid) + '][OSPF-MIB:ospfLsdbType = ' + str(self.ospflsdbtype) + '][OSPF-MIB:ospfLsdbLsid = ' + str(self.ospflsdblsid) + '][OSPF-MIB:ospfLsdbRouterId = ' + str(self.ospflsdbrouterid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ospflsdbareaid is not None:
                    return True

                if self.ospflsdbtype is not None:
                    return True

                if self.ospflsdblsid is not None:
                    return True

                if self.ospflsdbrouterid is not None:
                    return True

                if self.ospflsdbadvertisement is not None:
                    return True

                if self.ospflsdbage is not None:
                    return True

                if self.ospflsdbchecksum is not None:
                    return True

                if self.ospflsdbsequence is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                return meta._meta_table['OspfMib.Ospflsdbtable.Ospflsdbentry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfLsdbTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ospflsdbentry is not None:
                for child_ref in self.ospflsdbentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
            return meta._meta_table['OspfMib.Ospflsdbtable']['meta_info']


    class Ospfarearangetable(object):
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
            self.parent = None
            self.ospfarearangeentry = YList()
            self.ospfarearangeentry.parent = self
            self.ospfarearangeentry.name = 'ospfarearangeentry'


        class Ospfarearangeentry(object):
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
            	**type**\:   :py:class:`OspfarearangeeffectEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfarearangetable.Ospfarearangeentry.OspfarearangeeffectEnum>`
            
            	**status**\: obsolete
            
            .. attribute:: ospfarearangemask
            
            	The subnet mask that pertains to the net or subnet
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: obsolete
            
            .. attribute:: ospfarearangestatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                self.parent = None
                self.ospfarearangeareaid = None
                self.ospfarearangenet = None
                self.ospfarearangeeffect = None
                self.ospfarearangemask = None
                self.ospfarearangestatus = None

            class OspfarearangeeffectEnum(Enum):
                """
                OspfarearangeeffectEnum

                Subnets subsumed by ranges either trigger the

                advertisement of the indicated summary

                (advertiseMatching) or result in the subnet's not

                being advertised at all outside the area.

                .. data:: advertiseMatching = 1

                .. data:: doNotAdvertiseMatching = 2

                """

                advertiseMatching = 1

                doNotAdvertiseMatching = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospfarearangetable.Ospfarearangeentry.OspfarearangeeffectEnum']


            @property
            def _common_path(self):
                if self.ospfarearangeareaid is None:
                    raise YPYModelError('Key property ospfarearangeareaid is None')
                if self.ospfarearangenet is None:
                    raise YPYModelError('Key property ospfarearangenet is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfAreaRangeTable/OSPF-MIB:ospfAreaRangeEntry[OSPF-MIB:ospfAreaRangeAreaId = ' + str(self.ospfarearangeareaid) + '][OSPF-MIB:ospfAreaRangeNet = ' + str(self.ospfarearangenet) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ospfarearangeareaid is not None:
                    return True

                if self.ospfarearangenet is not None:
                    return True

                if self.ospfarearangeeffect is not None:
                    return True

                if self.ospfarearangemask is not None:
                    return True

                if self.ospfarearangestatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                return meta._meta_table['OspfMib.Ospfarearangetable.Ospfarearangeentry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfAreaRangeTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ospfarearangeentry is not None:
                for child_ref in self.ospfarearangeentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
            return meta._meta_table['OspfMib.Ospfarearangetable']['meta_info']


    class Ospfhosttable(object):
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
            self.parent = None
            self.ospfhostentry = YList()
            self.ospfhostentry.parent = self
            self.ospfhostentry.name = 'ospfhostentry'


        class Ospfhostentry(object):
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
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                self.parent = None
                self.ospfhostipaddress = None
                self.ospfhosttos = None
                self.ospfhostareaid = None
                self.ospfhostcfgareaid = None
                self.ospfhostmetric = None
                self.ospfhoststatus = None

            @property
            def _common_path(self):
                if self.ospfhostipaddress is None:
                    raise YPYModelError('Key property ospfhostipaddress is None')
                if self.ospfhosttos is None:
                    raise YPYModelError('Key property ospfhosttos is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfHostTable/OSPF-MIB:ospfHostEntry[OSPF-MIB:ospfHostIpAddress = ' + str(self.ospfhostipaddress) + '][OSPF-MIB:ospfHostTOS = ' + str(self.ospfhosttos) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ospfhostipaddress is not None:
                    return True

                if self.ospfhosttos is not None:
                    return True

                if self.ospfhostareaid is not None:
                    return True

                if self.ospfhostcfgareaid is not None:
                    return True

                if self.ospfhostmetric is not None:
                    return True

                if self.ospfhoststatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                return meta._meta_table['OspfMib.Ospfhosttable.Ospfhostentry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfHostTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ospfhostentry is not None:
                for child_ref in self.ospfhostentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
            return meta._meta_table['OspfMib.Ospfhosttable']['meta_info']


    class Ospfiftable(object):
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
            self.parent = None
            self.ospfifentry = YList()
            self.ospfifentry.parent = self
            self.ospfifentry.name = 'ospfifentry'


        class Ospfifentry(object):
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
            	**type**\:   :py:class:`StatusEnum <ydk.models.cisco_ios_xe.OSPF_MIB.StatusEnum>`
            
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
            	**type**\:   :py:class:`OspfauthenticationtypeEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfauthenticationtypeEnum>`
            
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
            	**type**\:   :py:class:`OspfifmulticastforwardingEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfiftable.Ospfifentry.OspfifmulticastforwardingEnum>`
            
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
            	**type**\:   :py:class:`OspfifstateEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfiftable.Ospfifentry.OspfifstateEnum>`
            
            .. attribute:: ospfifstatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: ospfiftransitdelay
            
            	The estimated number of seconds it takes to transmit a link state update packet over this interface.  Note that the minimal value SHOULD be 1 second
            	**type**\:  int
            
            	**range:** 0..3600
            
            	**units**\: seconds
            
            .. attribute:: ospfiftype
            
            	The OSPF interface type. By way of a default, this field may be intuited from the corresponding value of ifType. Broadcast LANs, such as Ethernet and IEEE 802.5, take the value 'broadcast', X.25 and similar technologies take the value 'nbma', and links that are definitively point to point take the value 'pointToPoint'
            	**type**\:   :py:class:`OspfiftypeEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfiftable.Ospfifentry.OspfiftypeEnum>`
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                self.parent = None
                self.ospfifipaddress = None
                self.ospfaddresslessif = None
                self.cospfiflsacksumsum = None
                self.cospfiflsacount = None
                self.ospfifadminstat = None
                self.ospfifareaid = None
                self.ospfifauthkey = None
                self.ospfifauthtype = None
                self.ospfifbackupdesignatedrouter = None
                self.ospfifbackupdesignatedrouterid = None
                self.ospfifdemand = None
                self.ospfifdesignatedrouter = None
                self.ospfifdesignatedrouterid = None
                self.ospfifevents = None
                self.ospfifhellointerval = None
                self.ospfiflsacksumsum = None
                self.ospfiflsacount = None
                self.ospfifmulticastforwarding = None
                self.ospfifpollinterval = None
                self.ospfifretransinterval = None
                self.ospfifrtrdeadinterval = None
                self.ospfifrtrpriority = None
                self.ospfifstate = None
                self.ospfifstatus = None
                self.ospfiftransitdelay = None
                self.ospfiftype = None

            class OspfifmulticastforwardingEnum(Enum):
                """
                OspfifmulticastforwardingEnum

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

                blocked = 1

                multicast = 2

                unicast = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospfiftable.Ospfifentry.OspfifmulticastforwardingEnum']


            class OspfifstateEnum(Enum):
                """
                OspfifstateEnum

                The OSPF Interface State.

                .. data:: down = 1

                .. data:: loopback = 2

                .. data:: waiting = 3

                .. data:: pointToPoint = 4

                .. data:: designatedRouter = 5

                .. data:: backupDesignatedRouter = 6

                .. data:: otherDesignatedRouter = 7

                """

                down = 1

                loopback = 2

                waiting = 3

                pointToPoint = 4

                designatedRouter = 5

                backupDesignatedRouter = 6

                otherDesignatedRouter = 7


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospfiftable.Ospfifentry.OspfifstateEnum']


            class OspfiftypeEnum(Enum):
                """
                OspfiftypeEnum

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

                broadcast = 1

                nbma = 2

                pointToPoint = 3

                pointToMultipoint = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospfiftable.Ospfifentry.OspfiftypeEnum']


            @property
            def _common_path(self):
                if self.ospfifipaddress is None:
                    raise YPYModelError('Key property ospfifipaddress is None')
                if self.ospfaddresslessif is None:
                    raise YPYModelError('Key property ospfaddresslessif is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfIfTable/OSPF-MIB:ospfIfEntry[OSPF-MIB:ospfIfIpAddress = ' + str(self.ospfifipaddress) + '][OSPF-MIB:ospfAddressLessIf = ' + str(self.ospfaddresslessif) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ospfifipaddress is not None:
                    return True

                if self.ospfaddresslessif is not None:
                    return True

                if self.cospfiflsacksumsum is not None:
                    return True

                if self.cospfiflsacount is not None:
                    return True

                if self.ospfifadminstat is not None:
                    return True

                if self.ospfifareaid is not None:
                    return True

                if self.ospfifauthkey is not None:
                    return True

                if self.ospfifauthtype is not None:
                    return True

                if self.ospfifbackupdesignatedrouter is not None:
                    return True

                if self.ospfifbackupdesignatedrouterid is not None:
                    return True

                if self.ospfifdemand is not None:
                    return True

                if self.ospfifdesignatedrouter is not None:
                    return True

                if self.ospfifdesignatedrouterid is not None:
                    return True

                if self.ospfifevents is not None:
                    return True

                if self.ospfifhellointerval is not None:
                    return True

                if self.ospfiflsacksumsum is not None:
                    return True

                if self.ospfiflsacount is not None:
                    return True

                if self.ospfifmulticastforwarding is not None:
                    return True

                if self.ospfifpollinterval is not None:
                    return True

                if self.ospfifretransinterval is not None:
                    return True

                if self.ospfifrtrdeadinterval is not None:
                    return True

                if self.ospfifrtrpriority is not None:
                    return True

                if self.ospfifstate is not None:
                    return True

                if self.ospfifstatus is not None:
                    return True

                if self.ospfiftransitdelay is not None:
                    return True

                if self.ospfiftype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                return meta._meta_table['OspfMib.Ospfiftable.Ospfifentry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfIfTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ospfifentry is not None:
                for child_ref in self.ospfifentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
            return meta._meta_table['OspfMib.Ospfiftable']['meta_info']


    class Ospfifmetrictable(object):
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
            self.parent = None
            self.ospfifmetricentry = YList()
            self.ospfifmetricentry.parent = self
            self.ospfifmetricentry.name = 'ospfifmetricentry'


        class Ospfifmetricentry(object):
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
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: ospfifmetricvalue
            
            	The metric of using this Type of Service on this interface.  The default value of the TOS 0 metric is 10^8 / ifSpeed
            	**type**\:  int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                self.parent = None
                self.ospfifmetricipaddress = None
                self.ospfifmetricaddresslessif = None
                self.ospfifmetrictos = None
                self.ospfifmetricstatus = None
                self.ospfifmetricvalue = None

            @property
            def _common_path(self):
                if self.ospfifmetricipaddress is None:
                    raise YPYModelError('Key property ospfifmetricipaddress is None')
                if self.ospfifmetricaddresslessif is None:
                    raise YPYModelError('Key property ospfifmetricaddresslessif is None')
                if self.ospfifmetrictos is None:
                    raise YPYModelError('Key property ospfifmetrictos is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfIfMetricTable/OSPF-MIB:ospfIfMetricEntry[OSPF-MIB:ospfIfMetricIpAddress = ' + str(self.ospfifmetricipaddress) + '][OSPF-MIB:ospfIfMetricAddressLessIf = ' + str(self.ospfifmetricaddresslessif) + '][OSPF-MIB:ospfIfMetricTOS = ' + str(self.ospfifmetrictos) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ospfifmetricipaddress is not None:
                    return True

                if self.ospfifmetricaddresslessif is not None:
                    return True

                if self.ospfifmetrictos is not None:
                    return True

                if self.ospfifmetricstatus is not None:
                    return True

                if self.ospfifmetricvalue is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                return meta._meta_table['OspfMib.Ospfifmetrictable.Ospfifmetricentry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfIfMetricTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ospfifmetricentry is not None:
                for child_ref in self.ospfifmetricentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
            return meta._meta_table['OspfMib.Ospfifmetrictable']['meta_info']


    class Ospfvirtiftable(object):
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
            self.parent = None
            self.ospfvirtifentry = YList()
            self.ospfvirtifentry.parent = self
            self.ospfvirtifentry.name = 'ospfvirtifentry'


        class Ospfvirtifentry(object):
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
            	**type**\:   :py:class:`OspfauthenticationtypeEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfauthenticationtypeEnum>`
            
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
            	**type**\:   :py:class:`OspfvirtifstateEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfvirtiftable.Ospfvirtifentry.OspfvirtifstateEnum>`
            
            .. attribute:: ospfvirtifstatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: ospfvirtiftransitdelay
            
            	The estimated number of seconds it takes to transmit a Link State update packet over this interface.  Note that the minimal value SHOULD be 1 second
            	**type**\:  int
            
            	**range:** 0..3600
            
            	**units**\: seconds
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                self.parent = None
                self.ospfvirtifareaid = None
                self.ospfvirtifneighbor = None
                self.cospfvirtiflsacksumsum = None
                self.cospfvirtiflsacount = None
                self.ospfvirtifauthkey = None
                self.ospfvirtifauthtype = None
                self.ospfvirtifevents = None
                self.ospfvirtifhellointerval = None
                self.ospfvirtiflsacksumsum = None
                self.ospfvirtiflsacount = None
                self.ospfvirtifretransinterval = None
                self.ospfvirtifrtrdeadinterval = None
                self.ospfvirtifstate = None
                self.ospfvirtifstatus = None
                self.ospfvirtiftransitdelay = None

            class OspfvirtifstateEnum(Enum):
                """
                OspfvirtifstateEnum

                OSPF virtual interface states.

                .. data:: down = 1

                .. data:: pointToPoint = 4

                """

                down = 1

                pointToPoint = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospfvirtiftable.Ospfvirtifentry.OspfvirtifstateEnum']


            @property
            def _common_path(self):
                if self.ospfvirtifareaid is None:
                    raise YPYModelError('Key property ospfvirtifareaid is None')
                if self.ospfvirtifneighbor is None:
                    raise YPYModelError('Key property ospfvirtifneighbor is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfVirtIfTable/OSPF-MIB:ospfVirtIfEntry[OSPF-MIB:ospfVirtIfAreaId = ' + str(self.ospfvirtifareaid) + '][OSPF-MIB:ospfVirtIfNeighbor = ' + str(self.ospfvirtifneighbor) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ospfvirtifareaid is not None:
                    return True

                if self.ospfvirtifneighbor is not None:
                    return True

                if self.cospfvirtiflsacksumsum is not None:
                    return True

                if self.cospfvirtiflsacount is not None:
                    return True

                if self.ospfvirtifauthkey is not None:
                    return True

                if self.ospfvirtifauthtype is not None:
                    return True

                if self.ospfvirtifevents is not None:
                    return True

                if self.ospfvirtifhellointerval is not None:
                    return True

                if self.ospfvirtiflsacksumsum is not None:
                    return True

                if self.ospfvirtiflsacount is not None:
                    return True

                if self.ospfvirtifretransinterval is not None:
                    return True

                if self.ospfvirtifrtrdeadinterval is not None:
                    return True

                if self.ospfvirtifstate is not None:
                    return True

                if self.ospfvirtifstatus is not None:
                    return True

                if self.ospfvirtiftransitdelay is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                return meta._meta_table['OspfMib.Ospfvirtiftable.Ospfvirtifentry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfVirtIfTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ospfvirtifentry is not None:
                for child_ref in self.ospfvirtifentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
            return meta._meta_table['OspfMib.Ospfvirtiftable']['meta_info']


    class Ospfnbrtable(object):
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
            self.parent = None
            self.ospfnbrentry = YList()
            self.ospfnbrentry.parent = self
            self.ospfnbrentry.name = 'ospfnbrentry'


        class Ospfnbrentry(object):
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
            	**type**\:   :py:class:`OspfnbmanbrpermanenceEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfnbrtable.Ospfnbrentry.OspfnbmanbrpermanenceEnum>`
            
            .. attribute:: ospfnbmanbrstatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
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
            	**type**\:   :py:class:`OspfnbrrestarthelperexitreasonEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfnbrtable.Ospfnbrentry.OspfnbrrestarthelperexitreasonEnum>`
            
            .. attribute:: ospfnbrrestarthelperstatus
            
            	Indicates whether the router is acting as a graceful restart helper for the neighbor
            	**type**\:   :py:class:`OspfnbrrestarthelperstatusEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfnbrtable.Ospfnbrentry.OspfnbrrestarthelperstatusEnum>`
            
            .. attribute:: ospfnbrrtrid
            
            	A 32\-bit integer (represented as a type IpAddress) uniquely identifying the neighboring router in the Autonomous System
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfnbrstate
            
            	The state of the relationship with this neighbor
            	**type**\:   :py:class:`OspfnbrstateEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfnbrtable.Ospfnbrentry.OspfnbrstateEnum>`
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                self.parent = None
                self.ospfnbripaddr = None
                self.ospfnbraddresslessindex = None
                self.ospfnbmanbrpermanence = None
                self.ospfnbmanbrstatus = None
                self.ospfnbrevents = None
                self.ospfnbrhellosuppressed = None
                self.ospfnbrlsretransqlen = None
                self.ospfnbroptions = None
                self.ospfnbrpriority = None
                self.ospfnbrrestarthelperage = None
                self.ospfnbrrestarthelperexitreason = None
                self.ospfnbrrestarthelperstatus = None
                self.ospfnbrrtrid = None
                self.ospfnbrstate = None

            class OspfnbmanbrpermanenceEnum(Enum):
                """
                OspfnbmanbrpermanenceEnum

                This variable displays the status of the entry;

                'dynamic' and 'permanent' refer to how the neighbor

                became known.

                .. data:: dynamic = 1

                .. data:: permanent = 2

                """

                dynamic = 1

                permanent = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospfnbrtable.Ospfnbrentry.OspfnbmanbrpermanenceEnum']


            class OspfnbrrestarthelperexitreasonEnum(Enum):
                """
                OspfnbrrestarthelperexitreasonEnum

                Describes the outcome of the last attempt at acting

                as a graceful restart helper for the neighbor.

                .. data:: none = 1

                .. data:: inProgress = 2

                .. data:: completed = 3

                .. data:: timedOut = 4

                .. data:: topologyChanged = 5

                """

                none = 1

                inProgress = 2

                completed = 3

                timedOut = 4

                topologyChanged = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospfnbrtable.Ospfnbrentry.OspfnbrrestarthelperexitreasonEnum']


            class OspfnbrrestarthelperstatusEnum(Enum):
                """
                OspfnbrrestarthelperstatusEnum

                Indicates whether the router is acting

                as a graceful restart helper for the neighbor.

                .. data:: notHelping = 1

                .. data:: helping = 2

                """

                notHelping = 1

                helping = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospfnbrtable.Ospfnbrentry.OspfnbrrestarthelperstatusEnum']


            class OspfnbrstateEnum(Enum):
                """
                OspfnbrstateEnum

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

                down = 1

                attempt = 2

                init = 3

                twoWay = 4

                exchangeStart = 5

                exchange = 6

                loading = 7

                full = 8


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospfnbrtable.Ospfnbrentry.OspfnbrstateEnum']


            @property
            def _common_path(self):
                if self.ospfnbripaddr is None:
                    raise YPYModelError('Key property ospfnbripaddr is None')
                if self.ospfnbraddresslessindex is None:
                    raise YPYModelError('Key property ospfnbraddresslessindex is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfNbrTable/OSPF-MIB:ospfNbrEntry[OSPF-MIB:ospfNbrIpAddr = ' + str(self.ospfnbripaddr) + '][OSPF-MIB:ospfNbrAddressLessIndex = ' + str(self.ospfnbraddresslessindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ospfnbripaddr is not None:
                    return True

                if self.ospfnbraddresslessindex is not None:
                    return True

                if self.ospfnbmanbrpermanence is not None:
                    return True

                if self.ospfnbmanbrstatus is not None:
                    return True

                if self.ospfnbrevents is not None:
                    return True

                if self.ospfnbrhellosuppressed is not None:
                    return True

                if self.ospfnbrlsretransqlen is not None:
                    return True

                if self.ospfnbroptions is not None:
                    return True

                if self.ospfnbrpriority is not None:
                    return True

                if self.ospfnbrrestarthelperage is not None:
                    return True

                if self.ospfnbrrestarthelperexitreason is not None:
                    return True

                if self.ospfnbrrestarthelperstatus is not None:
                    return True

                if self.ospfnbrrtrid is not None:
                    return True

                if self.ospfnbrstate is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                return meta._meta_table['OspfMib.Ospfnbrtable.Ospfnbrentry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfNbrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ospfnbrentry is not None:
                for child_ref in self.ospfnbrentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
            return meta._meta_table['OspfMib.Ospfnbrtable']['meta_info']


    class Ospfvirtnbrtable(object):
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
            self.parent = None
            self.ospfvirtnbrentry = YList()
            self.ospfvirtnbrentry.parent = self
            self.ospfvirtnbrentry.name = 'ospfvirtnbrentry'


        class Ospfvirtnbrentry(object):
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
            	**type**\:   :py:class:`OspfvirtnbrrestarthelperexitreasonEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfvirtnbrtable.Ospfvirtnbrentry.OspfvirtnbrrestarthelperexitreasonEnum>`
            
            .. attribute:: ospfvirtnbrrestarthelperstatus
            
            	Indicates whether the router is acting as a graceful restart helper for the neighbor
            	**type**\:   :py:class:`OspfvirtnbrrestarthelperstatusEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfvirtnbrtable.Ospfvirtnbrentry.OspfvirtnbrrestarthelperstatusEnum>`
            
            .. attribute:: ospfvirtnbrstate
            
            	The state of the virtual neighbor relationship
            	**type**\:   :py:class:`OspfvirtnbrstateEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfvirtnbrtable.Ospfvirtnbrentry.OspfvirtnbrstateEnum>`
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                self.parent = None
                self.ospfvirtnbrarea = None
                self.ospfvirtnbrrtrid = None
                self.ospfvirtnbrevents = None
                self.ospfvirtnbrhellosuppressed = None
                self.ospfvirtnbripaddr = None
                self.ospfvirtnbrlsretransqlen = None
                self.ospfvirtnbroptions = None
                self.ospfvirtnbrrestarthelperage = None
                self.ospfvirtnbrrestarthelperexitreason = None
                self.ospfvirtnbrrestarthelperstatus = None
                self.ospfvirtnbrstate = None

            class OspfvirtnbrrestarthelperexitreasonEnum(Enum):
                """
                OspfvirtnbrrestarthelperexitreasonEnum

                Describes the outcome of the last attempt at acting

                as a graceful restart helper for the neighbor.

                .. data:: none = 1

                .. data:: inProgress = 2

                .. data:: completed = 3

                .. data:: timedOut = 4

                .. data:: topologyChanged = 5

                """

                none = 1

                inProgress = 2

                completed = 3

                timedOut = 4

                topologyChanged = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospfvirtnbrtable.Ospfvirtnbrentry.OspfvirtnbrrestarthelperexitreasonEnum']


            class OspfvirtnbrrestarthelperstatusEnum(Enum):
                """
                OspfvirtnbrrestarthelperstatusEnum

                Indicates whether the router is acting

                as a graceful restart helper for the neighbor.

                .. data:: notHelping = 1

                .. data:: helping = 2

                """

                notHelping = 1

                helping = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospfvirtnbrtable.Ospfvirtnbrentry.OspfvirtnbrrestarthelperstatusEnum']


            class OspfvirtnbrstateEnum(Enum):
                """
                OspfvirtnbrstateEnum

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

                down = 1

                attempt = 2

                init = 3

                twoWay = 4

                exchangeStart = 5

                exchange = 6

                loading = 7

                full = 8


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospfvirtnbrtable.Ospfvirtnbrentry.OspfvirtnbrstateEnum']


            @property
            def _common_path(self):
                if self.ospfvirtnbrarea is None:
                    raise YPYModelError('Key property ospfvirtnbrarea is None')
                if self.ospfvirtnbrrtrid is None:
                    raise YPYModelError('Key property ospfvirtnbrrtrid is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfVirtNbrTable/OSPF-MIB:ospfVirtNbrEntry[OSPF-MIB:ospfVirtNbrArea = ' + str(self.ospfvirtnbrarea) + '][OSPF-MIB:ospfVirtNbrRtrId = ' + str(self.ospfvirtnbrrtrid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ospfvirtnbrarea is not None:
                    return True

                if self.ospfvirtnbrrtrid is not None:
                    return True

                if self.ospfvirtnbrevents is not None:
                    return True

                if self.ospfvirtnbrhellosuppressed is not None:
                    return True

                if self.ospfvirtnbripaddr is not None:
                    return True

                if self.ospfvirtnbrlsretransqlen is not None:
                    return True

                if self.ospfvirtnbroptions is not None:
                    return True

                if self.ospfvirtnbrrestarthelperage is not None:
                    return True

                if self.ospfvirtnbrrestarthelperexitreason is not None:
                    return True

                if self.ospfvirtnbrrestarthelperstatus is not None:
                    return True

                if self.ospfvirtnbrstate is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                return meta._meta_table['OspfMib.Ospfvirtnbrtable.Ospfvirtnbrentry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfVirtNbrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ospfvirtnbrentry is not None:
                for child_ref in self.ospfvirtnbrentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
            return meta._meta_table['OspfMib.Ospfvirtnbrtable']['meta_info']


    class Ospfextlsdbtable(object):
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
            self.parent = None
            self.ospfextlsdbentry = YList()
            self.ospfextlsdbentry.parent = self
            self.ospfextlsdbentry.name = 'ospfextlsdbentry'


        class Ospfextlsdbentry(object):
            """
            A single link state advertisement.
            
            .. attribute:: ospfextlsdbtype  <key>
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\:   :py:class:`OspfextlsdbtypeEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfextlsdbtable.Ospfextlsdbentry.OspfextlsdbtypeEnum>`
            
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
                self.parent = None
                self.ospfextlsdbtype = None
                self.ospfextlsdblsid = None
                self.ospfextlsdbrouterid = None
                self.ospfextlsdbadvertisement = None
                self.ospfextlsdbage = None
                self.ospfextlsdbchecksum = None
                self.ospfextlsdbsequence = None

            class OspfextlsdbtypeEnum(Enum):
                """
                OspfextlsdbtypeEnum

                The type of the link state advertisement.

                Each link state type has a separate advertisement

                format.

                .. data:: asExternalLink = 5

                """

                asExternalLink = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospfextlsdbtable.Ospfextlsdbentry.OspfextlsdbtypeEnum']


            @property
            def _common_path(self):
                if self.ospfextlsdbtype is None:
                    raise YPYModelError('Key property ospfextlsdbtype is None')
                if self.ospfextlsdblsid is None:
                    raise YPYModelError('Key property ospfextlsdblsid is None')
                if self.ospfextlsdbrouterid is None:
                    raise YPYModelError('Key property ospfextlsdbrouterid is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfExtLsdbTable/OSPF-MIB:ospfExtLsdbEntry[OSPF-MIB:ospfExtLsdbType = ' + str(self.ospfextlsdbtype) + '][OSPF-MIB:ospfExtLsdbLsid = ' + str(self.ospfextlsdblsid) + '][OSPF-MIB:ospfExtLsdbRouterId = ' + str(self.ospfextlsdbrouterid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ospfextlsdbtype is not None:
                    return True

                if self.ospfextlsdblsid is not None:
                    return True

                if self.ospfextlsdbrouterid is not None:
                    return True

                if self.ospfextlsdbadvertisement is not None:
                    return True

                if self.ospfextlsdbage is not None:
                    return True

                if self.ospfextlsdbchecksum is not None:
                    return True

                if self.ospfextlsdbsequence is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                return meta._meta_table['OspfMib.Ospfextlsdbtable.Ospfextlsdbentry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfExtLsdbTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ospfextlsdbentry is not None:
                for child_ref in self.ospfextlsdbentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
            return meta._meta_table['OspfMib.Ospfextlsdbtable']['meta_info']


    class Ospfareaaggregatetable(object):
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
            self.parent = None
            self.ospfareaaggregateentry = YList()
            self.ospfareaaggregateentry.parent = self
            self.ospfareaaggregateentry.name = 'ospfareaaggregateentry'


        class Ospfareaaggregateentry(object):
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
            	**type**\:   :py:class:`OspfareaaggregatelsdbtypeEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfareaaggregatetable.Ospfareaaggregateentry.OspfareaaggregatelsdbtypeEnum>`
            
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
            	**type**\:   :py:class:`OspfareaaggregateeffectEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfareaaggregatetable.Ospfareaaggregateentry.OspfareaaggregateeffectEnum>`
            
            .. attribute:: ospfareaaggregateextroutetag
            
            	External route tag to be included in NSSA (type\-7) LSAs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfareaaggregatestatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                self.parent = None
                self.ospfareaaggregateareaid = None
                self.ospfareaaggregatelsdbtype = None
                self.ospfareaaggregatenet = None
                self.ospfareaaggregatemask = None
                self.ospfareaaggregateeffect = None
                self.ospfareaaggregateextroutetag = None
                self.ospfareaaggregatestatus = None

            class OspfareaaggregateeffectEnum(Enum):
                """
                OspfareaaggregateeffectEnum

                Subnets subsumed by ranges either trigger the

                advertisement of the indicated aggregate

                (advertiseMatching) or result in the subnet's not

                being advertised at all outside the area.

                .. data:: advertiseMatching = 1

                .. data:: doNotAdvertiseMatching = 2

                """

                advertiseMatching = 1

                doNotAdvertiseMatching = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospfareaaggregatetable.Ospfareaaggregateentry.OspfareaaggregateeffectEnum']


            class OspfareaaggregatelsdbtypeEnum(Enum):
                """
                OspfareaaggregatelsdbtypeEnum

                The type of the address aggregate.  This field

                specifies the Lsdb type that this address

                aggregate applies to.

                .. data:: summaryLink = 3

                .. data:: nssaExternalLink = 7

                """

                summaryLink = 3

                nssaExternalLink = 7


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospfareaaggregatetable.Ospfareaaggregateentry.OspfareaaggregatelsdbtypeEnum']


            @property
            def _common_path(self):
                if self.ospfareaaggregateareaid is None:
                    raise YPYModelError('Key property ospfareaaggregateareaid is None')
                if self.ospfareaaggregatelsdbtype is None:
                    raise YPYModelError('Key property ospfareaaggregatelsdbtype is None')
                if self.ospfareaaggregatenet is None:
                    raise YPYModelError('Key property ospfareaaggregatenet is None')
                if self.ospfareaaggregatemask is None:
                    raise YPYModelError('Key property ospfareaaggregatemask is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfAreaAggregateTable/OSPF-MIB:ospfAreaAggregateEntry[OSPF-MIB:ospfAreaAggregateAreaID = ' + str(self.ospfareaaggregateareaid) + '][OSPF-MIB:ospfAreaAggregateLsdbType = ' + str(self.ospfareaaggregatelsdbtype) + '][OSPF-MIB:ospfAreaAggregateNet = ' + str(self.ospfareaaggregatenet) + '][OSPF-MIB:ospfAreaAggregateMask = ' + str(self.ospfareaaggregatemask) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ospfareaaggregateareaid is not None:
                    return True

                if self.ospfareaaggregatelsdbtype is not None:
                    return True

                if self.ospfareaaggregatenet is not None:
                    return True

                if self.ospfareaaggregatemask is not None:
                    return True

                if self.ospfareaaggregateeffect is not None:
                    return True

                if self.ospfareaaggregateextroutetag is not None:
                    return True

                if self.ospfareaaggregatestatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                return meta._meta_table['OspfMib.Ospfareaaggregatetable.Ospfareaaggregateentry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfAreaAggregateTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ospfareaaggregateentry is not None:
                for child_ref in self.ospfareaaggregateentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
            return meta._meta_table['OspfMib.Ospfareaaggregatetable']['meta_info']


    class Ospflocallsdbtable(object):
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
            self.parent = None
            self.ospflocallsdbentry = YList()
            self.ospflocallsdbentry.parent = self
            self.ospflocallsdbentry.name = 'ospflocallsdbentry'


        class Ospflocallsdbentry(object):
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
            	**type**\:   :py:class:`OspflocallsdbtypeEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospflocallsdbtable.Ospflocallsdbentry.OspflocallsdbtypeEnum>`
            
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
                self.parent = None
                self.ospflocallsdbipaddress = None
                self.ospflocallsdbaddresslessif = None
                self.ospflocallsdbtype = None
                self.ospflocallsdblsid = None
                self.ospflocallsdbrouterid = None
                self.ospflocallsdbadvertisement = None
                self.ospflocallsdbage = None
                self.ospflocallsdbchecksum = None
                self.ospflocallsdbsequence = None

            class OspflocallsdbtypeEnum(Enum):
                """
                OspflocallsdbtypeEnum

                The type of the link state advertisement.

                Each link state type has a separate

                advertisement format.

                .. data:: localOpaqueLink = 9

                """

                localOpaqueLink = 9


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospflocallsdbtable.Ospflocallsdbentry.OspflocallsdbtypeEnum']


            @property
            def _common_path(self):
                if self.ospflocallsdbipaddress is None:
                    raise YPYModelError('Key property ospflocallsdbipaddress is None')
                if self.ospflocallsdbaddresslessif is None:
                    raise YPYModelError('Key property ospflocallsdbaddresslessif is None')
                if self.ospflocallsdbtype is None:
                    raise YPYModelError('Key property ospflocallsdbtype is None')
                if self.ospflocallsdblsid is None:
                    raise YPYModelError('Key property ospflocallsdblsid is None')
                if self.ospflocallsdbrouterid is None:
                    raise YPYModelError('Key property ospflocallsdbrouterid is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfLocalLsdbTable/OSPF-MIB:ospfLocalLsdbEntry[OSPF-MIB:ospfLocalLsdbIpAddress = ' + str(self.ospflocallsdbipaddress) + '][OSPF-MIB:ospfLocalLsdbAddressLessIf = ' + str(self.ospflocallsdbaddresslessif) + '][OSPF-MIB:ospfLocalLsdbType = ' + str(self.ospflocallsdbtype) + '][OSPF-MIB:ospfLocalLsdbLsid = ' + str(self.ospflocallsdblsid) + '][OSPF-MIB:ospfLocalLsdbRouterId = ' + str(self.ospflocallsdbrouterid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ospflocallsdbipaddress is not None:
                    return True

                if self.ospflocallsdbaddresslessif is not None:
                    return True

                if self.ospflocallsdbtype is not None:
                    return True

                if self.ospflocallsdblsid is not None:
                    return True

                if self.ospflocallsdbrouterid is not None:
                    return True

                if self.ospflocallsdbadvertisement is not None:
                    return True

                if self.ospflocallsdbage is not None:
                    return True

                if self.ospflocallsdbchecksum is not None:
                    return True

                if self.ospflocallsdbsequence is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                return meta._meta_table['OspfMib.Ospflocallsdbtable.Ospflocallsdbentry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfLocalLsdbTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ospflocallsdbentry is not None:
                for child_ref in self.ospflocallsdbentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
            return meta._meta_table['OspfMib.Ospflocallsdbtable']['meta_info']


    class Ospfvirtlocallsdbtable(object):
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
            self.parent = None
            self.ospfvirtlocallsdbentry = YList()
            self.ospfvirtlocallsdbentry.parent = self
            self.ospfvirtlocallsdbentry.name = 'ospfvirtlocallsdbentry'


        class Ospfvirtlocallsdbentry(object):
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
            	**type**\:   :py:class:`OspfvirtlocallsdbtypeEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfvirtlocallsdbtable.Ospfvirtlocallsdbentry.OspfvirtlocallsdbtypeEnum>`
            
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
                self.parent = None
                self.ospfvirtlocallsdbtransitarea = None
                self.ospfvirtlocallsdbneighbor = None
                self.ospfvirtlocallsdbtype = None
                self.ospfvirtlocallsdblsid = None
                self.ospfvirtlocallsdbrouterid = None
                self.ospfvirtlocallsdbadvertisement = None
                self.ospfvirtlocallsdbage = None
                self.ospfvirtlocallsdbchecksum = None
                self.ospfvirtlocallsdbsequence = None

            class OspfvirtlocallsdbtypeEnum(Enum):
                """
                OspfvirtlocallsdbtypeEnum

                The type of the link state advertisement.

                Each link state type has a separate

                advertisement format.

                .. data:: localOpaqueLink = 9

                """

                localOpaqueLink = 9


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospfvirtlocallsdbtable.Ospfvirtlocallsdbentry.OspfvirtlocallsdbtypeEnum']


            @property
            def _common_path(self):
                if self.ospfvirtlocallsdbtransitarea is None:
                    raise YPYModelError('Key property ospfvirtlocallsdbtransitarea is None')
                if self.ospfvirtlocallsdbneighbor is None:
                    raise YPYModelError('Key property ospfvirtlocallsdbneighbor is None')
                if self.ospfvirtlocallsdbtype is None:
                    raise YPYModelError('Key property ospfvirtlocallsdbtype is None')
                if self.ospfvirtlocallsdblsid is None:
                    raise YPYModelError('Key property ospfvirtlocallsdblsid is None')
                if self.ospfvirtlocallsdbrouterid is None:
                    raise YPYModelError('Key property ospfvirtlocallsdbrouterid is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfVirtLocalLsdbTable/OSPF-MIB:ospfVirtLocalLsdbEntry[OSPF-MIB:ospfVirtLocalLsdbTransitArea = ' + str(self.ospfvirtlocallsdbtransitarea) + '][OSPF-MIB:ospfVirtLocalLsdbNeighbor = ' + str(self.ospfvirtlocallsdbneighbor) + '][OSPF-MIB:ospfVirtLocalLsdbType = ' + str(self.ospfvirtlocallsdbtype) + '][OSPF-MIB:ospfVirtLocalLsdbLsid = ' + str(self.ospfvirtlocallsdblsid) + '][OSPF-MIB:ospfVirtLocalLsdbRouterId = ' + str(self.ospfvirtlocallsdbrouterid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ospfvirtlocallsdbtransitarea is not None:
                    return True

                if self.ospfvirtlocallsdbneighbor is not None:
                    return True

                if self.ospfvirtlocallsdbtype is not None:
                    return True

                if self.ospfvirtlocallsdblsid is not None:
                    return True

                if self.ospfvirtlocallsdbrouterid is not None:
                    return True

                if self.ospfvirtlocallsdbadvertisement is not None:
                    return True

                if self.ospfvirtlocallsdbage is not None:
                    return True

                if self.ospfvirtlocallsdbchecksum is not None:
                    return True

                if self.ospfvirtlocallsdbsequence is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                return meta._meta_table['OspfMib.Ospfvirtlocallsdbtable.Ospfvirtlocallsdbentry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfVirtLocalLsdbTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ospfvirtlocallsdbentry is not None:
                for child_ref in self.ospfvirtlocallsdbentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
            return meta._meta_table['OspfMib.Ospfvirtlocallsdbtable']['meta_info']


    class Ospfaslsdbtable(object):
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
            self.parent = None
            self.ospfaslsdbentry = YList()
            self.ospfaslsdbentry.parent = self
            self.ospfaslsdbentry.name = 'ospfaslsdbentry'


        class Ospfaslsdbentry(object):
            """
            A single link state advertisement.
            
            .. attribute:: ospfaslsdbtype  <key>
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\:   :py:class:`OspfaslsdbtypeEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfaslsdbtable.Ospfaslsdbentry.OspfaslsdbtypeEnum>`
            
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
                self.parent = None
                self.ospfaslsdbtype = None
                self.ospfaslsdblsid = None
                self.ospfaslsdbrouterid = None
                self.ospfaslsdbadvertisement = None
                self.ospfaslsdbage = None
                self.ospfaslsdbchecksum = None
                self.ospfaslsdbsequence = None

            class OspfaslsdbtypeEnum(Enum):
                """
                OspfaslsdbtypeEnum

                The type of the link state advertisement.

                Each link state type has a separate

                advertisement format.

                .. data:: asExternalLink = 5

                .. data:: asOpaqueLink = 11

                """

                asExternalLink = 5

                asOpaqueLink = 11


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospfaslsdbtable.Ospfaslsdbentry.OspfaslsdbtypeEnum']


            @property
            def _common_path(self):
                if self.ospfaslsdbtype is None:
                    raise YPYModelError('Key property ospfaslsdbtype is None')
                if self.ospfaslsdblsid is None:
                    raise YPYModelError('Key property ospfaslsdblsid is None')
                if self.ospfaslsdbrouterid is None:
                    raise YPYModelError('Key property ospfaslsdbrouterid is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfAsLsdbTable/OSPF-MIB:ospfAsLsdbEntry[OSPF-MIB:ospfAsLsdbType = ' + str(self.ospfaslsdbtype) + '][OSPF-MIB:ospfAsLsdbLsid = ' + str(self.ospfaslsdblsid) + '][OSPF-MIB:ospfAsLsdbRouterId = ' + str(self.ospfaslsdbrouterid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ospfaslsdbtype is not None:
                    return True

                if self.ospfaslsdblsid is not None:
                    return True

                if self.ospfaslsdbrouterid is not None:
                    return True

                if self.ospfaslsdbadvertisement is not None:
                    return True

                if self.ospfaslsdbage is not None:
                    return True

                if self.ospfaslsdbchecksum is not None:
                    return True

                if self.ospfaslsdbsequence is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                return meta._meta_table['OspfMib.Ospfaslsdbtable.Ospfaslsdbentry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfAsLsdbTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ospfaslsdbentry is not None:
                for child_ref in self.ospfaslsdbentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
            return meta._meta_table['OspfMib.Ospfaslsdbtable']['meta_info']


    class Ospfarealsacounttable(object):
        """
        This table maintains per\-area, per\-LSA\-type counters
        
        .. attribute:: ospfarealsacountentry
        
        	An entry with a number of link advertisements  of a given type for a given area
        	**type**\: list of    :py:class:`Ospfarealsacountentry <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfarealsacounttable.Ospfarealsacountentry>`
        
        

        """

        _prefix = 'OSPF-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            self.parent = None
            self.ospfarealsacountentry = YList()
            self.ospfarealsacountentry.parent = self
            self.ospfarealsacountentry.name = 'ospfarealsacountentry'


        class Ospfarealsacountentry(object):
            """
            An entry with a number of link advertisements
            
            of a given type for a given area.
            
            .. attribute:: ospfarealsacountareaid  <key>
            
            	This entry Area ID
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfarealsacountlsatype  <key>
            
            	This entry LSA type
            	**type**\:   :py:class:`OspfarealsacountlsatypeEnum <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospfarealsacounttable.Ospfarealsacountentry.OspfarealsacountlsatypeEnum>`
            
            .. attribute:: ospfarealsacountnumber
            
            	Number of LSAs of a given type for a given area
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'OSPF-MIB'
            _revision = '2006-11-10'

            def __init__(self):
                self.parent = None
                self.ospfarealsacountareaid = None
                self.ospfarealsacountlsatype = None
                self.ospfarealsacountnumber = None

            class OspfarealsacountlsatypeEnum(Enum):
                """
                OspfarealsacountlsatypeEnum

                This entry LSA type.

                .. data:: routerLink = 1

                .. data:: networkLink = 2

                .. data:: summaryLink = 3

                .. data:: asSummaryLink = 4

                .. data:: multicastLink = 6

                .. data:: nssaExternalLink = 7

                .. data:: areaOpaqueLink = 10

                """

                routerLink = 1

                networkLink = 2

                summaryLink = 3

                asSummaryLink = 4

                multicastLink = 6

                nssaExternalLink = 7

                areaOpaqueLink = 10


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                    return meta._meta_table['OspfMib.Ospfarealsacounttable.Ospfarealsacountentry.OspfarealsacountlsatypeEnum']


            @property
            def _common_path(self):
                if self.ospfarealsacountareaid is None:
                    raise YPYModelError('Key property ospfarealsacountareaid is None')
                if self.ospfarealsacountlsatype is None:
                    raise YPYModelError('Key property ospfarealsacountlsatype is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfAreaLsaCountTable/OSPF-MIB:ospfAreaLsaCountEntry[OSPF-MIB:ospfAreaLsaCountAreaId = ' + str(self.ospfarealsacountareaid) + '][OSPF-MIB:ospfAreaLsaCountLsaType = ' + str(self.ospfarealsacountlsatype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ospfarealsacountareaid is not None:
                    return True

                if self.ospfarealsacountlsatype is not None:
                    return True

                if self.ospfarealsacountnumber is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
                return meta._meta_table['OspfMib.Ospfarealsacounttable.Ospfarealsacountentry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfAreaLsaCountTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ospfarealsacountentry is not None:
                for child_ref in self.ospfarealsacountentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
            return meta._meta_table['OspfMib.Ospfarealsacounttable']['meta_info']

    @property
    def _common_path(self):

        return '/OSPF-MIB:OSPF-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.ospfareaaggregatetable is not None and self.ospfareaaggregatetable._has_data():
            return True

        if self.ospfarealsacounttable is not None and self.ospfarealsacounttable._has_data():
            return True

        if self.ospfarearangetable is not None and self.ospfarearangetable._has_data():
            return True

        if self.ospfareatable is not None and self.ospfareatable._has_data():
            return True

        if self.ospfaslsdbtable is not None and self.ospfaslsdbtable._has_data():
            return True

        if self.ospfextlsdbtable is not None and self.ospfextlsdbtable._has_data():
            return True

        if self.ospfgeneralgroup is not None and self.ospfgeneralgroup._has_data():
            return True

        if self.ospfhosttable is not None and self.ospfhosttable._has_data():
            return True

        if self.ospfifmetrictable is not None and self.ospfifmetrictable._has_data():
            return True

        if self.ospfiftable is not None and self.ospfiftable._has_data():
            return True

        if self.ospflocallsdbtable is not None and self.ospflocallsdbtable._has_data():
            return True

        if self.ospflsdbtable is not None and self.ospflsdbtable._has_data():
            return True

        if self.ospfnbrtable is not None and self.ospfnbrtable._has_data():
            return True

        if self.ospfstubareatable is not None and self.ospfstubareatable._has_data():
            return True

        if self.ospfvirtiftable is not None and self.ospfvirtiftable._has_data():
            return True

        if self.ospfvirtlocallsdbtable is not None and self.ospfvirtlocallsdbtable._has_data():
            return True

        if self.ospfvirtnbrtable is not None and self.ospfvirtnbrtable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _OSPF_MIB as meta
        return meta._meta_table['OspfMib']['meta_info']



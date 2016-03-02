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

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum

class OspfAuthenticationType_Enum(Enum):
    """
    OspfAuthenticationType_Enum

    The authentication type.

    """

    NONE = 0

    SIMPLEPASSWORD = 1

    MD5 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ospf._meta import _OSPF_MIB as meta
        return meta._meta_table['OspfAuthenticationType_Enum']


class Status_Enum(Enum):
    """
    Status_Enum

    An indication of the operability of an OSPF
    function or feature.  For example, the status
    of an interface\: 'enabled' indicates that
    it is willing to communicate with other OSPF routers,
    and 'disabled' indicates that it is not.

    """

    ENABLED = 1

    DISABLED = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ospf._meta import _OSPF_MIB as meta
        return meta._meta_table['Status_Enum']



class OSPFMIB(object):
    """
    
    
    .. attribute:: ospfareaaggregatetable
    
    	The Area Aggregate Table acts as an adjunct to the Area Table.  It describes those address aggregates that are configured to be propagated from an area. Its purpose is to reduce the amount of information that is known beyond an Area's borders.  It contains a set of IP address ranges specified by an IP address/IP network mask pair. For example, a class B address range of X.X.X.X with a network mask of 255.255.0.0 includes all IP addresses from X.X.0.0 to X.X.255.255.  Note that if ranges are configured such that one range subsumes another range (e.g., 10.0.0.0 mask 255.0.0.0 and 10.1.0.0 mask 255.255.0.0), the most specific match is the preferred one
    	**type**\: :py:class:`OspfAreaAggregateTable <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfAreaAggregateTable>`
    
    .. attribute:: ospfarealsacounttable
    
    	This table maintains per\-area, per\-LSA\-type counters
    	**type**\: :py:class:`OspfAreaLsaCountTable <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfAreaLsaCountTable>`
    
    .. attribute:: ospfarearangetable
    
    	The Address Range Table acts as an adjunct to the Area Table.  It describes those Address Range Summaries that are configured to be propagated from an Area to reduce the amount of information about it that is known beyond its borders.  It contains a set of IP address ranges specified by an IP address/IP network mask pair. For example, class B address range of X.X.X.X with a network mask of 255.255.0.0 includes all IP addresses from X.X.0.0 to X.X.255.255.  Note that this table is obsoleted and is replaced by the Area Aggregate Table
    	**type**\: :py:class:`OspfAreaRangeTable <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfAreaRangeTable>`
    
    .. attribute:: ospfareatable
    
    	Information describing the configured parameters and cumulative statistics of the router's attached areas. The interfaces and virtual links are configured as part of these areas.  Area 0.0.0.0, by definition, is the backbone area
    	**type**\: :py:class:`OspfAreaTable <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfAreaTable>`
    
    .. attribute:: ospfaslsdbtable
    
    	The OSPF Process's AS\-scope LSA link state database. The database contains the AS\-scope Link State Advertisements from throughout the areas that the device is attached to.  This table is identical to the OSPF LSDB Table in format, but contains only AS\-scope Link State Advertisements.  The purpose is to allow AS\-scope LSAs to be displayed once for the router rather than once in each non\-stub area
    	**type**\: :py:class:`OspfAsLsdbTable <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfAsLsdbTable>`
    
    .. attribute:: ospfextlsdbtable
    
    	The OSPF Process's external LSA link state database.  This table is identical to the OSPF LSDB Table in format, but contains only external link state advertisements.  The purpose is to allow external  LSAs to be displayed once for the router rather than once in each non\-stub area.  Note that external LSAs are also in the AS\-scope link state database
    	**type**\: :py:class:`OspfExtLsdbTable <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfExtLsdbTable>`
    
    .. attribute:: ospfgeneralgroup
    
    	
    	**type**\: :py:class:`OspfGeneralGroup <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfGeneralGroup>`
    
    .. attribute:: ospfhosttable
    
    	The Host/Metric Table indicates what hosts are directly  attached to the router, what metrics and types of service should be advertised for them, and what areas they are found within
    	**type**\: :py:class:`OspfHostTable <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfHostTable>`
    
    .. attribute:: ospfifmetrictable
    
    	The Metric Table describes the metrics to be advertised for a specified interface at the various types of service. As such, this table is an adjunct of the OSPF Interface Table.  Types of service, as defined by RFC 791, have the ability to request low delay, high bandwidth, or reliable linkage.  For the purposes of this specification, the measure of bandwidth\:  Metric = referenceBandwidth / ifSpeed  is the default value. The default reference bandwidth is 10^8. For multiple link interfaces, note that ifSpeed is the sum of the individual link speeds.  This yields a number having the following typical values\:  Network Type/bit rate   Metric  >= 100 MBPS                 1 Ethernet/802.3             10 E1                         48 T1 (ESF)                   65 64 KBPS                    1562 56 KBPS                    1785 19.2 KBPS                  5208 9.6 KBPS                   10416  Routes that are not specified use the default (TOS 0) metric.  Note that the default reference bandwidth can be configured using the general group object ospfReferenceBandwidth
    	**type**\: :py:class:`OspfIfMetricTable <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfIfMetricTable>`
    
    .. attribute:: ospfiftable
    
    	The OSPF Interface Table describes the interfaces from the viewpoint of OSPF. It augments the ipAddrTable with OSPF specific information
    	**type**\: :py:class:`OspfIfTable <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfIfTable>`
    
    .. attribute:: ospflocallsdbtable
    
    	The OSPF Process's link\-local link state database for non\-virtual links. This table is identical to the OSPF LSDB Table in format, but contains only link\-local Link State Advertisements for non\-virtual links.  The purpose is to allow link\-local LSAs to be displayed for each non\-virtual interface.  This table is implemented to support type\-9 LSAs that are defined in 'The OSPF Opaque LSA Option'
    	**type**\: :py:class:`OspfLocalLsdbTable <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfLocalLsdbTable>`
    
    .. attribute:: ospflsdbtable
    
    	The OSPF Process's link state database (LSDB). The LSDB contains the link state advertisements from throughout the areas that the device is attached to
    	**type**\: :py:class:`OspfLsdbTable <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfLsdbTable>`
    
    .. attribute:: ospfnbrtable
    
    	A table describing all non\-virtual neighbors in the locality of the OSPF router
    	**type**\: :py:class:`OspfNbrTable <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfNbrTable>`
    
    .. attribute:: ospfstubareatable
    
    	The set of metrics that will be advertised by a default Area Border Router into a stub area
    	**type**\: :py:class:`OspfStubAreaTable <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfStubAreaTable>`
    
    .. attribute:: ospfvirtiftable
    
    	Information about this router's virtual interfaces that the OSPF Process is configured to carry on
    	**type**\: :py:class:`OspfVirtIfTable <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfVirtIfTable>`
    
    .. attribute:: ospfvirtlocallsdbtable
    
    	The OSPF Process's link\-local link state database for virtual links.  This table is identical to the OSPF LSDB Table in format, but contains only link\-local Link State Advertisements for virtual links.  The purpose is to allow link\-local LSAs to be displayed for each virtual interface.  This table is implemented to support type\-9 LSAs that are defined in 'The OSPF Opaque LSA Option'
    	**type**\: :py:class:`OspfVirtLocalLsdbTable <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfVirtLocalLsdbTable>`
    
    .. attribute:: ospfvirtnbrtable
    
    	This table describes all virtual neighbors. Since virtual links are configured in the Virtual Interface Table, this table is read\-only
    	**type**\: :py:class:`OspfVirtNbrTable <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfVirtNbrTable>`
    
    

    """

    _prefix = 'ospf-mib'
    _revision = '2006-11-10'

    def __init__(self):
        self.ospfareaaggregatetable = OSPFMIB.OspfAreaAggregateTable()
        self.ospfareaaggregatetable.parent = self
        self.ospfarealsacounttable = OSPFMIB.OspfAreaLsaCountTable()
        self.ospfarealsacounttable.parent = self
        self.ospfarearangetable = OSPFMIB.OspfAreaRangeTable()
        self.ospfarearangetable.parent = self
        self.ospfareatable = OSPFMIB.OspfAreaTable()
        self.ospfareatable.parent = self
        self.ospfaslsdbtable = OSPFMIB.OspfAsLsdbTable()
        self.ospfaslsdbtable.parent = self
        self.ospfextlsdbtable = OSPFMIB.OspfExtLsdbTable()
        self.ospfextlsdbtable.parent = self
        self.ospfgeneralgroup = OSPFMIB.OspfGeneralGroup()
        self.ospfgeneralgroup.parent = self
        self.ospfhosttable = OSPFMIB.OspfHostTable()
        self.ospfhosttable.parent = self
        self.ospfifmetrictable = OSPFMIB.OspfIfMetricTable()
        self.ospfifmetrictable.parent = self
        self.ospfiftable = OSPFMIB.OspfIfTable()
        self.ospfiftable.parent = self
        self.ospflocallsdbtable = OSPFMIB.OspfLocalLsdbTable()
        self.ospflocallsdbtable.parent = self
        self.ospflsdbtable = OSPFMIB.OspfLsdbTable()
        self.ospflsdbtable.parent = self
        self.ospfnbrtable = OSPFMIB.OspfNbrTable()
        self.ospfnbrtable.parent = self
        self.ospfstubareatable = OSPFMIB.OspfStubAreaTable()
        self.ospfstubareatable.parent = self
        self.ospfvirtiftable = OSPFMIB.OspfVirtIfTable()
        self.ospfvirtiftable.parent = self
        self.ospfvirtlocallsdbtable = OSPFMIB.OspfVirtLocalLsdbTable()
        self.ospfvirtlocallsdbtable.parent = self
        self.ospfvirtnbrtable = OSPFMIB.OspfVirtNbrTable()
        self.ospfvirtnbrtable.parent = self


    class OspfAreaAggregateTable(object):
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
        	**type**\: list of :py:class:`OspfAreaAggregateEntry <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfAreaAggregateTable.OspfAreaAggregateEntry>`
        
        

        """

        _prefix = 'ospf-mib'
        _revision = '2006-11-10'

        def __init__(self):
            self.parent = None
            self.ospfareaaggregateentry = YList()
            self.ospfareaaggregateentry.parent = self
            self.ospfareaaggregateentry.name = 'ospfareaaggregateentry'


        class OspfAreaAggregateEntry(object):
            """
            A single area aggregate entry.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            storage.
            
            .. attribute:: ospfareaaggregateareaid
            
            	The area within which the address aggregate is to be found
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfareaaggregatelsdbtype
            
            	The type of the address aggregate.  This field specifies the Lsdb type that this address aggregate applies to
            	**type**\: :py:class:`OspfAreaAggregateLsdbType_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfAreaAggregateTable.OspfAreaAggregateEntry.OspfAreaAggregateLsdbType_Enum>`
            
            .. attribute:: ospfareaaggregatemask
            
            	The subnet mask that pertains to the net or subnet
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfareaaggregatenet
            
            	The IP address of the net or subnet indicated by the range
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfareaaggregateeffect
            
            	Subnets subsumed by ranges either trigger the advertisement of the indicated aggregate (advertiseMatching) or result in the subnet's not being advertised at all outside the area
            	**type**\: :py:class:`OspfAreaAggregateEffect_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfAreaAggregateTable.OspfAreaAggregateEntry.OspfAreaAggregateEffect_Enum>`
            
            .. attribute:: ospfareaaggregateextroutetag
            
            	External route tag to be included in NSSA (type\-7) LSAs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfareaaggregatestatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'ospf-mib'
            _revision = '2006-11-10'

            def __init__(self):
                self.parent = None
                self.ospfareaaggregateareaid = None
                self.ospfareaaggregatelsdbtype = None
                self.ospfareaaggregatemask = None
                self.ospfareaaggregatenet = None
                self.ospfareaaggregateeffect = None
                self.ospfareaaggregateextroutetag = None
                self.ospfareaaggregatestatus = None

            class OspfAreaAggregateEffect_Enum(Enum):
                """
                OspfAreaAggregateEffect_Enum

                Subnets subsumed by ranges either trigger the
                advertisement of the indicated aggregate
                (advertiseMatching) or result in the subnet's not
                being advertised at all outside the area.

                """

                ADVERTISEMATCHING = 1

                DONOTADVERTISEMATCHING = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfAreaAggregateTable.OspfAreaAggregateEntry.OspfAreaAggregateEffect_Enum']


            class OspfAreaAggregateLsdbType_Enum(Enum):
                """
                OspfAreaAggregateLsdbType_Enum

                The type of the address aggregate.  This field
                specifies the Lsdb type that this address
                aggregate applies to.

                """

                SUMMARYLINK = 3

                NSSAEXTERNALLINK = 7


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfAreaAggregateTable.OspfAreaAggregateEntry.OspfAreaAggregateLsdbType_Enum']


            @property
            def _common_path(self):
                if self.ospfareaaggregateareaid is None:
                    raise YPYDataValidationError('Key property ospfareaaggregateareaid is None')
                if self.ospfareaaggregatelsdbtype is None:
                    raise YPYDataValidationError('Key property ospfareaaggregatelsdbtype is None')
                if self.ospfareaaggregatemask is None:
                    raise YPYDataValidationError('Key property ospfareaaggregatemask is None')
                if self.ospfareaaggregatenet is None:
                    raise YPYDataValidationError('Key property ospfareaaggregatenet is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfAreaAggregateTable/OSPF-MIB:ospfAreaAggregateEntry[OSPF-MIB:ospfAreaAggregateAreaID = ' + str(self.ospfareaaggregateareaid) + '][OSPF-MIB:ospfAreaAggregateLsdbType = ' + str(self.ospfareaaggregatelsdbtype) + '][OSPF-MIB:ospfAreaAggregateMask = ' + str(self.ospfareaaggregatemask) + '][OSPF-MIB:ospfAreaAggregateNet = ' + str(self.ospfareaaggregatenet) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ospfareaaggregateareaid is not None:
                    return True

                if self.ospfareaaggregatelsdbtype is not None:
                    return True

                if self.ospfareaaggregatemask is not None:
                    return True

                if self.ospfareaaggregatenet is not None:
                    return True

                if self.ospfareaaggregateeffect is not None:
                    return True

                if self.ospfareaaggregateextroutetag is not None:
                    return True

                if self.ospfareaaggregatestatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _OSPF_MIB as meta
                return meta._meta_table['OSPFMIB.OspfAreaAggregateTable.OspfAreaAggregateEntry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfAreaAggregateTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ospfareaaggregateentry is not None:
                for child_ref in self.ospfareaaggregateentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _OSPF_MIB as meta
            return meta._meta_table['OSPFMIB.OspfAreaAggregateTable']['meta_info']


    class OspfAreaLsaCountTable(object):
        """
        This table maintains per\-area, per\-LSA\-type counters
        
        .. attribute:: ospfarealsacountentry
        
        	An entry with a number of link advertisements  of a given type for a given area
        	**type**\: list of :py:class:`OspfAreaLsaCountEntry <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfAreaLsaCountTable.OspfAreaLsaCountEntry>`
        
        

        """

        _prefix = 'ospf-mib'
        _revision = '2006-11-10'

        def __init__(self):
            self.parent = None
            self.ospfarealsacountentry = YList()
            self.ospfarealsacountentry.parent = self
            self.ospfarealsacountentry.name = 'ospfarealsacountentry'


        class OspfAreaLsaCountEntry(object):
            """
            An entry with a number of link advertisements
            
            of a given type for a given area.
            
            .. attribute:: ospfarealsacountareaid
            
            	This entry Area ID
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfarealsacountlsatype
            
            	This entry LSA type
            	**type**\: :py:class:`OspfAreaLsaCountLsaType_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfAreaLsaCountTable.OspfAreaLsaCountEntry.OspfAreaLsaCountLsaType_Enum>`
            
            .. attribute:: ospfarealsacountnumber
            
            	Number of LSAs of a given type for a given area
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ospf-mib'
            _revision = '2006-11-10'

            def __init__(self):
                self.parent = None
                self.ospfarealsacountareaid = None
                self.ospfarealsacountlsatype = None
                self.ospfarealsacountnumber = None

            class OspfAreaLsaCountLsaType_Enum(Enum):
                """
                OspfAreaLsaCountLsaType_Enum

                This entry LSA type.

                """

                ROUTERLINK = 1

                NETWORKLINK = 2

                SUMMARYLINK = 3

                ASSUMMARYLINK = 4

                MULTICASTLINK = 6

                NSSAEXTERNALLINK = 7

                AREAOPAQUELINK = 10


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfAreaLsaCountTable.OspfAreaLsaCountEntry.OspfAreaLsaCountLsaType_Enum']


            @property
            def _common_path(self):
                if self.ospfarealsacountareaid is None:
                    raise YPYDataValidationError('Key property ospfarealsacountareaid is None')
                if self.ospfarealsacountlsatype is None:
                    raise YPYDataValidationError('Key property ospfarealsacountlsatype is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfAreaLsaCountTable/OSPF-MIB:ospfAreaLsaCountEntry[OSPF-MIB:ospfAreaLsaCountAreaId = ' + str(self.ospfarealsacountareaid) + '][OSPF-MIB:ospfAreaLsaCountLsaType = ' + str(self.ospfarealsacountlsatype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ospfarealsacountareaid is not None:
                    return True

                if self.ospfarealsacountlsatype is not None:
                    return True

                if self.ospfarealsacountnumber is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _OSPF_MIB as meta
                return meta._meta_table['OSPFMIB.OspfAreaLsaCountTable.OspfAreaLsaCountEntry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfAreaLsaCountTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ospfarealsacountentry is not None:
                for child_ref in self.ospfarealsacountentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _OSPF_MIB as meta
            return meta._meta_table['OSPFMIB.OspfAreaLsaCountTable']['meta_info']


    class OspfAreaRangeTable(object):
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
        	**type**\: list of :py:class:`OspfAreaRangeEntry <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfAreaRangeTable.OspfAreaRangeEntry>`
        
        

        """

        _prefix = 'ospf-mib'
        _revision = '2006-11-10'

        def __init__(self):
            self.parent = None
            self.ospfarearangeentry = YList()
            self.ospfarearangeentry.parent = self
            self.ospfarearangeentry.name = 'ospfarearangeentry'


        class OspfAreaRangeEntry(object):
            """
            A single area address range.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            storage.
            
            .. attribute:: ospfarearangeareaid
            
            	The area that the address range is to be found within
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfarearangenet
            
            	The IP address of the net or subnet indicated by the range
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfarearangeeffect
            
            	Subnets subsumed by ranges either trigger the advertisement of the indicated summary (advertiseMatching) or result in the subnet's not being advertised at all outside the area
            	**type**\: :py:class:`OspfAreaRangeEffect_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfAreaRangeTable.OspfAreaRangeEntry.OspfAreaRangeEffect_Enum>`
            
            .. attribute:: ospfarearangemask
            
            	The subnet mask that pertains to the net or subnet
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfarearangestatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'ospf-mib'
            _revision = '2006-11-10'

            def __init__(self):
                self.parent = None
                self.ospfarearangeareaid = None
                self.ospfarearangenet = None
                self.ospfarearangeeffect = None
                self.ospfarearangemask = None
                self.ospfarearangestatus = None

            class OspfAreaRangeEffect_Enum(Enum):
                """
                OspfAreaRangeEffect_Enum

                Subnets subsumed by ranges either trigger the
                advertisement of the indicated summary
                (advertiseMatching) or result in the subnet's not
                being advertised at all outside the area.

                """

                ADVERTISEMATCHING = 1

                DONOTADVERTISEMATCHING = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfAreaRangeTable.OspfAreaRangeEntry.OspfAreaRangeEffect_Enum']


            @property
            def _common_path(self):
                if self.ospfarearangeareaid is None:
                    raise YPYDataValidationError('Key property ospfarearangeareaid is None')
                if self.ospfarearangenet is None:
                    raise YPYDataValidationError('Key property ospfarearangenet is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfAreaRangeTable/OSPF-MIB:ospfAreaRangeEntry[OSPF-MIB:ospfAreaRangeAreaId = ' + str(self.ospfarearangeareaid) + '][OSPF-MIB:ospfAreaRangeNet = ' + str(self.ospfarearangenet) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _OSPF_MIB as meta
                return meta._meta_table['OSPFMIB.OspfAreaRangeTable.OspfAreaRangeEntry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfAreaRangeTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ospfarearangeentry is not None:
                for child_ref in self.ospfarearangeentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _OSPF_MIB as meta
            return meta._meta_table['OSPFMIB.OspfAreaRangeTable']['meta_info']


    class OspfAreaTable(object):
        """
        Information describing the configured parameters and
        cumulative statistics of the router's attached areas.
        The interfaces and virtual links are configured
        as part of these areas.  Area 0.0.0.0, by definition,
        is the backbone area.
        
        .. attribute:: ospfareaentry
        
        	Information describing the configured parameters and cumulative statistics of one of the router's attached areas. The interfaces and virtual links are configured as part of these areas.  Area 0.0.0.0, by definition, is the backbone area.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile storage
        	**type**\: list of :py:class:`OspfAreaEntry <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfAreaTable.OspfAreaEntry>`
        
        

        """

        _prefix = 'ospf-mib'
        _revision = '2006-11-10'

        def __init__(self):
            self.parent = None
            self.ospfareaentry = YList()
            self.ospfareaentry.parent = self
            self.ospfareaentry.name = 'ospfareaentry'


        class OspfAreaEntry(object):
            """
            Information describing the configured parameters and
            cumulative statistics of one of the router's attached areas.
            The interfaces and virtual links are configured as part of
            these areas.  Area 0.0.0.0, by definition, is the backbone
            area.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            storage.
            
            .. attribute:: ospfareaid
            
            	A 32\-bit integer uniquely identifying an area. Area ID 0.0.0.0 is used for the OSPF backbone
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfareanssatranslatorevents
            
            	Indicates the number of Translator State changes that have occurred since the last boot\-up
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfareanssatranslatorrole
            
            	Indicates an NSSA Border router's ability to perform NSSA translation of type\-7 LSAs into type\-5 LSAs
            	**type**\: :py:class:`CospfAreaNssaTranslatorRole_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfAreaTable.OspfAreaEntry.CospfAreaNssaTranslatorRole_Enum>`
            
            .. attribute:: cospfareanssatranslatorstate
            
            	Indicates if and how an NSSA Border router is performing NSSA translation of type\-7 LSAs into type\-5 LSAs. When this object set to enabled, the NSSA Border router's cospfAreaNssaExtTranslatorRole has been set to always. When this object is set to elected, a candidate NSSA Border router is Translating type\-7 LSAs into type\-5. When this object is set to disabled, a candidate NSSA Border router is NOT translating type\-7 LSAs into type\-5
            	**type**\: :py:class:`CospfAreaNssaTranslatorState_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfAreaTable.OspfAreaEntry.CospfAreaNssaTranslatorState_Enum>`
            
            .. attribute:: cospfopaquearealsacksumsum
            
            	The 32\-bit unsigned sum of the Opaque Area and AS  link\-state advertisements' LS checksums contained  link state database of this area.  The sum can be  used to determine if there has been a change in the  link state database for Opaque Area and AS link\-state advertisements
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfopaquearealsacount
            
            	The total number of Opaque Area and AS link\-state  advertisements in the link state database of this area
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfareabdrrtrcount
            
            	The total number of Area Border Routers reachable within this area.  This is initially zero and is calculated in each Shortest Path First (SPF) pass
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfarealsacksumsum
            
            	The 32\-bit sum of the link state advertisements' LS checksums contained in this area's link state database.  This sum excludes external (LS type\-5) link state advertisements. The sum can be used to determine if there has been a change in a router's link state database, and to compare the link state database of two routers.  The value should be treated as unsigned when comparing two sums of checksums
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospfarealsacount
            
            	The total number of link state advertisements in this area's link state database, excluding AS\-external LSAs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfareanssatranslatorevents
            
            	Indicates the number of translator state changes that have occurred since the last boot\-up.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ospfDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfareanssatranslatorrole
            
            	Indicates an NSSA border router's ability to perform NSSA translation of type\-7 LSAs into type\-5 LSAs
            	**type**\: :py:class:`OspfAreaNssaTranslatorRole_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfAreaTable.OspfAreaEntry.OspfAreaNssaTranslatorRole_Enum>`
            
            .. attribute:: ospfareanssatranslatorstabilityinterval
            
            	The number of seconds after an elected translator determines its services are no longer required, that it should continue to perform its translation duties
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ospfareanssatranslatorstate
            
            	Indicates if and how an NSSA border router is performing NSSA translation of type\-7 LSAs into type\-5  LSAs.  When this object is set to enabled, the NSSA Border router's OspfAreaNssaExtTranslatorRole has been set to always.  When this object is set to elected, a candidate NSSA Border router is Translating type\-7 LSAs into type\-5. When this object is set to disabled, a candidate NSSA border router is NOT translating type\-7 LSAs into type\-5
            	**type**\: :py:class:`OspfAreaNssaTranslatorState_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfAreaTable.OspfAreaEntry.OspfAreaNssaTranslatorState_Enum>`
            
            .. attribute:: ospfareastatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: ospfareasummary
            
            	The variable ospfAreaSummary controls the import of summary LSAs into stub and NSSA areas. It has no effect on other areas.  If it is noAreaSummary, the router will not originate summary LSAs into the stub or NSSA area. It will rely entirely on its default route.  If it is sendAreaSummary, the router will both summarize and propagate summary LSAs
            	**type**\: :py:class:`OspfAreaSummary_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfAreaTable.OspfAreaEntry.OspfAreaSummary_Enum>`
            
            .. attribute:: ospfasbdrrtrcount
            
            	The total number of Autonomous System Border Routers reachable within this area.  This is initially zero and is calculated in each SPF pass
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfauthtype
            
            	The authentication type specified for an area
            	**type**\: :py:class:`OspfAuthenticationType_Enum <ydk.models.ospf.OSPF_MIB.OspfAuthenticationType_Enum>`
            
            .. attribute:: ospfimportasextern
            
            	Indicates if an area is a stub area, NSSA, or standard area.  Type\-5 AS\-external LSAs and type\-11 Opaque LSAs are not imported into stub areas or NSSAs.  NSSAs import AS\-external data as type\-7 LSAs
            	**type**\: :py:class:`OspfImportAsExtern_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfAreaTable.OspfAreaEntry.OspfImportAsExtern_Enum>`
            
            .. attribute:: ospfspfruns
            
            	The number of times that the intra\-area route table has been calculated using this area's link state database.  This is typically done using Dijkstra's algorithm.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ospfDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ospf-mib'
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

            class CospfAreaNssaTranslatorRole_Enum(Enum):
                """
                CospfAreaNssaTranslatorRole_Enum

                Indicates an NSSA Border router's ability to
                perform NSSA translation of type\-7 LSAs into
                type\-5 LSAs.

                """

                ALWAYS = 1

                CANDIDATE = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfAreaTable.OspfAreaEntry.CospfAreaNssaTranslatorRole_Enum']


            class CospfAreaNssaTranslatorState_Enum(Enum):
                """
                CospfAreaNssaTranslatorState_Enum

                Indicates if and how an NSSA Border router is
                performing NSSA translation of type\-7 LSAs into type\-5
                LSAs. When this object set to enabled, the NSSA Border
                router's cospfAreaNssaExtTranslatorRole has been set to
                always. When this object is set to elected, a candidate
                NSSA Border router is Translating type\-7 LSAs into type\-5.
                When this object is set to disabled, a candidate NSSA
                Border router is NOT translating type\-7 LSAs into type\-5.

                """

                ENABLED = 1

                ELECTED = 2

                DISABLED = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfAreaTable.OspfAreaEntry.CospfAreaNssaTranslatorState_Enum']


            class OspfAreaNssaTranslatorRole_Enum(Enum):
                """
                OspfAreaNssaTranslatorRole_Enum

                Indicates an NSSA border router's ability to
                perform NSSA translation of type\-7 LSAs into
                type\-5 LSAs.

                """

                ALWAYS = 1

                CANDIDATE = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfAreaTable.OspfAreaEntry.OspfAreaNssaTranslatorRole_Enum']


            class OspfAreaNssaTranslatorState_Enum(Enum):
                """
                OspfAreaNssaTranslatorState_Enum

                Indicates if and how an NSSA border router is
                performing NSSA translation of type\-7 LSAs into type\-5
                
                LSAs.  When this object is set to enabled, the NSSA Border
                router's OspfAreaNssaExtTranslatorRole has been set to
                always.  When this object is set to elected, a candidate
                NSSA Border router is Translating type\-7 LSAs into type\-5.
                When this object is set to disabled, a candidate NSSA
                border router is NOT translating type\-7 LSAs into type\-5.

                """

                ENABLED = 1

                ELECTED = 2

                DISABLED = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfAreaTable.OspfAreaEntry.OspfAreaNssaTranslatorState_Enum']


            class OspfAreaSummary_Enum(Enum):
                """
                OspfAreaSummary_Enum

                The variable ospfAreaSummary controls the
                import of summary LSAs into stub and NSSA areas.
                It has no effect on other areas.
                
                If it is noAreaSummary, the router will not
                originate summary LSAs into the stub or NSSA area.
                It will rely entirely on its default route.
                
                If it is sendAreaSummary, the router will both
                summarize and propagate summary LSAs.

                """

                NOAREASUMMARY = 1

                SENDAREASUMMARY = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfAreaTable.OspfAreaEntry.OspfAreaSummary_Enum']


            class OspfImportAsExtern_Enum(Enum):
                """
                OspfImportAsExtern_Enum

                Indicates if an area is a stub area, NSSA, or standard
                area.  Type\-5 AS\-external LSAs and type\-11 Opaque LSAs are
                not imported into stub areas or NSSAs.  NSSAs import
                AS\-external data as type\-7 LSAs

                """

                IMPORTEXTERNAL = 1

                IMPORTNOEXTERNAL = 2

                IMPORTNSSA = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfAreaTable.OspfAreaEntry.OspfImportAsExtern_Enum']


            @property
            def _common_path(self):
                if self.ospfareaid is None:
                    raise YPYDataValidationError('Key property ospfareaid is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfAreaTable/OSPF-MIB:ospfAreaEntry[OSPF-MIB:ospfAreaId = ' + str(self.ospfareaid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _OSPF_MIB as meta
                return meta._meta_table['OSPFMIB.OspfAreaTable.OspfAreaEntry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfAreaTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ospfareaentry is not None:
                for child_ref in self.ospfareaentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _OSPF_MIB as meta
            return meta._meta_table['OSPFMIB.OspfAreaTable']['meta_info']


    class OspfAsLsdbTable(object):
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
        	**type**\: list of :py:class:`OspfAsLsdbEntry <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfAsLsdbTable.OspfAsLsdbEntry>`
        
        

        """

        _prefix = 'ospf-mib'
        _revision = '2006-11-10'

        def __init__(self):
            self.parent = None
            self.ospfaslsdbentry = YList()
            self.ospfaslsdbentry.parent = self
            self.ospfaslsdbentry.name = 'ospfaslsdbentry'


        class OspfAsLsdbEntry(object):
            """
            A single link state advertisement.
            
            .. attribute:: ospfaslsdblsid
            
            	The Link State ID is an LS Type Specific field containing either a Router ID or an IP address;  it identifies the piece of the routing domain that is being described by the advertisement
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfaslsdbrouterid
            
            	The 32\-bit number that uniquely identifies the originating router in the Autonomous System
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfaslsdbtype
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\: :py:class:`OspfAsLsdbType_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfAsLsdbTable.OspfAsLsdbEntry.OspfAsLsdbType_Enum>`
            
            .. attribute:: ospfaslsdbadvertisement
            
            	The entire link state advertisement, including its header
            	**type**\: str
            
            	**range:** 1..65535
            
            .. attribute:: ospfaslsdbage
            
            	This field is the age of the link state advertisement in seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospfaslsdbchecksum
            
            	This field is the checksum of the complete contents of the advertisement, excepting the age field.  The age field is excepted so that an advertisement's age can be incremented without updating the checksum.  The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred to as the Fletcher checksum
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospfaslsdbsequence
            
            	The sequence number field is a signed 32\-bit integer.  It starts with the value '80000001'h, or \-'7FFFFFFF'h, and increments until '7FFFFFFF'h. Thus, a typical sequence number will be very negative. It is used to detect old and duplicate link state advertisements.  The space of sequence numbers is linearly ordered.  The larger the sequence number, the more recent the advertisement
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'ospf-mib'
            _revision = '2006-11-10'

            def __init__(self):
                self.parent = None
                self.ospfaslsdblsid = None
                self.ospfaslsdbrouterid = None
                self.ospfaslsdbtype = None
                self.ospfaslsdbadvertisement = None
                self.ospfaslsdbage = None
                self.ospfaslsdbchecksum = None
                self.ospfaslsdbsequence = None

            class OspfAsLsdbType_Enum(Enum):
                """
                OspfAsLsdbType_Enum

                The type of the link state advertisement.
                Each link state type has a separate
                advertisement format.

                """

                ASEXTERNALLINK = 5

                ASOPAQUELINK = 11


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfAsLsdbTable.OspfAsLsdbEntry.OspfAsLsdbType_Enum']


            @property
            def _common_path(self):
                if self.ospfaslsdblsid is None:
                    raise YPYDataValidationError('Key property ospfaslsdblsid is None')
                if self.ospfaslsdbrouterid is None:
                    raise YPYDataValidationError('Key property ospfaslsdbrouterid is None')
                if self.ospfaslsdbtype is None:
                    raise YPYDataValidationError('Key property ospfaslsdbtype is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfAsLsdbTable/OSPF-MIB:ospfAsLsdbEntry[OSPF-MIB:ospfAsLsdbLsid = ' + str(self.ospfaslsdblsid) + '][OSPF-MIB:ospfAsLsdbRouterId = ' + str(self.ospfaslsdbrouterid) + '][OSPF-MIB:ospfAsLsdbType = ' + str(self.ospfaslsdbtype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ospfaslsdblsid is not None:
                    return True

                if self.ospfaslsdbrouterid is not None:
                    return True

                if self.ospfaslsdbtype is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _OSPF_MIB as meta
                return meta._meta_table['OSPFMIB.OspfAsLsdbTable.OspfAsLsdbEntry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfAsLsdbTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ospfaslsdbentry is not None:
                for child_ref in self.ospfaslsdbentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _OSPF_MIB as meta
            return meta._meta_table['OSPFMIB.OspfAsLsdbTable']['meta_info']


    class OspfExtLsdbTable(object):
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
        	**type**\: list of :py:class:`OspfExtLsdbEntry <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfExtLsdbTable.OspfExtLsdbEntry>`
        
        

        """

        _prefix = 'ospf-mib'
        _revision = '2006-11-10'

        def __init__(self):
            self.parent = None
            self.ospfextlsdbentry = YList()
            self.ospfextlsdbentry.parent = self
            self.ospfextlsdbentry.name = 'ospfextlsdbentry'


        class OspfExtLsdbEntry(object):
            """
            A single link state advertisement.
            
            .. attribute:: ospfextlsdblsid
            
            	The Link State ID is an LS Type Specific field containing either a Router ID or an IP address; it identifies the piece of the routing domain that is being described by the advertisement
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfextlsdbrouterid
            
            	The 32\-bit number that uniquely identifies the originating router in the Autonomous System
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfextlsdbtype
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\: :py:class:`OspfExtLsdbType_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfExtLsdbTable.OspfExtLsdbEntry.OspfExtLsdbType_Enum>`
            
            .. attribute:: ospfextlsdbadvertisement
            
            	The entire link state advertisement, including its header
            	**type**\: str
            
            	**range:** 36
            
            .. attribute:: ospfextlsdbage
            
            	This field is the age of the link state advertisement in seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospfextlsdbchecksum
            
            	This field is the checksum of the complete contents of the advertisement, excepting the age field.  The age field is excepted so that an advertisement's age can be incremented without updating the checksum.  The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred to as the Fletcher checksum
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospfextlsdbsequence
            
            	The sequence number field is a signed 32\-bit integer.  It starts with the value '80000001'h, or \-'7FFFFFFF'h, and increments until '7FFFFFFF'h. Thus, a typical sequence number will be very negative. It is used to detect old and duplicate link state advertisements.  The space of sequence numbers is linearly ordered.  The larger the sequence number, the more recent the advertisement
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'ospf-mib'
            _revision = '2006-11-10'

            def __init__(self):
                self.parent = None
                self.ospfextlsdblsid = None
                self.ospfextlsdbrouterid = None
                self.ospfextlsdbtype = None
                self.ospfextlsdbadvertisement = None
                self.ospfextlsdbage = None
                self.ospfextlsdbchecksum = None
                self.ospfextlsdbsequence = None

            class OspfExtLsdbType_Enum(Enum):
                """
                OspfExtLsdbType_Enum

                The type of the link state advertisement.
                Each link state type has a separate advertisement
                format.

                """

                ASEXTERNALLINK = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfExtLsdbTable.OspfExtLsdbEntry.OspfExtLsdbType_Enum']


            @property
            def _common_path(self):
                if self.ospfextlsdblsid is None:
                    raise YPYDataValidationError('Key property ospfextlsdblsid is None')
                if self.ospfextlsdbrouterid is None:
                    raise YPYDataValidationError('Key property ospfextlsdbrouterid is None')
                if self.ospfextlsdbtype is None:
                    raise YPYDataValidationError('Key property ospfextlsdbtype is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfExtLsdbTable/OSPF-MIB:ospfExtLsdbEntry[OSPF-MIB:ospfExtLsdbLsid = ' + str(self.ospfextlsdblsid) + '][OSPF-MIB:ospfExtLsdbRouterId = ' + str(self.ospfextlsdbrouterid) + '][OSPF-MIB:ospfExtLsdbType = ' + str(self.ospfextlsdbtype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ospfextlsdblsid is not None:
                    return True

                if self.ospfextlsdbrouterid is not None:
                    return True

                if self.ospfextlsdbtype is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _OSPF_MIB as meta
                return meta._meta_table['OSPFMIB.OspfExtLsdbTable.OspfExtLsdbEntry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfExtLsdbTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ospfextlsdbentry is not None:
                for child_ref in self.ospfextlsdbentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _OSPF_MIB as meta
            return meta._meta_table['OSPFMIB.OspfExtLsdbTable']['meta_info']


    class OspfGeneralGroup(object):
        """
        
        
        .. attribute:: ospfadminstat
        
        	The administrative status of OSPF in the router.  The value 'enabled' denotes that the OSPF Process is active on at least one interface; 'disabled' disables it on all interfaces.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\: :py:class:`Status_Enum <ydk.models.ospf.OSPF_MIB.Status_Enum>`
        
        .. attribute:: ospfareabdrrtrstatus
        
        	A flag to note whether this router is an Area Border Router
        	**type**\: bool
        
        .. attribute:: ospfasbdrrtrstatus
        
        	A flag to note whether this router is configured as an Autonomous System Border Router.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\: bool
        
        .. attribute:: ospfaslsacksumsum
        
        	The 32\-bit unsigned sum of the LS checksums of the AS link state advertisements contained in the AS\-scope link state database.  This sum can be used to determine if there has been a change in a router's AS\-scope link state database, and to compare the AS\-scope link state database of two routers
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ospfaslsacount
        
        	The number of AS\-scope link state advertisements in the AS\-scope link state database
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ospfdemandextensions
        
        	The router's support for demand routing. This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\: bool
        
        .. attribute:: ospfdiscontinuitytime
        
        	The value of sysUpTime on the most recent occasion at which any one of this MIB's counters suffered a discontinuity.  If no such discontinuities have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ospfexitoverflowinterval
        
        	The number of seconds that, after entering OverflowState, a router will attempt to leave OverflowState.  This allows the router to again originate non\-default AS\-external LSAs.  When set to 0, the router will not leave overflow state until restarted.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: ospfexternlsacksumsum
        
        	The 32\-bit sum of the LS checksums of the external link state advertisements contained in the link state database.  This sum can be used to determine if there has been a change in a router's link state database and to compare the link state database of two routers.  The value should be treated as unsigned when comparing two sums of checksums
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: ospfexternlsacount
        
        	The number of external (LS type\-5) link state advertisements in the link state database
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
        
        .. attribute:: ospfopaquelsasupport
        
        	The router's support for Opaque LSA types
        	**type**\: bool
        
        .. attribute:: ospforiginatenewlsas
        
        	The number of new link state advertisements that have been originated.  This number is incremented each time the router originates a new LSA.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ospfDiscontinuityTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ospfreferencebandwidth
        
        	Reference bandwidth in kilobits/second for  calculating default interface metrics.  The default value is 100,000 KBPS (100 MBPS).  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ospfrestartage
        
        	Remaining time in current OSPF graceful restart interval
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ospfrestartexitreason
        
        	Describes the outcome of the last attempt at a graceful restart.  If the value is 'none', no restart has yet been attempted.  If the value is 'inProgress', a restart attempt is currently underway
        	**type**\: :py:class:`OspfRestartExitReason_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfGeneralGroup.OspfRestartExitReason_Enum>`
        
        .. attribute:: ospfrestartinterval
        
        	Configured OSPF graceful restart timeout interval.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\: int
        
        	**range:** 1..1800
        
        .. attribute:: ospfrestartstatus
        
        	Current status of OSPF graceful restart
        	**type**\: :py:class:`OspfRestartStatus_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfGeneralGroup.OspfRestartStatus_Enum>`
        
        .. attribute:: ospfrestartstrictlsachecking
        
        	Indicates if strict LSA checking is enabled for graceful restart.  This object is persistent and when written the entity SHOULD save the change to non\-volatile  storage
        	**type**\: bool
        
        .. attribute:: ospfrestartsupport
        
        	The router's support for OSPF graceful restart. Options include\: no restart support, only planned restarts, or both planned and unplanned restarts.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\: :py:class:`OspfRestartSupport_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfGeneralGroup.OspfRestartSupport_Enum>`
        
        .. attribute:: ospfrfc1583compatibility
        
        	Indicates metrics used to choose among multiple AS\-external LSAs.  When RFC1583Compatibility is set to enabled, only cost will be used when choosing among multiple AS\-external LSAs advertising the same destination.  When RFC1583Compatibility is set to disabled, preference will be driven first by type of path using cost only to break ties.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\: bool
        
        .. attribute:: ospfrouterid
        
        	A 32\-bit integer uniquely identifying the router in the Autonomous System. By convention, to ensure uniqueness, this should default to the value of one of the router's IP interface addresses.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: ospfrxnewlsas
        
        	The number of link state advertisements received that are determined to be new instantiations. This number does not include newer instantiations of self\-originated link state advertisements.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ospfDiscontinuityTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ospfstubrouteradvertisement
        
        	This object controls the advertisement of stub router LSAs by the router.  The value doNotAdvertise will result in the advertisement of a standard router LSA and is the default value.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\: :py:class:`OspfStubRouterAdvertisement_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfGeneralGroup.OspfStubRouterAdvertisement_Enum>`
        
        .. attribute:: ospfstubroutersupport
        
        	The router's support for stub router functionality
        	**type**\: bool
        
        .. attribute:: ospftossupport
        
        	The router's support for type\-of\-service routing.  This object is persistent and when written the entity SHOULD save the change to non\-volatile storage
        	**type**\: bool
        
        .. attribute:: ospfversionnumber
        
        	The current version number of the OSPF protocol is 2
        	**type**\: :py:class:`OspfVersionNumber_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfGeneralGroup.OspfVersionNumber_Enum>`
        
        

        """

        _prefix = 'ospf-mib'
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

        class OspfRestartExitReason_Enum(Enum):
            """
            OspfRestartExitReason_Enum

            Describes the outcome of the last attempt at a
            graceful restart.  If the value is 'none', no restart
            has yet been attempted.  If the value is 'inProgress',
            a restart attempt is currently underway.

            """

            NONE = 1

            INPROGRESS = 2

            COMPLETED = 3

            TIMEDOUT = 4

            TOPOLOGYCHANGED = 5


            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _OSPF_MIB as meta
                return meta._meta_table['OSPFMIB.OspfGeneralGroup.OspfRestartExitReason_Enum']


        class OspfRestartStatus_Enum(Enum):
            """
            OspfRestartStatus_Enum

            Current status of OSPF graceful restart.

            """

            NOTRESTARTING = 1

            PLANNEDRESTART = 2

            UNPLANNEDRESTART = 3


            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _OSPF_MIB as meta
                return meta._meta_table['OSPFMIB.OspfGeneralGroup.OspfRestartStatus_Enum']


        class OspfRestartSupport_Enum(Enum):
            """
            OspfRestartSupport_Enum

            The router's support for OSPF graceful restart.
            Options include\: no restart support, only planned
            restarts, or both planned and unplanned restarts.
            
            This object is persistent and when written
            the entity SHOULD save the change to non\-volatile
            storage.

            """

            NONE = 1

            PLANNEDONLY = 2

            PLANNEDANDUNPLANNED = 3


            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _OSPF_MIB as meta
                return meta._meta_table['OSPFMIB.OspfGeneralGroup.OspfRestartSupport_Enum']


        class OspfStubRouterAdvertisement_Enum(Enum):
            """
            OspfStubRouterAdvertisement_Enum

            This object controls the advertisement of
            stub router LSAs by the router.  The value
            doNotAdvertise will result in the advertisement
            of a standard router LSA and is the default value.
            
            This object is persistent and when written
            the entity SHOULD save the change to non\-volatile
            storage.

            """

            DONOTADVERTISE = 1

            ADVERTISE = 2


            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _OSPF_MIB as meta
                return meta._meta_table['OSPFMIB.OspfGeneralGroup.OspfStubRouterAdvertisement_Enum']


        class OspfVersionNumber_Enum(Enum):
            """
            OspfVersionNumber_Enum

            The current version number of the OSPF protocol is 2.

            """

            VERSION2 = 2


            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _OSPF_MIB as meta
                return meta._meta_table['OSPFMIB.OspfGeneralGroup.OspfVersionNumber_Enum']


        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfGeneralGroup'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
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

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _OSPF_MIB as meta
            return meta._meta_table['OSPFMIB.OspfGeneralGroup']['meta_info']


    class OspfHostTable(object):
        """
        The Host/Metric Table indicates what hosts are directly
        
        attached to the router, what metrics and types
        of service should be advertised for them,
        and what areas they are found within.
        
        .. attribute:: ospfhostentry
        
        	A metric to be advertised, for a given type of service, when a given host is reachable.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile storage
        	**type**\: list of :py:class:`OspfHostEntry <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfHostTable.OspfHostEntry>`
        
        

        """

        _prefix = 'ospf-mib'
        _revision = '2006-11-10'

        def __init__(self):
            self.parent = None
            self.ospfhostentry = YList()
            self.ospfhostentry.parent = self
            self.ospfhostentry.name = 'ospfhostentry'


        class OspfHostEntry(object):
            """
            A metric to be advertised, for a given type of
            service, when a given host is reachable.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            storage.
            
            .. attribute:: ospfhostipaddress
            
            	The IP address of the host
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfhosttos
            
            	The Type of Service of the route being configured
            	**type**\: int
            
            	**range:** 0..30
            
            .. attribute:: ospfhostareaid
            
            	The OSPF area to which the host belongs. Deprecated by ospfHostCfgAreaID
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfhostcfgareaid
            
            	To configure the OSPF area to which the host belongs
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfhostmetric
            
            	The metric to be advertised
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: ospfhoststatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'ospf-mib'
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
                    raise YPYDataValidationError('Key property ospfhostipaddress is None')
                if self.ospfhosttos is None:
                    raise YPYDataValidationError('Key property ospfhosttos is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfHostTable/OSPF-MIB:ospfHostEntry[OSPF-MIB:ospfHostIpAddress = ' + str(self.ospfhostipaddress) + '][OSPF-MIB:ospfHostTOS = ' + str(self.ospfhosttos) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _OSPF_MIB as meta
                return meta._meta_table['OSPFMIB.OspfHostTable.OspfHostEntry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfHostTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ospfhostentry is not None:
                for child_ref in self.ospfhostentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _OSPF_MIB as meta
            return meta._meta_table['OSPFMIB.OspfHostTable']['meta_info']


    class OspfIfMetricTable(object):
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
        	**type**\: list of :py:class:`OspfIfMetricEntry <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfIfMetricTable.OspfIfMetricEntry>`
        
        

        """

        _prefix = 'ospf-mib'
        _revision = '2006-11-10'

        def __init__(self):
            self.parent = None
            self.ospfifmetricentry = YList()
            self.ospfifmetricentry.parent = self
            self.ospfifmetricentry.name = 'ospfifmetricentry'


        class OspfIfMetricEntry(object):
            """
            A particular TOS metric for a non\-virtual interface
            identified by the interface index.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            storage.
            
            .. attribute:: ospfifmetricaddresslessif
            
            	For the purpose of easing the instancing of addressed and addressless interfaces; this variable takes the value 0 on interfaces with IP addresses and the value of ifIndex for interfaces having no IP address.  On row creation, this can be derived from the instance
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ospfifmetricipaddress
            
            	The IP address of this OSPF interface.  On row creation, this can be derived from the instance
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfifmetrictos
            
            	The Type of Service metric being referenced. On row creation, this can be derived from the instance
            	**type**\: int
            
            	**range:** 0..30
            
            .. attribute:: ospfifmetricstatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: ospfifmetricvalue
            
            	The metric of using this Type of Service on this interface.  The default value of the TOS 0 metric is 10^8 / ifSpeed
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'ospf-mib'
            _revision = '2006-11-10'

            def __init__(self):
                self.parent = None
                self.ospfifmetricaddresslessif = None
                self.ospfifmetricipaddress = None
                self.ospfifmetrictos = None
                self.ospfifmetricstatus = None
                self.ospfifmetricvalue = None

            @property
            def _common_path(self):
                if self.ospfifmetricaddresslessif is None:
                    raise YPYDataValidationError('Key property ospfifmetricaddresslessif is None')
                if self.ospfifmetricipaddress is None:
                    raise YPYDataValidationError('Key property ospfifmetricipaddress is None')
                if self.ospfifmetrictos is None:
                    raise YPYDataValidationError('Key property ospfifmetrictos is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfIfMetricTable/OSPF-MIB:ospfIfMetricEntry[OSPF-MIB:ospfIfMetricAddressLessIf = ' + str(self.ospfifmetricaddresslessif) + '][OSPF-MIB:ospfIfMetricIpAddress = ' + str(self.ospfifmetricipaddress) + '][OSPF-MIB:ospfIfMetricTOS = ' + str(self.ospfifmetrictos) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ospfifmetricaddresslessif is not None:
                    return True

                if self.ospfifmetricipaddress is not None:
                    return True

                if self.ospfifmetrictos is not None:
                    return True

                if self.ospfifmetricstatus is not None:
                    return True

                if self.ospfifmetricvalue is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _OSPF_MIB as meta
                return meta._meta_table['OSPFMIB.OspfIfMetricTable.OspfIfMetricEntry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfIfMetricTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ospfifmetricentry is not None:
                for child_ref in self.ospfifmetricentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _OSPF_MIB as meta
            return meta._meta_table['OSPFMIB.OspfIfMetricTable']['meta_info']


    class OspfIfTable(object):
        """
        The OSPF Interface Table describes the interfaces
        from the viewpoint of OSPF.
        It augments the ipAddrTable with OSPF specific information.
        
        .. attribute:: ospfifentry
        
        	The OSPF interface entry describes one interface from the viewpoint of OSPF.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile storage
        	**type**\: list of :py:class:`OspfIfEntry <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfIfTable.OspfIfEntry>`
        
        

        """

        _prefix = 'ospf-mib'
        _revision = '2006-11-10'

        def __init__(self):
            self.parent = None
            self.ospfifentry = YList()
            self.ospfifentry.parent = self
            self.ospfifentry.name = 'ospfifentry'


        class OspfIfEntry(object):
            """
            The OSPF interface entry describes one interface
            from the viewpoint of OSPF.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            storage.
            
            .. attribute:: ospfaddresslessif
            
            	For the purpose of easing the instancing of addressed and addressless interfaces; this variable takes the value 0 on interfaces with IP addresses and the corresponding value of ifIndex for interfaces having no IP address
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ospfifipaddress
            
            	The IP address of this OSPF interface
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfiflsacksumsum
            
            	The 32\-bit unsigned sum of the link\-state advertisements' LS checksums contained in this interface's link\-local link  state database. The sum can be used to determine if there has been a change in the interface's link state database, and to compare the interface link\-state database of routers  attached to the same subnet
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfiflsacount
            
            	The total number of link\-local link state advertisements in this interface's link\-local link state database
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfifadminstat
            
            	The OSPF interface's administrative status. The value formed on the interface, and the interface will be advertised as an internal route to some area. The value 'disabled' denotes that the interface is external to OSPF
            	**type**\: :py:class:`Status_Enum <ydk.models.ospf.OSPF_MIB.Status_Enum>`
            
            .. attribute:: ospfifareaid
            
            	A 32\-bit integer uniquely identifying the area to which the interface connects.  Area ID 0.0.0.0 is used for the OSPF backbone
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfifauthkey
            
            	The cleartext password used as an OSPF authentication key when simplePassword security is enabled.  This object does not access any OSPF cryptogaphic (e.g., MD5) authentication key under any circumstance.  If the key length is shorter than 8 octets, the agent will left adjust and zero fill to 8 octets.  Unauthenticated interfaces need no authentication key, and simple password authentication cannot use a key of more than 8 octets.  Note that the use of simplePassword authentication is NOT recommended when there is concern regarding attack upon the OSPF system.  SimplePassword authentication is only sufficient to protect against accidental misconfigurations because it re\-uses cleartext passwords [RFC1704].  When read, ospfIfAuthKey always returns an octet string of length zero
            	**type**\: str
            
            	**range:** 0..256
            
            .. attribute:: ospfifauthtype
            
            	The authentication type specified for an interface.  Note that this object can be used to engage in significant attacks against an OSPF router
            	**type**\: :py:class:`OspfAuthenticationType_Enum <ydk.models.ospf.OSPF_MIB.OspfAuthenticationType_Enum>`
            
            .. attribute:: ospfifbackupdesignatedrouter
            
            	The IP address of the backup designated router
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfifbackupdesignatedrouterid
            
            	The Router ID of the backup designated router
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfifdemand
            
            	Indicates whether Demand OSPF procedures (hello suppression to FULL neighbors and setting the DoNotAge flag on propagated LSAs) should be performed on this interface
            	**type**\: bool
            
            .. attribute:: ospfifdesignatedrouter
            
            	The IP address of the designated router
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfifdesignatedrouterid
            
            	The Router ID of the designated router
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfifevents
            
            	The number of times this OSPF interface has changed its state or an error has occurred.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ospfDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfifhellointerval
            
            	The length of time, in seconds, between the Hello packets that the router sends on the interface.  This value must be the same for all routers attached to a common network
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: ospfiflsacksumsum
            
            	The 32\-bit unsigned sum of the Link State Advertisements' LS checksums contained in this interface's link\-local link state database. The sum can be used to determine if there has been a change in the interface's link state database and to compare the interface link state database of routers attached to the same subnet
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfiflsacount
            
            	The total number of link\-local link state advertisements in this interface's link\-local link state database
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfifmulticastforwarding
            
            	The way multicasts should be forwarded on this interface\: not forwarded, forwarded as data link multicasts, or forwarded as data link unicasts.  Data link multicasting is not meaningful on point\-to\-point and NBMA interfaces, and setting ospfMulticastForwarding to 0 effectively disables all multicast forwarding
            	**type**\: :py:class:`OspfIfMulticastForwarding_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfIfTable.OspfIfEntry.OspfIfMulticastForwarding_Enum>`
            
            .. attribute:: ospfifpollinterval
            
            	The larger time interval, in seconds, between the Hello packets sent to an inactive non\-broadcast multi\-access neighbor
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ospfifretransinterval
            
            	The number of seconds between link state advertisement retransmissions, for adjacencies belonging to this interface.  This value is also used when retransmitting  database description and Link State request packets. Note that minimal value SHOULD be 1 second
            	**type**\: int
            
            	**range:** 0..3600
            
            .. attribute:: ospfifrtrdeadinterval
            
            	The number of seconds that a router's Hello packets have not been seen before its neighbors declare the router down. This should be some multiple of the Hello interval.  This value must be the same for all routers attached to a common network
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ospfifrtrpriority
            
            	The priority of this interface.  Used in multi\-access networks, this field is used in the designated router election algorithm.  The value 0 signifies that the router is not eligible to become the designated router on this particular network.  In the event of a tie in this value, routers will use their Router ID as a tie breaker
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: ospfifstate
            
            	The OSPF Interface State
            	**type**\: :py:class:`OspfIfState_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfIfTable.OspfIfEntry.OspfIfState_Enum>`
            
            .. attribute:: ospfifstatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: ospfiftransitdelay
            
            	The estimated number of seconds it takes to transmit a link state update packet over this interface.  Note that the minimal value SHOULD be 1 second
            	**type**\: int
            
            	**range:** 0..3600
            
            .. attribute:: ospfiftype
            
            	The OSPF interface type. By way of a default, this field may be intuited from the corresponding value of ifType. Broadcast LANs, such as Ethernet and IEEE 802.5, take the value 'broadcast', X.25 and similar technologies take the value 'nbma', and links that are definitively point to point take the value 'pointToPoint'
            	**type**\: :py:class:`OspfIfType_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfIfTable.OspfIfEntry.OspfIfType_Enum>`
            
            

            """

            _prefix = 'ospf-mib'
            _revision = '2006-11-10'

            def __init__(self):
                self.parent = None
                self.ospfaddresslessif = None
                self.ospfifipaddress = None
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

            class OspfIfMulticastForwarding_Enum(Enum):
                """
                OspfIfMulticastForwarding_Enum

                The way multicasts should be forwarded on this
                interface\: not forwarded, forwarded as data
                link multicasts, or forwarded as data link
                unicasts.  Data link multicasting is not
                meaningful on point\-to\-point and NBMA interfaces,
                and setting ospfMulticastForwarding to 0 effectively
                disables all multicast forwarding.

                """

                BLOCKED = 1

                MULTICAST = 2

                UNICAST = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfIfTable.OspfIfEntry.OspfIfMulticastForwarding_Enum']


            class OspfIfState_Enum(Enum):
                """
                OspfIfState_Enum

                The OSPF Interface State.

                """

                DOWN = 1

                LOOPBACK = 2

                WAITING = 3

                POINTTOPOINT = 4

                DESIGNATEDROUTER = 5

                BACKUPDESIGNATEDROUTER = 6

                OTHERDESIGNATEDROUTER = 7


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfIfTable.OspfIfEntry.OspfIfState_Enum']


            class OspfIfType_Enum(Enum):
                """
                OspfIfType_Enum

                The OSPF interface type.
                By way of a default, this field may be intuited
                from the corresponding value of ifType.
                Broadcast LANs, such as Ethernet and IEEE 802.5,
                take the value 'broadcast', X.25 and similar
                technologies take the value 'nbma', and links
                that are definitively point to point take the
                value 'pointToPoint'.

                """

                BROADCAST = 1

                NBMA = 2

                POINTTOPOINT = 3

                POINTTOMULTIPOINT = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfIfTable.OspfIfEntry.OspfIfType_Enum']


            @property
            def _common_path(self):
                if self.ospfaddresslessif is None:
                    raise YPYDataValidationError('Key property ospfaddresslessif is None')
                if self.ospfifipaddress is None:
                    raise YPYDataValidationError('Key property ospfifipaddress is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfIfTable/OSPF-MIB:ospfIfEntry[OSPF-MIB:ospfAddressLessIf = ' + str(self.ospfaddresslessif) + '][OSPF-MIB:ospfIfIpAddress = ' + str(self.ospfifipaddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ospfaddresslessif is not None:
                    return True

                if self.ospfifipaddress is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _OSPF_MIB as meta
                return meta._meta_table['OSPFMIB.OspfIfTable.OspfIfEntry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfIfTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ospfifentry is not None:
                for child_ref in self.ospfifentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _OSPF_MIB as meta
            return meta._meta_table['OSPFMIB.OspfIfTable']['meta_info']


    class OspfLocalLsdbTable(object):
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
        	**type**\: list of :py:class:`OspfLocalLsdbEntry <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfLocalLsdbTable.OspfLocalLsdbEntry>`
        
        

        """

        _prefix = 'ospf-mib'
        _revision = '2006-11-10'

        def __init__(self):
            self.parent = None
            self.ospflocallsdbentry = YList()
            self.ospflocallsdbentry.parent = self
            self.ospflocallsdbentry.name = 'ospflocallsdbentry'


        class OspfLocalLsdbEntry(object):
            """
            A single link state advertisement.
            
            .. attribute:: ospflocallsdbaddresslessif
            
            	The interface index of the interface from which the LSA was received if the interface is unnumbered
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ospflocallsdbipaddress
            
            	The IP address of the interface from which the LSA was received if the interface is numbered
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospflocallsdblsid
            
            	The Link State ID is an LS Type Specific field containing a 32\-bit identifier in IP address format; it identifies the piece of the routing domain that is being described by the advertisement
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospflocallsdbrouterid
            
            	The 32\-bit number that uniquely identifies the originating router in the Autonomous System
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospflocallsdbtype
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\: :py:class:`OspfLocalLsdbType_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfLocalLsdbTable.OspfLocalLsdbEntry.OspfLocalLsdbType_Enum>`
            
            .. attribute:: ospflocallsdbadvertisement
            
            	The entire link state advertisement, including its header.  Note that for variable length LSAs, SNMP agents may not be able to return the largest string size
            	**type**\: str
            
            	**range:** 1..65535
            
            .. attribute:: ospflocallsdbage
            
            	This field is the age of the link state advertisement in seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospflocallsdbchecksum
            
            	This field is the checksum of the complete contents of the advertisement, excepting the age field.  The age field is excepted so that an advertisement's age can be incremented without updating the checksum.  The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred to as the Fletcher checksum
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospflocallsdbsequence
            
            	The sequence number field is a signed 32\-bit integer.  It starts with the value '80000001'h, or \-'7FFFFFFF'h, and increments until '7FFFFFFF'h. Thus, a typical sequence number will be very negative. It is used to detect old and duplicate link state advertisements.  The space of sequence numbers is linearly ordered.  The larger the sequence number, the more recent the advertisement
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'ospf-mib'
            _revision = '2006-11-10'

            def __init__(self):
                self.parent = None
                self.ospflocallsdbaddresslessif = None
                self.ospflocallsdbipaddress = None
                self.ospflocallsdblsid = None
                self.ospflocallsdbrouterid = None
                self.ospflocallsdbtype = None
                self.ospflocallsdbadvertisement = None
                self.ospflocallsdbage = None
                self.ospflocallsdbchecksum = None
                self.ospflocallsdbsequence = None

            class OspfLocalLsdbType_Enum(Enum):
                """
                OspfLocalLsdbType_Enum

                The type of the link state advertisement.
                Each link state type has a separate
                advertisement format.

                """

                LOCALOPAQUELINK = 9


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfLocalLsdbTable.OspfLocalLsdbEntry.OspfLocalLsdbType_Enum']


            @property
            def _common_path(self):
                if self.ospflocallsdbaddresslessif is None:
                    raise YPYDataValidationError('Key property ospflocallsdbaddresslessif is None')
                if self.ospflocallsdbipaddress is None:
                    raise YPYDataValidationError('Key property ospflocallsdbipaddress is None')
                if self.ospflocallsdblsid is None:
                    raise YPYDataValidationError('Key property ospflocallsdblsid is None')
                if self.ospflocallsdbrouterid is None:
                    raise YPYDataValidationError('Key property ospflocallsdbrouterid is None')
                if self.ospflocallsdbtype is None:
                    raise YPYDataValidationError('Key property ospflocallsdbtype is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfLocalLsdbTable/OSPF-MIB:ospfLocalLsdbEntry[OSPF-MIB:ospfLocalLsdbAddressLessIf = ' + str(self.ospflocallsdbaddresslessif) + '][OSPF-MIB:ospfLocalLsdbIpAddress = ' + str(self.ospflocallsdbipaddress) + '][OSPF-MIB:ospfLocalLsdbLsid = ' + str(self.ospflocallsdblsid) + '][OSPF-MIB:ospfLocalLsdbRouterId = ' + str(self.ospflocallsdbrouterid) + '][OSPF-MIB:ospfLocalLsdbType = ' + str(self.ospflocallsdbtype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ospflocallsdbaddresslessif is not None:
                    return True

                if self.ospflocallsdbipaddress is not None:
                    return True

                if self.ospflocallsdblsid is not None:
                    return True

                if self.ospflocallsdbrouterid is not None:
                    return True

                if self.ospflocallsdbtype is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _OSPF_MIB as meta
                return meta._meta_table['OSPFMIB.OspfLocalLsdbTable.OspfLocalLsdbEntry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfLocalLsdbTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ospflocallsdbentry is not None:
                for child_ref in self.ospflocallsdbentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _OSPF_MIB as meta
            return meta._meta_table['OSPFMIB.OspfLocalLsdbTable']['meta_info']


    class OspfLsdbTable(object):
        """
        The OSPF Process's link state database (LSDB).
        The LSDB contains the link state advertisements
        from throughout the areas that the device is attached to.
        
        .. attribute:: ospflsdbentry
        
        	A single link state advertisement
        	**type**\: list of :py:class:`OspfLsdbEntry <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfLsdbTable.OspfLsdbEntry>`
        
        

        """

        _prefix = 'ospf-mib'
        _revision = '2006-11-10'

        def __init__(self):
            self.parent = None
            self.ospflsdbentry = YList()
            self.ospflsdbentry.parent = self
            self.ospflsdbentry.name = 'ospflsdbentry'


        class OspfLsdbEntry(object):
            """
            A single link state advertisement.
            
            .. attribute:: ospflsdbareaid
            
            	The 32\-bit identifier of the area from which the LSA was received
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospflsdblsid
            
            	The Link State ID is an LS Type Specific field containing either a Router ID or an IP address; it identifies the piece of the routing domain that is being described by the advertisement
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospflsdbrouterid
            
            	The 32\-bit number that uniquely identifies the originating router in the Autonomous System
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospflsdbtype
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format.  Note\: External link state advertisements are permitted for backward compatibility, but should be displayed in the ospfAsLsdbTable rather than here
            	**type**\: :py:class:`OspfLsdbType_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfLsdbTable.OspfLsdbEntry.OspfLsdbType_Enum>`
            
            .. attribute:: ospflsdbadvertisement
            
            	The entire link state advertisement, including its header.  Note that for variable length LSAs, SNMP agents may not be able to return the largest string size
            	**type**\: str
            
            	**range:** 1..65535
            
            .. attribute:: ospflsdbage
            
            	This field is the age of the link state advertisement in seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospflsdbchecksum
            
            	This field is the checksum of the complete contents of the advertisement, excepting the age field.  The age field is excepted so that an advertisement's age can be incremented without updating the checksum.  The checksum used is the same that is used for ISO connectionless  datagrams; it is commonly referred to as the Fletcher checksum
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospflsdbsequence
            
            	The sequence number field is a signed 32\-bit integer.  It starts with the value '80000001'h, or \-'7FFFFFFF'h, and increments until '7FFFFFFF'h. Thus, a typical sequence number will be very negative. It is used to detect old and duplicate Link State Advertisements.  The space of sequence numbers is linearly ordered.  The larger the sequence number, the more recent the advertisement
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'ospf-mib'
            _revision = '2006-11-10'

            def __init__(self):
                self.parent = None
                self.ospflsdbareaid = None
                self.ospflsdblsid = None
                self.ospflsdbrouterid = None
                self.ospflsdbtype = None
                self.ospflsdbadvertisement = None
                self.ospflsdbage = None
                self.ospflsdbchecksum = None
                self.ospflsdbsequence = None

            class OspfLsdbType_Enum(Enum):
                """
                OspfLsdbType_Enum

                The type of the link state advertisement.
                Each link state type has a separate advertisement
                format.
                
                Note\: External link state advertisements are permitted
                for backward compatibility, but should be displayed
                in the ospfAsLsdbTable rather than here.

                """

                ROUTERLINK = 1

                NETWORKLINK = 2

                SUMMARYLINK = 3

                ASSUMMARYLINK = 4

                ASEXTERNALLINK = 5

                MULTICASTLINK = 6

                NSSAEXTERNALLINK = 7

                AREAOPAQUELINK = 10


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfLsdbTable.OspfLsdbEntry.OspfLsdbType_Enum']


            @property
            def _common_path(self):
                if self.ospflsdbareaid is None:
                    raise YPYDataValidationError('Key property ospflsdbareaid is None')
                if self.ospflsdblsid is None:
                    raise YPYDataValidationError('Key property ospflsdblsid is None')
                if self.ospflsdbrouterid is None:
                    raise YPYDataValidationError('Key property ospflsdbrouterid is None')
                if self.ospflsdbtype is None:
                    raise YPYDataValidationError('Key property ospflsdbtype is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfLsdbTable/OSPF-MIB:ospfLsdbEntry[OSPF-MIB:ospfLsdbAreaId = ' + str(self.ospflsdbareaid) + '][OSPF-MIB:ospfLsdbLsid = ' + str(self.ospflsdblsid) + '][OSPF-MIB:ospfLsdbRouterId = ' + str(self.ospflsdbrouterid) + '][OSPF-MIB:ospfLsdbType = ' + str(self.ospflsdbtype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ospflsdbareaid is not None:
                    return True

                if self.ospflsdblsid is not None:
                    return True

                if self.ospflsdbrouterid is not None:
                    return True

                if self.ospflsdbtype is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _OSPF_MIB as meta
                return meta._meta_table['OSPFMIB.OspfLsdbTable.OspfLsdbEntry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfLsdbTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ospflsdbentry is not None:
                for child_ref in self.ospflsdbentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _OSPF_MIB as meta
            return meta._meta_table['OSPFMIB.OspfLsdbTable']['meta_info']


    class OspfNbrTable(object):
        """
        A table describing all non\-virtual neighbors
        in the locality of the OSPF router.
        
        .. attribute:: ospfnbrentry
        
        	The information regarding a single neighbor.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile  storage
        	**type**\: list of :py:class:`OspfNbrEntry <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfNbrTable.OspfNbrEntry>`
        
        

        """

        _prefix = 'ospf-mib'
        _revision = '2006-11-10'

        def __init__(self):
            self.parent = None
            self.ospfnbrentry = YList()
            self.ospfnbrentry.parent = self
            self.ospfnbrentry.name = 'ospfnbrentry'


        class OspfNbrEntry(object):
            """
            The information regarding a single neighbor.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            
            storage.
            
            .. attribute:: ospfnbraddresslessindex
            
            	On an interface having an IP address, zero. On addressless interfaces, the corresponding value of ifIndex in the Internet Standard MIB. On row creation, this can be derived from the instance
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ospfnbripaddr
            
            	The IP address this neighbor is using in its IP source address.  Note that, on addressless links, this will not be 0.0.0.0 but the  address of another of the neighbor's interfaces
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfnbmanbrpermanence
            
            	This variable displays the status of the entry; 'dynamic' and 'permanent' refer to how the neighbor became known
            	**type**\: :py:class:`OspfNbmaNbrPermanence_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfNbrTable.OspfNbrEntry.OspfNbmaNbrPermanence_Enum>`
            
            .. attribute:: ospfnbmanbrstatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: ospfnbrevents
            
            	The number of times this neighbor relationship has changed state or an error has occurred.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ospfDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfnbrhellosuppressed
            
            	Indicates whether Hellos are being suppressed to the neighbor
            	**type**\: bool
            
            .. attribute:: ospfnbrlsretransqlen
            
            	The current length of the retransmission queue
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfnbroptions
            
            	A bit mask corresponding to the neighbor's options field.  Bit 0, if set, indicates that the system will operate on Type of Service metrics other than TOS 0.  If zero, the neighbor will ignore all metrics except the TOS 0 metric.  Bit 1, if set, indicates that the associated area accepts and operates on external information; if zero, it is a stub area.  Bit 2, if set, indicates that the system is capable of routing IP multicast datagrams, that is that it implements the multicast extensions to OSPF.  Bit 3, if set, indicates that the associated area is an NSSA.  These areas are capable of carrying type\-7 external advertisements, which are translated into type\-5 external advertisements at NSSA borders
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospfnbrpriority
            
            	The priority of this neighbor in the designated router election algorithm.  The value 0 signifies that the neighbor is not eligible to become the designated router on this particular network
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: ospfnbrrestarthelperage
            
            	Remaining time in current OSPF graceful restart interval, if the router is acting as a restart helper for the neighbor
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfnbrrestarthelperexitreason
            
            	Describes the outcome of the last attempt at acting as a graceful restart helper for the neighbor
            	**type**\: :py:class:`OspfNbrRestartHelperExitReason_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfNbrTable.OspfNbrEntry.OspfNbrRestartHelperExitReason_Enum>`
            
            .. attribute:: ospfnbrrestarthelperstatus
            
            	Indicates whether the router is acting as a graceful restart helper for the neighbor
            	**type**\: :py:class:`OspfNbrRestartHelperStatus_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfNbrTable.OspfNbrEntry.OspfNbrRestartHelperStatus_Enum>`
            
            .. attribute:: ospfnbrrtrid
            
            	A 32\-bit integer (represented as a type IpAddress) uniquely identifying the neighboring router in the Autonomous System
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfnbrstate
            
            	The state of the relationship with this neighbor
            	**type**\: :py:class:`OspfNbrState_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfNbrTable.OspfNbrEntry.OspfNbrState_Enum>`
            
            

            """

            _prefix = 'ospf-mib'
            _revision = '2006-11-10'

            def __init__(self):
                self.parent = None
                self.ospfnbraddresslessindex = None
                self.ospfnbripaddr = None
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

            class OspfNbmaNbrPermanence_Enum(Enum):
                """
                OspfNbmaNbrPermanence_Enum

                This variable displays the status of the entry;
                'dynamic' and 'permanent' refer to how the neighbor
                became known.

                """

                DYNAMIC = 1

                PERMANENT = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfNbrTable.OspfNbrEntry.OspfNbmaNbrPermanence_Enum']


            class OspfNbrRestartHelperExitReason_Enum(Enum):
                """
                OspfNbrRestartHelperExitReason_Enum

                Describes the outcome of the last attempt at acting
                as a graceful restart helper for the neighbor.

                """

                NONE = 1

                INPROGRESS = 2

                COMPLETED = 3

                TIMEDOUT = 4

                TOPOLOGYCHANGED = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfNbrTable.OspfNbrEntry.OspfNbrRestartHelperExitReason_Enum']


            class OspfNbrRestartHelperStatus_Enum(Enum):
                """
                OspfNbrRestartHelperStatus_Enum

                Indicates whether the router is acting
                as a graceful restart helper for the neighbor.

                """

                NOTHELPING = 1

                HELPING = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfNbrTable.OspfNbrEntry.OspfNbrRestartHelperStatus_Enum']


            class OspfNbrState_Enum(Enum):
                """
                OspfNbrState_Enum

                The state of the relationship with this neighbor.

                """

                DOWN = 1

                ATTEMPT = 2

                INIT = 3

                TWOWAY = 4

                EXCHANGESTART = 5

                EXCHANGE = 6

                LOADING = 7

                FULL = 8


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfNbrTable.OspfNbrEntry.OspfNbrState_Enum']


            @property
            def _common_path(self):
                if self.ospfnbraddresslessindex is None:
                    raise YPYDataValidationError('Key property ospfnbraddresslessindex is None')
                if self.ospfnbripaddr is None:
                    raise YPYDataValidationError('Key property ospfnbripaddr is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfNbrTable/OSPF-MIB:ospfNbrEntry[OSPF-MIB:ospfNbrAddressLessIndex = ' + str(self.ospfnbraddresslessindex) + '][OSPF-MIB:ospfNbrIpAddr = ' + str(self.ospfnbripaddr) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ospfnbraddresslessindex is not None:
                    return True

                if self.ospfnbripaddr is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _OSPF_MIB as meta
                return meta._meta_table['OSPFMIB.OspfNbrTable.OspfNbrEntry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfNbrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ospfnbrentry is not None:
                for child_ref in self.ospfnbrentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _OSPF_MIB as meta
            return meta._meta_table['OSPFMIB.OspfNbrTable']['meta_info']


    class OspfStubAreaTable(object):
        """
        The set of metrics that will be advertised
        by a default Area Border Router into a stub area.
        
        .. attribute:: ospfstubareaentry
        
        	The metric for a given Type of Service that will be advertised by a default Area Border Router into a stub area.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile storage
        	**type**\: list of :py:class:`OspfStubAreaEntry <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfStubAreaTable.OspfStubAreaEntry>`
        
        

        """

        _prefix = 'ospf-mib'
        _revision = '2006-11-10'

        def __init__(self):
            self.parent = None
            self.ospfstubareaentry = YList()
            self.ospfstubareaentry.parent = self
            self.ospfstubareaentry.name = 'ospfstubareaentry'


        class OspfStubAreaEntry(object):
            """
            The metric for a given Type of Service that
            will be advertised by a default Area Border
            Router into a stub area.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            storage.
            
            .. attribute:: ospfstubareaid
            
            	The 32\-bit identifier for the stub area.  On creation, this can be derived from the instance
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfstubtos
            
            	The Type of Service associated with the metric.  On creation, this can be derived from  the instance
            	**type**\: int
            
            	**range:** 0..30
            
            .. attribute:: ospfstubmetric
            
            	The metric value applied at the indicated Type of Service.  By default, this equals the least metric at the Type of Service among the interfaces to other areas
            	**type**\: int
            
            	**range:** 0..16777215
            
            .. attribute:: ospfstubmetrictype
            
            	This variable displays the type of metric advertised as a default route
            	**type**\: :py:class:`OspfStubMetricType_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfStubAreaTable.OspfStubAreaEntry.OspfStubMetricType_Enum>`
            
            .. attribute:: ospfstubstatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'ospf-mib'
            _revision = '2006-11-10'

            def __init__(self):
                self.parent = None
                self.ospfstubareaid = None
                self.ospfstubtos = None
                self.ospfstubmetric = None
                self.ospfstubmetrictype = None
                self.ospfstubstatus = None

            class OspfStubMetricType_Enum(Enum):
                """
                OspfStubMetricType_Enum

                This variable displays the type of metric
                advertised as a default route.

                """

                OSPFMETRIC = 1

                COMPARABLECOST = 2

                NONCOMPARABLE = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfStubAreaTable.OspfStubAreaEntry.OspfStubMetricType_Enum']


            @property
            def _common_path(self):
                if self.ospfstubareaid is None:
                    raise YPYDataValidationError('Key property ospfstubareaid is None')
                if self.ospfstubtos is None:
                    raise YPYDataValidationError('Key property ospfstubtos is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfStubAreaTable/OSPF-MIB:ospfStubAreaEntry[OSPF-MIB:ospfStubAreaId = ' + str(self.ospfstubareaid) + '][OSPF-MIB:ospfStubTOS = ' + str(self.ospfstubtos) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _OSPF_MIB as meta
                return meta._meta_table['OSPFMIB.OspfStubAreaTable.OspfStubAreaEntry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfStubAreaTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ospfstubareaentry is not None:
                for child_ref in self.ospfstubareaentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _OSPF_MIB as meta
            return meta._meta_table['OSPFMIB.OspfStubAreaTable']['meta_info']


    class OspfVirtIfTable(object):
        """
        Information about this router's virtual interfaces
        that the OSPF Process is configured to carry on.
        
        .. attribute:: ospfvirtifentry
        
        	Information about a single virtual interface.  Information in this table is persistent and when this object is written the entity SHOULD save the change to non\-volatile storage
        	**type**\: list of :py:class:`OspfVirtIfEntry <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfVirtIfTable.OspfVirtIfEntry>`
        
        

        """

        _prefix = 'ospf-mib'
        _revision = '2006-11-10'

        def __init__(self):
            self.parent = None
            self.ospfvirtifentry = YList()
            self.ospfvirtifentry.parent = self
            self.ospfvirtifentry.name = 'ospfvirtifentry'


        class OspfVirtIfEntry(object):
            """
            Information about a single virtual interface.
            
            Information in this table is persistent and when this object
            is written the entity SHOULD save the change to non\-volatile
            storage.
            
            .. attribute:: ospfvirtifareaid
            
            	The transit area that the virtual link traverses.  By definition, this is not 0.0.0.0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfvirtifneighbor
            
            	The Router ID of the virtual neighbor
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfvirtiflsacksumsum
            
            	The 32\-bit unsigned sum of the link\-state advertisements' LS checksums contained in this virtual interface's link\-local link state database. The sum can be used to determine if there has been a change in the virtual interface's link state database, and to compare the virtual interface link\-state database of the virtual neighbors
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfvirtiflsacount
            
            	The total number of link\-local link state advertisements in this virtual interface's link\-local link state database
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfvirtifauthkey
            
            	The cleartext password used as an OSPF authentication key when simplePassword security is enabled.  This object does not access any OSPF cryptogaphic (e.g., MD5) authentication key under any circumstance.  If the key length is shorter than 8 octets, the agent will left adjust and zero fill to 8 octets.  Unauthenticated interfaces need no authentication key, and simple password authentication cannot use a key of more than 8 octets.  Note that the use of simplePassword authentication is NOT recommended when there is concern regarding attack upon the OSPF system.  SimplePassword authentication is only sufficient to protect against accidental misconfigurations because it re\-uses cleartext passwords.  [RFC1704]  When read, ospfIfAuthKey always returns an octet string of length zero
            	**type**\: str
            
            	**range:** 0..256
            
            .. attribute:: ospfvirtifauthtype
            
            	The authentication type specified for a virtual interface.  Note that this object can be used to engage in significant attacks against an OSPF router
            	**type**\: :py:class:`OspfAuthenticationType_Enum <ydk.models.ospf.OSPF_MIB.OspfAuthenticationType_Enum>`
            
            .. attribute:: ospfvirtifevents
            
            	The number of state changes or error events on this virtual link.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ospfDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfvirtifhellointerval
            
            	The length of time, in seconds, between the Hello packets that the router sends on the interface.  This value must be the same for the virtual neighbor
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: ospfvirtiflsacksumsum
            
            	The 32\-bit unsigned sum of the link state advertisements' LS checksums contained in this virtual interface's link\-local link state database. The sum can be used to determine if there has been a change in the virtual interface's link state database, and to compare the virtual interface link state database of the virtual neighbors
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfvirtiflsacount
            
            	The total number of link\-local link state advertisements in this virtual interface's link\-local link state database
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfvirtifretransinterval
            
            	The number of seconds between link state avertisement retransmissions, for adjacencies belonging to this interface.  This value is also used when retransmitting database description and Link State request packets.  This value should be well over the expected round\-trip time.  Note that the minimal value SHOULD be 1 second
            	**type**\: int
            
            	**range:** 0..3600
            
            .. attribute:: ospfvirtifrtrdeadinterval
            
            	The number of seconds that a router's Hello packets have not been seen before its neighbors declare the router down.  This should be some multiple of the Hello interval.  This value must be the same for the virtual neighbor
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ospfvirtifstate
            
            	OSPF virtual interface states
            	**type**\: :py:class:`OspfVirtIfState_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfVirtIfTable.OspfVirtIfEntry.OspfVirtIfState_Enum>`
            
            .. attribute:: ospfvirtifstatus
            
            	This object permits management of the table by facilitating actions such as row creation, construction, and destruction.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: ospfvirtiftransitdelay
            
            	The estimated number of seconds it takes to transmit a Link State update packet over this interface.  Note that the minimal value SHOULD be 1 second
            	**type**\: int
            
            	**range:** 0..3600
            
            

            """

            _prefix = 'ospf-mib'
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

            class OspfVirtIfState_Enum(Enum):
                """
                OspfVirtIfState_Enum

                OSPF virtual interface states.

                """

                DOWN = 1

                POINTTOPOINT = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfVirtIfTable.OspfVirtIfEntry.OspfVirtIfState_Enum']


            @property
            def _common_path(self):
                if self.ospfvirtifareaid is None:
                    raise YPYDataValidationError('Key property ospfvirtifareaid is None')
                if self.ospfvirtifneighbor is None:
                    raise YPYDataValidationError('Key property ospfvirtifneighbor is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfVirtIfTable/OSPF-MIB:ospfVirtIfEntry[OSPF-MIB:ospfVirtIfAreaId = ' + str(self.ospfvirtifareaid) + '][OSPF-MIB:ospfVirtIfNeighbor = ' + str(self.ospfvirtifneighbor) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _OSPF_MIB as meta
                return meta._meta_table['OSPFMIB.OspfVirtIfTable.OspfVirtIfEntry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfVirtIfTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ospfvirtifentry is not None:
                for child_ref in self.ospfvirtifentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _OSPF_MIB as meta
            return meta._meta_table['OSPFMIB.OspfVirtIfTable']['meta_info']


    class OspfVirtLocalLsdbTable(object):
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
        	**type**\: list of :py:class:`OspfVirtLocalLsdbEntry <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfVirtLocalLsdbTable.OspfVirtLocalLsdbEntry>`
        
        

        """

        _prefix = 'ospf-mib'
        _revision = '2006-11-10'

        def __init__(self):
            self.parent = None
            self.ospfvirtlocallsdbentry = YList()
            self.ospfvirtlocallsdbentry.parent = self
            self.ospfvirtlocallsdbentry.name = 'ospfvirtlocallsdbentry'


        class OspfVirtLocalLsdbEntry(object):
            """
            A single link state advertisement.
            
            .. attribute:: ospfvirtlocallsdblsid
            
            	The Link State ID is an LS Type Specific field containing a 32\-bit identifier in IP address format; it identifies the piece of the routing domain that is being described by the advertisement
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfvirtlocallsdbneighbor
            
            	The Router ID of the virtual neighbor
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfvirtlocallsdbrouterid
            
            	The 32\-bit number that uniquely identifies the originating router in the Autonomous System
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfvirtlocallsdbtransitarea
            
            	The transit area that the virtual link traverses.  By definition, this is not 0.0.0.0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfvirtlocallsdbtype
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\: :py:class:`OspfVirtLocalLsdbType_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfVirtLocalLsdbTable.OspfVirtLocalLsdbEntry.OspfVirtLocalLsdbType_Enum>`
            
            .. attribute:: ospfvirtlocallsdbadvertisement
            
            	The entire link state advertisement, including its header
            	**type**\: str
            
            	**range:** 1..65535
            
            .. attribute:: ospfvirtlocallsdbage
            
            	This field is the age of the link state advertisement in seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospfvirtlocallsdbchecksum
            
            	This field is the checksum of the complete contents of the advertisement, excepting the age field.  The age field is excepted so that  an advertisement's age can be incremented without updating the checksum.  The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred to as the Fletcher checksum
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospfvirtlocallsdbsequence
            
            	The sequence number field is a signed 32\-bit integer.  It starts with the value '80000001'h, or \-'7FFFFFFF'h, and increments until '7FFFFFFF'h. Thus, a typical sequence number will be very negative. It is used to detect old and duplicate link state advertisements.  The space of sequence numbers is linearly ordered.  The larger the sequence number, the more recent the advertisement
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'ospf-mib'
            _revision = '2006-11-10'

            def __init__(self):
                self.parent = None
                self.ospfvirtlocallsdblsid = None
                self.ospfvirtlocallsdbneighbor = None
                self.ospfvirtlocallsdbrouterid = None
                self.ospfvirtlocallsdbtransitarea = None
                self.ospfvirtlocallsdbtype = None
                self.ospfvirtlocallsdbadvertisement = None
                self.ospfvirtlocallsdbage = None
                self.ospfvirtlocallsdbchecksum = None
                self.ospfvirtlocallsdbsequence = None

            class OspfVirtLocalLsdbType_Enum(Enum):
                """
                OspfVirtLocalLsdbType_Enum

                The type of the link state advertisement.
                Each link state type has a separate
                advertisement format.

                """

                LOCALOPAQUELINK = 9


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfVirtLocalLsdbTable.OspfVirtLocalLsdbEntry.OspfVirtLocalLsdbType_Enum']


            @property
            def _common_path(self):
                if self.ospfvirtlocallsdblsid is None:
                    raise YPYDataValidationError('Key property ospfvirtlocallsdblsid is None')
                if self.ospfvirtlocallsdbneighbor is None:
                    raise YPYDataValidationError('Key property ospfvirtlocallsdbneighbor is None')
                if self.ospfvirtlocallsdbrouterid is None:
                    raise YPYDataValidationError('Key property ospfvirtlocallsdbrouterid is None')
                if self.ospfvirtlocallsdbtransitarea is None:
                    raise YPYDataValidationError('Key property ospfvirtlocallsdbtransitarea is None')
                if self.ospfvirtlocallsdbtype is None:
                    raise YPYDataValidationError('Key property ospfvirtlocallsdbtype is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfVirtLocalLsdbTable/OSPF-MIB:ospfVirtLocalLsdbEntry[OSPF-MIB:ospfVirtLocalLsdbLsid = ' + str(self.ospfvirtlocallsdblsid) + '][OSPF-MIB:ospfVirtLocalLsdbNeighbor = ' + str(self.ospfvirtlocallsdbneighbor) + '][OSPF-MIB:ospfVirtLocalLsdbRouterId = ' + str(self.ospfvirtlocallsdbrouterid) + '][OSPF-MIB:ospfVirtLocalLsdbTransitArea = ' + str(self.ospfvirtlocallsdbtransitarea) + '][OSPF-MIB:ospfVirtLocalLsdbType = ' + str(self.ospfvirtlocallsdbtype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ospfvirtlocallsdblsid is not None:
                    return True

                if self.ospfvirtlocallsdbneighbor is not None:
                    return True

                if self.ospfvirtlocallsdbrouterid is not None:
                    return True

                if self.ospfvirtlocallsdbtransitarea is not None:
                    return True

                if self.ospfvirtlocallsdbtype is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _OSPF_MIB as meta
                return meta._meta_table['OSPFMIB.OspfVirtLocalLsdbTable.OspfVirtLocalLsdbEntry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfVirtLocalLsdbTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ospfvirtlocallsdbentry is not None:
                for child_ref in self.ospfvirtlocallsdbentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _OSPF_MIB as meta
            return meta._meta_table['OSPFMIB.OspfVirtLocalLsdbTable']['meta_info']


    class OspfVirtNbrTable(object):
        """
        This table describes all virtual neighbors.
        Since virtual links are configured
        in the Virtual Interface Table, this table is read\-only.
        
        .. attribute:: ospfvirtnbrentry
        
        	Virtual neighbor information
        	**type**\: list of :py:class:`OspfVirtNbrEntry <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfVirtNbrTable.OspfVirtNbrEntry>`
        
        

        """

        _prefix = 'ospf-mib'
        _revision = '2006-11-10'

        def __init__(self):
            self.parent = None
            self.ospfvirtnbrentry = YList()
            self.ospfvirtnbrentry.parent = self
            self.ospfvirtnbrentry.name = 'ospfvirtnbrentry'


        class OspfVirtNbrEntry(object):
            """
            Virtual neighbor information.
            
            .. attribute:: ospfvirtnbrarea
            
            	The Transit Area Identifier
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfvirtnbrrtrid
            
            	A 32\-bit integer uniquely identifying the neighboring router in the Autonomous System
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfvirtnbrevents
            
            	The number of times this virtual link has changed its state or an error has occurred.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ospfDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfvirtnbrhellosuppressed
            
            	Indicates whether Hellos are being suppressed to the neighbor
            	**type**\: bool
            
            .. attribute:: ospfvirtnbripaddr
            
            	The IP address this virtual neighbor is using
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospfvirtnbrlsretransqlen
            
            	The current length of the retransmission queue
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfvirtnbroptions
            
            	A bit mask corresponding to the neighbor's options field.  Bit 1, if set, indicates that the system will operate on Type of Service metrics other than TOS 0.  If zero, the neighbor will ignore all metrics except the TOS 0 metric.  Bit 2, if set, indicates that the system is network multicast capable, i.e., that it implements OSPF multicast routing
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ospfvirtnbrrestarthelperage
            
            	Remaining time in current OSPF graceful restart interval, if the router is acting as a restart helper for the neighbor
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfvirtnbrrestarthelperexitreason
            
            	Describes the outcome of the last attempt at acting as a graceful restart helper for the neighbor
            	**type**\: :py:class:`OspfVirtNbrRestartHelperExitReason_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfVirtNbrTable.OspfVirtNbrEntry.OspfVirtNbrRestartHelperExitReason_Enum>`
            
            .. attribute:: ospfvirtnbrrestarthelperstatus
            
            	Indicates whether the router is acting as a graceful restart helper for the neighbor
            	**type**\: :py:class:`OspfVirtNbrRestartHelperStatus_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfVirtNbrTable.OspfVirtNbrEntry.OspfVirtNbrRestartHelperStatus_Enum>`
            
            .. attribute:: ospfvirtnbrstate
            
            	The state of the virtual neighbor relationship
            	**type**\: :py:class:`OspfVirtNbrState_Enum <ydk.models.ospf.OSPF_MIB.OSPFMIB.OspfVirtNbrTable.OspfVirtNbrEntry.OspfVirtNbrState_Enum>`
            
            

            """

            _prefix = 'ospf-mib'
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

            class OspfVirtNbrRestartHelperExitReason_Enum(Enum):
                """
                OspfVirtNbrRestartHelperExitReason_Enum

                Describes the outcome of the last attempt at acting
                as a graceful restart helper for the neighbor.

                """

                NONE = 1

                INPROGRESS = 2

                COMPLETED = 3

                TIMEDOUT = 4

                TOPOLOGYCHANGED = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfVirtNbrTable.OspfVirtNbrEntry.OspfVirtNbrRestartHelperExitReason_Enum']


            class OspfVirtNbrRestartHelperStatus_Enum(Enum):
                """
                OspfVirtNbrRestartHelperStatus_Enum

                Indicates whether the router is acting
                as a graceful restart helper for the neighbor.

                """

                NOTHELPING = 1

                HELPING = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfVirtNbrTable.OspfVirtNbrEntry.OspfVirtNbrRestartHelperStatus_Enum']


            class OspfVirtNbrState_Enum(Enum):
                """
                OspfVirtNbrState_Enum

                The state of the virtual neighbor relationship.

                """

                DOWN = 1

                ATTEMPT = 2

                INIT = 3

                TWOWAY = 4

                EXCHANGESTART = 5

                EXCHANGE = 6

                LOADING = 7

                FULL = 8


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _OSPF_MIB as meta
                    return meta._meta_table['OSPFMIB.OspfVirtNbrTable.OspfVirtNbrEntry.OspfVirtNbrState_Enum']


            @property
            def _common_path(self):
                if self.ospfvirtnbrarea is None:
                    raise YPYDataValidationError('Key property ospfvirtnbrarea is None')
                if self.ospfvirtnbrrtrid is None:
                    raise YPYDataValidationError('Key property ospfvirtnbrrtrid is None')

                return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfVirtNbrTable/OSPF-MIB:ospfVirtNbrEntry[OSPF-MIB:ospfVirtNbrArea = ' + str(self.ospfvirtnbrarea) + '][OSPF-MIB:ospfVirtNbrRtrId = ' + str(self.ospfvirtnbrrtrid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _OSPF_MIB as meta
                return meta._meta_table['OSPFMIB.OspfVirtNbrTable.OspfVirtNbrEntry']['meta_info']

        @property
        def _common_path(self):

            return '/OSPF-MIB:OSPF-MIB/OSPF-MIB:ospfVirtNbrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ospfvirtnbrentry is not None:
                for child_ref in self.ospfvirtnbrentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _OSPF_MIB as meta
            return meta._meta_table['OSPFMIB.OspfVirtNbrTable']['meta_info']

    @property
    def _common_path(self):

        return '/OSPF-MIB:OSPF-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.ospfareaaggregatetable is not None and self.ospfareaaggregatetable._has_data():
            return True

        if self.ospfareaaggregatetable is not None and self.ospfareaaggregatetable.is_presence():
            return True

        if self.ospfarealsacounttable is not None and self.ospfarealsacounttable._has_data():
            return True

        if self.ospfarealsacounttable is not None and self.ospfarealsacounttable.is_presence():
            return True

        if self.ospfarearangetable is not None and self.ospfarearangetable._has_data():
            return True

        if self.ospfarearangetable is not None and self.ospfarearangetable.is_presence():
            return True

        if self.ospfareatable is not None and self.ospfareatable._has_data():
            return True

        if self.ospfareatable is not None and self.ospfareatable.is_presence():
            return True

        if self.ospfaslsdbtable is not None and self.ospfaslsdbtable._has_data():
            return True

        if self.ospfaslsdbtable is not None and self.ospfaslsdbtable.is_presence():
            return True

        if self.ospfextlsdbtable is not None and self.ospfextlsdbtable._has_data():
            return True

        if self.ospfextlsdbtable is not None and self.ospfextlsdbtable.is_presence():
            return True

        if self.ospfgeneralgroup is not None and self.ospfgeneralgroup._has_data():
            return True

        if self.ospfgeneralgroup is not None and self.ospfgeneralgroup.is_presence():
            return True

        if self.ospfhosttable is not None and self.ospfhosttable._has_data():
            return True

        if self.ospfhosttable is not None and self.ospfhosttable.is_presence():
            return True

        if self.ospfifmetrictable is not None and self.ospfifmetrictable._has_data():
            return True

        if self.ospfifmetrictable is not None and self.ospfifmetrictable.is_presence():
            return True

        if self.ospfiftable is not None and self.ospfiftable._has_data():
            return True

        if self.ospfiftable is not None and self.ospfiftable.is_presence():
            return True

        if self.ospflocallsdbtable is not None and self.ospflocallsdbtable._has_data():
            return True

        if self.ospflocallsdbtable is not None and self.ospflocallsdbtable.is_presence():
            return True

        if self.ospflsdbtable is not None and self.ospflsdbtable._has_data():
            return True

        if self.ospflsdbtable is not None and self.ospflsdbtable.is_presence():
            return True

        if self.ospfnbrtable is not None and self.ospfnbrtable._has_data():
            return True

        if self.ospfnbrtable is not None and self.ospfnbrtable.is_presence():
            return True

        if self.ospfstubareatable is not None and self.ospfstubareatable._has_data():
            return True

        if self.ospfstubareatable is not None and self.ospfstubareatable.is_presence():
            return True

        if self.ospfvirtiftable is not None and self.ospfvirtiftable._has_data():
            return True

        if self.ospfvirtiftable is not None and self.ospfvirtiftable.is_presence():
            return True

        if self.ospfvirtlocallsdbtable is not None and self.ospfvirtlocallsdbtable._has_data():
            return True

        if self.ospfvirtlocallsdbtable is not None and self.ospfvirtlocallsdbtable.is_presence():
            return True

        if self.ospfvirtnbrtable is not None and self.ospfvirtnbrtable._has_data():
            return True

        if self.ospfvirtnbrtable is not None and self.ospfvirtnbrtable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ospf._meta import _OSPF_MIB as meta
        return meta._meta_table['OSPFMIB']['meta_info']



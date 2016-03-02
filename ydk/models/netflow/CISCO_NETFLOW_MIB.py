""" CISCO_NETFLOW_MIB 

The Netflow MIB provides a simple and easy method
to get NetFlow cache information, current NetFlow
configuration and statistics. It will enable medium to
small size enterprises to take advantage of NetFlow
technology over SNMP at a reduced infrastructure cost.
The MIB is created to provide Netflow information in
these areas\:

       1. Cache information and configuration.
       2. Export information and configuration.
       4. Export Statistics.
       5. Protocol Statistics.
       6. Version 9 Export Template information.
       7. Top Flows information.


Terminology used

Flow
A flow is defined as an unidirectional sequence of
packets between a given source and destination
endpoints. Network flows are highly granular;
flow endpoints are identified both by IP address as
well as by transport layer application port numbers.
NetFlow also utilizes the IP Protocol type,
Type of Service (ToS) and the input interface
identifier to uniquely identify flows.

Exporter
A device (for example, a router) with NetFlow
services enabled. The exporter monitors packets
entering an observation point and creates flows out
of these packets. The information from these flows
are exported in the form of Flow Records to
the collector.

Flow Record
A Flow Record provides information about an IP Flow
that exists on the Exporter. The Flow Records are
commonly referred to as NetFlow Services data or
NetFlow data.

Collector
The NetFlow Collector receives Flow Records from
one or more Exporters. It processes the received
export packet, i.e. parses, stores the Flow Record
information. The flow records may be optionally
aggregated before storing into the hard disk.

Template
NetFlow Version 9 Export format is template based.
Version 9 record format consists of a packet header
followed by at least one or more template or data
FlowSets. A template FlowSet (collection of one or more
template) provides a description of the fields that
will be present in future data FlowSets. Templates
provide an extensible design to the record format,
a feature that should allow future enhancements to
NetFlow services without requiring concurrent changes
to the basic flow\-record format.

One additional record type is also a part of
Version 9 specification\: an options template. Rather
than supplying information about IP flows, options are
used to supply meta\-data about the NetFlow process
itself.


Top Flows.

This feature provides a mechanism which allows the
top N flows in the netflow cache to be viewed
in real time.

Criteria can be set to limit the feature to particular
flows of interest, which can aid in DoS detection.

Only the number of flows (TopN) and the sort criteria
(SortBy) need be set.

Top Flows is not intended as a mechanism for exporting
the entire netflow cache.


Egress flows.

This feature provides a mechanism to identify a flow
as either an ingress or an egress flow.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.inet.INET_ADDRESS_MIB import InetAddressType_Enum
from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum

class NfCacheTypes_Enum(Enum):
    """
    NfCacheTypes_Enum

    Defines different types of netflow cache.

    """

    MAIN = 0

    AS = 1

    PROTOCOLPORT = 2

    SOURCEPREFIX = 3

    DESTINATIONPREFIX = 4

    PREFIX = 5

    DESTINATIONONLY = 6

    SOURCEDESTINATION = 7

    FULLFLOW = 8

    ASTOS = 9

    PROTOCOLPORTTOS = 10

    SOURCEPREFIXTOS = 11

    DESTINATIONPREFIXTOS = 12

    PREFIXTOS = 13

    PREFIXPORT = 14

    BGPNEXTHOPTOS = 15

    EXPBGPPREFIX = 23


    @staticmethod
    def _meta_info():
        from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
        return meta._meta_table['NfCacheTypes_Enum']


class NfFlowDirectionTypes_Enum(Enum):
    """
    NfFlowDirectionTypes_Enum

    Defines different directions for a flow.

    """

    FLOWDIRNONE = 0

    FLOWDIRINGRESS = 1

    FLOWDIREGRESS = 2


    @staticmethod
    def _meta_info():
        from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
        return meta._meta_table['NfFlowDirectionTypes_Enum']


class NfInterfaceDirectionTypes_Enum(Enum):
    """
    NfInterfaceDirectionTypes_Enum

    Defines different types of interface configuration.

    """

    INTERFACEDIRNONE = 0

    INTERFACEDIRINGRESS = 1

    INTERFACEDIREGRESS = 2

    INTERFACEDIRBOTH = 3


    @staticmethod
    def _meta_info():
        from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
        return meta._meta_table['NfInterfaceDirectionTypes_Enum']


class NfProtocolTypes_Enum(Enum):
    """
    NfProtocolTypes_Enum

    Defines different types of protocol and port combination.

    """

    TCPTELNET = 1

    TCPFTP = 2

    TCPFTPD = 3

    TCPWWW = 4

    TCPSMTP = 5

    TCPX = 6

    TCPBGP = 7

    TCPNNTP = 8

    TCPFRAG = 9

    TCPOTHER = 10

    UDPDNS = 11

    UDPNTP = 12

    UDPTFTP = 13

    UDPFRAG = 14

    UDPOTHER = 15

    ICMP = 16

    IGMP = 17

    IPINIP = 18

    IPV6INIP = 19

    GRE = 20

    IPOTHER = 21

    ALL = 22


    @staticmethod
    def _meta_info():
        from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
        return meta._meta_table['NfProtocolTypes_Enum']


class NfTemplateTypes_Enum(Enum):
    """
    NfTemplateTypes_Enum

    Defines different types of Template.

    """

    TEMPLATE = 1

    OPTIONTEMPLATE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
        return meta._meta_table['NfTemplateTypes_Enum']


class NfTopFlowsSortTypes_Enum(Enum):
    """
    NfTopFlowsSortTypes_Enum

    Defines different types of sort order.

    """

    NOSORT = 1

    BYPACKETS = 2

    BYBYTES = 3


    @staticmethod
    def _meta_info():
        from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
        return meta._meta_table['NfTopFlowsSortTypes_Enum']



class CISCONETFLOWMIB(object):
    """
    
    
    .. attribute:: cnfcacheinfo
    
    	
    	**type**\: :py:class:`CnfCacheInfo <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfCacheInfo>`
    
    .. attribute:: cnfcibridgedflowstatsctrltable
    
    	This table controls the reporting of bridged flow statistics per vlan
    	**type**\: :py:class:`CnfCIBridgedFlowStatsCtrlTable <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfCIBridgedFlowStatsCtrlTable>`
    
    .. attribute:: cnfcicachetable
    
    	A table containing configuration and statistics per cache. Cache may be main cache or an aggregation cache
    	**type**\: :py:class:`CnfCICacheTable <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfCICacheTable>`
    
    .. attribute:: cnfciinterfacetable
    
    	This table provides Netflow Enable information per interface
    	**type**\: :py:class:`CnfCIInterfaceTable <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfCIInterfaceTable>`
    
    .. attribute:: cnfeicollectortable
    
    	A control table to configure the collectors that the netflow packets are exported to. The number of entries that can be configured for the cache type is limited by the value of cnfEIMaxCollectors
    	**type**\: :py:class:`CnfEICollectorTable <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfEICollectorTable>`
    
    .. attribute:: cnfeiexportinfotable
    
    	A table containing information about export configuration per cache type
    	**type**\: :py:class:`CnfEIExportInfoTable <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfEIExportInfoTable>`
    
    .. attribute:: cnfexportinfo
    
    	
    	**type**\: :py:class:`CnfExportInfo <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfExportInfo>`
    
    .. attribute:: cnfexportstatistics
    
    	
    	**type**\: :py:class:`CnfExportStatistics <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfExportStatistics>`
    
    .. attribute:: cnfexporttemplate
    
    	
    	**type**\: :py:class:`CnfExportTemplate <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfExportTemplate>`
    
    .. attribute:: cnfprotocolstatistics
    
    	
    	**type**\: :py:class:`CnfProtocolStatistics <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfProtocolStatistics>`
    
    .. attribute:: cnfpsprotocolstattable
    
    	A table containing statistics per protocol. Information sorted in this table is global in nature (i.e. it's updated for all line cards where netflow is enabled) and follows the Counter64 semantics as described in RFC 2578
    	**type**\: :py:class:`CnfPSProtocolStatTable <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfPSProtocolStatTable>`
    
    .. attribute:: cnftemplateexportinfotable
    
    	A control table providing information about version 9
    	**type**\: :py:class:`CnfTemplateExportInfoTable <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfTemplateExportInfoTable>`
    
    .. attribute:: cnftemplatetable
    
    	A control table to provide statistics of version 9 Flow and Option templates
    	**type**\: :py:class:`CnfTemplateTable <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfTemplateTable>`
    
    .. attribute:: cnftopflows
    
    	
    	**type**\: :py:class:`CnfTopFlows <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfTopFlows>`
    
    .. attribute:: cnftopflowstable
    
    	Table of flows which have accrued the highest packets or bytes. Each row in the table represents one flow from the cache
    	**type**\: :py:class:`CnfTopFlowsTable <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfTopFlowsTable>`
    
    

    """

    _prefix = 'cisco-netflow'
    _revision = '2006-04-27'

    def __init__(self):
        self.cnfcacheinfo = CISCONETFLOWMIB.CnfCacheInfo()
        self.cnfcacheinfo.parent = self
        self.cnfcibridgedflowstatsctrltable = CISCONETFLOWMIB.CnfCIBridgedFlowStatsCtrlTable()
        self.cnfcibridgedflowstatsctrltable.parent = self
        self.cnfcicachetable = CISCONETFLOWMIB.CnfCICacheTable()
        self.cnfcicachetable.parent = self
        self.cnfciinterfacetable = CISCONETFLOWMIB.CnfCIInterfaceTable()
        self.cnfciinterfacetable.parent = self
        self.cnfeicollectortable = CISCONETFLOWMIB.CnfEICollectorTable()
        self.cnfeicollectortable.parent = self
        self.cnfeiexportinfotable = CISCONETFLOWMIB.CnfEIExportInfoTable()
        self.cnfeiexportinfotable.parent = self
        self.cnfexportinfo = CISCONETFLOWMIB.CnfExportInfo()
        self.cnfexportinfo.parent = self
        self.cnfexportstatistics = CISCONETFLOWMIB.CnfExportStatistics()
        self.cnfexportstatistics.parent = self
        self.cnfexporttemplate = CISCONETFLOWMIB.CnfExportTemplate()
        self.cnfexporttemplate.parent = self
        self.cnfprotocolstatistics = CISCONETFLOWMIB.CnfProtocolStatistics()
        self.cnfprotocolstatistics.parent = self
        self.cnfpsprotocolstattable = CISCONETFLOWMIB.CnfPSProtocolStatTable()
        self.cnfpsprotocolstattable.parent = self
        self.cnftemplateexportinfotable = CISCONETFLOWMIB.CnfTemplateExportInfoTable()
        self.cnftemplateexportinfotable.parent = self
        self.cnftemplatetable = CISCONETFLOWMIB.CnfTemplateTable()
        self.cnftemplatetable.parent = self
        self.cnftopflows = CISCONETFLOWMIB.CnfTopFlows()
        self.cnftopflows.parent = self
        self.cnftopflowstable = CISCONETFLOWMIB.CnfTopFlowsTable()
        self.cnftopflowstable.parent = self


    class CnfCIBridgedFlowStatsCtrlTable(object):
        """
        This table controls the reporting of bridged flow statistics
        per vlan.
        
        .. attribute:: cnfcibridgedflowstatsctrlentry
        
        	A conceptual row in the cnfCIBridgedFlowStatsCtrlTable, containing the configuration of bridged flow statistics per vlan. When a vlan is created in a device supporting this table, a corresponding entry will be added to this  table
        	**type**\: list of :py:class:`CnfCIBridgedFlowStatsCtrlEntry <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfCIBridgedFlowStatsCtrlTable.CnfCIBridgedFlowStatsCtrlEntry>`
        
        

        """

        _prefix = 'cisco-netflow'
        _revision = '2006-04-27'

        def __init__(self):
            self.parent = None
            self.cnfcibridgedflowstatsctrlentry = YList()
            self.cnfcibridgedflowstatsctrlentry.parent = self
            self.cnfcibridgedflowstatsctrlentry.name = 'cnfcibridgedflowstatsctrlentry'


        class CnfCIBridgedFlowStatsCtrlEntry(object):
            """
            A conceptual row in the cnfCIBridgedFlowStatsCtrlTable,
            containing the configuration of bridged flow statistics
            per vlan. When a vlan is created in a device supporting
            this table, a corresponding entry will be added to this 
            table.
            
            .. attribute:: cnfcibridgedflowvlan
            
            	Indicates the Vlan number on which the reporting of bridged flow statistics is configured
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnfcibridgedflowstatscrtenable
            
            	Indicates whether the bridged flow creation is enabled for this vlan
            	**type**\: bool
            
            .. attribute:: cnfcibridgedflowstatsexpenable
            
            	Indicates whether the export of bridged flow statistics is enabled for this vlan
            	**type**\: bool
            
            

            """

            _prefix = 'cisco-netflow'
            _revision = '2006-04-27'

            def __init__(self):
                self.parent = None
                self.cnfcibridgedflowvlan = None
                self.cnfcibridgedflowstatscrtenable = None
                self.cnfcibridgedflowstatsexpenable = None

            @property
            def _common_path(self):
                if self.cnfcibridgedflowvlan is None:
                    raise YPYDataValidationError('Key property cnfcibridgedflowvlan is None')

                return '/CISCO-NETFLOW-MIB:CISCO-NETFLOW-MIB/CISCO-NETFLOW-MIB:cnfCIBridgedFlowStatsCtrlTable/CISCO-NETFLOW-MIB:cnfCIBridgedFlowStatsCtrlEntry[CISCO-NETFLOW-MIB:cnfCIBridgedFlowVlan = ' + str(self.cnfcibridgedflowvlan) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cnfcibridgedflowvlan is not None:
                    return True

                if self.cnfcibridgedflowstatscrtenable is not None:
                    return True

                if self.cnfcibridgedflowstatsexpenable is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
                return meta._meta_table['CISCONETFLOWMIB.CnfCIBridgedFlowStatsCtrlTable.CnfCIBridgedFlowStatsCtrlEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-NETFLOW-MIB:CISCO-NETFLOW-MIB/CISCO-NETFLOW-MIB:cnfCIBridgedFlowStatsCtrlTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnfcibridgedflowstatsctrlentry is not None:
                for child_ref in self.cnfcibridgedflowstatsctrlentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
            return meta._meta_table['CISCONETFLOWMIB.CnfCIBridgedFlowStatsCtrlTable']['meta_info']


    class CnfCICacheTable(object):
        """
        A table containing configuration and statistics per cache.
        Cache may be main cache or an aggregation cache.
        
        .. attribute:: cnfcicacheentry
        
        	A conceptual row in the cnfCICacheEntry
        	**type**\: list of :py:class:`CnfCICacheEntry <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfCICacheTable.CnfCICacheEntry>`
        
        

        """

        _prefix = 'cisco-netflow'
        _revision = '2006-04-27'

        def __init__(self):
            self.parent = None
            self.cnfcicacheentry = YList()
            self.cnfcicacheentry.parent = self
            self.cnfcicacheentry.name = 'cnfcicacheentry'


        class CnfCICacheEntry(object):
            """
            A conceptual row in the cnfCICacheEntry.
            
            .. attribute:: cnfcicachetype
            
            	The type of netflow cache.  NetFlow aggregation maintains one or more extra flow caches with different combinations of fields that determine which traditional flows are grouped together
            	**type**\: :py:class:`NfCacheTypes_Enum <ydk.models.netflow.CISCO_NETFLOW_MIB.NfCacheTypes_Enum>`
            
            .. attribute:: cnfciactiveflows
            
            	Number of currently active flow entries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnfciactivetimeout
            
            	The timeout period (in minutes) for removing active flows from the cache
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnfcicacheenable
            
            	Indicates whether netflow is enabled for this cache type
            	**type**\: bool
            
            .. attribute:: cnfcicacheentries
            
            	The number of entries that can be cached for this cache type. The accepted value could be limited based on the amount of memory available in the system
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnfciinactiveflows
            
            	Number of available flow entries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnfciinactivetimeout
            
            	The timeout period (in seconds) for removing inactive flows from the cache
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnfcimindestinationmask
            
            	Destination route's minimum configured mask bits. This is used to configure the minimum mask for Router Based Aggregation (RBA). Minimum masking capability is available only if RBA is enabled. A value of 0 indicates that this object is not applicable to this cache type
            	**type**\: int
            
            	**range:** 0..2040
            
            .. attribute:: cnfciminsourcemask
            
            	Source route's minimum configured mask bits. This is used to configure the minimum mask for Router Based Aggregation (RBA). Minimum masking capability is available only if RBA is enabled. A value of 0 indicates that this object is not applicable to this cache type
            	**type**\: int
            
            	**range:** 0..2040
            
            

            """

            _prefix = 'cisco-netflow'
            _revision = '2006-04-27'

            def __init__(self):
                self.parent = None
                self.cnfcicachetype = None
                self.cnfciactiveflows = None
                self.cnfciactivetimeout = None
                self.cnfcicacheenable = None
                self.cnfcicacheentries = None
                self.cnfciinactiveflows = None
                self.cnfciinactivetimeout = None
                self.cnfcimindestinationmask = None
                self.cnfciminsourcemask = None

            @property
            def _common_path(self):
                if self.cnfcicachetype is None:
                    raise YPYDataValidationError('Key property cnfcicachetype is None')

                return '/CISCO-NETFLOW-MIB:CISCO-NETFLOW-MIB/CISCO-NETFLOW-MIB:cnfCICacheTable/CISCO-NETFLOW-MIB:cnfCICacheEntry[CISCO-NETFLOW-MIB:cnfCICacheType = ' + str(self.cnfcicachetype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cnfcicachetype is not None:
                    return True

                if self.cnfciactiveflows is not None:
                    return True

                if self.cnfciactivetimeout is not None:
                    return True

                if self.cnfcicacheenable is not None:
                    return True

                if self.cnfcicacheentries is not None:
                    return True

                if self.cnfciinactiveflows is not None:
                    return True

                if self.cnfciinactivetimeout is not None:
                    return True

                if self.cnfcimindestinationmask is not None:
                    return True

                if self.cnfciminsourcemask is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
                return meta._meta_table['CISCONETFLOWMIB.CnfCICacheTable.CnfCICacheEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-NETFLOW-MIB:CISCO-NETFLOW-MIB/CISCO-NETFLOW-MIB:cnfCICacheTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnfcicacheentry is not None:
                for child_ref in self.cnfcicacheentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
            return meta._meta_table['CISCONETFLOWMIB.CnfCICacheTable']['meta_info']


    class CnfCIInterfaceTable(object):
        """
        This table provides Netflow Enable information per interface.
        
        .. attribute:: cnfciinterfaceentry
        
        	A conceptual row in the cnfCIInterfaceEntry
        	**type**\: list of :py:class:`CnfCIInterfaceEntry <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfCIInterfaceTable.CnfCIInterfaceEntry>`
        
        

        """

        _prefix = 'cisco-netflow'
        _revision = '2006-04-27'

        def __init__(self):
            self.parent = None
            self.cnfciinterfaceentry = YList()
            self.cnfciinterfaceentry.parent = self
            self.cnfciinterfaceentry.name = 'cnfciinterfaceentry'


        class CnfCIInterfaceEntry(object):
            """
            A conceptual row in the cnfCIInterfaceEntry.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cnfcimcastnetflowenable
            
            	Indicates whether the multicast netflow accounting feature is enabled for this interface, and if so, in which  directions
            	**type**\: :py:class:`NfInterfaceDirectionTypes_Enum <ydk.models.netflow.CISCO_NETFLOW_MIB.NfInterfaceDirectionTypes_Enum>`
            
            .. attribute:: cnfcinetflowenable
            
            	Indicates whether the netflow feature is enabled for this interface, and if so, in which directions
            	**type**\: :py:class:`NfInterfaceDirectionTypes_Enum <ydk.models.netflow.CISCO_NETFLOW_MIB.NfInterfaceDirectionTypes_Enum>`
            
            

            """

            _prefix = 'cisco-netflow'
            _revision = '2006-04-27'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cnfcimcastnetflowenable = None
                self.cnfcinetflowenable = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-NETFLOW-MIB:CISCO-NETFLOW-MIB/CISCO-NETFLOW-MIB:cnfCIInterfaceTable/CISCO-NETFLOW-MIB:cnfCIInterfaceEntry[CISCO-NETFLOW-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.cnfcimcastnetflowenable is not None:
                    return True

                if self.cnfcinetflowenable is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
                return meta._meta_table['CISCONETFLOWMIB.CnfCIInterfaceTable.CnfCIInterfaceEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-NETFLOW-MIB:CISCO-NETFLOW-MIB/CISCO-NETFLOW-MIB:cnfCIInterfaceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnfciinterfaceentry is not None:
                for child_ref in self.cnfciinterfaceentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
            return meta._meta_table['CISCONETFLOWMIB.CnfCIInterfaceTable']['meta_info']


    class CnfCacheInfo(object):
        """
        
        
        .. attribute:: cnfcimcastnetflowrpffailedenable
        
        	Indicates whether netflow accounting for multicast data that fails the reverse path forwarding (RPF) check is enabled
        	**type**\: bool
        
        

        """

        _prefix = 'cisco-netflow'
        _revision = '2006-04-27'

        def __init__(self):
            self.parent = None
            self.cnfcimcastnetflowrpffailedenable = None

        @property
        def _common_path(self):

            return '/CISCO-NETFLOW-MIB:CISCO-NETFLOW-MIB/CISCO-NETFLOW-MIB:cnfCacheInfo'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnfcimcastnetflowrpffailedenable is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
            return meta._meta_table['CISCONETFLOWMIB.CnfCacheInfo']['meta_info']


    class CnfEICollectorTable(object):
        """
        A control table to configure the collectors that the netflow
        packets are exported to. The number of entries that can be
        configured for the cache type is limited by the value of
        cnfEIMaxCollectors.
        
        .. attribute:: cnfeicollectorentry
        
        	A conceptual row in the cnfEICollectorEntry
        	**type**\: list of :py:class:`CnfEICollectorEntry <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfEICollectorTable.CnfEICollectorEntry>`
        
        

        """

        _prefix = 'cisco-netflow'
        _revision = '2006-04-27'

        def __init__(self):
            self.parent = None
            self.cnfeicollectorentry = YList()
            self.cnfeicollectorentry.parent = self
            self.cnfeicollectorentry.name = 'cnfeicollectorentry'


        class CnfEICollectorEntry(object):
            """
            A conceptual row in the cnfEICollectorEntry.
            
            .. attribute:: cnfcicachetype
            
            	
            	**type**\: :py:class:`NfCacheTypes_Enum <ydk.models.netflow.CISCO_NETFLOW_MIB.NfCacheTypes_Enum>`
            
            .. attribute:: cnfeicollectoraddress
            
            	The Internet address of the collector. This is the address which the Netflow data is exported to
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cnfeicollectoraddresstype
            
            	The type of Internet address used by this entry
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cnfeicollectorport
            
            	The transport port of the collector which the Netflow data is exported to
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cnfeicollectorstatus
            
            	This object is used to create or delete an entry in the cnfEICollectorTable.  \* A row may be created using the 'CreateAndGo' option. When   the row is successfully created, the RowStatus would be   set to 'active' by the agent.  \* A row may be deleted by setting the RowStatus to 'destroy'
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'cisco-netflow'
            _revision = '2006-04-27'

            def __init__(self):
                self.parent = None
                self.cnfcicachetype = None
                self.cnfeicollectoraddress = None
                self.cnfeicollectoraddresstype = None
                self.cnfeicollectorport = None
                self.cnfeicollectorstatus = None

            @property
            def _common_path(self):
                if self.cnfcicachetype is None:
                    raise YPYDataValidationError('Key property cnfcicachetype is None')
                if self.cnfeicollectoraddress is None:
                    raise YPYDataValidationError('Key property cnfeicollectoraddress is None')
                if self.cnfeicollectoraddresstype is None:
                    raise YPYDataValidationError('Key property cnfeicollectoraddresstype is None')
                if self.cnfeicollectorport is None:
                    raise YPYDataValidationError('Key property cnfeicollectorport is None')

                return '/CISCO-NETFLOW-MIB:CISCO-NETFLOW-MIB/CISCO-NETFLOW-MIB:cnfEICollectorTable/CISCO-NETFLOW-MIB:cnfEICollectorEntry[CISCO-NETFLOW-MIB:cnfCICacheType = ' + str(self.cnfcicachetype) + '][CISCO-NETFLOW-MIB:cnfEICollectorAddress = ' + str(self.cnfeicollectoraddress) + '][CISCO-NETFLOW-MIB:cnfEICollectorAddressType = ' + str(self.cnfeicollectoraddresstype) + '][CISCO-NETFLOW-MIB:cnfEICollectorPort = ' + str(self.cnfeicollectorport) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cnfcicachetype is not None:
                    return True

                if self.cnfeicollectoraddress is not None:
                    return True

                if self.cnfeicollectoraddresstype is not None:
                    return True

                if self.cnfeicollectorport is not None:
                    return True

                if self.cnfeicollectorstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
                return meta._meta_table['CISCONETFLOWMIB.CnfEICollectorTable.CnfEICollectorEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-NETFLOW-MIB:CISCO-NETFLOW-MIB/CISCO-NETFLOW-MIB:cnfEICollectorTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnfeicollectorentry is not None:
                for child_ref in self.cnfeicollectorentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
            return meta._meta_table['CISCONETFLOWMIB.CnfEICollectorTable']['meta_info']


    class CnfEIExportInfoTable(object):
        """
        A table containing information about export configuration per
        cache type.
        
        .. attribute:: cnfeiexportinfoentry
        
        	A conceptual row in the cnfEIExportInfoEntry
        	**type**\: list of :py:class:`CnfEIExportInfoEntry <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfEIExportInfoTable.CnfEIExportInfoEntry>`
        
        

        """

        _prefix = 'cisco-netflow'
        _revision = '2006-04-27'

        def __init__(self):
            self.parent = None
            self.cnfeiexportinfoentry = YList()
            self.cnfeiexportinfoentry.parent = self
            self.cnfeiexportinfoentry.name = 'cnfeiexportinfoentry'


        class CnfEIExportInfoEntry(object):
            """
            A conceptual row in the cnfEIExportInfoEntry.
            
            .. attribute:: cnfcicachetype
            
            	
            	**type**\: :py:class:`NfCacheTypes_Enum <ydk.models.netflow.CISCO_NETFLOW_MIB.NfCacheTypes_Enum>`
            
            .. attribute:: cnfeibgpnexthop
            
            	This object enables collection of BGP Next Hops. cnfEIPeerAS, cnfEIOriginAS and cnfEIBgpNextHop are interdependent
            	**type**\: bool
            
            .. attribute:: cnfeiexportversion
            
            	The NetFlow data export version
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnfeioriginas
            
            	This object enables collection of AS numbers from an origin autonomous system. cnfEIPeerAS, cnfEIOriginAS and cnfEIBgpNextHop are interdependent
            	**type**\: bool
            
            .. attribute:: cnfeipeeras
            
            	This object enables collection of AS numbers from a peer autonomous system. cnfEIPeerAS, cnfEIOriginAS and cnfEIBgpNextHop are interdependent
            	**type**\: bool
            
            

            """

            _prefix = 'cisco-netflow'
            _revision = '2006-04-27'

            def __init__(self):
                self.parent = None
                self.cnfcicachetype = None
                self.cnfeibgpnexthop = None
                self.cnfeiexportversion = None
                self.cnfeioriginas = None
                self.cnfeipeeras = None

            @property
            def _common_path(self):
                if self.cnfcicachetype is None:
                    raise YPYDataValidationError('Key property cnfcicachetype is None')

                return '/CISCO-NETFLOW-MIB:CISCO-NETFLOW-MIB/CISCO-NETFLOW-MIB:cnfEIExportInfoTable/CISCO-NETFLOW-MIB:cnfEIExportInfoEntry[CISCO-NETFLOW-MIB:cnfCICacheType = ' + str(self.cnfcicachetype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cnfcicachetype is not None:
                    return True

                if self.cnfeibgpnexthop is not None:
                    return True

                if self.cnfeiexportversion is not None:
                    return True

                if self.cnfeioriginas is not None:
                    return True

                if self.cnfeipeeras is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
                return meta._meta_table['CISCONETFLOWMIB.CnfEIExportInfoTable.CnfEIExportInfoEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-NETFLOW-MIB:CISCO-NETFLOW-MIB/CISCO-NETFLOW-MIB:cnfEIExportInfoTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnfeiexportinfoentry is not None:
                for child_ref in self.cnfeiexportinfoentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
            return meta._meta_table['CISCONETFLOWMIB.CnfEIExportInfoTable']['meta_info']


    class CnfExportInfo(object):
        """
        
        
        .. attribute:: cnfeimaxcollectors
        
        	Maximum number of entries allowed in the cnfEICollectorTable for each cache type. A zero indicates export is not supported in the device. The agent should set this value during initialization, and the value for this object cannot be changed during the system's operation
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-netflow'
        _revision = '2006-04-27'

        def __init__(self):
            self.parent = None
            self.cnfeimaxcollectors = None

        @property
        def _common_path(self):

            return '/CISCO-NETFLOW-MIB:CISCO-NETFLOW-MIB/CISCO-NETFLOW-MIB:cnfExportInfo'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnfeimaxcollectors is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
            return meta._meta_table['CISCONETFLOWMIB.CnfExportInfo']['meta_info']


    class CnfExportStatistics(object):
        """
        
        
        .. attribute:: cnfesexportrate
        
        	Number of Bytes exported per second
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cnfespktsdropped
        
        	Number of export packets which were dropped at the time of ipwrite operation. The reasons for this failure are no FIB, adjacency failure, MTU failed, enqueue failed, IPC failed etc
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cnfespktsexported
        
        	Number of packets (udp datagrams) which were exported
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cnfespktsfailed
        
        	Number of times a flow record could not be exported because of a pak allocation failure
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cnfesrecordsexported
        
        	Number of flow statistics records which were exported
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cnfessampledpacket
        
        	Number of Sampled Packet
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-netflow'
        _revision = '2006-04-27'

        def __init__(self):
            self.parent = None
            self.cnfesexportrate = None
            self.cnfespktsdropped = None
            self.cnfespktsexported = None
            self.cnfespktsfailed = None
            self.cnfesrecordsexported = None
            self.cnfessampledpacket = None

        @property
        def _common_path(self):

            return '/CISCO-NETFLOW-MIB:CISCO-NETFLOW-MIB/CISCO-NETFLOW-MIB:cnfExportStatistics'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnfesexportrate is not None:
                return True

            if self.cnfespktsdropped is not None:
                return True

            if self.cnfespktsexported is not None:
                return True

            if self.cnfespktsfailed is not None:
                return True

            if self.cnfesrecordsexported is not None:
                return True

            if self.cnfessampledpacket is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
            return meta._meta_table['CISCONETFLOWMIB.CnfExportStatistics']['meta_info']


    class CnfExportTemplate(object):
        """
        
        
        .. attribute:: cnftemplateoptionsflag
        
        	Object to indicate Sub\- technologies in option template
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-netflow'
        _revision = '2006-04-27'

        def __init__(self):
            self.parent = None
            self.cnftemplateoptionsflag = None

        @property
        def _common_path(self):

            return '/CISCO-NETFLOW-MIB:CISCO-NETFLOW-MIB/CISCO-NETFLOW-MIB:cnfExportTemplate'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnftemplateoptionsflag is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
            return meta._meta_table['CISCONETFLOWMIB.CnfExportTemplate']['meta_info']


    class CnfPSProtocolStatTable(object):
        """
        A table containing statistics per protocol.
        Information sorted in this table is global in nature (i.e. it's
        updated for all line cards where netflow is enabled) and
        follows the Counter64 semantics as described in RFC 2578.
        
        .. attribute:: cnfpsprotocolstatentry
        
        	A conceptual row in the CnfPSProtocolStatEntry
        	**type**\: list of :py:class:`CnfPSProtocolStatEntry <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfPSProtocolStatTable.CnfPSProtocolStatEntry>`
        
        

        """

        _prefix = 'cisco-netflow'
        _revision = '2006-04-27'

        def __init__(self):
            self.parent = None
            self.cnfpsprotocolstatentry = YList()
            self.cnfpsprotocolstatentry.parent = self
            self.cnfpsprotocolstatentry.name = 'cnfpsprotocolstatentry'


        class CnfPSProtocolStatEntry(object):
            """
            A conceptual row in the CnfPSProtocolStatEntry.
            
            .. attribute:: cnfpsprotocoltype
            
            	This object is used as INDEX for protocol statistic table. Protocol type consists of groups based on well known ports and protocols
            	**type**\: :py:class:`NfProtocolTypes_Enum <ydk.models.netflow.CISCO_NETFLOW_MIB.NfProtocolTypes_Enum>`
            
            .. attribute:: cnfpsactive
            
            	This is a summation of active time of all flows belonging to the same protocol and port in milliseconds. The time between first switched packet and last switched packet is measured as the active time of a flow
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cnfpsbytes
            
            	Number of Bytes belonging to the same protocol and port, which were switched by netflow enabled interface(s). This counter contains the number of Packets switched by all netflow enabled line cards
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cnfpsexpiredflows
            
            	Number of flows belonging to the same protocol and port that were expired. This counter is incremented when a flow expires due to some reason like time out of flows, event based aging etc
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cnfpsinactive
            
            	This is a summation of inactive time of all flows belonging to the same protocol and port in milliseconds. The time between the last switched packet and expiry of a flow is measured as the inactive time of a flow
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cnfpspackets
            
            	Number of Packets belonging to the same protocol and port which were switched by netflow enabled interface(s). This counter contains the number of Packets switched by all netflow enabled line cards
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'cisco-netflow'
            _revision = '2006-04-27'

            def __init__(self):
                self.parent = None
                self.cnfpsprotocoltype = None
                self.cnfpsactive = None
                self.cnfpsbytes = None
                self.cnfpsexpiredflows = None
                self.cnfpsinactive = None
                self.cnfpspackets = None

            @property
            def _common_path(self):
                if self.cnfpsprotocoltype is None:
                    raise YPYDataValidationError('Key property cnfpsprotocoltype is None')

                return '/CISCO-NETFLOW-MIB:CISCO-NETFLOW-MIB/CISCO-NETFLOW-MIB:cnfPSProtocolStatTable/CISCO-NETFLOW-MIB:cnfPSProtocolStatEntry[CISCO-NETFLOW-MIB:cnfPSProtocolType = ' + str(self.cnfpsprotocoltype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cnfpsprotocoltype is not None:
                    return True

                if self.cnfpsactive is not None:
                    return True

                if self.cnfpsbytes is not None:
                    return True

                if self.cnfpsexpiredflows is not None:
                    return True

                if self.cnfpsinactive is not None:
                    return True

                if self.cnfpspackets is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
                return meta._meta_table['CISCONETFLOWMIB.CnfPSProtocolStatTable.CnfPSProtocolStatEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-NETFLOW-MIB:CISCO-NETFLOW-MIB/CISCO-NETFLOW-MIB:cnfPSProtocolStatTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnfpsprotocolstatentry is not None:
                for child_ref in self.cnfpsprotocolstatentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
            return meta._meta_table['CISCONETFLOWMIB.CnfPSProtocolStatTable']['meta_info']


    class CnfProtocolStatistics(object):
        """
        
        
        .. attribute:: cnfpslastclearelapsedtime
        
        	Object indicates time in millisecond since the last clearing time of protocol statistics
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cnfpspacketsizedistribution
        
        	A string contain IP Packet Size Distribution statistics. Distribution grouping are following \:1\-32   64   96  128 160  192  224  256 288  320  352 384  416  448  480  512 544  576 1024 1536 2048 2560 3072 3584 4096 4608. Value for each group will be expressed in 2 bytes (in Network byte order) and need to divide by 1000 to get the exact value given by CLI using show ip cache flow command
        	**type**\: str
        
        	**range:** 52
        
        

        """

        _prefix = 'cisco-netflow'
        _revision = '2006-04-27'

        def __init__(self):
            self.parent = None
            self.cnfpslastclearelapsedtime = None
            self.cnfpspacketsizedistribution = None

        @property
        def _common_path(self):

            return '/CISCO-NETFLOW-MIB:CISCO-NETFLOW-MIB/CISCO-NETFLOW-MIB:cnfProtocolStatistics'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnfpslastclearelapsedtime is not None:
                return True

            if self.cnfpspacketsizedistribution is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
            return meta._meta_table['CISCONETFLOWMIB.CnfProtocolStatistics']['meta_info']


    class CnfTemplateExportInfoTable(object):
        """
        A control table providing information about version 9.
        
        .. attribute:: cnftemplateexportinfoentry
        
        	A conceptual row in the cnfTemplateExportInfoEntry
        	**type**\: list of :py:class:`CnfTemplateExportInfoEntry <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfTemplateExportInfoTable.CnfTemplateExportInfoEntry>`
        
        

        """

        _prefix = 'cisco-netflow'
        _revision = '2006-04-27'

        def __init__(self):
            self.parent = None
            self.cnftemplateexportinfoentry = YList()
            self.cnftemplateexportinfoentry.parent = self
            self.cnftemplateexportinfoentry.name = 'cnftemplateexportinfoentry'


        class CnfTemplateExportInfoEntry(object):
            """
            A conceptual row in the cnfTemplateExportInfoEntry.
            
            .. attribute:: cnfcicachetype
            
            	
            	**type**\: :py:class:`NfCacheTypes_Enum <ydk.models.netflow.CISCO_NETFLOW_MIB.NfCacheTypes_Enum>`
            
            .. attribute:: cnftemplateexportver9enable
            
            	Object to indicate whether version 9 export is configured or not
            	**type**\: bool
            
            .. attribute:: cnftemplateexportver9optrefreshrate
            
            	Option refresh rate. Options are resent after this many packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnftemplateexportver9opttimeout
            
            	Export option time out. Options are resent after this time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnftemplateexportver9tplrefreshrate
            
            	Template refresh rate. Templates are resent after this many packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnftemplateexportver9tpltimeout
            
            	Export template time out. Templates are resent after this time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-netflow'
            _revision = '2006-04-27'

            def __init__(self):
                self.parent = None
                self.cnfcicachetype = None
                self.cnftemplateexportver9enable = None
                self.cnftemplateexportver9optrefreshrate = None
                self.cnftemplateexportver9opttimeout = None
                self.cnftemplateexportver9tplrefreshrate = None
                self.cnftemplateexportver9tpltimeout = None

            @property
            def _common_path(self):
                if self.cnfcicachetype is None:
                    raise YPYDataValidationError('Key property cnfcicachetype is None')

                return '/CISCO-NETFLOW-MIB:CISCO-NETFLOW-MIB/CISCO-NETFLOW-MIB:cnfTemplateExportInfoTable/CISCO-NETFLOW-MIB:cnfTemplateExportInfoEntry[CISCO-NETFLOW-MIB:cnfCICacheType = ' + str(self.cnfcicachetype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cnfcicachetype is not None:
                    return True

                if self.cnftemplateexportver9enable is not None:
                    return True

                if self.cnftemplateexportver9optrefreshrate is not None:
                    return True

                if self.cnftemplateexportver9opttimeout is not None:
                    return True

                if self.cnftemplateexportver9tplrefreshrate is not None:
                    return True

                if self.cnftemplateexportver9tpltimeout is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
                return meta._meta_table['CISCONETFLOWMIB.CnfTemplateExportInfoTable.CnfTemplateExportInfoEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-NETFLOW-MIB:CISCO-NETFLOW-MIB/CISCO-NETFLOW-MIB:cnfTemplateExportInfoTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnftemplateexportinfoentry is not None:
                for child_ref in self.cnftemplateexportinfoentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
            return meta._meta_table['CISCONETFLOWMIB.CnfTemplateExportInfoTable']['meta_info']


    class CnfTemplateTable(object):
        """
        A control table to provide statistics of version 9
        Flow and Option templates.
        
        .. attribute:: cnftemplateentry
        
        	A conceptual row in the cnfTemplateEntry
        	**type**\: list of :py:class:`CnfTemplateEntry <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfTemplateTable.CnfTemplateEntry>`
        
        

        """

        _prefix = 'cisco-netflow'
        _revision = '2006-04-27'

        def __init__(self):
            self.parent = None
            self.cnftemplateentry = YList()
            self.cnftemplateentry.parent = self
            self.cnftemplateentry.name = 'cnftemplateentry'


        class CnfTemplateEntry(object):
            """
            A conceptual row in the cnfTemplateEntry.
            
            .. attribute:: cnftemplatetype
            
            	Defines the structure and interpretation of fields in a data record and serves as an INDEX in this table. Version 9 has two types of Templates\: Flow Templates and Option Templates
            	**type**\: :py:class:`NfTemplateTypes_Enum <ydk.models.netflow.CISCO_NETFLOW_MIB.NfTemplateTypes_Enum>`
            
            .. attribute:: cnftemplateactive
            
            	Number of active templates
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnftemplateadded
            
            	Number of templates added
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnftemplateagerpolls
            
            	Number of template ager polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-netflow'
            _revision = '2006-04-27'

            def __init__(self):
                self.parent = None
                self.cnftemplatetype = None
                self.cnftemplateactive = None
                self.cnftemplateadded = None
                self.cnftemplateagerpolls = None

            @property
            def _common_path(self):
                if self.cnftemplatetype is None:
                    raise YPYDataValidationError('Key property cnftemplatetype is None')

                return '/CISCO-NETFLOW-MIB:CISCO-NETFLOW-MIB/CISCO-NETFLOW-MIB:cnfTemplateTable/CISCO-NETFLOW-MIB:cnfTemplateEntry[CISCO-NETFLOW-MIB:cnfTemplateType = ' + str(self.cnftemplatetype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cnftemplatetype is not None:
                    return True

                if self.cnftemplateactive is not None:
                    return True

                if self.cnftemplateadded is not None:
                    return True

                if self.cnftemplateagerpolls is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
                return meta._meta_table['CISCONETFLOWMIB.CnfTemplateTable.CnfTemplateEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-NETFLOW-MIB:CISCO-NETFLOW-MIB/CISCO-NETFLOW-MIB:cnfTemplateTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnftemplateentry is not None:
                for child_ref in self.cnftemplateentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
            return meta._meta_table['CISCONETFLOWMIB.CnfTemplateTable']['meta_info']


    class CnfTopFlows(object):
        """
        
        
        .. attribute:: cnftopflowsavailableflows
        
        	The number of entries currently available in cnfTopFlowsTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cnftopflowscachetimeout
        
        	Top Flows Cache timeout. Top flows are cached for this length of time and not recalculated. Configure a high value to ensure the cache does not change during long queries. Setting this object (to any value) will expire the cache
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cnftopflowsgenerate
        
        	A control variable used to generate the Top Flows.   Setting this object to 'true' will generate the Top Flows  and populate the Top Flows report in cnfTopFlowsTable   unless cnfTopFlowsNextGenActionEffect is supported and the value of cnfTopFlowsNextGenActionEffect is 'noOp'.  Setting this object to 'false' has no effect.  When read, this object always returns 'false'
        	**type**\: bool
        
        .. attribute:: cnftopflowsmatchclass
        
        	Class name to match. Leave blank to disable this match criteria
        	**type**\: str
        
        	**pattern:** \\p{IsBasicLatin}{0,255}
        
        .. attribute:: cnftopflowsmatchdirection
        
        	Flow direction to match. A value of 0 disables this match criteria
        	**type**\: :py:class:`NfFlowDirectionTypes_Enum <ydk.models.netflow.CISCO_NETFLOW_MIB.NfFlowDirectionTypes_Enum>`
        
        .. attribute:: cnftopflowsmatchdstaddress
        
        	Destination address prefix to match
        	**type**\: str
        
        	**range:** 0..255
        
        .. attribute:: cnftopflowsmatchdstaddressmask
        
        	The length of the match destination address prefix. This prefix length must be consistent with the address type specified in cnfTopFlowsMatchDstAddressType. A length of zero only matches the all\-zero address of the specified type
        	**type**\: int
        
        	**range:** 0..2040
        
        .. attribute:: cnftopflowsmatchdstaddresstype
        
        	Destination address type to match. A value of 'unknown' (ie, 0) indicates the destination address is not used as a top flows match criteria, and clears the cnfTopFlowsMatchDstAddress and cnfTopFlowsMatchDstAddressMask configuration
        	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
        
        .. attribute:: cnftopflowsmatchdstas
        
        	Destination AS number to match. A value of \-1 disables this match criteria
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: cnftopflowsmatchdstporthi
        
        	The maximum value that the layer\-4 destination port number in the flow must have in order to match. A value of \-1 disables this match criteria
        	**type**\: int
        
        	**range:** \-1..65535
        
        .. attribute:: cnftopflowsmatchdstportlo
        
        	The minimum value that the layer\-4 destination port number in the flow must have in order to match. A value of \-1 disables this match criteria
        	**type**\: int
        
        	**range:** \-1..65535
        
        .. attribute:: cnftopflowsmatchingflows
        
        	Total number of matching flows in the netflow cache
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cnftopflowsmatchinputif
        
        	Input interface to match. A value of 0 disables this match criteria
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: cnftopflowsmatchmaxbytes
        
        	Maximum bytes to match. A value of 0 disables this match criteria
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cnftopflowsmatchmaxpackets
        
        	Maximum packets to match. A value of 0 disables this match criteria
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cnftopflowsmatchminbytes
        
        	Minimum bytes to match. A value of 0 disables this match criteria
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cnftopflowsmatchminpackets
        
        	Minimum packets to match. A value of 0 disables this match criteria
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cnftopflowsmatchnhaddress
        
        	Nexthop address prefix to match
        	**type**\: str
        
        	**range:** 0..255
        
        .. attribute:: cnftopflowsmatchnhaddressmask
        
        	The length of the match nexthop address Prefix. This prefix length must be consistent with the address type specified in cnfTopFlowsMatchNhAddressType. A length of zero only matches the all\-zero address of the specified type
        	**type**\: int
        
        	**range:** 0..2040
        
        .. attribute:: cnftopflowsmatchnhaddresstype
        
        	Nexthop address type to match. A value of 'unknown' (ie, 0) indicates the nexthop address is not used as a top flows match criteria, and clears the cnfTopFlowsMatchNhAddress and cnfTopFlowsMatchNhAddressMask configuration
        	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
        
        .. attribute:: cnftopflowsmatchoutputif
        
        	Output interface to match. A value of 0 disables this match criteria
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: cnftopflowsmatchprotocol
        
        	Protocol to match. A value of \-1 disables this match criteria
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: cnftopflowsmatchsampler
        
        	Sampler name to match. Leave blank to disable this match criteria
        	**type**\: str
        
        	**pattern:** \\p{IsBasicLatin}{0,255}
        
        .. attribute:: cnftopflowsmatchsrcaddress
        
        	Source address prefix to match
        	**type**\: str
        
        	**range:** 0..255
        
        .. attribute:: cnftopflowsmatchsrcaddressmask
        
        	The length of the match source address prefix. This prefix length must be consistent with the address type specified in cnfTopFlowsMatchSrcAddressType. A length of zero only matches the all\-zero address of the specified type
        	**type**\: int
        
        	**range:** 0..2040
        
        .. attribute:: cnftopflowsmatchsrcaddresstype
        
        	Source address type to match. A value of 'unknown' (ie, 0) indicates the source address is not used as a top flows match criteria, and clears the cnfTopFlowsMatchSrcAddress and cnfTopFlowsMatchSrcAddressMask configuration
        	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
        
        .. attribute:: cnftopflowsmatchsrcas
        
        	Source AS number to match. A value of \-1 disables this match criteria
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: cnftopflowsmatchsrcporthi
        
        	The maximum value that the layer\-4 source port number in the flow must have in order to match. A value of \-1 disables this match criteria
        	**type**\: int
        
        	**range:** \-1..65535
        
        .. attribute:: cnftopflowsmatchsrcportlo
        
        	The minimum value that the layer\-4 source port number in the flow must have in order to match. A value of \-1 disables this match criteria
        	**type**\: int
        
        	**range:** \-1..65535
        
        .. attribute:: cnftopflowsmatchtosbyte
        
        	TOS byte to match. A value of \-1 disables this match criteria
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: cnftopflowsnextgenactioneffect
        
        	Indicates the action effect on the system when the  cnfTopFlowsGenerate is set to 'true'.    'noOp' \-\- indicate that the system will make no operation            when the cnfTopFlowsGenerate is set to 'true'.         Examples when this object could return 'noOp' are\:         1. the system is still in the top flow generation             process.          2. the system will not generate the top flows             report when the value of             cnfTopFlowsReportAvailable is 'true'.  'generate' \-\- indicates that the system will start the top                flows generation process if the                cntTopFlowsGenerate is set to 'true'.         Examples when this object could return 'generate'          are\:         1. When the value of cnfTopFlowsReportAvailable is             'false'.           2. The system will always generate the top flow            report when cnfTopFlowsGenerate is set to             'true'
        	**type**\: :py:class:`CnfTopFlowsNextGenActionEffect_Enum <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfTopFlows.CnfTopFlowsNextGenActionEffect_Enum>`
        
        .. attribute:: cnftopflowsreportavailable
        
        	Indicates whether the Top Flows report has been  successfully generated and is available in  cnfTopFlowsTable.   When the value of this object is 'true', the  top flows report is available in cnfTopFlowsTable.  When the value of this object is 'false', there is no top flows report available in cnfTopFlowsTable.  For Example\:     1. When top flows report has not been generated or         is currently in the generation process.     2. When the top flows has been purged due to        the modification of a matching criteria or the        expiration of top flow cache timeout
        	**type**\: bool
        
        .. attribute:: cnftopflowsreportsource
        
        	Indicates the source of Top Flows report generation for  the entries populated in cnfTopFlowsTable.  'other'    \- The Top Flows are not available or the source               of the Top Flows cannot be identified.  'hardware' \- The Top Flows report has been generated based               on the flows detected by the hardware platform              with netflow capabilities.  'software' \- The Top Flows report has been generated based              on the flows detected by the software.  'both'     \- The Top Flows report is an integrated list of               Top Flows detected by both the hardware              platform and the software
        	**type**\: :py:class:`CnfTopFlowsReportSource_Enum <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfTopFlows.CnfTopFlowsReportSource_Enum>`
        
        .. attribute:: cnftopflowssortby
        
        	Indicates how the entries in cnfTopFLowsTable are to be sorted. A value of 'noSort' disables Top Flows
        	**type**\: :py:class:`NfTopFlowsSortTypes_Enum <ydk.models.netflow.CISCO_NETFLOW_MIB.NfTopFlowsSortTypes_Enum>`
        
        .. attribute:: cnftopflowstimestamp
        
        	Indicates the time when cnfTopFlowsTable was last updated
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cnftopflowstopn
        
        	Maximum number of top flows to calculate. A value of 0 disables the Top Flows feature
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cnftopflowstotalflows
        
        	Total number of flows in the netflow cache
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-netflow'
        _revision = '2006-04-27'

        def __init__(self):
            self.parent = None
            self.cnftopflowsavailableflows = None
            self.cnftopflowscachetimeout = None
            self.cnftopflowsgenerate = None
            self.cnftopflowsmatchclass = None
            self.cnftopflowsmatchdirection = None
            self.cnftopflowsmatchdstaddress = None
            self.cnftopflowsmatchdstaddressmask = None
            self.cnftopflowsmatchdstaddresstype = None
            self.cnftopflowsmatchdstas = None
            self.cnftopflowsmatchdstporthi = None
            self.cnftopflowsmatchdstportlo = None
            self.cnftopflowsmatchingflows = None
            self.cnftopflowsmatchinputif = None
            self.cnftopflowsmatchmaxbytes = None
            self.cnftopflowsmatchmaxpackets = None
            self.cnftopflowsmatchminbytes = None
            self.cnftopflowsmatchminpackets = None
            self.cnftopflowsmatchnhaddress = None
            self.cnftopflowsmatchnhaddressmask = None
            self.cnftopflowsmatchnhaddresstype = None
            self.cnftopflowsmatchoutputif = None
            self.cnftopflowsmatchprotocol = None
            self.cnftopflowsmatchsampler = None
            self.cnftopflowsmatchsrcaddress = None
            self.cnftopflowsmatchsrcaddressmask = None
            self.cnftopflowsmatchsrcaddresstype = None
            self.cnftopflowsmatchsrcas = None
            self.cnftopflowsmatchsrcporthi = None
            self.cnftopflowsmatchsrcportlo = None
            self.cnftopflowsmatchtosbyte = None
            self.cnftopflowsnextgenactioneffect = None
            self.cnftopflowsreportavailable = None
            self.cnftopflowsreportsource = None
            self.cnftopflowssortby = None
            self.cnftopflowstimestamp = None
            self.cnftopflowstopn = None
            self.cnftopflowstotalflows = None

        class CnfTopFlowsNextGenActionEffect_Enum(Enum):
            """
            CnfTopFlowsNextGenActionEffect_Enum

            Indicates the action effect on the system when the 
            cnfTopFlowsGenerate is set to 'true'.  
            
            'noOp' \-\- indicate that the system will make no operation 
                      when the cnfTopFlowsGenerate is set to 'true'.
                    Examples when this object could return 'noOp' are\:
                    1. the system is still in the top flow generation 
                       process. 
                    2. the system will not generate the top flows 
                       report when the value of 
                       cnfTopFlowsReportAvailable is 'true'.
            
            'generate' \-\- indicates that the system will start the top 
                          flows generation process if the 
                          cntTopFlowsGenerate is set to 'true'.
                    Examples when this object could return 'generate' 
                    are\:
                    1. When the value of cnfTopFlowsReportAvailable is 
                       'false'.  
                    2. The system will always generate the top flow
                       report when cnfTopFlowsGenerate is set to 
                       'true'.

            """

            NOOP = 1

            GENERATE = 2


            @staticmethod
            def _meta_info():
                from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
                return meta._meta_table['CISCONETFLOWMIB.CnfTopFlows.CnfTopFlowsNextGenActionEffect_Enum']


        class CnfTopFlowsReportSource_Enum(Enum):
            """
            CnfTopFlowsReportSource_Enum

            Indicates the source of Top Flows report generation for 
            the entries populated in cnfTopFlowsTable.
            
            'other'    \- The Top Flows are not available or the source 
                         of the Top Flows cannot be identified.
            
            'hardware' \- The Top Flows report has been generated based 
                         on the flows detected by the hardware platform
                         with netflow capabilities.
            
            'software' \- The Top Flows report has been generated based
                         on the flows detected by the software.
            
            'both'     \- The Top Flows report is an integrated list of 
                         Top Flows detected by both the hardware
                         platform and the software.

            """

            OTHER = 1

            HARDWARE = 2

            SOFTWARE = 3

            BOTH = 4


            @staticmethod
            def _meta_info():
                from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
                return meta._meta_table['CISCONETFLOWMIB.CnfTopFlows.CnfTopFlowsReportSource_Enum']


        @property
        def _common_path(self):

            return '/CISCO-NETFLOW-MIB:CISCO-NETFLOW-MIB/CISCO-NETFLOW-MIB:cnfTopFlows'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnftopflowsavailableflows is not None:
                return True

            if self.cnftopflowscachetimeout is not None:
                return True

            if self.cnftopflowsgenerate is not None:
                return True

            if self.cnftopflowsmatchclass is not None:
                return True

            if self.cnftopflowsmatchdirection is not None:
                return True

            if self.cnftopflowsmatchdstaddress is not None:
                return True

            if self.cnftopflowsmatchdstaddressmask is not None:
                return True

            if self.cnftopflowsmatchdstaddresstype is not None:
                return True

            if self.cnftopflowsmatchdstas is not None:
                return True

            if self.cnftopflowsmatchdstporthi is not None:
                return True

            if self.cnftopflowsmatchdstportlo is not None:
                return True

            if self.cnftopflowsmatchingflows is not None:
                return True

            if self.cnftopflowsmatchinputif is not None:
                return True

            if self.cnftopflowsmatchmaxbytes is not None:
                return True

            if self.cnftopflowsmatchmaxpackets is not None:
                return True

            if self.cnftopflowsmatchminbytes is not None:
                return True

            if self.cnftopflowsmatchminpackets is not None:
                return True

            if self.cnftopflowsmatchnhaddress is not None:
                return True

            if self.cnftopflowsmatchnhaddressmask is not None:
                return True

            if self.cnftopflowsmatchnhaddresstype is not None:
                return True

            if self.cnftopflowsmatchoutputif is not None:
                return True

            if self.cnftopflowsmatchprotocol is not None:
                return True

            if self.cnftopflowsmatchsampler is not None:
                return True

            if self.cnftopflowsmatchsrcaddress is not None:
                return True

            if self.cnftopflowsmatchsrcaddressmask is not None:
                return True

            if self.cnftopflowsmatchsrcaddresstype is not None:
                return True

            if self.cnftopflowsmatchsrcas is not None:
                return True

            if self.cnftopflowsmatchsrcporthi is not None:
                return True

            if self.cnftopflowsmatchsrcportlo is not None:
                return True

            if self.cnftopflowsmatchtosbyte is not None:
                return True

            if self.cnftopflowsnextgenactioneffect is not None:
                return True

            if self.cnftopflowsreportavailable is not None:
                return True

            if self.cnftopflowsreportsource is not None:
                return True

            if self.cnftopflowssortby is not None:
                return True

            if self.cnftopflowstimestamp is not None:
                return True

            if self.cnftopflowstopn is not None:
                return True

            if self.cnftopflowstotalflows is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
            return meta._meta_table['CISCONETFLOWMIB.CnfTopFlows']['meta_info']


    class CnfTopFlowsTable(object):
        """
        Table of flows which have accrued the highest packets or bytes.
        Each row in the table represents one flow from the cache.
        
        .. attribute:: cnftopflowstableentry
        
        	A conceptual row in the cnfTopFlowsTable
        	**type**\: list of :py:class:`CnfTopFlowsTableEntry <ydk.models.netflow.CISCO_NETFLOW_MIB.CISCONETFLOWMIB.CnfTopFlowsTable.CnfTopFlowsTableEntry>`
        
        

        """

        _prefix = 'cisco-netflow'
        _revision = '2006-04-27'

        def __init__(self):
            self.parent = None
            self.cnftopflowstableentry = YList()
            self.cnftopflowstableentry.parent = self
            self.cnftopflowstableentry.name = 'cnftopflowstableentry'


        class CnfTopFlowsTableEntry(object):
            """
            A conceptual row in the cnfTopFlowsTable.
            
            .. attribute:: cnftopflowsindex
            
            	Index to select top flows. A value of 1 selects the topmost flow
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnftopflowsbytes
            
            	Number of bytes in the flow
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnftopflowsclassid
            
            	Netflow Class ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnftopflowsdstaddress
            
            	Destination address
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cnftopflowsdstaddressmask
            
            	Number of bits in destination address mask
            	**type**\: int
            
            	**range:** 0..2040
            
            .. attribute:: cnftopflowsdstaddresstype
            
            	Type of destination address
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cnftopflowsdstas
            
            	Destination AS number
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnftopflowsdstport
            
            	Destination port number
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cnftopflowsfirstswitched
            
            	Time flow was first switched
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnftopflowsflags
            
            	Flow flags
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnftopflowsinputifindex
            
            	Input interface index
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cnftopflowslastswitched
            
            	Time flow was last switched
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnftopflowsnhaddress
            
            	Nexthop address
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cnftopflowsnhaddresstype
            
            	The type of nexthop address
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cnftopflowsoutputifindex
            
            	Output interface index
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cnftopflowspackets
            
            	Number of packets in the flow
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnftopflowsprotocol
            
            	Protocol number
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnftopflowssamplerid
            
            	Netflow Sampler ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnftopflowssrcaddress
            
            	Source address
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cnftopflowssrcaddressmask
            
            	Number of bits in source address mask
            	**type**\: int
            
            	**range:** 0..2040
            
            .. attribute:: cnftopflowssrcaddresstype
            
            	Type of source address
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cnftopflowssrcas
            
            	Source AS number
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnftopflowssrcport
            
            	Source port number
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cnftopflowstcpflags
            
            	TCP flags
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnftopflowstos
            
            	Type of service
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cnftopflowsvlan
            
            	The VLAN\-ID of this flow
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-netflow'
            _revision = '2006-04-27'

            def __init__(self):
                self.parent = None
                self.cnftopflowsindex = None
                self.cnftopflowsbytes = None
                self.cnftopflowsclassid = None
                self.cnftopflowsdstaddress = None
                self.cnftopflowsdstaddressmask = None
                self.cnftopflowsdstaddresstype = None
                self.cnftopflowsdstas = None
                self.cnftopflowsdstport = None
                self.cnftopflowsfirstswitched = None
                self.cnftopflowsflags = None
                self.cnftopflowsinputifindex = None
                self.cnftopflowslastswitched = None
                self.cnftopflowsnhaddress = None
                self.cnftopflowsnhaddresstype = None
                self.cnftopflowsoutputifindex = None
                self.cnftopflowspackets = None
                self.cnftopflowsprotocol = None
                self.cnftopflowssamplerid = None
                self.cnftopflowssrcaddress = None
                self.cnftopflowssrcaddressmask = None
                self.cnftopflowssrcaddresstype = None
                self.cnftopflowssrcas = None
                self.cnftopflowssrcport = None
                self.cnftopflowstcpflags = None
                self.cnftopflowstos = None
                self.cnftopflowsvlan = None

            @property
            def _common_path(self):
                if self.cnftopflowsindex is None:
                    raise YPYDataValidationError('Key property cnftopflowsindex is None')

                return '/CISCO-NETFLOW-MIB:CISCO-NETFLOW-MIB/CISCO-NETFLOW-MIB:cnfTopFlowsTable/CISCO-NETFLOW-MIB:cnfTopFlowsTableEntry[CISCO-NETFLOW-MIB:cnfTopFlowsIndex = ' + str(self.cnftopflowsindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cnftopflowsindex is not None:
                    return True

                if self.cnftopflowsbytes is not None:
                    return True

                if self.cnftopflowsclassid is not None:
                    return True

                if self.cnftopflowsdstaddress is not None:
                    return True

                if self.cnftopflowsdstaddressmask is not None:
                    return True

                if self.cnftopflowsdstaddresstype is not None:
                    return True

                if self.cnftopflowsdstas is not None:
                    return True

                if self.cnftopflowsdstport is not None:
                    return True

                if self.cnftopflowsfirstswitched is not None:
                    return True

                if self.cnftopflowsflags is not None:
                    return True

                if self.cnftopflowsinputifindex is not None:
                    return True

                if self.cnftopflowslastswitched is not None:
                    return True

                if self.cnftopflowsnhaddress is not None:
                    return True

                if self.cnftopflowsnhaddresstype is not None:
                    return True

                if self.cnftopflowsoutputifindex is not None:
                    return True

                if self.cnftopflowspackets is not None:
                    return True

                if self.cnftopflowsprotocol is not None:
                    return True

                if self.cnftopflowssamplerid is not None:
                    return True

                if self.cnftopflowssrcaddress is not None:
                    return True

                if self.cnftopflowssrcaddressmask is not None:
                    return True

                if self.cnftopflowssrcaddresstype is not None:
                    return True

                if self.cnftopflowssrcas is not None:
                    return True

                if self.cnftopflowssrcport is not None:
                    return True

                if self.cnftopflowstcpflags is not None:
                    return True

                if self.cnftopflowstos is not None:
                    return True

                if self.cnftopflowsvlan is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
                return meta._meta_table['CISCONETFLOWMIB.CnfTopFlowsTable.CnfTopFlowsTableEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-NETFLOW-MIB:CISCO-NETFLOW-MIB/CISCO-NETFLOW-MIB:cnfTopFlowsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cnftopflowstableentry is not None:
                for child_ref in self.cnftopflowstableentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
            return meta._meta_table['CISCONETFLOWMIB.CnfTopFlowsTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-NETFLOW-MIB:CISCO-NETFLOW-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cnfcacheinfo is not None and self.cnfcacheinfo._has_data():
            return True

        if self.cnfcacheinfo is not None and self.cnfcacheinfo.is_presence():
            return True

        if self.cnfcibridgedflowstatsctrltable is not None and self.cnfcibridgedflowstatsctrltable._has_data():
            return True

        if self.cnfcibridgedflowstatsctrltable is not None and self.cnfcibridgedflowstatsctrltable.is_presence():
            return True

        if self.cnfcicachetable is not None and self.cnfcicachetable._has_data():
            return True

        if self.cnfcicachetable is not None and self.cnfcicachetable.is_presence():
            return True

        if self.cnfciinterfacetable is not None and self.cnfciinterfacetable._has_data():
            return True

        if self.cnfciinterfacetable is not None and self.cnfciinterfacetable.is_presence():
            return True

        if self.cnfeicollectortable is not None and self.cnfeicollectortable._has_data():
            return True

        if self.cnfeicollectortable is not None and self.cnfeicollectortable.is_presence():
            return True

        if self.cnfeiexportinfotable is not None and self.cnfeiexportinfotable._has_data():
            return True

        if self.cnfeiexportinfotable is not None and self.cnfeiexportinfotable.is_presence():
            return True

        if self.cnfexportinfo is not None and self.cnfexportinfo._has_data():
            return True

        if self.cnfexportinfo is not None and self.cnfexportinfo.is_presence():
            return True

        if self.cnfexportstatistics is not None and self.cnfexportstatistics._has_data():
            return True

        if self.cnfexportstatistics is not None and self.cnfexportstatistics.is_presence():
            return True

        if self.cnfexporttemplate is not None and self.cnfexporttemplate._has_data():
            return True

        if self.cnfexporttemplate is not None and self.cnfexporttemplate.is_presence():
            return True

        if self.cnfprotocolstatistics is not None and self.cnfprotocolstatistics._has_data():
            return True

        if self.cnfprotocolstatistics is not None and self.cnfprotocolstatistics.is_presence():
            return True

        if self.cnfpsprotocolstattable is not None and self.cnfpsprotocolstattable._has_data():
            return True

        if self.cnfpsprotocolstattable is not None and self.cnfpsprotocolstattable.is_presence():
            return True

        if self.cnftemplateexportinfotable is not None and self.cnftemplateexportinfotable._has_data():
            return True

        if self.cnftemplateexportinfotable is not None and self.cnftemplateexportinfotable.is_presence():
            return True

        if self.cnftemplatetable is not None and self.cnftemplatetable._has_data():
            return True

        if self.cnftemplatetable is not None and self.cnftemplatetable.is_presence():
            return True

        if self.cnftopflows is not None and self.cnftopflows._has_data():
            return True

        if self.cnftopflows is not None and self.cnftopflows.is_presence():
            return True

        if self.cnftopflowstable is not None and self.cnftopflowstable._has_data():
            return True

        if self.cnftopflowstable is not None and self.cnftopflowstable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.netflow._meta import _CISCO_NETFLOW_MIB as meta
        return meta._meta_table['CISCONETFLOWMIB']['meta_info']



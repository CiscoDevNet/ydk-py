""" CISCO_IETF_MPLS_TE_EXT_STD_03_MIB 

Copyright (c) 2012 IETF Trust and the persons identified
as the document authors.  All rights reserved.
This MIB module contains generic object definitions for
MPLS Traffic Engineering in transport networks.This module is a
cisco\-ized version of the IETF draft\:
draft\-ietf\-mpls\-tp\-te\-mib\-03

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum
from ydk.models.snmpv2.SNMPv2_TC import StorageType_Enum


class CISCOIETFMPLSTEEXTSTD03MIB(object):
    """
    
    
    .. attribute:: cmplsnodeconfigtable
    
    	This table allows the administrator to map a node or LSR Identifier (IP compatible [Global\_Node\_ID] or ICC) with a local identifier.   This table is created to reuse the existing mplsTunnelTable for MPLS based transport network tunnels also. Since the MPLS tunnel's Ingress/Egress LSR identifiers' size (Unsigned32) value is not compatible for MPLS\-TP tunnel i.e. Global\_Node\_Id of size 8 bytes and ICC of size 6 bytes, there exists a need to map the Global\_Node\_ID or ICC with the local identifier of size 4 bytes (Unsigned32) value in order to index (Ingress/Egress LSR identifier) the existing mplsTunnelTable
    	**type**\: :py:class:`CmplsNodeConfigTable <ydk.models.ietf.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CISCOIETFMPLSTEEXTSTD03MIB.CmplsNodeConfigTable>`
    
    .. attribute:: cmplsnodeiccmaptable
    
    	This read\-only table allows the administrator to retrieve the local identifier for a given ICC operator in an ICC operator environment.  This table MAY be used in on\-demand and/or proactive OAM operations to get the Ingress/Egress LSR identifier (Local Identifier) from Src\-ICC or Dst\-ICC and the Ingress and Egress LSR identifiers are used to retrieve the tunnel entry. This table returns nothing when the associated entry is not defined in mplsNodeConfigTable
    	**type**\: :py:class:`CmplsNodeIccMapTable <ydk.models.ietf.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CISCOIETFMPLSTEEXTSTD03MIB.CmplsNodeIccMapTable>`
    
    .. attribute:: cmplsnodeipmaptable
    
    	This read\-only table allows the administrator to retrieve the local identifier for a given Global\_Node\_ID in an IP compatible operator environment.  This table MAY be used in on\-demand and/or proactive OAM operations to get the Ingress/Egress LSR identifier (Local Identifier) from Src\-Global\_Node\_ID or Dst\-Global\_Node\_ID and the Ingress and Egress LSR identifiers are used to retrieve the tunnel entry.  This table returns nothing when the associated entry is not defined in mplsNodeConfigTable
    	**type**\: :py:class:`CmplsNodeIpMapTable <ydk.models.ietf.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CISCOIETFMPLSTEEXTSTD03MIB.CmplsNodeIpMapTable>`
    
    .. attribute:: cmplstunnelexttable
    
    	This table represents MPLS\-TP specific extensions to mplsTunnelTable.  As per MPLS\-TP Identifiers [RFC6370], LSP\_ID for IP based co\-routed bidirectional tunnel,  A1\-{Global\_ID\:\:Node\_ID\:\:Tunnel\_Num}\:\:Z9\-{Global\_ID\:\: Node\_ID\:\:Tunnel\_Num}\:\:LSP\_Num  LSP\_ID for IP based associated bidirectional tunnel, A1\-{Global\_ID\:\:Node\_ID\:\:Tunnel\_Num\:\:LSP\_Num}\:\: Z9\-{Global\_ID\:\:Node\_ID\:\:Tunnel\_Num\:\:LSP\_Num}  mplsTunnelTable is reused for forming the LSP\_ID as follows,  Source Tunnel\_Num is mapped with mplsTunnelIndex, Source Node\_ID is mapped with mplsTunnelIngressLSRId, Destination Node\_ID is mapped with mplsTunnelEgressLSRId LSP\_Num is mapped with mplsTunnelInstance.  Source Global\_Node\_ID and/or ICC and Destination Global\_Node\_ID and/or ICC are maintained in the mplsNodeConfigTable and mplsNodeConfigLocalId is used to create an entry in mplsTunnelTable
    	**type**\: :py:class:`CmplsTunnelExtTable <ydk.models.ietf.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CISCOIETFMPLSTEEXTSTD03MIB.CmplsTunnelExtTable>`
    
    .. attribute:: cmplstunnelreverseperftable
    
    	This table extends the mplsTunnelTable to provide per\-tunnel packet performance information for the reverse direction of a bidirectional tunnel.  It can be seen as supplementing the mplsTunnelPerfTable, which augments the mplsTunnelTable.  For links that do not transport packets, these packet counters cannot be maintained.  For such links, attempts to read the objects in this table will return noSuchInstance
    	**type**\: :py:class:`CmplsTunnelReversePerfTable <ydk.models.ietf.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CISCOIETFMPLSTEEXTSTD03MIB.CmplsTunnelReversePerfTable>`
    
    

    """

    _prefix = 'cisco-ietf'
    _revision = '2012-06-06'

    def __init__(self):
        self.cmplsnodeconfigtable = CISCOIETFMPLSTEEXTSTD03MIB.CmplsNodeConfigTable()
        self.cmplsnodeconfigtable.parent = self
        self.cmplsnodeiccmaptable = CISCOIETFMPLSTEEXTSTD03MIB.CmplsNodeIccMapTable()
        self.cmplsnodeiccmaptable.parent = self
        self.cmplsnodeipmaptable = CISCOIETFMPLSTEEXTSTD03MIB.CmplsNodeIpMapTable()
        self.cmplsnodeipmaptable.parent = self
        self.cmplstunnelexttable = CISCOIETFMPLSTEEXTSTD03MIB.CmplsTunnelExtTable()
        self.cmplstunnelexttable.parent = self
        self.cmplstunnelreverseperftable = CISCOIETFMPLSTEEXTSTD03MIB.CmplsTunnelReversePerfTable()
        self.cmplstunnelreverseperftable.parent = self


    class CmplsNodeConfigTable(object):
        """
        This table allows the administrator to map a node or
        LSR Identifier (IP compatible [Global\_Node\_ID] or ICC)
        with a local identifier.
        
        
        This table is created to reuse the existing
        mplsTunnelTable for MPLS based transport network
        tunnels also.
        Since the MPLS tunnel's Ingress/Egress LSR identifiers'
        size (Unsigned32) value is not compatible for
        MPLS\-TP tunnel i.e. Global\_Node\_Id of size 8 bytes and
        ICC of size 6 bytes, there exists a need to map the
        Global\_Node\_ID or ICC with the local identifier of size
        4 bytes (Unsigned32) value in order
        to index (Ingress/Egress LSR identifier)
        the existing mplsTunnelTable.
        
        .. attribute:: cmplsnodeconfigentry
        
        	An entry in this table represents a mapping identification for the operator or service provider with node or LSR.  As per [RFC6370], this mapping is  represented as Global\_Node\_ID or ICC.  Note\: Each entry in this table should have a unique Global\_ID and Node\_ID combination
        	**type**\: list of :py:class:`CmplsNodeConfigEntry <ydk.models.ietf.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CISCOIETFMPLSTEEXTSTD03MIB.CmplsNodeConfigTable.CmplsNodeConfigEntry>`
        
        

        """

        _prefix = 'cisco-ietf'
        _revision = '2012-06-06'

        def __init__(self):
            self.parent = None
            self.cmplsnodeconfigentry = YList()
            self.cmplsnodeconfigentry.parent = self
            self.cmplsnodeconfigentry.name = 'cmplsnodeconfigentry'


        class CmplsNodeConfigEntry(object):
            """
            An entry in this table represents a mapping
            identification for the operator or service provider
            with node or LSR.
            
            As per [RFC6370], this mapping is
            
            represented as Global\_Node\_ID or ICC.
            
            Note\: Each entry in this table should have a unique
            Global\_ID and Node\_ID combination.
            
            .. attribute:: cmplsnodeconfiglocalid
            
            	This object allows the administrator to assign a unique local identifier to map Global\_Node\_ID or ICC
            	**type**\: int
            
            	**range:** 1..16777215
            
            .. attribute:: cmplsnodeconfigglobalid
            
            	This object indicates the Global Operator Identifier. This object value should be zero when mplsNodeConfigIccId is configured with non\-null value
            	**type**\: str
            
            	**range:** 4
            
            .. attribute:: cmplsnodeconfigiccid
            
            	This object allows the operator or service provider to configure a unique MPLS\-TP ITU\-T Carrier Code (ICC) either for Ingress ID or Egress ID.  This object value should be zero when mplsNodeConfigGlobalId and mplsNodeConfigNodeId are assigned with non\-zero value
            	**type**\: str
            
            	**range:** 1..6
            
            .. attribute:: cmplsnodeconfignodeid
            
            	This object indicates the Node\_ID within the operator. This object value should be zero when mplsNodeConfigIccId is configured with non\-null value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsnodeconfigrowstatus
            
            	This object allows the administrator to create, modify, and/or delete a row in this table
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: cmplsnodeconfigstoragetype
            
            	This variable indicates the storage type for this object. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'cisco-ietf'
            _revision = '2012-06-06'

            def __init__(self):
                self.parent = None
                self.cmplsnodeconfiglocalid = None
                self.cmplsnodeconfigglobalid = None
                self.cmplsnodeconfigiccid = None
                self.cmplsnodeconfignodeid = None
                self.cmplsnodeconfigrowstatus = None
                self.cmplsnodeconfigstoragetype = None

            @property
            def _common_path(self):
                if self.cmplsnodeconfiglocalid is None:
                    raise YPYDataValidationError('Key property cmplsnodeconfiglocalid is None')

                return '/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:cmplsNodeConfigTable/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:cmplsNodeConfigEntry[CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:cmplsNodeConfigLocalId = ' + str(self.cmplsnodeconfiglocalid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cmplsnodeconfiglocalid is not None:
                    return True

                if self.cmplsnodeconfigglobalid is not None:
                    return True

                if self.cmplsnodeconfigiccid is not None:
                    return True

                if self.cmplsnodeconfignodeid is not None:
                    return True

                if self.cmplsnodeconfigrowstatus is not None:
                    return True

                if self.cmplsnodeconfigstoragetype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _CISCO_IETF_MPLS_TE_EXT_STD_03_MIB as meta
                return meta._meta_table['CISCOIETFMPLSTEEXTSTD03MIB.CmplsNodeConfigTable.CmplsNodeConfigEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:cmplsNodeConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cmplsnodeconfigentry is not None:
                for child_ref in self.cmplsnodeconfigentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _CISCO_IETF_MPLS_TE_EXT_STD_03_MIB as meta
            return meta._meta_table['CISCOIETFMPLSTEEXTSTD03MIB.CmplsNodeConfigTable']['meta_info']


    class CmplsNodeIccMapTable(object):
        """
        This read\-only table allows the administrator to retrieve
        the local identifier for a given ICC operator in an ICC
        operator environment.
        
        This table MAY be used in on\-demand and/or proactive
        OAM operations to get the Ingress/Egress LSR
        identifier (Local Identifier) from Src\-ICC
        or Dst\-ICC and the Ingress and Egress LSR
        identifiers are used to retrieve the tunnel entry.
        This table returns nothing when the associated entry
        is not defined in mplsNodeConfigTable.
        
        .. attribute:: cmplsnodeiccmapentry
        
        	An entry in this table represents a mapping of ICC with the local identifier.  An entry in this table is created automatically when the Local identifier is associated with ICC in the mplsNodeConfigTable
        	**type**\: list of :py:class:`CmplsNodeIccMapEntry <ydk.models.ietf.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CISCOIETFMPLSTEEXTSTD03MIB.CmplsNodeIccMapTable.CmplsNodeIccMapEntry>`
        
        

        """

        _prefix = 'cisco-ietf'
        _revision = '2012-06-06'

        def __init__(self):
            self.parent = None
            self.cmplsnodeiccmapentry = YList()
            self.cmplsnodeiccmapentry.parent = self
            self.cmplsnodeiccmapentry.name = 'cmplsnodeiccmapentry'


        class CmplsNodeIccMapEntry(object):
            """
            An entry in this table represents a mapping of ICC with
            the local identifier.
            
            An entry in this table is created automatically when
            the Local identifier is associated with ICC in
            the mplsNodeConfigTable.
            
            .. attribute:: cmplsnodeiccmapiccid
            
            	This object allows the operator or service provider to configure a unique MPLS\-TP ITU\-T Carrier Code (ICC) either for Ingress or Egress LSR ID.  The ICC is a string of one to six characters, each character being either alphabetic (i.e.  A\-Z) or numeric (i.e. 0\-9) characters. Alphabetic characters in the ICC should be represented with upper case letters
            	**type**\: str
            
            	**range:** 1..6
            
            .. attribute:: cmplsnodeiccmaplocalid
            
            	This object contains an ICC based local identifier which is defined in mplsNodeConfigTable
            	**type**\: int
            
            	**range:** 1..16777215
            
            

            """

            _prefix = 'cisco-ietf'
            _revision = '2012-06-06'

            def __init__(self):
                self.parent = None
                self.cmplsnodeiccmapiccid = None
                self.cmplsnodeiccmaplocalid = None

            @property
            def _common_path(self):
                if self.cmplsnodeiccmapiccid is None:
                    raise YPYDataValidationError('Key property cmplsnodeiccmapiccid is None')

                return '/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:cmplsNodeIccMapTable/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:cmplsNodeIccMapEntry[CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:cmplsNodeIccMapIccId = ' + str(self.cmplsnodeiccmapiccid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cmplsnodeiccmapiccid is not None:
                    return True

                if self.cmplsnodeiccmaplocalid is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _CISCO_IETF_MPLS_TE_EXT_STD_03_MIB as meta
                return meta._meta_table['CISCOIETFMPLSTEEXTSTD03MIB.CmplsNodeIccMapTable.CmplsNodeIccMapEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:cmplsNodeIccMapTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cmplsnodeiccmapentry is not None:
                for child_ref in self.cmplsnodeiccmapentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _CISCO_IETF_MPLS_TE_EXT_STD_03_MIB as meta
            return meta._meta_table['CISCOIETFMPLSTEEXTSTD03MIB.CmplsNodeIccMapTable']['meta_info']


    class CmplsNodeIpMapTable(object):
        """
        This read\-only table allows the administrator to retrieve
        the local identifier for a given Global\_Node\_ID in an IP
        compatible operator environment.
        
        This table MAY be used in on\-demand and/or proactive
        OAM operations to get the Ingress/Egress LSR identifier
        (Local Identifier) from Src\-Global\_Node\_ID
        or Dst\-Global\_Node\_ID and the Ingress and Egress LSR
        identifiers are used to retrieve the tunnel entry.
        
        This table returns nothing when the associated entry
        is not defined in mplsNodeConfigTable.
        
        .. attribute:: cmplsnodeipmapentry
        
        	An entry in this table represents a mapping of Global\_Node\_ID with the local identifier.  An entry in this table is created automatically when the Local identifier is associated with Global\_ID and Node\_Id in the mplsNodeConfigTable. Note\: Each entry in this table should have a unique Global\_ID and Node\_ID combination
        	**type**\: list of :py:class:`CmplsNodeIpMapEntry <ydk.models.ietf.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CISCOIETFMPLSTEEXTSTD03MIB.CmplsNodeIpMapTable.CmplsNodeIpMapEntry>`
        
        

        """

        _prefix = 'cisco-ietf'
        _revision = '2012-06-06'

        def __init__(self):
            self.parent = None
            self.cmplsnodeipmapentry = YList()
            self.cmplsnodeipmapentry.parent = self
            self.cmplsnodeipmapentry.name = 'cmplsnodeipmapentry'


        class CmplsNodeIpMapEntry(object):
            """
            An entry in this table represents a mapping of
            Global\_Node\_ID with the local identifier.
            
            An entry in this table is created automatically when
            the Local identifier is associated with Global\_ID and
            Node\_Id in the mplsNodeConfigTable.
            Note\: Each entry in this table should have a unique
            Global\_ID and Node\_ID combination.
            
            .. attribute:: cmplsnodeipmapglobalid
            
            	This object indicates the Global\_ID
            	**type**\: str
            
            	**range:** 4
            
            .. attribute:: cmplsnodeipmapnodeid
            
            	This object indicates the Node\_ID within the operator
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsnodeipmaplocalid
            
            	This object contains an IP compatible local identifier which is defined in mplsNodeConfigTable
            	**type**\: int
            
            	**range:** 1..16777215
            
            

            """

            _prefix = 'cisco-ietf'
            _revision = '2012-06-06'

            def __init__(self):
                self.parent = None
                self.cmplsnodeipmapglobalid = None
                self.cmplsnodeipmapnodeid = None
                self.cmplsnodeipmaplocalid = None

            @property
            def _common_path(self):
                if self.cmplsnodeipmapglobalid is None:
                    raise YPYDataValidationError('Key property cmplsnodeipmapglobalid is None')
                if self.cmplsnodeipmapnodeid is None:
                    raise YPYDataValidationError('Key property cmplsnodeipmapnodeid is None')

                return '/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:cmplsNodeIpMapTable/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:cmplsNodeIpMapEntry[CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:cmplsNodeIpMapGlobalId = ' + str(self.cmplsnodeipmapglobalid) + '][CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:cmplsNodeIpMapNodeId = ' + str(self.cmplsnodeipmapnodeid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cmplsnodeipmapglobalid is not None:
                    return True

                if self.cmplsnodeipmapnodeid is not None:
                    return True

                if self.cmplsnodeipmaplocalid is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _CISCO_IETF_MPLS_TE_EXT_STD_03_MIB as meta
                return meta._meta_table['CISCOIETFMPLSTEEXTSTD03MIB.CmplsNodeIpMapTable.CmplsNodeIpMapEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:cmplsNodeIpMapTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cmplsnodeipmapentry is not None:
                for child_ref in self.cmplsnodeipmapentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _CISCO_IETF_MPLS_TE_EXT_STD_03_MIB as meta
            return meta._meta_table['CISCOIETFMPLSTEEXTSTD03MIB.CmplsNodeIpMapTable']['meta_info']


    class CmplsTunnelExtTable(object):
        """
        This table represents MPLS\-TP specific extensions to
        mplsTunnelTable.
        
        As per MPLS\-TP Identifiers [RFC6370], LSP\_ID for IP based
        co\-routed bidirectional tunnel,
        
        A1\-{Global\_ID\:\:Node\_ID\:\:Tunnel\_Num}\:\:Z9\-{Global\_ID\:\:
        Node\_ID\:\:Tunnel\_Num}\:\:LSP\_Num
        
        LSP\_ID for IP based associated bidirectional tunnel,
        A1\-{Global\_ID\:\:Node\_ID\:\:Tunnel\_Num\:\:LSP\_Num}\:\:
        Z9\-{Global\_ID\:\:Node\_ID\:\:Tunnel\_Num\:\:LSP\_Num}
        
        mplsTunnelTable is reused for forming the LSP\_ID
        as follows,
        
        Source Tunnel\_Num is mapped with mplsTunnelIndex,
        Source Node\_ID is mapped with
        mplsTunnelIngressLSRId, Destination Node\_ID is
        mapped with mplsTunnelEgressLSRId LSP\_Num is mapped with
        mplsTunnelInstance.
        
        Source Global\_Node\_ID and/or ICC and Destination
        Global\_Node\_ID and/or ICC are maintained in the
        mplsNodeConfigTable and mplsNodeConfigLocalId is
        used to create an entry in mplsTunnelTable.
        
        .. attribute:: cmplstunnelextentry
        
        	An entry in this table represents MPLS\-TP specific additional tunnel configurations
        	**type**\: list of :py:class:`CmplsTunnelExtEntry <ydk.models.ietf.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CISCOIETFMPLSTEEXTSTD03MIB.CmplsTunnelExtTable.CmplsTunnelExtEntry>`
        
        

        """

        _prefix = 'cisco-ietf'
        _revision = '2012-06-06'

        def __init__(self):
            self.parent = None
            self.cmplstunnelextentry = YList()
            self.cmplstunnelextentry.parent = self
            self.cmplstunnelextentry.name = 'cmplstunnelextentry'


        class CmplsTunnelExtEntry(object):
            """
            An entry in this table represents MPLS\-TP
            specific additional tunnel configurations.
            
            .. attribute:: mplstunnelegresslsrid
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelindex
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: mplstunnelingresslsrid
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelinstance
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplstunnelextdesttnlindex
            
            	This object is applicable only for the bidirectional tunnel that has the forward and reverse LSPs in the same tunnel or in the different tunnels.  This object holds the same value as that of the mplsTunnelIndex of mplsTunnelEntry if the forward and reverse LSPs are in the same tunnel. Otherwise, this object holds the value of the other direction associated LSP's mplsTunnelIndex from a different tunnel.  The values of this object and the mplsTunnelExtDestTnlLspIndex object together can be used to identify an opposite direction LSP i.e. if the mplsTunnelIndex and mplsTunnelInstance hold the value for forward LSP, this object and mplsTunnelExtDestTnlLspIndex can be used to retrieve the reverse direction LSP and vice versa.  This object and mplsTunnelExtDestTnlLspIndex values provide the first two indices of tunnel entry and the remaining indices can be derived as follows, if both the forward and reverse LSPs are present in the same tunnel, the opposite direction LSP's Ingress and Egress Identifier will be same for both the LSPs, else the Ingress and Egress Identifiers should be swapped in order to index the other direction tunnel
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cmplstunnelextdesttnllspindex
            
            	This object is applicable only for the bidirectional tunnel that has the forward and reverse LSPs in the same tunnel or in the different tunnels.  This object should contain different value if both the forward and reverse LSPs present in the same tunnel.  This object can contain same value or different values if the forward and reverse LSPs present in the different tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplstunnelextdesttnlvalid
            
            	Denotes whether or not this tunnel uses mplsTunnelExtDestTnlIndex and mplsTunnelExtDestTnlLspIndex for identifying the opposite direction tunnel information. Note that if this variable is set to true then the mplsTunnelExtDestTnlIndex and mplsTunnelExtDestTnlLspIndex objects should have the valid opposite direction tunnel indices
            	**type**\: bool
            
            .. attribute:: cmplstunnelextoppositedirtnlvalid
            
            	Denotes whether or not this tunnel uses mplsTunnelOppositeDirPtr for identifying the opposite direction tunnel information. Note that if this variable is set to true then the mplsTunnelOppositeDirPtr should point to the first accessible row of the opposite direction tunnel
            	**type**\: bool
            
            .. attribute:: cmplstunneloppositedirptr
            
            	This object is applicable only for the bidirectional tunnel that has the forward and reverse LSPs in the same tunnel or in the different tunnels.  This object holds the opposite direction tunnel entry if the bidirectional tunnel is setup by configuring two tunnel entries in mplsTunnelTable.  The value of zeroDotZero indicates single tunnel entry is used for bidirectional tunnel setup
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'cisco-ietf'
            _revision = '2012-06-06'

            def __init__(self):
                self.parent = None
                self.mplstunnelegresslsrid = None
                self.mplstunnelindex = None
                self.mplstunnelingresslsrid = None
                self.mplstunnelinstance = None
                self.cmplstunnelextdesttnlindex = None
                self.cmplstunnelextdesttnllspindex = None
                self.cmplstunnelextdesttnlvalid = None
                self.cmplstunnelextoppositedirtnlvalid = None
                self.cmplstunneloppositedirptr = None

            @property
            def _common_path(self):
                if self.mplstunnelegresslsrid is None:
                    raise YPYDataValidationError('Key property mplstunnelegresslsrid is None')
                if self.mplstunnelindex is None:
                    raise YPYDataValidationError('Key property mplstunnelindex is None')
                if self.mplstunnelingresslsrid is None:
                    raise YPYDataValidationError('Key property mplstunnelingresslsrid is None')
                if self.mplstunnelinstance is None:
                    raise YPYDataValidationError('Key property mplstunnelinstance is None')

                return '/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:cmplsTunnelExtTable/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:cmplsTunnelExtEntry[CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:mplsTunnelEgressLSRId = ' + str(self.mplstunnelegresslsrid) + '][CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:mplsTunnelIndex = ' + str(self.mplstunnelindex) + '][CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:mplsTunnelIngressLSRId = ' + str(self.mplstunnelingresslsrid) + '][CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:mplsTunnelInstance = ' + str(self.mplstunnelinstance) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.mplstunnelegresslsrid is not None:
                    return True

                if self.mplstunnelindex is not None:
                    return True

                if self.mplstunnelingresslsrid is not None:
                    return True

                if self.mplstunnelinstance is not None:
                    return True

                if self.cmplstunnelextdesttnlindex is not None:
                    return True

                if self.cmplstunnelextdesttnllspindex is not None:
                    return True

                if self.cmplstunnelextdesttnlvalid is not None:
                    return True

                if self.cmplstunnelextoppositedirtnlvalid is not None:
                    return True

                if self.cmplstunneloppositedirptr is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _CISCO_IETF_MPLS_TE_EXT_STD_03_MIB as meta
                return meta._meta_table['CISCOIETFMPLSTEEXTSTD03MIB.CmplsTunnelExtTable.CmplsTunnelExtEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:cmplsTunnelExtTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cmplstunnelextentry is not None:
                for child_ref in self.cmplstunnelextentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _CISCO_IETF_MPLS_TE_EXT_STD_03_MIB as meta
            return meta._meta_table['CISCOIETFMPLSTEEXTSTD03MIB.CmplsTunnelExtTable']['meta_info']


    class CmplsTunnelReversePerfTable(object):
        """
        This table extends the mplsTunnelTable to provide
        per\-tunnel packet performance information for the reverse
        direction of a bidirectional tunnel.  It can be seen as
        supplementing the mplsTunnelPerfTable, which augments the
        mplsTunnelTable.
        
        For links that do not transport packets, these packet
        counters cannot be maintained.  For such links, attempts
        to read the objects in this table will return
        noSuchInstance.
        
        .. attribute:: cmplstunnelreverseperfentry
        
        	An entry in this table is created by the LSR for every bidirectional MPLS tunnel where packets are visible to the LSR
        	**type**\: list of :py:class:`CmplsTunnelReversePerfEntry <ydk.models.ietf.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CISCOIETFMPLSTEEXTSTD03MIB.CmplsTunnelReversePerfTable.CmplsTunnelReversePerfEntry>`
        
        

        """

        _prefix = 'cisco-ietf'
        _revision = '2012-06-06'

        def __init__(self):
            self.parent = None
            self.cmplstunnelreverseperfentry = YList()
            self.cmplstunnelreverseperfentry.parent = self
            self.cmplstunnelreverseperfentry.name = 'cmplstunnelreverseperfentry'


        class CmplsTunnelReversePerfEntry(object):
            """
            An entry in this table is created by the LSR for every
            bidirectional MPLS tunnel where packets are visible to the
            LSR.
            
            .. attribute:: mplstunnelegresslsrid
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelindex
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: mplstunnelingresslsrid
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelinstance
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplstunnelreverseperfbytes
            
            	Number of bytes forwarded on the tunnel in the reverse direction if it is bidirectional.  This object represents the 32\-bit value of the least significant part of the 64\-bit value if both mplsTunnelReversePerfHCBytes and this object are returned.  For links that do not transport packets, this packet counter cannot be maintained.  For such links, this value will return noSuchInstance
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplstunnelreverseperferrors
            
            	Number of errored packets received on the tunnel in the reverse direction if it is bidirectional.  For links that do not transport packets, this packet counter cannot be maintained.  For such links, this value will return noSuchInstance
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplstunnelreverseperfhcbytes
            
            	High\-capacity counter for number of bytes forwarded on the tunnel in the reverse direction if it is bidirectional.  For links that do not transport packets, this packet counter cannot be maintained.  For such links, this value will return noSuchInstance
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cmplstunnelreverseperfhcpackets
            
            	High\-capacity counter for number of packets forwarded on the tunnel in the reverse direction if it is bidirectional.  For links that do not transport packets, this packet counter cannot be maintained.  For such links, this value will return noSuchInstance
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cmplstunnelreverseperfpackets
            
            	Number of packets forwarded on the tunnel in the reverse direction if it is bidirectional.  This object represents the 32\-bit value of the least significant part of the 64\-bit value if both mplsTunnelReversePerfHCPackets and this object are returned.  For links that do not transport packets, this packet counter cannot be maintained.  For such links, this value will return noSuchInstance
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-ietf'
            _revision = '2012-06-06'

            def __init__(self):
                self.parent = None
                self.mplstunnelegresslsrid = None
                self.mplstunnelindex = None
                self.mplstunnelingresslsrid = None
                self.mplstunnelinstance = None
                self.cmplstunnelreverseperfbytes = None
                self.cmplstunnelreverseperferrors = None
                self.cmplstunnelreverseperfhcbytes = None
                self.cmplstunnelreverseperfhcpackets = None
                self.cmplstunnelreverseperfpackets = None

            @property
            def _common_path(self):
                if self.mplstunnelegresslsrid is None:
                    raise YPYDataValidationError('Key property mplstunnelegresslsrid is None')
                if self.mplstunnelindex is None:
                    raise YPYDataValidationError('Key property mplstunnelindex is None')
                if self.mplstunnelingresslsrid is None:
                    raise YPYDataValidationError('Key property mplstunnelingresslsrid is None')
                if self.mplstunnelinstance is None:
                    raise YPYDataValidationError('Key property mplstunnelinstance is None')

                return '/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:cmplsTunnelReversePerfTable/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:cmplsTunnelReversePerfEntry[CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:mplsTunnelEgressLSRId = ' + str(self.mplstunnelegresslsrid) + '][CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:mplsTunnelIndex = ' + str(self.mplstunnelindex) + '][CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:mplsTunnelIngressLSRId = ' + str(self.mplstunnelingresslsrid) + '][CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:mplsTunnelInstance = ' + str(self.mplstunnelinstance) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.mplstunnelegresslsrid is not None:
                    return True

                if self.mplstunnelindex is not None:
                    return True

                if self.mplstunnelingresslsrid is not None:
                    return True

                if self.mplstunnelinstance is not None:
                    return True

                if self.cmplstunnelreverseperfbytes is not None:
                    return True

                if self.cmplstunnelreverseperferrors is not None:
                    return True

                if self.cmplstunnelreverseperfhcbytes is not None:
                    return True

                if self.cmplstunnelreverseperfhcpackets is not None:
                    return True

                if self.cmplstunnelreverseperfpackets is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _CISCO_IETF_MPLS_TE_EXT_STD_03_MIB as meta
                return meta._meta_table['CISCOIETFMPLSTEEXTSTD03MIB.CmplsTunnelReversePerfTable.CmplsTunnelReversePerfEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:cmplsTunnelReversePerfTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cmplstunnelreverseperfentry is not None:
                for child_ref in self.cmplstunnelreverseperfentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _CISCO_IETF_MPLS_TE_EXT_STD_03_MIB as meta
            return meta._meta_table['CISCOIETFMPLSTEEXTSTD03MIB.CmplsTunnelReversePerfTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cmplsnodeconfigtable is not None and self.cmplsnodeconfigtable._has_data():
            return True

        if self.cmplsnodeconfigtable is not None and self.cmplsnodeconfigtable.is_presence():
            return True

        if self.cmplsnodeiccmaptable is not None and self.cmplsnodeiccmaptable._has_data():
            return True

        if self.cmplsnodeiccmaptable is not None and self.cmplsnodeiccmaptable.is_presence():
            return True

        if self.cmplsnodeipmaptable is not None and self.cmplsnodeipmaptable._has_data():
            return True

        if self.cmplsnodeipmaptable is not None and self.cmplsnodeipmaptable.is_presence():
            return True

        if self.cmplstunnelexttable is not None and self.cmplstunnelexttable._has_data():
            return True

        if self.cmplstunnelexttable is not None and self.cmplstunnelexttable.is_presence():
            return True

        if self.cmplstunnelreverseperftable is not None and self.cmplstunnelreverseperftable._has_data():
            return True

        if self.cmplstunnelreverseperftable is not None and self.cmplstunnelreverseperftable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _CISCO_IETF_MPLS_TE_EXT_STD_03_MIB as meta
        return meta._meta_table['CISCOIETFMPLSTEEXTSTD03MIB']['meta_info']



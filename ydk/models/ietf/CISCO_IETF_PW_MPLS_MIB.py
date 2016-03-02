""" CISCO_IETF_PW_MPLS_MIB 

This MIB complements the CISCO\-IETF\-PW\-MIB for PW operation 
over MPLS. 

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum
from ydk.models.snmpv2.SNMPv2_TC import StorageType_Enum


class CISCOIETFPWMPLSMIB(object):
    """
    
    
    .. attribute:: cpwvcmplsinboundtable
    
    	This table associates VCs using MPLS PSN with the inbound  MPLS tunnels (i.e. for packets coming from the PSN),   if such association is desired (mainly for security   reasons)
    	**type**\: :py:class:`CpwVcMplsInboundTable <ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsInboundTable>`
    
    .. attribute:: cpwvcmplsnontemappingtable
    
    	This table maps an inbound/outbound Tunnel to a VC in non\-  TE applications
    	**type**\: :py:class:`CpwVcMplsNonTeMappingTable <ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable>`
    
    .. attribute:: cpwvcmplsobjects
    
    	
    	**type**\: :py:class:`CpwVcMplsObjects <ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsObjects>`
    
    .. attribute:: cpwvcmplsoutboundtable
    
    	This table associates VCs using MPLS PSN with the outbound  MPLS tunnels (i.e. toward the PSN) or the physical   interface in case of VC only
    	**type**\: :py:class:`CpwVcMplsOutboundTable <ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsOutboundTable>`
    
    .. attribute:: cpwvcmplstable
    
    	This table specifies information for VC to be carried over   MPLS PSN
    	**type**\: :py:class:`CpwVcMplsTable <ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsTable>`
    
    .. attribute:: cpwvcmplstemappingtable
    
    	This table maps an inbound/outbound Tunnel to a VC in   MPLS\-TE applications
    	**type**\: :py:class:`CpwVcMplsTeMappingTable <ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable>`
    
    

    """

    _prefix = 'cisco-ietf-pw-mpls'
    _revision = '2003-02-26'

    def __init__(self):
        self.cpwvcmplsinboundtable = CISCOIETFPWMPLSMIB.CpwVcMplsInboundTable()
        self.cpwvcmplsinboundtable.parent = self
        self.cpwvcmplsnontemappingtable = CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable()
        self.cpwvcmplsnontemappingtable.parent = self
        self.cpwvcmplsobjects = CISCOIETFPWMPLSMIB.CpwVcMplsObjects()
        self.cpwvcmplsobjects.parent = self
        self.cpwvcmplsoutboundtable = CISCOIETFPWMPLSMIB.CpwVcMplsOutboundTable()
        self.cpwvcmplsoutboundtable.parent = self
        self.cpwvcmplstable = CISCOIETFPWMPLSMIB.CpwVcMplsTable()
        self.cpwvcmplstable.parent = self
        self.cpwvcmplstemappingtable = CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable()
        self.cpwvcmplstemappingtable.parent = self


    class CpwVcMplsInboundTable(object):
        """
        This table associates VCs using MPLS PSN with the inbound 
        MPLS tunnels (i.e. for packets coming from the PSN),  
        if such association is desired (mainly for security  
        reasons).
        
        .. attribute:: cpwvcmplsinboundentry
        
        	A row in this table represents a link between PW VCs (that  require MPLS tunnels) and MPLS tunnel for packets arriving  from the PSN.  This table is indexed by the set of indexes used to  identify the VC \- cpwVcIndex and an additional  index enabling multiple rows for the same VC index.   Note that the first entry for each VC can be indexed by   cpwVcMplsOutboundIndex equal zero without a need for   retrieval of cpwVcMplsInboundIndexNext.   An entry is created in this table either automatically by   the local agent or created manually by the operator in   cases that strict mode is required.   Note that the control messages contain VC ID and VC type,   which together with the remote IP address identify the  cpwVcIndex in the local node.  This table points to the appropriate MPLS MIB. In the case   of MPLS\-TE, the 4 variables relevant to the indexing of a  TE MPLS tunnel are set as in Srinivasan, et al, <draft\-  ietf\-mpls\-te\-mib>.   In case of non\-TE MPLS tunnel (an outer tunnel label   assigned by LDP or manually) the table points to the XC   entry in the MPLS\-LSR\-MIB as in Srinivasan, et al, <draft\-  ietf\-mpls\-lsr\-mib>.   Each VC may have multiple rows in this tables if protection   is available at the outer tunnel level, each row may be of  different type except for VC only, on which only rows with  ifIndex of the port are allowed. 
        	**type**\: list of :py:class:`CpwVcMplsInboundEntry <ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsInboundTable.CpwVcMplsInboundEntry>`
        
        

        """

        _prefix = 'cisco-ietf-pw-mpls'
        _revision = '2003-02-26'

        def __init__(self):
            self.parent = None
            self.cpwvcmplsinboundentry = YList()
            self.cpwvcmplsinboundentry.parent = self
            self.cpwvcmplsinboundentry.name = 'cpwvcmplsinboundentry'


        class CpwVcMplsInboundEntry(object):
            """
            A row in this table represents a link between PW VCs (that 
            require MPLS tunnels) and MPLS tunnel for packets arriving 
            from the PSN. 
            This table is indexed by the set of indexes used to 
            identify the VC \- cpwVcIndex and an additional 
            index enabling multiple rows for the same VC index. 
            
            Note that the first entry for each VC can be indexed by  
            cpwVcMplsOutboundIndex equal zero without a need for  
            retrieval of cpwVcMplsInboundIndexNext. 
            
            An entry is created in this table either automatically by  
            the local agent or created manually by the operator in  
            cases that strict mode is required. 
            
            Note that the control messages contain VC ID and VC type,  
            which together with the remote IP address identify the 
            cpwVcIndex in the local node. 
            This table points to the appropriate MPLS MIB. In the case  
            of MPLS\-TE, the 4 variables relevant to the indexing of a 
            TE MPLS tunnel are set as in Srinivasan, et al, <draft\- 
            ietf\-mpls\-te\-mib>. 
            
            In case of non\-TE MPLS tunnel (an outer tunnel label  
            assigned by LDP or manually) the table points to the XC  
            entry in the MPLS\-LSR\-MIB as in Srinivasan, et al, <draft\- 
            ietf\-mpls\-lsr\-mib>. 
            
            Each VC may have multiple rows in this tables if protection  
            is available at the outer tunnel level, each row may be of 
            different type except for VC only, on which only rows with 
            ifIndex of the port are allowed. 
            
            .. attribute:: cpwvcindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsinboundindex
            
            	Arbitrary index for enabling multiple rows per VC in  this table. Next available free index can be retrieved  using cpwVcMplsInboundIndexNext. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsinboundifindex
            
            	In case of VC only (no outer tunnel), this object holds the  ifIndex of the inbound port, otherwise set to zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cpwvcmplsinboundlsrxcindex
            
            	If the outer label is defined in the MPL\-LSR\-MIB, i.e. set   by LDP or manually, this object points to the XC index   of the outer tunnel. Otherwise, it is set to zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsinboundrowstatus
            
            	For creating, modifying, and deleting this row
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: cpwvcmplsinboundstoragetype
            
            	This variable indicates the storage type for this row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: cpwvcmplsinboundtunnelindex
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cpwvcmplsinboundtunnelinstance
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsinboundtunnellcllsr
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\: str
            
            	**range:** 4
            
            .. attribute:: cpwvcmplsinboundtunnelpeerlsr
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\: str
            
            	**range:** 4
            
            

            """

            _prefix = 'cisco-ietf-pw-mpls'
            _revision = '2003-02-26'

            def __init__(self):
                self.parent = None
                self.cpwvcindex = None
                self.cpwvcmplsinboundindex = None
                self.cpwvcmplsinboundifindex = None
                self.cpwvcmplsinboundlsrxcindex = None
                self.cpwvcmplsinboundrowstatus = None
                self.cpwvcmplsinboundstoragetype = None
                self.cpwvcmplsinboundtunnelindex = None
                self.cpwvcmplsinboundtunnelinstance = None
                self.cpwvcmplsinboundtunnellcllsr = None
                self.cpwvcmplsinboundtunnelpeerlsr = None

            @property
            def _common_path(self):
                if self.cpwvcindex is None:
                    raise YPYDataValidationError('Key property cpwvcindex is None')
                if self.cpwvcmplsinboundindex is None:
                    raise YPYDataValidationError('Key property cpwvcmplsinboundindex is None')

                return '/CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsInboundTable/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsInboundEntry[CISCO-IETF-PW-MPLS-MIB:cpwVcIndex = ' + str(self.cpwvcindex) + '][CISCO-IETF-PW-MPLS-MIB:cpwVcMplsInboundIndex = ' + str(self.cpwvcmplsinboundindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cpwvcindex is not None:
                    return True

                if self.cpwvcmplsinboundindex is not None:
                    return True

                if self.cpwvcmplsinboundifindex is not None:
                    return True

                if self.cpwvcmplsinboundlsrxcindex is not None:
                    return True

                if self.cpwvcmplsinboundrowstatus is not None:
                    return True

                if self.cpwvcmplsinboundstoragetype is not None:
                    return True

                if self.cpwvcmplsinboundtunnelindex is not None:
                    return True

                if self.cpwvcmplsinboundtunnelinstance is not None:
                    return True

                if self.cpwvcmplsinboundtunnellcllsr is not None:
                    return True

                if self.cpwvcmplsinboundtunnelpeerlsr is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _CISCO_IETF_PW_MPLS_MIB as meta
                return meta._meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsInboundTable.CpwVcMplsInboundEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsInboundTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cpwvcmplsinboundentry is not None:
                for child_ref in self.cpwvcmplsinboundentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _CISCO_IETF_PW_MPLS_MIB as meta
            return meta._meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsInboundTable']['meta_info']


    class CpwVcMplsNonTeMappingTable(object):
        """
        This table maps an inbound/outbound Tunnel to a VC in non\- 
        TE applications.
        
        .. attribute:: cpwvcmplsnontemappingentry
        
        	A row in this table represents the association  between the PW VC and it's non TE MPLS outer Tunnel  it's physical interface if there is no outer tunnel   (VC only).   An application can use this table to quickly retrieve the   PW carried over specific non\-TE MPLS outer tunnel or   physical interface.   The table in indexed by the XC index for MPLS Non\-TE   tunnel, or ifIndex of the port in VC only case, the   direction of the VC in the specific entry and the VCIndex.   The same table is used in both inbound and outbound  directions, but in a different row for each direction. If   the inbound association is not known, no rows should exist   for it.   Rows are created by the local agent when all the   association data is available for display
        	**type**\: list of :py:class:`CpwVcMplsNonTeMappingEntry <ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable.CpwVcMplsNonTeMappingEntry>`
        
        

        """

        _prefix = 'cisco-ietf-pw-mpls'
        _revision = '2003-02-26'

        def __init__(self):
            self.parent = None
            self.cpwvcmplsnontemappingentry = YList()
            self.cpwvcmplsnontemappingentry.parent = self
            self.cpwvcmplsnontemappingentry.name = 'cpwvcmplsnontemappingentry'


        class CpwVcMplsNonTeMappingEntry(object):
            """
            A row in this table represents the association 
            between the PW VC and it's non TE MPLS outer Tunnel 
            it's physical interface if there is no outer tunnel  
            (VC only). 
            
            An application can use this table to quickly retrieve the  
            PW carried over specific non\-TE MPLS outer tunnel or  
            physical interface. 
            
            The table in indexed by the XC index for MPLS Non\-TE  
            tunnel, or ifIndex of the port in VC only case, the  
            direction of the VC in the specific entry and the VCIndex. 
            
            The same table is used in both inbound and outbound 
            directions, but in a different row for each direction. If  
            the inbound association is not known, no rows should exist  
            for it. 
            
            Rows are created by the local agent when all the  
            association data is available for display.
            
            .. attribute:: cpwvcmplsnontemappingifindex
            
            	Identify the port on which the VC is carried for VC only   case
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cpwvcmplsnontemappingtunneldirection
            
            	Identifies if the row represent an outbound or inbound   mapping
            	**type**\: :py:class:`CpwVcMplsNonTeMappingTunnelDirection_Enum <ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable.CpwVcMplsNonTeMappingEntry.CpwVcMplsNonTeMappingTunnelDirection_Enum>`
            
            .. attribute:: cpwvcmplsnontemappingvcindex
            
            	The value that represent the VC in the cpwVcTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsnontemappingxctunnelindex
            
            	Index for the conceptual XC row identifying Tunnel to VC   mappings when the outer tunnel is created by the MPLS\-LSR\-  MIB, Zero otherwise
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-ietf-pw-mpls'
            _revision = '2003-02-26'

            def __init__(self):
                self.parent = None
                self.cpwvcmplsnontemappingifindex = None
                self.cpwvcmplsnontemappingtunneldirection = None
                self.cpwvcmplsnontemappingvcindex = None
                self.cpwvcmplsnontemappingxctunnelindex = None

            class CpwVcMplsNonTeMappingTunnelDirection_Enum(Enum):
                """
                CpwVcMplsNonTeMappingTunnelDirection_Enum

                Identifies if the row represent an outbound or inbound  
                mapping.

                """

                OUTBOUND = 1

                INBOUND = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _CISCO_IETF_PW_MPLS_MIB as meta
                    return meta._meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable.CpwVcMplsNonTeMappingEntry.CpwVcMplsNonTeMappingTunnelDirection_Enum']


            @property
            def _common_path(self):
                if self.cpwvcmplsnontemappingifindex is None:
                    raise YPYDataValidationError('Key property cpwvcmplsnontemappingifindex is None')
                if self.cpwvcmplsnontemappingtunneldirection is None:
                    raise YPYDataValidationError('Key property cpwvcmplsnontemappingtunneldirection is None')
                if self.cpwvcmplsnontemappingvcindex is None:
                    raise YPYDataValidationError('Key property cpwvcmplsnontemappingvcindex is None')
                if self.cpwvcmplsnontemappingxctunnelindex is None:
                    raise YPYDataValidationError('Key property cpwvcmplsnontemappingxctunnelindex is None')

                return '/CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsNonTeMappingTable/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsNonTeMappingEntry[CISCO-IETF-PW-MPLS-MIB:cpwVcMplsNonTeMappingIfIndex = ' + str(self.cpwvcmplsnontemappingifindex) + '][CISCO-IETF-PW-MPLS-MIB:cpwVcMplsNonTeMappingTunnelDirection = ' + str(self.cpwvcmplsnontemappingtunneldirection) + '][CISCO-IETF-PW-MPLS-MIB:cpwVcMplsNonTeMappingVcIndex = ' + str(self.cpwvcmplsnontemappingvcindex) + '][CISCO-IETF-PW-MPLS-MIB:cpwVcMplsNonTeMappingXcTunnelIndex = ' + str(self.cpwvcmplsnontemappingxctunnelindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cpwvcmplsnontemappingifindex is not None:
                    return True

                if self.cpwvcmplsnontemappingtunneldirection is not None:
                    return True

                if self.cpwvcmplsnontemappingvcindex is not None:
                    return True

                if self.cpwvcmplsnontemappingxctunnelindex is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _CISCO_IETF_PW_MPLS_MIB as meta
                return meta._meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable.CpwVcMplsNonTeMappingEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsNonTeMappingTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cpwvcmplsnontemappingentry is not None:
                for child_ref in self.cpwvcmplsnontemappingentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _CISCO_IETF_PW_MPLS_MIB as meta
            return meta._meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable']['meta_info']


    class CpwVcMplsObjects(object):
        """
        
        
        .. attribute:: cpwvcmplsinboundindexnext
        
        	This object contains an appropriate value to  be used for cpwVcMplsInboundIndex when creating  entries in the cpwVcMplsInboundTable. The value  0 indicates that no unassigned entries are  available. To obtain the cpwVcMplsInboundIndex  value for a new entry, the manager issues a  management protocol retrieval operation to obtain  the current value of this object.  After each  retrieval, the agent should modify the value to  the next unassigned index, however the agent MUST  NOT assume such retrieval will be done for each   row created
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cpwvcmplsoutboundindexnext
        
        	This object contains an appropriate value to  be used for cpwVcMplsOutboundIndex when creating  entries in the cpwVcMplsOutboundTable. The value  0 indicates that no unassigned entries are  available. To obtain the cpwVcMplsOutboundIndex  value for a new entry, the manager issues a  management protocol retrieval operation to obtain  the current value of this object.  After each  retrieval, the agent should modify the value to  the next unassigned index, however the agent MUST  NOT assume such retrieval will be done for each   row created
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-ietf-pw-mpls'
        _revision = '2003-02-26'

        def __init__(self):
            self.parent = None
            self.cpwvcmplsinboundindexnext = None
            self.cpwvcmplsoutboundindexnext = None

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cpwvcmplsinboundindexnext is not None:
                return True

            if self.cpwvcmplsoutboundindexnext is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _CISCO_IETF_PW_MPLS_MIB as meta
            return meta._meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsObjects']['meta_info']


    class CpwVcMplsOutboundTable(object):
        """
        This table associates VCs using MPLS PSN with the outbound 
        MPLS tunnels (i.e. toward the PSN) or the physical  
        interface in case of VC only.
        
        .. attribute:: cpwvcmplsoutboundentry
        
        	A row in this table represents a link between PW VC (that  require MPLS tunnels) and MPLS tunnel toward the PSN.  In the case of VC only, it associate the VC with the   interface that shall carry the VC.  This table is indexed by the pwVcIndex and an additional  index enabling multiple rows for the same VC index.   At least one entry is created in this table by the operator   for each PW VC that requires MPLS PSN. Note that the first  entry for each VC can be indexed by cpwVcMplsOutboundIndex   equal zero without a need for retrieval of   cpwVcMplsOutboundIndexNext.   This table points to the appropriate MPLS MIB. In the case   of MPLS\-TE, the 4 variables relevant to the indexing of   a TE MPLS tunnel are set as in Srinivasan, et al, <draft\-  ietf\-mpls\-te\-mib>.  In case of Non\-TE MPLS (an outer tunnel label assigned by   LDP or manually) the table points to the XC entry in the   LSR MIB as in Srinivasan, et al, <draft\-ietf\-mpls\-lsr\-mib>.  In case of VC only (no outer tunnel) the ifIndex of the  port to carry the VC is configured.    Each VC may have multiple rows in this tables if protection   is available at the outer tunnel level, each row may be of  different type except for VC only, on which only rows with  ifIndex of the port are allowed. 
        	**type**\: list of :py:class:`CpwVcMplsOutboundEntry <ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsOutboundTable.CpwVcMplsOutboundEntry>`
        
        

        """

        _prefix = 'cisco-ietf-pw-mpls'
        _revision = '2003-02-26'

        def __init__(self):
            self.parent = None
            self.cpwvcmplsoutboundentry = YList()
            self.cpwvcmplsoutboundentry.parent = self
            self.cpwvcmplsoutboundentry.name = 'cpwvcmplsoutboundentry'


        class CpwVcMplsOutboundEntry(object):
            """
            A row in this table represents a link between PW VC (that 
            require MPLS tunnels) and MPLS tunnel toward the PSN. 
            In the case of VC only, it associate the VC with the  
            interface that shall carry the VC. 
            This table is indexed by the pwVcIndex and an additional 
            index enabling multiple rows for the same VC index. 
            
            At least one entry is created in this table by the operator  
            for each PW VC that requires MPLS PSN. Note that the first 
            entry for each VC can be indexed by cpwVcMplsOutboundIndex  
            equal zero without a need for retrieval of  
            cpwVcMplsOutboundIndexNext. 
            
            This table points to the appropriate MPLS MIB. In the case  
            of MPLS\-TE, the 4 variables relevant to the indexing of  
            a TE MPLS tunnel are set as in Srinivasan, et al, <draft\- 
            ietf\-mpls\-te\-mib>. 
            In case of Non\-TE MPLS (an outer tunnel label assigned by  
            LDP or manually) the table points to the XC entry in the  
            LSR MIB as in Srinivasan, et al, <draft\-ietf\-mpls\-lsr\-mib>. 
            In case of VC only (no outer tunnel) the ifIndex of the 
            port to carry the VC is configured.  
            
            Each VC may have multiple rows in this tables if protection  
            is available at the outer tunnel level, each row may be of 
            different type except for VC only, on which only rows with 
            ifIndex of the port are allowed. 
            
            .. attribute:: cpwvcindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsoutboundindex
            
            	Arbitrary index for enabling multiple rows per VC in  this table. Next available free index can be retrieved   using cpwVcMplsOutboundIndexNext. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsoutboundifindex
            
            	In case of VC only (no outer tunnel), this object holds  the ifIndex of the outbound port, otherwise set to zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cpwvcmplsoutboundlsrxcindex
            
            	This object will be set by the operator. If the outer  label is defined in the MPL\-LSR\-MIB, i.e. set by LDP  or manually, this object points to the XC index   of the outer tunnel. Otherwise, it is set to zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsoutboundrowstatus
            
            	For creating, modifying, and deleting this row
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: cpwvcmplsoutboundstoragetype
            
            	This variable indicates the storage type for this object
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: cpwvcmplsoutboundtunnelindex
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cpwvcmplsoutboundtunnelinstance
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsoutboundtunnellcllsr
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\: str
            
            	**range:** 4
            
            .. attribute:: cpwvcmplsoutboundtunnelpeerlsr
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\: str
            
            	**range:** 4
            
            

            """

            _prefix = 'cisco-ietf-pw-mpls'
            _revision = '2003-02-26'

            def __init__(self):
                self.parent = None
                self.cpwvcindex = None
                self.cpwvcmplsoutboundindex = None
                self.cpwvcmplsoutboundifindex = None
                self.cpwvcmplsoutboundlsrxcindex = None
                self.cpwvcmplsoutboundrowstatus = None
                self.cpwvcmplsoutboundstoragetype = None
                self.cpwvcmplsoutboundtunnelindex = None
                self.cpwvcmplsoutboundtunnelinstance = None
                self.cpwvcmplsoutboundtunnellcllsr = None
                self.cpwvcmplsoutboundtunnelpeerlsr = None

            @property
            def _common_path(self):
                if self.cpwvcindex is None:
                    raise YPYDataValidationError('Key property cpwvcindex is None')
                if self.cpwvcmplsoutboundindex is None:
                    raise YPYDataValidationError('Key property cpwvcmplsoutboundindex is None')

                return '/CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsOutboundTable/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsOutboundEntry[CISCO-IETF-PW-MPLS-MIB:cpwVcIndex = ' + str(self.cpwvcindex) + '][CISCO-IETF-PW-MPLS-MIB:cpwVcMplsOutboundIndex = ' + str(self.cpwvcmplsoutboundindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cpwvcindex is not None:
                    return True

                if self.cpwvcmplsoutboundindex is not None:
                    return True

                if self.cpwvcmplsoutboundifindex is not None:
                    return True

                if self.cpwvcmplsoutboundlsrxcindex is not None:
                    return True

                if self.cpwvcmplsoutboundrowstatus is not None:
                    return True

                if self.cpwvcmplsoutboundstoragetype is not None:
                    return True

                if self.cpwvcmplsoutboundtunnelindex is not None:
                    return True

                if self.cpwvcmplsoutboundtunnelinstance is not None:
                    return True

                if self.cpwvcmplsoutboundtunnellcllsr is not None:
                    return True

                if self.cpwvcmplsoutboundtunnelpeerlsr is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _CISCO_IETF_PW_MPLS_MIB as meta
                return meta._meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsOutboundTable.CpwVcMplsOutboundEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsOutboundTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cpwvcmplsoutboundentry is not None:
                for child_ref in self.cpwvcmplsoutboundentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _CISCO_IETF_PW_MPLS_MIB as meta
            return meta._meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsOutboundTable']['meta_info']


    class CpwVcMplsTable(object):
        """
        This table specifies information for VC to be carried over  
        MPLS PSN.
        
        .. attribute:: cpwvcmplsentry
        
        	A row in this table represents parameters specific to MPLS   PSN for a pseudo wire connection (VC). The row is created   automatically by the local agent if the cpwVcPsnType is   MPLS. It is indexed by cpwVcIndex, which uniquely   identifying a singular connection. 
        	**type**\: list of :py:class:`CpwVcMplsEntry <ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsTable.CpwVcMplsEntry>`
        
        

        """

        _prefix = 'cisco-ietf-pw-mpls'
        _revision = '2003-02-26'

        def __init__(self):
            self.parent = None
            self.cpwvcmplsentry = YList()
            self.cpwvcmplsentry.parent = self
            self.cpwvcmplsentry.name = 'cpwvcmplsentry'


        class CpwVcMplsEntry(object):
            """
            A row in this table represents parameters specific to MPLS  
            PSN for a pseudo wire connection (VC). The row is created  
            automatically by the local agent if the cpwVcPsnType is  
            MPLS. It is indexed by cpwVcIndex, which uniquely  
            identifying a singular connection. 
            
            .. attribute:: cpwvcindex
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsexpbits
            
            	Set by the operator to indicate the MPLS EXP bits to be   used on the VC shim label if cpwVcMplsExpBitsMode is    specifiedValue(2), zero otherwise
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: cpwvcmplsexpbitsmode
            
            	Set by the operator to indicate the way the VC shim label  EXP bits are to be determined. The value of outerTunnel(1)  is used where there is an outer tunnel \- cpwVcMplsMplsType   is mplsTe or mplsNonTe. Note that in this case there is no  need to mark the VC label with the EXP bits since the VC   label is not visible to the intermediate nodes.  If there is no outer tunnel, specifiedValue(2) indicate   that the value is specified by cpwVcMplsExpBits, and   serviceDependant(3) indicate that the EXP bits are setup   based on a rule specified in the emulated service specific   tables, for example when the EXP bits are a function of   802.1p marking for Ethernet emulated service
            	**type**\: :py:class:`CpwVcMplsExpBitsMode_Enum <ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsTable.CpwVcMplsEntry.CpwVcMplsExpBitsMode_Enum>`
            
            .. attribute:: cpwvcmplslocalldpentityid
            
            	The local LDP Entity index of the LDP entity to be used   for this VC on the local node. Should be set to all zeros   if not used
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplslocalldpid
            
            	The local LDP identifier of the LDP entity creating  this VC in the local node. As the VC labels are always  set from the per platform label space, the last two octets   in the LDP ID MUST be always both zeros
            	**type**\: str
            
            .. attribute:: cpwvcmplsmplstype
            
            	Set by the operator to indicate the outer tunnel types, if  exists. mplsTe is used if the outer tunnel was set\-up by   MPLS\-TE, and mplsNonTe is used the outer tunnel was set up  by LDP or manually. Combination of mplsTe and mplsNonTe   may exist in case of outer tunnel protection.  vcOnly is used if there is no outer tunnel label. vcOnly   cannot be combined with mplsNonTe or mplsTe
            	**type**\: :py:class:`CpwVcMplsMplsType_Bits <ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsTable.CpwVcMplsEntry.CpwVcMplsMplsType_Bits>`
            
            .. attribute:: cpwvcmplspeerldpid
            
            	The peer LDP identifier as identified from the LDP   session. Should be zero if not relevant or not known yet
            	**type**\: str
            
            .. attribute:: cpwvcmplsstoragetype
            
            	This variable indicates the storage type for this row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: cpwvcmplsttl
            
            	Set by the operator to indicate the VC TTL bits to be used  on the VC shim label
            	**type**\: int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'cisco-ietf-pw-mpls'
            _revision = '2003-02-26'

            def __init__(self):
                self.parent = None
                self.cpwvcindex = None
                self.cpwvcmplsexpbits = None
                self.cpwvcmplsexpbitsmode = None
                self.cpwvcmplslocalldpentityid = None
                self.cpwvcmplslocalldpid = None
                self.cpwvcmplsmplstype = CISCOIETFPWMPLSMIB.CpwVcMplsTable.CpwVcMplsEntry.CpwVcMplsMplsType_Bits()
                self.cpwvcmplspeerldpid = None
                self.cpwvcmplsstoragetype = None
                self.cpwvcmplsttl = None

            class CpwVcMplsExpBitsMode_Enum(Enum):
                """
                CpwVcMplsExpBitsMode_Enum

                Set by the operator to indicate the way the VC shim label 
                EXP bits are to be determined. The value of outerTunnel(1) 
                is used where there is an outer tunnel \- cpwVcMplsMplsType  
                is mplsTe or mplsNonTe. Note that in this case there is no 
                need to mark the VC label with the EXP bits since the VC  
                label is not visible to the intermediate nodes. 
                If there is no outer tunnel, specifiedValue(2) indicate  
                that the value is specified by cpwVcMplsExpBits, and  
                serviceDependant(3) indicate that the EXP bits are setup  
                based on a rule specified in the emulated service specific  
                tables, for example when the EXP bits are a function of  
                802.1p marking for Ethernet emulated service.

                """

                OUTERTUNNEL = 1

                SPECIFIEDVALUE = 2

                SERVICEDEPENDANT = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _CISCO_IETF_PW_MPLS_MIB as meta
                    return meta._meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsTable.CpwVcMplsEntry.CpwVcMplsExpBitsMode_Enum']


            class CpwVcMplsMplsType_Bits(FixedBitsDict):
                """
                CpwVcMplsMplsType_Bits

                Set by the operator to indicate the outer tunnel types, if 
                exists. mplsTe is used if the outer tunnel was set\-up by  
                MPLS\-TE, and mplsNonTe is used the outer tunnel was set up 
                by LDP or manually. Combination of mplsTe and mplsNonTe  
                may exist in case of outer tunnel protection. 
                vcOnly is used if there is no outer tunnel label. vcOnly  
                cannot be combined with mplsNonTe or mplsTe.
                Keys are:- mplsNonTe , vcOnly , mplsTe

                """

                def __init__(self):
                    self._dictionary = { 
                        'mplsNonTe':False,
                        'vcOnly':False,
                        'mplsTe':False,
                    }
                    self._pos_map = { 
                        'mplsNonTe':1,
                        'vcOnly':2,
                        'mplsTe':0,
                    }

            @property
            def _common_path(self):
                if self.cpwvcindex is None:
                    raise YPYDataValidationError('Key property cpwvcindex is None')

                return '/CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsTable/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsEntry[CISCO-IETF-PW-MPLS-MIB:cpwVcIndex = ' + str(self.cpwvcindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cpwvcindex is not None:
                    return True

                if self.cpwvcmplsexpbits is not None:
                    return True

                if self.cpwvcmplsexpbitsmode is not None:
                    return True

                if self.cpwvcmplslocalldpentityid is not None:
                    return True

                if self.cpwvcmplslocalldpid is not None:
                    return True

                if self.cpwvcmplsmplstype is not None:
                    if self.cpwvcmplsmplstype._has_data():
                        return True

                if self.cpwvcmplspeerldpid is not None:
                    return True

                if self.cpwvcmplsstoragetype is not None:
                    return True

                if self.cpwvcmplsttl is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _CISCO_IETF_PW_MPLS_MIB as meta
                return meta._meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsTable.CpwVcMplsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cpwvcmplsentry is not None:
                for child_ref in self.cpwvcmplsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _CISCO_IETF_PW_MPLS_MIB as meta
            return meta._meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsTable']['meta_info']


    class CpwVcMplsTeMappingTable(object):
        """
        This table maps an inbound/outbound Tunnel to a VC in  
        MPLS\-TE applications.
        
        .. attribute:: cpwvcmplstemappingentry
        
        	A row in this table represents the association  between a PW VC and it's MPLS\-TE outer Tunnel.   An application can use this table to quickly retrieve the   PW carried over specific TE MPLS outer tunnel.   The table in indexed by the 4 indexes of a TE tunnel,  the direction of the VC specific entry and the VcIndex.   The same table is used in both inbound and outbound  directions, a different row for each direction. If the   inbound association is not known, no rows should exist for   it.   Rows are created by the local agent when all the   association data is available for display
        	**type**\: list of :py:class:`CpwVcMplsTeMappingEntry <ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable.CpwVcMplsTeMappingEntry>`
        
        

        """

        _prefix = 'cisco-ietf-pw-mpls'
        _revision = '2003-02-26'

        def __init__(self):
            self.parent = None
            self.cpwvcmplstemappingentry = YList()
            self.cpwvcmplstemappingentry.parent = self
            self.cpwvcmplstemappingentry.name = 'cpwvcmplstemappingentry'


        class CpwVcMplsTeMappingEntry(object):
            """
            A row in this table represents the association 
            between a PW VC and it's MPLS\-TE outer Tunnel. 
            
            An application can use this table to quickly retrieve the  
            PW carried over specific TE MPLS outer tunnel. 
            
            The table in indexed by the 4 indexes of a TE tunnel, 
            the direction of the VC specific entry and the VcIndex. 
            
            The same table is used in both inbound and outbound 
            directions, a different row for each direction. If the  
            inbound association is not known, no rows should exist for  
            it. 
            
            Rows are created by the local agent when all the  
            association data is available for display.
            
            .. attribute:: cpwvcmplstemappingtunneldirection
            
            	Identifies if the row represent an outbound or inbound   mapping
            	**type**\: :py:class:`CpwVcMplsTeMappingTunnelDirection_Enum <ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB.CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable.CpwVcMplsTeMappingEntry.CpwVcMplsTeMappingTunnelDirection_Enum>`
            
            .. attribute:: cpwvcmplstemappingtunnelindex
            
            	Primary index for the conceptual row identifying the   MPLS\-TE tunnel
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cpwvcmplstemappingtunnelinstance
            
            	Identifies an instance of the MPLS\-TE tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplstemappingtunnellocallsrid
            
            	Identifies the local LSR
            	**type**\: str
            
            	**range:** 4
            
            .. attribute:: cpwvcmplstemappingtunnelpeerlsrid
            
            	Identifies an Peer LSR when the outer tunnel is MPLS\-TE   based
            	**type**\: str
            
            	**range:** 4
            
            .. attribute:: cpwvcmplstemappingvcindex
            
            	The value that represent the VC in the cpwVcTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-ietf-pw-mpls'
            _revision = '2003-02-26'

            def __init__(self):
                self.parent = None
                self.cpwvcmplstemappingtunneldirection = None
                self.cpwvcmplstemappingtunnelindex = None
                self.cpwvcmplstemappingtunnelinstance = None
                self.cpwvcmplstemappingtunnellocallsrid = None
                self.cpwvcmplstemappingtunnelpeerlsrid = None
                self.cpwvcmplstemappingvcindex = None

            class CpwVcMplsTeMappingTunnelDirection_Enum(Enum):
                """
                CpwVcMplsTeMappingTunnelDirection_Enum

                Identifies if the row represent an outbound or inbound  
                mapping.

                """

                OUTBOUND = 1

                INBOUND = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _CISCO_IETF_PW_MPLS_MIB as meta
                    return meta._meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable.CpwVcMplsTeMappingEntry.CpwVcMplsTeMappingTunnelDirection_Enum']


            @property
            def _common_path(self):
                if self.cpwvcmplstemappingtunneldirection is None:
                    raise YPYDataValidationError('Key property cpwvcmplstemappingtunneldirection is None')
                if self.cpwvcmplstemappingtunnelindex is None:
                    raise YPYDataValidationError('Key property cpwvcmplstemappingtunnelindex is None')
                if self.cpwvcmplstemappingtunnelinstance is None:
                    raise YPYDataValidationError('Key property cpwvcmplstemappingtunnelinstance is None')
                if self.cpwvcmplstemappingtunnellocallsrid is None:
                    raise YPYDataValidationError('Key property cpwvcmplstemappingtunnellocallsrid is None')
                if self.cpwvcmplstemappingtunnelpeerlsrid is None:
                    raise YPYDataValidationError('Key property cpwvcmplstemappingtunnelpeerlsrid is None')
                if self.cpwvcmplstemappingvcindex is None:
                    raise YPYDataValidationError('Key property cpwvcmplstemappingvcindex is None')

                return '/CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsTeMappingTable/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsTeMappingEntry[CISCO-IETF-PW-MPLS-MIB:cpwVcMplsTeMappingTunnelDirection = ' + str(self.cpwvcmplstemappingtunneldirection) + '][CISCO-IETF-PW-MPLS-MIB:cpwVcMplsTeMappingTunnelIndex = ' + str(self.cpwvcmplstemappingtunnelindex) + '][CISCO-IETF-PW-MPLS-MIB:cpwVcMplsTeMappingTunnelInstance = ' + str(self.cpwvcmplstemappingtunnelinstance) + '][CISCO-IETF-PW-MPLS-MIB:cpwVcMplsTeMappingTunnelLocalLsrID = ' + str(self.cpwvcmplstemappingtunnellocallsrid) + '][CISCO-IETF-PW-MPLS-MIB:cpwVcMplsTeMappingTunnelPeerLsrID = ' + str(self.cpwvcmplstemappingtunnelpeerlsrid) + '][CISCO-IETF-PW-MPLS-MIB:cpwVcMplsTeMappingVcIndex = ' + str(self.cpwvcmplstemappingvcindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cpwvcmplstemappingtunneldirection is not None:
                    return True

                if self.cpwvcmplstemappingtunnelindex is not None:
                    return True

                if self.cpwvcmplstemappingtunnelinstance is not None:
                    return True

                if self.cpwvcmplstemappingtunnellocallsrid is not None:
                    return True

                if self.cpwvcmplstemappingtunnelpeerlsrid is not None:
                    return True

                if self.cpwvcmplstemappingvcindex is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _CISCO_IETF_PW_MPLS_MIB as meta
                return meta._meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable.CpwVcMplsTeMappingEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsTeMappingTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cpwvcmplstemappingentry is not None:
                for child_ref in self.cpwvcmplstemappingentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _CISCO_IETF_PW_MPLS_MIB as meta
            return meta._meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cpwvcmplsinboundtable is not None and self.cpwvcmplsinboundtable._has_data():
            return True

        if self.cpwvcmplsinboundtable is not None and self.cpwvcmplsinboundtable.is_presence():
            return True

        if self.cpwvcmplsnontemappingtable is not None and self.cpwvcmplsnontemappingtable._has_data():
            return True

        if self.cpwvcmplsnontemappingtable is not None and self.cpwvcmplsnontemappingtable.is_presence():
            return True

        if self.cpwvcmplsobjects is not None and self.cpwvcmplsobjects._has_data():
            return True

        if self.cpwvcmplsobjects is not None and self.cpwvcmplsobjects.is_presence():
            return True

        if self.cpwvcmplsoutboundtable is not None and self.cpwvcmplsoutboundtable._has_data():
            return True

        if self.cpwvcmplsoutboundtable is not None and self.cpwvcmplsoutboundtable.is_presence():
            return True

        if self.cpwvcmplstable is not None and self.cpwvcmplstable._has_data():
            return True

        if self.cpwvcmplstable is not None and self.cpwvcmplstable.is_presence():
            return True

        if self.cpwvcmplstemappingtable is not None and self.cpwvcmplstemappingtable._has_data():
            return True

        if self.cpwvcmplstemappingtable is not None and self.cpwvcmplstemappingtable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _CISCO_IETF_PW_MPLS_MIB as meta
        return meta._meta_table['CISCOIETFPWMPLSMIB']['meta_info']



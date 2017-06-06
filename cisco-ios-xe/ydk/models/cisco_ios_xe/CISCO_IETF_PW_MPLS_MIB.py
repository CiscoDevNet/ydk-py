""" CISCO_IETF_PW_MPLS_MIB 

This MIB complements the CISCO\-IETF\-PW\-MIB for PW operation 
over MPLS. 

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoIetfPwMplsMib(object):
    """
    
    
    .. attribute:: cpwvcmplsinboundtable
    
    	This table associates VCs using MPLS PSN with the inbound  MPLS tunnels (i.e. for packets coming from the PSN),   if such association is desired (mainly for security   reasons)
    	**type**\:   :py:class:`Cpwvcmplsinboundtable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplsinboundtable>`
    
    .. attribute:: cpwvcmplsnontemappingtable
    
    	This table maps an inbound/outbound Tunnel to a VC in non\-  TE applications
    	**type**\:   :py:class:`Cpwvcmplsnontemappingtable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable>`
    
    .. attribute:: cpwvcmplsobjects
    
    	
    	**type**\:   :py:class:`Cpwvcmplsobjects <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplsobjects>`
    
    .. attribute:: cpwvcmplsoutboundtable
    
    	This table associates VCs using MPLS PSN with the outbound  MPLS tunnels (i.e. toward the PSN) or the physical   interface in case of VC only
    	**type**\:   :py:class:`Cpwvcmplsoutboundtable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplsoutboundtable>`
    
    .. attribute:: cpwvcmplstable
    
    	This table specifies information for VC to be carried over   MPLS PSN
    	**type**\:   :py:class:`Cpwvcmplstable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplstable>`
    
    .. attribute:: cpwvcmplstemappingtable
    
    	This table maps an inbound/outbound Tunnel to a VC in   MPLS\-TE applications
    	**type**\:   :py:class:`Cpwvcmplstemappingtable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplstemappingtable>`
    
    

    """

    _prefix = 'CISCO-IETF-PW-MPLS-MIB'
    _revision = '2003-02-26'

    def __init__(self):
        self.cpwvcmplsinboundtable = CiscoIetfPwMplsMib.Cpwvcmplsinboundtable()
        self.cpwvcmplsinboundtable.parent = self
        self.cpwvcmplsnontemappingtable = CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable()
        self.cpwvcmplsnontemappingtable.parent = self
        self.cpwvcmplsobjects = CiscoIetfPwMplsMib.Cpwvcmplsobjects()
        self.cpwvcmplsobjects.parent = self
        self.cpwvcmplsoutboundtable = CiscoIetfPwMplsMib.Cpwvcmplsoutboundtable()
        self.cpwvcmplsoutboundtable.parent = self
        self.cpwvcmplstable = CiscoIetfPwMplsMib.Cpwvcmplstable()
        self.cpwvcmplstable.parent = self
        self.cpwvcmplstemappingtable = CiscoIetfPwMplsMib.Cpwvcmplstemappingtable()
        self.cpwvcmplstemappingtable.parent = self


    class Cpwvcmplsobjects(object):
        """
        
        
        .. attribute:: cpwvcmplsinboundindexnext
        
        	This object contains an appropriate value to  be used for cpwVcMplsInboundIndex when creating  entries in the cpwVcMplsInboundTable. The value  0 indicates that no unassigned entries are  available. To obtain the cpwVcMplsInboundIndex  value for a new entry, the manager issues a  management protocol retrieval operation to obtain  the current value of this object.  After each  retrieval, the agent should modify the value to  the next unassigned index, however the agent MUST  NOT assume such retrieval will be done for each   row created
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cpwvcmplsoutboundindexnext
        
        	This object contains an appropriate value to  be used for cpwVcMplsOutboundIndex when creating  entries in the cpwVcMplsOutboundTable. The value  0 indicates that no unassigned entries are  available. To obtain the cpwVcMplsOutboundIndex  value for a new entry, the manager issues a  management protocol retrieval operation to obtain  the current value of this object.  After each  retrieval, the agent should modify the value to  the next unassigned index, however the agent MUST  NOT assume such retrieval will be done for each   row created
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-IETF-PW-MPLS-MIB'
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
            if self.cpwvcmplsinboundindexnext is not None:
                return True

            if self.cpwvcmplsoutboundindexnext is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MPLS_MIB as meta
            return meta._meta_table['CiscoIetfPwMplsMib.Cpwvcmplsobjects']['meta_info']


    class Cpwvcmplstable(object):
        """
        This table specifies information for VC to be carried over  
        MPLS PSN.
        
        .. attribute:: cpwvcmplsentry
        
        	A row in this table represents parameters specific to MPLS   PSN for a pseudo wire connection (VC). The row is created   automatically by the local agent if the cpwVcPsnType is   MPLS. It is indexed by cpwVcIndex, which uniquely   identifying a singular connection. 
        	**type**\: list of    :py:class:`Cpwvcmplsentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplstable.Cpwvcmplsentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MPLS-MIB'
        _revision = '2003-02-26'

        def __init__(self):
            self.parent = None
            self.cpwvcmplsentry = YList()
            self.cpwvcmplsentry.parent = self
            self.cpwvcmplsentry.name = 'cpwvcmplsentry'


        class Cpwvcmplsentry(object):
            """
            A row in this table represents parameters specific to MPLS  
            PSN for a pseudo wire connection (VC). The row is created  
            automatically by the local agent if the cpwVcPsnType is  
            MPLS. It is indexed by cpwVcIndex, which uniquely  
            identifying a singular connection. 
            
            .. attribute:: cpwvcindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwvcmplsexpbits
            
            	Set by the operator to indicate the MPLS EXP bits to be   used on the VC shim label if cpwVcMplsExpBitsMode is    specifiedValue(2), zero otherwise
            	**type**\:  int
            
            	**range:** 0..7
            
            .. attribute:: cpwvcmplsexpbitsmode
            
            	Set by the operator to indicate the way the VC shim label  EXP bits are to be determined. The value of outerTunnel(1)  is used where there is an outer tunnel \- cpwVcMplsMplsType   is mplsTe or mplsNonTe. Note that in this case there is no  need to mark the VC label with the EXP bits since the VC   label is not visible to the intermediate nodes.  If there is no outer tunnel, specifiedValue(2) indicate   that the value is specified by cpwVcMplsExpBits, and   serviceDependant(3) indicate that the EXP bits are setup   based on a rule specified in the emulated service specific   tables, for example when the EXP bits are a function of   802.1p marking for Ethernet emulated service
            	**type**\:   :py:class:`CpwvcmplsexpbitsmodeEnum <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplstable.Cpwvcmplsentry.CpwvcmplsexpbitsmodeEnum>`
            
            .. attribute:: cpwvcmplslocalldpentityid
            
            	The local LDP Entity index of the LDP entity to be used   for this VC on the local node. Should be set to all zeros   if not used
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplslocalldpid
            
            	The local LDP identifier of the LDP entity creating  this VC in the local node. As the VC labels are always  set from the per platform label space, the last two octets   in the LDP ID MUST be always both zeros
            	**type**\:  str
            
            .. attribute:: cpwvcmplsmplstype
            
            	Set by the operator to indicate the outer tunnel types, if  exists. mplsTe is used if the outer tunnel was set\-up by   MPLS\-TE, and mplsNonTe is used the outer tunnel was set up  by LDP or manually. Combination of mplsTe and mplsNonTe   may exist in case of outer tunnel protection.  vcOnly is used if there is no outer tunnel label. vcOnly   cannot be combined with mplsNonTe or mplsTe
            	**type**\:   :py:class:`Cpwvcmplsmplstype <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplstable.Cpwvcmplsentry.Cpwvcmplsmplstype>`
            
            .. attribute:: cpwvcmplspeerldpid
            
            	The peer LDP identifier as identified from the LDP   session. Should be zero if not relevant or not known yet
            	**type**\:  str
            
            .. attribute:: cpwvcmplsstoragetype
            
            	This variable indicates the storage type for this row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            .. attribute:: cpwvcmplsttl
            
            	Set by the operator to indicate the VC TTL bits to be used  on the VC shim label
            	**type**\:  int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'CISCO-IETF-PW-MPLS-MIB'
            _revision = '2003-02-26'

            def __init__(self):
                self.parent = None
                self.cpwvcindex = None
                self.cpwvcmplsexpbits = None
                self.cpwvcmplsexpbitsmode = None
                self.cpwvcmplslocalldpentityid = None
                self.cpwvcmplslocalldpid = None
                self.cpwvcmplsmplstype = CiscoIetfPwMplsMib.Cpwvcmplstable.Cpwvcmplsentry.Cpwvcmplsmplstype()
                self.cpwvcmplspeerldpid = None
                self.cpwvcmplsstoragetype = None
                self.cpwvcmplsttl = None

            class CpwvcmplsexpbitsmodeEnum(Enum):
                """
                CpwvcmplsexpbitsmodeEnum

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

                .. data:: outerTunnel = 1

                .. data:: specifiedValue = 2

                .. data:: serviceDependant = 3

                """

                outerTunnel = 1

                specifiedValue = 2

                serviceDependant = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MPLS_MIB as meta
                    return meta._meta_table['CiscoIetfPwMplsMib.Cpwvcmplstable.Cpwvcmplsentry.CpwvcmplsexpbitsmodeEnum']


            class Cpwvcmplsmplstype(FixedBitsDict):
                """
                Cpwvcmplsmplstype

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
                    raise YPYModelError('Key property cpwvcindex is None')

                return '/CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsTable/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsEntry[CISCO-IETF-PW-MPLS-MIB:cpwVcIndex = ' + str(self.cpwvcindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MPLS_MIB as meta
                return meta._meta_table['CiscoIetfPwMplsMib.Cpwvcmplstable.Cpwvcmplsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpwvcmplsentry is not None:
                for child_ref in self.cpwvcmplsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MPLS_MIB as meta
            return meta._meta_table['CiscoIetfPwMplsMib.Cpwvcmplstable']['meta_info']


    class Cpwvcmplsoutboundtable(object):
        """
        This table associates VCs using MPLS PSN with the outbound 
        MPLS tunnels (i.e. toward the PSN) or the physical  
        interface in case of VC only.
        
        .. attribute:: cpwvcmplsoutboundentry
        
        	A row in this table represents a link between PW VC (that  require MPLS tunnels) and MPLS tunnel toward the PSN.  In the case of VC only, it associate the VC with the   interface that shall carry the VC.  This table is indexed by the pwVcIndex and an additional  index enabling multiple rows for the same VC index.   At least one entry is created in this table by the operator   for each PW VC that requires MPLS PSN. Note that the first  entry for each VC can be indexed by cpwVcMplsOutboundIndex   equal zero without a need for retrieval of   cpwVcMplsOutboundIndexNext.   This table points to the appropriate MPLS MIB. In the case   of MPLS\-TE, the 4 variables relevant to the indexing of   a TE MPLS tunnel are set as in Srinivasan, et al, <draft\-  ietf\-mpls\-te\-mib>.  In case of Non\-TE MPLS (an outer tunnel label assigned by   LDP or manually) the table points to the XC entry in the   LSR MIB as in Srinivasan, et al, <draft\-ietf\-mpls\-lsr\-mib>.  In case of VC only (no outer tunnel) the ifIndex of the  port to carry the VC is configured.    Each VC may have multiple rows in this tables if protection   is available at the outer tunnel level, each row may be of  different type except for VC only, on which only rows with  ifIndex of the port are allowed. 
        	**type**\: list of    :py:class:`Cpwvcmplsoutboundentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplsoutboundtable.Cpwvcmplsoutboundentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MPLS-MIB'
        _revision = '2003-02-26'

        def __init__(self):
            self.parent = None
            self.cpwvcmplsoutboundentry = YList()
            self.cpwvcmplsoutboundentry.parent = self
            self.cpwvcmplsoutboundentry.name = 'cpwvcmplsoutboundentry'


        class Cpwvcmplsoutboundentry(object):
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
            
            .. attribute:: cpwvcindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwvcmplsoutboundindex  <key>
            
            	Arbitrary index for enabling multiple rows per VC in  this table. Next available free index can be retrieved   using cpwVcMplsOutboundIndexNext. 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsoutboundifindex
            
            	In case of VC only (no outer tunnel), this object holds  the ifIndex of the outbound port, otherwise set to zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cpwvcmplsoutboundlsrxcindex
            
            	This object will be set by the operator. If the outer  label is defined in the MPL\-LSR\-MIB, i.e. set by LDP  or manually, this object points to the XC index   of the outer tunnel. Otherwise, it is set to zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsoutboundrowstatus
            
            	For creating, modifying, and deleting this row
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: cpwvcmplsoutboundstoragetype
            
            	This variable indicates the storage type for this object
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            .. attribute:: cpwvcmplsoutboundtunnelindex
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cpwvcmplsoutboundtunnelinstance
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsoutboundtunnellcllsr
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: cpwvcmplsoutboundtunnelpeerlsr
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\:  str
            
            	**length:** 4
            
            

            """

            _prefix = 'CISCO-IETF-PW-MPLS-MIB'
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
                    raise YPYModelError('Key property cpwvcindex is None')
                if self.cpwvcmplsoutboundindex is None:
                    raise YPYModelError('Key property cpwvcmplsoutboundindex is None')

                return '/CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsOutboundTable/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsOutboundEntry[CISCO-IETF-PW-MPLS-MIB:cpwVcIndex = ' + str(self.cpwvcindex) + '][CISCO-IETF-PW-MPLS-MIB:cpwVcMplsOutboundIndex = ' + str(self.cpwvcmplsoutboundindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MPLS_MIB as meta
                return meta._meta_table['CiscoIetfPwMplsMib.Cpwvcmplsoutboundtable.Cpwvcmplsoutboundentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsOutboundTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpwvcmplsoutboundentry is not None:
                for child_ref in self.cpwvcmplsoutboundentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MPLS_MIB as meta
            return meta._meta_table['CiscoIetfPwMplsMib.Cpwvcmplsoutboundtable']['meta_info']


    class Cpwvcmplsinboundtable(object):
        """
        This table associates VCs using MPLS PSN with the inbound 
        MPLS tunnels (i.e. for packets coming from the PSN),  
        if such association is desired (mainly for security  
        reasons).
        
        .. attribute:: cpwvcmplsinboundentry
        
        	A row in this table represents a link between PW VCs (that  require MPLS tunnels) and MPLS tunnel for packets arriving  from the PSN.  This table is indexed by the set of indexes used to  identify the VC \- cpwVcIndex and an additional  index enabling multiple rows for the same VC index.   Note that the first entry for each VC can be indexed by   cpwVcMplsOutboundIndex equal zero without a need for   retrieval of cpwVcMplsInboundIndexNext.   An entry is created in this table either automatically by   the local agent or created manually by the operator in   cases that strict mode is required.   Note that the control messages contain VC ID and VC type,   which together with the remote IP address identify the  cpwVcIndex in the local node.  This table points to the appropriate MPLS MIB. In the case   of MPLS\-TE, the 4 variables relevant to the indexing of a  TE MPLS tunnel are set as in Srinivasan, et al, <draft\-  ietf\-mpls\-te\-mib>.   In case of non\-TE MPLS tunnel (an outer tunnel label   assigned by LDP or manually) the table points to the XC   entry in the MPLS\-LSR\-MIB as in Srinivasan, et al, <draft\-  ietf\-mpls\-lsr\-mib>.   Each VC may have multiple rows in this tables if protection   is available at the outer tunnel level, each row may be of  different type except for VC only, on which only rows with  ifIndex of the port are allowed. 
        	**type**\: list of    :py:class:`Cpwvcmplsinboundentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplsinboundtable.Cpwvcmplsinboundentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MPLS-MIB'
        _revision = '2003-02-26'

        def __init__(self):
            self.parent = None
            self.cpwvcmplsinboundentry = YList()
            self.cpwvcmplsinboundentry.parent = self
            self.cpwvcmplsinboundentry.name = 'cpwvcmplsinboundentry'


        class Cpwvcmplsinboundentry(object):
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
            
            .. attribute:: cpwvcindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwvcmplsinboundindex  <key>
            
            	Arbitrary index for enabling multiple rows per VC in  this table. Next available free index can be retrieved  using cpwVcMplsInboundIndexNext. 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsinboundifindex
            
            	In case of VC only (no outer tunnel), this object holds the  ifIndex of the inbound port, otherwise set to zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cpwvcmplsinboundlsrxcindex
            
            	If the outer label is defined in the MPL\-LSR\-MIB, i.e. set   by LDP or manually, this object points to the XC index   of the outer tunnel. Otherwise, it is set to zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsinboundrowstatus
            
            	For creating, modifying, and deleting this row
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: cpwvcmplsinboundstoragetype
            
            	This variable indicates the storage type for this row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            .. attribute:: cpwvcmplsinboundtunnelindex
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cpwvcmplsinboundtunnelinstance
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsinboundtunnellcllsr
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: cpwvcmplsinboundtunnelpeerlsr
            
            	Part of set of indexes for outbound tunnel in the case of   MPLS\-TE outer tunnel, otherwise set to zero
            	**type**\:  str
            
            	**length:** 4
            
            

            """

            _prefix = 'CISCO-IETF-PW-MPLS-MIB'
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
                    raise YPYModelError('Key property cpwvcindex is None')
                if self.cpwvcmplsinboundindex is None:
                    raise YPYModelError('Key property cpwvcmplsinboundindex is None')

                return '/CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsInboundTable/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsInboundEntry[CISCO-IETF-PW-MPLS-MIB:cpwVcIndex = ' + str(self.cpwvcindex) + '][CISCO-IETF-PW-MPLS-MIB:cpwVcMplsInboundIndex = ' + str(self.cpwvcmplsinboundindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MPLS_MIB as meta
                return meta._meta_table['CiscoIetfPwMplsMib.Cpwvcmplsinboundtable.Cpwvcmplsinboundentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsInboundTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpwvcmplsinboundentry is not None:
                for child_ref in self.cpwvcmplsinboundentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MPLS_MIB as meta
            return meta._meta_table['CiscoIetfPwMplsMib.Cpwvcmplsinboundtable']['meta_info']


    class Cpwvcmplsnontemappingtable(object):
        """
        This table maps an inbound/outbound Tunnel to a VC in non\- 
        TE applications.
        
        .. attribute:: cpwvcmplsnontemappingentry
        
        	A row in this table represents the association  between the PW VC and it's non TE MPLS outer Tunnel  it's physical interface if there is no outer tunnel   (VC only).   An application can use this table to quickly retrieve the   PW carried over specific non\-TE MPLS outer tunnel or   physical interface.   The table in indexed by the XC index for MPLS Non\-TE   tunnel, or ifIndex of the port in VC only case, the   direction of the VC in the specific entry and the VCIndex.   The same table is used in both inbound and outbound  directions, but in a different row for each direction. If   the inbound association is not known, no rows should exist   for it.   Rows are created by the local agent when all the   association data is available for display
        	**type**\: list of    :py:class:`Cpwvcmplsnontemappingentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable.Cpwvcmplsnontemappingentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MPLS-MIB'
        _revision = '2003-02-26'

        def __init__(self):
            self.parent = None
            self.cpwvcmplsnontemappingentry = YList()
            self.cpwvcmplsnontemappingentry.parent = self
            self.cpwvcmplsnontemappingentry.name = 'cpwvcmplsnontemappingentry'


        class Cpwvcmplsnontemappingentry(object):
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
            
            .. attribute:: cpwvcmplsnontemappingtunneldirection  <key>
            
            	Identifies if the row represent an outbound or inbound   mapping
            	**type**\:   :py:class:`CpwvcmplsnontemappingtunneldirectionEnum <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable.Cpwvcmplsnontemappingentry.CpwvcmplsnontemappingtunneldirectionEnum>`
            
            .. attribute:: cpwvcmplsnontemappingxctunnelindex  <key>
            
            	Index for the conceptual XC row identifying Tunnel to VC   mappings when the outer tunnel is created by the MPLS\-LSR\-  MIB, Zero otherwise
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplsnontemappingifindex  <key>
            
            	Identify the port on which the VC is carried for VC only   case
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cpwvcmplsnontemappingvcindex  <key>
            
            	The value that represent the VC in the cpwVcTable
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-PW-MPLS-MIB'
            _revision = '2003-02-26'

            def __init__(self):
                self.parent = None
                self.cpwvcmplsnontemappingtunneldirection = None
                self.cpwvcmplsnontemappingxctunnelindex = None
                self.cpwvcmplsnontemappingifindex = None
                self.cpwvcmplsnontemappingvcindex = None

            class CpwvcmplsnontemappingtunneldirectionEnum(Enum):
                """
                CpwvcmplsnontemappingtunneldirectionEnum

                Identifies if the row represent an outbound or inbound  

                mapping.

                .. data:: outbound = 1

                .. data:: inbound = 2

                """

                outbound = 1

                inbound = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MPLS_MIB as meta
                    return meta._meta_table['CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable.Cpwvcmplsnontemappingentry.CpwvcmplsnontemappingtunneldirectionEnum']


            @property
            def _common_path(self):
                if self.cpwvcmplsnontemappingtunneldirection is None:
                    raise YPYModelError('Key property cpwvcmplsnontemappingtunneldirection is None')
                if self.cpwvcmplsnontemappingxctunnelindex is None:
                    raise YPYModelError('Key property cpwvcmplsnontemappingxctunnelindex is None')
                if self.cpwvcmplsnontemappingifindex is None:
                    raise YPYModelError('Key property cpwvcmplsnontemappingifindex is None')
                if self.cpwvcmplsnontemappingvcindex is None:
                    raise YPYModelError('Key property cpwvcmplsnontemappingvcindex is None')

                return '/CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsNonTeMappingTable/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsNonTeMappingEntry[CISCO-IETF-PW-MPLS-MIB:cpwVcMplsNonTeMappingTunnelDirection = ' + str(self.cpwvcmplsnontemappingtunneldirection) + '][CISCO-IETF-PW-MPLS-MIB:cpwVcMplsNonTeMappingXcTunnelIndex = ' + str(self.cpwvcmplsnontemappingxctunnelindex) + '][CISCO-IETF-PW-MPLS-MIB:cpwVcMplsNonTeMappingIfIndex = ' + str(self.cpwvcmplsnontemappingifindex) + '][CISCO-IETF-PW-MPLS-MIB:cpwVcMplsNonTeMappingVcIndex = ' + str(self.cpwvcmplsnontemappingvcindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cpwvcmplsnontemappingtunneldirection is not None:
                    return True

                if self.cpwvcmplsnontemappingxctunnelindex is not None:
                    return True

                if self.cpwvcmplsnontemappingifindex is not None:
                    return True

                if self.cpwvcmplsnontemappingvcindex is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MPLS_MIB as meta
                return meta._meta_table['CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable.Cpwvcmplsnontemappingentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsNonTeMappingTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpwvcmplsnontemappingentry is not None:
                for child_ref in self.cpwvcmplsnontemappingentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MPLS_MIB as meta
            return meta._meta_table['CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable']['meta_info']


    class Cpwvcmplstemappingtable(object):
        """
        This table maps an inbound/outbound Tunnel to a VC in  
        MPLS\-TE applications.
        
        .. attribute:: cpwvcmplstemappingentry
        
        	A row in this table represents the association  between a PW VC and it's MPLS\-TE outer Tunnel.   An application can use this table to quickly retrieve the   PW carried over specific TE MPLS outer tunnel.   The table in indexed by the 4 indexes of a TE tunnel,  the direction of the VC specific entry and the VcIndex.   The same table is used in both inbound and outbound  directions, a different row for each direction. If the   inbound association is not known, no rows should exist for   it.   Rows are created by the local agent when all the   association data is available for display
        	**type**\: list of    :py:class:`Cpwvcmplstemappingentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplstemappingtable.Cpwvcmplstemappingentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-MPLS-MIB'
        _revision = '2003-02-26'

        def __init__(self):
            self.parent = None
            self.cpwvcmplstemappingentry = YList()
            self.cpwvcmplstemappingentry.parent = self
            self.cpwvcmplstemappingentry.name = 'cpwvcmplstemappingentry'


        class Cpwvcmplstemappingentry(object):
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
            
            .. attribute:: cpwvcmplstemappingtunneldirection  <key>
            
            	Identifies if the row represent an outbound or inbound   mapping
            	**type**\:   :py:class:`CpwvcmplstemappingtunneldirectionEnum <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB.CiscoIetfPwMplsMib.Cpwvcmplstemappingtable.Cpwvcmplstemappingentry.CpwvcmplstemappingtunneldirectionEnum>`
            
            .. attribute:: cpwvcmplstemappingtunnelindex  <key>
            
            	Primary index for the conceptual row identifying the   MPLS\-TE tunnel
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cpwvcmplstemappingtunnelinstance  <key>
            
            	Identifies an instance of the MPLS\-TE tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwvcmplstemappingtunnelpeerlsrid  <key>
            
            	Identifies an Peer LSR when the outer tunnel is MPLS\-TE   based
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: cpwvcmplstemappingtunnellocallsrid  <key>
            
            	Identifies the local LSR
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: cpwvcmplstemappingvcindex  <key>
            
            	The value that represent the VC in the cpwVcTable
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-PW-MPLS-MIB'
            _revision = '2003-02-26'

            def __init__(self):
                self.parent = None
                self.cpwvcmplstemappingtunneldirection = None
                self.cpwvcmplstemappingtunnelindex = None
                self.cpwvcmplstemappingtunnelinstance = None
                self.cpwvcmplstemappingtunnelpeerlsrid = None
                self.cpwvcmplstemappingtunnellocallsrid = None
                self.cpwvcmplstemappingvcindex = None

            class CpwvcmplstemappingtunneldirectionEnum(Enum):
                """
                CpwvcmplstemappingtunneldirectionEnum

                Identifies if the row represent an outbound or inbound  

                mapping.

                .. data:: outbound = 1

                .. data:: inbound = 2

                """

                outbound = 1

                inbound = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MPLS_MIB as meta
                    return meta._meta_table['CiscoIetfPwMplsMib.Cpwvcmplstemappingtable.Cpwvcmplstemappingentry.CpwvcmplstemappingtunneldirectionEnum']


            @property
            def _common_path(self):
                if self.cpwvcmplstemappingtunneldirection is None:
                    raise YPYModelError('Key property cpwvcmplstemappingtunneldirection is None')
                if self.cpwvcmplstemappingtunnelindex is None:
                    raise YPYModelError('Key property cpwvcmplstemappingtunnelindex is None')
                if self.cpwvcmplstemappingtunnelinstance is None:
                    raise YPYModelError('Key property cpwvcmplstemappingtunnelinstance is None')
                if self.cpwvcmplstemappingtunnelpeerlsrid is None:
                    raise YPYModelError('Key property cpwvcmplstemappingtunnelpeerlsrid is None')
                if self.cpwvcmplstemappingtunnellocallsrid is None:
                    raise YPYModelError('Key property cpwvcmplstemappingtunnellocallsrid is None')
                if self.cpwvcmplstemappingvcindex is None:
                    raise YPYModelError('Key property cpwvcmplstemappingvcindex is None')

                return '/CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsTeMappingTable/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsTeMappingEntry[CISCO-IETF-PW-MPLS-MIB:cpwVcMplsTeMappingTunnelDirection = ' + str(self.cpwvcmplstemappingtunneldirection) + '][CISCO-IETF-PW-MPLS-MIB:cpwVcMplsTeMappingTunnelIndex = ' + str(self.cpwvcmplstemappingtunnelindex) + '][CISCO-IETF-PW-MPLS-MIB:cpwVcMplsTeMappingTunnelInstance = ' + str(self.cpwvcmplstemappingtunnelinstance) + '][CISCO-IETF-PW-MPLS-MIB:cpwVcMplsTeMappingTunnelPeerLsrID = ' + str(self.cpwvcmplstemappingtunnelpeerlsrid) + '][CISCO-IETF-PW-MPLS-MIB:cpwVcMplsTeMappingTunnelLocalLsrID = ' + str(self.cpwvcmplstemappingtunnellocallsrid) + '][CISCO-IETF-PW-MPLS-MIB:cpwVcMplsTeMappingVcIndex = ' + str(self.cpwvcmplstemappingvcindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cpwvcmplstemappingtunneldirection is not None:
                    return True

                if self.cpwvcmplstemappingtunnelindex is not None:
                    return True

                if self.cpwvcmplstemappingtunnelinstance is not None:
                    return True

                if self.cpwvcmplstemappingtunnelpeerlsrid is not None:
                    return True

                if self.cpwvcmplstemappingtunnellocallsrid is not None:
                    return True

                if self.cpwvcmplstemappingvcindex is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MPLS_MIB as meta
                return meta._meta_table['CiscoIetfPwMplsMib.Cpwvcmplstemappingtable.Cpwvcmplstemappingentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB/CISCO-IETF-PW-MPLS-MIB:cpwVcMplsTeMappingTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpwvcmplstemappingentry is not None:
                for child_ref in self.cpwvcmplstemappingentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MPLS_MIB as meta
            return meta._meta_table['CiscoIetfPwMplsMib.Cpwvcmplstemappingtable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IETF-PW-MPLS-MIB:CISCO-IETF-PW-MPLS-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cpwvcmplsinboundtable is not None and self.cpwvcmplsinboundtable._has_data():
            return True

        if self.cpwvcmplsnontemappingtable is not None and self.cpwvcmplsnontemappingtable._has_data():
            return True

        if self.cpwvcmplsobjects is not None and self.cpwvcmplsobjects._has_data():
            return True

        if self.cpwvcmplsoutboundtable is not None and self.cpwvcmplsoutboundtable._has_data():
            return True

        if self.cpwvcmplstable is not None and self.cpwvcmplstable._has_data():
            return True

        if self.cpwvcmplstemappingtable is not None and self.cpwvcmplstemappingtable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_MPLS_MIB as meta
        return meta._meta_table['CiscoIetfPwMplsMib']['meta_info']



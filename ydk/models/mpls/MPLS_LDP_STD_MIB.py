""" MPLS_LDP_STD_MIB 

Copyright (C) The Internet Society (2004). The
initial version of this MIB module was published


in RFC 3815. For full legal notices see the RFC
itself or see\:
http\://www.ietf.org/copyrights/ianamib.html

This MIB contains managed object definitions for the
'Multiprotocol Label Switching, Label Distribution
Protocol, LDP' document.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.inet.INET_ADDRESS_MIB import InetAddressType_Enum
from ydk.models.mpls.MPLS_TC_STD_MIB import MplsLabelDistributionMethod_Enum
from ydk.models.mpls.MPLS_TC_STD_MIB import MplsLdpLabelType_Enum
from ydk.models.mpls.MPLS_TC_STD_MIB import MplsLspType_Enum
from ydk.models.mpls.MPLS_TC_STD_MIB import MplsRetentionMode_Enum
from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum
from ydk.models.snmpv2.SNMPv2_TC import StorageType_Enum


class MPLSLDPSTDMIB(object):
    """
    
    
    .. attribute:: mplsfecobjects
    
    	
    	**type**\: :py:class:`MplsFecObjects <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsFecObjects>`
    
    .. attribute:: mplsfectable
    
    	This table represents the FEC (Forwarding Equivalence Class) Information associated with an LSP
    	**type**\: :py:class:`MplsFecTable <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsFecTable>`
    
    .. attribute:: mplsinsegmentldplsptable
    
    	A table of LDP LSP's which map to the mplsInSegmentTable in the MPLS\-LSR\-STD\-MIB module
    	**type**\: :py:class:`MplsInSegmentLdpLspTable <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsInSegmentLdpLspTable>`
    
    .. attribute:: mplsldpentityobjects
    
    	
    	**type**\: :py:class:`MplsLdpEntityObjects <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpEntityObjects>`
    
    .. attribute:: mplsldpentitytable
    
    	This table contains information about the MPLS Label Distribution Protocol Entities which exist on this Label Switching Router (LSR) or Label Edge Router (LER)
    	**type**\: :py:class:`MplsLdpEntityTable <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpEntityTable>`
    
    .. attribute:: mplsldphelloadjacencytable
    
    	A table of Hello Adjacencies for Sessions
    	**type**\: :py:class:`MplsLdpHelloAdjacencyTable <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpHelloAdjacencyTable>`
    
    .. attribute:: mplsldplspfectable
    
    	A table which shows the relationship between LDP LSPs and FECs.  Each row represents a single LDP LSP to FEC association
    	**type**\: :py:class:`MplsLdpLspFecTable <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpLspFecTable>`
    
    .. attribute:: mplsldplsrobjects
    
    	
    	**type**\: :py:class:`MplsLdpLsrObjects <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpLsrObjects>`
    
    .. attribute:: mplsldppeertable
    
    	Information about LDP peers known by Entities in the mplsLdpEntityTable.  The information in this table is based on information from the Entity\-Peer interaction during session initialization but is not appropriate for the mplsLdpSessionTable, because objects in this table may or may not be used in session establishment
    	**type**\: :py:class:`MplsLdpPeerTable <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpPeerTable>`
    
    .. attribute:: mplsldpsessionobjects
    
    	
    	**type**\: :py:class:`MplsLdpSessionObjects <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpSessionObjects>`
    
    .. attribute:: mplsldpsessionpeeraddrtable
    
    	This table 'extends' the mplsLdpSessionTable. This table is used to store Label Address Information from Label Address Messages received by this LSR from Peers.  This table is read\-only and should be updated   when Label Withdraw Address Messages are received, i.e., Rows should be deleted as appropriate.  NOTE\:  since more than one address may be contained in a Label Address Message, this table 'sparse augments', the mplsLdpSessionTable's information
    	**type**\: :py:class:`MplsLdpSessionPeerAddrTable <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpSessionPeerAddrTable>`
    
    .. attribute:: mplsoutsegmentldplsptable
    
    	A table of LDP LSP's which map to the mplsOutSegmentTable in the MPLS\-LSR\-STD\-MIB
    	**type**\: :py:class:`MplsOutSegmentLdpLspTable <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsOutSegmentLdpLspTable>`
    
    

    """

    _prefix = 'mpls-ldp'
    _revision = '2004-06-03'

    def __init__(self):
        self.mplsfecobjects = MPLSLDPSTDMIB.MplsFecObjects()
        self.mplsfecobjects.parent = self
        self.mplsfectable = MPLSLDPSTDMIB.MplsFecTable()
        self.mplsfectable.parent = self
        self.mplsinsegmentldplsptable = MPLSLDPSTDMIB.MplsInSegmentLdpLspTable()
        self.mplsinsegmentldplsptable.parent = self
        self.mplsldpentityobjects = MPLSLDPSTDMIB.MplsLdpEntityObjects()
        self.mplsldpentityobjects.parent = self
        self.mplsldpentitytable = MPLSLDPSTDMIB.MplsLdpEntityTable()
        self.mplsldpentitytable.parent = self
        self.mplsldphelloadjacencytable = MPLSLDPSTDMIB.MplsLdpHelloAdjacencyTable()
        self.mplsldphelloadjacencytable.parent = self
        self.mplsldplspfectable = MPLSLDPSTDMIB.MplsLdpLspFecTable()
        self.mplsldplspfectable.parent = self
        self.mplsldplsrobjects = MPLSLDPSTDMIB.MplsLdpLsrObjects()
        self.mplsldplsrobjects.parent = self
        self.mplsldppeertable = MPLSLDPSTDMIB.MplsLdpPeerTable()
        self.mplsldppeertable.parent = self
        self.mplsldpsessionobjects = MPLSLDPSTDMIB.MplsLdpSessionObjects()
        self.mplsldpsessionobjects.parent = self
        self.mplsldpsessionpeeraddrtable = MPLSLDPSTDMIB.MplsLdpSessionPeerAddrTable()
        self.mplsldpsessionpeeraddrtable.parent = self
        self.mplsoutsegmentldplsptable = MPLSLDPSTDMIB.MplsOutSegmentLdpLspTable()
        self.mplsoutsegmentldplsptable.parent = self


    class MplsFecObjects(object):
        """
        
        
        .. attribute:: mplsfecindexnext
        
        	This object contains an appropriate value to be used for mplsFecIndex when creating entries in the mplsFecTable. The value 0 indicates that no unassigned entries are available
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplsfeclastchange
        
        	The value of sysUpTime at the time of the most recent addition/deletion of an entry to/from the mplsLdpFectTable or the most recent change in values to any objects in the mplsLdpFecTable.  If no such changes have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'mpls-ldp'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplsfecindexnext = None
            self.mplsfeclastchange = None

        @property
        def _common_path(self):

            return '/MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/MPLS-LDP-STD-MIB:mplsFecObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mplsfecindexnext is not None:
                return True

            if self.mplsfeclastchange is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
            return meta._meta_table['MPLSLDPSTDMIB.MplsFecObjects']['meta_info']


    class MplsFecTable(object):
        """
        This table represents the FEC
        (Forwarding Equivalence Class)
        Information associated with an LSP.
        
        .. attribute:: mplsfecentry
        
        	Each row represents a single FEC Element
        	**type**\: list of :py:class:`MplsFecEntry <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsFecTable.MplsFecEntry>`
        
        

        """

        _prefix = 'mpls-ldp'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplsfecentry = YList()
            self.mplsfecentry.parent = self
            self.mplsfecentry.name = 'mplsfecentry'


        class MplsFecEntry(object):
            """
            Each row represents a single FEC Element.
            
            .. attribute:: mplsfecindex
            
            	The index which uniquely identifies this entry
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplsfecaddr
            
            	The value of this object is interpreted based on the value of the 'mplsFecAddrType' object.  This address is then further interpretted as an being used with the address prefix, or as the host address.  This further interpretation is indicated by the 'mplsFecType' object. In other words, the FEC element is populated according to the Prefix FEC Element value encoding, or the Host Address FEC Element encoding
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: mplsfecaddrprefixlength
            
            	If the value of the 'mplsFecType' is 'hostAddress(2)' then this object is undefined.  If the value of 'mplsFecType' is 'prefix(1)' then the value of this object is the length in bits of the address prefix represented by 'mplsFecAddr', or zero.  If the value of this object is zero, this indicates that the prefix matches all addresses.  In this case the address prefix MUST also be zero (i.e., 'mplsFecAddr' should have the value of zero.)
            	**type**\: int
            
            	**range:** 0..2040
            
            .. attribute:: mplsfecaddrtype
            
            	The value of this object is the type of the Internet address.  The value of this object, decides how the value of the mplsFecAddr object is interpreted
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: mplsfecrowstatus
            
            	The status of this conceptual row.  If the value of this object is 'active(1)', then none of the writable objects of this entry can be modified, except to set this object to 'destroy(6)'.  NOTE\: if this row is being referenced by any entry in the mplsLdpLspFecTable, then a request to destroy this row, will result in an inconsistentValue error
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: mplsfecstoragetype
            
            	The storage type for this conceptual row. Conceptual rows having the value 'permanent(4)' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: mplsfectype
            
            	The type of the FEC.  If the value of this object is 'prefix(1)' then the FEC type described by this row is an address prefix.  If the value of this object is 'hostAddress(2)' then the FEC type described by this row is a host address
            	**type**\: :py:class:`MplsFecType_Enum <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsFecTable.MplsFecEntry.MplsFecType_Enum>`
            
            

            """

            _prefix = 'mpls-ldp'
            _revision = '2004-06-03'

            def __init__(self):
                self.parent = None
                self.mplsfecindex = None
                self.mplsfecaddr = None
                self.mplsfecaddrprefixlength = None
                self.mplsfecaddrtype = None
                self.mplsfecrowstatus = None
                self.mplsfecstoragetype = None
                self.mplsfectype = None

            class MplsFecType_Enum(Enum):
                """
                MplsFecType_Enum

                The type of the FEC.  If the value of this object
                is 'prefix(1)' then the FEC type described by this
                row is an address prefix.
                
                If the value of this object is 'hostAddress(2)' then
                the FEC type described by this row is a host address.

                """

                PREFIX = 1

                HOSTADDRESS = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
                    return meta._meta_table['MPLSLDPSTDMIB.MplsFecTable.MplsFecEntry.MplsFecType_Enum']


            @property
            def _common_path(self):
                if self.mplsfecindex is None:
                    raise YPYDataValidationError('Key property mplsfecindex is None')

                return '/MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/MPLS-LDP-STD-MIB:mplsFecTable/MPLS-LDP-STD-MIB:mplsFecEntry[MPLS-LDP-STD-MIB:mplsFecIndex = ' + str(self.mplsfecindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.mplsfecindex is not None:
                    return True

                if self.mplsfecaddr is not None:
                    return True

                if self.mplsfecaddrprefixlength is not None:
                    return True

                if self.mplsfecaddrtype is not None:
                    return True

                if self.mplsfecrowstatus is not None:
                    return True

                if self.mplsfecstoragetype is not None:
                    return True

                if self.mplsfectype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
                return meta._meta_table['MPLSLDPSTDMIB.MplsFecTable.MplsFecEntry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/MPLS-LDP-STD-MIB:mplsFecTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mplsfecentry is not None:
                for child_ref in self.mplsfecentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
            return meta._meta_table['MPLSLDPSTDMIB.MplsFecTable']['meta_info']


    class MplsInSegmentLdpLspTable(object):
        """
        A table of LDP LSP's which
        map to the mplsInSegmentTable in the
        MPLS\-LSR\-STD\-MIB module.
        
        .. attribute:: mplsinsegmentldplspentry
        
        	An entry in this table represents information on a single LDP LSP which is represented by a session's index triple (mplsLdpEntityLdpId, mplsLdpEntityIndex, mplsLdpPeerLdpId) AND the index for the mplsInSegmentTable (mplsInSegmentLdpLspLabelIndex) from the MPLS\-LSR\-STD\-MIB.  The information contained in a row is read\-only
        	**type**\: list of :py:class:`MplsInSegmentLdpLspEntry <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsInSegmentLdpLspTable.MplsInSegmentLdpLspEntry>`
        
        

        """

        _prefix = 'mpls-ldp'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplsinsegmentldplspentry = YList()
            self.mplsinsegmentldplspentry.parent = self
            self.mplsinsegmentldplspentry.name = 'mplsinsegmentldplspentry'


        class MplsInSegmentLdpLspEntry(object):
            """
            An entry in this table represents information
            on a single LDP LSP which is represented by
            a session's index triple (mplsLdpEntityLdpId,
            mplsLdpEntityIndex, mplsLdpPeerLdpId) AND the
            index for the mplsInSegmentTable
            (mplsInSegmentLdpLspLabelIndex) from the
            MPLS\-LSR\-STD\-MIB.
            
            The information contained in a row is read\-only.
            
            .. attribute:: mplsinsegmentldplspindex
            
            	This contains the same value as the mplsInSegmentIndex in the MPLS\-LSR\-STD\-MIB's mplsInSegmentTable
            	**type**\: str
            
            	**range:** 1..24
            
            .. attribute:: mplsldpentityindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplsldpentityldpid
            
            	
            	**type**\: str
            
            .. attribute:: mplsldppeerldpid
            
            	
            	**type**\: str
            
            .. attribute:: mplsinsegmentldplsplabeltype
            
            	The Layer 2 Label Type
            	**type**\: :py:class:`MplsLdpLabelType_Enum <ydk.models.mpls.MPLS_TC_STD_MIB.MplsLdpLabelType_Enum>`
            
            .. attribute:: mplsinsegmentldplsptype
            
            	The type of LSP connection
            	**type**\: :py:class:`MplsLspType_Enum <ydk.models.mpls.MPLS_TC_STD_MIB.MplsLspType_Enum>`
            
            

            """

            _prefix = 'mpls-ldp'
            _revision = '2004-06-03'

            def __init__(self):
                self.parent = None
                self.mplsinsegmentldplspindex = None
                self.mplsldpentityindex = None
                self.mplsldpentityldpid = None
                self.mplsldppeerldpid = None
                self.mplsinsegmentldplsplabeltype = None
                self.mplsinsegmentldplsptype = None

            @property
            def _common_path(self):
                if self.mplsinsegmentldplspindex is None:
                    raise YPYDataValidationError('Key property mplsinsegmentldplspindex is None')
                if self.mplsldpentityindex is None:
                    raise YPYDataValidationError('Key property mplsldpentityindex is None')
                if self.mplsldpentityldpid is None:
                    raise YPYDataValidationError('Key property mplsldpentityldpid is None')
                if self.mplsldppeerldpid is None:
                    raise YPYDataValidationError('Key property mplsldppeerldpid is None')

                return '/MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/MPLS-LDP-STD-MIB:mplsInSegmentLdpLspTable/MPLS-LDP-STD-MIB:mplsInSegmentLdpLspEntry[MPLS-LDP-STD-MIB:mplsInSegmentLdpLspIndex = ' + str(self.mplsinsegmentldplspindex) + '][MPLS-LDP-STD-MIB:mplsLdpEntityIndex = ' + str(self.mplsldpentityindex) + '][MPLS-LDP-STD-MIB:mplsLdpEntityLdpId = ' + str(self.mplsldpentityldpid) + '][MPLS-LDP-STD-MIB:mplsLdpPeerLdpId = ' + str(self.mplsldppeerldpid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.mplsinsegmentldplspindex is not None:
                    return True

                if self.mplsldpentityindex is not None:
                    return True

                if self.mplsldpentityldpid is not None:
                    return True

                if self.mplsldppeerldpid is not None:
                    return True

                if self.mplsinsegmentldplsplabeltype is not None:
                    return True

                if self.mplsinsegmentldplsptype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
                return meta._meta_table['MPLSLDPSTDMIB.MplsInSegmentLdpLspTable.MplsInSegmentLdpLspEntry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/MPLS-LDP-STD-MIB:mplsInSegmentLdpLspTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mplsinsegmentldplspentry is not None:
                for child_ref in self.mplsinsegmentldplspentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
            return meta._meta_table['MPLSLDPSTDMIB.MplsInSegmentLdpLspTable']['meta_info']


    class MplsLdpEntityObjects(object):
        """
        
        
        .. attribute:: mplsldpentityindexnext
        
        	This object contains an appropriate value to be used for mplsLdpEntityIndex when creating entries in the mplsLdpEntityTable. The value 0 indicates that no unassigned entries are available
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplsldpentitylastchange
        
        	The value of sysUpTime at the time of the most recent addition or deletion of an entry to/from the mplsLdpEntityTable/mplsLdpEntityStatsTable, or the most recent change in value of any objects in the mplsLdpEntityTable.   If no such changes have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'mpls-ldp'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplsldpentityindexnext = None
            self.mplsldpentitylastchange = None

        @property
        def _common_path(self):

            return '/MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/MPLS-LDP-STD-MIB:mplsLdpEntityObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mplsldpentityindexnext is not None:
                return True

            if self.mplsldpentitylastchange is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
            return meta._meta_table['MPLSLDPSTDMIB.MplsLdpEntityObjects']['meta_info']


    class MplsLdpEntityTable(object):
        """
        This table contains information about the
        MPLS Label Distribution Protocol Entities which
        exist on this Label Switching Router (LSR)
        or Label Edge Router (LER).
        
        .. attribute:: mplsldpentityentry
        
        	An entry in this table represents an LDP entity. An entry can be created by a network administrator or by an SNMP agent as instructed by LDP
        	**type**\: list of :py:class:`MplsLdpEntityEntry <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry>`
        
        

        """

        _prefix = 'mpls-ldp'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplsldpentityentry = YList()
            self.mplsldpentityentry.parent = self
            self.mplsldpentityentry.name = 'mplsldpentityentry'


        class MplsLdpEntityEntry(object):
            """
            An entry in this table represents an LDP entity.
            An entry can be created by a network administrator
            or by an SNMP agent as instructed by LDP.
            
            .. attribute:: mplsldpentityindex
            
            	This index is used as a secondary index to uniquely identify this row.  Before creating a row in this table, the 'mplsLdpEntityIndexNext' object should be retrieved. That value should be used for the value of this index when creating a row in this table.  NOTE\:  if a value of zero (0) is retrieved, that indicates that no rows can be created in this table at this time.  A secondary index (this object) is meaningful to some but not all, LDP implementations.  For example an LDP implementation which uses PPP would use this index to differentiate PPP sub\-links.  Another way to use this index is to give this the value of ifIndex.  However, this is dependant   on the implementation
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplsldpentityldpid
            
            	The LDP identifier
            	**type**\: str
            
            .. attribute:: mplsldpentityadminstatus
            
            	The administrative status of this LDP Entity. If this object is changed from 'enable' to 'disable' and this entity has already attempted to establish contact with a Peer, then all contact with that Peer is lost and all information from that Peer needs to be removed from the MIB. (This implies that the network management subsystem should clean up any related entry in the mplsLdpPeerTable.  This further implies that a 'tear\-down' for that session is issued and the session and all information related to that session cease to exist).  At this point the operator is able to change values which are related to this entity.  When the admin status is set back to 'enable', then this Entity will attempt to establish a new session with the Peer
            	**type**\: :py:class:`MplsLdpEntityAdminStatus_Enum <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry.MplsLdpEntityAdminStatus_Enum>`
            
            .. attribute:: mplsldpentitydiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this entity's counters suffered a discontinuity.  The relevant counters are the specific instances associated with this entity of any Counter32 object contained in the 'mplsLdpEntityStatsTable'.  If no such discontinuities have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentityhelloholdtimer
            
            	The 16\-bit integer value which is the proposed Hello hold timer for this LDP Entity. The Hello Hold time in seconds.   An LSR maintains a record of Hellos received from potential peers.  This object represents the Hold Time in the Common Hello Parameters TLV of the Hello Message.  A value of 0 is a default value and should be interpretted in conjunction with the mplsLdpEntityTargetPeer object.  If the value of this object is 0\: if the value of the mplsLdpEntityTargetPeer object is false(2), then this specifies that the Hold Time's actual default value is 15 seconds (i.e., the default Hold time for Link Hellos is 15 seconds).  Otherwise if the value of the mplsLdpEntityTargetPeer object is true(1), then this specifies that the Hold Time's actual default value is 45 seconds (i.e., the default Hold time for Targeted Hellos is 45 seconds).  A value of 65535 means infinite (i.e., wait forever).  All other values represent the amount of time in seconds to wait for a Hello Message.  Setting the hold time to a value smaller than 15 is not recommended, although not forbidden according to RFC3036
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: mplsldpentityhopcountlimit
            
            	If the value of this object is 0 (zero), then Loop Detection using Hop Counters is disabled.  If the value of this object is greater than 0 (zero) then Loop Detection using Hop Counters is enabled, and this object specifies this Entity's maximum allowable value for the Hop Count. Also, the value of the object mplsLdpLsrLoopDetectionCapable must be set to either 'hopCount(3)' or 'hopCountAndPathVector(5)' if this object has a value greater than 0 (zero), otherwise it is ignored
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: mplsldpentityinitsessionthreshold
            
            	When attempting to establish a session with a given Peer, the given LDP Entity should send out the SNMP notification, 'mplsLdpInitSessionThresholdExceeded', when the number of Session Initialization messages sent exceeds this threshold.  The notification is used to notify an operator when this Entity and its Peer are possibly engaged in an endless sequence of messages as each NAKs the other's   Initialization messages with Error Notification messages.  Setting this threshold which triggers the notification is one way to notify the operator.  The notification should be generated each time this threshold is exceeded and for every subsequent Initialization message which is NAK'd with an Error Notification message after this threshold is exceeded.  A value of 0 (zero) for this object indicates that the threshold is infinity, thus the SNMP notification will never be generated
            	**type**\: int
            
            	**range:** 0..100
            
            .. attribute:: mplsldpentitykeepaliveholdtimer
            
            	The 16\-bit integer value which is the proposed keep alive hold timer for this LDP Entity
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: mplsldpentitylabeldistmethod
            
            	For any given LDP session, the method of label distribution must be specified
            	**type**\: :py:class:`MplsLabelDistributionMethod_Enum <ydk.models.mpls.MPLS_TC_STD_MIB.MplsLabelDistributionMethod_Enum>`
            
            .. attribute:: mplsldpentitylabelretentionmode
            
            	The LDP Entity can be configured to use either conservative or liberal label retention mode.  If the value of this object is conservative(1) then advertized label mappings are retained only if they will be used to forward packets, i.e., if label came from a valid next hop.  If the value of this object is liberal(2) then all advertized label mappings are retained whether they are from a valid next hop or not
            	**type**\: :py:class:`MplsRetentionMode_Enum <ydk.models.mpls.MPLS_TC_STD_MIB.MplsRetentionMode_Enum>`
            
            .. attribute:: mplsldpentitylabeltype
            
            	Specifies the optional parameters for the LDP Initialization Message.  If the value is generic(1) then no optional parameters will be sent in the LDP Initialization message associated with this Entity.  If the value is atmParameters(2) then a row must be created in the mplsLdpEntityAtmTable, which corresponds to this entry.  If the value is frameRelayParameters(3) then a row must be created in the mplsLdpEntityFrameRelayTable, which corresponds to this entry
            	**type**\: :py:class:`MplsLdpLabelType_Enum <ydk.models.mpls.MPLS_TC_STD_MIB.MplsLdpLabelType_Enum>`
            
            .. attribute:: mplsldpentitymaxpdulength
            
            	The maximum PDU Length that is sent in the Common Session Parameters of an Initialization Message. According to the LDP Specification [RFC3036] a value of 255 or less specifies the default maximum length of 4096 octets, this is why the value of this object starts at 256.  The operator should explicitly choose the default value (i.e., 4096), or some other value.  The receiving LSR MUST calculate the maximum PDU length for the session by using the smaller of its and its peer's proposals for Max PDU Length
            	**type**\: int
            
            	**range:** 256..65535
            
            .. attribute:: mplsldpentityoperstatus
            
            	The operational status of this LDP Entity.  The value of unknown(1) indicates that the operational status cannot be determined at this time.  The value of unknown should be a transient condition before changing to enabled(2) or disabled(3)
            	**type**\: :py:class:`MplsLdpEntityOperStatus_Enum <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry.MplsLdpEntityOperStatus_Enum>`
            
            .. attribute:: mplsldpentitypathvectorlimit
            
            	If the value of this object is 0 (zero) then Loop Detection for Path Vectors is disabled.  Otherwise, if this object has a value greater than zero, then Loop Dection for Path Vectors is enabled, and the Path Vector Limit is this value. Also, the value of the object, 'mplsLdpLsrLoopDetectionCapable', must be set to either 'pathVector(4)' or 'hopCountAndPathVector(5)', if this object has a value greater than 0 (zero), otherwise it is ignored
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: mplsldpentityprotocolversion
            
            	The version number of the LDP protocol which will be used in the session initialization message.  Section 3.5.3 in the LDP Specification specifies that the version of the LDP protocol is negotiated during session establishment. The value of this object represents the value that is sent in the initialization message
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: mplsldpentityrowstatus
            
            	The status of this conceptual row.  All writable objects in this row may be modified at any time, however, as described in detail in the section entitled, 'Changing Values After Session Establishment', and again described in the DESCRIPTION clause of the mplsLdpEntityAdminStatus object, if a session has been initiated with a Peer, changing objects in this table will wreak havoc with the session and interrupt traffic.  To repeat again\: the recommended procedure is to set the mplsLdpEntityAdminStatus to down, thereby explicitly causing a session to be torn down. Then, change objects in this entry, then set the mplsLdpEntityAdminStatus to enable, which enables a new session to be initiated
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: mplsldpentitystatsbadldpidentifiererrors
            
            	This object counts the number of Bad LDP Identifier Fatal Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystatsbadmessagelengtherrors
            
            	This object counts the number of Bad Message Length Fatal Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystatsbadpdulengtherrors
            
            	This object counts the number of Bad PDU Length Fatal Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystatsbadtlvlengtherrors
            
            	This object counts the number of Bad TLV Length Fatal Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystatskeepalivetimerexperrors
            
            	This object counts the number of Session Keep Alive Timer Expired Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystatsmalformedtlvvalueerrors
            
            	This object counts the number of Malformed TLV Value Fatal Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystatssessionattempts
            
            	A count of the Session Initialization messages which were sent or received by this LDP Entity and were NAK'd.   In other words, this counter counts the number of session initializations that failed.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystatssessionrejectedaderrors
            
            	A count of the Session Rejected/Parameters Advertisement Mode Error Notification Messages sent or received by this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystatssessionrejectedlrerrors
            
            	A count of the Session Rejected/Parameters Label Range Notification Messages sent or received by this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystatssessionrejectedmaxpduerrors
            
            	A count of the Session Rejected/Parameters  Max Pdu Length Error Notification Messages sent or received by this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystatssessionrejectednohelloerrors
            
            	A count of the Session Rejected/No Hello Error Notification Messages sent or received by this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystatsshutdownreceivednotifications
            
            	This object counts the number of Shutdown Notifications received related to session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystatsshutdownsentnotifications
            
            	This object counts the number of Shutdown Notfications sent related to session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of   mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystoragetype
            
            	The storage type for this conceptual row. Conceptual rows having the value 'permanent(4)' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: mplsldpentitytargetpeer
            
            	If this LDP entity uses targeted peer then set this to true
            	**type**\: bool
            
            .. attribute:: mplsldpentitytargetpeeraddr
            
            	The value of the internetwork layer address used for the Extended Discovery.  The value of mplsLdpEntityTargetPeerAddrType specifies how this address is to be interpreted
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: mplsldpentitytargetpeeraddrtype
            
            	The type of the internetwork layer address used for the Extended Discovery.  This object indicates how the value of mplsLdpEntityTargetPeerAddr is to be interpreted
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: mplsldpentitytcpport
            
            	The TCP Port for LDP.  The default value is the well\-known value of this port
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: mplsldpentitytransportaddrkind
            
            	This specifies whether the loopback or interface address is to be used as the transport address in the transport address TLV of the hello message.  If the value is interface(1), then the IP address of the interface from which hello messages are sent is used as the transport address in the hello message.  Otherwise, if the value is loopback(2), then the IP address of the loopback interface is used as the transport address in the hello message
            	**type**\: :py:class:`MplsLdpEntityTransportAddrKind_Enum <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry.MplsLdpEntityTransportAddrKind_Enum>`
            
            .. attribute:: mplsldpentityudpdscport
            
            	The UDP Discovery Port for LDP.  The default value is the well\-known value for this port
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'mpls-ldp'
            _revision = '2004-06-03'

            def __init__(self):
                self.parent = None
                self.mplsldpentityindex = None
                self.mplsldpentityldpid = None
                self.mplsldpentityadminstatus = None
                self.mplsldpentitydiscontinuitytime = None
                self.mplsldpentityhelloholdtimer = None
                self.mplsldpentityhopcountlimit = None
                self.mplsldpentityinitsessionthreshold = None
                self.mplsldpentitykeepaliveholdtimer = None
                self.mplsldpentitylabeldistmethod = None
                self.mplsldpentitylabelretentionmode = None
                self.mplsldpentitylabeltype = None
                self.mplsldpentitymaxpdulength = None
                self.mplsldpentityoperstatus = None
                self.mplsldpentitypathvectorlimit = None
                self.mplsldpentityprotocolversion = None
                self.mplsldpentityrowstatus = None
                self.mplsldpentitystatsbadldpidentifiererrors = None
                self.mplsldpentitystatsbadmessagelengtherrors = None
                self.mplsldpentitystatsbadpdulengtherrors = None
                self.mplsldpentitystatsbadtlvlengtherrors = None
                self.mplsldpentitystatskeepalivetimerexperrors = None
                self.mplsldpentitystatsmalformedtlvvalueerrors = None
                self.mplsldpentitystatssessionattempts = None
                self.mplsldpentitystatssessionrejectedaderrors = None
                self.mplsldpentitystatssessionrejectedlrerrors = None
                self.mplsldpentitystatssessionrejectedmaxpduerrors = None
                self.mplsldpentitystatssessionrejectednohelloerrors = None
                self.mplsldpentitystatsshutdownreceivednotifications = None
                self.mplsldpentitystatsshutdownsentnotifications = None
                self.mplsldpentitystoragetype = None
                self.mplsldpentitytargetpeer = None
                self.mplsldpentitytargetpeeraddr = None
                self.mplsldpentitytargetpeeraddrtype = None
                self.mplsldpentitytcpport = None
                self.mplsldpentitytransportaddrkind = None
                self.mplsldpentityudpdscport = None

            class MplsLdpEntityAdminStatus_Enum(Enum):
                """
                MplsLdpEntityAdminStatus_Enum

                The administrative status of this LDP Entity.
                If this object is changed from 'enable' to 'disable'
                and this entity has already attempted to establish
                contact with a Peer, then all contact with that
                Peer is lost and all information from that Peer
                needs to be removed from the MIB. (This implies
                that the network management subsystem should clean
                up any related entry in the mplsLdpPeerTable.  This
                further implies that a 'tear\-down' for that session
                is issued and the session and all information related
                to that session cease to exist).
                
                At this point the operator is able to change values
                which are related to this entity.
                
                When the admin status is set back to 'enable', then
                this Entity will attempt to establish a new session
                with the Peer.

                """

                ENABLE = 1

                DISABLE = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
                    return meta._meta_table['MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry.MplsLdpEntityAdminStatus_Enum']


            class MplsLdpEntityOperStatus_Enum(Enum):
                """
                MplsLdpEntityOperStatus_Enum

                The operational status of this LDP Entity.
                
                The value of unknown(1) indicates that the
                operational status cannot be determined at
                this time.  The value of unknown should be
                a transient condition before changing
                to enabled(2) or disabled(3).

                """

                UNKNOWN = 1

                ENABLED = 2

                DISABLED = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
                    return meta._meta_table['MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry.MplsLdpEntityOperStatus_Enum']


            class MplsLdpEntityTransportAddrKind_Enum(Enum):
                """
                MplsLdpEntityTransportAddrKind_Enum

                This specifies whether the loopback or interface
                address is to be used as the transport address
                in the transport address TLV of the
                hello message.
                
                If the value is interface(1), then the IP
                address of the interface from which hello
                messages are sent is used as the transport
                address in the hello message.
                
                Otherwise, if the value is loopback(2), then the IP
                address of the loopback interface is used as the
                transport address in the hello message.

                """

                INTERFACE = 1

                LOOPBACK = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
                    return meta._meta_table['MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry.MplsLdpEntityTransportAddrKind_Enum']


            @property
            def _common_path(self):
                if self.mplsldpentityindex is None:
                    raise YPYDataValidationError('Key property mplsldpentityindex is None')
                if self.mplsldpentityldpid is None:
                    raise YPYDataValidationError('Key property mplsldpentityldpid is None')

                return '/MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/MPLS-LDP-STD-MIB:mplsLdpEntityTable/MPLS-LDP-STD-MIB:mplsLdpEntityEntry[MPLS-LDP-STD-MIB:mplsLdpEntityIndex = ' + str(self.mplsldpentityindex) + '][MPLS-LDP-STD-MIB:mplsLdpEntityLdpId = ' + str(self.mplsldpentityldpid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.mplsldpentityindex is not None:
                    return True

                if self.mplsldpentityldpid is not None:
                    return True

                if self.mplsldpentityadminstatus is not None:
                    return True

                if self.mplsldpentitydiscontinuitytime is not None:
                    return True

                if self.mplsldpentityhelloholdtimer is not None:
                    return True

                if self.mplsldpentityhopcountlimit is not None:
                    return True

                if self.mplsldpentityinitsessionthreshold is not None:
                    return True

                if self.mplsldpentitykeepaliveholdtimer is not None:
                    return True

                if self.mplsldpentitylabeldistmethod is not None:
                    return True

                if self.mplsldpentitylabelretentionmode is not None:
                    return True

                if self.mplsldpentitylabeltype is not None:
                    return True

                if self.mplsldpentitymaxpdulength is not None:
                    return True

                if self.mplsldpentityoperstatus is not None:
                    return True

                if self.mplsldpentitypathvectorlimit is not None:
                    return True

                if self.mplsldpentityprotocolversion is not None:
                    return True

                if self.mplsldpentityrowstatus is not None:
                    return True

                if self.mplsldpentitystatsbadldpidentifiererrors is not None:
                    return True

                if self.mplsldpentitystatsbadmessagelengtherrors is not None:
                    return True

                if self.mplsldpentitystatsbadpdulengtherrors is not None:
                    return True

                if self.mplsldpentitystatsbadtlvlengtherrors is not None:
                    return True

                if self.mplsldpentitystatskeepalivetimerexperrors is not None:
                    return True

                if self.mplsldpentitystatsmalformedtlvvalueerrors is not None:
                    return True

                if self.mplsldpentitystatssessionattempts is not None:
                    return True

                if self.mplsldpentitystatssessionrejectedaderrors is not None:
                    return True

                if self.mplsldpentitystatssessionrejectedlrerrors is not None:
                    return True

                if self.mplsldpentitystatssessionrejectedmaxpduerrors is not None:
                    return True

                if self.mplsldpentitystatssessionrejectednohelloerrors is not None:
                    return True

                if self.mplsldpentitystatsshutdownreceivednotifications is not None:
                    return True

                if self.mplsldpentitystatsshutdownsentnotifications is not None:
                    return True

                if self.mplsldpentitystoragetype is not None:
                    return True

                if self.mplsldpentitytargetpeer is not None:
                    return True

                if self.mplsldpentitytargetpeeraddr is not None:
                    return True

                if self.mplsldpentitytargetpeeraddrtype is not None:
                    return True

                if self.mplsldpentitytcpport is not None:
                    return True

                if self.mplsldpentitytransportaddrkind is not None:
                    return True

                if self.mplsldpentityudpdscport is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
                return meta._meta_table['MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/MPLS-LDP-STD-MIB:mplsLdpEntityTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mplsldpentityentry is not None:
                for child_ref in self.mplsldpentityentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
            return meta._meta_table['MPLSLDPSTDMIB.MplsLdpEntityTable']['meta_info']


    class MplsLdpHelloAdjacencyTable(object):
        """
        A table of Hello Adjacencies for Sessions.
        
        .. attribute:: mplsldphelloadjacencyentry
        
        	Each row represents a single LDP Hello Adjacency. An LDP Session can have one or more Hello Adjacencies
        	**type**\: list of :py:class:`MplsLdpHelloAdjacencyEntry <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpHelloAdjacencyTable.MplsLdpHelloAdjacencyEntry>`
        
        

        """

        _prefix = 'mpls-ldp'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplsldphelloadjacencyentry = YList()
            self.mplsldphelloadjacencyentry.parent = self
            self.mplsldphelloadjacencyentry.name = 'mplsldphelloadjacencyentry'


        class MplsLdpHelloAdjacencyEntry(object):
            """
            Each row represents a single LDP Hello Adjacency.
            An LDP Session can have one or more Hello
            Adjacencies.
            
            .. attribute:: mplsldpentityindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplsldpentityldpid
            
            	
            	**type**\: str
            
            .. attribute:: mplsldphelloadjacencyindex
            
            	An identifier for this specific adjacency
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplsldppeerldpid
            
            	
            	**type**\: str
            
            .. attribute:: mplsldphelloadjacencyholdtime
            
            	The Hello hold time which is negotiated between the Entity and the Peer.  The entity associated with this Hello Adjacency issues a proposed Hello Hold Time value in the mplsLdpEntityHelloHoldTimer object.  The peer also proposes a value and this object represents the negotiated value.  A value of 0 means the default, which is 15 seconds for Link Hellos and 45 seconds for Targeted Hellos. A value of 65535 indicates an infinite hold time
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: mplsldphelloadjacencyholdtimerem
            
            	If the value of this object is 65535, this means that the hold time is infinite (i.e., wait forever).  Otherwise, the time remaining for this Hello Adjacency to receive its next Hello Message.  This interval will change when the 'next' Hello Message which corresponds to this Hello Adjacency is received unless it is infinite
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplsldphelloadjacencytype
            
            	This adjacency is the result of a 'link' hello if the value of this object is link(1).   Otherwise, it is a result of a 'targeted' hello, targeted(2)
            	**type**\: :py:class:`MplsLdpHelloAdjacencyType_Enum <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpHelloAdjacencyTable.MplsLdpHelloAdjacencyEntry.MplsLdpHelloAdjacencyType_Enum>`
            
            

            """

            _prefix = 'mpls-ldp'
            _revision = '2004-06-03'

            def __init__(self):
                self.parent = None
                self.mplsldpentityindex = None
                self.mplsldpentityldpid = None
                self.mplsldphelloadjacencyindex = None
                self.mplsldppeerldpid = None
                self.mplsldphelloadjacencyholdtime = None
                self.mplsldphelloadjacencyholdtimerem = None
                self.mplsldphelloadjacencytype = None

            class MplsLdpHelloAdjacencyType_Enum(Enum):
                """
                MplsLdpHelloAdjacencyType_Enum

                This adjacency is the result of a 'link'
                hello if the value of this object is link(1).
                
                
                Otherwise, it is a result of a 'targeted'
                hello, targeted(2).

                """

                LINK = 1

                TARGETED = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
                    return meta._meta_table['MPLSLDPSTDMIB.MplsLdpHelloAdjacencyTable.MplsLdpHelloAdjacencyEntry.MplsLdpHelloAdjacencyType_Enum']


            @property
            def _common_path(self):
                if self.mplsldpentityindex is None:
                    raise YPYDataValidationError('Key property mplsldpentityindex is None')
                if self.mplsldpentityldpid is None:
                    raise YPYDataValidationError('Key property mplsldpentityldpid is None')
                if self.mplsldphelloadjacencyindex is None:
                    raise YPYDataValidationError('Key property mplsldphelloadjacencyindex is None')
                if self.mplsldppeerldpid is None:
                    raise YPYDataValidationError('Key property mplsldppeerldpid is None')

                return '/MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/MPLS-LDP-STD-MIB:mplsLdpHelloAdjacencyTable/MPLS-LDP-STD-MIB:mplsLdpHelloAdjacencyEntry[MPLS-LDP-STD-MIB:mplsLdpEntityIndex = ' + str(self.mplsldpentityindex) + '][MPLS-LDP-STD-MIB:mplsLdpEntityLdpId = ' + str(self.mplsldpentityldpid) + '][MPLS-LDP-STD-MIB:mplsLdpHelloAdjacencyIndex = ' + str(self.mplsldphelloadjacencyindex) + '][MPLS-LDP-STD-MIB:mplsLdpPeerLdpId = ' + str(self.mplsldppeerldpid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.mplsldpentityindex is not None:
                    return True

                if self.mplsldpentityldpid is not None:
                    return True

                if self.mplsldphelloadjacencyindex is not None:
                    return True

                if self.mplsldppeerldpid is not None:
                    return True

                if self.mplsldphelloadjacencyholdtime is not None:
                    return True

                if self.mplsldphelloadjacencyholdtimerem is not None:
                    return True

                if self.mplsldphelloadjacencytype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
                return meta._meta_table['MPLSLDPSTDMIB.MplsLdpHelloAdjacencyTable.MplsLdpHelloAdjacencyEntry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/MPLS-LDP-STD-MIB:mplsLdpHelloAdjacencyTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mplsldphelloadjacencyentry is not None:
                for child_ref in self.mplsldphelloadjacencyentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
            return meta._meta_table['MPLSLDPSTDMIB.MplsLdpHelloAdjacencyTable']['meta_info']


    class MplsLdpLspFecTable(object):
        """
        A table which shows the relationship between
        LDP LSPs and FECs.  Each row represents
        a single LDP LSP to FEC association.
        
        .. attribute:: mplsldplspfecentry
        
        	An entry represents a LDP LSP to FEC association
        	**type**\: list of :py:class:`MplsLdpLspFecEntry <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpLspFecTable.MplsLdpLspFecEntry>`
        
        

        """

        _prefix = 'mpls-ldp'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplsldplspfecentry = YList()
            self.mplsldplspfecentry.parent = self
            self.mplsldplspfecentry.name = 'mplsldplspfecentry'


        class MplsLdpLspFecEntry(object):
            """
            An entry represents a LDP LSP
            to FEC association.
            
            .. attribute:: mplsldpentityindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplsldpentityldpid
            
            	
            	**type**\: str
            
            .. attribute:: mplsldplspfecindex
            
            	This index identifies the FEC entry in the mplsFecTable associated with this session. In other words, the value of this index is the same as the value of the mplsFecIndex that denotes the FEC associated with this Session
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplsldplspfecsegment
            
            	If the value is inSegment(1), then this indicates that the following index, mplsLdpLspFecSegmentIndex, contains the same value as the mplsInSegmentLdpLspIndex.  Otherwise, if the value of this object is   outSegment(2),  then this indicates that following index, mplsLdpLspFecSegmentIndex, contains the same value as the mplsOutSegmentLdpLspIndex
            	**type**\: :py:class:`MplsLdpLspFecSegment_Enum <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpLspFecTable.MplsLdpLspFecEntry.MplsLdpLspFecSegment_Enum>`
            
            .. attribute:: mplsldplspfecsegmentindex
            
            	This index is interpretted by using the value of the mplsLdpLspFecSegment.  If the mplsLdpLspFecSegment is inSegment(1), then this index has the same value as mplsInSegmentLdpLspIndex.  If the mplsLdpLspFecSegment is outSegment(2), then this index has the same value as mplsOutSegmentLdpLspIndex
            	**type**\: str
            
            	**range:** 1..24
            
            .. attribute:: mplsldppeerldpid
            
            	
            	**type**\: str
            
            .. attribute:: mplsldplspfecrowstatus
            
            	The status of this conceptual row.  If the value of this object is 'active(1)', then none of the writable objects of this entry can be modified.  The Agent should delete this row when the session ceases to exist.  If an operator wants to associate the session with a different FEC, the recommended procedure is (as described in detail in the section entitled, 'Changing Values After Session Establishment', and again described in the DESCRIPTION clause of the mplsLdpEntityAdminStatus object) is to set the mplsLdpEntityAdminStatus to down, thereby explicitly causing a session to be torn down. This will also cause this entry to be deleted.  Then, set the mplsLdpEntityAdminStatus to enable which enables a new session to be initiated. Once the session is initiated, an entry may be added to this table to associate the new session with a FEC
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: mplsldplspfecstoragetype
            
            	The storage type for this conceptual row. Conceptual rows having the value 'permanent(4)' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'mpls-ldp'
            _revision = '2004-06-03'

            def __init__(self):
                self.parent = None
                self.mplsldpentityindex = None
                self.mplsldpentityldpid = None
                self.mplsldplspfecindex = None
                self.mplsldplspfecsegment = None
                self.mplsldplspfecsegmentindex = None
                self.mplsldppeerldpid = None
                self.mplsldplspfecrowstatus = None
                self.mplsldplspfecstoragetype = None

            class MplsLdpLspFecSegment_Enum(Enum):
                """
                MplsLdpLspFecSegment_Enum

                If the value is inSegment(1), then this
                indicates that the following index,
                mplsLdpLspFecSegmentIndex, contains the same
                value as the mplsInSegmentLdpLspIndex.
                
                Otherwise, if the value of this object is
                
                
                outSegment(2),  then this
                indicates that following index,
                mplsLdpLspFecSegmentIndex, contains the same
                value as the mplsOutSegmentLdpLspIndex.

                """

                INSEGMENT = 1

                OUTSEGMENT = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
                    return meta._meta_table['MPLSLDPSTDMIB.MplsLdpLspFecTable.MplsLdpLspFecEntry.MplsLdpLspFecSegment_Enum']


            @property
            def _common_path(self):
                if self.mplsldpentityindex is None:
                    raise YPYDataValidationError('Key property mplsldpentityindex is None')
                if self.mplsldpentityldpid is None:
                    raise YPYDataValidationError('Key property mplsldpentityldpid is None')
                if self.mplsldplspfecindex is None:
                    raise YPYDataValidationError('Key property mplsldplspfecindex is None')
                if self.mplsldplspfecsegment is None:
                    raise YPYDataValidationError('Key property mplsldplspfecsegment is None')
                if self.mplsldplspfecsegmentindex is None:
                    raise YPYDataValidationError('Key property mplsldplspfecsegmentindex is None')
                if self.mplsldppeerldpid is None:
                    raise YPYDataValidationError('Key property mplsldppeerldpid is None')

                return '/MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/MPLS-LDP-STD-MIB:mplsLdpLspFecTable/MPLS-LDP-STD-MIB:mplsLdpLspFecEntry[MPLS-LDP-STD-MIB:mplsLdpEntityIndex = ' + str(self.mplsldpentityindex) + '][MPLS-LDP-STD-MIB:mplsLdpEntityLdpId = ' + str(self.mplsldpentityldpid) + '][MPLS-LDP-STD-MIB:mplsLdpLspFecIndex = ' + str(self.mplsldplspfecindex) + '][MPLS-LDP-STD-MIB:mplsLdpLspFecSegment = ' + str(self.mplsldplspfecsegment) + '][MPLS-LDP-STD-MIB:mplsLdpLspFecSegmentIndex = ' + str(self.mplsldplspfecsegmentindex) + '][MPLS-LDP-STD-MIB:mplsLdpPeerLdpId = ' + str(self.mplsldppeerldpid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.mplsldpentityindex is not None:
                    return True

                if self.mplsldpentityldpid is not None:
                    return True

                if self.mplsldplspfecindex is not None:
                    return True

                if self.mplsldplspfecsegment is not None:
                    return True

                if self.mplsldplspfecsegmentindex is not None:
                    return True

                if self.mplsldppeerldpid is not None:
                    return True

                if self.mplsldplspfecrowstatus is not None:
                    return True

                if self.mplsldplspfecstoragetype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
                return meta._meta_table['MPLSLDPSTDMIB.MplsLdpLspFecTable.MplsLdpLspFecEntry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/MPLS-LDP-STD-MIB:mplsLdpLspFecTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mplsldplspfecentry is not None:
                for child_ref in self.mplsldplspfecentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
            return meta._meta_table['MPLSLDPSTDMIB.MplsLdpLspFecTable']['meta_info']


    class MplsLdpLsrObjects(object):
        """
        
        
        .. attribute:: mplsldplsrid
        
        	The Label Switching Router's Identifier
        	**type**\: str
        
        	**range:** 4
        
        .. attribute:: mplsldplsrloopdetectioncapable
        
        	A indication of whether this Label Switching Router supports loop detection.  none(1) \-\- Loop Detection is not supported            on this LSR.  other(2) \-\- Loop Detection is supported but             by a method other than those             listed below.  hopCount(3) \-\- Loop Detection is supported by                Hop Count only.  pathVector(4) \-\- Loop Detection is supported by                  Path Vector only.  hopCountAndPathVector(5) \-\- Loop Detection is                      supported by both Hop Count                      And Path Vector.  Since Loop Detection is determined during Session Initialization, an individual session may not be running with loop detection.  This object simply gives an indication of whether or not the LSR has the ability to support Loop Detection and which types
        	**type**\: :py:class:`MplsLdpLsrLoopDetectionCapable_Enum <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpLsrObjects.MplsLdpLsrLoopDetectionCapable_Enum>`
        
        

        """

        _prefix = 'mpls-ldp'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplsldplsrid = None
            self.mplsldplsrloopdetectioncapable = None

        class MplsLdpLsrLoopDetectionCapable_Enum(Enum):
            """
            MplsLdpLsrLoopDetectionCapable_Enum

            A indication of whether this
            Label Switching Router supports
            loop detection.
            
            none(1) \-\- Loop Detection is not supported
                       on this LSR.
            
            other(2) \-\- Loop Detection is supported but
                        by a method other than those
                        listed below.
            
            hopCount(3) \-\- Loop Detection is supported by
                           Hop Count only.
            
            pathVector(4) \-\- Loop Detection is supported by
                             Path Vector only.
            
            hopCountAndPathVector(5) \-\- Loop Detection is
                                 supported by both Hop Count
                                 And Path Vector.
            
            Since Loop Detection is determined during
            Session Initialization, an individual session
            may not be running with loop detection.  This
            object simply gives an indication of whether or not the
            LSR has the ability to support Loop Detection and
            which types.

            """

            NONE = 1

            OTHER = 2

            HOPCOUNT = 3

            PATHVECTOR = 4

            HOPCOUNTANDPATHVECTOR = 5


            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
                return meta._meta_table['MPLSLDPSTDMIB.MplsLdpLsrObjects.MplsLdpLsrLoopDetectionCapable_Enum']


        @property
        def _common_path(self):

            return '/MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/MPLS-LDP-STD-MIB:mplsLdpLsrObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mplsldplsrid is not None:
                return True

            if self.mplsldplsrloopdetectioncapable is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
            return meta._meta_table['MPLSLDPSTDMIB.MplsLdpLsrObjects']['meta_info']


    class MplsLdpPeerTable(object):
        """
        Information about LDP peers known by Entities in
        the mplsLdpEntityTable.  The information in this table
        is based on information from the Entity\-Peer interaction
        during session initialization but is not appropriate
        for the mplsLdpSessionTable, because objects in this
        table may or may not be used in session establishment.
        
        .. attribute:: mplsldppeerentry
        
        	Information about a single Peer which is related to a Session.  This table is augmented by the mplsLdpSessionTable
        	**type**\: list of :py:class:`MplsLdpPeerEntry <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpPeerTable.MplsLdpPeerEntry>`
        
        

        """

        _prefix = 'mpls-ldp'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplsldppeerentry = YList()
            self.mplsldppeerentry.parent = self
            self.mplsldppeerentry.name = 'mplsldppeerentry'


        class MplsLdpPeerEntry(object):
            """
            Information about a single Peer which is related
            to a Session.  This table is augmented by
            the mplsLdpSessionTable.
            
            .. attribute:: mplsldpentityindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplsldpentityldpid
            
            	
            	**type**\: str
            
            .. attribute:: mplsldppeerldpid
            
            	The LDP identifier of this LDP Peer
            	**type**\: str
            
            .. attribute:: mplsldppeerlabeldistmethod
            
            	For any given LDP session, the method of label distribution must be specified
            	**type**\: :py:class:`MplsLabelDistributionMethod_Enum <ydk.models.mpls.MPLS_TC_STD_MIB.MplsLabelDistributionMethod_Enum>`
            
            .. attribute:: mplsldppeerpathvectorlimit
            
            	If the value of this object is 0 (zero) then Loop Dection for Path Vectors for this Peer is disabled.  Otherwise, if this object has a value greater than zero, then Loop Dection for Path  Vectors for this Peer is enabled and the Path Vector Limit is this value
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: mplsldppeertransportaddr
            
            	The Internet address advertised by the peer in the Hello Message or the Hello source address.  The type of this address is specified by the value of the mplsLdpPeerTransportAddrType object
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: mplsldppeertransportaddrtype
            
            	The type of the Internet address for the mplsLdpPeerTransportAddr object.  The LDP specification describes this as being either an IPv4 Transport Address or IPv6 Transport   Address which is used in opening the LDP session's TCP connection, or if the optional TLV is not present, then this is the IPv4/IPv6 source address for the UPD packet carrying the Hellos.  This object specifies how the value of the mplsLdpPeerTransportAddr object should be interpreted
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: mplsldpsessiondiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this session's counters suffered a discontinuity.  The relevant counters are the specific instances associated with this session of any Counter32 object contained in the mplsLdpSessionStatsTable.  The initial value of this object is the value of sysUpTime when the entry was created in this table.  Also, a command generator can distinguish when a session between a given Entity and Peer goes away and a new session is established.  This value would change and thus indicate to the command generator that this is a different session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpsessionkeepaliveholdtimerem
            
            	The keep alive hold time remaining for this session
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplsldpsessionkeepalivetime
            
            	The negotiated KeepAlive Time which represents the amount of seconds between keep alive messages.  The mplsLdpEntityKeepAliveHoldTimer related to this Session is the value that was proposed as the KeepAlive Time for this session.  This value is negotiated during session initialization between the entity's proposed value (i.e., the value configured in mplsLdpEntityKeepAliveHoldTimer) and the peer's proposed KeepAlive Hold Timer value. This value is the smaller of the two proposed values
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: mplsldpsessionmaxpdulength
            
            	The value of maximum allowable length for LDP PDUs for this session.  This value may have been negotiated during the Session Initialization.  This object is related to the mplsLdpEntityMaxPduLength object.  The mplsLdpEntityMaxPduLength object specifies the requested LDP PDU length, and this object reflects the negotiated LDP PDU length between the Entity and the Peer
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: mplsldpsessionprotocolversion
            
            	The version of the LDP Protocol which this session is using.  This is the version of   the LDP protocol which has been negotiated during session initialization
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: mplsldpsessionrole
            
            	During session establishment the LSR/LER takes either the active role or the passive role based on address comparisons.  This object indicates whether this LSR/LER was behaving in an active role or passive role during this session's establishment.  The value of unknown(1), indicates that the role is not able to be determined at the present time
            	**type**\: :py:class:`MplsLdpSessionRole_Enum <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpPeerTable.MplsLdpPeerEntry.MplsLdpSessionRole_Enum>`
            
            .. attribute:: mplsldpsessionstate
            
            	The current state of the session, all of the states 1 to 5 are based on the state machine for session negotiation behavior
            	**type**\: :py:class:`MplsLdpSessionState_Enum <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpPeerTable.MplsLdpPeerEntry.MplsLdpSessionState_Enum>`
            
            .. attribute:: mplsldpsessionstatelastchange
            
            	The value of sysUpTime at the time this Session entered its current state as denoted by the mplsLdpSessionState object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpsessionstatsunknownmestypeerrors
            
            	This object counts the number of Unknown Message Type Errors detected by this LSR/LER during this session.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpSessionDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpsessionstatsunknowntlverrors
            
            	This object counts the number of Unknown TLV Errors detected by this LSR/LER during this session.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpSessionDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'mpls-ldp'
            _revision = '2004-06-03'

            def __init__(self):
                self.parent = None
                self.mplsldpentityindex = None
                self.mplsldpentityldpid = None
                self.mplsldppeerldpid = None
                self.mplsldppeerlabeldistmethod = None
                self.mplsldppeerpathvectorlimit = None
                self.mplsldppeertransportaddr = None
                self.mplsldppeertransportaddrtype = None
                self.mplsldpsessiondiscontinuitytime = None
                self.mplsldpsessionkeepaliveholdtimerem = None
                self.mplsldpsessionkeepalivetime = None
                self.mplsldpsessionmaxpdulength = None
                self.mplsldpsessionprotocolversion = None
                self.mplsldpsessionrole = None
                self.mplsldpsessionstate = None
                self.mplsldpsessionstatelastchange = None
                self.mplsldpsessionstatsunknownmestypeerrors = None
                self.mplsldpsessionstatsunknowntlverrors = None

            class MplsLdpSessionRole_Enum(Enum):
                """
                MplsLdpSessionRole_Enum

                During session establishment the LSR/LER takes either
                the active role or the passive role based on address
                comparisons.  This object indicates whether this LSR/LER
                was behaving in an active role or passive role during
                this session's establishment.
                
                The value of unknown(1), indicates that the role is not
                able to be determined at the present time.

                """

                UNKNOWN = 1

                ACTIVE = 2

                PASSIVE = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
                    return meta._meta_table['MPLSLDPSTDMIB.MplsLdpPeerTable.MplsLdpPeerEntry.MplsLdpSessionRole_Enum']


            class MplsLdpSessionState_Enum(Enum):
                """
                MplsLdpSessionState_Enum

                The current state of the session, all of the
                states 1 to 5 are based on the state machine
                for session negotiation behavior.

                """

                NONEXISTENT = 1

                INITIALIZED = 2

                OPENREC = 3

                OPENSENT = 4

                OPERATIONAL = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
                    return meta._meta_table['MPLSLDPSTDMIB.MplsLdpPeerTable.MplsLdpPeerEntry.MplsLdpSessionState_Enum']


            @property
            def _common_path(self):
                if self.mplsldpentityindex is None:
                    raise YPYDataValidationError('Key property mplsldpentityindex is None')
                if self.mplsldpentityldpid is None:
                    raise YPYDataValidationError('Key property mplsldpentityldpid is None')
                if self.mplsldppeerldpid is None:
                    raise YPYDataValidationError('Key property mplsldppeerldpid is None')

                return '/MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/MPLS-LDP-STD-MIB:mplsLdpPeerTable/MPLS-LDP-STD-MIB:mplsLdpPeerEntry[MPLS-LDP-STD-MIB:mplsLdpEntityIndex = ' + str(self.mplsldpentityindex) + '][MPLS-LDP-STD-MIB:mplsLdpEntityLdpId = ' + str(self.mplsldpentityldpid) + '][MPLS-LDP-STD-MIB:mplsLdpPeerLdpId = ' + str(self.mplsldppeerldpid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.mplsldpentityindex is not None:
                    return True

                if self.mplsldpentityldpid is not None:
                    return True

                if self.mplsldppeerldpid is not None:
                    return True

                if self.mplsldppeerlabeldistmethod is not None:
                    return True

                if self.mplsldppeerpathvectorlimit is not None:
                    return True

                if self.mplsldppeertransportaddr is not None:
                    return True

                if self.mplsldppeertransportaddrtype is not None:
                    return True

                if self.mplsldpsessiondiscontinuitytime is not None:
                    return True

                if self.mplsldpsessionkeepaliveholdtimerem is not None:
                    return True

                if self.mplsldpsessionkeepalivetime is not None:
                    return True

                if self.mplsldpsessionmaxpdulength is not None:
                    return True

                if self.mplsldpsessionprotocolversion is not None:
                    return True

                if self.mplsldpsessionrole is not None:
                    return True

                if self.mplsldpsessionstate is not None:
                    return True

                if self.mplsldpsessionstatelastchange is not None:
                    return True

                if self.mplsldpsessionstatsunknownmestypeerrors is not None:
                    return True

                if self.mplsldpsessionstatsunknowntlverrors is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
                return meta._meta_table['MPLSLDPSTDMIB.MplsLdpPeerTable.MplsLdpPeerEntry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/MPLS-LDP-STD-MIB:mplsLdpPeerTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mplsldppeerentry is not None:
                for child_ref in self.mplsldppeerentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
            return meta._meta_table['MPLSLDPSTDMIB.MplsLdpPeerTable']['meta_info']


    class MplsLdpSessionObjects(object):
        """
        
        
        .. attribute:: mplsldplspfeclastchange
        
        	The value of sysUpTime at the time of the most recent addition/deletion of an entry to/from the mplsLdpLspFecTable or the most recent change in values to any objects in the mplsLdpLspFecTable.  If no such changes have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplsldppeerlastchange
        
        	The value of sysUpTime at the time of the most recent addition or deletion to/from the mplsLdpPeerTable/mplsLdpSessionTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'mpls-ldp'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplsldplspfeclastchange = None
            self.mplsldppeerlastchange = None

        @property
        def _common_path(self):

            return '/MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/MPLS-LDP-STD-MIB:mplsLdpSessionObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mplsldplspfeclastchange is not None:
                return True

            if self.mplsldppeerlastchange is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
            return meta._meta_table['MPLSLDPSTDMIB.MplsLdpSessionObjects']['meta_info']


    class MplsLdpSessionPeerAddrTable(object):
        """
        This table 'extends' the mplsLdpSessionTable.
        This table is used to store Label Address Information
        from Label Address Messages received by this LSR from
        Peers.  This table is read\-only and should be updated
        
        
        when Label Withdraw Address Messages are received, i.e.,
        Rows should be deleted as appropriate.
        
        NOTE\:  since more than one address may be contained
        in a Label Address Message, this table 'sparse augments',
        the mplsLdpSessionTable's information.
        
        .. attribute:: mplsldpsessionpeeraddrentry
        
        	An entry in this table represents information on a session's single next hop address which was advertised in an Address Message from the LDP peer. The information contained in a row is read\-only
        	**type**\: list of :py:class:`MplsLdpSessionPeerAddrEntry <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpSessionPeerAddrTable.MplsLdpSessionPeerAddrEntry>`
        
        

        """

        _prefix = 'mpls-ldp'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplsldpsessionpeeraddrentry = YList()
            self.mplsldpsessionpeeraddrentry.parent = self
            self.mplsldpsessionpeeraddrentry.name = 'mplsldpsessionpeeraddrentry'


        class MplsLdpSessionPeerAddrEntry(object):
            """
            An entry in this table represents information on
            a session's single next hop address which was
            advertised in an Address Message from the LDP peer.
            The information contained in a row is read\-only.
            
            .. attribute:: mplsldpentityindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplsldpentityldpid
            
            	
            	**type**\: str
            
            .. attribute:: mplsldppeerldpid
            
            	
            	**type**\: str
            
            .. attribute:: mplsldpsessionpeeraddrindex
            
            	An index which uniquely identifies this entry within a given session
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplsldpsessionpeernexthopaddr
            
            	The next hop address.  The type of this address is specified by the value of the mplsLdpSessionPeerNextHopAddrType
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: mplsldpsessionpeernexthopaddrtype
            
            	The internetwork layer address type of this Next Hop Address as specified in the Label Address Message associated with this Session. The value of this object indicates how to interpret the value of   mplsLdpSessionPeerNextHopAddr
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            

            """

            _prefix = 'mpls-ldp'
            _revision = '2004-06-03'

            def __init__(self):
                self.parent = None
                self.mplsldpentityindex = None
                self.mplsldpentityldpid = None
                self.mplsldppeerldpid = None
                self.mplsldpsessionpeeraddrindex = None
                self.mplsldpsessionpeernexthopaddr = None
                self.mplsldpsessionpeernexthopaddrtype = None

            @property
            def _common_path(self):
                if self.mplsldpentityindex is None:
                    raise YPYDataValidationError('Key property mplsldpentityindex is None')
                if self.mplsldpentityldpid is None:
                    raise YPYDataValidationError('Key property mplsldpentityldpid is None')
                if self.mplsldppeerldpid is None:
                    raise YPYDataValidationError('Key property mplsldppeerldpid is None')
                if self.mplsldpsessionpeeraddrindex is None:
                    raise YPYDataValidationError('Key property mplsldpsessionpeeraddrindex is None')

                return '/MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/MPLS-LDP-STD-MIB:mplsLdpSessionPeerAddrTable/MPLS-LDP-STD-MIB:mplsLdpSessionPeerAddrEntry[MPLS-LDP-STD-MIB:mplsLdpEntityIndex = ' + str(self.mplsldpentityindex) + '][MPLS-LDP-STD-MIB:mplsLdpEntityLdpId = ' + str(self.mplsldpentityldpid) + '][MPLS-LDP-STD-MIB:mplsLdpPeerLdpId = ' + str(self.mplsldppeerldpid) + '][MPLS-LDP-STD-MIB:mplsLdpSessionPeerAddrIndex = ' + str(self.mplsldpsessionpeeraddrindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.mplsldpentityindex is not None:
                    return True

                if self.mplsldpentityldpid is not None:
                    return True

                if self.mplsldppeerldpid is not None:
                    return True

                if self.mplsldpsessionpeeraddrindex is not None:
                    return True

                if self.mplsldpsessionpeernexthopaddr is not None:
                    return True

                if self.mplsldpsessionpeernexthopaddrtype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
                return meta._meta_table['MPLSLDPSTDMIB.MplsLdpSessionPeerAddrTable.MplsLdpSessionPeerAddrEntry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/MPLS-LDP-STD-MIB:mplsLdpSessionPeerAddrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mplsldpsessionpeeraddrentry is not None:
                for child_ref in self.mplsldpsessionpeeraddrentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
            return meta._meta_table['MPLSLDPSTDMIB.MplsLdpSessionPeerAddrTable']['meta_info']


    class MplsOutSegmentLdpLspTable(object):
        """
        A table of LDP LSP's which
        map to the mplsOutSegmentTable in the
        MPLS\-LSR\-STD\-MIB.
        
        .. attribute:: mplsoutsegmentldplspentry
        
        	An entry in this table represents information on a single LDP LSP which is represented by a session's index triple (mplsLdpEntityLdpId, mplsLdpEntityIndex, mplsLdpPeerLdpId) AND the index (mplsOutSegmentLdpLspIndex) for the mplsOutSegmentTable.  The information contained in a row is read\-only
        	**type**\: list of :py:class:`MplsOutSegmentLdpLspEntry <ydk.models.mpls.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsOutSegmentLdpLspTable.MplsOutSegmentLdpLspEntry>`
        
        

        """

        _prefix = 'mpls-ldp'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplsoutsegmentldplspentry = YList()
            self.mplsoutsegmentldplspentry.parent = self
            self.mplsoutsegmentldplspentry.name = 'mplsoutsegmentldplspentry'


        class MplsOutSegmentLdpLspEntry(object):
            """
            An entry in this table represents information
            on a single LDP LSP which is represented by
            a session's index triple (mplsLdpEntityLdpId,
            mplsLdpEntityIndex, mplsLdpPeerLdpId) AND the
            index (mplsOutSegmentLdpLspIndex)
            for the mplsOutSegmentTable.
            
            The information contained in a row is read\-only.
            
            .. attribute:: mplsldpentityindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplsldpentityldpid
            
            	
            	**type**\: str
            
            .. attribute:: mplsldppeerldpid
            
            	
            	**type**\: str
            
            .. attribute:: mplsoutsegmentldplspindex
            
            	This contains the same value as the mplsOutSegmentIndex in the MPLS\-LSR\-STD\-MIB's mplsOutSegmentTable
            	**type**\: str
            
            	**range:** 1..24
            
            .. attribute:: mplsoutsegmentldplsplabeltype
            
            	The Layer 2 Label Type
            	**type**\: :py:class:`MplsLdpLabelType_Enum <ydk.models.mpls.MPLS_TC_STD_MIB.MplsLdpLabelType_Enum>`
            
            .. attribute:: mplsoutsegmentldplsptype
            
            	The type of LSP connection
            	**type**\: :py:class:`MplsLspType_Enum <ydk.models.mpls.MPLS_TC_STD_MIB.MplsLspType_Enum>`
            
            

            """

            _prefix = 'mpls-ldp'
            _revision = '2004-06-03'

            def __init__(self):
                self.parent = None
                self.mplsldpentityindex = None
                self.mplsldpentityldpid = None
                self.mplsldppeerldpid = None
                self.mplsoutsegmentldplspindex = None
                self.mplsoutsegmentldplsplabeltype = None
                self.mplsoutsegmentldplsptype = None

            @property
            def _common_path(self):
                if self.mplsldpentityindex is None:
                    raise YPYDataValidationError('Key property mplsldpentityindex is None')
                if self.mplsldpentityldpid is None:
                    raise YPYDataValidationError('Key property mplsldpentityldpid is None')
                if self.mplsldppeerldpid is None:
                    raise YPYDataValidationError('Key property mplsldppeerldpid is None')
                if self.mplsoutsegmentldplspindex is None:
                    raise YPYDataValidationError('Key property mplsoutsegmentldplspindex is None')

                return '/MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/MPLS-LDP-STD-MIB:mplsOutSegmentLdpLspTable/MPLS-LDP-STD-MIB:mplsOutSegmentLdpLspEntry[MPLS-LDP-STD-MIB:mplsLdpEntityIndex = ' + str(self.mplsldpentityindex) + '][MPLS-LDP-STD-MIB:mplsLdpEntityLdpId = ' + str(self.mplsldpentityldpid) + '][MPLS-LDP-STD-MIB:mplsLdpPeerLdpId = ' + str(self.mplsldppeerldpid) + '][MPLS-LDP-STD-MIB:mplsOutSegmentLdpLspIndex = ' + str(self.mplsoutsegmentldplspindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.mplsldpentityindex is not None:
                    return True

                if self.mplsldpentityldpid is not None:
                    return True

                if self.mplsldppeerldpid is not None:
                    return True

                if self.mplsoutsegmentldplspindex is not None:
                    return True

                if self.mplsoutsegmentldplsplabeltype is not None:
                    return True

                if self.mplsoutsegmentldplsptype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
                return meta._meta_table['MPLSLDPSTDMIB.MplsOutSegmentLdpLspTable.MplsOutSegmentLdpLspEntry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/MPLS-LDP-STD-MIB:mplsOutSegmentLdpLspTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mplsoutsegmentldplspentry is not None:
                for child_ref in self.mplsoutsegmentldplspentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
            return meta._meta_table['MPLSLDPSTDMIB.MplsOutSegmentLdpLspTable']['meta_info']

    @property
    def _common_path(self):

        return '/MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.mplsfecobjects is not None and self.mplsfecobjects._has_data():
            return True

        if self.mplsfecobjects is not None and self.mplsfecobjects.is_presence():
            return True

        if self.mplsfectable is not None and self.mplsfectable._has_data():
            return True

        if self.mplsfectable is not None and self.mplsfectable.is_presence():
            return True

        if self.mplsinsegmentldplsptable is not None and self.mplsinsegmentldplsptable._has_data():
            return True

        if self.mplsinsegmentldplsptable is not None and self.mplsinsegmentldplsptable.is_presence():
            return True

        if self.mplsldpentityobjects is not None and self.mplsldpentityobjects._has_data():
            return True

        if self.mplsldpentityobjects is not None and self.mplsldpentityobjects.is_presence():
            return True

        if self.mplsldpentitytable is not None and self.mplsldpentitytable._has_data():
            return True

        if self.mplsldpentitytable is not None and self.mplsldpentitytable.is_presence():
            return True

        if self.mplsldphelloadjacencytable is not None and self.mplsldphelloadjacencytable._has_data():
            return True

        if self.mplsldphelloadjacencytable is not None and self.mplsldphelloadjacencytable.is_presence():
            return True

        if self.mplsldplspfectable is not None and self.mplsldplspfectable._has_data():
            return True

        if self.mplsldplspfectable is not None and self.mplsldplspfectable.is_presence():
            return True

        if self.mplsldplsrobjects is not None and self.mplsldplsrobjects._has_data():
            return True

        if self.mplsldplsrobjects is not None and self.mplsldplsrobjects.is_presence():
            return True

        if self.mplsldppeertable is not None and self.mplsldppeertable._has_data():
            return True

        if self.mplsldppeertable is not None and self.mplsldppeertable.is_presence():
            return True

        if self.mplsldpsessionobjects is not None and self.mplsldpsessionobjects._has_data():
            return True

        if self.mplsldpsessionobjects is not None and self.mplsldpsessionobjects.is_presence():
            return True

        if self.mplsldpsessionpeeraddrtable is not None and self.mplsldpsessionpeeraddrtable._has_data():
            return True

        if self.mplsldpsessionpeeraddrtable is not None and self.mplsldpsessionpeeraddrtable.is_presence():
            return True

        if self.mplsoutsegmentldplsptable is not None and self.mplsoutsegmentldplsptable._has_data():
            return True

        if self.mplsoutsegmentldplsptable is not None and self.mplsoutsegmentldplsptable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _MPLS_LDP_STD_MIB as meta
        return meta._meta_table['MPLSLDPSTDMIB']['meta_info']



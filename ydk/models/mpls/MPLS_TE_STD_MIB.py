""" MPLS_TE_STD_MIB 

Copyright (C) The Internet Society (2004). The
initial version of this MIB module was published
in RFC 3812. For full legal notices see the RFC
itself or see\: http\://www.ietf.org/copyrights/ianamib.html

This MIB module contains managed object definitions
 for MPLS Traffic Engineering (TE) as defined in\:
1. Extensions to RSVP for LSP Tunnels, Awduche et
 al, RFC 3209, December 2001
2. Constraint\-Based LSP Setup using LDP, Jamoussi
 (Editor), RFC 3212, January 2002
3. Requirements for Traffic Engineering Over MPLS,
 Awduche, D., Malcolm, J., Agogbua, J., O'Dell, M.,
 and J. McManus, [RFC2702], September 1999

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.mpls.MPLS_TC_STD_MIB import MplsOwner_Enum
from ydk.models.mpls.MPLS_TC_STD_MIB import TeHopAddressType_Enum
from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum
from ydk.models.snmpv2.SNMPv2_TC import StorageType_Enum


class MPLSTESTDMIB(object):
    """
    
    
    .. attribute:: mplsteobjects
    
    	
    	**type**\: :py:class:`MplsTeObjects <ydk.models.mpls.MPLS_TE_STD_MIB.MPLSTESTDMIB.MplsTeObjects>`
    
    .. attribute:: mplstescalars
    
    	
    	**type**\: :py:class:`MplsTeScalars <ydk.models.mpls.MPLS_TE_STD_MIB.MPLSTESTDMIB.MplsTeScalars>`
    
    .. attribute:: mplstunnelarhoptable
    
    	The mplsTunnelARHopTable is used to indicate the hops for an MPLS tunnel defined in mplsTunnelTable, as reported by the MPLS signalling protocol. Thus at a transit LSR, this table (if the table is supported and if the signaling protocol is recording actual route information) contains the actual route of the whole tunnel. If the signaling protocol is not recording the actual route, this table MAY report the information from the mplsTunnelHopTable or the mplsTunnelCHopTable.  Each row in this table is indexed by mplsTunnelARHopListIndex. Each row also has a secondary index mplsTunnelARHopIndex, corresponding to the next hop that this row corresponds to.  Please note that since the information necessary to build entries within this table is not provided by some MPLS signalling protocols, implementation of this table is optional. Furthermore, since the information in this table is actually provided by the MPLS signalling protocol after the path has been set\-up, the entries in this table are provided only for observation, and hence, all variables in this table are accessible exclusively as read\- only.  Note also that the contents of this table may change while it is being read because of re\-routing activities. A network administrator may verify that the actual route read is consistent by reference to the mplsTunnelLastPathChange object
    	**type**\: :py:class:`MplsTunnelARHopTable <ydk.models.mpls.MPLS_TE_STD_MIB.MPLSTESTDMIB.MplsTunnelARHopTable>`
    
    .. attribute:: mplstunnelchoptable
    
    	The mplsTunnelCHopTable is used to indicate the hops, strict or loose, for an MPLS tunnel defined in mplsTunnelTable, as computed by a constraint\- based routing protocol, based on the mplsTunnelHopTable for the outgoing direction of the tunnel. Thus at a transit LSR, this table (if the table is supported) MAY contain the path computed by the CSPF engine on (or on behalf of) this LSR. Each row in this table is indexed by mplsTunnelCHopListIndex.  Each row also has a secondary index mplsTunnelCHopIndex, corresponding to the next hop that this row corresponds to. In case we want to specify a particular interface on the originating LSR of an outgoing tunnel by which we want packets to exit the LSR, we specify this as the first hop for this tunnel in mplsTunnelCHopTable.  Please note that since the information necessary to build entries within this table may not be supported by some LSRs, implementation of this table is optional. Furthermore, since the information in this table describes the path computed by the CSPF engine the entries in this table are read\-only
    	**type**\: :py:class:`MplsTunnelCHopTable <ydk.models.mpls.MPLS_TE_STD_MIB.MPLSTESTDMIB.MplsTunnelCHopTable>`
    
    .. attribute:: mplstunnelcrldprestable
    
    	The mplsTunnelCRLDPResTable allows a manager to specify which CR\-LDP\-specific resources are desired for an MPLS tunnel if that tunnel is signaled using CR\-LDP. Note that these attributes are in addition to those specified in mplsTunnelResourceTable. This table also allows several tunnels to point to a single entry in this table, implying that these tunnels should share resources
    	**type**\: :py:class:`MplsTunnelCRLDPResTable <ydk.models.mpls.MPLS_TE_STD_MIB.MPLSTESTDMIB.MplsTunnelCRLDPResTable>`
    
    .. attribute:: mplstunnelhoptable
    
    	The mplsTunnelHopTable is used to indicate the hops, strict or loose, for an instance of an MPLS tunnel defined in mplsTunnelTable, when it is established via signalling, for the outgoing direction of the tunnel. Thus at a transit LSR, this table contains the desired path of the tunnel from this LSR onwards. Each row in this table is indexed by mplsTunnelHopListIndex which corresponds to a group of hop lists or path options.  Each row also has a secondary index mplsTunnelHopIndex, which indicates a group of hops (also known as a path option). Finally, the third index, mplsTunnelHopIndex indicates the specific hop information for a path option. In case we want to specify a particular interface on the originating LSR of an outgoing tunnel by which we want packets to exit the LSR, we specify this as the first hop for this tunnel in mplsTunnelHopTable
    	**type**\: :py:class:`MplsTunnelHopTable <ydk.models.mpls.MPLS_TE_STD_MIB.MPLSTESTDMIB.MplsTunnelHopTable>`
    
    .. attribute:: mplstunnelresourcetable
    
    	The mplsTunnelResourceTable allows a manager to specify which resources are desired for an MPLS tunnel.  This table also allows several tunnels to point to a single entry in this table, implying that these tunnels should share resources
    	**type**\: :py:class:`MplsTunnelResourceTable <ydk.models.mpls.MPLS_TE_STD_MIB.MPLSTESTDMIB.MplsTunnelResourceTable>`
    
    .. attribute:: mplstunneltable
    
    	The mplsTunnelTable allows new MPLS tunnels to be created between an LSR and a remote endpoint, and existing tunnels to be reconfigured or removed. Note that only point\-to\-point tunnel segments are supported, although multipoint\-to\-point and point\- to\-multipoint connections are supported by an LSR acting as a cross\-connect.  Each MPLS tunnel can thus have one out\-segment originating at this LSR and/or one in\-segment terminating at this LSR
    	**type**\: :py:class:`MplsTunnelTable <ydk.models.mpls.MPLS_TE_STD_MIB.MPLSTESTDMIB.MplsTunnelTable>`
    
    

    """

    _prefix = 'mpls-te'
    _revision = '2004-06-03'

    def __init__(self):
        self.mplsteobjects = MPLSTESTDMIB.MplsTeObjects()
        self.mplsteobjects.parent = self
        self.mplstescalars = MPLSTESTDMIB.MplsTeScalars()
        self.mplstescalars.parent = self
        self.mplstunnelarhoptable = MPLSTESTDMIB.MplsTunnelARHopTable()
        self.mplstunnelarhoptable.parent = self
        self.mplstunnelchoptable = MPLSTESTDMIB.MplsTunnelCHopTable()
        self.mplstunnelchoptable.parent = self
        self.mplstunnelcrldprestable = MPLSTESTDMIB.MplsTunnelCRLDPResTable()
        self.mplstunnelcrldprestable.parent = self
        self.mplstunnelhoptable = MPLSTESTDMIB.MplsTunnelHopTable()
        self.mplstunnelhoptable.parent = self
        self.mplstunnelresourcetable = MPLSTESTDMIB.MplsTunnelResourceTable()
        self.mplstunnelresourcetable.parent = self
        self.mplstunneltable = MPLSTESTDMIB.MplsTunnelTable()
        self.mplstunneltable.parent = self


    class MplsTeObjects(object):
        """
        
        
        .. attribute:: mplstunnelhoplistindexnext
        
        	This object contains an appropriate value to be used for mplsTunnelHopListIndex when creating entries in the mplsTunnelHopTable.  If the number of unassigned entries is exhausted, a retrieval operation will return a value of 0.  This object may also return a value of 0 when the LSR is unable to accept conceptual row creation, for example, if the mplsTunnelHopTable is implemented as read\-only. To obtain the value of mplsTunnelHopListIndex for a new entry in the mplsTunnelHopTable, the manager issues a management protocol retrieval operation to obtain the current value of mplsTunnelHopIndex.  When the SET is performed to create a row in the mplsTunnelHopTable, the Command Responder (agent) must determine whether the value is indeed still unused; Two Network Management Applications may attempt to create a row (configuration entry) simultaneously and use the same value. If it is currently unused, the SET succeeds and the Command Responder (agent) changes the value of this object, according to an implementation\-specific algorithm. If the value is in use, however, the SET fails.  The Network Management Application must then re\-read this variable to obtain a new usable value
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplstunnelindexnext
        
        	This object contains an unused value for mplsTunnelIndex, or a zero to indicate that none exist. Negative values are not allowed, as they do not correspond to valid values of mplsTunnelIndex.  Note that this object offers an unused value for an mplsTunnelIndex value at the ingress side of a tunnel. At other LSRs the value of mplsTunnelIndex SHOULD be taken from the value signaled by the MPLS signaling protocol
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: mplstunnelnotificationenable
        
        	If this object is true, then it enables the generation of mplsTunnelUp and mplsTunnelDown traps, otherwise these traps are not emitted
        	**type**\: bool
        
        .. attribute:: mplstunnelresourceindexnext
        
        	This object contains the next appropriate value to be used for mplsTunnelResourceIndex when creating entries in the mplsTunnelResourceTable. If the number of unassigned entries is exhausted, a retrieval operation will return a value of 0.  This object may also return a value of 0 when the LSR is unable to accept conceptual row creation, for example, if the mplsTunnelTable is implemented as read\-only.  To obtain the mplsTunnelResourceIndex value for a new entry, the manager must first issue a management protocol retrieval operation to obtain the current value of this object.  When the SET is performed to create a row in the mplsTunnelResourceTable, the Command Responder (agent) must determine whether the value is indeed still unused; Two Network Management Applications may attempt to create a row (configuration entry) simultaneously and use the same value. If it is currently unused, the SET succeeds and the Command Responder (agent) changes the value of this object, according to an implementation\-specific algorithm. If the value is in use, however, the SET fails.  The Network Management Application must then re\-read this variable to obtain a new usable value
        	**type**\: int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'mpls-te'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplstunnelhoplistindexnext = None
            self.mplstunnelindexnext = None
            self.mplstunnelnotificationenable = None
            self.mplstunnelresourceindexnext = None

        @property
        def _common_path(self):

            return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTeObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mplstunnelhoplistindexnext is not None:
                return True

            if self.mplstunnelindexnext is not None:
                return True

            if self.mplstunnelnotificationenable is not None:
                return True

            if self.mplstunnelresourceindexnext is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _MPLS_TE_STD_MIB as meta
            return meta._meta_table['MPLSTESTDMIB.MplsTeObjects']['meta_info']


    class MplsTeScalars(object):
        """
        
        
        .. attribute:: mplstunnelactive
        
        	The number of tunnels active on this device. A tunnel is considered active if the mplsTunnelOperStatus is up(1)
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplstunnelconfigured
        
        	The number of tunnels configured on this device. A tunnel is considered configured if the mplsTunnelRowStatus is active(1)
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplstunnelmaxhops
        
        	The maximum number of hops that can be specified for a tunnel on this device
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplstunnelnotificationmaxrate
        
        	This variable indicates the maximum number of notifications issued per second. If events occur more rapidly, the implementation may simply fail to emit these notifications during that period, or may queue them until an appropriate time. A value of 0 means no throttling is applied and events may be notified at the rate at which they occur
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplstunneltedistproto
        
        	The traffic engineering distribution protocol(s) used by this LSR. Note that an LSR may support more than one distribution protocol simultaneously
        	**type**\: :py:class:`MplsTunnelTEDistProto_Bits <ydk.models.mpls.MPLS_TE_STD_MIB.MPLSTESTDMIB.MplsTeScalars.MplsTunnelTEDistProto_Bits>`
        
        

        """

        _prefix = 'mpls-te'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplstunnelactive = None
            self.mplstunnelconfigured = None
            self.mplstunnelmaxhops = None
            self.mplstunnelnotificationmaxrate = None
            self.mplstunneltedistproto = MPLSTESTDMIB.MplsTeScalars.MplsTunnelTEDistProto_Bits()

        class MplsTunnelTEDistProto_Bits(FixedBitsDict):
            """
            MplsTunnelTEDistProto_Bits

            The traffic engineering distribution protocol(s)
            used by this LSR. Note that an LSR may support more
            than one distribution protocol simultaneously.
            Keys are:- isis , other , ospf

            """

            def __init__(self):
                self._dictionary = { 
                    'isis':False,
                    'other':False,
                    'ospf':False,
                }
                self._pos_map = { 
                    'isis':2,
                    'other':0,
                    'ospf':1,
                }

        @property
        def _common_path(self):

            return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTeScalars'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mplstunnelactive is not None:
                return True

            if self.mplstunnelconfigured is not None:
                return True

            if self.mplstunnelmaxhops is not None:
                return True

            if self.mplstunnelnotificationmaxrate is not None:
                return True

            if self.mplstunneltedistproto is not None:
                if self.mplstunneltedistproto._has_data():
                    return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _MPLS_TE_STD_MIB as meta
            return meta._meta_table['MPLSTESTDMIB.MplsTeScalars']['meta_info']


    class MplsTunnelARHopTable(object):
        """
        The mplsTunnelARHopTable is used to indicate the
        hops for an MPLS tunnel defined in mplsTunnelTable,
        as reported by the MPLS signalling protocol. Thus at
        a transit LSR, this table (if the table is supported
        and if the signaling protocol is recording actual
        route information) contains the actual route of the
        whole tunnel. If the signaling protocol is not
        recording the actual route, this table MAY report
        the information from the mplsTunnelHopTable or the
        mplsTunnelCHopTable.
        
        Each row in this table is indexed by
        mplsTunnelARHopListIndex. Each row also has a
        secondary index mplsTunnelARHopIndex, corresponding
        to the next hop that this row corresponds to.
        
        Please note that since the information necessary to
        build entries within this table is not provided by
        some MPLS signalling protocols, implementation of
        this table is optional. Furthermore, since the
        information in this table is actually provided by
        the MPLS signalling protocol after the path has
        been set\-up, the entries in this table are provided
        only for observation, and hence, all variables in
        this table are accessible exclusively as read\-
        only.
        
        Note also that the contents of this table may change
        while it is being read because of re\-routing
        activities. A network administrator may verify that
        the actual route read is consistent by reference to
        the mplsTunnelLastPathChange object.
        
        .. attribute:: mplstunnelarhopentry
        
        	An entry in this table represents a tunnel hop.  An entry is created by the agent for signaled ERLSP set up by an MPLS signalling protocol
        	**type**\: list of :py:class:`MplsTunnelARHopEntry <ydk.models.mpls.MPLS_TE_STD_MIB.MPLSTESTDMIB.MplsTunnelARHopTable.MplsTunnelARHopEntry>`
        
        

        """

        _prefix = 'mpls-te'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplstunnelarhopentry = YList()
            self.mplstunnelarhopentry.parent = self
            self.mplstunnelarhopentry.name = 'mplstunnelarhopentry'


        class MplsTunnelARHopEntry(object):
            """
            An entry in this table represents a tunnel hop.  An
            entry is created by the agent for signaled ERLSP
            set up by an MPLS signalling protocol.
            
            .. attribute:: mplstunnelarhopindex
            
            	Secondary index into this table identifying the particular hop
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplstunnelarhoplistindex
            
            	Primary index into this table identifying a particular recorded hop list
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplstunnelarhopaddrtype
            
            	The Hop Address Type of this tunnel hop.  Note that lspid(5) is a valid option only for tunnels signaled via CRLDP
            	**type**\: :py:class:`TeHopAddressType_Enum <ydk.models.mpls.MPLS_TC_STD_MIB.TeHopAddressType_Enum>`
            
            .. attribute:: mplstunnelarhopaddrunnum
            
            	If mplsTunnelARHopAddrType is set to unnum(4), then this value will contain the interface identifier of the unnumbered interface for this hop. This object should be used in conjunction with mplsTunnelARHopIpAddr which would contain the LSR Router ID in this case. Otherwise the agent should set this object to zero\-length string and the manager should ignore this
            	**type**\: str
            
            	**range:** 4
            
            .. attribute:: mplstunnelarhopipaddr
            
            	The Tunnel Hop Address for this tunnel hop.  The type of this address is determined by the value of the corresponding mplsTunnelARHopAddrType. If mplsTunnelARHopAddrType is set to unnum(4),  then this value contains the LSR Router ID of the  unnumbered interface. Otherwise the agent SHOULD  set this object to the zero\-length string and the  manager should ignore this object
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mplstunnelarhoplspid
            
            	If mplsTunnelARHopAddrType is set to lspid(5), then this value will contain the LSP ID of this hop. This object is otherwise insignificant and should contain a value of 0 to indicate this fact
            	**type**\: str
            
            	**range:** 2 \| 6
            
            

            """

            _prefix = 'mpls-te'
            _revision = '2004-06-03'

            def __init__(self):
                self.parent = None
                self.mplstunnelarhopindex = None
                self.mplstunnelarhoplistindex = None
                self.mplstunnelarhopaddrtype = None
                self.mplstunnelarhopaddrunnum = None
                self.mplstunnelarhopipaddr = None
                self.mplstunnelarhoplspid = None

            @property
            def _common_path(self):
                if self.mplstunnelarhopindex is None:
                    raise YPYDataValidationError('Key property mplstunnelarhopindex is None')
                if self.mplstunnelarhoplistindex is None:
                    raise YPYDataValidationError('Key property mplstunnelarhoplistindex is None')

                return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTunnelARHopTable/MPLS-TE-STD-MIB:mplsTunnelARHopEntry[MPLS-TE-STD-MIB:mplsTunnelARHopIndex = ' + str(self.mplstunnelarhopindex) + '][MPLS-TE-STD-MIB:mplsTunnelARHopListIndex = ' + str(self.mplstunnelarhoplistindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.mplstunnelarhopindex is not None:
                    return True

                if self.mplstunnelarhoplistindex is not None:
                    return True

                if self.mplstunnelarhopaddrtype is not None:
                    return True

                if self.mplstunnelarhopaddrunnum is not None:
                    return True

                if self.mplstunnelarhopipaddr is not None:
                    return True

                if self.mplstunnelarhoplspid is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _MPLS_TE_STD_MIB as meta
                return meta._meta_table['MPLSTESTDMIB.MplsTunnelARHopTable.MplsTunnelARHopEntry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTunnelARHopTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mplstunnelarhopentry is not None:
                for child_ref in self.mplstunnelarhopentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _MPLS_TE_STD_MIB as meta
            return meta._meta_table['MPLSTESTDMIB.MplsTunnelARHopTable']['meta_info']


    class MplsTunnelCHopTable(object):
        """
        The mplsTunnelCHopTable is used to indicate the
        hops, strict or loose, for an MPLS tunnel defined
        in mplsTunnelTable, as computed by a constraint\-
        based routing protocol, based on the
        mplsTunnelHopTable for the outgoing direction of
        the tunnel. Thus at a transit LSR, this table (if
        the table is supported) MAY contain the path
        computed by the CSPF engine on (or on behalf of)
        this LSR. Each row in this table is indexed by
        mplsTunnelCHopListIndex.  Each row also has a
        secondary index mplsTunnelCHopIndex, corresponding
        to the next hop that this row corresponds to. In
        case we want to specify a particular interface on
        the originating LSR of an outgoing tunnel by which
        we want packets to exit the LSR, we specify this as
        the first hop for this tunnel in
        mplsTunnelCHopTable.
        
        Please note that since the information necessary to
        build entries within this table may not be
        supported by some LSRs, implementation of this
        table is optional. Furthermore, since the
        information in this table describes the path
        computed by the CSPF engine the entries in this
        table are read\-only.
        
        .. attribute:: mplstunnelchopentry
        
        	An entry in this table represents a tunnel hop.  An entry in this table is created by a path computation engine using CSPF techniques applied to the information collected by routing protocols and the hops specified in the corresponding mplsTunnelHopTable
        	**type**\: list of :py:class:`MplsTunnelCHopEntry <ydk.models.mpls.MPLS_TE_STD_MIB.MPLSTESTDMIB.MplsTunnelCHopTable.MplsTunnelCHopEntry>`
        
        

        """

        _prefix = 'mpls-te'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplstunnelchopentry = YList()
            self.mplstunnelchopentry.parent = self
            self.mplstunnelchopentry.name = 'mplstunnelchopentry'


        class MplsTunnelCHopEntry(object):
            """
            An entry in this table represents a tunnel hop.  An
            entry in this table is created by a path
            computation engine using CSPF techniques applied to
            the information collected by routing protocols and
            the hops specified in the corresponding
            mplsTunnelHopTable.
            
            .. attribute:: mplstunnelchopindex
            
            	Secondary index into this table identifying the particular hop
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplstunnelchoplistindex
            
            	Primary index into this table identifying a particular computed hop list
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplstunnelchopaddrtype
            
            	The Hop Address Type of this tunnel hop.  Note that lspid(5) is a valid option only for tunnels signaled via CRLDP
            	**type**\: :py:class:`TeHopAddressType_Enum <ydk.models.mpls.MPLS_TC_STD_MIB.TeHopAddressType_Enum>`
            
            .. attribute:: mplstunnelchopaddrunnum
            
            	If mplsTunnelCHopAddrType is set to unnum(4), then this value will contain the unnumbered interface identifier of this hop. This object should be used in conjunction with mplsTunnelCHopIpAddr which would contain the LSR Router ID in this case. Otherwise the agent should set this object to zero\- length string and the manager should ignore this
            	**type**\: str
            
            	**range:** 4
            
            .. attribute:: mplstunnelchopasnumber
            
            	If mplsTunnelCHopAddrType is set to asnumber(3), then this value will contain the AS number of this hop. Otherwise the agent should set this object to zero\-length string and the manager should ignore this
            	**type**\: str
            
            	**range:** 4
            
            .. attribute:: mplstunnelchopipaddr
            
            	The Tunnel Hop Address for this tunnel hop. The type of this address is determined by the  value of the corresponding mplsTunnelCHopAddrType.  If mplsTunnelCHopAddrType is set to unnum(4), then  this value will contain the LSR Router ID of the  unnumbered interface. Otherwise the agent should  set this object to the zero\-length string and the  manager SHOULD ignore this object
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mplstunnelchopipprefixlen
            
            	If mplsTunnelCHopAddrType is set to ipv4(1) or ipv6(2), then this value will contain an appropriate prefix length for the IP address in object mplsTunnelCHopIpAddr. Otherwise this value is irrelevant and should be ignored
            	**type**\: int
            
            	**range:** 0..2040
            
            .. attribute:: mplstunnelchoplspid
            
            	If mplsTunnelCHopAddrType is set to lspid(5), then this value will contain the LSP ID of this hop. This object is otherwise insignificant and should contain a value of 0 to indicate this fact
            	**type**\: str
            
            	**range:** 2 \| 6
            
            .. attribute:: mplstunnelchoptype
            
            	Denotes whether this is tunnel hop is routed in a strict or loose fashion
            	**type**\: :py:class:`MplsTunnelCHopType_Enum <ydk.models.mpls.MPLS_TE_STD_MIB.MPLSTESTDMIB.MplsTunnelCHopTable.MplsTunnelCHopEntry.MplsTunnelCHopType_Enum>`
            
            

            """

            _prefix = 'mpls-te'
            _revision = '2004-06-03'

            def __init__(self):
                self.parent = None
                self.mplstunnelchopindex = None
                self.mplstunnelchoplistindex = None
                self.mplstunnelchopaddrtype = None
                self.mplstunnelchopaddrunnum = None
                self.mplstunnelchopasnumber = None
                self.mplstunnelchopipaddr = None
                self.mplstunnelchopipprefixlen = None
                self.mplstunnelchoplspid = None
                self.mplstunnelchoptype = None

            class MplsTunnelCHopType_Enum(Enum):
                """
                MplsTunnelCHopType_Enum

                Denotes whether this is tunnel hop is routed in a
                strict or loose fashion.

                """

                STRICT = 1

                LOOSE = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _MPLS_TE_STD_MIB as meta
                    return meta._meta_table['MPLSTESTDMIB.MplsTunnelCHopTable.MplsTunnelCHopEntry.MplsTunnelCHopType_Enum']


            @property
            def _common_path(self):
                if self.mplstunnelchopindex is None:
                    raise YPYDataValidationError('Key property mplstunnelchopindex is None')
                if self.mplstunnelchoplistindex is None:
                    raise YPYDataValidationError('Key property mplstunnelchoplistindex is None')

                return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTunnelCHopTable/MPLS-TE-STD-MIB:mplsTunnelCHopEntry[MPLS-TE-STD-MIB:mplsTunnelCHopIndex = ' + str(self.mplstunnelchopindex) + '][MPLS-TE-STD-MIB:mplsTunnelCHopListIndex = ' + str(self.mplstunnelchoplistindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.mplstunnelchopindex is not None:
                    return True

                if self.mplstunnelchoplistindex is not None:
                    return True

                if self.mplstunnelchopaddrtype is not None:
                    return True

                if self.mplstunnelchopaddrunnum is not None:
                    return True

                if self.mplstunnelchopasnumber is not None:
                    return True

                if self.mplstunnelchopipaddr is not None:
                    return True

                if self.mplstunnelchopipprefixlen is not None:
                    return True

                if self.mplstunnelchoplspid is not None:
                    return True

                if self.mplstunnelchoptype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _MPLS_TE_STD_MIB as meta
                return meta._meta_table['MPLSTESTDMIB.MplsTunnelCHopTable.MplsTunnelCHopEntry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTunnelCHopTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mplstunnelchopentry is not None:
                for child_ref in self.mplstunnelchopentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _MPLS_TE_STD_MIB as meta
            return meta._meta_table['MPLSTESTDMIB.MplsTunnelCHopTable']['meta_info']


    class MplsTunnelCRLDPResTable(object):
        """
        The mplsTunnelCRLDPResTable allows a manager to
        specify which CR\-LDP\-specific resources are desired
        for an MPLS tunnel if that tunnel is signaled using
        CR\-LDP. Note that these attributes are in addition
        to those specified in mplsTunnelResourceTable. This
        table also allows several tunnels to point to a
        single entry in this table, implying that these
        tunnels should share resources.
        
        .. attribute:: mplstunnelcrldpresentry
        
        	An entry in this table represents a set of resources for an MPLS tunnel established using CRLDP (mplsTunnelSignallingProto equal to crldp (3)). An entry can be created by a network administrator or by an SNMP agent as instructed by any MPLS signalling protocol
        	**type**\: list of :py:class:`MplsTunnelCRLDPResEntry <ydk.models.mpls.MPLS_TE_STD_MIB.MPLSTESTDMIB.MplsTunnelCRLDPResTable.MplsTunnelCRLDPResEntry>`
        
        

        """

        _prefix = 'mpls-te'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplstunnelcrldpresentry = YList()
            self.mplstunnelcrldpresentry.parent = self
            self.mplstunnelcrldpresentry.name = 'mplstunnelcrldpresentry'


        class MplsTunnelCRLDPResEntry(object):
            """
            An entry in this table represents a set of resources
            for an MPLS tunnel established using CRLDP
            (mplsTunnelSignallingProto equal to crldp (3)). An
            entry can be created by a network administrator or
            by an SNMP agent as instructed by any MPLS
            signalling protocol.
            
            .. attribute:: mplstunnelresourceindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: mplstunnelcrldpresexburstsize
            
            	The Excess burst size in bytes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelcrldpresflags
            
            	The value of the 1 byte Flags conveyed as part of the traffic parameters during the establishment of the CRLSP. The bits in this object are to be interpreted as follows.  +\-\-+\-\-+\-\-+\-\-+\-\-+\-\-+\-\-+\-\-+ \| Res \|F6\|F5\|F4\|F3\|F2\|F1\| +\-\-+\-\-+\-\-+\-\-+\-\-+\-\-+\-\-+\-\-+  Res \- These bits are reserved. Zero on transmission. Ignored on receipt. F1 \- Corresponds to the PDR. F2 \- Corresponds to the PBS. F3 \- Corresponds to the CDR. F4 \- Corresponds to the CBS. F5 \- Corresponds to the EBS. F6 \- Corresponds to the Weight.  Each flag if is a Negotiable Flag corresponding to a Traffic Parameter. The Negotiable Flag value zero denotes Not Negotiable and value one denotes Negotiable
            	**type**\: int
            
            	**range:** 0..63
            
            .. attribute:: mplstunnelcrldpresfrequency
            
            	The granularity of the availability of committed rate
            	**type**\: :py:class:`MplsTunnelCRLDPResFrequency_Enum <ydk.models.mpls.MPLS_TE_STD_MIB.MPLSTESTDMIB.MplsTunnelCRLDPResTable.MplsTunnelCRLDPResEntry.MplsTunnelCRLDPResFrequency_Enum>`
            
            .. attribute:: mplstunnelcrldpresmeanburstsize
            
            	The mean burst size in bytes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelcrldpresrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table.  When a row in this table is in active(1) state, no objects in that row can be modified by the agent except mplsTunnelCRLDPResRowStatus and mplsTunnelCRLDPResStorageType
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: mplstunnelcrldpresstoragetype
            
            	The storage type for this CR\-LDP Resource entry. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: mplstunnelcrldpresweight
            
            	The relative weight for using excess bandwidth above its committed rate.  The value of 0 means that weight is not applicable for the CR\-LSP
            	**type**\: int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'mpls-te'
            _revision = '2004-06-03'

            def __init__(self):
                self.parent = None
                self.mplstunnelresourceindex = None
                self.mplstunnelcrldpresexburstsize = None
                self.mplstunnelcrldpresflags = None
                self.mplstunnelcrldpresfrequency = None
                self.mplstunnelcrldpresmeanburstsize = None
                self.mplstunnelcrldpresrowstatus = None
                self.mplstunnelcrldpresstoragetype = None
                self.mplstunnelcrldpresweight = None

            class MplsTunnelCRLDPResFrequency_Enum(Enum):
                """
                MplsTunnelCRLDPResFrequency_Enum

                The granularity of the availability of committed
                rate.

                """

                UNSPECIFIED = 1

                FREQUENT = 2

                VERYFREQUENT = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _MPLS_TE_STD_MIB as meta
                    return meta._meta_table['MPLSTESTDMIB.MplsTunnelCRLDPResTable.MplsTunnelCRLDPResEntry.MplsTunnelCRLDPResFrequency_Enum']


            @property
            def _common_path(self):
                if self.mplstunnelresourceindex is None:
                    raise YPYDataValidationError('Key property mplstunnelresourceindex is None')

                return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTunnelCRLDPResTable/MPLS-TE-STD-MIB:mplsTunnelCRLDPResEntry[MPLS-TE-STD-MIB:mplsTunnelResourceIndex = ' + str(self.mplstunnelresourceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.mplstunnelresourceindex is not None:
                    return True

                if self.mplstunnelcrldpresexburstsize is not None:
                    return True

                if self.mplstunnelcrldpresflags is not None:
                    return True

                if self.mplstunnelcrldpresfrequency is not None:
                    return True

                if self.mplstunnelcrldpresmeanburstsize is not None:
                    return True

                if self.mplstunnelcrldpresrowstatus is not None:
                    return True

                if self.mplstunnelcrldpresstoragetype is not None:
                    return True

                if self.mplstunnelcrldpresweight is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _MPLS_TE_STD_MIB as meta
                return meta._meta_table['MPLSTESTDMIB.MplsTunnelCRLDPResTable.MplsTunnelCRLDPResEntry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTunnelCRLDPResTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mplstunnelcrldpresentry is not None:
                for child_ref in self.mplstunnelcrldpresentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _MPLS_TE_STD_MIB as meta
            return meta._meta_table['MPLSTESTDMIB.MplsTunnelCRLDPResTable']['meta_info']


    class MplsTunnelHopTable(object):
        """
        The mplsTunnelHopTable is used to indicate the hops,
        strict or loose, for an instance of an MPLS tunnel
        defined in mplsTunnelTable, when it is established
        via signalling, for the outgoing direction of the
        tunnel. Thus at a transit LSR, this table contains
        the desired path of the tunnel from this LSR
        onwards. Each row in this table is indexed by
        mplsTunnelHopListIndex which corresponds to a group
        of hop lists or path options.  Each row also has a
        secondary index mplsTunnelHopIndex, which indicates
        a group of hops (also known as a path option).
        Finally, the third index, mplsTunnelHopIndex
        indicates the specific hop information for a path
        option. In case we want to specify a particular
        interface on the originating LSR of an outgoing
        tunnel by which we want packets to exit the LSR,
        we specify this as the first hop for this tunnel in
        mplsTunnelHopTable.
        
        .. attribute:: mplstunnelhopentry
        
        	An entry in this table represents a tunnel hop.  An entry is created by a network administrator for signaled ERLSP set up by an MPLS signalling protocol
        	**type**\: list of :py:class:`MplsTunnelHopEntry <ydk.models.mpls.MPLS_TE_STD_MIB.MPLSTESTDMIB.MplsTunnelHopTable.MplsTunnelHopEntry>`
        
        

        """

        _prefix = 'mpls-te'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplstunnelhopentry = YList()
            self.mplstunnelhopentry.parent = self
            self.mplstunnelhopentry.name = 'mplstunnelhopentry'


        class MplsTunnelHopEntry(object):
            """
            An entry in this table represents a tunnel hop.  An
            entry is created by a network administrator for
            signaled ERLSP set up by an MPLS signalling
            protocol.
            
            .. attribute:: mplstunnelhopindex
            
            	Tertiary index into this table identifying a particular hop
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplstunnelhoplistindex
            
            	Primary index into this table identifying a particular explicit route object
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplstunnelhoppathoptionindex
            
            	Secondary index into this table identifying a particular group of hops representing a particular configured path. This is otherwise known as a path option
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplstunnelhopaddrtype
            
            	The Hop Address Type of this tunnel hop.  The value of this object cannot be changed if the value of the corresponding mplsTunnelHopRowStatus object is 'active'.  Note that lspid(5) is a valid option only for tunnels signaled via CRLDP
            	**type**\: :py:class:`TeHopAddressType_Enum <ydk.models.mpls.MPLS_TC_STD_MIB.TeHopAddressType_Enum>`
            
            .. attribute:: mplstunnelhopaddrunnum
            
            	If mplsTunnelHopAddrType is set to unnum(4), then this value will contain the interface identifier of the unnumbered interface for this hop. This object should be used in conjunction with mplsTunnelHopIpAddress which would contain the LSR Router ID in this case. Otherwise the agent should set this object to zero\-length string and the manager should ignore this
            	**type**\: str
            
            	**range:** 4
            
            .. attribute:: mplstunnelhopasnumber
            
            	If mplsTunnelHopAddrType is set to asnumber(3), then this value will contain the AS number of this hop. Otherwise the agent should set this object to zero\- length string and the manager should ignore this
            	**type**\: str
            
            	**range:** 4
            
            .. attribute:: mplstunnelhopentrypathcomp
            
            	If this value is set to dynamic, then the user should only specify the source and destination of the path and expect that the CSPF will calculate the remainder of the path.  If this value is set to explicit, the user should specify the entire path for the tunnel to take.  This path may contain strict or loose hops.  Each hop along a specific path SHOULD have this object set to the same value
            	**type**\: :py:class:`MplsTunnelHopEntryPathComp_Enum <ydk.models.mpls.MPLS_TE_STD_MIB.MPLSTESTDMIB.MplsTunnelHopTable.MplsTunnelHopEntry.MplsTunnelHopEntryPathComp_Enum>`
            
            .. attribute:: mplstunnelhopinclude
            
            	If this value is set to true, then this indicates that this hop must be included in the tunnel's path. If this value is set to 'false', then this hop must be avoided when calculating the path for this tunnel. The default value of this object is 'true', so that by default all indicated hops are included in the CSPF path computation. If this object is set to 'false' the value of mplsTunnelHopType should be ignored
            	**type**\: bool
            
            .. attribute:: mplstunnelhopipaddr
            
            	The Tunnel Hop Address for this tunnel hop.  The type of this address is determined by the value of the corresponding mplsTunnelHopAddrType.  The value of this object cannot be changed if the value of the corresponding mplsTunnelHopRowStatus object is 'active'
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: mplstunnelhopipprefixlen
            
            	If mplsTunnelHopAddrType is set to ipv4(1) or ipv6(2), then this value will contain an appropriate prefix length for the IP address in object mplsTunnelHopIpAddr. Otherwise this value is irrelevant and should be ignored
            	**type**\: int
            
            	**range:** 0..2040
            
            .. attribute:: mplstunnelhoplspid
            
            	If mplsTunnelHopAddrType is set to lspid(5), then this value will contain the LSPID of a tunnel of this hop. The present tunnel being configured is tunneled through this hop (using label stacking). This object is otherwise insignificant and should contain a value of 0 to indicate this fact
            	**type**\: str
            
            	**range:** 2 \| 6
            
            .. attribute:: mplstunnelhoppathoptionname
            
            	The description of this series of hops as they relate to the specified path option. The value of this object SHOULD be the same for each hop in the series that comprises a path option
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: mplstunnelhoprowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table.  When a row in this table is in active(1) state, no objects in that row can be modified by the agent except mplsTunnelHopRowStatus and mplsTunnelHopStorageType
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: mplstunnelhopstoragetype
            
            	The storage type for this Hop entry. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: mplstunnelhoptype
            
            	Denotes whether this tunnel hop is routed in a strict or loose fashion. The value of this object has no meaning if the mplsTunnelHopInclude object is set to 'false'
            	**type**\: :py:class:`MplsTunnelHopType_Enum <ydk.models.mpls.MPLS_TE_STD_MIB.MPLSTESTDMIB.MplsTunnelHopTable.MplsTunnelHopEntry.MplsTunnelHopType_Enum>`
            
            

            """

            _prefix = 'mpls-te'
            _revision = '2004-06-03'

            def __init__(self):
                self.parent = None
                self.mplstunnelhopindex = None
                self.mplstunnelhoplistindex = None
                self.mplstunnelhoppathoptionindex = None
                self.mplstunnelhopaddrtype = None
                self.mplstunnelhopaddrunnum = None
                self.mplstunnelhopasnumber = None
                self.mplstunnelhopentrypathcomp = None
                self.mplstunnelhopinclude = None
                self.mplstunnelhopipaddr = None
                self.mplstunnelhopipprefixlen = None
                self.mplstunnelhoplspid = None
                self.mplstunnelhoppathoptionname = None
                self.mplstunnelhoprowstatus = None
                self.mplstunnelhopstoragetype = None
                self.mplstunnelhoptype = None

            class MplsTunnelHopEntryPathComp_Enum(Enum):
                """
                MplsTunnelHopEntryPathComp_Enum

                If this value is set to dynamic, then the user
                should only specify the source and destination of
                the path and expect that the CSPF will calculate
                the remainder of the path.  If this value is set to
                explicit, the user should specify the entire path
                for the tunnel to take.  This path may contain
                strict or loose hops.  Each hop along a specific
                path SHOULD have this object set to the same value

                """

                DYNAMIC = 1

                EXPLICIT = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _MPLS_TE_STD_MIB as meta
                    return meta._meta_table['MPLSTESTDMIB.MplsTunnelHopTable.MplsTunnelHopEntry.MplsTunnelHopEntryPathComp_Enum']


            class MplsTunnelHopType_Enum(Enum):
                """
                MplsTunnelHopType_Enum

                Denotes whether this tunnel hop is routed in a
                strict or loose fashion. The value of this object
                has no meaning if the mplsTunnelHopInclude object
                is set to 'false'.

                """

                STRICT = 1

                LOOSE = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _MPLS_TE_STD_MIB as meta
                    return meta._meta_table['MPLSTESTDMIB.MplsTunnelHopTable.MplsTunnelHopEntry.MplsTunnelHopType_Enum']


            @property
            def _common_path(self):
                if self.mplstunnelhopindex is None:
                    raise YPYDataValidationError('Key property mplstunnelhopindex is None')
                if self.mplstunnelhoplistindex is None:
                    raise YPYDataValidationError('Key property mplstunnelhoplistindex is None')
                if self.mplstunnelhoppathoptionindex is None:
                    raise YPYDataValidationError('Key property mplstunnelhoppathoptionindex is None')

                return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTunnelHopTable/MPLS-TE-STD-MIB:mplsTunnelHopEntry[MPLS-TE-STD-MIB:mplsTunnelHopIndex = ' + str(self.mplstunnelhopindex) + '][MPLS-TE-STD-MIB:mplsTunnelHopListIndex = ' + str(self.mplstunnelhoplistindex) + '][MPLS-TE-STD-MIB:mplsTunnelHopPathOptionIndex = ' + str(self.mplstunnelhoppathoptionindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.mplstunnelhopindex is not None:
                    return True

                if self.mplstunnelhoplistindex is not None:
                    return True

                if self.mplstunnelhoppathoptionindex is not None:
                    return True

                if self.mplstunnelhopaddrtype is not None:
                    return True

                if self.mplstunnelhopaddrunnum is not None:
                    return True

                if self.mplstunnelhopasnumber is not None:
                    return True

                if self.mplstunnelhopentrypathcomp is not None:
                    return True

                if self.mplstunnelhopinclude is not None:
                    return True

                if self.mplstunnelhopipaddr is not None:
                    return True

                if self.mplstunnelhopipprefixlen is not None:
                    return True

                if self.mplstunnelhoplspid is not None:
                    return True

                if self.mplstunnelhoppathoptionname is not None:
                    return True

                if self.mplstunnelhoprowstatus is not None:
                    return True

                if self.mplstunnelhopstoragetype is not None:
                    return True

                if self.mplstunnelhoptype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _MPLS_TE_STD_MIB as meta
                return meta._meta_table['MPLSTESTDMIB.MplsTunnelHopTable.MplsTunnelHopEntry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTunnelHopTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mplstunnelhopentry is not None:
                for child_ref in self.mplstunnelhopentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _MPLS_TE_STD_MIB as meta
            return meta._meta_table['MPLSTESTDMIB.MplsTunnelHopTable']['meta_info']


    class MplsTunnelResourceTable(object):
        """
        The mplsTunnelResourceTable allows a manager to
        specify which resources are desired for an MPLS
        tunnel.  This table also allows several tunnels to
        point to a single entry in this table, implying
        that these tunnels should share resources.
        
        .. attribute:: mplstunnelresourceentry
        
        	An entry in this table represents a set of resources for an MPLS tunnel.  An entry can be created by a network administrator or by an SNMP agent as instructed by any MPLS signalling protocol. An entry in this table referenced by a tunnel instance with zero mplsTunnelInstance value indicates a configured set of resource parameter. An entry referenced by a tunnel instance with a non\-zero mplsTunnelInstance reflects the in\-use resource parameters for the tunnel instance which may have been negotiated or modified by the MPLS signaling protocols
        	**type**\: list of :py:class:`MplsTunnelResourceEntry <ydk.models.mpls.MPLS_TE_STD_MIB.MPLSTESTDMIB.MplsTunnelResourceTable.MplsTunnelResourceEntry>`
        
        

        """

        _prefix = 'mpls-te'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplstunnelresourceentry = YList()
            self.mplstunnelresourceentry.parent = self
            self.mplstunnelresourceentry.name = 'mplstunnelresourceentry'


        class MplsTunnelResourceEntry(object):
            """
            An entry in this table represents a set of resources
            for an MPLS tunnel.  An entry can be created by a
            network administrator or by an SNMP agent as
            instructed by any MPLS signalling protocol.
            An entry in this table referenced by a tunnel instance
            with zero mplsTunnelInstance value indicates a
            configured set of resource parameter. An entry
            referenced by a tunnel instance with a non\-zero
            mplsTunnelInstance reflects the in\-use resource
            parameters for the tunnel instance which may have
            been negotiated or modified by the MPLS signaling
            protocols.
            
            .. attribute:: mplstunnelresourceindex
            
            	Uniquely identifies this row
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: mplstunnelresourceexburstsize
            
            	The Excess burst size in bytes.  The implementations which do not implement this variable must return noSuchObject exception for this object and must not allow a user to set this value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelresourcefrequency
            
            	The granularity of the availability of committed rate.  The implementations which do not implement this variable must return unspecified(1) for this value and must not allow a user to set this value
            	**type**\: :py:class:`MplsTunnelResourceFrequency_Enum <ydk.models.mpls.MPLS_TE_STD_MIB.MPLSTESTDMIB.MplsTunnelResourceTable.MplsTunnelResourceEntry.MplsTunnelResourceFrequency_Enum>`
            
            .. attribute:: mplstunnelresourcemaxburstsize
            
            	The maximum burst size in bytes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelresourcemaxrate
            
            	The maximum rate in bits/second.  Note that setting mplsTunnelResourceMaxRate, mplsTunnelResourceMeanRate, and mplsTunnelResourceMaxBurstSize to 0 indicates best\- effort treatment
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelresourcemeanburstsize
            
            	The mean burst size in bytes.  The implementations which do not implement this variable must return a noSuchObject exception for this object and must not allow a user to set this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelresourcemeanrate
            
            	This object is copied into an instance of mplsTrafficParamMeanRate in the mplsTrafficParamTable. The OID of this table entry is then copied into the corresponding mplsInSegmentTrafficParamPtr
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelresourcerowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table.  When a row in this table is in active(1) state, no objects in that row can be modified by the agent except mplsTunnelResourceRowStatus and mplsTunnelResourceStorageType
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: mplstunnelresourcestoragetype
            
            	The storage type for this Hop entry. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: mplstunnelresourceweight
            
            	The relative weight for using excess bandwidth above its committed rate.  The value of 0 means that weight is not applicable for the CR\-LSP
            	**type**\: int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'mpls-te'
            _revision = '2004-06-03'

            def __init__(self):
                self.parent = None
                self.mplstunnelresourceindex = None
                self.mplstunnelresourceexburstsize = None
                self.mplstunnelresourcefrequency = None
                self.mplstunnelresourcemaxburstsize = None
                self.mplstunnelresourcemaxrate = None
                self.mplstunnelresourcemeanburstsize = None
                self.mplstunnelresourcemeanrate = None
                self.mplstunnelresourcerowstatus = None
                self.mplstunnelresourcestoragetype = None
                self.mplstunnelresourceweight = None

            class MplsTunnelResourceFrequency_Enum(Enum):
                """
                MplsTunnelResourceFrequency_Enum

                The granularity of the availability of committed
                rate.  The implementations which do not implement
                this variable must return unspecified(1) for this
                value and must not allow a user to set this value.

                """

                UNSPECIFIED = 1

                FREQUENT = 2

                VERYFREQUENT = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _MPLS_TE_STD_MIB as meta
                    return meta._meta_table['MPLSTESTDMIB.MplsTunnelResourceTable.MplsTunnelResourceEntry.MplsTunnelResourceFrequency_Enum']


            @property
            def _common_path(self):
                if self.mplstunnelresourceindex is None:
                    raise YPYDataValidationError('Key property mplstunnelresourceindex is None')

                return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTunnelResourceTable/MPLS-TE-STD-MIB:mplsTunnelResourceEntry[MPLS-TE-STD-MIB:mplsTunnelResourceIndex = ' + str(self.mplstunnelresourceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.mplstunnelresourceindex is not None:
                    return True

                if self.mplstunnelresourceexburstsize is not None:
                    return True

                if self.mplstunnelresourcefrequency is not None:
                    return True

                if self.mplstunnelresourcemaxburstsize is not None:
                    return True

                if self.mplstunnelresourcemaxrate is not None:
                    return True

                if self.mplstunnelresourcemeanburstsize is not None:
                    return True

                if self.mplstunnelresourcemeanrate is not None:
                    return True

                if self.mplstunnelresourcerowstatus is not None:
                    return True

                if self.mplstunnelresourcestoragetype is not None:
                    return True

                if self.mplstunnelresourceweight is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _MPLS_TE_STD_MIB as meta
                return meta._meta_table['MPLSTESTDMIB.MplsTunnelResourceTable.MplsTunnelResourceEntry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTunnelResourceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mplstunnelresourceentry is not None:
                for child_ref in self.mplstunnelresourceentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _MPLS_TE_STD_MIB as meta
            return meta._meta_table['MPLSTESTDMIB.MplsTunnelResourceTable']['meta_info']


    class MplsTunnelTable(object):
        """
        The mplsTunnelTable allows new MPLS tunnels to be
        created between an LSR and a remote endpoint, and
        existing tunnels to be reconfigured or removed.
        Note that only point\-to\-point tunnel segments are
        supported, although multipoint\-to\-point and point\-
        to\-multipoint connections are supported by an LSR
        acting as a cross\-connect.  Each MPLS tunnel can
        thus have one out\-segment originating at this LSR
        and/or one in\-segment terminating at this LSR.
        
        .. attribute:: mplstunnelentry
        
        	An entry in this table represents an MPLS tunnel. An entry can be created by a network administrator or by an SNMP agent as instructed by an MPLS signalling protocol. Whenever a new entry is created with mplsTunnelIsIf set to true(1), then a corresponding entry is created in ifTable as well (see RFC 2863). The ifType of this entry is mplsTunnel(150).  A tunnel entry needs to be uniquely identified across a MPLS network. Indices mplsTunnelIndex and mplsTunnelInstance uniquely identify a tunnel on the LSR originating the tunnel.  To uniquely identify a tunnel across an MPLS network requires index mplsTunnelIngressLSRId.  The last index mplsTunnelEgressLSRId is useful in identifying all instances of a tunnel that terminate on the same egress LSR
        	**type**\: list of :py:class:`MplsTunnelEntry <ydk.models.mpls.MPLS_TE_STD_MIB.MPLSTESTDMIB.MplsTunnelTable.MplsTunnelEntry>`
        
        

        """

        _prefix = 'mpls-te'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplstunnelentry = YList()
            self.mplstunnelentry.parent = self
            self.mplstunnelentry.name = 'mplstunnelentry'


        class MplsTunnelEntry(object):
            """
            An entry in this table represents an MPLS tunnel.
            An entry can be created by a network administrator
            or by an SNMP agent as instructed by an MPLS
            signalling protocol. Whenever a new entry is
            created with mplsTunnelIsIf set to true(1), then a
            corresponding entry is created in ifTable as well
            (see RFC 2863). The ifType of this entry is
            mplsTunnel(150).
            
            A tunnel entry needs to be uniquely identified across
            a MPLS network. Indices mplsTunnelIndex and
            mplsTunnelInstance uniquely identify a tunnel on
            the LSR originating the tunnel.  To uniquely
            identify a tunnel across an MPLS network requires
            index mplsTunnelIngressLSRId.  The last index
            mplsTunnelEgressLSRId is useful in identifying all
            instances of a tunnel that terminate on the same
            egress LSR.
            
            .. attribute:: mplstunnelegresslsrid
            
            	Identity of the egress LSR associated with this tunnel instance
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelindex
            
            	Uniquely identifies a set of tunnel instances between a pair of ingress and egress LSRs. Managers should obtain new values for row creation in this table by reading mplsTunnelIndexNext. When the MPLS signalling protocol is rsvp(2) this value SHOULD be equal to the value signaled in the Tunnel Id of the Session object. When the MPLS signalling protocol is crldp(3) this value SHOULD be equal to the value signaled in the LSP ID
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: mplstunnelingresslsrid
            
            	Identity of the ingress LSR associated with this tunnel instance. When the MPLS signalling protocol is rsvp(2) this value SHOULD be equal to the Tunnel Sender Address in the Sender Template object and MAY be equal to the Extended Tunnel Id field in the SESSION object. When the MPLS signalling protocol is crldp(3) this value SHOULD be equal to the Ingress LSR Router ID field in the LSPID TLV object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelinstance
            
            	Uniquely identifies a particular instance of a tunnel between a pair of ingress and egress LSRs. It is useful to identify multiple instances of tunnels for the purposes of backup and parallel tunnels. When the MPLS signaling protocol is rsvp(2) this value SHOULD be equal to the LSP Id of the Sender Template object. When the signaling protocol is crldp(3) there is no equivalent signaling object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunneladminstatus
            
            	Indicates the desired operational status of this tunnel
            	**type**\: :py:class:`MplsTunnelAdminStatus_Enum <ydk.models.mpls.MPLS_TE_STD_MIB.MPLSTESTDMIB.MplsTunnelTable.MplsTunnelEntry.MplsTunnelAdminStatus_Enum>`
            
            .. attribute:: mplstunnelarhoptableindex
            
            	Index into the mplsTunnelARHopTable entry that specifies the actual hops traversed by the tunnel. This is automatically updated by the agent when the actual hops becomes available
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelchoptableindex
            
            	Index into the mplsTunnelCHopTable entry that specifies the computed hops traversed by the tunnel. This is automatically updated by the agent when computed hops become available or when computed hops get modified
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelcreationtime
            
            	Specifies the value of SysUpTime when the first instance of this tunnel came into existence. That is, when the value of mplsTunnelOperStatus was first set to up(1)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunneldescr
            
            	A textual string containing information about the tunnel.  If there is no description this object contains a zero length string. This object is may not be signaled by MPLS signaling protocols, consequentally the value of this object at transit and egress LSRs MAY be automatically generated or absent
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: mplstunnelexcludeanyaffinity
            
            	A link satisfies the exclude\-any constraint if and only if the link contains none of the administrative groups specified in the constraint
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelholdingprio
            
            	Indicates the holding priority for this tunnel
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: mplstunnelhoptableindex
            
            	Index into the mplsTunnelHopTable entry that specifies the explicit route hops for this tunnel. This object is meaningful only at the head\-end of the tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelifindex
            
            	If mplsTunnelIsIf is set to true, then this value contains the LSR\-assigned ifIndex which corresponds to an entry in the interfaces table.  Otherwise this variable should contain the value of zero indicating that a valid ifIndex was not assigned to this tunnel interface
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplstunnelincludeallaffinity
            
            	A link satisfies the include\-all constraint if and only if the link contains all of the administrative groups specified in the constraint
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelincludeanyaffinity
            
            	A link satisfies the include\-any constraint if and only if the constraint is zero, or the link and the constraint have a resource class in common
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelinstancepriority
            
            	This value indicates which priority, in descending order, with 0 indicating the lowest priority, within a group of tunnel instances. A group of tunnel instances is defined as a set of LSPs with the same mplsTunnelIndex in this table, but with a different mplsTunnelInstance. Tunnel instance priorities are used to denote the priority at which a particular tunnel instance will supercede another. Instances of tunnels containing the same mplsTunnelInstancePriority will be used for load sharing
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelinstanceuptime
            
            	This value identifies the total time that this tunnel instance's operStatus has been Up(1)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelisif
            
            	Denotes whether or not this tunnel corresponds to an interface represented in the interfaces group table. Note that if this variable is set to true then the ifName of the interface corresponding to this tunnel should have a value equal to mplsTunnelName.  Also see the description of ifName in RFC 2863.  This object is meaningful only at the ingress and egress LSRs
            	**type**\: bool
            
            .. attribute:: mplstunnellastpathchange
            
            	Specifies the time since the last change to the actual path for this tunnel instance
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnellocalprotectinuse
            
            	Indicates that the local repair mechanism is in use to maintain this tunnel (usually in the face of an outage of the link it was previously routed over)
            	**type**\: bool
            
            .. attribute:: mplstunnelname
            
            	The canonical name assigned to the tunnel. This name can be used to refer to the tunnel on the LSR's console port.  If mplsTunnelIsIf is set to true then the ifName of the interface corresponding to this tunnel should have a value equal to mplsTunnelName.  Also see the description of ifName in RFC 2863
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: mplstunneloperstatus
            
            	Indicates the actual operational status of this tunnel, which is typically but not limited to, a function of the state of individual segments of this tunnel
            	**type**\: :py:class:`MplsTunnelOperStatus_Enum <ydk.models.mpls.MPLS_TE_STD_MIB.MPLSTESTDMIB.MplsTunnelTable.MplsTunnelEntry.MplsTunnelOperStatus_Enum>`
            
            .. attribute:: mplstunnelowner
            
            	Denotes the entity that created and is responsible for managing this tunnel. This column is automatically filled by the agent on creation of a row
            	**type**\: :py:class:`MplsOwner_Enum <ydk.models.mpls.MPLS_TC_STD_MIB.MplsOwner_Enum>`
            
            .. attribute:: mplstunnelpathchanges
            
            	Specifies the number of times the actual path for this tunnel instance has changed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelpathinuse
            
            	This value denotes the configured path that was chosen for this tunnel. This value reflects the secondary index into mplsTunnelHopTable. This path may not exactly match the one in mplsTunnelARHopTable due to the fact that some CSPF modification may have taken place. See mplsTunnelARHopTable for the actual path being taken by the tunnel. A value of zero denotes that no path is currently in use or available
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelperfbytes
            
            	Number of bytes forwarded by the tunnel. This object should represents the 32\-bit value of the least significant part of the 64\-bit value if both mplsTunnelPerfHCBytes is returned
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelperferrors
            
            	Number of packets dropped because of errors or for other reasons
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelperfhcbytes
            
            	High capacity counter for number of bytes forwarded by the tunnel
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: mplstunnelperfhcpackets
            
            	High capacity counter for number of packets forwarded by the tunnel. 
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: mplstunnelperfpackets
            
            	Number of packets forwarded by the tunnel. This object should represents the 32\-bit value of the least significant part of the 64\-bit value if both mplsTunnelPerfHCPackets is returned
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelprimaryinstance
            
            	Specifies the instance index of the primary instance of this tunnel. More details of the definition of tunnel instances and the primary tunnel instance can be found in the description of the TEXTUAL\-CONVENTION MplsTunnelInstanceIndex
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelprimaryuptime
            
            	Specifies the total time the primary instance of this tunnel has been active. The primary instance of this tunnel is defined in mplsTunnelPrimaryInstance
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelresourcepointer
            
            	This variable represents a pointer to the traffic parameter specification for this tunnel.  This value may point at an entry in the mplsTunnelResourceEntry to indicate which mplsTunnelResourceEntry is to be assigned to this LSP instance.  This value may optionally point at an externally defined traffic parameter specification table.  A value of zeroDotZero indicates best\-effort treatment.  By having the same value of this object, two or more LSPs can indicate resource sharing
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplstunnelrole
            
            	This value signifies the role that this tunnel entry/instance represents. This value MUST be set to head(1) at the originating point of the tunnel. This value MUST be set to transit(2) at transit points along the tunnel, if transit points are supported. This value MUST be set to tail(3) at the terminating point of the tunnel if tunnel tails are supported.  The value headTail(4) is provided for tunnels that begin and end on the same LSR
            	**type**\: :py:class:`MplsTunnelRole_Enum <ydk.models.mpls.MPLS_TE_STD_MIB.MPLSTESTDMIB.MplsTunnelTable.MplsTunnelEntry.MplsTunnelRole_Enum>`
            
            .. attribute:: mplstunnelrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table.  When a row in this table is in active(1) state, no objects in that row can be modified by the agent except mplsTunnelAdminStatus, mplsTunnelRowStatus and mplsTunnelStorageType
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: mplstunnelsessionattributes
            
            	This bit mask indicates optional session values for this tunnel. The following describes these bit fields\:  fastRerouteThis flag indicates that the any tunnel hop may choose to reroute this tunnel without tearing it down.  This flag permits transit routers to use a local repair mechanism which may result in violation of the explicit routing of this tunnel. When a fault is detected on an adjacent downstream link or node, a transit router can re\-route traffic for fast service restoration.  mergingPermitted This flag permits transit routers to merge this session with other RSVP sessions for the purpose of reducing resource overhead on downstream transit routers, thereby providing better network scaling.  isPersistent  Indicates whether this tunnel should be restored automatically after a failure occurs.  isPinned   This flag indicates whether the loose\- routed hops of this tunnel are to be pinned.  recordRouteThis flag indicates whether or not the signalling protocol should remember the tunnel path after it has been signaled
            	**type**\: :py:class:`MplsTunnelSessionAttributes_Bits <ydk.models.mpls.MPLS_TE_STD_MIB.MPLSTESTDMIB.MplsTunnelTable.MplsTunnelEntry.MplsTunnelSessionAttributes_Bits>`
            
            .. attribute:: mplstunnelsetupprio
            
            	Indicates the setup priority of this tunnel
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: mplstunnelsignallingproto
            
            	The signalling protocol, if any, used to setup this tunnel
            	**type**\: :py:class:`MplsTunnelSignallingProto_Enum <ydk.models.mpls.MPLS_TE_STD_MIB.MPLSTESTDMIB.MplsTunnelTable.MplsTunnelEntry.MplsTunnelSignallingProto_Enum>`
            
            .. attribute:: mplstunnelstatetransitions
            
            	Specifies the number of times the state (mplsTunnelOperStatus) of this tunnel instance has changed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelstoragetype
            
            	The storage type for this tunnel entry. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: mplstunneltotaluptime
            
            	This value represents the aggregate up time for all instances of this tunnel, if available. If this value is unavailable, it MUST return a value of 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelxcpointer
            
            	This variable points to a row in the mplsXCTable. This table identifies the segments that compose this tunnel, their characteristics, and relationships to each other. A value of zeroDotZero indicates that no LSP has been associated with this tunnel yet
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'mpls-te'
            _revision = '2004-06-03'

            def __init__(self):
                self.parent = None
                self.mplstunnelegresslsrid = None
                self.mplstunnelindex = None
                self.mplstunnelingresslsrid = None
                self.mplstunnelinstance = None
                self.mplstunneladminstatus = None
                self.mplstunnelarhoptableindex = None
                self.mplstunnelchoptableindex = None
                self.mplstunnelcreationtime = None
                self.mplstunneldescr = None
                self.mplstunnelexcludeanyaffinity = None
                self.mplstunnelholdingprio = None
                self.mplstunnelhoptableindex = None
                self.mplstunnelifindex = None
                self.mplstunnelincludeallaffinity = None
                self.mplstunnelincludeanyaffinity = None
                self.mplstunnelinstancepriority = None
                self.mplstunnelinstanceuptime = None
                self.mplstunnelisif = None
                self.mplstunnellastpathchange = None
                self.mplstunnellocalprotectinuse = None
                self.mplstunnelname = None
                self.mplstunneloperstatus = None
                self.mplstunnelowner = None
                self.mplstunnelpathchanges = None
                self.mplstunnelpathinuse = None
                self.mplstunnelperfbytes = None
                self.mplstunnelperferrors = None
                self.mplstunnelperfhcbytes = None
                self.mplstunnelperfhcpackets = None
                self.mplstunnelperfpackets = None
                self.mplstunnelprimaryinstance = None
                self.mplstunnelprimaryuptime = None
                self.mplstunnelresourcepointer = None
                self.mplstunnelrole = None
                self.mplstunnelrowstatus = None
                self.mplstunnelsessionattributes = MPLSTESTDMIB.MplsTunnelTable.MplsTunnelEntry.MplsTunnelSessionAttributes_Bits()
                self.mplstunnelsetupprio = None
                self.mplstunnelsignallingproto = None
                self.mplstunnelstatetransitions = None
                self.mplstunnelstoragetype = None
                self.mplstunneltotaluptime = None
                self.mplstunnelxcpointer = None

            class MplsTunnelAdminStatus_Enum(Enum):
                """
                MplsTunnelAdminStatus_Enum

                Indicates the desired operational status of this
                tunnel.

                """

                UP = 1

                DOWN = 2

                TESTING = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _MPLS_TE_STD_MIB as meta
                    return meta._meta_table['MPLSTESTDMIB.MplsTunnelTable.MplsTunnelEntry.MplsTunnelAdminStatus_Enum']


            class MplsTunnelOperStatus_Enum(Enum):
                """
                MplsTunnelOperStatus_Enum

                Indicates the actual operational status of this
                tunnel, which is typically but not limited to, a
                function of the state of individual segments of
                this tunnel.

                """

                UP = 1

                DOWN = 2

                TESTING = 3

                UNKNOWN = 4

                DORMANT = 5

                NOTPRESENT = 6

                LOWERLAYERDOWN = 7


                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _MPLS_TE_STD_MIB as meta
                    return meta._meta_table['MPLSTESTDMIB.MplsTunnelTable.MplsTunnelEntry.MplsTunnelOperStatus_Enum']


            class MplsTunnelRole_Enum(Enum):
                """
                MplsTunnelRole_Enum

                This value signifies the role that this tunnel
                entry/instance represents. This value MUST be set
                to head(1) at the originating point of the tunnel.
                This value MUST be set to transit(2) at transit
                points along the tunnel, if transit points are
                supported. This value MUST be set to tail(3) at the
                terminating point of the tunnel if tunnel tails are
                supported.
                
                The value headTail(4) is provided for tunnels that
                begin and end on the same LSR.

                """

                HEAD = 1

                TRANSIT = 2

                TAIL = 3

                HEADTAIL = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _MPLS_TE_STD_MIB as meta
                    return meta._meta_table['MPLSTESTDMIB.MplsTunnelTable.MplsTunnelEntry.MplsTunnelRole_Enum']


            class MplsTunnelSignallingProto_Enum(Enum):
                """
                MplsTunnelSignallingProto_Enum

                The signalling protocol, if any, used to setup this
                tunnel.

                """

                NONE = 1

                RSVP = 2

                CRLDP = 3

                OTHER = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _MPLS_TE_STD_MIB as meta
                    return meta._meta_table['MPLSTESTDMIB.MplsTunnelTable.MplsTunnelEntry.MplsTunnelSignallingProto_Enum']


            class MplsTunnelSessionAttributes_Bits(FixedBitsDict):
                """
                MplsTunnelSessionAttributes_Bits

                This bit mask indicates optional session values for
                this tunnel. The following describes these bit
                fields\:
                
                fastRerouteThis flag indicates that the any tunnel
                hop may choose to reroute this tunnel without
                tearing it down.  This flag permits transit routers
                to use a local repair mechanism which may result in
                violation of the explicit routing of this tunnel.
                When a fault is detected on an adjacent downstream
                link or node, a transit router can re\-route traffic
                for fast service restoration.
                
                mergingPermitted This flag permits transit routers
                to merge this session with other RSVP sessions for
                the purpose of reducing resource overhead on
                downstream transit routers, thereby providing
                better network scaling.
                
                isPersistent  Indicates whether this tunnel should
                be restored automatically after a failure occurs.
                
                isPinned   This flag indicates whether the loose\-
                routed hops of this tunnel are to be pinned.
                
                recordRouteThis flag indicates whether or not the
                signalling protocol should remember the tunnel path
                after it has been signaled.
                Keys are:- isPersistent , recordRoute , mergingPermitted , fastReroute , isPinned

                """

                def __init__(self):
                    self._dictionary = { 
                        'isPersistent':False,
                        'recordRoute':False,
                        'mergingPermitted':False,
                        'fastReroute':False,
                        'isPinned':False,
                    }
                    self._pos_map = { 
                        'isPersistent':2,
                        'recordRoute':4,
                        'mergingPermitted':1,
                        'fastReroute':0,
                        'isPinned':3,
                    }

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

                return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTunnelTable/MPLS-TE-STD-MIB:mplsTunnelEntry[MPLS-TE-STD-MIB:mplsTunnelEgressLSRId = ' + str(self.mplstunnelegresslsrid) + '][MPLS-TE-STD-MIB:mplsTunnelIndex = ' + str(self.mplstunnelindex) + '][MPLS-TE-STD-MIB:mplsTunnelIngressLSRId = ' + str(self.mplstunnelingresslsrid) + '][MPLS-TE-STD-MIB:mplsTunnelInstance = ' + str(self.mplstunnelinstance) + ']'

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

                if self.mplstunneladminstatus is not None:
                    return True

                if self.mplstunnelarhoptableindex is not None:
                    return True

                if self.mplstunnelchoptableindex is not None:
                    return True

                if self.mplstunnelcreationtime is not None:
                    return True

                if self.mplstunneldescr is not None:
                    return True

                if self.mplstunnelexcludeanyaffinity is not None:
                    return True

                if self.mplstunnelholdingprio is not None:
                    return True

                if self.mplstunnelhoptableindex is not None:
                    return True

                if self.mplstunnelifindex is not None:
                    return True

                if self.mplstunnelincludeallaffinity is not None:
                    return True

                if self.mplstunnelincludeanyaffinity is not None:
                    return True

                if self.mplstunnelinstancepriority is not None:
                    return True

                if self.mplstunnelinstanceuptime is not None:
                    return True

                if self.mplstunnelisif is not None:
                    return True

                if self.mplstunnellastpathchange is not None:
                    return True

                if self.mplstunnellocalprotectinuse is not None:
                    return True

                if self.mplstunnelname is not None:
                    return True

                if self.mplstunneloperstatus is not None:
                    return True

                if self.mplstunnelowner is not None:
                    return True

                if self.mplstunnelpathchanges is not None:
                    return True

                if self.mplstunnelpathinuse is not None:
                    return True

                if self.mplstunnelperfbytes is not None:
                    return True

                if self.mplstunnelperferrors is not None:
                    return True

                if self.mplstunnelperfhcbytes is not None:
                    return True

                if self.mplstunnelperfhcpackets is not None:
                    return True

                if self.mplstunnelperfpackets is not None:
                    return True

                if self.mplstunnelprimaryinstance is not None:
                    return True

                if self.mplstunnelprimaryuptime is not None:
                    return True

                if self.mplstunnelresourcepointer is not None:
                    return True

                if self.mplstunnelrole is not None:
                    return True

                if self.mplstunnelrowstatus is not None:
                    return True

                if self.mplstunnelsessionattributes is not None:
                    if self.mplstunnelsessionattributes._has_data():
                        return True

                if self.mplstunnelsetupprio is not None:
                    return True

                if self.mplstunnelsignallingproto is not None:
                    return True

                if self.mplstunnelstatetransitions is not None:
                    return True

                if self.mplstunnelstoragetype is not None:
                    return True

                if self.mplstunneltotaluptime is not None:
                    return True

                if self.mplstunnelxcpointer is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _MPLS_TE_STD_MIB as meta
                return meta._meta_table['MPLSTESTDMIB.MplsTunnelTable.MplsTunnelEntry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTunnelTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mplstunnelentry is not None:
                for child_ref in self.mplstunnelentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _MPLS_TE_STD_MIB as meta
            return meta._meta_table['MPLSTESTDMIB.MplsTunnelTable']['meta_info']

    @property
    def _common_path(self):

        return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.mplsteobjects is not None and self.mplsteobjects._has_data():
            return True

        if self.mplsteobjects is not None and self.mplsteobjects.is_presence():
            return True

        if self.mplstescalars is not None and self.mplstescalars._has_data():
            return True

        if self.mplstescalars is not None and self.mplstescalars.is_presence():
            return True

        if self.mplstunnelarhoptable is not None and self.mplstunnelarhoptable._has_data():
            return True

        if self.mplstunnelarhoptable is not None and self.mplstunnelarhoptable.is_presence():
            return True

        if self.mplstunnelchoptable is not None and self.mplstunnelchoptable._has_data():
            return True

        if self.mplstunnelchoptable is not None and self.mplstunnelchoptable.is_presence():
            return True

        if self.mplstunnelcrldprestable is not None and self.mplstunnelcrldprestable._has_data():
            return True

        if self.mplstunnelcrldprestable is not None and self.mplstunnelcrldprestable.is_presence():
            return True

        if self.mplstunnelhoptable is not None and self.mplstunnelhoptable._has_data():
            return True

        if self.mplstunnelhoptable is not None and self.mplstunnelhoptable.is_presence():
            return True

        if self.mplstunnelresourcetable is not None and self.mplstunnelresourcetable._has_data():
            return True

        if self.mplstunnelresourcetable is not None and self.mplstunnelresourcetable.is_presence():
            return True

        if self.mplstunneltable is not None and self.mplstunneltable._has_data():
            return True

        if self.mplstunneltable is not None and self.mplstunneltable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _MPLS_TE_STD_MIB as meta
        return meta._meta_table['MPLSTESTDMIB']['meta_info']



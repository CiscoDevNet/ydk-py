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

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class MplsTeStdMib(object):
    """
    
    
    .. attribute:: mplsteobjects
    
    	
    	**type**\:   :py:class:`Mplsteobjects <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplsteobjects>`
    
    .. attribute:: mplstescalars
    
    	
    	**type**\:   :py:class:`Mplstescalars <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstescalars>`
    
    .. attribute:: mplstunnelarhoptable
    
    	The mplsTunnelARHopTable is used to indicate the hops for an MPLS tunnel defined in mplsTunnelTable, as reported by the MPLS signalling protocol. Thus at a transit LSR, this table (if the table is supported and if the signaling protocol is recording actual route information) contains the actual route of the whole tunnel. If the signaling protocol is not recording the actual route, this table MAY report the information from the mplsTunnelHopTable or the mplsTunnelCHopTable.  Each row in this table is indexed by mplsTunnelARHopListIndex. Each row also has a secondary index mplsTunnelARHopIndex, corresponding to the next hop that this row corresponds to.  Please note that since the information necessary to build entries within this table is not provided by some MPLS signalling protocols, implementation of this table is optional. Furthermore, since the information in this table is actually provided by the MPLS signalling protocol after the path has been set\-up, the entries in this table are provided only for observation, and hence, all variables in this table are accessible exclusively as read\- only.  Note also that the contents of this table may change while it is being read because of re\-routing activities. A network administrator may verify that the actual route read is consistent by reference to the mplsTunnelLastPathChange object
    	**type**\:   :py:class:`Mplstunnelarhoptable <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelarhoptable>`
    
    .. attribute:: mplstunnelchoptable
    
    	The mplsTunnelCHopTable is used to indicate the hops, strict or loose, for an MPLS tunnel defined in mplsTunnelTable, as computed by a constraint\- based routing protocol, based on the mplsTunnelHopTable for the outgoing direction of the tunnel. Thus at a transit LSR, this table (if the table is supported) MAY contain the path computed by the CSPF engine on (or on behalf of) this LSR. Each row in this table is indexed by mplsTunnelCHopListIndex.  Each row also has a secondary index mplsTunnelCHopIndex, corresponding to the next hop that this row corresponds to. In case we want to specify a particular interface on the originating LSR of an outgoing tunnel by which we want packets to exit the LSR, we specify this as the first hop for this tunnel in mplsTunnelCHopTable.  Please note that since the information necessary to build entries within this table may not be supported by some LSRs, implementation of this table is optional. Furthermore, since the information in this table describes the path computed by the CSPF engine the entries in this table are read\-only
    	**type**\:   :py:class:`Mplstunnelchoptable <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelchoptable>`
    
    .. attribute:: mplstunnelcrldprestable
    
    	The mplsTunnelCRLDPResTable allows a manager to specify which CR\-LDP\-specific resources are desired for an MPLS tunnel if that tunnel is signaled using CR\-LDP. Note that these attributes are in addition to those specified in mplsTunnelResourceTable. This table also allows several tunnels to point to a single entry in this table, implying that these tunnels should share resources
    	**type**\:   :py:class:`Mplstunnelcrldprestable <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelcrldprestable>`
    
    .. attribute:: mplstunnelhoptable
    
    	The mplsTunnelHopTable is used to indicate the hops, strict or loose, for an instance of an MPLS tunnel defined in mplsTunnelTable, when it is established via signalling, for the outgoing direction of the tunnel. Thus at a transit LSR, this table contains the desired path of the tunnel from this LSR onwards. Each row in this table is indexed by mplsTunnelHopListIndex which corresponds to a group of hop lists or path options.  Each row also has a secondary index mplsTunnelHopIndex, which indicates a group of hops (also known as a path option). Finally, the third index, mplsTunnelHopIndex indicates the specific hop information for a path option. In case we want to specify a particular interface on the originating LSR of an outgoing tunnel by which we want packets to exit the LSR, we specify this as the first hop for this tunnel in mplsTunnelHopTable
    	**type**\:   :py:class:`Mplstunnelhoptable <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelhoptable>`
    
    .. attribute:: mplstunnelresourcetable
    
    	The mplsTunnelResourceTable allows a manager to specify which resources are desired for an MPLS tunnel.  This table also allows several tunnels to point to a single entry in this table, implying that these tunnels should share resources
    	**type**\:   :py:class:`Mplstunnelresourcetable <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelresourcetable>`
    
    .. attribute:: mplstunneltable
    
    	The mplsTunnelTable allows new MPLS tunnels to be created between an LSR and a remote endpoint, and existing tunnels to be reconfigured or removed. Note that only point\-to\-point tunnel segments are supported, although multipoint\-to\-point and point\- to\-multipoint connections are supported by an LSR acting as a cross\-connect.  Each MPLS tunnel can thus have one out\-segment originating at this LSR and/or one in\-segment terminating at this LSR
    	**type**\:   :py:class:`Mplstunneltable <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunneltable>`
    
    

    """

    _prefix = 'MPLS-TE-STD-MIB'
    _revision = '2004-06-03'

    def __init__(self):
        self.mplsteobjects = MplsTeStdMib.Mplsteobjects()
        self.mplsteobjects.parent = self
        self.mplstescalars = MplsTeStdMib.Mplstescalars()
        self.mplstescalars.parent = self
        self.mplstunnelarhoptable = MplsTeStdMib.Mplstunnelarhoptable()
        self.mplstunnelarhoptable.parent = self
        self.mplstunnelchoptable = MplsTeStdMib.Mplstunnelchoptable()
        self.mplstunnelchoptable.parent = self
        self.mplstunnelcrldprestable = MplsTeStdMib.Mplstunnelcrldprestable()
        self.mplstunnelcrldprestable.parent = self
        self.mplstunnelhoptable = MplsTeStdMib.Mplstunnelhoptable()
        self.mplstunnelhoptable.parent = self
        self.mplstunnelresourcetable = MplsTeStdMib.Mplstunnelresourcetable()
        self.mplstunnelresourcetable.parent = self
        self.mplstunneltable = MplsTeStdMib.Mplstunneltable()
        self.mplstunneltable.parent = self


    class Mplstescalars(object):
        """
        
        
        .. attribute:: mplstunnelactive
        
        	The number of tunnels active on this device. A tunnel is considered active if the mplsTunnelOperStatus is up(1)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplstunnelconfigured
        
        	The number of tunnels configured on this device. A tunnel is considered configured if the mplsTunnelRowStatus is active(1)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplstunnelmaxhops
        
        	The maximum number of hops that can be specified for a tunnel on this device
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplstunnelnotificationmaxrate
        
        	This variable indicates the maximum number of notifications issued per second. If events occur more rapidly, the implementation may simply fail to emit these notifications during that period, or may queue them until an appropriate time. A value of 0 means no throttling is applied and events may be notified at the rate at which they occur
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplstunneltedistproto
        
        	The traffic engineering distribution protocol(s) used by this LSR. Note that an LSR may support more than one distribution protocol simultaneously
        	**type**\:   :py:class:`Mplstunneltedistproto <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstescalars.Mplstunneltedistproto>`
        
        

        """

        _prefix = 'MPLS-TE-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplstunnelactive = None
            self.mplstunnelconfigured = None
            self.mplstunnelmaxhops = None
            self.mplstunnelnotificationmaxrate = None
            self.mplstunneltedistproto = MplsTeStdMib.Mplstescalars.Mplstunneltedistproto()

        class Mplstunneltedistproto(FixedBitsDict):
            """
            Mplstunneltedistproto

            The traffic engineering distribution protocol(s)
            used by this LSR. Note that an LSR may support more
            than one distribution protocol simultaneously.
            Keys are:- other , ospf , isis

            """

            def __init__(self):
                self._dictionary = { 
                    'other':False,
                    'ospf':False,
                    'isis':False,
                }
                self._pos_map = { 
                    'other':0,
                    'ospf':1,
                    'isis':2,
                }

        @property
        def _common_path(self):

            return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTeScalars'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
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

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_TE_STD_MIB as meta
            return meta._meta_table['MplsTeStdMib.Mplstescalars']['meta_info']


    class Mplsteobjects(object):
        """
        
        
        .. attribute:: mplstunnelhoplistindexnext
        
        	This object contains an appropriate value to be used for mplsTunnelHopListIndex when creating entries in the mplsTunnelHopTable.  If the number of unassigned entries is exhausted, a retrieval operation will return a value of 0.  This object may also return a value of 0 when the LSR is unable to accept conceptual row creation, for example, if the mplsTunnelHopTable is implemented as read\-only. To obtain the value of mplsTunnelHopListIndex for a new entry in the mplsTunnelHopTable, the manager issues a management protocol retrieval operation to obtain the current value of mplsTunnelHopIndex.  When the SET is performed to create a row in the mplsTunnelHopTable, the Command Responder (agent) must determine whether the value is indeed still unused; Two Network Management Applications may attempt to create a row (configuration entry) simultaneously and use the same value. If it is currently unused, the SET succeeds and the Command Responder (agent) changes the value of this object, according to an implementation\-specific algorithm. If the value is in use, however, the SET fails.  The Network Management Application must then re\-read this variable to obtain a new usable value
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplstunnelindexnext
        
        	This object contains an unused value for mplsTunnelIndex, or a zero to indicate that none exist. Negative values are not allowed, as they do not correspond to valid values of mplsTunnelIndex.  Note that this object offers an unused value for an mplsTunnelIndex value at the ingress side of a tunnel. At other LSRs the value of mplsTunnelIndex SHOULD be taken from the value signaled by the MPLS signaling protocol
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: mplstunnelnotificationenable
        
        	If this object is true, then it enables the generation of mplsTunnelUp and mplsTunnelDown traps, otherwise these traps are not emitted
        	**type**\:  bool
        
        .. attribute:: mplstunnelresourceindexnext
        
        	This object contains the next appropriate value to be used for mplsTunnelResourceIndex when creating entries in the mplsTunnelResourceTable. If the number of unassigned entries is exhausted, a retrieval operation will return a value of 0.  This object may also return a value of 0 when the LSR is unable to accept conceptual row creation, for example, if the mplsTunnelTable is implemented as read\-only.  To obtain the mplsTunnelResourceIndex value for a new entry, the manager must first issue a management protocol retrieval operation to obtain the current value of this object.  When the SET is performed to create a row in the mplsTunnelResourceTable, the Command Responder (agent) must determine whether the value is indeed still unused; Two Network Management Applications may attempt to create a row (configuration entry) simultaneously and use the same value. If it is currently unused, the SET succeeds and the Command Responder (agent) changes the value of this object, according to an implementation\-specific algorithm. If the value is in use, however, the SET fails.  The Network Management Application must then re\-read this variable to obtain a new usable value
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'MPLS-TE-STD-MIB'
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
            if self.mplstunnelhoplistindexnext is not None:
                return True

            if self.mplstunnelindexnext is not None:
                return True

            if self.mplstunnelnotificationenable is not None:
                return True

            if self.mplstunnelresourceindexnext is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_TE_STD_MIB as meta
            return meta._meta_table['MplsTeStdMib.Mplsteobjects']['meta_info']


    class Mplstunneltable(object):
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
        	**type**\: list of    :py:class:`Mplstunnelentry <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunneltable.Mplstunnelentry>`
        
        

        """

        _prefix = 'MPLS-TE-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplstunnelentry = YList()
            self.mplstunnelentry.parent = self
            self.mplstunnelentry.name = 'mplstunnelentry'


        class Mplstunnelentry(object):
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
            
            .. attribute:: mplstunnelindex  <key>
            
            	Uniquely identifies a set of tunnel instances between a pair of ingress and egress LSRs. Managers should obtain new values for row creation in this table by reading mplsTunnelIndexNext. When the MPLS signalling protocol is rsvp(2) this value SHOULD be equal to the value signaled in the Tunnel Id of the Session object. When the MPLS signalling protocol is crldp(3) this value SHOULD be equal to the value signaled in the LSP ID
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: mplstunnelinstance  <key>
            
            	Uniquely identifies a particular instance of a tunnel between a pair of ingress and egress LSRs. It is useful to identify multiple instances of tunnels for the purposes of backup and parallel tunnels. When the MPLS signaling protocol is rsvp(2) this value SHOULD be equal to the LSP Id of the Sender Template object. When the signaling protocol is crldp(3) there is no equivalent signaling object
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelingresslsrid  <key>
            
            	Identity of the ingress LSR associated with this tunnel instance. When the MPLS signalling protocol is rsvp(2) this value SHOULD be equal to the Tunnel Sender Address in the Sender Template object and MAY be equal to the Extended Tunnel Id field in the SESSION object. When the MPLS signalling protocol is crldp(3) this value SHOULD be equal to the Ingress LSR Router ID field in the LSPID TLV object
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelegresslsrid  <key>
            
            	Identity of the egress LSR associated with this tunnel instance
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunneladminstatus
            
            	Indicates the desired operational status of this tunnel
            	**type**\:   :py:class:`MplstunneladminstatusEnum <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunneltable.Mplstunnelentry.MplstunneladminstatusEnum>`
            
            .. attribute:: mplstunnelarhoptableindex
            
            	Index into the mplsTunnelARHopTable entry that specifies the actual hops traversed by the tunnel. This is automatically updated by the agent when the actual hops becomes available
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelchoptableindex
            
            	Index into the mplsTunnelCHopTable entry that specifies the computed hops traversed by the tunnel. This is automatically updated by the agent when computed hops become available or when computed hops get modified
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelcreationtime
            
            	Specifies the value of SysUpTime when the first instance of this tunnel came into existence. That is, when the value of mplsTunnelOperStatus was first set to up(1)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunneldescr
            
            	A textual string containing information about the tunnel.  If there is no description this object contains a zero length string. This object is may not be signaled by MPLS signaling protocols, consequentally the value of this object at transit and egress LSRs MAY be automatically generated or absent
            	**type**\:  str
            
            .. attribute:: mplstunnelexcludeanyaffinity
            
            	A link satisfies the exclude\-any constraint if and only if the link contains none of the administrative groups specified in the constraint
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelholdingprio
            
            	Indicates the holding priority for this tunnel
            	**type**\:  int
            
            	**range:** 0..7
            
            .. attribute:: mplstunnelhoptableindex
            
            	Index into the mplsTunnelHopTable entry that specifies the explicit route hops for this tunnel. This object is meaningful only at the head\-end of the tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelifindex
            
            	If mplsTunnelIsIf is set to true, then this value contains the LSR\-assigned ifIndex which corresponds to an entry in the interfaces table.  Otherwise this variable should contain the value of zero indicating that a valid ifIndex was not assigned to this tunnel interface
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplstunnelincludeallaffinity
            
            	A link satisfies the include\-all constraint if and only if the link contains all of the administrative groups specified in the constraint
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelincludeanyaffinity
            
            	A link satisfies the include\-any constraint if and only if the constraint is zero, or the link and the constraint have a resource class in common
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelinstancepriority
            
            	This value indicates which priority, in descending order, with 0 indicating the lowest priority, within a group of tunnel instances. A group of tunnel instances is defined as a set of LSPs with the same mplsTunnelIndex in this table, but with a different mplsTunnelInstance. Tunnel instance priorities are used to denote the priority at which a particular tunnel instance will supercede another. Instances of tunnels containing the same mplsTunnelInstancePriority will be used for load sharing
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelinstanceuptime
            
            	This value identifies the total time that this tunnel instance's operStatus has been Up(1)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelisif
            
            	Denotes whether or not this tunnel corresponds to an interface represented in the interfaces group table. Note that if this variable is set to true then the ifName of the interface corresponding to this tunnel should have a value equal to mplsTunnelName.  Also see the description of ifName in RFC 2863.  This object is meaningful only at the ingress and egress LSRs
            	**type**\:  bool
            
            .. attribute:: mplstunnellastpathchange
            
            	Specifies the time since the last change to the actual path for this tunnel instance
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnellocalprotectinuse
            
            	Indicates that the local repair mechanism is in use to maintain this tunnel (usually in the face of an outage of the link it was previously routed over)
            	**type**\:  bool
            
            .. attribute:: mplstunnelname
            
            	The canonical name assigned to the tunnel. This name can be used to refer to the tunnel on the LSR's console port.  If mplsTunnelIsIf is set to true then the ifName of the interface corresponding to this tunnel should have a value equal to mplsTunnelName.  Also see the description of ifName in RFC 2863
            	**type**\:  str
            
            .. attribute:: mplstunneloperstatus
            
            	Indicates the actual operational status of this tunnel, which is typically but not limited to, a function of the state of individual segments of this tunnel
            	**type**\:   :py:class:`MplstunneloperstatusEnum <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunneltable.Mplstunnelentry.MplstunneloperstatusEnum>`
            
            .. attribute:: mplstunnelowner
            
            	Denotes the entity that created and is responsible for managing this tunnel. This column is automatically filled by the agent on creation of a row
            	**type**\:   :py:class:`MplsownerEnum <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.MplsownerEnum>`
            
            .. attribute:: mplstunnelpathchanges
            
            	Specifies the number of times the actual path for this tunnel instance has changed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelpathinuse
            
            	This value denotes the configured path that was chosen for this tunnel. This value reflects the secondary index into mplsTunnelHopTable. This path may not exactly match the one in mplsTunnelARHopTable due to the fact that some CSPF modification may have taken place. See mplsTunnelARHopTable for the actual path being taken by the tunnel. A value of zero denotes that no path is currently in use or available
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelperfbytes
            
            	Number of bytes forwarded by the tunnel. This object should represents the 32\-bit value of the least significant part of the 64\-bit value if both mplsTunnelPerfHCBytes is returned
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelperferrors
            
            	Number of packets dropped because of errors or for other reasons
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelperfhcbytes
            
            	High capacity counter for number of bytes forwarded by the tunnel
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: mplstunnelperfhcpackets
            
            	High capacity counter for number of packets forwarded by the tunnel. 
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: mplstunnelperfpackets
            
            	Number of packets forwarded by the tunnel. This object should represents the 32\-bit value of the least significant part of the 64\-bit value if both mplsTunnelPerfHCPackets is returned
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelprimaryinstance
            
            	Specifies the instance index of the primary instance of this tunnel. More details of the definition of tunnel instances and the primary tunnel instance can be found in the description of the TEXTUAL\-CONVENTION MplsTunnelInstanceIndex
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelprimaryuptime
            
            	Specifies the total time the primary instance of this tunnel has been active. The primary instance of this tunnel is defined in mplsTunnelPrimaryInstance
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelresourcepointer
            
            	This variable represents a pointer to the traffic parameter specification for this tunnel.  This value may point at an entry in the mplsTunnelResourceEntry to indicate which mplsTunnelResourceEntry is to be assigned to this LSP instance.  This value may optionally point at an externally defined traffic parameter specification table.  A value of zeroDotZero indicates best\-effort treatment.  By having the same value of this object, two or more LSPs can indicate resource sharing
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplstunnelrole
            
            	This value signifies the role that this tunnel entry/instance represents. This value MUST be set to head(1) at the originating point of the tunnel. This value MUST be set to transit(2) at transit points along the tunnel, if transit points are supported. This value MUST be set to tail(3) at the terminating point of the tunnel if tunnel tails are supported.  The value headTail(4) is provided for tunnels that begin and end on the same LSR
            	**type**\:   :py:class:`MplstunnelroleEnum <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunneltable.Mplstunnelentry.MplstunnelroleEnum>`
            
            .. attribute:: mplstunnelrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table.  When a row in this table is in active(1) state, no objects in that row can be modified by the agent except mplsTunnelAdminStatus, mplsTunnelRowStatus and mplsTunnelStorageType
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: mplstunnelsessionattributes
            
            	This bit mask indicates optional session values for this tunnel. The following describes these bit fields\:  fastRerouteThis flag indicates that the any tunnel hop may choose to reroute this tunnel without tearing it down.  This flag permits transit routers to use a local repair mechanism which may result in violation of the explicit routing of this tunnel. When a fault is detected on an adjacent downstream link or node, a transit router can re\-route traffic for fast service restoration.  mergingPermitted This flag permits transit routers to merge this session with other RSVP sessions for the purpose of reducing resource overhead on downstream transit routers, thereby providing better network scaling.  isPersistent  Indicates whether this tunnel should be restored automatically after a failure occurs.  isPinned   This flag indicates whether the loose\- routed hops of this tunnel are to be pinned.  recordRouteThis flag indicates whether or not the signalling protocol should remember the tunnel path after it has been signaled
            	**type**\:   :py:class:`Mplstunnelsessionattributes <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunneltable.Mplstunnelentry.Mplstunnelsessionattributes>`
            
            .. attribute:: mplstunnelsetupprio
            
            	Indicates the setup priority of this tunnel
            	**type**\:  int
            
            	**range:** 0..7
            
            .. attribute:: mplstunnelsignallingproto
            
            	The signalling protocol, if any, used to setup this tunnel
            	**type**\:   :py:class:`MplstunnelsignallingprotoEnum <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunneltable.Mplstunnelentry.MplstunnelsignallingprotoEnum>`
            
            .. attribute:: mplstunnelstatetransitions
            
            	Specifies the number of times the state (mplsTunnelOperStatus) of this tunnel instance has changed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelstoragetype
            
            	The storage type for this tunnel entry. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            .. attribute:: mplstunneltotaluptime
            
            	This value represents the aggregate up time for all instances of this tunnel, if available. If this value is unavailable, it MUST return a value of 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelxcpointer
            
            	This variable points to a row in the mplsXCTable. This table identifies the segments that compose this tunnel, their characteristics, and relationships to each other. A value of zeroDotZero indicates that no LSP has been associated with this tunnel yet
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'MPLS-TE-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                self.parent = None
                self.mplstunnelindex = None
                self.mplstunnelinstance = None
                self.mplstunnelingresslsrid = None
                self.mplstunnelegresslsrid = None
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
                self.mplstunnelsessionattributes = MplsTeStdMib.Mplstunneltable.Mplstunnelentry.Mplstunnelsessionattributes()
                self.mplstunnelsetupprio = None
                self.mplstunnelsignallingproto = None
                self.mplstunnelstatetransitions = None
                self.mplstunnelstoragetype = None
                self.mplstunneltotaluptime = None
                self.mplstunnelxcpointer = None

            class MplstunneladminstatusEnum(Enum):
                """
                MplstunneladminstatusEnum

                Indicates the desired operational status of this

                tunnel.

                .. data:: up = 1

                .. data:: down = 2

                .. data:: testing = 3

                """

                up = 1

                down = 2

                testing = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _MPLS_TE_STD_MIB as meta
                    return meta._meta_table['MplsTeStdMib.Mplstunneltable.Mplstunnelentry.MplstunneladminstatusEnum']


            class MplstunneloperstatusEnum(Enum):
                """
                MplstunneloperstatusEnum

                Indicates the actual operational status of this

                tunnel, which is typically but not limited to, a

                function of the state of individual segments of

                this tunnel.

                .. data:: up = 1

                .. data:: down = 2

                .. data:: testing = 3

                .. data:: unknown = 4

                .. data:: dormant = 5

                .. data:: notPresent = 6

                .. data:: lowerLayerDown = 7

                """

                up = 1

                down = 2

                testing = 3

                unknown = 4

                dormant = 5

                notPresent = 6

                lowerLayerDown = 7


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _MPLS_TE_STD_MIB as meta
                    return meta._meta_table['MplsTeStdMib.Mplstunneltable.Mplstunnelentry.MplstunneloperstatusEnum']


            class MplstunnelroleEnum(Enum):
                """
                MplstunnelroleEnum

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

                .. data:: head = 1

                .. data:: transit = 2

                .. data:: tail = 3

                .. data:: headTail = 4

                """

                head = 1

                transit = 2

                tail = 3

                headTail = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _MPLS_TE_STD_MIB as meta
                    return meta._meta_table['MplsTeStdMib.Mplstunneltable.Mplstunnelentry.MplstunnelroleEnum']


            class MplstunnelsignallingprotoEnum(Enum):
                """
                MplstunnelsignallingprotoEnum

                The signalling protocol, if any, used to setup this

                tunnel.

                .. data:: none = 1

                .. data:: rsvp = 2

                .. data:: crldp = 3

                .. data:: other = 4

                """

                none = 1

                rsvp = 2

                crldp = 3

                other = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _MPLS_TE_STD_MIB as meta
                    return meta._meta_table['MplsTeStdMib.Mplstunneltable.Mplstunnelentry.MplstunnelsignallingprotoEnum']


            class Mplstunnelsessionattributes(FixedBitsDict):
                """
                Mplstunnelsessionattributes

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
                Keys are:- isPersistent , recordRoute , isPinned , fastReroute , mergingPermitted

                """

                def __init__(self):
                    self._dictionary = { 
                        'isPersistent':False,
                        'recordRoute':False,
                        'isPinned':False,
                        'fastReroute':False,
                        'mergingPermitted':False,
                    }
                    self._pos_map = { 
                        'isPersistent':2,
                        'recordRoute':4,
                        'isPinned':3,
                        'fastReroute':0,
                        'mergingPermitted':1,
                    }

            @property
            def _common_path(self):
                if self.mplstunnelindex is None:
                    raise YPYModelError('Key property mplstunnelindex is None')
                if self.mplstunnelinstance is None:
                    raise YPYModelError('Key property mplstunnelinstance is None')
                if self.mplstunnelingresslsrid is None:
                    raise YPYModelError('Key property mplstunnelingresslsrid is None')
                if self.mplstunnelegresslsrid is None:
                    raise YPYModelError('Key property mplstunnelegresslsrid is None')

                return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTunnelTable/MPLS-TE-STD-MIB:mplsTunnelEntry[MPLS-TE-STD-MIB:mplsTunnelIndex = ' + str(self.mplstunnelindex) + '][MPLS-TE-STD-MIB:mplsTunnelInstance = ' + str(self.mplstunnelinstance) + '][MPLS-TE-STD-MIB:mplsTunnelIngressLSRId = ' + str(self.mplstunnelingresslsrid) + '][MPLS-TE-STD-MIB:mplsTunnelEgressLSRId = ' + str(self.mplstunnelegresslsrid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mplstunnelindex is not None:
                    return True

                if self.mplstunnelinstance is not None:
                    return True

                if self.mplstunnelingresslsrid is not None:
                    return True

                if self.mplstunnelegresslsrid is not None:
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _MPLS_TE_STD_MIB as meta
                return meta._meta_table['MplsTeStdMib.Mplstunneltable.Mplstunnelentry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTunnelTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplstunnelentry is not None:
                for child_ref in self.mplstunnelentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_TE_STD_MIB as meta
            return meta._meta_table['MplsTeStdMib.Mplstunneltable']['meta_info']


    class Mplstunnelhoptable(object):
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
        	**type**\: list of    :py:class:`Mplstunnelhopentry <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelhoptable.Mplstunnelhopentry>`
        
        

        """

        _prefix = 'MPLS-TE-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplstunnelhopentry = YList()
            self.mplstunnelhopentry.parent = self
            self.mplstunnelhopentry.name = 'mplstunnelhopentry'


        class Mplstunnelhopentry(object):
            """
            An entry in this table represents a tunnel hop.  An
            entry is created by a network administrator for
            signaled ERLSP set up by an MPLS signalling
            protocol.
            
            .. attribute:: mplstunnelhoplistindex  <key>
            
            	Primary index into this table identifying a particular explicit route object
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplstunnelhoppathoptionindex  <key>
            
            	Secondary index into this table identifying a particular group of hops representing a particular configured path. This is otherwise known as a path option
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplstunnelhopindex  <key>
            
            	Tertiary index into this table identifying a particular hop
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplstunnelhopaddrtype
            
            	The Hop Address Type of this tunnel hop.  The value of this object cannot be changed if the value of the corresponding mplsTunnelHopRowStatus object is 'active'.  Note that lspid(5) is a valid option only for tunnels signaled via CRLDP
            	**type**\:   :py:class:`TehopaddresstypeEnum <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.TehopaddresstypeEnum>`
            
            .. attribute:: mplstunnelhopaddrunnum
            
            	If mplsTunnelHopAddrType is set to unnum(4), then this value will contain the interface identifier of the unnumbered interface for this hop. This object should be used in conjunction with mplsTunnelHopIpAddress which would contain the LSR Router ID in this case. Otherwise the agent should set this object to zero\-length string and the manager should ignore this
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: mplstunnelhopasnumber
            
            	If mplsTunnelHopAddrType is set to asnumber(3), then this value will contain the AS number of this hop. Otherwise the agent should set this object to zero\- length string and the manager should ignore this
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: mplstunnelhopentrypathcomp
            
            	If this value is set to dynamic, then the user should only specify the source and destination of the path and expect that the CSPF will calculate the remainder of the path.  If this value is set to explicit, the user should specify the entire path for the tunnel to take.  This path may contain strict or loose hops.  Each hop along a specific path SHOULD have this object set to the same value
            	**type**\:   :py:class:`MplstunnelhopentrypathcompEnum <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelhoptable.Mplstunnelhopentry.MplstunnelhopentrypathcompEnum>`
            
            .. attribute:: mplstunnelhopinclude
            
            	If this value is set to true, then this indicates that this hop must be included in the tunnel's path. If this value is set to 'false', then this hop must be avoided when calculating the path for this tunnel. The default value of this object is 'true', so that by default all indicated hops are included in the CSPF path computation. If this object is set to 'false' the value of mplsTunnelHopType should be ignored
            	**type**\:  bool
            
            .. attribute:: mplstunnelhopipaddr
            
            	The Tunnel Hop Address for this tunnel hop.  The type of this address is determined by the value of the corresponding mplsTunnelHopAddrType.  The value of this object cannot be changed if the value of the corresponding mplsTunnelHopRowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mplstunnelhopipprefixlen
            
            	If mplsTunnelHopAddrType is set to ipv4(1) or ipv6(2), then this value will contain an appropriate prefix length for the IP address in object mplsTunnelHopIpAddr. Otherwise this value is irrelevant and should be ignored
            	**type**\:  int
            
            	**range:** 0..2040
            
            .. attribute:: mplstunnelhoplspid
            
            	If mplsTunnelHopAddrType is set to lspid(5), then this value will contain the LSPID of a tunnel of this hop. The present tunnel being configured is tunneled through this hop (using label stacking). This object is otherwise insignificant and should contain a value of 0 to indicate this fact
            	**type**\:  str
            
            	**length:** 2 \| 6
            
            .. attribute:: mplstunnelhoppathoptionname
            
            	The description of this series of hops as they relate to the specified path option. The value of this object SHOULD be the same for each hop in the series that comprises a path option
            	**type**\:  str
            
            .. attribute:: mplstunnelhoprowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table.  When a row in this table is in active(1) state, no objects in that row can be modified by the agent except mplsTunnelHopRowStatus and mplsTunnelHopStorageType
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: mplstunnelhopstoragetype
            
            	The storage type for this Hop entry. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            .. attribute:: mplstunnelhoptype
            
            	Denotes whether this tunnel hop is routed in a strict or loose fashion. The value of this object has no meaning if the mplsTunnelHopInclude object is set to 'false'
            	**type**\:   :py:class:`MplstunnelhoptypeEnum <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelhoptable.Mplstunnelhopentry.MplstunnelhoptypeEnum>`
            
            

            """

            _prefix = 'MPLS-TE-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                self.parent = None
                self.mplstunnelhoplistindex = None
                self.mplstunnelhoppathoptionindex = None
                self.mplstunnelhopindex = None
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

            class MplstunnelhopentrypathcompEnum(Enum):
                """
                MplstunnelhopentrypathcompEnum

                If this value is set to dynamic, then the user

                should only specify the source and destination of

                the path and expect that the CSPF will calculate

                the remainder of the path.  If this value is set to

                explicit, the user should specify the entire path

                for the tunnel to take.  This path may contain

                strict or loose hops.  Each hop along a specific

                path SHOULD have this object set to the same value

                .. data:: dynamic = 1

                .. data:: explicit = 2

                """

                dynamic = 1

                explicit = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _MPLS_TE_STD_MIB as meta
                    return meta._meta_table['MplsTeStdMib.Mplstunnelhoptable.Mplstunnelhopentry.MplstunnelhopentrypathcompEnum']


            class MplstunnelhoptypeEnum(Enum):
                """
                MplstunnelhoptypeEnum

                Denotes whether this tunnel hop is routed in a

                strict or loose fashion. The value of this object

                has no meaning if the mplsTunnelHopInclude object

                is set to 'false'.

                .. data:: strict = 1

                .. data:: loose = 2

                """

                strict = 1

                loose = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _MPLS_TE_STD_MIB as meta
                    return meta._meta_table['MplsTeStdMib.Mplstunnelhoptable.Mplstunnelhopentry.MplstunnelhoptypeEnum']


            @property
            def _common_path(self):
                if self.mplstunnelhoplistindex is None:
                    raise YPYModelError('Key property mplstunnelhoplistindex is None')
                if self.mplstunnelhoppathoptionindex is None:
                    raise YPYModelError('Key property mplstunnelhoppathoptionindex is None')
                if self.mplstunnelhopindex is None:
                    raise YPYModelError('Key property mplstunnelhopindex is None')

                return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTunnelHopTable/MPLS-TE-STD-MIB:mplsTunnelHopEntry[MPLS-TE-STD-MIB:mplsTunnelHopListIndex = ' + str(self.mplstunnelhoplistindex) + '][MPLS-TE-STD-MIB:mplsTunnelHopPathOptionIndex = ' + str(self.mplstunnelhoppathoptionindex) + '][MPLS-TE-STD-MIB:mplsTunnelHopIndex = ' + str(self.mplstunnelhopindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mplstunnelhoplistindex is not None:
                    return True

                if self.mplstunnelhoppathoptionindex is not None:
                    return True

                if self.mplstunnelhopindex is not None:
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _MPLS_TE_STD_MIB as meta
                return meta._meta_table['MplsTeStdMib.Mplstunnelhoptable.Mplstunnelhopentry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTunnelHopTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplstunnelhopentry is not None:
                for child_ref in self.mplstunnelhopentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_TE_STD_MIB as meta
            return meta._meta_table['MplsTeStdMib.Mplstunnelhoptable']['meta_info']


    class Mplstunnelresourcetable(object):
        """
        The mplsTunnelResourceTable allows a manager to
        specify which resources are desired for an MPLS
        tunnel.  This table also allows several tunnels to
        point to a single entry in this table, implying
        that these tunnels should share resources.
        
        .. attribute:: mplstunnelresourceentry
        
        	An entry in this table represents a set of resources for an MPLS tunnel.  An entry can be created by a network administrator or by an SNMP agent as instructed by any MPLS signalling protocol. An entry in this table referenced by a tunnel instance with zero mplsTunnelInstance value indicates a configured set of resource parameter. An entry referenced by a tunnel instance with a non\-zero mplsTunnelInstance reflects the in\-use resource parameters for the tunnel instance which may have been negotiated or modified by the MPLS signaling protocols
        	**type**\: list of    :py:class:`Mplstunnelresourceentry <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelresourcetable.Mplstunnelresourceentry>`
        
        

        """

        _prefix = 'MPLS-TE-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplstunnelresourceentry = YList()
            self.mplstunnelresourceentry.parent = self
            self.mplstunnelresourceentry.name = 'mplstunnelresourceentry'


        class Mplstunnelresourceentry(object):
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
            
            .. attribute:: mplstunnelresourceindex  <key>
            
            	Uniquely identifies this row
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: mplstunnelresourceexburstsize
            
            	The Excess burst size in bytes.  The implementations which do not implement this variable must return noSuchObject exception for this object and must not allow a user to set this value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: mplstunnelresourcefrequency
            
            	The granularity of the availability of committed rate.  The implementations which do not implement this variable must return unspecified(1) for this value and must not allow a user to set this value
            	**type**\:   :py:class:`MplstunnelresourcefrequencyEnum <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelresourcetable.Mplstunnelresourceentry.MplstunnelresourcefrequencyEnum>`
            
            .. attribute:: mplstunnelresourcemaxburstsize
            
            	The maximum burst size in bytes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: mplstunnelresourcemaxrate
            
            	The maximum rate in bits/second.  Note that setting mplsTunnelResourceMaxRate, mplsTunnelResourceMeanRate, and mplsTunnelResourceMaxBurstSize to 0 indicates best\- effort treatment
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilobits per second
            
            .. attribute:: mplstunnelresourcemeanburstsize
            
            	The mean burst size in bytes.  The implementations which do not implement this variable must return a noSuchObject exception for this object and must not allow a user to set this object
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: mplstunnelresourcemeanrate
            
            	This object is copied into an instance of mplsTrafficParamMeanRate in the mplsTrafficParamTable. The OID of this table entry is then copied into the corresponding mplsInSegmentTrafficParamPtr
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilobits per second
            
            .. attribute:: mplstunnelresourcerowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table.  When a row in this table is in active(1) state, no objects in that row can be modified by the agent except mplsTunnelResourceRowStatus and mplsTunnelResourceStorageType
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: mplstunnelresourcestoragetype
            
            	The storage type for this Hop entry. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            .. attribute:: mplstunnelresourceweight
            
            	The relative weight for using excess bandwidth above its committed rate.  The value of 0 means that weight is not applicable for the CR\-LSP
            	**type**\:  int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'MPLS-TE-STD-MIB'
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

            class MplstunnelresourcefrequencyEnum(Enum):
                """
                MplstunnelresourcefrequencyEnum

                The granularity of the availability of committed

                rate.  The implementations which do not implement

                this variable must return unspecified(1) for this

                value and must not allow a user to set this value.

                .. data:: unspecified = 1

                .. data:: frequent = 2

                .. data:: veryFrequent = 3

                """

                unspecified = 1

                frequent = 2

                veryFrequent = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _MPLS_TE_STD_MIB as meta
                    return meta._meta_table['MplsTeStdMib.Mplstunnelresourcetable.Mplstunnelresourceentry.MplstunnelresourcefrequencyEnum']


            @property
            def _common_path(self):
                if self.mplstunnelresourceindex is None:
                    raise YPYModelError('Key property mplstunnelresourceindex is None')

                return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTunnelResourceTable/MPLS-TE-STD-MIB:mplsTunnelResourceEntry[MPLS-TE-STD-MIB:mplsTunnelResourceIndex = ' + str(self.mplstunnelresourceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _MPLS_TE_STD_MIB as meta
                return meta._meta_table['MplsTeStdMib.Mplstunnelresourcetable.Mplstunnelresourceentry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTunnelResourceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplstunnelresourceentry is not None:
                for child_ref in self.mplstunnelresourceentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_TE_STD_MIB as meta
            return meta._meta_table['MplsTeStdMib.Mplstunnelresourcetable']['meta_info']


    class Mplstunnelarhoptable(object):
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
        	**type**\: list of    :py:class:`Mplstunnelarhopentry <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelarhoptable.Mplstunnelarhopentry>`
        
        

        """

        _prefix = 'MPLS-TE-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplstunnelarhopentry = YList()
            self.mplstunnelarhopentry.parent = self
            self.mplstunnelarhopentry.name = 'mplstunnelarhopentry'


        class Mplstunnelarhopentry(object):
            """
            An entry in this table represents a tunnel hop.  An
            entry is created by the agent for signaled ERLSP
            set up by an MPLS signalling protocol.
            
            .. attribute:: mplstunnelarhoplistindex  <key>
            
            	Primary index into this table identifying a particular recorded hop list
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplstunnelarhopindex  <key>
            
            	Secondary index into this table identifying the particular hop
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplstunnelarhopaddrtype
            
            	The Hop Address Type of this tunnel hop.  Note that lspid(5) is a valid option only for tunnels signaled via CRLDP
            	**type**\:   :py:class:`TehopaddresstypeEnum <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.TehopaddresstypeEnum>`
            
            .. attribute:: mplstunnelarhopaddrunnum
            
            	If mplsTunnelARHopAddrType is set to unnum(4), then this value will contain the interface identifier of the unnumbered interface for this hop. This object should be used in conjunction with mplsTunnelARHopIpAddr which would contain the LSR Router ID in this case. Otherwise the agent should set this object to zero\-length string and the manager should ignore this
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: mplstunnelarhopipaddr
            
            	The Tunnel Hop Address for this tunnel hop.  The type of this address is determined by the value of the corresponding mplsTunnelARHopAddrType. If mplsTunnelARHopAddrType is set to unnum(4),  then this value contains the LSR Router ID of the  unnumbered interface. Otherwise the agent SHOULD  set this object to the zero\-length string and the  manager should ignore this object
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mplstunnelarhoplspid
            
            	If mplsTunnelARHopAddrType is set to lspid(5), then this value will contain the LSP ID of this hop. This object is otherwise insignificant and should contain a value of 0 to indicate this fact
            	**type**\:  str
            
            	**length:** 2 \| 6
            
            

            """

            _prefix = 'MPLS-TE-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                self.parent = None
                self.mplstunnelarhoplistindex = None
                self.mplstunnelarhopindex = None
                self.mplstunnelarhopaddrtype = None
                self.mplstunnelarhopaddrunnum = None
                self.mplstunnelarhopipaddr = None
                self.mplstunnelarhoplspid = None

            @property
            def _common_path(self):
                if self.mplstunnelarhoplistindex is None:
                    raise YPYModelError('Key property mplstunnelarhoplistindex is None')
                if self.mplstunnelarhopindex is None:
                    raise YPYModelError('Key property mplstunnelarhopindex is None')

                return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTunnelARHopTable/MPLS-TE-STD-MIB:mplsTunnelARHopEntry[MPLS-TE-STD-MIB:mplsTunnelARHopListIndex = ' + str(self.mplstunnelarhoplistindex) + '][MPLS-TE-STD-MIB:mplsTunnelARHopIndex = ' + str(self.mplstunnelarhopindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mplstunnelarhoplistindex is not None:
                    return True

                if self.mplstunnelarhopindex is not None:
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _MPLS_TE_STD_MIB as meta
                return meta._meta_table['MplsTeStdMib.Mplstunnelarhoptable.Mplstunnelarhopentry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTunnelARHopTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplstunnelarhopentry is not None:
                for child_ref in self.mplstunnelarhopentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_TE_STD_MIB as meta
            return meta._meta_table['MplsTeStdMib.Mplstunnelarhoptable']['meta_info']


    class Mplstunnelchoptable(object):
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
        	**type**\: list of    :py:class:`Mplstunnelchopentry <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelchoptable.Mplstunnelchopentry>`
        
        

        """

        _prefix = 'MPLS-TE-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplstunnelchopentry = YList()
            self.mplstunnelchopentry.parent = self
            self.mplstunnelchopentry.name = 'mplstunnelchopentry'


        class Mplstunnelchopentry(object):
            """
            An entry in this table represents a tunnel hop.  An
            entry in this table is created by a path
            computation engine using CSPF techniques applied to
            the information collected by routing protocols and
            the hops specified in the corresponding
            mplsTunnelHopTable.
            
            .. attribute:: mplstunnelchoplistindex  <key>
            
            	Primary index into this table identifying a particular computed hop list
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplstunnelchopindex  <key>
            
            	Secondary index into this table identifying the particular hop
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplstunnelchopaddrtype
            
            	The Hop Address Type of this tunnel hop.  Note that lspid(5) is a valid option only for tunnels signaled via CRLDP
            	**type**\:   :py:class:`TehopaddresstypeEnum <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.TehopaddresstypeEnum>`
            
            .. attribute:: mplstunnelchopaddrunnum
            
            	If mplsTunnelCHopAddrType is set to unnum(4), then this value will contain the unnumbered interface identifier of this hop. This object should be used in conjunction with mplsTunnelCHopIpAddr which would contain the LSR Router ID in this case. Otherwise the agent should set this object to zero\- length string and the manager should ignore this
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: mplstunnelchopasnumber
            
            	If mplsTunnelCHopAddrType is set to asnumber(3), then this value will contain the AS number of this hop. Otherwise the agent should set this object to zero\-length string and the manager should ignore this
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: mplstunnelchopipaddr
            
            	The Tunnel Hop Address for this tunnel hop. The type of this address is determined by the  value of the corresponding mplsTunnelCHopAddrType.  If mplsTunnelCHopAddrType is set to unnum(4), then  this value will contain the LSR Router ID of the  unnumbered interface. Otherwise the agent should  set this object to the zero\-length string and the  manager SHOULD ignore this object
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mplstunnelchopipprefixlen
            
            	If mplsTunnelCHopAddrType is set to ipv4(1) or ipv6(2), then this value will contain an appropriate prefix length for the IP address in object mplsTunnelCHopIpAddr. Otherwise this value is irrelevant and should be ignored
            	**type**\:  int
            
            	**range:** 0..2040
            
            .. attribute:: mplstunnelchoplspid
            
            	If mplsTunnelCHopAddrType is set to lspid(5), then this value will contain the LSP ID of this hop. This object is otherwise insignificant and should contain a value of 0 to indicate this fact
            	**type**\:  str
            
            	**length:** 2 \| 6
            
            .. attribute:: mplstunnelchoptype
            
            	Denotes whether this is tunnel hop is routed in a strict or loose fashion
            	**type**\:   :py:class:`MplstunnelchoptypeEnum <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelchoptable.Mplstunnelchopentry.MplstunnelchoptypeEnum>`
            
            

            """

            _prefix = 'MPLS-TE-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                self.parent = None
                self.mplstunnelchoplistindex = None
                self.mplstunnelchopindex = None
                self.mplstunnelchopaddrtype = None
                self.mplstunnelchopaddrunnum = None
                self.mplstunnelchopasnumber = None
                self.mplstunnelchopipaddr = None
                self.mplstunnelchopipprefixlen = None
                self.mplstunnelchoplspid = None
                self.mplstunnelchoptype = None

            class MplstunnelchoptypeEnum(Enum):
                """
                MplstunnelchoptypeEnum

                Denotes whether this is tunnel hop is routed in a

                strict or loose fashion.

                .. data:: strict = 1

                .. data:: loose = 2

                """

                strict = 1

                loose = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _MPLS_TE_STD_MIB as meta
                    return meta._meta_table['MplsTeStdMib.Mplstunnelchoptable.Mplstunnelchopentry.MplstunnelchoptypeEnum']


            @property
            def _common_path(self):
                if self.mplstunnelchoplistindex is None:
                    raise YPYModelError('Key property mplstunnelchoplistindex is None')
                if self.mplstunnelchopindex is None:
                    raise YPYModelError('Key property mplstunnelchopindex is None')

                return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTunnelCHopTable/MPLS-TE-STD-MIB:mplsTunnelCHopEntry[MPLS-TE-STD-MIB:mplsTunnelCHopListIndex = ' + str(self.mplstunnelchoplistindex) + '][MPLS-TE-STD-MIB:mplsTunnelCHopIndex = ' + str(self.mplstunnelchopindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mplstunnelchoplistindex is not None:
                    return True

                if self.mplstunnelchopindex is not None:
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _MPLS_TE_STD_MIB as meta
                return meta._meta_table['MplsTeStdMib.Mplstunnelchoptable.Mplstunnelchopentry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTunnelCHopTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplstunnelchopentry is not None:
                for child_ref in self.mplstunnelchopentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_TE_STD_MIB as meta
            return meta._meta_table['MplsTeStdMib.Mplstunnelchoptable']['meta_info']


    class Mplstunnelcrldprestable(object):
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
        	**type**\: list of    :py:class:`Mplstunnelcrldpresentry <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelcrldprestable.Mplstunnelcrldpresentry>`
        
        

        """

        _prefix = 'MPLS-TE-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            self.parent = None
            self.mplstunnelcrldpresentry = YList()
            self.mplstunnelcrldpresentry.parent = self
            self.mplstunnelcrldpresentry.name = 'mplstunnelcrldpresentry'


        class Mplstunnelcrldpresentry(object):
            """
            An entry in this table represents a set of resources
            for an MPLS tunnel established using CRLDP
            (mplsTunnelSignallingProto equal to crldp (3)). An
            entry can be created by a network administrator or
            by an SNMP agent as instructed by any MPLS
            signalling protocol.
            
            .. attribute:: mplstunnelresourceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`mplstunnelresourceindex <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelresourcetable.Mplstunnelresourceentry>`
            
            .. attribute:: mplstunnelcrldpresexburstsize
            
            	The Excess burst size in bytes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: mplstunnelcrldpresflags
            
            	The value of the 1 byte Flags conveyed as part of the traffic parameters during the establishment of the CRLSP. The bits in this object are to be interpreted as follows.  +\-\-+\-\-+\-\-+\-\-+\-\-+\-\-+\-\-+\-\-+ \| Res \|F6\|F5\|F4\|F3\|F2\|F1\| +\-\-+\-\-+\-\-+\-\-+\-\-+\-\-+\-\-+\-\-+  Res \- These bits are reserved. Zero on transmission. Ignored on receipt. F1 \- Corresponds to the PDR. F2 \- Corresponds to the PBS. F3 \- Corresponds to the CDR. F4 \- Corresponds to the CBS. F5 \- Corresponds to the EBS. F6 \- Corresponds to the Weight.  Each flag if is a Negotiable Flag corresponding to a Traffic Parameter. The Negotiable Flag value zero denotes Not Negotiable and value one denotes Negotiable
            	**type**\:  int
            
            	**range:** 0..63
            
            .. attribute:: mplstunnelcrldpresfrequency
            
            	The granularity of the availability of committed rate
            	**type**\:   :py:class:`MplstunnelcrldpresfrequencyEnum <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelcrldprestable.Mplstunnelcrldpresentry.MplstunnelcrldpresfrequencyEnum>`
            
            .. attribute:: mplstunnelcrldpresmeanburstsize
            
            	The mean burst size in bytes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: mplstunnelcrldpresrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table.  When a row in this table is in active(1) state, no objects in that row can be modified by the agent except mplsTunnelCRLDPResRowStatus and mplsTunnelCRLDPResStorageType
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: mplstunnelcrldpresstoragetype
            
            	The storage type for this CR\-LDP Resource entry. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            .. attribute:: mplstunnelcrldpresweight
            
            	The relative weight for using excess bandwidth above its committed rate.  The value of 0 means that weight is not applicable for the CR\-LSP
            	**type**\:  int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'MPLS-TE-STD-MIB'
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

            class MplstunnelcrldpresfrequencyEnum(Enum):
                """
                MplstunnelcrldpresfrequencyEnum

                The granularity of the availability of committed

                rate.

                .. data:: unspecified = 1

                .. data:: frequent = 2

                .. data:: veryFrequent = 3

                """

                unspecified = 1

                frequent = 2

                veryFrequent = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _MPLS_TE_STD_MIB as meta
                    return meta._meta_table['MplsTeStdMib.Mplstunnelcrldprestable.Mplstunnelcrldpresentry.MplstunnelcrldpresfrequencyEnum']


            @property
            def _common_path(self):
                if self.mplstunnelresourceindex is None:
                    raise YPYModelError('Key property mplstunnelresourceindex is None')

                return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTunnelCRLDPResTable/MPLS-TE-STD-MIB:mplsTunnelCRLDPResEntry[MPLS-TE-STD-MIB:mplsTunnelResourceIndex = ' + str(self.mplstunnelresourceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _MPLS_TE_STD_MIB as meta
                return meta._meta_table['MplsTeStdMib.Mplstunnelcrldprestable.Mplstunnelcrldpresentry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/MPLS-TE-STD-MIB:mplsTunnelCRLDPResTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplstunnelcrldpresentry is not None:
                for child_ref in self.mplstunnelcrldpresentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_TE_STD_MIB as meta
            return meta._meta_table['MplsTeStdMib.Mplstunnelcrldprestable']['meta_info']

    @property
    def _common_path(self):

        return '/MPLS-TE-STD-MIB:MPLS-TE-STD-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.mplsteobjects is not None and self.mplsteobjects._has_data():
            return True

        if self.mplstescalars is not None and self.mplstescalars._has_data():
            return True

        if self.mplstunnelarhoptable is not None and self.mplstunnelarhoptable._has_data():
            return True

        if self.mplstunnelchoptable is not None and self.mplstunnelchoptable._has_data():
            return True

        if self.mplstunnelcrldprestable is not None and self.mplstunnelcrldprestable._has_data():
            return True

        if self.mplstunnelhoptable is not None and self.mplstunnelhoptable._has_data():
            return True

        if self.mplstunnelresourcetable is not None and self.mplstunnelresourcetable._has_data():
            return True

        if self.mplstunneltable is not None and self.mplstunneltable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _MPLS_TE_STD_MIB as meta
        return meta._meta_table['MplsTeStdMib']['meta_info']



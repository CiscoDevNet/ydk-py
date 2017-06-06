""" MPLS_VPN_MIB 

This MIB contains managed object definitions for the
Multiprotocol Label Switching (MPLS)/Border Gateway


Protocol (BGP) Virtual Private Networks (VPNs) as
defined in \: Rosen, E., Viswanathan, A., and R.
Callon, Multiprotocol Label Switching Architecture,
RFC3031, January 2001.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class MplsVpnMib(object):
    """
    
    
    .. attribute:: mplsvpninterfaceconftable
    
    	This table specifies per\-interface MPLS capability and associated information
    	**type**\:   :py:class:`Mplsvpninterfaceconftable <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpninterfaceconftable>`
    
    .. attribute:: mplsvpnscalars
    
    	
    	**type**\:   :py:class:`Mplsvpnscalars <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnscalars>`
    
    .. attribute:: mplsvpnvrfbgpnbraddrtable
    
    	Each entry in this table specifies a per\-interface  MPLS/EBGP neighbor
    	**type**\:   :py:class:`Mplsvpnvrfbgpnbraddrtable <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfbgpnbraddrtable>`
    
    .. attribute:: mplsvpnvrfbgpnbrprefixtable
    
    	This table specifies per\-VRF vpnv4 multi\-protocol prefixes supported by BGP
    	**type**\:   :py:class:`Mplsvpnvrfbgpnbrprefixtable <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable>`
    
    .. attribute:: mplsvpnvrfroutetable
    
    	This table specifies per\-interface MPLS/BGP VPN VRF Table routing information. Entries in this table define VRF routing entries associated with the specified MPLS/VPN interfaces. Note that this table contains both BGP and IGP routes, as both may appear in the same VRF
    	**type**\:   :py:class:`Mplsvpnvrfroutetable <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfroutetable>`
    
    .. attribute:: mplsvpnvrfroutetargettable
    
    	This table specifies per\-VRF route target association. Each entry identifies a connectivity policy supported as part of a VPN
    	**type**\:   :py:class:`Mplsvpnvrfroutetargettable <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfroutetargettable>`
    
    .. attribute:: mplsvpnvrftable
    
    	This table specifies per\-interface MPLS/BGP VPN VRF Table capability and associated information. Entries in this table define VRF routing instances associated with MPLS/VPN interfaces. Note that multiple interfaces can belong to the same VRF instance. The collection of all VRF instances comprises an actual VPN
    	**type**\:   :py:class:`Mplsvpnvrftable <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrftable>`
    
    

    """

    _prefix = 'MPLS-VPN-MIB'
    _revision = '2001-10-15'

    def __init__(self):
        self.mplsvpninterfaceconftable = MplsVpnMib.Mplsvpninterfaceconftable()
        self.mplsvpninterfaceconftable.parent = self
        self.mplsvpnscalars = MplsVpnMib.Mplsvpnscalars()
        self.mplsvpnscalars.parent = self
        self.mplsvpnvrfbgpnbraddrtable = MplsVpnMib.Mplsvpnvrfbgpnbraddrtable()
        self.mplsvpnvrfbgpnbraddrtable.parent = self
        self.mplsvpnvrfbgpnbrprefixtable = MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable()
        self.mplsvpnvrfbgpnbrprefixtable.parent = self
        self.mplsvpnvrfroutetable = MplsVpnMib.Mplsvpnvrfroutetable()
        self.mplsvpnvrfroutetable.parent = self
        self.mplsvpnvrfroutetargettable = MplsVpnMib.Mplsvpnvrfroutetargettable()
        self.mplsvpnvrfroutetargettable.parent = self
        self.mplsvpnvrftable = MplsVpnMib.Mplsvpnvrftable()
        self.mplsvpnvrftable.parent = self


    class Mplsvpnscalars(object):
        """
        
        
        .. attribute:: mplsvpnactivevrfs
        
        	The number of VRFs which are active on this node. That is, those VRFs whose corresponding mplsVpnVrfOperStatus  object value is equal to operational (1)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplsvpnconfiguredvrfs
        
        	The number of VRFs which are configured on this node
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplsvpnconnectedinterfaces
        
        	Total number of interfaces connected to a VRF
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplsvpnnotificationenable
        
        	If this object is true, then it enables the generation of all notifications defined in  this MIB
        	**type**\:  bool
        
        .. attribute:: mplsvpnvrfconfmaxpossibleroutes
        
        	Denotes maximum number of routes which the device will allow all VRFs jointly to hold. If this value is set to 0, this indicates that the device is  unable to determine the absolute maximum. In this case, the configured maximum MAY not actually be allowed by the device
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'MPLS-VPN-MIB'
        _revision = '2001-10-15'

        def __init__(self):
            self.parent = None
            self.mplsvpnactivevrfs = None
            self.mplsvpnconfiguredvrfs = None
            self.mplsvpnconnectedinterfaces = None
            self.mplsvpnnotificationenable = None
            self.mplsvpnvrfconfmaxpossibleroutes = None

        @property
        def _common_path(self):

            return '/MPLS-VPN-MIB:MPLS-VPN-MIB/MPLS-VPN-MIB:mplsVpnScalars'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplsvpnactivevrfs is not None:
                return True

            if self.mplsvpnconfiguredvrfs is not None:
                return True

            if self.mplsvpnconnectedinterfaces is not None:
                return True

            if self.mplsvpnnotificationenable is not None:
                return True

            if self.mplsvpnvrfconfmaxpossibleroutes is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_VPN_MIB as meta
            return meta._meta_table['MplsVpnMib.Mplsvpnscalars']['meta_info']


    class Mplsvpninterfaceconftable(object):
        """
        This table specifies per\-interface MPLS capability
        and associated information.
        
        .. attribute:: mplsvpninterfaceconfentry
        
        	An entry in this table is created by an LSR for every interface capable of supporting MPLS/BGP VPN.   Each entry in this table is meant to correspond to an entry in the Interfaces Table
        	**type**\: list of    :py:class:`Mplsvpninterfaceconfentry <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry>`
        
        

        """

        _prefix = 'MPLS-VPN-MIB'
        _revision = '2001-10-15'

        def __init__(self):
            self.parent = None
            self.mplsvpninterfaceconfentry = YList()
            self.mplsvpninterfaceconfentry.parent = self
            self.mplsvpninterfaceconfentry.name = 'mplsvpninterfaceconfentry'


        class Mplsvpninterfaceconfentry(object):
            """
            An entry in this table is created by an LSR for
            every interface capable of supporting MPLS/BGP VPN.
            
            
            Each entry in this table is meant to correspond to
            an entry in the Interfaces Table.
            
            .. attribute:: mplsvpnvrfname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..31
            
            	**refers to**\:  :py:class:`mplsvpnvrfname <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry>`
            
            .. attribute:: mplsvpninterfaceconfindex  <key>
            
            	This is a unique index for an entry in the MplsVPNInterfaceConfTable. A non\-zero index for an entry indicates the ifIndex for the corresponding interface entry in the MPLS\-VPN\-layer in the ifTable. Note that this table does not necessarily correspond one\-to\-one with all entries in the Interface MIB having an ifType of MPLS\-layer; rather, only those which are enabled for MPLS/BGP VPN functionality
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: mplsvpninterfaceconfrowstatus
            
            	The row status for this entry. This value is used to create a row in this table, signifying that the specified interface is to be associated with the specified interface. If this operation succeeds, the interface will have been associated, otherwise the agent would not allow the association.  If the agent only allows read\-only operations on this table, it will create entries in this table as they are created
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: mplsvpninterfaceconfstoragetype
            
            	The storage type for this entry
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            .. attribute:: mplsvpninterfacelabeledgetype
            
            	Either the providerEdge(0) (PE) or customerEdge(1) (CE) bit MUST be set
            	**type**\:   :py:class:`MplsvpninterfacelabeledgetypeEnum <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry.MplsvpninterfacelabeledgetypeEnum>`
            
            .. attribute:: mplsvpninterfacevpnclassification
            
            	Denotes whether this link participates in a carrier\-of\-carrier's, enterprise, or inter\-provider scenario
            	**type**\:   :py:class:`MplsvpninterfacevpnclassificationEnum <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry.MplsvpninterfacevpnclassificationEnum>`
            
            .. attribute:: mplsvpninterfacevpnroutedistprotocol
            
            	Denotes the route distribution protocol across the PE\-CE link. Note that more than one routing protocol may be enabled at the same time
            	**type**\:   :py:class:`Mplsvpninterfacevpnroutedistprotocol <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry.Mplsvpninterfacevpnroutedistprotocol>`
            
            

            """

            _prefix = 'MPLS-VPN-MIB'
            _revision = '2001-10-15'

            def __init__(self):
                self.parent = None
                self.mplsvpnvrfname = None
                self.mplsvpninterfaceconfindex = None
                self.mplsvpninterfaceconfrowstatus = None
                self.mplsvpninterfaceconfstoragetype = None
                self.mplsvpninterfacelabeledgetype = None
                self.mplsvpninterfacevpnclassification = None
                self.mplsvpninterfacevpnroutedistprotocol = MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry.Mplsvpninterfacevpnroutedistprotocol()

            class MplsvpninterfacelabeledgetypeEnum(Enum):
                """
                MplsvpninterfacelabeledgetypeEnum

                Either the providerEdge(0) (PE) or customerEdge(1)

                (CE) bit MUST be set.

                .. data:: providerEdge = 1

                .. data:: customerEdge = 2

                """

                providerEdge = 1

                customerEdge = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _MPLS_VPN_MIB as meta
                    return meta._meta_table['MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry.MplsvpninterfacelabeledgetypeEnum']


            class MplsvpninterfacevpnclassificationEnum(Enum):
                """
                MplsvpninterfacevpnclassificationEnum

                Denotes whether this link participates in a

                carrier\-of\-carrier's, enterprise, or inter\-provider

                scenario.

                .. data:: carrierOfCarrier = 1

                .. data:: enterprise = 2

                .. data:: interProvider = 3

                """

                carrierOfCarrier = 1

                enterprise = 2

                interProvider = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _MPLS_VPN_MIB as meta
                    return meta._meta_table['MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry.MplsvpninterfacevpnclassificationEnum']


            class Mplsvpninterfacevpnroutedistprotocol(FixedBitsDict):
                """
                Mplsvpninterfacevpnroutedistprotocol

                Denotes the route distribution protocol across the
                PE\-CE link. Note that more than one routing protocol
                may be enabled at the same time.
                Keys are:- rip , isis , none , other , bgp , dummy , ospf

                """

                def __init__(self):
                    self._dictionary = { 
                        'rip':False,
                        'isis':False,
                        'none':False,
                        'other':False,
                        'bgp':False,
                        'dummy':False,
                        'ospf':False,
                    }
                    self._pos_map = { 
                        'rip':4,
                        'isis':5,
                        'none':1,
                        'other':6,
                        'bgp':2,
                        'dummy':0,
                        'ospf':3,
                    }

            @property
            def _common_path(self):
                if self.mplsvpnvrfname is None:
                    raise YPYModelError('Key property mplsvpnvrfname is None')
                if self.mplsvpninterfaceconfindex is None:
                    raise YPYModelError('Key property mplsvpninterfaceconfindex is None')

                return '/MPLS-VPN-MIB:MPLS-VPN-MIB/MPLS-VPN-MIB:mplsVpnInterfaceConfTable/MPLS-VPN-MIB:mplsVpnInterfaceConfEntry[MPLS-VPN-MIB:mplsVpnVrfName = ' + str(self.mplsvpnvrfname) + '][MPLS-VPN-MIB:mplsVpnInterfaceConfIndex = ' + str(self.mplsvpninterfaceconfindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mplsvpnvrfname is not None:
                    return True

                if self.mplsvpninterfaceconfindex is not None:
                    return True

                if self.mplsvpninterfaceconfrowstatus is not None:
                    return True

                if self.mplsvpninterfaceconfstoragetype is not None:
                    return True

                if self.mplsvpninterfacelabeledgetype is not None:
                    return True

                if self.mplsvpninterfacevpnclassification is not None:
                    return True

                if self.mplsvpninterfacevpnroutedistprotocol is not None:
                    if self.mplsvpninterfacevpnroutedistprotocol._has_data():
                        return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _MPLS_VPN_MIB as meta
                return meta._meta_table['MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-VPN-MIB:MPLS-VPN-MIB/MPLS-VPN-MIB:mplsVpnInterfaceConfTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplsvpninterfaceconfentry is not None:
                for child_ref in self.mplsvpninterfaceconfentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_VPN_MIB as meta
            return meta._meta_table['MplsVpnMib.Mplsvpninterfaceconftable']['meta_info']


    class Mplsvpnvrftable(object):
        """
        This table specifies per\-interface MPLS/BGP VPN
        VRF Table capability and associated information.
        Entries in this table define VRF routing instances
        associated with MPLS/VPN interfaces. Note that
        multiple interfaces can belong to the same VRF
        instance. The collection of all VRF instances
        comprises an actual VPN.
        
        .. attribute:: mplsvpnvrfentry
        
        	An entry in this table is created by an LSR for every VRF capable of supporting MPLS/BGP VPN. The indexing provides an ordering of VRFs per\-VPN interface
        	**type**\: list of    :py:class:`Mplsvpnvrfentry <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry>`
        
        

        """

        _prefix = 'MPLS-VPN-MIB'
        _revision = '2001-10-15'

        def __init__(self):
            self.parent = None
            self.mplsvpnvrfentry = YList()
            self.mplsvpnvrfentry.parent = self
            self.mplsvpnvrfentry.name = 'mplsvpnvrfentry'


        class Mplsvpnvrfentry(object):
            """
            An entry in this table is created by an LSR for
            every VRF capable of supporting MPLS/BGP VPN. The
            indexing provides an ordering of VRFs per\-VPN
            interface.
            
            .. attribute:: mplsvpnvrfname  <key>
            
            	The human\-readable name of this VPN. This MAY be equivalent to the RFC2685 VPN\-ID
            	**type**\:  str
            
            	**length:** 0..31
            
            .. attribute:: mplsvpnvrfactiveinterfaces
            
            	Total number of interfaces connected to this VRF with    ifOperStatus = up(1).   This counter should be incremented when\:  a. When the ifOperStatus of one of the connected interfaces     changes from down(2) to up(1).  b. When an interface with ifOperStatus = up(1) is connected    to this VRF.  This counter should be decremented when\:  a. When the ifOperStatus of one of the connected interfaces     changes from up(1) to down(2).  b. When one of the connected interfaces with     ifOperStatus = up(1) gets disconnected from this VRF
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfassociatedinterfaces
            
            	Total number of interfaces connected to this VRF  (independent of ifOperStatus type)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfconfhighroutethreshold
            
            	Denotes high\-level water marker for the number of routes which  this VRF may hold
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfconflastchanged
            
            	The value of sysUpTime at the time of the last change of this table entry, which includes changes of VRF parameters defined in this table or addition or deletion of interfaces associated with this VRF
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfconfmaxroutes
            
            	Denotes maximum number of routes which this VRF is configured to hold. This value MUST be less than or equal to mplsVrfMaxPossibleRoutes unless it is set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfconfmidroutethreshold
            
            	Denotes mid\-level water marker for the number of routes which  this VRF may hold
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfconfrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: mplsvpnvrfconfstoragetype
            
            	The storage type for this entry
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            .. attribute:: mplsvpnvrfcreationtime
            
            	The time at which this VRF entry was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfdescription
            
            	The human\-readable description of this VRF
            	**type**\:  str
            
            .. attribute:: mplsvpnvrfoperstatus
            
            	Denotes whether a VRF is operational or not. A VRF is  up(1) when at least one interface associated with the VRF, which ifOperStatus is up(1). A VRF is down(2) when\:  a. There does not exist at least one interface whose    ifOperStatus is up(1).  b. There are no interfaces associated with the VRF
            	**type**\:   :py:class:`MplsvpnvrfoperstatusEnum <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry.MplsvpnvrfoperstatusEnum>`
            
            .. attribute:: mplsvpnvrfperfcurrnumroutes
            
            	Indicates the number of routes currently used by this VRF
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfperfroutesadded
            
            	Indicates the number of routes added to this VPN/VRF over the coarse of its lifetime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfperfroutesdeleted
            
            	Indicates the number of routes removed from this VPN/VRF
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfroutedistinguisher
            
            	The route distinguisher for this VRF
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: mplsvpnvrfsecillegallabelrcvthresh
            
            	The number of illegally received labels above which this  notification is issued
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfsecillegallabelviolations
            
            	Indicates the number of illegally received labels on this VPN/VRF
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'MPLS-VPN-MIB'
            _revision = '2001-10-15'

            def __init__(self):
                self.parent = None
                self.mplsvpnvrfname = None
                self.mplsvpnvrfactiveinterfaces = None
                self.mplsvpnvrfassociatedinterfaces = None
                self.mplsvpnvrfconfhighroutethreshold = None
                self.mplsvpnvrfconflastchanged = None
                self.mplsvpnvrfconfmaxroutes = None
                self.mplsvpnvrfconfmidroutethreshold = None
                self.mplsvpnvrfconfrowstatus = None
                self.mplsvpnvrfconfstoragetype = None
                self.mplsvpnvrfcreationtime = None
                self.mplsvpnvrfdescription = None
                self.mplsvpnvrfoperstatus = None
                self.mplsvpnvrfperfcurrnumroutes = None
                self.mplsvpnvrfperfroutesadded = None
                self.mplsvpnvrfperfroutesdeleted = None
                self.mplsvpnvrfroutedistinguisher = None
                self.mplsvpnvrfsecillegallabelrcvthresh = None
                self.mplsvpnvrfsecillegallabelviolations = None

            class MplsvpnvrfoperstatusEnum(Enum):
                """
                MplsvpnvrfoperstatusEnum

                Denotes whether a VRF is operational or not. A VRF is 

                up(1) when at least one interface associated with the

                VRF, which ifOperStatus is up(1). A VRF is down(2) when\:

                a. There does not exist at least one interface whose

                   ifOperStatus is up(1).

                b. There are no interfaces associated with the VRF.

                .. data:: up = 1

                .. data:: down = 2

                """

                up = 1

                down = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _MPLS_VPN_MIB as meta
                    return meta._meta_table['MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry.MplsvpnvrfoperstatusEnum']


            @property
            def _common_path(self):
                if self.mplsvpnvrfname is None:
                    raise YPYModelError('Key property mplsvpnvrfname is None')

                return '/MPLS-VPN-MIB:MPLS-VPN-MIB/MPLS-VPN-MIB:mplsVpnVrfTable/MPLS-VPN-MIB:mplsVpnVrfEntry[MPLS-VPN-MIB:mplsVpnVrfName = ' + str(self.mplsvpnvrfname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mplsvpnvrfname is not None:
                    return True

                if self.mplsvpnvrfactiveinterfaces is not None:
                    return True

                if self.mplsvpnvrfassociatedinterfaces is not None:
                    return True

                if self.mplsvpnvrfconfhighroutethreshold is not None:
                    return True

                if self.mplsvpnvrfconflastchanged is not None:
                    return True

                if self.mplsvpnvrfconfmaxroutes is not None:
                    return True

                if self.mplsvpnvrfconfmidroutethreshold is not None:
                    return True

                if self.mplsvpnvrfconfrowstatus is not None:
                    return True

                if self.mplsvpnvrfconfstoragetype is not None:
                    return True

                if self.mplsvpnvrfcreationtime is not None:
                    return True

                if self.mplsvpnvrfdescription is not None:
                    return True

                if self.mplsvpnvrfoperstatus is not None:
                    return True

                if self.mplsvpnvrfperfcurrnumroutes is not None:
                    return True

                if self.mplsvpnvrfperfroutesadded is not None:
                    return True

                if self.mplsvpnvrfperfroutesdeleted is not None:
                    return True

                if self.mplsvpnvrfroutedistinguisher is not None:
                    return True

                if self.mplsvpnvrfsecillegallabelrcvthresh is not None:
                    return True

                if self.mplsvpnvrfsecillegallabelviolations is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _MPLS_VPN_MIB as meta
                return meta._meta_table['MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-VPN-MIB:MPLS-VPN-MIB/MPLS-VPN-MIB:mplsVpnVrfTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplsvpnvrfentry is not None:
                for child_ref in self.mplsvpnvrfentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_VPN_MIB as meta
            return meta._meta_table['MplsVpnMib.Mplsvpnvrftable']['meta_info']


    class Mplsvpnvrfroutetargettable(object):
        """
        This table specifies per\-VRF route target association.
        Each entry identifies a connectivity policy supported
        as part of a VPN.
        
        .. attribute:: mplsvpnvrfroutetargetentry
        
        	 An entry in this table is created by an LSR for each route target configured for a VRF supporting a MPLS/BGP VPN instance. The indexing provides an ordering per\-VRF instance
        	**type**\: list of    :py:class:`Mplsvpnvrfroutetargetentry <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfroutetargettable.Mplsvpnvrfroutetargetentry>`
        
        

        """

        _prefix = 'MPLS-VPN-MIB'
        _revision = '2001-10-15'

        def __init__(self):
            self.parent = None
            self.mplsvpnvrfroutetargetentry = YList()
            self.mplsvpnvrfroutetargetentry.parent = self
            self.mplsvpnvrfroutetargetentry.name = 'mplsvpnvrfroutetargetentry'


        class Mplsvpnvrfroutetargetentry(object):
            """
             An entry in this table is created by an LSR for
            each route target configured for a VRF supporting
            a MPLS/BGP VPN instance. The indexing provides an
            ordering per\-VRF instance.
            
            .. attribute:: mplsvpnvrfname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..31
            
            	**refers to**\:  :py:class:`mplsvpnvrfname <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry>`
            
            .. attribute:: mplsvpnvrfroutetargetindex  <key>
            
            	Auxiliary index for route\-targets configured for a  particular VRF
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfroutetargettype  <key>
            
            	The route target export distribution type
            	**type**\:   :py:class:`MplsvpnvrfroutetargettypeEnum <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfroutetargettable.Mplsvpnvrfroutetargetentry.MplsvpnvrfroutetargettypeEnum>`
            
            .. attribute:: mplsvpnvrfroutetarget
            
            	The route target distribution policy
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: mplsvpnvrfroutetargetdescr
            
            	Description of the route target
            	**type**\:  str
            
            .. attribute:: mplsvpnvrfroutetargetrowstatus
            
            	Row status for this entry
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            

            """

            _prefix = 'MPLS-VPN-MIB'
            _revision = '2001-10-15'

            def __init__(self):
                self.parent = None
                self.mplsvpnvrfname = None
                self.mplsvpnvrfroutetargetindex = None
                self.mplsvpnvrfroutetargettype = None
                self.mplsvpnvrfroutetarget = None
                self.mplsvpnvrfroutetargetdescr = None
                self.mplsvpnvrfroutetargetrowstatus = None

            class MplsvpnvrfroutetargettypeEnum(Enum):
                """
                MplsvpnvrfroutetargettypeEnum

                The route target export distribution type.

                .. data:: import_ = 1

                .. data:: export = 2

                .. data:: both = 3

                """

                import_ = 1

                export = 2

                both = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _MPLS_VPN_MIB as meta
                    return meta._meta_table['MplsVpnMib.Mplsvpnvrfroutetargettable.Mplsvpnvrfroutetargetentry.MplsvpnvrfroutetargettypeEnum']


            @property
            def _common_path(self):
                if self.mplsvpnvrfname is None:
                    raise YPYModelError('Key property mplsvpnvrfname is None')
                if self.mplsvpnvrfroutetargetindex is None:
                    raise YPYModelError('Key property mplsvpnvrfroutetargetindex is None')
                if self.mplsvpnvrfroutetargettype is None:
                    raise YPYModelError('Key property mplsvpnvrfroutetargettype is None')

                return '/MPLS-VPN-MIB:MPLS-VPN-MIB/MPLS-VPN-MIB:mplsVpnVrfRouteTargetTable/MPLS-VPN-MIB:mplsVpnVrfRouteTargetEntry[MPLS-VPN-MIB:mplsVpnVrfName = ' + str(self.mplsvpnvrfname) + '][MPLS-VPN-MIB:mplsVpnVrfRouteTargetIndex = ' + str(self.mplsvpnvrfroutetargetindex) + '][MPLS-VPN-MIB:mplsVpnVrfRouteTargetType = ' + str(self.mplsvpnvrfroutetargettype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mplsvpnvrfname is not None:
                    return True

                if self.mplsvpnvrfroutetargetindex is not None:
                    return True

                if self.mplsvpnvrfroutetargettype is not None:
                    return True

                if self.mplsvpnvrfroutetarget is not None:
                    return True

                if self.mplsvpnvrfroutetargetdescr is not None:
                    return True

                if self.mplsvpnvrfroutetargetrowstatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _MPLS_VPN_MIB as meta
                return meta._meta_table['MplsVpnMib.Mplsvpnvrfroutetargettable.Mplsvpnvrfroutetargetentry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-VPN-MIB:MPLS-VPN-MIB/MPLS-VPN-MIB:mplsVpnVrfRouteTargetTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplsvpnvrfroutetargetentry is not None:
                for child_ref in self.mplsvpnvrfroutetargetentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_VPN_MIB as meta
            return meta._meta_table['MplsVpnMib.Mplsvpnvrfroutetargettable']['meta_info']


    class Mplsvpnvrfbgpnbraddrtable(object):
        """
        Each entry in this table specifies a per\-interface 
        MPLS/EBGP neighbor.
        
        .. attribute:: mplsvpnvrfbgpnbraddrentry
        
        	An entry in this table is created by an LSR for every VRF capable of supporting MPLS/BGP VPN. The indexing provides an ordering of VRFs per\-VPN interface
        	**type**\: list of    :py:class:`Mplsvpnvrfbgpnbraddrentry <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfbgpnbraddrtable.Mplsvpnvrfbgpnbraddrentry>`
        
        

        """

        _prefix = 'MPLS-VPN-MIB'
        _revision = '2001-10-15'

        def __init__(self):
            self.parent = None
            self.mplsvpnvrfbgpnbraddrentry = YList()
            self.mplsvpnvrfbgpnbraddrentry.parent = self
            self.mplsvpnvrfbgpnbraddrentry.name = 'mplsvpnvrfbgpnbraddrentry'


        class Mplsvpnvrfbgpnbraddrentry(object):
            """
            An entry in this table is created by an LSR for
            every VRF capable of supporting MPLS/BGP VPN. The
            indexing provides an ordering of VRFs per\-VPN
            interface.
            
            .. attribute:: mplsvpnvrfname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..31
            
            	**refers to**\:  :py:class:`mplsvpnvrfname <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry>`
            
            .. attribute:: mplsvpninterfaceconfindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`mplsvpninterfaceconfindex <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry>`
            
            .. attribute:: mplsvpnvrfbgpnbrindex  <key>
            
            	This is a unique tertiary index for an entry in the MplsVpnVrfBgpNbrAddrEntry Table
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfbgpnbraddr
            
            	Denotes the EBGP neighbor address
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsvpnvrfbgpnbrrole
            
            	Denotes the role played by this EBGP neighbor with respect to this VRF
            	**type**\:   :py:class:`MplsvpnvrfbgpnbrroleEnum <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfbgpnbraddrtable.Mplsvpnvrfbgpnbraddrentry.MplsvpnvrfbgpnbrroleEnum>`
            
            .. attribute:: mplsvpnvrfbgpnbrrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: mplsvpnvrfbgpnbrstoragetype
            
            	The storage type for this entry
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            .. attribute:: mplsvpnvrfbgpnbrtype
            
            	Denotes the address family of the PE address
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            

            """

            _prefix = 'MPLS-VPN-MIB'
            _revision = '2001-10-15'

            def __init__(self):
                self.parent = None
                self.mplsvpnvrfname = None
                self.mplsvpninterfaceconfindex = None
                self.mplsvpnvrfbgpnbrindex = None
                self.mplsvpnvrfbgpnbraddr = None
                self.mplsvpnvrfbgpnbrrole = None
                self.mplsvpnvrfbgpnbrrowstatus = None
                self.mplsvpnvrfbgpnbrstoragetype = None
                self.mplsvpnvrfbgpnbrtype = None

            class MplsvpnvrfbgpnbrroleEnum(Enum):
                """
                MplsvpnvrfbgpnbrroleEnum

                Denotes the role played by this EBGP neighbor

                with respect to this VRF.

                .. data:: ce = 1

                .. data:: pe = 2

                """

                ce = 1

                pe = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _MPLS_VPN_MIB as meta
                    return meta._meta_table['MplsVpnMib.Mplsvpnvrfbgpnbraddrtable.Mplsvpnvrfbgpnbraddrentry.MplsvpnvrfbgpnbrroleEnum']


            @property
            def _common_path(self):
                if self.mplsvpnvrfname is None:
                    raise YPYModelError('Key property mplsvpnvrfname is None')
                if self.mplsvpninterfaceconfindex is None:
                    raise YPYModelError('Key property mplsvpninterfaceconfindex is None')
                if self.mplsvpnvrfbgpnbrindex is None:
                    raise YPYModelError('Key property mplsvpnvrfbgpnbrindex is None')

                return '/MPLS-VPN-MIB:MPLS-VPN-MIB/MPLS-VPN-MIB:mplsVpnVrfBgpNbrAddrTable/MPLS-VPN-MIB:mplsVpnVrfBgpNbrAddrEntry[MPLS-VPN-MIB:mplsVpnVrfName = ' + str(self.mplsvpnvrfname) + '][MPLS-VPN-MIB:mplsVpnInterfaceConfIndex = ' + str(self.mplsvpninterfaceconfindex) + '][MPLS-VPN-MIB:mplsVpnVrfBgpNbrIndex = ' + str(self.mplsvpnvrfbgpnbrindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mplsvpnvrfname is not None:
                    return True

                if self.mplsvpninterfaceconfindex is not None:
                    return True

                if self.mplsvpnvrfbgpnbrindex is not None:
                    return True

                if self.mplsvpnvrfbgpnbraddr is not None:
                    return True

                if self.mplsvpnvrfbgpnbrrole is not None:
                    return True

                if self.mplsvpnvrfbgpnbrrowstatus is not None:
                    return True

                if self.mplsvpnvrfbgpnbrstoragetype is not None:
                    return True

                if self.mplsvpnvrfbgpnbrtype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _MPLS_VPN_MIB as meta
                return meta._meta_table['MplsVpnMib.Mplsvpnvrfbgpnbraddrtable.Mplsvpnvrfbgpnbraddrentry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-VPN-MIB:MPLS-VPN-MIB/MPLS-VPN-MIB:mplsVpnVrfBgpNbrAddrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplsvpnvrfbgpnbraddrentry is not None:
                for child_ref in self.mplsvpnvrfbgpnbraddrentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_VPN_MIB as meta
            return meta._meta_table['MplsVpnMib.Mplsvpnvrfbgpnbraddrtable']['meta_info']


    class Mplsvpnvrfbgpnbrprefixtable(object):
        """
        This table specifies per\-VRF vpnv4 multi\-protocol
        prefixes supported by BGP.
        
        .. attribute:: mplsvpnvrfbgpnbrprefixentry
        
        	An entry in this table is created by an LSR for every BGP prefix associated with a VRF supporting a  MPLS/BGP VPN. The indexing provides an ordering of  BGP prefixes per VRF
        	**type**\: list of    :py:class:`Mplsvpnvrfbgpnbrprefixentry <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry>`
        
        

        """

        _prefix = 'MPLS-VPN-MIB'
        _revision = '2001-10-15'

        def __init__(self):
            self.parent = None
            self.mplsvpnvrfbgpnbrprefixentry = YList()
            self.mplsvpnvrfbgpnbrprefixentry.parent = self
            self.mplsvpnvrfbgpnbrprefixentry.name = 'mplsvpnvrfbgpnbrprefixentry'


        class Mplsvpnvrfbgpnbrprefixentry(object):
            """
            An entry in this table is created by an LSR for
            every BGP prefix associated with a VRF supporting a 
            MPLS/BGP VPN. The indexing provides an ordering of 
            BGP prefixes per VRF.
            
            .. attribute:: mplsvpnvrfname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..31
            
            	**refers to**\:  :py:class:`mplsvpnvrfname <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry>`
            
            .. attribute:: mplsvpnvrfbgppathattripaddrprefix  <key>
            
            	An IP address prefix in the Network Layer Reachability Information field.  This object is an IP address containing the prefix with length specified by mplsVpnVrfBgpPathAttrIpAddrPrefixLen. Any bits beyond the length specified by mplsVpnVrfBgpPathAttrIpAddrPrefixLen are zeroed
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsvpnvrfbgppathattripaddrprefixlen  <key>
            
            	Length in bits of the IP address prefix in the Network Layer Reachability Information field
            	**type**\:  int
            
            	**range:** 0..32
            
            .. attribute:: mplsvpnvrfbgppathattrpeer  <key>
            
            	The IP address of the peer where the path information was learned
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsvpnvrfbgppathattraggregatoraddr
            
            	The IP address of the last BGP4 speaker that performed route aggregation.  A value of 0.0.0.0 indicates the absence of this attribute
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsvpnvrfbgppathattraggregatoras
            
            	The AS number of the last BGP4 speaker that performed route aggregation.  A value of zero (0) indicates the absence of this attribute
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: mplsvpnvrfbgppathattraspathsegment
            
            	The sequence of AS path segments.  Each AS path segment is represented by a triple <type, length, value>.   The type is a 1\-octet field which has two  possible values\:      1      AS\_SET\: unordered set of ASs a             route in the UPDATE             message has traversed      2      AS\_SEQUENCE\: ordered set of ASs             a route in the UPDATE             message has traversed.             The length is a 1\-octet field containing the               number of ASs in the value field.              The value field contains one or more AS             numbers, each AS is represented in the octet             string as a pair of octets according to the             following algorithm\:              first\-byte\-of\-pair = ASNumber / 256;             second\-byte\-of\-pair = ASNumber & 255;
            	**type**\:  str
            
            	**length:** 2..255
            
            .. attribute:: mplsvpnvrfbgppathattratomicaggregate
            
            	Whether or not the local system has selected a less specific route without selecting a more specific route
            	**type**\:   :py:class:`MplsvpnvrfbgppathattratomicaggregateEnum <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry.MplsvpnvrfbgppathattratomicaggregateEnum>`
            
            .. attribute:: mplsvpnvrfbgppathattrbest
            
            	An indication of whether or not this route was chosen as the best BGP4 route
            	**type**\:   :py:class:`MplsvpnvrfbgppathattrbestEnum <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry.MplsvpnvrfbgppathattrbestEnum>`
            
            .. attribute:: mplsvpnvrfbgppathattrcalclocalpref
            
            	The degree of preference calculated by the receiving BGP4 speaker for an advertised route.  A value of \-1 indicates the absence of this attribute
            	**type**\:  int
            
            	**range:** \-1..2147483647
            
            .. attribute:: mplsvpnvrfbgppathattrlocalpref
            
            	The originating BGP4 speaker's degree of preference for an advertised route.  A value of \-1 indicates the absence of this attribute
            	**type**\:  int
            
            	**range:** \-1..2147483647
            
            .. attribute:: mplsvpnvrfbgppathattrmultiexitdisc
            
            	This metric is used to discriminate between multiple exit points to an adjacent autonomous system.  A value of \-1 indicates the absence of this attribute
            	**type**\:  int
            
            	**range:** \-1..2147483647
            
            .. attribute:: mplsvpnvrfbgppathattrnexthop
            
            	The address of the border router that should be used for the destination network
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsvpnvrfbgppathattrorigin
            
            	The ultimate origin of the path information
            	**type**\:   :py:class:`MplsvpnvrfbgppathattroriginEnum <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry.MplsvpnvrfbgppathattroriginEnum>`
            
            .. attribute:: mplsvpnvrfbgppathattrunknown
            
            	One or more path attributes not understood by this BGP4 speaker.  Size zero (0) indicates the absence of such attribute(s).  Octets beyond the maximum size, if any, are not recorded by this object
            	**type**\:  str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'MPLS-VPN-MIB'
            _revision = '2001-10-15'

            def __init__(self):
                self.parent = None
                self.mplsvpnvrfname = None
                self.mplsvpnvrfbgppathattripaddrprefix = None
                self.mplsvpnvrfbgppathattripaddrprefixlen = None
                self.mplsvpnvrfbgppathattrpeer = None
                self.mplsvpnvrfbgppathattraggregatoraddr = None
                self.mplsvpnvrfbgppathattraggregatoras = None
                self.mplsvpnvrfbgppathattraspathsegment = None
                self.mplsvpnvrfbgppathattratomicaggregate = None
                self.mplsvpnvrfbgppathattrbest = None
                self.mplsvpnvrfbgppathattrcalclocalpref = None
                self.mplsvpnvrfbgppathattrlocalpref = None
                self.mplsvpnvrfbgppathattrmultiexitdisc = None
                self.mplsvpnvrfbgppathattrnexthop = None
                self.mplsvpnvrfbgppathattrorigin = None
                self.mplsvpnvrfbgppathattrunknown = None

            class MplsvpnvrfbgppathattratomicaggregateEnum(Enum):
                """
                MplsvpnvrfbgppathattratomicaggregateEnum

                Whether or not the local system has

                selected a less specific route without

                selecting a more specific route.

                .. data:: lessSpecificRrouteNotSelected = 1

                .. data:: lessSpecificRouteSelected = 2

                """

                lessSpecificRrouteNotSelected = 1

                lessSpecificRouteSelected = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _MPLS_VPN_MIB as meta
                    return meta._meta_table['MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry.MplsvpnvrfbgppathattratomicaggregateEnum']


            class MplsvpnvrfbgppathattrbestEnum(Enum):
                """
                MplsvpnvrfbgppathattrbestEnum

                An indication of whether or not this route

                was chosen as the best BGP4 route.

                .. data:: false = 1

                .. data:: true = 2

                """

                false = 1

                true = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _MPLS_VPN_MIB as meta
                    return meta._meta_table['MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry.MplsvpnvrfbgppathattrbestEnum']


            class MplsvpnvrfbgppathattroriginEnum(Enum):
                """
                MplsvpnvrfbgppathattroriginEnum

                The ultimate origin of the path

                information.

                .. data:: igp = 1

                .. data:: egp = 2

                .. data:: incomplete = 3

                """

                igp = 1

                egp = 2

                incomplete = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _MPLS_VPN_MIB as meta
                    return meta._meta_table['MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry.MplsvpnvrfbgppathattroriginEnum']


            @property
            def _common_path(self):
                if self.mplsvpnvrfname is None:
                    raise YPYModelError('Key property mplsvpnvrfname is None')
                if self.mplsvpnvrfbgppathattripaddrprefix is None:
                    raise YPYModelError('Key property mplsvpnvrfbgppathattripaddrprefix is None')
                if self.mplsvpnvrfbgppathattripaddrprefixlen is None:
                    raise YPYModelError('Key property mplsvpnvrfbgppathattripaddrprefixlen is None')
                if self.mplsvpnvrfbgppathattrpeer is None:
                    raise YPYModelError('Key property mplsvpnvrfbgppathattrpeer is None')

                return '/MPLS-VPN-MIB:MPLS-VPN-MIB/MPLS-VPN-MIB:mplsVpnVrfBgpNbrPrefixTable/MPLS-VPN-MIB:mplsVpnVrfBgpNbrPrefixEntry[MPLS-VPN-MIB:mplsVpnVrfName = ' + str(self.mplsvpnvrfname) + '][MPLS-VPN-MIB:mplsVpnVrfBgpPathAttrIpAddrPrefix = ' + str(self.mplsvpnvrfbgppathattripaddrprefix) + '][MPLS-VPN-MIB:mplsVpnVrfBgpPathAttrIpAddrPrefixLen = ' + str(self.mplsvpnvrfbgppathattripaddrprefixlen) + '][MPLS-VPN-MIB:mplsVpnVrfBgpPathAttrPeer = ' + str(self.mplsvpnvrfbgppathattrpeer) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mplsvpnvrfname is not None:
                    return True

                if self.mplsvpnvrfbgppathattripaddrprefix is not None:
                    return True

                if self.mplsvpnvrfbgppathattripaddrprefixlen is not None:
                    return True

                if self.mplsvpnvrfbgppathattrpeer is not None:
                    return True

                if self.mplsvpnvrfbgppathattraggregatoraddr is not None:
                    return True

                if self.mplsvpnvrfbgppathattraggregatoras is not None:
                    return True

                if self.mplsvpnvrfbgppathattraspathsegment is not None:
                    return True

                if self.mplsvpnvrfbgppathattratomicaggregate is not None:
                    return True

                if self.mplsvpnvrfbgppathattrbest is not None:
                    return True

                if self.mplsvpnvrfbgppathattrcalclocalpref is not None:
                    return True

                if self.mplsvpnvrfbgppathattrlocalpref is not None:
                    return True

                if self.mplsvpnvrfbgppathattrmultiexitdisc is not None:
                    return True

                if self.mplsvpnvrfbgppathattrnexthop is not None:
                    return True

                if self.mplsvpnvrfbgppathattrorigin is not None:
                    return True

                if self.mplsvpnvrfbgppathattrunknown is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _MPLS_VPN_MIB as meta
                return meta._meta_table['MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-VPN-MIB:MPLS-VPN-MIB/MPLS-VPN-MIB:mplsVpnVrfBgpNbrPrefixTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplsvpnvrfbgpnbrprefixentry is not None:
                for child_ref in self.mplsvpnvrfbgpnbrprefixentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_VPN_MIB as meta
            return meta._meta_table['MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable']['meta_info']


    class Mplsvpnvrfroutetable(object):
        """
        This table specifies per\-interface MPLS/BGP VPN VRF Table
        routing information. Entries in this table define VRF routing
        entries associated with the specified MPLS/VPN interfaces. Note
        that this table contains both BGP and IGP routes, as both may
        appear in the same VRF.
        
        .. attribute:: mplsvpnvrfrouteentry
        
        	An entry in this table is created by an LSR for every route present configured (either dynamically or statically) within the context of a specific VRF capable of supporting MPLS/BGP VPN. The indexing provides an ordering of VRFs per\-VPN interface
        	**type**\: list of    :py:class:`Mplsvpnvrfrouteentry <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry>`
        
        

        """

        _prefix = 'MPLS-VPN-MIB'
        _revision = '2001-10-15'

        def __init__(self):
            self.parent = None
            self.mplsvpnvrfrouteentry = YList()
            self.mplsvpnvrfrouteentry.parent = self
            self.mplsvpnvrfrouteentry.name = 'mplsvpnvrfrouteentry'


        class Mplsvpnvrfrouteentry(object):
            """
            An entry in this table is created by an LSR for every route
            present configured (either dynamically or statically) within
            the context of a specific VRF capable of supporting MPLS/BGP
            VPN. The indexing provides an ordering of VRFs per\-VPN
            interface.
            
            .. attribute:: mplsvpnvrfname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..31
            
            	**refers to**\:  :py:class:`mplsvpnvrfname <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry>`
            
            .. attribute:: mplsvpnvrfroutedest  <key>
            
            	The destination IP address of this route. This object may not take a Multicast (Class D) address value.  Any assignment (implicit or otherwise) of an instance of this object to a value x must be rejected if the bit\-wise logical\-AND of x with the value of the corresponding instance of the mplsVpnVrfRouteMask object is not equal to x
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsvpnvrfroutemask  <key>
            
            	Indicate the mask to be logical\-ANDed with the destination  address  before  being compared to the value  in  the  mplsVpnVrfRouteDest field. For those  systems  that  do  not support arbitrary subnet masks, an agent constructs the value of the mplsVpnVrfRouteMask by reference   to the IP Address Class.  Any assignment (implicit or otherwise) of an instance of this object to a value x must be rejected if the bit\-wise logical\-AND of x with the value of the corresponding instance of the mplsVpnVrfRouteDest object is not equal to mplsVpnVrfRouteDest
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsvpnvrfroutetos  <key>
            
            	The IP TOS Field is used to specify the policy to be applied to this route.  The encoding of IP TOS is as specified  by  the  following convention. Zero indicates the default path if no more specific policy applies.  +\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+ \|                 \|                       \|     \| \|   PRECEDENCE    \|    TYPE OF SERVICE    \|  0  \| \|                 \|                       \|     \| +\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+             IP TOS                IP TOS       Field     Policy      Field     Policy       Contents    Code      Contents    Code       0 0 0 0  ==>   0      0 0 0 1  ==>   2       0 0 1 0  ==>   4      0 0 1 1  ==>   6       0 1 0 0  ==>   8      0 1 0 1  ==>  10       0 1 1 0  ==>  12      0 1 1 1  ==>  14       1 0 0 0  ==>  16      1 0 0 1  ==>  18       1 0 1 0  ==>  20      1 0 1 1  ==>  22       1 1 0 0  ==>  24      1 1 0 1  ==>  26       1 1 1 0  ==>  28      1 1 1 1  ==>  30
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfroutenexthop  <key>
            
            	On remote routes, the address of the next system en route; Otherwise, 0.0.0.0. 
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsvpnvrfrouteage
            
            	The number of seconds since this route was last updated or otherwise determined to be correct. Note that no semantics of `too old' can be implied except through knowledge of the routing protocol by which the route was learned
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfroutedestaddrtype
            
            	The address type of the mplsVpnVrfRouteDest entry
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: mplsvpnvrfrouteifindex
            
            	The ifIndex value that identifies the local interface  through  which  the next hop of this route should be reached
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplsvpnvrfrouteinfo
            
            	A reference to MIB definitions specific to the particular routing protocol which is responsi\-   ble for this route, as determined by the  value specified  in the route's mplsVpnVrfRouteProto value. If this information is not present, its value SHOULD be set to the OBJECT IDENTIFIER { 0 0 }, which is a syntactically valid object identif\-ier, and any implementation conforming to ASN.1 and the Basic Encoding Rules must be able to generate and recognize this value
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplsvpnvrfroutemaskaddrtype
            
            	The address type of mplsVpnVrfRouteMask
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: mplsvpnvrfroutemetric1
            
            	The primary routing metric for this route. The semantics of this metric are determined by the routing\-protocol specified in  the  route's mplsVpnVrfRouteProto value. If this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mplsvpnvrfroutemetric2
            
            	An alternate routing metric for this route. The semantics of this metric are determined by the routing\-protocol specified in  the  route's mplsVpnVrfRouteProto value. If this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mplsvpnvrfroutemetric3
            
            	An alternate routing metric for this route. The semantics of this metric are determined by the routing\-protocol specified in  the  route's mplsVpnVrfRouteProto value. If this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mplsvpnvrfroutemetric4
            
            	An alternate routing metric for this route. The semantics of this metric are determined by the routing\-protocol specified in  the  route's mplsVpnVrfRouteProto value. If this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mplsvpnvrfroutemetric5
            
            	An alternate routing metric for this route. The semantics of this metric are determined by the routing\-protocol specified in  the  route's mplsVpnVrfRouteProto value. If this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mplsvpnvrfroutenexthopaddrtype
            
            	The address type of the mplsVpnVrfRouteNextHopAddrType object
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: mplsvpnvrfroutenexthopas
            
            	The Autonomous System Number of the Next Hop. The semantics of this object are determined by the routing\-protocol specified in the route's mplsVpnVrfRouteProto value. When this object is unknown or not relevant its value should be set to zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfrouteproto
            
            	The routing mechanism via which this route was learned.  Inclusion of values for gateway rout\- ing protocols is not  intended  to  imply  that hosts should support those protocols
            	**type**\:   :py:class:`MplsvpnvrfrouteprotoEnum <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry.MplsvpnvrfrouteprotoEnum>`
            
            .. attribute:: mplsvpnvrfrouterowstatus
            
            	Row status for this table. It is used according to row installation and removal conventions
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: mplsvpnvrfroutestoragetype
            
            	Storage type value
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            .. attribute:: mplsvpnvrfroutetype
            
            	The type of route.  Note that local(3)  refers to a route for which the next hop is the final destination; remote(4) refers to a route for that the next  hop is not the final destination. Routes which do not result in traffic forwarding or rejection should not be displayed even if the implementation keeps them stored internally.  reject (2) refers to a route which, if matched, discards the message as unreachable. This is used in some protocols as a means of correctly aggregating routes
            	**type**\:   :py:class:`MplsvpnvrfroutetypeEnum <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MplsVpnMib.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry.MplsvpnvrfroutetypeEnum>`
            
            

            """

            _prefix = 'MPLS-VPN-MIB'
            _revision = '2001-10-15'

            def __init__(self):
                self.parent = None
                self.mplsvpnvrfname = None
                self.mplsvpnvrfroutedest = None
                self.mplsvpnvrfroutemask = None
                self.mplsvpnvrfroutetos = None
                self.mplsvpnvrfroutenexthop = None
                self.mplsvpnvrfrouteage = None
                self.mplsvpnvrfroutedestaddrtype = None
                self.mplsvpnvrfrouteifindex = None
                self.mplsvpnvrfrouteinfo = None
                self.mplsvpnvrfroutemaskaddrtype = None
                self.mplsvpnvrfroutemetric1 = None
                self.mplsvpnvrfroutemetric2 = None
                self.mplsvpnvrfroutemetric3 = None
                self.mplsvpnvrfroutemetric4 = None
                self.mplsvpnvrfroutemetric5 = None
                self.mplsvpnvrfroutenexthopaddrtype = None
                self.mplsvpnvrfroutenexthopas = None
                self.mplsvpnvrfrouteproto = None
                self.mplsvpnvrfrouterowstatus = None
                self.mplsvpnvrfroutestoragetype = None
                self.mplsvpnvrfroutetype = None

            class MplsvpnvrfrouteprotoEnum(Enum):
                """
                MplsvpnvrfrouteprotoEnum

                The routing mechanism via which this route was

                learned.  Inclusion of values for gateway rout\-

                ing protocols is not  intended  to  imply  that

                hosts should support those protocols.

                .. data:: other = 1

                .. data:: local = 2

                .. data:: netmgmt = 3

                .. data:: icmp = 4

                .. data:: egp = 5

                .. data:: ggp = 6

                .. data:: hello = 7

                .. data:: rip = 8

                .. data:: isIs = 9

                .. data:: esIs = 10

                .. data:: ciscoIgrp = 11

                .. data:: bbnSpfIgp = 12

                .. data:: ospf = 13

                .. data:: bgp = 14

                .. data:: idpr = 15

                .. data:: ciscoEigrp = 16

                """

                other = 1

                local = 2

                netmgmt = 3

                icmp = 4

                egp = 5

                ggp = 6

                hello = 7

                rip = 8

                isIs = 9

                esIs = 10

                ciscoIgrp = 11

                bbnSpfIgp = 12

                ospf = 13

                bgp = 14

                idpr = 15

                ciscoEigrp = 16


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _MPLS_VPN_MIB as meta
                    return meta._meta_table['MplsVpnMib.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry.MplsvpnvrfrouteprotoEnum']


            class MplsvpnvrfroutetypeEnum(Enum):
                """
                MplsvpnvrfroutetypeEnum

                The type of route.  Note that local(3)  refers

                to a route for which the next hop is the final

                destination; remote(4) refers to a route for

                that the next  hop is not the final destination.

                Routes which do not result in traffic forwarding or

                rejection should not be displayed even if the

                implementation keeps them stored internally.

                reject (2) refers to a route which, if matched,

                discards the message as unreachable. This is used

                in some protocols as a means of correctly aggregating

                routes.

                .. data:: other = 1

                .. data:: reject = 2

                .. data:: local = 3

                .. data:: remote = 4

                """

                other = 1

                reject = 2

                local = 3

                remote = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _MPLS_VPN_MIB as meta
                    return meta._meta_table['MplsVpnMib.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry.MplsvpnvrfroutetypeEnum']


            @property
            def _common_path(self):
                if self.mplsvpnvrfname is None:
                    raise YPYModelError('Key property mplsvpnvrfname is None')
                if self.mplsvpnvrfroutedest is None:
                    raise YPYModelError('Key property mplsvpnvrfroutedest is None')
                if self.mplsvpnvrfroutemask is None:
                    raise YPYModelError('Key property mplsvpnvrfroutemask is None')
                if self.mplsvpnvrfroutetos is None:
                    raise YPYModelError('Key property mplsvpnvrfroutetos is None')
                if self.mplsvpnvrfroutenexthop is None:
                    raise YPYModelError('Key property mplsvpnvrfroutenexthop is None')

                return '/MPLS-VPN-MIB:MPLS-VPN-MIB/MPLS-VPN-MIB:mplsVpnVrfRouteTable/MPLS-VPN-MIB:mplsVpnVrfRouteEntry[MPLS-VPN-MIB:mplsVpnVrfName = ' + str(self.mplsvpnvrfname) + '][MPLS-VPN-MIB:mplsVpnVrfRouteDest = ' + str(self.mplsvpnvrfroutedest) + '][MPLS-VPN-MIB:mplsVpnVrfRouteMask = ' + str(self.mplsvpnvrfroutemask) + '][MPLS-VPN-MIB:mplsVpnVrfRouteTos = ' + str(self.mplsvpnvrfroutetos) + '][MPLS-VPN-MIB:mplsVpnVrfRouteNextHop = ' + str(self.mplsvpnvrfroutenexthop) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mplsvpnvrfname is not None:
                    return True

                if self.mplsvpnvrfroutedest is not None:
                    return True

                if self.mplsvpnvrfroutemask is not None:
                    return True

                if self.mplsvpnvrfroutetos is not None:
                    return True

                if self.mplsvpnvrfroutenexthop is not None:
                    return True

                if self.mplsvpnvrfrouteage is not None:
                    return True

                if self.mplsvpnvrfroutedestaddrtype is not None:
                    return True

                if self.mplsvpnvrfrouteifindex is not None:
                    return True

                if self.mplsvpnvrfrouteinfo is not None:
                    return True

                if self.mplsvpnvrfroutemaskaddrtype is not None:
                    return True

                if self.mplsvpnvrfroutemetric1 is not None:
                    return True

                if self.mplsvpnvrfroutemetric2 is not None:
                    return True

                if self.mplsvpnvrfroutemetric3 is not None:
                    return True

                if self.mplsvpnvrfroutemetric4 is not None:
                    return True

                if self.mplsvpnvrfroutemetric5 is not None:
                    return True

                if self.mplsvpnvrfroutenexthopaddrtype is not None:
                    return True

                if self.mplsvpnvrfroutenexthopas is not None:
                    return True

                if self.mplsvpnvrfrouteproto is not None:
                    return True

                if self.mplsvpnvrfrouterowstatus is not None:
                    return True

                if self.mplsvpnvrfroutestoragetype is not None:
                    return True

                if self.mplsvpnvrfroutetype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _MPLS_VPN_MIB as meta
                return meta._meta_table['MplsVpnMib.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-VPN-MIB:MPLS-VPN-MIB/MPLS-VPN-MIB:mplsVpnVrfRouteTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplsvpnvrfrouteentry is not None:
                for child_ref in self.mplsvpnvrfrouteentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_VPN_MIB as meta
            return meta._meta_table['MplsVpnMib.Mplsvpnvrfroutetable']['meta_info']

    @property
    def _common_path(self):

        return '/MPLS-VPN-MIB:MPLS-VPN-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.mplsvpninterfaceconftable is not None and self.mplsvpninterfaceconftable._has_data():
            return True

        if self.mplsvpnscalars is not None and self.mplsvpnscalars._has_data():
            return True

        if self.mplsvpnvrfbgpnbraddrtable is not None and self.mplsvpnvrfbgpnbraddrtable._has_data():
            return True

        if self.mplsvpnvrfbgpnbrprefixtable is not None and self.mplsvpnvrfbgpnbrprefixtable._has_data():
            return True

        if self.mplsvpnvrfroutetable is not None and self.mplsvpnvrfroutetable._has_data():
            return True

        if self.mplsvpnvrfroutetargettable is not None and self.mplsvpnvrfroutetargettable._has_data():
            return True

        if self.mplsvpnvrftable is not None and self.mplsvpnvrftable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _MPLS_VPN_MIB as meta
        return meta._meta_table['MplsVpnMib']['meta_info']



""" MPLS_L3VPN_STD_MIB 

This MIB contains managed object definitions for the
Layer\-3 Multiprotocol Label Switching Virtual
Private Networks.

Copyright (C) The Internet Society (2006).  This
version of this MIB module is part of RFC4382; see
the RFC itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class Mplsl3VpnrttypeEnum(Enum):
    """
    Mplsl3VpnrttypeEnum

    Used to define the type of a route target usage.

    Route targets can be specified to be imported,

    exported, or both.  For a complete definition of a

    route target, see [RFC4364].

    .. data:: import_ = 1

    .. data:: export = 2

    .. data:: both = 3

    """

    import_ = 1

    export = 2

    both = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _MPLS_L3VPN_STD_MIB as meta
        return meta._meta_table['Mplsl3VpnrttypeEnum']



class MplsL3VpnStdMib(object):
    """
    
    
    .. attribute:: mplsl3vpnifconftable
    
    	This table specifies per\-interface MPLS capability and associated information
    	**type**\:   :py:class:`Mplsl3Vpnifconftable <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnifconftable>`
    
    .. attribute:: mplsl3vpnscalars
    
    	
    	**type**\:   :py:class:`Mplsl3Vpnscalars <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnscalars>`
    
    .. attribute:: mplsl3vpnvrfrtetable
    
    	This table specifies per\-interface MPLS L3VPN VRF Table routing information.  Entries in this table define VRF routing entries associated with the specified MPLS/VPN interfaces.  Note  that this table contains both BGP and Interior Gateway Protocol IGP routes, as both may appear in the same VRF
    	**type**\:   :py:class:`Mplsl3Vpnvrfrtetable <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable>`
    
    .. attribute:: mplsl3vpnvrfrttable
    
    	This table specifies per\-VRF route target association. Each entry identifies a connectivity policy supported as part of a VPN
    	**type**\:   :py:class:`Mplsl3Vpnvrfrttable <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnvrfrttable>`
    
    .. attribute:: mplsl3vpnvrftable
    
    	This table specifies per\-interface MPLS L3VPN VRF Table capability and associated information. Entries in this table define VRF routing instances associated with MPLS/VPN interfaces.  Note that multiple interfaces can belong to the same VRF instance.  The collection of all VRF instances comprises an actual VPN
    	**type**\:   :py:class:`Mplsl3Vpnvrftable <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnvrftable>`
    
    

    """

    _prefix = 'MPLS-L3VPN-STD-MIB'
    _revision = '2006-01-23'

    def __init__(self):
        self.mplsl3vpnifconftable = MplsL3VpnStdMib.Mplsl3Vpnifconftable()
        self.mplsl3vpnifconftable.parent = self
        self.mplsl3vpnscalars = MplsL3VpnStdMib.Mplsl3Vpnscalars()
        self.mplsl3vpnscalars.parent = self
        self.mplsl3vpnvrfrtetable = MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable()
        self.mplsl3vpnvrfrtetable.parent = self
        self.mplsl3vpnvrfrttable = MplsL3VpnStdMib.Mplsl3Vpnvrfrttable()
        self.mplsl3vpnvrfrttable.parent = self
        self.mplsl3vpnvrftable = MplsL3VpnStdMib.Mplsl3Vpnvrftable()
        self.mplsl3vpnvrftable.parent = self


    class Mplsl3Vpnscalars(object):
        """
        
        
        .. attribute:: mplsl3vpnactivevrfs
        
        	The number of VRFs that are active on this node. That is, those VRFs whose corresponding mplsL3VpnVrfOperStatus object value is equal to operational (1)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplsl3vpnconfiguredvrfs
        
        	The number of VRFs that are configured on this node
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplsl3vpnconnectedinterfaces
        
        	Total number of interfaces connected to a VRF
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplsl3vpnilllblrcvthrsh
        
        	The number of illegally received labels above which the mplsNumVrfSecIllglLblThrshExcd notification is issued.  The persistence of this value mimics that of the device's configuration
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplsl3vpnnotificationenable
        
        	If this object is true, then it enables the generation of all notifications defined in this MIB.  This object's value should be preserved across agent reboots
        	**type**\:  bool
        
        .. attribute:: mplsl3vpnvrfconfmaxpossrts
        
        	Denotes maximum number of routes that the device will allow all VRFs jointly to hold.  If this value is set to 0, this indicates that the device is unable to determine the absolute maximum.  In this case, the configured maximum MAY not actually be allowed by the device
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplsl3vpnvrfconfrtemxthrshtime
        
        	Denotes the interval in seconds, at which the route max threshold notification may be reissued after the maximum value has been exceeded (or has been reached if mplsL3VpnVrfConfMaxRoutes and mplsL3VpnVrfConfHighRteThresh are equal) and the initial notification has been issued.  This value is intended to prevent continuous generation of notifications by an agent in the event that routes are continually added to a VRF after it has reached its maximum value.  If this value is set to 0, the agent should only issue a single notification at the time that the maximum threshold has been reached, and should not issue any more notifications until the value of routes has fallen below the configured threshold value.  This is the recommended default behavior
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: seconds
        
        

        """

        _prefix = 'MPLS-L3VPN-STD-MIB'
        _revision = '2006-01-23'

        def __init__(self):
            self.parent = None
            self.mplsl3vpnactivevrfs = None
            self.mplsl3vpnconfiguredvrfs = None
            self.mplsl3vpnconnectedinterfaces = None
            self.mplsl3vpnilllblrcvthrsh = None
            self.mplsl3vpnnotificationenable = None
            self.mplsl3vpnvrfconfmaxpossrts = None
            self.mplsl3vpnvrfconfrtemxthrshtime = None

        @property
        def _common_path(self):

            return '/MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/MPLS-L3VPN-STD-MIB:mplsL3VpnScalars'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplsl3vpnactivevrfs is not None:
                return True

            if self.mplsl3vpnconfiguredvrfs is not None:
                return True

            if self.mplsl3vpnconnectedinterfaces is not None:
                return True

            if self.mplsl3vpnilllblrcvthrsh is not None:
                return True

            if self.mplsl3vpnnotificationenable is not None:
                return True

            if self.mplsl3vpnvrfconfmaxpossrts is not None:
                return True

            if self.mplsl3vpnvrfconfrtemxthrshtime is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_L3VPN_STD_MIB as meta
            return meta._meta_table['MplsL3VpnStdMib.Mplsl3Vpnscalars']['meta_info']


    class Mplsl3Vpnifconftable(object):
        """
        This table specifies per\-interface MPLS capability
        and associated information.
        
        .. attribute:: mplsl3vpnifconfentry
        
        	An entry in this table is created by an LSR for every interface capable of supporting MPLS L3VPN. Each entry in this table is meant to correspond to an entry in the Interfaces Table
        	**type**\: list of    :py:class:`Mplsl3Vpnifconfentry <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry>`
        
        

        """

        _prefix = 'MPLS-L3VPN-STD-MIB'
        _revision = '2006-01-23'

        def __init__(self):
            self.parent = None
            self.mplsl3vpnifconfentry = YList()
            self.mplsl3vpnifconfentry.parent = self
            self.mplsl3vpnifconfentry.name = 'mplsl3vpnifconfentry'


        class Mplsl3Vpnifconfentry(object):
            """
            An entry in this table is created by an LSR for
            every interface capable of supporting MPLS L3VPN.
            Each entry in this table is meant to correspond to
            an entry in the Interfaces Table.
            
            .. attribute:: mplsl3vpnvrfname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..31
            
            	**refers to**\:  :py:class:`mplsl3vpnvrfname <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry>`
            
            .. attribute:: mplsl3vpnifconfindex  <key>
            
            	This is a unique index for an entry in the mplsL3VpnIfConfTable.  A non\-zero index for an entry indicates the ifIndex for the corresponding interface entry in the MPLS\-VPN\-layer in the ifTable. Note that this table does not necessarily correspond one\-to\-one with all entries in the Interface MIB having an ifType of MPLS\-layer; rather, only those that are enabled for MPLS L3VPN functionality
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: mplsl3vpnifconfrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table.  Rows in this table signify that the specified interface is associated with this VRF.  If the row creation operation succeeds, the interface will have been associated with the specified VRF, otherwise the agent MUST not allow the association.  If the agent only allows read\-only operations on this table, it MUST create entries in this table as they are created on the device.  When a row in this table is in active(1) state, no objects in that row can be modified except mplsL3VpnIfConfStorageType and mplsL3VpnIfConfRowStatus
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: mplsl3vpnifconfstoragetype
            
            	The storage type for this VPN If entry. Conceptual rows having the value 'permanent' need not allow write access to any columnar objects in the row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            .. attribute:: mplsl3vpnifvpnclassification
            
            	Denotes whether this link participates in a carrier's carrier, enterprise, or inter\-provider scenario
            	**type**\:   :py:class:`Mplsl3VpnifvpnclassificationEnum <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry.Mplsl3VpnifvpnclassificationEnum>`
            
            .. attribute:: mplsl3vpnifvpnroutedistprotocol
            
            	Denotes the route distribution protocol across the PE\-CE link.  Note that more than one routing protocol may be enabled at the same time; thus, this object is specified as a bitmask.  For example, static(5) and ospf(2) are a typical configuration
            	**type**\:   :py:class:`Mplsl3Vpnifvpnroutedistprotocol <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry.Mplsl3Vpnifvpnroutedistprotocol>`
            
            

            """

            _prefix = 'MPLS-L3VPN-STD-MIB'
            _revision = '2006-01-23'

            def __init__(self):
                self.parent = None
                self.mplsl3vpnvrfname = None
                self.mplsl3vpnifconfindex = None
                self.mplsl3vpnifconfrowstatus = None
                self.mplsl3vpnifconfstoragetype = None
                self.mplsl3vpnifvpnclassification = None
                self.mplsl3vpnifvpnroutedistprotocol = MplsL3VpnStdMib.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry.Mplsl3Vpnifvpnroutedistprotocol()

            class Mplsl3VpnifvpnclassificationEnum(Enum):
                """
                Mplsl3VpnifvpnclassificationEnum

                Denotes whether this link participates in a

                carrier's carrier, enterprise, or inter\-provider

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
                    from ydk.models.cisco_ios_xe._meta import _MPLS_L3VPN_STD_MIB as meta
                    return meta._meta_table['MplsL3VpnStdMib.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry.Mplsl3VpnifvpnclassificationEnum']


            class Mplsl3Vpnifvpnroutedistprotocol(FixedBitsDict):
                """
                Mplsl3Vpnifvpnroutedistprotocol

                Denotes the route distribution protocol across the
                PE\-CE link.  Note that more than one routing protocol
                may be enabled at the same time; thus, this object is
                specified as a bitmask.  For example, static(5) and
                ospf(2) are a typical configuration.
                Keys are:- rip , static , isis , none , other , bgp , ospf

                """

                def __init__(self):
                    self._dictionary = { 
                        'rip':False,
                        'static':False,
                        'isis':False,
                        'none':False,
                        'other':False,
                        'bgp':False,
                        'ospf':False,
                    }
                    self._pos_map = { 
                        'rip':3,
                        'static':5,
                        'isis':4,
                        'none':0,
                        'other':6,
                        'bgp':1,
                        'ospf':2,
                    }

            @property
            def _common_path(self):
                if self.mplsl3vpnvrfname is None:
                    raise YPYModelError('Key property mplsl3vpnvrfname is None')
                if self.mplsl3vpnifconfindex is None:
                    raise YPYModelError('Key property mplsl3vpnifconfindex is None')

                return '/MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/MPLS-L3VPN-STD-MIB:mplsL3VpnIfConfTable/MPLS-L3VPN-STD-MIB:mplsL3VpnIfConfEntry[MPLS-L3VPN-STD-MIB:mplsL3VpnVrfName = ' + str(self.mplsl3vpnvrfname) + '][MPLS-L3VPN-STD-MIB:mplsL3VpnIfConfIndex = ' + str(self.mplsl3vpnifconfindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mplsl3vpnvrfname is not None:
                    return True

                if self.mplsl3vpnifconfindex is not None:
                    return True

                if self.mplsl3vpnifconfrowstatus is not None:
                    return True

                if self.mplsl3vpnifconfstoragetype is not None:
                    return True

                if self.mplsl3vpnifvpnclassification is not None:
                    return True

                if self.mplsl3vpnifvpnroutedistprotocol is not None:
                    if self.mplsl3vpnifvpnroutedistprotocol._has_data():
                        return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _MPLS_L3VPN_STD_MIB as meta
                return meta._meta_table['MplsL3VpnStdMib.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/MPLS-L3VPN-STD-MIB:mplsL3VpnIfConfTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplsl3vpnifconfentry is not None:
                for child_ref in self.mplsl3vpnifconfentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_L3VPN_STD_MIB as meta
            return meta._meta_table['MplsL3VpnStdMib.Mplsl3Vpnifconftable']['meta_info']


    class Mplsl3Vpnvrftable(object):
        """
        This table specifies per\-interface MPLS L3VPN
        VRF Table capability and associated information.
        Entries in this table define VRF routing instances
        associated with MPLS/VPN interfaces.  Note that
        multiple interfaces can belong to the same VRF
        instance.  The collection of all VRF instances
        comprises an actual VPN.
        
        .. attribute:: mplsl3vpnvrfentry
        
        	An entry in this table is created by an LSR for every VRF capable of supporting MPLS L3VPN.  The indexing provides an ordering of VRFs per\-VPN interface
        	**type**\: list of    :py:class:`Mplsl3Vpnvrfentry <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry>`
        
        

        """

        _prefix = 'MPLS-L3VPN-STD-MIB'
        _revision = '2006-01-23'

        def __init__(self):
            self.parent = None
            self.mplsl3vpnvrfentry = YList()
            self.mplsl3vpnvrfentry.parent = self
            self.mplsl3vpnvrfentry.name = 'mplsl3vpnvrfentry'


        class Mplsl3Vpnvrfentry(object):
            """
            An entry in this table is created by an LSR for
            every VRF capable of supporting MPLS L3VPN.  The
            indexing provides an ordering of VRFs per\-VPN
            interface.
            
            .. attribute:: mplsl3vpnvrfname  <key>
            
            	The human\-readable name of this VPN.  This MAY be equivalent to the [RFC2685] VPN\-ID, but may also vary.  If it is set to the VPN ID, it MUST be equivalent to the value of mplsL3VpnVrfVpnId. It is strongly recommended that all sites supporting VRFs that are part of the same VPN use the same naming convention for VRFs as well as the same VPN ID
            	**type**\:  str
            
            	**length:** 0..31
            
            .. attribute:: mplsl3vpnvrfactiveinterfaces
            
            	Total number of interfaces connected to this VRF with ifOperStatus = up(1).  This value should increase when an interface is associated with the corresponding VRF and its corresponding ifOperStatus is equal to up(1).  If an interface is associated whose ifOperStatus is not up(1), then the value is not incremented until such time as it transitions to this state.  This value should be decremented when an interface is disassociated with a VRF or the corresponding ifOperStatus transitions out of the up(1) state to any other state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfassociatedinterfaces
            
            	Total number of interfaces connected to this VRF (independent of ifOperStatus type)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfconfadminstatus
            
            	Indicates the desired operational status of this VRF
            	**type**\:   :py:class:`Mplsl3VpnvrfconfadminstatusEnum <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry.Mplsl3VpnvrfconfadminstatusEnum>`
            
            .. attribute:: mplsl3vpnvrfconfhighrtethresh
            
            	Denotes high\-level water marker for the number of routes that this VRF may hold
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfconflastchanged
            
            	The value of sysUpTime at the time of the last change of this table entry, which includes changes of VRF parameters defined in this table or addition or deletion of interfaces associated with this VRF
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfconfmaxroutes
            
            	Denotes maximum number of routes that this VRF is configured to hold.  This value MUST be less than or equal to mplsL3VpnVrfConfMaxPossRts unless it is set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfconfmidrtethresh
            
            	Denotes mid\-level water marker for the number of routes that this VRF may hold
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfconfrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table.  When a row in this table is in active(1) state, no objects in that row can be modified except mplsL3VpnVrfConfAdminStatus, mplsL3VpnVrfConfRowStatus, and mplsL3VpnVrfConfStorageType
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: mplsl3vpnvrfconfstoragetype
            
            	The storage type for this VPN VRF entry. Conceptual rows having the value 'permanent' need not allow write access to any columnar objects in the row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            .. attribute:: mplsl3vpnvrfcreationtime
            
            	The time at which this VRF entry was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfdescription
            
            	The human\-readable description of this VRF
            	**type**\:  str
            
            .. attribute:: mplsl3vpnvrfoperstatus
            
            	Denotes whether or not a VRF is operational.  A VRF is up(1) when there is at least one interface associated with the VRF whose ifOperStatus is up(1).  A VRF is down(2) when\: a. There does not exist at least one interface whose    ifOperStatus is up(1). b. There are no interfaces associated with the VRF
            	**type**\:   :py:class:`Mplsl3VpnvrfoperstatusEnum <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry.Mplsl3VpnvrfoperstatusEnum>`
            
            .. attribute:: mplsl3vpnvrfperfcurrnumroutes
            
            	Indicates the number of routes currently used by this VRF
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfperfdisctime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this entry's counters suffered a discontinuity.  If no such discontinuities have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfperfroutesadded
            
            	Indicates the number of routes added to this VPN/VRF since the last discontinuity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsL3VpnVrfPerfDiscTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfperfroutesdeleted
            
            	Indicates the number of routes removed from this VPN/VRF.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsL3VpnVrfPerfDiscTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfperfroutesdropped
            
            	This counter should be incremented when the number of routes contained by the specified VRF exceeds or attempts to exceed the maximum allowed value as indicated by mplsL3VpnVrfMaxRouteThreshold.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsL3VpnVrfPerfDiscTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfrd
            
            	The route distinguisher for this VRF
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: mplsl3vpnvrfsecdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this entry's counters suffered a discontinuity.  If no such discontinuities have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfsecillegallblvltns
            
            	Indicates the number of illegally received labels on this VPN/VRF.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsL3VpnVrfSecDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfvpnid
            
            	The VPN ID as specified in [RFC2685].  If a VPN ID has not been specified for this VRF, then this variable SHOULD be set to a zero\-length OCTET STRING
            	**type**\:  str
            
            	**length:** 0 \| 7
            
            

            """

            _prefix = 'MPLS-L3VPN-STD-MIB'
            _revision = '2006-01-23'

            def __init__(self):
                self.parent = None
                self.mplsl3vpnvrfname = None
                self.mplsl3vpnvrfactiveinterfaces = None
                self.mplsl3vpnvrfassociatedinterfaces = None
                self.mplsl3vpnvrfconfadminstatus = None
                self.mplsl3vpnvrfconfhighrtethresh = None
                self.mplsl3vpnvrfconflastchanged = None
                self.mplsl3vpnvrfconfmaxroutes = None
                self.mplsl3vpnvrfconfmidrtethresh = None
                self.mplsl3vpnvrfconfrowstatus = None
                self.mplsl3vpnvrfconfstoragetype = None
                self.mplsl3vpnvrfcreationtime = None
                self.mplsl3vpnvrfdescription = None
                self.mplsl3vpnvrfoperstatus = None
                self.mplsl3vpnvrfperfcurrnumroutes = None
                self.mplsl3vpnvrfperfdisctime = None
                self.mplsl3vpnvrfperfroutesadded = None
                self.mplsl3vpnvrfperfroutesdeleted = None
                self.mplsl3vpnvrfperfroutesdropped = None
                self.mplsl3vpnvrfrd = None
                self.mplsl3vpnvrfsecdiscontinuitytime = None
                self.mplsl3vpnvrfsecillegallblvltns = None
                self.mplsl3vpnvrfvpnid = None

            class Mplsl3VpnvrfconfadminstatusEnum(Enum):
                """
                Mplsl3VpnvrfconfadminstatusEnum

                Indicates the desired operational status of this

                VRF.

                .. data:: up = 1

                .. data:: down = 2

                .. data:: testing = 3

                """

                up = 1

                down = 2

                testing = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _MPLS_L3VPN_STD_MIB as meta
                    return meta._meta_table['MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry.Mplsl3VpnvrfconfadminstatusEnum']


            class Mplsl3VpnvrfoperstatusEnum(Enum):
                """
                Mplsl3VpnvrfoperstatusEnum

                Denotes whether or not a VRF is operational.  A VRF is

                up(1) when there is at least one interface associated

                with the VRF whose ifOperStatus is up(1).  A VRF is

                down(2) when\:

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
                    from ydk.models.cisco_ios_xe._meta import _MPLS_L3VPN_STD_MIB as meta
                    return meta._meta_table['MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry.Mplsl3VpnvrfoperstatusEnum']


            @property
            def _common_path(self):
                if self.mplsl3vpnvrfname is None:
                    raise YPYModelError('Key property mplsl3vpnvrfname is None')

                return '/MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/MPLS-L3VPN-STD-MIB:mplsL3VpnVrfTable/MPLS-L3VPN-STD-MIB:mplsL3VpnVrfEntry[MPLS-L3VPN-STD-MIB:mplsL3VpnVrfName = ' + str(self.mplsl3vpnvrfname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mplsl3vpnvrfname is not None:
                    return True

                if self.mplsl3vpnvrfactiveinterfaces is not None:
                    return True

                if self.mplsl3vpnvrfassociatedinterfaces is not None:
                    return True

                if self.mplsl3vpnvrfconfadminstatus is not None:
                    return True

                if self.mplsl3vpnvrfconfhighrtethresh is not None:
                    return True

                if self.mplsl3vpnvrfconflastchanged is not None:
                    return True

                if self.mplsl3vpnvrfconfmaxroutes is not None:
                    return True

                if self.mplsl3vpnvrfconfmidrtethresh is not None:
                    return True

                if self.mplsl3vpnvrfconfrowstatus is not None:
                    return True

                if self.mplsl3vpnvrfconfstoragetype is not None:
                    return True

                if self.mplsl3vpnvrfcreationtime is not None:
                    return True

                if self.mplsl3vpnvrfdescription is not None:
                    return True

                if self.mplsl3vpnvrfoperstatus is not None:
                    return True

                if self.mplsl3vpnvrfperfcurrnumroutes is not None:
                    return True

                if self.mplsl3vpnvrfperfdisctime is not None:
                    return True

                if self.mplsl3vpnvrfperfroutesadded is not None:
                    return True

                if self.mplsl3vpnvrfperfroutesdeleted is not None:
                    return True

                if self.mplsl3vpnvrfperfroutesdropped is not None:
                    return True

                if self.mplsl3vpnvrfrd is not None:
                    return True

                if self.mplsl3vpnvrfsecdiscontinuitytime is not None:
                    return True

                if self.mplsl3vpnvrfsecillegallblvltns is not None:
                    return True

                if self.mplsl3vpnvrfvpnid is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _MPLS_L3VPN_STD_MIB as meta
                return meta._meta_table['MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/MPLS-L3VPN-STD-MIB:mplsL3VpnVrfTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplsl3vpnvrfentry is not None:
                for child_ref in self.mplsl3vpnvrfentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_L3VPN_STD_MIB as meta
            return meta._meta_table['MplsL3VpnStdMib.Mplsl3Vpnvrftable']['meta_info']


    class Mplsl3Vpnvrfrttable(object):
        """
        This table specifies per\-VRF route target association.
        Each entry identifies a connectivity policy supported
        as part of a VPN.
        
        .. attribute:: mplsl3vpnvrfrtentry
        
        	An entry in this table is created by an LSR for each route target configured for a VRF supporting a MPLS L3VPN instance.  The indexing provides an ordering per\-VRF instance.  See [RFC4364] for a complete definition of a route target
        	**type**\: list of    :py:class:`Mplsl3Vpnvrfrtentry <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnvrfrttable.Mplsl3Vpnvrfrtentry>`
        
        

        """

        _prefix = 'MPLS-L3VPN-STD-MIB'
        _revision = '2006-01-23'

        def __init__(self):
            self.parent = None
            self.mplsl3vpnvrfrtentry = YList()
            self.mplsl3vpnvrfrtentry.parent = self
            self.mplsl3vpnvrfrtentry.name = 'mplsl3vpnvrfrtentry'


        class Mplsl3Vpnvrfrtentry(object):
            """
            An entry in this table is created by an LSR for
            each route target configured for a VRF supporting
            a MPLS L3VPN instance.  The indexing provides an
            ordering per\-VRF instance.  See [RFC4364] for a
            complete definition of a route target.
            
            .. attribute:: mplsl3vpnvrfname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..31
            
            	**refers to**\:  :py:class:`mplsl3vpnvrfname <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry>`
            
            .. attribute:: mplsl3vpnvrfrtindex  <key>
            
            	Auxiliary index for route targets configured for a particular VRF
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplsl3vpnvrfrttype  <key>
            
            	The route target distribution type
            	**type**\:   :py:class:`Mplsl3VpnrttypeEnum <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.Mplsl3VpnrttypeEnum>`
            
            .. attribute:: mplsl3vpnvrfrt
            
            	The route target distribution policy
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: mplsl3vpnvrfrtdescr
            
            	Description of the route target
            	**type**\:  str
            
            .. attribute:: mplsl3vpnvrfrtrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table.  When a row in this table is in active(1) state, no objects in that row can be modified except mplsL3VpnVrfRTRowStatus
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: mplsl3vpnvrfrtstoragetype
            
            	The storage type for this VPN route target (RT) entry. Conceptual rows having the value 'permanent' need not allow write access to any columnar objects in the row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            

            """

            _prefix = 'MPLS-L3VPN-STD-MIB'
            _revision = '2006-01-23'

            def __init__(self):
                self.parent = None
                self.mplsl3vpnvrfname = None
                self.mplsl3vpnvrfrtindex = None
                self.mplsl3vpnvrfrttype = None
                self.mplsl3vpnvrfrt = None
                self.mplsl3vpnvrfrtdescr = None
                self.mplsl3vpnvrfrtrowstatus = None
                self.mplsl3vpnvrfrtstoragetype = None

            @property
            def _common_path(self):
                if self.mplsl3vpnvrfname is None:
                    raise YPYModelError('Key property mplsl3vpnvrfname is None')
                if self.mplsl3vpnvrfrtindex is None:
                    raise YPYModelError('Key property mplsl3vpnvrfrtindex is None')
                if self.mplsl3vpnvrfrttype is None:
                    raise YPYModelError('Key property mplsl3vpnvrfrttype is None')

                return '/MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/MPLS-L3VPN-STD-MIB:mplsL3VpnVrfRTTable/MPLS-L3VPN-STD-MIB:mplsL3VpnVrfRTEntry[MPLS-L3VPN-STD-MIB:mplsL3VpnVrfName = ' + str(self.mplsl3vpnvrfname) + '][MPLS-L3VPN-STD-MIB:mplsL3VpnVrfRTIndex = ' + str(self.mplsl3vpnvrfrtindex) + '][MPLS-L3VPN-STD-MIB:mplsL3VpnVrfRTType = ' + str(self.mplsl3vpnvrfrttype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mplsl3vpnvrfname is not None:
                    return True

                if self.mplsl3vpnvrfrtindex is not None:
                    return True

                if self.mplsl3vpnvrfrttype is not None:
                    return True

                if self.mplsl3vpnvrfrt is not None:
                    return True

                if self.mplsl3vpnvrfrtdescr is not None:
                    return True

                if self.mplsl3vpnvrfrtrowstatus is not None:
                    return True

                if self.mplsl3vpnvrfrtstoragetype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _MPLS_L3VPN_STD_MIB as meta
                return meta._meta_table['MplsL3VpnStdMib.Mplsl3Vpnvrfrttable.Mplsl3Vpnvrfrtentry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/MPLS-L3VPN-STD-MIB:mplsL3VpnVrfRTTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplsl3vpnvrfrtentry is not None:
                for child_ref in self.mplsl3vpnvrfrtentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_L3VPN_STD_MIB as meta
            return meta._meta_table['MplsL3VpnStdMib.Mplsl3Vpnvrfrttable']['meta_info']


    class Mplsl3Vpnvrfrtetable(object):
        """
        This table specifies per\-interface MPLS L3VPN VRF Table
        routing information.  Entries in this table define VRF routing
        entries associated with the specified MPLS/VPN interfaces.  Note
        
        that this table contains both BGP and Interior Gateway Protocol
        IGP routes, as both may appear in the same VRF.
        
        .. attribute:: mplsl3vpnvrfrteentry
        
        	An entry in this table is created by an LSR for every route present configured (either dynamically or statically) within the context of a specific VRF capable of supporting MPLS/BGP VPN.  The indexing provides an ordering of VRFs per\-VPN interface.  Implementers need to be aware that there are quite a few index objects that together can exceed the size allowed for an Object Identifier (OID).  So implementers must make sure that OIDs of column instances in this table will have no more than 128 sub\-identifiers, otherwise they cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3
        	**type**\: list of    :py:class:`Mplsl3Vpnvrfrteentry <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable.Mplsl3Vpnvrfrteentry>`
        
        

        """

        _prefix = 'MPLS-L3VPN-STD-MIB'
        _revision = '2006-01-23'

        def __init__(self):
            self.parent = None
            self.mplsl3vpnvrfrteentry = YList()
            self.mplsl3vpnvrfrteentry.parent = self
            self.mplsl3vpnvrfrteentry.name = 'mplsl3vpnvrfrteentry'


        class Mplsl3Vpnvrfrteentry(object):
            """
            An entry in this table is created by an LSR for every route
            present configured (either dynamically or statically) within
            the context of a specific VRF capable of supporting MPLS/BGP
            VPN.  The indexing provides an ordering of VRFs per\-VPN
            interface.
            
            Implementers need to be aware that there are quite a few
            index objects that together can exceed the size allowed
            for an Object Identifier (OID).  So implementers must make
            sure that OIDs of column instances in this table will have
            no more than 128 sub\-identifiers, otherwise they cannot be
            accessed using SNMPv1, SNMPv2c, or SNMPv3.
            
            .. attribute:: mplsl3vpnvrfname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..31
            
            	**refers to**\:  :py:class:`mplsl3vpnvrfname <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry>`
            
            .. attribute:: mplsl3vpnvrfrteinetcidrdesttype  <key>
            
            	The type of the mplsL3VpnVrfRteInetCidrDest address, as defined in the InetAddress MIB.  Only those address types that may appear in an actual routing table are allowed as values of this object
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: mplsl3vpnvrfrteinetcidrdest  <key>
            
            	The destination IP address of this route.  The type of this address is determined by the value of the mplsL3VpnVrfRteInetCidrDestType object.  The values for the index objects mplsL3VpnVrfRteInetCidrDest and mplsL3VpnVrfRteInetCidrPfxLen must be consistent.  When the value of mplsL3VpnVrfRteInetCidrDest is x, then the bitwise logical\-AND of x with the value of the mask formed from the corresponding index object mplsL3VpnVrfRteInetCidrPfxLen MUST be equal to x.  If not, then the index pair is not consistent and an inconsistentName error must be returned on SET or CREATE requests
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsl3vpnvrfrteinetcidrpfxlen  <key>
            
            	Indicates the number of leading one bits that form the  mask to be logical\-ANDed with the destination address before being compared to the value in the mplsL3VpnVrfRteInetCidrDest field.  The values for the index objects mplsL3VpnVrfRteInetCidrDest and mplsL3VpnVrfRteInetCidrPfxLen must be consistent.  When the value of mplsL3VpnVrfRteInetCidrDest is x, then the bitwise logical\-AND of x with the value of the mask formed from the corresponding index object mplsL3VpnVrfRteInetCidrPfxLen MUST be equal to x.  If not, then the index pair is not consistent and an inconsistentName error must be returned on SET or CREATE requests
            	**type**\:  int
            
            	**range:** 0..128
            
            .. attribute:: mplsl3vpnvrfrteinetcidrpolicy  <key>
            
            	This object is an opaque object without any defined semantics.  Its purpose is to serve as an additional index that may delineate between multiple entries to the same destination.  The value { 0 0 } shall be used as the default value for this object
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplsl3vpnvrfrteinetcidrnhoptype  <key>
            
            	The type of the mplsL3VpnVrfRteInetCidrNextHop address, as defined in the InetAddress MIB.  Value should be set to unknown(0) for non\-remote routes.  Only those address types that may appear in an actual routing table are allowed as values of this object
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: mplsl3vpnvrfrteinetcidrnexthop  <key>
            
            	On remote routes, the address of the next system en route.  For non\-remote routes, a zero\-length string. The type of this address is determined by the value of the mplsL3VpnVrfRteInetCidrNHopType object
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsl3vpnvrfrteinetcidrage
            
            	The number of seconds since this route was last updated or otherwise determined to be correct.  Note that no semantics of 'too old' can be implied except through knowledge of the routing protocol by which the route was learned
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfrteinetcidrifindex
            
            	The ifIndex value that identifies the local interface through which the next hop of this route should be reached.  A value of 0 is valid and represents the scenario where no interface is specified
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplsl3vpnvrfrteinetcidrmetric1
            
            	The primary routing metric for this route.  The semantics of this metric are determined by the  routing protocol specified in the route's mplsL3VpnVrfRteInetCidrProto value.  If this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-1..2147483647
            
            .. attribute:: mplsl3vpnvrfrteinetcidrmetric2
            
            	An alternate routing metric for this route.  The semantics of this metric are determined by the routing protocol specified in the route's mplsL3VpnVrfRteInetCidrProto value.  If this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-1..2147483647
            
            .. attribute:: mplsl3vpnvrfrteinetcidrmetric3
            
            	An alternate routing metric for this route.  The semantics of this metric are determined by the routing protocol specified in the route's mplsL3VpnVrfRteInetCidrProto value.  If this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-1..2147483647
            
            .. attribute:: mplsl3vpnvrfrteinetcidrmetric4
            
            	An alternate routing metric for this route.  The semantics of this metric are determined by the routing protocol specified in the route's mplsL3VpnVrfRteInetCidrProto value.  If this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-1..2147483647
            
            .. attribute:: mplsl3vpnvrfrteinetcidrmetric5
            
            	An alternate routing metric for this route.  The semantics of this metric are determined by the routing protocol specified in the route's mplsL3VpnVrfRteInetCidrProto value.  If this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-1..2147483647
            
            .. attribute:: mplsl3vpnvrfrteinetcidrnexthopas
            
            	The Autonomous System Number of the next hop.  The semantics of this object are determined by the routing protocol specified in the route's mplsL3VpnVrfRteInetCidrProto value.  When this object is unknown or not relevant, its value should be set to zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfrteinetcidrproto
            
            	The routing mechanism via which this route was learned. Inclusion of values for gateway routing protocols is not intended to imply that hosts should support those protocols
            	**type**\:   :py:class:`IanaiprouteprotocolEnum <ydk.models.cisco_ios_xe.IANA_RTPROTO_MIB.IanaiprouteprotocolEnum>`
            
            .. attribute:: mplsl3vpnvrfrteinetcidrstatus
            
            	The row status variable, used according to row installation and removal conventions.  A row entry cannot be modified when the status is marked as active(1)
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: mplsl3vpnvrfrteinetcidrtype
            
            	The type of route.  Note that local(3) refers to a route for which the next hop is the final destination; remote(4) refers to a route for which the next hop is not the final destination.  Routes that do not result in traffic forwarding or rejection should not be displayed even if the implementation keeps them stored internally.  reject(2) refers to a route that, if matched, discards the message as unreachable and returns a notification (e.g., ICMP error) to the message sender.  This is used in some protocols as a means of correctly aggregating routes.  blackhole(5) refers to a route that, if matched, discards the message silently
            	**type**\:   :py:class:`Mplsl3VpnvrfrteinetcidrtypeEnum <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable.Mplsl3Vpnvrfrteentry.Mplsl3VpnvrfrteinetcidrtypeEnum>`
            
            .. attribute:: mplsl3vpnvrfrtexcpointer
            
            	Index into mplsXCTable that identifies which cross\- connect entry is associated with this VRF route entry by containing the mplsXCIndex of that cross\-connect entry. The string containing the single\-octet 0x00 indicates that a label stack is not associated with this route entry.  This can be the case because the label bindings have not yet been established, or because some change in the agent has removed them.  When the label stack associated with this VRF route is created, it MUST establish the associated cross\-connect entry in the mplsXCTable and then set that index to the value of this object.  Changes to the cross\-connect object in the mplsXCTable MUST automatically be reflected in the value of this object.  If this object represents a static routing entry, then the manager must ensure that this entry is maintained consistently in the corresponding mplsXCTable as well
            	**type**\:  str
            
            	**length:** 1..24
            
            

            """

            _prefix = 'MPLS-L3VPN-STD-MIB'
            _revision = '2006-01-23'

            def __init__(self):
                self.parent = None
                self.mplsl3vpnvrfname = None
                self.mplsl3vpnvrfrteinetcidrdesttype = None
                self.mplsl3vpnvrfrteinetcidrdest = None
                self.mplsl3vpnvrfrteinetcidrpfxlen = None
                self.mplsl3vpnvrfrteinetcidrpolicy = None
                self.mplsl3vpnvrfrteinetcidrnhoptype = None
                self.mplsl3vpnvrfrteinetcidrnexthop = None
                self.mplsl3vpnvrfrteinetcidrage = None
                self.mplsl3vpnvrfrteinetcidrifindex = None
                self.mplsl3vpnvrfrteinetcidrmetric1 = None
                self.mplsl3vpnvrfrteinetcidrmetric2 = None
                self.mplsl3vpnvrfrteinetcidrmetric3 = None
                self.mplsl3vpnvrfrteinetcidrmetric4 = None
                self.mplsl3vpnvrfrteinetcidrmetric5 = None
                self.mplsl3vpnvrfrteinetcidrnexthopas = None
                self.mplsl3vpnvrfrteinetcidrproto = None
                self.mplsl3vpnvrfrteinetcidrstatus = None
                self.mplsl3vpnvrfrteinetcidrtype = None
                self.mplsl3vpnvrfrtexcpointer = None

            class Mplsl3VpnvrfrteinetcidrtypeEnum(Enum):
                """
                Mplsl3VpnvrfrteinetcidrtypeEnum

                The type of route.  Note that local(3) refers to a

                route for which the next hop is the final destination;

                remote(4) refers to a route for which the next hop is

                not the final destination.

                Routes that do not result in traffic forwarding or

                rejection should not be displayed even if the

                implementation keeps them stored internally.

                reject(2) refers to a route that, if matched, discards

                the message as unreachable and returns a notification

                (e.g., ICMP error) to the message sender.  This is used

                in some protocols as a means of correctly aggregating

                routes.

                blackhole(5) refers to a route that, if matched,

                discards the message silently.

                .. data:: other = 1

                .. data:: reject = 2

                .. data:: local = 3

                .. data:: remote = 4

                .. data:: blackhole = 5

                """

                other = 1

                reject = 2

                local = 3

                remote = 4

                blackhole = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _MPLS_L3VPN_STD_MIB as meta
                    return meta._meta_table['MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable.Mplsl3Vpnvrfrteentry.Mplsl3VpnvrfrteinetcidrtypeEnum']


            @property
            def _common_path(self):
                if self.mplsl3vpnvrfname is None:
                    raise YPYModelError('Key property mplsl3vpnvrfname is None')
                if self.mplsl3vpnvrfrteinetcidrdesttype is None:
                    raise YPYModelError('Key property mplsl3vpnvrfrteinetcidrdesttype is None')
                if self.mplsl3vpnvrfrteinetcidrdest is None:
                    raise YPYModelError('Key property mplsl3vpnvrfrteinetcidrdest is None')
                if self.mplsl3vpnvrfrteinetcidrpfxlen is None:
                    raise YPYModelError('Key property mplsl3vpnvrfrteinetcidrpfxlen is None')
                if self.mplsl3vpnvrfrteinetcidrpolicy is None:
                    raise YPYModelError('Key property mplsl3vpnvrfrteinetcidrpolicy is None')
                if self.mplsl3vpnvrfrteinetcidrnhoptype is None:
                    raise YPYModelError('Key property mplsl3vpnvrfrteinetcidrnhoptype is None')
                if self.mplsl3vpnvrfrteinetcidrnexthop is None:
                    raise YPYModelError('Key property mplsl3vpnvrfrteinetcidrnexthop is None')

                return '/MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/MPLS-L3VPN-STD-MIB:mplsL3VpnVrfRteTable/MPLS-L3VPN-STD-MIB:mplsL3VpnVrfRteEntry[MPLS-L3VPN-STD-MIB:mplsL3VpnVrfName = ' + str(self.mplsl3vpnvrfname) + '][MPLS-L3VPN-STD-MIB:mplsL3VpnVrfRteInetCidrDestType = ' + str(self.mplsl3vpnvrfrteinetcidrdesttype) + '][MPLS-L3VPN-STD-MIB:mplsL3VpnVrfRteInetCidrDest = ' + str(self.mplsl3vpnvrfrteinetcidrdest) + '][MPLS-L3VPN-STD-MIB:mplsL3VpnVrfRteInetCidrPfxLen = ' + str(self.mplsl3vpnvrfrteinetcidrpfxlen) + '][MPLS-L3VPN-STD-MIB:mplsL3VpnVrfRteInetCidrPolicy = ' + str(self.mplsl3vpnvrfrteinetcidrpolicy) + '][MPLS-L3VPN-STD-MIB:mplsL3VpnVrfRteInetCidrNHopType = ' + str(self.mplsl3vpnvrfrteinetcidrnhoptype) + '][MPLS-L3VPN-STD-MIB:mplsL3VpnVrfRteInetCidrNextHop = ' + str(self.mplsl3vpnvrfrteinetcidrnexthop) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mplsl3vpnvrfname is not None:
                    return True

                if self.mplsl3vpnvrfrteinetcidrdesttype is not None:
                    return True

                if self.mplsl3vpnvrfrteinetcidrdest is not None:
                    return True

                if self.mplsl3vpnvrfrteinetcidrpfxlen is not None:
                    return True

                if self.mplsl3vpnvrfrteinetcidrpolicy is not None:
                    return True

                if self.mplsl3vpnvrfrteinetcidrnhoptype is not None:
                    return True

                if self.mplsl3vpnvrfrteinetcidrnexthop is not None:
                    return True

                if self.mplsl3vpnvrfrteinetcidrage is not None:
                    return True

                if self.mplsl3vpnvrfrteinetcidrifindex is not None:
                    return True

                if self.mplsl3vpnvrfrteinetcidrmetric1 is not None:
                    return True

                if self.mplsl3vpnvrfrteinetcidrmetric2 is not None:
                    return True

                if self.mplsl3vpnvrfrteinetcidrmetric3 is not None:
                    return True

                if self.mplsl3vpnvrfrteinetcidrmetric4 is not None:
                    return True

                if self.mplsl3vpnvrfrteinetcidrmetric5 is not None:
                    return True

                if self.mplsl3vpnvrfrteinetcidrnexthopas is not None:
                    return True

                if self.mplsl3vpnvrfrteinetcidrproto is not None:
                    return True

                if self.mplsl3vpnvrfrteinetcidrstatus is not None:
                    return True

                if self.mplsl3vpnvrfrteinetcidrtype is not None:
                    return True

                if self.mplsl3vpnvrfrtexcpointer is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _MPLS_L3VPN_STD_MIB as meta
                return meta._meta_table['MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable.Mplsl3Vpnvrfrteentry']['meta_info']

        @property
        def _common_path(self):

            return '/MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/MPLS-L3VPN-STD-MIB:mplsL3VpnVrfRteTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mplsl3vpnvrfrteentry is not None:
                for child_ref in self.mplsl3vpnvrfrteentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _MPLS_L3VPN_STD_MIB as meta
            return meta._meta_table['MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable']['meta_info']

    @property
    def _common_path(self):

        return '/MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.mplsl3vpnifconftable is not None and self.mplsl3vpnifconftable._has_data():
            return True

        if self.mplsl3vpnscalars is not None and self.mplsl3vpnscalars._has_data():
            return True

        if self.mplsl3vpnvrfrtetable is not None and self.mplsl3vpnvrfrtetable._has_data():
            return True

        if self.mplsl3vpnvrfrttable is not None and self.mplsl3vpnvrfrttable._has_data():
            return True

        if self.mplsl3vpnvrftable is not None and self.mplsl3vpnvrftable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _MPLS_L3VPN_STD_MIB as meta
        return meta._meta_table['MplsL3VpnStdMib']['meta_info']



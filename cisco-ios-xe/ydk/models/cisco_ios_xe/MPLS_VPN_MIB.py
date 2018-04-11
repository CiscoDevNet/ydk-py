""" MPLS_VPN_MIB 

This MIB contains managed object definitions for the
Multiprotocol Label Switching (MPLS)/Border Gateway


Protocol (BGP) Virtual Private Networks (VPNs) as
defined in \: Rosen, E., Viswanathan, A., and R.
Callon, Multiprotocol Label Switching Architecture,
RFC3031, January 2001.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MPLSVPNMIB(Entity):
    """
    
    
    .. attribute:: mplsvpnscalars
    
    	
    	**type**\:  :py:class:`Mplsvpnscalars <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpnscalars>`
    
    .. attribute:: mplsvpninterfaceconftable
    
    	This table specifies per\-interface MPLS capability and associated information
    	**type**\:  :py:class:`Mplsvpninterfaceconftable <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpninterfaceconftable>`
    
    .. attribute:: mplsvpnvrftable
    
    	This table specifies per\-interface MPLS/BGP VPN VRF Table capability and associated information. Entries in this table define VRF routing instances associated with MPLS/VPN interfaces. Note that multiple interfaces can belong to the same VRF instance. The collection of all VRF instances comprises an actual VPN
    	**type**\:  :py:class:`Mplsvpnvrftable <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpnvrftable>`
    
    .. attribute:: mplsvpnvrfroutetargettable
    
    	This table specifies per\-VRF route target association. Each entry identifies a connectivity policy supported as part of a VPN
    	**type**\:  :py:class:`Mplsvpnvrfroutetargettable <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpnvrfroutetargettable>`
    
    .. attribute:: mplsvpnvrfbgpnbraddrtable
    
    	Each entry in this table specifies a per\-interface  MPLS/EBGP neighbor
    	**type**\:  :py:class:`Mplsvpnvrfbgpnbraddrtable <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpnvrfbgpnbraddrtable>`
    
    .. attribute:: mplsvpnvrfbgpnbrprefixtable
    
    	This table specifies per\-VRF vpnv4 multi\-protocol prefixes supported by BGP
    	**type**\:  :py:class:`Mplsvpnvrfbgpnbrprefixtable <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpnvrfbgpnbrprefixtable>`
    
    .. attribute:: mplsvpnvrfroutetable
    
    	This table specifies per\-interface MPLS/BGP VPN VRF Table routing information. Entries in this table define VRF routing entries associated with the specified MPLS/VPN interfaces. Note that this table contains both BGP and IGP routes, as both may appear in the same VRF
    	**type**\:  :py:class:`Mplsvpnvrfroutetable <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpnvrfroutetable>`
    
    

    """

    _prefix = 'MPLS-VPN-MIB'
    _revision = '2001-10-15'

    def __init__(self):
        super(MPLSVPNMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "MPLS-VPN-MIB"
        self.yang_parent_name = "MPLS-VPN-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("mplsVpnScalars", ("mplsvpnscalars", MPLSVPNMIB.Mplsvpnscalars)), ("mplsVpnInterfaceConfTable", ("mplsvpninterfaceconftable", MPLSVPNMIB.Mplsvpninterfaceconftable)), ("mplsVpnVrfTable", ("mplsvpnvrftable", MPLSVPNMIB.Mplsvpnvrftable)), ("mplsVpnVrfRouteTargetTable", ("mplsvpnvrfroutetargettable", MPLSVPNMIB.Mplsvpnvrfroutetargettable)), ("mplsVpnVrfBgpNbrAddrTable", ("mplsvpnvrfbgpnbraddrtable", MPLSVPNMIB.Mplsvpnvrfbgpnbraddrtable)), ("mplsVpnVrfBgpNbrPrefixTable", ("mplsvpnvrfbgpnbrprefixtable", MPLSVPNMIB.Mplsvpnvrfbgpnbrprefixtable)), ("mplsVpnVrfRouteTable", ("mplsvpnvrfroutetable", MPLSVPNMIB.Mplsvpnvrfroutetable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.mplsvpnscalars = MPLSVPNMIB.Mplsvpnscalars()
        self.mplsvpnscalars.parent = self
        self._children_name_map["mplsvpnscalars"] = "mplsVpnScalars"
        self._children_yang_names.add("mplsVpnScalars")

        self.mplsvpninterfaceconftable = MPLSVPNMIB.Mplsvpninterfaceconftable()
        self.mplsvpninterfaceconftable.parent = self
        self._children_name_map["mplsvpninterfaceconftable"] = "mplsVpnInterfaceConfTable"
        self._children_yang_names.add("mplsVpnInterfaceConfTable")

        self.mplsvpnvrftable = MPLSVPNMIB.Mplsvpnvrftable()
        self.mplsvpnvrftable.parent = self
        self._children_name_map["mplsvpnvrftable"] = "mplsVpnVrfTable"
        self._children_yang_names.add("mplsVpnVrfTable")

        self.mplsvpnvrfroutetargettable = MPLSVPNMIB.Mplsvpnvrfroutetargettable()
        self.mplsvpnvrfroutetargettable.parent = self
        self._children_name_map["mplsvpnvrfroutetargettable"] = "mplsVpnVrfRouteTargetTable"
        self._children_yang_names.add("mplsVpnVrfRouteTargetTable")

        self.mplsvpnvrfbgpnbraddrtable = MPLSVPNMIB.Mplsvpnvrfbgpnbraddrtable()
        self.mplsvpnvrfbgpnbraddrtable.parent = self
        self._children_name_map["mplsvpnvrfbgpnbraddrtable"] = "mplsVpnVrfBgpNbrAddrTable"
        self._children_yang_names.add("mplsVpnVrfBgpNbrAddrTable")

        self.mplsvpnvrfbgpnbrprefixtable = MPLSVPNMIB.Mplsvpnvrfbgpnbrprefixtable()
        self.mplsvpnvrfbgpnbrprefixtable.parent = self
        self._children_name_map["mplsvpnvrfbgpnbrprefixtable"] = "mplsVpnVrfBgpNbrPrefixTable"
        self._children_yang_names.add("mplsVpnVrfBgpNbrPrefixTable")

        self.mplsvpnvrfroutetable = MPLSVPNMIB.Mplsvpnvrfroutetable()
        self.mplsvpnvrfroutetable.parent = self
        self._children_name_map["mplsvpnvrfroutetable"] = "mplsVpnVrfRouteTable"
        self._children_yang_names.add("mplsVpnVrfRouteTable")
        self._segment_path = lambda: "MPLS-VPN-MIB:MPLS-VPN-MIB"


    class Mplsvpnscalars(Entity):
        """
        
        
        .. attribute:: mplsvpnconfiguredvrfs
        
        	The number of VRFs which are configured on this node
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplsvpnactivevrfs
        
        	The number of VRFs which are active on this node. That is, those VRFs whose corresponding mplsVpnVrfOperStatus  object value is equal to operational (1)
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplsvpnconnectedinterfaces
        
        	Total number of interfaces connected to a VRF
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplsvpnnotificationenable
        
        	If this object is true, then it enables the generation of all notifications defined in  this MIB
        	**type**\: bool
        
        .. attribute:: mplsvpnvrfconfmaxpossibleroutes
        
        	Denotes maximum number of routes which the device will allow all VRFs jointly to hold. If this value is set to 0, this indicates that the device is  unable to determine the absolute maximum. In this case, the configured maximum MAY not actually be allowed by the device
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'MPLS-VPN-MIB'
        _revision = '2001-10-15'

        def __init__(self):
            super(MPLSVPNMIB.Mplsvpnscalars, self).__init__()

            self.yang_name = "mplsVpnScalars"
            self.yang_parent_name = "MPLS-VPN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('mplsvpnconfiguredvrfs', YLeaf(YType.uint32, 'mplsVpnConfiguredVrfs')),
                ('mplsvpnactivevrfs', YLeaf(YType.uint32, 'mplsVpnActiveVrfs')),
                ('mplsvpnconnectedinterfaces', YLeaf(YType.uint32, 'mplsVpnConnectedInterfaces')),
                ('mplsvpnnotificationenable', YLeaf(YType.boolean, 'mplsVpnNotificationEnable')),
                ('mplsvpnvrfconfmaxpossibleroutes', YLeaf(YType.uint32, 'mplsVpnVrfConfMaxPossibleRoutes')),
            ])
            self.mplsvpnconfiguredvrfs = None
            self.mplsvpnactivevrfs = None
            self.mplsvpnconnectedinterfaces = None
            self.mplsvpnnotificationenable = None
            self.mplsvpnvrfconfmaxpossibleroutes = None
            self._segment_path = lambda: "mplsVpnScalars"
            self._absolute_path = lambda: "MPLS-VPN-MIB:MPLS-VPN-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSVPNMIB.Mplsvpnscalars, ['mplsvpnconfiguredvrfs', 'mplsvpnactivevrfs', 'mplsvpnconnectedinterfaces', 'mplsvpnnotificationenable', 'mplsvpnvrfconfmaxpossibleroutes'], name, value)


    class Mplsvpninterfaceconftable(Entity):
        """
        This table specifies per\-interface MPLS capability
        and associated information.
        
        .. attribute:: mplsvpninterfaceconfentry
        
        	An entry in this table is created by an LSR for every interface capable of supporting MPLS/BGP VPN.   Each entry in this table is meant to correspond to an entry in the Interfaces Table
        	**type**\: list of  		 :py:class:`Mplsvpninterfaceconfentry <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry>`
        
        

        """

        _prefix = 'MPLS-VPN-MIB'
        _revision = '2001-10-15'

        def __init__(self):
            super(MPLSVPNMIB.Mplsvpninterfaceconftable, self).__init__()

            self.yang_name = "mplsVpnInterfaceConfTable"
            self.yang_parent_name = "MPLS-VPN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("mplsVpnInterfaceConfEntry", ("mplsvpninterfaceconfentry", MPLSVPNMIB.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry))])
            self._leafs = OrderedDict()

            self.mplsvpninterfaceconfentry = YList(self)
            self._segment_path = lambda: "mplsVpnInterfaceConfTable"
            self._absolute_path = lambda: "MPLS-VPN-MIB:MPLS-VPN-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSVPNMIB.Mplsvpninterfaceconftable, [], name, value)


        class Mplsvpninterfaceconfentry(Entity):
            """
            An entry in this table is created by an LSR for
            every interface capable of supporting MPLS/BGP VPN.
            
            
            Each entry in this table is meant to correspond to
            an entry in the Interfaces Table.
            
            .. attribute:: mplsvpnvrfname  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..31
            
            	**refers to**\:  :py:class:`mplsvpnvrfname <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpnvrftable.Mplsvpnvrfentry>`
            
            .. attribute:: mplsvpninterfaceconfindex  (key)
            
            	This is a unique index for an entry in the MplsVPNInterfaceConfTable. A non\-zero index for an entry indicates the ifIndex for the corresponding interface entry in the MPLS\-VPN\-layer in the ifTable. Note that this table does not necessarily correspond one\-to\-one with all entries in the Interface MIB having an ifType of MPLS\-layer; rather, only those which are enabled for MPLS/BGP VPN functionality
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: mplsvpninterfacelabeledgetype
            
            	Either the providerEdge(0) (PE) or customerEdge(1) (CE) bit MUST be set
            	**type**\:  :py:class:`Mplsvpninterfacelabeledgetype <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry.Mplsvpninterfacelabeledgetype>`
            
            .. attribute:: mplsvpninterfacevpnclassification
            
            	Denotes whether this link participates in a carrier\-of\-carrier's, enterprise, or inter\-provider scenario
            	**type**\:  :py:class:`Mplsvpninterfacevpnclassification <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry.Mplsvpninterfacevpnclassification>`
            
            .. attribute:: mplsvpninterfacevpnroutedistprotocol
            
            	Denotes the route distribution protocol across the PE\-CE link. Note that more than one routing protocol may be enabled at the same time
            	**type**\:  :py:class:`Mplsvpninterfacevpnroutedistprotocol <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry.Mplsvpninterfacevpnroutedistprotocol>`
            
            .. attribute:: mplsvpninterfaceconfstoragetype
            
            	The storage type for this entry
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: mplsvpninterfaceconfrowstatus
            
            	The row status for this entry. This value is used to create a row in this table, signifying that the specified interface is to be associated with the specified interface. If this operation succeeds, the interface will have been associated, otherwise the agent would not allow the association.  If the agent only allows read\-only operations on this table, it will create entries in this table as they are created
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'MPLS-VPN-MIB'
            _revision = '2001-10-15'

            def __init__(self):
                super(MPLSVPNMIB.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry, self).__init__()

                self.yang_name = "mplsVpnInterfaceConfEntry"
                self.yang_parent_name = "mplsVpnInterfaceConfTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mplsvpnvrfname','mplsvpninterfaceconfindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mplsvpnvrfname', YLeaf(YType.str, 'mplsVpnVrfName')),
                    ('mplsvpninterfaceconfindex', YLeaf(YType.int32, 'mplsVpnInterfaceConfIndex')),
                    ('mplsvpninterfacelabeledgetype', YLeaf(YType.enumeration, 'mplsVpnInterfaceLabelEdgeType')),
                    ('mplsvpninterfacevpnclassification', YLeaf(YType.enumeration, 'mplsVpnInterfaceVpnClassification')),
                    ('mplsvpninterfacevpnroutedistprotocol', YLeaf(YType.bits, 'mplsVpnInterfaceVpnRouteDistProtocol')),
                    ('mplsvpninterfaceconfstoragetype', YLeaf(YType.enumeration, 'mplsVpnInterfaceConfStorageType')),
                    ('mplsvpninterfaceconfrowstatus', YLeaf(YType.enumeration, 'mplsVpnInterfaceConfRowStatus')),
                ])
                self.mplsvpnvrfname = None
                self.mplsvpninterfaceconfindex = None
                self.mplsvpninterfacelabeledgetype = None
                self.mplsvpninterfacevpnclassification = None
                self.mplsvpninterfacevpnroutedistprotocol = Bits()
                self.mplsvpninterfaceconfstoragetype = None
                self.mplsvpninterfaceconfrowstatus = None
                self._segment_path = lambda: "mplsVpnInterfaceConfEntry" + "[mplsVpnVrfName='" + str(self.mplsvpnvrfname) + "']" + "[mplsVpnInterfaceConfIndex='" + str(self.mplsvpninterfaceconfindex) + "']"
                self._absolute_path = lambda: "MPLS-VPN-MIB:MPLS-VPN-MIB/mplsVpnInterfaceConfTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MPLSVPNMIB.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry, ['mplsvpnvrfname', 'mplsvpninterfaceconfindex', 'mplsvpninterfacelabeledgetype', 'mplsvpninterfacevpnclassification', 'mplsvpninterfacevpnroutedistprotocol', 'mplsvpninterfaceconfstoragetype', 'mplsvpninterfaceconfrowstatus'], name, value)

            class Mplsvpninterfacelabeledgetype(Enum):
                """
                Mplsvpninterfacelabeledgetype (Enum Class)

                Either the providerEdge(0) (PE) or customerEdge(1)

                (CE) bit MUST be set.

                .. data:: providerEdge = 1

                .. data:: customerEdge = 2

                """

                providerEdge = Enum.YLeaf(1, "providerEdge")

                customerEdge = Enum.YLeaf(2, "customerEdge")


            class Mplsvpninterfacevpnclassification(Enum):
                """
                Mplsvpninterfacevpnclassification (Enum Class)

                Denotes whether this link participates in a

                carrier\-of\-carrier's, enterprise, or inter\-provider

                scenario.

                .. data:: carrierOfCarrier = 1

                .. data:: enterprise = 2

                .. data:: interProvider = 3

                """

                carrierOfCarrier = Enum.YLeaf(1, "carrierOfCarrier")

                enterprise = Enum.YLeaf(2, "enterprise")

                interProvider = Enum.YLeaf(3, "interProvider")



    class Mplsvpnvrftable(Entity):
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
        	**type**\: list of  		 :py:class:`Mplsvpnvrfentry <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpnvrftable.Mplsvpnvrfentry>`
        
        

        """

        _prefix = 'MPLS-VPN-MIB'
        _revision = '2001-10-15'

        def __init__(self):
            super(MPLSVPNMIB.Mplsvpnvrftable, self).__init__()

            self.yang_name = "mplsVpnVrfTable"
            self.yang_parent_name = "MPLS-VPN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("mplsVpnVrfEntry", ("mplsvpnvrfentry", MPLSVPNMIB.Mplsvpnvrftable.Mplsvpnvrfentry))])
            self._leafs = OrderedDict()

            self.mplsvpnvrfentry = YList(self)
            self._segment_path = lambda: "mplsVpnVrfTable"
            self._absolute_path = lambda: "MPLS-VPN-MIB:MPLS-VPN-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSVPNMIB.Mplsvpnvrftable, [], name, value)


        class Mplsvpnvrfentry(Entity):
            """
            An entry in this table is created by an LSR for
            every VRF capable of supporting MPLS/BGP VPN. The
            indexing provides an ordering of VRFs per\-VPN
            interface.
            
            .. attribute:: mplsvpnvrfname  (key)
            
            	The human\-readable name of this VPN. This MAY be equivalent to the RFC2685 VPN\-ID
            	**type**\: str
            
            	**length:** 0..31
            
            .. attribute:: mplsvpnvrfdescription
            
            	The human\-readable description of this VRF
            	**type**\: str
            
            .. attribute:: mplsvpnvrfroutedistinguisher
            
            	The route distinguisher for this VRF
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: mplsvpnvrfcreationtime
            
            	The time at which this VRF entry was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfoperstatus
            
            	Denotes whether a VRF is operational or not. A VRF is  up(1) when at least one interface associated with the VRF, which ifOperStatus is up(1). A VRF is down(2) when\:  a. There does not exist at least one interface whose    ifOperStatus is up(1).  b. There are no interfaces associated with the VRF
            	**type**\:  :py:class:`Mplsvpnvrfoperstatus <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpnvrftable.Mplsvpnvrfentry.Mplsvpnvrfoperstatus>`
            
            .. attribute:: mplsvpnvrfactiveinterfaces
            
            	Total number of interfaces connected to this VRF with    ifOperStatus = up(1).   This counter should be incremented when\:  a. When the ifOperStatus of one of the connected interfaces     changes from down(2) to up(1).  b. When an interface with ifOperStatus = up(1) is connected    to this VRF.  This counter should be decremented when\:  a. When the ifOperStatus of one of the connected interfaces     changes from up(1) to down(2).  b. When one of the connected interfaces with     ifOperStatus = up(1) gets disconnected from this VRF
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfassociatedinterfaces
            
            	Total number of interfaces connected to this VRF  (independent of ifOperStatus type)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfconfmidroutethreshold
            
            	Denotes mid\-level water marker for the number of routes which  this VRF may hold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfconfhighroutethreshold
            
            	Denotes high\-level water marker for the number of routes which  this VRF may hold
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfconfmaxroutes
            
            	Denotes maximum number of routes which this VRF is configured to hold. This value MUST be less than or equal to mplsVrfMaxPossibleRoutes unless it is set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfconflastchanged
            
            	The value of sysUpTime at the time of the last change of this table entry, which includes changes of VRF parameters defined in this table or addition or deletion of interfaces associated with this VRF
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfconfrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: mplsvpnvrfconfstoragetype
            
            	The storage type for this entry
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: mplsvpnvrfsecillegallabelviolations
            
            	Indicates the number of illegally received labels on this VPN/VRF
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfsecillegallabelrcvthresh
            
            	The number of illegally received labels above which this  notification is issued
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfperfroutesadded
            
            	Indicates the number of routes added to this VPN/VRF over the coarse of its lifetime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfperfroutesdeleted
            
            	Indicates the number of routes removed from this VPN/VRF
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfperfcurrnumroutes
            
            	Indicates the number of routes currently used by this VRF
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'MPLS-VPN-MIB'
            _revision = '2001-10-15'

            def __init__(self):
                super(MPLSVPNMIB.Mplsvpnvrftable.Mplsvpnvrfentry, self).__init__()

                self.yang_name = "mplsVpnVrfEntry"
                self.yang_parent_name = "mplsVpnVrfTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mplsvpnvrfname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mplsvpnvrfname', YLeaf(YType.str, 'mplsVpnVrfName')),
                    ('mplsvpnvrfdescription', YLeaf(YType.str, 'mplsVpnVrfDescription')),
                    ('mplsvpnvrfroutedistinguisher', YLeaf(YType.str, 'mplsVpnVrfRouteDistinguisher')),
                    ('mplsvpnvrfcreationtime', YLeaf(YType.uint32, 'mplsVpnVrfCreationTime')),
                    ('mplsvpnvrfoperstatus', YLeaf(YType.enumeration, 'mplsVpnVrfOperStatus')),
                    ('mplsvpnvrfactiveinterfaces', YLeaf(YType.uint32, 'mplsVpnVrfActiveInterfaces')),
                    ('mplsvpnvrfassociatedinterfaces', YLeaf(YType.uint32, 'mplsVpnVrfAssociatedInterfaces')),
                    ('mplsvpnvrfconfmidroutethreshold', YLeaf(YType.uint32, 'mplsVpnVrfConfMidRouteThreshold')),
                    ('mplsvpnvrfconfhighroutethreshold', YLeaf(YType.uint32, 'mplsVpnVrfConfHighRouteThreshold')),
                    ('mplsvpnvrfconfmaxroutes', YLeaf(YType.uint32, 'mplsVpnVrfConfMaxRoutes')),
                    ('mplsvpnvrfconflastchanged', YLeaf(YType.uint32, 'mplsVpnVrfConfLastChanged')),
                    ('mplsvpnvrfconfrowstatus', YLeaf(YType.enumeration, 'mplsVpnVrfConfRowStatus')),
                    ('mplsvpnvrfconfstoragetype', YLeaf(YType.enumeration, 'mplsVpnVrfConfStorageType')),
                    ('mplsvpnvrfsecillegallabelviolations', YLeaf(YType.uint32, 'mplsVpnVrfSecIllegalLabelViolations')),
                    ('mplsvpnvrfsecillegallabelrcvthresh', YLeaf(YType.uint32, 'mplsVpnVrfSecIllegalLabelRcvThresh')),
                    ('mplsvpnvrfperfroutesadded', YLeaf(YType.uint32, 'mplsVpnVrfPerfRoutesAdded')),
                    ('mplsvpnvrfperfroutesdeleted', YLeaf(YType.uint32, 'mplsVpnVrfPerfRoutesDeleted')),
                    ('mplsvpnvrfperfcurrnumroutes', YLeaf(YType.uint32, 'mplsVpnVrfPerfCurrNumRoutes')),
                ])
                self.mplsvpnvrfname = None
                self.mplsvpnvrfdescription = None
                self.mplsvpnvrfroutedistinguisher = None
                self.mplsvpnvrfcreationtime = None
                self.mplsvpnvrfoperstatus = None
                self.mplsvpnvrfactiveinterfaces = None
                self.mplsvpnvrfassociatedinterfaces = None
                self.mplsvpnvrfconfmidroutethreshold = None
                self.mplsvpnvrfconfhighroutethreshold = None
                self.mplsvpnvrfconfmaxroutes = None
                self.mplsvpnvrfconflastchanged = None
                self.mplsvpnvrfconfrowstatus = None
                self.mplsvpnvrfconfstoragetype = None
                self.mplsvpnvrfsecillegallabelviolations = None
                self.mplsvpnvrfsecillegallabelrcvthresh = None
                self.mplsvpnvrfperfroutesadded = None
                self.mplsvpnvrfperfroutesdeleted = None
                self.mplsvpnvrfperfcurrnumroutes = None
                self._segment_path = lambda: "mplsVpnVrfEntry" + "[mplsVpnVrfName='" + str(self.mplsvpnvrfname) + "']"
                self._absolute_path = lambda: "MPLS-VPN-MIB:MPLS-VPN-MIB/mplsVpnVrfTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MPLSVPNMIB.Mplsvpnvrftable.Mplsvpnvrfentry, ['mplsvpnvrfname', 'mplsvpnvrfdescription', 'mplsvpnvrfroutedistinguisher', 'mplsvpnvrfcreationtime', 'mplsvpnvrfoperstatus', 'mplsvpnvrfactiveinterfaces', 'mplsvpnvrfassociatedinterfaces', 'mplsvpnvrfconfmidroutethreshold', 'mplsvpnvrfconfhighroutethreshold', 'mplsvpnvrfconfmaxroutes', 'mplsvpnvrfconflastchanged', 'mplsvpnvrfconfrowstatus', 'mplsvpnvrfconfstoragetype', 'mplsvpnvrfsecillegallabelviolations', 'mplsvpnvrfsecillegallabelrcvthresh', 'mplsvpnvrfperfroutesadded', 'mplsvpnvrfperfroutesdeleted', 'mplsvpnvrfperfcurrnumroutes'], name, value)

            class Mplsvpnvrfoperstatus(Enum):
                """
                Mplsvpnvrfoperstatus (Enum Class)

                Denotes whether a VRF is operational or not. A VRF is 

                up(1) when at least one interface associated with the

                VRF, which ifOperStatus is up(1). A VRF is down(2) when\:

                a. There does not exist at least one interface whose

                   ifOperStatus is up(1).

                b. There are no interfaces associated with the VRF.

                .. data:: up = 1

                .. data:: down = 2

                """

                up = Enum.YLeaf(1, "up")

                down = Enum.YLeaf(2, "down")



    class Mplsvpnvrfroutetargettable(Entity):
        """
        This table specifies per\-VRF route target association.
        Each entry identifies a connectivity policy supported
        as part of a VPN.
        
        .. attribute:: mplsvpnvrfroutetargetentry
        
        	 An entry in this table is created by an LSR for each route target configured for a VRF supporting a MPLS/BGP VPN instance. The indexing provides an ordering per\-VRF instance
        	**type**\: list of  		 :py:class:`Mplsvpnvrfroutetargetentry <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpnvrfroutetargettable.Mplsvpnvrfroutetargetentry>`
        
        

        """

        _prefix = 'MPLS-VPN-MIB'
        _revision = '2001-10-15'

        def __init__(self):
            super(MPLSVPNMIB.Mplsvpnvrfroutetargettable, self).__init__()

            self.yang_name = "mplsVpnVrfRouteTargetTable"
            self.yang_parent_name = "MPLS-VPN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("mplsVpnVrfRouteTargetEntry", ("mplsvpnvrfroutetargetentry", MPLSVPNMIB.Mplsvpnvrfroutetargettable.Mplsvpnvrfroutetargetentry))])
            self._leafs = OrderedDict()

            self.mplsvpnvrfroutetargetentry = YList(self)
            self._segment_path = lambda: "mplsVpnVrfRouteTargetTable"
            self._absolute_path = lambda: "MPLS-VPN-MIB:MPLS-VPN-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSVPNMIB.Mplsvpnvrfroutetargettable, [], name, value)


        class Mplsvpnvrfroutetargetentry(Entity):
            """
             An entry in this table is created by an LSR for
            each route target configured for a VRF supporting
            a MPLS/BGP VPN instance. The indexing provides an
            ordering per\-VRF instance.
            
            .. attribute:: mplsvpnvrfname  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..31
            
            	**refers to**\:  :py:class:`mplsvpnvrfname <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpnvrftable.Mplsvpnvrfentry>`
            
            .. attribute:: mplsvpnvrfroutetargetindex  (key)
            
            	Auxiliary index for route\-targets configured for a  particular VRF
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfroutetargettype  (key)
            
            	The route target export distribution type
            	**type**\:  :py:class:`Mplsvpnvrfroutetargettype <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpnvrfroutetargettable.Mplsvpnvrfroutetargetentry.Mplsvpnvrfroutetargettype>`
            
            .. attribute:: mplsvpnvrfroutetarget
            
            	The route target distribution policy
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: mplsvpnvrfroutetargetdescr
            
            	Description of the route target
            	**type**\: str
            
            .. attribute:: mplsvpnvrfroutetargetrowstatus
            
            	Row status for this entry
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'MPLS-VPN-MIB'
            _revision = '2001-10-15'

            def __init__(self):
                super(MPLSVPNMIB.Mplsvpnvrfroutetargettable.Mplsvpnvrfroutetargetentry, self).__init__()

                self.yang_name = "mplsVpnVrfRouteTargetEntry"
                self.yang_parent_name = "mplsVpnVrfRouteTargetTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mplsvpnvrfname','mplsvpnvrfroutetargetindex','mplsvpnvrfroutetargettype']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mplsvpnvrfname', YLeaf(YType.str, 'mplsVpnVrfName')),
                    ('mplsvpnvrfroutetargetindex', YLeaf(YType.uint32, 'mplsVpnVrfRouteTargetIndex')),
                    ('mplsvpnvrfroutetargettype', YLeaf(YType.enumeration, 'mplsVpnVrfRouteTargetType')),
                    ('mplsvpnvrfroutetarget', YLeaf(YType.str, 'mplsVpnVrfRouteTarget')),
                    ('mplsvpnvrfroutetargetdescr', YLeaf(YType.str, 'mplsVpnVrfRouteTargetDescr')),
                    ('mplsvpnvrfroutetargetrowstatus', YLeaf(YType.enumeration, 'mplsVpnVrfRouteTargetRowStatus')),
                ])
                self.mplsvpnvrfname = None
                self.mplsvpnvrfroutetargetindex = None
                self.mplsvpnvrfroutetargettype = None
                self.mplsvpnvrfroutetarget = None
                self.mplsvpnvrfroutetargetdescr = None
                self.mplsvpnvrfroutetargetrowstatus = None
                self._segment_path = lambda: "mplsVpnVrfRouteTargetEntry" + "[mplsVpnVrfName='" + str(self.mplsvpnvrfname) + "']" + "[mplsVpnVrfRouteTargetIndex='" + str(self.mplsvpnvrfroutetargetindex) + "']" + "[mplsVpnVrfRouteTargetType='" + str(self.mplsvpnvrfroutetargettype) + "']"
                self._absolute_path = lambda: "MPLS-VPN-MIB:MPLS-VPN-MIB/mplsVpnVrfRouteTargetTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MPLSVPNMIB.Mplsvpnvrfroutetargettable.Mplsvpnvrfroutetargetentry, ['mplsvpnvrfname', 'mplsvpnvrfroutetargetindex', 'mplsvpnvrfroutetargettype', 'mplsvpnvrfroutetarget', 'mplsvpnvrfroutetargetdescr', 'mplsvpnvrfroutetargetrowstatus'], name, value)

            class Mplsvpnvrfroutetargettype(Enum):
                """
                Mplsvpnvrfroutetargettype (Enum Class)

                The route target export distribution type.

                .. data:: import_ = 1

                .. data:: export = 2

                .. data:: both = 3

                """

                import_ = Enum.YLeaf(1, "import")

                export = Enum.YLeaf(2, "export")

                both = Enum.YLeaf(3, "both")



    class Mplsvpnvrfbgpnbraddrtable(Entity):
        """
        Each entry in this table specifies a per\-interface 
        MPLS/EBGP neighbor.
        
        .. attribute:: mplsvpnvrfbgpnbraddrentry
        
        	An entry in this table is created by an LSR for every VRF capable of supporting MPLS/BGP VPN. The indexing provides an ordering of VRFs per\-VPN interface
        	**type**\: list of  		 :py:class:`Mplsvpnvrfbgpnbraddrentry <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpnvrfbgpnbraddrtable.Mplsvpnvrfbgpnbraddrentry>`
        
        

        """

        _prefix = 'MPLS-VPN-MIB'
        _revision = '2001-10-15'

        def __init__(self):
            super(MPLSVPNMIB.Mplsvpnvrfbgpnbraddrtable, self).__init__()

            self.yang_name = "mplsVpnVrfBgpNbrAddrTable"
            self.yang_parent_name = "MPLS-VPN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("mplsVpnVrfBgpNbrAddrEntry", ("mplsvpnvrfbgpnbraddrentry", MPLSVPNMIB.Mplsvpnvrfbgpnbraddrtable.Mplsvpnvrfbgpnbraddrentry))])
            self._leafs = OrderedDict()

            self.mplsvpnvrfbgpnbraddrentry = YList(self)
            self._segment_path = lambda: "mplsVpnVrfBgpNbrAddrTable"
            self._absolute_path = lambda: "MPLS-VPN-MIB:MPLS-VPN-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSVPNMIB.Mplsvpnvrfbgpnbraddrtable, [], name, value)


        class Mplsvpnvrfbgpnbraddrentry(Entity):
            """
            An entry in this table is created by an LSR for
            every VRF capable of supporting MPLS/BGP VPN. The
            indexing provides an ordering of VRFs per\-VPN
            interface.
            
            .. attribute:: mplsvpnvrfname  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..31
            
            	**refers to**\:  :py:class:`mplsvpnvrfname <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpnvrftable.Mplsvpnvrfentry>`
            
            .. attribute:: mplsvpninterfaceconfindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`mplsvpninterfaceconfindex <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry>`
            
            .. attribute:: mplsvpnvrfbgpnbrindex  (key)
            
            	This is a unique tertiary index for an entry in the MplsVpnVrfBgpNbrAddrEntry Table
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfbgpnbrrole
            
            	Denotes the role played by this EBGP neighbor with respect to this VRF
            	**type**\:  :py:class:`Mplsvpnvrfbgpnbrrole <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpnvrfbgpnbraddrtable.Mplsvpnvrfbgpnbraddrentry.Mplsvpnvrfbgpnbrrole>`
            
            .. attribute:: mplsvpnvrfbgpnbrtype
            
            	Denotes the address family of the PE address
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: mplsvpnvrfbgpnbraddr
            
            	Denotes the EBGP neighbor address
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: mplsvpnvrfbgpnbrrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: mplsvpnvrfbgpnbrstoragetype
            
            	The storage type for this entry
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            

            """

            _prefix = 'MPLS-VPN-MIB'
            _revision = '2001-10-15'

            def __init__(self):
                super(MPLSVPNMIB.Mplsvpnvrfbgpnbraddrtable.Mplsvpnvrfbgpnbraddrentry, self).__init__()

                self.yang_name = "mplsVpnVrfBgpNbrAddrEntry"
                self.yang_parent_name = "mplsVpnVrfBgpNbrAddrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mplsvpnvrfname','mplsvpninterfaceconfindex','mplsvpnvrfbgpnbrindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mplsvpnvrfname', YLeaf(YType.str, 'mplsVpnVrfName')),
                    ('mplsvpninterfaceconfindex', YLeaf(YType.str, 'mplsVpnInterfaceConfIndex')),
                    ('mplsvpnvrfbgpnbrindex', YLeaf(YType.uint32, 'mplsVpnVrfBgpNbrIndex')),
                    ('mplsvpnvrfbgpnbrrole', YLeaf(YType.enumeration, 'mplsVpnVrfBgpNbrRole')),
                    ('mplsvpnvrfbgpnbrtype', YLeaf(YType.enumeration, 'mplsVpnVrfBgpNbrType')),
                    ('mplsvpnvrfbgpnbraddr', YLeaf(YType.str, 'mplsVpnVrfBgpNbrAddr')),
                    ('mplsvpnvrfbgpnbrrowstatus', YLeaf(YType.enumeration, 'mplsVpnVrfBgpNbrRowStatus')),
                    ('mplsvpnvrfbgpnbrstoragetype', YLeaf(YType.enumeration, 'mplsVpnVrfBgpNbrStorageType')),
                ])
                self.mplsvpnvrfname = None
                self.mplsvpninterfaceconfindex = None
                self.mplsvpnvrfbgpnbrindex = None
                self.mplsvpnvrfbgpnbrrole = None
                self.mplsvpnvrfbgpnbrtype = None
                self.mplsvpnvrfbgpnbraddr = None
                self.mplsvpnvrfbgpnbrrowstatus = None
                self.mplsvpnvrfbgpnbrstoragetype = None
                self._segment_path = lambda: "mplsVpnVrfBgpNbrAddrEntry" + "[mplsVpnVrfName='" + str(self.mplsvpnvrfname) + "']" + "[mplsVpnInterfaceConfIndex='" + str(self.mplsvpninterfaceconfindex) + "']" + "[mplsVpnVrfBgpNbrIndex='" + str(self.mplsvpnvrfbgpnbrindex) + "']"
                self._absolute_path = lambda: "MPLS-VPN-MIB:MPLS-VPN-MIB/mplsVpnVrfBgpNbrAddrTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MPLSVPNMIB.Mplsvpnvrfbgpnbraddrtable.Mplsvpnvrfbgpnbraddrentry, ['mplsvpnvrfname', 'mplsvpninterfaceconfindex', 'mplsvpnvrfbgpnbrindex', 'mplsvpnvrfbgpnbrrole', 'mplsvpnvrfbgpnbrtype', 'mplsvpnvrfbgpnbraddr', 'mplsvpnvrfbgpnbrrowstatus', 'mplsvpnvrfbgpnbrstoragetype'], name, value)

            class Mplsvpnvrfbgpnbrrole(Enum):
                """
                Mplsvpnvrfbgpnbrrole (Enum Class)

                Denotes the role played by this EBGP neighbor

                with respect to this VRF.

                .. data:: ce = 1

                .. data:: pe = 2

                """

                ce = Enum.YLeaf(1, "ce")

                pe = Enum.YLeaf(2, "pe")



    class Mplsvpnvrfbgpnbrprefixtable(Entity):
        """
        This table specifies per\-VRF vpnv4 multi\-protocol
        prefixes supported by BGP.
        
        .. attribute:: mplsvpnvrfbgpnbrprefixentry
        
        	An entry in this table is created by an LSR for every BGP prefix associated with a VRF supporting a  MPLS/BGP VPN. The indexing provides an ordering of  BGP prefixes per VRF
        	**type**\: list of  		 :py:class:`Mplsvpnvrfbgpnbrprefixentry <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry>`
        
        

        """

        _prefix = 'MPLS-VPN-MIB'
        _revision = '2001-10-15'

        def __init__(self):
            super(MPLSVPNMIB.Mplsvpnvrfbgpnbrprefixtable, self).__init__()

            self.yang_name = "mplsVpnVrfBgpNbrPrefixTable"
            self.yang_parent_name = "MPLS-VPN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("mplsVpnVrfBgpNbrPrefixEntry", ("mplsvpnvrfbgpnbrprefixentry", MPLSVPNMIB.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry))])
            self._leafs = OrderedDict()

            self.mplsvpnvrfbgpnbrprefixentry = YList(self)
            self._segment_path = lambda: "mplsVpnVrfBgpNbrPrefixTable"
            self._absolute_path = lambda: "MPLS-VPN-MIB:MPLS-VPN-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSVPNMIB.Mplsvpnvrfbgpnbrprefixtable, [], name, value)


        class Mplsvpnvrfbgpnbrprefixentry(Entity):
            """
            An entry in this table is created by an LSR for
            every BGP prefix associated with a VRF supporting a 
            MPLS/BGP VPN. The indexing provides an ordering of 
            BGP prefixes per VRF.
            
            .. attribute:: mplsvpnvrfname  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..31
            
            	**refers to**\:  :py:class:`mplsvpnvrfname <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpnvrftable.Mplsvpnvrfentry>`
            
            .. attribute:: mplsvpnvrfbgppathattripaddrprefix  (key)
            
            	An IP address prefix in the Network Layer Reachability Information field.  This object is an IP address containing the prefix with length specified by mplsVpnVrfBgpPathAttrIpAddrPrefixLen. Any bits beyond the length specified by mplsVpnVrfBgpPathAttrIpAddrPrefixLen are zeroed
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: mplsvpnvrfbgppathattripaddrprefixlen  (key)
            
            	Length in bits of the IP address prefix in the Network Layer Reachability Information field
            	**type**\: int
            
            	**range:** 0..32
            
            .. attribute:: mplsvpnvrfbgppathattrpeer  (key)
            
            	The IP address of the peer where the path information was learned
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: mplsvpnvrfbgppathattrorigin
            
            	The ultimate origin of the path information
            	**type**\:  :py:class:`Mplsvpnvrfbgppathattrorigin <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry.Mplsvpnvrfbgppathattrorigin>`
            
            .. attribute:: mplsvpnvrfbgppathattraspathsegment
            
            	The sequence of AS path segments.  Each AS path segment is represented by a triple <type, length, value>.   The type is a 1\-octet field which has two  possible values\:      1      AS\_SET\: unordered set of ASs a             route in the UPDATE             message has traversed      2      AS\_SEQUENCE\: ordered set of ASs             a route in the UPDATE             message has traversed.             The length is a 1\-octet field containing the               number of ASs in the value field.              The value field contains one or more AS             numbers, each AS is represented in the octet             string as a pair of octets according to the             following algorithm\:              first\-byte\-of\-pair = ASNumber / 256;             second\-byte\-of\-pair = ASNumber & 255;
            	**type**\: str
            
            	**length:** 2..255
            
            .. attribute:: mplsvpnvrfbgppathattrnexthop
            
            	The address of the border router that should be used for the destination network
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: mplsvpnvrfbgppathattrmultiexitdisc
            
            	This metric is used to discriminate between multiple exit points to an adjacent autonomous system.  A value of \-1 indicates the absence of this attribute
            	**type**\: int
            
            	**range:** \-1..2147483647
            
            .. attribute:: mplsvpnvrfbgppathattrlocalpref
            
            	The originating BGP4 speaker's degree of preference for an advertised route.  A value of \-1 indicates the absence of this attribute
            	**type**\: int
            
            	**range:** \-1..2147483647
            
            .. attribute:: mplsvpnvrfbgppathattratomicaggregate
            
            	Whether or not the local system has selected a less specific route without selecting a more specific route
            	**type**\:  :py:class:`Mplsvpnvrfbgppathattratomicaggregate <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry.Mplsvpnvrfbgppathattratomicaggregate>`
            
            .. attribute:: mplsvpnvrfbgppathattraggregatoras
            
            	The AS number of the last BGP4 speaker that performed route aggregation.  A value of zero (0) indicates the absence of this attribute
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: mplsvpnvrfbgppathattraggregatoraddr
            
            	The IP address of the last BGP4 speaker that performed route aggregation.  A value of 0.0.0.0 indicates the absence of this attribute
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: mplsvpnvrfbgppathattrcalclocalpref
            
            	The degree of preference calculated by the receiving BGP4 speaker for an advertised route.  A value of \-1 indicates the absence of this attribute
            	**type**\: int
            
            	**range:** \-1..2147483647
            
            .. attribute:: mplsvpnvrfbgppathattrbest
            
            	An indication of whether or not this route was chosen as the best BGP4 route
            	**type**\:  :py:class:`Mplsvpnvrfbgppathattrbest <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry.Mplsvpnvrfbgppathattrbest>`
            
            .. attribute:: mplsvpnvrfbgppathattrunknown
            
            	One or more path attributes not understood by this BGP4 speaker.  Size zero (0) indicates the absence of such attribute(s).  Octets beyond the maximum size, if any, are not recorded by this object
            	**type**\: str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'MPLS-VPN-MIB'
            _revision = '2001-10-15'

            def __init__(self):
                super(MPLSVPNMIB.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry, self).__init__()

                self.yang_name = "mplsVpnVrfBgpNbrPrefixEntry"
                self.yang_parent_name = "mplsVpnVrfBgpNbrPrefixTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mplsvpnvrfname','mplsvpnvrfbgppathattripaddrprefix','mplsvpnvrfbgppathattripaddrprefixlen','mplsvpnvrfbgppathattrpeer']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mplsvpnvrfname', YLeaf(YType.str, 'mplsVpnVrfName')),
                    ('mplsvpnvrfbgppathattripaddrprefix', YLeaf(YType.str, 'mplsVpnVrfBgpPathAttrIpAddrPrefix')),
                    ('mplsvpnvrfbgppathattripaddrprefixlen', YLeaf(YType.int32, 'mplsVpnVrfBgpPathAttrIpAddrPrefixLen')),
                    ('mplsvpnvrfbgppathattrpeer', YLeaf(YType.str, 'mplsVpnVrfBgpPathAttrPeer')),
                    ('mplsvpnvrfbgppathattrorigin', YLeaf(YType.enumeration, 'mplsVpnVrfBgpPathAttrOrigin')),
                    ('mplsvpnvrfbgppathattraspathsegment', YLeaf(YType.str, 'mplsVpnVrfBgpPathAttrASPathSegment')),
                    ('mplsvpnvrfbgppathattrnexthop', YLeaf(YType.str, 'mplsVpnVrfBgpPathAttrNextHop')),
                    ('mplsvpnvrfbgppathattrmultiexitdisc', YLeaf(YType.int32, 'mplsVpnVrfBgpPathAttrMultiExitDisc')),
                    ('mplsvpnvrfbgppathattrlocalpref', YLeaf(YType.int32, 'mplsVpnVrfBgpPathAttrLocalPref')),
                    ('mplsvpnvrfbgppathattratomicaggregate', YLeaf(YType.enumeration, 'mplsVpnVrfBgpPathAttrAtomicAggregate')),
                    ('mplsvpnvrfbgppathattraggregatoras', YLeaf(YType.int32, 'mplsVpnVrfBgpPathAttrAggregatorAS')),
                    ('mplsvpnvrfbgppathattraggregatoraddr', YLeaf(YType.str, 'mplsVpnVrfBgpPathAttrAggregatorAddr')),
                    ('mplsvpnvrfbgppathattrcalclocalpref', YLeaf(YType.int32, 'mplsVpnVrfBgpPathAttrCalcLocalPref')),
                    ('mplsvpnvrfbgppathattrbest', YLeaf(YType.enumeration, 'mplsVpnVrfBgpPathAttrBest')),
                    ('mplsvpnvrfbgppathattrunknown', YLeaf(YType.str, 'mplsVpnVrfBgpPathAttrUnknown')),
                ])
                self.mplsvpnvrfname = None
                self.mplsvpnvrfbgppathattripaddrprefix = None
                self.mplsvpnvrfbgppathattripaddrprefixlen = None
                self.mplsvpnvrfbgppathattrpeer = None
                self.mplsvpnvrfbgppathattrorigin = None
                self.mplsvpnvrfbgppathattraspathsegment = None
                self.mplsvpnvrfbgppathattrnexthop = None
                self.mplsvpnvrfbgppathattrmultiexitdisc = None
                self.mplsvpnvrfbgppathattrlocalpref = None
                self.mplsvpnvrfbgppathattratomicaggregate = None
                self.mplsvpnvrfbgppathattraggregatoras = None
                self.mplsvpnvrfbgppathattraggregatoraddr = None
                self.mplsvpnvrfbgppathattrcalclocalpref = None
                self.mplsvpnvrfbgppathattrbest = None
                self.mplsvpnvrfbgppathattrunknown = None
                self._segment_path = lambda: "mplsVpnVrfBgpNbrPrefixEntry" + "[mplsVpnVrfName='" + str(self.mplsvpnvrfname) + "']" + "[mplsVpnVrfBgpPathAttrIpAddrPrefix='" + str(self.mplsvpnvrfbgppathattripaddrprefix) + "']" + "[mplsVpnVrfBgpPathAttrIpAddrPrefixLen='" + str(self.mplsvpnvrfbgppathattripaddrprefixlen) + "']" + "[mplsVpnVrfBgpPathAttrPeer='" + str(self.mplsvpnvrfbgppathattrpeer) + "']"
                self._absolute_path = lambda: "MPLS-VPN-MIB:MPLS-VPN-MIB/mplsVpnVrfBgpNbrPrefixTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MPLSVPNMIB.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry, ['mplsvpnvrfname', 'mplsvpnvrfbgppathattripaddrprefix', 'mplsvpnvrfbgppathattripaddrprefixlen', 'mplsvpnvrfbgppathattrpeer', 'mplsvpnvrfbgppathattrorigin', 'mplsvpnvrfbgppathattraspathsegment', 'mplsvpnvrfbgppathattrnexthop', 'mplsvpnvrfbgppathattrmultiexitdisc', 'mplsvpnvrfbgppathattrlocalpref', 'mplsvpnvrfbgppathattratomicaggregate', 'mplsvpnvrfbgppathattraggregatoras', 'mplsvpnvrfbgppathattraggregatoraddr', 'mplsvpnvrfbgppathattrcalclocalpref', 'mplsvpnvrfbgppathattrbest', 'mplsvpnvrfbgppathattrunknown'], name, value)

            class Mplsvpnvrfbgppathattratomicaggregate(Enum):
                """
                Mplsvpnvrfbgppathattratomicaggregate (Enum Class)

                Whether or not the local system has

                selected a less specific route without

                selecting a more specific route.

                .. data:: lessSpecificRrouteNotSelected = 1

                .. data:: lessSpecificRouteSelected = 2

                """

                lessSpecificRrouteNotSelected = Enum.YLeaf(1, "lessSpecificRrouteNotSelected")

                lessSpecificRouteSelected = Enum.YLeaf(2, "lessSpecificRouteSelected")


            class Mplsvpnvrfbgppathattrbest(Enum):
                """
                Mplsvpnvrfbgppathattrbest (Enum Class)

                An indication of whether or not this route

                was chosen as the best BGP4 route.

                .. data:: false = 1

                .. data:: true = 2

                """

                false = Enum.YLeaf(1, "false")

                true = Enum.YLeaf(2, "true")


            class Mplsvpnvrfbgppathattrorigin(Enum):
                """
                Mplsvpnvrfbgppathattrorigin (Enum Class)

                The ultimate origin of the path

                information.

                .. data:: igp = 1

                .. data:: egp = 2

                .. data:: incomplete = 3

                """

                igp = Enum.YLeaf(1, "igp")

                egp = Enum.YLeaf(2, "egp")

                incomplete = Enum.YLeaf(3, "incomplete")



    class Mplsvpnvrfroutetable(Entity):
        """
        This table specifies per\-interface MPLS/BGP VPN VRF Table
        routing information. Entries in this table define VRF routing
        entries associated with the specified MPLS/VPN interfaces. Note
        that this table contains both BGP and IGP routes, as both may
        appear in the same VRF.
        
        .. attribute:: mplsvpnvrfrouteentry
        
        	An entry in this table is created by an LSR for every route present configured (either dynamically or statically) within the context of a specific VRF capable of supporting MPLS/BGP VPN. The indexing provides an ordering of VRFs per\-VPN interface
        	**type**\: list of  		 :py:class:`Mplsvpnvrfrouteentry <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry>`
        
        

        """

        _prefix = 'MPLS-VPN-MIB'
        _revision = '2001-10-15'

        def __init__(self):
            super(MPLSVPNMIB.Mplsvpnvrfroutetable, self).__init__()

            self.yang_name = "mplsVpnVrfRouteTable"
            self.yang_parent_name = "MPLS-VPN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("mplsVpnVrfRouteEntry", ("mplsvpnvrfrouteentry", MPLSVPNMIB.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry))])
            self._leafs = OrderedDict()

            self.mplsvpnvrfrouteentry = YList(self)
            self._segment_path = lambda: "mplsVpnVrfRouteTable"
            self._absolute_path = lambda: "MPLS-VPN-MIB:MPLS-VPN-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSVPNMIB.Mplsvpnvrfroutetable, [], name, value)


        class Mplsvpnvrfrouteentry(Entity):
            """
            An entry in this table is created by an LSR for every route
            present configured (either dynamically or statically) within
            the context of a specific VRF capable of supporting MPLS/BGP
            VPN. The indexing provides an ordering of VRFs per\-VPN
            interface.
            
            .. attribute:: mplsvpnvrfname  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..31
            
            	**refers to**\:  :py:class:`mplsvpnvrfname <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpnvrftable.Mplsvpnvrfentry>`
            
            .. attribute:: mplsvpnvrfroutedest  (key)
            
            	The destination IP address of this route. This object may not take a Multicast (Class D) address value.  Any assignment (implicit or otherwise) of an instance of this object to a value x must be rejected if the bit\-wise logical\-AND of x with the value of the corresponding instance of the mplsVpnVrfRouteMask object is not equal to x
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: mplsvpnvrfroutemask  (key)
            
            	Indicate the mask to be logical\-ANDed with the destination  address  before  being compared to the value  in  the  mplsVpnVrfRouteDest field. For those  systems  that  do  not support arbitrary subnet masks, an agent constructs the value of the mplsVpnVrfRouteMask by reference   to the IP Address Class.  Any assignment (implicit or otherwise) of an instance of this object to a value x must be rejected if the bit\-wise logical\-AND of x with the value of the corresponding instance of the mplsVpnVrfRouteDest object is not equal to mplsVpnVrfRouteDest
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: mplsvpnvrfroutetos  (key)
            
            	The IP TOS Field is used to specify the policy to be applied to this route.  The encoding of IP TOS is as specified  by  the  following convention. Zero indicates the default path if no more specific policy applies.  +\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+ \|                 \|                       \|     \| \|   PRECEDENCE    \|    TYPE OF SERVICE    \|  0  \| \|                 \|                       \|     \| +\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+\-\-\-\-\-+             IP TOS                IP TOS       Field     Policy      Field     Policy       Contents    Code      Contents    Code       0 0 0 0  ==>   0      0 0 0 1  ==>   2       0 0 1 0  ==>   4      0 0 1 1  ==>   6       0 1 0 0  ==>   8      0 1 0 1  ==>  10       0 1 1 0  ==>  12      0 1 1 1  ==>  14       1 0 0 0  ==>  16      1 0 0 1  ==>  18       1 0 1 0  ==>  20      1 0 1 1  ==>  22       1 1 0 0  ==>  24      1 1 0 1  ==>  26       1 1 1 0  ==>  28      1 1 1 1  ==>  30
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfroutenexthop  (key)
            
            	On remote routes, the address of the next system en route; Otherwise, 0.0.0.0. 
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: mplsvpnvrfroutedestaddrtype
            
            	The address type of the mplsVpnVrfRouteDest entry
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: mplsvpnvrfroutemaskaddrtype
            
            	The address type of mplsVpnVrfRouteMask
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: mplsvpnvrfroutenexthopaddrtype
            
            	The address type of the mplsVpnVrfRouteNextHopAddrType object
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: mplsvpnvrfrouteifindex
            
            	The ifIndex value that identifies the local interface  through  which  the next hop of this route should be reached
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplsvpnvrfroutetype
            
            	The type of route.  Note that local(3)  refers to a route for which the next hop is the final destination; remote(4) refers to a route for that the next  hop is not the final destination. Routes which do not result in traffic forwarding or rejection should not be displayed even if the implementation keeps them stored internally.  reject (2) refers to a route which, if matched, discards the message as unreachable. This is used in some protocols as a means of correctly aggregating routes
            	**type**\:  :py:class:`Mplsvpnvrfroutetype <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry.Mplsvpnvrfroutetype>`
            
            .. attribute:: mplsvpnvrfrouteproto
            
            	The routing mechanism via which this route was learned.  Inclusion of values for gateway rout\- ing protocols is not  intended  to  imply  that hosts should support those protocols
            	**type**\:  :py:class:`Mplsvpnvrfrouteproto <ydk.models.cisco_ios_xe.MPLS_VPN_MIB.MPLSVPNMIB.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry.Mplsvpnvrfrouteproto>`
            
            .. attribute:: mplsvpnvrfrouteage
            
            	The number of seconds since this route was last updated or otherwise determined to be correct. Note that no semantics of `too old' can be implied except through knowledge of the routing protocol by which the route was learned
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfrouteinfo
            
            	A reference to MIB definitions specific to the particular routing protocol which is responsi\-   ble for this route, as determined by the  value specified  in the route's mplsVpnVrfRouteProto value. If this information is not present, its value SHOULD be set to the OBJECT IDENTIFIER { 0 0 }, which is a syntactically valid object identif\-ier, and any implementation conforming to ASN.1 and the Basic Encoding Rules must be able to generate and recognize this value
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplsvpnvrfroutenexthopas
            
            	The Autonomous System Number of the Next Hop. The semantics of this object are determined by the routing\-protocol specified in the route's mplsVpnVrfRouteProto value. When this object is unknown or not relevant its value should be set to zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsvpnvrfroutemetric1
            
            	The primary routing metric for this route. The semantics of this metric are determined by the routing\-protocol specified in  the  route's mplsVpnVrfRouteProto value. If this metric is not used, its value should be set to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mplsvpnvrfroutemetric2
            
            	An alternate routing metric for this route. The semantics of this metric are determined by the routing\-protocol specified in  the  route's mplsVpnVrfRouteProto value. If this metric is not used, its value should be set to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mplsvpnvrfroutemetric3
            
            	An alternate routing metric for this route. The semantics of this metric are determined by the routing\-protocol specified in  the  route's mplsVpnVrfRouteProto value. If this metric is not used, its value should be set to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mplsvpnvrfroutemetric4
            
            	An alternate routing metric for this route. The semantics of this metric are determined by the routing\-protocol specified in  the  route's mplsVpnVrfRouteProto value. If this metric is not used, its value should be set to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mplsvpnvrfroutemetric5
            
            	An alternate routing metric for this route. The semantics of this metric are determined by the routing\-protocol specified in  the  route's mplsVpnVrfRouteProto value. If this metric is not used, its value should be set to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: mplsvpnvrfrouterowstatus
            
            	Row status for this table. It is used according to row installation and removal conventions
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: mplsvpnvrfroutestoragetype
            
            	Storage type value
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            

            """

            _prefix = 'MPLS-VPN-MIB'
            _revision = '2001-10-15'

            def __init__(self):
                super(MPLSVPNMIB.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry, self).__init__()

                self.yang_name = "mplsVpnVrfRouteEntry"
                self.yang_parent_name = "mplsVpnVrfRouteTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mplsvpnvrfname','mplsvpnvrfroutedest','mplsvpnvrfroutemask','mplsvpnvrfroutetos','mplsvpnvrfroutenexthop']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mplsvpnvrfname', YLeaf(YType.str, 'mplsVpnVrfName')),
                    ('mplsvpnvrfroutedest', YLeaf(YType.str, 'mplsVpnVrfRouteDest')),
                    ('mplsvpnvrfroutemask', YLeaf(YType.str, 'mplsVpnVrfRouteMask')),
                    ('mplsvpnvrfroutetos', YLeaf(YType.uint32, 'mplsVpnVrfRouteTos')),
                    ('mplsvpnvrfroutenexthop', YLeaf(YType.str, 'mplsVpnVrfRouteNextHop')),
                    ('mplsvpnvrfroutedestaddrtype', YLeaf(YType.enumeration, 'mplsVpnVrfRouteDestAddrType')),
                    ('mplsvpnvrfroutemaskaddrtype', YLeaf(YType.enumeration, 'mplsVpnVrfRouteMaskAddrType')),
                    ('mplsvpnvrfroutenexthopaddrtype', YLeaf(YType.enumeration, 'mplsVpnVrfRouteNextHopAddrType')),
                    ('mplsvpnvrfrouteifindex', YLeaf(YType.int32, 'mplsVpnVrfRouteIfIndex')),
                    ('mplsvpnvrfroutetype', YLeaf(YType.enumeration, 'mplsVpnVrfRouteType')),
                    ('mplsvpnvrfrouteproto', YLeaf(YType.enumeration, 'mplsVpnVrfRouteProto')),
                    ('mplsvpnvrfrouteage', YLeaf(YType.uint32, 'mplsVpnVrfRouteAge')),
                    ('mplsvpnvrfrouteinfo', YLeaf(YType.str, 'mplsVpnVrfRouteInfo')),
                    ('mplsvpnvrfroutenexthopas', YLeaf(YType.uint32, 'mplsVpnVrfRouteNextHopAS')),
                    ('mplsvpnvrfroutemetric1', YLeaf(YType.int32, 'mplsVpnVrfRouteMetric1')),
                    ('mplsvpnvrfroutemetric2', YLeaf(YType.int32, 'mplsVpnVrfRouteMetric2')),
                    ('mplsvpnvrfroutemetric3', YLeaf(YType.int32, 'mplsVpnVrfRouteMetric3')),
                    ('mplsvpnvrfroutemetric4', YLeaf(YType.int32, 'mplsVpnVrfRouteMetric4')),
                    ('mplsvpnvrfroutemetric5', YLeaf(YType.int32, 'mplsVpnVrfRouteMetric5')),
                    ('mplsvpnvrfrouterowstatus', YLeaf(YType.enumeration, 'mplsVpnVrfRouteRowStatus')),
                    ('mplsvpnvrfroutestoragetype', YLeaf(YType.enumeration, 'mplsVpnVrfRouteStorageType')),
                ])
                self.mplsvpnvrfname = None
                self.mplsvpnvrfroutedest = None
                self.mplsvpnvrfroutemask = None
                self.mplsvpnvrfroutetos = None
                self.mplsvpnvrfroutenexthop = None
                self.mplsvpnvrfroutedestaddrtype = None
                self.mplsvpnvrfroutemaskaddrtype = None
                self.mplsvpnvrfroutenexthopaddrtype = None
                self.mplsvpnvrfrouteifindex = None
                self.mplsvpnvrfroutetype = None
                self.mplsvpnvrfrouteproto = None
                self.mplsvpnvrfrouteage = None
                self.mplsvpnvrfrouteinfo = None
                self.mplsvpnvrfroutenexthopas = None
                self.mplsvpnvrfroutemetric1 = None
                self.mplsvpnvrfroutemetric2 = None
                self.mplsvpnvrfroutemetric3 = None
                self.mplsvpnvrfroutemetric4 = None
                self.mplsvpnvrfroutemetric5 = None
                self.mplsvpnvrfrouterowstatus = None
                self.mplsvpnvrfroutestoragetype = None
                self._segment_path = lambda: "mplsVpnVrfRouteEntry" + "[mplsVpnVrfName='" + str(self.mplsvpnvrfname) + "']" + "[mplsVpnVrfRouteDest='" + str(self.mplsvpnvrfroutedest) + "']" + "[mplsVpnVrfRouteMask='" + str(self.mplsvpnvrfroutemask) + "']" + "[mplsVpnVrfRouteTos='" + str(self.mplsvpnvrfroutetos) + "']" + "[mplsVpnVrfRouteNextHop='" + str(self.mplsvpnvrfroutenexthop) + "']"
                self._absolute_path = lambda: "MPLS-VPN-MIB:MPLS-VPN-MIB/mplsVpnVrfRouteTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MPLSVPNMIB.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry, ['mplsvpnvrfname', 'mplsvpnvrfroutedest', 'mplsvpnvrfroutemask', 'mplsvpnvrfroutetos', 'mplsvpnvrfroutenexthop', 'mplsvpnvrfroutedestaddrtype', 'mplsvpnvrfroutemaskaddrtype', 'mplsvpnvrfroutenexthopaddrtype', 'mplsvpnvrfrouteifindex', 'mplsvpnvrfroutetype', 'mplsvpnvrfrouteproto', 'mplsvpnvrfrouteage', 'mplsvpnvrfrouteinfo', 'mplsvpnvrfroutenexthopas', 'mplsvpnvrfroutemetric1', 'mplsvpnvrfroutemetric2', 'mplsvpnvrfroutemetric3', 'mplsvpnvrfroutemetric4', 'mplsvpnvrfroutemetric5', 'mplsvpnvrfrouterowstatus', 'mplsvpnvrfroutestoragetype'], name, value)

            class Mplsvpnvrfrouteproto(Enum):
                """
                Mplsvpnvrfrouteproto (Enum Class)

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

                other = Enum.YLeaf(1, "other")

                local = Enum.YLeaf(2, "local")

                netmgmt = Enum.YLeaf(3, "netmgmt")

                icmp = Enum.YLeaf(4, "icmp")

                egp = Enum.YLeaf(5, "egp")

                ggp = Enum.YLeaf(6, "ggp")

                hello = Enum.YLeaf(7, "hello")

                rip = Enum.YLeaf(8, "rip")

                isIs = Enum.YLeaf(9, "isIs")

                esIs = Enum.YLeaf(10, "esIs")

                ciscoIgrp = Enum.YLeaf(11, "ciscoIgrp")

                bbnSpfIgp = Enum.YLeaf(12, "bbnSpfIgp")

                ospf = Enum.YLeaf(13, "ospf")

                bgp = Enum.YLeaf(14, "bgp")

                idpr = Enum.YLeaf(15, "idpr")

                ciscoEigrp = Enum.YLeaf(16, "ciscoEigrp")


            class Mplsvpnvrfroutetype(Enum):
                """
                Mplsvpnvrfroutetype (Enum Class)

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

                other = Enum.YLeaf(1, "other")

                reject = Enum.YLeaf(2, "reject")

                local = Enum.YLeaf(3, "local")

                remote = Enum.YLeaf(4, "remote")


    def clone_ptr(self):
        self._top_entity = MPLSVPNMIB()
        return self._top_entity


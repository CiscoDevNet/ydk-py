""" MPLS_L3VPN_STD_MIB 

This MIB contains managed object definitions for the
Layer\-3 Multiprotocol Label Switching Virtual
Private Networks.

Copyright (C) The Internet Society (2006).  This
version of this MIB module is part of RFC4382; see
the RFC itself for full legal notices.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MplsL3VpnRtType(Enum):
    """
    MplsL3VpnRtType

    Used to define the type of a route target usage.

    Route targets can be specified to be imported,

    exported, or both.  For a complete definition of a

    route target, see [RFC4364].

    .. data:: import_ = 1

    .. data:: export = 2

    .. data:: both = 3

    """

    import_ = Enum.YLeaf(1, "import")

    export = Enum.YLeaf(2, "export")

    both = Enum.YLeaf(3, "both")



class MPLSL3VPNSTDMIB(Entity):
    """
    
    
    .. attribute:: mplsl3vpnifconftable
    
    	This table specifies per\-interface MPLS capability and associated information
    	**type**\:   :py:class:`Mplsl3Vpnifconftable <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MPLSL3VPNSTDMIB.Mplsl3Vpnifconftable>`
    
    .. attribute:: mplsl3vpnscalars
    
    	
    	**type**\:   :py:class:`Mplsl3Vpnscalars <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MPLSL3VPNSTDMIB.Mplsl3Vpnscalars>`
    
    .. attribute:: mplsl3vpnvrfrtetable
    
    	This table specifies per\-interface MPLS L3VPN VRF Table routing information.  Entries in this table define VRF routing entries associated with the specified MPLS/VPN interfaces.  Note  that this table contains both BGP and Interior Gateway Protocol IGP routes, as both may appear in the same VRF
    	**type**\:   :py:class:`Mplsl3Vpnvrfrtetable <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MPLSL3VPNSTDMIB.Mplsl3Vpnvrfrtetable>`
    
    .. attribute:: mplsl3vpnvrfrttable
    
    	This table specifies per\-VRF route target association. Each entry identifies a connectivity policy supported as part of a VPN
    	**type**\:   :py:class:`Mplsl3Vpnvrfrttable <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MPLSL3VPNSTDMIB.Mplsl3Vpnvrfrttable>`
    
    .. attribute:: mplsl3vpnvrftable
    
    	This table specifies per\-interface MPLS L3VPN VRF Table capability and associated information. Entries in this table define VRF routing instances associated with MPLS/VPN interfaces.  Note that multiple interfaces can belong to the same VRF instance.  The collection of all VRF instances comprises an actual VPN
    	**type**\:   :py:class:`Mplsl3Vpnvrftable <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MPLSL3VPNSTDMIB.Mplsl3Vpnvrftable>`
    
    

    """

    _prefix = 'MPLS-L3VPN-STD-MIB'
    _revision = '2006-01-23'

    def __init__(self):
        super(MPLSL3VPNSTDMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "MPLS-L3VPN-STD-MIB"
        self.yang_parent_name = "MPLS-L3VPN-STD-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"mplsL3VpnIfConfTable" : ("mplsl3vpnifconftable", MPLSL3VPNSTDMIB.Mplsl3Vpnifconftable), "mplsL3VpnScalars" : ("mplsl3vpnscalars", MPLSL3VPNSTDMIB.Mplsl3Vpnscalars), "mplsL3VpnVrfRteTable" : ("mplsl3vpnvrfrtetable", MPLSL3VPNSTDMIB.Mplsl3Vpnvrfrtetable), "mplsL3VpnVrfRTTable" : ("mplsl3vpnvrfrttable", MPLSL3VPNSTDMIB.Mplsl3Vpnvrfrttable), "mplsL3VpnVrfTable" : ("mplsl3vpnvrftable", MPLSL3VPNSTDMIB.Mplsl3Vpnvrftable)}
        self._child_list_classes = {}

        self.mplsl3vpnifconftable = MPLSL3VPNSTDMIB.Mplsl3Vpnifconftable()
        self.mplsl3vpnifconftable.parent = self
        self._children_name_map["mplsl3vpnifconftable"] = "mplsL3VpnIfConfTable"
        self._children_yang_names.add("mplsL3VpnIfConfTable")

        self.mplsl3vpnscalars = MPLSL3VPNSTDMIB.Mplsl3Vpnscalars()
        self.mplsl3vpnscalars.parent = self
        self._children_name_map["mplsl3vpnscalars"] = "mplsL3VpnScalars"
        self._children_yang_names.add("mplsL3VpnScalars")

        self.mplsl3vpnvrfrtetable = MPLSL3VPNSTDMIB.Mplsl3Vpnvrfrtetable()
        self.mplsl3vpnvrfrtetable.parent = self
        self._children_name_map["mplsl3vpnvrfrtetable"] = "mplsL3VpnVrfRteTable"
        self._children_yang_names.add("mplsL3VpnVrfRteTable")

        self.mplsl3vpnvrfrttable = MPLSL3VPNSTDMIB.Mplsl3Vpnvrfrttable()
        self.mplsl3vpnvrfrttable.parent = self
        self._children_name_map["mplsl3vpnvrfrttable"] = "mplsL3VpnVrfRTTable"
        self._children_yang_names.add("mplsL3VpnVrfRTTable")

        self.mplsl3vpnvrftable = MPLSL3VPNSTDMIB.Mplsl3Vpnvrftable()
        self.mplsl3vpnvrftable.parent = self
        self._children_name_map["mplsl3vpnvrftable"] = "mplsL3VpnVrfTable"
        self._children_yang_names.add("mplsL3VpnVrfTable")
        self._segment_path = lambda: "MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB"


    class Mplsl3Vpnifconftable(Entity):
        """
        This table specifies per\-interface MPLS capability
        and associated information.
        
        .. attribute:: mplsl3vpnifconfentry
        
        	An entry in this table is created by an LSR for every interface capable of supporting MPLS L3VPN. Each entry in this table is meant to correspond to an entry in the Interfaces Table
        	**type**\: list of    :py:class:`Mplsl3Vpnifconfentry <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MPLSL3VPNSTDMIB.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry>`
        
        

        """

        _prefix = 'MPLS-L3VPN-STD-MIB'
        _revision = '2006-01-23'

        def __init__(self):
            super(MPLSL3VPNSTDMIB.Mplsl3Vpnifconftable, self).__init__()

            self.yang_name = "mplsL3VpnIfConfTable"
            self.yang_parent_name = "MPLS-L3VPN-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"mplsL3VpnIfConfEntry" : ("mplsl3vpnifconfentry", MPLSL3VPNSTDMIB.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry)}

            self.mplsl3vpnifconfentry = YList(self)
            self._segment_path = lambda: "mplsL3VpnIfConfTable"
            self._absolute_path = lambda: "MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSL3VPNSTDMIB.Mplsl3Vpnifconftable, [], name, value)


        class Mplsl3Vpnifconfentry(Entity):
            """
            An entry in this table is created by an LSR for
            every interface capable of supporting MPLS L3VPN.
            Each entry in this table is meant to correspond to
            an entry in the Interfaces Table.
            
            .. attribute:: mplsl3vpnvrfname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..31
            
            	**refers to**\:  :py:class:`mplsl3vpnvrfname <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MPLSL3VPNSTDMIB.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry>`
            
            .. attribute:: mplsl3vpnifconfindex  <key>
            
            	This is a unique index for an entry in the mplsL3VpnIfConfTable.  A non\-zero index for an entry indicates the ifIndex for the corresponding interface entry in the MPLS\-VPN\-layer in the ifTable. Note that this table does not necessarily correspond one\-to\-one with all entries in the Interface MIB having an ifType of MPLS\-layer; rather, only those that are enabled for MPLS L3VPN functionality
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: mplsl3vpnifconfrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table.  Rows in this table signify that the specified interface is associated with this VRF.  If the row creation operation succeeds, the interface will have been associated with the specified VRF, otherwise the agent MUST not allow the association.  If the agent only allows read\-only operations on this table, it MUST create entries in this table as they are created on the device.  When a row in this table is in active(1) state, no objects in that row can be modified except mplsL3VpnIfConfStorageType and mplsL3VpnIfConfRowStatus
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: mplsl3vpnifconfstoragetype
            
            	The storage type for this VPN If entry. Conceptual rows having the value 'permanent' need not allow write access to any columnar objects in the row
            	**type**\:   :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: mplsl3vpnifvpnclassification
            
            	Denotes whether this link participates in a carrier's carrier, enterprise, or inter\-provider scenario
            	**type**\:   :py:class:`Mplsl3Vpnifvpnclassification <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MPLSL3VPNSTDMIB.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry.Mplsl3Vpnifvpnclassification>`
            
            .. attribute:: mplsl3vpnifvpnroutedistprotocol
            
            	Denotes the route distribution protocol across the PE\-CE link.  Note that more than one routing protocol may be enabled at the same time; thus, this object is specified as a bitmask.  For example, static(5) and ospf(2) are a typical configuration
            	**type**\:   :py:class:`Mplsl3Vpnifvpnroutedistprotocol <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MPLSL3VPNSTDMIB.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry.Mplsl3Vpnifvpnroutedistprotocol>`
            
            

            """

            _prefix = 'MPLS-L3VPN-STD-MIB'
            _revision = '2006-01-23'

            def __init__(self):
                super(MPLSL3VPNSTDMIB.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry, self).__init__()

                self.yang_name = "mplsL3VpnIfConfEntry"
                self.yang_parent_name = "mplsL3VpnIfConfTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.mplsl3vpnvrfname = YLeaf(YType.str, "mplsL3VpnVrfName")

                self.mplsl3vpnifconfindex = YLeaf(YType.int32, "mplsL3VpnIfConfIndex")

                self.mplsl3vpnifconfrowstatus = YLeaf(YType.enumeration, "mplsL3VpnIfConfRowStatus")

                self.mplsl3vpnifconfstoragetype = YLeaf(YType.enumeration, "mplsL3VpnIfConfStorageType")

                self.mplsl3vpnifvpnclassification = YLeaf(YType.enumeration, "mplsL3VpnIfVpnClassification")

                self.mplsl3vpnifvpnroutedistprotocol = YLeaf(YType.bits, "mplsL3VpnIfVpnRouteDistProtocol")
                self._segment_path = lambda: "mplsL3VpnIfConfEntry" + "[mplsL3VpnVrfName='" + self.mplsl3vpnvrfname.get() + "']" + "[mplsL3VpnIfConfIndex='" + self.mplsl3vpnifconfindex.get() + "']"
                self._absolute_path = lambda: "MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/mplsL3VpnIfConfTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MPLSL3VPNSTDMIB.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry, ['mplsl3vpnvrfname', 'mplsl3vpnifconfindex', 'mplsl3vpnifconfrowstatus', 'mplsl3vpnifconfstoragetype', 'mplsl3vpnifvpnclassification', 'mplsl3vpnifvpnroutedistprotocol'], name, value)

            class Mplsl3Vpnifvpnclassification(Enum):
                """
                Mplsl3Vpnifvpnclassification

                Denotes whether this link participates in a

                carrier's carrier, enterprise, or inter\-provider

                scenario.

                .. data:: carrierOfCarrier = 1

                .. data:: enterprise = 2

                .. data:: interProvider = 3

                """

                carrierOfCarrier = Enum.YLeaf(1, "carrierOfCarrier")

                enterprise = Enum.YLeaf(2, "enterprise")

                interProvider = Enum.YLeaf(3, "interProvider")



    class Mplsl3Vpnscalars(Entity):
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
            super(MPLSL3VPNSTDMIB.Mplsl3Vpnscalars, self).__init__()

            self.yang_name = "mplsL3VpnScalars"
            self.yang_parent_name = "MPLS-L3VPN-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.mplsl3vpnactivevrfs = YLeaf(YType.uint32, "mplsL3VpnActiveVrfs")

            self.mplsl3vpnconfiguredvrfs = YLeaf(YType.uint32, "mplsL3VpnConfiguredVrfs")

            self.mplsl3vpnconnectedinterfaces = YLeaf(YType.uint32, "mplsL3VpnConnectedInterfaces")

            self.mplsl3vpnilllblrcvthrsh = YLeaf(YType.uint32, "mplsL3VpnIllLblRcvThrsh")

            self.mplsl3vpnnotificationenable = YLeaf(YType.boolean, "mplsL3VpnNotificationEnable")

            self.mplsl3vpnvrfconfmaxpossrts = YLeaf(YType.uint32, "mplsL3VpnVrfConfMaxPossRts")

            self.mplsl3vpnvrfconfrtemxthrshtime = YLeaf(YType.uint32, "mplsL3VpnVrfConfRteMxThrshTime")
            self._segment_path = lambda: "mplsL3VpnScalars"
            self._absolute_path = lambda: "MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSL3VPNSTDMIB.Mplsl3Vpnscalars, ['mplsl3vpnactivevrfs', 'mplsl3vpnconfiguredvrfs', 'mplsl3vpnconnectedinterfaces', 'mplsl3vpnilllblrcvthrsh', 'mplsl3vpnnotificationenable', 'mplsl3vpnvrfconfmaxpossrts', 'mplsl3vpnvrfconfrtemxthrshtime'], name, value)


    class Mplsl3Vpnvrfrtetable(Entity):
        """
        This table specifies per\-interface MPLS L3VPN VRF Table
        routing information.  Entries in this table define VRF routing
        entries associated with the specified MPLS/VPN interfaces.  Note
        
        that this table contains both BGP and Interior Gateway Protocol
        IGP routes, as both may appear in the same VRF.
        
        .. attribute:: mplsl3vpnvrfrteentry
        
        	An entry in this table is created by an LSR for every route present configured (either dynamically or statically) within the context of a specific VRF capable of supporting MPLS/BGP VPN.  The indexing provides an ordering of VRFs per\-VPN interface.  Implementers need to be aware that there are quite a few index objects that together can exceed the size allowed for an Object Identifier (OID).  So implementers must make sure that OIDs of column instances in this table will have no more than 128 sub\-identifiers, otherwise they cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3
        	**type**\: list of    :py:class:`Mplsl3Vpnvrfrteentry <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MPLSL3VPNSTDMIB.Mplsl3Vpnvrfrtetable.Mplsl3Vpnvrfrteentry>`
        
        

        """

        _prefix = 'MPLS-L3VPN-STD-MIB'
        _revision = '2006-01-23'

        def __init__(self):
            super(MPLSL3VPNSTDMIB.Mplsl3Vpnvrfrtetable, self).__init__()

            self.yang_name = "mplsL3VpnVrfRteTable"
            self.yang_parent_name = "MPLS-L3VPN-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"mplsL3VpnVrfRteEntry" : ("mplsl3vpnvrfrteentry", MPLSL3VPNSTDMIB.Mplsl3Vpnvrfrtetable.Mplsl3Vpnvrfrteentry)}

            self.mplsl3vpnvrfrteentry = YList(self)
            self._segment_path = lambda: "mplsL3VpnVrfRteTable"
            self._absolute_path = lambda: "MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSL3VPNSTDMIB.Mplsl3Vpnvrfrtetable, [], name, value)


        class Mplsl3Vpnvrfrteentry(Entity):
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
            
            	**refers to**\:  :py:class:`mplsl3vpnvrfname <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MPLSL3VPNSTDMIB.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry>`
            
            .. attribute:: mplsl3vpnvrfrteinetcidrdesttype  <key>
            
            	The type of the mplsL3VpnVrfRteInetCidrDest address, as defined in the InetAddress MIB.  Only those address types that may appear in an actual routing table are allowed as values of this object
            	**type**\:   :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
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
            	**type**\:   :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
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
            	**type**\:   :py:class:`IANAipRouteProtocol <ydk.models.cisco_ios_xe.IANA_RTPROTO_MIB.IANAipRouteProtocol>`
            
            .. attribute:: mplsl3vpnvrfrteinetcidrstatus
            
            	The row status variable, used according to row installation and removal conventions.  A row entry cannot be modified when the status is marked as active(1)
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: mplsl3vpnvrfrteinetcidrtype
            
            	The type of route.  Note that local(3) refers to a route for which the next hop is the final destination; remote(4) refers to a route for which the next hop is not the final destination.  Routes that do not result in traffic forwarding or rejection should not be displayed even if the implementation keeps them stored internally.  reject(2) refers to a route that, if matched, discards the message as unreachable and returns a notification (e.g., ICMP error) to the message sender.  This is used in some protocols as a means of correctly aggregating routes.  blackhole(5) refers to a route that, if matched, discards the message silently
            	**type**\:   :py:class:`Mplsl3Vpnvrfrteinetcidrtype <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MPLSL3VPNSTDMIB.Mplsl3Vpnvrfrtetable.Mplsl3Vpnvrfrteentry.Mplsl3Vpnvrfrteinetcidrtype>`
            
            .. attribute:: mplsl3vpnvrfrtexcpointer
            
            	Index into mplsXCTable that identifies which cross\- connect entry is associated with this VRF route entry by containing the mplsXCIndex of that cross\-connect entry. The string containing the single\-octet 0x00 indicates that a label stack is not associated with this route entry.  This can be the case because the label bindings have not yet been established, or because some change in the agent has removed them.  When the label stack associated with this VRF route is created, it MUST establish the associated cross\-connect entry in the mplsXCTable and then set that index to the value of this object.  Changes to the cross\-connect object in the mplsXCTable MUST automatically be reflected in the value of this object.  If this object represents a static routing entry, then the manager must ensure that this entry is maintained consistently in the corresponding mplsXCTable as well
            	**type**\:  str
            
            	**length:** 1..24
            
            

            """

            _prefix = 'MPLS-L3VPN-STD-MIB'
            _revision = '2006-01-23'

            def __init__(self):
                super(MPLSL3VPNSTDMIB.Mplsl3Vpnvrfrtetable.Mplsl3Vpnvrfrteentry, self).__init__()

                self.yang_name = "mplsL3VpnVrfRteEntry"
                self.yang_parent_name = "mplsL3VpnVrfRteTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.mplsl3vpnvrfname = YLeaf(YType.str, "mplsL3VpnVrfName")

                self.mplsl3vpnvrfrteinetcidrdesttype = YLeaf(YType.enumeration, "mplsL3VpnVrfRteInetCidrDestType")

                self.mplsl3vpnvrfrteinetcidrdest = YLeaf(YType.str, "mplsL3VpnVrfRteInetCidrDest")

                self.mplsl3vpnvrfrteinetcidrpfxlen = YLeaf(YType.uint32, "mplsL3VpnVrfRteInetCidrPfxLen")

                self.mplsl3vpnvrfrteinetcidrpolicy = YLeaf(YType.str, "mplsL3VpnVrfRteInetCidrPolicy")

                self.mplsl3vpnvrfrteinetcidrnhoptype = YLeaf(YType.enumeration, "mplsL3VpnVrfRteInetCidrNHopType")

                self.mplsl3vpnvrfrteinetcidrnexthop = YLeaf(YType.str, "mplsL3VpnVrfRteInetCidrNextHop")

                self.mplsl3vpnvrfrteinetcidrage = YLeaf(YType.uint32, "mplsL3VpnVrfRteInetCidrAge")

                self.mplsl3vpnvrfrteinetcidrifindex = YLeaf(YType.int32, "mplsL3VpnVrfRteInetCidrIfIndex")

                self.mplsl3vpnvrfrteinetcidrmetric1 = YLeaf(YType.int32, "mplsL3VpnVrfRteInetCidrMetric1")

                self.mplsl3vpnvrfrteinetcidrmetric2 = YLeaf(YType.int32, "mplsL3VpnVrfRteInetCidrMetric2")

                self.mplsl3vpnvrfrteinetcidrmetric3 = YLeaf(YType.int32, "mplsL3VpnVrfRteInetCidrMetric3")

                self.mplsl3vpnvrfrteinetcidrmetric4 = YLeaf(YType.int32, "mplsL3VpnVrfRteInetCidrMetric4")

                self.mplsl3vpnvrfrteinetcidrmetric5 = YLeaf(YType.int32, "mplsL3VpnVrfRteInetCidrMetric5")

                self.mplsl3vpnvrfrteinetcidrnexthopas = YLeaf(YType.uint32, "mplsL3VpnVrfRteInetCidrNextHopAS")

                self.mplsl3vpnvrfrteinetcidrproto = YLeaf(YType.enumeration, "mplsL3VpnVrfRteInetCidrProto")

                self.mplsl3vpnvrfrteinetcidrstatus = YLeaf(YType.enumeration, "mplsL3VpnVrfRteInetCidrStatus")

                self.mplsl3vpnvrfrteinetcidrtype = YLeaf(YType.enumeration, "mplsL3VpnVrfRteInetCidrType")

                self.mplsl3vpnvrfrtexcpointer = YLeaf(YType.str, "mplsL3VpnVrfRteXCPointer")
                self._segment_path = lambda: "mplsL3VpnVrfRteEntry" + "[mplsL3VpnVrfName='" + self.mplsl3vpnvrfname.get() + "']" + "[mplsL3VpnVrfRteInetCidrDestType='" + self.mplsl3vpnvrfrteinetcidrdesttype.get() + "']" + "[mplsL3VpnVrfRteInetCidrDest='" + self.mplsl3vpnvrfrteinetcidrdest.get() + "']" + "[mplsL3VpnVrfRteInetCidrPfxLen='" + self.mplsl3vpnvrfrteinetcidrpfxlen.get() + "']" + "[mplsL3VpnVrfRteInetCidrPolicy='" + self.mplsl3vpnvrfrteinetcidrpolicy.get() + "']" + "[mplsL3VpnVrfRteInetCidrNHopType='" + self.mplsl3vpnvrfrteinetcidrnhoptype.get() + "']" + "[mplsL3VpnVrfRteInetCidrNextHop='" + self.mplsl3vpnvrfrteinetcidrnexthop.get() + "']"
                self._absolute_path = lambda: "MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/mplsL3VpnVrfRteTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MPLSL3VPNSTDMIB.Mplsl3Vpnvrfrtetable.Mplsl3Vpnvrfrteentry, ['mplsl3vpnvrfname', 'mplsl3vpnvrfrteinetcidrdesttype', 'mplsl3vpnvrfrteinetcidrdest', 'mplsl3vpnvrfrteinetcidrpfxlen', 'mplsl3vpnvrfrteinetcidrpolicy', 'mplsl3vpnvrfrteinetcidrnhoptype', 'mplsl3vpnvrfrteinetcidrnexthop', 'mplsl3vpnvrfrteinetcidrage', 'mplsl3vpnvrfrteinetcidrifindex', 'mplsl3vpnvrfrteinetcidrmetric1', 'mplsl3vpnvrfrteinetcidrmetric2', 'mplsl3vpnvrfrteinetcidrmetric3', 'mplsl3vpnvrfrteinetcidrmetric4', 'mplsl3vpnvrfrteinetcidrmetric5', 'mplsl3vpnvrfrteinetcidrnexthopas', 'mplsl3vpnvrfrteinetcidrproto', 'mplsl3vpnvrfrteinetcidrstatus', 'mplsl3vpnvrfrteinetcidrtype', 'mplsl3vpnvrfrtexcpointer'], name, value)

            class Mplsl3Vpnvrfrteinetcidrtype(Enum):
                """
                Mplsl3Vpnvrfrteinetcidrtype

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

                other = Enum.YLeaf(1, "other")

                reject = Enum.YLeaf(2, "reject")

                local = Enum.YLeaf(3, "local")

                remote = Enum.YLeaf(4, "remote")

                blackhole = Enum.YLeaf(5, "blackhole")



    class Mplsl3Vpnvrfrttable(Entity):
        """
        This table specifies per\-VRF route target association.
        Each entry identifies a connectivity policy supported
        as part of a VPN.
        
        .. attribute:: mplsl3vpnvrfrtentry
        
        	An entry in this table is created by an LSR for each route target configured for a VRF supporting a MPLS L3VPN instance.  The indexing provides an ordering per\-VRF instance.  See [RFC4364] for a complete definition of a route target
        	**type**\: list of    :py:class:`Mplsl3Vpnvrfrtentry <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MPLSL3VPNSTDMIB.Mplsl3Vpnvrfrttable.Mplsl3Vpnvrfrtentry>`
        
        

        """

        _prefix = 'MPLS-L3VPN-STD-MIB'
        _revision = '2006-01-23'

        def __init__(self):
            super(MPLSL3VPNSTDMIB.Mplsl3Vpnvrfrttable, self).__init__()

            self.yang_name = "mplsL3VpnVrfRTTable"
            self.yang_parent_name = "MPLS-L3VPN-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"mplsL3VpnVrfRTEntry" : ("mplsl3vpnvrfrtentry", MPLSL3VPNSTDMIB.Mplsl3Vpnvrfrttable.Mplsl3Vpnvrfrtentry)}

            self.mplsl3vpnvrfrtentry = YList(self)
            self._segment_path = lambda: "mplsL3VpnVrfRTTable"
            self._absolute_path = lambda: "MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSL3VPNSTDMIB.Mplsl3Vpnvrfrttable, [], name, value)


        class Mplsl3Vpnvrfrtentry(Entity):
            """
            An entry in this table is created by an LSR for
            each route target configured for a VRF supporting
            a MPLS L3VPN instance.  The indexing provides an
            ordering per\-VRF instance.  See [RFC4364] for a
            complete definition of a route target.
            
            .. attribute:: mplsl3vpnvrfname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..31
            
            	**refers to**\:  :py:class:`mplsl3vpnvrfname <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MPLSL3VPNSTDMIB.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry>`
            
            .. attribute:: mplsl3vpnvrfrtindex  <key>
            
            	Auxiliary index for route targets configured for a particular VRF
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplsl3vpnvrfrttype  <key>
            
            	The route target distribution type
            	**type**\:   :py:class:`MplsL3VpnRtType <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MplsL3VpnRtType>`
            
            .. attribute:: mplsl3vpnvrfrt
            
            	The route target distribution policy
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: mplsl3vpnvrfrtdescr
            
            	Description of the route target
            	**type**\:  str
            
            .. attribute:: mplsl3vpnvrfrtrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table.  When a row in this table is in active(1) state, no objects in that row can be modified except mplsL3VpnVrfRTRowStatus
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: mplsl3vpnvrfrtstoragetype
            
            	The storage type for this VPN route target (RT) entry. Conceptual rows having the value 'permanent' need not allow write access to any columnar objects in the row
            	**type**\:   :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            

            """

            _prefix = 'MPLS-L3VPN-STD-MIB'
            _revision = '2006-01-23'

            def __init__(self):
                super(MPLSL3VPNSTDMIB.Mplsl3Vpnvrfrttable.Mplsl3Vpnvrfrtentry, self).__init__()

                self.yang_name = "mplsL3VpnVrfRTEntry"
                self.yang_parent_name = "mplsL3VpnVrfRTTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.mplsl3vpnvrfname = YLeaf(YType.str, "mplsL3VpnVrfName")

                self.mplsl3vpnvrfrtindex = YLeaf(YType.uint32, "mplsL3VpnVrfRTIndex")

                self.mplsl3vpnvrfrttype = YLeaf(YType.enumeration, "mplsL3VpnVrfRTType")

                self.mplsl3vpnvrfrt = YLeaf(YType.str, "mplsL3VpnVrfRT")

                self.mplsl3vpnvrfrtdescr = YLeaf(YType.str, "mplsL3VpnVrfRTDescr")

                self.mplsl3vpnvrfrtrowstatus = YLeaf(YType.enumeration, "mplsL3VpnVrfRTRowStatus")

                self.mplsl3vpnvrfrtstoragetype = YLeaf(YType.enumeration, "mplsL3VpnVrfRTStorageType")
                self._segment_path = lambda: "mplsL3VpnVrfRTEntry" + "[mplsL3VpnVrfName='" + self.mplsl3vpnvrfname.get() + "']" + "[mplsL3VpnVrfRTIndex='" + self.mplsl3vpnvrfrtindex.get() + "']" + "[mplsL3VpnVrfRTType='" + self.mplsl3vpnvrfrttype.get() + "']"
                self._absolute_path = lambda: "MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/mplsL3VpnVrfRTTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MPLSL3VPNSTDMIB.Mplsl3Vpnvrfrttable.Mplsl3Vpnvrfrtentry, ['mplsl3vpnvrfname', 'mplsl3vpnvrfrtindex', 'mplsl3vpnvrfrttype', 'mplsl3vpnvrfrt', 'mplsl3vpnvrfrtdescr', 'mplsl3vpnvrfrtrowstatus', 'mplsl3vpnvrfrtstoragetype'], name, value)


    class Mplsl3Vpnvrftable(Entity):
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
        	**type**\: list of    :py:class:`Mplsl3Vpnvrfentry <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MPLSL3VPNSTDMIB.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry>`
        
        

        """

        _prefix = 'MPLS-L3VPN-STD-MIB'
        _revision = '2006-01-23'

        def __init__(self):
            super(MPLSL3VPNSTDMIB.Mplsl3Vpnvrftable, self).__init__()

            self.yang_name = "mplsL3VpnVrfTable"
            self.yang_parent_name = "MPLS-L3VPN-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"mplsL3VpnVrfEntry" : ("mplsl3vpnvrfentry", MPLSL3VPNSTDMIB.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry)}

            self.mplsl3vpnvrfentry = YList(self)
            self._segment_path = lambda: "mplsL3VpnVrfTable"
            self._absolute_path = lambda: "MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSL3VPNSTDMIB.Mplsl3Vpnvrftable, [], name, value)


        class Mplsl3Vpnvrfentry(Entity):
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
            	**type**\:   :py:class:`Mplsl3Vpnvrfconfadminstatus <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MPLSL3VPNSTDMIB.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry.Mplsl3Vpnvrfconfadminstatus>`
            
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
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: mplsl3vpnvrfconfstoragetype
            
            	The storage type for this VPN VRF entry. Conceptual rows having the value 'permanent' need not allow write access to any columnar objects in the row
            	**type**\:   :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: mplsl3vpnvrfcreationtime
            
            	The time at which this VRF entry was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsl3vpnvrfdescription
            
            	The human\-readable description of this VRF
            	**type**\:  str
            
            .. attribute:: mplsl3vpnvrfoperstatus
            
            	Denotes whether or not a VRF is operational.  A VRF is up(1) when there is at least one interface associated with the VRF whose ifOperStatus is up(1).  A VRF is down(2) when\: a. There does not exist at least one interface whose    ifOperStatus is up(1). b. There are no interfaces associated with the VRF
            	**type**\:   :py:class:`Mplsl3Vpnvrfoperstatus <ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB.MPLSL3VPNSTDMIB.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry.Mplsl3Vpnvrfoperstatus>`
            
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
                super(MPLSL3VPNSTDMIB.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry, self).__init__()

                self.yang_name = "mplsL3VpnVrfEntry"
                self.yang_parent_name = "mplsL3VpnVrfTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.mplsl3vpnvrfname = YLeaf(YType.str, "mplsL3VpnVrfName")

                self.mplsl3vpnvrfactiveinterfaces = YLeaf(YType.uint32, "mplsL3VpnVrfActiveInterfaces")

                self.mplsl3vpnvrfassociatedinterfaces = YLeaf(YType.uint32, "mplsL3VpnVrfAssociatedInterfaces")

                self.mplsl3vpnvrfconfadminstatus = YLeaf(YType.enumeration, "mplsL3VpnVrfConfAdminStatus")

                self.mplsl3vpnvrfconfhighrtethresh = YLeaf(YType.uint32, "mplsL3VpnVrfConfHighRteThresh")

                self.mplsl3vpnvrfconflastchanged = YLeaf(YType.uint32, "mplsL3VpnVrfConfLastChanged")

                self.mplsl3vpnvrfconfmaxroutes = YLeaf(YType.uint32, "mplsL3VpnVrfConfMaxRoutes")

                self.mplsl3vpnvrfconfmidrtethresh = YLeaf(YType.uint32, "mplsL3VpnVrfConfMidRteThresh")

                self.mplsl3vpnvrfconfrowstatus = YLeaf(YType.enumeration, "mplsL3VpnVrfConfRowStatus")

                self.mplsl3vpnvrfconfstoragetype = YLeaf(YType.enumeration, "mplsL3VpnVrfConfStorageType")

                self.mplsl3vpnvrfcreationtime = YLeaf(YType.uint32, "mplsL3VpnVrfCreationTime")

                self.mplsl3vpnvrfdescription = YLeaf(YType.str, "mplsL3VpnVrfDescription")

                self.mplsl3vpnvrfoperstatus = YLeaf(YType.enumeration, "mplsL3VpnVrfOperStatus")

                self.mplsl3vpnvrfperfcurrnumroutes = YLeaf(YType.uint32, "mplsL3VpnVrfPerfCurrNumRoutes")

                self.mplsl3vpnvrfperfdisctime = YLeaf(YType.uint32, "mplsL3VpnVrfPerfDiscTime")

                self.mplsl3vpnvrfperfroutesadded = YLeaf(YType.uint32, "mplsL3VpnVrfPerfRoutesAdded")

                self.mplsl3vpnvrfperfroutesdeleted = YLeaf(YType.uint32, "mplsL3VpnVrfPerfRoutesDeleted")

                self.mplsl3vpnvrfperfroutesdropped = YLeaf(YType.uint32, "mplsL3VpnVrfPerfRoutesDropped")

                self.mplsl3vpnvrfrd = YLeaf(YType.str, "mplsL3VpnVrfRD")

                self.mplsl3vpnvrfsecdiscontinuitytime = YLeaf(YType.uint32, "mplsL3VpnVrfSecDiscontinuityTime")

                self.mplsl3vpnvrfsecillegallblvltns = YLeaf(YType.uint32, "mplsL3VpnVrfSecIllegalLblVltns")

                self.mplsl3vpnvrfvpnid = YLeaf(YType.str, "mplsL3VpnVrfVpnId")
                self._segment_path = lambda: "mplsL3VpnVrfEntry" + "[mplsL3VpnVrfName='" + self.mplsl3vpnvrfname.get() + "']"
                self._absolute_path = lambda: "MPLS-L3VPN-STD-MIB:MPLS-L3VPN-STD-MIB/mplsL3VpnVrfTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MPLSL3VPNSTDMIB.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry, ['mplsl3vpnvrfname', 'mplsl3vpnvrfactiveinterfaces', 'mplsl3vpnvrfassociatedinterfaces', 'mplsl3vpnvrfconfadminstatus', 'mplsl3vpnvrfconfhighrtethresh', 'mplsl3vpnvrfconflastchanged', 'mplsl3vpnvrfconfmaxroutes', 'mplsl3vpnvrfconfmidrtethresh', 'mplsl3vpnvrfconfrowstatus', 'mplsl3vpnvrfconfstoragetype', 'mplsl3vpnvrfcreationtime', 'mplsl3vpnvrfdescription', 'mplsl3vpnvrfoperstatus', 'mplsl3vpnvrfperfcurrnumroutes', 'mplsl3vpnvrfperfdisctime', 'mplsl3vpnvrfperfroutesadded', 'mplsl3vpnvrfperfroutesdeleted', 'mplsl3vpnvrfperfroutesdropped', 'mplsl3vpnvrfrd', 'mplsl3vpnvrfsecdiscontinuitytime', 'mplsl3vpnvrfsecillegallblvltns', 'mplsl3vpnvrfvpnid'], name, value)

            class Mplsl3Vpnvrfconfadminstatus(Enum):
                """
                Mplsl3Vpnvrfconfadminstatus

                Indicates the desired operational status of this

                VRF.

                .. data:: up = 1

                .. data:: down = 2

                .. data:: testing = 3

                """

                up = Enum.YLeaf(1, "up")

                down = Enum.YLeaf(2, "down")

                testing = Enum.YLeaf(3, "testing")


            class Mplsl3Vpnvrfoperstatus(Enum):
                """
                Mplsl3Vpnvrfoperstatus

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

                up = Enum.YLeaf(1, "up")

                down = Enum.YLeaf(2, "down")


    def clone_ptr(self):
        self._top_entity = MPLSL3VPNSTDMIB()
        return self._top_entity


""" CISCO_IETF_FRR_MIB 

This MIB module contains managed object definitions for MPLS
Fast Reroute (FRR) as defined in\:Pan, P., Gan, D., Swallow, G.,
Vasseur, J.Ph., Cooper, D., Atlas, A., Jork, M., Fast Reroute
Techniques in RSVP\-TE, draft\-ietf\-mpls\-rsvp\-lsp\-fastreroute\-
00.txt, January 2002.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOIETFFRRMIB(Entity):
    """
    
    
    .. attribute:: cmplsfrrscalars
    
    	
    	**type**\:  :py:class:`Cmplsfrrscalars <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CISCOIETFFRRMIB.Cmplsfrrscalars>`
    
    .. attribute:: cmplsfrrconsttable
    
    	This table shows detour setup constraints
    	**type**\:  :py:class:`Cmplsfrrconsttable <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CISCOIETFFRRMIB.Cmplsfrrconsttable>`
    
    .. attribute:: cmplsfrrlogtable
    
    	The fast reroute log table records fast reroute events such as protected links going up or down or the FRR feature kicking in
    	**type**\:  :py:class:`Cmplsfrrlogtable <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CISCOIETFFRRMIB.Cmplsfrrlogtable>`
    
    .. attribute:: cmplsfrrfacroutedbtable
    
    	The mplsFrrFacRouteDBTable provides information about the  fast reroute database.  Each entry belongs to an interface, protecting backup tunnel and protected tunnel. MPLS  interfaces defined on this node are protected by backup tunnels and are indexed by mplsFrrFacRouteProtectedIndex. Backup tunnels defined to protect the tunnels traversing an interface, and are indexed by  mplsFrrFacRouteProtectingTunIndex.  Note that the tunnel  instance index is not required, since it is implied to be 0,  which indicates the tunnel head interface for the protecting  tunnel. The protecting tunnel is defined to exist on the PLR  in the FRR specification.  Protected tunnels are the LSPs that  traverse the protected link.  These LSPs are uniquely  identified by mplsFrrFacRouteProtectedTunIndex, mplsFrrFacRouteProtectedTunInstance,  mplsFrrFacRouteProtectedTunIngressLSRId, and  mplsFrrFacRouteProtectedTunEgressLSRId
    	**type**\:  :py:class:`Cmplsfrrfacroutedbtable <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CISCOIETFFRRMIB.Cmplsfrrfacroutedbtable>`
    
    

    """

    _prefix = 'CISCO-IETF-FRR-MIB'
    _revision = '2008-04-29'

    def __init__(self):
        super(CISCOIETFFRRMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IETF-FRR-MIB"
        self.yang_parent_name = "CISCO-IETF-FRR-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("cmplsFrrScalars", ("cmplsfrrscalars", CISCOIETFFRRMIB.Cmplsfrrscalars)), ("cmplsFrrConstTable", ("cmplsfrrconsttable", CISCOIETFFRRMIB.Cmplsfrrconsttable)), ("cmplsFrrLogTable", ("cmplsfrrlogtable", CISCOIETFFRRMIB.Cmplsfrrlogtable)), ("cmplsFrrFacRouteDBTable", ("cmplsfrrfacroutedbtable", CISCOIETFFRRMIB.Cmplsfrrfacroutedbtable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.cmplsfrrscalars = CISCOIETFFRRMIB.Cmplsfrrscalars()
        self.cmplsfrrscalars.parent = self
        self._children_name_map["cmplsfrrscalars"] = "cmplsFrrScalars"
        self._children_yang_names.add("cmplsFrrScalars")

        self.cmplsfrrconsttable = CISCOIETFFRRMIB.Cmplsfrrconsttable()
        self.cmplsfrrconsttable.parent = self
        self._children_name_map["cmplsfrrconsttable"] = "cmplsFrrConstTable"
        self._children_yang_names.add("cmplsFrrConstTable")

        self.cmplsfrrlogtable = CISCOIETFFRRMIB.Cmplsfrrlogtable()
        self.cmplsfrrlogtable.parent = self
        self._children_name_map["cmplsfrrlogtable"] = "cmplsFrrLogTable"
        self._children_yang_names.add("cmplsFrrLogTable")

        self.cmplsfrrfacroutedbtable = CISCOIETFFRRMIB.Cmplsfrrfacroutedbtable()
        self.cmplsfrrfacroutedbtable.parent = self
        self._children_name_map["cmplsfrrfacroutedbtable"] = "cmplsFrrFacRouteDBTable"
        self._children_yang_names.add("cmplsFrrFacRouteDBTable")
        self._segment_path = lambda: "CISCO-IETF-FRR-MIB:CISCO-IETF-FRR-MIB"


    class Cmplsfrrscalars(Entity):
        """
        
        
        .. attribute:: cmplsfrrdetourincoming
        
        	The number of detour LSPs entering the device if mplsFrrConstProtectionMethod is set to oneToOneBackup(0), or or 0 if mplsFrrConstProtectionMethod is set to facilityBackup(1)
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cmplsfrrdetouroutgoing
        
        	The number of detour LSPs leaving the device if mplsFrrConstProtectionMethod is set to oneToOneBackup(0), or 0 if mplsFrrConstProtectionMethod is set to  to facilityBackup(1)
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cmplsfrrdetouroriginating
        
        	The number of detour LSPs originating at this PLR if mplsFrrConstProtectionMethod is set to oneToOneBackup(0). This object MUST return 0 if the mplsFrrConstProtectionMethod  is set to facilityBackup(1)
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cmplsfrrswitchover
        
        	The number of tunnel instances that are switched over to their corresponding detour LSP if mplsFrrConstProtectionMethod is set to oneToOneBackup(0), or tunnels being switched over if mplsFrrConstProtectionMethod is set to facilityBackup(1)
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cmplsfrrnumofconfifs
        
        	Indicates the number of MPLS interfaces configured for  protection by the FRR feature, otherwise this value MUST return 0 to indicate that LSPs traversing any  interface may be protected
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cmplsfrractprotectedifs
        
        	Indicates the number of interfaces currently being protected  by the FRR feature if mplsFrrConstProtectionMethod is set to facilityBackup(1), otherwise this value should return 0 to indicate that LSPs traversing any interface may be protected. This value MUST be less than or equal to mplsFrrConfIfs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cmplsfrrconfprotectingtuns
        
        	Indicates the number of bypass tunnels configured to  protect facilities on this LSR using the FRR feature  if mplsFrrConstProtectionMethod is set to  facilityBackup(1), otherwise this value MUST return  0
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cmplsfrractprotectedtuns
        
        	Indicates the number of bypass tunnels indicated in mplsFrrConfProtectingTuns whose operStatus is up(1) indicating that they are currently protecting facilities on this LSR using the FRR feature. This object MUST return 0 if mplsFrrConstProtectionMethod  is set to facilityBackup(1)
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cmplsfrractprotectedlsps
        
        	Indicates the number of LSPs currently protected by  the FRR feature. If mplsFrrConstProtectionMethod is set  to facilityBackup(1)this object MUST return 0
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cmplsfrrconstprotectionmethod
        
        	Indicates which protection method is to be used for fast reroute. Some devices may require a reboot of their routing processors if this variable is changed. An agent which does not wish to reboot or modify its FRR mode  MUST return an inconsistentValue error. Please  consult the device's agent capability statement  for more details
        	**type**\:  :py:class:`Cmplsfrrconstprotectionmethod <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CISCOIETFFRRMIB.Cmplsfrrscalars.Cmplsfrrconstprotectionmethod>`
        
        .. attribute:: cmplsfrrnotifsenabled
        
        	Enables or disables FRR notifications defined in this MIB module. Notifications are disabled by default
        	**type**\: bool
        
        .. attribute:: cmplsfrrlogtablemaxentries
        
        	Indicates the maximum number of entries allowed in the FRR Log table. Agents receiving SETs for values that cannot be used must return an inconsistent value error. If a manager sets this value to 0, this indicates that no logging should take place by the agent.    If this value is returned as 0, this indicates that no additional log entries will be added to the current table either because the table has been completely filled or logging has been disabled. However, agents may wish to not delete existing entries in the log table so that managers may review them in the future.   It is implied that when mplsFrrLogTableCurrEntries  has reached the value of this variable, that logging  entries may not continue to be added to the table,  although existing ones may remain.  Furthermore, an agent may begin to delete existing (perhaps the oldest entries) entries to make room for new ones
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cmplsfrrlogtablecurrentries
        
        	Indicates the current number of entries in the FRR log table
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cmplsfrrnotifmaxrate
        
        	This variable indicates the number of milliseconds that must elapse between notification emissions. If events occur more rapidly, the implementation may simply fail to emit these notifications during that period, or may queue them until an appropriate time in the future. A value of 0 means no minimum  elapsed period is specified
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-IETF-FRR-MIB'
        _revision = '2008-04-29'

        def __init__(self):
            super(CISCOIETFFRRMIB.Cmplsfrrscalars, self).__init__()

            self.yang_name = "cmplsFrrScalars"
            self.yang_parent_name = "CISCO-IETF-FRR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cmplsfrrdetourincoming', YLeaf(YType.uint32, 'cmplsFrrDetourIncoming')),
                ('cmplsfrrdetouroutgoing', YLeaf(YType.uint32, 'cmplsFrrDetourOutgoing')),
                ('cmplsfrrdetouroriginating', YLeaf(YType.uint32, 'cmplsFrrDetourOriginating')),
                ('cmplsfrrswitchover', YLeaf(YType.uint32, 'cmplsFrrSwitchover')),
                ('cmplsfrrnumofconfifs', YLeaf(YType.uint32, 'cmplsFrrNumOfConfIfs')),
                ('cmplsfrractprotectedifs', YLeaf(YType.uint32, 'cmplsFrrActProtectedIfs')),
                ('cmplsfrrconfprotectingtuns', YLeaf(YType.uint32, 'cmplsFrrConfProtectingTuns')),
                ('cmplsfrractprotectedtuns', YLeaf(YType.uint32, 'cmplsFrrActProtectedTuns')),
                ('cmplsfrractprotectedlsps', YLeaf(YType.uint32, 'cmplsFrrActProtectedLSPs')),
                ('cmplsfrrconstprotectionmethod', YLeaf(YType.enumeration, 'cmplsFrrConstProtectionMethod')),
                ('cmplsfrrnotifsenabled', YLeaf(YType.boolean, 'cmplsFrrNotifsEnabled')),
                ('cmplsfrrlogtablemaxentries', YLeaf(YType.uint32, 'cmplsFrrLogTableMaxEntries')),
                ('cmplsfrrlogtablecurrentries', YLeaf(YType.uint32, 'cmplsFrrLogTableCurrEntries')),
                ('cmplsfrrnotifmaxrate', YLeaf(YType.uint32, 'cmplsFrrNotifMaxRate')),
            ])
            self.cmplsfrrdetourincoming = None
            self.cmplsfrrdetouroutgoing = None
            self.cmplsfrrdetouroriginating = None
            self.cmplsfrrswitchover = None
            self.cmplsfrrnumofconfifs = None
            self.cmplsfrractprotectedifs = None
            self.cmplsfrrconfprotectingtuns = None
            self.cmplsfrractprotectedtuns = None
            self.cmplsfrractprotectedlsps = None
            self.cmplsfrrconstprotectionmethod = None
            self.cmplsfrrnotifsenabled = None
            self.cmplsfrrlogtablemaxentries = None
            self.cmplsfrrlogtablecurrentries = None
            self.cmplsfrrnotifmaxrate = None
            self._segment_path = lambda: "cmplsFrrScalars"
            self._absolute_path = lambda: "CISCO-IETF-FRR-MIB:CISCO-IETF-FRR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFFRRMIB.Cmplsfrrscalars, ['cmplsfrrdetourincoming', 'cmplsfrrdetouroutgoing', 'cmplsfrrdetouroriginating', 'cmplsfrrswitchover', 'cmplsfrrnumofconfifs', 'cmplsfrractprotectedifs', 'cmplsfrrconfprotectingtuns', 'cmplsfrractprotectedtuns', 'cmplsfrractprotectedlsps', 'cmplsfrrconstprotectionmethod', 'cmplsfrrnotifsenabled', 'cmplsfrrlogtablemaxentries', 'cmplsfrrlogtablecurrentries', 'cmplsfrrnotifmaxrate'], name, value)

        class Cmplsfrrconstprotectionmethod(Enum):
            """
            Cmplsfrrconstprotectionmethod (Enum Class)

            Indicates which protection method is to be used for fast

            reroute. Some devices may require a reboot of their routing

            processors if this variable is changed. An agent which

            does not wish to reboot or modify its FRR mode 

            MUST return an inconsistentValue error. Please 

            consult the device's agent capability statement 

            for more details.

            .. data:: oneToOneBackup = 0

            .. data:: facilityBackup = 1

            """

            oneToOneBackup = Enum.YLeaf(0, "oneToOneBackup")

            facilityBackup = Enum.YLeaf(1, "facilityBackup")



    class Cmplsfrrconsttable(Entity):
        """
        This table shows detour setup constraints.
        
        .. attribute:: cmplsfrrconstentry
        
        	An entry in this table represents detour LSP or bypass tunnel  setup constraints for a tunnel instance to be protected by  detour LSPs or a tunnel. Agents must allow entries in this table  to be created only for tunnel instances that require fast\-reroute. Entries indexed with mplsFrrConstIfIndex set to 0 apply to all interfaces on this device for which the FRR feature can operate on
        	**type**\: list of  		 :py:class:`Cmplsfrrconstentry <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CISCOIETFFRRMIB.Cmplsfrrconsttable.Cmplsfrrconstentry>`
        
        

        """

        _prefix = 'CISCO-IETF-FRR-MIB'
        _revision = '2008-04-29'

        def __init__(self):
            super(CISCOIETFFRRMIB.Cmplsfrrconsttable, self).__init__()

            self.yang_name = "cmplsFrrConstTable"
            self.yang_parent_name = "CISCO-IETF-FRR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cmplsFrrConstEntry", ("cmplsfrrconstentry", CISCOIETFFRRMIB.Cmplsfrrconsttable.Cmplsfrrconstentry))])
            self._leafs = OrderedDict()

            self.cmplsfrrconstentry = YList(self)
            self._segment_path = lambda: "cmplsFrrConstTable"
            self._absolute_path = lambda: "CISCO-IETF-FRR-MIB:CISCO-IETF-FRR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFFRRMIB.Cmplsfrrconsttable, [], name, value)


        class Cmplsfrrconstentry(Entity):
            """
            An entry in this table represents detour LSP or bypass tunnel 
            setup constraints for a tunnel instance to be protected by 
            detour LSPs or a tunnel. Agents must allow entries in this table 
            to be created only for tunnel instances that require fast\-reroute.
            Entries indexed with mplsFrrConstIfIndex set to 0 apply to all
            interfaces on this device for which the FRR feature can operate
            on.
            
            .. attribute:: cmplsfrrconstifindex  (key)
            
            	Uniquely identifies an interface for which fast reroute is configured. Tabular entries indexed with a 0 value apply to all interfaces on this device for which the FRR feature can operate on
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cmplsfrrconsttunnelindex  (key)
            
            	Uniquely identifies a tunnel for which fast reroute is requested
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cmplsfrrconsttunnelinstance  (key)
            
            	Uniquely identifies an instance of this tunnel for which fast reroute is requested
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsfrrconstsetupprio
            
            	Indicates the setup priority of detour LSP
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: cmplsfrrconstholdingprio
            
            	Indicates the holding priority for detour LSP
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: cmplsfrrconstinclanyaffinity
            
            	A link satisfies the include\-any constraint if and only if the constraint is zero, or the link and the constraint have a resource class in common
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsfrrconstinclallaffinity
            
            	A link satisfies the include\-all constraint if and only if the link contains all of the administrative groups specified in the constraint
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsfrrconstexclallaffinity
            
            	A link satisfies the exclude\-all constraint if and only if the link contains none of the administrative groups specified in the constraint
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsfrrconsthoplimit
            
            	The maximum number of hops that the detour LSP may traverse
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: cmplsfrrconstbandwidth
            
            	This variable represents the bandwidth for detour LSPs of this tunnel, in units of thousands of bits per second (Kbps)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsfrrconstrowstatus
            
            	This object is used to create, modify, and/or delete a row in this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: cmplsfrrconstnumprotectingtunonif
            
            	The number of backup tunnels protecting the specified interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsfrrconstnumprotectedtunonif
            
            	The number of tunnels protected on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-FRR-MIB'
            _revision = '2008-04-29'

            def __init__(self):
                super(CISCOIETFFRRMIB.Cmplsfrrconsttable.Cmplsfrrconstentry, self).__init__()

                self.yang_name = "cmplsFrrConstEntry"
                self.yang_parent_name = "cmplsFrrConstTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cmplsfrrconstifindex','cmplsfrrconsttunnelindex','cmplsfrrconsttunnelinstance']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cmplsfrrconstifindex', YLeaf(YType.int32, 'cmplsFrrConstIfIndex')),
                    ('cmplsfrrconsttunnelindex', YLeaf(YType.uint32, 'cmplsFrrConstTunnelIndex')),
                    ('cmplsfrrconsttunnelinstance', YLeaf(YType.uint32, 'cmplsFrrConstTunnelInstance')),
                    ('cmplsfrrconstsetupprio', YLeaf(YType.uint32, 'cmplsFrrConstSetupPrio')),
                    ('cmplsfrrconstholdingprio', YLeaf(YType.uint32, 'cmplsFrrConstHoldingPrio')),
                    ('cmplsfrrconstinclanyaffinity', YLeaf(YType.uint32, 'cmplsFrrConstInclAnyAffinity')),
                    ('cmplsfrrconstinclallaffinity', YLeaf(YType.uint32, 'cmplsFrrConstInclAllAffinity')),
                    ('cmplsfrrconstexclallaffinity', YLeaf(YType.uint32, 'cmplsFrrConstExclAllAffinity')),
                    ('cmplsfrrconsthoplimit', YLeaf(YType.uint32, 'cmplsFrrConstHopLimit')),
                    ('cmplsfrrconstbandwidth', YLeaf(YType.uint32, 'cmplsFrrConstBandwidth')),
                    ('cmplsfrrconstrowstatus', YLeaf(YType.enumeration, 'cmplsFrrConstRowStatus')),
                    ('cmplsfrrconstnumprotectingtunonif', YLeaf(YType.uint32, 'cmplsFrrConstNumProtectingTunOnIf')),
                    ('cmplsfrrconstnumprotectedtunonif', YLeaf(YType.uint32, 'cmplsFrrConstNumProtectedTunOnIf')),
                ])
                self.cmplsfrrconstifindex = None
                self.cmplsfrrconsttunnelindex = None
                self.cmplsfrrconsttunnelinstance = None
                self.cmplsfrrconstsetupprio = None
                self.cmplsfrrconstholdingprio = None
                self.cmplsfrrconstinclanyaffinity = None
                self.cmplsfrrconstinclallaffinity = None
                self.cmplsfrrconstexclallaffinity = None
                self.cmplsfrrconsthoplimit = None
                self.cmplsfrrconstbandwidth = None
                self.cmplsfrrconstrowstatus = None
                self.cmplsfrrconstnumprotectingtunonif = None
                self.cmplsfrrconstnumprotectedtunonif = None
                self._segment_path = lambda: "cmplsFrrConstEntry" + "[cmplsFrrConstIfIndex='" + str(self.cmplsfrrconstifindex) + "']" + "[cmplsFrrConstTunnelIndex='" + str(self.cmplsfrrconsttunnelindex) + "']" + "[cmplsFrrConstTunnelInstance='" + str(self.cmplsfrrconsttunnelinstance) + "']"
                self._absolute_path = lambda: "CISCO-IETF-FRR-MIB:CISCO-IETF-FRR-MIB/cmplsFrrConstTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFFRRMIB.Cmplsfrrconsttable.Cmplsfrrconstentry, ['cmplsfrrconstifindex', 'cmplsfrrconsttunnelindex', 'cmplsfrrconsttunnelinstance', 'cmplsfrrconstsetupprio', 'cmplsfrrconstholdingprio', 'cmplsfrrconstinclanyaffinity', 'cmplsfrrconstinclallaffinity', 'cmplsfrrconstexclallaffinity', 'cmplsfrrconsthoplimit', 'cmplsfrrconstbandwidth', 'cmplsfrrconstrowstatus', 'cmplsfrrconstnumprotectingtunonif', 'cmplsfrrconstnumprotectedtunonif'], name, value)


    class Cmplsfrrlogtable(Entity):
        """
        The fast reroute log table records fast reroute events such
        as protected links going up or down or the FRR feature
        kicking in.
        
        .. attribute:: cmplsfrrlogentry
        
        	An entry in this table is created to describe one fast reroute event.  Entries in this table are only created and destroyed by the agent implementation. The maximum number  of entries in this log is governed by the scalar
        	**type**\: list of  		 :py:class:`Cmplsfrrlogentry <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CISCOIETFFRRMIB.Cmplsfrrlogtable.Cmplsfrrlogentry>`
        
        

        """

        _prefix = 'CISCO-IETF-FRR-MIB'
        _revision = '2008-04-29'

        def __init__(self):
            super(CISCOIETFFRRMIB.Cmplsfrrlogtable, self).__init__()

            self.yang_name = "cmplsFrrLogTable"
            self.yang_parent_name = "CISCO-IETF-FRR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cmplsFrrLogEntry", ("cmplsfrrlogentry", CISCOIETFFRRMIB.Cmplsfrrlogtable.Cmplsfrrlogentry))])
            self._leafs = OrderedDict()

            self.cmplsfrrlogentry = YList(self)
            self._segment_path = lambda: "cmplsFrrLogTable"
            self._absolute_path = lambda: "CISCO-IETF-FRR-MIB:CISCO-IETF-FRR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFFRRMIB.Cmplsfrrlogtable, [], name, value)


        class Cmplsfrrlogentry(Entity):
            """
            An entry in this table is created to describe one fast
            reroute event.  Entries in this table are only created and
            destroyed by the agent implementation. The maximum number 
            of entries in this log is governed by the scalar.
            
            .. attribute:: cmplsfrrlogindex  (key)
            
            	Uniquely identifies a fast reroute event entry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsfrrlogeventtime
            
            	This object provides the amount of time ticks since this event occured
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsfrrloginterface
            
            	This object indicates which interface was affected by this FRR event. This value may be set to 0 if mplsFrrConstProtectionMethod is set to oneToOneBackup(0)
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cmplsfrrlogeventtype
            
            	This object describes what type of fast reroute event occured
            	**type**\:  :py:class:`Cmplsfrrlogeventtype <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CISCOIETFFRRMIB.Cmplsfrrlogtable.Cmplsfrrlogentry.Cmplsfrrlogeventtype>`
            
            .. attribute:: cmplsfrrlogeventduration
            
            	This object describes the duration of this event
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsfrrlogeventreasonstring
            
            	This object contains an implementation\-specific explanation of the event
            	**type**\: str
            
            	**length:** 128
            
            

            """

            _prefix = 'CISCO-IETF-FRR-MIB'
            _revision = '2008-04-29'

            def __init__(self):
                super(CISCOIETFFRRMIB.Cmplsfrrlogtable.Cmplsfrrlogentry, self).__init__()

                self.yang_name = "cmplsFrrLogEntry"
                self.yang_parent_name = "cmplsFrrLogTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cmplsfrrlogindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cmplsfrrlogindex', YLeaf(YType.uint32, 'cmplsFrrLogIndex')),
                    ('cmplsfrrlogeventtime', YLeaf(YType.uint32, 'cmplsFrrLogEventTime')),
                    ('cmplsfrrloginterface', YLeaf(YType.int32, 'cmplsFrrLogInterface')),
                    ('cmplsfrrlogeventtype', YLeaf(YType.enumeration, 'cmplsFrrLogEventType')),
                    ('cmplsfrrlogeventduration', YLeaf(YType.uint32, 'cmplsFrrLogEventDuration')),
                    ('cmplsfrrlogeventreasonstring', YLeaf(YType.str, 'cmplsFrrLogEventReasonString')),
                ])
                self.cmplsfrrlogindex = None
                self.cmplsfrrlogeventtime = None
                self.cmplsfrrloginterface = None
                self.cmplsfrrlogeventtype = None
                self.cmplsfrrlogeventduration = None
                self.cmplsfrrlogeventreasonstring = None
                self._segment_path = lambda: "cmplsFrrLogEntry" + "[cmplsFrrLogIndex='" + str(self.cmplsfrrlogindex) + "']"
                self._absolute_path = lambda: "CISCO-IETF-FRR-MIB:CISCO-IETF-FRR-MIB/cmplsFrrLogTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFFRRMIB.Cmplsfrrlogtable.Cmplsfrrlogentry, ['cmplsfrrlogindex', 'cmplsfrrlogeventtime', 'cmplsfrrloginterface', 'cmplsfrrlogeventtype', 'cmplsfrrlogeventduration', 'cmplsfrrlogeventreasonstring'], name, value)

            class Cmplsfrrlogeventtype(Enum):
                """
                Cmplsfrrlogeventtype (Enum Class)

                This object describes what type of fast reroute event

                occured.

                .. data:: other = 1

                .. data:: protected = 2

                """

                other = Enum.YLeaf(1, "other")

                protected = Enum.YLeaf(2, "protected")



    class Cmplsfrrfacroutedbtable(Entity):
        """
        The mplsFrrFacRouteDBTable provides information about the 
        fast reroute database.  Each entry belongs to an interface,
        protecting backup tunnel and protected tunnel. MPLS 
        interfaces defined on this node are protected by backup
        tunnels and are indexed by mplsFrrFacRouteProtectedIndex.
        Backup tunnels defined to protect the tunnels traversing an
        interface, and are indexed by 
        mplsFrrFacRouteProtectingTunIndex.  Note that the tunnel 
        instance index is not required, since it is implied to be 0, 
        which indicates the tunnel head interface for the protecting 
        tunnel. The protecting tunnel is defined to exist on the PLR 
        in the FRR specification.  Protected tunnels are the LSPs that 
        traverse the protected link.  These LSPs are uniquely 
        identified by mplsFrrFacRouteProtectedTunIndex,
        mplsFrrFacRouteProtectedTunInstance, 
        mplsFrrFacRouteProtectedTunIngressLSRId, and 
        mplsFrrFacRouteProtectedTunEgressLSRId.
        
        .. attribute:: cmplsfrrfacroutedbentry
        
        	An entry in the mplsFrrDBTable represents a single protected LSP, protected by a backup tunnel and defined for a specific protected interface. Note that for brevity, managers should consult the mplsTunnelTable present in the MPLS\-TE MIB for additional information about the protecting and protected tunnels, and the ifEntry in the IF\-MIB for the protected interface
        	**type**\: list of  		 :py:class:`Cmplsfrrfacroutedbentry <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CISCOIETFFRRMIB.Cmplsfrrfacroutedbtable.Cmplsfrrfacroutedbentry>`
        
        

        """

        _prefix = 'CISCO-IETF-FRR-MIB'
        _revision = '2008-04-29'

        def __init__(self):
            super(CISCOIETFFRRMIB.Cmplsfrrfacroutedbtable, self).__init__()

            self.yang_name = "cmplsFrrFacRouteDBTable"
            self.yang_parent_name = "CISCO-IETF-FRR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cmplsFrrFacRouteDBEntry", ("cmplsfrrfacroutedbentry", CISCOIETFFRRMIB.Cmplsfrrfacroutedbtable.Cmplsfrrfacroutedbentry))])
            self._leafs = OrderedDict()

            self.cmplsfrrfacroutedbentry = YList(self)
            self._segment_path = lambda: "cmplsFrrFacRouteDBTable"
            self._absolute_path = lambda: "CISCO-IETF-FRR-MIB:CISCO-IETF-FRR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFFRRMIB.Cmplsfrrfacroutedbtable, [], name, value)


        class Cmplsfrrfacroutedbentry(Entity):
            """
            An entry in the mplsFrrDBTable represents a single protected
            LSP, protected by a backup tunnel and defined for a specific
            protected interface. Note that for brevity, managers should
            consult the mplsTunnelTable present in the MPLS\-TE MIB for
            additional information about the protecting and protected
            tunnels, and the ifEntry in the IF\-MIB for the protected
            interface.
            
            .. attribute:: cmplsfrrfacrouteprotectedifindex  (key)
            
            	Uniquely identifies the interface configured for FRR protection
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cmplsfrrfacrouteprotectingtunindex  (key)
            
            	Uniquely identifies the mplsTunnelEntry primary index for the tunnel head interface designated to protect the  interface as specified in the mplsFrrFacRouteIfProtectedIndex (and all of the tunnels using this interface)
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cmplsfrrfacrouteprotectedtunindex  (key)
            
            	Uniquely identifies an mplsTunnelEntry that is being protected by FRR
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cmplsfrrfacrouteprotectedtuninstance  (key)
            
            	Uniquely identifies an mplsTunnelEntry that is being protected by FRR
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsfrrfacrouteprotectedtuningresslsrid  (key)
            
            	Uniquely identifies an mplsTunnelEntry that is being protected by FRR
            	**type**\: str
            
            	**length:** 4
            
            .. attribute:: cmplsfrrfacrouteprotectedtunegresslsrid  (key)
            
            	Uniquely identifies an mplsTunnelEntry that is being protected by FRR
            	**type**\: str
            
            	**length:** 4
            
            .. attribute:: cmplsfrrfacrouteprotectedtunstatus
            
            	Specifies the state of the protected tunnel.  active  This tunnel's label has been placed in the          LFIB and is ready to be applied to incoming          packets.           ready \-  This tunnel's label entry has been created but is          not yet in the LFIB.           partial \- This tunnel's label entry as not been fully           created
            	**type**\:  :py:class:`Cmplsfrrfacrouteprotectedtunstatus <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CISCOIETFFRRMIB.Cmplsfrrfacroutedbtable.Cmplsfrrfacroutedbentry.Cmplsfrrfacrouteprotectedtunstatus>`
            
            .. attribute:: cmplsfrrfacrouteprotectingtunresvbw
            
            	Specifies the amount of bandwidth in megabytes per second that is actually reserved by the backup tunnel for facility backup. This value is repeated here from the MPLS\- TE MIB because the tunnel entry will reveal the bandwidth reserved by the signaling protocol, which is typically 0 for backup tunnels so as to not over\-book bandwidth. However, internal reservations are typically made on the PLR, thus this value should be revealed here
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsfrrfacrouteprotectingtunprotectiontype
            
            	Indicates type of the resource protection
            	**type**\:  :py:class:`Cmplsfrrfacrouteprotectingtunprotectiontype <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CISCOIETFFRRMIB.Cmplsfrrfacroutedbtable.Cmplsfrrfacroutedbentry.Cmplsfrrfacrouteprotectingtunprotectiontype>`
            
            

            """

            _prefix = 'CISCO-IETF-FRR-MIB'
            _revision = '2008-04-29'

            def __init__(self):
                super(CISCOIETFFRRMIB.Cmplsfrrfacroutedbtable.Cmplsfrrfacroutedbentry, self).__init__()

                self.yang_name = "cmplsFrrFacRouteDBEntry"
                self.yang_parent_name = "cmplsFrrFacRouteDBTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cmplsfrrfacrouteprotectedifindex','cmplsfrrfacrouteprotectingtunindex','cmplsfrrfacrouteprotectedtunindex','cmplsfrrfacrouteprotectedtuninstance','cmplsfrrfacrouteprotectedtuningresslsrid','cmplsfrrfacrouteprotectedtunegresslsrid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cmplsfrrfacrouteprotectedifindex', YLeaf(YType.int32, 'cmplsFrrFacRouteProtectedIfIndex')),
                    ('cmplsfrrfacrouteprotectingtunindex', YLeaf(YType.uint32, 'cmplsFrrFacRouteProtectingTunIndex')),
                    ('cmplsfrrfacrouteprotectedtunindex', YLeaf(YType.uint32, 'cmplsFrrFacRouteProtectedTunIndex')),
                    ('cmplsfrrfacrouteprotectedtuninstance', YLeaf(YType.uint32, 'cmplsFrrFacRouteProtectedTunInstance')),
                    ('cmplsfrrfacrouteprotectedtuningresslsrid', YLeaf(YType.str, 'cmplsFrrFacRouteProtectedTunIngressLSRId')),
                    ('cmplsfrrfacrouteprotectedtunegresslsrid', YLeaf(YType.str, 'cmplsFrrFacRouteProtectedTunEgressLSRId')),
                    ('cmplsfrrfacrouteprotectedtunstatus', YLeaf(YType.enumeration, 'cmplsFrrFacRouteProtectedTunStatus')),
                    ('cmplsfrrfacrouteprotectingtunresvbw', YLeaf(YType.uint32, 'cmplsFrrFacRouteProtectingTunResvBw')),
                    ('cmplsfrrfacrouteprotectingtunprotectiontype', YLeaf(YType.enumeration, 'cmplsFrrFacRouteProtectingTunProtectionType')),
                ])
                self.cmplsfrrfacrouteprotectedifindex = None
                self.cmplsfrrfacrouteprotectingtunindex = None
                self.cmplsfrrfacrouteprotectedtunindex = None
                self.cmplsfrrfacrouteprotectedtuninstance = None
                self.cmplsfrrfacrouteprotectedtuningresslsrid = None
                self.cmplsfrrfacrouteprotectedtunegresslsrid = None
                self.cmplsfrrfacrouteprotectedtunstatus = None
                self.cmplsfrrfacrouteprotectingtunresvbw = None
                self.cmplsfrrfacrouteprotectingtunprotectiontype = None
                self._segment_path = lambda: "cmplsFrrFacRouteDBEntry" + "[cmplsFrrFacRouteProtectedIfIndex='" + str(self.cmplsfrrfacrouteprotectedifindex) + "']" + "[cmplsFrrFacRouteProtectingTunIndex='" + str(self.cmplsfrrfacrouteprotectingtunindex) + "']" + "[cmplsFrrFacRouteProtectedTunIndex='" + str(self.cmplsfrrfacrouteprotectedtunindex) + "']" + "[cmplsFrrFacRouteProtectedTunInstance='" + str(self.cmplsfrrfacrouteprotectedtuninstance) + "']" + "[cmplsFrrFacRouteProtectedTunIngressLSRId='" + str(self.cmplsfrrfacrouteprotectedtuningresslsrid) + "']" + "[cmplsFrrFacRouteProtectedTunEgressLSRId='" + str(self.cmplsfrrfacrouteprotectedtunegresslsrid) + "']"
                self._absolute_path = lambda: "CISCO-IETF-FRR-MIB:CISCO-IETF-FRR-MIB/cmplsFrrFacRouteDBTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFFRRMIB.Cmplsfrrfacroutedbtable.Cmplsfrrfacroutedbentry, ['cmplsfrrfacrouteprotectedifindex', 'cmplsfrrfacrouteprotectingtunindex', 'cmplsfrrfacrouteprotectedtunindex', 'cmplsfrrfacrouteprotectedtuninstance', 'cmplsfrrfacrouteprotectedtuningresslsrid', 'cmplsfrrfacrouteprotectedtunegresslsrid', 'cmplsfrrfacrouteprotectedtunstatus', 'cmplsfrrfacrouteprotectingtunresvbw', 'cmplsfrrfacrouteprotectingtunprotectiontype'], name, value)

            class Cmplsfrrfacrouteprotectedtunstatus(Enum):
                """
                Cmplsfrrfacrouteprotectedtunstatus (Enum Class)

                Specifies the state of the protected tunnel.

                active  This tunnel's label has been placed in the

                         LFIB and is ready to be applied to incoming

                         packets.

                ready \-  This tunnel's label entry has been created but is

                         not yet in the LFIB.

                partial \- This tunnel's label entry as not been fully

                          created.

                .. data:: active = 1

                .. data:: ready = 2

                .. data:: partial = 3

                """

                active = Enum.YLeaf(1, "active")

                ready = Enum.YLeaf(2, "ready")

                partial = Enum.YLeaf(3, "partial")


            class Cmplsfrrfacrouteprotectingtunprotectiontype(Enum):
                """
                Cmplsfrrfacrouteprotectingtunprotectiontype (Enum Class)

                Indicates type of the resource protection.

                .. data:: linkProtection = 0

                .. data:: nodeProtection = 1

                """

                linkProtection = Enum.YLeaf(0, "linkProtection")

                nodeProtection = Enum.YLeaf(1, "nodeProtection")


    def clone_ptr(self):
        self._top_entity = CISCOIETFFRRMIB()
        return self._top_entity


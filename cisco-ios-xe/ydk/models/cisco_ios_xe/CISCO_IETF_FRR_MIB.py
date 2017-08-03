""" CISCO_IETF_FRR_MIB 

This MIB module contains managed object definitions for MPLS
Fast Reroute (FRR) as defined in\:Pan, P., Gan, D., Swallow, G.,
Vasseur, J.Ph., Cooper, D., Atlas, A., Jork, M., Fast Reroute
Techniques in RSVP\-TE, draft\-ietf\-mpls\-rsvp\-lsp\-fastreroute\-
00.txt, January 2002.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoIetfFrrMib(Entity):
    """
    
    
    .. attribute:: cmplsfrrconsttable
    
    	This table shows detour setup constraints
    	**type**\:   :py:class:`Cmplsfrrconsttable <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CiscoIetfFrrMib.Cmplsfrrconsttable>`
    
    .. attribute:: cmplsfrrfacroutedbtable
    
    	The mplsFrrFacRouteDBTable provides information about the  fast reroute database.  Each entry belongs to an interface, protecting backup tunnel and protected tunnel. MPLS  interfaces defined on this node are protected by backup tunnels and are indexed by mplsFrrFacRouteProtectedIndex. Backup tunnels defined to protect the tunnels traversing an interface, and are indexed by  mplsFrrFacRouteProtectingTunIndex.  Note that the tunnel  instance index is not required, since it is implied to be 0,  which indicates the tunnel head interface for the protecting  tunnel. The protecting tunnel is defined to exist on the PLR  in the FRR specification.  Protected tunnels are the LSPs that  traverse the protected link.  These LSPs are uniquely  identified by mplsFrrFacRouteProtectedTunIndex, mplsFrrFacRouteProtectedTunInstance,  mplsFrrFacRouteProtectedTunIngressLSRId, and  mplsFrrFacRouteProtectedTunEgressLSRId
    	**type**\:   :py:class:`Cmplsfrrfacroutedbtable <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CiscoIetfFrrMib.Cmplsfrrfacroutedbtable>`
    
    .. attribute:: cmplsfrrlogtable
    
    	The fast reroute log table records fast reroute events such as protected links going up or down or the FRR feature kicking in
    	**type**\:   :py:class:`Cmplsfrrlogtable <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CiscoIetfFrrMib.Cmplsfrrlogtable>`
    
    .. attribute:: cmplsfrrscalars
    
    	
    	**type**\:   :py:class:`Cmplsfrrscalars <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CiscoIetfFrrMib.Cmplsfrrscalars>`
    
    

    """

    _prefix = 'CISCO-IETF-FRR-MIB'
    _revision = '2008-04-29'

    def __init__(self):
        super(CiscoIetfFrrMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IETF-FRR-MIB"
        self.yang_parent_name = "CISCO-IETF-FRR-MIB"

        self.cmplsfrrconsttable = CiscoIetfFrrMib.Cmplsfrrconsttable()
        self.cmplsfrrconsttable.parent = self
        self._children_name_map["cmplsfrrconsttable"] = "cmplsFrrConstTable"
        self._children_yang_names.add("cmplsFrrConstTable")

        self.cmplsfrrfacroutedbtable = CiscoIetfFrrMib.Cmplsfrrfacroutedbtable()
        self.cmplsfrrfacroutedbtable.parent = self
        self._children_name_map["cmplsfrrfacroutedbtable"] = "cmplsFrrFacRouteDBTable"
        self._children_yang_names.add("cmplsFrrFacRouteDBTable")

        self.cmplsfrrlogtable = CiscoIetfFrrMib.Cmplsfrrlogtable()
        self.cmplsfrrlogtable.parent = self
        self._children_name_map["cmplsfrrlogtable"] = "cmplsFrrLogTable"
        self._children_yang_names.add("cmplsFrrLogTable")

        self.cmplsfrrscalars = CiscoIetfFrrMib.Cmplsfrrscalars()
        self.cmplsfrrscalars.parent = self
        self._children_name_map["cmplsfrrscalars"] = "cmplsFrrScalars"
        self._children_yang_names.add("cmplsFrrScalars")


    class Cmplsfrrscalars(Entity):
        """
        
        
        .. attribute:: cmplsfrractprotectedifs
        
        	Indicates the number of interfaces currently being protected  by the FRR feature if mplsFrrConstProtectionMethod is set to facilityBackup(1), otherwise this value should return 0 to indicate that LSPs traversing any interface may be protected. This value MUST be less than or equal to mplsFrrConfIfs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cmplsfrractprotectedlsps
        
        	Indicates the number of LSPs currently protected by  the FRR feature. If mplsFrrConstProtectionMethod is set  to facilityBackup(1)this object MUST return 0
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cmplsfrractprotectedtuns
        
        	Indicates the number of bypass tunnels indicated in mplsFrrConfProtectingTuns whose operStatus is up(1) indicating that they are currently protecting facilities on this LSR using the FRR feature. This object MUST return 0 if mplsFrrConstProtectionMethod  is set to facilityBackup(1)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cmplsfrrconfprotectingtuns
        
        	Indicates the number of bypass tunnels configured to  protect facilities on this LSR using the FRR feature  if mplsFrrConstProtectionMethod is set to  facilityBackup(1), otherwise this value MUST return  0
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cmplsfrrconstprotectionmethod
        
        	Indicates which protection method is to be used for fast reroute. Some devices may require a reboot of their routing processors if this variable is changed. An agent which does not wish to reboot or modify its FRR mode  MUST return an inconsistentValue error. Please  consult the device's agent capability statement  for more details
        	**type**\:   :py:class:`Cmplsfrrconstprotectionmethod <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CiscoIetfFrrMib.Cmplsfrrscalars.Cmplsfrrconstprotectionmethod>`
        
        .. attribute:: cmplsfrrdetourincoming
        
        	The number of detour LSPs entering the device if mplsFrrConstProtectionMethod is set to oneToOneBackup(0), or or 0 if mplsFrrConstProtectionMethod is set to facilityBackup(1)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cmplsfrrdetouroriginating
        
        	The number of detour LSPs originating at this PLR if mplsFrrConstProtectionMethod is set to oneToOneBackup(0). This object MUST return 0 if the mplsFrrConstProtectionMethod  is set to facilityBackup(1)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cmplsfrrdetouroutgoing
        
        	The number of detour LSPs leaving the device if mplsFrrConstProtectionMethod is set to oneToOneBackup(0), or 0 if mplsFrrConstProtectionMethod is set to  to facilityBackup(1)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cmplsfrrlogtablecurrentries
        
        	Indicates the current number of entries in the FRR log table
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cmplsfrrlogtablemaxentries
        
        	Indicates the maximum number of entries allowed in the FRR Log table. Agents receiving SETs for values that cannot be used must return an inconsistent value error. If a manager sets this value to 0, this indicates that no logging should take place by the agent.    If this value is returned as 0, this indicates that no additional log entries will be added to the current table either because the table has been completely filled or logging has been disabled. However, agents may wish to not delete existing entries in the log table so that managers may review them in the future.   It is implied that when mplsFrrLogTableCurrEntries  has reached the value of this variable, that logging  entries may not continue to be added to the table,  although existing ones may remain.  Furthermore, an agent may begin to delete existing (perhaps the oldest entries) entries to make room for new ones
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cmplsfrrnotifmaxrate
        
        	This variable indicates the number of milliseconds that must elapse between notification emissions. If events occur more rapidly, the implementation may simply fail to emit these notifications during that period, or may queue them until an appropriate time in the future. A value of 0 means no minimum  elapsed period is specified
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cmplsfrrnotifsenabled
        
        	Enables or disables FRR notifications defined in this MIB module. Notifications are disabled by default
        	**type**\:  bool
        
        .. attribute:: cmplsfrrnumofconfifs
        
        	Indicates the number of MPLS interfaces configured for  protection by the FRR feature, otherwise this value MUST return 0 to indicate that LSPs traversing any  interface may be protected
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cmplsfrrswitchover
        
        	The number of tunnel instances that are switched over to their corresponding detour LSP if mplsFrrConstProtectionMethod is set to oneToOneBackup(0), or tunnels being switched over if mplsFrrConstProtectionMethod is set to facilityBackup(1)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-IETF-FRR-MIB'
        _revision = '2008-04-29'

        def __init__(self):
            super(CiscoIetfFrrMib.Cmplsfrrscalars, self).__init__()

            self.yang_name = "cmplsFrrScalars"
            self.yang_parent_name = "CISCO-IETF-FRR-MIB"

            self.cmplsfrractprotectedifs = YLeaf(YType.uint32, "cmplsFrrActProtectedIfs")

            self.cmplsfrractprotectedlsps = YLeaf(YType.uint32, "cmplsFrrActProtectedLSPs")

            self.cmplsfrractprotectedtuns = YLeaf(YType.uint32, "cmplsFrrActProtectedTuns")

            self.cmplsfrrconfprotectingtuns = YLeaf(YType.uint32, "cmplsFrrConfProtectingTuns")

            self.cmplsfrrconstprotectionmethod = YLeaf(YType.enumeration, "cmplsFrrConstProtectionMethod")

            self.cmplsfrrdetourincoming = YLeaf(YType.uint32, "cmplsFrrDetourIncoming")

            self.cmplsfrrdetouroriginating = YLeaf(YType.uint32, "cmplsFrrDetourOriginating")

            self.cmplsfrrdetouroutgoing = YLeaf(YType.uint32, "cmplsFrrDetourOutgoing")

            self.cmplsfrrlogtablecurrentries = YLeaf(YType.uint32, "cmplsFrrLogTableCurrEntries")

            self.cmplsfrrlogtablemaxentries = YLeaf(YType.uint32, "cmplsFrrLogTableMaxEntries")

            self.cmplsfrrnotifmaxrate = YLeaf(YType.uint32, "cmplsFrrNotifMaxRate")

            self.cmplsfrrnotifsenabled = YLeaf(YType.boolean, "cmplsFrrNotifsEnabled")

            self.cmplsfrrnumofconfifs = YLeaf(YType.uint32, "cmplsFrrNumOfConfIfs")

            self.cmplsfrrswitchover = YLeaf(YType.uint32, "cmplsFrrSwitchover")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cmplsfrractprotectedifs",
                            "cmplsfrractprotectedlsps",
                            "cmplsfrractprotectedtuns",
                            "cmplsfrrconfprotectingtuns",
                            "cmplsfrrconstprotectionmethod",
                            "cmplsfrrdetourincoming",
                            "cmplsfrrdetouroriginating",
                            "cmplsfrrdetouroutgoing",
                            "cmplsfrrlogtablecurrentries",
                            "cmplsfrrlogtablemaxentries",
                            "cmplsfrrnotifmaxrate",
                            "cmplsfrrnotifsenabled",
                            "cmplsfrrnumofconfifs",
                            "cmplsfrrswitchover") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIetfFrrMib.Cmplsfrrscalars, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfFrrMib.Cmplsfrrscalars, self).__setattr__(name, value)

        class Cmplsfrrconstprotectionmethod(Enum):
            """
            Cmplsfrrconstprotectionmethod

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


        def has_data(self):
            return (
                self.cmplsfrractprotectedifs.is_set or
                self.cmplsfrractprotectedlsps.is_set or
                self.cmplsfrractprotectedtuns.is_set or
                self.cmplsfrrconfprotectingtuns.is_set or
                self.cmplsfrrconstprotectionmethod.is_set or
                self.cmplsfrrdetourincoming.is_set or
                self.cmplsfrrdetouroriginating.is_set or
                self.cmplsfrrdetouroutgoing.is_set or
                self.cmplsfrrlogtablecurrentries.is_set or
                self.cmplsfrrlogtablemaxentries.is_set or
                self.cmplsfrrnotifmaxrate.is_set or
                self.cmplsfrrnotifsenabled.is_set or
                self.cmplsfrrnumofconfifs.is_set or
                self.cmplsfrrswitchover.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cmplsfrractprotectedifs.yfilter != YFilter.not_set or
                self.cmplsfrractprotectedlsps.yfilter != YFilter.not_set or
                self.cmplsfrractprotectedtuns.yfilter != YFilter.not_set or
                self.cmplsfrrconfprotectingtuns.yfilter != YFilter.not_set or
                self.cmplsfrrconstprotectionmethod.yfilter != YFilter.not_set or
                self.cmplsfrrdetourincoming.yfilter != YFilter.not_set or
                self.cmplsfrrdetouroriginating.yfilter != YFilter.not_set or
                self.cmplsfrrdetouroutgoing.yfilter != YFilter.not_set or
                self.cmplsfrrlogtablecurrentries.yfilter != YFilter.not_set or
                self.cmplsfrrlogtablemaxentries.yfilter != YFilter.not_set or
                self.cmplsfrrnotifmaxrate.yfilter != YFilter.not_set or
                self.cmplsfrrnotifsenabled.yfilter != YFilter.not_set or
                self.cmplsfrrnumofconfifs.yfilter != YFilter.not_set or
                self.cmplsfrrswitchover.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cmplsFrrScalars" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-FRR-MIB:CISCO-IETF-FRR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cmplsfrractprotectedifs.is_set or self.cmplsfrractprotectedifs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cmplsfrractprotectedifs.get_name_leafdata())
            if (self.cmplsfrractprotectedlsps.is_set or self.cmplsfrractprotectedlsps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cmplsfrractprotectedlsps.get_name_leafdata())
            if (self.cmplsfrractprotectedtuns.is_set or self.cmplsfrractprotectedtuns.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cmplsfrractprotectedtuns.get_name_leafdata())
            if (self.cmplsfrrconfprotectingtuns.is_set or self.cmplsfrrconfprotectingtuns.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cmplsfrrconfprotectingtuns.get_name_leafdata())
            if (self.cmplsfrrconstprotectionmethod.is_set or self.cmplsfrrconstprotectionmethod.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cmplsfrrconstprotectionmethod.get_name_leafdata())
            if (self.cmplsfrrdetourincoming.is_set or self.cmplsfrrdetourincoming.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cmplsfrrdetourincoming.get_name_leafdata())
            if (self.cmplsfrrdetouroriginating.is_set or self.cmplsfrrdetouroriginating.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cmplsfrrdetouroriginating.get_name_leafdata())
            if (self.cmplsfrrdetouroutgoing.is_set or self.cmplsfrrdetouroutgoing.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cmplsfrrdetouroutgoing.get_name_leafdata())
            if (self.cmplsfrrlogtablecurrentries.is_set or self.cmplsfrrlogtablecurrentries.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cmplsfrrlogtablecurrentries.get_name_leafdata())
            if (self.cmplsfrrlogtablemaxentries.is_set or self.cmplsfrrlogtablemaxentries.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cmplsfrrlogtablemaxentries.get_name_leafdata())
            if (self.cmplsfrrnotifmaxrate.is_set or self.cmplsfrrnotifmaxrate.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cmplsfrrnotifmaxrate.get_name_leafdata())
            if (self.cmplsfrrnotifsenabled.is_set or self.cmplsfrrnotifsenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cmplsfrrnotifsenabled.get_name_leafdata())
            if (self.cmplsfrrnumofconfifs.is_set or self.cmplsfrrnumofconfifs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cmplsfrrnumofconfifs.get_name_leafdata())
            if (self.cmplsfrrswitchover.is_set or self.cmplsfrrswitchover.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cmplsfrrswitchover.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cmplsFrrActProtectedIfs" or name == "cmplsFrrActProtectedLSPs" or name == "cmplsFrrActProtectedTuns" or name == "cmplsFrrConfProtectingTuns" or name == "cmplsFrrConstProtectionMethod" or name == "cmplsFrrDetourIncoming" or name == "cmplsFrrDetourOriginating" or name == "cmplsFrrDetourOutgoing" or name == "cmplsFrrLogTableCurrEntries" or name == "cmplsFrrLogTableMaxEntries" or name == "cmplsFrrNotifMaxRate" or name == "cmplsFrrNotifsEnabled" or name == "cmplsFrrNumOfConfIfs" or name == "cmplsFrrSwitchover"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cmplsFrrActProtectedIfs"):
                self.cmplsfrractprotectedifs = value
                self.cmplsfrractprotectedifs.value_namespace = name_space
                self.cmplsfrractprotectedifs.value_namespace_prefix = name_space_prefix
            if(value_path == "cmplsFrrActProtectedLSPs"):
                self.cmplsfrractprotectedlsps = value
                self.cmplsfrractprotectedlsps.value_namespace = name_space
                self.cmplsfrractprotectedlsps.value_namespace_prefix = name_space_prefix
            if(value_path == "cmplsFrrActProtectedTuns"):
                self.cmplsfrractprotectedtuns = value
                self.cmplsfrractprotectedtuns.value_namespace = name_space
                self.cmplsfrractprotectedtuns.value_namespace_prefix = name_space_prefix
            if(value_path == "cmplsFrrConfProtectingTuns"):
                self.cmplsfrrconfprotectingtuns = value
                self.cmplsfrrconfprotectingtuns.value_namespace = name_space
                self.cmplsfrrconfprotectingtuns.value_namespace_prefix = name_space_prefix
            if(value_path == "cmplsFrrConstProtectionMethod"):
                self.cmplsfrrconstprotectionmethod = value
                self.cmplsfrrconstprotectionmethod.value_namespace = name_space
                self.cmplsfrrconstprotectionmethod.value_namespace_prefix = name_space_prefix
            if(value_path == "cmplsFrrDetourIncoming"):
                self.cmplsfrrdetourincoming = value
                self.cmplsfrrdetourincoming.value_namespace = name_space
                self.cmplsfrrdetourincoming.value_namespace_prefix = name_space_prefix
            if(value_path == "cmplsFrrDetourOriginating"):
                self.cmplsfrrdetouroriginating = value
                self.cmplsfrrdetouroriginating.value_namespace = name_space
                self.cmplsfrrdetouroriginating.value_namespace_prefix = name_space_prefix
            if(value_path == "cmplsFrrDetourOutgoing"):
                self.cmplsfrrdetouroutgoing = value
                self.cmplsfrrdetouroutgoing.value_namespace = name_space
                self.cmplsfrrdetouroutgoing.value_namespace_prefix = name_space_prefix
            if(value_path == "cmplsFrrLogTableCurrEntries"):
                self.cmplsfrrlogtablecurrentries = value
                self.cmplsfrrlogtablecurrentries.value_namespace = name_space
                self.cmplsfrrlogtablecurrentries.value_namespace_prefix = name_space_prefix
            if(value_path == "cmplsFrrLogTableMaxEntries"):
                self.cmplsfrrlogtablemaxentries = value
                self.cmplsfrrlogtablemaxentries.value_namespace = name_space
                self.cmplsfrrlogtablemaxentries.value_namespace_prefix = name_space_prefix
            if(value_path == "cmplsFrrNotifMaxRate"):
                self.cmplsfrrnotifmaxrate = value
                self.cmplsfrrnotifmaxrate.value_namespace = name_space
                self.cmplsfrrnotifmaxrate.value_namespace_prefix = name_space_prefix
            if(value_path == "cmplsFrrNotifsEnabled"):
                self.cmplsfrrnotifsenabled = value
                self.cmplsfrrnotifsenabled.value_namespace = name_space
                self.cmplsfrrnotifsenabled.value_namespace_prefix = name_space_prefix
            if(value_path == "cmplsFrrNumOfConfIfs"):
                self.cmplsfrrnumofconfifs = value
                self.cmplsfrrnumofconfifs.value_namespace = name_space
                self.cmplsfrrnumofconfifs.value_namespace_prefix = name_space_prefix
            if(value_path == "cmplsFrrSwitchover"):
                self.cmplsfrrswitchover = value
                self.cmplsfrrswitchover.value_namespace = name_space
                self.cmplsfrrswitchover.value_namespace_prefix = name_space_prefix


    class Cmplsfrrconsttable(Entity):
        """
        This table shows detour setup constraints.
        
        .. attribute:: cmplsfrrconstentry
        
        	An entry in this table represents detour LSP or bypass tunnel  setup constraints for a tunnel instance to be protected by  detour LSPs or a tunnel. Agents must allow entries in this table  to be created only for tunnel instances that require fast\-reroute. Entries indexed with mplsFrrConstIfIndex set to 0 apply to all interfaces on this device for which the FRR feature can operate on
        	**type**\: list of    :py:class:`Cmplsfrrconstentry <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CiscoIetfFrrMib.Cmplsfrrconsttable.Cmplsfrrconstentry>`
        
        

        """

        _prefix = 'CISCO-IETF-FRR-MIB'
        _revision = '2008-04-29'

        def __init__(self):
            super(CiscoIetfFrrMib.Cmplsfrrconsttable, self).__init__()

            self.yang_name = "cmplsFrrConstTable"
            self.yang_parent_name = "CISCO-IETF-FRR-MIB"

            self.cmplsfrrconstentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIetfFrrMib.Cmplsfrrconsttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfFrrMib.Cmplsfrrconsttable, self).__setattr__(name, value)


        class Cmplsfrrconstentry(Entity):
            """
            An entry in this table represents detour LSP or bypass tunnel 
            setup constraints for a tunnel instance to be protected by 
            detour LSPs or a tunnel. Agents must allow entries in this table 
            to be created only for tunnel instances that require fast\-reroute.
            Entries indexed with mplsFrrConstIfIndex set to 0 apply to all
            interfaces on this device for which the FRR feature can operate
            on.
            
            .. attribute:: cmplsfrrconstifindex  <key>
            
            	Uniquely identifies an interface for which fast reroute is configured. Tabular entries indexed with a 0 value apply to all interfaces on this device for which the FRR feature can operate on
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cmplsfrrconsttunnelindex  <key>
            
            	Uniquely identifies a tunnel for which fast reroute is requested
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cmplsfrrconsttunnelinstance  <key>
            
            	Uniquely identifies an instance of this tunnel for which fast reroute is requested
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsfrrconstbandwidth
            
            	This variable represents the bandwidth for detour LSPs of this tunnel, in units of thousands of bits per second (Kbps)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsfrrconstexclallaffinity
            
            	A link satisfies the exclude\-all constraint if and only if the link contains none of the administrative groups specified in the constraint
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsfrrconstholdingprio
            
            	Indicates the holding priority for detour LSP
            	**type**\:  int
            
            	**range:** 0..7
            
            .. attribute:: cmplsfrrconsthoplimit
            
            	The maximum number of hops that the detour LSP may traverse
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: cmplsfrrconstinclallaffinity
            
            	A link satisfies the include\-all constraint if and only if the link contains all of the administrative groups specified in the constraint
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsfrrconstinclanyaffinity
            
            	A link satisfies the include\-any constraint if and only if the constraint is zero, or the link and the constraint have a resource class in common
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsfrrconstnumprotectedtunonif
            
            	The number of tunnels protected on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsfrrconstnumprotectingtunonif
            
            	The number of backup tunnels protecting the specified interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsfrrconstrowstatus
            
            	This object is used to create, modify, and/or delete a row in this table
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cmplsfrrconstsetupprio
            
            	Indicates the setup priority of detour LSP
            	**type**\:  int
            
            	**range:** 0..7
            
            

            """

            _prefix = 'CISCO-IETF-FRR-MIB'
            _revision = '2008-04-29'

            def __init__(self):
                super(CiscoIetfFrrMib.Cmplsfrrconsttable.Cmplsfrrconstentry, self).__init__()

                self.yang_name = "cmplsFrrConstEntry"
                self.yang_parent_name = "cmplsFrrConstTable"

                self.cmplsfrrconstifindex = YLeaf(YType.int32, "cmplsFrrConstIfIndex")

                self.cmplsfrrconsttunnelindex = YLeaf(YType.uint32, "cmplsFrrConstTunnelIndex")

                self.cmplsfrrconsttunnelinstance = YLeaf(YType.uint32, "cmplsFrrConstTunnelInstance")

                self.cmplsfrrconstbandwidth = YLeaf(YType.uint32, "cmplsFrrConstBandwidth")

                self.cmplsfrrconstexclallaffinity = YLeaf(YType.uint32, "cmplsFrrConstExclAllAffinity")

                self.cmplsfrrconstholdingprio = YLeaf(YType.uint32, "cmplsFrrConstHoldingPrio")

                self.cmplsfrrconsthoplimit = YLeaf(YType.uint32, "cmplsFrrConstHopLimit")

                self.cmplsfrrconstinclallaffinity = YLeaf(YType.uint32, "cmplsFrrConstInclAllAffinity")

                self.cmplsfrrconstinclanyaffinity = YLeaf(YType.uint32, "cmplsFrrConstInclAnyAffinity")

                self.cmplsfrrconstnumprotectedtunonif = YLeaf(YType.uint32, "cmplsFrrConstNumProtectedTunOnIf")

                self.cmplsfrrconstnumprotectingtunonif = YLeaf(YType.uint32, "cmplsFrrConstNumProtectingTunOnIf")

                self.cmplsfrrconstrowstatus = YLeaf(YType.enumeration, "cmplsFrrConstRowStatus")

                self.cmplsfrrconstsetupprio = YLeaf(YType.uint32, "cmplsFrrConstSetupPrio")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cmplsfrrconstifindex",
                                "cmplsfrrconsttunnelindex",
                                "cmplsfrrconsttunnelinstance",
                                "cmplsfrrconstbandwidth",
                                "cmplsfrrconstexclallaffinity",
                                "cmplsfrrconstholdingprio",
                                "cmplsfrrconsthoplimit",
                                "cmplsfrrconstinclallaffinity",
                                "cmplsfrrconstinclanyaffinity",
                                "cmplsfrrconstnumprotectedtunonif",
                                "cmplsfrrconstnumprotectingtunonif",
                                "cmplsfrrconstrowstatus",
                                "cmplsfrrconstsetupprio") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfFrrMib.Cmplsfrrconsttable.Cmplsfrrconstentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfFrrMib.Cmplsfrrconsttable.Cmplsfrrconstentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cmplsfrrconstifindex.is_set or
                    self.cmplsfrrconsttunnelindex.is_set or
                    self.cmplsfrrconsttunnelinstance.is_set or
                    self.cmplsfrrconstbandwidth.is_set or
                    self.cmplsfrrconstexclallaffinity.is_set or
                    self.cmplsfrrconstholdingprio.is_set or
                    self.cmplsfrrconsthoplimit.is_set or
                    self.cmplsfrrconstinclallaffinity.is_set or
                    self.cmplsfrrconstinclanyaffinity.is_set or
                    self.cmplsfrrconstnumprotectedtunonif.is_set or
                    self.cmplsfrrconstnumprotectingtunonif.is_set or
                    self.cmplsfrrconstrowstatus.is_set or
                    self.cmplsfrrconstsetupprio.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cmplsfrrconstifindex.yfilter != YFilter.not_set or
                    self.cmplsfrrconsttunnelindex.yfilter != YFilter.not_set or
                    self.cmplsfrrconsttunnelinstance.yfilter != YFilter.not_set or
                    self.cmplsfrrconstbandwidth.yfilter != YFilter.not_set or
                    self.cmplsfrrconstexclallaffinity.yfilter != YFilter.not_set or
                    self.cmplsfrrconstholdingprio.yfilter != YFilter.not_set or
                    self.cmplsfrrconsthoplimit.yfilter != YFilter.not_set or
                    self.cmplsfrrconstinclallaffinity.yfilter != YFilter.not_set or
                    self.cmplsfrrconstinclanyaffinity.yfilter != YFilter.not_set or
                    self.cmplsfrrconstnumprotectedtunonif.yfilter != YFilter.not_set or
                    self.cmplsfrrconstnumprotectingtunonif.yfilter != YFilter.not_set or
                    self.cmplsfrrconstrowstatus.yfilter != YFilter.not_set or
                    self.cmplsfrrconstsetupprio.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cmplsFrrConstEntry" + "[cmplsFrrConstIfIndex='" + self.cmplsfrrconstifindex.get() + "']" + "[cmplsFrrConstTunnelIndex='" + self.cmplsfrrconsttunnelindex.get() + "']" + "[cmplsFrrConstTunnelInstance='" + self.cmplsfrrconsttunnelinstance.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-FRR-MIB:CISCO-IETF-FRR-MIB/cmplsFrrConstTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cmplsfrrconstifindex.is_set or self.cmplsfrrconstifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrconstifindex.get_name_leafdata())
                if (self.cmplsfrrconsttunnelindex.is_set or self.cmplsfrrconsttunnelindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrconsttunnelindex.get_name_leafdata())
                if (self.cmplsfrrconsttunnelinstance.is_set or self.cmplsfrrconsttunnelinstance.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrconsttunnelinstance.get_name_leafdata())
                if (self.cmplsfrrconstbandwidth.is_set or self.cmplsfrrconstbandwidth.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrconstbandwidth.get_name_leafdata())
                if (self.cmplsfrrconstexclallaffinity.is_set or self.cmplsfrrconstexclallaffinity.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrconstexclallaffinity.get_name_leafdata())
                if (self.cmplsfrrconstholdingprio.is_set or self.cmplsfrrconstholdingprio.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrconstholdingprio.get_name_leafdata())
                if (self.cmplsfrrconsthoplimit.is_set or self.cmplsfrrconsthoplimit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrconsthoplimit.get_name_leafdata())
                if (self.cmplsfrrconstinclallaffinity.is_set or self.cmplsfrrconstinclallaffinity.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrconstinclallaffinity.get_name_leafdata())
                if (self.cmplsfrrconstinclanyaffinity.is_set or self.cmplsfrrconstinclanyaffinity.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrconstinclanyaffinity.get_name_leafdata())
                if (self.cmplsfrrconstnumprotectedtunonif.is_set or self.cmplsfrrconstnumprotectedtunonif.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrconstnumprotectedtunonif.get_name_leafdata())
                if (self.cmplsfrrconstnumprotectingtunonif.is_set or self.cmplsfrrconstnumprotectingtunonif.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrconstnumprotectingtunonif.get_name_leafdata())
                if (self.cmplsfrrconstrowstatus.is_set or self.cmplsfrrconstrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrconstrowstatus.get_name_leafdata())
                if (self.cmplsfrrconstsetupprio.is_set or self.cmplsfrrconstsetupprio.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrconstsetupprio.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cmplsFrrConstIfIndex" or name == "cmplsFrrConstTunnelIndex" or name == "cmplsFrrConstTunnelInstance" or name == "cmplsFrrConstBandwidth" or name == "cmplsFrrConstExclAllAffinity" or name == "cmplsFrrConstHoldingPrio" or name == "cmplsFrrConstHopLimit" or name == "cmplsFrrConstInclAllAffinity" or name == "cmplsFrrConstInclAnyAffinity" or name == "cmplsFrrConstNumProtectedTunOnIf" or name == "cmplsFrrConstNumProtectingTunOnIf" or name == "cmplsFrrConstRowStatus" or name == "cmplsFrrConstSetupPrio"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cmplsFrrConstIfIndex"):
                    self.cmplsfrrconstifindex = value
                    self.cmplsfrrconstifindex.value_namespace = name_space
                    self.cmplsfrrconstifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsFrrConstTunnelIndex"):
                    self.cmplsfrrconsttunnelindex = value
                    self.cmplsfrrconsttunnelindex.value_namespace = name_space
                    self.cmplsfrrconsttunnelindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsFrrConstTunnelInstance"):
                    self.cmplsfrrconsttunnelinstance = value
                    self.cmplsfrrconsttunnelinstance.value_namespace = name_space
                    self.cmplsfrrconsttunnelinstance.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsFrrConstBandwidth"):
                    self.cmplsfrrconstbandwidth = value
                    self.cmplsfrrconstbandwidth.value_namespace = name_space
                    self.cmplsfrrconstbandwidth.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsFrrConstExclAllAffinity"):
                    self.cmplsfrrconstexclallaffinity = value
                    self.cmplsfrrconstexclallaffinity.value_namespace = name_space
                    self.cmplsfrrconstexclallaffinity.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsFrrConstHoldingPrio"):
                    self.cmplsfrrconstholdingprio = value
                    self.cmplsfrrconstholdingprio.value_namespace = name_space
                    self.cmplsfrrconstholdingprio.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsFrrConstHopLimit"):
                    self.cmplsfrrconsthoplimit = value
                    self.cmplsfrrconsthoplimit.value_namespace = name_space
                    self.cmplsfrrconsthoplimit.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsFrrConstInclAllAffinity"):
                    self.cmplsfrrconstinclallaffinity = value
                    self.cmplsfrrconstinclallaffinity.value_namespace = name_space
                    self.cmplsfrrconstinclallaffinity.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsFrrConstInclAnyAffinity"):
                    self.cmplsfrrconstinclanyaffinity = value
                    self.cmplsfrrconstinclanyaffinity.value_namespace = name_space
                    self.cmplsfrrconstinclanyaffinity.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsFrrConstNumProtectedTunOnIf"):
                    self.cmplsfrrconstnumprotectedtunonif = value
                    self.cmplsfrrconstnumprotectedtunonif.value_namespace = name_space
                    self.cmplsfrrconstnumprotectedtunonif.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsFrrConstNumProtectingTunOnIf"):
                    self.cmplsfrrconstnumprotectingtunonif = value
                    self.cmplsfrrconstnumprotectingtunonif.value_namespace = name_space
                    self.cmplsfrrconstnumprotectingtunonif.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsFrrConstRowStatus"):
                    self.cmplsfrrconstrowstatus = value
                    self.cmplsfrrconstrowstatus.value_namespace = name_space
                    self.cmplsfrrconstrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsFrrConstSetupPrio"):
                    self.cmplsfrrconstsetupprio = value
                    self.cmplsfrrconstsetupprio.value_namespace = name_space
                    self.cmplsfrrconstsetupprio.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cmplsfrrconstentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cmplsfrrconstentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cmplsFrrConstTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-FRR-MIB:CISCO-IETF-FRR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cmplsFrrConstEntry"):
                for c in self.cmplsfrrconstentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfFrrMib.Cmplsfrrconsttable.Cmplsfrrconstentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cmplsfrrconstentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cmplsFrrConstEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cmplsfrrlogtable(Entity):
        """
        The fast reroute log table records fast reroute events such
        as protected links going up or down or the FRR feature
        kicking in.
        
        .. attribute:: cmplsfrrlogentry
        
        	An entry in this table is created to describe one fast reroute event.  Entries in this table are only created and destroyed by the agent implementation. The maximum number  of entries in this log is governed by the scalar
        	**type**\: list of    :py:class:`Cmplsfrrlogentry <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CiscoIetfFrrMib.Cmplsfrrlogtable.Cmplsfrrlogentry>`
        
        

        """

        _prefix = 'CISCO-IETF-FRR-MIB'
        _revision = '2008-04-29'

        def __init__(self):
            super(CiscoIetfFrrMib.Cmplsfrrlogtable, self).__init__()

            self.yang_name = "cmplsFrrLogTable"
            self.yang_parent_name = "CISCO-IETF-FRR-MIB"

            self.cmplsfrrlogentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIetfFrrMib.Cmplsfrrlogtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfFrrMib.Cmplsfrrlogtable, self).__setattr__(name, value)


        class Cmplsfrrlogentry(Entity):
            """
            An entry in this table is created to describe one fast
            reroute event.  Entries in this table are only created and
            destroyed by the agent implementation. The maximum number 
            of entries in this log is governed by the scalar.
            
            .. attribute:: cmplsfrrlogindex  <key>
            
            	Uniquely identifies a fast reroute event entry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsfrrlogeventduration
            
            	This object describes the duration of this event
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsfrrlogeventreasonstring
            
            	This object contains an implementation\-specific explanation of the event
            	**type**\:  str
            
            	**length:** 128
            
            .. attribute:: cmplsfrrlogeventtime
            
            	This object provides the amount of time ticks since this event occured
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsfrrlogeventtype
            
            	This object describes what type of fast reroute event occured
            	**type**\:   :py:class:`Cmplsfrrlogeventtype <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CiscoIetfFrrMib.Cmplsfrrlogtable.Cmplsfrrlogentry.Cmplsfrrlogeventtype>`
            
            .. attribute:: cmplsfrrloginterface
            
            	This object indicates which interface was affected by this FRR event. This value may be set to 0 if mplsFrrConstProtectionMethod is set to oneToOneBackup(0)
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'CISCO-IETF-FRR-MIB'
            _revision = '2008-04-29'

            def __init__(self):
                super(CiscoIetfFrrMib.Cmplsfrrlogtable.Cmplsfrrlogentry, self).__init__()

                self.yang_name = "cmplsFrrLogEntry"
                self.yang_parent_name = "cmplsFrrLogTable"

                self.cmplsfrrlogindex = YLeaf(YType.uint32, "cmplsFrrLogIndex")

                self.cmplsfrrlogeventduration = YLeaf(YType.uint32, "cmplsFrrLogEventDuration")

                self.cmplsfrrlogeventreasonstring = YLeaf(YType.str, "cmplsFrrLogEventReasonString")

                self.cmplsfrrlogeventtime = YLeaf(YType.uint32, "cmplsFrrLogEventTime")

                self.cmplsfrrlogeventtype = YLeaf(YType.enumeration, "cmplsFrrLogEventType")

                self.cmplsfrrloginterface = YLeaf(YType.int32, "cmplsFrrLogInterface")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cmplsfrrlogindex",
                                "cmplsfrrlogeventduration",
                                "cmplsfrrlogeventreasonstring",
                                "cmplsfrrlogeventtime",
                                "cmplsfrrlogeventtype",
                                "cmplsfrrloginterface") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfFrrMib.Cmplsfrrlogtable.Cmplsfrrlogentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfFrrMib.Cmplsfrrlogtable.Cmplsfrrlogentry, self).__setattr__(name, value)

            class Cmplsfrrlogeventtype(Enum):
                """
                Cmplsfrrlogeventtype

                This object describes what type of fast reroute event

                occured.

                .. data:: other = 1

                .. data:: protected = 2

                """

                other = Enum.YLeaf(1, "other")

                protected = Enum.YLeaf(2, "protected")


            def has_data(self):
                return (
                    self.cmplsfrrlogindex.is_set or
                    self.cmplsfrrlogeventduration.is_set or
                    self.cmplsfrrlogeventreasonstring.is_set or
                    self.cmplsfrrlogeventtime.is_set or
                    self.cmplsfrrlogeventtype.is_set or
                    self.cmplsfrrloginterface.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cmplsfrrlogindex.yfilter != YFilter.not_set or
                    self.cmplsfrrlogeventduration.yfilter != YFilter.not_set or
                    self.cmplsfrrlogeventreasonstring.yfilter != YFilter.not_set or
                    self.cmplsfrrlogeventtime.yfilter != YFilter.not_set or
                    self.cmplsfrrlogeventtype.yfilter != YFilter.not_set or
                    self.cmplsfrrloginterface.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cmplsFrrLogEntry" + "[cmplsFrrLogIndex='" + self.cmplsfrrlogindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-FRR-MIB:CISCO-IETF-FRR-MIB/cmplsFrrLogTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cmplsfrrlogindex.is_set or self.cmplsfrrlogindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrlogindex.get_name_leafdata())
                if (self.cmplsfrrlogeventduration.is_set or self.cmplsfrrlogeventduration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrlogeventduration.get_name_leafdata())
                if (self.cmplsfrrlogeventreasonstring.is_set or self.cmplsfrrlogeventreasonstring.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrlogeventreasonstring.get_name_leafdata())
                if (self.cmplsfrrlogeventtime.is_set or self.cmplsfrrlogeventtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrlogeventtime.get_name_leafdata())
                if (self.cmplsfrrlogeventtype.is_set or self.cmplsfrrlogeventtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrlogeventtype.get_name_leafdata())
                if (self.cmplsfrrloginterface.is_set or self.cmplsfrrloginterface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrloginterface.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cmplsFrrLogIndex" or name == "cmplsFrrLogEventDuration" or name == "cmplsFrrLogEventReasonString" or name == "cmplsFrrLogEventTime" or name == "cmplsFrrLogEventType" or name == "cmplsFrrLogInterface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cmplsFrrLogIndex"):
                    self.cmplsfrrlogindex = value
                    self.cmplsfrrlogindex.value_namespace = name_space
                    self.cmplsfrrlogindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsFrrLogEventDuration"):
                    self.cmplsfrrlogeventduration = value
                    self.cmplsfrrlogeventduration.value_namespace = name_space
                    self.cmplsfrrlogeventduration.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsFrrLogEventReasonString"):
                    self.cmplsfrrlogeventreasonstring = value
                    self.cmplsfrrlogeventreasonstring.value_namespace = name_space
                    self.cmplsfrrlogeventreasonstring.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsFrrLogEventTime"):
                    self.cmplsfrrlogeventtime = value
                    self.cmplsfrrlogeventtime.value_namespace = name_space
                    self.cmplsfrrlogeventtime.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsFrrLogEventType"):
                    self.cmplsfrrlogeventtype = value
                    self.cmplsfrrlogeventtype.value_namespace = name_space
                    self.cmplsfrrlogeventtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsFrrLogInterface"):
                    self.cmplsfrrloginterface = value
                    self.cmplsfrrloginterface.value_namespace = name_space
                    self.cmplsfrrloginterface.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cmplsfrrlogentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cmplsfrrlogentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cmplsFrrLogTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-FRR-MIB:CISCO-IETF-FRR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cmplsFrrLogEntry"):
                for c in self.cmplsfrrlogentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfFrrMib.Cmplsfrrlogtable.Cmplsfrrlogentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cmplsfrrlogentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cmplsFrrLogEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Cmplsfrrfacroutedbentry <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CiscoIetfFrrMib.Cmplsfrrfacroutedbtable.Cmplsfrrfacroutedbentry>`
        
        

        """

        _prefix = 'CISCO-IETF-FRR-MIB'
        _revision = '2008-04-29'

        def __init__(self):
            super(CiscoIetfFrrMib.Cmplsfrrfacroutedbtable, self).__init__()

            self.yang_name = "cmplsFrrFacRouteDBTable"
            self.yang_parent_name = "CISCO-IETF-FRR-MIB"

            self.cmplsfrrfacroutedbentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIetfFrrMib.Cmplsfrrfacroutedbtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfFrrMib.Cmplsfrrfacroutedbtable, self).__setattr__(name, value)


        class Cmplsfrrfacroutedbentry(Entity):
            """
            An entry in the mplsFrrDBTable represents a single protected
            LSP, protected by a backup tunnel and defined for a specific
            protected interface. Note that for brevity, managers should
            consult the mplsTunnelTable present in the MPLS\-TE MIB for
            additional information about the protecting and protected
            tunnels, and the ifEntry in the IF\-MIB for the protected
            interface.
            
            .. attribute:: cmplsfrrfacrouteprotectedifindex  <key>
            
            	Uniquely identifies the interface configured for FRR protection
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cmplsfrrfacrouteprotectingtunindex  <key>
            
            	Uniquely identifies the mplsTunnelEntry primary index for the tunnel head interface designated to protect the  interface as specified in the mplsFrrFacRouteIfProtectedIndex (and all of the tunnels using this interface)
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cmplsfrrfacrouteprotectedtunindex  <key>
            
            	Uniquely identifies an mplsTunnelEntry that is being protected by FRR
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cmplsfrrfacrouteprotectedtuninstance  <key>
            
            	Uniquely identifies an mplsTunnelEntry that is being protected by FRR
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsfrrfacrouteprotectedtuningresslsrid  <key>
            
            	Uniquely identifies an mplsTunnelEntry that is being protected by FRR
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: cmplsfrrfacrouteprotectedtunegresslsrid  <key>
            
            	Uniquely identifies an mplsTunnelEntry that is being protected by FRR
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: cmplsfrrfacrouteprotectedtunstatus
            
            	Specifies the state of the protected tunnel.  active  This tunnel's label has been placed in the          LFIB and is ready to be applied to incoming          packets.           ready \-  This tunnel's label entry has been created but is          not yet in the LFIB.           partial \- This tunnel's label entry as not been fully           created
            	**type**\:   :py:class:`Cmplsfrrfacrouteprotectedtunstatus <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CiscoIetfFrrMib.Cmplsfrrfacroutedbtable.Cmplsfrrfacroutedbentry.Cmplsfrrfacrouteprotectedtunstatus>`
            
            .. attribute:: cmplsfrrfacrouteprotectingtunprotectiontype
            
            	Indicates type of the resource protection
            	**type**\:   :py:class:`Cmplsfrrfacrouteprotectingtunprotectiontype <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CiscoIetfFrrMib.Cmplsfrrfacroutedbtable.Cmplsfrrfacroutedbentry.Cmplsfrrfacrouteprotectingtunprotectiontype>`
            
            .. attribute:: cmplsfrrfacrouteprotectingtunresvbw
            
            	Specifies the amount of bandwidth in megabytes per second that is actually reserved by the backup tunnel for facility backup. This value is repeated here from the MPLS\- TE MIB because the tunnel entry will reveal the bandwidth reserved by the signaling protocol, which is typically 0 for backup tunnels so as to not over\-book bandwidth. However, internal reservations are typically made on the PLR, thus this value should be revealed here
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-FRR-MIB'
            _revision = '2008-04-29'

            def __init__(self):
                super(CiscoIetfFrrMib.Cmplsfrrfacroutedbtable.Cmplsfrrfacroutedbentry, self).__init__()

                self.yang_name = "cmplsFrrFacRouteDBEntry"
                self.yang_parent_name = "cmplsFrrFacRouteDBTable"

                self.cmplsfrrfacrouteprotectedifindex = YLeaf(YType.int32, "cmplsFrrFacRouteProtectedIfIndex")

                self.cmplsfrrfacrouteprotectingtunindex = YLeaf(YType.uint32, "cmplsFrrFacRouteProtectingTunIndex")

                self.cmplsfrrfacrouteprotectedtunindex = YLeaf(YType.uint32, "cmplsFrrFacRouteProtectedTunIndex")

                self.cmplsfrrfacrouteprotectedtuninstance = YLeaf(YType.uint32, "cmplsFrrFacRouteProtectedTunInstance")

                self.cmplsfrrfacrouteprotectedtuningresslsrid = YLeaf(YType.str, "cmplsFrrFacRouteProtectedTunIngressLSRId")

                self.cmplsfrrfacrouteprotectedtunegresslsrid = YLeaf(YType.str, "cmplsFrrFacRouteProtectedTunEgressLSRId")

                self.cmplsfrrfacrouteprotectedtunstatus = YLeaf(YType.enumeration, "cmplsFrrFacRouteProtectedTunStatus")

                self.cmplsfrrfacrouteprotectingtunprotectiontype = YLeaf(YType.enumeration, "cmplsFrrFacRouteProtectingTunProtectionType")

                self.cmplsfrrfacrouteprotectingtunresvbw = YLeaf(YType.uint32, "cmplsFrrFacRouteProtectingTunResvBw")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cmplsfrrfacrouteprotectedifindex",
                                "cmplsfrrfacrouteprotectingtunindex",
                                "cmplsfrrfacrouteprotectedtunindex",
                                "cmplsfrrfacrouteprotectedtuninstance",
                                "cmplsfrrfacrouteprotectedtuningresslsrid",
                                "cmplsfrrfacrouteprotectedtunegresslsrid",
                                "cmplsfrrfacrouteprotectedtunstatus",
                                "cmplsfrrfacrouteprotectingtunprotectiontype",
                                "cmplsfrrfacrouteprotectingtunresvbw") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfFrrMib.Cmplsfrrfacroutedbtable.Cmplsfrrfacroutedbentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfFrrMib.Cmplsfrrfacroutedbtable.Cmplsfrrfacroutedbentry, self).__setattr__(name, value)

            class Cmplsfrrfacrouteprotectedtunstatus(Enum):
                """
                Cmplsfrrfacrouteprotectedtunstatus

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
                Cmplsfrrfacrouteprotectingtunprotectiontype

                Indicates type of the resource protection.

                .. data:: linkProtection = 0

                .. data:: nodeProtection = 1

                """

                linkProtection = Enum.YLeaf(0, "linkProtection")

                nodeProtection = Enum.YLeaf(1, "nodeProtection")


            def has_data(self):
                return (
                    self.cmplsfrrfacrouteprotectedifindex.is_set or
                    self.cmplsfrrfacrouteprotectingtunindex.is_set or
                    self.cmplsfrrfacrouteprotectedtunindex.is_set or
                    self.cmplsfrrfacrouteprotectedtuninstance.is_set or
                    self.cmplsfrrfacrouteprotectedtuningresslsrid.is_set or
                    self.cmplsfrrfacrouteprotectedtunegresslsrid.is_set or
                    self.cmplsfrrfacrouteprotectedtunstatus.is_set or
                    self.cmplsfrrfacrouteprotectingtunprotectiontype.is_set or
                    self.cmplsfrrfacrouteprotectingtunresvbw.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cmplsfrrfacrouteprotectedifindex.yfilter != YFilter.not_set or
                    self.cmplsfrrfacrouteprotectingtunindex.yfilter != YFilter.not_set or
                    self.cmplsfrrfacrouteprotectedtunindex.yfilter != YFilter.not_set or
                    self.cmplsfrrfacrouteprotectedtuninstance.yfilter != YFilter.not_set or
                    self.cmplsfrrfacrouteprotectedtuningresslsrid.yfilter != YFilter.not_set or
                    self.cmplsfrrfacrouteprotectedtunegresslsrid.yfilter != YFilter.not_set or
                    self.cmplsfrrfacrouteprotectedtunstatus.yfilter != YFilter.not_set or
                    self.cmplsfrrfacrouteprotectingtunprotectiontype.yfilter != YFilter.not_set or
                    self.cmplsfrrfacrouteprotectingtunresvbw.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cmplsFrrFacRouteDBEntry" + "[cmplsFrrFacRouteProtectedIfIndex='" + self.cmplsfrrfacrouteprotectedifindex.get() + "']" + "[cmplsFrrFacRouteProtectingTunIndex='" + self.cmplsfrrfacrouteprotectingtunindex.get() + "']" + "[cmplsFrrFacRouteProtectedTunIndex='" + self.cmplsfrrfacrouteprotectedtunindex.get() + "']" + "[cmplsFrrFacRouteProtectedTunInstance='" + self.cmplsfrrfacrouteprotectedtuninstance.get() + "']" + "[cmplsFrrFacRouteProtectedTunIngressLSRId='" + self.cmplsfrrfacrouteprotectedtuningresslsrid.get() + "']" + "[cmplsFrrFacRouteProtectedTunEgressLSRId='" + self.cmplsfrrfacrouteprotectedtunegresslsrid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-FRR-MIB:CISCO-IETF-FRR-MIB/cmplsFrrFacRouteDBTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cmplsfrrfacrouteprotectedifindex.is_set or self.cmplsfrrfacrouteprotectedifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrfacrouteprotectedifindex.get_name_leafdata())
                if (self.cmplsfrrfacrouteprotectingtunindex.is_set or self.cmplsfrrfacrouteprotectingtunindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrfacrouteprotectingtunindex.get_name_leafdata())
                if (self.cmplsfrrfacrouteprotectedtunindex.is_set or self.cmplsfrrfacrouteprotectedtunindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrfacrouteprotectedtunindex.get_name_leafdata())
                if (self.cmplsfrrfacrouteprotectedtuninstance.is_set or self.cmplsfrrfacrouteprotectedtuninstance.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrfacrouteprotectedtuninstance.get_name_leafdata())
                if (self.cmplsfrrfacrouteprotectedtuningresslsrid.is_set or self.cmplsfrrfacrouteprotectedtuningresslsrid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrfacrouteprotectedtuningresslsrid.get_name_leafdata())
                if (self.cmplsfrrfacrouteprotectedtunegresslsrid.is_set or self.cmplsfrrfacrouteprotectedtunegresslsrid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrfacrouteprotectedtunegresslsrid.get_name_leafdata())
                if (self.cmplsfrrfacrouteprotectedtunstatus.is_set or self.cmplsfrrfacrouteprotectedtunstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrfacrouteprotectedtunstatus.get_name_leafdata())
                if (self.cmplsfrrfacrouteprotectingtunprotectiontype.is_set or self.cmplsfrrfacrouteprotectingtunprotectiontype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrfacrouteprotectingtunprotectiontype.get_name_leafdata())
                if (self.cmplsfrrfacrouteprotectingtunresvbw.is_set or self.cmplsfrrfacrouteprotectingtunresvbw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsfrrfacrouteprotectingtunresvbw.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cmplsFrrFacRouteProtectedIfIndex" or name == "cmplsFrrFacRouteProtectingTunIndex" or name == "cmplsFrrFacRouteProtectedTunIndex" or name == "cmplsFrrFacRouteProtectedTunInstance" or name == "cmplsFrrFacRouteProtectedTunIngressLSRId" or name == "cmplsFrrFacRouteProtectedTunEgressLSRId" or name == "cmplsFrrFacRouteProtectedTunStatus" or name == "cmplsFrrFacRouteProtectingTunProtectionType" or name == "cmplsFrrFacRouteProtectingTunResvBw"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cmplsFrrFacRouteProtectedIfIndex"):
                    self.cmplsfrrfacrouteprotectedifindex = value
                    self.cmplsfrrfacrouteprotectedifindex.value_namespace = name_space
                    self.cmplsfrrfacrouteprotectedifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsFrrFacRouteProtectingTunIndex"):
                    self.cmplsfrrfacrouteprotectingtunindex = value
                    self.cmplsfrrfacrouteprotectingtunindex.value_namespace = name_space
                    self.cmplsfrrfacrouteprotectingtunindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsFrrFacRouteProtectedTunIndex"):
                    self.cmplsfrrfacrouteprotectedtunindex = value
                    self.cmplsfrrfacrouteprotectedtunindex.value_namespace = name_space
                    self.cmplsfrrfacrouteprotectedtunindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsFrrFacRouteProtectedTunInstance"):
                    self.cmplsfrrfacrouteprotectedtuninstance = value
                    self.cmplsfrrfacrouteprotectedtuninstance.value_namespace = name_space
                    self.cmplsfrrfacrouteprotectedtuninstance.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsFrrFacRouteProtectedTunIngressLSRId"):
                    self.cmplsfrrfacrouteprotectedtuningresslsrid = value
                    self.cmplsfrrfacrouteprotectedtuningresslsrid.value_namespace = name_space
                    self.cmplsfrrfacrouteprotectedtuningresslsrid.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsFrrFacRouteProtectedTunEgressLSRId"):
                    self.cmplsfrrfacrouteprotectedtunegresslsrid = value
                    self.cmplsfrrfacrouteprotectedtunegresslsrid.value_namespace = name_space
                    self.cmplsfrrfacrouteprotectedtunegresslsrid.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsFrrFacRouteProtectedTunStatus"):
                    self.cmplsfrrfacrouteprotectedtunstatus = value
                    self.cmplsfrrfacrouteprotectedtunstatus.value_namespace = name_space
                    self.cmplsfrrfacrouteprotectedtunstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsFrrFacRouteProtectingTunProtectionType"):
                    self.cmplsfrrfacrouteprotectingtunprotectiontype = value
                    self.cmplsfrrfacrouteprotectingtunprotectiontype.value_namespace = name_space
                    self.cmplsfrrfacrouteprotectingtunprotectiontype.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsFrrFacRouteProtectingTunResvBw"):
                    self.cmplsfrrfacrouteprotectingtunresvbw = value
                    self.cmplsfrrfacrouteprotectingtunresvbw.value_namespace = name_space
                    self.cmplsfrrfacrouteprotectingtunresvbw.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cmplsfrrfacroutedbentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cmplsfrrfacroutedbentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cmplsFrrFacRouteDBTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-FRR-MIB:CISCO-IETF-FRR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cmplsFrrFacRouteDBEntry"):
                for c in self.cmplsfrrfacroutedbentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfFrrMib.Cmplsfrrfacroutedbtable.Cmplsfrrfacroutedbentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cmplsfrrfacroutedbentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cmplsFrrFacRouteDBEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cmplsfrrconsttable is not None and self.cmplsfrrconsttable.has_data()) or
            (self.cmplsfrrfacroutedbtable is not None and self.cmplsfrrfacroutedbtable.has_data()) or
            (self.cmplsfrrlogtable is not None and self.cmplsfrrlogtable.has_data()) or
            (self.cmplsfrrscalars is not None and self.cmplsfrrscalars.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cmplsfrrconsttable is not None and self.cmplsfrrconsttable.has_operation()) or
            (self.cmplsfrrfacroutedbtable is not None and self.cmplsfrrfacroutedbtable.has_operation()) or
            (self.cmplsfrrlogtable is not None and self.cmplsfrrlogtable.has_operation()) or
            (self.cmplsfrrscalars is not None and self.cmplsfrrscalars.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-IETF-FRR-MIB:CISCO-IETF-FRR-MIB" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "cmplsFrrConstTable"):
            if (self.cmplsfrrconsttable is None):
                self.cmplsfrrconsttable = CiscoIetfFrrMib.Cmplsfrrconsttable()
                self.cmplsfrrconsttable.parent = self
                self._children_name_map["cmplsfrrconsttable"] = "cmplsFrrConstTable"
            return self.cmplsfrrconsttable

        if (child_yang_name == "cmplsFrrFacRouteDBTable"):
            if (self.cmplsfrrfacroutedbtable is None):
                self.cmplsfrrfacroutedbtable = CiscoIetfFrrMib.Cmplsfrrfacroutedbtable()
                self.cmplsfrrfacroutedbtable.parent = self
                self._children_name_map["cmplsfrrfacroutedbtable"] = "cmplsFrrFacRouteDBTable"
            return self.cmplsfrrfacroutedbtable

        if (child_yang_name == "cmplsFrrLogTable"):
            if (self.cmplsfrrlogtable is None):
                self.cmplsfrrlogtable = CiscoIetfFrrMib.Cmplsfrrlogtable()
                self.cmplsfrrlogtable.parent = self
                self._children_name_map["cmplsfrrlogtable"] = "cmplsFrrLogTable"
            return self.cmplsfrrlogtable

        if (child_yang_name == "cmplsFrrScalars"):
            if (self.cmplsfrrscalars is None):
                self.cmplsfrrscalars = CiscoIetfFrrMib.Cmplsfrrscalars()
                self.cmplsfrrscalars.parent = self
                self._children_name_map["cmplsfrrscalars"] = "cmplsFrrScalars"
            return self.cmplsfrrscalars

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cmplsFrrConstTable" or name == "cmplsFrrFacRouteDBTable" or name == "cmplsFrrLogTable" or name == "cmplsFrrScalars"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoIetfFrrMib()
        return self._top_entity


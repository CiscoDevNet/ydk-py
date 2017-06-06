""" CISCO_IETF_FRR_MIB 

This MIB module contains managed object definitions for MPLS
Fast Reroute (FRR) as defined in\:Pan, P., Gan, D., Swallow, G.,
Vasseur, J.Ph., Cooper, D., Atlas, A., Jork, M., Fast Reroute
Techniques in RSVP\-TE, draft\-ietf\-mpls\-rsvp\-lsp\-fastreroute\-
00.txt, January 2002.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoIetfFrrMib(object):
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
        self.cmplsfrrconsttable = CiscoIetfFrrMib.Cmplsfrrconsttable()
        self.cmplsfrrconsttable.parent = self
        self.cmplsfrrfacroutedbtable = CiscoIetfFrrMib.Cmplsfrrfacroutedbtable()
        self.cmplsfrrfacroutedbtable.parent = self
        self.cmplsfrrlogtable = CiscoIetfFrrMib.Cmplsfrrlogtable()
        self.cmplsfrrlogtable.parent = self
        self.cmplsfrrscalars = CiscoIetfFrrMib.Cmplsfrrscalars()
        self.cmplsfrrscalars.parent = self


    class Cmplsfrrscalars(object):
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
        	**type**\:   :py:class:`CmplsfrrconstprotectionmethodEnum <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CiscoIetfFrrMib.Cmplsfrrscalars.CmplsfrrconstprotectionmethodEnum>`
        
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
            self.parent = None
            self.cmplsfrractprotectedifs = None
            self.cmplsfrractprotectedlsps = None
            self.cmplsfrractprotectedtuns = None
            self.cmplsfrrconfprotectingtuns = None
            self.cmplsfrrconstprotectionmethod = None
            self.cmplsfrrdetourincoming = None
            self.cmplsfrrdetouroriginating = None
            self.cmplsfrrdetouroutgoing = None
            self.cmplsfrrlogtablecurrentries = None
            self.cmplsfrrlogtablemaxentries = None
            self.cmplsfrrnotifmaxrate = None
            self.cmplsfrrnotifsenabled = None
            self.cmplsfrrnumofconfifs = None
            self.cmplsfrrswitchover = None

        class CmplsfrrconstprotectionmethodEnum(Enum):
            """
            CmplsfrrconstprotectionmethodEnum

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

            oneToOneBackup = 0

            facilityBackup = 1


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_FRR_MIB as meta
                return meta._meta_table['CiscoIetfFrrMib.Cmplsfrrscalars.CmplsfrrconstprotectionmethodEnum']


        @property
        def _common_path(self):

            return '/CISCO-IETF-FRR-MIB:CISCO-IETF-FRR-MIB/CISCO-IETF-FRR-MIB:cmplsFrrScalars'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cmplsfrractprotectedifs is not None:
                return True

            if self.cmplsfrractprotectedlsps is not None:
                return True

            if self.cmplsfrractprotectedtuns is not None:
                return True

            if self.cmplsfrrconfprotectingtuns is not None:
                return True

            if self.cmplsfrrconstprotectionmethod is not None:
                return True

            if self.cmplsfrrdetourincoming is not None:
                return True

            if self.cmplsfrrdetouroriginating is not None:
                return True

            if self.cmplsfrrdetouroutgoing is not None:
                return True

            if self.cmplsfrrlogtablecurrentries is not None:
                return True

            if self.cmplsfrrlogtablemaxentries is not None:
                return True

            if self.cmplsfrrnotifmaxrate is not None:
                return True

            if self.cmplsfrrnotifsenabled is not None:
                return True

            if self.cmplsfrrnumofconfifs is not None:
                return True

            if self.cmplsfrrswitchover is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_FRR_MIB as meta
            return meta._meta_table['CiscoIetfFrrMib.Cmplsfrrscalars']['meta_info']


    class Cmplsfrrconsttable(object):
        """
        This table shows detour setup constraints.
        
        .. attribute:: cmplsfrrconstentry
        
        	An entry in this table represents detour LSP or bypass tunnel  setup constraints for a tunnel instance to be protected by  detour LSPs or a tunnel. Agents must allow entries in this table  to be created only for tunnel instances that require fast\-reroute. Entries indexed with mplsFrrConstIfIndex set to 0 apply to all interfaces on this device for which the FRR feature can operate on
        	**type**\: list of    :py:class:`Cmplsfrrconstentry <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CiscoIetfFrrMib.Cmplsfrrconsttable.Cmplsfrrconstentry>`
        
        

        """

        _prefix = 'CISCO-IETF-FRR-MIB'
        _revision = '2008-04-29'

        def __init__(self):
            self.parent = None
            self.cmplsfrrconstentry = YList()
            self.cmplsfrrconstentry.parent = self
            self.cmplsfrrconstentry.name = 'cmplsfrrconstentry'


        class Cmplsfrrconstentry(object):
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
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: cmplsfrrconstsetupprio
            
            	Indicates the setup priority of detour LSP
            	**type**\:  int
            
            	**range:** 0..7
            
            

            """

            _prefix = 'CISCO-IETF-FRR-MIB'
            _revision = '2008-04-29'

            def __init__(self):
                self.parent = None
                self.cmplsfrrconstifindex = None
                self.cmplsfrrconsttunnelindex = None
                self.cmplsfrrconsttunnelinstance = None
                self.cmplsfrrconstbandwidth = None
                self.cmplsfrrconstexclallaffinity = None
                self.cmplsfrrconstholdingprio = None
                self.cmplsfrrconsthoplimit = None
                self.cmplsfrrconstinclallaffinity = None
                self.cmplsfrrconstinclanyaffinity = None
                self.cmplsfrrconstnumprotectedtunonif = None
                self.cmplsfrrconstnumprotectingtunonif = None
                self.cmplsfrrconstrowstatus = None
                self.cmplsfrrconstsetupprio = None

            @property
            def _common_path(self):
                if self.cmplsfrrconstifindex is None:
                    raise YPYModelError('Key property cmplsfrrconstifindex is None')
                if self.cmplsfrrconsttunnelindex is None:
                    raise YPYModelError('Key property cmplsfrrconsttunnelindex is None')
                if self.cmplsfrrconsttunnelinstance is None:
                    raise YPYModelError('Key property cmplsfrrconsttunnelinstance is None')

                return '/CISCO-IETF-FRR-MIB:CISCO-IETF-FRR-MIB/CISCO-IETF-FRR-MIB:cmplsFrrConstTable/CISCO-IETF-FRR-MIB:cmplsFrrConstEntry[CISCO-IETF-FRR-MIB:cmplsFrrConstIfIndex = ' + str(self.cmplsfrrconstifindex) + '][CISCO-IETF-FRR-MIB:cmplsFrrConstTunnelIndex = ' + str(self.cmplsfrrconsttunnelindex) + '][CISCO-IETF-FRR-MIB:cmplsFrrConstTunnelInstance = ' + str(self.cmplsfrrconsttunnelinstance) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cmplsfrrconstifindex is not None:
                    return True

                if self.cmplsfrrconsttunnelindex is not None:
                    return True

                if self.cmplsfrrconsttunnelinstance is not None:
                    return True

                if self.cmplsfrrconstbandwidth is not None:
                    return True

                if self.cmplsfrrconstexclallaffinity is not None:
                    return True

                if self.cmplsfrrconstholdingprio is not None:
                    return True

                if self.cmplsfrrconsthoplimit is not None:
                    return True

                if self.cmplsfrrconstinclallaffinity is not None:
                    return True

                if self.cmplsfrrconstinclanyaffinity is not None:
                    return True

                if self.cmplsfrrconstnumprotectedtunonif is not None:
                    return True

                if self.cmplsfrrconstnumprotectingtunonif is not None:
                    return True

                if self.cmplsfrrconstrowstatus is not None:
                    return True

                if self.cmplsfrrconstsetupprio is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_FRR_MIB as meta
                return meta._meta_table['CiscoIetfFrrMib.Cmplsfrrconsttable.Cmplsfrrconstentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-FRR-MIB:CISCO-IETF-FRR-MIB/CISCO-IETF-FRR-MIB:cmplsFrrConstTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cmplsfrrconstentry is not None:
                for child_ref in self.cmplsfrrconstentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_FRR_MIB as meta
            return meta._meta_table['CiscoIetfFrrMib.Cmplsfrrconsttable']['meta_info']


    class Cmplsfrrlogtable(object):
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
            self.parent = None
            self.cmplsfrrlogentry = YList()
            self.cmplsfrrlogentry.parent = self
            self.cmplsfrrlogentry.name = 'cmplsfrrlogentry'


        class Cmplsfrrlogentry(object):
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
            	**type**\:   :py:class:`CmplsfrrlogeventtypeEnum <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CiscoIetfFrrMib.Cmplsfrrlogtable.Cmplsfrrlogentry.CmplsfrrlogeventtypeEnum>`
            
            .. attribute:: cmplsfrrloginterface
            
            	This object indicates which interface was affected by this FRR event. This value may be set to 0 if mplsFrrConstProtectionMethod is set to oneToOneBackup(0)
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'CISCO-IETF-FRR-MIB'
            _revision = '2008-04-29'

            def __init__(self):
                self.parent = None
                self.cmplsfrrlogindex = None
                self.cmplsfrrlogeventduration = None
                self.cmplsfrrlogeventreasonstring = None
                self.cmplsfrrlogeventtime = None
                self.cmplsfrrlogeventtype = None
                self.cmplsfrrloginterface = None

            class CmplsfrrlogeventtypeEnum(Enum):
                """
                CmplsfrrlogeventtypeEnum

                This object describes what type of fast reroute event

                occured.

                .. data:: other = 1

                .. data:: protected = 2

                """

                other = 1

                protected = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_FRR_MIB as meta
                    return meta._meta_table['CiscoIetfFrrMib.Cmplsfrrlogtable.Cmplsfrrlogentry.CmplsfrrlogeventtypeEnum']


            @property
            def _common_path(self):
                if self.cmplsfrrlogindex is None:
                    raise YPYModelError('Key property cmplsfrrlogindex is None')

                return '/CISCO-IETF-FRR-MIB:CISCO-IETF-FRR-MIB/CISCO-IETF-FRR-MIB:cmplsFrrLogTable/CISCO-IETF-FRR-MIB:cmplsFrrLogEntry[CISCO-IETF-FRR-MIB:cmplsFrrLogIndex = ' + str(self.cmplsfrrlogindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cmplsfrrlogindex is not None:
                    return True

                if self.cmplsfrrlogeventduration is not None:
                    return True

                if self.cmplsfrrlogeventreasonstring is not None:
                    return True

                if self.cmplsfrrlogeventtime is not None:
                    return True

                if self.cmplsfrrlogeventtype is not None:
                    return True

                if self.cmplsfrrloginterface is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_FRR_MIB as meta
                return meta._meta_table['CiscoIetfFrrMib.Cmplsfrrlogtable.Cmplsfrrlogentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-FRR-MIB:CISCO-IETF-FRR-MIB/CISCO-IETF-FRR-MIB:cmplsFrrLogTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cmplsfrrlogentry is not None:
                for child_ref in self.cmplsfrrlogentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_FRR_MIB as meta
            return meta._meta_table['CiscoIetfFrrMib.Cmplsfrrlogtable']['meta_info']


    class Cmplsfrrfacroutedbtable(object):
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
            self.parent = None
            self.cmplsfrrfacroutedbentry = YList()
            self.cmplsfrrfacroutedbentry.parent = self
            self.cmplsfrrfacroutedbentry.name = 'cmplsfrrfacroutedbentry'


        class Cmplsfrrfacroutedbentry(object):
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
            	**type**\:   :py:class:`CmplsfrrfacrouteprotectedtunstatusEnum <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CiscoIetfFrrMib.Cmplsfrrfacroutedbtable.Cmplsfrrfacroutedbentry.CmplsfrrfacrouteprotectedtunstatusEnum>`
            
            .. attribute:: cmplsfrrfacrouteprotectingtunprotectiontype
            
            	Indicates type of the resource protection
            	**type**\:   :py:class:`CmplsfrrfacrouteprotectingtunprotectiontypeEnum <ydk.models.cisco_ios_xe.CISCO_IETF_FRR_MIB.CiscoIetfFrrMib.Cmplsfrrfacroutedbtable.Cmplsfrrfacroutedbentry.CmplsfrrfacrouteprotectingtunprotectiontypeEnum>`
            
            .. attribute:: cmplsfrrfacrouteprotectingtunresvbw
            
            	Specifies the amount of bandwidth in megabytes per second that is actually reserved by the backup tunnel for facility backup. This value is repeated here from the MPLS\- TE MIB because the tunnel entry will reveal the bandwidth reserved by the signaling protocol, which is typically 0 for backup tunnels so as to not over\-book bandwidth. However, internal reservations are typically made on the PLR, thus this value should be revealed here
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-FRR-MIB'
            _revision = '2008-04-29'

            def __init__(self):
                self.parent = None
                self.cmplsfrrfacrouteprotectedifindex = None
                self.cmplsfrrfacrouteprotectingtunindex = None
                self.cmplsfrrfacrouteprotectedtunindex = None
                self.cmplsfrrfacrouteprotectedtuninstance = None
                self.cmplsfrrfacrouteprotectedtuningresslsrid = None
                self.cmplsfrrfacrouteprotectedtunegresslsrid = None
                self.cmplsfrrfacrouteprotectedtunstatus = None
                self.cmplsfrrfacrouteprotectingtunprotectiontype = None
                self.cmplsfrrfacrouteprotectingtunresvbw = None

            class CmplsfrrfacrouteprotectedtunstatusEnum(Enum):
                """
                CmplsfrrfacrouteprotectedtunstatusEnum

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

                active = 1

                ready = 2

                partial = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_FRR_MIB as meta
                    return meta._meta_table['CiscoIetfFrrMib.Cmplsfrrfacroutedbtable.Cmplsfrrfacroutedbentry.CmplsfrrfacrouteprotectedtunstatusEnum']


            class CmplsfrrfacrouteprotectingtunprotectiontypeEnum(Enum):
                """
                CmplsfrrfacrouteprotectingtunprotectiontypeEnum

                Indicates type of the resource protection.

                .. data:: linkProtection = 0

                .. data:: nodeProtection = 1

                """

                linkProtection = 0

                nodeProtection = 1


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_FRR_MIB as meta
                    return meta._meta_table['CiscoIetfFrrMib.Cmplsfrrfacroutedbtable.Cmplsfrrfacroutedbentry.CmplsfrrfacrouteprotectingtunprotectiontypeEnum']


            @property
            def _common_path(self):
                if self.cmplsfrrfacrouteprotectedifindex is None:
                    raise YPYModelError('Key property cmplsfrrfacrouteprotectedifindex is None')
                if self.cmplsfrrfacrouteprotectingtunindex is None:
                    raise YPYModelError('Key property cmplsfrrfacrouteprotectingtunindex is None')
                if self.cmplsfrrfacrouteprotectedtunindex is None:
                    raise YPYModelError('Key property cmplsfrrfacrouteprotectedtunindex is None')
                if self.cmplsfrrfacrouteprotectedtuninstance is None:
                    raise YPYModelError('Key property cmplsfrrfacrouteprotectedtuninstance is None')
                if self.cmplsfrrfacrouteprotectedtuningresslsrid is None:
                    raise YPYModelError('Key property cmplsfrrfacrouteprotectedtuningresslsrid is None')
                if self.cmplsfrrfacrouteprotectedtunegresslsrid is None:
                    raise YPYModelError('Key property cmplsfrrfacrouteprotectedtunegresslsrid is None')

                return '/CISCO-IETF-FRR-MIB:CISCO-IETF-FRR-MIB/CISCO-IETF-FRR-MIB:cmplsFrrFacRouteDBTable/CISCO-IETF-FRR-MIB:cmplsFrrFacRouteDBEntry[CISCO-IETF-FRR-MIB:cmplsFrrFacRouteProtectedIfIndex = ' + str(self.cmplsfrrfacrouteprotectedifindex) + '][CISCO-IETF-FRR-MIB:cmplsFrrFacRouteProtectingTunIndex = ' + str(self.cmplsfrrfacrouteprotectingtunindex) + '][CISCO-IETF-FRR-MIB:cmplsFrrFacRouteProtectedTunIndex = ' + str(self.cmplsfrrfacrouteprotectedtunindex) + '][CISCO-IETF-FRR-MIB:cmplsFrrFacRouteProtectedTunInstance = ' + str(self.cmplsfrrfacrouteprotectedtuninstance) + '][CISCO-IETF-FRR-MIB:cmplsFrrFacRouteProtectedTunIngressLSRId = ' + str(self.cmplsfrrfacrouteprotectedtuningresslsrid) + '][CISCO-IETF-FRR-MIB:cmplsFrrFacRouteProtectedTunEgressLSRId = ' + str(self.cmplsfrrfacrouteprotectedtunegresslsrid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cmplsfrrfacrouteprotectedifindex is not None:
                    return True

                if self.cmplsfrrfacrouteprotectingtunindex is not None:
                    return True

                if self.cmplsfrrfacrouteprotectedtunindex is not None:
                    return True

                if self.cmplsfrrfacrouteprotectedtuninstance is not None:
                    return True

                if self.cmplsfrrfacrouteprotectedtuningresslsrid is not None:
                    return True

                if self.cmplsfrrfacrouteprotectedtunegresslsrid is not None:
                    return True

                if self.cmplsfrrfacrouteprotectedtunstatus is not None:
                    return True

                if self.cmplsfrrfacrouteprotectingtunprotectiontype is not None:
                    return True

                if self.cmplsfrrfacrouteprotectingtunresvbw is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_FRR_MIB as meta
                return meta._meta_table['CiscoIetfFrrMib.Cmplsfrrfacroutedbtable.Cmplsfrrfacroutedbentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-FRR-MIB:CISCO-IETF-FRR-MIB/CISCO-IETF-FRR-MIB:cmplsFrrFacRouteDBTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cmplsfrrfacroutedbentry is not None:
                for child_ref in self.cmplsfrrfacroutedbentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_FRR_MIB as meta
            return meta._meta_table['CiscoIetfFrrMib.Cmplsfrrfacroutedbtable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IETF-FRR-MIB:CISCO-IETF-FRR-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cmplsfrrconsttable is not None and self.cmplsfrrconsttable._has_data():
            return True

        if self.cmplsfrrfacroutedbtable is not None and self.cmplsfrrfacroutedbtable._has_data():
            return True

        if self.cmplsfrrlogtable is not None and self.cmplsfrrlogtable._has_data():
            return True

        if self.cmplsfrrscalars is not None and self.cmplsfrrscalars._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_FRR_MIB as meta
        return meta._meta_table['CiscoIetfFrrMib']['meta_info']



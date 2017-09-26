""" CISCO_ENVMON_MIB 

The MIB module to describe the status of the Environmental
Monitor on those devices which support one.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CiscoEnvMonState(Enum):
    """
    CiscoEnvMonState

    Represents the state of a device being monitored.

    Valid values are\:

    normal(1)\:         the environment is good, such as low

                       temperature.

    warning(2)\:        the environment is bad, such as temperature

                       above normal operation range but not too

                       high.

    critical(3)\:       the environment is very bad, such as

                       temperature much higher than normal

                       operation limit.

    shutdown(4)\:       the environment is the worst, the system

                       should be shutdown immediately.

    notPresent(5)\:     the environmental monitor is not present,

                       such as temperature sensors do not exist.

    notFunctioning(6)\: the environmental monitor does not 

                       function properly, such as a temperature

                       sensor generates a abnormal data like

                       1000 C.

    .. data:: normal = 1

    .. data:: warning = 2

    .. data:: critical = 3

    .. data:: shutdown = 4

    .. data:: notPresent = 5

    .. data:: notFunctioning = 6

    """

    normal = Enum.YLeaf(1, "normal")

    warning = Enum.YLeaf(2, "warning")

    critical = Enum.YLeaf(3, "critical")

    shutdown = Enum.YLeaf(4, "shutdown")

    notPresent = Enum.YLeaf(5, "notPresent")

    notFunctioning = Enum.YLeaf(6, "notFunctioning")



class CISCOENVMONMIB(Entity):
    """
    
    
    .. attribute:: ciscoenvmonfanstatustable
    
    	The table of fan status maintained by the environmental monitor
    	**type**\:   :py:class:`Ciscoenvmonfanstatustable <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.Ciscoenvmonfanstatustable>`
    
    .. attribute:: ciscoenvmonmibnotificationenables
    
    	
    	**type**\:   :py:class:`Ciscoenvmonmibnotificationenables <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.Ciscoenvmonmibnotificationenables>`
    
    .. attribute:: ciscoenvmonobjects
    
    	
    	**type**\:   :py:class:`Ciscoenvmonobjects <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.Ciscoenvmonobjects>`
    
    .. attribute:: ciscoenvmonsupplystatustable
    
    	The table of power supply status maintained by the environmental monitor card
    	**type**\:   :py:class:`Ciscoenvmonsupplystatustable <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.Ciscoenvmonsupplystatustable>`
    
    .. attribute:: ciscoenvmontemperaturestatustable
    
    	The table of ambient temperature status maintained by the environmental monitor
    	**type**\:   :py:class:`Ciscoenvmontemperaturestatustable <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.Ciscoenvmontemperaturestatustable>`
    
    .. attribute:: ciscoenvmonvoltagestatustable
    
    	The table of voltage status maintained by the environmental monitor
    	**type**\:   :py:class:`Ciscoenvmonvoltagestatustable <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.Ciscoenvmonvoltagestatustable>`
    
    

    """

    _prefix = 'CISCO-ENVMON-MIB'
    _revision = '2003-12-01'

    def __init__(self):
        super(CISCOENVMONMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-ENVMON-MIB"
        self.yang_parent_name = "CISCO-ENVMON-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"ciscoEnvMonFanStatusTable" : ("ciscoenvmonfanstatustable", CISCOENVMONMIB.Ciscoenvmonfanstatustable), "ciscoEnvMonMIBNotificationEnables" : ("ciscoenvmonmibnotificationenables", CISCOENVMONMIB.Ciscoenvmonmibnotificationenables), "ciscoEnvMonObjects" : ("ciscoenvmonobjects", CISCOENVMONMIB.Ciscoenvmonobjects), "ciscoEnvMonSupplyStatusTable" : ("ciscoenvmonsupplystatustable", CISCOENVMONMIB.Ciscoenvmonsupplystatustable), "ciscoEnvMonTemperatureStatusTable" : ("ciscoenvmontemperaturestatustable", CISCOENVMONMIB.Ciscoenvmontemperaturestatustable), "ciscoEnvMonVoltageStatusTable" : ("ciscoenvmonvoltagestatustable", CISCOENVMONMIB.Ciscoenvmonvoltagestatustable)}
        self._child_list_classes = {}

        self.ciscoenvmonfanstatustable = CISCOENVMONMIB.Ciscoenvmonfanstatustable()
        self.ciscoenvmonfanstatustable.parent = self
        self._children_name_map["ciscoenvmonfanstatustable"] = "ciscoEnvMonFanStatusTable"
        self._children_yang_names.add("ciscoEnvMonFanStatusTable")

        self.ciscoenvmonmibnotificationenables = CISCOENVMONMIB.Ciscoenvmonmibnotificationenables()
        self.ciscoenvmonmibnotificationenables.parent = self
        self._children_name_map["ciscoenvmonmibnotificationenables"] = "ciscoEnvMonMIBNotificationEnables"
        self._children_yang_names.add("ciscoEnvMonMIBNotificationEnables")

        self.ciscoenvmonobjects = CISCOENVMONMIB.Ciscoenvmonobjects()
        self.ciscoenvmonobjects.parent = self
        self._children_name_map["ciscoenvmonobjects"] = "ciscoEnvMonObjects"
        self._children_yang_names.add("ciscoEnvMonObjects")

        self.ciscoenvmonsupplystatustable = CISCOENVMONMIB.Ciscoenvmonsupplystatustable()
        self.ciscoenvmonsupplystatustable.parent = self
        self._children_name_map["ciscoenvmonsupplystatustable"] = "ciscoEnvMonSupplyStatusTable"
        self._children_yang_names.add("ciscoEnvMonSupplyStatusTable")

        self.ciscoenvmontemperaturestatustable = CISCOENVMONMIB.Ciscoenvmontemperaturestatustable()
        self.ciscoenvmontemperaturestatustable.parent = self
        self._children_name_map["ciscoenvmontemperaturestatustable"] = "ciscoEnvMonTemperatureStatusTable"
        self._children_yang_names.add("ciscoEnvMonTemperatureStatusTable")

        self.ciscoenvmonvoltagestatustable = CISCOENVMONMIB.Ciscoenvmonvoltagestatustable()
        self.ciscoenvmonvoltagestatustable.parent = self
        self._children_name_map["ciscoenvmonvoltagestatustable"] = "ciscoEnvMonVoltageStatusTable"
        self._children_yang_names.add("ciscoEnvMonVoltageStatusTable")
        self._segment_path = lambda: "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB"


    class Ciscoenvmonfanstatustable(Entity):
        """
        The table of fan status maintained by the environmental
        monitor.
        
        .. attribute:: ciscoenvmonfanstatusentry
        
        	An entry in the fan status table, representing the status of the associated fan maintained by the environmental monitor
        	**type**\: list of    :py:class:`Ciscoenvmonfanstatusentry <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.Ciscoenvmonfanstatustable.Ciscoenvmonfanstatusentry>`
        
        

        """

        _prefix = 'CISCO-ENVMON-MIB'
        _revision = '2003-12-01'

        def __init__(self):
            super(CISCOENVMONMIB.Ciscoenvmonfanstatustable, self).__init__()

            self.yang_name = "ciscoEnvMonFanStatusTable"
            self.yang_parent_name = "CISCO-ENVMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"ciscoEnvMonFanStatusEntry" : ("ciscoenvmonfanstatusentry", CISCOENVMONMIB.Ciscoenvmonfanstatustable.Ciscoenvmonfanstatusentry)}

            self.ciscoenvmonfanstatusentry = YList(self)
            self._segment_path = lambda: "ciscoEnvMonFanStatusTable"
            self._absolute_path = lambda: "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENVMONMIB.Ciscoenvmonfanstatustable, [], name, value)


        class Ciscoenvmonfanstatusentry(Entity):
            """
            An entry in the fan status table, representing the status of
            the associated fan maintained by the environmental monitor.
            
            .. attribute:: ciscoenvmonfanstatusindex  <key>
            
            	Unique index for the fan being instrumented. This index is for SNMP purposes only, and has no intrinsic meaning
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciscoenvmonfanstate
            
            	The current state of the fan being instrumented
            	**type**\:   :py:class:`CiscoEnvMonState <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoEnvMonState>`
            
            .. attribute:: ciscoenvmonfanstatusdescr
            
            	Textual description of the fan being instrumented. This description is a short textual label, suitable as a human\-sensible identification for the rest of the information in the entry
            	**type**\:  str
            
            	**length:** 0..32
            
            

            """

            _prefix = 'CISCO-ENVMON-MIB'
            _revision = '2003-12-01'

            def __init__(self):
                super(CISCOENVMONMIB.Ciscoenvmonfanstatustable.Ciscoenvmonfanstatusentry, self).__init__()

                self.yang_name = "ciscoEnvMonFanStatusEntry"
                self.yang_parent_name = "ciscoEnvMonFanStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ciscoenvmonfanstatusindex = YLeaf(YType.int32, "ciscoEnvMonFanStatusIndex")

                self.ciscoenvmonfanstate = YLeaf(YType.enumeration, "ciscoEnvMonFanState")

                self.ciscoenvmonfanstatusdescr = YLeaf(YType.str, "ciscoEnvMonFanStatusDescr")
                self._segment_path = lambda: "ciscoEnvMonFanStatusEntry" + "[ciscoEnvMonFanStatusIndex='" + self.ciscoenvmonfanstatusindex.get() + "']"
                self._absolute_path = lambda: "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/ciscoEnvMonFanStatusTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENVMONMIB.Ciscoenvmonfanstatustable.Ciscoenvmonfanstatusentry, ['ciscoenvmonfanstatusindex', 'ciscoenvmonfanstate', 'ciscoenvmonfanstatusdescr'], name, value)


    class Ciscoenvmonmibnotificationenables(Entity):
        """
        
        
        .. attribute:: ciscoenvmonenablefannotification
        
        	This variable  indicates  whether  the  system produces the ciscoEnvMonFanNotification. A false value prevents fan notifications  from being sent by  this entity. This object is  deprecated in favour of  ciscoEnvMonEnableStatChangeNotif
        	**type**\:  bool
        
        	**status**\: deprecated
        
        .. attribute:: ciscoenvmonenableredundantsupplynotification
        
        	This variable  indicates  whether  the  system produces the ciscoEnvMonRedundantSupplyNotification.  A false value prevents redundant supply notifications from being generated by this system. This object is deprecated in favour of  ciscoEnvMonEnableStatChangeNotif
        	**type**\:  bool
        
        	**status**\: deprecated
        
        .. attribute:: ciscoenvmonenableshutdownnotification
        
        	This variable  indicates  whether  the  system produces the ciscoEnvMonShutdownNotification.  A false  value will prevent shutdown notifications  from being generated by this system
        	**type**\:  bool
        
        .. attribute:: ciscoenvmonenablestatchangenotif
        
        	This variable indicates whether the system produces the ciscoEnvMonVoltStatusChangeNotif, ciscoEnvMonTempStatusChangeNotif,  ciscoEnvMonFanStatusChangeNotif and   ciscoEnvMonSuppStatusChangeNotif. A false value will  prevent these notifications from being generated by  this system
        	**type**\:  bool
        
        .. attribute:: ciscoenvmonenabletemperaturenotification
        
        	This variable  indicates  whether  the  system produces the ciscoEnvMonTemperatureNotification. A false value prevents temperature notifications  from being sent by  this entity. This object is  deprecated in favour of  ciscoEnvMonEnableStatChangeNotif
        	**type**\:  bool
        
        	**status**\: deprecated
        
        .. attribute:: ciscoenvmonenablevoltagenotification
        
        	This variable  indicates  whether  the  system produces the ciscoEnvMonVoltageNotification. A false  value will prevent voltage notifications from being  generated by this system. This object is deprecated in favour of ciscoEnvMonEnableStatChangeNotif
        	**type**\:  bool
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'CISCO-ENVMON-MIB'
        _revision = '2003-12-01'

        def __init__(self):
            super(CISCOENVMONMIB.Ciscoenvmonmibnotificationenables, self).__init__()

            self.yang_name = "ciscoEnvMonMIBNotificationEnables"
            self.yang_parent_name = "CISCO-ENVMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.ciscoenvmonenablefannotification = YLeaf(YType.boolean, "ciscoEnvMonEnableFanNotification")

            self.ciscoenvmonenableredundantsupplynotification = YLeaf(YType.boolean, "ciscoEnvMonEnableRedundantSupplyNotification")

            self.ciscoenvmonenableshutdownnotification = YLeaf(YType.boolean, "ciscoEnvMonEnableShutdownNotification")

            self.ciscoenvmonenablestatchangenotif = YLeaf(YType.boolean, "ciscoEnvMonEnableStatChangeNotif")

            self.ciscoenvmonenabletemperaturenotification = YLeaf(YType.boolean, "ciscoEnvMonEnableTemperatureNotification")

            self.ciscoenvmonenablevoltagenotification = YLeaf(YType.boolean, "ciscoEnvMonEnableVoltageNotification")
            self._segment_path = lambda: "ciscoEnvMonMIBNotificationEnables"
            self._absolute_path = lambda: "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENVMONMIB.Ciscoenvmonmibnotificationenables, ['ciscoenvmonenablefannotification', 'ciscoenvmonenableredundantsupplynotification', 'ciscoenvmonenableshutdownnotification', 'ciscoenvmonenablestatchangenotif', 'ciscoenvmonenabletemperaturenotification', 'ciscoenvmonenablevoltagenotification'], name, value)


    class Ciscoenvmonobjects(Entity):
        """
        
        
        .. attribute:: ciscoenvmonalarmcontacts
        
        	Each bit is set to reflect the respective alarm being set.  The bit will be cleared when the respective alarm is cleared
        	**type**\:   :py:class:`Ciscoenvmonalarmcontacts <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.Ciscoenvmonobjects.Ciscoenvmonalarmcontacts>`
        
        .. attribute:: ciscoenvmonpresent
        
        	The type of environmental monitor located in the chassis. An oldAgs environmental monitor card is identical to an ags environmental card except that it is not capable of supplying data, and hence no instance of the remaining objects in this MIB will be returned in response to an SNMP query.  Note that only a firmware upgrade is required to convert an oldAgs into an ags card
        	**type**\:   :py:class:`Ciscoenvmonpresent <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.Ciscoenvmonobjects.Ciscoenvmonpresent>`
        
        

        """

        _prefix = 'CISCO-ENVMON-MIB'
        _revision = '2003-12-01'

        def __init__(self):
            super(CISCOENVMONMIB.Ciscoenvmonobjects, self).__init__()

            self.yang_name = "ciscoEnvMonObjects"
            self.yang_parent_name = "CISCO-ENVMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.ciscoenvmonalarmcontacts = YLeaf(YType.bits, "ciscoEnvMonAlarmContacts")

            self.ciscoenvmonpresent = YLeaf(YType.enumeration, "ciscoEnvMonPresent")
            self._segment_path = lambda: "ciscoEnvMonObjects"
            self._absolute_path = lambda: "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENVMONMIB.Ciscoenvmonobjects, ['ciscoenvmonalarmcontacts', 'ciscoenvmonpresent'], name, value)

        class Ciscoenvmonpresent(Enum):
            """
            Ciscoenvmonpresent

            The type of environmental monitor located in the chassis.

            An oldAgs environmental monitor card is identical to an ags

            environmental card except that it is not capable of supplying

            data, and hence no instance of the remaining objects in this

            MIB will be returned in response to an SNMP query.  Note that

            only a firmware upgrade is required to convert an oldAgs into

            an ags card.

            .. data:: oldAgs = 1

            .. data:: ags = 2

            .. data:: c7000 = 3

            .. data:: ci = 4

            .. data:: cAccessMon = 6

            .. data:: cat6000 = 7

            .. data:: ubr7200 = 8

            .. data:: cat4000 = 9

            .. data:: c10000 = 10

            .. data:: osr7600 = 11

            .. data:: c7600 = 12

            .. data:: c37xx = 13

            .. data:: other = 14

            """

            oldAgs = Enum.YLeaf(1, "oldAgs")

            ags = Enum.YLeaf(2, "ags")

            c7000 = Enum.YLeaf(3, "c7000")

            ci = Enum.YLeaf(4, "ci")

            cAccessMon = Enum.YLeaf(6, "cAccessMon")

            cat6000 = Enum.YLeaf(7, "cat6000")

            ubr7200 = Enum.YLeaf(8, "ubr7200")

            cat4000 = Enum.YLeaf(9, "cat4000")

            c10000 = Enum.YLeaf(10, "c10000")

            osr7600 = Enum.YLeaf(11, "osr7600")

            c7600 = Enum.YLeaf(12, "c7600")

            c37xx = Enum.YLeaf(13, "c37xx")

            other = Enum.YLeaf(14, "other")



    class Ciscoenvmonsupplystatustable(Entity):
        """
        The table of power supply status maintained by the
        environmental monitor card.
        
        .. attribute:: ciscoenvmonsupplystatusentry
        
        	An entry in the power supply status table, representing the status of the associated power supply maintained by the environmental monitor card
        	**type**\: list of    :py:class:`Ciscoenvmonsupplystatusentry <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.Ciscoenvmonsupplystatustable.Ciscoenvmonsupplystatusentry>`
        
        

        """

        _prefix = 'CISCO-ENVMON-MIB'
        _revision = '2003-12-01'

        def __init__(self):
            super(CISCOENVMONMIB.Ciscoenvmonsupplystatustable, self).__init__()

            self.yang_name = "ciscoEnvMonSupplyStatusTable"
            self.yang_parent_name = "CISCO-ENVMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"ciscoEnvMonSupplyStatusEntry" : ("ciscoenvmonsupplystatusentry", CISCOENVMONMIB.Ciscoenvmonsupplystatustable.Ciscoenvmonsupplystatusentry)}

            self.ciscoenvmonsupplystatusentry = YList(self)
            self._segment_path = lambda: "ciscoEnvMonSupplyStatusTable"
            self._absolute_path = lambda: "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENVMONMIB.Ciscoenvmonsupplystatustable, [], name, value)


        class Ciscoenvmonsupplystatusentry(Entity):
            """
            An entry in the power supply status table, representing the
            status of the associated power supply maintained by the
            environmental monitor card.
            
            .. attribute:: ciscoenvmonsupplystatusindex  <key>
            
            	Unique index for the power supply being instrumented. This index is for SNMP purposes only, and has no intrinsic meaning
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciscoenvmonsupplysource
            
            	The power supply source. unknown \- Power supply source unknown ac      \- AC power supply dc      \- DC power supply externalPowerSupply \- External power supply internalRedundant \- Internal redundant power supply 
            	**type**\:   :py:class:`Ciscoenvmonsupplysource <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.Ciscoenvmonsupplystatustable.Ciscoenvmonsupplystatusentry.Ciscoenvmonsupplysource>`
            
            .. attribute:: ciscoenvmonsupplystate
            
            	The current state of the power supply being instrumented
            	**type**\:   :py:class:`CiscoEnvMonState <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoEnvMonState>`
            
            .. attribute:: ciscoenvmonsupplystatusdescr
            
            	Textual description of the power supply being instrumented. This description is a short textual label, suitable as a human\-sensible identification for the rest of the information in the entry
            	**type**\:  str
            
            	**length:** 0..64
            
            

            """

            _prefix = 'CISCO-ENVMON-MIB'
            _revision = '2003-12-01'

            def __init__(self):
                super(CISCOENVMONMIB.Ciscoenvmonsupplystatustable.Ciscoenvmonsupplystatusentry, self).__init__()

                self.yang_name = "ciscoEnvMonSupplyStatusEntry"
                self.yang_parent_name = "ciscoEnvMonSupplyStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ciscoenvmonsupplystatusindex = YLeaf(YType.int32, "ciscoEnvMonSupplyStatusIndex")

                self.ciscoenvmonsupplysource = YLeaf(YType.enumeration, "ciscoEnvMonSupplySource")

                self.ciscoenvmonsupplystate = YLeaf(YType.enumeration, "ciscoEnvMonSupplyState")

                self.ciscoenvmonsupplystatusdescr = YLeaf(YType.str, "ciscoEnvMonSupplyStatusDescr")
                self._segment_path = lambda: "ciscoEnvMonSupplyStatusEntry" + "[ciscoEnvMonSupplyStatusIndex='" + self.ciscoenvmonsupplystatusindex.get() + "']"
                self._absolute_path = lambda: "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/ciscoEnvMonSupplyStatusTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENVMONMIB.Ciscoenvmonsupplystatustable.Ciscoenvmonsupplystatusentry, ['ciscoenvmonsupplystatusindex', 'ciscoenvmonsupplysource', 'ciscoenvmonsupplystate', 'ciscoenvmonsupplystatusdescr'], name, value)

            class Ciscoenvmonsupplysource(Enum):
                """
                Ciscoenvmonsupplysource

                The power supply source.

                unknown \- Power supply source unknown

                ac      \- AC power supply

                dc      \- DC power supply

                externalPowerSupply \- External power supply

                internalRedundant \- Internal redundant power supply 

                .. data:: unknown = 1

                .. data:: ac = 2

                .. data:: dc = 3

                .. data:: externalPowerSupply = 4

                .. data:: internalRedundant = 5

                """

                unknown = Enum.YLeaf(1, "unknown")

                ac = Enum.YLeaf(2, "ac")

                dc = Enum.YLeaf(3, "dc")

                externalPowerSupply = Enum.YLeaf(4, "externalPowerSupply")

                internalRedundant = Enum.YLeaf(5, "internalRedundant")



    class Ciscoenvmontemperaturestatustable(Entity):
        """
        The table of ambient temperature status maintained by the
        environmental monitor.
        
        .. attribute:: ciscoenvmontemperaturestatusentry
        
        	An entry in the ambient temperature status table, representing the status of the associated testpoint maintained by the environmental monitor
        	**type**\: list of    :py:class:`Ciscoenvmontemperaturestatusentry <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.Ciscoenvmontemperaturestatustable.Ciscoenvmontemperaturestatusentry>`
        
        

        """

        _prefix = 'CISCO-ENVMON-MIB'
        _revision = '2003-12-01'

        def __init__(self):
            super(CISCOENVMONMIB.Ciscoenvmontemperaturestatustable, self).__init__()

            self.yang_name = "ciscoEnvMonTemperatureStatusTable"
            self.yang_parent_name = "CISCO-ENVMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"ciscoEnvMonTemperatureStatusEntry" : ("ciscoenvmontemperaturestatusentry", CISCOENVMONMIB.Ciscoenvmontemperaturestatustable.Ciscoenvmontemperaturestatusentry)}

            self.ciscoenvmontemperaturestatusentry = YList(self)
            self._segment_path = lambda: "ciscoEnvMonTemperatureStatusTable"
            self._absolute_path = lambda: "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENVMONMIB.Ciscoenvmontemperaturestatustable, [], name, value)


        class Ciscoenvmontemperaturestatusentry(Entity):
            """
            An entry in the ambient temperature status table, representing
            the status of the associated testpoint maintained by the
            environmental monitor.
            
            .. attribute:: ciscoenvmontemperaturestatusindex  <key>
            
            	Unique index for the testpoint being instrumented. This index is for SNMP purposes only, and has no intrinsic meaning
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciscoenvmontemperaturelastshutdown
            
            	The value of the associated instance of the object ciscoEnvMonTemperatureStatusValue at the time an emergency shutdown of the managed device was last initiated.  This value is stored in non\-volatile RAM and hence is able to survive the shutdown
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: degrees Celsius
            
            .. attribute:: ciscoenvmontemperaturestate
            
            	The current state of the testpoint being instrumented
            	**type**\:   :py:class:`CiscoEnvMonState <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoEnvMonState>`
            
            .. attribute:: ciscoenvmontemperaturestatusdescr
            
            	Textual description of the testpoint being instrumented. This description is a short textual label, suitable as a human\-sensible identification for the rest of the information in the entry
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: ciscoenvmontemperaturestatusvalue
            
            	The current measurement of the testpoint being instrumented
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: degrees Celsius
            
            .. attribute:: ciscoenvmontemperaturethreshold
            
            	The highest value that the associated instance of the object ciscoEnvMonTemperatureStatusValue may obtain before an emergency shutdown of the managed device is initiated
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: degrees Celsius
            
            

            """

            _prefix = 'CISCO-ENVMON-MIB'
            _revision = '2003-12-01'

            def __init__(self):
                super(CISCOENVMONMIB.Ciscoenvmontemperaturestatustable.Ciscoenvmontemperaturestatusentry, self).__init__()

                self.yang_name = "ciscoEnvMonTemperatureStatusEntry"
                self.yang_parent_name = "ciscoEnvMonTemperatureStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ciscoenvmontemperaturestatusindex = YLeaf(YType.int32, "ciscoEnvMonTemperatureStatusIndex")

                self.ciscoenvmontemperaturelastshutdown = YLeaf(YType.int32, "ciscoEnvMonTemperatureLastShutdown")

                self.ciscoenvmontemperaturestate = YLeaf(YType.enumeration, "ciscoEnvMonTemperatureState")

                self.ciscoenvmontemperaturestatusdescr = YLeaf(YType.str, "ciscoEnvMonTemperatureStatusDescr")

                self.ciscoenvmontemperaturestatusvalue = YLeaf(YType.uint32, "ciscoEnvMonTemperatureStatusValue")

                self.ciscoenvmontemperaturethreshold = YLeaf(YType.int32, "ciscoEnvMonTemperatureThreshold")
                self._segment_path = lambda: "ciscoEnvMonTemperatureStatusEntry" + "[ciscoEnvMonTemperatureStatusIndex='" + self.ciscoenvmontemperaturestatusindex.get() + "']"
                self._absolute_path = lambda: "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/ciscoEnvMonTemperatureStatusTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENVMONMIB.Ciscoenvmontemperaturestatustable.Ciscoenvmontemperaturestatusentry, ['ciscoenvmontemperaturestatusindex', 'ciscoenvmontemperaturelastshutdown', 'ciscoenvmontemperaturestate', 'ciscoenvmontemperaturestatusdescr', 'ciscoenvmontemperaturestatusvalue', 'ciscoenvmontemperaturethreshold'], name, value)


    class Ciscoenvmonvoltagestatustable(Entity):
        """
        The table of voltage status maintained by the environmental
        monitor.
        
        .. attribute:: ciscoenvmonvoltagestatusentry
        
        	An entry in the voltage status table, representing the status of the associated testpoint maintained by the environmental monitor
        	**type**\: list of    :py:class:`Ciscoenvmonvoltagestatusentry <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.Ciscoenvmonvoltagestatustable.Ciscoenvmonvoltagestatusentry>`
        
        

        """

        _prefix = 'CISCO-ENVMON-MIB'
        _revision = '2003-12-01'

        def __init__(self):
            super(CISCOENVMONMIB.Ciscoenvmonvoltagestatustable, self).__init__()

            self.yang_name = "ciscoEnvMonVoltageStatusTable"
            self.yang_parent_name = "CISCO-ENVMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"ciscoEnvMonVoltageStatusEntry" : ("ciscoenvmonvoltagestatusentry", CISCOENVMONMIB.Ciscoenvmonvoltagestatustable.Ciscoenvmonvoltagestatusentry)}

            self.ciscoenvmonvoltagestatusentry = YList(self)
            self._segment_path = lambda: "ciscoEnvMonVoltageStatusTable"
            self._absolute_path = lambda: "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENVMONMIB.Ciscoenvmonvoltagestatustable, [], name, value)


        class Ciscoenvmonvoltagestatusentry(Entity):
            """
            An entry in the voltage status table, representing the status
            of the associated testpoint maintained by the environmental
            monitor.
            
            .. attribute:: ciscoenvmonvoltagestatusindex  <key>
            
            	Unique index for the testpoint being instrumented. This index is for SNMP purposes only, and has no intrinsic meaning
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciscoenvmonvoltagelastshutdown
            
            	The value of the associated instance of the object ciscoEnvMonVoltageStatusValue at the time an emergency shutdown of the managed device was last initiated.  This value is stored in non\-volatile RAM and hence is able to survive the shutdown
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: millivolts
            
            .. attribute:: ciscoenvmonvoltagestate
            
            	The current state of the testpoint being instrumented
            	**type**\:   :py:class:`CiscoEnvMonState <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoEnvMonState>`
            
            .. attribute:: ciscoenvmonvoltagestatusdescr
            
            	Textual description of the testpoint being instrumented. This description is a short textual label, suitable as a human\-sensible identification for the rest of the information in the entry
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: ciscoenvmonvoltagestatusvalue
            
            	The current measurement of the testpoint being instrumented
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: millivolts
            
            .. attribute:: ciscoenvmonvoltagethresholdhigh
            
            	The highest value that the associated instance of the object ciscoEnvMonVoltageStatusValue may obtain before an emergency shutdown of the managed device is initiated
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: millivolts
            
            .. attribute:: ciscoenvmonvoltagethresholdlow
            
            	The lowest value that the associated instance of the object ciscoEnvMonVoltageStatusValue may obtain before an emergency shutdown of the managed device is initiated
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: millivolts
            
            

            """

            _prefix = 'CISCO-ENVMON-MIB'
            _revision = '2003-12-01'

            def __init__(self):
                super(CISCOENVMONMIB.Ciscoenvmonvoltagestatustable.Ciscoenvmonvoltagestatusentry, self).__init__()

                self.yang_name = "ciscoEnvMonVoltageStatusEntry"
                self.yang_parent_name = "ciscoEnvMonVoltageStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ciscoenvmonvoltagestatusindex = YLeaf(YType.int32, "ciscoEnvMonVoltageStatusIndex")

                self.ciscoenvmonvoltagelastshutdown = YLeaf(YType.int32, "ciscoEnvMonVoltageLastShutdown")

                self.ciscoenvmonvoltagestate = YLeaf(YType.enumeration, "ciscoEnvMonVoltageState")

                self.ciscoenvmonvoltagestatusdescr = YLeaf(YType.str, "ciscoEnvMonVoltageStatusDescr")

                self.ciscoenvmonvoltagestatusvalue = YLeaf(YType.int32, "ciscoEnvMonVoltageStatusValue")

                self.ciscoenvmonvoltagethresholdhigh = YLeaf(YType.int32, "ciscoEnvMonVoltageThresholdHigh")

                self.ciscoenvmonvoltagethresholdlow = YLeaf(YType.int32, "ciscoEnvMonVoltageThresholdLow")
                self._segment_path = lambda: "ciscoEnvMonVoltageStatusEntry" + "[ciscoEnvMonVoltageStatusIndex='" + self.ciscoenvmonvoltagestatusindex.get() + "']"
                self._absolute_path = lambda: "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/ciscoEnvMonVoltageStatusTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENVMONMIB.Ciscoenvmonvoltagestatustable.Ciscoenvmonvoltagestatusentry, ['ciscoenvmonvoltagestatusindex', 'ciscoenvmonvoltagelastshutdown', 'ciscoenvmonvoltagestate', 'ciscoenvmonvoltagestatusdescr', 'ciscoenvmonvoltagestatusvalue', 'ciscoenvmonvoltagethresholdhigh', 'ciscoenvmonvoltagethresholdlow'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOENVMONMIB()
        return self._top_entity


""" CISCO_ENVMON_MIB 

The MIB module to describe the status of the Environmental
Monitor on those devices which support one.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoEnvMonState(Enum):
    """
    CiscoEnvMonState (Enum Class)

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
    
    
    .. attribute:: ciscoenvmonobjects
    
    	
    	**type**\:  :py:class:`CiscoEnvMonObjects <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.CiscoEnvMonObjects>`
    
    	**config**\: False
    
    .. attribute:: ciscoenvmonmibnotificationenables
    
    	
    	**type**\:  :py:class:`CiscoEnvMonMIBNotificationEnables <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.CiscoEnvMonMIBNotificationEnables>`
    
    	**config**\: False
    
    .. attribute:: ciscoenvmonvoltagestatustable
    
    	The table of voltage status maintained by the environmental monitor
    	**type**\:  :py:class:`CiscoEnvMonVoltageStatusTable <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.CiscoEnvMonVoltageStatusTable>`
    
    	**config**\: False
    
    .. attribute:: ciscoenvmontemperaturestatustable
    
    	The table of ambient temperature status maintained by the environmental monitor
    	**type**\:  :py:class:`CiscoEnvMonTemperatureStatusTable <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.CiscoEnvMonTemperatureStatusTable>`
    
    	**config**\: False
    
    .. attribute:: ciscoenvmonfanstatustable
    
    	The table of fan status maintained by the environmental monitor
    	**type**\:  :py:class:`CiscoEnvMonFanStatusTable <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.CiscoEnvMonFanStatusTable>`
    
    	**config**\: False
    
    .. attribute:: ciscoenvmonsupplystatustable
    
    	The table of power supply status maintained by the environmental monitor card
    	**type**\:  :py:class:`CiscoEnvMonSupplyStatusTable <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.CiscoEnvMonSupplyStatusTable>`
    
    	**config**\: False
    
    

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
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ciscoEnvMonObjects", ("ciscoenvmonobjects", CISCOENVMONMIB.CiscoEnvMonObjects)), ("ciscoEnvMonMIBNotificationEnables", ("ciscoenvmonmibnotificationenables", CISCOENVMONMIB.CiscoEnvMonMIBNotificationEnables)), ("ciscoEnvMonVoltageStatusTable", ("ciscoenvmonvoltagestatustable", CISCOENVMONMIB.CiscoEnvMonVoltageStatusTable)), ("ciscoEnvMonTemperatureStatusTable", ("ciscoenvmontemperaturestatustable", CISCOENVMONMIB.CiscoEnvMonTemperatureStatusTable)), ("ciscoEnvMonFanStatusTable", ("ciscoenvmonfanstatustable", CISCOENVMONMIB.CiscoEnvMonFanStatusTable)), ("ciscoEnvMonSupplyStatusTable", ("ciscoenvmonsupplystatustable", CISCOENVMONMIB.CiscoEnvMonSupplyStatusTable))])
        self._leafs = OrderedDict()

        self.ciscoenvmonobjects = CISCOENVMONMIB.CiscoEnvMonObjects()
        self.ciscoenvmonobjects.parent = self
        self._children_name_map["ciscoenvmonobjects"] = "ciscoEnvMonObjects"

        self.ciscoenvmonmibnotificationenables = CISCOENVMONMIB.CiscoEnvMonMIBNotificationEnables()
        self.ciscoenvmonmibnotificationenables.parent = self
        self._children_name_map["ciscoenvmonmibnotificationenables"] = "ciscoEnvMonMIBNotificationEnables"

        self.ciscoenvmonvoltagestatustable = CISCOENVMONMIB.CiscoEnvMonVoltageStatusTable()
        self.ciscoenvmonvoltagestatustable.parent = self
        self._children_name_map["ciscoenvmonvoltagestatustable"] = "ciscoEnvMonVoltageStatusTable"

        self.ciscoenvmontemperaturestatustable = CISCOENVMONMIB.CiscoEnvMonTemperatureStatusTable()
        self.ciscoenvmontemperaturestatustable.parent = self
        self._children_name_map["ciscoenvmontemperaturestatustable"] = "ciscoEnvMonTemperatureStatusTable"

        self.ciscoenvmonfanstatustable = CISCOENVMONMIB.CiscoEnvMonFanStatusTable()
        self.ciscoenvmonfanstatustable.parent = self
        self._children_name_map["ciscoenvmonfanstatustable"] = "ciscoEnvMonFanStatusTable"

        self.ciscoenvmonsupplystatustable = CISCOENVMONMIB.CiscoEnvMonSupplyStatusTable()
        self.ciscoenvmonsupplystatustable.parent = self
        self._children_name_map["ciscoenvmonsupplystatustable"] = "ciscoEnvMonSupplyStatusTable"
        self._segment_path = lambda: "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOENVMONMIB, [], name, value)


    class CiscoEnvMonObjects(Entity):
        """
        
        
        .. attribute:: ciscoenvmonpresent
        
        	The type of environmental monitor located in the chassis. An oldAgs environmental monitor card is identical to an ags environmental card except that it is not capable of supplying data, and hence no instance of the remaining objects in this MIB will be returned in response to an SNMP query.  Note that only a firmware upgrade is required to convert an oldAgs into an ags card
        	**type**\:  :py:class:`CiscoEnvMonPresent <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.CiscoEnvMonObjects.CiscoEnvMonPresent>`
        
        	**config**\: False
        
        .. attribute:: ciscoenvmonalarmcontacts
        
        	Each bit is set to reflect the respective alarm being set.  The bit will be cleared when the respective alarm is cleared
        	**type**\:  :py:class:`CiscoEnvMonAlarmContacts <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.CiscoEnvMonObjects.CiscoEnvMonAlarmContacts>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-ENVMON-MIB'
        _revision = '2003-12-01'

        def __init__(self):
            super(CISCOENVMONMIB.CiscoEnvMonObjects, self).__init__()

            self.yang_name = "ciscoEnvMonObjects"
            self.yang_parent_name = "CISCO-ENVMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ciscoenvmonpresent', (YLeaf(YType.enumeration, 'ciscoEnvMonPresent'), [('ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB', 'CISCOENVMONMIB', 'CiscoEnvMonObjects.CiscoEnvMonPresent')])),
                ('ciscoenvmonalarmcontacts', (YLeaf(YType.bits, 'ciscoEnvMonAlarmContacts'), ['Bits'])),
            ])
            self.ciscoenvmonpresent = None
            self.ciscoenvmonalarmcontacts = Bits()
            self._segment_path = lambda: "ciscoEnvMonObjects"
            self._absolute_path = lambda: "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENVMONMIB.CiscoEnvMonObjects, ['ciscoenvmonpresent', 'ciscoenvmonalarmcontacts'], name, value)

        class CiscoEnvMonPresent(Enum):
            """
            CiscoEnvMonPresent (Enum Class)

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




    class CiscoEnvMonMIBNotificationEnables(Entity):
        """
        
        
        .. attribute:: ciscoenvmonenableshutdownnotification
        
        	This variable  indicates  whether  the  system produces the ciscoEnvMonShutdownNotification.  A false  value will prevent shutdown notifications  from being generated by this system
        	**type**\: bool
        
        	**config**\: False
        
        .. attribute:: ciscoenvmonenablevoltagenotification
        
        	This variable  indicates  whether  the  system produces the ciscoEnvMonVoltageNotification. A false  value will prevent voltage notifications from being  generated by this system. This object is deprecated in favour of ciscoEnvMonEnableStatChangeNotif
        	**type**\: bool
        
        	**config**\: False
        
        	**status**\: deprecated
        
        .. attribute:: ciscoenvmonenabletemperaturenotification
        
        	This variable  indicates  whether  the  system produces the ciscoEnvMonTemperatureNotification. A false value prevents temperature notifications  from being sent by  this entity. This object is  deprecated in favour of  ciscoEnvMonEnableStatChangeNotif
        	**type**\: bool
        
        	**config**\: False
        
        	**status**\: deprecated
        
        .. attribute:: ciscoenvmonenablefannotification
        
        	This variable  indicates  whether  the  system produces the ciscoEnvMonFanNotification. A false value prevents fan notifications  from being sent by  this entity. This object is  deprecated in favour of  ciscoEnvMonEnableStatChangeNotif
        	**type**\: bool
        
        	**config**\: False
        
        	**status**\: deprecated
        
        .. attribute:: ciscoenvmonenableredundantsupplynotification
        
        	This variable  indicates  whether  the  system produces the ciscoEnvMonRedundantSupplyNotification.  A false value prevents redundant supply notifications from being generated by this system. This object is deprecated in favour of  ciscoEnvMonEnableStatChangeNotif
        	**type**\: bool
        
        	**config**\: False
        
        	**status**\: deprecated
        
        .. attribute:: ciscoenvmonenablestatchangenotif
        
        	This variable indicates whether the system produces the ciscoEnvMonVoltStatusChangeNotif, ciscoEnvMonTempStatusChangeNotif,  ciscoEnvMonFanStatusChangeNotif and   ciscoEnvMonSuppStatusChangeNotif. A false value will  prevent these notifications from being generated by  this system
        	**type**\: bool
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-ENVMON-MIB'
        _revision = '2003-12-01'

        def __init__(self):
            super(CISCOENVMONMIB.CiscoEnvMonMIBNotificationEnables, self).__init__()

            self.yang_name = "ciscoEnvMonMIBNotificationEnables"
            self.yang_parent_name = "CISCO-ENVMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ciscoenvmonenableshutdownnotification', (YLeaf(YType.boolean, 'ciscoEnvMonEnableShutdownNotification'), ['bool'])),
                ('ciscoenvmonenablevoltagenotification', (YLeaf(YType.boolean, 'ciscoEnvMonEnableVoltageNotification'), ['bool'])),
                ('ciscoenvmonenabletemperaturenotification', (YLeaf(YType.boolean, 'ciscoEnvMonEnableTemperatureNotification'), ['bool'])),
                ('ciscoenvmonenablefannotification', (YLeaf(YType.boolean, 'ciscoEnvMonEnableFanNotification'), ['bool'])),
                ('ciscoenvmonenableredundantsupplynotification', (YLeaf(YType.boolean, 'ciscoEnvMonEnableRedundantSupplyNotification'), ['bool'])),
                ('ciscoenvmonenablestatchangenotif', (YLeaf(YType.boolean, 'ciscoEnvMonEnableStatChangeNotif'), ['bool'])),
            ])
            self.ciscoenvmonenableshutdownnotification = None
            self.ciscoenvmonenablevoltagenotification = None
            self.ciscoenvmonenabletemperaturenotification = None
            self.ciscoenvmonenablefannotification = None
            self.ciscoenvmonenableredundantsupplynotification = None
            self.ciscoenvmonenablestatchangenotif = None
            self._segment_path = lambda: "ciscoEnvMonMIBNotificationEnables"
            self._absolute_path = lambda: "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENVMONMIB.CiscoEnvMonMIBNotificationEnables, ['ciscoenvmonenableshutdownnotification', 'ciscoenvmonenablevoltagenotification', 'ciscoenvmonenabletemperaturenotification', 'ciscoenvmonenablefannotification', 'ciscoenvmonenableredundantsupplynotification', 'ciscoenvmonenablestatchangenotif'], name, value)



    class CiscoEnvMonVoltageStatusTable(Entity):
        """
        The table of voltage status maintained by the environmental
        monitor.
        
        .. attribute:: ciscoenvmonvoltagestatusentry
        
        	An entry in the voltage status table, representing the status of the associated testpoint maintained by the environmental monitor
        	**type**\: list of  		 :py:class:`CiscoEnvMonVoltageStatusEntry <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.CiscoEnvMonVoltageStatusTable.CiscoEnvMonVoltageStatusEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-ENVMON-MIB'
        _revision = '2003-12-01'

        def __init__(self):
            super(CISCOENVMONMIB.CiscoEnvMonVoltageStatusTable, self).__init__()

            self.yang_name = "ciscoEnvMonVoltageStatusTable"
            self.yang_parent_name = "CISCO-ENVMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ciscoEnvMonVoltageStatusEntry", ("ciscoenvmonvoltagestatusentry", CISCOENVMONMIB.CiscoEnvMonVoltageStatusTable.CiscoEnvMonVoltageStatusEntry))])
            self._leafs = OrderedDict()

            self.ciscoenvmonvoltagestatusentry = YList(self)
            self._segment_path = lambda: "ciscoEnvMonVoltageStatusTable"
            self._absolute_path = lambda: "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENVMONMIB.CiscoEnvMonVoltageStatusTable, [], name, value)


        class CiscoEnvMonVoltageStatusEntry(Entity):
            """
            An entry in the voltage status table, representing the status
            of the associated testpoint maintained by the environmental
            monitor.
            
            .. attribute:: ciscoenvmonvoltagestatusindex  (key)
            
            	Unique index for the testpoint being instrumented. This index is for SNMP purposes only, and has no intrinsic meaning
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: ciscoenvmonvoltagestatusdescr
            
            	Textual description of the testpoint being instrumented. This description is a short textual label, suitable as a human\-sensible identification for the rest of the information in the entry
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: ciscoenvmonvoltagestatusvalue
            
            	The current measurement of the testpoint being instrumented
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: millivolts
            
            .. attribute:: ciscoenvmonvoltagethresholdlow
            
            	The lowest value that the associated instance of the object ciscoEnvMonVoltageStatusValue may obtain before an emergency shutdown of the managed device is initiated
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: millivolts
            
            .. attribute:: ciscoenvmonvoltagethresholdhigh
            
            	The highest value that the associated instance of the object ciscoEnvMonVoltageStatusValue may obtain before an emergency shutdown of the managed device is initiated
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: millivolts
            
            .. attribute:: ciscoenvmonvoltagelastshutdown
            
            	The value of the associated instance of the object ciscoEnvMonVoltageStatusValue at the time an emergency shutdown of the managed device was last initiated.  This value is stored in non\-volatile RAM and hence is able to survive the shutdown
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: millivolts
            
            .. attribute:: ciscoenvmonvoltagestate
            
            	The current state of the testpoint being instrumented
            	**type**\:  :py:class:`CiscoEnvMonState <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoEnvMonState>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-ENVMON-MIB'
            _revision = '2003-12-01'

            def __init__(self):
                super(CISCOENVMONMIB.CiscoEnvMonVoltageStatusTable.CiscoEnvMonVoltageStatusEntry, self).__init__()

                self.yang_name = "ciscoEnvMonVoltageStatusEntry"
                self.yang_parent_name = "ciscoEnvMonVoltageStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ciscoenvmonvoltagestatusindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ciscoenvmonvoltagestatusindex', (YLeaf(YType.int32, 'ciscoEnvMonVoltageStatusIndex'), ['int'])),
                    ('ciscoenvmonvoltagestatusdescr', (YLeaf(YType.str, 'ciscoEnvMonVoltageStatusDescr'), ['str'])),
                    ('ciscoenvmonvoltagestatusvalue', (YLeaf(YType.int32, 'ciscoEnvMonVoltageStatusValue'), ['int'])),
                    ('ciscoenvmonvoltagethresholdlow', (YLeaf(YType.int32, 'ciscoEnvMonVoltageThresholdLow'), ['int'])),
                    ('ciscoenvmonvoltagethresholdhigh', (YLeaf(YType.int32, 'ciscoEnvMonVoltageThresholdHigh'), ['int'])),
                    ('ciscoenvmonvoltagelastshutdown', (YLeaf(YType.int32, 'ciscoEnvMonVoltageLastShutdown'), ['int'])),
                    ('ciscoenvmonvoltagestate', (YLeaf(YType.enumeration, 'ciscoEnvMonVoltageState'), [('ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB', 'CiscoEnvMonState', '')])),
                ])
                self.ciscoenvmonvoltagestatusindex = None
                self.ciscoenvmonvoltagestatusdescr = None
                self.ciscoenvmonvoltagestatusvalue = None
                self.ciscoenvmonvoltagethresholdlow = None
                self.ciscoenvmonvoltagethresholdhigh = None
                self.ciscoenvmonvoltagelastshutdown = None
                self.ciscoenvmonvoltagestate = None
                self._segment_path = lambda: "ciscoEnvMonVoltageStatusEntry" + "[ciscoEnvMonVoltageStatusIndex='" + str(self.ciscoenvmonvoltagestatusindex) + "']"
                self._absolute_path = lambda: "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/ciscoEnvMonVoltageStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENVMONMIB.CiscoEnvMonVoltageStatusTable.CiscoEnvMonVoltageStatusEntry, ['ciscoenvmonvoltagestatusindex', 'ciscoenvmonvoltagestatusdescr', 'ciscoenvmonvoltagestatusvalue', 'ciscoenvmonvoltagethresholdlow', 'ciscoenvmonvoltagethresholdhigh', 'ciscoenvmonvoltagelastshutdown', 'ciscoenvmonvoltagestate'], name, value)




    class CiscoEnvMonTemperatureStatusTable(Entity):
        """
        The table of ambient temperature status maintained by the
        environmental monitor.
        
        .. attribute:: ciscoenvmontemperaturestatusentry
        
        	An entry in the ambient temperature status table, representing the status of the associated testpoint maintained by the environmental monitor
        	**type**\: list of  		 :py:class:`CiscoEnvMonTemperatureStatusEntry <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.CiscoEnvMonTemperatureStatusTable.CiscoEnvMonTemperatureStatusEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-ENVMON-MIB'
        _revision = '2003-12-01'

        def __init__(self):
            super(CISCOENVMONMIB.CiscoEnvMonTemperatureStatusTable, self).__init__()

            self.yang_name = "ciscoEnvMonTemperatureStatusTable"
            self.yang_parent_name = "CISCO-ENVMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ciscoEnvMonTemperatureStatusEntry", ("ciscoenvmontemperaturestatusentry", CISCOENVMONMIB.CiscoEnvMonTemperatureStatusTable.CiscoEnvMonTemperatureStatusEntry))])
            self._leafs = OrderedDict()

            self.ciscoenvmontemperaturestatusentry = YList(self)
            self._segment_path = lambda: "ciscoEnvMonTemperatureStatusTable"
            self._absolute_path = lambda: "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENVMONMIB.CiscoEnvMonTemperatureStatusTable, [], name, value)


        class CiscoEnvMonTemperatureStatusEntry(Entity):
            """
            An entry in the ambient temperature status table, representing
            the status of the associated testpoint maintained by the
            environmental monitor.
            
            .. attribute:: ciscoenvmontemperaturestatusindex  (key)
            
            	Unique index for the testpoint being instrumented. This index is for SNMP purposes only, and has no intrinsic meaning
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: ciscoenvmontemperaturestatusdescr
            
            	Textual description of the testpoint being instrumented. This description is a short textual label, suitable as a human\-sensible identification for the rest of the information in the entry
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: ciscoenvmontemperaturestatusvalue
            
            	The current measurement of the testpoint being instrumented
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: degrees Celsius
            
            .. attribute:: ciscoenvmontemperaturethreshold
            
            	The highest value that the associated instance of the object ciscoEnvMonTemperatureStatusValue may obtain before an emergency shutdown of the managed device is initiated
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: degrees Celsius
            
            .. attribute:: ciscoenvmontemperaturelastshutdown
            
            	The value of the associated instance of the object ciscoEnvMonTemperatureStatusValue at the time an emergency shutdown of the managed device was last initiated.  This value is stored in non\-volatile RAM and hence is able to survive the shutdown
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: degrees Celsius
            
            .. attribute:: ciscoenvmontemperaturestate
            
            	The current state of the testpoint being instrumented
            	**type**\:  :py:class:`CiscoEnvMonState <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoEnvMonState>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-ENVMON-MIB'
            _revision = '2003-12-01'

            def __init__(self):
                super(CISCOENVMONMIB.CiscoEnvMonTemperatureStatusTable.CiscoEnvMonTemperatureStatusEntry, self).__init__()

                self.yang_name = "ciscoEnvMonTemperatureStatusEntry"
                self.yang_parent_name = "ciscoEnvMonTemperatureStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ciscoenvmontemperaturestatusindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ciscoenvmontemperaturestatusindex', (YLeaf(YType.int32, 'ciscoEnvMonTemperatureStatusIndex'), ['int'])),
                    ('ciscoenvmontemperaturestatusdescr', (YLeaf(YType.str, 'ciscoEnvMonTemperatureStatusDescr'), ['str'])),
                    ('ciscoenvmontemperaturestatusvalue', (YLeaf(YType.uint32, 'ciscoEnvMonTemperatureStatusValue'), ['int'])),
                    ('ciscoenvmontemperaturethreshold', (YLeaf(YType.int32, 'ciscoEnvMonTemperatureThreshold'), ['int'])),
                    ('ciscoenvmontemperaturelastshutdown', (YLeaf(YType.int32, 'ciscoEnvMonTemperatureLastShutdown'), ['int'])),
                    ('ciscoenvmontemperaturestate', (YLeaf(YType.enumeration, 'ciscoEnvMonTemperatureState'), [('ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB', 'CiscoEnvMonState', '')])),
                ])
                self.ciscoenvmontemperaturestatusindex = None
                self.ciscoenvmontemperaturestatusdescr = None
                self.ciscoenvmontemperaturestatusvalue = None
                self.ciscoenvmontemperaturethreshold = None
                self.ciscoenvmontemperaturelastshutdown = None
                self.ciscoenvmontemperaturestate = None
                self._segment_path = lambda: "ciscoEnvMonTemperatureStatusEntry" + "[ciscoEnvMonTemperatureStatusIndex='" + str(self.ciscoenvmontemperaturestatusindex) + "']"
                self._absolute_path = lambda: "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/ciscoEnvMonTemperatureStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENVMONMIB.CiscoEnvMonTemperatureStatusTable.CiscoEnvMonTemperatureStatusEntry, ['ciscoenvmontemperaturestatusindex', 'ciscoenvmontemperaturestatusdescr', 'ciscoenvmontemperaturestatusvalue', 'ciscoenvmontemperaturethreshold', 'ciscoenvmontemperaturelastshutdown', 'ciscoenvmontemperaturestate'], name, value)




    class CiscoEnvMonFanStatusTable(Entity):
        """
        The table of fan status maintained by the environmental
        monitor.
        
        .. attribute:: ciscoenvmonfanstatusentry
        
        	An entry in the fan status table, representing the status of the associated fan maintained by the environmental monitor
        	**type**\: list of  		 :py:class:`CiscoEnvMonFanStatusEntry <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.CiscoEnvMonFanStatusTable.CiscoEnvMonFanStatusEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-ENVMON-MIB'
        _revision = '2003-12-01'

        def __init__(self):
            super(CISCOENVMONMIB.CiscoEnvMonFanStatusTable, self).__init__()

            self.yang_name = "ciscoEnvMonFanStatusTable"
            self.yang_parent_name = "CISCO-ENVMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ciscoEnvMonFanStatusEntry", ("ciscoenvmonfanstatusentry", CISCOENVMONMIB.CiscoEnvMonFanStatusTable.CiscoEnvMonFanStatusEntry))])
            self._leafs = OrderedDict()

            self.ciscoenvmonfanstatusentry = YList(self)
            self._segment_path = lambda: "ciscoEnvMonFanStatusTable"
            self._absolute_path = lambda: "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENVMONMIB.CiscoEnvMonFanStatusTable, [], name, value)


        class CiscoEnvMonFanStatusEntry(Entity):
            """
            An entry in the fan status table, representing the status of
            the associated fan maintained by the environmental monitor.
            
            .. attribute:: ciscoenvmonfanstatusindex  (key)
            
            	Unique index for the fan being instrumented. This index is for SNMP purposes only, and has no intrinsic meaning
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: ciscoenvmonfanstatusdescr
            
            	Textual description of the fan being instrumented. This description is a short textual label, suitable as a human\-sensible identification for the rest of the information in the entry
            	**type**\: str
            
            	**length:** 0..32
            
            	**config**\: False
            
            .. attribute:: ciscoenvmonfanstate
            
            	The current state of the fan being instrumented
            	**type**\:  :py:class:`CiscoEnvMonState <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoEnvMonState>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-ENVMON-MIB'
            _revision = '2003-12-01'

            def __init__(self):
                super(CISCOENVMONMIB.CiscoEnvMonFanStatusTable.CiscoEnvMonFanStatusEntry, self).__init__()

                self.yang_name = "ciscoEnvMonFanStatusEntry"
                self.yang_parent_name = "ciscoEnvMonFanStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ciscoenvmonfanstatusindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ciscoenvmonfanstatusindex', (YLeaf(YType.int32, 'ciscoEnvMonFanStatusIndex'), ['int'])),
                    ('ciscoenvmonfanstatusdescr', (YLeaf(YType.str, 'ciscoEnvMonFanStatusDescr'), ['str'])),
                    ('ciscoenvmonfanstate', (YLeaf(YType.enumeration, 'ciscoEnvMonFanState'), [('ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB', 'CiscoEnvMonState', '')])),
                ])
                self.ciscoenvmonfanstatusindex = None
                self.ciscoenvmonfanstatusdescr = None
                self.ciscoenvmonfanstate = None
                self._segment_path = lambda: "ciscoEnvMonFanStatusEntry" + "[ciscoEnvMonFanStatusIndex='" + str(self.ciscoenvmonfanstatusindex) + "']"
                self._absolute_path = lambda: "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/ciscoEnvMonFanStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENVMONMIB.CiscoEnvMonFanStatusTable.CiscoEnvMonFanStatusEntry, ['ciscoenvmonfanstatusindex', 'ciscoenvmonfanstatusdescr', 'ciscoenvmonfanstate'], name, value)




    class CiscoEnvMonSupplyStatusTable(Entity):
        """
        The table of power supply status maintained by the
        environmental monitor card.
        
        .. attribute:: ciscoenvmonsupplystatusentry
        
        	An entry in the power supply status table, representing the status of the associated power supply maintained by the environmental monitor card
        	**type**\: list of  		 :py:class:`CiscoEnvMonSupplyStatusEntry <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.CiscoEnvMonSupplyStatusTable.CiscoEnvMonSupplyStatusEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-ENVMON-MIB'
        _revision = '2003-12-01'

        def __init__(self):
            super(CISCOENVMONMIB.CiscoEnvMonSupplyStatusTable, self).__init__()

            self.yang_name = "ciscoEnvMonSupplyStatusTable"
            self.yang_parent_name = "CISCO-ENVMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ciscoEnvMonSupplyStatusEntry", ("ciscoenvmonsupplystatusentry", CISCOENVMONMIB.CiscoEnvMonSupplyStatusTable.CiscoEnvMonSupplyStatusEntry))])
            self._leafs = OrderedDict()

            self.ciscoenvmonsupplystatusentry = YList(self)
            self._segment_path = lambda: "ciscoEnvMonSupplyStatusTable"
            self._absolute_path = lambda: "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENVMONMIB.CiscoEnvMonSupplyStatusTable, [], name, value)


        class CiscoEnvMonSupplyStatusEntry(Entity):
            """
            An entry in the power supply status table, representing the
            status of the associated power supply maintained by the
            environmental monitor card.
            
            .. attribute:: ciscoenvmonsupplystatusindex  (key)
            
            	Unique index for the power supply being instrumented. This index is for SNMP purposes only, and has no intrinsic meaning
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: ciscoenvmonsupplystatusdescr
            
            	Textual description of the power supply being instrumented. This description is a short textual label, suitable as a human\-sensible identification for the rest of the information in the entry
            	**type**\: str
            
            	**length:** 0..64
            
            	**config**\: False
            
            .. attribute:: ciscoenvmonsupplystate
            
            	The current state of the power supply being instrumented
            	**type**\:  :py:class:`CiscoEnvMonState <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoEnvMonState>`
            
            	**config**\: False
            
            .. attribute:: ciscoenvmonsupplysource
            
            	The power supply source. unknown \- Power supply source unknown ac      \- AC power supply dc      \- DC power supply externalPowerSupply \- External power supply internalRedundant \- Internal redundant power supply 
            	**type**\:  :py:class:`CiscoEnvMonSupplySource <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CISCOENVMONMIB.CiscoEnvMonSupplyStatusTable.CiscoEnvMonSupplyStatusEntry.CiscoEnvMonSupplySource>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-ENVMON-MIB'
            _revision = '2003-12-01'

            def __init__(self):
                super(CISCOENVMONMIB.CiscoEnvMonSupplyStatusTable.CiscoEnvMonSupplyStatusEntry, self).__init__()

                self.yang_name = "ciscoEnvMonSupplyStatusEntry"
                self.yang_parent_name = "ciscoEnvMonSupplyStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ciscoenvmonsupplystatusindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ciscoenvmonsupplystatusindex', (YLeaf(YType.int32, 'ciscoEnvMonSupplyStatusIndex'), ['int'])),
                    ('ciscoenvmonsupplystatusdescr', (YLeaf(YType.str, 'ciscoEnvMonSupplyStatusDescr'), ['str'])),
                    ('ciscoenvmonsupplystate', (YLeaf(YType.enumeration, 'ciscoEnvMonSupplyState'), [('ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB', 'CiscoEnvMonState', '')])),
                    ('ciscoenvmonsupplysource', (YLeaf(YType.enumeration, 'ciscoEnvMonSupplySource'), [('ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB', 'CISCOENVMONMIB', 'CiscoEnvMonSupplyStatusTable.CiscoEnvMonSupplyStatusEntry.CiscoEnvMonSupplySource')])),
                ])
                self.ciscoenvmonsupplystatusindex = None
                self.ciscoenvmonsupplystatusdescr = None
                self.ciscoenvmonsupplystate = None
                self.ciscoenvmonsupplysource = None
                self._segment_path = lambda: "ciscoEnvMonSupplyStatusEntry" + "[ciscoEnvMonSupplyStatusIndex='" + str(self.ciscoenvmonsupplystatusindex) + "']"
                self._absolute_path = lambda: "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/ciscoEnvMonSupplyStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENVMONMIB.CiscoEnvMonSupplyStatusTable.CiscoEnvMonSupplyStatusEntry, ['ciscoenvmonsupplystatusindex', 'ciscoenvmonsupplystatusdescr', 'ciscoenvmonsupplystate', 'ciscoenvmonsupplysource'], name, value)

            class CiscoEnvMonSupplySource(Enum):
                """
                CiscoEnvMonSupplySource (Enum Class)

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




    def clone_ptr(self):
        self._top_entity = CISCOENVMONMIB()
        return self._top_entity




""" CISCO_ENVMON_MIB 

The MIB module to describe the status of the Environmental
Monitor on those devices which support one.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CiscoenvmonstateEnum(Enum):
    """
    CiscoenvmonstateEnum

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

    normal = 1

    warning = 2

    critical = 3

    shutdown = 4

    notPresent = 5

    notFunctioning = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ENVMON_MIB as meta
        return meta._meta_table['CiscoenvmonstateEnum']



class CiscoEnvmonMib(object):
    """
    
    
    .. attribute:: ciscoenvmonfanstatustable
    
    	The table of fan status maintained by the environmental monitor
    	**type**\:   :py:class:`Ciscoenvmonfanstatustable <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoEnvmonMib.Ciscoenvmonfanstatustable>`
    
    .. attribute:: ciscoenvmonmibnotificationenables
    
    	
    	**type**\:   :py:class:`Ciscoenvmonmibnotificationenables <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoEnvmonMib.Ciscoenvmonmibnotificationenables>`
    
    .. attribute:: ciscoenvmonobjects
    
    	
    	**type**\:   :py:class:`Ciscoenvmonobjects <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoEnvmonMib.Ciscoenvmonobjects>`
    
    .. attribute:: ciscoenvmonsupplystatustable
    
    	The table of power supply status maintained by the environmental monitor card
    	**type**\:   :py:class:`Ciscoenvmonsupplystatustable <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoEnvmonMib.Ciscoenvmonsupplystatustable>`
    
    .. attribute:: ciscoenvmontemperaturestatustable
    
    	The table of ambient temperature status maintained by the environmental monitor
    	**type**\:   :py:class:`Ciscoenvmontemperaturestatustable <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoEnvmonMib.Ciscoenvmontemperaturestatustable>`
    
    .. attribute:: ciscoenvmonvoltagestatustable
    
    	The table of voltage status maintained by the environmental monitor
    	**type**\:   :py:class:`Ciscoenvmonvoltagestatustable <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoEnvmonMib.Ciscoenvmonvoltagestatustable>`
    
    

    """

    _prefix = 'CISCO-ENVMON-MIB'
    _revision = '2003-12-01'

    def __init__(self):
        self.ciscoenvmonfanstatustable = CiscoEnvmonMib.Ciscoenvmonfanstatustable()
        self.ciscoenvmonfanstatustable.parent = self
        self.ciscoenvmonmibnotificationenables = CiscoEnvmonMib.Ciscoenvmonmibnotificationenables()
        self.ciscoenvmonmibnotificationenables.parent = self
        self.ciscoenvmonobjects = CiscoEnvmonMib.Ciscoenvmonobjects()
        self.ciscoenvmonobjects.parent = self
        self.ciscoenvmonsupplystatustable = CiscoEnvmonMib.Ciscoenvmonsupplystatustable()
        self.ciscoenvmonsupplystatustable.parent = self
        self.ciscoenvmontemperaturestatustable = CiscoEnvmonMib.Ciscoenvmontemperaturestatustable()
        self.ciscoenvmontemperaturestatustable.parent = self
        self.ciscoenvmonvoltagestatustable = CiscoEnvmonMib.Ciscoenvmonvoltagestatustable()
        self.ciscoenvmonvoltagestatustable.parent = self


    class Ciscoenvmonobjects(object):
        """
        
        
        .. attribute:: ciscoenvmonalarmcontacts
        
        	Each bit is set to reflect the respective alarm being set.  The bit will be cleared when the respective alarm is cleared
        	**type**\:   :py:class:`Ciscoenvmonalarmcontacts <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoEnvmonMib.Ciscoenvmonobjects.Ciscoenvmonalarmcontacts>`
        
        .. attribute:: ciscoenvmonpresent
        
        	The type of environmental monitor located in the chassis. An oldAgs environmental monitor card is identical to an ags environmental card except that it is not capable of supplying data, and hence no instance of the remaining objects in this MIB will be returned in response to an SNMP query.  Note that only a firmware upgrade is required to convert an oldAgs into an ags card
        	**type**\:   :py:class:`CiscoenvmonpresentEnum <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoEnvmonMib.Ciscoenvmonobjects.CiscoenvmonpresentEnum>`
        
        

        """

        _prefix = 'CISCO-ENVMON-MIB'
        _revision = '2003-12-01'

        def __init__(self):
            self.parent = None
            self.ciscoenvmonalarmcontacts = CiscoEnvmonMib.Ciscoenvmonobjects.Ciscoenvmonalarmcontacts()
            self.ciscoenvmonpresent = None

        class CiscoenvmonpresentEnum(Enum):
            """
            CiscoenvmonpresentEnum

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

            oldAgs = 1

            ags = 2

            c7000 = 3

            ci = 4

            cAccessMon = 6

            cat6000 = 7

            ubr7200 = 8

            cat4000 = 9

            c10000 = 10

            osr7600 = 11

            c7600 = 12

            c37xx = 13

            other = 14


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENVMON_MIB as meta
                return meta._meta_table['CiscoEnvmonMib.Ciscoenvmonobjects.CiscoenvmonpresentEnum']


        class Ciscoenvmonalarmcontacts(FixedBitsDict):
            """
            Ciscoenvmonalarmcontacts

            Each bit is set to reflect the respective
            alarm being set.  The bit will be cleared
            when the respective alarm is cleared.
            Keys are:- minorAudible , input , criticalAudible , minorVisual , majorAudible , majorVisual , criticalVisual

            """

            def __init__(self):
                self._dictionary = { 
                    'minorAudible':False,
                    'input':False,
                    'criticalAudible':False,
                    'minorVisual':False,
                    'majorAudible':False,
                    'majorVisual':False,
                    'criticalVisual':False,
                }
                self._pos_map = { 
                    'minorAudible':3,
                    'input':6,
                    'criticalAudible':5,
                    'minorVisual':0,
                    'majorAudible':4,
                    'majorVisual':1,
                    'criticalVisual':2,
                }

        @property
        def _common_path(self):

            return '/CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/CISCO-ENVMON-MIB:ciscoEnvMonObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ciscoenvmonalarmcontacts is not None:
                if self.ciscoenvmonalarmcontacts._has_data():
                    return True

            if self.ciscoenvmonpresent is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENVMON_MIB as meta
            return meta._meta_table['CiscoEnvmonMib.Ciscoenvmonobjects']['meta_info']


    class Ciscoenvmonmibnotificationenables(object):
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
            self.parent = None
            self.ciscoenvmonenablefannotification = None
            self.ciscoenvmonenableredundantsupplynotification = None
            self.ciscoenvmonenableshutdownnotification = None
            self.ciscoenvmonenablestatchangenotif = None
            self.ciscoenvmonenabletemperaturenotification = None
            self.ciscoenvmonenablevoltagenotification = None

        @property
        def _common_path(self):

            return '/CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/CISCO-ENVMON-MIB:ciscoEnvMonMIBNotificationEnables'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ciscoenvmonenablefannotification is not None:
                return True

            if self.ciscoenvmonenableredundantsupplynotification is not None:
                return True

            if self.ciscoenvmonenableshutdownnotification is not None:
                return True

            if self.ciscoenvmonenablestatchangenotif is not None:
                return True

            if self.ciscoenvmonenabletemperaturenotification is not None:
                return True

            if self.ciscoenvmonenablevoltagenotification is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENVMON_MIB as meta
            return meta._meta_table['CiscoEnvmonMib.Ciscoenvmonmibnotificationenables']['meta_info']


    class Ciscoenvmonvoltagestatustable(object):
        """
        The table of voltage status maintained by the environmental
        monitor.
        
        .. attribute:: ciscoenvmonvoltagestatusentry
        
        	An entry in the voltage status table, representing the status of the associated testpoint maintained by the environmental monitor
        	**type**\: list of    :py:class:`Ciscoenvmonvoltagestatusentry <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoEnvmonMib.Ciscoenvmonvoltagestatustable.Ciscoenvmonvoltagestatusentry>`
        
        

        """

        _prefix = 'CISCO-ENVMON-MIB'
        _revision = '2003-12-01'

        def __init__(self):
            self.parent = None
            self.ciscoenvmonvoltagestatusentry = YList()
            self.ciscoenvmonvoltagestatusentry.parent = self
            self.ciscoenvmonvoltagestatusentry.name = 'ciscoenvmonvoltagestatusentry'


        class Ciscoenvmonvoltagestatusentry(object):
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
            	**type**\:   :py:class:`CiscoenvmonstateEnum <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoenvmonstateEnum>`
            
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
                self.parent = None
                self.ciscoenvmonvoltagestatusindex = None
                self.ciscoenvmonvoltagelastshutdown = None
                self.ciscoenvmonvoltagestate = None
                self.ciscoenvmonvoltagestatusdescr = None
                self.ciscoenvmonvoltagestatusvalue = None
                self.ciscoenvmonvoltagethresholdhigh = None
                self.ciscoenvmonvoltagethresholdlow = None

            @property
            def _common_path(self):
                if self.ciscoenvmonvoltagestatusindex is None:
                    raise YPYModelError('Key property ciscoenvmonvoltagestatusindex is None')

                return '/CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/CISCO-ENVMON-MIB:ciscoEnvMonVoltageStatusTable/CISCO-ENVMON-MIB:ciscoEnvMonVoltageStatusEntry[CISCO-ENVMON-MIB:ciscoEnvMonVoltageStatusIndex = ' + str(self.ciscoenvmonvoltagestatusindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ciscoenvmonvoltagestatusindex is not None:
                    return True

                if self.ciscoenvmonvoltagelastshutdown is not None:
                    return True

                if self.ciscoenvmonvoltagestate is not None:
                    return True

                if self.ciscoenvmonvoltagestatusdescr is not None:
                    return True

                if self.ciscoenvmonvoltagestatusvalue is not None:
                    return True

                if self.ciscoenvmonvoltagethresholdhigh is not None:
                    return True

                if self.ciscoenvmonvoltagethresholdlow is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENVMON_MIB as meta
                return meta._meta_table['CiscoEnvmonMib.Ciscoenvmonvoltagestatustable.Ciscoenvmonvoltagestatusentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/CISCO-ENVMON-MIB:ciscoEnvMonVoltageStatusTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ciscoenvmonvoltagestatusentry is not None:
                for child_ref in self.ciscoenvmonvoltagestatusentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENVMON_MIB as meta
            return meta._meta_table['CiscoEnvmonMib.Ciscoenvmonvoltagestatustable']['meta_info']


    class Ciscoenvmontemperaturestatustable(object):
        """
        The table of ambient temperature status maintained by the
        environmental monitor.
        
        .. attribute:: ciscoenvmontemperaturestatusentry
        
        	An entry in the ambient temperature status table, representing the status of the associated testpoint maintained by the environmental monitor
        	**type**\: list of    :py:class:`Ciscoenvmontemperaturestatusentry <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoEnvmonMib.Ciscoenvmontemperaturestatustable.Ciscoenvmontemperaturestatusentry>`
        
        

        """

        _prefix = 'CISCO-ENVMON-MIB'
        _revision = '2003-12-01'

        def __init__(self):
            self.parent = None
            self.ciscoenvmontemperaturestatusentry = YList()
            self.ciscoenvmontemperaturestatusentry.parent = self
            self.ciscoenvmontemperaturestatusentry.name = 'ciscoenvmontemperaturestatusentry'


        class Ciscoenvmontemperaturestatusentry(object):
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
            	**type**\:   :py:class:`CiscoenvmonstateEnum <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoenvmonstateEnum>`
            
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
                self.parent = None
                self.ciscoenvmontemperaturestatusindex = None
                self.ciscoenvmontemperaturelastshutdown = None
                self.ciscoenvmontemperaturestate = None
                self.ciscoenvmontemperaturestatusdescr = None
                self.ciscoenvmontemperaturestatusvalue = None
                self.ciscoenvmontemperaturethreshold = None

            @property
            def _common_path(self):
                if self.ciscoenvmontemperaturestatusindex is None:
                    raise YPYModelError('Key property ciscoenvmontemperaturestatusindex is None')

                return '/CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/CISCO-ENVMON-MIB:ciscoEnvMonTemperatureStatusTable/CISCO-ENVMON-MIB:ciscoEnvMonTemperatureStatusEntry[CISCO-ENVMON-MIB:ciscoEnvMonTemperatureStatusIndex = ' + str(self.ciscoenvmontemperaturestatusindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ciscoenvmontemperaturestatusindex is not None:
                    return True

                if self.ciscoenvmontemperaturelastshutdown is not None:
                    return True

                if self.ciscoenvmontemperaturestate is not None:
                    return True

                if self.ciscoenvmontemperaturestatusdescr is not None:
                    return True

                if self.ciscoenvmontemperaturestatusvalue is not None:
                    return True

                if self.ciscoenvmontemperaturethreshold is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENVMON_MIB as meta
                return meta._meta_table['CiscoEnvmonMib.Ciscoenvmontemperaturestatustable.Ciscoenvmontemperaturestatusentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/CISCO-ENVMON-MIB:ciscoEnvMonTemperatureStatusTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ciscoenvmontemperaturestatusentry is not None:
                for child_ref in self.ciscoenvmontemperaturestatusentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENVMON_MIB as meta
            return meta._meta_table['CiscoEnvmonMib.Ciscoenvmontemperaturestatustable']['meta_info']


    class Ciscoenvmonfanstatustable(object):
        """
        The table of fan status maintained by the environmental
        monitor.
        
        .. attribute:: ciscoenvmonfanstatusentry
        
        	An entry in the fan status table, representing the status of the associated fan maintained by the environmental monitor
        	**type**\: list of    :py:class:`Ciscoenvmonfanstatusentry <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoEnvmonMib.Ciscoenvmonfanstatustable.Ciscoenvmonfanstatusentry>`
        
        

        """

        _prefix = 'CISCO-ENVMON-MIB'
        _revision = '2003-12-01'

        def __init__(self):
            self.parent = None
            self.ciscoenvmonfanstatusentry = YList()
            self.ciscoenvmonfanstatusentry.parent = self
            self.ciscoenvmonfanstatusentry.name = 'ciscoenvmonfanstatusentry'


        class Ciscoenvmonfanstatusentry(object):
            """
            An entry in the fan status table, representing the status of
            the associated fan maintained by the environmental monitor.
            
            .. attribute:: ciscoenvmonfanstatusindex  <key>
            
            	Unique index for the fan being instrumented. This index is for SNMP purposes only, and has no intrinsic meaning
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciscoenvmonfanstate
            
            	The current state of the fan being instrumented
            	**type**\:   :py:class:`CiscoenvmonstateEnum <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoenvmonstateEnum>`
            
            .. attribute:: ciscoenvmonfanstatusdescr
            
            	Textual description of the fan being instrumented. This description is a short textual label, suitable as a human\-sensible identification for the rest of the information in the entry
            	**type**\:  str
            
            	**length:** 0..32
            
            

            """

            _prefix = 'CISCO-ENVMON-MIB'
            _revision = '2003-12-01'

            def __init__(self):
                self.parent = None
                self.ciscoenvmonfanstatusindex = None
                self.ciscoenvmonfanstate = None
                self.ciscoenvmonfanstatusdescr = None

            @property
            def _common_path(self):
                if self.ciscoenvmonfanstatusindex is None:
                    raise YPYModelError('Key property ciscoenvmonfanstatusindex is None')

                return '/CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/CISCO-ENVMON-MIB:ciscoEnvMonFanStatusTable/CISCO-ENVMON-MIB:ciscoEnvMonFanStatusEntry[CISCO-ENVMON-MIB:ciscoEnvMonFanStatusIndex = ' + str(self.ciscoenvmonfanstatusindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ciscoenvmonfanstatusindex is not None:
                    return True

                if self.ciscoenvmonfanstate is not None:
                    return True

                if self.ciscoenvmonfanstatusdescr is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENVMON_MIB as meta
                return meta._meta_table['CiscoEnvmonMib.Ciscoenvmonfanstatustable.Ciscoenvmonfanstatusentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/CISCO-ENVMON-MIB:ciscoEnvMonFanStatusTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ciscoenvmonfanstatusentry is not None:
                for child_ref in self.ciscoenvmonfanstatusentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENVMON_MIB as meta
            return meta._meta_table['CiscoEnvmonMib.Ciscoenvmonfanstatustable']['meta_info']


    class Ciscoenvmonsupplystatustable(object):
        """
        The table of power supply status maintained by the
        environmental monitor card.
        
        .. attribute:: ciscoenvmonsupplystatusentry
        
        	An entry in the power supply status table, representing the status of the associated power supply maintained by the environmental monitor card
        	**type**\: list of    :py:class:`Ciscoenvmonsupplystatusentry <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoEnvmonMib.Ciscoenvmonsupplystatustable.Ciscoenvmonsupplystatusentry>`
        
        

        """

        _prefix = 'CISCO-ENVMON-MIB'
        _revision = '2003-12-01'

        def __init__(self):
            self.parent = None
            self.ciscoenvmonsupplystatusentry = YList()
            self.ciscoenvmonsupplystatusentry.parent = self
            self.ciscoenvmonsupplystatusentry.name = 'ciscoenvmonsupplystatusentry'


        class Ciscoenvmonsupplystatusentry(object):
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
            	**type**\:   :py:class:`CiscoenvmonsupplysourceEnum <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoEnvmonMib.Ciscoenvmonsupplystatustable.Ciscoenvmonsupplystatusentry.CiscoenvmonsupplysourceEnum>`
            
            .. attribute:: ciscoenvmonsupplystate
            
            	The current state of the power supply being instrumented
            	**type**\:   :py:class:`CiscoenvmonstateEnum <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoenvmonstateEnum>`
            
            .. attribute:: ciscoenvmonsupplystatusdescr
            
            	Textual description of the power supply being instrumented. This description is a short textual label, suitable as a human\-sensible identification for the rest of the information in the entry
            	**type**\:  str
            
            	**length:** 0..64
            
            

            """

            _prefix = 'CISCO-ENVMON-MIB'
            _revision = '2003-12-01'

            def __init__(self):
                self.parent = None
                self.ciscoenvmonsupplystatusindex = None
                self.ciscoenvmonsupplysource = None
                self.ciscoenvmonsupplystate = None
                self.ciscoenvmonsupplystatusdescr = None

            class CiscoenvmonsupplysourceEnum(Enum):
                """
                CiscoenvmonsupplysourceEnum

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

                unknown = 1

                ac = 2

                dc = 3

                externalPowerSupply = 4

                internalRedundant = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_ENVMON_MIB as meta
                    return meta._meta_table['CiscoEnvmonMib.Ciscoenvmonsupplystatustable.Ciscoenvmonsupplystatusentry.CiscoenvmonsupplysourceEnum']


            @property
            def _common_path(self):
                if self.ciscoenvmonsupplystatusindex is None:
                    raise YPYModelError('Key property ciscoenvmonsupplystatusindex is None')

                return '/CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/CISCO-ENVMON-MIB:ciscoEnvMonSupplyStatusTable/CISCO-ENVMON-MIB:ciscoEnvMonSupplyStatusEntry[CISCO-ENVMON-MIB:ciscoEnvMonSupplyStatusIndex = ' + str(self.ciscoenvmonsupplystatusindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ciscoenvmonsupplystatusindex is not None:
                    return True

                if self.ciscoenvmonsupplysource is not None:
                    return True

                if self.ciscoenvmonsupplystate is not None:
                    return True

                if self.ciscoenvmonsupplystatusdescr is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENVMON_MIB as meta
                return meta._meta_table['CiscoEnvmonMib.Ciscoenvmonsupplystatustable.Ciscoenvmonsupplystatusentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/CISCO-ENVMON-MIB:ciscoEnvMonSupplyStatusTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ciscoenvmonsupplystatusentry is not None:
                for child_ref in self.ciscoenvmonsupplystatusentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENVMON_MIB as meta
            return meta._meta_table['CiscoEnvmonMib.Ciscoenvmonsupplystatustable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-ENVMON-MIB:CISCO-ENVMON-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.ciscoenvmonfanstatustable is not None and self.ciscoenvmonfanstatustable._has_data():
            return True

        if self.ciscoenvmonmibnotificationenables is not None and self.ciscoenvmonmibnotificationenables._has_data():
            return True

        if self.ciscoenvmonobjects is not None and self.ciscoenvmonobjects._has_data():
            return True

        if self.ciscoenvmonsupplystatustable is not None and self.ciscoenvmonsupplystatustable._has_data():
            return True

        if self.ciscoenvmontemperaturestatustable is not None and self.ciscoenvmontemperaturestatustable._has_data():
            return True

        if self.ciscoenvmonvoltagestatustable is not None and self.ciscoenvmonvoltagestatustable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ENVMON_MIB as meta
        return meta._meta_table['CiscoEnvmonMib']['meta_info']



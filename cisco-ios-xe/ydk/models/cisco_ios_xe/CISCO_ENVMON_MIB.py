""" CISCO_ENVMON_MIB 

The MIB module to describe the status of the Environmental
Monitor on those devices which support one.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ciscoenvmonstate(Enum):
    """
    Ciscoenvmonstate

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



class CiscoEnvmonMib(Entity):
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
        super(CiscoEnvmonMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-ENVMON-MIB"
        self.yang_parent_name = "CISCO-ENVMON-MIB"

        self.ciscoenvmonfanstatustable = CiscoEnvmonMib.Ciscoenvmonfanstatustable()
        self.ciscoenvmonfanstatustable.parent = self
        self._children_name_map["ciscoenvmonfanstatustable"] = "ciscoEnvMonFanStatusTable"
        self._children_yang_names.add("ciscoEnvMonFanStatusTable")

        self.ciscoenvmonmibnotificationenables = CiscoEnvmonMib.Ciscoenvmonmibnotificationenables()
        self.ciscoenvmonmibnotificationenables.parent = self
        self._children_name_map["ciscoenvmonmibnotificationenables"] = "ciscoEnvMonMIBNotificationEnables"
        self._children_yang_names.add("ciscoEnvMonMIBNotificationEnables")

        self.ciscoenvmonobjects = CiscoEnvmonMib.Ciscoenvmonobjects()
        self.ciscoenvmonobjects.parent = self
        self._children_name_map["ciscoenvmonobjects"] = "ciscoEnvMonObjects"
        self._children_yang_names.add("ciscoEnvMonObjects")

        self.ciscoenvmonsupplystatustable = CiscoEnvmonMib.Ciscoenvmonsupplystatustable()
        self.ciscoenvmonsupplystatustable.parent = self
        self._children_name_map["ciscoenvmonsupplystatustable"] = "ciscoEnvMonSupplyStatusTable"
        self._children_yang_names.add("ciscoEnvMonSupplyStatusTable")

        self.ciscoenvmontemperaturestatustable = CiscoEnvmonMib.Ciscoenvmontemperaturestatustable()
        self.ciscoenvmontemperaturestatustable.parent = self
        self._children_name_map["ciscoenvmontemperaturestatustable"] = "ciscoEnvMonTemperatureStatusTable"
        self._children_yang_names.add("ciscoEnvMonTemperatureStatusTable")

        self.ciscoenvmonvoltagestatustable = CiscoEnvmonMib.Ciscoenvmonvoltagestatustable()
        self.ciscoenvmonvoltagestatustable.parent = self
        self._children_name_map["ciscoenvmonvoltagestatustable"] = "ciscoEnvMonVoltageStatusTable"
        self._children_yang_names.add("ciscoEnvMonVoltageStatusTable")


    class Ciscoenvmonobjects(Entity):
        """
        
        
        .. attribute:: ciscoenvmonalarmcontacts
        
        	Each bit is set to reflect the respective alarm being set.  The bit will be cleared when the respective alarm is cleared
        	**type**\:   :py:class:`Ciscoenvmonalarmcontacts <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoEnvmonMib.Ciscoenvmonobjects.Ciscoenvmonalarmcontacts>`
        
        .. attribute:: ciscoenvmonpresent
        
        	The type of environmental monitor located in the chassis. An oldAgs environmental monitor card is identical to an ags environmental card except that it is not capable of supplying data, and hence no instance of the remaining objects in this MIB will be returned in response to an SNMP query.  Note that only a firmware upgrade is required to convert an oldAgs into an ags card
        	**type**\:   :py:class:`Ciscoenvmonpresent <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoEnvmonMib.Ciscoenvmonobjects.Ciscoenvmonpresent>`
        
        

        """

        _prefix = 'CISCO-ENVMON-MIB'
        _revision = '2003-12-01'

        def __init__(self):
            super(CiscoEnvmonMib.Ciscoenvmonobjects, self).__init__()

            self.yang_name = "ciscoEnvMonObjects"
            self.yang_parent_name = "CISCO-ENVMON-MIB"

            self.ciscoenvmonalarmcontacts = YLeaf(YType.bits, "ciscoEnvMonAlarmContacts")

            self.ciscoenvmonpresent = YLeaf(YType.enumeration, "ciscoEnvMonPresent")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ciscoenvmonalarmcontacts",
                            "ciscoenvmonpresent") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoEnvmonMib.Ciscoenvmonobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEnvmonMib.Ciscoenvmonobjects, self).__setattr__(name, value)

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


        def has_data(self):
            return (
                self.ciscoenvmonalarmcontacts.is_set or
                self.ciscoenvmonpresent.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ciscoenvmonalarmcontacts.yfilter != YFilter.not_set or
                self.ciscoenvmonpresent.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoEnvMonObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ciscoenvmonalarmcontacts.is_set or self.ciscoenvmonalarmcontacts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ciscoenvmonalarmcontacts.get_name_leafdata())
            if (self.ciscoenvmonpresent.is_set or self.ciscoenvmonpresent.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ciscoenvmonpresent.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ciscoEnvMonAlarmContacts" or name == "ciscoEnvMonPresent"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ciscoEnvMonAlarmContacts"):
                self.ciscoenvmonalarmcontacts[value] = True
            if(value_path == "ciscoEnvMonPresent"):
                self.ciscoenvmonpresent = value
                self.ciscoenvmonpresent.value_namespace = name_space
                self.ciscoenvmonpresent.value_namespace_prefix = name_space_prefix


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
            super(CiscoEnvmonMib.Ciscoenvmonmibnotificationenables, self).__init__()

            self.yang_name = "ciscoEnvMonMIBNotificationEnables"
            self.yang_parent_name = "CISCO-ENVMON-MIB"

            self.ciscoenvmonenablefannotification = YLeaf(YType.boolean, "ciscoEnvMonEnableFanNotification")

            self.ciscoenvmonenableredundantsupplynotification = YLeaf(YType.boolean, "ciscoEnvMonEnableRedundantSupplyNotification")

            self.ciscoenvmonenableshutdownnotification = YLeaf(YType.boolean, "ciscoEnvMonEnableShutdownNotification")

            self.ciscoenvmonenablestatchangenotif = YLeaf(YType.boolean, "ciscoEnvMonEnableStatChangeNotif")

            self.ciscoenvmonenabletemperaturenotification = YLeaf(YType.boolean, "ciscoEnvMonEnableTemperatureNotification")

            self.ciscoenvmonenablevoltagenotification = YLeaf(YType.boolean, "ciscoEnvMonEnableVoltageNotification")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ciscoenvmonenablefannotification",
                            "ciscoenvmonenableredundantsupplynotification",
                            "ciscoenvmonenableshutdownnotification",
                            "ciscoenvmonenablestatchangenotif",
                            "ciscoenvmonenabletemperaturenotification",
                            "ciscoenvmonenablevoltagenotification") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoEnvmonMib.Ciscoenvmonmibnotificationenables, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEnvmonMib.Ciscoenvmonmibnotificationenables, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.ciscoenvmonenablefannotification.is_set or
                self.ciscoenvmonenableredundantsupplynotification.is_set or
                self.ciscoenvmonenableshutdownnotification.is_set or
                self.ciscoenvmonenablestatchangenotif.is_set or
                self.ciscoenvmonenabletemperaturenotification.is_set or
                self.ciscoenvmonenablevoltagenotification.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ciscoenvmonenablefannotification.yfilter != YFilter.not_set or
                self.ciscoenvmonenableredundantsupplynotification.yfilter != YFilter.not_set or
                self.ciscoenvmonenableshutdownnotification.yfilter != YFilter.not_set or
                self.ciscoenvmonenablestatchangenotif.yfilter != YFilter.not_set or
                self.ciscoenvmonenabletemperaturenotification.yfilter != YFilter.not_set or
                self.ciscoenvmonenablevoltagenotification.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoEnvMonMIBNotificationEnables" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ciscoenvmonenablefannotification.is_set or self.ciscoenvmonenablefannotification.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ciscoenvmonenablefannotification.get_name_leafdata())
            if (self.ciscoenvmonenableredundantsupplynotification.is_set or self.ciscoenvmonenableredundantsupplynotification.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ciscoenvmonenableredundantsupplynotification.get_name_leafdata())
            if (self.ciscoenvmonenableshutdownnotification.is_set or self.ciscoenvmonenableshutdownnotification.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ciscoenvmonenableshutdownnotification.get_name_leafdata())
            if (self.ciscoenvmonenablestatchangenotif.is_set or self.ciscoenvmonenablestatchangenotif.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ciscoenvmonenablestatchangenotif.get_name_leafdata())
            if (self.ciscoenvmonenabletemperaturenotification.is_set or self.ciscoenvmonenabletemperaturenotification.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ciscoenvmonenabletemperaturenotification.get_name_leafdata())
            if (self.ciscoenvmonenablevoltagenotification.is_set or self.ciscoenvmonenablevoltagenotification.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ciscoenvmonenablevoltagenotification.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ciscoEnvMonEnableFanNotification" or name == "ciscoEnvMonEnableRedundantSupplyNotification" or name == "ciscoEnvMonEnableShutdownNotification" or name == "ciscoEnvMonEnableStatChangeNotif" or name == "ciscoEnvMonEnableTemperatureNotification" or name == "ciscoEnvMonEnableVoltageNotification"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ciscoEnvMonEnableFanNotification"):
                self.ciscoenvmonenablefannotification = value
                self.ciscoenvmonenablefannotification.value_namespace = name_space
                self.ciscoenvmonenablefannotification.value_namespace_prefix = name_space_prefix
            if(value_path == "ciscoEnvMonEnableRedundantSupplyNotification"):
                self.ciscoenvmonenableredundantsupplynotification = value
                self.ciscoenvmonenableredundantsupplynotification.value_namespace = name_space
                self.ciscoenvmonenableredundantsupplynotification.value_namespace_prefix = name_space_prefix
            if(value_path == "ciscoEnvMonEnableShutdownNotification"):
                self.ciscoenvmonenableshutdownnotification = value
                self.ciscoenvmonenableshutdownnotification.value_namespace = name_space
                self.ciscoenvmonenableshutdownnotification.value_namespace_prefix = name_space_prefix
            if(value_path == "ciscoEnvMonEnableStatChangeNotif"):
                self.ciscoenvmonenablestatchangenotif = value
                self.ciscoenvmonenablestatchangenotif.value_namespace = name_space
                self.ciscoenvmonenablestatchangenotif.value_namespace_prefix = name_space_prefix
            if(value_path == "ciscoEnvMonEnableTemperatureNotification"):
                self.ciscoenvmonenabletemperaturenotification = value
                self.ciscoenvmonenabletemperaturenotification.value_namespace = name_space
                self.ciscoenvmonenabletemperaturenotification.value_namespace_prefix = name_space_prefix
            if(value_path == "ciscoEnvMonEnableVoltageNotification"):
                self.ciscoenvmonenablevoltagenotification = value
                self.ciscoenvmonenablevoltagenotification.value_namespace = name_space
                self.ciscoenvmonenablevoltagenotification.value_namespace_prefix = name_space_prefix


    class Ciscoenvmonvoltagestatustable(Entity):
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
            super(CiscoEnvmonMib.Ciscoenvmonvoltagestatustable, self).__init__()

            self.yang_name = "ciscoEnvMonVoltageStatusTable"
            self.yang_parent_name = "CISCO-ENVMON-MIB"

            self.ciscoenvmonvoltagestatusentry = YList(self)

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
                        super(CiscoEnvmonMib.Ciscoenvmonvoltagestatustable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEnvmonMib.Ciscoenvmonvoltagestatustable, self).__setattr__(name, value)


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
            	**type**\:   :py:class:`Ciscoenvmonstate <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.Ciscoenvmonstate>`
            
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
                super(CiscoEnvmonMib.Ciscoenvmonvoltagestatustable.Ciscoenvmonvoltagestatusentry, self).__init__()

                self.yang_name = "ciscoEnvMonVoltageStatusEntry"
                self.yang_parent_name = "ciscoEnvMonVoltageStatusTable"

                self.ciscoenvmonvoltagestatusindex = YLeaf(YType.int32, "ciscoEnvMonVoltageStatusIndex")

                self.ciscoenvmonvoltagelastshutdown = YLeaf(YType.int32, "ciscoEnvMonVoltageLastShutdown")

                self.ciscoenvmonvoltagestate = YLeaf(YType.enumeration, "ciscoEnvMonVoltageState")

                self.ciscoenvmonvoltagestatusdescr = YLeaf(YType.str, "ciscoEnvMonVoltageStatusDescr")

                self.ciscoenvmonvoltagestatusvalue = YLeaf(YType.int32, "ciscoEnvMonVoltageStatusValue")

                self.ciscoenvmonvoltagethresholdhigh = YLeaf(YType.int32, "ciscoEnvMonVoltageThresholdHigh")

                self.ciscoenvmonvoltagethresholdlow = YLeaf(YType.int32, "ciscoEnvMonVoltageThresholdLow")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciscoenvmonvoltagestatusindex",
                                "ciscoenvmonvoltagelastshutdown",
                                "ciscoenvmonvoltagestate",
                                "ciscoenvmonvoltagestatusdescr",
                                "ciscoenvmonvoltagestatusvalue",
                                "ciscoenvmonvoltagethresholdhigh",
                                "ciscoenvmonvoltagethresholdlow") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEnvmonMib.Ciscoenvmonvoltagestatustable.Ciscoenvmonvoltagestatusentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEnvmonMib.Ciscoenvmonvoltagestatustable.Ciscoenvmonvoltagestatusentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ciscoenvmonvoltagestatusindex.is_set or
                    self.ciscoenvmonvoltagelastshutdown.is_set or
                    self.ciscoenvmonvoltagestate.is_set or
                    self.ciscoenvmonvoltagestatusdescr.is_set or
                    self.ciscoenvmonvoltagestatusvalue.is_set or
                    self.ciscoenvmonvoltagethresholdhigh.is_set or
                    self.ciscoenvmonvoltagethresholdlow.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciscoenvmonvoltagestatusindex.yfilter != YFilter.not_set or
                    self.ciscoenvmonvoltagelastshutdown.yfilter != YFilter.not_set or
                    self.ciscoenvmonvoltagestate.yfilter != YFilter.not_set or
                    self.ciscoenvmonvoltagestatusdescr.yfilter != YFilter.not_set or
                    self.ciscoenvmonvoltagestatusvalue.yfilter != YFilter.not_set or
                    self.ciscoenvmonvoltagethresholdhigh.yfilter != YFilter.not_set or
                    self.ciscoenvmonvoltagethresholdlow.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ciscoEnvMonVoltageStatusEntry" + "[ciscoEnvMonVoltageStatusIndex='" + self.ciscoenvmonvoltagestatusindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/ciscoEnvMonVoltageStatusTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciscoenvmonvoltagestatusindex.is_set or self.ciscoenvmonvoltagestatusindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoenvmonvoltagestatusindex.get_name_leafdata())
                if (self.ciscoenvmonvoltagelastshutdown.is_set or self.ciscoenvmonvoltagelastshutdown.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoenvmonvoltagelastshutdown.get_name_leafdata())
                if (self.ciscoenvmonvoltagestate.is_set or self.ciscoenvmonvoltagestate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoenvmonvoltagestate.get_name_leafdata())
                if (self.ciscoenvmonvoltagestatusdescr.is_set or self.ciscoenvmonvoltagestatusdescr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoenvmonvoltagestatusdescr.get_name_leafdata())
                if (self.ciscoenvmonvoltagestatusvalue.is_set or self.ciscoenvmonvoltagestatusvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoenvmonvoltagestatusvalue.get_name_leafdata())
                if (self.ciscoenvmonvoltagethresholdhigh.is_set or self.ciscoenvmonvoltagethresholdhigh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoenvmonvoltagethresholdhigh.get_name_leafdata())
                if (self.ciscoenvmonvoltagethresholdlow.is_set or self.ciscoenvmonvoltagethresholdlow.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoenvmonvoltagethresholdlow.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ciscoEnvMonVoltageStatusIndex" or name == "ciscoEnvMonVoltageLastShutdown" or name == "ciscoEnvMonVoltageState" or name == "ciscoEnvMonVoltageStatusDescr" or name == "ciscoEnvMonVoltageStatusValue" or name == "ciscoEnvMonVoltageThresholdHigh" or name == "ciscoEnvMonVoltageThresholdLow"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ciscoEnvMonVoltageStatusIndex"):
                    self.ciscoenvmonvoltagestatusindex = value
                    self.ciscoenvmonvoltagestatusindex.value_namespace = name_space
                    self.ciscoenvmonvoltagestatusindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoEnvMonVoltageLastShutdown"):
                    self.ciscoenvmonvoltagelastshutdown = value
                    self.ciscoenvmonvoltagelastshutdown.value_namespace = name_space
                    self.ciscoenvmonvoltagelastshutdown.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoEnvMonVoltageState"):
                    self.ciscoenvmonvoltagestate = value
                    self.ciscoenvmonvoltagestate.value_namespace = name_space
                    self.ciscoenvmonvoltagestate.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoEnvMonVoltageStatusDescr"):
                    self.ciscoenvmonvoltagestatusdescr = value
                    self.ciscoenvmonvoltagestatusdescr.value_namespace = name_space
                    self.ciscoenvmonvoltagestatusdescr.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoEnvMonVoltageStatusValue"):
                    self.ciscoenvmonvoltagestatusvalue = value
                    self.ciscoenvmonvoltagestatusvalue.value_namespace = name_space
                    self.ciscoenvmonvoltagestatusvalue.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoEnvMonVoltageThresholdHigh"):
                    self.ciscoenvmonvoltagethresholdhigh = value
                    self.ciscoenvmonvoltagethresholdhigh.value_namespace = name_space
                    self.ciscoenvmonvoltagethresholdhigh.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoEnvMonVoltageThresholdLow"):
                    self.ciscoenvmonvoltagethresholdlow = value
                    self.ciscoenvmonvoltagethresholdlow.value_namespace = name_space
                    self.ciscoenvmonvoltagethresholdlow.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciscoenvmonvoltagestatusentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciscoenvmonvoltagestatusentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoEnvMonVoltageStatusTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ciscoEnvMonVoltageStatusEntry"):
                for c in self.ciscoenvmonvoltagestatusentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEnvmonMib.Ciscoenvmonvoltagestatustable.Ciscoenvmonvoltagestatusentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciscoenvmonvoltagestatusentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ciscoEnvMonVoltageStatusEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ciscoenvmontemperaturestatustable(Entity):
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
            super(CiscoEnvmonMib.Ciscoenvmontemperaturestatustable, self).__init__()

            self.yang_name = "ciscoEnvMonTemperatureStatusTable"
            self.yang_parent_name = "CISCO-ENVMON-MIB"

            self.ciscoenvmontemperaturestatusentry = YList(self)

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
                        super(CiscoEnvmonMib.Ciscoenvmontemperaturestatustable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEnvmonMib.Ciscoenvmontemperaturestatustable, self).__setattr__(name, value)


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
            	**type**\:   :py:class:`Ciscoenvmonstate <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.Ciscoenvmonstate>`
            
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
                super(CiscoEnvmonMib.Ciscoenvmontemperaturestatustable.Ciscoenvmontemperaturestatusentry, self).__init__()

                self.yang_name = "ciscoEnvMonTemperatureStatusEntry"
                self.yang_parent_name = "ciscoEnvMonTemperatureStatusTable"

                self.ciscoenvmontemperaturestatusindex = YLeaf(YType.int32, "ciscoEnvMonTemperatureStatusIndex")

                self.ciscoenvmontemperaturelastshutdown = YLeaf(YType.int32, "ciscoEnvMonTemperatureLastShutdown")

                self.ciscoenvmontemperaturestate = YLeaf(YType.enumeration, "ciscoEnvMonTemperatureState")

                self.ciscoenvmontemperaturestatusdescr = YLeaf(YType.str, "ciscoEnvMonTemperatureStatusDescr")

                self.ciscoenvmontemperaturestatusvalue = YLeaf(YType.uint32, "ciscoEnvMonTemperatureStatusValue")

                self.ciscoenvmontemperaturethreshold = YLeaf(YType.int32, "ciscoEnvMonTemperatureThreshold")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciscoenvmontemperaturestatusindex",
                                "ciscoenvmontemperaturelastshutdown",
                                "ciscoenvmontemperaturestate",
                                "ciscoenvmontemperaturestatusdescr",
                                "ciscoenvmontemperaturestatusvalue",
                                "ciscoenvmontemperaturethreshold") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEnvmonMib.Ciscoenvmontemperaturestatustable.Ciscoenvmontemperaturestatusentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEnvmonMib.Ciscoenvmontemperaturestatustable.Ciscoenvmontemperaturestatusentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ciscoenvmontemperaturestatusindex.is_set or
                    self.ciscoenvmontemperaturelastshutdown.is_set or
                    self.ciscoenvmontemperaturestate.is_set or
                    self.ciscoenvmontemperaturestatusdescr.is_set or
                    self.ciscoenvmontemperaturestatusvalue.is_set or
                    self.ciscoenvmontemperaturethreshold.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciscoenvmontemperaturestatusindex.yfilter != YFilter.not_set or
                    self.ciscoenvmontemperaturelastshutdown.yfilter != YFilter.not_set or
                    self.ciscoenvmontemperaturestate.yfilter != YFilter.not_set or
                    self.ciscoenvmontemperaturestatusdescr.yfilter != YFilter.not_set or
                    self.ciscoenvmontemperaturestatusvalue.yfilter != YFilter.not_set or
                    self.ciscoenvmontemperaturethreshold.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ciscoEnvMonTemperatureStatusEntry" + "[ciscoEnvMonTemperatureStatusIndex='" + self.ciscoenvmontemperaturestatusindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/ciscoEnvMonTemperatureStatusTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciscoenvmontemperaturestatusindex.is_set or self.ciscoenvmontemperaturestatusindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoenvmontemperaturestatusindex.get_name_leafdata())
                if (self.ciscoenvmontemperaturelastshutdown.is_set or self.ciscoenvmontemperaturelastshutdown.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoenvmontemperaturelastshutdown.get_name_leafdata())
                if (self.ciscoenvmontemperaturestate.is_set or self.ciscoenvmontemperaturestate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoenvmontemperaturestate.get_name_leafdata())
                if (self.ciscoenvmontemperaturestatusdescr.is_set or self.ciscoenvmontemperaturestatusdescr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoenvmontemperaturestatusdescr.get_name_leafdata())
                if (self.ciscoenvmontemperaturestatusvalue.is_set or self.ciscoenvmontemperaturestatusvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoenvmontemperaturestatusvalue.get_name_leafdata())
                if (self.ciscoenvmontemperaturethreshold.is_set or self.ciscoenvmontemperaturethreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoenvmontemperaturethreshold.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ciscoEnvMonTemperatureStatusIndex" or name == "ciscoEnvMonTemperatureLastShutdown" or name == "ciscoEnvMonTemperatureState" or name == "ciscoEnvMonTemperatureStatusDescr" or name == "ciscoEnvMonTemperatureStatusValue" or name == "ciscoEnvMonTemperatureThreshold"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ciscoEnvMonTemperatureStatusIndex"):
                    self.ciscoenvmontemperaturestatusindex = value
                    self.ciscoenvmontemperaturestatusindex.value_namespace = name_space
                    self.ciscoenvmontemperaturestatusindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoEnvMonTemperatureLastShutdown"):
                    self.ciscoenvmontemperaturelastshutdown = value
                    self.ciscoenvmontemperaturelastshutdown.value_namespace = name_space
                    self.ciscoenvmontemperaturelastshutdown.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoEnvMonTemperatureState"):
                    self.ciscoenvmontemperaturestate = value
                    self.ciscoenvmontemperaturestate.value_namespace = name_space
                    self.ciscoenvmontemperaturestate.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoEnvMonTemperatureStatusDescr"):
                    self.ciscoenvmontemperaturestatusdescr = value
                    self.ciscoenvmontemperaturestatusdescr.value_namespace = name_space
                    self.ciscoenvmontemperaturestatusdescr.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoEnvMonTemperatureStatusValue"):
                    self.ciscoenvmontemperaturestatusvalue = value
                    self.ciscoenvmontemperaturestatusvalue.value_namespace = name_space
                    self.ciscoenvmontemperaturestatusvalue.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoEnvMonTemperatureThreshold"):
                    self.ciscoenvmontemperaturethreshold = value
                    self.ciscoenvmontemperaturethreshold.value_namespace = name_space
                    self.ciscoenvmontemperaturethreshold.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciscoenvmontemperaturestatusentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciscoenvmontemperaturestatusentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoEnvMonTemperatureStatusTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ciscoEnvMonTemperatureStatusEntry"):
                for c in self.ciscoenvmontemperaturestatusentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEnvmonMib.Ciscoenvmontemperaturestatustable.Ciscoenvmontemperaturestatusentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciscoenvmontemperaturestatusentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ciscoEnvMonTemperatureStatusEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ciscoenvmonfanstatustable(Entity):
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
            super(CiscoEnvmonMib.Ciscoenvmonfanstatustable, self).__init__()

            self.yang_name = "ciscoEnvMonFanStatusTable"
            self.yang_parent_name = "CISCO-ENVMON-MIB"

            self.ciscoenvmonfanstatusentry = YList(self)

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
                        super(CiscoEnvmonMib.Ciscoenvmonfanstatustable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEnvmonMib.Ciscoenvmonfanstatustable, self).__setattr__(name, value)


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
            	**type**\:   :py:class:`Ciscoenvmonstate <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.Ciscoenvmonstate>`
            
            .. attribute:: ciscoenvmonfanstatusdescr
            
            	Textual description of the fan being instrumented. This description is a short textual label, suitable as a human\-sensible identification for the rest of the information in the entry
            	**type**\:  str
            
            	**length:** 0..32
            
            

            """

            _prefix = 'CISCO-ENVMON-MIB'
            _revision = '2003-12-01'

            def __init__(self):
                super(CiscoEnvmonMib.Ciscoenvmonfanstatustable.Ciscoenvmonfanstatusentry, self).__init__()

                self.yang_name = "ciscoEnvMonFanStatusEntry"
                self.yang_parent_name = "ciscoEnvMonFanStatusTable"

                self.ciscoenvmonfanstatusindex = YLeaf(YType.int32, "ciscoEnvMonFanStatusIndex")

                self.ciscoenvmonfanstate = YLeaf(YType.enumeration, "ciscoEnvMonFanState")

                self.ciscoenvmonfanstatusdescr = YLeaf(YType.str, "ciscoEnvMonFanStatusDescr")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciscoenvmonfanstatusindex",
                                "ciscoenvmonfanstate",
                                "ciscoenvmonfanstatusdescr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEnvmonMib.Ciscoenvmonfanstatustable.Ciscoenvmonfanstatusentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEnvmonMib.Ciscoenvmonfanstatustable.Ciscoenvmonfanstatusentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ciscoenvmonfanstatusindex.is_set or
                    self.ciscoenvmonfanstate.is_set or
                    self.ciscoenvmonfanstatusdescr.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciscoenvmonfanstatusindex.yfilter != YFilter.not_set or
                    self.ciscoenvmonfanstate.yfilter != YFilter.not_set or
                    self.ciscoenvmonfanstatusdescr.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ciscoEnvMonFanStatusEntry" + "[ciscoEnvMonFanStatusIndex='" + self.ciscoenvmonfanstatusindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/ciscoEnvMonFanStatusTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciscoenvmonfanstatusindex.is_set or self.ciscoenvmonfanstatusindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoenvmonfanstatusindex.get_name_leafdata())
                if (self.ciscoenvmonfanstate.is_set or self.ciscoenvmonfanstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoenvmonfanstate.get_name_leafdata())
                if (self.ciscoenvmonfanstatusdescr.is_set or self.ciscoenvmonfanstatusdescr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoenvmonfanstatusdescr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ciscoEnvMonFanStatusIndex" or name == "ciscoEnvMonFanState" or name == "ciscoEnvMonFanStatusDescr"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ciscoEnvMonFanStatusIndex"):
                    self.ciscoenvmonfanstatusindex = value
                    self.ciscoenvmonfanstatusindex.value_namespace = name_space
                    self.ciscoenvmonfanstatusindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoEnvMonFanState"):
                    self.ciscoenvmonfanstate = value
                    self.ciscoenvmonfanstate.value_namespace = name_space
                    self.ciscoenvmonfanstate.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoEnvMonFanStatusDescr"):
                    self.ciscoenvmonfanstatusdescr = value
                    self.ciscoenvmonfanstatusdescr.value_namespace = name_space
                    self.ciscoenvmonfanstatusdescr.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciscoenvmonfanstatusentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciscoenvmonfanstatusentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoEnvMonFanStatusTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ciscoEnvMonFanStatusEntry"):
                for c in self.ciscoenvmonfanstatusentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEnvmonMib.Ciscoenvmonfanstatustable.Ciscoenvmonfanstatusentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciscoenvmonfanstatusentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ciscoEnvMonFanStatusEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ciscoenvmonsupplystatustable(Entity):
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
            super(CiscoEnvmonMib.Ciscoenvmonsupplystatustable, self).__init__()

            self.yang_name = "ciscoEnvMonSupplyStatusTable"
            self.yang_parent_name = "CISCO-ENVMON-MIB"

            self.ciscoenvmonsupplystatusentry = YList(self)

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
                        super(CiscoEnvmonMib.Ciscoenvmonsupplystatustable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEnvmonMib.Ciscoenvmonsupplystatustable, self).__setattr__(name, value)


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
            	**type**\:   :py:class:`Ciscoenvmonsupplysource <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.CiscoEnvmonMib.Ciscoenvmonsupplystatustable.Ciscoenvmonsupplystatusentry.Ciscoenvmonsupplysource>`
            
            .. attribute:: ciscoenvmonsupplystate
            
            	The current state of the power supply being instrumented
            	**type**\:   :py:class:`Ciscoenvmonstate <ydk.models.cisco_ios_xe.CISCO_ENVMON_MIB.Ciscoenvmonstate>`
            
            .. attribute:: ciscoenvmonsupplystatusdescr
            
            	Textual description of the power supply being instrumented. This description is a short textual label, suitable as a human\-sensible identification for the rest of the information in the entry
            	**type**\:  str
            
            	**length:** 0..64
            
            

            """

            _prefix = 'CISCO-ENVMON-MIB'
            _revision = '2003-12-01'

            def __init__(self):
                super(CiscoEnvmonMib.Ciscoenvmonsupplystatustable.Ciscoenvmonsupplystatusentry, self).__init__()

                self.yang_name = "ciscoEnvMonSupplyStatusEntry"
                self.yang_parent_name = "ciscoEnvMonSupplyStatusTable"

                self.ciscoenvmonsupplystatusindex = YLeaf(YType.int32, "ciscoEnvMonSupplyStatusIndex")

                self.ciscoenvmonsupplysource = YLeaf(YType.enumeration, "ciscoEnvMonSupplySource")

                self.ciscoenvmonsupplystate = YLeaf(YType.enumeration, "ciscoEnvMonSupplyState")

                self.ciscoenvmonsupplystatusdescr = YLeaf(YType.str, "ciscoEnvMonSupplyStatusDescr")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciscoenvmonsupplystatusindex",
                                "ciscoenvmonsupplysource",
                                "ciscoenvmonsupplystate",
                                "ciscoenvmonsupplystatusdescr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEnvmonMib.Ciscoenvmonsupplystatustable.Ciscoenvmonsupplystatusentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEnvmonMib.Ciscoenvmonsupplystatustable.Ciscoenvmonsupplystatusentry, self).__setattr__(name, value)

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


            def has_data(self):
                return (
                    self.ciscoenvmonsupplystatusindex.is_set or
                    self.ciscoenvmonsupplysource.is_set or
                    self.ciscoenvmonsupplystate.is_set or
                    self.ciscoenvmonsupplystatusdescr.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciscoenvmonsupplystatusindex.yfilter != YFilter.not_set or
                    self.ciscoenvmonsupplysource.yfilter != YFilter.not_set or
                    self.ciscoenvmonsupplystate.yfilter != YFilter.not_set or
                    self.ciscoenvmonsupplystatusdescr.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ciscoEnvMonSupplyStatusEntry" + "[ciscoEnvMonSupplyStatusIndex='" + self.ciscoenvmonsupplystatusindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/ciscoEnvMonSupplyStatusTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciscoenvmonsupplystatusindex.is_set or self.ciscoenvmonsupplystatusindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoenvmonsupplystatusindex.get_name_leafdata())
                if (self.ciscoenvmonsupplysource.is_set or self.ciscoenvmonsupplysource.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoenvmonsupplysource.get_name_leafdata())
                if (self.ciscoenvmonsupplystate.is_set or self.ciscoenvmonsupplystate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoenvmonsupplystate.get_name_leafdata())
                if (self.ciscoenvmonsupplystatusdescr.is_set or self.ciscoenvmonsupplystatusdescr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoenvmonsupplystatusdescr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ciscoEnvMonSupplyStatusIndex" or name == "ciscoEnvMonSupplySource" or name == "ciscoEnvMonSupplyState" or name == "ciscoEnvMonSupplyStatusDescr"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ciscoEnvMonSupplyStatusIndex"):
                    self.ciscoenvmonsupplystatusindex = value
                    self.ciscoenvmonsupplystatusindex.value_namespace = name_space
                    self.ciscoenvmonsupplystatusindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoEnvMonSupplySource"):
                    self.ciscoenvmonsupplysource = value
                    self.ciscoenvmonsupplysource.value_namespace = name_space
                    self.ciscoenvmonsupplysource.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoEnvMonSupplyState"):
                    self.ciscoenvmonsupplystate = value
                    self.ciscoenvmonsupplystate.value_namespace = name_space
                    self.ciscoenvmonsupplystate.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoEnvMonSupplyStatusDescr"):
                    self.ciscoenvmonsupplystatusdescr = value
                    self.ciscoenvmonsupplystatusdescr.value_namespace = name_space
                    self.ciscoenvmonsupplystatusdescr.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciscoenvmonsupplystatusentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciscoenvmonsupplystatusentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoEnvMonSupplyStatusTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ciscoEnvMonSupplyStatusEntry"):
                for c in self.ciscoenvmonsupplystatusentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEnvmonMib.Ciscoenvmonsupplystatustable.Ciscoenvmonsupplystatusentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciscoenvmonsupplystatusentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ciscoEnvMonSupplyStatusEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.ciscoenvmonfanstatustable is not None and self.ciscoenvmonfanstatustable.has_data()) or
            (self.ciscoenvmonmibnotificationenables is not None and self.ciscoenvmonmibnotificationenables.has_data()) or
            (self.ciscoenvmonobjects is not None and self.ciscoenvmonobjects.has_data()) or
            (self.ciscoenvmonsupplystatustable is not None and self.ciscoenvmonsupplystatustable.has_data()) or
            (self.ciscoenvmontemperaturestatustable is not None and self.ciscoenvmontemperaturestatustable.has_data()) or
            (self.ciscoenvmonvoltagestatustable is not None and self.ciscoenvmonvoltagestatustable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ciscoenvmonfanstatustable is not None and self.ciscoenvmonfanstatustable.has_operation()) or
            (self.ciscoenvmonmibnotificationenables is not None and self.ciscoenvmonmibnotificationenables.has_operation()) or
            (self.ciscoenvmonobjects is not None and self.ciscoenvmonobjects.has_operation()) or
            (self.ciscoenvmonsupplystatustable is not None and self.ciscoenvmonsupplystatustable.has_operation()) or
            (self.ciscoenvmontemperaturestatustable is not None and self.ciscoenvmontemperaturestatustable.has_operation()) or
            (self.ciscoenvmonvoltagestatustable is not None and self.ciscoenvmonvoltagestatustable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-ENVMON-MIB:CISCO-ENVMON-MIB" + path_buffer

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

        if (child_yang_name == "ciscoEnvMonFanStatusTable"):
            if (self.ciscoenvmonfanstatustable is None):
                self.ciscoenvmonfanstatustable = CiscoEnvmonMib.Ciscoenvmonfanstatustable()
                self.ciscoenvmonfanstatustable.parent = self
                self._children_name_map["ciscoenvmonfanstatustable"] = "ciscoEnvMonFanStatusTable"
            return self.ciscoenvmonfanstatustable

        if (child_yang_name == "ciscoEnvMonMIBNotificationEnables"):
            if (self.ciscoenvmonmibnotificationenables is None):
                self.ciscoenvmonmibnotificationenables = CiscoEnvmonMib.Ciscoenvmonmibnotificationenables()
                self.ciscoenvmonmibnotificationenables.parent = self
                self._children_name_map["ciscoenvmonmibnotificationenables"] = "ciscoEnvMonMIBNotificationEnables"
            return self.ciscoenvmonmibnotificationenables

        if (child_yang_name == "ciscoEnvMonObjects"):
            if (self.ciscoenvmonobjects is None):
                self.ciscoenvmonobjects = CiscoEnvmonMib.Ciscoenvmonobjects()
                self.ciscoenvmonobjects.parent = self
                self._children_name_map["ciscoenvmonobjects"] = "ciscoEnvMonObjects"
            return self.ciscoenvmonobjects

        if (child_yang_name == "ciscoEnvMonSupplyStatusTable"):
            if (self.ciscoenvmonsupplystatustable is None):
                self.ciscoenvmonsupplystatustable = CiscoEnvmonMib.Ciscoenvmonsupplystatustable()
                self.ciscoenvmonsupplystatustable.parent = self
                self._children_name_map["ciscoenvmonsupplystatustable"] = "ciscoEnvMonSupplyStatusTable"
            return self.ciscoenvmonsupplystatustable

        if (child_yang_name == "ciscoEnvMonTemperatureStatusTable"):
            if (self.ciscoenvmontemperaturestatustable is None):
                self.ciscoenvmontemperaturestatustable = CiscoEnvmonMib.Ciscoenvmontemperaturestatustable()
                self.ciscoenvmontemperaturestatustable.parent = self
                self._children_name_map["ciscoenvmontemperaturestatustable"] = "ciscoEnvMonTemperatureStatusTable"
            return self.ciscoenvmontemperaturestatustable

        if (child_yang_name == "ciscoEnvMonVoltageStatusTable"):
            if (self.ciscoenvmonvoltagestatustable is None):
                self.ciscoenvmonvoltagestatustable = CiscoEnvmonMib.Ciscoenvmonvoltagestatustable()
                self.ciscoenvmonvoltagestatustable.parent = self
                self._children_name_map["ciscoenvmonvoltagestatustable"] = "ciscoEnvMonVoltageStatusTable"
            return self.ciscoenvmonvoltagestatustable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ciscoEnvMonFanStatusTable" or name == "ciscoEnvMonMIBNotificationEnables" or name == "ciscoEnvMonObjects" or name == "ciscoEnvMonSupplyStatusTable" or name == "ciscoEnvMonTemperatureStatusTable" or name == "ciscoEnvMonVoltageStatusTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoEnvmonMib()
        return self._top_entity


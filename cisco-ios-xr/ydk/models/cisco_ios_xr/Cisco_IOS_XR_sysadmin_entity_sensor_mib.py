""" Cisco_IOS_XR_sysadmin_entity_sensor_mib 

This module contains definitions
for the Calvados model objects.

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

Copyright(c) 2015\-2017 by Cisco Systems, Inc.
All rights reserved.

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SensorDataScale(Enum):
    """
    SensorDataScale (Enum Class)

    .. data:: yocto = 1

    .. data:: zepto = 2

    .. data:: atto = 3

    .. data:: femto = 4

    .. data:: pico = 5

    .. data:: nano = 6

    .. data:: micro = 7

    .. data:: milli = 8

    .. data:: units = 9

    .. data:: kilo = 10

    .. data:: mega = 11

    .. data:: giga = 12

    .. data:: tera = 13

    .. data:: exa = 14

    .. data:: peta = 15

    .. data:: zetta = 16

    .. data:: yotta = 17

    """

    yocto = Enum.YLeaf(1, "yocto")

    zepto = Enum.YLeaf(2, "zepto")

    atto = Enum.YLeaf(3, "atto")

    femto = Enum.YLeaf(4, "femto")

    pico = Enum.YLeaf(5, "pico")

    nano = Enum.YLeaf(6, "nano")

    micro = Enum.YLeaf(7, "micro")

    milli = Enum.YLeaf(8, "milli")

    units = Enum.YLeaf(9, "units")

    kilo = Enum.YLeaf(10, "kilo")

    mega = Enum.YLeaf(11, "mega")

    giga = Enum.YLeaf(12, "giga")

    tera = Enum.YLeaf(13, "tera")

    exa = Enum.YLeaf(14, "exa")

    peta = Enum.YLeaf(15, "peta")

    zetta = Enum.YLeaf(16, "zetta")

    yotta = Enum.YLeaf(17, "yotta")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_sensor_mib as meta
        return meta._meta_table['SensorDataScale']


class SensorDataType(Enum):
    """
    SensorDataType (Enum Class)

    .. data:: other = 1

    .. data:: unknown = 2

    .. data:: voltsAC = 3

    .. data:: voltsDC = 4

    .. data:: amperes = 5

    .. data:: watts = 6

    .. data:: hertz = 7

    .. data:: celsius = 8

    .. data:: percentRH = 9

    .. data:: rpm = 10

    .. data:: cmm = 11

    .. data:: truthvalue = 12

    .. data:: specialEnum = 13

    """

    other = Enum.YLeaf(1, "other")

    unknown = Enum.YLeaf(2, "unknown")

    voltsAC = Enum.YLeaf(3, "voltsAC")

    voltsDC = Enum.YLeaf(4, "voltsDC")

    amperes = Enum.YLeaf(5, "amperes")

    watts = Enum.YLeaf(6, "watts")

    hertz = Enum.YLeaf(7, "hertz")

    celsius = Enum.YLeaf(8, "celsius")

    percentRH = Enum.YLeaf(9, "percentRH")

    rpm = Enum.YLeaf(10, "rpm")

    cmm = Enum.YLeaf(11, "cmm")

    truthvalue = Enum.YLeaf(12, "truthvalue")

    specialEnum = Enum.YLeaf(13, "specialEnum")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_sensor_mib as meta
        return meta._meta_table['SensorDataType']


class SensorStatus(Enum):
    """
    SensorStatus (Enum Class)

    .. data:: ok = 1

    .. data:: unavailable = 2

    .. data:: nonoperational = 3

    """

    ok = Enum.YLeaf(1, "ok")

    unavailable = Enum.YLeaf(2, "unavailable")

    nonoperational = Enum.YLeaf(3, "nonoperational")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_sensor_mib as meta
        return meta._meta_table['SensorStatus']


class SensorThresholdRelation(Enum):
    """
    SensorThresholdRelation (Enum Class)

    .. data:: lessThan = 1

    .. data:: lessOrEqual = 2

    .. data:: greaterThan = 3

    .. data:: greaterOrEqual = 4

    .. data:: equalTo = 5

    .. data:: notEqualTo = 6

    """

    lessThan = Enum.YLeaf(1, "lessThan")

    lessOrEqual = Enum.YLeaf(2, "lessOrEqual")

    greaterThan = Enum.YLeaf(3, "greaterThan")

    greaterOrEqual = Enum.YLeaf(4, "greaterOrEqual")

    equalTo = Enum.YLeaf(5, "equalTo")

    notEqualTo = Enum.YLeaf(6, "notEqualTo")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_sensor_mib as meta
        return meta._meta_table['SensorThresholdRelation']


class SensorThresholdSeverity(Enum):
    """
    SensorThresholdSeverity (Enum Class)

    .. data:: other = 1

    .. data:: minor = 10

    .. data:: major = 20

    .. data:: critical = 30

    """

    other = Enum.YLeaf(1, "other")

    minor = Enum.YLeaf(10, "minor")

    major = Enum.YLeaf(20, "major")

    critical = Enum.YLeaf(30, "critical")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_sensor_mib as meta
        return meta._meta_table['SensorThresholdSeverity']



class CISCOENTITYSENSORMIB(_Entity_):
    """
    
    
    .. attribute:: entsensorvaluetable
    
    	
    	**type**\:  :py:class:`EntSensorValueTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_sensor_mib.CISCOENTITYSENSORMIB.EntSensorValueTable>`
    
    	**config**\: False
    
    .. attribute:: entsensorthresholdtable
    
    	
    	**type**\:  :py:class:`EntSensorThresholdTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_sensor_mib.CISCOENTITYSENSORMIB.EntSensorThresholdTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO_ENTITY_SENSOR_MIB'
    _revision = '2017-04-12'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(CISCOENTITYSENSORMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-ENTITY-SENSOR-MIB"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-entity-sensor-mib"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("entSensorValueTable", ("entsensorvaluetable", CISCOENTITYSENSORMIB.EntSensorValueTable)), ("entSensorThresholdTable", ("entsensorthresholdtable", CISCOENTITYSENSORMIB.EntSensorThresholdTable))])
        self._leafs = OrderedDict()

        self.entsensorvaluetable = CISCOENTITYSENSORMIB.EntSensorValueTable()
        self.entsensorvaluetable.parent = self
        self._children_name_map["entsensorvaluetable"] = "entSensorValueTable"

        self.entsensorthresholdtable = CISCOENTITYSENSORMIB.EntSensorThresholdTable()
        self.entsensorthresholdtable.parent = self
        self._children_name_map["entsensorthresholdtable"] = "entSensorThresholdTable"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-entity-sensor-mib:CISCO-ENTITY-SENSOR-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOENTITYSENSORMIB, [], name, value)


    class EntSensorValueTable(_Entity_):
        """
        
        
        .. attribute:: entsensorvalueentry
        
        	
        	**type**\: list of  		 :py:class:`EntSensorValueEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_sensor_mib.CISCOENTITYSENSORMIB.EntSensorValueTable.EntSensorValueEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO_ENTITY_SENSOR_MIB'
        _revision = '2017-04-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(CISCOENTITYSENSORMIB.EntSensorValueTable, self).__init__()

            self.yang_name = "entSensorValueTable"
            self.yang_parent_name = "CISCO-ENTITY-SENSOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("entSensorValueEntry", ("entsensorvalueentry", CISCOENTITYSENSORMIB.EntSensorValueTable.EntSensorValueEntry))])
            self._leafs = OrderedDict()

            self.entsensorvalueentry = YList(self)
            self._segment_path = lambda: "entSensorValueTable"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-sensor-mib:CISCO-ENTITY-SENSOR-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYSENSORMIB.EntSensorValueTable, [], name, value)


        class EntSensorValueEntry(_Entity_):
            """
            
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: entsensortype
            
            	
            	**type**\:  :py:class:`SensorDataType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_sensor_mib.SensorDataType>`
            
            	**config**\: False
            
            .. attribute:: entsensorscale
            
            	
            	**type**\:  :py:class:`SensorDataScale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_sensor_mib.SensorDataScale>`
            
            	**config**\: False
            
            .. attribute:: entsensorprecision
            
            	
            	**type**\: int
            
            	**range:** \-8..9
            
            	**config**\: False
            
            .. attribute:: entsensorvalue
            
            	
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            	**config**\: False
            
            .. attribute:: entsensorstatus
            
            	
            	**type**\:  :py:class:`SensorStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_sensor_mib.SensorStatus>`
            
            	**config**\: False
            
            .. attribute:: entsensorvaluetimestamp
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: entsensorvalueupdaterate
            
            	
            	**type**\: int
            
            	**range:** 0..999999999
            
            	**config**\: False
            
            .. attribute:: entsensormeasuredentity
            
            	
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO_ENTITY_SENSOR_MIB'
            _revision = '2017-04-12'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(CISCOENTITYSENSORMIB.EntSensorValueTable.EntSensorValueEntry, self).__init__()

                self.yang_name = "entSensorValueEntry"
                self.yang_parent_name = "entSensorValueTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.int32, 'entPhysicalIndex'), ['int'])),
                    ('entsensortype', (YLeaf(YType.enumeration, 'entSensorType'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_sensor_mib', 'SensorDataType', '')])),
                    ('entsensorscale', (YLeaf(YType.enumeration, 'entSensorScale'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_sensor_mib', 'SensorDataScale', '')])),
                    ('entsensorprecision', (YLeaf(YType.int32, 'entSensorPrecision'), ['int'])),
                    ('entsensorvalue', (YLeaf(YType.int32, 'entSensorValue'), ['int'])),
                    ('entsensorstatus', (YLeaf(YType.enumeration, 'entSensorStatus'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_sensor_mib', 'SensorStatus', '')])),
                    ('entsensorvaluetimestamp', (YLeaf(YType.uint32, 'entSensorValueTimeStamp'), ['int'])),
                    ('entsensorvalueupdaterate', (YLeaf(YType.int32, 'entSensorValueUpdateRate'), ['int'])),
                    ('entsensormeasuredentity', (YLeaf(YType.int32, 'entSensorMeasuredEntity'), ['int'])),
                ])
                self.entphysicalindex = None
                self.entsensortype = None
                self.entsensorscale = None
                self.entsensorprecision = None
                self.entsensorvalue = None
                self.entsensorstatus = None
                self.entsensorvaluetimestamp = None
                self.entsensorvalueupdaterate = None
                self.entsensormeasuredentity = None
                self._segment_path = lambda: "entSensorValueEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-sensor-mib:CISCO-ENTITY-SENSOR-MIB/entSensorValueTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYSENSORMIB.EntSensorValueTable.EntSensorValueEntry, ['entphysicalindex', 'entsensortype', 'entsensorscale', 'entsensorprecision', 'entsensorvalue', 'entsensorstatus', 'entsensorvaluetimestamp', 'entsensorvalueupdaterate', 'entsensormeasuredentity'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_sensor_mib as meta
                return meta._meta_table['CISCOENTITYSENSORMIB.EntSensorValueTable.EntSensorValueEntry']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_sensor_mib as meta
            return meta._meta_table['CISCOENTITYSENSORMIB.EntSensorValueTable']['meta_info']


    class EntSensorThresholdTable(_Entity_):
        """
        
        
        .. attribute:: entsensorthresholdentry
        
        	
        	**type**\: list of  		 :py:class:`EntSensorThresholdEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_sensor_mib.CISCOENTITYSENSORMIB.EntSensorThresholdTable.EntSensorThresholdEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO_ENTITY_SENSOR_MIB'
        _revision = '2017-04-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(CISCOENTITYSENSORMIB.EntSensorThresholdTable, self).__init__()

            self.yang_name = "entSensorThresholdTable"
            self.yang_parent_name = "CISCO-ENTITY-SENSOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("entSensorThresholdEntry", ("entsensorthresholdentry", CISCOENTITYSENSORMIB.EntSensorThresholdTable.EntSensorThresholdEntry))])
            self._leafs = OrderedDict()

            self.entsensorthresholdentry = YList(self)
            self._segment_path = lambda: "entSensorThresholdTable"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-sensor-mib:CISCO-ENTITY-SENSOR-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYSENSORMIB.EntSensorThresholdTable, [], name, value)


        class EntSensorThresholdEntry(_Entity_):
            """
            
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: entsensorthresholdindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..99999999
            
            	**config**\: False
            
            .. attribute:: entsensorthresholdseverity
            
            	
            	**type**\:  :py:class:`SensorThresholdSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_sensor_mib.SensorThresholdSeverity>`
            
            	**config**\: False
            
            .. attribute:: entsensorthresholdrelation
            
            	
            	**type**\:  :py:class:`SensorThresholdRelation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_sensor_mib.SensorThresholdRelation>`
            
            	**config**\: False
            
            .. attribute:: entsensorthresholdvalue
            
            	
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            	**config**\: False
            
            .. attribute:: entsensorthresholdevaluation
            
            	
            	**type**\:  :py:class:`TruthValue <ydk.models.cisco_ios_xr.SNMPv2_TC.TruthValue>`
            
            	**config**\: False
            
            .. attribute:: entsensorthresholdnotificationenable
            
            	
            	**type**\:  :py:class:`TruthValue <ydk.models.cisco_ios_xr.SNMPv2_TC.TruthValue>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO_ENTITY_SENSOR_MIB'
            _revision = '2017-04-12'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(CISCOENTITYSENSORMIB.EntSensorThresholdTable.EntSensorThresholdEntry, self).__init__()

                self.yang_name = "entSensorThresholdEntry"
                self.yang_parent_name = "entSensorThresholdTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','entsensorthresholdindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.int32, 'entPhysicalIndex'), ['int'])),
                    ('entsensorthresholdindex', (YLeaf(YType.int32, 'entSensorThresholdIndex'), ['int'])),
                    ('entsensorthresholdseverity', (YLeaf(YType.enumeration, 'entSensorThresholdSeverity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_sensor_mib', 'SensorThresholdSeverity', '')])),
                    ('entsensorthresholdrelation', (YLeaf(YType.enumeration, 'entSensorThresholdRelation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_entity_sensor_mib', 'SensorThresholdRelation', '')])),
                    ('entsensorthresholdvalue', (YLeaf(YType.int32, 'entSensorThresholdValue'), ['int'])),
                    ('entsensorthresholdevaluation', (YLeaf(YType.enumeration, 'entSensorThresholdEvaluation'), [('ydk.models.cisco_ios_xr.SNMPv2_TC', 'TruthValue', '')])),
                    ('entsensorthresholdnotificationenable', (YLeaf(YType.enumeration, 'entSensorThresholdNotificationEnable'), [('ydk.models.cisco_ios_xr.SNMPv2_TC', 'TruthValue', '')])),
                ])
                self.entphysicalindex = None
                self.entsensorthresholdindex = None
                self.entsensorthresholdseverity = None
                self.entsensorthresholdrelation = None
                self.entsensorthresholdvalue = None
                self.entsensorthresholdevaluation = None
                self.entsensorthresholdnotificationenable = None
                self._segment_path = lambda: "entSensorThresholdEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[entSensorThresholdIndex='" + str(self.entsensorthresholdindex) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-entity-sensor-mib:CISCO-ENTITY-SENSOR-MIB/entSensorThresholdTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYSENSORMIB.EntSensorThresholdTable.EntSensorThresholdEntry, ['entphysicalindex', 'entsensorthresholdindex', 'entsensorthresholdseverity', 'entsensorthresholdrelation', 'entsensorthresholdvalue', 'entsensorthresholdevaluation', 'entsensorthresholdnotificationenable'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_sensor_mib as meta
                return meta._meta_table['CISCOENTITYSENSORMIB.EntSensorThresholdTable.EntSensorThresholdEntry']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_sensor_mib as meta
            return meta._meta_table['CISCOENTITYSENSORMIB.EntSensorThresholdTable']['meta_info']

    def clone_ptr(self):
        self._top_entity = CISCOENTITYSENSORMIB()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_sensor_mib as meta
        return meta._meta_table['CISCOENTITYSENSORMIB']['meta_info']



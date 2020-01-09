""" CISCO_ENTITY_FRU_CONTROL_MIB 

This module contains definitions
for the Calvados model objects.

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



class CefcFanTrayOperStatusType(Enum):
    """
    CefcFanTrayOperStatusType (Enum Class)

    .. data:: unknown = 1

    .. data:: up = 2

    .. data:: down = 3

    .. data:: warning = 4

    """

    unknown = Enum.YLeaf(1, "unknown")

    up = Enum.YLeaf(2, "up")

    down = Enum.YLeaf(3, "down")

    warning = Enum.YLeaf(4, "warning")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
        return meta._meta_table['CefcFanTrayOperStatusType']


class CefcPhysicalStatusType(Enum):
    """
    CefcPhysicalStatusType (Enum Class)

    .. data:: other = 1

    .. data:: supported = 2

    .. data:: unsupported = 3

    .. data:: incompatible = 4

    """

    other = Enum.YLeaf(1, "other")

    supported = Enum.YLeaf(2, "supported")

    unsupported = Enum.YLeaf(3, "unsupported")

    incompatible = Enum.YLeaf(4, "incompatible")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
        return meta._meta_table['CefcPhysicalStatusType']


class ModuleAdminType(Enum):
    """
    ModuleAdminType (Enum Class)

    .. data:: enabled = 1

    .. data:: disabled = 2

    .. data:: reset = 3

    .. data:: outOfServiceAdmin = 4

    """

    enabled = Enum.YLeaf(1, "enabled")

    disabled = Enum.YLeaf(2, "disabled")

    reset = Enum.YLeaf(3, "reset")

    outOfServiceAdmin = Enum.YLeaf(4, "outOfServiceAdmin")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
        return meta._meta_table['ModuleAdminType']


class ModuleOperType(Enum):
    """
    ModuleOperType (Enum Class)

    .. data:: unknown = 1

    .. data:: ok = 2

    .. data:: disabled = 3

    .. data:: okButDiagFailed = 4

    .. data:: boot = 5

    .. data:: selfTest = 6

    .. data:: failed = 7

    .. data:: missing = 8

    .. data:: mismatchWithParent = 9

    .. data:: mismatchConfig = 10

    .. data:: diagFailed = 11

    .. data:: dormant = 12

    .. data:: outOfServiceAdmin = 13

    .. data:: outOfServiceEnvTemp = 14

    .. data:: poweredDown = 15

    .. data:: poweredUp = 16

    .. data:: powerDenied = 17

    .. data:: powerCycled = 18

    .. data:: okButPowerOverWarning = 19

    .. data:: okButPowerOverCritical = 20

    .. data:: updatingFPD = 21

    """

    unknown = Enum.YLeaf(1, "unknown")

    ok = Enum.YLeaf(2, "ok")

    disabled = Enum.YLeaf(3, "disabled")

    okButDiagFailed = Enum.YLeaf(4, "okButDiagFailed")

    boot = Enum.YLeaf(5, "boot")

    selfTest = Enum.YLeaf(6, "selfTest")

    failed = Enum.YLeaf(7, "failed")

    missing = Enum.YLeaf(8, "missing")

    mismatchWithParent = Enum.YLeaf(9, "mismatchWithParent")

    mismatchConfig = Enum.YLeaf(10, "mismatchConfig")

    diagFailed = Enum.YLeaf(11, "diagFailed")

    dormant = Enum.YLeaf(12, "dormant")

    outOfServiceAdmin = Enum.YLeaf(13, "outOfServiceAdmin")

    outOfServiceEnvTemp = Enum.YLeaf(14, "outOfServiceEnvTemp")

    poweredDown = Enum.YLeaf(15, "poweredDown")

    poweredUp = Enum.YLeaf(16, "poweredUp")

    powerDenied = Enum.YLeaf(17, "powerDenied")

    powerCycled = Enum.YLeaf(18, "powerCycled")

    okButPowerOverWarning = Enum.YLeaf(19, "okButPowerOverWarning")

    okButPowerOverCritical = Enum.YLeaf(20, "okButPowerOverCritical")

    updatingFPD = Enum.YLeaf(21, "updatingFPD")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
        return meta._meta_table['ModuleOperType']


class ModuleResetReasonType(Enum):
    """
    ModuleResetReasonType (Enum Class)

    .. data:: unknown = 1

    .. data:: powerUp = 2

    .. data:: parityError = 3

    .. data:: clearConfigReset = 4

    .. data:: manualReset = 5

    .. data:: watchDogTimeoutReset = 6

    .. data:: resourceOverflowReset = 7

    .. data:: missingTaskReset = 8

    .. data:: lowVoltageReset = 9

    .. data:: controllerReset = 10

    .. data:: systemReset = 11

    .. data:: switchoverReset = 12

    .. data:: upgradeReset = 13

    .. data:: downgradeReset = 14

    .. data:: cacheErrorReset = 15

    .. data:: deviceDriverReset = 16

    .. data:: softwareExceptionReset = 17

    .. data:: restoreConfigReset = 18

    .. data:: abortRevReset = 19

    .. data:: burnBootReset = 20

    .. data:: standbyCdHealthierReset = 21

    .. data:: nonNativeConfigClearReset = 22

    .. data:: memoryProtectionErrorReset = 23

    """

    unknown = Enum.YLeaf(1, "unknown")

    powerUp = Enum.YLeaf(2, "powerUp")

    parityError = Enum.YLeaf(3, "parityError")

    clearConfigReset = Enum.YLeaf(4, "clearConfigReset")

    manualReset = Enum.YLeaf(5, "manualReset")

    watchDogTimeoutReset = Enum.YLeaf(6, "watchDogTimeoutReset")

    resourceOverflowReset = Enum.YLeaf(7, "resourceOverflowReset")

    missingTaskReset = Enum.YLeaf(8, "missingTaskReset")

    lowVoltageReset = Enum.YLeaf(9, "lowVoltageReset")

    controllerReset = Enum.YLeaf(10, "controllerReset")

    systemReset = Enum.YLeaf(11, "systemReset")

    switchoverReset = Enum.YLeaf(12, "switchoverReset")

    upgradeReset = Enum.YLeaf(13, "upgradeReset")

    downgradeReset = Enum.YLeaf(14, "downgradeReset")

    cacheErrorReset = Enum.YLeaf(15, "cacheErrorReset")

    deviceDriverReset = Enum.YLeaf(16, "deviceDriverReset")

    softwareExceptionReset = Enum.YLeaf(17, "softwareExceptionReset")

    restoreConfigReset = Enum.YLeaf(18, "restoreConfigReset")

    abortRevReset = Enum.YLeaf(19, "abortRevReset")

    burnBootReset = Enum.YLeaf(20, "burnBootReset")

    standbyCdHealthierReset = Enum.YLeaf(21, "standbyCdHealthierReset")

    nonNativeConfigClearReset = Enum.YLeaf(22, "nonNativeConfigClearReset")

    memoryProtectionErrorReset = Enum.YLeaf(23, "memoryProtectionErrorReset")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
        return meta._meta_table['ModuleResetReasonType']


class PowerAdminType(Enum):
    """
    PowerAdminType (Enum Class)

    .. data:: on = 1

    .. data:: off = 2

    .. data:: inlineAuto = 3

    .. data:: inlineOn = 4

    """

    on = Enum.YLeaf(1, "on")

    off = Enum.YLeaf(2, "off")

    inlineAuto = Enum.YLeaf(3, "inlineAuto")

    inlineOn = Enum.YLeaf(4, "inlineOn")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
        return meta._meta_table['PowerAdminType']


class PowerOperType(Enum):
    """
    PowerOperType (Enum Class)

    .. data:: offEnvOther = 1

    .. data:: on = 2

    .. data:: offAdmin = 3

    .. data:: offDenied = 4

    .. data:: offEnvPower = 5

    .. data:: offEnvTemp = 6

    .. data:: offEnvFan = 7

    .. data:: failed = 8

    .. data:: onButFanFail = 9

    """

    offEnvOther = Enum.YLeaf(1, "offEnvOther")

    on = Enum.YLeaf(2, "on")

    offAdmin = Enum.YLeaf(3, "offAdmin")

    offDenied = Enum.YLeaf(4, "offDenied")

    offEnvPower = Enum.YLeaf(5, "offEnvPower")

    offEnvTemp = Enum.YLeaf(6, "offEnvTemp")

    offEnvFan = Enum.YLeaf(7, "offEnvFan")

    failed = Enum.YLeaf(8, "failed")

    onButFanFail = Enum.YLeaf(9, "onButFanFail")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
        return meta._meta_table['PowerOperType']


class PowerRedundancyType(Enum):
    """
    PowerRedundancyType (Enum Class)

    .. data:: notsupported = 1

    .. data:: redundant = 2

    .. data:: combined = 3

    """

    notsupported = Enum.YLeaf(1, "notsupported")

    redundant = Enum.YLeaf(2, "redundant")

    combined = Enum.YLeaf(3, "combined")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
        return meta._meta_table['PowerRedundancyType']



class CISCOENTITYFRUCONTROLMIB(_Entity_):
    """
    
    
    .. attribute:: cefcfrupower
    
    	
    	**type**\:  :py:class:`CefcFRUPower <ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFRUPower>`
    
    	**config**\: False
    
    .. attribute:: cefcmibnotificationenables
    
    	
    	**type**\:  :py:class:`CefcMIBNotificationEnables <ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcMIBNotificationEnables>`
    
    	**config**\: False
    
    .. attribute:: cefcfrupowersupplygrouptable
    
    	
    	**type**\:  :py:class:`CefcFRUPowerSupplyGroupTable <ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable>`
    
    	**config**\: False
    
    .. attribute:: cefcfrupowerstatustable
    
    	
    	**type**\:  :py:class:`CefcFRUPowerStatusTable <ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable>`
    
    	**config**\: False
    
    .. attribute:: cefcfrupowersupplyvaluetable
    
    	
    	**type**\:  :py:class:`CefcFRUPowerSupplyValueTable <ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable>`
    
    	**config**\: False
    
    .. attribute:: cefcmoduletable
    
    	
    	**type**\:  :py:class:`CefcModuleTable <ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcModuleTable>`
    
    	**config**\: False
    
    .. attribute:: cefcintellimoduletable
    
    	
    	**type**\:  :py:class:`CefcIntelliModuleTable <ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable>`
    
    	**config**\: False
    
    .. attribute:: cefcfantraystatustable
    
    	
    	**type**\:  :py:class:`CefcFanTrayStatusTable <ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable>`
    
    	**config**\: False
    
    .. attribute:: cefcphysicaltable
    
    	
    	**type**\:  :py:class:`CefcPhysicalTable <ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO_ENTITY_FRU_CONTROL_MIB'
    _revision = '2003-11-24'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(CISCOENTITYFRUCONTROLMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
        self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cefcFRUPower", ("cefcfrupower", CISCOENTITYFRUCONTROLMIB.CefcFRUPower)), ("cefcMIBNotificationEnables", ("cefcmibnotificationenables", CISCOENTITYFRUCONTROLMIB.CefcMIBNotificationEnables)), ("cefcFRUPowerSupplyGroupTable", ("cefcfrupowersupplygrouptable", CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable)), ("cefcFRUPowerStatusTable", ("cefcfrupowerstatustable", CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable)), ("cefcFRUPowerSupplyValueTable", ("cefcfrupowersupplyvaluetable", CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable)), ("cefcModuleTable", ("cefcmoduletable", CISCOENTITYFRUCONTROLMIB.CefcModuleTable)), ("cefcIntelliModuleTable", ("cefcintellimoduletable", CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable)), ("cefcFanTrayStatusTable", ("cefcfantraystatustable", CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable)), ("cefcPhysicalTable", ("cefcphysicaltable", CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable))])
        self._leafs = OrderedDict()

        self.cefcfrupower = CISCOENTITYFRUCONTROLMIB.CefcFRUPower()
        self.cefcfrupower.parent = self
        self._children_name_map["cefcfrupower"] = "cefcFRUPower"

        self.cefcmibnotificationenables = CISCOENTITYFRUCONTROLMIB.CefcMIBNotificationEnables()
        self.cefcmibnotificationenables.parent = self
        self._children_name_map["cefcmibnotificationenables"] = "cefcMIBNotificationEnables"

        self.cefcfrupowersupplygrouptable = CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable()
        self.cefcfrupowersupplygrouptable.parent = self
        self._children_name_map["cefcfrupowersupplygrouptable"] = "cefcFRUPowerSupplyGroupTable"

        self.cefcfrupowerstatustable = CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable()
        self.cefcfrupowerstatustable.parent = self
        self._children_name_map["cefcfrupowerstatustable"] = "cefcFRUPowerStatusTable"

        self.cefcfrupowersupplyvaluetable = CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable()
        self.cefcfrupowersupplyvaluetable.parent = self
        self._children_name_map["cefcfrupowersupplyvaluetable"] = "cefcFRUPowerSupplyValueTable"

        self.cefcmoduletable = CISCOENTITYFRUCONTROLMIB.CefcModuleTable()
        self.cefcmoduletable.parent = self
        self._children_name_map["cefcmoduletable"] = "cefcModuleTable"

        self.cefcintellimoduletable = CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable()
        self.cefcintellimoduletable.parent = self
        self._children_name_map["cefcintellimoduletable"] = "cefcIntelliModuleTable"

        self.cefcfantraystatustable = CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable()
        self.cefcfantraystatustable.parent = self
        self._children_name_map["cefcfantraystatustable"] = "cefcFanTrayStatusTable"

        self.cefcphysicaltable = CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable()
        self.cefcphysicaltable.parent = self
        self._children_name_map["cefcphysicaltable"] = "cefcPhysicalTable"
        self._segment_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOENTITYFRUCONTROLMIB, [], name, value)


    class CefcFRUPower(_Entity_):
        """
        
        
        .. attribute:: cefcmaxdefaultinlinepower
        
        	
        	**type**\: int
        
        	**range:** 0..12500
        
        	**config**\: False
        
        	**default value**\: 12500
        
        .. attribute:: cefcmaxdefaulthighinlinepower
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO_ENTITY_FRU_CONTROL_MIB'
        _revision = '2003-11-24'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(CISCOENTITYFRUCONTROLMIB.CefcFRUPower, self).__init__()

            self.yang_name = "cefcFRUPower"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cefcmaxdefaultinlinepower', (YLeaf(YType.int32, 'cefcMaxDefaultInLinePower'), ['int'])),
                ('cefcmaxdefaulthighinlinepower', (YLeaf(YType.uint32, 'cefcMaxDefaultHighInLinePower'), ['int'])),
            ])
            self.cefcmaxdefaultinlinepower = None
            self.cefcmaxdefaulthighinlinepower = None
            self._segment_path = lambda: "cefcFRUPower"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcFRUPower, ['cefcmaxdefaultinlinepower', 'cefcmaxdefaulthighinlinepower'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcFRUPower']['meta_info']


    class CefcMIBNotificationEnables(_Entity_):
        """
        
        
        .. attribute:: cefcmibenablestatusnotification
        
        	
        	**type**\:  :py:class:`TruthValue <ydk.models.cisco_ios_xr.SNMPv2_TC.TruthValue>`
        
        	**config**\: False
        
        	**default value**\: false
        
        

        """

        _prefix = 'CISCO_ENTITY_FRU_CONTROL_MIB'
        _revision = '2003-11-24'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(CISCOENTITYFRUCONTROLMIB.CefcMIBNotificationEnables, self).__init__()

            self.yang_name = "cefcMIBNotificationEnables"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cefcmibenablestatusnotification', (YLeaf(YType.enumeration, 'cefcMIBEnableStatusNotification'), [('ydk.models.cisco_ios_xr.SNMPv2_TC', 'TruthValue', '')])),
            ])
            self.cefcmibenablestatusnotification = None
            self._segment_path = lambda: "cefcMIBNotificationEnables"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcMIBNotificationEnables, ['cefcmibenablestatusnotification'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcMIBNotificationEnables']['meta_info']


    class CefcFRUPowerSupplyGroupTable(_Entity_):
        """
        
        
        .. attribute:: cefcfrupowersupplygroupentry
        
        	
        	**type**\: list of  		 :py:class:`CefcFRUPowerSupplyGroupEntry <ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable.CefcFRUPowerSupplyGroupEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO_ENTITY_FRU_CONTROL_MIB'
        _revision = '2003-11-24'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable, self).__init__()

            self.yang_name = "cefcFRUPowerSupplyGroupTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefcFRUPowerSupplyGroupEntry", ("cefcfrupowersupplygroupentry", CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable.CefcFRUPowerSupplyGroupEntry))])
            self._leafs = OrderedDict()

            self.cefcfrupowersupplygroupentry = YList(self)
            self._segment_path = lambda: "cefcFRUPowerSupplyGroupTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable, [], name, value)


        class CefcFRUPowerSupplyGroupEntry(_Entity_):
            """
            
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: cefcpowerredundancymode
            
            	
            	**type**\:  :py:class:`PowerRedundancyType <ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB.PowerRedundancyType>`
            
            	**config**\: False
            
            .. attribute:: cefcpowerunits
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cefctotalavailablecurrent
            
            	
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            	**config**\: False
            
            .. attribute:: cefctotaldrawncurrent
            
            	
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            	**config**\: False
            
            .. attribute:: cefcpowerredundancyopermode
            
            	
            	**type**\:  :py:class:`PowerRedundancyType <ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB.PowerRedundancyType>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO_ENTITY_FRU_CONTROL_MIB'
            _revision = '2003-11-24'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable.CefcFRUPowerSupplyGroupEntry, self).__init__()

                self.yang_name = "cefcFRUPowerSupplyGroupEntry"
                self.yang_parent_name = "cefcFRUPowerSupplyGroupTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.int32, 'entPhysicalIndex'), ['int'])),
                    ('cefcpowerredundancymode', (YLeaf(YType.enumeration, 'cefcPowerRedundancyMode'), [('ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB', 'PowerRedundancyType', '')])),
                    ('cefcpowerunits', (YLeaf(YType.str, 'cefcPowerUnits'), ['str'])),
                    ('cefctotalavailablecurrent', (YLeaf(YType.int32, 'cefcTotalAvailableCurrent'), ['int'])),
                    ('cefctotaldrawncurrent', (YLeaf(YType.int32, 'cefcTotalDrawnCurrent'), ['int'])),
                    ('cefcpowerredundancyopermode', (YLeaf(YType.enumeration, 'cefcPowerRedundancyOperMode'), [('ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB', 'PowerRedundancyType', '')])),
                ])
                self.entphysicalindex = None
                self.cefcpowerredundancymode = None
                self.cefcpowerunits = None
                self.cefctotalavailablecurrent = None
                self.cefctotaldrawncurrent = None
                self.cefcpowerredundancyopermode = None
                self._segment_path = lambda: "cefcFRUPowerSupplyGroupEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcFRUPowerSupplyGroupTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable.CefcFRUPowerSupplyGroupEntry, ['entphysicalindex', 'cefcpowerredundancymode', 'cefcpowerunits', 'cefctotalavailablecurrent', 'cefctotaldrawncurrent', 'cefcpowerredundancyopermode'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable.CefcFRUPowerSupplyGroupEntry']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable']['meta_info']


    class CefcFRUPowerStatusTable(_Entity_):
        """
        
        
        .. attribute:: cefcfrupowerstatusentry
        
        	
        	**type**\: list of  		 :py:class:`CefcFRUPowerStatusEntry <ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable.CefcFRUPowerStatusEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO_ENTITY_FRU_CONTROL_MIB'
        _revision = '2003-11-24'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable, self).__init__()

            self.yang_name = "cefcFRUPowerStatusTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefcFRUPowerStatusEntry", ("cefcfrupowerstatusentry", CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable.CefcFRUPowerStatusEntry))])
            self._leafs = OrderedDict()

            self.cefcfrupowerstatusentry = YList(self)
            self._segment_path = lambda: "cefcFRUPowerStatusTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable, [], name, value)


        class CefcFRUPowerStatusEntry(_Entity_):
            """
            
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: cefcfrupoweradminstatus
            
            	
            	**type**\:  :py:class:`PowerAdminType <ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB.PowerAdminType>`
            
            	**config**\: False
            
            .. attribute:: cefcfrupoweroperstatus
            
            	
            	**type**\:  :py:class:`PowerOperType <ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB.PowerOperType>`
            
            	**config**\: False
            
            .. attribute:: cefcfrucurrent
            
            	
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO_ENTITY_FRU_CONTROL_MIB'
            _revision = '2003-11-24'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable.CefcFRUPowerStatusEntry, self).__init__()

                self.yang_name = "cefcFRUPowerStatusEntry"
                self.yang_parent_name = "cefcFRUPowerStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.int32, 'entPhysicalIndex'), ['int'])),
                    ('cefcfrupoweradminstatus', (YLeaf(YType.enumeration, 'cefcFRUPowerAdminStatus'), [('ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB', 'PowerAdminType', '')])),
                    ('cefcfrupoweroperstatus', (YLeaf(YType.enumeration, 'cefcFRUPowerOperStatus'), [('ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB', 'PowerOperType', '')])),
                    ('cefcfrucurrent', (YLeaf(YType.int32, 'cefcFRUCurrent'), ['int'])),
                ])
                self.entphysicalindex = None
                self.cefcfrupoweradminstatus = None
                self.cefcfrupoweroperstatus = None
                self.cefcfrucurrent = None
                self._segment_path = lambda: "cefcFRUPowerStatusEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcFRUPowerStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable.CefcFRUPowerStatusEntry, ['entphysicalindex', 'cefcfrupoweradminstatus', 'cefcfrupoweroperstatus', 'cefcfrucurrent'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable.CefcFRUPowerStatusEntry']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable']['meta_info']


    class CefcFRUPowerSupplyValueTable(_Entity_):
        """
        
        
        .. attribute:: cefcfrupowersupplyvalueentry
        
        	
        	**type**\: list of  		 :py:class:`CefcFRUPowerSupplyValueEntry <ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable.CefcFRUPowerSupplyValueEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO_ENTITY_FRU_CONTROL_MIB'
        _revision = '2003-11-24'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable, self).__init__()

            self.yang_name = "cefcFRUPowerSupplyValueTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefcFRUPowerSupplyValueEntry", ("cefcfrupowersupplyvalueentry", CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable.CefcFRUPowerSupplyValueEntry))])
            self._leafs = OrderedDict()

            self.cefcfrupowersupplyvalueentry = YList(self)
            self._segment_path = lambda: "cefcFRUPowerSupplyValueTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable, [], name, value)


        class CefcFRUPowerSupplyValueEntry(_Entity_):
            """
            
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: cefcfrutotalsystemcurrent
            
            	
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            	**config**\: False
            
            .. attribute:: cefcfrudrawnsystemcurrent
            
            	
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            	**config**\: False
            
            .. attribute:: cefcfrutotalinlinecurrent
            
            	
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            	**config**\: False
            
            .. attribute:: cefcfrudrawninlinecurrent
            
            	
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO_ENTITY_FRU_CONTROL_MIB'
            _revision = '2003-11-24'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable.CefcFRUPowerSupplyValueEntry, self).__init__()

                self.yang_name = "cefcFRUPowerSupplyValueEntry"
                self.yang_parent_name = "cefcFRUPowerSupplyValueTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.int32, 'entPhysicalIndex'), ['int'])),
                    ('cefcfrutotalsystemcurrent', (YLeaf(YType.int32, 'cefcFRUTotalSystemCurrent'), ['int'])),
                    ('cefcfrudrawnsystemcurrent', (YLeaf(YType.int32, 'cefcFRUDrawnSystemCurrent'), ['int'])),
                    ('cefcfrutotalinlinecurrent', (YLeaf(YType.int32, 'cefcFRUTotalInlineCurrent'), ['int'])),
                    ('cefcfrudrawninlinecurrent', (YLeaf(YType.int32, 'cefcFRUDrawnInlineCurrent'), ['int'])),
                ])
                self.entphysicalindex = None
                self.cefcfrutotalsystemcurrent = None
                self.cefcfrudrawnsystemcurrent = None
                self.cefcfrutotalinlinecurrent = None
                self.cefcfrudrawninlinecurrent = None
                self._segment_path = lambda: "cefcFRUPowerSupplyValueEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcFRUPowerSupplyValueTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable.CefcFRUPowerSupplyValueEntry, ['entphysicalindex', 'cefcfrutotalsystemcurrent', 'cefcfrudrawnsystemcurrent', 'cefcfrutotalinlinecurrent', 'cefcfrudrawninlinecurrent'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable.CefcFRUPowerSupplyValueEntry']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable']['meta_info']


    class CefcModuleTable(_Entity_):
        """
        
        
        .. attribute:: cefcmoduleentry
        
        	
        	**type**\: list of  		 :py:class:`CefcModuleEntry <ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcModuleTable.CefcModuleEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO_ENTITY_FRU_CONTROL_MIB'
        _revision = '2003-11-24'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(CISCOENTITYFRUCONTROLMIB.CefcModuleTable, self).__init__()

            self.yang_name = "cefcModuleTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefcModuleEntry", ("cefcmoduleentry", CISCOENTITYFRUCONTROLMIB.CefcModuleTable.CefcModuleEntry))])
            self._leafs = OrderedDict()

            self.cefcmoduleentry = YList(self)
            self._segment_path = lambda: "cefcModuleTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcModuleTable, [], name, value)


        class CefcModuleEntry(_Entity_):
            """
            
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: cefcmoduleadminstatus
            
            	
            	**type**\:  :py:class:`ModuleAdminType <ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB.ModuleAdminType>`
            
            	**config**\: False
            
            .. attribute:: cefcmoduleoperstatus
            
            	
            	**type**\:  :py:class:`ModuleOperType <ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB.ModuleOperType>`
            
            	**config**\: False
            
            .. attribute:: cefcmoduleresetreason
            
            	
            	**type**\:  :py:class:`ModuleResetReasonType <ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB.ModuleResetReasonType>`
            
            	**config**\: False
            
            .. attribute:: cefcmodulestatuslastchangetime
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cefcmodulelastclearconfigtime
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cefcmoduleresetreasondescription
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cefcmodulestatechangereasondescr
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cefcmoduleuptime
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO_ENTITY_FRU_CONTROL_MIB'
            _revision = '2003-11-24'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(CISCOENTITYFRUCONTROLMIB.CefcModuleTable.CefcModuleEntry, self).__init__()

                self.yang_name = "cefcModuleEntry"
                self.yang_parent_name = "cefcModuleTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.int32, 'entPhysicalIndex'), ['int'])),
                    ('cefcmoduleadminstatus', (YLeaf(YType.enumeration, 'cefcModuleAdminStatus'), [('ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB', 'ModuleAdminType', '')])),
                    ('cefcmoduleoperstatus', (YLeaf(YType.enumeration, 'cefcModuleOperStatus'), [('ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB', 'ModuleOperType', '')])),
                    ('cefcmoduleresetreason', (YLeaf(YType.enumeration, 'cefcModuleResetReason'), [('ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB', 'ModuleResetReasonType', '')])),
                    ('cefcmodulestatuslastchangetime', (YLeaf(YType.uint32, 'cefcModuleStatusLastChangeTime'), ['int'])),
                    ('cefcmodulelastclearconfigtime', (YLeaf(YType.uint32, 'cefcModuleLastClearConfigTime'), ['int'])),
                    ('cefcmoduleresetreasondescription', (YLeaf(YType.str, 'cefcModuleResetReasonDescription'), ['str'])),
                    ('cefcmodulestatechangereasondescr', (YLeaf(YType.str, 'cefcModuleStateChangeReasonDescr'), ['str'])),
                    ('cefcmoduleuptime', (YLeaf(YType.uint32, 'cefcModuleUpTime'), ['int'])),
                ])
                self.entphysicalindex = None
                self.cefcmoduleadminstatus = None
                self.cefcmoduleoperstatus = None
                self.cefcmoduleresetreason = None
                self.cefcmodulestatuslastchangetime = None
                self.cefcmodulelastclearconfigtime = None
                self.cefcmoduleresetreasondescription = None
                self.cefcmodulestatechangereasondescr = None
                self.cefcmoduleuptime = None
                self._segment_path = lambda: "cefcModuleEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcModuleTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcModuleTable.CefcModuleEntry, ['entphysicalindex', 'cefcmoduleadminstatus', 'cefcmoduleoperstatus', 'cefcmoduleresetreason', 'cefcmodulestatuslastchangetime', 'cefcmodulelastclearconfigtime', 'cefcmoduleresetreasondescription', 'cefcmodulestatechangereasondescr', 'cefcmoduleuptime'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcModuleTable.CefcModuleEntry']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcModuleTable']['meta_info']


    class CefcIntelliModuleTable(_Entity_):
        """
        
        
        .. attribute:: cefcintellimoduleentry
        
        	
        	**type**\: list of  		 :py:class:`CefcIntelliModuleEntry <ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable.CefcIntelliModuleEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO_ENTITY_FRU_CONTROL_MIB'
        _revision = '2003-11-24'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable, self).__init__()

            self.yang_name = "cefcIntelliModuleTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefcIntelliModuleEntry", ("cefcintellimoduleentry", CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable.CefcIntelliModuleEntry))])
            self._leafs = OrderedDict()

            self.cefcintellimoduleentry = YList(self)
            self._segment_path = lambda: "cefcIntelliModuleTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable, [], name, value)


        class CefcIntelliModuleEntry(_Entity_):
            """
            
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: cefcintellimoduleipaddrtype
            
            	
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xr.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cefcintellimoduleipaddr
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO_ENTITY_FRU_CONTROL_MIB'
            _revision = '2003-11-24'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable.CefcIntelliModuleEntry, self).__init__()

                self.yang_name = "cefcIntelliModuleEntry"
                self.yang_parent_name = "cefcIntelliModuleTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.int32, 'entPhysicalIndex'), ['int'])),
                    ('cefcintellimoduleipaddrtype', (YLeaf(YType.enumeration, 'cefcIntelliModuleIPAddrType'), [('ydk.models.cisco_ios_xr.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cefcintellimoduleipaddr', (YLeaf(YType.str, 'cefcIntelliModuleIPAddr'), ['str'])),
                ])
                self.entphysicalindex = None
                self.cefcintellimoduleipaddrtype = None
                self.cefcintellimoduleipaddr = None
                self._segment_path = lambda: "cefcIntelliModuleEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcIntelliModuleTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable.CefcIntelliModuleEntry, ['entphysicalindex', 'cefcintellimoduleipaddrtype', 'cefcintellimoduleipaddr'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable.CefcIntelliModuleEntry']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable']['meta_info']


    class CefcFanTrayStatusTable(_Entity_):
        """
        
        
        .. attribute:: cefcfantraystatusentry
        
        	
        	**type**\: list of  		 :py:class:`CefcFanTrayStatusEntry <ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable.CefcFanTrayStatusEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO_ENTITY_FRU_CONTROL_MIB'
        _revision = '2003-11-24'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable, self).__init__()

            self.yang_name = "cefcFanTrayStatusTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefcFanTrayStatusEntry", ("cefcfantraystatusentry", CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable.CefcFanTrayStatusEntry))])
            self._leafs = OrderedDict()

            self.cefcfantraystatusentry = YList(self)
            self._segment_path = lambda: "cefcFanTrayStatusTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable, [], name, value)


        class CefcFanTrayStatusEntry(_Entity_):
            """
            
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: cefcfantrayoperstatus
            
            	
            	**type**\:  :py:class:`CefcFanTrayOperStatusType <ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB.CefcFanTrayOperStatusType>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO_ENTITY_FRU_CONTROL_MIB'
            _revision = '2003-11-24'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable.CefcFanTrayStatusEntry, self).__init__()

                self.yang_name = "cefcFanTrayStatusEntry"
                self.yang_parent_name = "cefcFanTrayStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.int32, 'entPhysicalIndex'), ['int'])),
                    ('cefcfantrayoperstatus', (YLeaf(YType.enumeration, 'cefcFanTrayOperStatus'), [('ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB', 'CefcFanTrayOperStatusType', '')])),
                ])
                self.entphysicalindex = None
                self.cefcfantrayoperstatus = None
                self._segment_path = lambda: "cefcFanTrayStatusEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcFanTrayStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable.CefcFanTrayStatusEntry, ['entphysicalindex', 'cefcfantrayoperstatus'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable.CefcFanTrayStatusEntry']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable']['meta_info']


    class CefcPhysicalTable(_Entity_):
        """
        
        
        .. attribute:: cefcphysicalentry
        
        	
        	**type**\: list of  		 :py:class:`CefcPhysicalEntry <ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable.CefcPhysicalEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO_ENTITY_FRU_CONTROL_MIB'
        _revision = '2003-11-24'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable, self).__init__()

            self.yang_name = "cefcPhysicalTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefcPhysicalEntry", ("cefcphysicalentry", CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable.CefcPhysicalEntry))])
            self._leafs = OrderedDict()

            self.cefcphysicalentry = YList(self)
            self._segment_path = lambda: "cefcPhysicalTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable, [], name, value)


        class CefcPhysicalEntry(_Entity_):
            """
            
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: cefcphysicalstatus
            
            	
            	**type**\:  :py:class:`CefcPhysicalStatusType <ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB.CefcPhysicalStatusType>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO_ENTITY_FRU_CONTROL_MIB'
            _revision = '2003-11-24'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable.CefcPhysicalEntry, self).__init__()

                self.yang_name = "cefcPhysicalEntry"
                self.yang_parent_name = "cefcPhysicalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.int32, 'entPhysicalIndex'), ['int'])),
                    ('cefcphysicalstatus', (YLeaf(YType.enumeration, 'cefcPhysicalStatus'), [('ydk.models.cisco_ios_xr.CISCO_ENTITY_FRU_CONTROL_MIB', 'CefcPhysicalStatusType', '')])),
                ])
                self.entphysicalindex = None
                self.cefcphysicalstatus = None
                self._segment_path = lambda: "cefcPhysicalEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcPhysicalTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable.CefcPhysicalEntry, ['entphysicalindex', 'cefcphysicalstatus'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable.CefcPhysicalEntry']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable']['meta_info']

    def clone_ptr(self):
        self._top_entity = CISCOENTITYFRUCONTROLMIB()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
        return meta._meta_table['CISCOENTITYFRUCONTROLMIB']['meta_info']



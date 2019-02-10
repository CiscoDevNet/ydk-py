""" Cisco_IOS_XE_controller_vdsl_oper 

This module contains a collection of YANG definitions
for monitoring controller VDSL operational information.
Copyright (c) 2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IdbStates(Enum):
    """
    IdbStates (Enum Class)

    Interface state

    .. data:: down = 0

    	Interface down

    .. data:: going_down = 1

    	Interface going down

    .. data:: init = 2

    	Interface init

    .. data:: testing = 3

    	Interface testing

    .. data:: up = 4

    	Interface up

    .. data:: reset = 5

    	Interface reset

    .. data:: admindown = 6

    	Interface admindown

    .. data:: deleted = 7

    	Interface deleted

    """

    down = Enum.YLeaf(0, "down")

    going_down = Enum.YLeaf(1, "going-down")

    init = Enum.YLeaf(2, "init")

    testing = Enum.YLeaf(3, "testing")

    up = Enum.YLeaf(4, "up")

    reset = Enum.YLeaf(5, "reset")

    admindown = Enum.YLeaf(6, "admindown")

    deleted = Enum.YLeaf(7, "deleted")


class ModeTc(Enum):
    """
    ModeTc (Enum Class)

    Operation Mode

    .. data:: ptm = 0

    	MODE Ethernet

    .. data:: atm = 1

    	MODE Atm

    """

    ptm = Enum.YLeaf(0, "ptm")

    atm = Enum.YLeaf(1, "atm")



class VdslOperData(Entity):
    """
    VDSL controller information
    
    .. attribute:: vdsl_info
    
    	VDSL controller information
    	**type**\: list of  		 :py:class:`VdslInfo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_controller_vdsl_oper.VdslOperData.VdslInfo>`
    
    	**config**\: False
    
    

    """

    _prefix = 'vdsl-ios-xe-oper'
    _revision = '2018-01-31'

    def __init__(self):
        super(VdslOperData, self).__init__()
        self._top_entity = None

        self.yang_name = "vdsl-oper-data"
        self.yang_parent_name = "Cisco-IOS-XE-controller-vdsl-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("vdsl-info", ("vdsl_info", VdslOperData.VdslInfo))])
        self._leafs = OrderedDict()

        self.vdsl_info = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-controller-vdsl-oper:vdsl-oper-data"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(VdslOperData, [], name, value)


    class VdslInfo(Entity):
        """
        VDSL controller information
        
        .. attribute:: slot_num  (key)
        
        	Slot number
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: subslot_num  (key)
        
        	Sub Slot number
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: state
        
        	Controller database state
        	**type**\:  :py:class:`IdbStates <ydk.models.cisco_ios_xe.Cisco_IOS_XE_controller_vdsl_oper.IdbStates>`
        
        	**config**\: False
        
        .. attribute:: mode
        
        	Operational mode
        	**type**\:  :py:class:`ModeTc <ydk.models.cisco_ios_xe.Cisco_IOS_XE_controller_vdsl_oper.ModeTc>`
        
        	**config**\: False
        
        .. attribute:: modem_status
        
        	Modem status
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: trained_mode
        
        	Trained Mode
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: firmware_version
        
        	Firmware version
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: phy_version
        
        	PHY version
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: cpe_stats
        
        	XTU\-R customer\-premises equipment statistics
        	**type**\:  :py:class:`CpeStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_controller_vdsl_oper.VdslOperData.VdslInfo.CpeStats>`
        
        	**config**\: False
        
        .. attribute:: co_stats
        
        	XTU\-C central office statistics
        	**type**\:  :py:class:`CoStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_controller_vdsl_oper.VdslOperData.VdslInfo.CoStats>`
        
        	**config**\: False
        
        

        """

        _prefix = 'vdsl-ios-xe-oper'
        _revision = '2018-01-31'

        def __init__(self):
            super(VdslOperData.VdslInfo, self).__init__()

            self.yang_name = "vdsl-info"
            self.yang_parent_name = "vdsl-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['slot_num','subslot_num']
            self._child_classes = OrderedDict([("cpe-stats", ("cpe_stats", VdslOperData.VdslInfo.CpeStats)), ("co-stats", ("co_stats", VdslOperData.VdslInfo.CoStats))])
            self._leafs = OrderedDict([
                ('slot_num', (YLeaf(YType.uint32, 'slot-num'), ['int'])),
                ('subslot_num', (YLeaf(YType.uint32, 'subslot-num'), ['int'])),
                ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_controller_vdsl_oper', 'IdbStates', '')])),
                ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_controller_vdsl_oper', 'ModeTc', '')])),
                ('modem_status', (YLeaf(YType.str, 'modem-status'), ['str'])),
                ('trained_mode', (YLeaf(YType.str, 'trained-mode'), ['str'])),
                ('firmware_version', (YLeaf(YType.str, 'firmware-version'), ['str'])),
                ('phy_version', (YLeaf(YType.str, 'phy-version'), ['str'])),
            ])
            self.slot_num = None
            self.subslot_num = None
            self.state = None
            self.mode = None
            self.modem_status = None
            self.trained_mode = None
            self.firmware_version = None
            self.phy_version = None

            self.cpe_stats = VdslOperData.VdslInfo.CpeStats()
            self.cpe_stats.parent = self
            self._children_name_map["cpe_stats"] = "cpe-stats"

            self.co_stats = VdslOperData.VdslInfo.CoStats()
            self.co_stats.parent = self
            self._children_name_map["co_stats"] = "co-stats"
            self._segment_path = lambda: "vdsl-info" + "[slot-num='" + str(self.slot_num) + "']" + "[subslot-num='" + str(self.subslot_num) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-controller-vdsl-oper:vdsl-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(VdslOperData.VdslInfo, ['slot_num', 'subslot_num', 'state', 'mode', 'modem_status', 'trained_mode', 'firmware_version', 'phy_version'], name, value)


        class CpeStats(Entity):
            """
            XTU\-R customer\-premises equipment statistics
            
            .. attribute:: chip_vendor
            
            	Chip vendor ID
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: line_attenuation
            
            	Line attenuation in decibels
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: noise_margin
            
            	Noise margin in decibels
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: attainable_rate
            
            	Attainable rate in kilobits per sec
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: actual_power
            
            	Actual power in decibel\-milliwatts
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: speed
            
            	Speed in kilobits per sec
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'vdsl-ios-xe-oper'
            _revision = '2018-01-31'

            def __init__(self):
                super(VdslOperData.VdslInfo.CpeStats, self).__init__()

                self.yang_name = "cpe-stats"
                self.yang_parent_name = "vdsl-info"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('chip_vendor', (YLeaf(YType.str, 'chip-vendor'), ['str'])),
                    ('line_attenuation', (YLeaf(YType.str, 'line-attenuation'), ['str'])),
                    ('noise_margin', (YLeaf(YType.str, 'noise-margin'), ['str'])),
                    ('attainable_rate', (YLeaf(YType.uint32, 'attainable-rate'), ['int'])),
                    ('actual_power', (YLeaf(YType.str, 'actual-power'), ['str'])),
                    ('speed', (YLeaf(YType.uint32, 'speed'), ['int'])),
                ])
                self.chip_vendor = None
                self.line_attenuation = None
                self.noise_margin = None
                self.attainable_rate = None
                self.actual_power = None
                self.speed = None
                self._segment_path = lambda: "cpe-stats"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(VdslOperData.VdslInfo.CpeStats, ['chip_vendor', 'line_attenuation', 'noise_margin', 'attainable_rate', 'actual_power', 'speed'], name, value)



        class CoStats(Entity):
            """
            XTU\-C central office statistics
            
            .. attribute:: chip_vendor
            
            	Chip vendor ID
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: line_attenuation
            
            	Line attenuation in decibels
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: noise_margin
            
            	Noise margin in decibels
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: attainable_rate
            
            	Attainable rate in kilobits per sec
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: actual_power
            
            	Actual power in decibel\-milliwatts
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: speed
            
            	Speed in kilobits per sec
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'vdsl-ios-xe-oper'
            _revision = '2018-01-31'

            def __init__(self):
                super(VdslOperData.VdslInfo.CoStats, self).__init__()

                self.yang_name = "co-stats"
                self.yang_parent_name = "vdsl-info"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('chip_vendor', (YLeaf(YType.str, 'chip-vendor'), ['str'])),
                    ('line_attenuation', (YLeaf(YType.str, 'line-attenuation'), ['str'])),
                    ('noise_margin', (YLeaf(YType.str, 'noise-margin'), ['str'])),
                    ('attainable_rate', (YLeaf(YType.uint32, 'attainable-rate'), ['int'])),
                    ('actual_power', (YLeaf(YType.str, 'actual-power'), ['str'])),
                    ('speed', (YLeaf(YType.uint32, 'speed'), ['int'])),
                ])
                self.chip_vendor = None
                self.line_attenuation = None
                self.noise_margin = None
                self.attainable_rate = None
                self.actual_power = None
                self.speed = None
                self._segment_path = lambda: "co-stats"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(VdslOperData.VdslInfo.CoStats, ['chip_vendor', 'line_attenuation', 'noise_margin', 'attainable_rate', 'actual_power', 'speed'], name, value)



    def clone_ptr(self):
        self._top_entity = VdslOperData()
        return self._top_entity




""" Cisco_IOS_XR_ncs1001_ots_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs1001\-ots package operational data.

This module contains definitions
for the following management objects\:
  hw\-module\: ncs1001 hw\-module command chain

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Chfilter(Enum):
    """
    Chfilter (Enum Class)

    Chfilter

    .. data:: ch_filter_active = 0

    	Active

    .. data:: ch_filter_all = 1

    	All

    """

    ch_filter_active = Enum.YLeaf(0, "ch-filter-active")

    ch_filter_all = Enum.YLeaf(1, "ch-filter-all")


class OtsAmpliTrailData(Enum):
    """
    OtsAmpliTrailData (Enum Class)

    Ots ampli trail data

    .. data:: all = 1

    	Displays Booster and Pre trail data

    .. data:: bst = 2

    	Displays Booster trail data

    .. data:: pre = 3

    	Displays Pre trail data

    """

    all = Enum.YLeaf(1, "all")

    bst = Enum.YLeaf(2, "bst")

    pre = Enum.YLeaf(3, "pre")


class OtsChannelsTrailData(Enum):
    """
    OtsChannelsTrailData (Enum Class)

    Ots channels trail data

    .. data:: all = 1

    	Displays all channels trail data

    .. data:: active = 2

    	Displays active channels trail data

    """

    all = Enum.YLeaf(1, "all")

    active = Enum.YLeaf(2, "active")


class Trailview(Enum):
    """
    Trailview (Enum Class)

    Trailview

    .. data:: trail_view_all = 0

    	All

    .. data:: trail_view_bst = 1

    	Booster

    .. data:: trail_view_pre = 2

    	Pre

    """

    trail_view_all = Enum.YLeaf(0, "trail-view-all")

    trail_view_bst = Enum.YLeaf(1, "trail-view-bst")

    trail_view_pre = Enum.YLeaf(2, "trail-view-pre")



class HwModule(Entity):
    """
    ncs1001 hw\-module command chain
    
    .. attribute:: amplifier_trails
    
    	Amplifier trail data information
    	**type**\:  :py:class:`AmplifierTrails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_oper.HwModule.AmplifierTrails>`
    
    .. attribute:: channels_trails
    
    	Channels trail data information
    	**type**\:  :py:class:`ChannelsTrails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_oper.HwModule.ChannelsTrails>`
    
    

    """

    _prefix = 'ncs1001-ots-oper'
    _revision = '2018-01-23'

    def __init__(self):
        super(HwModule, self).__init__()
        self._top_entity = None

        self.yang_name = "hw-module"
        self.yang_parent_name = "Cisco-IOS-XR-ncs1001-ots-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("amplifier-trails", ("amplifier_trails", HwModule.AmplifierTrails)), ("channels-trails", ("channels_trails", HwModule.ChannelsTrails))])
        self._leafs = OrderedDict()

        self.amplifier_trails = HwModule.AmplifierTrails()
        self.amplifier_trails.parent = self
        self._children_name_map["amplifier_trails"] = "amplifier-trails"

        self.channels_trails = HwModule.ChannelsTrails()
        self.channels_trails.parent = self
        self._children_name_map["channels_trails"] = "channels-trails"
        self._segment_path = lambda: "Cisco-IOS-XR-ncs1001-ots-oper:hw-module"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(HwModule, [], name, value)


    class AmplifierTrails(Entity):
        """
        Amplifier trail data information
        
        .. attribute:: amplifier_trail
        
        	Slot Id
        	**type**\: list of  		 :py:class:`AmplifierTrail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_oper.HwModule.AmplifierTrails.AmplifierTrail>`
        
        

        """

        _prefix = 'ncs1001-ots-oper'
        _revision = '2018-01-23'

        def __init__(self):
            super(HwModule.AmplifierTrails, self).__init__()

            self.yang_name = "amplifier-trails"
            self.yang_parent_name = "hw-module"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("amplifier-trail", ("amplifier_trail", HwModule.AmplifierTrails.AmplifierTrail))])
            self._leafs = OrderedDict()

            self.amplifier_trail = YList(self)
            self._segment_path = lambda: "amplifier-trails"
            self._absolute_path = lambda: "Cisco-IOS-XR-ncs1001-ots-oper:hw-module/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HwModule.AmplifierTrails, [], name, value)


        class AmplifierTrail(Entity):
            """
            Slot Id
            
            .. attribute:: slot_id  (key)
            
            	Details associated with a particular slot number
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: amplifier_trail_data
            
            	Trail data information
            	**type**\: list of  		 :py:class:`AmplifierTrailData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_oper.HwModule.AmplifierTrails.AmplifierTrail.AmplifierTrailData>`
            
            

            """

            _prefix = 'ncs1001-ots-oper'
            _revision = '2018-01-23'

            def __init__(self):
                super(HwModule.AmplifierTrails.AmplifierTrail, self).__init__()

                self.yang_name = "amplifier-trail"
                self.yang_parent_name = "amplifier-trails"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['slot_id']
                self._child_classes = OrderedDict([("amplifier-trail-data", ("amplifier_trail_data", HwModule.AmplifierTrails.AmplifierTrail.AmplifierTrailData))])
                self._leafs = OrderedDict([
                    ('slot_id', (YLeaf(YType.uint32, 'slot-id'), ['int'])),
                ])
                self.slot_id = None

                self.amplifier_trail_data = YList(self)
                self._segment_path = lambda: "amplifier-trail" + "[slot-id='" + str(self.slot_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ncs1001-ots-oper:hw-module/amplifier-trails/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModule.AmplifierTrails.AmplifierTrail, ['slot_id'], name, value)


            class AmplifierTrailData(Entity):
                """
                Trail data information
                
                .. attribute:: amplifier_trail_data_type  (key)
                
                	Select trail data
                	**type**\:  :py:class:`OtsAmpliTrailData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_oper.OtsAmpliTrailData>`
                
                .. attribute:: ampli_trail_info
                
                	ampli trail info
                	**type**\: list of  		 :py:class:`AmpliTrailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_oper.HwModule.AmplifierTrails.AmplifierTrail.AmplifierTrailData.AmpliTrailInfo>`
                
                .. attribute:: channel_trail_info
                
                	channel trail info
                	**type**\: list of  		 :py:class:`ChannelTrailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_oper.HwModule.AmplifierTrails.AmplifierTrail.AmplifierTrailData.ChannelTrailInfo>`
                
                

                """

                _prefix = 'ncs1001-ots-oper'
                _revision = '2018-01-23'

                def __init__(self):
                    super(HwModule.AmplifierTrails.AmplifierTrail.AmplifierTrailData, self).__init__()

                    self.yang_name = "amplifier-trail-data"
                    self.yang_parent_name = "amplifier-trail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['amplifier_trail_data_type']
                    self._child_classes = OrderedDict([("ampli-trail-info", ("ampli_trail_info", HwModule.AmplifierTrails.AmplifierTrail.AmplifierTrailData.AmpliTrailInfo)), ("channel-trail-info", ("channel_trail_info", HwModule.AmplifierTrails.AmplifierTrail.AmplifierTrailData.ChannelTrailInfo))])
                    self._leafs = OrderedDict([
                        ('amplifier_trail_data_type', (YLeaf(YType.enumeration, 'amplifier-trail-data-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_oper', 'OtsAmpliTrailData', '')])),
                    ])
                    self.amplifier_trail_data_type = None

                    self.ampli_trail_info = YList(self)
                    self.channel_trail_info = YList(self)
                    self._segment_path = lambda: "amplifier-trail-data" + "[amplifier-trail-data-type='" + str(self.amplifier_trail_data_type) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModule.AmplifierTrails.AmplifierTrail.AmplifierTrailData, ['amplifier_trail_data_type'], name, value)


                class AmpliTrailInfo(Entity):
                    """
                    ampli trail info
                    
                    .. attribute:: eqpt_fail
                    
                    	Eqpt fail
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: view
                    
                    	View
                    	**type**\:  :py:class:`Trailview <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_oper.Trailview>`
                    
                    .. attribute:: com_port_number
                    
                    	ComPortNumber
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: com_port_name
                    
                    	ComPortName
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    .. attribute:: line_port_number
                    
                    	LinePortNumber
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: line_port_name
                    
                    	LinePortName
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    .. attribute:: bst_in_rx_power
                    
                    	BstInRxPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: bst_in_rx_total_power
                    
                    	BstInRxTotalPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: bst_in_rx_power_th_low
                    
                    	BstInRxPowerThLow
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: bst_out_tx_power
                    
                    	BstOutTxPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: bst_out_tx_total_power
                    
                    	BstOutTxTotalPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: bst_out_tx_power_th_low
                    
                    	BstOutTxPowerThLow
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: bst_working_mode
                    
                    	BstWorkingMode
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: bst_safety_mode
                    
                    	BstSafetyMode
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: bst_gain_range
                    
                    	BstGainRange
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: bst_osri
                    
                    	BstOsri
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: bst_channel_power
                    
                    	BstChannelPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: bst_gain
                    
                    	BstGain
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: bst_tilt
                    
                    	BstTilt
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: pre_in_rx_power
                    
                    	PreInRxPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: pre_in_rx_total_power
                    
                    	PreInRxTotalPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: pre_in_rx_power_th_low
                    
                    	PreInRxPowerThLow
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: pre_out_tx_power
                    
                    	PreOutTxPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: pre_out_tx_total_power
                    
                    	PreOutTxTotalPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: pre_out_tx_power_th_low
                    
                    	PreOutTxPowerThLow
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: pre_working_mode
                    
                    	PreWorkingMode
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: pre_safety_mode
                    
                    	PreSafetyMode
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: pre_gain_range
                    
                    	PreGainRange
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: pre_osri
                    
                    	PreOsri
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: pre_channel_power
                    
                    	PreChannelPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: pre_gain
                    
                    	PreGain
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: pre_tilt
                    
                    	PreTilt
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    

                    """

                    _prefix = 'ncs1001-ots-oper'
                    _revision = '2018-01-23'

                    def __init__(self):
                        super(HwModule.AmplifierTrails.AmplifierTrail.AmplifierTrailData.AmpliTrailInfo, self).__init__()

                        self.yang_name = "ampli-trail-info"
                        self.yang_parent_name = "amplifier-trail-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('eqpt_fail', (YLeaf(YType.uint8, 'eqpt-fail'), ['int'])),
                            ('view', (YLeaf(YType.enumeration, 'view'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_oper', 'Trailview', '')])),
                            ('com_port_number', (YLeaf(YType.uint8, 'com-port-number'), ['int'])),
                            ('com_port_name', (YLeaf(YType.str, 'com-port-name'), ['str'])),
                            ('line_port_number', (YLeaf(YType.uint8, 'line-port-number'), ['int'])),
                            ('line_port_name', (YLeaf(YType.str, 'line-port-name'), ['str'])),
                            ('bst_in_rx_power', (YLeaf(YType.int16, 'bst-in-rx-power'), ['int'])),
                            ('bst_in_rx_total_power', (YLeaf(YType.int16, 'bst-in-rx-total-power'), ['int'])),
                            ('bst_in_rx_power_th_low', (YLeaf(YType.int16, 'bst-in-rx-power-th-low'), ['int'])),
                            ('bst_out_tx_power', (YLeaf(YType.int16, 'bst-out-tx-power'), ['int'])),
                            ('bst_out_tx_total_power', (YLeaf(YType.int16, 'bst-out-tx-total-power'), ['int'])),
                            ('bst_out_tx_power_th_low', (YLeaf(YType.int16, 'bst-out-tx-power-th-low'), ['int'])),
                            ('bst_working_mode', (YLeaf(YType.uint16, 'bst-working-mode'), ['int'])),
                            ('bst_safety_mode', (YLeaf(YType.uint16, 'bst-safety-mode'), ['int'])),
                            ('bst_gain_range', (YLeaf(YType.uint16, 'bst-gain-range'), ['int'])),
                            ('bst_osri', (YLeaf(YType.uint16, 'bst-osri'), ['int'])),
                            ('bst_channel_power', (YLeaf(YType.int16, 'bst-channel-power'), ['int'])),
                            ('bst_gain', (YLeaf(YType.int16, 'bst-gain'), ['int'])),
                            ('bst_tilt', (YLeaf(YType.int16, 'bst-tilt'), ['int'])),
                            ('pre_in_rx_power', (YLeaf(YType.int16, 'pre-in-rx-power'), ['int'])),
                            ('pre_in_rx_total_power', (YLeaf(YType.int16, 'pre-in-rx-total-power'), ['int'])),
                            ('pre_in_rx_power_th_low', (YLeaf(YType.int16, 'pre-in-rx-power-th-low'), ['int'])),
                            ('pre_out_tx_power', (YLeaf(YType.int16, 'pre-out-tx-power'), ['int'])),
                            ('pre_out_tx_total_power', (YLeaf(YType.int16, 'pre-out-tx-total-power'), ['int'])),
                            ('pre_out_tx_power_th_low', (YLeaf(YType.int16, 'pre-out-tx-power-th-low'), ['int'])),
                            ('pre_working_mode', (YLeaf(YType.uint16, 'pre-working-mode'), ['int'])),
                            ('pre_safety_mode', (YLeaf(YType.uint16, 'pre-safety-mode'), ['int'])),
                            ('pre_gain_range', (YLeaf(YType.uint16, 'pre-gain-range'), ['int'])),
                            ('pre_osri', (YLeaf(YType.uint16, 'pre-osri'), ['int'])),
                            ('pre_channel_power', (YLeaf(YType.int16, 'pre-channel-power'), ['int'])),
                            ('pre_gain', (YLeaf(YType.int16, 'pre-gain'), ['int'])),
                            ('pre_tilt', (YLeaf(YType.int16, 'pre-tilt'), ['int'])),
                        ])
                        self.eqpt_fail = None
                        self.view = None
                        self.com_port_number = None
                        self.com_port_name = None
                        self.line_port_number = None
                        self.line_port_name = None
                        self.bst_in_rx_power = None
                        self.bst_in_rx_total_power = None
                        self.bst_in_rx_power_th_low = None
                        self.bst_out_tx_power = None
                        self.bst_out_tx_total_power = None
                        self.bst_out_tx_power_th_low = None
                        self.bst_working_mode = None
                        self.bst_safety_mode = None
                        self.bst_gain_range = None
                        self.bst_osri = None
                        self.bst_channel_power = None
                        self.bst_gain = None
                        self.bst_tilt = None
                        self.pre_in_rx_power = None
                        self.pre_in_rx_total_power = None
                        self.pre_in_rx_power_th_low = None
                        self.pre_out_tx_power = None
                        self.pre_out_tx_total_power = None
                        self.pre_out_tx_power_th_low = None
                        self.pre_working_mode = None
                        self.pre_safety_mode = None
                        self.pre_gain_range = None
                        self.pre_osri = None
                        self.pre_channel_power = None
                        self.pre_gain = None
                        self.pre_tilt = None
                        self._segment_path = lambda: "ampli-trail-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModule.AmplifierTrails.AmplifierTrail.AmplifierTrailData.AmpliTrailInfo, ['eqpt_fail', 'view', 'com_port_number', 'com_port_name', 'line_port_number', 'line_port_name', 'bst_in_rx_power', 'bst_in_rx_total_power', 'bst_in_rx_power_th_low', 'bst_out_tx_power', 'bst_out_tx_total_power', 'bst_out_tx_power_th_low', 'bst_working_mode', 'bst_safety_mode', 'bst_gain_range', 'bst_osri', 'bst_channel_power', 'bst_gain', 'bst_tilt', 'pre_in_rx_power', 'pre_in_rx_total_power', 'pre_in_rx_power_th_low', 'pre_out_tx_power', 'pre_out_tx_total_power', 'pre_out_tx_power_th_low', 'pre_working_mode', 'pre_safety_mode', 'pre_gain_range', 'pre_osri', 'pre_channel_power', 'pre_gain', 'pre_tilt'], name, value)


                class ChannelTrailInfo(Entity):
                    """
                    channel trail info
                    
                    .. attribute:: eqpt_fail
                    
                    	Eqpt fail
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: filter
                    
                    	Filter
                    	**type**\:  :py:class:`Chfilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_oper.Chfilter>`
                    
                    .. attribute:: och_name
                    
                    	OchName
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: wavelength
                    
                    	Wavelength
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: frequency
                    
                    	Frequency
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: com_port_number
                    
                    	ComPortNumber
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: com_port_name
                    
                    	ComPortName
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    .. attribute:: com_rx_power_th_low
                    
                    	ComRxPowerThLow
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: line_port_number
                    
                    	LinePortNumber
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: line_port_name
                    
                    	LinePortName
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    .. attribute:: line_rx_power_th_low
                    
                    	LineRxPowerThLow
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: bst_in_rx_power
                    
                    	BstInRxPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: bst_out_tx_power
                    
                    	BstOutTxPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: pre_in_rx_power
                    
                    	PreInRxPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: pre_out_tx_power
                    
                    	PreOutTxPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    

                    """

                    _prefix = 'ncs1001-ots-oper'
                    _revision = '2018-01-23'

                    def __init__(self):
                        super(HwModule.AmplifierTrails.AmplifierTrail.AmplifierTrailData.ChannelTrailInfo, self).__init__()

                        self.yang_name = "channel-trail-info"
                        self.yang_parent_name = "amplifier-trail-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('eqpt_fail', (YLeaf(YType.uint8, 'eqpt-fail'), ['int'])),
                            ('filter', (YLeaf(YType.enumeration, 'filter'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_oper', 'Chfilter', '')])),
                            ('och_name', (YLeaf(YType.str, 'och-name'), ['str'])),
                            ('wavelength', (YLeaf(YType.uint32, 'wavelength'), ['int'])),
                            ('frequency', (YLeaf(YType.uint32, 'frequency'), ['int'])),
                            ('com_port_number', (YLeaf(YType.uint8, 'com-port-number'), ['int'])),
                            ('com_port_name', (YLeaf(YType.str, 'com-port-name'), ['str'])),
                            ('com_rx_power_th_low', (YLeaf(YType.int16, 'com-rx-power-th-low'), ['int'])),
                            ('line_port_number', (YLeaf(YType.uint8, 'line-port-number'), ['int'])),
                            ('line_port_name', (YLeaf(YType.str, 'line-port-name'), ['str'])),
                            ('line_rx_power_th_low', (YLeaf(YType.int16, 'line-rx-power-th-low'), ['int'])),
                            ('bst_in_rx_power', (YLeaf(YType.int16, 'bst-in-rx-power'), ['int'])),
                            ('bst_out_tx_power', (YLeaf(YType.int16, 'bst-out-tx-power'), ['int'])),
                            ('pre_in_rx_power', (YLeaf(YType.int16, 'pre-in-rx-power'), ['int'])),
                            ('pre_out_tx_power', (YLeaf(YType.int16, 'pre-out-tx-power'), ['int'])),
                        ])
                        self.eqpt_fail = None
                        self.filter = None
                        self.och_name = None
                        self.wavelength = None
                        self.frequency = None
                        self.com_port_number = None
                        self.com_port_name = None
                        self.com_rx_power_th_low = None
                        self.line_port_number = None
                        self.line_port_name = None
                        self.line_rx_power_th_low = None
                        self.bst_in_rx_power = None
                        self.bst_out_tx_power = None
                        self.pre_in_rx_power = None
                        self.pre_out_tx_power = None
                        self._segment_path = lambda: "channel-trail-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModule.AmplifierTrails.AmplifierTrail.AmplifierTrailData.ChannelTrailInfo, ['eqpt_fail', 'filter', 'och_name', 'wavelength', 'frequency', 'com_port_number', 'com_port_name', 'com_rx_power_th_low', 'line_port_number', 'line_port_name', 'line_rx_power_th_low', 'bst_in_rx_power', 'bst_out_tx_power', 'pre_in_rx_power', 'pre_out_tx_power'], name, value)


    class ChannelsTrails(Entity):
        """
        Channels trail data information
        
        .. attribute:: channels_trail
        
        	Slot Id
        	**type**\: list of  		 :py:class:`ChannelsTrail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_oper.HwModule.ChannelsTrails.ChannelsTrail>`
        
        

        """

        _prefix = 'ncs1001-ots-oper'
        _revision = '2018-01-23'

        def __init__(self):
            super(HwModule.ChannelsTrails, self).__init__()

            self.yang_name = "channels-trails"
            self.yang_parent_name = "hw-module"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("channels-trail", ("channels_trail", HwModule.ChannelsTrails.ChannelsTrail))])
            self._leafs = OrderedDict()

            self.channels_trail = YList(self)
            self._segment_path = lambda: "channels-trails"
            self._absolute_path = lambda: "Cisco-IOS-XR-ncs1001-ots-oper:hw-module/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HwModule.ChannelsTrails, [], name, value)


        class ChannelsTrail(Entity):
            """
            Slot Id
            
            .. attribute:: slot_id  (key)
            
            	Details associated with a particular slot number
            	**type**\: int
            
            	**range:** 1..3
            
            .. attribute:: channels_trail_data
            
            	Trail data information
            	**type**\: list of  		 :py:class:`ChannelsTrailData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_oper.HwModule.ChannelsTrails.ChannelsTrail.ChannelsTrailData>`
            
            

            """

            _prefix = 'ncs1001-ots-oper'
            _revision = '2018-01-23'

            def __init__(self):
                super(HwModule.ChannelsTrails.ChannelsTrail, self).__init__()

                self.yang_name = "channels-trail"
                self.yang_parent_name = "channels-trails"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['slot_id']
                self._child_classes = OrderedDict([("channels-trail-data", ("channels_trail_data", HwModule.ChannelsTrails.ChannelsTrail.ChannelsTrailData))])
                self._leafs = OrderedDict([
                    ('slot_id', (YLeaf(YType.uint32, 'slot-id'), ['int'])),
                ])
                self.slot_id = None

                self.channels_trail_data = YList(self)
                self._segment_path = lambda: "channels-trail" + "[slot-id='" + str(self.slot_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ncs1001-ots-oper:hw-module/channels-trails/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModule.ChannelsTrails.ChannelsTrail, ['slot_id'], name, value)


            class ChannelsTrailData(Entity):
                """
                Trail data information
                
                .. attribute:: channels_trail_data_type  (key)
                
                	Select trail data
                	**type**\:  :py:class:`OtsChannelsTrailData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_oper.OtsChannelsTrailData>`
                
                .. attribute:: ampli_trail_info
                
                	ampli trail info
                	**type**\: list of  		 :py:class:`AmpliTrailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_oper.HwModule.ChannelsTrails.ChannelsTrail.ChannelsTrailData.AmpliTrailInfo>`
                
                .. attribute:: channel_trail_info
                
                	channel trail info
                	**type**\: list of  		 :py:class:`ChannelTrailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_oper.HwModule.ChannelsTrails.ChannelsTrail.ChannelsTrailData.ChannelTrailInfo>`
                
                

                """

                _prefix = 'ncs1001-ots-oper'
                _revision = '2018-01-23'

                def __init__(self):
                    super(HwModule.ChannelsTrails.ChannelsTrail.ChannelsTrailData, self).__init__()

                    self.yang_name = "channels-trail-data"
                    self.yang_parent_name = "channels-trail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['channels_trail_data_type']
                    self._child_classes = OrderedDict([("ampli-trail-info", ("ampli_trail_info", HwModule.ChannelsTrails.ChannelsTrail.ChannelsTrailData.AmpliTrailInfo)), ("channel-trail-info", ("channel_trail_info", HwModule.ChannelsTrails.ChannelsTrail.ChannelsTrailData.ChannelTrailInfo))])
                    self._leafs = OrderedDict([
                        ('channels_trail_data_type', (YLeaf(YType.enumeration, 'channels-trail-data-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_oper', 'OtsChannelsTrailData', '')])),
                    ])
                    self.channels_trail_data_type = None

                    self.ampli_trail_info = YList(self)
                    self.channel_trail_info = YList(self)
                    self._segment_path = lambda: "channels-trail-data" + "[channels-trail-data-type='" + str(self.channels_trail_data_type) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModule.ChannelsTrails.ChannelsTrail.ChannelsTrailData, ['channels_trail_data_type'], name, value)


                class AmpliTrailInfo(Entity):
                    """
                    ampli trail info
                    
                    .. attribute:: eqpt_fail
                    
                    	Eqpt fail
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: view
                    
                    	View
                    	**type**\:  :py:class:`Trailview <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_oper.Trailview>`
                    
                    .. attribute:: com_port_number
                    
                    	ComPortNumber
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: com_port_name
                    
                    	ComPortName
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    .. attribute:: line_port_number
                    
                    	LinePortNumber
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: line_port_name
                    
                    	LinePortName
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    .. attribute:: bst_in_rx_power
                    
                    	BstInRxPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: bst_in_rx_total_power
                    
                    	BstInRxTotalPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: bst_in_rx_power_th_low
                    
                    	BstInRxPowerThLow
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: bst_out_tx_power
                    
                    	BstOutTxPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: bst_out_tx_total_power
                    
                    	BstOutTxTotalPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: bst_out_tx_power_th_low
                    
                    	BstOutTxPowerThLow
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: bst_working_mode
                    
                    	BstWorkingMode
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: bst_safety_mode
                    
                    	BstSafetyMode
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: bst_gain_range
                    
                    	BstGainRange
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: bst_osri
                    
                    	BstOsri
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: bst_channel_power
                    
                    	BstChannelPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: bst_gain
                    
                    	BstGain
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: bst_tilt
                    
                    	BstTilt
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: pre_in_rx_power
                    
                    	PreInRxPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: pre_in_rx_total_power
                    
                    	PreInRxTotalPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: pre_in_rx_power_th_low
                    
                    	PreInRxPowerThLow
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: pre_out_tx_power
                    
                    	PreOutTxPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: pre_out_tx_total_power
                    
                    	PreOutTxTotalPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: pre_out_tx_power_th_low
                    
                    	PreOutTxPowerThLow
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: pre_working_mode
                    
                    	PreWorkingMode
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: pre_safety_mode
                    
                    	PreSafetyMode
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: pre_gain_range
                    
                    	PreGainRange
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: pre_osri
                    
                    	PreOsri
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: pre_channel_power
                    
                    	PreChannelPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: pre_gain
                    
                    	PreGain
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: pre_tilt
                    
                    	PreTilt
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    

                    """

                    _prefix = 'ncs1001-ots-oper'
                    _revision = '2018-01-23'

                    def __init__(self):
                        super(HwModule.ChannelsTrails.ChannelsTrail.ChannelsTrailData.AmpliTrailInfo, self).__init__()

                        self.yang_name = "ampli-trail-info"
                        self.yang_parent_name = "channels-trail-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('eqpt_fail', (YLeaf(YType.uint8, 'eqpt-fail'), ['int'])),
                            ('view', (YLeaf(YType.enumeration, 'view'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_oper', 'Trailview', '')])),
                            ('com_port_number', (YLeaf(YType.uint8, 'com-port-number'), ['int'])),
                            ('com_port_name', (YLeaf(YType.str, 'com-port-name'), ['str'])),
                            ('line_port_number', (YLeaf(YType.uint8, 'line-port-number'), ['int'])),
                            ('line_port_name', (YLeaf(YType.str, 'line-port-name'), ['str'])),
                            ('bst_in_rx_power', (YLeaf(YType.int16, 'bst-in-rx-power'), ['int'])),
                            ('bst_in_rx_total_power', (YLeaf(YType.int16, 'bst-in-rx-total-power'), ['int'])),
                            ('bst_in_rx_power_th_low', (YLeaf(YType.int16, 'bst-in-rx-power-th-low'), ['int'])),
                            ('bst_out_tx_power', (YLeaf(YType.int16, 'bst-out-tx-power'), ['int'])),
                            ('bst_out_tx_total_power', (YLeaf(YType.int16, 'bst-out-tx-total-power'), ['int'])),
                            ('bst_out_tx_power_th_low', (YLeaf(YType.int16, 'bst-out-tx-power-th-low'), ['int'])),
                            ('bst_working_mode', (YLeaf(YType.uint16, 'bst-working-mode'), ['int'])),
                            ('bst_safety_mode', (YLeaf(YType.uint16, 'bst-safety-mode'), ['int'])),
                            ('bst_gain_range', (YLeaf(YType.uint16, 'bst-gain-range'), ['int'])),
                            ('bst_osri', (YLeaf(YType.uint16, 'bst-osri'), ['int'])),
                            ('bst_channel_power', (YLeaf(YType.int16, 'bst-channel-power'), ['int'])),
                            ('bst_gain', (YLeaf(YType.int16, 'bst-gain'), ['int'])),
                            ('bst_tilt', (YLeaf(YType.int16, 'bst-tilt'), ['int'])),
                            ('pre_in_rx_power', (YLeaf(YType.int16, 'pre-in-rx-power'), ['int'])),
                            ('pre_in_rx_total_power', (YLeaf(YType.int16, 'pre-in-rx-total-power'), ['int'])),
                            ('pre_in_rx_power_th_low', (YLeaf(YType.int16, 'pre-in-rx-power-th-low'), ['int'])),
                            ('pre_out_tx_power', (YLeaf(YType.int16, 'pre-out-tx-power'), ['int'])),
                            ('pre_out_tx_total_power', (YLeaf(YType.int16, 'pre-out-tx-total-power'), ['int'])),
                            ('pre_out_tx_power_th_low', (YLeaf(YType.int16, 'pre-out-tx-power-th-low'), ['int'])),
                            ('pre_working_mode', (YLeaf(YType.uint16, 'pre-working-mode'), ['int'])),
                            ('pre_safety_mode', (YLeaf(YType.uint16, 'pre-safety-mode'), ['int'])),
                            ('pre_gain_range', (YLeaf(YType.uint16, 'pre-gain-range'), ['int'])),
                            ('pre_osri', (YLeaf(YType.uint16, 'pre-osri'), ['int'])),
                            ('pre_channel_power', (YLeaf(YType.int16, 'pre-channel-power'), ['int'])),
                            ('pre_gain', (YLeaf(YType.int16, 'pre-gain'), ['int'])),
                            ('pre_tilt', (YLeaf(YType.int16, 'pre-tilt'), ['int'])),
                        ])
                        self.eqpt_fail = None
                        self.view = None
                        self.com_port_number = None
                        self.com_port_name = None
                        self.line_port_number = None
                        self.line_port_name = None
                        self.bst_in_rx_power = None
                        self.bst_in_rx_total_power = None
                        self.bst_in_rx_power_th_low = None
                        self.bst_out_tx_power = None
                        self.bst_out_tx_total_power = None
                        self.bst_out_tx_power_th_low = None
                        self.bst_working_mode = None
                        self.bst_safety_mode = None
                        self.bst_gain_range = None
                        self.bst_osri = None
                        self.bst_channel_power = None
                        self.bst_gain = None
                        self.bst_tilt = None
                        self.pre_in_rx_power = None
                        self.pre_in_rx_total_power = None
                        self.pre_in_rx_power_th_low = None
                        self.pre_out_tx_power = None
                        self.pre_out_tx_total_power = None
                        self.pre_out_tx_power_th_low = None
                        self.pre_working_mode = None
                        self.pre_safety_mode = None
                        self.pre_gain_range = None
                        self.pre_osri = None
                        self.pre_channel_power = None
                        self.pre_gain = None
                        self.pre_tilt = None
                        self._segment_path = lambda: "ampli-trail-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModule.ChannelsTrails.ChannelsTrail.ChannelsTrailData.AmpliTrailInfo, ['eqpt_fail', 'view', 'com_port_number', 'com_port_name', 'line_port_number', 'line_port_name', 'bst_in_rx_power', 'bst_in_rx_total_power', 'bst_in_rx_power_th_low', 'bst_out_tx_power', 'bst_out_tx_total_power', 'bst_out_tx_power_th_low', 'bst_working_mode', 'bst_safety_mode', 'bst_gain_range', 'bst_osri', 'bst_channel_power', 'bst_gain', 'bst_tilt', 'pre_in_rx_power', 'pre_in_rx_total_power', 'pre_in_rx_power_th_low', 'pre_out_tx_power', 'pre_out_tx_total_power', 'pre_out_tx_power_th_low', 'pre_working_mode', 'pre_safety_mode', 'pre_gain_range', 'pre_osri', 'pre_channel_power', 'pre_gain', 'pre_tilt'], name, value)


                class ChannelTrailInfo(Entity):
                    """
                    channel trail info
                    
                    .. attribute:: eqpt_fail
                    
                    	Eqpt fail
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: filter
                    
                    	Filter
                    	**type**\:  :py:class:`Chfilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_oper.Chfilter>`
                    
                    .. attribute:: och_name
                    
                    	OchName
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: wavelength
                    
                    	Wavelength
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: frequency
                    
                    	Frequency
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: com_port_number
                    
                    	ComPortNumber
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: com_port_name
                    
                    	ComPortName
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    .. attribute:: com_rx_power_th_low
                    
                    	ComRxPowerThLow
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: line_port_number
                    
                    	LinePortNumber
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: line_port_name
                    
                    	LinePortName
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    .. attribute:: line_rx_power_th_low
                    
                    	LineRxPowerThLow
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: bst_in_rx_power
                    
                    	BstInRxPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: bst_out_tx_power
                    
                    	BstOutTxPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: pre_in_rx_power
                    
                    	PreInRxPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    .. attribute:: pre_out_tx_power
                    
                    	PreOutTxPower
                    	**type**\: int
                    
                    	**range:** \-32768..32767
                    
                    

                    """

                    _prefix = 'ncs1001-ots-oper'
                    _revision = '2018-01-23'

                    def __init__(self):
                        super(HwModule.ChannelsTrails.ChannelsTrail.ChannelsTrailData.ChannelTrailInfo, self).__init__()

                        self.yang_name = "channel-trail-info"
                        self.yang_parent_name = "channels-trail-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('eqpt_fail', (YLeaf(YType.uint8, 'eqpt-fail'), ['int'])),
                            ('filter', (YLeaf(YType.enumeration, 'filter'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_oper', 'Chfilter', '')])),
                            ('och_name', (YLeaf(YType.str, 'och-name'), ['str'])),
                            ('wavelength', (YLeaf(YType.uint32, 'wavelength'), ['int'])),
                            ('frequency', (YLeaf(YType.uint32, 'frequency'), ['int'])),
                            ('com_port_number', (YLeaf(YType.uint8, 'com-port-number'), ['int'])),
                            ('com_port_name', (YLeaf(YType.str, 'com-port-name'), ['str'])),
                            ('com_rx_power_th_low', (YLeaf(YType.int16, 'com-rx-power-th-low'), ['int'])),
                            ('line_port_number', (YLeaf(YType.uint8, 'line-port-number'), ['int'])),
                            ('line_port_name', (YLeaf(YType.str, 'line-port-name'), ['str'])),
                            ('line_rx_power_th_low', (YLeaf(YType.int16, 'line-rx-power-th-low'), ['int'])),
                            ('bst_in_rx_power', (YLeaf(YType.int16, 'bst-in-rx-power'), ['int'])),
                            ('bst_out_tx_power', (YLeaf(YType.int16, 'bst-out-tx-power'), ['int'])),
                            ('pre_in_rx_power', (YLeaf(YType.int16, 'pre-in-rx-power'), ['int'])),
                            ('pre_out_tx_power', (YLeaf(YType.int16, 'pre-out-tx-power'), ['int'])),
                        ])
                        self.eqpt_fail = None
                        self.filter = None
                        self.och_name = None
                        self.wavelength = None
                        self.frequency = None
                        self.com_port_number = None
                        self.com_port_name = None
                        self.com_rx_power_th_low = None
                        self.line_port_number = None
                        self.line_port_name = None
                        self.line_rx_power_th_low = None
                        self.bst_in_rx_power = None
                        self.bst_out_tx_power = None
                        self.pre_in_rx_power = None
                        self.pre_out_tx_power = None
                        self._segment_path = lambda: "channel-trail-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModule.ChannelsTrails.ChannelsTrail.ChannelsTrailData.ChannelTrailInfo, ['eqpt_fail', 'filter', 'och_name', 'wavelength', 'frequency', 'com_port_number', 'com_port_name', 'com_rx_power_th_low', 'line_port_number', 'line_port_name', 'line_rx_power_th_low', 'bst_in_rx_power', 'bst_out_tx_power', 'pre_in_rx_power', 'pre_out_tx_power'], name, value)

    def clone_ptr(self):
        self._top_entity = HwModule()
        return self._top_entity


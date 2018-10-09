""" Cisco_IOS_XR_ncs1001_ots_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs1001\-ots package configuration.

This module contains definitions
for the following management objects\:
  hardware\-module\: NCS1k HW module config

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class OtsAmplifierGridMode(Enum):
    """
    OtsAmplifierGridMode (Enum Class)

    Ots amplifier grid mode

    .. data:: Y_100g_hz = 0

    	100GHz mode

    .. data:: Y_50g_hz = 1

    	50GHz mode

    .. data:: gr_idle_ss = 2

    	Gridless mode

    """

    Y_100g_hz = Enum.YLeaf(0, "100g-hz")

    Y_50g_hz = Enum.YLeaf(1, "50g-hz")

    gr_idle_ss = Enum.YLeaf(2, "gr-idle-ss")


class OtsAmplifierNode(Enum):
    """
    OtsAmplifierNode (Enum Class)

    Ots amplifier node

    .. data:: term = 0

    	Nodetype TERM

    .. data:: ila = 1

    	Nodetype InLine Amplifier

    .. data:: roadm = 2

    	Nodetype ROADM

    """

    term = Enum.YLeaf(0, "term")

    ila = Enum.YLeaf(1, "ila")

    roadm = Enum.YLeaf(2, "roadm")


class OtsOtdrDirection(Enum):
    """
    OtsOtdrDirection (Enum Class)

    Ots otdr direction

    .. data:: tx = 0

    	Tx

    .. data:: rx = 1

    	Rx

    """

    tx = Enum.YLeaf(0, "tx")

    rx = Enum.YLeaf(1, "rx")


class OtsPsmLockoutFrom(Enum):
    """
    OtsPsmLockoutFrom (Enum Class)

    Ots psm lockout from

    .. data:: working = 1

    	Working port

    .. data:: protected = 2

    	Protected port

    """

    working = Enum.YLeaf(1, "working")

    protected = Enum.YLeaf(2, "protected")



class HardwareModule(Entity):
    """
    NCS1k HW module config
    
    .. attribute:: node
    
    	Node
    	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg.HardwareModule.Node>`
    
    

    """

    _prefix = 'ncs1001-ots-cfg'
    _revision = '2018-03-20'

    def __init__(self):
        super(HardwareModule, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module"
        self.yang_parent_name = "Cisco-IOS-XR-ncs1001-ots-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("node", ("node", HardwareModule.Node))])
        self._leafs = OrderedDict()

        self.node = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-ncs1001-ots-cfg:hardware-module"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(HardwareModule, [], name, value)


    class Node(Entity):
        """
        Node
        
        .. attribute:: location  (key)
        
        	Fully qualified line card specification
        	**type**\: str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: slot
        
        	Slot Id
        	**type**\: list of  		 :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg.HardwareModule.Node.Slot>`
        
        

        """

        _prefix = 'ncs1001-ots-cfg'
        _revision = '2018-03-20'

        def __init__(self):
            super(HardwareModule.Node, self).__init__()

            self.yang_name = "node"
            self.yang_parent_name = "hardware-module"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['location']
            self._child_classes = OrderedDict([("slot", ("slot", HardwareModule.Node.Slot))])
            self._leafs = OrderedDict([
                ('location', (YLeaf(YType.str, 'location'), ['str'])),
            ])
            self.location = None

            self.slot = YList(self)
            self._segment_path = lambda: "node" + "[location='" + str(self.location) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-ncs1001-ots-cfg:hardware-module/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HardwareModule.Node, ['location'], name, value)


        class Slot(Entity):
            """
            Slot Id
            
            .. attribute:: slot_id  (key)
            
            	Set Slot
            	**type**\: int
            
            	**range:** 1..3
            
            .. attribute:: otdrs
            
            	OTDR Configs
            	**type**\:  :py:class:`Otdrs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg.HardwareModule.Node.Slot.Otdrs>`
            
            .. attribute:: otdr_thresholds
            
            	Otdr Threshold
            	**type**\:  :py:class:`OtdrThresholds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg.HardwareModule.Node.Slot.OtdrThresholds>`
            
            .. attribute:: amplifier
            
            	Amplifier Configs
            	**type**\:  :py:class:`Amplifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg.HardwareModule.Node.Slot.Amplifier>`
            
            .. attribute:: psm
            
            	PSM Configs
            	**type**\:  :py:class:`Psm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg.HardwareModule.Node.Slot.Psm>`
            
            

            """

            _prefix = 'ncs1001-ots-cfg'
            _revision = '2018-03-20'

            def __init__(self):
                super(HardwareModule.Node.Slot, self).__init__()

                self.yang_name = "slot"
                self.yang_parent_name = "node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['slot_id']
                self._child_classes = OrderedDict([("otdrs", ("otdrs", HardwareModule.Node.Slot.Otdrs)), ("otdr-thresholds", ("otdr_thresholds", HardwareModule.Node.Slot.OtdrThresholds)), ("amplifier", ("amplifier", HardwareModule.Node.Slot.Amplifier)), ("psm", ("psm", HardwareModule.Node.Slot.Psm))])
                self._leafs = OrderedDict([
                    ('slot_id', (YLeaf(YType.uint32, 'slot-id'), ['int'])),
                ])
                self.slot_id = None

                self.otdrs = HardwareModule.Node.Slot.Otdrs()
                self.otdrs.parent = self
                self._children_name_map["otdrs"] = "otdrs"

                self.otdr_thresholds = HardwareModule.Node.Slot.OtdrThresholds()
                self.otdr_thresholds.parent = self
                self._children_name_map["otdr_thresholds"] = "otdr-thresholds"

                self.amplifier = HardwareModule.Node.Slot.Amplifier()
                self.amplifier.parent = self
                self._children_name_map["amplifier"] = "amplifier"

                self.psm = HardwareModule.Node.Slot.Psm()
                self.psm.parent = self
                self._children_name_map["psm"] = "psm"
                self._segment_path = lambda: "slot" + "[slot-id='" + str(self.slot_id) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HardwareModule.Node.Slot, ['slot_id'], name, value)


            class Otdrs(Entity):
                """
                OTDR Configs
                
                .. attribute:: otdr
                
                	Otdr Id
                	**type**\: list of  		 :py:class:`Otdr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg.HardwareModule.Node.Slot.Otdrs.Otdr>`
                
                

                """

                _prefix = 'ncs1001-ots-cfg'
                _revision = '2018-03-20'

                def __init__(self):
                    super(HardwareModule.Node.Slot.Otdrs, self).__init__()

                    self.yang_name = "otdrs"
                    self.yang_parent_name = "slot"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("otdr", ("otdr", HardwareModule.Node.Slot.Otdrs.Otdr))])
                    self._leafs = OrderedDict()

                    self.otdr = YList(self)
                    self._segment_path = lambda: "otdrs"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HardwareModule.Node.Slot.Otdrs, [], name, value)


                class Otdr(Entity):
                    """
                    Otdr Id
                    
                    .. attribute:: port  (key)
                    
                    	Port Id
                    	**type**\: int
                    
                    	**range:** 1..2
                    
                    .. attribute:: direction  (key)
                    
                    	Direction Id
                    	**type**\:  :py:class:`OtsOtdrDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg.OtsOtdrDirection>`
                    
                    .. attribute:: mode_auto
                    
                    	Mode Auto
                    	**type**\:  :py:class:`ModeAuto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg.HardwareModule.Node.Slot.Otdrs.Otdr.ModeAuto>`
                    
                    .. attribute:: mode_expert
                    
                    	Mode Expert
                    	**type**\:  :py:class:`ModeExpert <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg.HardwareModule.Node.Slot.Otdrs.Otdr.ModeExpert>`
                    
                    .. attribute:: total_loss
                    
                    	Otdr Insertion Loss, supported values [0 ,500] in units of 0.1dB
                    	**type**\: int
                    
                    	**range:** 0..500
                    
                    

                    """

                    _prefix = 'ncs1001-ots-cfg'
                    _revision = '2018-03-20'

                    def __init__(self):
                        super(HardwareModule.Node.Slot.Otdrs.Otdr, self).__init__()

                        self.yang_name = "otdr"
                        self.yang_parent_name = "otdrs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['port','direction']
                        self._child_classes = OrderedDict([("mode-auto", ("mode_auto", HardwareModule.Node.Slot.Otdrs.Otdr.ModeAuto)), ("mode-expert", ("mode_expert", HardwareModule.Node.Slot.Otdrs.Otdr.ModeExpert))])
                        self._leafs = OrderedDict([
                            ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                            ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg', 'OtsOtdrDirection', '')])),
                            ('total_loss', (YLeaf(YType.uint32, 'total-loss'), ['int'])),
                        ])
                        self.port = None
                        self.direction = None
                        self.total_loss = None

                        self.mode_auto = HardwareModule.Node.Slot.Otdrs.Otdr.ModeAuto()
                        self.mode_auto.parent = self
                        self._children_name_map["mode_auto"] = "mode-auto"

                        self.mode_expert = HardwareModule.Node.Slot.Otdrs.Otdr.ModeExpert()
                        self.mode_expert.parent = self
                        self._children_name_map["mode_expert"] = "mode-expert"
                        self._segment_path = lambda: "otdr" + "[port='" + str(self.port) + "']" + "[direction='" + str(self.direction) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HardwareModule.Node.Slot.Otdrs.Otdr, ['port', 'direction', 'total_loss'], name, value)


                    class ModeAuto(Entity):
                        """
                        Mode Auto
                        
                        .. attribute:: loss_sensitivity
                        
                        	Otdr Loss Sensitivity, supported values [4 ,50] in units of 0.1dB
                        	**type**\: int
                        
                        	**range:** 4..50
                        
                        .. attribute:: reflection_sensitivity
                        
                        	Otdr Reflection Sensitivity, supported values [\-400,\-140] in units of 0.1dB
                        	**type**\: int
                        
                        	**range:** \-400..\-140
                        
                        

                        """

                        _prefix = 'ncs1001-ots-cfg'
                        _revision = '2018-03-20'

                        def __init__(self):
                            super(HardwareModule.Node.Slot.Otdrs.Otdr.ModeAuto, self).__init__()

                            self.yang_name = "mode-auto"
                            self.yang_parent_name = "otdr"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('loss_sensitivity', (YLeaf(YType.uint32, 'loss-sensitivity'), ['int'])),
                                ('reflection_sensitivity', (YLeaf(YType.int32, 'reflection-sensitivity'), ['int'])),
                            ])
                            self.loss_sensitivity = None
                            self.reflection_sensitivity = None
                            self._segment_path = lambda: "mode-auto"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HardwareModule.Node.Slot.Otdrs.Otdr.ModeAuto, ['loss_sensitivity', 'reflection_sensitivity'], name, value)


                    class ModeExpert(Entity):
                        """
                        Mode Expert
                        
                        .. attribute:: fiber_resolution
                        
                        	Fiber Resolution in meters, supported values [0,100]
                        	**type**\: int
                        
                        	**range:** 0..100
                        
                        .. attribute:: capture_length
                        
                        	Capture Length in Km, supported values [0 ,150]
                        	**type**\: int
                        
                        	**range:** 0..150
                        
                        .. attribute:: pulse_width
                        
                        	Pulse Width in nanoseconds, supported values [8,100000]
                        	**type**\: int
                        
                        	**range:** 8..100000
                        
                        	**units**\: nanosecond
                        
                        .. attribute:: measure_time
                        
                        	Measure time in seconds, supported values [0,360]
                        	**type**\: int
                        
                        	**range:** 0..360
                        
                        	**units**\: second
                        
                        .. attribute:: loss_sensitivity
                        
                        	Otdr Loss Sensitivity, supported values [4 ,50] in units of 0.1dB
                        	**type**\: int
                        
                        	**range:** 4..50
                        
                        .. attribute:: capture_offset
                        
                        	Capture Offset in Km, supported values [0 ,150]
                        	**type**\: int
                        
                        	**range:** 0..150
                        
                        .. attribute:: span_length
                        
                        	Span Length in Km, supported values [0,150]
                        	**type**\: int
                        
                        	**range:** 0..150
                        
                        .. attribute:: reflection_sensitivity
                        
                        	Otdr Reflection Sensitivity, supported values [\-400,\-140] in units of 0.1dB
                        	**type**\: int
                        
                        	**range:** \-400..\-140
                        
                        

                        """

                        _prefix = 'ncs1001-ots-cfg'
                        _revision = '2018-03-20'

                        def __init__(self):
                            super(HardwareModule.Node.Slot.Otdrs.Otdr.ModeExpert, self).__init__()

                            self.yang_name = "mode-expert"
                            self.yang_parent_name = "otdr"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('fiber_resolution', (YLeaf(YType.uint32, 'fiber-resolution'), ['int'])),
                                ('capture_length', (YLeaf(YType.uint32, 'capture-length'), ['int'])),
                                ('pulse_width', (YLeaf(YType.uint32, 'pulse-width'), ['int'])),
                                ('measure_time', (YLeaf(YType.uint32, 'measure-time'), ['int'])),
                                ('loss_sensitivity', (YLeaf(YType.uint32, 'loss-sensitivity'), ['int'])),
                                ('capture_offset', (YLeaf(YType.uint32, 'capture-offset'), ['int'])),
                                ('span_length', (YLeaf(YType.uint32, 'span-length'), ['int'])),
                                ('reflection_sensitivity', (YLeaf(YType.int32, 'reflection-sensitivity'), ['int'])),
                            ])
                            self.fiber_resolution = None
                            self.capture_length = None
                            self.pulse_width = None
                            self.measure_time = None
                            self.loss_sensitivity = None
                            self.capture_offset = None
                            self.span_length = None
                            self.reflection_sensitivity = None
                            self._segment_path = lambda: "mode-expert"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HardwareModule.Node.Slot.Otdrs.Otdr.ModeExpert, ['fiber_resolution', 'capture_length', 'pulse_width', 'measure_time', 'loss_sensitivity', 'capture_offset', 'span_length', 'reflection_sensitivity'], name, value)


            class OtdrThresholds(Entity):
                """
                Otdr Threshold
                
                .. attribute:: otdr_threshold
                
                	Otdr Threshold
                	**type**\: list of  		 :py:class:`OtdrThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg.HardwareModule.Node.Slot.OtdrThresholds.OtdrThreshold>`
                
                

                """

                _prefix = 'ncs1001-ots-cfg'
                _revision = '2018-03-20'

                def __init__(self):
                    super(HardwareModule.Node.Slot.OtdrThresholds, self).__init__()

                    self.yang_name = "otdr-thresholds"
                    self.yang_parent_name = "slot"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("otdr-threshold", ("otdr_threshold", HardwareModule.Node.Slot.OtdrThresholds.OtdrThreshold))])
                    self._leafs = OrderedDict()

                    self.otdr_threshold = YList(self)
                    self._segment_path = lambda: "otdr-thresholds"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HardwareModule.Node.Slot.OtdrThresholds, [], name, value)


                class OtdrThreshold(Entity):
                    """
                    Otdr Threshold
                    
                    .. attribute:: port  (key)
                    
                    	Port Id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: loss_abs_threshold
                    
                    	Absolute Loss Threshold, supported values [1 ,300] in units of 0.1dB
                    	**type**\: int
                    
                    	**range:** 1..300
                    
                    .. attribute:: reflection_abs_threshold
                    
                    	Absolute Reflection Threshold, supported values [\-500,0] in units of 0.1dB
                    	**type**\: int
                    
                    	**range:** \-500..0
                    
                    .. attribute:: orl_abs_threshold
                    
                    	Absolute Orl Threshold, supported values [140,400] in units of 0.1dB
                    	**type**\: int
                    
                    	**range:** 140..400
                    
                    

                    """

                    _prefix = 'ncs1001-ots-cfg'
                    _revision = '2018-03-20'

                    def __init__(self):
                        super(HardwareModule.Node.Slot.OtdrThresholds.OtdrThreshold, self).__init__()

                        self.yang_name = "otdr-threshold"
                        self.yang_parent_name = "otdr-thresholds"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['port']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                            ('loss_abs_threshold', (YLeaf(YType.uint32, 'loss-abs-threshold'), ['int'])),
                            ('reflection_abs_threshold', (YLeaf(YType.int32, 'reflection-abs-threshold'), ['int'])),
                            ('orl_abs_threshold', (YLeaf(YType.uint32, 'orl-abs-threshold'), ['int'])),
                        ])
                        self.port = None
                        self.loss_abs_threshold = None
                        self.reflection_abs_threshold = None
                        self.orl_abs_threshold = None
                        self._segment_path = lambda: "otdr-threshold" + "[port='" + str(self.port) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HardwareModule.Node.Slot.OtdrThresholds.OtdrThreshold, ['port', 'loss_abs_threshold', 'reflection_abs_threshold', 'orl_abs_threshold'], name, value)


            class Amplifier(Entity):
                """
                Amplifier Configs
                
                .. attribute:: remote_node
                
                	RemoteNode Configuration
                	**type**\:  :py:class:`RemoteNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg.HardwareModule.Node.Slot.Amplifier.RemoteNode>`
                
                .. attribute:: node_type
                
                	Define the type of node in which the amplifier is set to work
                	**type**\:  :py:class:`OtsAmplifierNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg.OtsAmplifierNode>`
                
                .. attribute:: grid_mode
                
                	Define the working mode for the optical module
                	**type**\:  :py:class:`OtsAmplifierGridMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg.OtsAmplifierGridMode>`
                
                .. attribute:: udc_vlan
                
                	Define the VLAN ID in range <2\-4080>
                	**type**\: int
                
                	**range:** 2..4080
                
                .. attribute:: span_loss
                
                	SpanLoss configuration
                	**type**\: bool
                
                

                """

                _prefix = 'ncs1001-ots-cfg'
                _revision = '2018-03-20'

                def __init__(self):
                    super(HardwareModule.Node.Slot.Amplifier, self).__init__()

                    self.yang_name = "amplifier"
                    self.yang_parent_name = "slot"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("remote-node", ("remote_node", HardwareModule.Node.Slot.Amplifier.RemoteNode))])
                    self._leafs = OrderedDict([
                        ('node_type', (YLeaf(YType.enumeration, 'node-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg', 'OtsAmplifierNode', '')])),
                        ('grid_mode', (YLeaf(YType.enumeration, 'grid-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg', 'OtsAmplifierGridMode', '')])),
                        ('udc_vlan', (YLeaf(YType.uint32, 'udc-vlan'), ['int'])),
                        ('span_loss', (YLeaf(YType.boolean, 'span-loss'), ['bool'])),
                    ])
                    self.node_type = None
                    self.grid_mode = None
                    self.udc_vlan = None
                    self.span_loss = None

                    self.remote_node = HardwareModule.Node.Slot.Amplifier.RemoteNode()
                    self.remote_node.parent = self
                    self._children_name_map["remote_node"] = "remote-node"
                    self._segment_path = lambda: "amplifier"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HardwareModule.Node.Slot.Amplifier, ['node_type', 'grid_mode', 'udc_vlan', 'span_loss'], name, value)


                class RemoteNode(Entity):
                    """
                    RemoteNode Configuration
                    
                    .. attribute:: local_ip_address
                    
                    	IP address of local host
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: remote_ip_address
                    
                    	IP address of remote host
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: remote_slot_id
                    
                    	Set remote Slot
                    	**type**\: int
                    
                    	**range:** 1..3
                    
                    

                    """

                    _prefix = 'ncs1001-ots-cfg'
                    _revision = '2018-03-20'

                    def __init__(self):
                        super(HardwareModule.Node.Slot.Amplifier.RemoteNode, self).__init__()

                        self.yang_name = "remote-node"
                        self.yang_parent_name = "amplifier"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('local_ip_address', (YLeaf(YType.str, 'local-ip-address'), ['str','str'])),
                            ('remote_ip_address', (YLeaf(YType.str, 'remote-ip-address'), ['str','str'])),
                            ('remote_slot_id', (YLeaf(YType.uint32, 'remote-slot-id'), ['int'])),
                        ])
                        self.local_ip_address = None
                        self.remote_ip_address = None
                        self.remote_slot_id = None
                        self._segment_path = lambda: "remote-node"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HardwareModule.Node.Slot.Amplifier.RemoteNode, ['local_ip_address', 'remote_ip_address', 'remote_slot_id'], name, value)


            class Psm(Entity):
                """
                PSM Configs
                
                .. attribute:: mono_dir
                
                	Psm Uni directional configuration
                	**type**\: bool
                
                .. attribute:: auto_threshold
                
                	Psm Automatic Threshold Setting
                	**type**\: bool
                
                .. attribute:: path_protection
                
                	Psm path protection configuration
                	**type**\: bool
                
                .. attribute:: section_protection
                
                	Psm section protection configuration
                	**type**\: bool
                
                .. attribute:: lockout_from
                
                	Exclude selected port from protection
                	**type**\:  :py:class:`OtsPsmLockoutFrom <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg.OtsPsmLockoutFrom>`
                
                

                """

                _prefix = 'ncs1001-ots-cfg'
                _revision = '2018-03-20'

                def __init__(self):
                    super(HardwareModule.Node.Slot.Psm, self).__init__()

                    self.yang_name = "psm"
                    self.yang_parent_name = "slot"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('mono_dir', (YLeaf(YType.boolean, 'mono-dir'), ['bool'])),
                        ('auto_threshold', (YLeaf(YType.boolean, 'auto-threshold'), ['bool'])),
                        ('path_protection', (YLeaf(YType.boolean, 'path-protection'), ['bool'])),
                        ('section_protection', (YLeaf(YType.boolean, 'section-protection'), ['bool'])),
                        ('lockout_from', (YLeaf(YType.enumeration, 'lockout-from'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg', 'OtsPsmLockoutFrom', '')])),
                    ])
                    self.mono_dir = None
                    self.auto_threshold = None
                    self.path_protection = None
                    self.section_protection = None
                    self.lockout_from = None
                    self._segment_path = lambda: "psm"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HardwareModule.Node.Slot.Psm, ['mono_dir', 'auto_threshold', 'path_protection', 'section_protection', 'lockout_from'], name, value)

    def clone_ptr(self):
        self._top_entity = HardwareModule()
        return self._top_entity


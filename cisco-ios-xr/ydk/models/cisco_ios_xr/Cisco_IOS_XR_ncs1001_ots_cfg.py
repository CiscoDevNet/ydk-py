""" Cisco_IOS_XR_ncs1001_ots_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs1001\-ots package configuration.

This module contains definitions
for the following management objects\:
  hardware\-module\: NCS1k HW module config

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
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
    _revision = '2017-10-20'

    def __init__(self):
        super(HardwareModule, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module"
        self.yang_parent_name = "Cisco-IOS-XR-ncs1001-ots-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("node", ("node", HardwareModule.Node))])
        self._leafs = OrderedDict()

        self.node = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-ncs1001-ots-cfg:hardware-module"

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
        _revision = '2017-10-20'

        def __init__(self):
            super(HardwareModule.Node, self).__init__()

            self.yang_name = "node"
            self.yang_parent_name = "hardware-module"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['location']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("slot", ("slot", HardwareModule.Node.Slot))])
            self._leafs = OrderedDict([
                ('location', YLeaf(YType.str, 'location')),
            ])
            self.location = None

            self.slot = YList(self)
            self._segment_path = lambda: "node" + "[location='" + str(self.location) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-ncs1001-ots-cfg:hardware-module/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(HardwareModule.Node, ['location'], name, value)


        class Slot(Entity):
            """
            Slot Id
            
            .. attribute:: slot_id  (key)
            
            	Set Slot
            	**type**\: int
            
            	**range:** 1..3
            
            .. attribute:: amplifier
            
            	Amplifier Configs
            	**type**\:  :py:class:`Amplifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg.HardwareModule.Node.Slot.Amplifier>`
            
            .. attribute:: psm
            
            	PSM Configs
            	**type**\:  :py:class:`Psm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_ots_cfg.HardwareModule.Node.Slot.Psm>`
            
            

            """

            _prefix = 'ncs1001-ots-cfg'
            _revision = '2017-10-20'

            def __init__(self):
                super(HardwareModule.Node.Slot, self).__init__()

                self.yang_name = "slot"
                self.yang_parent_name = "node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['slot_id']
                self._child_container_classes = OrderedDict([("amplifier", ("amplifier", HardwareModule.Node.Slot.Amplifier)), ("psm", ("psm", HardwareModule.Node.Slot.Psm))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('slot_id', YLeaf(YType.uint32, 'slot-id')),
                ])
                self.slot_id = None

                self.amplifier = HardwareModule.Node.Slot.Amplifier()
                self.amplifier.parent = self
                self._children_name_map["amplifier"] = "amplifier"
                self._children_yang_names.add("amplifier")

                self.psm = HardwareModule.Node.Slot.Psm()
                self.psm.parent = self
                self._children_name_map["psm"] = "psm"
                self._children_yang_names.add("psm")
                self._segment_path = lambda: "slot" + "[slot-id='" + str(self.slot_id) + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(HardwareModule.Node.Slot, ['slot_id'], name, value)


            class Amplifier(Entity):
                """
                Amplifier Configs
                
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
                
                

                """

                _prefix = 'ncs1001-ots-cfg'
                _revision = '2017-10-20'

                def __init__(self):
                    super(HardwareModule.Node.Slot.Amplifier, self).__init__()

                    self.yang_name = "amplifier"
                    self.yang_parent_name = "slot"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('node_type', YLeaf(YType.enumeration, 'node-type')),
                        ('grid_mode', YLeaf(YType.enumeration, 'grid-mode')),
                        ('udc_vlan', YLeaf(YType.uint32, 'udc-vlan')),
                    ])
                    self.node_type = None
                    self.grid_mode = None
                    self.udc_vlan = None
                    self._segment_path = lambda: "amplifier"

                def __setattr__(self, name, value):
                    self._perform_setattr(HardwareModule.Node.Slot.Amplifier, ['node_type', 'grid_mode', 'udc_vlan'], name, value)


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
                _revision = '2017-10-20'

                def __init__(self):
                    super(HardwareModule.Node.Slot.Psm, self).__init__()

                    self.yang_name = "psm"
                    self.yang_parent_name = "slot"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('mono_dir', YLeaf(YType.boolean, 'mono-dir')),
                        ('auto_threshold', YLeaf(YType.boolean, 'auto-threshold')),
                        ('path_protection', YLeaf(YType.boolean, 'path-protection')),
                        ('section_protection', YLeaf(YType.boolean, 'section-protection')),
                        ('lockout_from', YLeaf(YType.enumeration, 'lockout-from')),
                    ])
                    self.mono_dir = None
                    self.auto_threshold = None
                    self.path_protection = None
                    self.section_protection = None
                    self.lockout_from = None
                    self._segment_path = lambda: "psm"

                def __setattr__(self, name, value):
                    self._perform_setattr(HardwareModule.Node.Slot.Psm, ['mono_dir', 'auto_threshold', 'path_protection', 'section_protection', 'lockout_from'], name, value)

    def clone_ptr(self):
        self._top_entity = HardwareModule()
        return self._top_entity


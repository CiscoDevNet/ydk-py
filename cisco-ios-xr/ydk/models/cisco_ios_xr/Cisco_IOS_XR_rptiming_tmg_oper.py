""" Cisco_IOS_XR_rptiming_tmg_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR rptiming\-tmg package operational data.

This module contains definitions
for the following management objects\:
  timing\-card\: Timing PLL status and configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class TimingCard(Entity):
    """
    Timing PLL status and configuration
    
    .. attribute:: nodes
    
    	List of nodes applicable to timing
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rptiming_tmg_oper.TimingCard.Nodes>`
    
    

    """

    _prefix = 'rptiming-tmg-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(TimingCard, self).__init__()
        self._top_entity = None

        self.yang_name = "timing-card"
        self.yang_parent_name = "Cisco-IOS-XR-rptiming-tmg-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", TimingCard.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = TimingCard.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-rptiming-tmg-oper:timing-card"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(TimingCard, [], name, value)


    class Nodes(Entity):
        """
        List of nodes applicable to timing
        
        .. attribute:: node
        
        	Timing operational data for a single node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rptiming_tmg_oper.TimingCard.Nodes.Node>`
        
        

        """

        _prefix = 'rptiming-tmg-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(TimingCard.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "timing-card"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", TimingCard.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-rptiming-tmg-oper:timing-card/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TimingCard.Nodes, [], name, value)


        class Node(Entity):
            """
            Timing operational data for a single node
            
            .. attribute:: node_name  (key)
            
            	Node Name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: input_clock
            
            	Display the timing card input clock status information
            	**type**\:  :py:class:`InputClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rptiming_tmg_oper.TimingCard.Nodes.Node.InputClock>`
            
            .. attribute:: pll
            
            	Display the timing card PLL status information
            	**type**\:  :py:class:`Pll <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rptiming_tmg_oper.TimingCard.Nodes.Node.Pll>`
            
            

            """

            _prefix = 'rptiming-tmg-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(TimingCard.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("input-clock", ("input_clock", TimingCard.Nodes.Node.InputClock)), ("pll", ("pll", TimingCard.Nodes.Node.Pll))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.input_clock = TimingCard.Nodes.Node.InputClock()
                self.input_clock.parent = self
                self._children_name_map["input_clock"] = "input-clock"

                self.pll = TimingCard.Nodes.Node.Pll()
                self.pll.parent = self
                self._children_name_map["pll"] = "pll"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-rptiming-tmg-oper:timing-card/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TimingCard.Nodes.Node, ['node_name'], name, value)


            class InputClock(Entity):
                """
                Display the timing card input clock status
                information
                
                .. attribute:: ic1_valid
                
                	IC Valid 1
                	**type**\: bool
                
                .. attribute:: ic2_valid
                
                	IC Valid 2
                	**type**\: bool
                
                .. attribute:: ic3_valid
                
                	IC Valid 3
                	**type**\: bool
                
                .. attribute:: ic4_valid
                
                	IC Valid 4
                	**type**\: bool
                
                .. attribute:: ic5_valid
                
                	IC Valid 5
                	**type**\: bool
                
                .. attribute:: ic6_valid
                
                	IC Valid 6
                	**type**\: bool
                
                .. attribute:: ic7_valid
                
                	IC Valid 7
                	**type**\: bool
                
                .. attribute:: ic8_valid
                
                	IC Valid 8
                	**type**\: bool
                
                .. attribute:: ic9_valid
                
                	IC Valid 9
                	**type**\: bool
                
                .. attribute:: ic10_valid
                
                	IC Valid 10
                	**type**\: bool
                
                .. attribute:: ic11_valid
                
                	IC Valid 11
                	**type**\: bool
                
                .. attribute:: ic1_slot
                
                	IC Slot 1
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic2_slot
                
                	IC Slot 2
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic3_slot
                
                	IC Slot 3
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic4_slot
                
                	IC Slot 4
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic5_slot
                
                	IC Slot 5
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic6_slot
                
                	IC Slot 6
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic7_slot
                
                	IC Slot 7
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic8_slot
                
                	IC Slot 8
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic9_slot
                
                	IC Slot 9
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic10_slot
                
                	IC Slot 10
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic11_slot
                
                	IC Slot 11
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic1_split_xom
                
                	IC1 Split XO Mode Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic2_split_xom
                
                	IC2 Split XO Mode Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic3_split_xom
                
                	IC3 Split XO Mode Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic4_split_xom
                
                	IC4 Split XO Mode Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic5_split_xom
                
                	IC5 Split XO Mode Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic6_split_xom
                
                	IC6 Split XO Mode Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic7_split_xom
                
                	IC7 Split XO Mode Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic8_split_xom
                
                	IC8 Split XO Mode Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic9_split_xom
                
                	IC9 Split XO Mode Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic10_split_xom
                
                	IC10 Split XO Mode Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic11_split_xom
                
                	IC11 Split XO Mode Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic1_eppsm
                
                	IC1 ePPSM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic2_eppsm
                
                	IC2 ePPSM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic3_eppsm
                
                	IC3 ePPSM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic4_eppsm
                
                	IC4 ePPSM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic5_eppsm
                
                	IC5 ePPSM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic6_eppsm
                
                	IC6 ePPSM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic7_eppsm
                
                	IC7 ePPSM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic8_eppsm
                
                	IC8 ePPSM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic9_eppsm
                
                	IC9 ePPSM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic10_eppsm
                
                	IC10 ePPSM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic11_eppsm
                
                	IC11 ePPSM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic1_pfm
                
                	IC1 PFM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic2_pfm
                
                	IC2 PFM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic3_pfm
                
                	IC3 PFM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic4_pfm
                
                	IC4 PFM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic5_pfm
                
                	IC5 PFM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic6_pfm
                
                	IC6 PFM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic7_pfm
                
                	IC7 PFM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic8_pfm
                
                	IC8 PFM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic9_pfm
                
                	IC9 PFM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic10_pfm
                
                	IC10 PFM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic11_pfm
                
                	IC11 PFM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic1_gst
                
                	IC1 GST Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic2_gst
                
                	IC2 GST Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic3_gst
                
                	IC3 GST Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic4_gst
                
                	IC4 GST Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic5_gst
                
                	IC5 GST Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic6_gst
                
                	IC6 GST Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic7_gst
                
                	IC7 GST Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic8_gst
                
                	IC8 GST Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic9_gst
                
                	IC9 GST Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic10_gst
                
                	IC10 GST Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic11_gst
                
                	IC11 GST Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic1_cfm
                
                	IC1 CFM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic2_cfm
                
                	IC2 CFM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic3_cfm
                
                	IC3 CFM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic4_cfm
                
                	IC4 CFM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic5_cfm
                
                	IC5 CFM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic6_cfm
                
                	IC6 CFM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic7_cfm
                
                	IC7 CFM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic8_cfm
                
                	IC8 CFM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic9_cfm
                
                	IC9 CFM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic10_cfm
                
                	IC10 CFM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic11_cfm
                
                	IC11 CFM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic1_scm
                
                	IC1 SCM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic2_scm
                
                	IC2 SCM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic3_scm
                
                	IC3 SCM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic4_scm
                
                	IC4 SCM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic5_scm
                
                	IC5 SCM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic6_scm
                
                	IC6 SCM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic7_scm
                
                	IC7 SCM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic8_scm
                
                	IC8 SCM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic9_scm
                
                	IC9 SCM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic10_scm
                
                	IC10 SCM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic11_scm
                
                	IC11 SCM Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic1_los
                
                	IC1 LOS Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic2_los
                
                	IC2 LOS Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic3_los
                
                	IC3 LOS Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic4_los
                
                	IC4 LOS Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic5_los
                
                	IC5 LOS Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic6_los
                
                	IC6 LOS Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic7_los
                
                	IC7 LOS Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic8_los
                
                	IC8 LOS Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic9_los
                
                	IC9 LOS Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic10_los
                
                	IC10 LOS Status
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic11_los
                
                	IC11 LOS Status
                	**type**\: str
                
                	**length:** 0..50
                
                

                """

                _prefix = 'rptiming-tmg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(TimingCard.Nodes.Node.InputClock, self).__init__()

                    self.yang_name = "input-clock"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ic1_valid', (YLeaf(YType.boolean, 'ic1-valid'), ['bool'])),
                        ('ic2_valid', (YLeaf(YType.boolean, 'ic2-valid'), ['bool'])),
                        ('ic3_valid', (YLeaf(YType.boolean, 'ic3-valid'), ['bool'])),
                        ('ic4_valid', (YLeaf(YType.boolean, 'ic4-valid'), ['bool'])),
                        ('ic5_valid', (YLeaf(YType.boolean, 'ic5-valid'), ['bool'])),
                        ('ic6_valid', (YLeaf(YType.boolean, 'ic6-valid'), ['bool'])),
                        ('ic7_valid', (YLeaf(YType.boolean, 'ic7-valid'), ['bool'])),
                        ('ic8_valid', (YLeaf(YType.boolean, 'ic8-valid'), ['bool'])),
                        ('ic9_valid', (YLeaf(YType.boolean, 'ic9-valid'), ['bool'])),
                        ('ic10_valid', (YLeaf(YType.boolean, 'ic10-valid'), ['bool'])),
                        ('ic11_valid', (YLeaf(YType.boolean, 'ic11-valid'), ['bool'])),
                        ('ic1_slot', (YLeaf(YType.str, 'ic1-slot'), ['str'])),
                        ('ic2_slot', (YLeaf(YType.str, 'ic2-slot'), ['str'])),
                        ('ic3_slot', (YLeaf(YType.str, 'ic3-slot'), ['str'])),
                        ('ic4_slot', (YLeaf(YType.str, 'ic4-slot'), ['str'])),
                        ('ic5_slot', (YLeaf(YType.str, 'ic5-slot'), ['str'])),
                        ('ic6_slot', (YLeaf(YType.str, 'ic6-slot'), ['str'])),
                        ('ic7_slot', (YLeaf(YType.str, 'ic7-slot'), ['str'])),
                        ('ic8_slot', (YLeaf(YType.str, 'ic8-slot'), ['str'])),
                        ('ic9_slot', (YLeaf(YType.str, 'ic9-slot'), ['str'])),
                        ('ic10_slot', (YLeaf(YType.str, 'ic10-slot'), ['str'])),
                        ('ic11_slot', (YLeaf(YType.str, 'ic11-slot'), ['str'])),
                        ('ic1_split_xom', (YLeaf(YType.str, 'ic1-split-xom'), ['str'])),
                        ('ic2_split_xom', (YLeaf(YType.str, 'ic2-split-xom'), ['str'])),
                        ('ic3_split_xom', (YLeaf(YType.str, 'ic3-split-xom'), ['str'])),
                        ('ic4_split_xom', (YLeaf(YType.str, 'ic4-split-xom'), ['str'])),
                        ('ic5_split_xom', (YLeaf(YType.str, 'ic5-split-xom'), ['str'])),
                        ('ic6_split_xom', (YLeaf(YType.str, 'ic6-split-xom'), ['str'])),
                        ('ic7_split_xom', (YLeaf(YType.str, 'ic7-split-xom'), ['str'])),
                        ('ic8_split_xom', (YLeaf(YType.str, 'ic8-split-xom'), ['str'])),
                        ('ic9_split_xom', (YLeaf(YType.str, 'ic9-split-xom'), ['str'])),
                        ('ic10_split_xom', (YLeaf(YType.str, 'ic10-split-xom'), ['str'])),
                        ('ic11_split_xom', (YLeaf(YType.str, 'ic11-split-xom'), ['str'])),
                        ('ic1_eppsm', (YLeaf(YType.str, 'ic1-eppsm'), ['str'])),
                        ('ic2_eppsm', (YLeaf(YType.str, 'ic2-eppsm'), ['str'])),
                        ('ic3_eppsm', (YLeaf(YType.str, 'ic3-eppsm'), ['str'])),
                        ('ic4_eppsm', (YLeaf(YType.str, 'ic4-eppsm'), ['str'])),
                        ('ic5_eppsm', (YLeaf(YType.str, 'ic5-eppsm'), ['str'])),
                        ('ic6_eppsm', (YLeaf(YType.str, 'ic6-eppsm'), ['str'])),
                        ('ic7_eppsm', (YLeaf(YType.str, 'ic7-eppsm'), ['str'])),
                        ('ic8_eppsm', (YLeaf(YType.str, 'ic8-eppsm'), ['str'])),
                        ('ic9_eppsm', (YLeaf(YType.str, 'ic9-eppsm'), ['str'])),
                        ('ic10_eppsm', (YLeaf(YType.str, 'ic10-eppsm'), ['str'])),
                        ('ic11_eppsm', (YLeaf(YType.str, 'ic11-eppsm'), ['str'])),
                        ('ic1_pfm', (YLeaf(YType.str, 'ic1-pfm'), ['str'])),
                        ('ic2_pfm', (YLeaf(YType.str, 'ic2-pfm'), ['str'])),
                        ('ic3_pfm', (YLeaf(YType.str, 'ic3-pfm'), ['str'])),
                        ('ic4_pfm', (YLeaf(YType.str, 'ic4-pfm'), ['str'])),
                        ('ic5_pfm', (YLeaf(YType.str, 'ic5-pfm'), ['str'])),
                        ('ic6_pfm', (YLeaf(YType.str, 'ic6-pfm'), ['str'])),
                        ('ic7_pfm', (YLeaf(YType.str, 'ic7-pfm'), ['str'])),
                        ('ic8_pfm', (YLeaf(YType.str, 'ic8-pfm'), ['str'])),
                        ('ic9_pfm', (YLeaf(YType.str, 'ic9-pfm'), ['str'])),
                        ('ic10_pfm', (YLeaf(YType.str, 'ic10-pfm'), ['str'])),
                        ('ic11_pfm', (YLeaf(YType.str, 'ic11-pfm'), ['str'])),
                        ('ic1_gst', (YLeaf(YType.str, 'ic1-gst'), ['str'])),
                        ('ic2_gst', (YLeaf(YType.str, 'ic2-gst'), ['str'])),
                        ('ic3_gst', (YLeaf(YType.str, 'ic3-gst'), ['str'])),
                        ('ic4_gst', (YLeaf(YType.str, 'ic4-gst'), ['str'])),
                        ('ic5_gst', (YLeaf(YType.str, 'ic5-gst'), ['str'])),
                        ('ic6_gst', (YLeaf(YType.str, 'ic6-gst'), ['str'])),
                        ('ic7_gst', (YLeaf(YType.str, 'ic7-gst'), ['str'])),
                        ('ic8_gst', (YLeaf(YType.str, 'ic8-gst'), ['str'])),
                        ('ic9_gst', (YLeaf(YType.str, 'ic9-gst'), ['str'])),
                        ('ic10_gst', (YLeaf(YType.str, 'ic10-gst'), ['str'])),
                        ('ic11_gst', (YLeaf(YType.str, 'ic11-gst'), ['str'])),
                        ('ic1_cfm', (YLeaf(YType.str, 'ic1-cfm'), ['str'])),
                        ('ic2_cfm', (YLeaf(YType.str, 'ic2-cfm'), ['str'])),
                        ('ic3_cfm', (YLeaf(YType.str, 'ic3-cfm'), ['str'])),
                        ('ic4_cfm', (YLeaf(YType.str, 'ic4-cfm'), ['str'])),
                        ('ic5_cfm', (YLeaf(YType.str, 'ic5-cfm'), ['str'])),
                        ('ic6_cfm', (YLeaf(YType.str, 'ic6-cfm'), ['str'])),
                        ('ic7_cfm', (YLeaf(YType.str, 'ic7-cfm'), ['str'])),
                        ('ic8_cfm', (YLeaf(YType.str, 'ic8-cfm'), ['str'])),
                        ('ic9_cfm', (YLeaf(YType.str, 'ic9-cfm'), ['str'])),
                        ('ic10_cfm', (YLeaf(YType.str, 'ic10-cfm'), ['str'])),
                        ('ic11_cfm', (YLeaf(YType.str, 'ic11-cfm'), ['str'])),
                        ('ic1_scm', (YLeaf(YType.str, 'ic1-scm'), ['str'])),
                        ('ic2_scm', (YLeaf(YType.str, 'ic2-scm'), ['str'])),
                        ('ic3_scm', (YLeaf(YType.str, 'ic3-scm'), ['str'])),
                        ('ic4_scm', (YLeaf(YType.str, 'ic4-scm'), ['str'])),
                        ('ic5_scm', (YLeaf(YType.str, 'ic5-scm'), ['str'])),
                        ('ic6_scm', (YLeaf(YType.str, 'ic6-scm'), ['str'])),
                        ('ic7_scm', (YLeaf(YType.str, 'ic7-scm'), ['str'])),
                        ('ic8_scm', (YLeaf(YType.str, 'ic8-scm'), ['str'])),
                        ('ic9_scm', (YLeaf(YType.str, 'ic9-scm'), ['str'])),
                        ('ic10_scm', (YLeaf(YType.str, 'ic10-scm'), ['str'])),
                        ('ic11_scm', (YLeaf(YType.str, 'ic11-scm'), ['str'])),
                        ('ic1_los', (YLeaf(YType.str, 'ic1-los'), ['str'])),
                        ('ic2_los', (YLeaf(YType.str, 'ic2-los'), ['str'])),
                        ('ic3_los', (YLeaf(YType.str, 'ic3-los'), ['str'])),
                        ('ic4_los', (YLeaf(YType.str, 'ic4-los'), ['str'])),
                        ('ic5_los', (YLeaf(YType.str, 'ic5-los'), ['str'])),
                        ('ic6_los', (YLeaf(YType.str, 'ic6-los'), ['str'])),
                        ('ic7_los', (YLeaf(YType.str, 'ic7-los'), ['str'])),
                        ('ic8_los', (YLeaf(YType.str, 'ic8-los'), ['str'])),
                        ('ic9_los', (YLeaf(YType.str, 'ic9-los'), ['str'])),
                        ('ic10_los', (YLeaf(YType.str, 'ic10-los'), ['str'])),
                        ('ic11_los', (YLeaf(YType.str, 'ic11-los'), ['str'])),
                    ])
                    self.ic1_valid = None
                    self.ic2_valid = None
                    self.ic3_valid = None
                    self.ic4_valid = None
                    self.ic5_valid = None
                    self.ic6_valid = None
                    self.ic7_valid = None
                    self.ic8_valid = None
                    self.ic9_valid = None
                    self.ic10_valid = None
                    self.ic11_valid = None
                    self.ic1_slot = None
                    self.ic2_slot = None
                    self.ic3_slot = None
                    self.ic4_slot = None
                    self.ic5_slot = None
                    self.ic6_slot = None
                    self.ic7_slot = None
                    self.ic8_slot = None
                    self.ic9_slot = None
                    self.ic10_slot = None
                    self.ic11_slot = None
                    self.ic1_split_xom = None
                    self.ic2_split_xom = None
                    self.ic3_split_xom = None
                    self.ic4_split_xom = None
                    self.ic5_split_xom = None
                    self.ic6_split_xom = None
                    self.ic7_split_xom = None
                    self.ic8_split_xom = None
                    self.ic9_split_xom = None
                    self.ic10_split_xom = None
                    self.ic11_split_xom = None
                    self.ic1_eppsm = None
                    self.ic2_eppsm = None
                    self.ic3_eppsm = None
                    self.ic4_eppsm = None
                    self.ic5_eppsm = None
                    self.ic6_eppsm = None
                    self.ic7_eppsm = None
                    self.ic8_eppsm = None
                    self.ic9_eppsm = None
                    self.ic10_eppsm = None
                    self.ic11_eppsm = None
                    self.ic1_pfm = None
                    self.ic2_pfm = None
                    self.ic3_pfm = None
                    self.ic4_pfm = None
                    self.ic5_pfm = None
                    self.ic6_pfm = None
                    self.ic7_pfm = None
                    self.ic8_pfm = None
                    self.ic9_pfm = None
                    self.ic10_pfm = None
                    self.ic11_pfm = None
                    self.ic1_gst = None
                    self.ic2_gst = None
                    self.ic3_gst = None
                    self.ic4_gst = None
                    self.ic5_gst = None
                    self.ic6_gst = None
                    self.ic7_gst = None
                    self.ic8_gst = None
                    self.ic9_gst = None
                    self.ic10_gst = None
                    self.ic11_gst = None
                    self.ic1_cfm = None
                    self.ic2_cfm = None
                    self.ic3_cfm = None
                    self.ic4_cfm = None
                    self.ic5_cfm = None
                    self.ic6_cfm = None
                    self.ic7_cfm = None
                    self.ic8_cfm = None
                    self.ic9_cfm = None
                    self.ic10_cfm = None
                    self.ic11_cfm = None
                    self.ic1_scm = None
                    self.ic2_scm = None
                    self.ic3_scm = None
                    self.ic4_scm = None
                    self.ic5_scm = None
                    self.ic6_scm = None
                    self.ic7_scm = None
                    self.ic8_scm = None
                    self.ic9_scm = None
                    self.ic10_scm = None
                    self.ic11_scm = None
                    self.ic1_los = None
                    self.ic2_los = None
                    self.ic3_los = None
                    self.ic4_los = None
                    self.ic5_los = None
                    self.ic6_los = None
                    self.ic7_los = None
                    self.ic8_los = None
                    self.ic9_los = None
                    self.ic10_los = None
                    self.ic11_los = None
                    self._segment_path = lambda: "input-clock"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(TimingCard.Nodes.Node.InputClock, ['ic1_valid', 'ic2_valid', 'ic3_valid', 'ic4_valid', 'ic5_valid', 'ic6_valid', 'ic7_valid', 'ic8_valid', 'ic9_valid', 'ic10_valid', 'ic11_valid', 'ic1_slot', 'ic2_slot', 'ic3_slot', 'ic4_slot', 'ic5_slot', 'ic6_slot', 'ic7_slot', 'ic8_slot', 'ic9_slot', 'ic10_slot', 'ic11_slot', 'ic1_split_xom', 'ic2_split_xom', 'ic3_split_xom', 'ic4_split_xom', 'ic5_split_xom', 'ic6_split_xom', 'ic7_split_xom', 'ic8_split_xom', 'ic9_split_xom', 'ic10_split_xom', 'ic11_split_xom', 'ic1_eppsm', 'ic2_eppsm', 'ic3_eppsm', 'ic4_eppsm', 'ic5_eppsm', 'ic6_eppsm', 'ic7_eppsm', 'ic8_eppsm', 'ic9_eppsm', 'ic10_eppsm', 'ic11_eppsm', 'ic1_pfm', 'ic2_pfm', 'ic3_pfm', 'ic4_pfm', 'ic5_pfm', 'ic6_pfm', 'ic7_pfm', 'ic8_pfm', 'ic9_pfm', 'ic10_pfm', 'ic11_pfm', 'ic1_gst', 'ic2_gst', 'ic3_gst', 'ic4_gst', 'ic5_gst', 'ic6_gst', 'ic7_gst', 'ic8_gst', 'ic9_gst', 'ic10_gst', 'ic11_gst', 'ic1_cfm', 'ic2_cfm', 'ic3_cfm', 'ic4_cfm', 'ic5_cfm', 'ic6_cfm', 'ic7_cfm', 'ic8_cfm', 'ic9_cfm', 'ic10_cfm', 'ic11_cfm', 'ic1_scm', 'ic2_scm', 'ic3_scm', 'ic4_scm', 'ic5_scm', 'ic6_scm', 'ic7_scm', 'ic8_scm', 'ic9_scm', 'ic10_scm', 'ic11_scm', 'ic1_los', 'ic2_los', 'ic3_los', 'ic4_los', 'ic5_los', 'ic6_los', 'ic7_los', 'ic8_los', 'ic9_los', 'ic10_los', 'ic11_los'], name, value)


            class Pll(Entity):
                """
                Display the timing card PLL status information
                
                .. attribute:: t0_pll_state
                
                	T0 PLL state
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: t4_pll_state
                
                	T4 PLL state
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ptp_pll_state
                
                	1588 PLL state
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: t0_pll_selected
                
                	T0 PLL selected
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: t4_pll_selected
                
                	T4 PLL selected
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ptp_pll_selected
                
                	1588 PLL selected
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: t0_pll_mode
                
                	T0 PLL mode
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: t4_pll_mode
                
                	T4 PLL mode
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ptp_pll_mode
                
                	1588 PLL mode
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: t0_pll_ic1_prio
                
                	T0 PLL IC1 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: t0_pll_ic2_prio
                
                	T0 PLL IC2 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: t0_pll_ic3_prio
                
                	T0 PLL IC3 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: t0_pll_ic4_prio
                
                	T0 PLL IC4 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: t0_pll_ic5_prio
                
                	T0 PLL IC5 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: t0_pll_ic6_prio
                
                	T0 PLL IC6 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: t0_pll_ic7_prio
                
                	T0 PLL IC7 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: t0_pll_ic8_prio
                
                	T0 PLL IC8 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: t0_pll_ic9_prio
                
                	T0 PLL IC9 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: t0_pll_ic10_prio
                
                	T0 PLL IC10 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: t0_pll_ic11_prio
                
                	T0 PLL IC11 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: t4_pll_ic1_prio
                
                	T4 PLL IC1 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: t4_pll_ic2_prio
                
                	T4 PLL IC2 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: t4_pll_ic3_prio
                
                	T4 PLL IC3 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: t4_pll_ic4_prio
                
                	T4 PLL IC4 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: t4_pll_ic5_prio
                
                	T4 PLL IC5 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: t4_pll_ic6_prio
                
                	T4 PLL IC6 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: t4_pll_ic7_prio
                
                	T4 PLL IC7 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: t4_pll_ic8_prio
                
                	T4 PLL IC8 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: t4_pll_ic9_prio
                
                	T4 PLL IC9 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: t4_pll_ic10_prio
                
                	T4 PLL IC10 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: t4_pll_ic11_prio
                
                	T4 PLL IC11 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: ptp_pll_ic1_prio
                
                	PTP PLL IC1 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: ptp_pll_ic2_prio
                
                	PTP PLL IC2 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: ptp_pll_ic3_prio
                
                	PTP PLL IC3 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: ptp_pll_ic4_prio
                
                	PTP PLL IC4 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: ptp_pll_ic5_prio
                
                	PTP PLL IC5 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: ptp_pll_ic6_prio
                
                	PTP PLL IC6 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: ptp_pll_ic7_prio
                
                	PTP PLL IC7 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: ptp_pll_ic8_prio
                
                	PTP PLL IC8 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: ptp_pll_ic9_prio
                
                	PTP PLL IC9 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: ptp_pll_ic10_prio
                
                	PTP PLL IC10 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: ptp_pll_ic11_prio
                
                	PTP PLL IC11 Priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: ic1_valid
                
                	IC Valid 1
                	**type**\: bool
                
                .. attribute:: ic2_valid
                
                	IC Valid 2
                	**type**\: bool
                
                .. attribute:: ic3_valid
                
                	IC Valid 3
                	**type**\: bool
                
                .. attribute:: ic4_valid
                
                	IC Valid 4
                	**type**\: bool
                
                .. attribute:: ic5_valid
                
                	IC Valid 5
                	**type**\: bool
                
                .. attribute:: ic6_valid
                
                	IC Valid 6
                	**type**\: bool
                
                .. attribute:: ic7_valid
                
                	IC Valid 7
                	**type**\: bool
                
                .. attribute:: ic8_valid
                
                	IC Valid 8
                	**type**\: bool
                
                .. attribute:: ic9_valid
                
                	IC Valid 9
                	**type**\: bool
                
                .. attribute:: ic10_valid
                
                	IC Valid 10
                	**type**\: bool
                
                .. attribute:: ic11_valid
                
                	IC Valid 11
                	**type**\: bool
                
                .. attribute:: t0_pll_freq_offset
                
                	T0 PLL Frequency Offset
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: t4_pll_freq_offset
                
                	T4 PLL Frequency Offset
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: ptp_pll_freq_offset
                
                	PTP PLL Frequency Offset
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: t0_pll_bandwidth
                
                	T0 PLL Bandwidth
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: t4_pll_bandwidth
                
                	T4 PLL Bandwidth
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ptp_pll_bandwidth
                
                	PTP PLL Bandwidth
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: t0_pll_psl
                
                	T0 PLL PSL
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: t4_pll_psl
                
                	T4 PLL PSL
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ptp_pll_psl
                
                	PTP PLL PSL
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic1_qual_min
                
                	IC1 Pull\-in/Hold\-in Min
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic1_qual_max
                
                	IC1 Pull\-in/Hold\-in Min
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic2_qual_min
                
                	IC2 Pull\-in/Hold\-in Min
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic2_qual_max
                
                	IC2 Pull\-in/Hold\-in Min
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic3_qual_min
                
                	IC3 Pull\-in/Hold\-in Min
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic3_qual_max
                
                	IC3 Pull\-in/Hold\-in Min
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic4_qual_min
                
                	IC4 Pull\-in/Hold\-in Min
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic4_qual_max
                
                	IC4 Pull\-in/Hold\-in Min
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic5_qual_min
                
                	IC5 Pull\-in/Hold\-in Min
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic5_qual_max
                
                	IC5 Pull\-in/Hold\-in Min
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic6_qual_min
                
                	IC6 Pull\-in/Hold\-in Min
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic6_qual_max
                
                	IC6 Pull\-in/Hold\-in Min
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic7_qual_min
                
                	IC7 Pull\-in/Hold\-in Min
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic7_qual_max
                
                	IC7 Pull\-in/Hold\-in Min
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic8_qual_min
                
                	IC8 Pull\-in/Hold\-in Min
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic8_qual_max
                
                	IC8 Pull\-in/Hold\-in Min
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic9_qual_min
                
                	IC9 Pull\-in/Hold\-in Min
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic9_qual_max
                
                	IC9 Pull\-in/Hold\-in Min
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic10_qual_min
                
                	IC10 Pull\-in/Hold\-in Min
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic10_qual_max
                
                	IC10 Pull\-in/Hold\-in Min
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic11_qual_min
                
                	IC11 Pull\-in/Hold\-in Min
                	**type**\: str
                
                	**length:** 0..50
                
                .. attribute:: ic11_qual_max
                
                	IC11 Pull\-in/Hold\-in Min
                	**type**\: str
                
                	**length:** 0..50
                
                

                """

                _prefix = 'rptiming-tmg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(TimingCard.Nodes.Node.Pll, self).__init__()

                    self.yang_name = "pll"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('t0_pll_state', (YLeaf(YType.str, 't0-pll-state'), ['str'])),
                        ('t4_pll_state', (YLeaf(YType.str, 't4-pll-state'), ['str'])),
                        ('ptp_pll_state', (YLeaf(YType.str, 'ptp-pll-state'), ['str'])),
                        ('t0_pll_selected', (YLeaf(YType.str, 't0-pll-selected'), ['str'])),
                        ('t4_pll_selected', (YLeaf(YType.str, 't4-pll-selected'), ['str'])),
                        ('ptp_pll_selected', (YLeaf(YType.str, 'ptp-pll-selected'), ['str'])),
                        ('t0_pll_mode', (YLeaf(YType.str, 't0-pll-mode'), ['str'])),
                        ('t4_pll_mode', (YLeaf(YType.str, 't4-pll-mode'), ['str'])),
                        ('ptp_pll_mode', (YLeaf(YType.str, 'ptp-pll-mode'), ['str'])),
                        ('t0_pll_ic1_prio', (YLeaf(YType.uint8, 't0-pll-ic1-prio'), ['int'])),
                        ('t0_pll_ic2_prio', (YLeaf(YType.uint8, 't0-pll-ic2-prio'), ['int'])),
                        ('t0_pll_ic3_prio', (YLeaf(YType.uint8, 't0-pll-ic3-prio'), ['int'])),
                        ('t0_pll_ic4_prio', (YLeaf(YType.uint8, 't0-pll-ic4-prio'), ['int'])),
                        ('t0_pll_ic5_prio', (YLeaf(YType.uint8, 't0-pll-ic5-prio'), ['int'])),
                        ('t0_pll_ic6_prio', (YLeaf(YType.uint8, 't0-pll-ic6-prio'), ['int'])),
                        ('t0_pll_ic7_prio', (YLeaf(YType.uint8, 't0-pll-ic7-prio'), ['int'])),
                        ('t0_pll_ic8_prio', (YLeaf(YType.uint8, 't0-pll-ic8-prio'), ['int'])),
                        ('t0_pll_ic9_prio', (YLeaf(YType.uint8, 't0-pll-ic9-prio'), ['int'])),
                        ('t0_pll_ic10_prio', (YLeaf(YType.uint8, 't0-pll-ic10-prio'), ['int'])),
                        ('t0_pll_ic11_prio', (YLeaf(YType.uint8, 't0-pll-ic11-prio'), ['int'])),
                        ('t4_pll_ic1_prio', (YLeaf(YType.uint8, 't4-pll-ic1-prio'), ['int'])),
                        ('t4_pll_ic2_prio', (YLeaf(YType.uint8, 't4-pll-ic2-prio'), ['int'])),
                        ('t4_pll_ic3_prio', (YLeaf(YType.uint8, 't4-pll-ic3-prio'), ['int'])),
                        ('t4_pll_ic4_prio', (YLeaf(YType.uint8, 't4-pll-ic4-prio'), ['int'])),
                        ('t4_pll_ic5_prio', (YLeaf(YType.uint8, 't4-pll-ic5-prio'), ['int'])),
                        ('t4_pll_ic6_prio', (YLeaf(YType.uint8, 't4-pll-ic6-prio'), ['int'])),
                        ('t4_pll_ic7_prio', (YLeaf(YType.uint8, 't4-pll-ic7-prio'), ['int'])),
                        ('t4_pll_ic8_prio', (YLeaf(YType.uint8, 't4-pll-ic8-prio'), ['int'])),
                        ('t4_pll_ic9_prio', (YLeaf(YType.uint8, 't4-pll-ic9-prio'), ['int'])),
                        ('t4_pll_ic10_prio', (YLeaf(YType.uint8, 't4-pll-ic10-prio'), ['int'])),
                        ('t4_pll_ic11_prio', (YLeaf(YType.uint8, 't4-pll-ic11-prio'), ['int'])),
                        ('ptp_pll_ic1_prio', (YLeaf(YType.uint8, 'ptp-pll-ic1-prio'), ['int'])),
                        ('ptp_pll_ic2_prio', (YLeaf(YType.uint8, 'ptp-pll-ic2-prio'), ['int'])),
                        ('ptp_pll_ic3_prio', (YLeaf(YType.uint8, 'ptp-pll-ic3-prio'), ['int'])),
                        ('ptp_pll_ic4_prio', (YLeaf(YType.uint8, 'ptp-pll-ic4-prio'), ['int'])),
                        ('ptp_pll_ic5_prio', (YLeaf(YType.uint8, 'ptp-pll-ic5-prio'), ['int'])),
                        ('ptp_pll_ic6_prio', (YLeaf(YType.uint8, 'ptp-pll-ic6-prio'), ['int'])),
                        ('ptp_pll_ic7_prio', (YLeaf(YType.uint8, 'ptp-pll-ic7-prio'), ['int'])),
                        ('ptp_pll_ic8_prio', (YLeaf(YType.uint8, 'ptp-pll-ic8-prio'), ['int'])),
                        ('ptp_pll_ic9_prio', (YLeaf(YType.uint8, 'ptp-pll-ic9-prio'), ['int'])),
                        ('ptp_pll_ic10_prio', (YLeaf(YType.uint8, 'ptp-pll-ic10-prio'), ['int'])),
                        ('ptp_pll_ic11_prio', (YLeaf(YType.uint8, 'ptp-pll-ic11-prio'), ['int'])),
                        ('ic1_valid', (YLeaf(YType.boolean, 'ic1-valid'), ['bool'])),
                        ('ic2_valid', (YLeaf(YType.boolean, 'ic2-valid'), ['bool'])),
                        ('ic3_valid', (YLeaf(YType.boolean, 'ic3-valid'), ['bool'])),
                        ('ic4_valid', (YLeaf(YType.boolean, 'ic4-valid'), ['bool'])),
                        ('ic5_valid', (YLeaf(YType.boolean, 'ic5-valid'), ['bool'])),
                        ('ic6_valid', (YLeaf(YType.boolean, 'ic6-valid'), ['bool'])),
                        ('ic7_valid', (YLeaf(YType.boolean, 'ic7-valid'), ['bool'])),
                        ('ic8_valid', (YLeaf(YType.boolean, 'ic8-valid'), ['bool'])),
                        ('ic9_valid', (YLeaf(YType.boolean, 'ic9-valid'), ['bool'])),
                        ('ic10_valid', (YLeaf(YType.boolean, 'ic10-valid'), ['bool'])),
                        ('ic11_valid', (YLeaf(YType.boolean, 'ic11-valid'), ['bool'])),
                        ('t0_pll_freq_offset', (YLeaf(YType.int32, 't0-pll-freq-offset'), ['int'])),
                        ('t4_pll_freq_offset', (YLeaf(YType.int32, 't4-pll-freq-offset'), ['int'])),
                        ('ptp_pll_freq_offset', (YLeaf(YType.int32, 'ptp-pll-freq-offset'), ['int'])),
                        ('t0_pll_bandwidth', (YLeaf(YType.str, 't0-pll-bandwidth'), ['str'])),
                        ('t4_pll_bandwidth', (YLeaf(YType.str, 't4-pll-bandwidth'), ['str'])),
                        ('ptp_pll_bandwidth', (YLeaf(YType.str, 'ptp-pll-bandwidth'), ['str'])),
                        ('t0_pll_psl', (YLeaf(YType.str, 't0-pll-psl'), ['str'])),
                        ('t4_pll_psl', (YLeaf(YType.str, 't4-pll-psl'), ['str'])),
                        ('ptp_pll_psl', (YLeaf(YType.str, 'ptp-pll-psl'), ['str'])),
                        ('ic1_qual_min', (YLeaf(YType.str, 'ic1-qual-min'), ['str'])),
                        ('ic1_qual_max', (YLeaf(YType.str, 'ic1-qual-max'), ['str'])),
                        ('ic2_qual_min', (YLeaf(YType.str, 'ic2-qual-min'), ['str'])),
                        ('ic2_qual_max', (YLeaf(YType.str, 'ic2-qual-max'), ['str'])),
                        ('ic3_qual_min', (YLeaf(YType.str, 'ic3-qual-min'), ['str'])),
                        ('ic3_qual_max', (YLeaf(YType.str, 'ic3-qual-max'), ['str'])),
                        ('ic4_qual_min', (YLeaf(YType.str, 'ic4-qual-min'), ['str'])),
                        ('ic4_qual_max', (YLeaf(YType.str, 'ic4-qual-max'), ['str'])),
                        ('ic5_qual_min', (YLeaf(YType.str, 'ic5-qual-min'), ['str'])),
                        ('ic5_qual_max', (YLeaf(YType.str, 'ic5-qual-max'), ['str'])),
                        ('ic6_qual_min', (YLeaf(YType.str, 'ic6-qual-min'), ['str'])),
                        ('ic6_qual_max', (YLeaf(YType.str, 'ic6-qual-max'), ['str'])),
                        ('ic7_qual_min', (YLeaf(YType.str, 'ic7-qual-min'), ['str'])),
                        ('ic7_qual_max', (YLeaf(YType.str, 'ic7-qual-max'), ['str'])),
                        ('ic8_qual_min', (YLeaf(YType.str, 'ic8-qual-min'), ['str'])),
                        ('ic8_qual_max', (YLeaf(YType.str, 'ic8-qual-max'), ['str'])),
                        ('ic9_qual_min', (YLeaf(YType.str, 'ic9-qual-min'), ['str'])),
                        ('ic9_qual_max', (YLeaf(YType.str, 'ic9-qual-max'), ['str'])),
                        ('ic10_qual_min', (YLeaf(YType.str, 'ic10-qual-min'), ['str'])),
                        ('ic10_qual_max', (YLeaf(YType.str, 'ic10-qual-max'), ['str'])),
                        ('ic11_qual_min', (YLeaf(YType.str, 'ic11-qual-min'), ['str'])),
                        ('ic11_qual_max', (YLeaf(YType.str, 'ic11-qual-max'), ['str'])),
                    ])
                    self.t0_pll_state = None
                    self.t4_pll_state = None
                    self.ptp_pll_state = None
                    self.t0_pll_selected = None
                    self.t4_pll_selected = None
                    self.ptp_pll_selected = None
                    self.t0_pll_mode = None
                    self.t4_pll_mode = None
                    self.ptp_pll_mode = None
                    self.t0_pll_ic1_prio = None
                    self.t0_pll_ic2_prio = None
                    self.t0_pll_ic3_prio = None
                    self.t0_pll_ic4_prio = None
                    self.t0_pll_ic5_prio = None
                    self.t0_pll_ic6_prio = None
                    self.t0_pll_ic7_prio = None
                    self.t0_pll_ic8_prio = None
                    self.t0_pll_ic9_prio = None
                    self.t0_pll_ic10_prio = None
                    self.t0_pll_ic11_prio = None
                    self.t4_pll_ic1_prio = None
                    self.t4_pll_ic2_prio = None
                    self.t4_pll_ic3_prio = None
                    self.t4_pll_ic4_prio = None
                    self.t4_pll_ic5_prio = None
                    self.t4_pll_ic6_prio = None
                    self.t4_pll_ic7_prio = None
                    self.t4_pll_ic8_prio = None
                    self.t4_pll_ic9_prio = None
                    self.t4_pll_ic10_prio = None
                    self.t4_pll_ic11_prio = None
                    self.ptp_pll_ic1_prio = None
                    self.ptp_pll_ic2_prio = None
                    self.ptp_pll_ic3_prio = None
                    self.ptp_pll_ic4_prio = None
                    self.ptp_pll_ic5_prio = None
                    self.ptp_pll_ic6_prio = None
                    self.ptp_pll_ic7_prio = None
                    self.ptp_pll_ic8_prio = None
                    self.ptp_pll_ic9_prio = None
                    self.ptp_pll_ic10_prio = None
                    self.ptp_pll_ic11_prio = None
                    self.ic1_valid = None
                    self.ic2_valid = None
                    self.ic3_valid = None
                    self.ic4_valid = None
                    self.ic5_valid = None
                    self.ic6_valid = None
                    self.ic7_valid = None
                    self.ic8_valid = None
                    self.ic9_valid = None
                    self.ic10_valid = None
                    self.ic11_valid = None
                    self.t0_pll_freq_offset = None
                    self.t4_pll_freq_offset = None
                    self.ptp_pll_freq_offset = None
                    self.t0_pll_bandwidth = None
                    self.t4_pll_bandwidth = None
                    self.ptp_pll_bandwidth = None
                    self.t0_pll_psl = None
                    self.t4_pll_psl = None
                    self.ptp_pll_psl = None
                    self.ic1_qual_min = None
                    self.ic1_qual_max = None
                    self.ic2_qual_min = None
                    self.ic2_qual_max = None
                    self.ic3_qual_min = None
                    self.ic3_qual_max = None
                    self.ic4_qual_min = None
                    self.ic4_qual_max = None
                    self.ic5_qual_min = None
                    self.ic5_qual_max = None
                    self.ic6_qual_min = None
                    self.ic6_qual_max = None
                    self.ic7_qual_min = None
                    self.ic7_qual_max = None
                    self.ic8_qual_min = None
                    self.ic8_qual_max = None
                    self.ic9_qual_min = None
                    self.ic9_qual_max = None
                    self.ic10_qual_min = None
                    self.ic10_qual_max = None
                    self.ic11_qual_min = None
                    self.ic11_qual_max = None
                    self._segment_path = lambda: "pll"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(TimingCard.Nodes.Node.Pll, ['t0_pll_state', 't4_pll_state', 'ptp_pll_state', 't0_pll_selected', 't4_pll_selected', 'ptp_pll_selected', 't0_pll_mode', 't4_pll_mode', 'ptp_pll_mode', 't0_pll_ic1_prio', 't0_pll_ic2_prio', 't0_pll_ic3_prio', 't0_pll_ic4_prio', 't0_pll_ic5_prio', 't0_pll_ic6_prio', 't0_pll_ic7_prio', 't0_pll_ic8_prio', 't0_pll_ic9_prio', 't0_pll_ic10_prio', 't0_pll_ic11_prio', 't4_pll_ic1_prio', 't4_pll_ic2_prio', 't4_pll_ic3_prio', 't4_pll_ic4_prio', 't4_pll_ic5_prio', 't4_pll_ic6_prio', 't4_pll_ic7_prio', 't4_pll_ic8_prio', 't4_pll_ic9_prio', 't4_pll_ic10_prio', 't4_pll_ic11_prio', 'ptp_pll_ic1_prio', 'ptp_pll_ic2_prio', 'ptp_pll_ic3_prio', 'ptp_pll_ic4_prio', 'ptp_pll_ic5_prio', 'ptp_pll_ic6_prio', 'ptp_pll_ic7_prio', 'ptp_pll_ic8_prio', 'ptp_pll_ic9_prio', 'ptp_pll_ic10_prio', 'ptp_pll_ic11_prio', 'ic1_valid', 'ic2_valid', 'ic3_valid', 'ic4_valid', 'ic5_valid', 'ic6_valid', 'ic7_valid', 'ic8_valid', 'ic9_valid', 'ic10_valid', 'ic11_valid', 't0_pll_freq_offset', 't4_pll_freq_offset', 'ptp_pll_freq_offset', 't0_pll_bandwidth', 't4_pll_bandwidth', 'ptp_pll_bandwidth', 't0_pll_psl', 't4_pll_psl', 'ptp_pll_psl', 'ic1_qual_min', 'ic1_qual_max', 'ic2_qual_min', 'ic2_qual_max', 'ic3_qual_min', 'ic3_qual_max', 'ic4_qual_min', 'ic4_qual_max', 'ic5_qual_min', 'ic5_qual_max', 'ic6_qual_min', 'ic6_qual_max', 'ic7_qual_min', 'ic7_qual_max', 'ic8_qual_min', 'ic8_qual_max', 'ic9_qual_min', 'ic9_qual_max', 'ic10_qual_min', 'ic10_qual_max', 'ic11_qual_min', 'ic11_qual_max'], name, value)

    def clone_ptr(self):
        self._top_entity = TimingCard()
        return self._top_entity


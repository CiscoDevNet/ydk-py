""" Cisco_IOS_XR_ncs1k_mxp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs1k\-mxp package configuration.

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



class ClientDataRate(Enum):
    """
    ClientDataRate (Enum Class)

    Client data rate

    .. data:: ten_gig = 1

    	TenGig

    .. data:: forty_gig = 2

    	FortyGig

    .. data:: hundred_gig = 3

    	HundredGig

    .. data:: ten_and_hundred_gig = 4

    	TenAndHundredGig

    """

    ten_gig = Enum.YLeaf(1, "ten-gig")

    forty_gig = Enum.YLeaf(2, "forty-gig")

    hundred_gig = Enum.YLeaf(3, "hundred-gig")

    ten_and_hundred_gig = Enum.YLeaf(4, "ten-and-hundred-gig")


class Fec(Enum):
    """
    Fec (Enum Class)

    Fec

    .. data:: sd7 = 1

    	SoftDecision7

    .. data:: sd20 = 2

    	SoftDecision20

    """

    sd7 = Enum.YLeaf(1, "sd7")

    sd20 = Enum.YLeaf(2, "sd20")


class TrunkDataRate(Enum):
    """
    TrunkDataRate (Enum Class)

    Trunk data rate

    .. data:: hundred_gig = 2

    	HundredGig

    .. data:: two_hundred_gig = 3

    	TwoHundredGig

    .. data:: two_hundred_fifty_gig = 4

    	TwoHundredFiftyGig

    """

    hundred_gig = Enum.YLeaf(2, "hundred-gig")

    two_hundred_gig = Enum.YLeaf(3, "two-hundred-gig")

    two_hundred_fifty_gig = Enum.YLeaf(4, "two-hundred-fifty-gig")



class HardwareModule(Entity):
    """
    NCS1k HW module config
    
    .. attribute:: node
    
    	Node
    	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg.HardwareModule.Node>`
    
    

    """

    _prefix = 'ncs1k-mxp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(HardwareModule, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module"
        self.yang_parent_name = "Cisco-IOS-XR-ncs1k-mxp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("node", ("node", HardwareModule.Node))])
        self._leafs = OrderedDict()

        self.node = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-ncs1k-mxp-cfg:hardware-module"
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
        
        .. attribute:: slice
        
        	Slice to be Provisioned
        	**type**\: list of  		 :py:class:`Slice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg.HardwareModule.Node.Slice>`
        
        

        """

        _prefix = 'ncs1k-mxp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(HardwareModule.Node, self).__init__()

            self.yang_name = "node"
            self.yang_parent_name = "hardware-module"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['location']
            self._child_classes = OrderedDict([("slice", ("slice", HardwareModule.Node.Slice))])
            self._leafs = OrderedDict([
                ('location', (YLeaf(YType.str, 'location'), ['str'])),
            ])
            self.location = None

            self.slice = YList(self)
            self._segment_path = lambda: "node" + "[location='" + str(self.location) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-ncs1k-mxp-cfg:hardware-module/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HardwareModule.Node, ['location'], name, value)


        class Slice(Entity):
            """
            Slice to be Provisioned
            
            .. attribute:: slice_id  (key)
            
            	Set Slice
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: values
            
            	Data rates & FEC
            	**type**\:  :py:class:`Values <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg.HardwareModule.Node.Slice.Values>`
            
            .. attribute:: client_ains
            
            	AINS Soak Interval Value
            	**type**\:  :py:class:`ClientAins <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg.HardwareModule.Node.Slice.ClientAins>`
            
            .. attribute:: lldp
            
            	Drop LLDP Packets
            	**type**\: bool
            
            

            """

            _prefix = 'ncs1k-mxp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModule.Node.Slice, self).__init__()

                self.yang_name = "slice"
                self.yang_parent_name = "node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['slice_id']
                self._child_classes = OrderedDict([("values", ("values", HardwareModule.Node.Slice.Values)), ("client-ains", ("client_ains", HardwareModule.Node.Slice.ClientAins))])
                self._leafs = OrderedDict([
                    ('slice_id', (YLeaf(YType.str, 'slice-id'), ['str'])),
                    ('lldp', (YLeaf(YType.boolean, 'lldp'), ['bool'])),
                ])
                self.slice_id = None
                self.lldp = None

                self.values = HardwareModule.Node.Slice.Values()
                self.values.parent = self
                self._children_name_map["values"] = "values"

                self.client_ains = HardwareModule.Node.Slice.ClientAins()
                self.client_ains.parent = self
                self._children_name_map["client_ains"] = "client-ains"
                self._segment_path = lambda: "slice" + "[slice-id='" + str(self.slice_id) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HardwareModule.Node.Slice, ['slice_id', 'lldp'], name, value)


            class Values(Entity):
                """
                Data rates & FEC
                
                .. attribute:: client_rate
                
                	Client Rate
                	**type**\:  :py:class:`ClientDataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg.ClientDataRate>`
                
                .. attribute:: trunk_rate
                
                	TrunkRate
                	**type**\:  :py:class:`TrunkDataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg.TrunkDataRate>`
                
                .. attribute:: fec
                
                	FEC
                	**type**\:  :py:class:`Fec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg.Fec>`
                
                .. attribute:: encrypted
                
                	Encrypted
                	**type**\: bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'ncs1k-mxp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HardwareModule.Node.Slice.Values, self).__init__()

                    self.yang_name = "values"
                    self.yang_parent_name = "slice"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('client_rate', (YLeaf(YType.enumeration, 'client-rate'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg', 'ClientDataRate', '')])),
                        ('trunk_rate', (YLeaf(YType.enumeration, 'trunk-rate'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg', 'TrunkDataRate', '')])),
                        ('fec', (YLeaf(YType.enumeration, 'fec'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg', 'Fec', '')])),
                        ('encrypted', (YLeaf(YType.boolean, 'encrypted'), ['bool'])),
                    ])
                    self.client_rate = None
                    self.trunk_rate = None
                    self.fec = None
                    self.encrypted = None
                    self._segment_path = lambda: "values"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HardwareModule.Node.Slice.Values, ['client_rate', 'trunk_rate', 'fec', 'encrypted'], name, value)


            class ClientAins(Entity):
                """
                AINS Soak Interval Value
                
                .. attribute:: hours
                
                	Hours
                	**type**\: int
                
                	**range:** 0..48
                
                	**units**\: hour
                
                .. attribute:: minutes
                
                	Minutes
                	**type**\: int
                
                	**range:** 0..59
                
                	**units**\: minute
                
                

                """

                _prefix = 'ncs1k-mxp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HardwareModule.Node.Slice.ClientAins, self).__init__()

                    self.yang_name = "client-ains"
                    self.yang_parent_name = "slice"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('hours', (YLeaf(YType.uint32, 'hours'), ['int'])),
                        ('minutes', (YLeaf(YType.uint32, 'minutes'), ['int'])),
                    ])
                    self.hours = None
                    self.minutes = None
                    self._segment_path = lambda: "client-ains"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HardwareModule.Node.Slice.ClientAins, ['hours', 'minutes'], name, value)

    def clone_ptr(self):
        self._top_entity = HardwareModule()
        return self._top_entity


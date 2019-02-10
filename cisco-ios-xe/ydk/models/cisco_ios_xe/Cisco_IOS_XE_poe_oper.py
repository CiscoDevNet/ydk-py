""" Cisco_IOS_XE_poe_oper 

This module contains a collection of YANG definitions for
monitoring power over ethernet feature in a Network Element.
Copyright (c) 2016\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IlpowerPdClass(Enum):
    """
    IlpowerPdClass (Enum Class)

    Name of the power class

    .. data:: poe_null = 0

    	List of POE interfaces, keyed by interface name

    .. data:: poe_unknown = 1

    	Power class unknown

    .. data:: poe_cisco = 2

    	Power class cisco

    .. data:: poe_ieee0 = 3

    	IEEE power class 0

    .. data:: poe_ieee1 = 4

    	IEEE power class 1

    .. data:: poe_ieee2 = 5

    	IEEE power class 2

    .. data:: poe_ieee3 = 6

    	IEEE power class 3

    .. data:: poe_ieee4 = 7

    	IEEE power class 4

    .. data:: poe_ieee5 = 8

    	IEEE power class 5

    .. data:: poe_ieee_unknown_class = 9

    	IEEE power class unknown

    """

    poe_null = Enum.YLeaf(0, "poe-null")

    poe_unknown = Enum.YLeaf(1, "poe-unknown")

    poe_cisco = Enum.YLeaf(2, "poe-cisco")

    poe_ieee0 = Enum.YLeaf(3, "poe-ieee0")

    poe_ieee1 = Enum.YLeaf(4, "poe-ieee1")

    poe_ieee2 = Enum.YLeaf(5, "poe-ieee2")

    poe_ieee3 = Enum.YLeaf(6, "poe-ieee3")

    poe_ieee4 = Enum.YLeaf(7, "poe-ieee4")

    poe_ieee5 = Enum.YLeaf(8, "poe-ieee5")

    poe_ieee_unknown_class = Enum.YLeaf(9, "poe-ieee-unknown-class")



class PoeOperData(Entity):
    """
    Informaton about POEs
    
    .. attribute:: poe_port
    
    	List of POE interfaces, keyed by interface name
    	**type**\: list of  		 :py:class:`PoePort <ydk.models.cisco_ios_xe.Cisco_IOS_XE_poe_oper.PoeOperData.PoePort>`
    
    	**config**\: False
    
    

    """

    _prefix = 'poe-ios-xe-oper'
    _revision = '2018-02-04'

    def __init__(self):
        super(PoeOperData, self).__init__()
        self._top_entity = None

        self.yang_name = "poe-oper-data"
        self.yang_parent_name = "Cisco-IOS-XE-poe-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("poe-port", ("poe_port", PoeOperData.PoePort))])
        self._leafs = OrderedDict()

        self.poe_port = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-poe-oper:poe-oper-data"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PoeOperData, [], name, value)


    class PoePort(Entity):
        """
        List of POE interfaces, keyed by interface name
        
        .. attribute:: intf_name  (key)
        
        	Name of the POE interface
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: poe_intf_enabled
        
        	POE interface admin state
        	**type**\: bool
        
        	**config**\: False
        
        .. attribute:: power_used
        
        	Power used by PD device
        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
        
        	**range:** \-92233720368547758.08..92233720368547758.07
        
        	**config**\: False
        
        .. attribute:: pd_class
        
        	Class of the PD device
        	**type**\:  :py:class:`IlpowerPdClass <ydk.models.cisco_ios_xe.Cisco_IOS_XE_poe_oper.IlpowerPdClass>`
        
        	**config**\: False
        
        

        """

        _prefix = 'poe-ios-xe-oper'
        _revision = '2018-02-04'

        def __init__(self):
            super(PoeOperData.PoePort, self).__init__()

            self.yang_name = "poe-port"
            self.yang_parent_name = "poe-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['intf_name']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('intf_name', (YLeaf(YType.str, 'intf-name'), ['str'])),
                ('poe_intf_enabled', (YLeaf(YType.boolean, 'poe-intf-enabled'), ['bool'])),
                ('power_used', (YLeaf(YType.str, 'power-used'), ['Decimal64'])),
                ('pd_class', (YLeaf(YType.enumeration, 'pd-class'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_poe_oper', 'IlpowerPdClass', '')])),
            ])
            self.intf_name = None
            self.poe_intf_enabled = None
            self.power_used = None
            self.pd_class = None
            self._segment_path = lambda: "poe-port" + "[intf-name='" + str(self.intf_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-poe-oper:poe-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PoeOperData.PoePort, ['intf_name', 'poe_intf_enabled', 'power_used', 'pd_class'], name, value)


    def clone_ptr(self):
        self._top_entity = PoeOperData()
        return self._top_entity




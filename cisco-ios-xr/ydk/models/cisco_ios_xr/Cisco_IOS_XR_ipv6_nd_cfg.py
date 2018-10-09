""" Cisco_IOS_XR_ipv6_nd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-nd package configuration.

This module contains definitions
for the following management objects\:
  ipv6\-neighbor\: IPv6 neighbor or neighbor discovery
    configuration

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ipv6NdRouterPref(Enum):
    """
    Ipv6NdRouterPref (Enum Class)

    Ipv6 nd router pref

    .. data:: high = 1

    	High preference

    .. data:: medium = 2

    	Medium preference

    .. data:: low = 3

    	Low preference

    """

    high = Enum.YLeaf(1, "high")

    medium = Enum.YLeaf(2, "medium")

    low = Enum.YLeaf(3, "low")


class Ipv6ndMonth(Enum):
    """
    Ipv6ndMonth (Enum Class)

    Ipv6nd month

    .. data:: january = 0

    	January

    .. data:: february = 1

    	February

    .. data:: march = 2

    	March

    .. data:: april = 3

    	April

    .. data:: may = 4

    	May

    .. data:: june = 5

    	June

    .. data:: july = 6

    	July

    .. data:: august = 7

    	August

    .. data:: september = 8

    	September

    .. data:: october = 9

    	October

    .. data:: november = 10

    	November

    .. data:: december = 11

    	December

    """

    january = Enum.YLeaf(0, "january")

    february = Enum.YLeaf(1, "february")

    march = Enum.YLeaf(2, "march")

    april = Enum.YLeaf(3, "april")

    may = Enum.YLeaf(4, "may")

    june = Enum.YLeaf(5, "june")

    july = Enum.YLeaf(6, "july")

    august = Enum.YLeaf(7, "august")

    september = Enum.YLeaf(8, "september")

    october = Enum.YLeaf(9, "october")

    november = Enum.YLeaf(10, "november")

    december = Enum.YLeaf(11, "december")


class Ipv6srpEncapsulation(Enum):
    """
    Ipv6srpEncapsulation (Enum Class)

    Ipv6srp encapsulation

    .. data:: srpa = 5

    	Encapsulation type SRP, prefer side A

    .. data:: srpb = 6

    	Encapsulation type SRP, prefer side B

    """

    srpa = Enum.YLeaf(5, "srpa")

    srpb = Enum.YLeaf(6, "srpb")



class Ipv6Neighbor(Entity):
    """
    IPv6 neighbor or neighbor discovery configuration
    
    .. attribute:: neighbors
    
    	IPv6 neighbors
    	**type**\:  :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg.Ipv6Neighbor.Neighbors>`
    
    .. attribute:: scavenge_timeout
    
    	Set lifetime for stale neighbor
    	**type**\: int
    
    	**range:** 1..43200
    
    	**units**\: second
    
    

    """

    _prefix = 'ipv6-nd-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(Ipv6Neighbor, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv6-neighbor"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-nd-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("neighbors", ("neighbors", Ipv6Neighbor.Neighbors))])
        self._leafs = OrderedDict([
            ('scavenge_timeout', (YLeaf(YType.uint32, 'scavenge-timeout'), ['int'])),
        ])
        self.scavenge_timeout = None

        self.neighbors = Ipv6Neighbor.Neighbors()
        self.neighbors.parent = self
        self._children_name_map["neighbors"] = "neighbors"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv6-nd-cfg:ipv6-neighbor"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ipv6Neighbor, ['scavenge_timeout'], name, value)


    class Neighbors(Entity):
        """
        IPv6 neighbors
        
        .. attribute:: neighbor
        
        	IPv6 neighbor configuration
        	**type**\: list of  		 :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg.Ipv6Neighbor.Neighbors.Neighbor>`
        
        

        """

        _prefix = 'ipv6-nd-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Ipv6Neighbor.Neighbors, self).__init__()

            self.yang_name = "neighbors"
            self.yang_parent_name = "ipv6-neighbor"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("neighbor", ("neighbor", Ipv6Neighbor.Neighbors.Neighbor))])
            self._leafs = OrderedDict()

            self.neighbor = YList(self)
            self._segment_path = lambda: "neighbors"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-nd-cfg:ipv6-neighbor/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv6Neighbor.Neighbors, [], name, value)


        class Neighbor(Entity):
            """
            IPv6 neighbor configuration
            
            .. attribute:: neighbor_address  (key)
            
            	IPv6 address
            	**type**\: str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: interface_name  (key)
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: zone
            
            	IPv6 address zone
            	**type**\: str
            
            	**default value**\: 0
            
            .. attribute:: mac_address
            
            	48\-bit hardware address H.H.H
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**mandatory**\: True
            
            .. attribute:: encapsulation
            
            	Encapsulation type only if interface type is SRP
            	**type**\:  :py:class:`Ipv6srpEncapsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg.Ipv6srpEncapsulation>`
            
            

            """

            _prefix = 'ipv6-nd-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ipv6Neighbor.Neighbors.Neighbor, self).__init__()

                self.yang_name = "neighbor"
                self.yang_parent_name = "neighbors"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['neighbor_address','interface_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str'])),
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('zone', (YLeaf(YType.str, 'zone'), ['str'])),
                    ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                    ('encapsulation', (YLeaf(YType.enumeration, 'encapsulation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg', 'Ipv6srpEncapsulation', '')])),
                ])
                self.neighbor_address = None
                self.interface_name = None
                self.zone = None
                self.mac_address = None
                self.encapsulation = None
                self._segment_path = lambda: "neighbor" + "[neighbor-address='" + str(self.neighbor_address) + "']" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-nd-cfg:ipv6-neighbor/neighbors/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv6Neighbor.Neighbors.Neighbor, ['neighbor_address', 'interface_name', 'zone', 'mac_address', 'encapsulation'], name, value)

    def clone_ptr(self):
        self._top_entity = Ipv6Neighbor()
        return self._top_entity


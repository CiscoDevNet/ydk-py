""" Cisco_IOS_XE_vlan_oper 

This module contains a collection of YANG definitions for
monitoring vlans in a Network Element.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class VlanStatusType(Enum):
    """
    VlanStatusType (Enum Class)

    Operational state of the VLAN

    .. data:: active = 0

    .. data:: suspend = 1

    """

    active = Enum.YLeaf(0, "active")

    suspend = Enum.YLeaf(1, "suspend")



class Vlans(Entity):
    """
    Informaton about VLANs
    
    .. attribute:: vlan
    
    	List of VLANs, keyed by id
    	**type**\: list of  		 :py:class:`Vlan <ydk.models.cisco_ios_xe.Cisco_IOS_XE_vlan_oper.Vlans.Vlan>`
    
    

    """

    _prefix = 'vlan-ios-xe-oper'
    _revision = '2017-05-05'

    def __init__(self):
        super(Vlans, self).__init__()
        self._top_entity = None

        self.yang_name = "vlans"
        self.yang_parent_name = "Cisco-IOS-XE-vlan-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("vlan", ("vlan", Vlans.Vlan))])
        self._leafs = OrderedDict()

        self.vlan = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-vlan-oper:vlans"

    def __setattr__(self, name, value):
        self._perform_setattr(Vlans, [], name, value)


    class Vlan(Entity):
        """
        List of VLANs, keyed by id
        
        .. attribute:: id  (key)
        
        	VLAN id
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: name
        
        	VLAN name
        	**type**\: str
        
        .. attribute:: status
        
        	VLAN status
        	**type**\:  :py:class:`VlanStatusType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_vlan_oper.VlanStatusType>`
        
        .. attribute:: ports
        
        	Assigned ports
        	**type**\: list of  		 :py:class:`Ports <ydk.models.cisco_ios_xe.Cisco_IOS_XE_vlan_oper.Vlans.Vlan.Ports>`
        
        

        """

        _prefix = 'vlan-ios-xe-oper'
        _revision = '2017-05-05'

        def __init__(self):
            super(Vlans.Vlan, self).__init__()

            self.yang_name = "vlan"
            self.yang_parent_name = "vlans"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['id']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ports", ("ports", Vlans.Vlan.Ports))])
            self._leafs = OrderedDict([
                ('id', YLeaf(YType.uint16, 'id')),
                ('name', YLeaf(YType.str, 'name')),
                ('status', YLeaf(YType.enumeration, 'status')),
            ])
            self.id = None
            self.name = None
            self.status = None

            self.ports = YList(self)
            self._segment_path = lambda: "vlan" + "[id='" + str(self.id) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-vlan-oper:vlans/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Vlans.Vlan, ['id', 'name', 'status'], name, value)


        class Ports(Entity):
            """
            Assigned ports
            
            .. attribute:: interface
            
            	Assigned interface
            	**type**\: str
            
            .. attribute:: subinterface
            
            	Assigned subinterface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'vlan-ios-xe-oper'
            _revision = '2017-05-05'

            def __init__(self):
                super(Vlans.Vlan.Ports, self).__init__()

                self.yang_name = "ports"
                self.yang_parent_name = "vlan"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('interface', YLeaf(YType.str, 'interface')),
                    ('subinterface', YLeaf(YType.uint32, 'subinterface')),
                ])
                self.interface = None
                self.subinterface = None
                self._segment_path = lambda: "ports"

            def __setattr__(self, name, value):
                self._perform_setattr(Vlans.Vlan.Ports, ['interface', 'subinterface'], name, value)

    def clone_ptr(self):
        self._top_entity = Vlans()
        return self._top_entity


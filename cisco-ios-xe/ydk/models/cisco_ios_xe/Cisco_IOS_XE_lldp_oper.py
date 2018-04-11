""" Cisco_IOS_XE_lldp_oper 

This module contains a collection of YANG definitions
for monitoring of LLDP state information.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class LldpEntries(Entity):
    """
    Data nodes for lldp entries
    
    .. attribute:: lldp_entry
    
    	The list of LLDP entries
    	**type**\: list of  		 :py:class:`LldpEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lldp_oper.LldpEntries.LldpEntry>`
    
    

    """

    _prefix = 'lldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(LldpEntries, self).__init__()
        self._top_entity = None

        self.yang_name = "lldp-entries"
        self.yang_parent_name = "Cisco-IOS-XE-lldp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("lldp-entry", ("lldp_entry", LldpEntries.LldpEntry))])
        self._leafs = OrderedDict()

        self.lldp_entry = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-lldp-oper:lldp-entries"

    def __setattr__(self, name, value):
        self._perform_setattr(LldpEntries, [], name, value)


    class LldpEntry(Entity):
        """
        The list of LLDP entries
        
        .. attribute:: device_id  (key)
        
        	Device ID of the link
        	**type**\: str
        
        .. attribute:: local_interface  (key)
        
        	Name of the local interface on the current device
        	**type**\: str
        
        .. attribute:: connecting_interface  (key)
        
        	Name of the connected interface to 'local\-interface'
        	**type**\: str
        
        .. attribute:: ttl
        
        	TTL denoting hold\-time of this link entry
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: capabilities
        
        	LLD device capabilities
        	**type**\:  :py:class:`Capabilities <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lldp_oper.LldpEntries.LldpEntry.Capabilities>`
        
        

        """

        _prefix = 'lldp-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(LldpEntries.LldpEntry, self).__init__()

            self.yang_name = "lldp-entry"
            self.yang_parent_name = "lldp-entries"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['device_id','local_interface','connecting_interface']
            self._child_container_classes = OrderedDict([("capabilities", ("capabilities", LldpEntries.LldpEntry.Capabilities))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('device_id', YLeaf(YType.str, 'device-id')),
                ('local_interface', YLeaf(YType.str, 'local-interface')),
                ('connecting_interface', YLeaf(YType.str, 'connecting-interface')),
                ('ttl', YLeaf(YType.uint32, 'ttl')),
            ])
            self.device_id = None
            self.local_interface = None
            self.connecting_interface = None
            self.ttl = None

            self.capabilities = LldpEntries.LldpEntry.Capabilities()
            self.capabilities.parent = self
            self._children_name_map["capabilities"] = "capabilities"
            self._children_yang_names.add("capabilities")
            self._segment_path = lambda: "lldp-entry" + "[device-id='" + str(self.device_id) + "']" + "[local-interface='" + str(self.local_interface) + "']" + "[connecting-interface='" + str(self.connecting_interface) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-lldp-oper:lldp-entries/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(LldpEntries.LldpEntry, ['device_id', 'local_interface', 'connecting_interface', 'ttl'], name, value)


        class Capabilities(Entity):
            """
            LLD device capabilities
            
            .. attribute:: repeater
            
            	Repeater
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: bridge
            
            	Bridge
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: access_point
            
            	Access point
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: router
            
            	Router
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: telephone
            
            	Phone
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: docsis
            
            	Docsis
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: station
            
            	Station
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: other
            
            	Other
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'lldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(LldpEntries.LldpEntry.Capabilities, self).__init__()

                self.yang_name = "capabilities"
                self.yang_parent_name = "lldp-entry"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('repeater', YLeaf(YType.empty, 'repeater')),
                    ('bridge', YLeaf(YType.empty, 'bridge')),
                    ('access_point', YLeaf(YType.empty, 'access-point')),
                    ('router', YLeaf(YType.empty, 'router')),
                    ('telephone', YLeaf(YType.empty, 'telephone')),
                    ('docsis', YLeaf(YType.empty, 'docsis')),
                    ('station', YLeaf(YType.empty, 'station')),
                    ('other', YLeaf(YType.empty, 'other')),
                ])
                self.repeater = None
                self.bridge = None
                self.access_point = None
                self.router = None
                self.telephone = None
                self.docsis = None
                self.station = None
                self.other = None
                self._segment_path = lambda: "capabilities"

            def __setattr__(self, name, value):
                self._perform_setattr(LldpEntries.LldpEntry.Capabilities, ['repeater', 'bridge', 'access_point', 'router', 'telephone', 'docsis', 'station', 'other'], name, value)

    def clone_ptr(self):
        self._top_entity = LldpEntries()
        return self._top_entity


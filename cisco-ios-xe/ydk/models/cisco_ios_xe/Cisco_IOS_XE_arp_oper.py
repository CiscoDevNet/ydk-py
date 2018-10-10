""" Cisco_IOS_XE_arp_oper 

This module contains a collection of YANG definitions
for IOS\-XE ARP operational data.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IosArpMode(Enum):
    """
    IosArpMode (Enum Class)

    The mode that this entry is running in

    .. data:: ios_arp_mode_null = 0

    	Undefined - error

    .. data:: ios_arp_mode_dynamic = 1

    	Entry has been learned

    .. data:: ios_arp_mode_incomplete = 2

    	We've requested, but have no reply yet

    .. data:: ios_arp_mode_interface = 3

    	Interface entry

    .. data:: ios_arp_mode_static = 4

    	Static Entry

    .. data:: ios_arp_mode_alias = 5

    	Static - We're fronting this host

    .. data:: ios_arp_mode_app_simple = 6

    	Simple Application ARP

    .. data:: ios_arp_mode_app_alias = 7

    	Application Alias

    .. data:: ios_arp_mode_app_timer = 8

    	Application Timer

    """

    ios_arp_mode_null = Enum.YLeaf(0, "ios-arp-mode-null")

    ios_arp_mode_dynamic = Enum.YLeaf(1, "ios-arp-mode-dynamic")

    ios_arp_mode_incomplete = Enum.YLeaf(2, "ios-arp-mode-incomplete")

    ios_arp_mode_interface = Enum.YLeaf(3, "ios-arp-mode-interface")

    ios_arp_mode_static = Enum.YLeaf(4, "ios-arp-mode-static")

    ios_arp_mode_alias = Enum.YLeaf(5, "ios-arp-mode-alias")

    ios_arp_mode_app_simple = Enum.YLeaf(6, "ios-arp-mode-app-simple")

    ios_arp_mode_app_alias = Enum.YLeaf(7, "ios-arp-mode-app-alias")

    ios_arp_mode_app_timer = Enum.YLeaf(8, "ios-arp-mode-app-timer")



class ArpData(Entity):
    """
    This module contains a collection of YANG definitions for
    monitoring the operation of IOS\-XE ARP.
    Copyright (c) 2018 by Cisco Systems, Inc.
    All rights reserved.
    
    .. attribute:: arp_vrf
    
    	List of current VRFs
    	**type**\: list of  		 :py:class:`ArpVrf <ydk.models.cisco_ios_xe.Cisco_IOS_XE_arp_oper.ArpData.ArpVrf>`
    
    

    """

    _prefix = 'arp-ios-xe-oper'
    _revision = '2017-12-13'

    def __init__(self):
        super(ArpData, self).__init__()
        self._top_entity = None

        self.yang_name = "arp-data"
        self.yang_parent_name = "Cisco-IOS-XE-arp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("arp-vrf", ("arp_vrf", ArpData.ArpVrf))])
        self._leafs = OrderedDict()

        self.arp_vrf = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-arp-oper:arp-data"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ArpData, [], name, value)


    class ArpVrf(Entity):
        """
        List of current VRFs
        
        .. attribute:: vrf  (key)
        
        	VRF name that this entry is tied to
        	**type**\: str
        
        .. attribute:: arp_oper
        
        	ARP entries associated with this VRF
        	**type**\: list of  		 :py:class:`ArpOper <ydk.models.cisco_ios_xe.Cisco_IOS_XE_arp_oper.ArpData.ArpVrf.ArpOper>`
        
        

        """

        _prefix = 'arp-ios-xe-oper'
        _revision = '2017-12-13'

        def __init__(self):
            super(ArpData.ArpVrf, self).__init__()

            self.yang_name = "arp-vrf"
            self.yang_parent_name = "arp-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['vrf']
            self._child_classes = OrderedDict([("arp-oper", ("arp_oper", ArpData.ArpVrf.ArpOper))])
            self._leafs = OrderedDict([
                ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
            ])
            self.vrf = None

            self.arp_oper = YList(self)
            self._segment_path = lambda: "arp-vrf" + "[vrf='" + str(self.vrf) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-arp-oper:arp-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ArpData.ArpVrf, ['vrf'], name, value)


        class ArpOper(Entity):
            """
            ARP entries associated with this VRF
            
            .. attribute:: address  (key)
            
            	High level protocol address
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: enctype
            
            	Protocol that produced the entry
            	**type**\:  :py:class:`IosEncapsType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ios_common_oper.IosEncapsType>`
            
            .. attribute:: interface
            
            	Interface associated with this ARP entry
            	**type**\: str
            
            .. attribute:: type
            
            	Protocol that this ARP entry belongs to
            	**type**\:  :py:class:`IosLinktype <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ios_common_oper.IosLinktype>`
            
            .. attribute:: mode
            
            	The mode that this entry is running in
            	**type**\:  :py:class:`IosArpMode <ydk.models.cisco_ios_xe.Cisco_IOS_XE_arp_oper.IosArpMode>`
            
            .. attribute:: hwtype
            
            	Type of HW address
            	**type**\:  :py:class:`IosSnpaType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ios_common_oper.IosSnpaType>`
            
            .. attribute:: hardware
            
            	hardware address
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: time
            
            	Time of the last update
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            

            """

            _prefix = 'arp-ios-xe-oper'
            _revision = '2017-12-13'

            def __init__(self):
                super(ArpData.ArpVrf.ArpOper, self).__init__()

                self.yang_name = "arp-oper"
                self.yang_parent_name = "arp-vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['address']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                    ('enctype', (YLeaf(YType.enumeration, 'enctype'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_ios_common_oper', 'IosEncapsType', '')])),
                    ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_ios_common_oper', 'IosLinktype', '')])),
                    ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_arp_oper', 'IosArpMode', '')])),
                    ('hwtype', (YLeaf(YType.enumeration, 'hwtype'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_ios_common_oper', 'IosSnpaType', '')])),
                    ('hardware', (YLeaf(YType.str, 'hardware'), ['str'])),
                    ('time', (YLeaf(YType.str, 'time'), ['str'])),
                ])
                self.address = None
                self.enctype = None
                self.interface = None
                self.type = None
                self.mode = None
                self.hwtype = None
                self.hardware = None
                self.time = None
                self._segment_path = lambda: "arp-oper" + "[address='" + str(self.address) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ArpData.ArpVrf.ArpOper, ['address', 'enctype', 'interface', 'type', 'mode', 'hwtype', 'hardware', 'time'], name, value)

    def clone_ptr(self):
        self._top_entity = ArpData()
        return self._top_entity


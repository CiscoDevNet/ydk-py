""" Cisco_IOS_XR_accounting_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR accounting package configuration.

This module contains definitions
for the following management objects\:
  accounting\: Global Accounting configuration commands

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Accounting(Entity):
    """
    Global Accounting configuration commands
    
    .. attribute:: interfaces
    
    	Interfaces configuration
    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_accounting_cfg.Accounting.Interfaces>`
    
    .. attribute:: enable
    
    	Enable Accounting
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'accounting-cfg'
    _revision = '2017-05-31'

    def __init__(self):
        super(Accounting, self).__init__()
        self._top_entity = None

        self.yang_name = "accounting"
        self.yang_parent_name = "Cisco-IOS-XR-accounting-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("interfaces", ("interfaces", Accounting.Interfaces))])
        self._leafs = OrderedDict([
            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
        ])
        self.enable = None

        self.interfaces = Accounting.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._segment_path = lambda: "Cisco-IOS-XR-accounting-cfg:accounting"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Accounting, ['enable'], name, value)


    class Interfaces(Entity):
        """
        Interfaces configuration
        
        .. attribute:: mpls
        
        	Interfaces MPLS configuration
        	**type**\:  :py:class:`Mpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_accounting_cfg.Accounting.Interfaces.Mpls>`
        
        .. attribute:: segment_routing
        
        	Interfaces Segment Routing configuration
        	**type**\:  :py:class:`SegmentRouting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_accounting_cfg.Accounting.Interfaces.SegmentRouting>`
        
        .. attribute:: enable
        
        	Enable accounting on Interfaces
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'accounting-cfg'
        _revision = '2017-05-31'

        def __init__(self):
            super(Accounting.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "accounting"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mpls", ("mpls", Accounting.Interfaces.Mpls)), ("segment-routing", ("segment_routing", Accounting.Interfaces.SegmentRouting))])
            self._leafs = OrderedDict([
                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ])
            self.enable = None

            self.mpls = Accounting.Interfaces.Mpls()
            self.mpls.parent = self
            self._children_name_map["mpls"] = "mpls"

            self.segment_routing = Accounting.Interfaces.SegmentRouting()
            self.segment_routing.parent = self
            self._children_name_map["segment_routing"] = "segment-routing"
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-accounting-cfg:accounting/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Accounting.Interfaces, ['enable'], name, value)


        class Mpls(Entity):
            """
            Interfaces MPLS configuration
            
            .. attribute:: enable
            
            	Enable accounting on MPLS
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enable_v4rsvpte
            
            	Enable accounting on MPLS IPv4 RSVP TE
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'accounting-cfg'
            _revision = '2017-05-31'

            def __init__(self):
                super(Accounting.Interfaces.Mpls, self).__init__()

                self.yang_name = "mpls"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ('enable_v4rsvpte', (YLeaf(YType.empty, 'enable-v4rsvpte'), ['Empty'])),
                ])
                self.enable = None
                self.enable_v4rsvpte = None
                self._segment_path = lambda: "mpls"
                self._absolute_path = lambda: "Cisco-IOS-XR-accounting-cfg:accounting/interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Accounting.Interfaces.Mpls, ['enable', 'enable_v4rsvpte'], name, value)


        class SegmentRouting(Entity):
            """
            Interfaces Segment Routing configuration
            
            .. attribute:: enable
            
            	Enable accounting on Segment Routing
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enable_mplsv4
            
            	Enable accounting on Segment Routing MPLS IPv4
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enable_mplsv6
            
            	Enable accounting on Segment Routing MPLS IPv6
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'accounting-cfg'
            _revision = '2017-05-31'

            def __init__(self):
                super(Accounting.Interfaces.SegmentRouting, self).__init__()

                self.yang_name = "segment-routing"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ('enable_mplsv4', (YLeaf(YType.empty, 'enable-mplsv4'), ['Empty'])),
                    ('enable_mplsv6', (YLeaf(YType.empty, 'enable-mplsv6'), ['Empty'])),
                ])
                self.enable = None
                self.enable_mplsv4 = None
                self.enable_mplsv6 = None
                self._segment_path = lambda: "segment-routing"
                self._absolute_path = lambda: "Cisco-IOS-XR-accounting-cfg:accounting/interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Accounting.Interfaces.SegmentRouting, ['enable', 'enable_mplsv4', 'enable_mplsv6'], name, value)

    def clone_ptr(self):
        self._top_entity = Accounting()
        return self._top_entity


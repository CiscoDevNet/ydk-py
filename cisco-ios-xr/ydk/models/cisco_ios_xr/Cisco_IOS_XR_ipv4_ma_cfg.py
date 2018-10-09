""" Cisco_IOS_XR_ipv4_ma_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-ma package configuration.

This module contains definitions
for the following management objects\:
  ipv4\-network\-global\: IPv4 network global configuration data
  subscriber\-pta\: subscriber pta

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ipv4Qppb(Enum):
    """
    Ipv4Qppb (Enum Class)

    Ipv4 qppb

    .. data:: none = 0

    	No QPPB configuration

    .. data:: ip_prec = 1

    	Enable ip-precedence based QPPB

    .. data:: qos_grp = 2

    	Enable qos-group based QPPB

    .. data:: both = 3

    	Enable both ip-precedence and qos-group based

    	QPPB

    """

    none = Enum.YLeaf(0, "none")

    ip_prec = Enum.YLeaf(1, "ip-prec")

    qos_grp = Enum.YLeaf(2, "qos-grp")

    both = Enum.YLeaf(3, "both")



class Ipv4NetworkGlobal(Entity):
    """
    IPv4 network global configuration data
    
    .. attribute:: unnumbered
    
    	Enable IPv4 processing without an explicit address
    	**type**\:  :py:class:`Unnumbered <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg.Ipv4NetworkGlobal.Unnumbered>`
    
    .. attribute:: qppb
    
    	QPPB
    	**type**\:  :py:class:`Qppb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg.Ipv4NetworkGlobal.Qppb>`
    
    .. attribute:: source_route
    
    	The flag for enabling whether to process packets with source routing header options
    	**type**\: bool
    
    	**default value**\: true
    
    .. attribute:: reassemble_max_packets
    
    	Percentage of total packets available in the system
    	**type**\: int
    
    	**range:** 1..50
    
    	**units**\: percentage
    
    .. attribute:: reassemble_time_out
    
    	Number of seconds a reassembly queue will hold before timeout
    	**type**\: int
    
    	**range:** 1..120
    
    	**units**\: second
    
    

    """

    _prefix = 'ipv4-ma-cfg'
    _revision = '2015-07-30'

    def __init__(self):
        super(Ipv4NetworkGlobal, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv4-network-global"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-ma-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("unnumbered", ("unnumbered", Ipv4NetworkGlobal.Unnumbered)), ("qppb", ("qppb", Ipv4NetworkGlobal.Qppb))])
        self._leafs = OrderedDict([
            ('source_route', (YLeaf(YType.boolean, 'source-route'), ['bool'])),
            ('reassemble_max_packets', (YLeaf(YType.uint32, 'reassemble-max-packets'), ['int'])),
            ('reassemble_time_out', (YLeaf(YType.uint32, 'reassemble-time-out'), ['int'])),
        ])
        self.source_route = None
        self.reassemble_max_packets = None
        self.reassemble_time_out = None

        self.unnumbered = Ipv4NetworkGlobal.Unnumbered()
        self.unnumbered.parent = self
        self._children_name_map["unnumbered"] = "unnumbered"

        self.qppb = Ipv4NetworkGlobal.Qppb()
        self.qppb.parent = self
        self._children_name_map["qppb"] = "qppb"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-ma-cfg:ipv4-network-global"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ipv4NetworkGlobal, ['source_route', 'reassemble_max_packets', 'reassemble_time_out'], name, value)


    class Unnumbered(Entity):
        """
        Enable IPv4 processing without an explicit
        address
        
        .. attribute:: mpls
        
        	Configure MPLS routing protocol parameters
        	**type**\:  :py:class:`Mpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg.Ipv4NetworkGlobal.Unnumbered.Mpls>`
        
        

        """

        _prefix = 'ipv4-ma-cfg'
        _revision = '2015-07-30'

        def __init__(self):
            super(Ipv4NetworkGlobal.Unnumbered, self).__init__()

            self.yang_name = "unnumbered"
            self.yang_parent_name = "ipv4-network-global"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mpls", ("mpls", Ipv4NetworkGlobal.Unnumbered.Mpls))])
            self._leafs = OrderedDict()

            self.mpls = Ipv4NetworkGlobal.Unnumbered.Mpls()
            self.mpls.parent = self
            self._children_name_map["mpls"] = "mpls"
            self._segment_path = lambda: "unnumbered"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ma-cfg:ipv4-network-global/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4NetworkGlobal.Unnumbered, [], name, value)


        class Mpls(Entity):
            """
            Configure MPLS routing protocol parameters
            
            .. attribute:: te
            
            	IPv4 commands for MPLS Traffic Engineering
            	**type**\:  :py:class:`Te <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg.Ipv4NetworkGlobal.Unnumbered.Mpls.Te>`
            
            

            """

            _prefix = 'ipv4-ma-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                super(Ipv4NetworkGlobal.Unnumbered.Mpls, self).__init__()

                self.yang_name = "mpls"
                self.yang_parent_name = "unnumbered"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("te", ("te", Ipv4NetworkGlobal.Unnumbered.Mpls.Te))])
                self._leafs = OrderedDict()

                self.te = Ipv4NetworkGlobal.Unnumbered.Mpls.Te()
                self.te.parent = self
                self._children_name_map["te"] = "te"
                self._segment_path = lambda: "mpls"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ma-cfg:ipv4-network-global/unnumbered/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4NetworkGlobal.Unnumbered.Mpls, [], name, value)


            class Te(Entity):
                """
                IPv4 commands for MPLS Traffic Engineering
                
                .. attribute:: interface
                
                	Enable IP processing without an explicit address on MPLS Traffic\-Eng
                	**type**\: str
                
                

                """

                _prefix = 'ipv4-ma-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Ipv4NetworkGlobal.Unnumbered.Mpls.Te, self).__init__()

                    self.yang_name = "te"
                    self.yang_parent_name = "mpls"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                    ])
                    self.interface = None
                    self._segment_path = lambda: "te"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ma-cfg:ipv4-network-global/unnumbered/mpls/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4NetworkGlobal.Unnumbered.Mpls.Te, ['interface'], name, value)


    class Qppb(Entity):
        """
        QPPB
        
        .. attribute:: source
        
        	QPPB configuration on source
        	**type**\:  :py:class:`Ipv4Qppb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg.Ipv4Qppb>`
        
        .. attribute:: destination
        
        	QPPB configuration on destination
        	**type**\:  :py:class:`Ipv4Qppb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg.Ipv4Qppb>`
        
        

        """

        _prefix = 'ipv4-ma-cfg'
        _revision = '2015-07-30'

        def __init__(self):
            super(Ipv4NetworkGlobal.Qppb, self).__init__()

            self.yang_name = "qppb"
            self.yang_parent_name = "ipv4-network-global"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('source', (YLeaf(YType.enumeration, 'source'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg', 'Ipv4Qppb', '')])),
                ('destination', (YLeaf(YType.enumeration, 'destination'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg', 'Ipv4Qppb', '')])),
            ])
            self.source = None
            self.destination = None
            self._segment_path = lambda: "qppb"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ma-cfg:ipv4-network-global/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4NetworkGlobal.Qppb, ['source', 'destination'], name, value)

    def clone_ptr(self):
        self._top_entity = Ipv4NetworkGlobal()
        return self._top_entity

class SubscriberPta(Entity):
    """
    subscriber pta
    
    .. attribute:: tcp_mss_adjust
    
    	TCP MSS Adjust (bytes)
    	**type**\: int
    
    	**range:** 1280..1536
    
    	**units**\: byte
    
    

    """

    _prefix = 'ipv4-ma-cfg'
    _revision = '2015-07-30'

    def __init__(self):
        super(SubscriberPta, self).__init__()
        self._top_entity = None

        self.yang_name = "subscriber-pta"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-ma-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('tcp_mss_adjust', (YLeaf(YType.uint32, 'tcp-mss-adjust'), ['int'])),
        ])
        self.tcp_mss_adjust = None
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-ma-cfg:subscriber-pta"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SubscriberPta, ['tcp_mss_adjust'], name, value)

    def clone_ptr(self):
        self._top_entity = SubscriberPta()
        return self._top_entity


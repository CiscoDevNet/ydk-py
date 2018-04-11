""" Cisco_IOS_XR_subscriber_pppoe_ma_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-pppoe\-ma package operational data.

This module contains definitions
for the following management objects\:
  pppoe\: PPPoE operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class PppoeMaLimitState(Enum):
    """
    PppoeMaLimitState (Enum Class)

    Pppoe ma limit state

    .. data:: ok = 0

    	OK State

    .. data:: warning = 1

    	Warn State

    .. data:: block = 2

    	Block State

    """

    ok = Enum.YLeaf(0, "ok")

    warning = Enum.YLeaf(1, "warning")

    block = Enum.YLeaf(2, "block")


class PppoeMaSessionIdbSrgState(Enum):
    """
    PppoeMaSessionIdbSrgState (Enum Class)

    Pppoe ma session idb srg state

    .. data:: none = 0

    	SRG-None state

    .. data:: active = 1

    	SRG-Active state

    .. data:: standby = 2

    	SRG-Standby state

    """

    none = Enum.YLeaf(0, "none")

    active = Enum.YLeaf(1, "active")

    standby = Enum.YLeaf(2, "standby")


class PppoeMaThrottleState(Enum):
    """
    PppoeMaThrottleState (Enum Class)

    Pppoe ma throttle state

    .. data:: idle = 0

    	Idle State

    .. data:: monitor = 1

    	Monitor State

    .. data:: block = 2

    	Block State

    """

    idle = Enum.YLeaf(0, "idle")

    monitor = Enum.YLeaf(1, "monitor")

    block = Enum.YLeaf(2, "block")



class Pppoe(Entity):
    """
    PPPoE operational data
    
    .. attribute:: access_interface_statistics
    
    	PPPoE access interface statistics information
    	**type**\:  :py:class:`AccessInterfaceStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics>`
    
    .. attribute:: nodes
    
    	Per\-node PPPoE operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes>`
    
    

    """

    _prefix = 'subscriber-pppoe-ma-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Pppoe, self).__init__()
        self._top_entity = None

        self.yang_name = "pppoe"
        self.yang_parent_name = "Cisco-IOS-XR-subscriber-pppoe-ma-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("access-interface-statistics", ("access_interface_statistics", Pppoe.AccessInterfaceStatistics)), ("nodes", ("nodes", Pppoe.Nodes))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.access_interface_statistics = Pppoe.AccessInterfaceStatistics()
        self.access_interface_statistics.parent = self
        self._children_name_map["access_interface_statistics"] = "access-interface-statistics"
        self._children_yang_names.add("access-interface-statistics")

        self.nodes = Pppoe.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-subscriber-pppoe-ma-oper:pppoe"


    class AccessInterfaceStatistics(Entity):
        """
        PPPoE access interface statistics information
        
        .. attribute:: access_interface_statistic
        
        	Statistics information for a PPPoE\-enabled access interface
        	**type**\: list of  		 :py:class:`AccessInterfaceStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic>`
        
        

        """

        _prefix = 'subscriber-pppoe-ma-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Pppoe.AccessInterfaceStatistics, self).__init__()

            self.yang_name = "access-interface-statistics"
            self.yang_parent_name = "pppoe"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("access-interface-statistic", ("access_interface_statistic", Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic))])
            self._leafs = OrderedDict()

            self.access_interface_statistic = YList(self)
            self._segment_path = lambda: "access-interface-statistics"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-pppoe-ma-oper:pppoe/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Pppoe.AccessInterfaceStatistics, [], name, value)


        class AccessInterfaceStatistic(Entity):
            """
            Statistics information for a PPPoE\-enabled
            access interface
            
            .. attribute:: interface_name  (key)
            
            	PPPoE Access Interface
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: packet_counts
            
            	Packet Counts
            	**type**\:  :py:class:`PacketCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts>`
            
            

            """

            _prefix = 'subscriber-pppoe-ma-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic, self).__init__()

                self.yang_name = "access-interface-statistic"
                self.yang_parent_name = "access-interface-statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_container_classes = OrderedDict([("packet-counts", ("packet_counts", Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                ])
                self.interface_name = None

                self.packet_counts = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts()
                self.packet_counts.parent = self
                self._children_name_map["packet_counts"] = "packet-counts"
                self._children_yang_names.add("packet-counts")
                self._segment_path = lambda: "access-interface-statistic" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-pppoe-ma-oper:pppoe/access-interface-statistics/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic, ['interface_name'], name, value)


            class PacketCounts(Entity):
                """
                Packet Counts
                
                .. attribute:: padi
                
                	PADI counts
                	**type**\:  :py:class:`Padi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padi>`
                
                .. attribute:: pado
                
                	PADO counts
                	**type**\:  :py:class:`Pado <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Pado>`
                
                .. attribute:: padr
                
                	PADR counts
                	**type**\:  :py:class:`Padr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padr>`
                
                .. attribute:: pads_success
                
                	PADS Success counts
                	**type**\:  :py:class:`PadsSuccess <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsSuccess>`
                
                .. attribute:: pads_error
                
                	PADS Error counts
                	**type**\:  :py:class:`PadsError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsError>`
                
                .. attribute:: padt
                
                	PADT counts
                	**type**\:  :py:class:`Padt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padt>`
                
                .. attribute:: session_state
                
                	Session Stage counts
                	**type**\:  :py:class:`SessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.SessionState>`
                
                .. attribute:: other
                
                	Other counts
                	**type**\:  :py:class:`Other <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Other>`
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts, self).__init__()

                    self.yang_name = "packet-counts"
                    self.yang_parent_name = "access-interface-statistic"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("padi", ("padi", Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padi)), ("pado", ("pado", Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Pado)), ("padr", ("padr", Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padr)), ("pads-success", ("pads_success", Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsSuccess)), ("pads-error", ("pads_error", Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsError)), ("padt", ("padt", Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padt)), ("session-state", ("session_state", Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.SessionState)), ("other", ("other", Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Other))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.padi = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padi()
                    self.padi.parent = self
                    self._children_name_map["padi"] = "padi"
                    self._children_yang_names.add("padi")

                    self.pado = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Pado()
                    self.pado.parent = self
                    self._children_name_map["pado"] = "pado"
                    self._children_yang_names.add("pado")

                    self.padr = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padr()
                    self.padr.parent = self
                    self._children_name_map["padr"] = "padr"
                    self._children_yang_names.add("padr")

                    self.pads_success = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsSuccess()
                    self.pads_success.parent = self
                    self._children_name_map["pads_success"] = "pads-success"
                    self._children_yang_names.add("pads-success")

                    self.pads_error = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsError()
                    self.pads_error.parent = self
                    self._children_name_map["pads_error"] = "pads-error"
                    self._children_yang_names.add("pads-error")

                    self.padt = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padt()
                    self.padt.parent = self
                    self._children_name_map["padt"] = "padt"
                    self._children_yang_names.add("padt")

                    self.session_state = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.SessionState()
                    self.session_state.parent = self
                    self._children_name_map["session_state"] = "session-state"
                    self._children_yang_names.add("session-state")

                    self.other = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Other()
                    self.other.parent = self
                    self._children_name_map["other"] = "other"
                    self._children_yang_names.add("other")
                    self._segment_path = lambda: "packet-counts"


                class Padi(Entity):
                    """
                    PADI counts
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padi, self).__init__()

                        self.yang_name = "padi"
                        self.yang_parent_name = "packet-counts"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sent', YLeaf(YType.uint32, 'sent')),
                            ('received', YLeaf(YType.uint32, 'received')),
                            ('dropped', YLeaf(YType.uint32, 'dropped')),
                        ])
                        self.sent = None
                        self.received = None
                        self.dropped = None
                        self._segment_path = lambda: "padi"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padi, ['sent', 'received', 'dropped'], name, value)


                class Pado(Entity):
                    """
                    PADO counts
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Pado, self).__init__()

                        self.yang_name = "pado"
                        self.yang_parent_name = "packet-counts"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sent', YLeaf(YType.uint32, 'sent')),
                            ('received', YLeaf(YType.uint32, 'received')),
                            ('dropped', YLeaf(YType.uint32, 'dropped')),
                        ])
                        self.sent = None
                        self.received = None
                        self.dropped = None
                        self._segment_path = lambda: "pado"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Pado, ['sent', 'received', 'dropped'], name, value)


                class Padr(Entity):
                    """
                    PADR counts
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padr, self).__init__()

                        self.yang_name = "padr"
                        self.yang_parent_name = "packet-counts"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sent', YLeaf(YType.uint32, 'sent')),
                            ('received', YLeaf(YType.uint32, 'received')),
                            ('dropped', YLeaf(YType.uint32, 'dropped')),
                        ])
                        self.sent = None
                        self.received = None
                        self.dropped = None
                        self._segment_path = lambda: "padr"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padr, ['sent', 'received', 'dropped'], name, value)


                class PadsSuccess(Entity):
                    """
                    PADS Success counts
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsSuccess, self).__init__()

                        self.yang_name = "pads-success"
                        self.yang_parent_name = "packet-counts"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sent', YLeaf(YType.uint32, 'sent')),
                            ('received', YLeaf(YType.uint32, 'received')),
                            ('dropped', YLeaf(YType.uint32, 'dropped')),
                        ])
                        self.sent = None
                        self.received = None
                        self.dropped = None
                        self._segment_path = lambda: "pads-success"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsSuccess, ['sent', 'received', 'dropped'], name, value)


                class PadsError(Entity):
                    """
                    PADS Error counts
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsError, self).__init__()

                        self.yang_name = "pads-error"
                        self.yang_parent_name = "packet-counts"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sent', YLeaf(YType.uint32, 'sent')),
                            ('received', YLeaf(YType.uint32, 'received')),
                            ('dropped', YLeaf(YType.uint32, 'dropped')),
                        ])
                        self.sent = None
                        self.received = None
                        self.dropped = None
                        self._segment_path = lambda: "pads-error"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsError, ['sent', 'received', 'dropped'], name, value)


                class Padt(Entity):
                    """
                    PADT counts
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padt, self).__init__()

                        self.yang_name = "padt"
                        self.yang_parent_name = "packet-counts"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sent', YLeaf(YType.uint32, 'sent')),
                            ('received', YLeaf(YType.uint32, 'received')),
                            ('dropped', YLeaf(YType.uint32, 'dropped')),
                        ])
                        self.sent = None
                        self.received = None
                        self.dropped = None
                        self._segment_path = lambda: "padt"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padt, ['sent', 'received', 'dropped'], name, value)


                class SessionState(Entity):
                    """
                    Session Stage counts
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.SessionState, self).__init__()

                        self.yang_name = "session-state"
                        self.yang_parent_name = "packet-counts"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sent', YLeaf(YType.uint32, 'sent')),
                            ('received', YLeaf(YType.uint32, 'received')),
                            ('dropped', YLeaf(YType.uint32, 'dropped')),
                        ])
                        self.sent = None
                        self.received = None
                        self.dropped = None
                        self._segment_path = lambda: "session-state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.SessionState, ['sent', 'received', 'dropped'], name, value)


                class Other(Entity):
                    """
                    Other counts
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Other, self).__init__()

                        self.yang_name = "other"
                        self.yang_parent_name = "packet-counts"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sent', YLeaf(YType.uint32, 'sent')),
                            ('received', YLeaf(YType.uint32, 'received')),
                            ('dropped', YLeaf(YType.uint32, 'dropped')),
                        ])
                        self.sent = None
                        self.received = None
                        self.dropped = None
                        self._segment_path = lambda: "other"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Other, ['sent', 'received', 'dropped'], name, value)


    class Nodes(Entity):
        """
        Per\-node PPPoE operational data
        
        .. attribute:: node
        
        	PPPoE operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node>`
        
        

        """

        _prefix = 'subscriber-pppoe-ma-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Pppoe.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "pppoe"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("node", ("node", Pppoe.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-pppoe-ma-oper:pppoe/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Pppoe.Nodes, [], name, value)


        class Node(Entity):
            """
            PPPoE operational data for a particular node
            
            .. attribute:: node_name  (key)
            
            	Node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: statistics
            
            	PPPoE statistics for a given node
            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics>`
            
            .. attribute:: access_interface
            
            	PPPoE access interface information
            	**type**\:  :py:class:`AccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.AccessInterface>`
            
            .. attribute:: interfaces
            
            	Per interface PPPoE operational data
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Interfaces>`
            
            .. attribute:: bba_groups
            
            	PPPoE BBA\-Group information
            	**type**\:  :py:class:`BbaGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups>`
            
            .. attribute:: summary_total
            
            	PPPoE statistics for a given node
            	**type**\:  :py:class:`SummaryTotal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.SummaryTotal>`
            
            

            """

            _prefix = 'subscriber-pppoe-ma-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Pppoe.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_container_classes = OrderedDict([("statistics", ("statistics", Pppoe.Nodes.Node.Statistics)), ("access-interface", ("access_interface", Pppoe.Nodes.Node.AccessInterface)), ("interfaces", ("interfaces", Pppoe.Nodes.Node.Interfaces)), ("bba-groups", ("bba_groups", Pppoe.Nodes.Node.BbaGroups)), ("summary-total", ("summary_total", Pppoe.Nodes.Node.SummaryTotal))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node_name', YLeaf(YType.str, 'node-name')),
                ])
                self.node_name = None

                self.statistics = Pppoe.Nodes.Node.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
                self._children_yang_names.add("statistics")

                self.access_interface = Pppoe.Nodes.Node.AccessInterface()
                self.access_interface.parent = self
                self._children_name_map["access_interface"] = "access-interface"
                self._children_yang_names.add("access-interface")

                self.interfaces = Pppoe.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.bba_groups = Pppoe.Nodes.Node.BbaGroups()
                self.bba_groups.parent = self
                self._children_name_map["bba_groups"] = "bba-groups"
                self._children_yang_names.add("bba-groups")

                self.summary_total = Pppoe.Nodes.Node.SummaryTotal()
                self.summary_total.parent = self
                self._children_name_map["summary_total"] = "summary-total"
                self._children_yang_names.add("summary-total")
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-pppoe-ma-oper:pppoe/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Pppoe.Nodes.Node, ['node_name'], name, value)


            class Statistics(Entity):
                """
                PPPoE statistics for a given node
                
                .. attribute:: packet_counts
                
                	Packet Counts
                	**type**\:  :py:class:`PacketCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts>`
                
                .. attribute:: packet_error_counts
                
                	Packet Error Counts
                	**type**\:  :py:class:`PacketErrorCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketErrorCounts>`
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Pppoe.Nodes.Node.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("packet-counts", ("packet_counts", Pppoe.Nodes.Node.Statistics.PacketCounts)), ("packet-error-counts", ("packet_error_counts", Pppoe.Nodes.Node.Statistics.PacketErrorCounts))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.packet_counts = Pppoe.Nodes.Node.Statistics.PacketCounts()
                    self.packet_counts.parent = self
                    self._children_name_map["packet_counts"] = "packet-counts"
                    self._children_yang_names.add("packet-counts")

                    self.packet_error_counts = Pppoe.Nodes.Node.Statistics.PacketErrorCounts()
                    self.packet_error_counts.parent = self
                    self._children_name_map["packet_error_counts"] = "packet-error-counts"
                    self._children_yang_names.add("packet-error-counts")
                    self._segment_path = lambda: "statistics"


                class PacketCounts(Entity):
                    """
                    Packet Counts
                    
                    .. attribute:: padi
                    
                    	PADI counts
                    	**type**\:  :py:class:`Padi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.Padi>`
                    
                    .. attribute:: pado
                    
                    	PADO counts
                    	**type**\:  :py:class:`Pado <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.Pado>`
                    
                    .. attribute:: padr
                    
                    	PADR counts
                    	**type**\:  :py:class:`Padr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.Padr>`
                    
                    .. attribute:: pads_success
                    
                    	PADS Success counts
                    	**type**\:  :py:class:`PadsSuccess <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.PadsSuccess>`
                    
                    .. attribute:: pads_error
                    
                    	PADS Error counts
                    	**type**\:  :py:class:`PadsError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.PadsError>`
                    
                    .. attribute:: padt
                    
                    	PADT counts
                    	**type**\:  :py:class:`Padt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.Padt>`
                    
                    .. attribute:: session_state
                    
                    	Session Stage counts
                    	**type**\:  :py:class:`SessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.SessionState>`
                    
                    .. attribute:: other
                    
                    	Other counts
                    	**type**\:  :py:class:`Other <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.Other>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.Nodes.Node.Statistics.PacketCounts, self).__init__()

                        self.yang_name = "packet-counts"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("padi", ("padi", Pppoe.Nodes.Node.Statistics.PacketCounts.Padi)), ("pado", ("pado", Pppoe.Nodes.Node.Statistics.PacketCounts.Pado)), ("padr", ("padr", Pppoe.Nodes.Node.Statistics.PacketCounts.Padr)), ("pads-success", ("pads_success", Pppoe.Nodes.Node.Statistics.PacketCounts.PadsSuccess)), ("pads-error", ("pads_error", Pppoe.Nodes.Node.Statistics.PacketCounts.PadsError)), ("padt", ("padt", Pppoe.Nodes.Node.Statistics.PacketCounts.Padt)), ("session-state", ("session_state", Pppoe.Nodes.Node.Statistics.PacketCounts.SessionState)), ("other", ("other", Pppoe.Nodes.Node.Statistics.PacketCounts.Other))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.padi = Pppoe.Nodes.Node.Statistics.PacketCounts.Padi()
                        self.padi.parent = self
                        self._children_name_map["padi"] = "padi"
                        self._children_yang_names.add("padi")

                        self.pado = Pppoe.Nodes.Node.Statistics.PacketCounts.Pado()
                        self.pado.parent = self
                        self._children_name_map["pado"] = "pado"
                        self._children_yang_names.add("pado")

                        self.padr = Pppoe.Nodes.Node.Statistics.PacketCounts.Padr()
                        self.padr.parent = self
                        self._children_name_map["padr"] = "padr"
                        self._children_yang_names.add("padr")

                        self.pads_success = Pppoe.Nodes.Node.Statistics.PacketCounts.PadsSuccess()
                        self.pads_success.parent = self
                        self._children_name_map["pads_success"] = "pads-success"
                        self._children_yang_names.add("pads-success")

                        self.pads_error = Pppoe.Nodes.Node.Statistics.PacketCounts.PadsError()
                        self.pads_error.parent = self
                        self._children_name_map["pads_error"] = "pads-error"
                        self._children_yang_names.add("pads-error")

                        self.padt = Pppoe.Nodes.Node.Statistics.PacketCounts.Padt()
                        self.padt.parent = self
                        self._children_name_map["padt"] = "padt"
                        self._children_yang_names.add("padt")

                        self.session_state = Pppoe.Nodes.Node.Statistics.PacketCounts.SessionState()
                        self.session_state.parent = self
                        self._children_name_map["session_state"] = "session-state"
                        self._children_yang_names.add("session-state")

                        self.other = Pppoe.Nodes.Node.Statistics.PacketCounts.Other()
                        self.other.parent = self
                        self._children_name_map["other"] = "other"
                        self._children_yang_names.add("other")
                        self._segment_path = lambda: "packet-counts"


                    class Padi(Entity):
                        """
                        PADI counts
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.Statistics.PacketCounts.Padi, self).__init__()

                            self.yang_name = "padi"
                            self.yang_parent_name = "packet-counts"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sent', YLeaf(YType.uint32, 'sent')),
                                ('received', YLeaf(YType.uint32, 'received')),
                                ('dropped', YLeaf(YType.uint32, 'dropped')),
                            ])
                            self.sent = None
                            self.received = None
                            self.dropped = None
                            self._segment_path = lambda: "padi"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketCounts.Padi, ['sent', 'received', 'dropped'], name, value)


                    class Pado(Entity):
                        """
                        PADO counts
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.Statistics.PacketCounts.Pado, self).__init__()

                            self.yang_name = "pado"
                            self.yang_parent_name = "packet-counts"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sent', YLeaf(YType.uint32, 'sent')),
                                ('received', YLeaf(YType.uint32, 'received')),
                                ('dropped', YLeaf(YType.uint32, 'dropped')),
                            ])
                            self.sent = None
                            self.received = None
                            self.dropped = None
                            self._segment_path = lambda: "pado"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketCounts.Pado, ['sent', 'received', 'dropped'], name, value)


                    class Padr(Entity):
                        """
                        PADR counts
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.Statistics.PacketCounts.Padr, self).__init__()

                            self.yang_name = "padr"
                            self.yang_parent_name = "packet-counts"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sent', YLeaf(YType.uint32, 'sent')),
                                ('received', YLeaf(YType.uint32, 'received')),
                                ('dropped', YLeaf(YType.uint32, 'dropped')),
                            ])
                            self.sent = None
                            self.received = None
                            self.dropped = None
                            self._segment_path = lambda: "padr"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketCounts.Padr, ['sent', 'received', 'dropped'], name, value)


                    class PadsSuccess(Entity):
                        """
                        PADS Success counts
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.Statistics.PacketCounts.PadsSuccess, self).__init__()

                            self.yang_name = "pads-success"
                            self.yang_parent_name = "packet-counts"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sent', YLeaf(YType.uint32, 'sent')),
                                ('received', YLeaf(YType.uint32, 'received')),
                                ('dropped', YLeaf(YType.uint32, 'dropped')),
                            ])
                            self.sent = None
                            self.received = None
                            self.dropped = None
                            self._segment_path = lambda: "pads-success"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketCounts.PadsSuccess, ['sent', 'received', 'dropped'], name, value)


                    class PadsError(Entity):
                        """
                        PADS Error counts
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.Statistics.PacketCounts.PadsError, self).__init__()

                            self.yang_name = "pads-error"
                            self.yang_parent_name = "packet-counts"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sent', YLeaf(YType.uint32, 'sent')),
                                ('received', YLeaf(YType.uint32, 'received')),
                                ('dropped', YLeaf(YType.uint32, 'dropped')),
                            ])
                            self.sent = None
                            self.received = None
                            self.dropped = None
                            self._segment_path = lambda: "pads-error"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketCounts.PadsError, ['sent', 'received', 'dropped'], name, value)


                    class Padt(Entity):
                        """
                        PADT counts
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.Statistics.PacketCounts.Padt, self).__init__()

                            self.yang_name = "padt"
                            self.yang_parent_name = "packet-counts"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sent', YLeaf(YType.uint32, 'sent')),
                                ('received', YLeaf(YType.uint32, 'received')),
                                ('dropped', YLeaf(YType.uint32, 'dropped')),
                            ])
                            self.sent = None
                            self.received = None
                            self.dropped = None
                            self._segment_path = lambda: "padt"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketCounts.Padt, ['sent', 'received', 'dropped'], name, value)


                    class SessionState(Entity):
                        """
                        Session Stage counts
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.Statistics.PacketCounts.SessionState, self).__init__()

                            self.yang_name = "session-state"
                            self.yang_parent_name = "packet-counts"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sent', YLeaf(YType.uint32, 'sent')),
                                ('received', YLeaf(YType.uint32, 'received')),
                                ('dropped', YLeaf(YType.uint32, 'dropped')),
                            ])
                            self.sent = None
                            self.received = None
                            self.dropped = None
                            self._segment_path = lambda: "session-state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketCounts.SessionState, ['sent', 'received', 'dropped'], name, value)


                    class Other(Entity):
                        """
                        Other counts
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.Statistics.PacketCounts.Other, self).__init__()

                            self.yang_name = "other"
                            self.yang_parent_name = "packet-counts"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sent', YLeaf(YType.uint32, 'sent')),
                                ('received', YLeaf(YType.uint32, 'received')),
                                ('dropped', YLeaf(YType.uint32, 'dropped')),
                            ])
                            self.sent = None
                            self.received = None
                            self.dropped = None
                            self._segment_path = lambda: "other"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketCounts.Other, ['sent', 'received', 'dropped'], name, value)


                class PacketErrorCounts(Entity):
                    """
                    Packet Error Counts
                    
                    .. attribute:: no_interface_handle
                    
                    	No interface handle
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_packet_payload
                    
                    	No packet payload
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_packet_mac_address
                    
                    	No packet mac\-address
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_version_type_value
                    
                    	Invalid version\-type value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bad_packet_length
                    
                    	Bad packet length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_interface
                    
                    	Unknown interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pado_received
                    
                    	PADO received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pads_received
                    
                    	PADS received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_packet_type_received
                    
                    	Unknown packet type received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unexpected_session_id_in_packet
                    
                    	Unexpected Session\-ID in packet
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_service_name_tag
                    
                    	No Service\-Name Tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: padt_for_unknown_session
                    
                    	PADT for unknown session
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: padt_with_wrong_peer_mac
                    
                    	PADT with wrong peer\-mac
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: padt_with_wrong_vlan_tags
                    
                    	PADT with wrong VLAN tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: zero_length_host_uniq
                    
                    	Zero\-length Host\-Uniq tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: padt_before_pads_sent
                    
                    	PADT before PADS sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_stage_packet_for_unknown_session
                    
                    	Session\-stage packet for unknown session
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_stage_packet_with_wrong_mac
                    
                    	Session\-stage packet with wrong mac
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_stage_packet_with_wrong_vlan_tags
                    
                    	Session\-stage packet with wrong VLAN tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_stage_packet_with_no_error
                    
                    	Session\-stage packet with no error
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tag_too_short
                    
                    	Tag too short
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bad_tag_length_field
                    
                    	Bad tag\-length field
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_service_name_tags
                    
                    	Multiple Service\-Name tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_max_payload_tags
                    
                    	Multiple Max\-Payload tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_max_payload_tag
                    
                    	Invalid Max\-Payload tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_vendor_specific_tags
                    
                    	Multiple Vendor\-specific tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unexpected_ac_name_tag
                    
                    	Unexpected AC\-Name tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unexpected_error_tags
                    
                    	Unexpected error tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_tag_received
                    
                    	Unknown tag received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_iana_code_invendor_tag
                    
                    	No IANA code in vendor tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_iana_code_invendor_tag
                    
                    	Invalid IANA code in vendor tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vendor_tag_too_short
                    
                    	Vendor tag too short
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bad_vendor_tag_length_field
                    
                    	Bad vendor tag length field
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_host_uniq_tags
                    
                    	Multiple Host\-Uniq tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_relay_session_id_tags
                    
                    	Multiple relay\-session\-id tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_circuit_id_tags
                    
                    	Multiple Circuit\-ID tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_remote_id_tags
                    
                    	Multiple Remote\-ID tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_dsl_tag
                    
                    	Invalid DSL tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_of_the_same_dsl_tag
                    
                    	Multiple of the same DSL tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_iwf_tag
                    
                    	Invalid IWF tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_iwf_tags
                    
                    	Multiple IWF tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknownvendor_tag
                    
                    	Unknown vendor\-tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_space_left_in_packet
                    
                    	No space left in packet
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: duplicate_host_uniq_tag_received
                    
                    	Duplicate Host\-Uniq tag received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: duplicate_relay_session_id_tag_received
                    
                    	Duplicate Relay Session ID tag received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: packet_too_long
                    
                    	Packet too long
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_ale_tag
                    
                    	Invalid ALE tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_ale_tags
                    
                    	Multiple ALE tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_service_name
                    
                    	Invalid Service Name
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_peer_mac
                    
                    	Invalid Peer MAC
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_vlan_tags
                    
                    	Invalid VLAN Tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: packet_on_srg_slave
                    
                    	Packet Received on SRG Slave
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.Nodes.Node.Statistics.PacketErrorCounts, self).__init__()

                        self.yang_name = "packet-error-counts"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('no_interface_handle', YLeaf(YType.uint32, 'no-interface-handle')),
                            ('no_packet_payload', YLeaf(YType.uint32, 'no-packet-payload')),
                            ('no_packet_mac_address', YLeaf(YType.uint32, 'no-packet-mac-address')),
                            ('invalid_version_type_value', YLeaf(YType.uint32, 'invalid-version-type-value')),
                            ('bad_packet_length', YLeaf(YType.uint32, 'bad-packet-length')),
                            ('unknown_interface', YLeaf(YType.uint32, 'unknown-interface')),
                            ('pado_received', YLeaf(YType.uint32, 'pado-received')),
                            ('pads_received', YLeaf(YType.uint32, 'pads-received')),
                            ('unknown_packet_type_received', YLeaf(YType.uint32, 'unknown-packet-type-received')),
                            ('unexpected_session_id_in_packet', YLeaf(YType.uint32, 'unexpected-session-id-in-packet')),
                            ('no_service_name_tag', YLeaf(YType.uint32, 'no-service-name-tag')),
                            ('padt_for_unknown_session', YLeaf(YType.uint32, 'padt-for-unknown-session')),
                            ('padt_with_wrong_peer_mac', YLeaf(YType.uint32, 'padt-with-wrong-peer-mac')),
                            ('padt_with_wrong_vlan_tags', YLeaf(YType.uint32, 'padt-with-wrong-vlan-tags')),
                            ('zero_length_host_uniq', YLeaf(YType.uint32, 'zero-length-host-uniq')),
                            ('padt_before_pads_sent', YLeaf(YType.uint32, 'padt-before-pads-sent')),
                            ('session_stage_packet_for_unknown_session', YLeaf(YType.uint32, 'session-stage-packet-for-unknown-session')),
                            ('session_stage_packet_with_wrong_mac', YLeaf(YType.uint32, 'session-stage-packet-with-wrong-mac')),
                            ('session_stage_packet_with_wrong_vlan_tags', YLeaf(YType.uint32, 'session-stage-packet-with-wrong-vlan-tags')),
                            ('session_stage_packet_with_no_error', YLeaf(YType.uint32, 'session-stage-packet-with-no-error')),
                            ('tag_too_short', YLeaf(YType.uint32, 'tag-too-short')),
                            ('bad_tag_length_field', YLeaf(YType.uint32, 'bad-tag-length-field')),
                            ('multiple_service_name_tags', YLeaf(YType.uint32, 'multiple-service-name-tags')),
                            ('multiple_max_payload_tags', YLeaf(YType.uint32, 'multiple-max-payload-tags')),
                            ('invalid_max_payload_tag', YLeaf(YType.uint32, 'invalid-max-payload-tag')),
                            ('multiple_vendor_specific_tags', YLeaf(YType.uint32, 'multiple-vendor-specific-tags')),
                            ('unexpected_ac_name_tag', YLeaf(YType.uint32, 'unexpected-ac-name-tag')),
                            ('unexpected_error_tags', YLeaf(YType.uint32, 'unexpected-error-tags')),
                            ('unknown_tag_received', YLeaf(YType.uint32, 'unknown-tag-received')),
                            ('no_iana_code_invendor_tag', YLeaf(YType.uint32, 'no-iana-code-invendor-tag')),
                            ('invalid_iana_code_invendor_tag', YLeaf(YType.uint32, 'invalid-iana-code-invendor-tag')),
                            ('vendor_tag_too_short', YLeaf(YType.uint32, 'vendor-tag-too-short')),
                            ('bad_vendor_tag_length_field', YLeaf(YType.uint32, 'bad-vendor-tag-length-field')),
                            ('multiple_host_uniq_tags', YLeaf(YType.uint32, 'multiple-host-uniq-tags')),
                            ('multiple_relay_session_id_tags', YLeaf(YType.uint32, 'multiple-relay-session-id-tags')),
                            ('multiple_circuit_id_tags', YLeaf(YType.uint32, 'multiple-circuit-id-tags')),
                            ('multiple_remote_id_tags', YLeaf(YType.uint32, 'multiple-remote-id-tags')),
                            ('invalid_dsl_tag', YLeaf(YType.uint32, 'invalid-dsl-tag')),
                            ('multiple_of_the_same_dsl_tag', YLeaf(YType.uint32, 'multiple-of-the-same-dsl-tag')),
                            ('invalid_iwf_tag', YLeaf(YType.uint32, 'invalid-iwf-tag')),
                            ('multiple_iwf_tags', YLeaf(YType.uint32, 'multiple-iwf-tags')),
                            ('unknownvendor_tag', YLeaf(YType.uint32, 'unknownvendor-tag')),
                            ('no_space_left_in_packet', YLeaf(YType.uint32, 'no-space-left-in-packet')),
                            ('duplicate_host_uniq_tag_received', YLeaf(YType.uint32, 'duplicate-host-uniq-tag-received')),
                            ('duplicate_relay_session_id_tag_received', YLeaf(YType.uint32, 'duplicate-relay-session-id-tag-received')),
                            ('packet_too_long', YLeaf(YType.uint32, 'packet-too-long')),
                            ('invalid_ale_tag', YLeaf(YType.uint32, 'invalid-ale-tag')),
                            ('multiple_ale_tags', YLeaf(YType.uint32, 'multiple-ale-tags')),
                            ('invalid_service_name', YLeaf(YType.uint32, 'invalid-service-name')),
                            ('invalid_peer_mac', YLeaf(YType.uint32, 'invalid-peer-mac')),
                            ('invalid_vlan_tags', YLeaf(YType.uint32, 'invalid-vlan-tags')),
                            ('packet_on_srg_slave', YLeaf(YType.uint32, 'packet-on-srg-slave')),
                        ])
                        self.no_interface_handle = None
                        self.no_packet_payload = None
                        self.no_packet_mac_address = None
                        self.invalid_version_type_value = None
                        self.bad_packet_length = None
                        self.unknown_interface = None
                        self.pado_received = None
                        self.pads_received = None
                        self.unknown_packet_type_received = None
                        self.unexpected_session_id_in_packet = None
                        self.no_service_name_tag = None
                        self.padt_for_unknown_session = None
                        self.padt_with_wrong_peer_mac = None
                        self.padt_with_wrong_vlan_tags = None
                        self.zero_length_host_uniq = None
                        self.padt_before_pads_sent = None
                        self.session_stage_packet_for_unknown_session = None
                        self.session_stage_packet_with_wrong_mac = None
                        self.session_stage_packet_with_wrong_vlan_tags = None
                        self.session_stage_packet_with_no_error = None
                        self.tag_too_short = None
                        self.bad_tag_length_field = None
                        self.multiple_service_name_tags = None
                        self.multiple_max_payload_tags = None
                        self.invalid_max_payload_tag = None
                        self.multiple_vendor_specific_tags = None
                        self.unexpected_ac_name_tag = None
                        self.unexpected_error_tags = None
                        self.unknown_tag_received = None
                        self.no_iana_code_invendor_tag = None
                        self.invalid_iana_code_invendor_tag = None
                        self.vendor_tag_too_short = None
                        self.bad_vendor_tag_length_field = None
                        self.multiple_host_uniq_tags = None
                        self.multiple_relay_session_id_tags = None
                        self.multiple_circuit_id_tags = None
                        self.multiple_remote_id_tags = None
                        self.invalid_dsl_tag = None
                        self.multiple_of_the_same_dsl_tag = None
                        self.invalid_iwf_tag = None
                        self.multiple_iwf_tags = None
                        self.unknownvendor_tag = None
                        self.no_space_left_in_packet = None
                        self.duplicate_host_uniq_tag_received = None
                        self.duplicate_relay_session_id_tag_received = None
                        self.packet_too_long = None
                        self.invalid_ale_tag = None
                        self.multiple_ale_tags = None
                        self.invalid_service_name = None
                        self.invalid_peer_mac = None
                        self.invalid_vlan_tags = None
                        self.packet_on_srg_slave = None
                        self._segment_path = lambda: "packet-error-counts"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketErrorCounts, ['no_interface_handle', 'no_packet_payload', 'no_packet_mac_address', 'invalid_version_type_value', 'bad_packet_length', 'unknown_interface', 'pado_received', 'pads_received', 'unknown_packet_type_received', 'unexpected_session_id_in_packet', 'no_service_name_tag', 'padt_for_unknown_session', 'padt_with_wrong_peer_mac', 'padt_with_wrong_vlan_tags', 'zero_length_host_uniq', 'padt_before_pads_sent', 'session_stage_packet_for_unknown_session', 'session_stage_packet_with_wrong_mac', 'session_stage_packet_with_wrong_vlan_tags', 'session_stage_packet_with_no_error', 'tag_too_short', 'bad_tag_length_field', 'multiple_service_name_tags', 'multiple_max_payload_tags', 'invalid_max_payload_tag', 'multiple_vendor_specific_tags', 'unexpected_ac_name_tag', 'unexpected_error_tags', 'unknown_tag_received', 'no_iana_code_invendor_tag', 'invalid_iana_code_invendor_tag', 'vendor_tag_too_short', 'bad_vendor_tag_length_field', 'multiple_host_uniq_tags', 'multiple_relay_session_id_tags', 'multiple_circuit_id_tags', 'multiple_remote_id_tags', 'invalid_dsl_tag', 'multiple_of_the_same_dsl_tag', 'invalid_iwf_tag', 'multiple_iwf_tags', 'unknownvendor_tag', 'no_space_left_in_packet', 'duplicate_host_uniq_tag_received', 'duplicate_relay_session_id_tag_received', 'packet_too_long', 'invalid_ale_tag', 'multiple_ale_tags', 'invalid_service_name', 'invalid_peer_mac', 'invalid_vlan_tags', 'packet_on_srg_slave'], name, value)


            class AccessInterface(Entity):
                """
                PPPoE access interface information
                
                .. attribute:: summaries
                
                	PPPoE access interface summary information
                	**type**\:  :py:class:`Summaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.AccessInterface.Summaries>`
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Pppoe.Nodes.Node.AccessInterface, self).__init__()

                    self.yang_name = "access-interface"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("summaries", ("summaries", Pppoe.Nodes.Node.AccessInterface.Summaries))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.summaries = Pppoe.Nodes.Node.AccessInterface.Summaries()
                    self.summaries.parent = self
                    self._children_name_map["summaries"] = "summaries"
                    self._children_yang_names.add("summaries")
                    self._segment_path = lambda: "access-interface"


                class Summaries(Entity):
                    """
                    PPPoE access interface summary information
                    
                    .. attribute:: summary
                    
                    	Summary information for a PPPoE\-enabled access interface
                    	**type**\: list of  		 :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.AccessInterface.Summaries.Summary>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.Nodes.Node.AccessInterface.Summaries, self).__init__()

                        self.yang_name = "summaries"
                        self.yang_parent_name = "access-interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("summary", ("summary", Pppoe.Nodes.Node.AccessInterface.Summaries.Summary))])
                        self._leafs = OrderedDict()

                        self.summary = YList(self)
                        self._segment_path = lambda: "summaries"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.Nodes.Node.AccessInterface.Summaries, [], name, value)


                    class Summary(Entity):
                        """
                        Summary information for a PPPoE\-enabled
                        access interface
                        
                        .. attribute:: interface_name  (key)
                        
                        	PPPoE Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: interface_name_xr
                        
                        	Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: interface_state
                        
                        	Interface State
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mac_address
                        
                        	Mac Address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: bba_group_name
                        
                        	BBA Group
                        	**type**\: str
                        
                        .. attribute:: is_ready
                        
                        	Is Ready
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: sessions
                        
                        	Session Count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incomplete_sessions
                        
                        	Incomplete Session Count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.AccessInterface.Summaries.Summary, self).__init__()

                            self.yang_name = "summary"
                            self.yang_parent_name = "summaries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['interface_name']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', YLeaf(YType.str, 'interface-name')),
                                ('interface_name_xr', YLeaf(YType.str, 'interface-name-xr')),
                                ('interface_state', YLeaf(YType.uint32, 'interface-state')),
                                ('mac_address', YLeaf(YType.str, 'mac-address')),
                                ('bba_group_name', YLeaf(YType.str, 'bba-group-name')),
                                ('is_ready', YLeaf(YType.int32, 'is-ready')),
                                ('sessions', YLeaf(YType.uint32, 'sessions')),
                                ('incomplete_sessions', YLeaf(YType.uint32, 'incomplete-sessions')),
                            ])
                            self.interface_name = None
                            self.interface_name_xr = None
                            self.interface_state = None
                            self.mac_address = None
                            self.bba_group_name = None
                            self.is_ready = None
                            self.sessions = None
                            self.incomplete_sessions = None
                            self._segment_path = lambda: "summary" + "[interface-name='" + str(self.interface_name) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.AccessInterface.Summaries.Summary, ['interface_name', 'interface_name_xr', 'interface_state', 'mac_address', 'bba_group_name', 'is_ready', 'sessions', 'incomplete_sessions'], name, value)


            class Interfaces(Entity):
                """
                Per interface PPPoE operational data
                
                .. attribute:: interface
                
                	Data for a PPPoE interface
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Pppoe.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("interface", ("interface", Pppoe.Nodes.Node.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(Pppoe.Nodes.Node.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    Data for a PPPoE interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	PPPoE Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: tags
                    
                    	Tags
                    	**type**\:  :py:class:`Tags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Interfaces.Interface.Tags>`
                    
                    .. attribute:: interface_name_xr
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: access_interface_name
                    
                    	Access Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: bba_group_name
                    
                    	BBA Group
                    	**type**\: str
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: local_mac_address
                    
                    	Local Mac\-Address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: peer_mac_address
                    
                    	Peer Mac\-Address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: is_complete
                    
                    	Is Complete
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: vlan_outer_id
                    
                    	VLAN Outer ID
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: vlan_inner_id
                    
                    	VLAN Inner ID
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: srg_state
                    
                    	SRG state
                    	**type**\:  :py:class:`PppoeMaSessionIdbSrgState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.PppoeMaSessionIdbSrgState>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_container_classes = OrderedDict([("tags", ("tags", Pppoe.Nodes.Node.Interfaces.Interface.Tags))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', YLeaf(YType.str, 'interface-name')),
                            ('interface_name_xr', YLeaf(YType.str, 'interface-name-xr')),
                            ('access_interface_name', YLeaf(YType.str, 'access-interface-name')),
                            ('bba_group_name', YLeaf(YType.str, 'bba-group-name')),
                            ('session_id', YLeaf(YType.uint16, 'session-id')),
                            ('local_mac_address', YLeaf(YType.str, 'local-mac-address')),
                            ('peer_mac_address', YLeaf(YType.str, 'peer-mac-address')),
                            ('is_complete', YLeaf(YType.int32, 'is-complete')),
                            ('vlan_outer_id', YLeaf(YType.uint16, 'vlan-outer-id')),
                            ('vlan_inner_id', YLeaf(YType.uint16, 'vlan-inner-id')),
                            ('srg_state', YLeaf(YType.enumeration, 'srg-state')),
                        ])
                        self.interface_name = None
                        self.interface_name_xr = None
                        self.access_interface_name = None
                        self.bba_group_name = None
                        self.session_id = None
                        self.local_mac_address = None
                        self.peer_mac_address = None
                        self.is_complete = None
                        self.vlan_outer_id = None
                        self.vlan_inner_id = None
                        self.srg_state = None

                        self.tags = Pppoe.Nodes.Node.Interfaces.Interface.Tags()
                        self.tags.parent = self
                        self._children_name_map["tags"] = "tags"
                        self._children_yang_names.add("tags")
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.Nodes.Node.Interfaces.Interface, ['interface_name', 'interface_name_xr', 'access_interface_name', 'bba_group_name', 'session_id', 'local_mac_address', 'peer_mac_address', 'is_complete', 'vlan_outer_id', 'vlan_inner_id', 'srg_state'], name, value)


                    class Tags(Entity):
                        """
                        Tags
                        
                        .. attribute:: access_loop_encapsulation
                        
                        	Access Loop Encapsulation
                        	**type**\:  :py:class:`AccessLoopEncapsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Interfaces.Interface.Tags.AccessLoopEncapsulation>`
                        
                        .. attribute:: service_name
                        
                        	Service Name
                        	**type**\: str
                        
                        .. attribute:: max_payload
                        
                        	Max Payload
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: host_uniq
                        
                        	Host Uniq
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: relay_session_id
                        
                        	Relay Session ID
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: remote_id
                        
                        	Remote ID
                        	**type**\: str
                        
                        .. attribute:: circuit_id
                        
                        	Circuit ID
                        	**type**\: str
                        
                        .. attribute:: is_iwf
                        
                        	Is IWF
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: dsl_actual_up
                        
                        	DSL Actual Up
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_actual_down
                        
                        	DSL Actual Down
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_min_up
                        
                        	DSL Min Up
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_min_down
                        
                        	DSL Min Down
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_attain_up
                        
                        	DSL Attain Up
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_attain_down
                        
                        	DSL Attain Down
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_max_up
                        
                        	DSL Max Up
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_max_down
                        
                        	DSL Max Down
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_min_up_low
                        
                        	DSL Min Up Low
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_min_down_low
                        
                        	DSL Min Down Low
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_max_delay_up
                        
                        	DSL Max Delay Up
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_actual_delay_up
                        
                        	DSL Actual Delay Up
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_max_delay_down
                        
                        	DSL Max Delay Down
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_actual_delay_down
                        
                        	DSL Actual Delay Down
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.Interfaces.Interface.Tags, self).__init__()

                            self.yang_name = "tags"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("access-loop-encapsulation", ("access_loop_encapsulation", Pppoe.Nodes.Node.Interfaces.Interface.Tags.AccessLoopEncapsulation))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('service_name', YLeaf(YType.str, 'service-name')),
                                ('max_payload', YLeaf(YType.uint16, 'max-payload')),
                                ('host_uniq', YLeaf(YType.str, 'host-uniq')),
                                ('relay_session_id', YLeaf(YType.str, 'relay-session-id')),
                                ('remote_id', YLeaf(YType.str, 'remote-id')),
                                ('circuit_id', YLeaf(YType.str, 'circuit-id')),
                                ('is_iwf', YLeaf(YType.int32, 'is-iwf')),
                                ('dsl_actual_up', YLeaf(YType.uint32, 'dsl-actual-up')),
                                ('dsl_actual_down', YLeaf(YType.uint32, 'dsl-actual-down')),
                                ('dsl_min_up', YLeaf(YType.uint32, 'dsl-min-up')),
                                ('dsl_min_down', YLeaf(YType.uint32, 'dsl-min-down')),
                                ('dsl_attain_up', YLeaf(YType.uint32, 'dsl-attain-up')),
                                ('dsl_attain_down', YLeaf(YType.uint32, 'dsl-attain-down')),
                                ('dsl_max_up', YLeaf(YType.uint32, 'dsl-max-up')),
                                ('dsl_max_down', YLeaf(YType.uint32, 'dsl-max-down')),
                                ('dsl_min_up_low', YLeaf(YType.uint32, 'dsl-min-up-low')),
                                ('dsl_min_down_low', YLeaf(YType.uint32, 'dsl-min-down-low')),
                                ('dsl_max_delay_up', YLeaf(YType.uint32, 'dsl-max-delay-up')),
                                ('dsl_actual_delay_up', YLeaf(YType.uint32, 'dsl-actual-delay-up')),
                                ('dsl_max_delay_down', YLeaf(YType.uint32, 'dsl-max-delay-down')),
                                ('dsl_actual_delay_down', YLeaf(YType.uint32, 'dsl-actual-delay-down')),
                            ])
                            self.service_name = None
                            self.max_payload = None
                            self.host_uniq = None
                            self.relay_session_id = None
                            self.remote_id = None
                            self.circuit_id = None
                            self.is_iwf = None
                            self.dsl_actual_up = None
                            self.dsl_actual_down = None
                            self.dsl_min_up = None
                            self.dsl_min_down = None
                            self.dsl_attain_up = None
                            self.dsl_attain_down = None
                            self.dsl_max_up = None
                            self.dsl_max_down = None
                            self.dsl_min_up_low = None
                            self.dsl_min_down_low = None
                            self.dsl_max_delay_up = None
                            self.dsl_actual_delay_up = None
                            self.dsl_max_delay_down = None
                            self.dsl_actual_delay_down = None

                            self.access_loop_encapsulation = Pppoe.Nodes.Node.Interfaces.Interface.Tags.AccessLoopEncapsulation()
                            self.access_loop_encapsulation.parent = self
                            self._children_name_map["access_loop_encapsulation"] = "access-loop-encapsulation"
                            self._children_yang_names.add("access-loop-encapsulation")
                            self._segment_path = lambda: "tags"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.Interfaces.Interface.Tags, ['service_name', 'max_payload', 'host_uniq', 'relay_session_id', 'remote_id', 'circuit_id', 'is_iwf', 'dsl_actual_up', 'dsl_actual_down', 'dsl_min_up', 'dsl_min_down', 'dsl_attain_up', 'dsl_attain_down', 'dsl_max_up', 'dsl_max_down', 'dsl_min_up_low', 'dsl_min_down_low', 'dsl_max_delay_up', 'dsl_actual_delay_up', 'dsl_max_delay_down', 'dsl_actual_delay_down'], name, value)


                        class AccessLoopEncapsulation(Entity):
                            """
                            Access Loop Encapsulation
                            
                            .. attribute:: data_link
                            
                            	Data Link
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: encaps1
                            
                            	Encaps 1
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: encaps2
                            
                            	Encaps 2
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.Interfaces.Interface.Tags.AccessLoopEncapsulation, self).__init__()

                                self.yang_name = "access-loop-encapsulation"
                                self.yang_parent_name = "tags"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('data_link', YLeaf(YType.uint8, 'data-link')),
                                    ('encaps1', YLeaf(YType.uint8, 'encaps1')),
                                    ('encaps2', YLeaf(YType.uint8, 'encaps2')),
                                ])
                                self.data_link = None
                                self.encaps1 = None
                                self.encaps2 = None
                                self._segment_path = lambda: "access-loop-encapsulation"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.Interfaces.Interface.Tags.AccessLoopEncapsulation, ['data_link', 'encaps1', 'encaps2'], name, value)


            class BbaGroups(Entity):
                """
                PPPoE BBA\-Group information
                
                .. attribute:: bba_group
                
                	PPPoE BBA\-Group information
                	**type**\: list of  		 :py:class:`BbaGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup>`
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Pppoe.Nodes.Node.BbaGroups, self).__init__()

                    self.yang_name = "bba-groups"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("bba-group", ("bba_group", Pppoe.Nodes.Node.BbaGroups.BbaGroup))])
                    self._leafs = OrderedDict()

                    self.bba_group = YList(self)
                    self._segment_path = lambda: "bba-groups"

                def __setattr__(self, name, value):
                    self._perform_setattr(Pppoe.Nodes.Node.BbaGroups, [], name, value)


                class BbaGroup(Entity):
                    """
                    PPPoE BBA\-Group information
                    
                    .. attribute:: bba_group_name  (key)
                    
                    	BBA Group
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: limit_config
                    
                    	BBA\-Group limit configuration information
                    	**type**\:  :py:class:`LimitConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig>`
                    
                    .. attribute:: limits
                    
                    	PPPoE session limit information
                    	**type**\:  :py:class:`Limits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits>`
                    
                    .. attribute:: throttles
                    
                    	PPPoE throttle information
                    	**type**\:  :py:class:`Throttles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles>`
                    
                    .. attribute:: throttle_config
                    
                    	BBA\-Group throttle configuration information
                    	**type**\:  :py:class:`ThrottleConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup, self).__init__()

                        self.yang_name = "bba-group"
                        self.yang_parent_name = "bba-groups"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['bba_group_name']
                        self._child_container_classes = OrderedDict([("limit-config", ("limit_config", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig)), ("limits", ("limits", Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits)), ("throttles", ("throttles", Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles)), ("throttle-config", ("throttle_config", Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('bba_group_name', YLeaf(YType.str, 'bba-group-name')),
                        ])
                        self.bba_group_name = None

                        self.limit_config = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig()
                        self.limit_config.parent = self
                        self._children_name_map["limit_config"] = "limit-config"
                        self._children_yang_names.add("limit-config")

                        self.limits = Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits()
                        self.limits.parent = self
                        self._children_name_map["limits"] = "limits"
                        self._children_yang_names.add("limits")

                        self.throttles = Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles()
                        self.throttles.parent = self
                        self._children_name_map["throttles"] = "throttles"
                        self._children_yang_names.add("throttles")

                        self.throttle_config = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig()
                        self.throttle_config.parent = self
                        self._children_name_map["throttle_config"] = "throttle-config"
                        self._children_yang_names.add("throttle-config")
                        self._segment_path = lambda: "bba-group" + "[bba-group-name='" + str(self.bba_group_name) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup, ['bba_group_name'], name, value)


                    class LimitConfig(Entity):
                        """
                        BBA\-Group limit configuration information
                        
                        .. attribute:: card
                        
                        	Card
                        	**type**\:  :py:class:`Card <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Card>`
                        
                        .. attribute:: access_intf
                        
                        	Access Interface
                        	**type**\:  :py:class:`AccessIntf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.AccessIntf>`
                        
                        .. attribute:: mac
                        
                        	MAC
                        	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Mac>`
                        
                        .. attribute:: mac_iwf
                        
                        	MAC IWF
                        	**type**\:  :py:class:`MacIwf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwf>`
                        
                        .. attribute:: mac_access_interface
                        
                        	MAC Access Interface
                        	**type**\:  :py:class:`MacAccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacAccessInterface>`
                        
                        .. attribute:: mac_iwf_access_interface
                        
                        	MAC IWF Access Interface
                        	**type**\:  :py:class:`MacIwfAccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwfAccessInterface>`
                        
                        .. attribute:: circuit_id
                        
                        	Circuit ID
                        	**type**\:  :py:class:`CircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitId>`
                        
                        .. attribute:: remote_id
                        
                        	Remote ID
                        	**type**\:  :py:class:`RemoteId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.RemoteId>`
                        
                        .. attribute:: circuit_id_and_remote_id
                        
                        	Circuit ID and Remote ID
                        	**type**\:  :py:class:`CircuitIdAndRemoteId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitIdAndRemoteId>`
                        
                        .. attribute:: outer_vlan_id
                        
                        	Outer VLAN ID
                        	**type**\:  :py:class:`OuterVlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.OuterVlanId>`
                        
                        .. attribute:: inner_vlan_id
                        
                        	Inner VLAN ID
                        	**type**\:  :py:class:`InnerVlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.InnerVlanId>`
                        
                        .. attribute:: vlan_id
                        
                        	VLAN ID
                        	**type**\:  :py:class:`VlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.VlanId>`
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig, self).__init__()

                            self.yang_name = "limit-config"
                            self.yang_parent_name = "bba-group"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("card", ("card", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Card)), ("access-intf", ("access_intf", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.AccessIntf)), ("mac", ("mac", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Mac)), ("mac-iwf", ("mac_iwf", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwf)), ("mac-access-interface", ("mac_access_interface", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacAccessInterface)), ("mac-iwf-access-interface", ("mac_iwf_access_interface", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwfAccessInterface)), ("circuit-id", ("circuit_id", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitId)), ("remote-id", ("remote_id", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.RemoteId)), ("circuit-id-and-remote-id", ("circuit_id_and_remote_id", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitIdAndRemoteId)), ("outer-vlan-id", ("outer_vlan_id", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.OuterVlanId)), ("inner-vlan-id", ("inner_vlan_id", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.InnerVlanId)), ("vlan-id", ("vlan_id", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.VlanId))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.card = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Card()
                            self.card.parent = self
                            self._children_name_map["card"] = "card"
                            self._children_yang_names.add("card")

                            self.access_intf = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.AccessIntf()
                            self.access_intf.parent = self
                            self._children_name_map["access_intf"] = "access-intf"
                            self._children_yang_names.add("access-intf")

                            self.mac = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Mac()
                            self.mac.parent = self
                            self._children_name_map["mac"] = "mac"
                            self._children_yang_names.add("mac")

                            self.mac_iwf = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwf()
                            self.mac_iwf.parent = self
                            self._children_name_map["mac_iwf"] = "mac-iwf"
                            self._children_yang_names.add("mac-iwf")

                            self.mac_access_interface = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacAccessInterface()
                            self.mac_access_interface.parent = self
                            self._children_name_map["mac_access_interface"] = "mac-access-interface"
                            self._children_yang_names.add("mac-access-interface")

                            self.mac_iwf_access_interface = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwfAccessInterface()
                            self.mac_iwf_access_interface.parent = self
                            self._children_name_map["mac_iwf_access_interface"] = "mac-iwf-access-interface"
                            self._children_yang_names.add("mac-iwf-access-interface")

                            self.circuit_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitId()
                            self.circuit_id.parent = self
                            self._children_name_map["circuit_id"] = "circuit-id"
                            self._children_yang_names.add("circuit-id")

                            self.remote_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.RemoteId()
                            self.remote_id.parent = self
                            self._children_name_map["remote_id"] = "remote-id"
                            self._children_yang_names.add("remote-id")

                            self.circuit_id_and_remote_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitIdAndRemoteId()
                            self.circuit_id_and_remote_id.parent = self
                            self._children_name_map["circuit_id_and_remote_id"] = "circuit-id-and-remote-id"
                            self._children_yang_names.add("circuit-id-and-remote-id")

                            self.outer_vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.OuterVlanId()
                            self.outer_vlan_id.parent = self
                            self._children_name_map["outer_vlan_id"] = "outer-vlan-id"
                            self._children_yang_names.add("outer-vlan-id")

                            self.inner_vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.InnerVlanId()
                            self.inner_vlan_id.parent = self
                            self._children_name_map["inner_vlan_id"] = "inner-vlan-id"
                            self._children_yang_names.add("inner-vlan-id")

                            self.vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.VlanId()
                            self.vlan_id.parent = self
                            self._children_name_map["vlan_id"] = "vlan-id"
                            self._children_yang_names.add("vlan-id")
                            self._segment_path = lambda: "limit-config"


                        class Card(Entity):
                            """
                            Card
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Card, self).__init__()

                                self.yang_name = "card"
                                self.yang_parent_name = "limit-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_limit', YLeaf(YType.uint32, 'max-limit')),
                                    ('threshold', YLeaf(YType.uint32, 'threshold')),
                                    ('radius_override_enabled', YLeaf(YType.int32, 'radius-override-enabled')),
                                ])
                                self.max_limit = None
                                self.threshold = None
                                self.radius_override_enabled = None
                                self._segment_path = lambda: "card"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Card, ['max_limit', 'threshold', 'radius_override_enabled'], name, value)


                        class AccessIntf(Entity):
                            """
                            Access Interface
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.AccessIntf, self).__init__()

                                self.yang_name = "access-intf"
                                self.yang_parent_name = "limit-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_limit', YLeaf(YType.uint32, 'max-limit')),
                                    ('threshold', YLeaf(YType.uint32, 'threshold')),
                                    ('radius_override_enabled', YLeaf(YType.int32, 'radius-override-enabled')),
                                ])
                                self.max_limit = None
                                self.threshold = None
                                self.radius_override_enabled = None
                                self._segment_path = lambda: "access-intf"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.AccessIntf, ['max_limit', 'threshold', 'radius_override_enabled'], name, value)


                        class Mac(Entity):
                            """
                            MAC
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Mac, self).__init__()

                                self.yang_name = "mac"
                                self.yang_parent_name = "limit-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_limit', YLeaf(YType.uint32, 'max-limit')),
                                    ('threshold', YLeaf(YType.uint32, 'threshold')),
                                    ('radius_override_enabled', YLeaf(YType.int32, 'radius-override-enabled')),
                                ])
                                self.max_limit = None
                                self.threshold = None
                                self.radius_override_enabled = None
                                self._segment_path = lambda: "mac"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Mac, ['max_limit', 'threshold', 'radius_override_enabled'], name, value)


                        class MacIwf(Entity):
                            """
                            MAC IWF
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwf, self).__init__()

                                self.yang_name = "mac-iwf"
                                self.yang_parent_name = "limit-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_limit', YLeaf(YType.uint32, 'max-limit')),
                                    ('threshold', YLeaf(YType.uint32, 'threshold')),
                                    ('radius_override_enabled', YLeaf(YType.int32, 'radius-override-enabled')),
                                ])
                                self.max_limit = None
                                self.threshold = None
                                self.radius_override_enabled = None
                                self._segment_path = lambda: "mac-iwf"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwf, ['max_limit', 'threshold', 'radius_override_enabled'], name, value)


                        class MacAccessInterface(Entity):
                            """
                            MAC Access Interface
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacAccessInterface, self).__init__()

                                self.yang_name = "mac-access-interface"
                                self.yang_parent_name = "limit-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_limit', YLeaf(YType.uint32, 'max-limit')),
                                    ('threshold', YLeaf(YType.uint32, 'threshold')),
                                    ('radius_override_enabled', YLeaf(YType.int32, 'radius-override-enabled')),
                                ])
                                self.max_limit = None
                                self.threshold = None
                                self.radius_override_enabled = None
                                self._segment_path = lambda: "mac-access-interface"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacAccessInterface, ['max_limit', 'threshold', 'radius_override_enabled'], name, value)


                        class MacIwfAccessInterface(Entity):
                            """
                            MAC IWF Access Interface
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwfAccessInterface, self).__init__()

                                self.yang_name = "mac-iwf-access-interface"
                                self.yang_parent_name = "limit-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_limit', YLeaf(YType.uint32, 'max-limit')),
                                    ('threshold', YLeaf(YType.uint32, 'threshold')),
                                    ('radius_override_enabled', YLeaf(YType.int32, 'radius-override-enabled')),
                                ])
                                self.max_limit = None
                                self.threshold = None
                                self.radius_override_enabled = None
                                self._segment_path = lambda: "mac-iwf-access-interface"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwfAccessInterface, ['max_limit', 'threshold', 'radius_override_enabled'], name, value)


                        class CircuitId(Entity):
                            """
                            Circuit ID
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitId, self).__init__()

                                self.yang_name = "circuit-id"
                                self.yang_parent_name = "limit-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_limit', YLeaf(YType.uint32, 'max-limit')),
                                    ('threshold', YLeaf(YType.uint32, 'threshold')),
                                    ('radius_override_enabled', YLeaf(YType.int32, 'radius-override-enabled')),
                                ])
                                self.max_limit = None
                                self.threshold = None
                                self.radius_override_enabled = None
                                self._segment_path = lambda: "circuit-id"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitId, ['max_limit', 'threshold', 'radius_override_enabled'], name, value)


                        class RemoteId(Entity):
                            """
                            Remote ID
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.RemoteId, self).__init__()

                                self.yang_name = "remote-id"
                                self.yang_parent_name = "limit-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_limit', YLeaf(YType.uint32, 'max-limit')),
                                    ('threshold', YLeaf(YType.uint32, 'threshold')),
                                    ('radius_override_enabled', YLeaf(YType.int32, 'radius-override-enabled')),
                                ])
                                self.max_limit = None
                                self.threshold = None
                                self.radius_override_enabled = None
                                self._segment_path = lambda: "remote-id"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.RemoteId, ['max_limit', 'threshold', 'radius_override_enabled'], name, value)


                        class CircuitIdAndRemoteId(Entity):
                            """
                            Circuit ID and Remote ID
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitIdAndRemoteId, self).__init__()

                                self.yang_name = "circuit-id-and-remote-id"
                                self.yang_parent_name = "limit-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_limit', YLeaf(YType.uint32, 'max-limit')),
                                    ('threshold', YLeaf(YType.uint32, 'threshold')),
                                    ('radius_override_enabled', YLeaf(YType.int32, 'radius-override-enabled')),
                                ])
                                self.max_limit = None
                                self.threshold = None
                                self.radius_override_enabled = None
                                self._segment_path = lambda: "circuit-id-and-remote-id"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitIdAndRemoteId, ['max_limit', 'threshold', 'radius_override_enabled'], name, value)


                        class OuterVlanId(Entity):
                            """
                            Outer VLAN ID
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.OuterVlanId, self).__init__()

                                self.yang_name = "outer-vlan-id"
                                self.yang_parent_name = "limit-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_limit', YLeaf(YType.uint32, 'max-limit')),
                                    ('threshold', YLeaf(YType.uint32, 'threshold')),
                                    ('radius_override_enabled', YLeaf(YType.int32, 'radius-override-enabled')),
                                ])
                                self.max_limit = None
                                self.threshold = None
                                self.radius_override_enabled = None
                                self._segment_path = lambda: "outer-vlan-id"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.OuterVlanId, ['max_limit', 'threshold', 'radius_override_enabled'], name, value)


                        class InnerVlanId(Entity):
                            """
                            Inner VLAN ID
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.InnerVlanId, self).__init__()

                                self.yang_name = "inner-vlan-id"
                                self.yang_parent_name = "limit-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_limit', YLeaf(YType.uint32, 'max-limit')),
                                    ('threshold', YLeaf(YType.uint32, 'threshold')),
                                    ('radius_override_enabled', YLeaf(YType.int32, 'radius-override-enabled')),
                                ])
                                self.max_limit = None
                                self.threshold = None
                                self.radius_override_enabled = None
                                self._segment_path = lambda: "inner-vlan-id"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.InnerVlanId, ['max_limit', 'threshold', 'radius_override_enabled'], name, value)


                        class VlanId(Entity):
                            """
                            VLAN ID
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.VlanId, self).__init__()

                                self.yang_name = "vlan-id"
                                self.yang_parent_name = "limit-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_limit', YLeaf(YType.uint32, 'max-limit')),
                                    ('threshold', YLeaf(YType.uint32, 'threshold')),
                                    ('radius_override_enabled', YLeaf(YType.int32, 'radius-override-enabled')),
                                ])
                                self.max_limit = None
                                self.threshold = None
                                self.radius_override_enabled = None
                                self._segment_path = lambda: "vlan-id"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.VlanId, ['max_limit', 'threshold', 'radius_override_enabled'], name, value)


                    class Limits(Entity):
                        """
                        PPPoE session limit information
                        
                        .. attribute:: limit
                        
                        	PPPoE session limit state
                        	**type**\: list of  		 :py:class:`Limit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits.Limit>`
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits, self).__init__()

                            self.yang_name = "limits"
                            self.yang_parent_name = "bba-group"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("limit", ("limit", Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits.Limit))])
                            self._leafs = OrderedDict()

                            self.limit = YList(self)
                            self._segment_path = lambda: "limits"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits, [], name, value)


                        class Limit(Entity):
                            """
                            PPPoE session limit state
                            
                            .. attribute:: interface_name
                            
                            	Access Interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: iwf
                            
                            	IWF flag
                            	**type**\: bool
                            
                            .. attribute:: circuit_id
                            
                            	Circuit ID
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: remote_id
                            
                            	Remote ID
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: outer_vlan_id
                            
                            	Outer VLAN ID
                            	**type**\: int
                            
                            	**range:** 0..4095
                            
                            .. attribute:: inner_vlan_id
                            
                            	Inner VLAN ID
                            	**type**\: int
                            
                            	**range:** 0..4095
                            
                            .. attribute:: state
                            
                            	State
                            	**type**\:  :py:class:`PppoeMaLimitState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.PppoeMaLimitState>`
                            
                            .. attribute:: session_count
                            
                            	Session Count
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_set
                            
                            	Overridden limit has been set
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: override_limit
                            
                            	Overridden limit if set
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits.Limit, self).__init__()

                                self.yang_name = "limit"
                                self.yang_parent_name = "limits"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ('mac_address', YLeaf(YType.str, 'mac-address')),
                                    ('iwf', YLeaf(YType.boolean, 'iwf')),
                                    ('circuit_id', YLeaf(YType.str, 'circuit-id')),
                                    ('remote_id', YLeaf(YType.str, 'remote-id')),
                                    ('outer_vlan_id', YLeaf(YType.uint32, 'outer-vlan-id')),
                                    ('inner_vlan_id', YLeaf(YType.uint32, 'inner-vlan-id')),
                                    ('state', YLeaf(YType.enumeration, 'state')),
                                    ('session_count', YLeaf(YType.uint32, 'session-count')),
                                    ('radius_override_set', YLeaf(YType.int32, 'radius-override-set')),
                                    ('override_limit', YLeaf(YType.uint32, 'override-limit')),
                                ])
                                self.interface_name = None
                                self.mac_address = None
                                self.iwf = None
                                self.circuit_id = None
                                self.remote_id = None
                                self.outer_vlan_id = None
                                self.inner_vlan_id = None
                                self.state = None
                                self.session_count = None
                                self.radius_override_set = None
                                self.override_limit = None
                                self._segment_path = lambda: "limit"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits.Limit, ['interface_name', 'mac_address', 'iwf', 'circuit_id', 'remote_id', 'outer_vlan_id', 'inner_vlan_id', 'state', 'session_count', 'radius_override_set', 'override_limit'], name, value)


                    class Throttles(Entity):
                        """
                        PPPoE throttle information
                        
                        .. attribute:: throttle
                        
                        	PPPoE session throttle state
                        	**type**\: list of  		 :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles.Throttle>`
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles, self).__init__()

                            self.yang_name = "throttles"
                            self.yang_parent_name = "bba-group"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("throttle", ("throttle", Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles.Throttle))])
                            self._leafs = OrderedDict()

                            self.throttle = YList(self)
                            self._segment_path = lambda: "throttles"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles, [], name, value)


                        class Throttle(Entity):
                            """
                            PPPoE session throttle state
                            
                            .. attribute:: interface_name
                            
                            	Access Interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: iwf
                            
                            	IWF flag
                            	**type**\: bool
                            
                            .. attribute:: circuit_id
                            
                            	Circuit ID
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: remote_id
                            
                            	Remote ID
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: outer_vlan_id
                            
                            	Outer VLAN ID
                            	**type**\: int
                            
                            	**range:** 0..4095
                            
                            .. attribute:: inner_vlan_id
                            
                            	Inner VLAN ID
                            	**type**\: int
                            
                            	**range:** 0..4095
                            
                            .. attribute:: state
                            
                            	State
                            	**type**\:  :py:class:`PppoeMaThrottleState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.PppoeMaThrottleState>`
                            
                            .. attribute:: time_left
                            
                            	Time left in seconds
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: since_reset
                            
                            	Number of seconds since counters reset
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: padi_count
                            
                            	PADI Count
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: padr_count
                            
                            	PADR Count
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles.Throttle, self).__init__()

                                self.yang_name = "throttle"
                                self.yang_parent_name = "throttles"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ('mac_address', YLeaf(YType.str, 'mac-address')),
                                    ('iwf', YLeaf(YType.boolean, 'iwf')),
                                    ('circuit_id', YLeaf(YType.str, 'circuit-id')),
                                    ('remote_id', YLeaf(YType.str, 'remote-id')),
                                    ('outer_vlan_id', YLeaf(YType.uint32, 'outer-vlan-id')),
                                    ('inner_vlan_id', YLeaf(YType.uint32, 'inner-vlan-id')),
                                    ('state', YLeaf(YType.enumeration, 'state')),
                                    ('time_left', YLeaf(YType.uint32, 'time-left')),
                                    ('since_reset', YLeaf(YType.uint32, 'since-reset')),
                                    ('padi_count', YLeaf(YType.uint32, 'padi-count')),
                                    ('padr_count', YLeaf(YType.uint32, 'padr-count')),
                                ])
                                self.interface_name = None
                                self.mac_address = None
                                self.iwf = None
                                self.circuit_id = None
                                self.remote_id = None
                                self.outer_vlan_id = None
                                self.inner_vlan_id = None
                                self.state = None
                                self.time_left = None
                                self.since_reset = None
                                self.padi_count = None
                                self.padr_count = None
                                self._segment_path = lambda: "throttle"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles.Throttle, ['interface_name', 'mac_address', 'iwf', 'circuit_id', 'remote_id', 'outer_vlan_id', 'inner_vlan_id', 'state', 'time_left', 'since_reset', 'padi_count', 'padr_count'], name, value)


                    class ThrottleConfig(Entity):
                        """
                        BBA\-Group throttle configuration information
                        
                        .. attribute:: mac
                        
                        	MAC
                        	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.Mac>`
                        
                        .. attribute:: mac_access_interface
                        
                        	MAC Access Interface
                        	**type**\:  :py:class:`MacAccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacAccessInterface>`
                        
                        .. attribute:: mac_iwf_access_interface
                        
                        	MAC IWF Access Interface
                        	**type**\:  :py:class:`MacIwfAccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacIwfAccessInterface>`
                        
                        .. attribute:: circuit_id
                        
                        	Circuit ID
                        	**type**\:  :py:class:`CircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitId>`
                        
                        .. attribute:: remote_id
                        
                        	Remote ID
                        	**type**\:  :py:class:`RemoteId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.RemoteId>`
                        
                        .. attribute:: circuit_id_and_remote_id
                        
                        	Circuit ID and Remote ID
                        	**type**\:  :py:class:`CircuitIdAndRemoteId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitIdAndRemoteId>`
                        
                        .. attribute:: outer_vlan_id
                        
                        	Outer VLAN ID
                        	**type**\:  :py:class:`OuterVlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.OuterVlanId>`
                        
                        .. attribute:: inner_vlan_id
                        
                        	Inner VLAN ID
                        	**type**\:  :py:class:`InnerVlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.InnerVlanId>`
                        
                        .. attribute:: vlan_id
                        
                        	VLAN ID
                        	**type**\:  :py:class:`VlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.VlanId>`
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig, self).__init__()

                            self.yang_name = "throttle-config"
                            self.yang_parent_name = "bba-group"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("mac", ("mac", Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.Mac)), ("mac-access-interface", ("mac_access_interface", Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacAccessInterface)), ("mac-iwf-access-interface", ("mac_iwf_access_interface", Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacIwfAccessInterface)), ("circuit-id", ("circuit_id", Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitId)), ("remote-id", ("remote_id", Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.RemoteId)), ("circuit-id-and-remote-id", ("circuit_id_and_remote_id", Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitIdAndRemoteId)), ("outer-vlan-id", ("outer_vlan_id", Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.OuterVlanId)), ("inner-vlan-id", ("inner_vlan_id", Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.InnerVlanId)), ("vlan-id", ("vlan_id", Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.VlanId))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.mac = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.Mac()
                            self.mac.parent = self
                            self._children_name_map["mac"] = "mac"
                            self._children_yang_names.add("mac")

                            self.mac_access_interface = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacAccessInterface()
                            self.mac_access_interface.parent = self
                            self._children_name_map["mac_access_interface"] = "mac-access-interface"
                            self._children_yang_names.add("mac-access-interface")

                            self.mac_iwf_access_interface = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacIwfAccessInterface()
                            self.mac_iwf_access_interface.parent = self
                            self._children_name_map["mac_iwf_access_interface"] = "mac-iwf-access-interface"
                            self._children_yang_names.add("mac-iwf-access-interface")

                            self.circuit_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitId()
                            self.circuit_id.parent = self
                            self._children_name_map["circuit_id"] = "circuit-id"
                            self._children_yang_names.add("circuit-id")

                            self.remote_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.RemoteId()
                            self.remote_id.parent = self
                            self._children_name_map["remote_id"] = "remote-id"
                            self._children_yang_names.add("remote-id")

                            self.circuit_id_and_remote_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitIdAndRemoteId()
                            self.circuit_id_and_remote_id.parent = self
                            self._children_name_map["circuit_id_and_remote_id"] = "circuit-id-and-remote-id"
                            self._children_yang_names.add("circuit-id-and-remote-id")

                            self.outer_vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.OuterVlanId()
                            self.outer_vlan_id.parent = self
                            self._children_name_map["outer_vlan_id"] = "outer-vlan-id"
                            self._children_yang_names.add("outer-vlan-id")

                            self.inner_vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.InnerVlanId()
                            self.inner_vlan_id.parent = self
                            self._children_name_map["inner_vlan_id"] = "inner-vlan-id"
                            self._children_yang_names.add("inner-vlan-id")

                            self.vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.VlanId()
                            self.vlan_id.parent = self
                            self._children_name_map["vlan_id"] = "vlan-id"
                            self._children_yang_names.add("vlan-id")
                            self._segment_path = lambda: "throttle-config"


                        class Mac(Entity):
                            """
                            MAC
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.Mac, self).__init__()

                                self.yang_name = "mac"
                                self.yang_parent_name = "throttle-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('limit', YLeaf(YType.uint32, 'limit')),
                                    ('request_period', YLeaf(YType.uint32, 'request-period')),
                                    ('blocking_period', YLeaf(YType.uint32, 'blocking-period')),
                                ])
                                self.limit = None
                                self.request_period = None
                                self.blocking_period = None
                                self._segment_path = lambda: "mac"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.Mac, ['limit', 'request_period', 'blocking_period'], name, value)


                        class MacAccessInterface(Entity):
                            """
                            MAC Access Interface
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacAccessInterface, self).__init__()

                                self.yang_name = "mac-access-interface"
                                self.yang_parent_name = "throttle-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('limit', YLeaf(YType.uint32, 'limit')),
                                    ('request_period', YLeaf(YType.uint32, 'request-period')),
                                    ('blocking_period', YLeaf(YType.uint32, 'blocking-period')),
                                ])
                                self.limit = None
                                self.request_period = None
                                self.blocking_period = None
                                self._segment_path = lambda: "mac-access-interface"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacAccessInterface, ['limit', 'request_period', 'blocking_period'], name, value)


                        class MacIwfAccessInterface(Entity):
                            """
                            MAC IWF Access Interface
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacIwfAccessInterface, self).__init__()

                                self.yang_name = "mac-iwf-access-interface"
                                self.yang_parent_name = "throttle-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('limit', YLeaf(YType.uint32, 'limit')),
                                    ('request_period', YLeaf(YType.uint32, 'request-period')),
                                    ('blocking_period', YLeaf(YType.uint32, 'blocking-period')),
                                ])
                                self.limit = None
                                self.request_period = None
                                self.blocking_period = None
                                self._segment_path = lambda: "mac-iwf-access-interface"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacIwfAccessInterface, ['limit', 'request_period', 'blocking_period'], name, value)


                        class CircuitId(Entity):
                            """
                            Circuit ID
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitId, self).__init__()

                                self.yang_name = "circuit-id"
                                self.yang_parent_name = "throttle-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('limit', YLeaf(YType.uint32, 'limit')),
                                    ('request_period', YLeaf(YType.uint32, 'request-period')),
                                    ('blocking_period', YLeaf(YType.uint32, 'blocking-period')),
                                ])
                                self.limit = None
                                self.request_period = None
                                self.blocking_period = None
                                self._segment_path = lambda: "circuit-id"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitId, ['limit', 'request_period', 'blocking_period'], name, value)


                        class RemoteId(Entity):
                            """
                            Remote ID
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.RemoteId, self).__init__()

                                self.yang_name = "remote-id"
                                self.yang_parent_name = "throttle-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('limit', YLeaf(YType.uint32, 'limit')),
                                    ('request_period', YLeaf(YType.uint32, 'request-period')),
                                    ('blocking_period', YLeaf(YType.uint32, 'blocking-period')),
                                ])
                                self.limit = None
                                self.request_period = None
                                self.blocking_period = None
                                self._segment_path = lambda: "remote-id"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.RemoteId, ['limit', 'request_period', 'blocking_period'], name, value)


                        class CircuitIdAndRemoteId(Entity):
                            """
                            Circuit ID and Remote ID
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitIdAndRemoteId, self).__init__()

                                self.yang_name = "circuit-id-and-remote-id"
                                self.yang_parent_name = "throttle-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('limit', YLeaf(YType.uint32, 'limit')),
                                    ('request_period', YLeaf(YType.uint32, 'request-period')),
                                    ('blocking_period', YLeaf(YType.uint32, 'blocking-period')),
                                ])
                                self.limit = None
                                self.request_period = None
                                self.blocking_period = None
                                self._segment_path = lambda: "circuit-id-and-remote-id"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitIdAndRemoteId, ['limit', 'request_period', 'blocking_period'], name, value)


                        class OuterVlanId(Entity):
                            """
                            Outer VLAN ID
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.OuterVlanId, self).__init__()

                                self.yang_name = "outer-vlan-id"
                                self.yang_parent_name = "throttle-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('limit', YLeaf(YType.uint32, 'limit')),
                                    ('request_period', YLeaf(YType.uint32, 'request-period')),
                                    ('blocking_period', YLeaf(YType.uint32, 'blocking-period')),
                                ])
                                self.limit = None
                                self.request_period = None
                                self.blocking_period = None
                                self._segment_path = lambda: "outer-vlan-id"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.OuterVlanId, ['limit', 'request_period', 'blocking_period'], name, value)


                        class InnerVlanId(Entity):
                            """
                            Inner VLAN ID
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.InnerVlanId, self).__init__()

                                self.yang_name = "inner-vlan-id"
                                self.yang_parent_name = "throttle-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('limit', YLeaf(YType.uint32, 'limit')),
                                    ('request_period', YLeaf(YType.uint32, 'request-period')),
                                    ('blocking_period', YLeaf(YType.uint32, 'blocking-period')),
                                ])
                                self.limit = None
                                self.request_period = None
                                self.blocking_period = None
                                self._segment_path = lambda: "inner-vlan-id"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.InnerVlanId, ['limit', 'request_period', 'blocking_period'], name, value)


                        class VlanId(Entity):
                            """
                            VLAN ID
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.VlanId, self).__init__()

                                self.yang_name = "vlan-id"
                                self.yang_parent_name = "throttle-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('limit', YLeaf(YType.uint32, 'limit')),
                                    ('request_period', YLeaf(YType.uint32, 'request-period')),
                                    ('blocking_period', YLeaf(YType.uint32, 'blocking-period')),
                                ])
                                self.limit = None
                                self.request_period = None
                                self.blocking_period = None
                                self._segment_path = lambda: "vlan-id"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.VlanId, ['limit', 'request_period', 'blocking_period'], name, value)


            class SummaryTotal(Entity):
                """
                PPPoE statistics for a given node
                
                .. attribute:: ready_access_interfaces
                
                	Ready Access Interface Count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: not_ready_access_interfaces
                
                	Not Ready Access Interface Count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: complete_sessions
                
                	Complete Session Count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: incomplete_sessions
                
                	Incomplete Session Count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: flow_control_limit
                
                	Flow Control credit limit
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: flow_control_in_flight_sessions
                
                	Flow Control In\-Flight Count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: flow_control_dropped_sessions
                
                	Flow Control Drop Count
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: flow_control_disconnected_sessions
                
                	Flow Control Disconnected Count
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: flow_control_successful_sessions
                
                	Flow Control Success Count, sessions completing call flow
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pppoema_subscriber_infra_flow_control
                
                	PPPoEMASubscriberInfraFlowControl
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Pppoe.Nodes.Node.SummaryTotal, self).__init__()

                    self.yang_name = "summary-total"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ready_access_interfaces', YLeaf(YType.uint32, 'ready-access-interfaces')),
                        ('not_ready_access_interfaces', YLeaf(YType.uint32, 'not-ready-access-interfaces')),
                        ('complete_sessions', YLeaf(YType.uint32, 'complete-sessions')),
                        ('incomplete_sessions', YLeaf(YType.uint32, 'incomplete-sessions')),
                        ('flow_control_limit', YLeaf(YType.uint32, 'flow-control-limit')),
                        ('flow_control_in_flight_sessions', YLeaf(YType.uint32, 'flow-control-in-flight-sessions')),
                        ('flow_control_dropped_sessions', YLeaf(YType.uint64, 'flow-control-dropped-sessions')),
                        ('flow_control_disconnected_sessions', YLeaf(YType.uint64, 'flow-control-disconnected-sessions')),
                        ('flow_control_successful_sessions', YLeaf(YType.uint64, 'flow-control-successful-sessions')),
                        ('pppoema_subscriber_infra_flow_control', YLeaf(YType.uint32, 'pppoema-subscriber-infra-flow-control')),
                    ])
                    self.ready_access_interfaces = None
                    self.not_ready_access_interfaces = None
                    self.complete_sessions = None
                    self.incomplete_sessions = None
                    self.flow_control_limit = None
                    self.flow_control_in_flight_sessions = None
                    self.flow_control_dropped_sessions = None
                    self.flow_control_disconnected_sessions = None
                    self.flow_control_successful_sessions = None
                    self.pppoema_subscriber_infra_flow_control = None
                    self._segment_path = lambda: "summary-total"

                def __setattr__(self, name, value):
                    self._perform_setattr(Pppoe.Nodes.Node.SummaryTotal, ['ready_access_interfaces', 'not_ready_access_interfaces', 'complete_sessions', 'incomplete_sessions', 'flow_control_limit', 'flow_control_in_flight_sessions', 'flow_control_dropped_sessions', 'flow_control_disconnected_sessions', 'flow_control_successful_sessions', 'pppoema_subscriber_infra_flow_control'], name, value)

    def clone_ptr(self):
        self._top_entity = Pppoe()
        return self._top_entity


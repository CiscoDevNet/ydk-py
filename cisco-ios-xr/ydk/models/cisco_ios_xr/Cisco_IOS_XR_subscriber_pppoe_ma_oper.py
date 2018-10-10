""" Cisco_IOS_XR_subscriber_pppoe_ma_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-pppoe\-ma package operational data.

This module contains definitions
for the following management objects\:
  pppoe\: PPPoE operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
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


class PppoeMaSessionState(Enum):
    """
    PppoeMaSessionState (Enum Class)

    Pppoe ma session state

    .. data:: destroying = 0

    	Destroying session

    .. data:: deleting = 1

    	Deleting interface

    .. data:: initializing = 2

    	Initializing

    .. data:: created = 3

    	Interface created

    .. data:: stopping = 4

    	Stopping AAA session

    .. data:: started = 5

    	AAA session started

    .. data:: activated = 6

    	SubDB Config activated

    .. data:: complete = 7

    	Complete

    """

    destroying = Enum.YLeaf(0, "destroying")

    deleting = Enum.YLeaf(1, "deleting")

    initializing = Enum.YLeaf(2, "initializing")

    created = Enum.YLeaf(3, "created")

    stopping = Enum.YLeaf(4, "stopping")

    started = Enum.YLeaf(5, "started")

    activated = Enum.YLeaf(6, "activated")

    complete = Enum.YLeaf(7, "complete")


class PppoeMaSessionTrig(Enum):
    """
    PppoeMaSessionTrig (Enum Class)

    Pppoe ma session trig

    .. data:: pppoe_ma_session_trig_error = 0

    	pppoe ma session trig error

    .. data:: pppoe_ma_session_trig_publish_encaps_attr_fail = 1

    	pppoe ma session trig publish encaps attr fail

    .. data:: pppoe_ma_session_trig_if_create_fail = 2

    	pppoe ma session trig if create fail

    .. data:: pppoe_ma_session_trig_iedge_session_start_fail = 3

    	pppoe ma session trig iedge session start fail

    .. data:: pppoe_ma_session_trig_iedge_session_update_fail = 4

    	pppoe ma session trig iedge session update fail

    .. data:: pppoe_ma_session_trig_sub_db_activate_fail = 5

    	pppoe ma session trig sub db activate fail

    .. data:: pppoe_ma_session_trig_in_flight_timeout = 6

    	pppoe ma session trig in flight timeout

    .. data:: pppoe_ma_session_trig_down = 7

    	pppoe ma session trig down

    .. data:: pppoe_ma_session_trig_parent = 8

    	pppoe ma session trig parent

    .. data:: pppoe_ma_session_trig_padt = 9

    	pppoe ma session trig padt

    .. data:: pppoe_ma_session_trig_session_pak = 10

    	pppoe ma session trig session pak

    .. data:: pppoe_ma_session_trig_final = 11

    	pppoe ma session trig final

    .. data:: pppoe_ma_session_trig_no_im_or = 12

    	pppoe ma session trig no im or

    .. data:: pppoe_ma_session_trig_restart = 13

    	pppoe ma session trig restart

    .. data:: pppoe_ma_session_trig_admissions_config_change = 14

    	pppoe ma session trig admissions config change

    .. data:: pppoe_ma_session_trig_iedge_disconnect = 15

    	pppoe ma session trig iedge disconnect

    .. data:: pppoe_ma_session_trig_invalid_vlan_tags = 16

    	pppoe ma session trig invalid vlan tags

    .. data:: pppoe_ma_session_trig_port_limit_disconnect = 17

    	pppoe ma session trig port limit disconnect

    .. data:: pppoe_ma_session_trig_srg_disconnect = 18

    	pppoe ma session trig srg disconnect

    .. data:: pppoe_ma_session_trig_srg_sweep = 19

    	pppoe ma session trig srg sweep

    .. data:: pppoe_ma_session_trig_count = 20

    	pppoe ma session trig count

    """

    pppoe_ma_session_trig_error = Enum.YLeaf(0, "pppoe-ma-session-trig-error")

    pppoe_ma_session_trig_publish_encaps_attr_fail = Enum.YLeaf(1, "pppoe-ma-session-trig-publish-encaps-attr-fail")

    pppoe_ma_session_trig_if_create_fail = Enum.YLeaf(2, "pppoe-ma-session-trig-if-create-fail")

    pppoe_ma_session_trig_iedge_session_start_fail = Enum.YLeaf(3, "pppoe-ma-session-trig-iedge-session-start-fail")

    pppoe_ma_session_trig_iedge_session_update_fail = Enum.YLeaf(4, "pppoe-ma-session-trig-iedge-session-update-fail")

    pppoe_ma_session_trig_sub_db_activate_fail = Enum.YLeaf(5, "pppoe-ma-session-trig-sub-db-activate-fail")

    pppoe_ma_session_trig_in_flight_timeout = Enum.YLeaf(6, "pppoe-ma-session-trig-in-flight-timeout")

    pppoe_ma_session_trig_down = Enum.YLeaf(7, "pppoe-ma-session-trig-down")

    pppoe_ma_session_trig_parent = Enum.YLeaf(8, "pppoe-ma-session-trig-parent")

    pppoe_ma_session_trig_padt = Enum.YLeaf(9, "pppoe-ma-session-trig-padt")

    pppoe_ma_session_trig_session_pak = Enum.YLeaf(10, "pppoe-ma-session-trig-session-pak")

    pppoe_ma_session_trig_final = Enum.YLeaf(11, "pppoe-ma-session-trig-final")

    pppoe_ma_session_trig_no_im_or = Enum.YLeaf(12, "pppoe-ma-session-trig-no-im-or")

    pppoe_ma_session_trig_restart = Enum.YLeaf(13, "pppoe-ma-session-trig-restart")

    pppoe_ma_session_trig_admissions_config_change = Enum.YLeaf(14, "pppoe-ma-session-trig-admissions-config-change")

    pppoe_ma_session_trig_iedge_disconnect = Enum.YLeaf(15, "pppoe-ma-session-trig-iedge-disconnect")

    pppoe_ma_session_trig_invalid_vlan_tags = Enum.YLeaf(16, "pppoe-ma-session-trig-invalid-vlan-tags")

    pppoe_ma_session_trig_port_limit_disconnect = Enum.YLeaf(17, "pppoe-ma-session-trig-port-limit-disconnect")

    pppoe_ma_session_trig_srg_disconnect = Enum.YLeaf(18, "pppoe-ma-session-trig-srg-disconnect")

    pppoe_ma_session_trig_srg_sweep = Enum.YLeaf(19, "pppoe-ma-session-trig-srg-sweep")

    pppoe_ma_session_trig_count = Enum.YLeaf(20, "pppoe-ma-session-trig-count")


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
        self._child_classes = OrderedDict([("access-interface-statistics", ("access_interface_statistics", Pppoe.AccessInterfaceStatistics)), ("nodes", ("nodes", Pppoe.Nodes))])
        self._leafs = OrderedDict()

        self.access_interface_statistics = Pppoe.AccessInterfaceStatistics()
        self.access_interface_statistics.parent = self
        self._children_name_map["access_interface_statistics"] = "access-interface-statistics"

        self.nodes = Pppoe.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-subscriber-pppoe-ma-oper:pppoe"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Pppoe, [], name, value)


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
            self._child_classes = OrderedDict([("access-interface-statistic", ("access_interface_statistic", Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic))])
            self._leafs = OrderedDict()

            self.access_interface_statistic = YList(self)
            self._segment_path = lambda: "access-interface-statistics"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-pppoe-ma-oper:pppoe/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pppoe.AccessInterfaceStatistics, [], name, value)


        class AccessInterfaceStatistic(Entity):
            """
            Statistics information for a PPPoE\-enabled
            access interface
            
            .. attribute:: interface_name  (key)
            
            	PPPoE Access Interface
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
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
                self._child_classes = OrderedDict([("packet-counts", ("packet_counts", Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts))])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                ])
                self.interface_name = None

                self.packet_counts = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts()
                self.packet_counts.parent = self
                self._children_name_map["packet_counts"] = "packet-counts"
                self._segment_path = lambda: "access-interface-statistic" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-pppoe-ma-oper:pppoe/access-interface-statistics/%s" % self._segment_path()
                self._is_frozen = True

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
                    self._child_classes = OrderedDict([("padi", ("padi", Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padi)), ("pado", ("pado", Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Pado)), ("padr", ("padr", Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padr)), ("pads-success", ("pads_success", Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsSuccess)), ("pads-error", ("pads_error", Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsError)), ("padt", ("padt", Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padt)), ("session-state", ("session_state", Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.SessionState)), ("other", ("other", Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Other))])
                    self._leafs = OrderedDict()

                    self.padi = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padi()
                    self.padi.parent = self
                    self._children_name_map["padi"] = "padi"

                    self.pado = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Pado()
                    self.pado.parent = self
                    self._children_name_map["pado"] = "pado"

                    self.padr = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padr()
                    self.padr.parent = self
                    self._children_name_map["padr"] = "padr"

                    self.pads_success = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsSuccess()
                    self.pads_success.parent = self
                    self._children_name_map["pads_success"] = "pads-success"

                    self.pads_error = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsError()
                    self.pads_error.parent = self
                    self._children_name_map["pads_error"] = "pads-error"

                    self.padt = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padt()
                    self.padt.parent = self
                    self._children_name_map["padt"] = "padt"

                    self.session_state = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.SessionState()
                    self.session_state.parent = self
                    self._children_name_map["session_state"] = "session-state"

                    self.other = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Other()
                    self.other.parent = self
                    self._children_name_map["other"] = "other"
                    self._segment_path = lambda: "packet-counts"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts, [], name, value)


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
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sent', (YLeaf(YType.uint32, 'sent'), ['int'])),
                            ('received', (YLeaf(YType.uint32, 'received'), ['int'])),
                            ('dropped', (YLeaf(YType.uint32, 'dropped'), ['int'])),
                        ])
                        self.sent = None
                        self.received = None
                        self.dropped = None
                        self._segment_path = lambda: "padi"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padi, [u'sent', u'received', u'dropped'], name, value)


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
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sent', (YLeaf(YType.uint32, 'sent'), ['int'])),
                            ('received', (YLeaf(YType.uint32, 'received'), ['int'])),
                            ('dropped', (YLeaf(YType.uint32, 'dropped'), ['int'])),
                        ])
                        self.sent = None
                        self.received = None
                        self.dropped = None
                        self._segment_path = lambda: "pado"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Pado, [u'sent', u'received', u'dropped'], name, value)


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
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sent', (YLeaf(YType.uint32, 'sent'), ['int'])),
                            ('received', (YLeaf(YType.uint32, 'received'), ['int'])),
                            ('dropped', (YLeaf(YType.uint32, 'dropped'), ['int'])),
                        ])
                        self.sent = None
                        self.received = None
                        self.dropped = None
                        self._segment_path = lambda: "padr"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padr, [u'sent', u'received', u'dropped'], name, value)


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
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sent', (YLeaf(YType.uint32, 'sent'), ['int'])),
                            ('received', (YLeaf(YType.uint32, 'received'), ['int'])),
                            ('dropped', (YLeaf(YType.uint32, 'dropped'), ['int'])),
                        ])
                        self.sent = None
                        self.received = None
                        self.dropped = None
                        self._segment_path = lambda: "pads-success"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsSuccess, [u'sent', u'received', u'dropped'], name, value)


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
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sent', (YLeaf(YType.uint32, 'sent'), ['int'])),
                            ('received', (YLeaf(YType.uint32, 'received'), ['int'])),
                            ('dropped', (YLeaf(YType.uint32, 'dropped'), ['int'])),
                        ])
                        self.sent = None
                        self.received = None
                        self.dropped = None
                        self._segment_path = lambda: "pads-error"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsError, [u'sent', u'received', u'dropped'], name, value)


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
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sent', (YLeaf(YType.uint32, 'sent'), ['int'])),
                            ('received', (YLeaf(YType.uint32, 'received'), ['int'])),
                            ('dropped', (YLeaf(YType.uint32, 'dropped'), ['int'])),
                        ])
                        self.sent = None
                        self.received = None
                        self.dropped = None
                        self._segment_path = lambda: "padt"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padt, [u'sent', u'received', u'dropped'], name, value)


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
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sent', (YLeaf(YType.uint32, 'sent'), ['int'])),
                            ('received', (YLeaf(YType.uint32, 'received'), ['int'])),
                            ('dropped', (YLeaf(YType.uint32, 'dropped'), ['int'])),
                        ])
                        self.sent = None
                        self.received = None
                        self.dropped = None
                        self._segment_path = lambda: "session-state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.SessionState, [u'sent', u'received', u'dropped'], name, value)


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
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sent', (YLeaf(YType.uint32, 'sent'), ['int'])),
                            ('received', (YLeaf(YType.uint32, 'received'), ['int'])),
                            ('dropped', (YLeaf(YType.uint32, 'dropped'), ['int'])),
                        ])
                        self.sent = None
                        self.received = None
                        self.dropped = None
                        self._segment_path = lambda: "other"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Other, [u'sent', u'received', u'dropped'], name, value)


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
            self._child_classes = OrderedDict([("node", ("node", Pppoe.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-pppoe-ma-oper:pppoe/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pppoe.Nodes, [], name, value)


        class Node(Entity):
            """
            PPPoE operational data for a particular node
            
            .. attribute:: node_name  (key)
            
            	Node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: disconnect_history
            
            	PPPoE disconnect history for a given node
            	**type**\:  :py:class:`DisconnectHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistory>`
            
            .. attribute:: disconnect_history_unique
            
            	PPPoE unique disconnect history for a given node
            	**type**\:  :py:class:`DisconnectHistoryUnique <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistoryUnique>`
            
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
                self._child_classes = OrderedDict([("disconnect-history", ("disconnect_history", Pppoe.Nodes.Node.DisconnectHistory)), ("disconnect-history-unique", ("disconnect_history_unique", Pppoe.Nodes.Node.DisconnectHistoryUnique)), ("statistics", ("statistics", Pppoe.Nodes.Node.Statistics)), ("access-interface", ("access_interface", Pppoe.Nodes.Node.AccessInterface)), ("interfaces", ("interfaces", Pppoe.Nodes.Node.Interfaces)), ("bba-groups", ("bba_groups", Pppoe.Nodes.Node.BbaGroups)), ("summary-total", ("summary_total", Pppoe.Nodes.Node.SummaryTotal))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.disconnect_history = Pppoe.Nodes.Node.DisconnectHistory()
                self.disconnect_history.parent = self
                self._children_name_map["disconnect_history"] = "disconnect-history"

                self.disconnect_history_unique = Pppoe.Nodes.Node.DisconnectHistoryUnique()
                self.disconnect_history_unique.parent = self
                self._children_name_map["disconnect_history_unique"] = "disconnect-history-unique"

                self.statistics = Pppoe.Nodes.Node.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"

                self.access_interface = Pppoe.Nodes.Node.AccessInterface()
                self.access_interface.parent = self
                self._children_name_map["access_interface"] = "access-interface"

                self.interfaces = Pppoe.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"

                self.bba_groups = Pppoe.Nodes.Node.BbaGroups()
                self.bba_groups.parent = self
                self._children_name_map["bba_groups"] = "bba-groups"

                self.summary_total = Pppoe.Nodes.Node.SummaryTotal()
                self.summary_total.parent = self
                self._children_name_map["summary_total"] = "summary-total"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-pppoe-ma-oper:pppoe/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Pppoe.Nodes.Node, ['node_name'], name, value)


            class DisconnectHistory(Entity):
                """
                PPPoE disconnect history for a given node
                
                .. attribute:: current_idx
                
                	Current index of history
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: entry
                
                	Array of disconnected subscribers
                	**type**\: list of  		 :py:class:`Entry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistory.Entry>`
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Pppoe.Nodes.Node.DisconnectHistory, self).__init__()

                    self.yang_name = "disconnect-history"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("entry", ("entry", Pppoe.Nodes.Node.DisconnectHistory.Entry))])
                    self._leafs = OrderedDict([
                        ('current_idx', (YLeaf(YType.uint32, 'current-idx'), ['int'])),
                    ])
                    self.current_idx = None

                    self.entry = YList(self)
                    self._segment_path = lambda: "disconnect-history"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistory, [u'current_idx'], name, value)


                class Entry(Entity):
                    """
                    Array of disconnected subscribers
                    
                    .. attribute:: session_idb
                    
                    	Session IDB
                    	**type**\:  :py:class:`SessionIdb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb>`
                    
                    .. attribute:: timestamp
                    
                    	Time when disconnected
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ifname
                    
                    	Interface name
                    	**type**\: str
                    
                    .. attribute:: trigger
                    
                    	Disconnect Trigger
                    	**type**\:  :py:class:`PppoeMaSessionTrig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.PppoeMaSessionTrig>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.Nodes.Node.DisconnectHistory.Entry, self).__init__()

                        self.yang_name = "entry"
                        self.yang_parent_name = "disconnect-history"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("session-idb", ("session_idb", Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb))])
                        self._leafs = OrderedDict([
                            ('timestamp', (YLeaf(YType.uint64, 'timestamp'), ['int'])),
                            ('ifname', (YLeaf(YType.str, 'ifname'), ['str'])),
                            ('trigger', (YLeaf(YType.enumeration, 'trigger'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'PppoeMaSessionTrig', '')])),
                        ])
                        self.timestamp = None
                        self.ifname = None
                        self.trigger = None

                        self.session_idb = Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb()
                        self.session_idb.parent = self
                        self._children_name_map["session_idb"] = "session-idb"
                        self._segment_path = lambda: "entry"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistory.Entry, [u'timestamp', u'ifname', u'trigger'], name, value)


                    class SessionIdb(Entity):
                        """
                        Session IDB
                        
                        .. attribute:: tags
                        
                        	Tags
                        	**type**\:  :py:class:`Tags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.Tags>`
                        
                        .. attribute:: vlan_outer_tag
                        
                        	VLAN Outer Tag
                        	**type**\:  :py:class:`VlanOuterTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.VlanOuterTag>`
                        
                        .. attribute:: vlan_inner_tag
                        
                        	VLAN Inner Tag
                        	**type**\:  :py:class:`VlanInnerTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.VlanInnerTag>`
                        
                        .. attribute:: interface
                        
                        	Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: access_interface
                        
                        	Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: session_id
                        
                        	Session ID
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: sub_label
                        
                        	Sub Label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: peer_mac_address
                        
                        	Peer Mac\-Address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: state
                        
                        	State
                        	**type**\:  :py:class:`PppoeMaSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.PppoeMaSessionState>`
                        
                        .. attribute:: cdm_object_handle
                        
                        	CDM Object Handle
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: chkpt_id
                        
                        	Chkpt ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: punted_count
                        
                        	Punted Count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: port_limit
                        
                        	Port Limit
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_counted
                        
                        	Is BBA Counted
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_vlan_outer_tag
                        
                        	Is VLAN Outer Tag
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_vlan_inner_tag
                        
                        	Is VLAN Inner Tag
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_cleanup_pending
                        
                        	Is Cleanup Pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_disconnect_done_pending
                        
                        	Is Disconnect Done Pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_delete_done_pending
                        
                        	Is Delete Done Pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_intf_create_callback_pending
                        
                        	Is Interface Create Callback pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_publish_encaps_attr_pending
                        
                        	Is Publish Encaps Attr pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_publish_encaps_attr_cb_pending
                        
                        	Is Publish Encaps Attr Callback pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_intf_delete_callback_pending
                        
                        	Is Interface Delete Callback pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_intf_delete_pending
                        
                        	Is Interface Delete pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_im_owned_resource
                        
                        	Is IM Owned Resource
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_im_final_received
                        
                        	Is IM Final received
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_im_owned_resource_missing
                        
                        	Is IM Owned Resource missing
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_aaa_start_request_callback_pending
                        
                        	Is AAA Start request callback pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_aaa_owned_resource
                        
                        	Is AAA Owned Resource
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_aaa_disconnect_requested
                        
                        	Is AAA Disconnect Requested
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_aaa_disconnect_received
                        
                        	Is AAA Disconnect Received
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_sub_db_activate_callback_pending
                        
                        	Is SubDB Activate callback pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_pads_sent
                        
                        	Is PADS Sent
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_padt_received
                        
                        	Is PADT Received
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_in_flight
                        
                        	Is Session In Flight
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_radius_override
                        
                        	Is RADIUS override enabled
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: expected_notifications
                        
                        	Expected Notifications
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: received_notifications
                        
                        	Received Notifications
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: srg_state
                        
                        	SRG state
                        	**type**\:  :py:class:`PppoeMaSessionIdbSrgState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.PppoeMaSessionIdbSrgState>`
                        
                        .. attribute:: is_srg_data_received
                        
                        	Is SRG Data Received
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_iedge_data_received
                        
                        	Is IEDGE Data Received
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb, self).__init__()

                            self.yang_name = "session-idb"
                            self.yang_parent_name = "entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("tags", ("tags", Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.Tags)), ("vlan-outer-tag", ("vlan_outer_tag", Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.VlanOuterTag)), ("vlan-inner-tag", ("vlan_inner_tag", Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.VlanInnerTag))])
                            self._leafs = OrderedDict([
                                ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                ('access_interface', (YLeaf(YType.str, 'access-interface'), ['str'])),
                                ('session_id', (YLeaf(YType.uint16, 'session-id'), ['int'])),
                                ('sub_label', (YLeaf(YType.uint32, 'sub-label'), ['int'])),
                                ('peer_mac_address', (YLeaf(YType.str, 'peer-mac-address'), ['str'])),
                                ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'PppoeMaSessionState', '')])),
                                ('cdm_object_handle', (YLeaf(YType.uint32, 'cdm-object-handle'), ['int'])),
                                ('chkpt_id', (YLeaf(YType.uint32, 'chkpt-id'), ['int'])),
                                ('punted_count', (YLeaf(YType.uint32, 'punted-count'), ['int'])),
                                ('port_limit', (YLeaf(YType.uint32, 'port-limit'), ['int'])),
                                ('is_counted', (YLeaf(YType.int32, 'is-counted'), ['int'])),
                                ('is_vlan_outer_tag', (YLeaf(YType.int32, 'is-vlan-outer-tag'), ['int'])),
                                ('is_vlan_inner_tag', (YLeaf(YType.int32, 'is-vlan-inner-tag'), ['int'])),
                                ('is_cleanup_pending', (YLeaf(YType.int32, 'is-cleanup-pending'), ['int'])),
                                ('is_disconnect_done_pending', (YLeaf(YType.int32, 'is-disconnect-done-pending'), ['int'])),
                                ('is_delete_done_pending', (YLeaf(YType.int32, 'is-delete-done-pending'), ['int'])),
                                ('is_intf_create_callback_pending', (YLeaf(YType.int32, 'is-intf-create-callback-pending'), ['int'])),
                                ('is_publish_encaps_attr_pending', (YLeaf(YType.int32, 'is-publish-encaps-attr-pending'), ['int'])),
                                ('is_publish_encaps_attr_cb_pending', (YLeaf(YType.int32, 'is-publish-encaps-attr-cb-pending'), ['int'])),
                                ('is_intf_delete_callback_pending', (YLeaf(YType.int32, 'is-intf-delete-callback-pending'), ['int'])),
                                ('is_intf_delete_pending', (YLeaf(YType.int32, 'is-intf-delete-pending'), ['int'])),
                                ('is_im_owned_resource', (YLeaf(YType.int32, 'is-im-owned-resource'), ['int'])),
                                ('is_im_final_received', (YLeaf(YType.int32, 'is-im-final-received'), ['int'])),
                                ('is_im_owned_resource_missing', (YLeaf(YType.int32, 'is-im-owned-resource-missing'), ['int'])),
                                ('is_aaa_start_request_callback_pending', (YLeaf(YType.int32, 'is-aaa-start-request-callback-pending'), ['int'])),
                                ('is_aaa_owned_resource', (YLeaf(YType.int32, 'is-aaa-owned-resource'), ['int'])),
                                ('is_aaa_disconnect_requested', (YLeaf(YType.int32, 'is-aaa-disconnect-requested'), ['int'])),
                                ('is_aaa_disconnect_received', (YLeaf(YType.int32, 'is-aaa-disconnect-received'), ['int'])),
                                ('is_sub_db_activate_callback_pending', (YLeaf(YType.int32, 'is-sub-db-activate-callback-pending'), ['int'])),
                                ('is_pads_sent', (YLeaf(YType.int32, 'is-pads-sent'), ['int'])),
                                ('is_padt_received', (YLeaf(YType.int32, 'is-padt-received'), ['int'])),
                                ('is_in_flight', (YLeaf(YType.int32, 'is-in-flight'), ['int'])),
                                ('is_radius_override', (YLeaf(YType.int32, 'is-radius-override'), ['int'])),
                                ('expected_notifications', (YLeaf(YType.uint8, 'expected-notifications'), ['int'])),
                                ('received_notifications', (YLeaf(YType.uint8, 'received-notifications'), ['int'])),
                                ('srg_state', (YLeaf(YType.enumeration, 'srg-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'PppoeMaSessionIdbSrgState', '')])),
                                ('is_srg_data_received', (YLeaf(YType.int32, 'is-srg-data-received'), ['int'])),
                                ('is_iedge_data_received', (YLeaf(YType.int32, 'is-iedge-data-received'), ['int'])),
                            ])
                            self.interface = None
                            self.access_interface = None
                            self.session_id = None
                            self.sub_label = None
                            self.peer_mac_address = None
                            self.state = None
                            self.cdm_object_handle = None
                            self.chkpt_id = None
                            self.punted_count = None
                            self.port_limit = None
                            self.is_counted = None
                            self.is_vlan_outer_tag = None
                            self.is_vlan_inner_tag = None
                            self.is_cleanup_pending = None
                            self.is_disconnect_done_pending = None
                            self.is_delete_done_pending = None
                            self.is_intf_create_callback_pending = None
                            self.is_publish_encaps_attr_pending = None
                            self.is_publish_encaps_attr_cb_pending = None
                            self.is_intf_delete_callback_pending = None
                            self.is_intf_delete_pending = None
                            self.is_im_owned_resource = None
                            self.is_im_final_received = None
                            self.is_im_owned_resource_missing = None
                            self.is_aaa_start_request_callback_pending = None
                            self.is_aaa_owned_resource = None
                            self.is_aaa_disconnect_requested = None
                            self.is_aaa_disconnect_received = None
                            self.is_sub_db_activate_callback_pending = None
                            self.is_pads_sent = None
                            self.is_padt_received = None
                            self.is_in_flight = None
                            self.is_radius_override = None
                            self.expected_notifications = None
                            self.received_notifications = None
                            self.srg_state = None
                            self.is_srg_data_received = None
                            self.is_iedge_data_received = None

                            self.tags = Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.Tags()
                            self.tags.parent = self
                            self._children_name_map["tags"] = "tags"

                            self.vlan_outer_tag = Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.VlanOuterTag()
                            self.vlan_outer_tag.parent = self
                            self._children_name_map["vlan_outer_tag"] = "vlan-outer-tag"

                            self.vlan_inner_tag = Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.VlanInnerTag()
                            self.vlan_inner_tag.parent = self
                            self._children_name_map["vlan_inner_tag"] = "vlan-inner-tag"
                            self._segment_path = lambda: "session-idb"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb, [u'interface', u'access_interface', u'session_id', u'sub_label', u'peer_mac_address', u'state', u'cdm_object_handle', u'chkpt_id', u'punted_count', u'port_limit', u'is_counted', u'is_vlan_outer_tag', u'is_vlan_inner_tag', u'is_cleanup_pending', u'is_disconnect_done_pending', u'is_delete_done_pending', u'is_intf_create_callback_pending', u'is_publish_encaps_attr_pending', u'is_publish_encaps_attr_cb_pending', u'is_intf_delete_callback_pending', u'is_intf_delete_pending', u'is_im_owned_resource', u'is_im_final_received', u'is_im_owned_resource_missing', u'is_aaa_start_request_callback_pending', u'is_aaa_owned_resource', u'is_aaa_disconnect_requested', u'is_aaa_disconnect_received', u'is_sub_db_activate_callback_pending', u'is_pads_sent', u'is_padt_received', u'is_in_flight', u'is_radius_override', u'expected_notifications', u'received_notifications', u'srg_state', u'is_srg_data_received', u'is_iedge_data_received'], name, value)


                        class Tags(Entity):
                            """
                            Tags
                            
                            .. attribute:: access_loop_encapsulation
                            
                            	Access Loop Encapsulation
                            	**type**\:  :py:class:`AccessLoopEncapsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.Tags.AccessLoopEncapsulation>`
                            
                            .. attribute:: is_service_name
                            
                            	Is Service Name
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_max_payload
                            
                            	Is Max Payload
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_host_uniq
                            
                            	Is Host Uniq
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_relay_session_id
                            
                            	Is Relay Session ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_vendor_specific
                            
                            	Is Vendor Specific
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_iwf
                            
                            	Is IWF
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_remote_id
                            
                            	Is Remote ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_circuit_id
                            
                            	Is Circuit ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_tag
                            
                            	Is DSL Tag
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: service_name
                            
                            	Service Name
                            	**type**\: str
                            
                            .. attribute:: max_payload
                            
                            	Max Payload
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
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
                            
                            .. attribute:: is_dsl_actual_up
                            
                            	Is DSL Actual Up
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_actual_down
                            
                            	Is DSL Actual Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_min_up
                            
                            	Is DSL Min Up
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_min_down
                            
                            	Is DSL Min Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_attain_up
                            
                            	Is DSL Attain Up
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_attain_down
                            
                            	Is DSL Attain Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_max_up
                            
                            	Is DSL Max Up
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_max_down
                            
                            	Is DSL Max Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_min_up_low
                            
                            	Is DSL Min Up Low
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_min_down_low
                            
                            	Is DSL Min Down Low
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_max_delay_up
                            
                            	Is DSL Max Delay Up
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_actual_delay_up
                            
                            	Is DSL Actual Delay Up
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_max_delay_down
                            
                            	Is DSL Max Delay Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_actual_delay_down
                            
                            	Is DSL Actual Delay Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_access_loop_encapsulation
                            
                            	Is Access Loop Encapsulation
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
                                super(Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.Tags, self).__init__()

                                self.yang_name = "tags"
                                self.yang_parent_name = "session-idb"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("access-loop-encapsulation", ("access_loop_encapsulation", Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.Tags.AccessLoopEncapsulation))])
                                self._leafs = OrderedDict([
                                    ('is_service_name', (YLeaf(YType.int32, 'is-service-name'), ['int'])),
                                    ('is_max_payload', (YLeaf(YType.int32, 'is-max-payload'), ['int'])),
                                    ('is_host_uniq', (YLeaf(YType.int32, 'is-host-uniq'), ['int'])),
                                    ('is_relay_session_id', (YLeaf(YType.int32, 'is-relay-session-id'), ['int'])),
                                    ('is_vendor_specific', (YLeaf(YType.int32, 'is-vendor-specific'), ['int'])),
                                    ('is_iwf', (YLeaf(YType.int32, 'is-iwf'), ['int'])),
                                    ('is_remote_id', (YLeaf(YType.int32, 'is-remote-id'), ['int'])),
                                    ('is_circuit_id', (YLeaf(YType.int32, 'is-circuit-id'), ['int'])),
                                    ('is_dsl_tag', (YLeaf(YType.int32, 'is-dsl-tag'), ['int'])),
                                    ('service_name', (YLeaf(YType.str, 'service-name'), ['str'])),
                                    ('max_payload', (YLeaf(YType.uint32, 'max-payload'), ['int'])),
                                    ('host_uniq', (YLeaf(YType.str, 'host-uniq'), ['str'])),
                                    ('relay_session_id', (YLeaf(YType.str, 'relay-session-id'), ['str'])),
                                    ('remote_id', (YLeaf(YType.str, 'remote-id'), ['str'])),
                                    ('circuit_id', (YLeaf(YType.str, 'circuit-id'), ['str'])),
                                    ('is_dsl_actual_up', (YLeaf(YType.int32, 'is-dsl-actual-up'), ['int'])),
                                    ('is_dsl_actual_down', (YLeaf(YType.int32, 'is-dsl-actual-down'), ['int'])),
                                    ('is_dsl_min_up', (YLeaf(YType.int32, 'is-dsl-min-up'), ['int'])),
                                    ('is_dsl_min_down', (YLeaf(YType.int32, 'is-dsl-min-down'), ['int'])),
                                    ('is_dsl_attain_up', (YLeaf(YType.int32, 'is-dsl-attain-up'), ['int'])),
                                    ('is_dsl_attain_down', (YLeaf(YType.int32, 'is-dsl-attain-down'), ['int'])),
                                    ('is_dsl_max_up', (YLeaf(YType.int32, 'is-dsl-max-up'), ['int'])),
                                    ('is_dsl_max_down', (YLeaf(YType.int32, 'is-dsl-max-down'), ['int'])),
                                    ('is_dsl_min_up_low', (YLeaf(YType.int32, 'is-dsl-min-up-low'), ['int'])),
                                    ('is_dsl_min_down_low', (YLeaf(YType.int32, 'is-dsl-min-down-low'), ['int'])),
                                    ('is_dsl_max_delay_up', (YLeaf(YType.int32, 'is-dsl-max-delay-up'), ['int'])),
                                    ('is_dsl_actual_delay_up', (YLeaf(YType.int32, 'is-dsl-actual-delay-up'), ['int'])),
                                    ('is_dsl_max_delay_down', (YLeaf(YType.int32, 'is-dsl-max-delay-down'), ['int'])),
                                    ('is_dsl_actual_delay_down', (YLeaf(YType.int32, 'is-dsl-actual-delay-down'), ['int'])),
                                    ('is_access_loop_encapsulation', (YLeaf(YType.int32, 'is-access-loop-encapsulation'), ['int'])),
                                    ('dsl_actual_up', (YLeaf(YType.uint32, 'dsl-actual-up'), ['int'])),
                                    ('dsl_actual_down', (YLeaf(YType.uint32, 'dsl-actual-down'), ['int'])),
                                    ('dsl_min_up', (YLeaf(YType.uint32, 'dsl-min-up'), ['int'])),
                                    ('dsl_min_down', (YLeaf(YType.uint32, 'dsl-min-down'), ['int'])),
                                    ('dsl_attain_up', (YLeaf(YType.uint32, 'dsl-attain-up'), ['int'])),
                                    ('dsl_attain_down', (YLeaf(YType.uint32, 'dsl-attain-down'), ['int'])),
                                    ('dsl_max_up', (YLeaf(YType.uint32, 'dsl-max-up'), ['int'])),
                                    ('dsl_max_down', (YLeaf(YType.uint32, 'dsl-max-down'), ['int'])),
                                    ('dsl_min_up_low', (YLeaf(YType.uint32, 'dsl-min-up-low'), ['int'])),
                                    ('dsl_min_down_low', (YLeaf(YType.uint32, 'dsl-min-down-low'), ['int'])),
                                    ('dsl_max_delay_up', (YLeaf(YType.uint32, 'dsl-max-delay-up'), ['int'])),
                                    ('dsl_actual_delay_up', (YLeaf(YType.uint32, 'dsl-actual-delay-up'), ['int'])),
                                    ('dsl_max_delay_down', (YLeaf(YType.uint32, 'dsl-max-delay-down'), ['int'])),
                                    ('dsl_actual_delay_down', (YLeaf(YType.uint32, 'dsl-actual-delay-down'), ['int'])),
                                ])
                                self.is_service_name = None
                                self.is_max_payload = None
                                self.is_host_uniq = None
                                self.is_relay_session_id = None
                                self.is_vendor_specific = None
                                self.is_iwf = None
                                self.is_remote_id = None
                                self.is_circuit_id = None
                                self.is_dsl_tag = None
                                self.service_name = None
                                self.max_payload = None
                                self.host_uniq = None
                                self.relay_session_id = None
                                self.remote_id = None
                                self.circuit_id = None
                                self.is_dsl_actual_up = None
                                self.is_dsl_actual_down = None
                                self.is_dsl_min_up = None
                                self.is_dsl_min_down = None
                                self.is_dsl_attain_up = None
                                self.is_dsl_attain_down = None
                                self.is_dsl_max_up = None
                                self.is_dsl_max_down = None
                                self.is_dsl_min_up_low = None
                                self.is_dsl_min_down_low = None
                                self.is_dsl_max_delay_up = None
                                self.is_dsl_actual_delay_up = None
                                self.is_dsl_max_delay_down = None
                                self.is_dsl_actual_delay_down = None
                                self.is_access_loop_encapsulation = None
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

                                self.access_loop_encapsulation = Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.Tags.AccessLoopEncapsulation()
                                self.access_loop_encapsulation.parent = self
                                self._children_name_map["access_loop_encapsulation"] = "access-loop-encapsulation"
                                self._segment_path = lambda: "tags"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.Tags, [u'is_service_name', u'is_max_payload', u'is_host_uniq', u'is_relay_session_id', u'is_vendor_specific', u'is_iwf', u'is_remote_id', u'is_circuit_id', u'is_dsl_tag', u'service_name', u'max_payload', u'host_uniq', u'relay_session_id', u'remote_id', u'circuit_id', u'is_dsl_actual_up', u'is_dsl_actual_down', u'is_dsl_min_up', u'is_dsl_min_down', u'is_dsl_attain_up', u'is_dsl_attain_down', u'is_dsl_max_up', u'is_dsl_max_down', u'is_dsl_min_up_low', u'is_dsl_min_down_low', u'is_dsl_max_delay_up', u'is_dsl_actual_delay_up', u'is_dsl_max_delay_down', u'is_dsl_actual_delay_down', u'is_access_loop_encapsulation', u'dsl_actual_up', u'dsl_actual_down', u'dsl_min_up', u'dsl_min_down', u'dsl_attain_up', u'dsl_attain_down', u'dsl_max_up', u'dsl_max_down', u'dsl_min_up_low', u'dsl_min_down_low', u'dsl_max_delay_up', u'dsl_actual_delay_up', u'dsl_max_delay_down', u'dsl_actual_delay_down'], name, value)


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
                                    super(Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.Tags.AccessLoopEncapsulation, self).__init__()

                                    self.yang_name = "access-loop-encapsulation"
                                    self.yang_parent_name = "tags"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('data_link', (YLeaf(YType.uint8, 'data-link'), ['int'])),
                                        ('encaps1', (YLeaf(YType.uint8, 'encaps1'), ['int'])),
                                        ('encaps2', (YLeaf(YType.uint8, 'encaps2'), ['int'])),
                                    ])
                                    self.data_link = None
                                    self.encaps1 = None
                                    self.encaps2 = None
                                    self._segment_path = lambda: "access-loop-encapsulation"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.Tags.AccessLoopEncapsulation, [u'data_link', u'encaps1', u'encaps2'], name, value)


                        class VlanOuterTag(Entity):
                            """
                            VLAN Outer Tag
                            
                            .. attribute:: ether_type
                            
                            	Ethertype. See IEEE 802.1Q for more information
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: user_priority
                            
                            	User Priority
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: cfi
                            
                            	CFI
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: vlan_id
                            
                            	VLAN ID
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.VlanOuterTag, self).__init__()

                                self.yang_name = "vlan-outer-tag"
                                self.yang_parent_name = "session-idb"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ether_type', (YLeaf(YType.uint16, 'ether-type'), ['int'])),
                                    ('user_priority', (YLeaf(YType.uint8, 'user-priority'), ['int'])),
                                    ('cfi', (YLeaf(YType.uint8, 'cfi'), ['int'])),
                                    ('vlan_id', (YLeaf(YType.uint16, 'vlan-id'), ['int'])),
                                ])
                                self.ether_type = None
                                self.user_priority = None
                                self.cfi = None
                                self.vlan_id = None
                                self._segment_path = lambda: "vlan-outer-tag"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.VlanOuterTag, [u'ether_type', u'user_priority', u'cfi', u'vlan_id'], name, value)


                        class VlanInnerTag(Entity):
                            """
                            VLAN Inner Tag
                            
                            .. attribute:: ether_type
                            
                            	Ethertype. See IEEE 802.1Q for more information
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: user_priority
                            
                            	User Priority
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: cfi
                            
                            	CFI
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: vlan_id
                            
                            	VLAN ID
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.VlanInnerTag, self).__init__()

                                self.yang_name = "vlan-inner-tag"
                                self.yang_parent_name = "session-idb"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ether_type', (YLeaf(YType.uint16, 'ether-type'), ['int'])),
                                    ('user_priority', (YLeaf(YType.uint8, 'user-priority'), ['int'])),
                                    ('cfi', (YLeaf(YType.uint8, 'cfi'), ['int'])),
                                    ('vlan_id', (YLeaf(YType.uint16, 'vlan-id'), ['int'])),
                                ])
                                self.ether_type = None
                                self.user_priority = None
                                self.cfi = None
                                self.vlan_id = None
                                self._segment_path = lambda: "vlan-inner-tag"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.VlanInnerTag, [u'ether_type', u'user_priority', u'cfi', u'vlan_id'], name, value)


            class DisconnectHistoryUnique(Entity):
                """
                PPPoE unique disconnect history for a given
                node
                
                .. attribute:: disconnect_count
                
                	The total number of disconnects
                	**type**\: list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: entry
                
                	Array of disconnected subscribers
                	**type**\: list of  		 :py:class:`Entry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry>`
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Pppoe.Nodes.Node.DisconnectHistoryUnique, self).__init__()

                    self.yang_name = "disconnect-history-unique"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("entry", ("entry", Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry))])
                    self._leafs = OrderedDict([
                        ('disconnect_count', (YLeafList(YType.uint32, 'disconnect-count'), ['int'])),
                    ])
                    self.disconnect_count = []

                    self.entry = YList(self)
                    self._segment_path = lambda: "disconnect-history-unique"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistoryUnique, [u'disconnect_count'], name, value)


                class Entry(Entity):
                    """
                    Array of disconnected subscribers
                    
                    .. attribute:: session_idb
                    
                    	Session IDB
                    	**type**\:  :py:class:`SessionIdb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb>`
                    
                    .. attribute:: timestamp
                    
                    	Time when disconnected
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ifname
                    
                    	Interface name
                    	**type**\: str
                    
                    .. attribute:: trigger
                    
                    	Disconnect Trigger
                    	**type**\:  :py:class:`PppoeMaSessionTrig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.PppoeMaSessionTrig>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry, self).__init__()

                        self.yang_name = "entry"
                        self.yang_parent_name = "disconnect-history-unique"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("session-idb", ("session_idb", Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb))])
                        self._leafs = OrderedDict([
                            ('timestamp', (YLeaf(YType.uint64, 'timestamp'), ['int'])),
                            ('ifname', (YLeaf(YType.str, 'ifname'), ['str'])),
                            ('trigger', (YLeaf(YType.enumeration, 'trigger'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'PppoeMaSessionTrig', '')])),
                        ])
                        self.timestamp = None
                        self.ifname = None
                        self.trigger = None

                        self.session_idb = Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb()
                        self.session_idb.parent = self
                        self._children_name_map["session_idb"] = "session-idb"
                        self._segment_path = lambda: "entry"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry, [u'timestamp', u'ifname', u'trigger'], name, value)


                    class SessionIdb(Entity):
                        """
                        Session IDB
                        
                        .. attribute:: tags
                        
                        	Tags
                        	**type**\:  :py:class:`Tags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.Tags>`
                        
                        .. attribute:: vlan_outer_tag
                        
                        	VLAN Outer Tag
                        	**type**\:  :py:class:`VlanOuterTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.VlanOuterTag>`
                        
                        .. attribute:: vlan_inner_tag
                        
                        	VLAN Inner Tag
                        	**type**\:  :py:class:`VlanInnerTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.VlanInnerTag>`
                        
                        .. attribute:: interface
                        
                        	Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: access_interface
                        
                        	Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: session_id
                        
                        	Session ID
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: sub_label
                        
                        	Sub Label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: peer_mac_address
                        
                        	Peer Mac\-Address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: state
                        
                        	State
                        	**type**\:  :py:class:`PppoeMaSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.PppoeMaSessionState>`
                        
                        .. attribute:: cdm_object_handle
                        
                        	CDM Object Handle
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: chkpt_id
                        
                        	Chkpt ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: punted_count
                        
                        	Punted Count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: port_limit
                        
                        	Port Limit
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_counted
                        
                        	Is BBA Counted
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_vlan_outer_tag
                        
                        	Is VLAN Outer Tag
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_vlan_inner_tag
                        
                        	Is VLAN Inner Tag
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_cleanup_pending
                        
                        	Is Cleanup Pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_disconnect_done_pending
                        
                        	Is Disconnect Done Pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_delete_done_pending
                        
                        	Is Delete Done Pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_intf_create_callback_pending
                        
                        	Is Interface Create Callback pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_publish_encaps_attr_pending
                        
                        	Is Publish Encaps Attr pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_publish_encaps_attr_cb_pending
                        
                        	Is Publish Encaps Attr Callback pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_intf_delete_callback_pending
                        
                        	Is Interface Delete Callback pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_intf_delete_pending
                        
                        	Is Interface Delete pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_im_owned_resource
                        
                        	Is IM Owned Resource
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_im_final_received
                        
                        	Is IM Final received
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_im_owned_resource_missing
                        
                        	Is IM Owned Resource missing
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_aaa_start_request_callback_pending
                        
                        	Is AAA Start request callback pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_aaa_owned_resource
                        
                        	Is AAA Owned Resource
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_aaa_disconnect_requested
                        
                        	Is AAA Disconnect Requested
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_aaa_disconnect_received
                        
                        	Is AAA Disconnect Received
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_sub_db_activate_callback_pending
                        
                        	Is SubDB Activate callback pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_pads_sent
                        
                        	Is PADS Sent
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_padt_received
                        
                        	Is PADT Received
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_in_flight
                        
                        	Is Session In Flight
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_radius_override
                        
                        	Is RADIUS override enabled
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: expected_notifications
                        
                        	Expected Notifications
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: received_notifications
                        
                        	Received Notifications
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: srg_state
                        
                        	SRG state
                        	**type**\:  :py:class:`PppoeMaSessionIdbSrgState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.PppoeMaSessionIdbSrgState>`
                        
                        .. attribute:: is_srg_data_received
                        
                        	Is SRG Data Received
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_iedge_data_received
                        
                        	Is IEDGE Data Received
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb, self).__init__()

                            self.yang_name = "session-idb"
                            self.yang_parent_name = "entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("tags", ("tags", Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.Tags)), ("vlan-outer-tag", ("vlan_outer_tag", Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.VlanOuterTag)), ("vlan-inner-tag", ("vlan_inner_tag", Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.VlanInnerTag))])
                            self._leafs = OrderedDict([
                                ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                ('access_interface', (YLeaf(YType.str, 'access-interface'), ['str'])),
                                ('session_id', (YLeaf(YType.uint16, 'session-id'), ['int'])),
                                ('sub_label', (YLeaf(YType.uint32, 'sub-label'), ['int'])),
                                ('peer_mac_address', (YLeaf(YType.str, 'peer-mac-address'), ['str'])),
                                ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'PppoeMaSessionState', '')])),
                                ('cdm_object_handle', (YLeaf(YType.uint32, 'cdm-object-handle'), ['int'])),
                                ('chkpt_id', (YLeaf(YType.uint32, 'chkpt-id'), ['int'])),
                                ('punted_count', (YLeaf(YType.uint32, 'punted-count'), ['int'])),
                                ('port_limit', (YLeaf(YType.uint32, 'port-limit'), ['int'])),
                                ('is_counted', (YLeaf(YType.int32, 'is-counted'), ['int'])),
                                ('is_vlan_outer_tag', (YLeaf(YType.int32, 'is-vlan-outer-tag'), ['int'])),
                                ('is_vlan_inner_tag', (YLeaf(YType.int32, 'is-vlan-inner-tag'), ['int'])),
                                ('is_cleanup_pending', (YLeaf(YType.int32, 'is-cleanup-pending'), ['int'])),
                                ('is_disconnect_done_pending', (YLeaf(YType.int32, 'is-disconnect-done-pending'), ['int'])),
                                ('is_delete_done_pending', (YLeaf(YType.int32, 'is-delete-done-pending'), ['int'])),
                                ('is_intf_create_callback_pending', (YLeaf(YType.int32, 'is-intf-create-callback-pending'), ['int'])),
                                ('is_publish_encaps_attr_pending', (YLeaf(YType.int32, 'is-publish-encaps-attr-pending'), ['int'])),
                                ('is_publish_encaps_attr_cb_pending', (YLeaf(YType.int32, 'is-publish-encaps-attr-cb-pending'), ['int'])),
                                ('is_intf_delete_callback_pending', (YLeaf(YType.int32, 'is-intf-delete-callback-pending'), ['int'])),
                                ('is_intf_delete_pending', (YLeaf(YType.int32, 'is-intf-delete-pending'), ['int'])),
                                ('is_im_owned_resource', (YLeaf(YType.int32, 'is-im-owned-resource'), ['int'])),
                                ('is_im_final_received', (YLeaf(YType.int32, 'is-im-final-received'), ['int'])),
                                ('is_im_owned_resource_missing', (YLeaf(YType.int32, 'is-im-owned-resource-missing'), ['int'])),
                                ('is_aaa_start_request_callback_pending', (YLeaf(YType.int32, 'is-aaa-start-request-callback-pending'), ['int'])),
                                ('is_aaa_owned_resource', (YLeaf(YType.int32, 'is-aaa-owned-resource'), ['int'])),
                                ('is_aaa_disconnect_requested', (YLeaf(YType.int32, 'is-aaa-disconnect-requested'), ['int'])),
                                ('is_aaa_disconnect_received', (YLeaf(YType.int32, 'is-aaa-disconnect-received'), ['int'])),
                                ('is_sub_db_activate_callback_pending', (YLeaf(YType.int32, 'is-sub-db-activate-callback-pending'), ['int'])),
                                ('is_pads_sent', (YLeaf(YType.int32, 'is-pads-sent'), ['int'])),
                                ('is_padt_received', (YLeaf(YType.int32, 'is-padt-received'), ['int'])),
                                ('is_in_flight', (YLeaf(YType.int32, 'is-in-flight'), ['int'])),
                                ('is_radius_override', (YLeaf(YType.int32, 'is-radius-override'), ['int'])),
                                ('expected_notifications', (YLeaf(YType.uint8, 'expected-notifications'), ['int'])),
                                ('received_notifications', (YLeaf(YType.uint8, 'received-notifications'), ['int'])),
                                ('srg_state', (YLeaf(YType.enumeration, 'srg-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'PppoeMaSessionIdbSrgState', '')])),
                                ('is_srg_data_received', (YLeaf(YType.int32, 'is-srg-data-received'), ['int'])),
                                ('is_iedge_data_received', (YLeaf(YType.int32, 'is-iedge-data-received'), ['int'])),
                            ])
                            self.interface = None
                            self.access_interface = None
                            self.session_id = None
                            self.sub_label = None
                            self.peer_mac_address = None
                            self.state = None
                            self.cdm_object_handle = None
                            self.chkpt_id = None
                            self.punted_count = None
                            self.port_limit = None
                            self.is_counted = None
                            self.is_vlan_outer_tag = None
                            self.is_vlan_inner_tag = None
                            self.is_cleanup_pending = None
                            self.is_disconnect_done_pending = None
                            self.is_delete_done_pending = None
                            self.is_intf_create_callback_pending = None
                            self.is_publish_encaps_attr_pending = None
                            self.is_publish_encaps_attr_cb_pending = None
                            self.is_intf_delete_callback_pending = None
                            self.is_intf_delete_pending = None
                            self.is_im_owned_resource = None
                            self.is_im_final_received = None
                            self.is_im_owned_resource_missing = None
                            self.is_aaa_start_request_callback_pending = None
                            self.is_aaa_owned_resource = None
                            self.is_aaa_disconnect_requested = None
                            self.is_aaa_disconnect_received = None
                            self.is_sub_db_activate_callback_pending = None
                            self.is_pads_sent = None
                            self.is_padt_received = None
                            self.is_in_flight = None
                            self.is_radius_override = None
                            self.expected_notifications = None
                            self.received_notifications = None
                            self.srg_state = None
                            self.is_srg_data_received = None
                            self.is_iedge_data_received = None

                            self.tags = Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.Tags()
                            self.tags.parent = self
                            self._children_name_map["tags"] = "tags"

                            self.vlan_outer_tag = Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.VlanOuterTag()
                            self.vlan_outer_tag.parent = self
                            self._children_name_map["vlan_outer_tag"] = "vlan-outer-tag"

                            self.vlan_inner_tag = Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.VlanInnerTag()
                            self.vlan_inner_tag.parent = self
                            self._children_name_map["vlan_inner_tag"] = "vlan-inner-tag"
                            self._segment_path = lambda: "session-idb"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb, [u'interface', u'access_interface', u'session_id', u'sub_label', u'peer_mac_address', u'state', u'cdm_object_handle', u'chkpt_id', u'punted_count', u'port_limit', u'is_counted', u'is_vlan_outer_tag', u'is_vlan_inner_tag', u'is_cleanup_pending', u'is_disconnect_done_pending', u'is_delete_done_pending', u'is_intf_create_callback_pending', u'is_publish_encaps_attr_pending', u'is_publish_encaps_attr_cb_pending', u'is_intf_delete_callback_pending', u'is_intf_delete_pending', u'is_im_owned_resource', u'is_im_final_received', u'is_im_owned_resource_missing', u'is_aaa_start_request_callback_pending', u'is_aaa_owned_resource', u'is_aaa_disconnect_requested', u'is_aaa_disconnect_received', u'is_sub_db_activate_callback_pending', u'is_pads_sent', u'is_padt_received', u'is_in_flight', u'is_radius_override', u'expected_notifications', u'received_notifications', u'srg_state', u'is_srg_data_received', u'is_iedge_data_received'], name, value)


                        class Tags(Entity):
                            """
                            Tags
                            
                            .. attribute:: access_loop_encapsulation
                            
                            	Access Loop Encapsulation
                            	**type**\:  :py:class:`AccessLoopEncapsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.Tags.AccessLoopEncapsulation>`
                            
                            .. attribute:: is_service_name
                            
                            	Is Service Name
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_max_payload
                            
                            	Is Max Payload
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_host_uniq
                            
                            	Is Host Uniq
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_relay_session_id
                            
                            	Is Relay Session ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_vendor_specific
                            
                            	Is Vendor Specific
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_iwf
                            
                            	Is IWF
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_remote_id
                            
                            	Is Remote ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_circuit_id
                            
                            	Is Circuit ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_tag
                            
                            	Is DSL Tag
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: service_name
                            
                            	Service Name
                            	**type**\: str
                            
                            .. attribute:: max_payload
                            
                            	Max Payload
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
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
                            
                            .. attribute:: is_dsl_actual_up
                            
                            	Is DSL Actual Up
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_actual_down
                            
                            	Is DSL Actual Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_min_up
                            
                            	Is DSL Min Up
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_min_down
                            
                            	Is DSL Min Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_attain_up
                            
                            	Is DSL Attain Up
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_attain_down
                            
                            	Is DSL Attain Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_max_up
                            
                            	Is DSL Max Up
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_max_down
                            
                            	Is DSL Max Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_min_up_low
                            
                            	Is DSL Min Up Low
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_min_down_low
                            
                            	Is DSL Min Down Low
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_max_delay_up
                            
                            	Is DSL Max Delay Up
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_actual_delay_up
                            
                            	Is DSL Actual Delay Up
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_max_delay_down
                            
                            	Is DSL Max Delay Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_dsl_actual_delay_down
                            
                            	Is DSL Actual Delay Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_access_loop_encapsulation
                            
                            	Is Access Loop Encapsulation
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
                                super(Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.Tags, self).__init__()

                                self.yang_name = "tags"
                                self.yang_parent_name = "session-idb"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("access-loop-encapsulation", ("access_loop_encapsulation", Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.Tags.AccessLoopEncapsulation))])
                                self._leafs = OrderedDict([
                                    ('is_service_name', (YLeaf(YType.int32, 'is-service-name'), ['int'])),
                                    ('is_max_payload', (YLeaf(YType.int32, 'is-max-payload'), ['int'])),
                                    ('is_host_uniq', (YLeaf(YType.int32, 'is-host-uniq'), ['int'])),
                                    ('is_relay_session_id', (YLeaf(YType.int32, 'is-relay-session-id'), ['int'])),
                                    ('is_vendor_specific', (YLeaf(YType.int32, 'is-vendor-specific'), ['int'])),
                                    ('is_iwf', (YLeaf(YType.int32, 'is-iwf'), ['int'])),
                                    ('is_remote_id', (YLeaf(YType.int32, 'is-remote-id'), ['int'])),
                                    ('is_circuit_id', (YLeaf(YType.int32, 'is-circuit-id'), ['int'])),
                                    ('is_dsl_tag', (YLeaf(YType.int32, 'is-dsl-tag'), ['int'])),
                                    ('service_name', (YLeaf(YType.str, 'service-name'), ['str'])),
                                    ('max_payload', (YLeaf(YType.uint32, 'max-payload'), ['int'])),
                                    ('host_uniq', (YLeaf(YType.str, 'host-uniq'), ['str'])),
                                    ('relay_session_id', (YLeaf(YType.str, 'relay-session-id'), ['str'])),
                                    ('remote_id', (YLeaf(YType.str, 'remote-id'), ['str'])),
                                    ('circuit_id', (YLeaf(YType.str, 'circuit-id'), ['str'])),
                                    ('is_dsl_actual_up', (YLeaf(YType.int32, 'is-dsl-actual-up'), ['int'])),
                                    ('is_dsl_actual_down', (YLeaf(YType.int32, 'is-dsl-actual-down'), ['int'])),
                                    ('is_dsl_min_up', (YLeaf(YType.int32, 'is-dsl-min-up'), ['int'])),
                                    ('is_dsl_min_down', (YLeaf(YType.int32, 'is-dsl-min-down'), ['int'])),
                                    ('is_dsl_attain_up', (YLeaf(YType.int32, 'is-dsl-attain-up'), ['int'])),
                                    ('is_dsl_attain_down', (YLeaf(YType.int32, 'is-dsl-attain-down'), ['int'])),
                                    ('is_dsl_max_up', (YLeaf(YType.int32, 'is-dsl-max-up'), ['int'])),
                                    ('is_dsl_max_down', (YLeaf(YType.int32, 'is-dsl-max-down'), ['int'])),
                                    ('is_dsl_min_up_low', (YLeaf(YType.int32, 'is-dsl-min-up-low'), ['int'])),
                                    ('is_dsl_min_down_low', (YLeaf(YType.int32, 'is-dsl-min-down-low'), ['int'])),
                                    ('is_dsl_max_delay_up', (YLeaf(YType.int32, 'is-dsl-max-delay-up'), ['int'])),
                                    ('is_dsl_actual_delay_up', (YLeaf(YType.int32, 'is-dsl-actual-delay-up'), ['int'])),
                                    ('is_dsl_max_delay_down', (YLeaf(YType.int32, 'is-dsl-max-delay-down'), ['int'])),
                                    ('is_dsl_actual_delay_down', (YLeaf(YType.int32, 'is-dsl-actual-delay-down'), ['int'])),
                                    ('is_access_loop_encapsulation', (YLeaf(YType.int32, 'is-access-loop-encapsulation'), ['int'])),
                                    ('dsl_actual_up', (YLeaf(YType.uint32, 'dsl-actual-up'), ['int'])),
                                    ('dsl_actual_down', (YLeaf(YType.uint32, 'dsl-actual-down'), ['int'])),
                                    ('dsl_min_up', (YLeaf(YType.uint32, 'dsl-min-up'), ['int'])),
                                    ('dsl_min_down', (YLeaf(YType.uint32, 'dsl-min-down'), ['int'])),
                                    ('dsl_attain_up', (YLeaf(YType.uint32, 'dsl-attain-up'), ['int'])),
                                    ('dsl_attain_down', (YLeaf(YType.uint32, 'dsl-attain-down'), ['int'])),
                                    ('dsl_max_up', (YLeaf(YType.uint32, 'dsl-max-up'), ['int'])),
                                    ('dsl_max_down', (YLeaf(YType.uint32, 'dsl-max-down'), ['int'])),
                                    ('dsl_min_up_low', (YLeaf(YType.uint32, 'dsl-min-up-low'), ['int'])),
                                    ('dsl_min_down_low', (YLeaf(YType.uint32, 'dsl-min-down-low'), ['int'])),
                                    ('dsl_max_delay_up', (YLeaf(YType.uint32, 'dsl-max-delay-up'), ['int'])),
                                    ('dsl_actual_delay_up', (YLeaf(YType.uint32, 'dsl-actual-delay-up'), ['int'])),
                                    ('dsl_max_delay_down', (YLeaf(YType.uint32, 'dsl-max-delay-down'), ['int'])),
                                    ('dsl_actual_delay_down', (YLeaf(YType.uint32, 'dsl-actual-delay-down'), ['int'])),
                                ])
                                self.is_service_name = None
                                self.is_max_payload = None
                                self.is_host_uniq = None
                                self.is_relay_session_id = None
                                self.is_vendor_specific = None
                                self.is_iwf = None
                                self.is_remote_id = None
                                self.is_circuit_id = None
                                self.is_dsl_tag = None
                                self.service_name = None
                                self.max_payload = None
                                self.host_uniq = None
                                self.relay_session_id = None
                                self.remote_id = None
                                self.circuit_id = None
                                self.is_dsl_actual_up = None
                                self.is_dsl_actual_down = None
                                self.is_dsl_min_up = None
                                self.is_dsl_min_down = None
                                self.is_dsl_attain_up = None
                                self.is_dsl_attain_down = None
                                self.is_dsl_max_up = None
                                self.is_dsl_max_down = None
                                self.is_dsl_min_up_low = None
                                self.is_dsl_min_down_low = None
                                self.is_dsl_max_delay_up = None
                                self.is_dsl_actual_delay_up = None
                                self.is_dsl_max_delay_down = None
                                self.is_dsl_actual_delay_down = None
                                self.is_access_loop_encapsulation = None
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

                                self.access_loop_encapsulation = Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.Tags.AccessLoopEncapsulation()
                                self.access_loop_encapsulation.parent = self
                                self._children_name_map["access_loop_encapsulation"] = "access-loop-encapsulation"
                                self._segment_path = lambda: "tags"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.Tags, [u'is_service_name', u'is_max_payload', u'is_host_uniq', u'is_relay_session_id', u'is_vendor_specific', u'is_iwf', u'is_remote_id', u'is_circuit_id', u'is_dsl_tag', u'service_name', u'max_payload', u'host_uniq', u'relay_session_id', u'remote_id', u'circuit_id', u'is_dsl_actual_up', u'is_dsl_actual_down', u'is_dsl_min_up', u'is_dsl_min_down', u'is_dsl_attain_up', u'is_dsl_attain_down', u'is_dsl_max_up', u'is_dsl_max_down', u'is_dsl_min_up_low', u'is_dsl_min_down_low', u'is_dsl_max_delay_up', u'is_dsl_actual_delay_up', u'is_dsl_max_delay_down', u'is_dsl_actual_delay_down', u'is_access_loop_encapsulation', u'dsl_actual_up', u'dsl_actual_down', u'dsl_min_up', u'dsl_min_down', u'dsl_attain_up', u'dsl_attain_down', u'dsl_max_up', u'dsl_max_down', u'dsl_min_up_low', u'dsl_min_down_low', u'dsl_max_delay_up', u'dsl_actual_delay_up', u'dsl_max_delay_down', u'dsl_actual_delay_down'], name, value)


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
                                    super(Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.Tags.AccessLoopEncapsulation, self).__init__()

                                    self.yang_name = "access-loop-encapsulation"
                                    self.yang_parent_name = "tags"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('data_link', (YLeaf(YType.uint8, 'data-link'), ['int'])),
                                        ('encaps1', (YLeaf(YType.uint8, 'encaps1'), ['int'])),
                                        ('encaps2', (YLeaf(YType.uint8, 'encaps2'), ['int'])),
                                    ])
                                    self.data_link = None
                                    self.encaps1 = None
                                    self.encaps2 = None
                                    self._segment_path = lambda: "access-loop-encapsulation"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.Tags.AccessLoopEncapsulation, [u'data_link', u'encaps1', u'encaps2'], name, value)


                        class VlanOuterTag(Entity):
                            """
                            VLAN Outer Tag
                            
                            .. attribute:: ether_type
                            
                            	Ethertype. See IEEE 802.1Q for more information
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: user_priority
                            
                            	User Priority
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: cfi
                            
                            	CFI
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: vlan_id
                            
                            	VLAN ID
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.VlanOuterTag, self).__init__()

                                self.yang_name = "vlan-outer-tag"
                                self.yang_parent_name = "session-idb"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ether_type', (YLeaf(YType.uint16, 'ether-type'), ['int'])),
                                    ('user_priority', (YLeaf(YType.uint8, 'user-priority'), ['int'])),
                                    ('cfi', (YLeaf(YType.uint8, 'cfi'), ['int'])),
                                    ('vlan_id', (YLeaf(YType.uint16, 'vlan-id'), ['int'])),
                                ])
                                self.ether_type = None
                                self.user_priority = None
                                self.cfi = None
                                self.vlan_id = None
                                self._segment_path = lambda: "vlan-outer-tag"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.VlanOuterTag, [u'ether_type', u'user_priority', u'cfi', u'vlan_id'], name, value)


                        class VlanInnerTag(Entity):
                            """
                            VLAN Inner Tag
                            
                            .. attribute:: ether_type
                            
                            	Ethertype. See IEEE 802.1Q for more information
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: user_priority
                            
                            	User Priority
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: cfi
                            
                            	CFI
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: vlan_id
                            
                            	VLAN ID
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.VlanInnerTag, self).__init__()

                                self.yang_name = "vlan-inner-tag"
                                self.yang_parent_name = "session-idb"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ether_type', (YLeaf(YType.uint16, 'ether-type'), ['int'])),
                                    ('user_priority', (YLeaf(YType.uint8, 'user-priority'), ['int'])),
                                    ('cfi', (YLeaf(YType.uint8, 'cfi'), ['int'])),
                                    ('vlan_id', (YLeaf(YType.uint16, 'vlan-id'), ['int'])),
                                ])
                                self.ether_type = None
                                self.user_priority = None
                                self.cfi = None
                                self.vlan_id = None
                                self._segment_path = lambda: "vlan-inner-tag"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.VlanInnerTag, [u'ether_type', u'user_priority', u'cfi', u'vlan_id'], name, value)


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
                    self._child_classes = OrderedDict([("packet-counts", ("packet_counts", Pppoe.Nodes.Node.Statistics.PacketCounts)), ("packet-error-counts", ("packet_error_counts", Pppoe.Nodes.Node.Statistics.PacketErrorCounts))])
                    self._leafs = OrderedDict()

                    self.packet_counts = Pppoe.Nodes.Node.Statistics.PacketCounts()
                    self.packet_counts.parent = self
                    self._children_name_map["packet_counts"] = "packet-counts"

                    self.packet_error_counts = Pppoe.Nodes.Node.Statistics.PacketErrorCounts()
                    self.packet_error_counts.parent = self
                    self._children_name_map["packet_error_counts"] = "packet-error-counts"
                    self._segment_path = lambda: "statistics"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pppoe.Nodes.Node.Statistics, [], name, value)


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
                        self._child_classes = OrderedDict([("padi", ("padi", Pppoe.Nodes.Node.Statistics.PacketCounts.Padi)), ("pado", ("pado", Pppoe.Nodes.Node.Statistics.PacketCounts.Pado)), ("padr", ("padr", Pppoe.Nodes.Node.Statistics.PacketCounts.Padr)), ("pads-success", ("pads_success", Pppoe.Nodes.Node.Statistics.PacketCounts.PadsSuccess)), ("pads-error", ("pads_error", Pppoe.Nodes.Node.Statistics.PacketCounts.PadsError)), ("padt", ("padt", Pppoe.Nodes.Node.Statistics.PacketCounts.Padt)), ("session-state", ("session_state", Pppoe.Nodes.Node.Statistics.PacketCounts.SessionState)), ("other", ("other", Pppoe.Nodes.Node.Statistics.PacketCounts.Other))])
                        self._leafs = OrderedDict()

                        self.padi = Pppoe.Nodes.Node.Statistics.PacketCounts.Padi()
                        self.padi.parent = self
                        self._children_name_map["padi"] = "padi"

                        self.pado = Pppoe.Nodes.Node.Statistics.PacketCounts.Pado()
                        self.pado.parent = self
                        self._children_name_map["pado"] = "pado"

                        self.padr = Pppoe.Nodes.Node.Statistics.PacketCounts.Padr()
                        self.padr.parent = self
                        self._children_name_map["padr"] = "padr"

                        self.pads_success = Pppoe.Nodes.Node.Statistics.PacketCounts.PadsSuccess()
                        self.pads_success.parent = self
                        self._children_name_map["pads_success"] = "pads-success"

                        self.pads_error = Pppoe.Nodes.Node.Statistics.PacketCounts.PadsError()
                        self.pads_error.parent = self
                        self._children_name_map["pads_error"] = "pads-error"

                        self.padt = Pppoe.Nodes.Node.Statistics.PacketCounts.Padt()
                        self.padt.parent = self
                        self._children_name_map["padt"] = "padt"

                        self.session_state = Pppoe.Nodes.Node.Statistics.PacketCounts.SessionState()
                        self.session_state.parent = self
                        self._children_name_map["session_state"] = "session-state"

                        self.other = Pppoe.Nodes.Node.Statistics.PacketCounts.Other()
                        self.other.parent = self
                        self._children_name_map["other"] = "other"
                        self._segment_path = lambda: "packet-counts"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketCounts, [], name, value)


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
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sent', (YLeaf(YType.uint32, 'sent'), ['int'])),
                                ('received', (YLeaf(YType.uint32, 'received'), ['int'])),
                                ('dropped', (YLeaf(YType.uint32, 'dropped'), ['int'])),
                            ])
                            self.sent = None
                            self.received = None
                            self.dropped = None
                            self._segment_path = lambda: "padi"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketCounts.Padi, [u'sent', u'received', u'dropped'], name, value)


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
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sent', (YLeaf(YType.uint32, 'sent'), ['int'])),
                                ('received', (YLeaf(YType.uint32, 'received'), ['int'])),
                                ('dropped', (YLeaf(YType.uint32, 'dropped'), ['int'])),
                            ])
                            self.sent = None
                            self.received = None
                            self.dropped = None
                            self._segment_path = lambda: "pado"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketCounts.Pado, [u'sent', u'received', u'dropped'], name, value)


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
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sent', (YLeaf(YType.uint32, 'sent'), ['int'])),
                                ('received', (YLeaf(YType.uint32, 'received'), ['int'])),
                                ('dropped', (YLeaf(YType.uint32, 'dropped'), ['int'])),
                            ])
                            self.sent = None
                            self.received = None
                            self.dropped = None
                            self._segment_path = lambda: "padr"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketCounts.Padr, [u'sent', u'received', u'dropped'], name, value)


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
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sent', (YLeaf(YType.uint32, 'sent'), ['int'])),
                                ('received', (YLeaf(YType.uint32, 'received'), ['int'])),
                                ('dropped', (YLeaf(YType.uint32, 'dropped'), ['int'])),
                            ])
                            self.sent = None
                            self.received = None
                            self.dropped = None
                            self._segment_path = lambda: "pads-success"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketCounts.PadsSuccess, [u'sent', u'received', u'dropped'], name, value)


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
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sent', (YLeaf(YType.uint32, 'sent'), ['int'])),
                                ('received', (YLeaf(YType.uint32, 'received'), ['int'])),
                                ('dropped', (YLeaf(YType.uint32, 'dropped'), ['int'])),
                            ])
                            self.sent = None
                            self.received = None
                            self.dropped = None
                            self._segment_path = lambda: "pads-error"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketCounts.PadsError, [u'sent', u'received', u'dropped'], name, value)


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
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sent', (YLeaf(YType.uint32, 'sent'), ['int'])),
                                ('received', (YLeaf(YType.uint32, 'received'), ['int'])),
                                ('dropped', (YLeaf(YType.uint32, 'dropped'), ['int'])),
                            ])
                            self.sent = None
                            self.received = None
                            self.dropped = None
                            self._segment_path = lambda: "padt"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketCounts.Padt, [u'sent', u'received', u'dropped'], name, value)


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
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sent', (YLeaf(YType.uint32, 'sent'), ['int'])),
                                ('received', (YLeaf(YType.uint32, 'received'), ['int'])),
                                ('dropped', (YLeaf(YType.uint32, 'dropped'), ['int'])),
                            ])
                            self.sent = None
                            self.received = None
                            self.dropped = None
                            self._segment_path = lambda: "session-state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketCounts.SessionState, [u'sent', u'received', u'dropped'], name, value)


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
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sent', (YLeaf(YType.uint32, 'sent'), ['int'])),
                                ('received', (YLeaf(YType.uint32, 'received'), ['int'])),
                                ('dropped', (YLeaf(YType.uint32, 'dropped'), ['int'])),
                            ])
                            self.sent = None
                            self.received = None
                            self.dropped = None
                            self._segment_path = lambda: "other"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketCounts.Other, [u'sent', u'received', u'dropped'], name, value)


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
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('no_interface_handle', (YLeaf(YType.uint32, 'no-interface-handle'), ['int'])),
                            ('no_packet_payload', (YLeaf(YType.uint32, 'no-packet-payload'), ['int'])),
                            ('no_packet_mac_address', (YLeaf(YType.uint32, 'no-packet-mac-address'), ['int'])),
                            ('invalid_version_type_value', (YLeaf(YType.uint32, 'invalid-version-type-value'), ['int'])),
                            ('bad_packet_length', (YLeaf(YType.uint32, 'bad-packet-length'), ['int'])),
                            ('unknown_interface', (YLeaf(YType.uint32, 'unknown-interface'), ['int'])),
                            ('pado_received', (YLeaf(YType.uint32, 'pado-received'), ['int'])),
                            ('pads_received', (YLeaf(YType.uint32, 'pads-received'), ['int'])),
                            ('unknown_packet_type_received', (YLeaf(YType.uint32, 'unknown-packet-type-received'), ['int'])),
                            ('unexpected_session_id_in_packet', (YLeaf(YType.uint32, 'unexpected-session-id-in-packet'), ['int'])),
                            ('no_service_name_tag', (YLeaf(YType.uint32, 'no-service-name-tag'), ['int'])),
                            ('padt_for_unknown_session', (YLeaf(YType.uint32, 'padt-for-unknown-session'), ['int'])),
                            ('padt_with_wrong_peer_mac', (YLeaf(YType.uint32, 'padt-with-wrong-peer-mac'), ['int'])),
                            ('padt_with_wrong_vlan_tags', (YLeaf(YType.uint32, 'padt-with-wrong-vlan-tags'), ['int'])),
                            ('zero_length_host_uniq', (YLeaf(YType.uint32, 'zero-length-host-uniq'), ['int'])),
                            ('padt_before_pads_sent', (YLeaf(YType.uint32, 'padt-before-pads-sent'), ['int'])),
                            ('session_stage_packet_for_unknown_session', (YLeaf(YType.uint32, 'session-stage-packet-for-unknown-session'), ['int'])),
                            ('session_stage_packet_with_wrong_mac', (YLeaf(YType.uint32, 'session-stage-packet-with-wrong-mac'), ['int'])),
                            ('session_stage_packet_with_wrong_vlan_tags', (YLeaf(YType.uint32, 'session-stage-packet-with-wrong-vlan-tags'), ['int'])),
                            ('session_stage_packet_with_no_error', (YLeaf(YType.uint32, 'session-stage-packet-with-no-error'), ['int'])),
                            ('tag_too_short', (YLeaf(YType.uint32, 'tag-too-short'), ['int'])),
                            ('bad_tag_length_field', (YLeaf(YType.uint32, 'bad-tag-length-field'), ['int'])),
                            ('multiple_service_name_tags', (YLeaf(YType.uint32, 'multiple-service-name-tags'), ['int'])),
                            ('multiple_max_payload_tags', (YLeaf(YType.uint32, 'multiple-max-payload-tags'), ['int'])),
                            ('invalid_max_payload_tag', (YLeaf(YType.uint32, 'invalid-max-payload-tag'), ['int'])),
                            ('multiple_vendor_specific_tags', (YLeaf(YType.uint32, 'multiple-vendor-specific-tags'), ['int'])),
                            ('unexpected_ac_name_tag', (YLeaf(YType.uint32, 'unexpected-ac-name-tag'), ['int'])),
                            ('unexpected_error_tags', (YLeaf(YType.uint32, 'unexpected-error-tags'), ['int'])),
                            ('unknown_tag_received', (YLeaf(YType.uint32, 'unknown-tag-received'), ['int'])),
                            ('no_iana_code_invendor_tag', (YLeaf(YType.uint32, 'no-iana-code-invendor-tag'), ['int'])),
                            ('invalid_iana_code_invendor_tag', (YLeaf(YType.uint32, 'invalid-iana-code-invendor-tag'), ['int'])),
                            ('vendor_tag_too_short', (YLeaf(YType.uint32, 'vendor-tag-too-short'), ['int'])),
                            ('bad_vendor_tag_length_field', (YLeaf(YType.uint32, 'bad-vendor-tag-length-field'), ['int'])),
                            ('multiple_host_uniq_tags', (YLeaf(YType.uint32, 'multiple-host-uniq-tags'), ['int'])),
                            ('multiple_relay_session_id_tags', (YLeaf(YType.uint32, 'multiple-relay-session-id-tags'), ['int'])),
                            ('multiple_circuit_id_tags', (YLeaf(YType.uint32, 'multiple-circuit-id-tags'), ['int'])),
                            ('multiple_remote_id_tags', (YLeaf(YType.uint32, 'multiple-remote-id-tags'), ['int'])),
                            ('invalid_dsl_tag', (YLeaf(YType.uint32, 'invalid-dsl-tag'), ['int'])),
                            ('multiple_of_the_same_dsl_tag', (YLeaf(YType.uint32, 'multiple-of-the-same-dsl-tag'), ['int'])),
                            ('invalid_iwf_tag', (YLeaf(YType.uint32, 'invalid-iwf-tag'), ['int'])),
                            ('multiple_iwf_tags', (YLeaf(YType.uint32, 'multiple-iwf-tags'), ['int'])),
                            ('unknownvendor_tag', (YLeaf(YType.uint32, 'unknownvendor-tag'), ['int'])),
                            ('no_space_left_in_packet', (YLeaf(YType.uint32, 'no-space-left-in-packet'), ['int'])),
                            ('duplicate_host_uniq_tag_received', (YLeaf(YType.uint32, 'duplicate-host-uniq-tag-received'), ['int'])),
                            ('duplicate_relay_session_id_tag_received', (YLeaf(YType.uint32, 'duplicate-relay-session-id-tag-received'), ['int'])),
                            ('packet_too_long', (YLeaf(YType.uint32, 'packet-too-long'), ['int'])),
                            ('invalid_ale_tag', (YLeaf(YType.uint32, 'invalid-ale-tag'), ['int'])),
                            ('multiple_ale_tags', (YLeaf(YType.uint32, 'multiple-ale-tags'), ['int'])),
                            ('invalid_service_name', (YLeaf(YType.uint32, 'invalid-service-name'), ['int'])),
                            ('invalid_peer_mac', (YLeaf(YType.uint32, 'invalid-peer-mac'), ['int'])),
                            ('invalid_vlan_tags', (YLeaf(YType.uint32, 'invalid-vlan-tags'), ['int'])),
                            ('packet_on_srg_slave', (YLeaf(YType.uint32, 'packet-on-srg-slave'), ['int'])),
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
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketErrorCounts, [u'no_interface_handle', u'no_packet_payload', u'no_packet_mac_address', u'invalid_version_type_value', u'bad_packet_length', u'unknown_interface', u'pado_received', u'pads_received', u'unknown_packet_type_received', u'unexpected_session_id_in_packet', u'no_service_name_tag', u'padt_for_unknown_session', u'padt_with_wrong_peer_mac', u'padt_with_wrong_vlan_tags', u'zero_length_host_uniq', u'padt_before_pads_sent', u'session_stage_packet_for_unknown_session', u'session_stage_packet_with_wrong_mac', u'session_stage_packet_with_wrong_vlan_tags', u'session_stage_packet_with_no_error', u'tag_too_short', u'bad_tag_length_field', u'multiple_service_name_tags', u'multiple_max_payload_tags', u'invalid_max_payload_tag', u'multiple_vendor_specific_tags', u'unexpected_ac_name_tag', u'unexpected_error_tags', u'unknown_tag_received', u'no_iana_code_invendor_tag', u'invalid_iana_code_invendor_tag', u'vendor_tag_too_short', u'bad_vendor_tag_length_field', u'multiple_host_uniq_tags', u'multiple_relay_session_id_tags', u'multiple_circuit_id_tags', u'multiple_remote_id_tags', u'invalid_dsl_tag', u'multiple_of_the_same_dsl_tag', u'invalid_iwf_tag', u'multiple_iwf_tags', u'unknownvendor_tag', u'no_space_left_in_packet', u'duplicate_host_uniq_tag_received', u'duplicate_relay_session_id_tag_received', u'packet_too_long', u'invalid_ale_tag', u'multiple_ale_tags', u'invalid_service_name', u'invalid_peer_mac', u'invalid_vlan_tags', u'packet_on_srg_slave'], name, value)


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
                    self._child_classes = OrderedDict([("summaries", ("summaries", Pppoe.Nodes.Node.AccessInterface.Summaries))])
                    self._leafs = OrderedDict()

                    self.summaries = Pppoe.Nodes.Node.AccessInterface.Summaries()
                    self.summaries.parent = self
                    self._children_name_map["summaries"] = "summaries"
                    self._segment_path = lambda: "access-interface"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pppoe.Nodes.Node.AccessInterface, [], name, value)


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
                        self._child_classes = OrderedDict([("summary", ("summary", Pppoe.Nodes.Node.AccessInterface.Summaries.Summary))])
                        self._leafs = OrderedDict()

                        self.summary = YList(self)
                        self._segment_path = lambda: "summaries"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.Nodes.Node.AccessInterface.Summaries, [], name, value)


                    class Summary(Entity):
                        """
                        Summary information for a PPPoE\-enabled
                        access interface
                        
                        .. attribute:: interface_name  (key)
                        
                        	PPPoE Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: interface_name_xr
                        
                        	Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
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
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('interface_name_xr', (YLeaf(YType.str, 'interface-name-xr'), ['str'])),
                                ('interface_state', (YLeaf(YType.uint32, 'interface-state'), ['int'])),
                                ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                ('bba_group_name', (YLeaf(YType.str, 'bba-group-name'), ['str'])),
                                ('is_ready', (YLeaf(YType.int32, 'is-ready'), ['int'])),
                                ('sessions', (YLeaf(YType.uint32, 'sessions'), ['int'])),
                                ('incomplete_sessions', (YLeaf(YType.uint32, 'incomplete-sessions'), ['int'])),
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
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.AccessInterface.Summaries.Summary, ['interface_name', u'interface_name_xr', u'interface_state', u'mac_address', u'bba_group_name', u'is_ready', u'sessions', u'incomplete_sessions'], name, value)


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
                    self._child_classes = OrderedDict([("interface", ("interface", Pppoe.Nodes.Node.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pppoe.Nodes.Node.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    Data for a PPPoE interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	PPPoE Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: tags
                    
                    	Tags
                    	**type**\:  :py:class:`Tags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Interfaces.Interface.Tags>`
                    
                    .. attribute:: interface_name_xr
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: access_interface_name
                    
                    	Access Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
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
                        self._child_classes = OrderedDict([("tags", ("tags", Pppoe.Nodes.Node.Interfaces.Interface.Tags))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('interface_name_xr', (YLeaf(YType.str, 'interface-name-xr'), ['str'])),
                            ('access_interface_name', (YLeaf(YType.str, 'access-interface-name'), ['str'])),
                            ('bba_group_name', (YLeaf(YType.str, 'bba-group-name'), ['str'])),
                            ('session_id', (YLeaf(YType.uint16, 'session-id'), ['int'])),
                            ('local_mac_address', (YLeaf(YType.str, 'local-mac-address'), ['str'])),
                            ('peer_mac_address', (YLeaf(YType.str, 'peer-mac-address'), ['str'])),
                            ('is_complete', (YLeaf(YType.int32, 'is-complete'), ['int'])),
                            ('vlan_outer_id', (YLeaf(YType.uint16, 'vlan-outer-id'), ['int'])),
                            ('vlan_inner_id', (YLeaf(YType.uint16, 'vlan-inner-id'), ['int'])),
                            ('srg_state', (YLeaf(YType.enumeration, 'srg-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'PppoeMaSessionIdbSrgState', '')])),
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
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pppoe.Nodes.Node.Interfaces.Interface, ['interface_name', u'interface_name_xr', u'access_interface_name', u'bba_group_name', u'session_id', u'local_mac_address', u'peer_mac_address', u'is_complete', u'vlan_outer_id', u'vlan_inner_id', u'srg_state'], name, value)


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
                            self._child_classes = OrderedDict([("access-loop-encapsulation", ("access_loop_encapsulation", Pppoe.Nodes.Node.Interfaces.Interface.Tags.AccessLoopEncapsulation))])
                            self._leafs = OrderedDict([
                                ('service_name', (YLeaf(YType.str, 'service-name'), ['str'])),
                                ('max_payload', (YLeaf(YType.uint16, 'max-payload'), ['int'])),
                                ('host_uniq', (YLeaf(YType.str, 'host-uniq'), ['str'])),
                                ('relay_session_id', (YLeaf(YType.str, 'relay-session-id'), ['str'])),
                                ('remote_id', (YLeaf(YType.str, 'remote-id'), ['str'])),
                                ('circuit_id', (YLeaf(YType.str, 'circuit-id'), ['str'])),
                                ('is_iwf', (YLeaf(YType.int32, 'is-iwf'), ['int'])),
                                ('dsl_actual_up', (YLeaf(YType.uint32, 'dsl-actual-up'), ['int'])),
                                ('dsl_actual_down', (YLeaf(YType.uint32, 'dsl-actual-down'), ['int'])),
                                ('dsl_min_up', (YLeaf(YType.uint32, 'dsl-min-up'), ['int'])),
                                ('dsl_min_down', (YLeaf(YType.uint32, 'dsl-min-down'), ['int'])),
                                ('dsl_attain_up', (YLeaf(YType.uint32, 'dsl-attain-up'), ['int'])),
                                ('dsl_attain_down', (YLeaf(YType.uint32, 'dsl-attain-down'), ['int'])),
                                ('dsl_max_up', (YLeaf(YType.uint32, 'dsl-max-up'), ['int'])),
                                ('dsl_max_down', (YLeaf(YType.uint32, 'dsl-max-down'), ['int'])),
                                ('dsl_min_up_low', (YLeaf(YType.uint32, 'dsl-min-up-low'), ['int'])),
                                ('dsl_min_down_low', (YLeaf(YType.uint32, 'dsl-min-down-low'), ['int'])),
                                ('dsl_max_delay_up', (YLeaf(YType.uint32, 'dsl-max-delay-up'), ['int'])),
                                ('dsl_actual_delay_up', (YLeaf(YType.uint32, 'dsl-actual-delay-up'), ['int'])),
                                ('dsl_max_delay_down', (YLeaf(YType.uint32, 'dsl-max-delay-down'), ['int'])),
                                ('dsl_actual_delay_down', (YLeaf(YType.uint32, 'dsl-actual-delay-down'), ['int'])),
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
                            self._segment_path = lambda: "tags"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.Interfaces.Interface.Tags, [u'service_name', u'max_payload', u'host_uniq', u'relay_session_id', u'remote_id', u'circuit_id', u'is_iwf', u'dsl_actual_up', u'dsl_actual_down', u'dsl_min_up', u'dsl_min_down', u'dsl_attain_up', u'dsl_attain_down', u'dsl_max_up', u'dsl_max_down', u'dsl_min_up_low', u'dsl_min_down_low', u'dsl_max_delay_up', u'dsl_actual_delay_up', u'dsl_max_delay_down', u'dsl_actual_delay_down'], name, value)


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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('data_link', (YLeaf(YType.uint8, 'data-link'), ['int'])),
                                    ('encaps1', (YLeaf(YType.uint8, 'encaps1'), ['int'])),
                                    ('encaps2', (YLeaf(YType.uint8, 'encaps2'), ['int'])),
                                ])
                                self.data_link = None
                                self.encaps1 = None
                                self.encaps2 = None
                                self._segment_path = lambda: "access-loop-encapsulation"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.Interfaces.Interface.Tags.AccessLoopEncapsulation, [u'data_link', u'encaps1', u'encaps2'], name, value)


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
                    self._child_classes = OrderedDict([("bba-group", ("bba_group", Pppoe.Nodes.Node.BbaGroups.BbaGroup))])
                    self._leafs = OrderedDict()

                    self.bba_group = YList(self)
                    self._segment_path = lambda: "bba-groups"
                    self._is_frozen = True

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
                        self._child_classes = OrderedDict([("limit-config", ("limit_config", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig)), ("limits", ("limits", Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits)), ("throttles", ("throttles", Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles)), ("throttle-config", ("throttle_config", Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig))])
                        self._leafs = OrderedDict([
                            ('bba_group_name', (YLeaf(YType.str, 'bba-group-name'), ['str'])),
                        ])
                        self.bba_group_name = None

                        self.limit_config = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig()
                        self.limit_config.parent = self
                        self._children_name_map["limit_config"] = "limit-config"

                        self.limits = Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits()
                        self.limits.parent = self
                        self._children_name_map["limits"] = "limits"

                        self.throttles = Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles()
                        self.throttles.parent = self
                        self._children_name_map["throttles"] = "throttles"

                        self.throttle_config = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig()
                        self.throttle_config.parent = self
                        self._children_name_map["throttle_config"] = "throttle-config"
                        self._segment_path = lambda: "bba-group" + "[bba-group-name='" + str(self.bba_group_name) + "']"
                        self._is_frozen = True

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
                            self._child_classes = OrderedDict([("card", ("card", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Card)), ("access-intf", ("access_intf", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.AccessIntf)), ("mac", ("mac", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Mac)), ("mac-iwf", ("mac_iwf", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwf)), ("mac-access-interface", ("mac_access_interface", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacAccessInterface)), ("mac-iwf-access-interface", ("mac_iwf_access_interface", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwfAccessInterface)), ("circuit-id", ("circuit_id", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitId)), ("remote-id", ("remote_id", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.RemoteId)), ("circuit-id-and-remote-id", ("circuit_id_and_remote_id", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitIdAndRemoteId)), ("outer-vlan-id", ("outer_vlan_id", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.OuterVlanId)), ("inner-vlan-id", ("inner_vlan_id", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.InnerVlanId)), ("vlan-id", ("vlan_id", Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.VlanId))])
                            self._leafs = OrderedDict()

                            self.card = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Card()
                            self.card.parent = self
                            self._children_name_map["card"] = "card"

                            self.access_intf = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.AccessIntf()
                            self.access_intf.parent = self
                            self._children_name_map["access_intf"] = "access-intf"

                            self.mac = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Mac()
                            self.mac.parent = self
                            self._children_name_map["mac"] = "mac"

                            self.mac_iwf = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwf()
                            self.mac_iwf.parent = self
                            self._children_name_map["mac_iwf"] = "mac-iwf"

                            self.mac_access_interface = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacAccessInterface()
                            self.mac_access_interface.parent = self
                            self._children_name_map["mac_access_interface"] = "mac-access-interface"

                            self.mac_iwf_access_interface = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwfAccessInterface()
                            self.mac_iwf_access_interface.parent = self
                            self._children_name_map["mac_iwf_access_interface"] = "mac-iwf-access-interface"

                            self.circuit_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitId()
                            self.circuit_id.parent = self
                            self._children_name_map["circuit_id"] = "circuit-id"

                            self.remote_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.RemoteId()
                            self.remote_id.parent = self
                            self._children_name_map["remote_id"] = "remote-id"

                            self.circuit_id_and_remote_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitIdAndRemoteId()
                            self.circuit_id_and_remote_id.parent = self
                            self._children_name_map["circuit_id_and_remote_id"] = "circuit-id-and-remote-id"

                            self.outer_vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.OuterVlanId()
                            self.outer_vlan_id.parent = self
                            self._children_name_map["outer_vlan_id"] = "outer-vlan-id"

                            self.inner_vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.InnerVlanId()
                            self.inner_vlan_id.parent = self
                            self._children_name_map["inner_vlan_id"] = "inner-vlan-id"

                            self.vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.VlanId()
                            self.vlan_id.parent = self
                            self._children_name_map["vlan_id"] = "vlan-id"
                            self._segment_path = lambda: "limit-config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig, [], name, value)


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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_limit', (YLeaf(YType.uint32, 'max-limit'), ['int'])),
                                    ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                                    ('radius_override_enabled', (YLeaf(YType.int32, 'radius-override-enabled'), ['int'])),
                                ])
                                self.max_limit = None
                                self.threshold = None
                                self.radius_override_enabled = None
                                self._segment_path = lambda: "card"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Card, [u'max_limit', u'threshold', u'radius_override_enabled'], name, value)


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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_limit', (YLeaf(YType.uint32, 'max-limit'), ['int'])),
                                    ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                                    ('radius_override_enabled', (YLeaf(YType.int32, 'radius-override-enabled'), ['int'])),
                                ])
                                self.max_limit = None
                                self.threshold = None
                                self.radius_override_enabled = None
                                self._segment_path = lambda: "access-intf"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.AccessIntf, [u'max_limit', u'threshold', u'radius_override_enabled'], name, value)


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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_limit', (YLeaf(YType.uint32, 'max-limit'), ['int'])),
                                    ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                                    ('radius_override_enabled', (YLeaf(YType.int32, 'radius-override-enabled'), ['int'])),
                                ])
                                self.max_limit = None
                                self.threshold = None
                                self.radius_override_enabled = None
                                self._segment_path = lambda: "mac"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Mac, [u'max_limit', u'threshold', u'radius_override_enabled'], name, value)


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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_limit', (YLeaf(YType.uint32, 'max-limit'), ['int'])),
                                    ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                                    ('radius_override_enabled', (YLeaf(YType.int32, 'radius-override-enabled'), ['int'])),
                                ])
                                self.max_limit = None
                                self.threshold = None
                                self.radius_override_enabled = None
                                self._segment_path = lambda: "mac-iwf"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwf, [u'max_limit', u'threshold', u'radius_override_enabled'], name, value)


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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_limit', (YLeaf(YType.uint32, 'max-limit'), ['int'])),
                                    ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                                    ('radius_override_enabled', (YLeaf(YType.int32, 'radius-override-enabled'), ['int'])),
                                ])
                                self.max_limit = None
                                self.threshold = None
                                self.radius_override_enabled = None
                                self._segment_path = lambda: "mac-access-interface"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacAccessInterface, [u'max_limit', u'threshold', u'radius_override_enabled'], name, value)


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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_limit', (YLeaf(YType.uint32, 'max-limit'), ['int'])),
                                    ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                                    ('radius_override_enabled', (YLeaf(YType.int32, 'radius-override-enabled'), ['int'])),
                                ])
                                self.max_limit = None
                                self.threshold = None
                                self.radius_override_enabled = None
                                self._segment_path = lambda: "mac-iwf-access-interface"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwfAccessInterface, [u'max_limit', u'threshold', u'radius_override_enabled'], name, value)


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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_limit', (YLeaf(YType.uint32, 'max-limit'), ['int'])),
                                    ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                                    ('radius_override_enabled', (YLeaf(YType.int32, 'radius-override-enabled'), ['int'])),
                                ])
                                self.max_limit = None
                                self.threshold = None
                                self.radius_override_enabled = None
                                self._segment_path = lambda: "circuit-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitId, [u'max_limit', u'threshold', u'radius_override_enabled'], name, value)


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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_limit', (YLeaf(YType.uint32, 'max-limit'), ['int'])),
                                    ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                                    ('radius_override_enabled', (YLeaf(YType.int32, 'radius-override-enabled'), ['int'])),
                                ])
                                self.max_limit = None
                                self.threshold = None
                                self.radius_override_enabled = None
                                self._segment_path = lambda: "remote-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.RemoteId, [u'max_limit', u'threshold', u'radius_override_enabled'], name, value)


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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_limit', (YLeaf(YType.uint32, 'max-limit'), ['int'])),
                                    ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                                    ('radius_override_enabled', (YLeaf(YType.int32, 'radius-override-enabled'), ['int'])),
                                ])
                                self.max_limit = None
                                self.threshold = None
                                self.radius_override_enabled = None
                                self._segment_path = lambda: "circuit-id-and-remote-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitIdAndRemoteId, [u'max_limit', u'threshold', u'radius_override_enabled'], name, value)


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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_limit', (YLeaf(YType.uint32, 'max-limit'), ['int'])),
                                    ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                                    ('radius_override_enabled', (YLeaf(YType.int32, 'radius-override-enabled'), ['int'])),
                                ])
                                self.max_limit = None
                                self.threshold = None
                                self.radius_override_enabled = None
                                self._segment_path = lambda: "outer-vlan-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.OuterVlanId, [u'max_limit', u'threshold', u'radius_override_enabled'], name, value)


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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_limit', (YLeaf(YType.uint32, 'max-limit'), ['int'])),
                                    ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                                    ('radius_override_enabled', (YLeaf(YType.int32, 'radius-override-enabled'), ['int'])),
                                ])
                                self.max_limit = None
                                self.threshold = None
                                self.radius_override_enabled = None
                                self._segment_path = lambda: "inner-vlan-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.InnerVlanId, [u'max_limit', u'threshold', u'radius_override_enabled'], name, value)


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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_limit', (YLeaf(YType.uint32, 'max-limit'), ['int'])),
                                    ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                                    ('radius_override_enabled', (YLeaf(YType.int32, 'radius-override-enabled'), ['int'])),
                                ])
                                self.max_limit = None
                                self.threshold = None
                                self.radius_override_enabled = None
                                self._segment_path = lambda: "vlan-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.VlanId, [u'max_limit', u'threshold', u'radius_override_enabled'], name, value)


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
                            self._child_classes = OrderedDict([("limit", ("limit", Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits.Limit))])
                            self._leafs = OrderedDict()

                            self.limit = YList(self)
                            self._segment_path = lambda: "limits"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits, [], name, value)


                        class Limit(Entity):
                            """
                            PPPoE session limit state
                            
                            .. attribute:: interface_name
                            
                            	Access Interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                    ('iwf', (YLeaf(YType.boolean, 'iwf'), ['bool'])),
                                    ('circuit_id', (YLeaf(YType.str, 'circuit-id'), ['str'])),
                                    ('remote_id', (YLeaf(YType.str, 'remote-id'), ['str'])),
                                    ('outer_vlan_id', (YLeaf(YType.uint32, 'outer-vlan-id'), ['int'])),
                                    ('inner_vlan_id', (YLeaf(YType.uint32, 'inner-vlan-id'), ['int'])),
                                    ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'PppoeMaLimitState', '')])),
                                    ('session_count', (YLeaf(YType.uint32, 'session-count'), ['int'])),
                                    ('radius_override_set', (YLeaf(YType.int32, 'radius-override-set'), ['int'])),
                                    ('override_limit', (YLeaf(YType.uint32, 'override-limit'), ['int'])),
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
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits.Limit, ['interface_name', 'mac_address', 'iwf', 'circuit_id', 'remote_id', 'outer_vlan_id', 'inner_vlan_id', u'state', u'session_count', u'radius_override_set', u'override_limit'], name, value)


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
                            self._child_classes = OrderedDict([("throttle", ("throttle", Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles.Throttle))])
                            self._leafs = OrderedDict()

                            self.throttle = YList(self)
                            self._segment_path = lambda: "throttles"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles, [], name, value)


                        class Throttle(Entity):
                            """
                            PPPoE session throttle state
                            
                            .. attribute:: interface_name
                            
                            	Access Interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                    ('iwf', (YLeaf(YType.boolean, 'iwf'), ['bool'])),
                                    ('circuit_id', (YLeaf(YType.str, 'circuit-id'), ['str'])),
                                    ('remote_id', (YLeaf(YType.str, 'remote-id'), ['str'])),
                                    ('outer_vlan_id', (YLeaf(YType.uint32, 'outer-vlan-id'), ['int'])),
                                    ('inner_vlan_id', (YLeaf(YType.uint32, 'inner-vlan-id'), ['int'])),
                                    ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'PppoeMaThrottleState', '')])),
                                    ('time_left', (YLeaf(YType.uint32, 'time-left'), ['int'])),
                                    ('since_reset', (YLeaf(YType.uint32, 'since-reset'), ['int'])),
                                    ('padi_count', (YLeaf(YType.uint32, 'padi-count'), ['int'])),
                                    ('padr_count', (YLeaf(YType.uint32, 'padr-count'), ['int'])),
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
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles.Throttle, ['interface_name', 'mac_address', 'iwf', 'circuit_id', 'remote_id', 'outer_vlan_id', 'inner_vlan_id', u'state', u'time_left', u'since_reset', u'padi_count', u'padr_count'], name, value)


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
                            self._child_classes = OrderedDict([("mac", ("mac", Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.Mac)), ("mac-access-interface", ("mac_access_interface", Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacAccessInterface)), ("mac-iwf-access-interface", ("mac_iwf_access_interface", Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacIwfAccessInterface)), ("circuit-id", ("circuit_id", Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitId)), ("remote-id", ("remote_id", Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.RemoteId)), ("circuit-id-and-remote-id", ("circuit_id_and_remote_id", Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitIdAndRemoteId)), ("outer-vlan-id", ("outer_vlan_id", Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.OuterVlanId)), ("inner-vlan-id", ("inner_vlan_id", Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.InnerVlanId)), ("vlan-id", ("vlan_id", Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.VlanId))])
                            self._leafs = OrderedDict()

                            self.mac = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.Mac()
                            self.mac.parent = self
                            self._children_name_map["mac"] = "mac"

                            self.mac_access_interface = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacAccessInterface()
                            self.mac_access_interface.parent = self
                            self._children_name_map["mac_access_interface"] = "mac-access-interface"

                            self.mac_iwf_access_interface = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacIwfAccessInterface()
                            self.mac_iwf_access_interface.parent = self
                            self._children_name_map["mac_iwf_access_interface"] = "mac-iwf-access-interface"

                            self.circuit_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitId()
                            self.circuit_id.parent = self
                            self._children_name_map["circuit_id"] = "circuit-id"

                            self.remote_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.RemoteId()
                            self.remote_id.parent = self
                            self._children_name_map["remote_id"] = "remote-id"

                            self.circuit_id_and_remote_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitIdAndRemoteId()
                            self.circuit_id_and_remote_id.parent = self
                            self._children_name_map["circuit_id_and_remote_id"] = "circuit-id-and-remote-id"

                            self.outer_vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.OuterVlanId()
                            self.outer_vlan_id.parent = self
                            self._children_name_map["outer_vlan_id"] = "outer-vlan-id"

                            self.inner_vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.InnerVlanId()
                            self.inner_vlan_id.parent = self
                            self._children_name_map["inner_vlan_id"] = "inner-vlan-id"

                            self.vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.VlanId()
                            self.vlan_id.parent = self
                            self._children_name_map["vlan_id"] = "vlan-id"
                            self._segment_path = lambda: "throttle-config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig, [], name, value)


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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('limit', (YLeaf(YType.uint32, 'limit'), ['int'])),
                                    ('request_period', (YLeaf(YType.uint32, 'request-period'), ['int'])),
                                    ('blocking_period', (YLeaf(YType.uint32, 'blocking-period'), ['int'])),
                                ])
                                self.limit = None
                                self.request_period = None
                                self.blocking_period = None
                                self._segment_path = lambda: "mac"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.Mac, [u'limit', u'request_period', u'blocking_period'], name, value)


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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('limit', (YLeaf(YType.uint32, 'limit'), ['int'])),
                                    ('request_period', (YLeaf(YType.uint32, 'request-period'), ['int'])),
                                    ('blocking_period', (YLeaf(YType.uint32, 'blocking-period'), ['int'])),
                                ])
                                self.limit = None
                                self.request_period = None
                                self.blocking_period = None
                                self._segment_path = lambda: "mac-access-interface"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacAccessInterface, [u'limit', u'request_period', u'blocking_period'], name, value)


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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('limit', (YLeaf(YType.uint32, 'limit'), ['int'])),
                                    ('request_period', (YLeaf(YType.uint32, 'request-period'), ['int'])),
                                    ('blocking_period', (YLeaf(YType.uint32, 'blocking-period'), ['int'])),
                                ])
                                self.limit = None
                                self.request_period = None
                                self.blocking_period = None
                                self._segment_path = lambda: "mac-iwf-access-interface"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacIwfAccessInterface, [u'limit', u'request_period', u'blocking_period'], name, value)


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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('limit', (YLeaf(YType.uint32, 'limit'), ['int'])),
                                    ('request_period', (YLeaf(YType.uint32, 'request-period'), ['int'])),
                                    ('blocking_period', (YLeaf(YType.uint32, 'blocking-period'), ['int'])),
                                ])
                                self.limit = None
                                self.request_period = None
                                self.blocking_period = None
                                self._segment_path = lambda: "circuit-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitId, [u'limit', u'request_period', u'blocking_period'], name, value)


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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('limit', (YLeaf(YType.uint32, 'limit'), ['int'])),
                                    ('request_period', (YLeaf(YType.uint32, 'request-period'), ['int'])),
                                    ('blocking_period', (YLeaf(YType.uint32, 'blocking-period'), ['int'])),
                                ])
                                self.limit = None
                                self.request_period = None
                                self.blocking_period = None
                                self._segment_path = lambda: "remote-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.RemoteId, [u'limit', u'request_period', u'blocking_period'], name, value)


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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('limit', (YLeaf(YType.uint32, 'limit'), ['int'])),
                                    ('request_period', (YLeaf(YType.uint32, 'request-period'), ['int'])),
                                    ('blocking_period', (YLeaf(YType.uint32, 'blocking-period'), ['int'])),
                                ])
                                self.limit = None
                                self.request_period = None
                                self.blocking_period = None
                                self._segment_path = lambda: "circuit-id-and-remote-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitIdAndRemoteId, [u'limit', u'request_period', u'blocking_period'], name, value)


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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('limit', (YLeaf(YType.uint32, 'limit'), ['int'])),
                                    ('request_period', (YLeaf(YType.uint32, 'request-period'), ['int'])),
                                    ('blocking_period', (YLeaf(YType.uint32, 'blocking-period'), ['int'])),
                                ])
                                self.limit = None
                                self.request_period = None
                                self.blocking_period = None
                                self._segment_path = lambda: "outer-vlan-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.OuterVlanId, [u'limit', u'request_period', u'blocking_period'], name, value)


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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('limit', (YLeaf(YType.uint32, 'limit'), ['int'])),
                                    ('request_period', (YLeaf(YType.uint32, 'request-period'), ['int'])),
                                    ('blocking_period', (YLeaf(YType.uint32, 'blocking-period'), ['int'])),
                                ])
                                self.limit = None
                                self.request_period = None
                                self.blocking_period = None
                                self._segment_path = lambda: "inner-vlan-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.InnerVlanId, [u'limit', u'request_period', u'blocking_period'], name, value)


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
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('limit', (YLeaf(YType.uint32, 'limit'), ['int'])),
                                    ('request_period', (YLeaf(YType.uint32, 'request-period'), ['int'])),
                                    ('blocking_period', (YLeaf(YType.uint32, 'blocking-period'), ['int'])),
                                ])
                                self.limit = None
                                self.request_period = None
                                self.blocking_period = None
                                self._segment_path = lambda: "vlan-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.VlanId, [u'limit', u'request_period', u'blocking_period'], name, value)


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
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ready_access_interfaces', (YLeaf(YType.uint32, 'ready-access-interfaces'), ['int'])),
                        ('not_ready_access_interfaces', (YLeaf(YType.uint32, 'not-ready-access-interfaces'), ['int'])),
                        ('complete_sessions', (YLeaf(YType.uint32, 'complete-sessions'), ['int'])),
                        ('incomplete_sessions', (YLeaf(YType.uint32, 'incomplete-sessions'), ['int'])),
                        ('flow_control_limit', (YLeaf(YType.uint32, 'flow-control-limit'), ['int'])),
                        ('flow_control_in_flight_sessions', (YLeaf(YType.uint32, 'flow-control-in-flight-sessions'), ['int'])),
                        ('flow_control_dropped_sessions', (YLeaf(YType.uint64, 'flow-control-dropped-sessions'), ['int'])),
                        ('flow_control_disconnected_sessions', (YLeaf(YType.uint64, 'flow-control-disconnected-sessions'), ['int'])),
                        ('flow_control_successful_sessions', (YLeaf(YType.uint64, 'flow-control-successful-sessions'), ['int'])),
                        ('pppoema_subscriber_infra_flow_control', (YLeaf(YType.uint32, 'pppoema-subscriber-infra-flow-control'), ['int'])),
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
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pppoe.Nodes.Node.SummaryTotal, [u'ready_access_interfaces', u'not_ready_access_interfaces', u'complete_sessions', u'incomplete_sessions', u'flow_control_limit', u'flow_control_in_flight_sessions', u'flow_control_dropped_sessions', u'flow_control_disconnected_sessions', u'flow_control_successful_sessions', u'pppoema_subscriber_infra_flow_control'], name, value)

    def clone_ptr(self):
        self._top_entity = Pppoe()
        return self._top_entity


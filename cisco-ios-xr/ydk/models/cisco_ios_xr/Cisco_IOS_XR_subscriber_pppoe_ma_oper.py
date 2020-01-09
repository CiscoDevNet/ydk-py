""" Cisco_IOS_XR_subscriber_pppoe_ma_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-pppoe\-ma package operational data.

This module contains definitions
for the following management objects\:
  pppoe\: PPPoE operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
        return meta._meta_table['PppoeMaLimitState']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
        return meta._meta_table['PppoeMaSessionIdbSrgState']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
        return meta._meta_table['PppoeMaSessionState']


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

    .. data:: pppoe_ma_session_trig_renegotiation = 20

    	pppoe ma session trig renegotiation

    .. data:: pppoe_ma_session_trig_count = 21

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

    pppoe_ma_session_trig_renegotiation = Enum.YLeaf(20, "pppoe-ma-session-trig-renegotiation")

    pppoe_ma_session_trig_count = Enum.YLeaf(21, "pppoe-ma-session-trig-count")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
        return meta._meta_table['PppoeMaSessionTrig']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
        return meta._meta_table['PppoeMaThrottleState']



class Pppoe(_Entity_):
    """
    PPPoE operational data
    
    .. attribute:: access_interface_statistics
    
    	PPPoE access interface statistics information
    	**type**\:  :py:class:`AccessInterfaceStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics>`
    
    	**config**\: False
    
    .. attribute:: nodes
    
    	Per\-node PPPoE operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes>`
    
    	**config**\: False
    
    

    """

    _prefix = 'subscriber-pppoe-ma-oper'
    _revision = '2019-10-07'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
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


    class AccessInterfaceStatistics(_Entity_):
        """
        PPPoE access interface statistics information
        
        .. attribute:: access_interface_statistic
        
        	Statistics information for a PPPoE\-enabled access interface
        	**type**\: list of  		 :py:class:`AccessInterfaceStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic>`
        
        	**config**\: False
        
        

        """

        _prefix = 'subscriber-pppoe-ma-oper'
        _revision = '2019-10-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class AccessInterfaceStatistic(_Entity_):
            """
            Statistics information for a PPPoE\-enabled
            access interface
            
            .. attribute:: interface_name  (key)
            
            	PPPoE Access Interface
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            	**config**\: False
            
            .. attribute:: packet_counts
            
            	Packet Counts
            	**type**\:  :py:class:`PacketCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts>`
            
            	**config**\: False
            
            

            """

            _prefix = 'subscriber-pppoe-ma-oper'
            _revision = '2019-10-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class PacketCounts(_Entity_):
                """
                Packet Counts
                
                .. attribute:: padi
                
                	PADI counts
                	**type**\:  :py:class:`Padi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padi>`
                
                	**config**\: False
                
                .. attribute:: pado
                
                	PADO counts
                	**type**\:  :py:class:`Pado <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Pado>`
                
                	**config**\: False
                
                .. attribute:: padr
                
                	PADR counts
                	**type**\:  :py:class:`Padr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padr>`
                
                	**config**\: False
                
                .. attribute:: pads_success
                
                	PADS Success counts
                	**type**\:  :py:class:`PadsSuccess <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsSuccess>`
                
                	**config**\: False
                
                .. attribute:: pads_error
                
                	PADS Error counts
                	**type**\:  :py:class:`PadsError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsError>`
                
                	**config**\: False
                
                .. attribute:: padt
                
                	PADT counts
                	**type**\:  :py:class:`Padt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padt>`
                
                	**config**\: False
                
                .. attribute:: session_state
                
                	Session Stage counts
                	**type**\:  :py:class:`SessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.SessionState>`
                
                	**config**\: False
                
                .. attribute:: other
                
                	Other counts
                	**type**\:  :py:class:`Other <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Other>`
                
                	**config**\: False
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2019-10-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class Padi(_Entity_):
                    """
                    PADI counts
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2019-10-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padi, ['sent', 'received', 'dropped'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padi']['meta_info']


                class Pado(_Entity_):
                    """
                    PADO counts
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2019-10-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Pado, ['sent', 'received', 'dropped'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Pado']['meta_info']


                class Padr(_Entity_):
                    """
                    PADR counts
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2019-10-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padr, ['sent', 'received', 'dropped'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padr']['meta_info']


                class PadsSuccess(_Entity_):
                    """
                    PADS Success counts
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2019-10-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsSuccess, ['sent', 'received', 'dropped'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsSuccess']['meta_info']


                class PadsError(_Entity_):
                    """
                    PADS Error counts
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2019-10-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsError, ['sent', 'received', 'dropped'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsError']['meta_info']


                class Padt(_Entity_):
                    """
                    PADT counts
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2019-10-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padt, ['sent', 'received', 'dropped'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padt']['meta_info']


                class SessionState(_Entity_):
                    """
                    Session Stage counts
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2019-10-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.SessionState, ['sent', 'received', 'dropped'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.SessionState']['meta_info']


                class Other(_Entity_):
                    """
                    Other counts
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2019-10-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Other, ['sent', 'received', 'dropped'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Other']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                    return meta._meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                return meta._meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
            return meta._meta_table['Pppoe.AccessInterfaceStatistics']['meta_info']


    class Nodes(_Entity_):
        """
        Per\-node PPPoE operational data
        
        .. attribute:: node
        
        	PPPoE operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'subscriber-pppoe-ma-oper'
        _revision = '2019-10-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class Node(_Entity_):
            """
            PPPoE operational data for a particular node
            
            .. attribute:: node_name  (key)
            
            	Node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: disconnect_history
            
            	PPPoE disconnect history for a given node
            	**type**\:  :py:class:`DisconnectHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistory>`
            
            	**config**\: False
            
            .. attribute:: disconnect_history_unique
            
            	PPPoE unique disconnect history for a given node
            	**type**\:  :py:class:`DisconnectHistoryUnique <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistoryUnique>`
            
            	**config**\: False
            
            .. attribute:: statistics
            
            	PPPoE statistics for a given node
            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics>`
            
            	**config**\: False
            
            .. attribute:: access_interface
            
            	PPPoE access interface information
            	**type**\:  :py:class:`AccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.AccessInterface>`
            
            	**config**\: False
            
            .. attribute:: interfaces
            
            	Per interface PPPoE operational data
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Interfaces>`
            
            	**config**\: False
            
            .. attribute:: bba_groups
            
            	PPPoE BBA\-Group information
            	**type**\:  :py:class:`BbaGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups>`
            
            	**config**\: False
            
            .. attribute:: summary_total
            
            	PPPoE statistics for a given node
            	**type**\:  :py:class:`SummaryTotal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.SummaryTotal>`
            
            	**config**\: False
            
            

            """

            _prefix = 'subscriber-pppoe-ma-oper'
            _revision = '2019-10-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class DisconnectHistory(_Entity_):
                """
                PPPoE disconnect history for a given node
                
                .. attribute:: current_idx
                
                	Current index of history
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: entry
                
                	Array of disconnected subscribers
                	**type**\: list of  		 :py:class:`Entry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistory.Entry>`
                
                	**config**\: False
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2019-10-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistory, ['current_idx'], name, value)


                class Entry(_Entity_):
                    """
                    Array of disconnected subscribers
                    
                    .. attribute:: session_idb
                    
                    	Session IDB
                    	**type**\:  :py:class:`SessionIdb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb>`
                    
                    	**config**\: False
                    
                    .. attribute:: timestamp
                    
                    	Time when disconnected
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: ifname
                    
                    	Interface name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: trigger
                    
                    	Disconnect Trigger
                    	**type**\:  :py:class:`PppoeMaSessionTrig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.PppoeMaSessionTrig>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2019-10-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistory.Entry, ['timestamp', 'ifname', 'trigger'], name, value)


                    class SessionIdb(_Entity_):
                        """
                        Session IDB
                        
                        .. attribute:: tags
                        
                        	Tags
                        	**type**\:  :py:class:`Tags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.Tags>`
                        
                        	**config**\: False
                        
                        .. attribute:: vlan_outer_tag
                        
                        	VLAN Outer Tag
                        	**type**\:  :py:class:`VlanOuterTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.VlanOuterTag>`
                        
                        	**config**\: False
                        
                        .. attribute:: vlan_inner_tag
                        
                        	VLAN Inner Tag
                        	**type**\:  :py:class:`VlanInnerTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.VlanInnerTag>`
                        
                        	**config**\: False
                        
                        .. attribute:: interface
                        
                        	Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: access_interface
                        
                        	Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: session_id
                        
                        	Session ID
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: sub_label
                        
                        	Sub Label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: peer_mac_address
                        
                        	Peer Mac\-Address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        	**config**\: False
                        
                        .. attribute:: state
                        
                        	State
                        	**type**\:  :py:class:`PppoeMaSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.PppoeMaSessionState>`
                        
                        	**config**\: False
                        
                        .. attribute:: cdm_object_handle
                        
                        	CDM Object Handle
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: chkpt_id
                        
                        	Chkpt ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: punted_count
                        
                        	Punted Count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: port_limit
                        
                        	Port Limit
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: is_counted
                        
                        	Is BBA Counted
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_vlan_outer_tag
                        
                        	Is VLAN Outer Tag
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_vlan_inner_tag
                        
                        	Is VLAN Inner Tag
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_cleanup_pending
                        
                        	Is Cleanup Pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_disconnect_done_pending
                        
                        	Is Disconnect Done Pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_delete_done_pending
                        
                        	Is Delete Done Pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_intf_create_callback_pending
                        
                        	Is Interface Create Callback pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_publish_encaps_attr_pending
                        
                        	Is Publish Encaps Attr pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_publish_encaps_attr_cb_pending
                        
                        	Is Publish Encaps Attr Callback pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_intf_delete_callback_pending
                        
                        	Is Interface Delete Callback pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_intf_delete_pending
                        
                        	Is Interface Delete pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_im_owned_resource
                        
                        	Is IM Owned Resource
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_im_final_received
                        
                        	Is IM Final received
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_im_owned_resource_missing
                        
                        	Is IM Owned Resource missing
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_aaa_start_request_callback_pending
                        
                        	Is AAA Start request callback pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_aaa_owned_resource
                        
                        	Is AAA Owned Resource
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_aaa_disconnect_requested
                        
                        	Is AAA Disconnect Requested
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_aaa_disconnect_received
                        
                        	Is AAA Disconnect Received
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_sub_db_activate_callback_pending
                        
                        	Is SubDB Activate callback pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_pads_sent
                        
                        	Is PADS Sent
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_padt_received
                        
                        	Is PADT Received
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_in_flight
                        
                        	Is Session In Flight
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_radius_override
                        
                        	Is RADIUS override enabled
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: expected_notifications
                        
                        	Expected Notifications
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: received_notifications
                        
                        	Received Notifications
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: srg_state
                        
                        	SRG state
                        	**type**\:  :py:class:`PppoeMaSessionIdbSrgState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.PppoeMaSessionIdbSrgState>`
                        
                        	**config**\: False
                        
                        .. attribute:: is_srg_data_received
                        
                        	Is SRG Data Received
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_iedge_data_received
                        
                        	Is IEDGE Data Received
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2019-10-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb, ['interface', 'access_interface', 'session_id', 'sub_label', 'peer_mac_address', 'state', 'cdm_object_handle', 'chkpt_id', 'punted_count', 'port_limit', 'is_counted', 'is_vlan_outer_tag', 'is_vlan_inner_tag', 'is_cleanup_pending', 'is_disconnect_done_pending', 'is_delete_done_pending', 'is_intf_create_callback_pending', 'is_publish_encaps_attr_pending', 'is_publish_encaps_attr_cb_pending', 'is_intf_delete_callback_pending', 'is_intf_delete_pending', 'is_im_owned_resource', 'is_im_final_received', 'is_im_owned_resource_missing', 'is_aaa_start_request_callback_pending', 'is_aaa_owned_resource', 'is_aaa_disconnect_requested', 'is_aaa_disconnect_received', 'is_sub_db_activate_callback_pending', 'is_pads_sent', 'is_padt_received', 'is_in_flight', 'is_radius_override', 'expected_notifications', 'received_notifications', 'srg_state', 'is_srg_data_received', 'is_iedge_data_received'], name, value)


                        class Tags(_Entity_):
                            """
                            Tags
                            
                            .. attribute:: access_loop_encapsulation
                            
                            	Access Loop Encapsulation
                            	**type**\:  :py:class:`AccessLoopEncapsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.Tags.AccessLoopEncapsulation>`
                            
                            	**config**\: False
                            
                            .. attribute:: is_service_name
                            
                            	Is Service Name
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_max_payload
                            
                            	Is Max Payload
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_host_uniq
                            
                            	Is Host Uniq
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_relay_session_id
                            
                            	Is Relay Session ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_vendor_specific
                            
                            	Is Vendor Specific
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_iwf
                            
                            	Is IWF
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_remote_id
                            
                            	Is Remote ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_circuit_id
                            
                            	Is Circuit ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_tag
                            
                            	Is DSL Tag
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: service_name
                            
                            	Service Name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: max_payload
                            
                            	Max Payload
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: host_uniq
                            
                            	Host Uniq
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            	**config**\: False
                            
                            .. attribute:: relay_session_id
                            
                            	Relay Session ID
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            	**config**\: False
                            
                            .. attribute:: remote_id
                            
                            	Remote ID
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: circuit_id
                            
                            	Circuit ID
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_actual_up
                            
                            	Is DSL Actual Up
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_actual_down
                            
                            	Is DSL Actual Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_min_up
                            
                            	Is DSL Min Up
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_min_down
                            
                            	Is DSL Min Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_attain_up
                            
                            	Is DSL Attain Up
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_attain_down
                            
                            	Is DSL Attain Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_max_up
                            
                            	Is DSL Max Up
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_max_down
                            
                            	Is DSL Max Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_min_up_low
                            
                            	Is DSL Min Up Low
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_min_down_low
                            
                            	Is DSL Min Down Low
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_max_delay_up
                            
                            	Is DSL Max Delay Up
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_actual_delay_up
                            
                            	Is DSL Actual Delay Up
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_max_delay_down
                            
                            	Is DSL Max Delay Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_actual_delay_down
                            
                            	Is DSL Actual Delay Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_access_loop_encapsulation
                            
                            	Is Access Loop Encapsulation
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_actual_up
                            
                            	DSL Actual Up
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_actual_down
                            
                            	DSL Actual Down
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_min_up
                            
                            	DSL Min Up
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_min_down
                            
                            	DSL Min Down
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_attain_up
                            
                            	DSL Attain Up
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_attain_down
                            
                            	DSL Attain Down
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_max_up
                            
                            	DSL Max Up
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_max_down
                            
                            	DSL Max Down
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_min_up_low
                            
                            	DSL Min Up Low
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_min_down_low
                            
                            	DSL Min Down Low
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_max_delay_up
                            
                            	DSL Max Delay Up
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_actual_delay_up
                            
                            	DSL Actual Delay Up
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_max_delay_down
                            
                            	DSL Max Delay Down
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_actual_delay_down
                            
                            	DSL Actual Delay Down
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.Tags, ['is_service_name', 'is_max_payload', 'is_host_uniq', 'is_relay_session_id', 'is_vendor_specific', 'is_iwf', 'is_remote_id', 'is_circuit_id', 'is_dsl_tag', 'service_name', 'max_payload', 'host_uniq', 'relay_session_id', 'remote_id', 'circuit_id', 'is_dsl_actual_up', 'is_dsl_actual_down', 'is_dsl_min_up', 'is_dsl_min_down', 'is_dsl_attain_up', 'is_dsl_attain_down', 'is_dsl_max_up', 'is_dsl_max_down', 'is_dsl_min_up_low', 'is_dsl_min_down_low', 'is_dsl_max_delay_up', 'is_dsl_actual_delay_up', 'is_dsl_max_delay_down', 'is_dsl_actual_delay_down', 'is_access_loop_encapsulation', 'dsl_actual_up', 'dsl_actual_down', 'dsl_min_up', 'dsl_min_down', 'dsl_attain_up', 'dsl_attain_down', 'dsl_max_up', 'dsl_max_down', 'dsl_min_up_low', 'dsl_min_down_low', 'dsl_max_delay_up', 'dsl_actual_delay_up', 'dsl_max_delay_down', 'dsl_actual_delay_down'], name, value)


                            class AccessLoopEncapsulation(_Entity_):
                                """
                                Access Loop Encapsulation
                                
                                .. attribute:: data_link
                                
                                	Data Link
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: encaps1
                                
                                	Encaps 1
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: encaps2
                                
                                	Encaps 2
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'subscriber-pppoe-ma-oper'
                                _revision = '2019-10-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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
                                    self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.Tags.AccessLoopEncapsulation, ['data_link', 'encaps1', 'encaps2'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                    return meta._meta_table['Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.Tags.AccessLoopEncapsulation']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.Tags']['meta_info']


                        class VlanOuterTag(_Entity_):
                            """
                            VLAN Outer Tag
                            
                            .. attribute:: ether_type
                            
                            	Ethertype. See IEEE 802.1Q for more information
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            .. attribute:: user_priority
                            
                            	User Priority
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: cfi
                            
                            	CFI
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: vlan_id
                            
                            	VLAN ID
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.VlanOuterTag, ['ether_type', 'user_priority', 'cfi', 'vlan_id'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.VlanOuterTag']['meta_info']


                        class VlanInnerTag(_Entity_):
                            """
                            VLAN Inner Tag
                            
                            .. attribute:: ether_type
                            
                            	Ethertype. See IEEE 802.1Q for more information
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            .. attribute:: user_priority
                            
                            	User Priority
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: cfi
                            
                            	CFI
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: vlan_id
                            
                            	VLAN ID
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.VlanInnerTag, ['ether_type', 'user_priority', 'cfi', 'vlan_id'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb.VlanInnerTag']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.DisconnectHistory.Entry.SessionIdb']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.Nodes.Node.DisconnectHistory.Entry']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                    return meta._meta_table['Pppoe.Nodes.Node.DisconnectHistory']['meta_info']


            class DisconnectHistoryUnique(_Entity_):
                """
                PPPoE unique disconnect history for a given
                node
                
                .. attribute:: disconnect_count
                
                	The total number of disconnects
                	**type**\: list of int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: entry
                
                	Array of disconnected subscribers
                	**type**\: list of  		 :py:class:`Entry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry>`
                
                	**config**\: False
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2019-10-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistoryUnique, ['disconnect_count'], name, value)


                class Entry(_Entity_):
                    """
                    Array of disconnected subscribers
                    
                    .. attribute:: session_idb
                    
                    	Session IDB
                    	**type**\:  :py:class:`SessionIdb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb>`
                    
                    	**config**\: False
                    
                    .. attribute:: timestamp
                    
                    	Time when disconnected
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: ifname
                    
                    	Interface name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: trigger
                    
                    	Disconnect Trigger
                    	**type**\:  :py:class:`PppoeMaSessionTrig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.PppoeMaSessionTrig>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2019-10-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry, ['timestamp', 'ifname', 'trigger'], name, value)


                    class SessionIdb(_Entity_):
                        """
                        Session IDB
                        
                        .. attribute:: tags
                        
                        	Tags
                        	**type**\:  :py:class:`Tags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.Tags>`
                        
                        	**config**\: False
                        
                        .. attribute:: vlan_outer_tag
                        
                        	VLAN Outer Tag
                        	**type**\:  :py:class:`VlanOuterTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.VlanOuterTag>`
                        
                        	**config**\: False
                        
                        .. attribute:: vlan_inner_tag
                        
                        	VLAN Inner Tag
                        	**type**\:  :py:class:`VlanInnerTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.VlanInnerTag>`
                        
                        	**config**\: False
                        
                        .. attribute:: interface
                        
                        	Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: access_interface
                        
                        	Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: session_id
                        
                        	Session ID
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: sub_label
                        
                        	Sub Label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: peer_mac_address
                        
                        	Peer Mac\-Address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        	**config**\: False
                        
                        .. attribute:: state
                        
                        	State
                        	**type**\:  :py:class:`PppoeMaSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.PppoeMaSessionState>`
                        
                        	**config**\: False
                        
                        .. attribute:: cdm_object_handle
                        
                        	CDM Object Handle
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: chkpt_id
                        
                        	Chkpt ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: punted_count
                        
                        	Punted Count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: port_limit
                        
                        	Port Limit
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: is_counted
                        
                        	Is BBA Counted
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_vlan_outer_tag
                        
                        	Is VLAN Outer Tag
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_vlan_inner_tag
                        
                        	Is VLAN Inner Tag
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_cleanup_pending
                        
                        	Is Cleanup Pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_disconnect_done_pending
                        
                        	Is Disconnect Done Pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_delete_done_pending
                        
                        	Is Delete Done Pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_intf_create_callback_pending
                        
                        	Is Interface Create Callback pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_publish_encaps_attr_pending
                        
                        	Is Publish Encaps Attr pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_publish_encaps_attr_cb_pending
                        
                        	Is Publish Encaps Attr Callback pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_intf_delete_callback_pending
                        
                        	Is Interface Delete Callback pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_intf_delete_pending
                        
                        	Is Interface Delete pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_im_owned_resource
                        
                        	Is IM Owned Resource
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_im_final_received
                        
                        	Is IM Final received
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_im_owned_resource_missing
                        
                        	Is IM Owned Resource missing
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_aaa_start_request_callback_pending
                        
                        	Is AAA Start request callback pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_aaa_owned_resource
                        
                        	Is AAA Owned Resource
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_aaa_disconnect_requested
                        
                        	Is AAA Disconnect Requested
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_aaa_disconnect_received
                        
                        	Is AAA Disconnect Received
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_sub_db_activate_callback_pending
                        
                        	Is SubDB Activate callback pending
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_pads_sent
                        
                        	Is PADS Sent
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_padt_received
                        
                        	Is PADT Received
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_in_flight
                        
                        	Is Session In Flight
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_radius_override
                        
                        	Is RADIUS override enabled
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: expected_notifications
                        
                        	Expected Notifications
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: received_notifications
                        
                        	Received Notifications
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: srg_state
                        
                        	SRG state
                        	**type**\:  :py:class:`PppoeMaSessionIdbSrgState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.PppoeMaSessionIdbSrgState>`
                        
                        	**config**\: False
                        
                        .. attribute:: is_srg_data_received
                        
                        	Is SRG Data Received
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: is_iedge_data_received
                        
                        	Is IEDGE Data Received
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2019-10-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb, ['interface', 'access_interface', 'session_id', 'sub_label', 'peer_mac_address', 'state', 'cdm_object_handle', 'chkpt_id', 'punted_count', 'port_limit', 'is_counted', 'is_vlan_outer_tag', 'is_vlan_inner_tag', 'is_cleanup_pending', 'is_disconnect_done_pending', 'is_delete_done_pending', 'is_intf_create_callback_pending', 'is_publish_encaps_attr_pending', 'is_publish_encaps_attr_cb_pending', 'is_intf_delete_callback_pending', 'is_intf_delete_pending', 'is_im_owned_resource', 'is_im_final_received', 'is_im_owned_resource_missing', 'is_aaa_start_request_callback_pending', 'is_aaa_owned_resource', 'is_aaa_disconnect_requested', 'is_aaa_disconnect_received', 'is_sub_db_activate_callback_pending', 'is_pads_sent', 'is_padt_received', 'is_in_flight', 'is_radius_override', 'expected_notifications', 'received_notifications', 'srg_state', 'is_srg_data_received', 'is_iedge_data_received'], name, value)


                        class Tags(_Entity_):
                            """
                            Tags
                            
                            .. attribute:: access_loop_encapsulation
                            
                            	Access Loop Encapsulation
                            	**type**\:  :py:class:`AccessLoopEncapsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.Tags.AccessLoopEncapsulation>`
                            
                            	**config**\: False
                            
                            .. attribute:: is_service_name
                            
                            	Is Service Name
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_max_payload
                            
                            	Is Max Payload
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_host_uniq
                            
                            	Is Host Uniq
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_relay_session_id
                            
                            	Is Relay Session ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_vendor_specific
                            
                            	Is Vendor Specific
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_iwf
                            
                            	Is IWF
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_remote_id
                            
                            	Is Remote ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_circuit_id
                            
                            	Is Circuit ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_tag
                            
                            	Is DSL Tag
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: service_name
                            
                            	Service Name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: max_payload
                            
                            	Max Payload
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: host_uniq
                            
                            	Host Uniq
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            	**config**\: False
                            
                            .. attribute:: relay_session_id
                            
                            	Relay Session ID
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            	**config**\: False
                            
                            .. attribute:: remote_id
                            
                            	Remote ID
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: circuit_id
                            
                            	Circuit ID
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_actual_up
                            
                            	Is DSL Actual Up
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_actual_down
                            
                            	Is DSL Actual Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_min_up
                            
                            	Is DSL Min Up
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_min_down
                            
                            	Is DSL Min Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_attain_up
                            
                            	Is DSL Attain Up
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_attain_down
                            
                            	Is DSL Attain Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_max_up
                            
                            	Is DSL Max Up
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_max_down
                            
                            	Is DSL Max Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_min_up_low
                            
                            	Is DSL Min Up Low
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_min_down_low
                            
                            	Is DSL Min Down Low
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_max_delay_up
                            
                            	Is DSL Max Delay Up
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_actual_delay_up
                            
                            	Is DSL Actual Delay Up
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_max_delay_down
                            
                            	Is DSL Max Delay Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_dsl_actual_delay_down
                            
                            	Is DSL Actual Delay Down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_access_loop_encapsulation
                            
                            	Is Access Loop Encapsulation
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_actual_up
                            
                            	DSL Actual Up
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_actual_down
                            
                            	DSL Actual Down
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_min_up
                            
                            	DSL Min Up
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_min_down
                            
                            	DSL Min Down
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_attain_up
                            
                            	DSL Attain Up
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_attain_down
                            
                            	DSL Attain Down
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_max_up
                            
                            	DSL Max Up
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_max_down
                            
                            	DSL Max Down
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_min_up_low
                            
                            	DSL Min Up Low
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_min_down_low
                            
                            	DSL Min Down Low
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_max_delay_up
                            
                            	DSL Max Delay Up
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_actual_delay_up
                            
                            	DSL Actual Delay Up
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_max_delay_down
                            
                            	DSL Max Delay Down
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: dsl_actual_delay_down
                            
                            	DSL Actual Delay Down
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.Tags, ['is_service_name', 'is_max_payload', 'is_host_uniq', 'is_relay_session_id', 'is_vendor_specific', 'is_iwf', 'is_remote_id', 'is_circuit_id', 'is_dsl_tag', 'service_name', 'max_payload', 'host_uniq', 'relay_session_id', 'remote_id', 'circuit_id', 'is_dsl_actual_up', 'is_dsl_actual_down', 'is_dsl_min_up', 'is_dsl_min_down', 'is_dsl_attain_up', 'is_dsl_attain_down', 'is_dsl_max_up', 'is_dsl_max_down', 'is_dsl_min_up_low', 'is_dsl_min_down_low', 'is_dsl_max_delay_up', 'is_dsl_actual_delay_up', 'is_dsl_max_delay_down', 'is_dsl_actual_delay_down', 'is_access_loop_encapsulation', 'dsl_actual_up', 'dsl_actual_down', 'dsl_min_up', 'dsl_min_down', 'dsl_attain_up', 'dsl_attain_down', 'dsl_max_up', 'dsl_max_down', 'dsl_min_up_low', 'dsl_min_down_low', 'dsl_max_delay_up', 'dsl_actual_delay_up', 'dsl_max_delay_down', 'dsl_actual_delay_down'], name, value)


                            class AccessLoopEncapsulation(_Entity_):
                                """
                                Access Loop Encapsulation
                                
                                .. attribute:: data_link
                                
                                	Data Link
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: encaps1
                                
                                	Encaps 1
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: encaps2
                                
                                	Encaps 2
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'subscriber-pppoe-ma-oper'
                                _revision = '2019-10-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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
                                    self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.Tags.AccessLoopEncapsulation, ['data_link', 'encaps1', 'encaps2'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                    return meta._meta_table['Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.Tags.AccessLoopEncapsulation']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.Tags']['meta_info']


                        class VlanOuterTag(_Entity_):
                            """
                            VLAN Outer Tag
                            
                            .. attribute:: ether_type
                            
                            	Ethertype. See IEEE 802.1Q for more information
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            .. attribute:: user_priority
                            
                            	User Priority
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: cfi
                            
                            	CFI
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: vlan_id
                            
                            	VLAN ID
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.VlanOuterTag, ['ether_type', 'user_priority', 'cfi', 'vlan_id'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.VlanOuterTag']['meta_info']


                        class VlanInnerTag(_Entity_):
                            """
                            VLAN Inner Tag
                            
                            .. attribute:: ether_type
                            
                            	Ethertype. See IEEE 802.1Q for more information
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            .. attribute:: user_priority
                            
                            	User Priority
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: cfi
                            
                            	CFI
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: vlan_id
                            
                            	VLAN ID
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.VlanInnerTag, ['ether_type', 'user_priority', 'cfi', 'vlan_id'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb.VlanInnerTag']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry.SessionIdb']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.Nodes.Node.DisconnectHistoryUnique.Entry']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                    return meta._meta_table['Pppoe.Nodes.Node.DisconnectHistoryUnique']['meta_info']


            class Statistics(_Entity_):
                """
                PPPoE statistics for a given node
                
                .. attribute:: packet_counts
                
                	Packet Counts
                	**type**\:  :py:class:`PacketCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts>`
                
                	**config**\: False
                
                .. attribute:: packet_error_counts
                
                	Packet Error Counts
                	**type**\:  :py:class:`PacketErrorCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketErrorCounts>`
                
                	**config**\: False
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2019-10-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class PacketCounts(_Entity_):
                    """
                    Packet Counts
                    
                    .. attribute:: padi
                    
                    	PADI counts
                    	**type**\:  :py:class:`Padi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.Padi>`
                    
                    	**config**\: False
                    
                    .. attribute:: pado
                    
                    	PADO counts
                    	**type**\:  :py:class:`Pado <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.Pado>`
                    
                    	**config**\: False
                    
                    .. attribute:: padr
                    
                    	PADR counts
                    	**type**\:  :py:class:`Padr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.Padr>`
                    
                    	**config**\: False
                    
                    .. attribute:: pads_success
                    
                    	PADS Success counts
                    	**type**\:  :py:class:`PadsSuccess <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.PadsSuccess>`
                    
                    	**config**\: False
                    
                    .. attribute:: pads_error
                    
                    	PADS Error counts
                    	**type**\:  :py:class:`PadsError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.PadsError>`
                    
                    	**config**\: False
                    
                    .. attribute:: padt
                    
                    	PADT counts
                    	**type**\:  :py:class:`Padt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.Padt>`
                    
                    	**config**\: False
                    
                    .. attribute:: session_state
                    
                    	Session Stage counts
                    	**type**\:  :py:class:`SessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.SessionState>`
                    
                    	**config**\: False
                    
                    .. attribute:: other
                    
                    	Other counts
                    	**type**\:  :py:class:`Other <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.Other>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2019-10-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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


                    class Padi(_Entity_):
                        """
                        PADI counts
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2019-10-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketCounts.Padi, ['sent', 'received', 'dropped'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts.Padi']['meta_info']


                    class Pado(_Entity_):
                        """
                        PADO counts
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2019-10-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketCounts.Pado, ['sent', 'received', 'dropped'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts.Pado']['meta_info']


                    class Padr(_Entity_):
                        """
                        PADR counts
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2019-10-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketCounts.Padr, ['sent', 'received', 'dropped'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts.Padr']['meta_info']


                    class PadsSuccess(_Entity_):
                        """
                        PADS Success counts
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2019-10-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketCounts.PadsSuccess, ['sent', 'received', 'dropped'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts.PadsSuccess']['meta_info']


                    class PadsError(_Entity_):
                        """
                        PADS Error counts
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2019-10-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketCounts.PadsError, ['sent', 'received', 'dropped'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts.PadsError']['meta_info']


                    class Padt(_Entity_):
                        """
                        PADT counts
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2019-10-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketCounts.Padt, ['sent', 'received', 'dropped'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts.Padt']['meta_info']


                    class SessionState(_Entity_):
                        """
                        Session Stage counts
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2019-10-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketCounts.SessionState, ['sent', 'received', 'dropped'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts.SessionState']['meta_info']


                    class Other(_Entity_):
                        """
                        Other counts
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2019-10-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketCounts.Other, ['sent', 'received', 'dropped'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts.Other']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts']['meta_info']


                class PacketErrorCounts(_Entity_):
                    """
                    Packet Error Counts
                    
                    .. attribute:: no_interface_handle
                    
                    	No interface handle
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: no_packet_payload
                    
                    	No packet payload
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: no_packet_mac_address
                    
                    	No packet mac\-address
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: invalid_version_type_value
                    
                    	Invalid version\-type value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: bad_packet_length
                    
                    	Bad packet length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: unknown_interface
                    
                    	Unknown interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: pado_received
                    
                    	PADO received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: pads_received
                    
                    	PADS received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: unknown_packet_type_received
                    
                    	Unknown packet type received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: unexpected_session_id_in_packet
                    
                    	Unexpected Session\-ID in packet
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: no_service_name_tag
                    
                    	No Service\-Name Tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: padt_for_unknown_session
                    
                    	PADT for unknown session
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: padt_with_wrong_peer_mac
                    
                    	PADT with wrong peer\-mac
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: padt_with_wrong_vlan_tags
                    
                    	PADT with wrong VLAN tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: zero_length_host_uniq
                    
                    	Zero\-length Host\-Uniq tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: padt_before_pads_sent
                    
                    	PADT before PADS sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: session_stage_packet_for_unknown_session
                    
                    	Session\-stage packet for unknown session
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: session_stage_packet_with_wrong_mac
                    
                    	Session\-stage packet with wrong mac
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: session_stage_packet_with_wrong_vlan_tags
                    
                    	Session\-stage packet with wrong VLAN tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: session_stage_packet_with_no_error
                    
                    	Session\-stage packet with no error
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: tag_too_short
                    
                    	Tag too short
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: bad_tag_length_field
                    
                    	Bad tag\-length field
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: multiple_service_name_tags
                    
                    	Multiple Service\-Name tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: multiple_max_payload_tags
                    
                    	Multiple Max\-Payload tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: invalid_max_payload_tag
                    
                    	Invalid Max\-Payload tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: multiple_vendor_specific_tags
                    
                    	Multiple Vendor\-specific tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: unexpected_ac_name_tag
                    
                    	Unexpected AC\-Name tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: unexpected_error_tags
                    
                    	Unexpected error tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: unknown_tag_received
                    
                    	Unknown tag received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: no_iana_code_invendor_tag
                    
                    	No IANA code in vendor tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: invalid_iana_code_invendor_tag
                    
                    	Invalid IANA code in vendor tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: vendor_tag_too_short
                    
                    	Vendor tag too short
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: bad_vendor_tag_length_field
                    
                    	Bad vendor tag length field
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: multiple_host_uniq_tags
                    
                    	Multiple Host\-Uniq tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: multiple_relay_session_id_tags
                    
                    	Multiple relay\-session\-id tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: multiple_circuit_id_tags
                    
                    	Multiple Circuit\-ID tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: multiple_remote_id_tags
                    
                    	Multiple Remote\-ID tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: invalid_dsl_tag
                    
                    	Invalid DSL tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: multiple_of_the_same_dsl_tag
                    
                    	Multiple of the same DSL tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: invalid_iwf_tag
                    
                    	Invalid IWF tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: multiple_iwf_tags
                    
                    	Multiple IWF tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: unknownvendor_tag
                    
                    	Unknown vendor\-tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: no_space_left_in_packet
                    
                    	No space left in packet
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: duplicate_host_uniq_tag_received
                    
                    	Duplicate Host\-Uniq tag received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: duplicate_relay_session_id_tag_received
                    
                    	Duplicate Relay Session ID tag received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: packet_too_long
                    
                    	Packet too long
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: invalid_ale_tag
                    
                    	Invalid ALE tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: multiple_ale_tags
                    
                    	Multiple ALE tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: invalid_service_name
                    
                    	Invalid Service Name
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: invalid_peer_mac
                    
                    	Invalid Peer MAC
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: invalid_vlan_tags
                    
                    	Invalid VLAN Tags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: packet_on_srg_slave
                    
                    	Packet Received on SRG Slave
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2019-10-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(Pppoe.Nodes.Node.Statistics.PacketErrorCounts, ['no_interface_handle', 'no_packet_payload', 'no_packet_mac_address', 'invalid_version_type_value', 'bad_packet_length', 'unknown_interface', 'pado_received', 'pads_received', 'unknown_packet_type_received', 'unexpected_session_id_in_packet', 'no_service_name_tag', 'padt_for_unknown_session', 'padt_with_wrong_peer_mac', 'padt_with_wrong_vlan_tags', 'zero_length_host_uniq', 'padt_before_pads_sent', 'session_stage_packet_for_unknown_session', 'session_stage_packet_with_wrong_mac', 'session_stage_packet_with_wrong_vlan_tags', 'session_stage_packet_with_no_error', 'tag_too_short', 'bad_tag_length_field', 'multiple_service_name_tags', 'multiple_max_payload_tags', 'invalid_max_payload_tag', 'multiple_vendor_specific_tags', 'unexpected_ac_name_tag', 'unexpected_error_tags', 'unknown_tag_received', 'no_iana_code_invendor_tag', 'invalid_iana_code_invendor_tag', 'vendor_tag_too_short', 'bad_vendor_tag_length_field', 'multiple_host_uniq_tags', 'multiple_relay_session_id_tags', 'multiple_circuit_id_tags', 'multiple_remote_id_tags', 'invalid_dsl_tag', 'multiple_of_the_same_dsl_tag', 'invalid_iwf_tag', 'multiple_iwf_tags', 'unknownvendor_tag', 'no_space_left_in_packet', 'duplicate_host_uniq_tag_received', 'duplicate_relay_session_id_tag_received', 'packet_too_long', 'invalid_ale_tag', 'multiple_ale_tags', 'invalid_service_name', 'invalid_peer_mac', 'invalid_vlan_tags', 'packet_on_srg_slave'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.Nodes.Node.Statistics.PacketErrorCounts']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                    return meta._meta_table['Pppoe.Nodes.Node.Statistics']['meta_info']


            class AccessInterface(_Entity_):
                """
                PPPoE access interface information
                
                .. attribute:: summaries
                
                	PPPoE access interface summary information
                	**type**\:  :py:class:`Summaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.AccessInterface.Summaries>`
                
                	**config**\: False
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2019-10-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class Summaries(_Entity_):
                    """
                    PPPoE access interface summary information
                    
                    .. attribute:: summary
                    
                    	Summary information for a PPPoE\-enabled access interface
                    	**type**\: list of  		 :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.AccessInterface.Summaries.Summary>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2019-10-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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


                    class Summary(_Entity_):
                        """
                        Summary information for a PPPoE\-enabled
                        access interface
                        
                        .. attribute:: interface_name  (key)
                        
                        	PPPoE Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: interface_name_xr
                        
                        	Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: interface_state
                        
                        	Interface State
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: mac_address
                        
                        	Mac Address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        	**config**\: False
                        
                        .. attribute:: bba_group_name
                        
                        	BBA Group
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: is_ready
                        
                        	Is Ready
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: sessions
                        
                        	Session Count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: incomplete_sessions
                        
                        	Incomplete Session Count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2019-10-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(Pppoe.Nodes.Node.AccessInterface.Summaries.Summary, ['interface_name', 'interface_name_xr', 'interface_state', 'mac_address', 'bba_group_name', 'is_ready', 'sessions', 'incomplete_sessions'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.AccessInterface.Summaries.Summary']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.Nodes.Node.AccessInterface.Summaries']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                    return meta._meta_table['Pppoe.Nodes.Node.AccessInterface']['meta_info']


            class Interfaces(_Entity_):
                """
                Per interface PPPoE operational data
                
                .. attribute:: interface
                
                	Data for a PPPoE interface
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Interfaces.Interface>`
                
                	**config**\: False
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2019-10-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class Interface(_Entity_):
                    """
                    Data for a PPPoE interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	PPPoE Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: tags
                    
                    	Tags
                    	**type**\:  :py:class:`Tags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Interfaces.Interface.Tags>`
                    
                    	**config**\: False
                    
                    .. attribute:: interface_name_xr
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: access_interface_name
                    
                    	Access Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: bba_group_name
                    
                    	BBA Group
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: local_mac_address
                    
                    	Local Mac\-Address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    	**config**\: False
                    
                    .. attribute:: peer_mac_address
                    
                    	Peer Mac\-Address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    	**config**\: False
                    
                    .. attribute:: is_complete
                    
                    	Is Complete
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: vlan_outer_id
                    
                    	VLAN Outer ID
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: vlan_inner_id
                    
                    	VLAN Inner ID
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: srg_state
                    
                    	SRG state
                    	**type**\:  :py:class:`PppoeMaSessionIdbSrgState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.PppoeMaSessionIdbSrgState>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2019-10-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(Pppoe.Nodes.Node.Interfaces.Interface, ['interface_name', 'interface_name_xr', 'access_interface_name', 'bba_group_name', 'session_id', 'local_mac_address', 'peer_mac_address', 'is_complete', 'vlan_outer_id', 'vlan_inner_id', 'srg_state'], name, value)


                    class Tags(_Entity_):
                        """
                        Tags
                        
                        .. attribute:: access_loop_encapsulation
                        
                        	Access Loop Encapsulation
                        	**type**\:  :py:class:`AccessLoopEncapsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Interfaces.Interface.Tags.AccessLoopEncapsulation>`
                        
                        	**config**\: False
                        
                        .. attribute:: service_name
                        
                        	Service Name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: max_payload
                        
                        	Max Payload
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: host_uniq
                        
                        	Host Uniq
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        	**config**\: False
                        
                        .. attribute:: relay_session_id
                        
                        	Relay Session ID
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        	**config**\: False
                        
                        .. attribute:: remote_id
                        
                        	Remote ID
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: circuit_id
                        
                        	Circuit ID
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: is_iwf
                        
                        	Is IWF
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: dsl_actual_up
                        
                        	DSL Actual Up
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: dsl_actual_down
                        
                        	DSL Actual Down
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: dsl_min_up
                        
                        	DSL Min Up
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: dsl_min_down
                        
                        	DSL Min Down
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: dsl_attain_up
                        
                        	DSL Attain Up
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: dsl_attain_down
                        
                        	DSL Attain Down
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: dsl_max_up
                        
                        	DSL Max Up
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: dsl_max_down
                        
                        	DSL Max Down
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: dsl_min_up_low
                        
                        	DSL Min Up Low
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: dsl_min_down_low
                        
                        	DSL Min Down Low
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: dsl_max_delay_up
                        
                        	DSL Max Delay Up
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: dsl_actual_delay_up
                        
                        	DSL Actual Delay Up
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: dsl_max_delay_down
                        
                        	DSL Max Delay Down
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: dsl_actual_delay_down
                        
                        	DSL Actual Delay Down
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2019-10-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(Pppoe.Nodes.Node.Interfaces.Interface.Tags, ['service_name', 'max_payload', 'host_uniq', 'relay_session_id', 'remote_id', 'circuit_id', 'is_iwf', 'dsl_actual_up', 'dsl_actual_down', 'dsl_min_up', 'dsl_min_down', 'dsl_attain_up', 'dsl_attain_down', 'dsl_max_up', 'dsl_max_down', 'dsl_min_up_low', 'dsl_min_down_low', 'dsl_max_delay_up', 'dsl_actual_delay_up', 'dsl_max_delay_down', 'dsl_actual_delay_down'], name, value)


                        class AccessLoopEncapsulation(_Entity_):
                            """
                            Access Loop Encapsulation
                            
                            .. attribute:: data_link
                            
                            	Data Link
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: encaps1
                            
                            	Encaps 1
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: encaps2
                            
                            	Encaps 2
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.Interfaces.Interface.Tags.AccessLoopEncapsulation, ['data_link', 'encaps1', 'encaps2'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.Interfaces.Interface.Tags.AccessLoopEncapsulation']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.Interfaces.Interface.Tags']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.Nodes.Node.Interfaces.Interface']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                    return meta._meta_table['Pppoe.Nodes.Node.Interfaces']['meta_info']


            class BbaGroups(_Entity_):
                """
                PPPoE BBA\-Group information
                
                .. attribute:: bba_group
                
                	PPPoE BBA\-Group information
                	**type**\: list of  		 :py:class:`BbaGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup>`
                
                	**config**\: False
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2019-10-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class BbaGroup(_Entity_):
                    """
                    PPPoE BBA\-Group information
                    
                    .. attribute:: bba_group_name  (key)
                    
                    	BBA Group
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: limit_config
                    
                    	BBA\-Group limit configuration information
                    	**type**\:  :py:class:`LimitConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig>`
                    
                    	**config**\: False
                    
                    .. attribute:: limits
                    
                    	PPPoE session limit information
                    	**type**\:  :py:class:`Limits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits>`
                    
                    	**config**\: False
                    
                    .. attribute:: throttles
                    
                    	PPPoE throttle information
                    	**type**\:  :py:class:`Throttles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles>`
                    
                    	**config**\: False
                    
                    .. attribute:: throttle_config
                    
                    	BBA\-Group throttle configuration information
                    	**type**\:  :py:class:`ThrottleConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2019-10-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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


                    class LimitConfig(_Entity_):
                        """
                        BBA\-Group limit configuration information
                        
                        .. attribute:: card
                        
                        	Card
                        	**type**\:  :py:class:`Card <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Card>`
                        
                        	**config**\: False
                        
                        .. attribute:: access_intf
                        
                        	Access Interface
                        	**type**\:  :py:class:`AccessIntf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.AccessIntf>`
                        
                        	**config**\: False
                        
                        .. attribute:: mac
                        
                        	MAC
                        	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Mac>`
                        
                        	**config**\: False
                        
                        .. attribute:: mac_iwf
                        
                        	MAC IWF
                        	**type**\:  :py:class:`MacIwf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwf>`
                        
                        	**config**\: False
                        
                        .. attribute:: mac_access_interface
                        
                        	MAC Access Interface
                        	**type**\:  :py:class:`MacAccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacAccessInterface>`
                        
                        	**config**\: False
                        
                        .. attribute:: mac_iwf_access_interface
                        
                        	MAC IWF Access Interface
                        	**type**\:  :py:class:`MacIwfAccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwfAccessInterface>`
                        
                        	**config**\: False
                        
                        .. attribute:: circuit_id
                        
                        	Circuit ID
                        	**type**\:  :py:class:`CircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitId>`
                        
                        	**config**\: False
                        
                        .. attribute:: remote_id
                        
                        	Remote ID
                        	**type**\:  :py:class:`RemoteId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.RemoteId>`
                        
                        	**config**\: False
                        
                        .. attribute:: circuit_id_and_remote_id
                        
                        	Circuit ID and Remote ID
                        	**type**\:  :py:class:`CircuitIdAndRemoteId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitIdAndRemoteId>`
                        
                        	**config**\: False
                        
                        .. attribute:: outer_vlan_id
                        
                        	Outer VLAN ID
                        	**type**\:  :py:class:`OuterVlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.OuterVlanId>`
                        
                        	**config**\: False
                        
                        .. attribute:: inner_vlan_id
                        
                        	Inner VLAN ID
                        	**type**\:  :py:class:`InnerVlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.InnerVlanId>`
                        
                        	**config**\: False
                        
                        .. attribute:: vlan_id
                        
                        	VLAN ID
                        	**type**\:  :py:class:`VlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.VlanId>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2019-10-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class Card(_Entity_):
                            """
                            Card
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Card, ['max_limit', 'threshold', 'radius_override_enabled'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Card']['meta_info']


                        class AccessIntf(_Entity_):
                            """
                            Access Interface
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.AccessIntf, ['max_limit', 'threshold', 'radius_override_enabled'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.AccessIntf']['meta_info']


                        class Mac(_Entity_):
                            """
                            MAC
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Mac, ['max_limit', 'threshold', 'radius_override_enabled'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Mac']['meta_info']


                        class MacIwf(_Entity_):
                            """
                            MAC IWF
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwf, ['max_limit', 'threshold', 'radius_override_enabled'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwf']['meta_info']


                        class MacAccessInterface(_Entity_):
                            """
                            MAC Access Interface
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacAccessInterface, ['max_limit', 'threshold', 'radius_override_enabled'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacAccessInterface']['meta_info']


                        class MacIwfAccessInterface(_Entity_):
                            """
                            MAC IWF Access Interface
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwfAccessInterface, ['max_limit', 'threshold', 'radius_override_enabled'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwfAccessInterface']['meta_info']


                        class CircuitId(_Entity_):
                            """
                            Circuit ID
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitId, ['max_limit', 'threshold', 'radius_override_enabled'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitId']['meta_info']


                        class RemoteId(_Entity_):
                            """
                            Remote ID
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.RemoteId, ['max_limit', 'threshold', 'radius_override_enabled'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.RemoteId']['meta_info']


                        class CircuitIdAndRemoteId(_Entity_):
                            """
                            Circuit ID and Remote ID
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitIdAndRemoteId, ['max_limit', 'threshold', 'radius_override_enabled'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitIdAndRemoteId']['meta_info']


                        class OuterVlanId(_Entity_):
                            """
                            Outer VLAN ID
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.OuterVlanId, ['max_limit', 'threshold', 'radius_override_enabled'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.OuterVlanId']['meta_info']


                        class InnerVlanId(_Entity_):
                            """
                            Inner VLAN ID
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.InnerVlanId, ['max_limit', 'threshold', 'radius_override_enabled'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.InnerVlanId']['meta_info']


                        class VlanId(_Entity_):
                            """
                            VLAN ID
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.VlanId, ['max_limit', 'threshold', 'radius_override_enabled'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.VlanId']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig']['meta_info']


                    class Limits(_Entity_):
                        """
                        PPPoE session limit information
                        
                        .. attribute:: limit
                        
                        	PPPoE session limit state
                        	**type**\: list of  		 :py:class:`Limit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits.Limit>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2019-10-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class Limit(_Entity_):
                            """
                            PPPoE session limit state
                            
                            .. attribute:: interface_name
                            
                            	Access Interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            	**config**\: False
                            
                            .. attribute:: iwf
                            
                            	IWF flag
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: circuit_id
                            
                            	Circuit ID
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            	**config**\: False
                            
                            .. attribute:: remote_id
                            
                            	Remote ID
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            	**config**\: False
                            
                            .. attribute:: outer_vlan_id
                            
                            	Outer VLAN ID
                            	**type**\: int
                            
                            	**range:** 0..4095
                            
                            	**config**\: False
                            
                            .. attribute:: inner_vlan_id
                            
                            	Inner VLAN ID
                            	**type**\: int
                            
                            	**range:** 0..4095
                            
                            	**config**\: False
                            
                            .. attribute:: state
                            
                            	State
                            	**type**\:  :py:class:`PppoeMaLimitState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.PppoeMaLimitState>`
                            
                            	**config**\: False
                            
                            .. attribute:: session_count
                            
                            	Session Count
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: radius_override_set
                            
                            	Overridden limit has been set
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: override_limit
                            
                            	Overridden limit if set
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits.Limit, ['interface_name', 'mac_address', 'iwf', 'circuit_id', 'remote_id', 'outer_vlan_id', 'inner_vlan_id', 'state', 'session_count', 'radius_override_set', 'override_limit'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits.Limit']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits']['meta_info']


                    class Throttles(_Entity_):
                        """
                        PPPoE throttle information
                        
                        .. attribute:: throttle
                        
                        	PPPoE session throttle state
                        	**type**\: list of  		 :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles.Throttle>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2019-10-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class Throttle(_Entity_):
                            """
                            PPPoE session throttle state
                            
                            .. attribute:: interface_name
                            
                            	Access Interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            	**config**\: False
                            
                            .. attribute:: iwf
                            
                            	IWF flag
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: circuit_id
                            
                            	Circuit ID
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            	**config**\: False
                            
                            .. attribute:: remote_id
                            
                            	Remote ID
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            	**config**\: False
                            
                            .. attribute:: outer_vlan_id
                            
                            	Outer VLAN ID
                            	**type**\: int
                            
                            	**range:** 0..4095
                            
                            	**config**\: False
                            
                            .. attribute:: inner_vlan_id
                            
                            	Inner VLAN ID
                            	**type**\: int
                            
                            	**range:** 0..4095
                            
                            	**config**\: False
                            
                            .. attribute:: state
                            
                            	State
                            	**type**\:  :py:class:`PppoeMaThrottleState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.PppoeMaThrottleState>`
                            
                            	**config**\: False
                            
                            .. attribute:: time_left
                            
                            	Time left in seconds
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            	**units**\: second
                            
                            .. attribute:: since_reset
                            
                            	Number of seconds since counters reset
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            	**units**\: second
                            
                            .. attribute:: padi_count
                            
                            	PADI Count
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: padr_count
                            
                            	PADR Count
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles.Throttle, ['interface_name', 'mac_address', 'iwf', 'circuit_id', 'remote_id', 'outer_vlan_id', 'inner_vlan_id', 'state', 'time_left', 'since_reset', 'padi_count', 'padr_count'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles.Throttle']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles']['meta_info']


                    class ThrottleConfig(_Entity_):
                        """
                        BBA\-Group throttle configuration information
                        
                        .. attribute:: mac
                        
                        	MAC
                        	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.Mac>`
                        
                        	**config**\: False
                        
                        .. attribute:: mac_access_interface
                        
                        	MAC Access Interface
                        	**type**\:  :py:class:`MacAccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacAccessInterface>`
                        
                        	**config**\: False
                        
                        .. attribute:: mac_iwf_access_interface
                        
                        	MAC IWF Access Interface
                        	**type**\:  :py:class:`MacIwfAccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacIwfAccessInterface>`
                        
                        	**config**\: False
                        
                        .. attribute:: circuit_id
                        
                        	Circuit ID
                        	**type**\:  :py:class:`CircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitId>`
                        
                        	**config**\: False
                        
                        .. attribute:: remote_id
                        
                        	Remote ID
                        	**type**\:  :py:class:`RemoteId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.RemoteId>`
                        
                        	**config**\: False
                        
                        .. attribute:: circuit_id_and_remote_id
                        
                        	Circuit ID and Remote ID
                        	**type**\:  :py:class:`CircuitIdAndRemoteId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitIdAndRemoteId>`
                        
                        	**config**\: False
                        
                        .. attribute:: outer_vlan_id
                        
                        	Outer VLAN ID
                        	**type**\:  :py:class:`OuterVlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.OuterVlanId>`
                        
                        	**config**\: False
                        
                        .. attribute:: inner_vlan_id
                        
                        	Inner VLAN ID
                        	**type**\:  :py:class:`InnerVlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.InnerVlanId>`
                        
                        	**config**\: False
                        
                        .. attribute:: vlan_id
                        
                        	VLAN ID
                        	**type**\:  :py:class:`VlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.VlanId>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2019-10-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class Mac(_Entity_):
                            """
                            MAC
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.Mac, ['limit', 'request_period', 'blocking_period'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.Mac']['meta_info']


                        class MacAccessInterface(_Entity_):
                            """
                            MAC Access Interface
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacAccessInterface, ['limit', 'request_period', 'blocking_period'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacAccessInterface']['meta_info']


                        class MacIwfAccessInterface(_Entity_):
                            """
                            MAC IWF Access Interface
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacIwfAccessInterface, ['limit', 'request_period', 'blocking_period'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacIwfAccessInterface']['meta_info']


                        class CircuitId(_Entity_):
                            """
                            Circuit ID
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitId, ['limit', 'request_period', 'blocking_period'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitId']['meta_info']


                        class RemoteId(_Entity_):
                            """
                            Remote ID
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.RemoteId, ['limit', 'request_period', 'blocking_period'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.RemoteId']['meta_info']


                        class CircuitIdAndRemoteId(_Entity_):
                            """
                            Circuit ID and Remote ID
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitIdAndRemoteId, ['limit', 'request_period', 'blocking_period'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitIdAndRemoteId']['meta_info']


                        class OuterVlanId(_Entity_):
                            """
                            Outer VLAN ID
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.OuterVlanId, ['limit', 'request_period', 'blocking_period'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.OuterVlanId']['meta_info']


                        class InnerVlanId(_Entity_):
                            """
                            Inner VLAN ID
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.InnerVlanId, ['limit', 'request_period', 'blocking_period'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.InnerVlanId']['meta_info']


                        class VlanId(_Entity_):
                            """
                            VLAN ID
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2019-10-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.VlanId, ['limit', 'request_period', 'blocking_period'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.VlanId']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                    return meta._meta_table['Pppoe.Nodes.Node.BbaGroups']['meta_info']


            class SummaryTotal(_Entity_):
                """
                PPPoE statistics for a given node
                
                .. attribute:: ready_access_interfaces
                
                	Ready Access Interface Count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: not_ready_access_interfaces
                
                	Not Ready Access Interface Count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: complete_sessions
                
                	Complete Session Count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: incomplete_sessions
                
                	Incomplete Session Count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: flow_control_limit
                
                	Flow Control credit limit
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: flow_control_in_flight_sessions
                
                	Flow Control In\-Flight Count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: flow_control_dropped_sessions
                
                	Flow Control Drop Count
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: flow_control_disconnected_sessions
                
                	Flow Control Disconnected Count
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: flow_control_successful_sessions
                
                	Flow Control Success Count, sessions completing call flow
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pppoema_subscriber_infra_flow_control
                
                	PPPoEMASubscriberInfraFlowControl
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2019-10-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(Pppoe.Nodes.Node.SummaryTotal, ['ready_access_interfaces', 'not_ready_access_interfaces', 'complete_sessions', 'incomplete_sessions', 'flow_control_limit', 'flow_control_in_flight_sessions', 'flow_control_dropped_sessions', 'flow_control_disconnected_sessions', 'flow_control_successful_sessions', 'pppoema_subscriber_infra_flow_control'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                    return meta._meta_table['Pppoe.Nodes.Node.SummaryTotal']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                return meta._meta_table['Pppoe.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
            return meta._meta_table['Pppoe.Nodes']['meta_info']

    def clone_ptr(self):
        self._top_entity = Pppoe()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
        return meta._meta_table['Pppoe']['meta_info']


